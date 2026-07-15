"""
Fetch 游戏日报 (yxrb.net) articles from its mobile site.

游戏日报's mobile listing (news.yxrb.net/mobile/) is a phpcms site whose list
pages expose article links shaped like
`index.php?m=mobile&c=index&a=show&catid={cat}&id={id}` but carry no visible
publish date. Each article page, however, does: the `.main-article` block holds
the `<h1>` title, an `.info` line beginning with `YYYY-MM-DD HH:MM:SS`, and a
`.content` body. So the collector scans the mobile home plus a few category
lists for show-links, opens each article page to read its real timestamp, and
keeps only those inside the window. Plain urllib + regex; no browser needed.
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


BASE = "https://news.yxrb.net/mobile/"
SOURCE_DOMAIN = "yxrb.net"
SOURCE_KEY = "yxrb"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
PER_ARTICLE_DELAY = 0.4
# 资讯 / 访谈 / 游理游据 —— the news-bearing categories.
LIST_CATEGORIES = (6, 7, 9)
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


def find_show_links(list_html: str) -> list[tuple[int, int]]:
    """Return (catid, id) pairs from show-links on a list page, newest-first order preserved."""
    out: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for m in re.finditer(r"a=show&(?:amp;)?catid=(\d+)&(?:amp;)?id=(\d+)", list_html):
        pair = (int(m.group(1)), int(m.group(2)))
        if pair in seen:
            continue
        seen.add(pair)
        out.append(pair)
    return out


def show_url(catid: int, art_id: int) -> str:
    return urljoin(BASE, f"index.php?m=mobile&c=index&a=show&catid={catid}&id={art_id}")


def parse_article(html_text: str) -> dict | None:
    block = extract_balanced_div(html_text, "main-article")
    if not block:
        return None
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", block, re.S)
    title = _html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else ""
    dm = re.search(r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})", block)
    if not dm:
        dm = re.search(r"(\d{4}-\d{2}-\d{2})", block)
    published = None
    if dm:
        try:
            published = datetime.fromisoformat(dm.group(1))
        except ValueError:
            published = None
    content_html = extract_balanced_div(block, "content") or extract_balanced_div(html_text, "content")
    if not title or published is None:
        return None
    return {"title": title, "published_at": published, "html": content_html}


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
    parser = argparse.ArgumentParser(description="Fetch 游戏日报 articles from the mobile site.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=2, help="Category list pages to scan per category.")
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

    # Gather candidate (catid, id) pairs from the home page + category lists.
    pairs: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()

    def add_pairs(html_text: str) -> None:
        for pair in find_show_links(html_text):
            if pair not in seen:
                seen.add(pair)
                pairs.append(pair)

    home = http_get(BASE)
    if home:
        add_pairs(home)
    for cat in LIST_CATEGORIES:
        for page in range(1, max(1, args.max_pages) + 1):
            suffix = "" if page == 1 else f"&page={page}"
            lst = http_get(urljoin(BASE, f"index.php?m=mobile&c=index&a=lists&catid={cat}{suffix}"))
            if not lst:
                break
            before = len(pairs)
            add_pairs(lst)
            if len(pairs) == before and page > 1:
                break
    print(f"[list] candidate articles: {len(pairs)}")

    ok = 0
    scanned = 0
    dup = 0
    seen_titles: set[str] = set()
    for catid, art_id in pairs:
        if args.limit and ok >= args.limit:
            break
        scanned += 1
        page = http_get(show_url(catid, art_id))
        if not page:
            continue
        art = parse_article(page)
        time.sleep(PER_ARTICLE_DELAY)
        if not art:
            continue
        pub = art["published_at"]
        if pub >= until or pub < since:
            continue
        # 源站列表常出现同标题重复条目（不同 id 指向同一文章），运行内按标题去重。
        title_key = re.sub(r"\s+", "", art["title"])
        if title_key in seen_titles:
            dup += 1
            continue
        seen_titles.add(title_key)
        item_id = f"{catid}_{art_id}"
        write_article_record(
            args.out,
            manifest,
            item_id,
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": art["title"],
                "url": show_url(catid, art_id),
                "text": html_to_text(art["html"]),
                "html": art["html"],
                "published_at": pub.isoformat(timespec="seconds"),
                "extra": {"catid": catid, "article_id": art_id},
            },
        )
        ok += 1
        print(f"[{item_id}] saved  {pub:%Y-%m-%d}  {art['title'][:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} dup_skipped={dup} scanned={scanned} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
