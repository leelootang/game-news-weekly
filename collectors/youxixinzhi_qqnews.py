"""
Fetch 游戏新知 articles from Tencent News (腾讯号) and export PDFs.

Discovery API:  https://i.news.qq.com/getSubNewsMixedList?guestSuid=8QIf3n5f74cYsT3e7gM%3D&...
Articles live at: new.qq.com/rain/a/[ID]

The collector queries the article-list JSON API directly (no browser rendering of
the author index page), paginates via the offsetInfo field until it finds articles
older than --since, then opens each article page with Playwright to extract the
body and export to PDF.
"""

from __future__ import annotations

import argparse
import asyncio
import html as html_mod
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright


# Author vendor ID (URL-encoded) found from the author page:
# https://news.qq.com/omn/author/8QIf3n5f74cYsT3e7gM=
AUTHOR_VID = "8QIf3n5f74cYsT3e7gM%3D"
LIST_API = (
    "https://i.news.qq.com/getSubNewsMixedList"
    f"?offset_info={{offset_info}}"
    f"&guestSuid={AUTHOR_VID}"
    "&tabId=om_index&caller=1&from_scene=103"
)
SOURCE_DOMAIN = "new.qq.com"
SOURCE_KEY = "youxixinzhi_qqnews"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 30_000
PER_ARTICLE_DELAY = 1.5
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


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

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


def make_article_url(article_id: str) -> str:
    return f"https://new.qq.com/rain/a/{article_id}"


def parse_api_time(value: str) -> datetime | None:
    """Parse 'YYYY-MM-DD HH:MM:SS' from the API time field."""
    text = value.strip()
    if not text:
        return None
    m = re.search(r"\d{4}-\d{1,2}-\d{1,2}(?:\s+\d{1,2}:\d{2}(?::\d{2})?)?", text)
    if not m:
        return None
    try:
        return datetime.fromisoformat(m.group(0))
    except ValueError:
        return None


def parse_unix_ts(value: str) -> datetime | None:
    text = value.strip()
    if re.fullmatch(r"\d{10}", text):
        try:
            return datetime.fromtimestamp(int(text))
        except (OSError, OverflowError):
            return None
    if re.fullmatch(r"\d{13}", text):
        try:
            return datetime.fromtimestamp(int(text) / 1000)
        except (OSError, OverflowError):
            return None
    return None


def parse_article_page_datetime(value: str) -> datetime | None:
    """Parse a publish date string extracted from the article page DOM."""
    text = value.strip()
    if not text:
        return None
    ts = parse_unix_ts(text)
    if ts:
        return ts
    # "YYYY年MM月DD日 HH:MM" or ISO variants
    normalized = text.replace("年", "-").replace("月", "-").replace("日", " ").strip()
    m = re.search(
        r"\d{4}-\d{1,2}-\d{1,2}(?:[ T]\d{1,2}:\d{2}(?::\d{2})?)?(?:Z|[+-]\d{2}:?\d{2})?",
        normalized,
    )
    if not m:
        return None
    raw = m.group(0).replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.tzinfo:
        return parsed.astimezone().replace(tzinfo=None)
    return parsed


# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------

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
        print(f"[manifest] broken, moved to {backup.name}", file=sys.stderr)
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


# ---------------------------------------------------------------------------
# Article list collection via API
# ---------------------------------------------------------------------------

async def fetch_api_page(page, offset_info: str) -> dict:
    """Fetch one page of the article list from the Tencent News JSON API."""
    url = LIST_API.format(offset_info=offset_info)
    print(f"[api] {url[:120]}")
    resp = await page.goto(url, wait_until="load", timeout=PAGE_TIMEOUT)
    if resp is None:
        raise RuntimeError("API page.goto returned None")
    ct = resp.headers.get("content-type", "")
    if "json" not in ct:
        body = await resp.body()
        raise RuntimeError(f"API returned non-JSON content-type={ct!r}: {body[:200]!r}")
    return await resp.json()


async def collect_news_items(
    page, since: datetime, until: datetime, max_pages: int
) -> list[NewsItem]:
    """
    Page through the JSON API until we find articles older than --since.
    Raises RuntimeError if we exhaust max_pages without reaching the boundary.
    """
    items: list[NewsItem] = []
    seen: set[str] = set()
    older_count = 0
    offset_info = ""

    for page_no in range(1, max_pages + 1):
        data = await fetch_api_page(page, offset_info)
        newslist = data.get("newslist") or []

        if not newslist:
            print(f"[list] page {page_no}: empty newslist")
            break

        page_new = 0
        for article in newslist:
            article_id = (article.get("id") or "").strip()
            if not article_id:
                continue

            title = re.sub(r"\s+", " ", article.get("title") or "").strip()
            raw_time = (article.get("time") or "").strip()
            ts_str = str(article.get("timestamp") or "").strip()

            published_at = parse_api_time(raw_time)
            if not published_at:
                published_at = parse_unix_ts(ts_str)

            if not title or not published_at:
                continue
            if article_id in seen:
                continue
            seen.add(article_id)

            article_url = make_article_url(article_id)

            if published_at >= until:
                continue
            if published_at < since:
                older_count += 1
                continue

            items.append(NewsItem(article_id, article_url, title, published_at, raw_time))
            page_new += 1

        has_next = bool(data.get("hasNext"))
        print(
            f"[list] page {page_no}: +{page_new} in-window, {older_count} older so far, hasNext={has_next}"
        )

        if older_count:
            break

        if not has_next:
            print("[list] API reports no more pages")
            break

        offset_info = data.get("offsetInfo") or ""
        if not offset_info:
            print("[list] no offsetInfo, cannot paginate further")
            break

    if not older_count:
        raise RuntimeError(
            f"Did not reach articles older than --since={since.date()} after "
            f"scanning {page_no} API page(s). Cannot prove completeness. "
            "Try --max-pages N (larger)."
        )

    print(f"[list] collected {len(items)} in-window article(s)")
    items.sort(key=lambda x: x.published_at)
    return items


