"""
Fetch Gcores news in a date range and export each article to PDF.

Typical weekly run:
    python gcores_news_to_pdf.py --preset last-7-days --out ./news_data

Typical daily run at 08:00 for yesterday's news:
    python gcores_news_to_pdf.py --preset yesterday --out ./news_data

The default date window is the last 7 days, ending at the current time.
You can also pin it explicitly:
    python gcores_news_to_pdf.py --since 2026-05-21 --until 2026-05-28
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from article_store import save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from urllib.parse import urljoin

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright


BASE = "https://www.gcores.com"
LIST_URL = f"{BASE}/news"
SOURCE_DOMAIN = "gcores.com"
SOURCE_KEY = "gcores"
PAGE_TIMEOUT = 30_000
PER_ARTICLE_DELAY = 2.0
MANIFEST_NAME = f"{SOURCE_DOMAIN}_manifest.json"
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


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    """Parse YYYY-MM-DD or ISO datetime as local naive time."""
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


def parse_gcores_list_time(value: str, now: datetime) -> datetime | None:
    text = value.strip()
    if not text:
        return None

    match = re.fullmatch(r"(\d+)\s*分钟前", text)
    if match:
        return now - timedelta(minutes=int(match.group(1)))
    match = re.fullmatch(r"(\d+)\s*小时前", text)
    if match:
        return now - timedelta(hours=int(match.group(1)))
    match = re.fullmatch(r"(\d+)\s*天前", text)
    if match:
        return now - timedelta(days=int(match.group(1)))

    if re.fullmatch(r"昨天(?:\s*\d{1,2}:\d{2})?", text):
        return now - timedelta(days=1)
    if re.fullmatch(r"前天(?:\s*\d{1,2}:\d{2})?", text):
        return now - timedelta(days=2)

    match = re.fullmatch(r"(\d{4})(?:-|/|年)(\d{1,2})(?:-|/|月)(\d{1,2})日?", text)
    if match:
        year, month, day = map(int, match.groups())
        return datetime(year, month, day)

    match = re.fullmatch(r"(\d{1,2})(?:-|/|月)(\d{1,2})日?", text)
    if match:
        month, day = map(int, match.groups())
        if not 1 <= month <= 12 or not 1 <= day <= 31:
            return None
        candidate = datetime(now.year, month, day)
        if candidate > now + timedelta(days=2):
            candidate = datetime(now.year - 1, month, day)
        return candidate

    return None


def parse_list_text(text: str, now: datetime) -> tuple[str, datetime | None]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "", None

    time_index = None
    published_at = None
    for index, line in enumerate(lines):
        parsed = parse_gcores_list_time(line, now)
        if parsed:
            time_index = index
            published_at = parsed
            break

    title_lines = lines[:time_index] if time_index is not None else lines[:1]
    title = " ".join(title_lines).strip()
    return title, published_at


def parse_article_datetime(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None

    normalized = text.replace("年", "-").replace("月", "-").replace("日", " ")
    normalized = re.sub(r"\s+", " ", normalized).strip()

    iso_match = re.search(
        r"\d{4}-\d{1,2}-\d{1,2}(?:[ T]\d{1,2}:\d{2}(?::\d{2})?)?(?:Z|[+-]\d{2}:?\d{2})?",
        normalized,
    )
    if not iso_match:
        return None

    raw = iso_match.group(0).replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.tzinfo:
        return parsed.astimezone().replace(tzinfo=None)
    return parsed


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
        return json.loads(path.read_text(encoding="utf-8"))
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
    tmp.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    tmp.replace(path)


async def collect_news_items(page, since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    """Collect list entries by paginating until entries are older than since."""
    items: list[NewsItem] = []
    seen: set[str] = set()

    for page_no in range(1, max_pages + 1):
        now = datetime.now().replace(microsecond=0)
        url = LIST_URL if page_no == 1 else f"{LIST_URL}?page={page_no}"
        print(f"[list] open {url}")
        await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.wait_for_load_state("networkidle", timeout=PAGE_TIMEOUT)

        try:
            await page.wait_for_selector('a[href*="/articles/"]', timeout=15_000)
        except PWTimeout:
            print("[list] no news links found; site structure may have changed", file=sys.stderr)
            break

        rows = await page.evaluate(
            """() => {
                const links = [...document.querySelectorAll('a[href*="/articles/"]')];
                return links.map(a => {
                    const href = a.getAttribute('href') || '';
                    const text = (a.innerText || a.textContent || '').trim();
                    return {
                        href,
                        text
                    };
                });
            }"""
        )

        page_new = 0
        older_count = 0
        for row in rows:
            href = row.get("href") or ""
            match = re.search(r"/articles/(\d+)", href)
            if not match:
                continue
            news_id = match.group(1)
            if news_id in seen:
                continue
            seen.add(news_id)

            title, published_local = parse_list_text(row.get("text") or "", now)
            if not published_local:
                continue

            if published_local >= until:
                continue
            if published_local < since:
                older_count += 1
                continue

            title = re.sub(r"\s+", " ", title)
            items.append(
                NewsItem(
                    news_id=news_id,
                    url=urljoin(BASE, href),
                    title=title or f"gcores-{news_id}",
                    published_at=published_local,
                )
            )
            page_new += 1

        print(f"[list] page {page_no}: +{page_new}, total {len(items)}")
        if older_count and page_new == 0:
            break

    items.sort(key=lambda x: x.published_at)
    return items


async def clean_page_for_pdf(page) -> None:
    await page.add_style_tag(
        content="""
            header, footer, nav, aside,
            [class*="comment"], [class*="Comment"],
            [class*="recommend"], [class*="Recommend"],
            [class*="share"], [class*="Share"],
            [class*="toolbar"], [class*="Toolbar"] {
                display: none !important;
            }
            body {
                background: #fff !important;
            }
            main, article {
                max-width: 820px !important;
                margin-left: auto !important;
                margin-right: auto !important;
            }
            img {
                max-width: 100% !important;
                height: auto !important;
            }
        """
    )


async def scroll_for_lazy_images(page) -> None:
    await page.evaluate(
        """async () => {
            const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
            const height = document.body.scrollHeight;
            for (let y = 0; y < height; y += 700) {
                window.scrollTo(0, y);
                await sleep(120);
            }
            window.scrollTo(0, 0);
        }"""
    )


async def fetch_article_page_meta(page) -> dict[str, str]:
    return await page.evaluate(
        """() => {
            const h1 = document.querySelector('h1');
            const time = document.querySelector('time');
            const content = (
                document.querySelector('article') ||
                document.querySelector('main') ||
                document.querySelector('[class*="original"]') ||
                document.body
            );
            return {
                title: h1 ? h1.innerText.trim() : '',
                published: time ? (time.getAttribute('datetime') || time.textContent || '').trim() : '',
                content_html: content ? content.innerHTML : '',
                content_text: content ? content.innerText.trim() : ''
            };
        }"""
    )


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
        await page.wait_for_selector('h1, article, main, [class*="original"]', timeout=15_000)
        page_meta = await fetch_article_page_meta(page)
        title = page_meta.get("title") or item.title
        page_published_at = parse_article_datetime(page_meta.get("published") or "")
        published_at = page_published_at or item.published_at
        date_part = published_at.strftime("%Y-%m-%d")
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
                    "text": page_meta.get("content_text") or "",
                    "html": page_meta.get("content_html") or "",
                    "published_at": published_at.isoformat(timespec="seconds"),
                    "extra": {
                        "list_published_at": item.published_at.isoformat(timespec="seconds"),
                        "page_published": page_meta.get("published") or "",
                    },
                },
            )
            save_manifest(out_dir, manifest)
            print(f"[{item.news_id}] saved text record")
            return True

        final_name = f"{SOURCE_DOMAIN}_{date_part}_{item.news_id}_{sanitize_filename(title)}.pdf"
        final_path = out_dir / final_name
        await scroll_for_lazy_images(page)
        await clean_page_for_pdf(page)
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
            "page_published": page_meta.get("published") or "",
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
    parser = argparse.ArgumentParser(description="Fetch Gcores news and save articles as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=8, help="Maximum list pages to scan")
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
        until = parse_date(args.until, end_of_day=False)
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


if __name__ == "__main__":
    asyncio.run(main())
