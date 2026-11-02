from __future__ import annotations

import asyncio
import json
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch
from playwright.async_api import TimeoutError as PWTimeout

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "collectors"))
import pocketgamer


def item():
    return pocketgamer.NewsItem("story", "https://www.pocketgamer.biz/story/", "Story", "", [],
                               "<p>Discovery excerpt.</p>", "", datetime(2026, 10, 26), "")


def test_challenge_is_never_saved_as_full_article() -> None:
    page = SimpleNamespace(goto=AsyncMock(return_value=SimpleNamespace(status=403)),
                           title=AsyncMock(return_value="Just a moment..."),
                           url=item().url, close=AsyncMock(),
                           wait_for_selector=AsyncMock(side_effect=PWTimeout("verification remains blocked")))
    context = SimpleNamespace(new_page=AsyncMock(return_value=page))
    try:
        asyncio.run(pocketgamer.fetch_article_content(context, item()))
    except RuntimeError as exc:
        assert "blocked" in str(exc)
    else:
        raise AssertionError("verification page must not be accepted as an article")
    page.close.assert_awaited_once()


def test_page_for_another_article_is_rejected() -> None:
    page = SimpleNamespace(goto=AsyncMock(return_value=SimpleNamespace(status=200)),
                           title=AsyncMock(return_value="Other story"), url=item().url,
                           wait_for_selector=AsyncMock(), close=AsyncMock(),
                           evaluate=AsyncMock(return_value=dict(canonical="https://www.pocketgamer.biz/other/", content_html="<p>Other body</p>")))
    try:
        asyncio.run(pocketgamer.fetch_article_content(SimpleNamespace(new_page=AsyncMock(return_value=page)), item()))
    except RuntimeError as exc:
        assert "canonical" in str(exc)
    else:
        raise AssertionError("another article must not be saved under this URL")


def test_verified_article_keeps_original_url_and_full_body() -> None:
    body = "<p>First complete article paragraph.</p><p>Second complete article paragraph.</p>"
    page = SimpleNamespace(goto=AsyncMock(return_value=SimpleNamespace(status=200)),
                           title=AsyncMock(return_value="Story"), url=item().url,
                           wait_for_selector=AsyncMock(), close=AsyncMock(),
                           evaluate=AsyncMock(return_value=dict(title="Story", strap="Summary", author="Author", content_html=body)))
    result = asyncio.run(pocketgamer.fetch_article_content(SimpleNamespace(new_page=AsyncMock(return_value=page)), item()))
    assert result.url == item().url and body in result.content_html
    assert result.author == "Author"
    page.close.assert_awaited_once()


def test_existing_full_record_is_not_downgraded_on_later_run() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        original = dict(id="story", url=item().url, title=item().title,
                        body_status="full", text="Previously retrieved complete article.")
        data = out / "articles.jsonl"
        data.write_text(json.dumps(original), encoding="utf-8")
        context = SimpleNamespace(new_page=AsyncMock(side_effect=AssertionError("cached full text should be reused")))
        with patch.object(pocketgamer, "save_pdf_enabled", return_value=False):
            result = asyncio.run(pocketgamer.save_article_pdf(context, item(), out, {"items": {"story": {"body_status": "full"}}}))
        assert result.saved and result.body_status == "full"
        assert json.loads(data.read_text(encoding="utf-8")) == original