# ---------------------------------------------------------------------------
# Article page content extraction
# ---------------------------------------------------------------------------

async def scroll_for_lazy_images(page) -> None:
    await page.evaluate(
        """async () => {
            const sleep = ms => new Promise(r => setTimeout(r, ms));
            for (let y = 0; y < document.body.scrollHeight; y += 700) {
                window.scrollTo(0, y);
                await sleep(100);
            }
            window.scrollTo(0, 0);
        }"""
    )


async def fetch_article_meta(page) -> dict[str, str]:
    """Extract title, published date, and body HTML from the article page."""
    return await page.evaluate(
        """() => {
            const txt = sel => {
                const el = document.querySelector(sel);
                return el ? (el.innerText || el.textContent || '').trim() : '';
            };

            // Title
            const title = (
                txt('h1.LEFT_TITLE') ||
                txt('.LEFT h1') ||
                txt('h1') ||
                txt('.article-title') ||
                ''
            );

            // Published date
            const published = (
                txt('.time-source') ||
                txt('.timeBox') ||
                txt('.LEFT .time') ||
                txt('.info-box .time') ||
                txt('time') ||
                txt('[class*="Time"]') ||
                ''
            );

            // Body content — try selectors from most to least specific
            const bodySelectors = [
                '.content-article',
                '.LEFT .article-content',
                '.Cnt-main-article-QQ',
                '#articleContent',
                '.article-content',
                '.content_article',
                '.article',
                'article',
            ];
            let content = null;
            for (const sel of bodySelectors) {
                const el = document.querySelector(sel);
                if (el && (el.innerText || '').trim().length > 80) {
                    content = el;
                    break;
                }
            }

            if (content) {
                content.querySelectorAll('img').forEach(img => {
                    const src = (
                        img.getAttribute('data-src') ||
                        img.getAttribute('data-original') ||
                        img.getAttribute('src') || ''
                    );
                    if (src) img.setAttribute('src', src);
                    img.removeAttribute('data-src');
                    img.removeAttribute('data-original');
                });
                content.querySelectorAll(
                    'script, iframe, .ad-wrap, .share-bar, ' +
                    '[class*="recommend"], [class*="Recommend"], ' +
                    '[class*="share"], [class*="Share"], ' +
                    '[class*="comment"], [class*="Comment"]'
                ).forEach(el => el.remove());
            }

            return {
                title,
                published,
                content_html: content ? content.innerHTML : '',
            };
        }"""
    )


def build_printable_html(title: str, published: str, content_html: str) -> str:
    safe_title = html_mod.escape(title)
    safe_meta = html_mod.escape(published)
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
      padding: 24px 10px 40px;
    }}
    h1 {{
      font-size: 26px;
      line-height: 1.35;
      margin: 0 0 12px;
      font-weight: 700;
    }}
    .meta {{
      color: #666;
      font-size: 14px;
      margin-bottom: 28px;
      border-bottom: 1px solid #eee;
      padding-bottom: 12px;
    }}
    img {{
      max-width: 100%;
      height: auto;
    }}
    p {{ margin: 0 0 1em; }}
    figure {{ margin: 1em 0; }}
  </style>
</head>
<body>
  <main>
    <h1>{safe_title}</h1>
    <div class="meta">游戏新知 · 腾讯号 &nbsp;|&nbsp; {safe_meta}</div>
    <article>{content_html}</article>
  </main>
</body>
</html>"""


# ---------------------------------------------------------------------------
# PDF export
# ---------------------------------------------------------------------------

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
        await page.goto(item.url, wait_until="load", timeout=PAGE_TIMEOUT)
        # Wait for the article body to appear; networkidle may never fire on QQ pages
        try:
            await page.wait_for_selector(
                "h1, .content-article, .LEFT, #articleContent, .article-content",
                timeout=15_000,
            )
        except PWTimeout:
            raise RuntimeError("article content selector did not appear within 15 s")

        await scroll_for_lazy_images(page)
        meta = await fetch_article_meta(page)

        if not meta.get("content_html"):
            raise RuntimeError("article body was empty after extraction")

        title = meta.get("title") or item.title
        page_published_at = parse_article_page_datetime(meta.get("published") or "")
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

        final_name = (
            f"{FILE_PREFIX}_{published_at:%Y-%m-%d}_{item.news_id}_"
            f"{sanitize_filename(title)}.pdf"
        )
        final_path = out_dir / final_name

        await page.set_content(
            build_printable_html(
                title,
                meta.get("published") or published_at.isoformat(sep=" ", timespec="minutes"),
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


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch 游戏新知 腾讯号 articles and save them as PDFs."
    )
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored when --since/--until are set.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. E.g. 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. E.g. 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=5, help="Max API pages to fetch for article list")
    parser.add_argument("--limit", type=int, default=0, help="Debug: max articles to export")
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

        api_page = await context.new_page()
        items = await collect_news_items(api_page, since, until, args.max_pages)
        await api_page.close()

        if args.limit > 0:
            items = items[: args.limit]
        print(f"[list] {len(items)} article(s) to export")

        ok = fail = 0
        for item in items:
            success = await save_article_pdf(context, item, args.out, manifest)
            if success:
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
