from __future__ import annotations

import sys
from io import BytesIO
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlsplit
from unittest.mock import patch


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


def test_fetch_refreshes_self_redirect_preserving_query_and_source_url() -> None:
    url = collector.CATALOG_URL + "?page=1&empty="
    error = HTTPError(url, 301, "redirect loop", {"Location": url}, None)
    with patch.object(collector, "urlopen", side_effect=[error, BytesIO("正文".encode())]) as open_mock, \
         patch.object(collector.time, "sleep") as sleep_mock:
        assert collector.fetch_text(url) == "正文"
    requested = [call.args[0].full_url for call in open_mock.call_args_list]
    assert requested[0] == url
    refreshed = urlsplit(requested[1])
    assert refreshed.scheme == "http" and refreshed.netloc == "www.nadianshi.com"
    query = parse_qs(refreshed.query, keep_blank_values=True)
    assert query["page"] == ["1"] and query["empty"] == [""]
    assert query["_nadianshi_refresh"][0].isdigit()
    assert url == collector.CATALOG_URL + "?page=1&empty="
    sleep_mock.assert_not_called()


def test_fetch_healthy_page_does_not_add_refresh_parameter() -> None:
    with patch.object(collector, "urlopen", return_value=BytesIO(b"normal")) as open_mock:
        assert collector.fetch_text(ARTICLE_URL) == "normal"
    assert open_mock.call_args.args[0].full_url == ARTICLE_URL
    open_mock.assert_called_once()


def test_fetch_404_does_not_retry_or_refresh() -> None:
    error = HTTPError(ARTICLE_URL, 404, "missing", {}, None)
    with patch.object(collector, "urlopen", side_effect=error) as open_mock, \
         patch.object(collector.time, "sleep") as sleep_mock:
        try:
            collector.fetch_text(ARTICLE_URL)
        except RuntimeError:
            pass
        else:
            raise AssertionError("404 must remain a failure")
    open_mock.assert_called_once()
    sleep_mock.assert_not_called()


def test_fetch_self_redirect_recovery_stays_bounded() -> None:
    def redirect(request, timeout):
        raise HTTPError(request.full_url, 301, "loop", {"Location": request.full_url}, None)
    with patch.object(collector, "urlopen", side_effect=redirect) as open_mock, \
         patch.object(collector.time, "sleep"):
        try:
            collector.fetch_text(collector.CATALOG_URL)
        except RuntimeError:
            pass
        else:
            raise AssertionError("persistent self-redirect must fail")
    assert open_mock.call_count == collector.HTTP_RETRIES
