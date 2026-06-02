"""
Fetch 竞核 articles from cgames.com and export PDFs.

The site injects channel lists dynamically, so this collector uses Playwright
for list discovery and article extraction. Article detail pages expose stable
title/date/body selectors.
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


BASE = "https://cgames.com"
CHANNELS = {
    "hot": f"{BASE}/channels/2.html",
    "game": f"{BASE}/channels/6.html",
    "review": f"{BASE}/channels/7.html",
    "producer": f"{BASE}/channels/8.html",
    "trend": f"{BASE}/channels/9.html",
}
SOURCE_DOMAIN = "cgames.com"
SOURCE_KEY = "cgames"
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
    channel: str


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
    match = re.search(r"/contents/\d+/(\d+)\.html", url)
    if match:
        return match.group(1)
    return re.sub(r"\W+", "_", url).strip("_")[-24:] or "unknown"


def parse_article_datetime(value: str) -> datetime | None:
    match = re.search(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", value.strip())
    if not match:
        return None
    year, month, day = (int(part) for part in match.groups())
    return datetime(year, month, day)


def parse_list_datetime(value: str, since: datetime, until: datetime) -> datetime | None:
    text = re.sub(r"\s+", " ", value.strip())
    match = re.search(r"(\d{4})[.\-/](\d{1,2})[.\-/](\d{1,2})", text)
    if match:
        year, month, day = (int(part) for part in match.groups())
        return datetime(year, month, day)
    match = re.search(r"(\d{1,2})月(\d{1,2})日", text)
    if match:
        month, day = (int(part) for part in match.groups())
        candidates = [datetime(year, month, day) for year in {since.year, until.year, datetime.now().year}]
        return min(candidates, key=lambda dt: min(abs((dt - since).total_seconds()), abs((dt - until).total_seconds())))
    match = re.search(r"(\d+)\s*小时前", text)
    if match:
        return datetime.now().replace(microsecond=0) - timedelta(hours=int(match.group(1)))
    match = re.search(r"(\d+)\s*分钟前", text)
    if match:
        return datetime.now().replace(microsecond=0) - timedelta(minutes=int(match.group(1)))
    return None


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


async def extract_list_links(page) -> list[dict[str, str]]:
    return await page.evaluate(
        """() => [...document.querySelectorAll('a[href*="/contents/"]')].map(a => ({
            href: a.href,
            text: (a.innerText || a.textContent || '').trim()
        })).filter(x => /\\/contents\\/\\d+\\/\\d+\\.html/.test(x.href) && x.text)"""
    )


async def fetch_article_item(context, url: str, channel: str) -> NewsItem:
    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.wait_for_load_state("networkidle", timeout=PAGE_TIMEOUT)
        await page.wait_for_selector(".kbxq_l h2, .xqnr", timeout=15_000)
        meta = await page.evaluate(
            """() => {
                const text = selector => {
                    const el = document.querySelector(selector);
                    return el ? (el.innerText || el.textContent || '').trim() : '';
                };
                const content = document.querySelector('.xqnr');
                if (content) {
                    content.querySelectorAll('img').forEach(img => {
                        const src = img.getAttribute('data-src') || img.getAttribute('data-original') || img.getAttribute('src');
                        if (src) img.setAttribute('src', new URL(src, location.href).href);
                        img.removeAttribute('data-src');
                        img.removeAttribute('data-original');
                    });
                    content.querySelectorAll('script, iframe, style').forEach(el => el.remove());
                }
                return {
                    title: text('.kbxq_l h2') || document.title.trim(),
                    published: text('.xqrq'),
                    content_html: content ? content.innerHTML : ''
                };
            }"""
        )
        published_at = parse_article_datetime(meta.get("published") or "")
        if not published_at:
            raise RuntimeError(f"cannot parse published time: {meta.get('published')!r}")
        if not meta.get("content_html"):
            raise RuntimeError("article content was empty")
        return NewsItem(
            news_id=make_news_id(url),
            url=url,
            title=meta.get("title") or make_news_id(url),
            content_html=meta["content_html"],
            published_at=published_at,
            raw_published_at=meta.get("published") or "",
            channel=channel,
        )
    finally:
        await page.close()


async def collect_news_items(context, since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    list_page = await context.new_page()
    items: dict[str, NewsItem] = {}
    seen: set[str] = set()
    channels_without_boundary: list[str] = []
    try:
        for channel, base_url in CHANNELS.items():
            reached_older_boundary = False
            for page_no in range(1, max_pages + 1):
                url = base_url if page_no == 1 else f"{base_url}?page={page_no}"
                print(f"[list] open {channel} {url}")
                await list_page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
                await list_page.wait_for_load_state("networkidle", timeout=PAGE_TIMEOUT)
                try:
                    await list_page.wait_for_selector('a[href*="/contents/"]', timeout=15_000)
                except PWTimeout as exc:
                    raise RuntimeError(f"no 竞核 article links found on {channel}; source structure may have changed") from exc

                rows = await extract_list_links(list_page)
                page_new = 0
                page_older = 0
                page_candidates = 0
                for row in rows:
                    href = urljoin(BASE, row["href"])
                    news_id = make_news_id(href)
                    if news_id in seen:
                        continue
                    seen.add(news_id)
                    list_published_at = parse_list_datetime(row.get("text") or "", since, until)
                    if list_published_at and list_published_at >= until:
                        continue
                    if list_published_at and list_published_at < since:
                        page_older += 1
                        continue
                    page_candidates += 1
                    try:
                        item = await fetch_article_item(context, href, channel)
                    except Exception as exc:
                        print(f"[{news_id}] metadata failed: {exc!r}", file=sys.stderr)
                        continue

                    if item.published_at >= until:
                        continue
                    if item.published_at < since:
                        page_older += 1
                        continue
                    items[item.news_id] = item
                    page_new += 1

                print(
                    f"[list] {channel} page {page_no}: candidates={page_candidates}, "
                    f"+{page_new}, older={page_older}, total {len(items)}"
                )
                if page_older:
                    reached_older_boundary = True
                    break
            if not reached_older_boundary:
                channels_without_boundary.append(channel)
    finally:
        await list_page.close()

    if channels_without_boundary:
        raise RuntimeError(
            "hit --max-pages before proving these 竞核 channels moved older than requested window: "
            + ", ".join(channels_without_boundary)
        )

    result = sorted(items.values(), key=lambda x: (x.published_at, x.news_id))
    return result


def build_printable_html(item: NewsItem) -> str:
    title = html.escape(item.title)
    published = html.escape(item.published_at.isoformat(sep=" ", timespec="minutes"))
    channel = html.escape(item.channel)
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
      line-height: 1.76;
    }}
    main {{
      max-width: 820px;
      margin: 0 auto;
      padding: 24px 10px 44px;
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
    h6 {{
      font-size: 16px;
      margin: 0 0 18px;
      color: #555;
    }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">竞核 {channel} {published}</div>
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
                "extra": {"raw_published_at": item.raw_published_at},
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
            "channel": item.channel,
            "published_at": item.published_at.isoformat(timespec="seconds"),
            "raw_published_at": item.raw_published_at,
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
    parser = argparse.ArgumentParser(description="Fetch 竞核 articles and save them as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=3, help="Maximum list pages to scan per channel")
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

        items = await collect_news_items(context, since, until, args.max_pages)
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
