from __future__ import annotations

import asyncio
import errno
import json
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch


COLLECTORS_DIR = Path(__file__).resolve().parents[1] / "collectors"
if str(COLLECTORS_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTORS_DIR))

import article_store
import pocketgamer
import youxiputao_sohu
from playwright.async_api import TimeoutError as PWTimeout


def pocketgamer_feed_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <item>
    <title>Window story</title>
    <link>https://www.pocketgamer.biz/window-story/</link>
    <pubDate>Mon, 10 Aug 2026 15:15:00 +0100</pubDate>
    <description><![CDATA[<p>A usable source summary.</p>]]></description>
    <category>News</category>
  </item>
  <item>
    <title>Older story</title>
    <link>https://www.pocketgamer.biz/older-story/</link>
    <pubDate>Sun, 09 Aug 2026 10:00:00 +0100</pubDate>
    <description><![CDATA[<p>Older summary.</p>]]></description>
  </item>
</channel></rss>"""


class CollectorResilienceTests(unittest.TestCase):
    def test_pocketgamer_prefers_working_canonical_feed(self) -> None:
        requested: list[str] = []

        def fake_fetch(url: str) -> str:
            requested.append(url)
            if url.endswith("/index.rss"):
                return pocketgamer_feed_xml()
            raise AssertionError("legacy endpoint should not be needed")

        with patch.object(pocketgamer, "fetch_text", side_effect=fake_fetch):
            items = pocketgamer.collect_feed_items(
                datetime(2026, 8, 10),
                datetime(2026, 8, 11),
                1,
            )

        self.assertEqual(["https://www.pocketgamer.biz/index.rss"], requested)
        self.assertEqual(["Window story"], [item.title for item in items])

    def test_pocketgamer_rss_fallback_is_auditable(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            out_dir = Path(temp_dir) / "industry_news" / "2026-08-10"
            item = pocketgamer.NewsItem(
                news_id="window_story",
                url="https://www.pocketgamer.biz/window-story/",
                title="Window story",
                author="",
                categories=["News"],
                description_html="<p>A usable source summary.</p>",
                image_url="",
                published_at=datetime(2026, 8, 10, 22, 15),
                raw_published_at="Mon, 10 Aug 2026 15:15:00 +0100",
            )
            manifest = {"items": {}}

            pocketgamer.write_text_record(
                out_dir,
                manifest,
                item,
                body_status="rss_summary",
                fallback="rss_summary",
                reason="HTTP 403",
            )

            record = json.loads((out_dir / "articles.jsonl").read_text(encoding="utf-8").strip())
            self.assertEqual("partial", record["fetch_status"])
            self.assertEqual("rss_summary", record["body_status"])
            self.assertEqual("rss_summary", record["fallback"])
            self.assertEqual("HTTP 403", record["extra"]["retrieval_error"])
            self.assertIn("A usable source summary", record["text"])

    def test_article_store_retries_windows_invalid_argument(self) -> None:
        attempts = 0

        def flaky_operation() -> str:
            nonlocal attempts
            attempts += 1
            if attempts < 3:
                exc = OSError(errno.EINVAL, "Invalid argument")
                exc.winerror = 87
                raise exc
            return "ok"

        self.assertEqual("ok", article_store._retry_io(flaky_operation))
        self.assertEqual(3, attempts)

    def test_article_store_atomic_write_leaves_complete_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            out_dir = Path(temp_dir) / "industry_news" / "2026-08-10"
            manifest = {"items": {}}
            article_store.write_article_record(
                out_dir,
                manifest,
                "sample",
                {
                    "source_key": "test",
                    "source": "example.com",
                    "title": "Sample",
                    "url": "https://example.com/sample",
                    "published_at": "2026-08-10T12:00:00",
                    "text": "Complete body",
                },
            )

            record = json.loads((out_dir / "articles.jsonl").read_text(encoding="utf-8"))
            self.assertEqual("sample", record["id"])
            self.assertTrue((out_dir / "articles_index.md").exists())
            self.assertFalse(list(out_dir.glob(".*.tmp")))


class FakeResponse:
    status = 200


class RetryPage:
    def __init__(self) -> None:
        self.attempts = 0
        self.url = "https://m.sohu.com/media/204824"

    async def goto(self, *_args, **_kwargs):
        self.attempts += 1
        return FakeResponse()

    async def wait_for_load_state(self, *_args, **_kwargs) -> None:
        return None

    async def wait_for_selector(self, *_args, **_kwargs) -> None:
        if self.attempts == 1:
            raise PWTimeout("transient empty page")

    async def wait_for_timeout(self, *_args, **_kwargs) -> None:
        return None

    async def evaluate(self, *_args, **_kwargs):
        return {"title": "temporary page", "url": self.url, "body_preview": ""}


class SohuResilienceTests(unittest.TestCase):
    def test_sohu_navigation_recovers_after_transient_empty_page(self) -> None:
        page = RetryPage()
        asyncio.run(
            youxiputao_sohu.open_with_retries(
                page,
                page.url,
                youxiputao_sohu.LIST_SELECTOR,
                "list",
            )
        )
        self.assertEqual(2, page.attempts)


if __name__ == "__main__":
    unittest.main()
