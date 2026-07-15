"""
Fetch indienova (indienova.com) independent-game news from its news channel.

indienova's news channel lives at https://indienova.com/indie-game-news/ with
pagination at /indie-game-news/page/N/. Each list page links out to article
pages shaped like /indie-game-news/{slug}/. An article page carries the title
in `<h1 class="big">`, a byline in `<span class="header-info">作者：<a>AUTHOR</a>
<br/>DATE …</span>`, and the body in
`<div class="postcontent clearfix indienova-post-content"><article><div class="single-post …">`.

The byline DATE is RELATIVE for very recent posts ("7 小时前 08:00", "昨天 09:12")
and ABSOLUTE for older ones ("2026-07-01"); parse_byline_date handles both. The
collector scans the news channel (plus a few paginated pages), opens each linked
article to read its real date, and keeps only those inside the window. Plain
urllib + regex; no browser needed.
"""

from __future__ import annotations

import argparse
import html as _html
import json
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from article_store import html_to_text, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


BASE = "https://indienova.com/"
NEWS_PATH = "indie-game-news/"
SOURCE_DOMAIN = "indienova.com"
SOURCE_KEY = "indienova"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
PER_ARTICLE_DELAY = 0.4
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str) -> str | None:
    last: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9"})
        try:
            with urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                return resp.read().decode("utf-8", "replace")
        except HTTPError as exc:
            last = exc
            if exc.code == 404:
                return None
        except (URLError, TimeoutError) as exc:
            last = exc
        if attempt < HTTP_RETRIES:
            time.sleep(1.2 * attempt)
    print(f"[warn] GET failed: {url} ({last!r})", file=sys.stderr)
    return None


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        dt = datetime.fromisoformat(raw)
        return dt + timedelta(days=1) if end_of_day else dt
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


def parse_byline_date(text: str, *, now: datetime | None = None) -> datetime | None:
    """Parse an indienova byline date, absolute or relative, into a naive datetime."""
    now = now or datetime.now().replace(microsecond=0)
    raw = re.sub(r"\s+", " ", text).strip()
    # Absolute "YYYY-MM-DD [HH:MM[:SS]]".
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})(?:\s+(\d{1,2}):(\d{2})(?::(\d{2}))?)?", raw)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        hh = int(m.group(4)) if m.group(4) else 0
        mm = int(m.group(5)) if m.group(5) else 0
        ss = int(m.group(6)) if m.group(6) else 0
        try:
            return datetime(y, mo, d, hh, mm, ss)
        except ValueError:
            return None
    # Relative forms. Optional trailing "HH:MM" is a wall-clock hint we honour.
    clock = re.search(r"(\d{1,2}):(\d{2})", raw)
    hh = int(clock.group(1)) if clock else now.hour
    mm = int(clock.group(2)) if clock else now.minute
    base_day = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
    m = re.search(r"(\d+)\s*分钟前", raw)
    if m:
        return (now - timedelta(minutes=int(m.group(1)))).replace(second=0, microsecond=0)
    m = re.search(r"(\d+)\s*小时前", raw)
    if m:
        return (now - timedelta(hours=int(m.group(1)))).replace(second=0, microsecond=0)
    m = re.search(r"(\d+)\s*天前", raw)
    if m:
        return base_day - timedelta(days=int(m.group(1)))
    if "前天" in raw:
        return base_day - timedelta(days=2)
    if "昨天" in raw:
        return base_day - timedelta(days=1)
    if "今天" in raw:
        return base_day
    return None


def extract_balanced_div(html_text: str, classname: str) -> str:
    m = re.search(r'<div[^>]*class="[^"]*\b' + re.escape(classname) + r'\b[^"]*"[^>]*>', html_text)
    if not m:
        return ""
    start = m.end()
    depth = 1
    for mm in re.finditer(r"<(/?)div\b", html_text[start:]):
        depth += -1 if mm.group(1) else 1
        if depth == 0:
            return html_text[start:start + mm.start()]
    return html_text[start:]


