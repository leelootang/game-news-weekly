from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "collectors"))
import gamespot


def full_body() -> str:
    return "".join(f"<p>Paragraph {i}. " + "The developer describes the production and release decisions. " * 6 + "</p>" for i in range(4))


def feed(description: str, content: str = "") -> str:
    return f'''<rss xmlns:content="http://purl.org/rss/1.0/modules/content/"><channel><item>
    <title>News</title><link>https://www.gamespot.com/articles/example/</link>
    <pubDate>Mon, 26 Oct 2026 12:00:00 +0000</pubDate>
    <description><![CDATA[{description}]]></description>
    {f'<content:encoded><![CDATA[{content}]]></content:encoded>' if content else ''}
    </item></channel></rss>'''


def test_full_description_is_not_mislabeled_as_snippet() -> None:
    entry = gamespot.parse_feed(feed(full_body()))[0]
    assert entry["body_status"] == "full"
    assert entry["content_origin"] == "description"
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "industry_news" / "2026-10-26"
        assert gamespot.write_feed_record(out, {"items": {}}, entry) == "full"
        record = json.loads((out / "articles.jsonl").read_text(encoding="utf-8"))
        assert record["body_status"] == "full" and record["fetch_status"] == "ok"
        assert record["fallback"] == "none"
        assert record["extra"]["content_origin"] == "description"


def test_long_truncated_body_is_still_partial() -> None:
    body = full_body() + '<p>... [<a href="https://www.gamespot.com/articles/example/">MORE</a>]</p>'
    assert gamespot.classify_feed_body(body) == "snippet"


def test_short_and_empty_feed_records_are_not_full() -> None:
    assert gamespot.classify_feed_body("<p>A brief discovery summary.</p>") == "snippet"
    assert gamespot.classify_feed_body("") == "empty"


def test_content_encoded_precedes_description_but_still_needs_validation() -> None:
    entry = gamespot.parse_feed(feed("Brief summary", full_body()))[0]
    assert entry["body_status"] == "full" and entry["content_origin"] == "content:encoded"
    entry = gamespot.parse_feed(feed(full_body(), "<p>Read the full article</p>"))[0]
    assert entry["body_status"] == "snippet"


def test_long_plain_excerpt_without_article_structure_is_not_full() -> None:
    assert gamespot.classify_feed_body("summary " * 200) == "snippet"
