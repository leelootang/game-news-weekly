"""
Fetch GameLook articles from the public WordPress API and export PDFs.

GameLook's official site exposes recent posts through WordPress REST endpoints,
which are more stable than scraping rendered list pages. The collector paginates
newest-first until it sees articles older than the requested window.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from urllib.error import URLError
from urllib.request import Request, urlopen

from playwright.async_api import async_playwright


API_URL = "http://www.gamelook.com.cn/wp-json/wp/v2/posts"
SOURCE_DOMAIN = "gamelook.com.cn"
SOURCE_KEY = "gamelook"
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
    content_html: str
    published_at: datetime
    raw_published_at: str
    raw_published_gmt: str


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


def parse_post_datetime(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw).replace(tzinfo=None)
    except ValueError:
        return None


def fetch_json(url: str) -> list[dict]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8-sig"))
    except (OSError, URLError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"failed to fetch GameLook API: {url}: {exc}") from exc


def clean_api_html(content_html: str) -> str:
    content_html = re.sub(r"<script\b[^>]*>.*?</script>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"<iframe\b[^>]*>.*?</iframe>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"<style\b[^>]*>.*?</style>", "", content_html, flags=re.I | re.S)
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
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        backup = out_dir / f"{MANIFEST_NAME}.broken"
        path.replace(backup)
        print(f"[manifest] manifest broken, moved to {backup.name}", file=sys.stderr)
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def collect_news_items(since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    items: list[NewsItem] = []
    seen: set[str] = set()
    reached_older_boundary = False

    for page_no in range(1, max_pages + 1):
        url = f"{API_URL}?per_page=100&page={page_no}&orderby=date&order=desc"
        print(f"[list] open {url}")
        posts = fetch_json(url)
        if not posts:
            reached_older_boundary = True
            break

        page_new = 0
        page_older = 0
        for post in posts:
            news_id = str(post.get("id") or "")
            if not news_id or news_id in seen:
                continue
            seen.add(news_id)

            published_at = parse_post_datetime(post.get("date") or "")
            if not published_at:
                continue
            if published_at >= until:
                continue
            if published_at < since:
                page_older += 1
                continue

            title = html.unescape((post.get("title") or {}).get("rendered") or "").strip()
            content_html = clean_api_html((post.get("content") or {}).get("rendered") or "")
            link = post.get("link") or f"http://www.gamelook.com.cn/?p={news_id}"
            items.append(
                NewsItem(
                    news_id=news_id,
                    url=link,
                    title=title or f"gamelook-{news_id}",
                    content_html=content_html,
                    published_at=published_at,
                    raw_published_at=post.get("date") or "",
                    raw_published_gmt=post.get("date_gmt") or "",
                )
            )
            page_new += 1

        print(f"[list] page {page_no}: +{page_new}, older={page_older}, total {len(items)}")
        if page_older and page_new == 0:
            reached_older_boundary = True
            break

    if not reached_older_boundary and max_pages > 0:
        raise RuntimeError(
            f"hit --max-pages={max_pages} before proving GameLook moved older than requested window"
        )

    items.sort(key=lambda x: x.published_at)
    return items


def build_printable_html(item: NewsItem) -> str:
    title = html.escape(item.title)
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
      line-height: 1.72;
    }}
    main {{
      max-width: 820px;
      margin: 0 auto;
      padding: 24px 10px 40px;
    }}
    h1 {{
      font-size: 28px;
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
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">GameLook {published}</div>
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
                "text": html_to_text(item.content_html),
                "html": item.content_html,
                "extra": {
                    "raw_published_at": item.raw_published_at,
                    "raw_published_gmt": item.raw_published_gmt,
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
            "published_at": item.published_at.isoformat(timespec="seconds"),
            "raw_published_at": item.raw_published_at,
            "raw_published_gmt": item.raw_published_gmt,
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
    parser = argparse.ArgumentParser(description="Fetch GameLook articles and save them as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=5, help="Maximum API pages to scan")
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
    print(f"[config] window: {since} <= published < {until}")
    print(f"[config] output: {args.out.resolve()}")

    items = collect_news_items(since, until, args.max_pages)
    if args.limit > 0:
        items = items[: args.limit]
    print(f"[list] collected {len(items)} article(s)")

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
