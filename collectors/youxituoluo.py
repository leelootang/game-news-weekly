"""
Fetch 游戏陀螺 articles from youxituoluo.com and export PDFs.

The homepage exposes a newest-first article list with stable timestamps. The
collector scans that list until it sees entries older than the requested window,
then opens each article page to extract canonical title, timestamp, and body.
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
from urllib.parse import urljoin

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright


BASE = "https://www.youxituoluo.com"
LIST_URL = f"{BASE}/"
SOURCE_DOMAIN = "youxituoluo.com"
SOURCE_KEY = "youxituoluo"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 30_000
PER_ARTICLE_DELAY = 1.0
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
    published_at: datetime
    raw_published_at: str


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
    match = re.search(r"/(\d+)\.html(?:$|\?)", url)
    if match:
        return match.group(1)
    return re.sub(r"\W+", "_", url).strip("_")[-24:] or "unknown"


def parse_list_datetime(value: str, now: datetime) -> datetime | None:
    text = re.sub(r"\s+", " ", value.strip())
    if not text:
        return None
    match = re.search(r"(\d{4}-\d{2}-\d{2}\s+\d{1,2}:\d{2})", text)
    if match:
        return datetime.fromisoformat(match.group(1))
    match = re.search(r"(\d+)\s*小时前", text)
    if match:
        return now - timedelta(hours=int(match.group(1)))
    match = re.search(r"(\d+)\s*分钟前", text)
    if match:
        return now - timedelta(minutes=int(match.group(1)))
    return None


def parse_article_datetime(value: str) -> datetime | None:
    match = re.search(r"(\d{4}-\d{2}-\d{2}\s+\d{1,2}:\d{2})", value.strip())
    if not match:
        return None
    return datetime.fromisoformat(match.group(1))


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
        backup = path.with_suffix(path.suffix + ".broken")
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


async def collect_news_items(page, since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    print(f"[list] open {LIST_URL}")
    await page.goto(LIST_URL, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
    await page.wait_for_load_state("networkidle", timeout=PAGE_TIMEOUT)

    for _ in range(max(0, max_pages - 1)):
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(500)

    try:
        await page.wait_for_selector(".article_list li .intro", timeout=15_000)
    except PWTimeout as exc:
        raise RuntimeError("no 游戏陀螺 article list items found; source structure may have changed") from exc

    rows = await page.evaluate(
        """() => [...document.querySelectorAll('.article_list li .intro')].map(item => {
            const link = item.querySelector('a.title[href]');
            const time = item.querySelector('.otherInfo span');
            const status = item.querySelector('.status');
            let title = link ? link.innerText.trim() : '';
            if (status && title.startsWith(status.innerText.trim())) {
                title = title.slice(status.innerText.trim().length).trim();
            }
            return {
                href: link ? link.href : '',
                title,
                time: time ? time.innerText.trim() : '',
                text: item.innerText || item.textContent || ''
            };
        })"""
    )

    items: list[NewsItem] = []
    seen: set[str] = set()
    now = datetime.now().replace(microsecond=0)
    older_count = 0

    for row in rows:
        href = urljoin(BASE, row.get("href") or "")
        title = re.sub(r"\s+", " ", row.get("title") or "").strip()
        raw_time = row.get("time") or row.get("text") or ""
        published_at = parse_list_datetime(raw_time, now)
        if not href or not title or not published_at:
            continue
        news_id = make_news_id(href)
        if news_id in seen:
            continue
        seen.add(news_id)
        if published_at >= until:
            continue
        if published_at < since:
            older_count += 1
            continue
        items.append(NewsItem(news_id, href, title, published_at, raw_time))

    if not older_count:
        raise RuntimeError("homepage scan did not reach articles older than --since; cannot prove completeness")

    print(f"[list] collected candidates={len(items)} older={older_count} scanned={len(rows)}")
    items.sort(key=lambda x: x.published_at)
    return items


async def fetch_article_meta(page) -> dict[str, str]:
    return await page.evaluate(
        """() => {
            const text = selector => {
                const el = document.querySelector(selector);
                return el ? (el.innerText || el.textContent || '').trim() : '';
            };
            const content = document.querySelector('.content_con');
            if (content) {
                content.querySelectorAll('img').forEach(img => {
                    const src = img.getAttribute('data-src') || img.getAttribute('src');
                    if (src) img.setAttribute('src', src);
                    img.removeAttribute('data-src');
                });
                content.querySelectorAll('script, iframe, style').forEach(el => el.remove());
            }
            return {
                title: text('.title_detail'),
                published: text('.description_content'),
                content_html: content ? content.innerHTML : ''
            };
        }"""
    )


async def scroll_for_lazy_images(page) -> None:
    await page.evaluate(
        """async () => {
            const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
            const height = document.body.scrollHeight;
            for (let y = 0; y < height; y += 700) {
                window.scrollTo(0, y);
                await sleep(100);
            }
            window.scrollTo(0, 0);
        }"""
    )


def build_printable_html(title: str, published: str, content_html: str) -> str:
    safe_title = html.escape(title)
    safe_published = html.escape(published)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>{safe_title}</title>
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
    <h1>{safe_title}</h1>
    <div class="meta">游戏陀螺 {safe_published}</div>
    <article>{content_html}</article>
  </main>
</body>
</html>"""


