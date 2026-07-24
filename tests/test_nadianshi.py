from __future__ import annotations

import sys
from pathlib import Path


COLLECTORS_DIR = Path(__file__).resolve().parents[1] / "collectors"
if str(COLLECTORS_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTORS_DIR))

import nadianshi as collector


ARTICLE_URL = "http://www.nadianshi.com/2026/07/415476"


def test_discovery_deduplicates_article_links() -> None:
    catalog = f'''
    <div class="partCont_left">
      <a href="{ARTICLE_URL}">title</a><a href="{ARTICLE_URL}">image</a>
    </div>
    <div class="partCont_right"><a href="http://www.nadianshi.com/2023/12/357731">sidebar</a></div>
    '''
    assert collector.discover_article_urls(catalog) == [ARTICLE_URL]


def test_article_parser_extracts_body_without_related_news() -> None:
    page = """
    <div class="partCont_content_mod_article">
      <h1>原创丨莉莉丝的新FPS项目曝光了：正招聘人才</h1>
      <div class="info"><div class="info_date">7月 21, 23:40</div></div>
      <div class="text">
        <p>文丨游戏那点事丨willow</p>
        <p>莉莉丝UE5预研项目《Project F1》是一款FPS游戏。</p>
      </div>
    </div>
    <h2>相关资讯</h2><p>不应进入正文。</p>
    """
    article = collector.parse_article(ARTICLE_URL, page)
    assert article is not None
    assert article["published_at"].isoformat() == "2026-07-21T23:40:00"
    assert article["author"] == "willow"
    assert "Project F1" in article["text"]
    assert "不应进入正文" not in article["text"]
