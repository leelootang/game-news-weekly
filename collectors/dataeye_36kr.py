"""
Fetch DataEye articles from its 36Kr author page and export PDFs.

The author page is protected by a JavaScript challenge and signs its API calls
in the browser, so this collector uses Playwright for list discovery. It does
not filter by topic; DataEye posts about games, short drama, AI video, and ads
are all collected for later AI-side filtering.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from urllib.error import URLError
from urllib.request import Request, urlopen

from playwright.async_api import async_playwright


AUTHOR_URL = "https://36kr.com/user/15154927"
ARTICLE_LIST_API = "https://gateway.36kr.com/api/mis/me/article"
BASE = "https://36kr.com"
SOURCE_DOMAIN = "36kr.com"
SOURCE_KEY = "dataeye_36kr"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 45_000
PER_ARTICLE_DELAY = 1.0
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
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
    summary: str
    image_url: str
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


def sanitize_filename(name: str, max_len: int = 70) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:max_len].rstrip(" .") or "untitled"


def parse_publish_ms(value: object) -> datetime | None:
    try:
        ts = int(value)
    except (TypeError, ValueError):
        return None
    if ts <= 0:
        return None
    if ts > 10_000_000_000:
        ts = ts / 1000
    return datetime.fromtimestamp(ts, LOCAL_TZ).replace(tzinfo=None)


def parse_article_page_datetime(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None
    normalized = text.replace("年", "-").replace("月", "-").replace("日", " ")
    match = re.search(r"\d{4}-\d{1,2}-\d{1,2}(?:\s+\d{1,2}:\d{2})?", normalized)
    if not match:
        return None
    try:
        return datetime.fromisoformat(match.group(0))
    except ValueError:
        return None


def article_url(item_id: str) -> str:
    return f"{BASE}/p/{item_id}"


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


def items_from_api_payload(data: dict) -> tuple[list[NewsItem], bool]:
    payload = data.get("data") or {}
    result: list[NewsItem] = []
    for row in payload.get("itemList") or []:
        material = row.get("templateMaterial") or {}
        item_id = str(material.get("itemId") or row.get("itemId") or "").strip()
        title = re.sub(r"\s+", " ", material.get("widgetTitle") or "").strip()
        published_at = parse_publish_ms(material.get("publishTime"))
        if not item_id or not title or not published_at:
            continue
        result.append(
            NewsItem(
                news_id=item_id,
                url=article_url(item_id),
                title=title,
                summary=re.sub(r"\s+", " ", material.get("widgetContent") or "").strip(),
                image_url=material.get("widgetImage") or "",
                published_at=published_at,
                raw_published_at=str(material.get("publishTime") or ""),
            )
        )
    return result, bool(payload.get("hasNextPage"))


def fetch_json(url: str, body: dict) -> dict:
    request = Request(
        url,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
            "Origin": BASE,
            "Referer": AUTHOR_URL,
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8-sig"))
    except (OSError, URLError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"failed to fetch DataEye 36Kr API: {exc}") from exc


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,*/*",
            "Referer": AUTHOR_URL,
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8-sig")
    except (OSError, URLError, UnicodeDecodeError) as exc:
        raise RuntimeError(f"failed to fetch DataEye 36Kr article page: {url}: {exc}") from exc


def fetch_api_page(page_callback: str, page_event: int) -> dict:
    body = {
        "nonce": "codex-dataeye-36kr",
        "partner_id": "web",
        "timestamp": int(time.time() * 1000),
        "param": {
            "userId": "15154927",
            "pageEvent": page_event,
            "pageSize": 20,
            "pageCallback": page_callback,
            "siteId": 1,
            "platformId": 2,
        },
    }
    return fetch_json(ARTICLE_LIST_API, body)


def collect_news_items(since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    items: dict[str, NewsItem] = {}
    seen: set[str] = set()
    reached_older_boundary = False
    page_callback = ""

    has_next = True
    for page_no in range(1, max_pages + 1):
        print(f"[list] fetch API page {page_no}")
        data = fetch_api_page(page_callback, 0 if page_no == 1 else 1)

        page_items, has_next = items_from_api_payload(data)
        page_callback = (data.get("data") or {}).get("pageCallback") or ""
        page_new = 0
        page_older = 0
        for item in page_items:
            if item.news_id in seen:
                continue
            seen.add(item.news_id)
            if item.published_at >= until:
                continue
            if item.published_at < since:
                page_older += 1
                continue
            items[item.news_id] = item
            page_new += 1

        print(
            f"[list] page {page_no}: +{page_new}, older={page_older}, "
            f"hasNext={has_next}, total={len(items)}"
        )
        if page_older:
            reached_older_boundary = True
            break
        if not has_next:
            reached_older_boundary = True
            break

    if not reached_older_boundary:
        raise RuntimeError(
            f"hit --max-pages={max_pages} before proving DataEye 36Kr moved older than requested window"
        )

    return sorted(items.values(), key=lambda x: (x.published_at, x.news_id))


async def scroll_for_lazy_images(page) -> None:
    await page.evaluate(
        """async () => {
            const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
            for (let y = 0; y < document.body.scrollHeight; y += 700) {
                window.scrollTo(0, y);
                await sleep(100);
            }
            window.scrollTo(0, 0);
        }"""
    )


async def fetch_article_meta(page) -> dict[str, str]:
    return await page.evaluate(
        """() => {
            const text = selector => {
                const el = document.querySelector(selector);
                return el ? (el.innerText || el.textContent || '').trim() : '';
            };
            const content = (
                document.querySelector('.articleDetailContent') ||
                document.querySelector('.kr-rich-text-wrapper') ||
                document.querySelector('.article-content article') ||
                document.querySelector('article')
            );
            if (content) {
                content.querySelectorAll('img').forEach(img => {
                    const src = img.getAttribute('data-src') || img.getAttribute('data-original') || img.getAttribute('src');
                    if (src) img.setAttribute('src', new URL(src, location.href).href);
                    img.removeAttribute('data-src');
                    img.removeAttribute('data-original');
                    img.removeAttribute('srcset');
                    img.removeAttribute('sizes');
                });
                content.querySelectorAll(
                    'script, iframe, style, .advert, .ad, [class*="share"], [class*="comment"], [class*="recommend"]'
                ).forEach(el => el.remove());
            }
            return {
                title: text('.article-title') || text('h1'),
                author: text('.title-icon-item.item-a') || text('a[href^="/user/"]'),
                published: text('.title-icon-item.item-time') || text('time'),
                summary: text('.summary'),
                content_html: content ? content.innerHTML : ''
            };
        }"""
    )


def build_printable_html(item: NewsItem, title: str, author: str, published: str, summary: str, content_html: str) -> str:
    safe_title = html.escape(title)
    safe_author = html.escape(author or "DataEye")
    safe_published = html.escape(published)
    safe_summary = html.escape(summary or item.summary)
    hero = f'<img class="hero" src="{html.escape(item.image_url)}" alt="">' if item.image_url else ""
    summary_html = f'<p class="summary">{safe_summary}</p>' if safe_summary else ""
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
      line-height: 1.75;
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
      margin-bottom: 24px;
    }}
    .hero {{
      display: block;
      width: 100%;
      max-height: 430px;
      object-fit: contain;
      margin: 0 0 24px;
    }}
    .summary {{
      color: #444;
      font-size: 17px;
      font-weight: 600;
      margin-bottom: 24px;
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
    <div class="meta">36氪 · {safe_author} · {safe_published}</div>
    {hero}
    {summary_html}
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
        print(f"[{item.news_id}] fetch {item.url}")
        source_html = fetch_text(item.url)
        await page.set_content(source_html, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.wait_for_selector(".articleDetailContent, .article-title, .kr-rich-text-wrapper", timeout=PAGE_TIMEOUT)
        await scroll_for_lazy_images(page)
        meta = await fetch_article_meta(page)
        if not meta.get("content_html"):
            raise RuntimeError("article content was empty")

        title = item.title or meta.get("title") or item.news_id
        page_published_at = parse_article_page_datetime(meta.get("published") or "")
        published_at = page_published_at or item.published_at
        if not save_pdf_enabled():
            text = html_to_text(meta["content_html"])
            write_article_record(
                out_dir,
                manifest,
                item.news_id,
                {
                    "source": SOURCE_DOMAIN,
                    "source_key": SOURCE_KEY,
                    "title": title,
                    "url": item.url,
                    "author": meta.get("author") or "DataEye",
                    "excerpt": item.summary or meta.get("summary") or "",
                    "text": text,
                    "html": meta["content_html"],
                    "published_at": published_at.isoformat(timespec="seconds"),
                    "extra": {
                        "list_published_at": item.published_at.isoformat(timespec="seconds"),
                        "raw_published_at": item.raw_published_at,
                        "page_published": meta.get("published") or "",
                        "image_url": item.image_url,
                    },
                },
            )
            save_manifest(out_dir, manifest)
            print(f"[{item.news_id}] saved text record")
            return True

        final_name = f"{FILE_PREFIX}_{published_at:%Y-%m-%d}_{item.news_id}_{sanitize_filename(title)}.pdf"
        final_path = out_dir / final_name

        await page.set_content(
            build_printable_html(
                item,
                title,
                meta.get("author") or "DataEye",
                meta.get("published") or published_at.isoformat(sep=" ", timespec="minutes"),
                item.summary or meta.get("summary") or "",
                meta["content_html"],
            ),
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
            "author": meta.get("author") or "DataEye",
            "summary": item.summary or meta.get("summary") or "",
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
    parser = argparse.ArgumentParser(description="Fetch DataEye 36Kr articles and save them as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=3, help="Maximum author-list pages to scan")
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

        items = collect_news_items(since, until, args.max_pages)
        if args.limit > 0:
            items = items[: args.limit]
        print(f"[list] selected {len(items)} article(s)")

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