def find_article_links(list_html: str) -> list[str]:
    """Return absolute article URLs (/indie-game-news/{slug}/) in list order, deduped."""
    out: list[str] = []
    seen: set[str] = set()
    for m in re.finditer(r'href=["\']([^"\']*/indie-game-news/[^"\']+)["\']', list_html):
        href = _html.unescape(m.group(1))
        abs_url = urljoin(BASE, href)
        # Skip pagination and the channel root itself.
        if re.search(r"/indie-game-news/(page/\d+/?)?$", abs_url):
            continue
        # Article slug pages: /indie-game-news/<slug>/ (single trailing segment).
        if not re.search(r"/indie-game-news/[^/]+/?$", abs_url):
            continue
        abs_url = abs_url.split("#", 1)[0]
        if abs_url in seen:
            continue
        seen.add(abs_url)
        out.append(abs_url)
    return out


def parse_article(html_text: str) -> dict | None:
    h1 = re.search(r'<h1[^>]*class="[^"]*\bbig\b[^"]*"[^>]*>(.*?)</h1>', html_text, re.S)
    if not h1:
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html_text, re.S)
    title = _html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else ""

    author = ""
    published = None
    hi = re.search(r'<span[^>]*class="[^"]*\bheader-info\b[^"]*"[^>]*>(.*?)</span>', html_text, re.S)
    if hi:
        info_html = hi.group(1)
        am = re.search(r"作者：\s*<a[^>]*>(.*?)</a>", info_html, re.S)
        if am:
            author = _html.unescape(re.sub(r"<[^>]+>", "", am.group(1))).strip()
        info_text = _html.unescape(re.sub(r"<[^>]+>", " ", info_html))
        published = parse_byline_date(info_text)

    content_html = extract_balanced_div(html_text, "single-post")
    if not content_html:
        content_html = extract_balanced_div(html_text, "indienova-post-content")
    if not title or published is None:
        return None
    return {"title": title, "author": author, "published_at": published, "html": content_html}


def article_id(url: str) -> str:
    m = re.search(r"/indie-game-news/([^/]+)/?$", url)
    slug = m.group(1) if m else url
    return re.sub(r"\W+", "-", slug).strip("-")[:80] or "unknown"


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
    except Exception:
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch indienova indie-game news.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=3, help="News list pages to scan.")
    parser.add_argument("--headful", action="store_true", help="Unused; CLI compatibility.")
    args = parser.parse_args()

    try:
        since, until = preset_window(args.preset)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if args.since:
        since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    print(f"[config] window: {since} <= published < {until}")

    urls: list[str] = []
    seen: set[str] = set()
    for page in range(1, max(1, args.max_pages) + 1):
        list_url = urljoin(BASE, NEWS_PATH) if page == 1 else urljoin(BASE, f"{NEWS_PATH}page/{page}/")
        lst = http_get(list_url)
        if not lst:
            break
        before = len(urls)
        for u in find_article_links(lst):
            if u not in seen:
                seen.add(u)
                urls.append(u)
        if len(urls) == before and page > 1:
            break
    print(f"[list] candidate articles: {len(urls)}")

    ok = 0
    scanned = 0
    seen_titles: set[str] = set()
    for url in urls:
        if args.limit and ok >= args.limit:
            break
        scanned += 1
        page = http_get(url)
        time.sleep(PER_ARTICLE_DELAY)
        if not page:
            continue
        art = parse_article(page)
        if not art:
            continue
        pub = art["published_at"]
        if pub >= until or pub < since:
            continue
        title_key = re.sub(r"\s+", "", art["title"])
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        item_id = article_id(url)
        write_article_record(
            args.out,
            manifest,
            item_id,
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": art["title"],
                "url": url,
                "author": art["author"],
                "text": html_to_text(art["html"]),
                "html": art["html"],
                "published_at": pub.isoformat(timespec="seconds"),
            },
        )
        ok += 1
        print(f"[{item_id}] saved  {pub:%Y-%m-%d}  {art['title'][:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} scanned={scanned} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
