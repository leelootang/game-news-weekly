"""
Fetch 游研社 long-form docs from the RSS feed and export PDFs.

The /docs list renders relative times such as "2天前", while the RSS feed
contains canonical pubDate values and full article HTML. Use RSS for discovery
and content, then render a clean PDF locally.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from playwright.async_api import async_playwright


RSS_URL = "https://www.yystv.cn/rss/feed"
SOURCE_DOMAIN = "yystv.net"
SOURCE_KEY = "yystv"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 30_000
PER_ARTICLE_DELAY = 0.8
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class NewsItem:
    news_id: str
    url: str
    title: str
    category: str
    content_html: str
    published_at: datetime
    raw_published_at: str
    author: str


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        dt = datetime.fromisoformat(raw)
        if end_of_day:
            return dt + timedelta(days=1)
        return dt
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


def sanitize_filename(name: str, max_len: int = 90) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:max_len].rstrip(" .") or "untitled"


def make_news_id(url: str) -> str:
    match = re.search(r"/p/(\d+)", url)
    if match:
        return match.group(1)
    parsed = urlparse(url)
    return re.sub(r"\W+", "_", parsed.path).strip("_")[-24:] or "unknown"


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml,text/xml,*/*"})
    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            with urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8-sig")
        except (OSError, URLError) as exc:
            last_exc = exc
            if attempt < 3:
                print(f"[rss] retry {attempt}/3 after 游研社 RSS error: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch 游研社 RSS: {url}: {last_exc}") from last_exc


def parse_rss_datetime(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    try:
        dt = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None
    if dt.tzinfo:
        return dt.astimezone(timezone(timedelta(hours=8))).replace(tzinfo=None)
    return dt


def item_text(item: ET.Element, tag: str) -> str:
    node = item.find(tag)
    return node.text.strip() if node is not None and node.text else ""


def parse_author(source_text: str) -> str:
    match = re.search(r"by\s+(.+)$", source_text.strip())
    return match.group(1).strip() if match else source_text.strip()


def clean_content_html(content_html: str) -> str:
    content_html = re.sub(r"<script\b[^>]*>.*?</script>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"<iframe\b[^>]*>.*?</iframe>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"<style\b[^>]*>.*?</style>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"\sdata-original=", " src=", content_html)
    return content_html


def load_manifest(out_dir: Path) -> dict:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    legacy_paths = legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_paths:
        if not path.exists() and legacy_path.exists():
            path = legacy_path
            break
    if not path.exists():
        return {"items": {}}
    try:
        manifest = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        backup = path.with_suffix(path.suffix + ".broken")
        path.replace(backup)
        print(f"[manifest] manifest broken, moved to {backup.name}", file=sys.stderr)
        return {"items": {}}

    # Older experimental yystv manifests used /n/ short-news URLs. Drop those
    # records so runner counts represent long-form /docs articles only.
    manifest["items"] = {
        item_id: item
        for item_id, item in manifest.get("items", {}).items()
        if "/p/" in (item.get("url") or "")
    }
    return manifest


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def collect_news_items(since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    if max_pages != 1:
        print("[rss] 游研社 RSS is a single feed; --max-pages is accepted for runner compatibility")

    print(f"[rss] open {RSS_URL}")
    root = ET.fromstring(fetch_text(RSS_URL))
    items: list[NewsItem] = []
    older = 0
    skipped_future = 0

    for node in root.findall("./channel/item"):
        title = item_text(node, "title")
        url = item_text(node, "link")
        raw_published = item_text(node, "pubDate")
        published_at = parse_rss_datetime(raw_published)
        if not url or not title or not published_at:
            continue
        if published_at >= until:
            skipped_future += 1
            continue
        if published_at < since:
            older += 1
            continue

        content_html = clean_content_html(item_text(node, "description"))
        if not content_html:
            print(f"[{make_news_id(url)}] empty RSS content, skip", file=sys.stderr)
            continue
        items.append(
            NewsItem(
                news_id=make_news_id(url),
                url=url.replace("https://www.yystv.cn", "http://www.yystv.net"),
                title=title,
                category=item_text(node, "category"),
                content_html=content_html,
                published_at=published_at,
                raw_published_at=raw_published,
                author=parse_author(item_text(node, "source")),
            )
        )

    print(f"[rss] collected {len(items)} article(s), older={older}, future_or_today={skipped_future}")
    if not older and items:
        raise RuntimeError("RSS did not include an item older than --since; cannot prove completeness")
    items.sort(key=lambda x: x.published_at)
    return items


def build_printable_html(item: NewsItem) -> str:
    title = html.escape(item.title)
    author = html.escape(item.author)
    category = html.escape(item.category)
    published = html.escape(item.published_at.isoformat(sep=" ", timespec="minutes"))
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    body {{
      margin: 0;
      background: #fff;
      color: #111;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif;
      line-height: 1.78;
    }}
    main {{
      max-width: 820px;
      margin: 0 auto;
      padding: 24px 10px 44px;
    }}
    h1 {{
      font-size: 30px;
      line-height: 1.35;
      margin: 0 0 12px;
      font-weight: 700;
    }}
    .meta {{
      color: #666;
      font-size: 14px;
      margin-bottom: 28px;
    }}
    img {{
      max-width: 100%;
      height: auto;
    }}
    p {{
      margin: 0 0 1em;
    }}
    blockquote {{
      margin: 0 0 1.2em;
      padding: 0 0 0 16px;
      border-left: 4px solid #ddd;
      color: #333;
    }}
    .picinfo {{
      display: block;
      color: #777;
      font-size: 13px;
      text-align: center;
      margin-top: 4px;
    }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">游研社 {category} {author} {published}</div>
    <article>{item.content_html}</article>
  </main>
</body>
</html>"""


