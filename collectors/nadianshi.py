"""Fetch full-text industry news from 手游那点事 (nadianshi.com).

Discovery is limited to the site's ``今日关注`` category. Article pages expose
server-rendered titles, minute-level publication times, and a dedicated ``text``
container, allowing full-body extraction without browser automation.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from datetime import datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from article_store import write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths


CATALOG_URL = "http://www.nadianshi.com/category/today"
SOURCE_DOMAIN = "nadianshi.com"
SOURCE_KEY = "nadianshi"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.7",
        },
    )
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        try:
            with urlopen(request, timeout=HTTP_TIMEOUT) as response:
                return response.read().decode("utf-8-sig", "replace")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_exc = exc
            if isinstance(exc, HTTPError) and exc.code == 404:
                break
            if attempt < HTTP_RETRIES:
                print(f"[http] retry {attempt}/{HTTP_RETRIES}: {url} ({exc})", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"GET failed after {HTTP_RETRIES} tries: {url} ({last_exc!r})")


def parse_date(value: str) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return datetime.fromisoformat(raw)
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).replace(tzinfo=None)


def preset_window(name: str) -> tuple[datetime, datetime]:
    now = datetime.now().replace(microsecond=0)
    today = now.replace(hour=0, minute=0, second=0)
    if name == "last-7-days":
        return now - timedelta(days=7), now
    if name == "yesterday":
        return today - timedelta(days=1), today
    if name == "today":
        return today, now
    raise ValueError(f"unknown preset: {name}")


def catalog_url(page: int) -> str:
    return CATALOG_URL if page == 1 else f"{CATALOG_URL}/page/{page}"


class _CatalogParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.urls: list[str] = []
        self._seen: set[str] = set()
        self._main_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = set(next((value or "" for key, value in attrs if key == "class"), "").split())
        if tag == "div" and "partCont_left" in classes and self._main_depth == 0:
            self._main_depth = 1
            return
        if self._main_depth and tag == "div":
            self._main_depth += 1
        if self._main_depth and tag == "a":
            href = next((value or "" for key, value in attrs if key == "href"), "")
            if not re.fullmatch(r"https?://(?:www\.)?nadianshi\.com/\d{4}/\d{2}/\d+/?", href, re.I):
                return
            url = urljoin(CATALOG_URL, html.unescape(href)).rstrip("/")
            if url not in self._seen:
                self._seen.add(url)
                self.urls.append(url)

    def handle_endtag(self, tag: str) -> None:
        if tag == "div" and self._main_depth:
            self._main_depth -= 1


def discover_article_urls(page_html: str) -> list[str]:
    parser = _CatalogParser()
    parser.feed(page_html)
    return parser.urls


class _ArticleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.date_text = ""
        self.body_parts: list[str] = []
        self._in_article_title = False
        self._in_date = False
        self._body_depth = 0

    @staticmethod
    def _classes(attrs: list[tuple[str, str | None]]) -> set[str]:
        value = next((value or "" for key, value in attrs if key == "class"), "")
        return set(value.split())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = self._classes(attrs)
        if tag == "h1" and not self.title:
            self._in_article_title = True
        if tag == "div" and "info_date" in classes:
            self._in_date = True
        if tag == "div" and "text" in classes and self._body_depth == 0:
            self._body_depth = 1
            return
        if self._body_depth:
            if tag == "div":
                self._body_depth += 1
            if tag in {"p", "br", "h2", "h3", "li"}:
                self.body_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1":
            self._in_article_title = False
        if tag == "div" and self._in_date:
            self._in_date = False
        if tag == "div" and self._body_depth:
            self._body_depth -= 1
        if self._body_depth and tag in {"p", "h2", "h3", "li"}:
            self.body_parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._in_article_title:
            self.title += data
        if self._in_date:
            self.date_text += data
        if self._body_depth:
            self.body_parts.append(data)


def parse_article_datetime(url: str, value: str) -> datetime | None:
    path_match = re.search(r"/(\d{4})/(\d{2})/\d+", urlparse(url).path)
    date_match = re.search(r"(\d{1,2})月\s*(\d{1,2}),\s*(\d{1,2}):(\d{2})", value)
    if not path_match or not date_match:
        return None
    year, url_month = map(int, path_match.groups())
    month, day, hour, minute = map(int, date_match.groups())
    if month != url_month:
        return None
    try:
        return datetime(year, month, day, hour, minute)
    except ValueError:
        return None


def make_item_id(url: str) -> str:
    path = urlparse(url).path.strip("/")
    clean = re.sub(r"\W+", "_", path).strip("_")
    if len(clean) <= 56:
        return clean
    return f"{clean[:47].rstrip('_')}_{hashlib.sha1(url.encode('utf-8')).hexdigest()[:8]}"


def parse_article(url: str, page_html: str) -> dict | None:
    parser = _ArticleParser()
    parser.feed(page_html)
    title = re.sub(r"\s+", " ", parser.title).strip()
    published_at = parse_article_datetime(url, parser.date_text)
    body_text = "\n".join(
        line for line in (re.sub(r"\s+", " ", part).strip() for part in "".join(parser.body_parts).splitlines()) if line
    )
    if not title or published_at is None or not body_text:
        return None
    author = ""
    author_match = re.search(r"^文[丨｜|]\s*游戏那点事[丨｜|]\s*([^\n]+)", body_text)
    if author_match:
        author = author_match.group(1).strip()
    return {
        "id": make_item_id(url),
        "url": url,
        "title": title,
        "published_at": published_at,
        "author": author,
        "text": body_text,
        "html": "",
    }


def load_manifest(out_dir: Path) -> dict:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME):
        if not path.exists() and legacy_path.exists():
            path = legacy_path
            break
    if not path.exists():
        return {"items": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch full-text news from 手游那点事 今日关注.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=3)
    parser.add_argument("--headful", action="store_true", help="Unused; CLI compatibility.")
    args = parser.parse_args()

    since, until = preset_window(args.preset)
    if args.since:
        since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    urls: list[str] = []
    seen: set[str] = set()
    for page in range(1, max(1, args.max_pages) + 1):
        url = catalog_url(page)
        print(f"[catalog] open {url}")
        page_urls = discover_article_urls(fetch_text(url))
        print(f"[catalog] page={page} discovered={len(page_urls)}")
        for article_url in page_urls:
            if article_url not in seen:
                seen.add(article_url)
                urls.append(article_url)

    selected: list[dict] = []
    failures = 0
    for url in urls:
        try:
            article = parse_article(url, fetch_text(url))
        except RuntimeError as exc:
            failures += 1
            print(f"[article] failed: {url} ({exc})", file=sys.stderr)
            continue
        if article is None:
            failures += 1
            print(f"[article] missing title/date/body: {url}", file=sys.stderr)
            continue
        if since <= article["published_at"] < until:
            selected.append(article)

    selected.sort(key=lambda item: item["published_at"], reverse=True)
    if args.limit > 0:
        selected = selected[: args.limit]

    for article in selected:
        write_article_record(
            args.out,
            manifest,
            article["id"],
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "section": "industry_news",
                "title": article["title"],
                "url": article["url"],
                "author": article["author"],
                "text": article["text"],
                "html": article["html"],
                "published_at": article["published_at"].isoformat(timespec="seconds"),
            },
        )
        print(f"[{article['id']}] saved {article['published_at']:%Y-%m-%d %H:%M} {article['title'][:60]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={len(selected)} failures={failures} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
