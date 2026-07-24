from __future__ import annotations

import sys
from pathlib import Path


COLLECTORS_DIR = Path(__file__).resolve().parents[1] / "collectors"
if str(COLLECTORS_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTORS_DIR))

import roblox_newsroom as collector


ARTICLE_URL = "https://about.roblox.com/newsroom/2026/07/test-post"
ARTICLE_HTML = """
<html><head>
<meta property="og:title" content="Test Post | Roblox">
<meta property="article:published_time" content="2026-07-16T12:00:00.000Z">
<meta property="article:author" content="Roblox Newsroom">
</head><body>
<section id="section-text-0"><div><p>It’s a complete first paragraph.</p></div></section>
<section id="section-image-1"><img alt="ignored"></section>
<section id="section-text-2"><div><h2>Details</h2><p>Second paragraph.</p></div></section>
<section id="related-news"><p>This must not be included.</p></section>
</body></html>
"""


def test_discover_article_urls_deduplicates_and_ignores_non_articles() -> None:
    catalog = """
    <a href="/newsroom/2026/07/test-post">one</a>
    <a href="/newsroom/2026/07/test-post">duplicate</a>
    <a href="/newsroom">catalog</a>
    """
    assert collector.discover_article_urls(catalog) == [ARTICLE_URL]


def test_parse_article_extracts_metadata_and_text_sections_only() -> None:
    article = collector.parse_article(ARTICLE_URL, ARTICLE_HTML)
    assert article is not None
    assert article["title"] == "Test Post"
    assert article["author"] == "Roblox Newsroom"
    assert article["published_at"].isoformat() == "2026-07-16T20:00:00"
    assert "It’s a complete first paragraph." in article["text"]
    assert "Second paragraph." in article["text"]
    assert "This must not be included." not in article["text"]