async def save_article_pdf(context, item: NewsItem, out_dir: Path, manifest: dict) -> bool:
    if not save_pdf_enabled():
        write_article_record(
            out_dir,
            manifest,
            item.news_id,
            {
                "source_key": SOURCE_KEY,
                "source": SOURCE_DOMAIN,
                "title": item.title,
                "url": item.url,
                "published_at": item.published_at.isoformat(timespec="seconds"),
                "author": item.author,
                "text": html_to_text(item.content_html),
                "html": item.content_html,
                "extra": {
                    "category": item.category,
                    "raw_published_at": item.raw_published_at,
                },
            },
        )
        save_manifest(out_dir, manifest)
        print(f"[{item.news_id}] saved text record")
        return True

    recorded = manifest.setdefault("items", {}).get(item.news_id)
    if recorded and recorded.get("data_file"):
        print(f"[{item.news_id}] already saved, skip")
        return True
    if save_pdf_enabled() and recorded and recorded.get("file") and (out_dir / recorded["file"]).exists():
        print(f"[{item.news_id}] already saved, skip")
        return True

    page = await context.new_page()
    tmp_path = out_dir / f".tmp_{item.news_id}.pdf"
    try:
        final_name = f"{FILE_PREFIX}_{item.published_at:%Y-%m-%d}_{item.news_id}_{sanitize_filename(item.title)}.pdf"
        final_path = out_dir / final_name

        print(f"[{item.news_id}] render {item.url}")
        await page.set_content(build_printable_html(item), wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.emulate_media(media="screen")
        await page.pdf(
            path=str(tmp_path),
            format="A4",
            print_background=True,
            margin={"top": "12mm", "right": "10mm", "bottom": "12mm", "left": "10mm"},
        )
        tmp_path.replace(final_path)

        manifest["items"][item.news_id] = {
            "file": final_name,
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "title": item.title,
            "url": item.url,
            "category": item.category,
            "published_at": item.published_at.isoformat(timespec="seconds"),
            "raw_published_at": item.raw_published_at,
            "author": item.author,
            "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        save_manifest(out_dir, manifest)
        print(f"[{item.news_id}] saved {final_name}")
        return True
    except Exception as exc:
        print(f"[{item.news_id}] failed: {exc!r}", file=sys.stderr)
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
        return False
    finally:
        await page.close()


async def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch 游研社 long-form docs and save them as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility")
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum articles to export")
    parser.add_argument("--headful", action="store_true", help="Show browser window")
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
    save_manifest(args.out, manifest)
    print(f"[config] window: {since} <= published < {until}")
    print(f"[config] output: {args.out.resolve()}")

    items = collect_news_items(since, until, args.max_pages)
    if args.limit > 0:
        items = items[: args.limit]
    print(f"[rss] selected {len(items)} article(s)")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not args.headful)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale="zh-CN",
            timezone_id="Asia/Shanghai",
            viewport={"width": 1280, "height": 900},
        )

        ok = 0
        fail = 0
        for item in items:
            if await save_article_pdf(context, item, args.out, manifest):
                ok += 1
            else:
                fail += 1
            await asyncio.sleep(PER_ARTICLE_DELAY)

        await context.close()
        await browser.close()

    print(f"[done] ok={ok} fail={fail} output={args.out.resolve()}")
    if fail:
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())