async def save_article_pdf(context, item: NewsItem, out_dir: Path, manifest: dict) -> bool:
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
        print(f"[{item.news_id}] open {item.url}")
        await page.goto(item.url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.wait_for_load_state("networkidle", timeout=PAGE_TIMEOUT)
        await page.wait_for_selector(".title_detail, .content_con", timeout=15_000)
        await scroll_for_lazy_images(page)
        meta = await fetch_article_meta(page)
        if not meta.get("content_html"):
            raise RuntimeError("article content was empty")

        title = meta.get("title") or item.title
        page_published_at = parse_article_datetime(meta.get("published") or "")
        published_at = page_published_at or item.published_at
        if not save_pdf_enabled():
            write_article_record(
                out_dir,
                manifest,
                item.news_id,
                {
                    "source": SOURCE_DOMAIN,
                    "source_key": SOURCE_KEY,
                    "title": title,
                    "url": item.url,
                    "text": html_to_text(meta["content_html"]),
                    "html": meta["content_html"],
                    "published_at": published_at.isoformat(timespec="seconds"),
                    "extra": {
                        "list_published_at": item.published_at.isoformat(timespec="seconds"),
                        "raw_published_at": item.raw_published_at,
                        "page_published": meta.get("published") or "",
                    },
                },
            )
            save_manifest(out_dir, manifest)
            print(f"[{item.news_id}] saved text record")
            return True

        final_name = f"{FILE_PREFIX}_{published_at:%Y-%m-%d}_{item.news_id}_{sanitize_filename(title)}.pdf"
        final_path = out_dir / final_name

        await page.set_content(
            build_printable_html(title, meta.get("published") or published_at.isoformat(sep=" ", timespec="minutes"), meta["content_html"]),
            wait_until="domcontentloaded",
        )
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
            "title": title,
            "url": item.url,
            "published_at": published_at.isoformat(timespec="seconds"),
            "list_published_at": item.published_at.isoformat(timespec="seconds"),
            "raw_published_at": item.raw_published_at,
            "page_published": meta.get("published") or "",
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
    parser = argparse.ArgumentParser(description="Fetch 游戏陀螺 articles and save them as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=3, help="Homepage scroll depth")
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

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not args.headful)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale="zh-CN",
            timezone_id="Asia/Shanghai",
            viewport={"width": 1280, "height": 900},
        )
        list_page = await context.new_page()
        items = await collect_news_items(list_page, since, until, args.max_pages)
        await list_page.close()
        if args.limit > 0:
            items = items[: args.limit]
        print(f"[list] collected {len(items)} article(s)")

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
