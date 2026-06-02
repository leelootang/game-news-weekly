"""
Fetch AI HOT selected AI news and export linked source pages to PDFs.

AI HOT's public RSS feed is used for discovery, timestamps, summaries, and
source attribution. Each item links to an external source page; this collector
opens that linked page and prints it to PDF. If a source page is blocked or
unreadable, it falls back to a compact AI HOT summary PDF and records the
fallback mode in the manifest.
"""

from __future__ import annotations

import argparse
import asyncio
import gzip
import hashlib
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

from article_store import save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright


RSS_URL = "https://aihot.virxact.com/feed.xml"
DAILY_URL_TEMPLATE = "https://aihot.virxact.com/daily/{date}"
SOURCE_DOMAIN = "aihot.virxact.com"
SOURCE_KEY = "aihot"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 35_000
PER_ARTICLE_DELAY = 0.8
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
DAILY_ARTICLE_RE = re.compile(
    r'<article class="daily-article">.*?'
    r'<h3 class="daily-article-title"><a href="(?P<url>[^"]+)"[^>]*>(?P<title>.*?)</a></h3>.*?'
    r'<div class="daily-article-source">(?P<source>.*?)</div>.*?'
    r'<p class="daily-article-summary">(?P<summary>.*?)</p>.*?'
    r"</article>",
    re.S,
)
HTML_TAG_RE = re.compile(r"<[^>]+>")


@dataclass(frozen=True)
class NewsItem:
    news_id: str
    url: str
    title: str
    summary: str
    source_name: str
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


def make_news_id(url: str, guid: str) -> str:
    if guid:
        return re.sub(r"\W+", "_", guid).strip("_")[:80]
    parsed = urlparse(url)
    slug = parsed.path.strip("/").split("/")[-1] or parsed.netloc
    clean_slug = re.sub(r"\W+", "_", slug).strip("_") or "unknown"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    if len(clean_slug) <= 48:
        return clean_slug
    return f"{clean_slug[:48].rstrip('_')}_{digest}"


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml,text/xml,*/*",
            "Accept-Encoding": "gzip",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )
    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            with urlopen(request, timeout=30) as response:
                raw = response.read()
                if response.headers.get("content-encoding", "").lower() == "gzip":
                    raw = gzip.decompress(raw)
                return raw.decode("utf-8-sig")
        except (OSError, URLError, UnicodeDecodeError) as exc:
            last_exc = exc
            if attempt < 3:
                print(f"[rss] retry {attempt}/3 after AI HOT RSS error: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch AI HOT RSS: {url}: {last_exc}") from last_exc


def parse_rss_datetime(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    try:
        dt = parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None
    if dt.tzinfo:
        return dt.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return dt


def item_text(item: ET.Element, tag: str) -> str:
    node = item.find(tag)
    return node.text.strip() if node is not None and node.text else ""


def clean_html_text(value: str) -> str:
    text = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    text = HTML_TAG_RE.sub(" ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def parse_author_source(author: str) -> str:
    match = re.search(r"\((.+)\)\s*$", author.strip())
    return match.group(1).strip() if match else author.strip()


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


def collect_feed_items(since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    if max_pages != 1:
        print("[rss] AI HOT selected feed is a single feed; --max-pages is accepted for runner compatibility")

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
        author = item_text(node, "author")
        items.append(
            NewsItem(
                news_id=make_news_id(url, item_text(node, "guid")),
                url=url,
                title=html.unescape(title),
                summary=html.unescape(item_text(node, "description")),
                source_name=parse_author_source(author),
                published_at=published_at,
                raw_published_at=raw_published,
            )
        )

    print(f"[rss] collected {len(items)} article(s), older={older}, future_or_today={skipped_future}")
    if not older:
        print(
            "[rss] warning: AI HOT RSS did not include an item older than --since; "
            "collecting the visible feed window only"
        )
    items.sort(key=lambda x: x.published_at)
    return items


def collect_daily_page_items(day: datetime) -> list[NewsItem]:
    day_str = day.strftime("%Y-%m-%d")
    url = DAILY_URL_TEMPLATE.format(date=day_str)
    print(f"[daily] open {url}")
    page_html = fetch_text(url)
    items: list[NewsItem] = []
    for index, match in enumerate(DAILY_ARTICLE_RE.finditer(page_html), start=1):
        item_url = html.unescape(match.group("url"))
        title = clean_html_text(match.group("title"))
        source_name = clean_html_text(match.group("source"))
        summary = clean_html_text(match.group("summary")) or "AI HOT日报条目，原站未提供摘要。"
        if not item_url or not title:
            continue
        items.append(
            NewsItem(
                news_id=make_news_id(item_url, f"aihot-daily-{day_str}-{index:02d}"),
                url=item_url,
                title=title,
                summary=summary,
                source_name=source_name,
                published_at=day.replace(hour=8, minute=0, second=0, microsecond=0),
                raw_published_at=day_str,
            )
        )
    print(f"[daily] collected {len(items)} article(s)")
    return items


async def cleanup_external_page(page) -> None:
    await page.add_style_tag(
        content="""
            nav, header, footer, aside,
            [class*="cookie"], [id*="cookie"],
            [class*="advert"], [class*="Advertisement"], [class*="ad-"],
            [class*="share"], [class*="Share"],
            [class*="comment"], [class*="Comment"],
            [class*="newsletter"], [class*="subscribe"],
            [class*="related"], [class*="recommend"] {
                display: none !important;
            }
            body {
                background: #fff !important;
            }
            article, main {
                max-width: 920px !important;
                margin-left: auto !important;
                margin-right: auto !important;
            }
            img, video {
                max-width: 100% !important;
                height: auto !important;
            }
        """
    )


async def scroll_for_lazy_images(page) -> None:
    await page.evaluate(
        """async () => {
            const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
            for (let y = 0; y < document.body.scrollHeight; y += 800) {
                window.scrollTo(0, y);
                await sleep(100);
            }
            window.scrollTo(0, 0);
        }"""
    )


def build_fallback_html(item: NewsItem, reason: str) -> str:
    title = html.escape(item.title)
    summary = html.escape(item.summary)
    source_name = html.escape(item.source_name)
    url = html.escape(item.url)
    published = html.escape(item.published_at.isoformat(sep=" ", timespec="minutes"))
    reason_text = html.escape(reason)
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
      padding: 24px 10px 44px;
    }}
    h1 {{
      font-size: 28px;
      line-height: 1.35;
      margin: 0 0 12px;
    }}
    .meta, .fallback {{
      color: #666;
      font-size: 14px;
      margin-bottom: 20px;
    }}
    .summary {{
      font-size: 17px;
      font-weight: 600;
    }}
    a {{
      color: #0645ad;
      word-break: break-all;
    }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">AI HOT · {source_name} · {published}</div>
    <p class="summary">{summary}</p>
    <p>原文链接：<a href="{url}">{url}</a></p>
    <p class="fallback">外部网页 PDF 抓取失败，已用 AI HOT 摘要兜底。原因：{reason_text}</p>
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

    if not save_pdf_enabled():
        text = "\n".join(
            part
            for part in [
                item.title,
                f"Source: {item.source_name}" if item.source_name else "",
                f"Original URL: {item.url}",
                item.summary,
            ]
            if part
        )
        write_article_record(
            out_dir,
            manifest,
            item.news_id,
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": item.title,
                "url": item.url,
                "author": item.source_name,
                "excerpt": item.summary,
                "text": text,
                "published_at": item.published_at.isoformat(timespec="seconds"),
                "fallback": "source_excerpt",
                "extra": {
                    "source_name": item.source_name,
                    "raw_published_at": item.raw_published_at,
                },
            },
        )
        save_manifest(out_dir, manifest)
        print(f"[{item.news_id}] saved text record")
        return True

    page = await context.new_page()
    tmp_path = out_dir / f".tmp_{item.news_id}.pdf"
    render_mode = "external_page"
    failure_reason = ""
    try:
        final_name = f"{FILE_PREFIX}_{item.published_at:%Y-%m-%d}_{item.news_id}_{sanitize_filename(item.title)}.pdf"
        final_path = out_dir / final_name

        try:
            print(f"[{item.news_id}] open external {item.url}")
            await page.goto(item.url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
            await page.wait_for_timeout(1800)
            body_text = await page.locator("body").inner_text(timeout=5_000)
            if len(body_text.strip()) < 80:
                raise RuntimeError("external page body too short")
            await scroll_for_lazy_images(page)
            await cleanup_external_page(page)
            await page.emulate_media(media="screen")
        except Exception as exc:
            render_mode = "summary_fallback"
            failure_reason = repr(exc)
            print(f"[{item.news_id}] external failed, fallback to summary: {failure_reason}", file=sys.stderr)
            await page.set_content(build_fallback_html(item, failure_reason), wait_until="domcontentloaded")

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
            "source_name": item.source_name,
            "summary": item.summary,
            "render_mode": render_mode,
            "fallback_reason": failure_reason,
            "published_at": item.published_at.isoformat(timespec="seconds"),
            "raw_published_at": item.raw_published_at,
            "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        save_manifest(out_dir, manifest)
        print(f"[{item.news_id}] saved {final_name} ({render_mode})")
        return True
    except Exception as exc:
        print(f"[{item.news_id}] failed: {exc!r}", file=sys.stderr)
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
        return False
    finally:
        await page.close()


async def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch AI HOT selected AI news and save linked pages as PDFs.")
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
    print(f"[config] window: {since} <= published < {until}")
    print(f"[config] output: {args.out.resolve()}")

    try:
        items = collect_feed_items(since, until, args.max_pages)
    except RuntimeError as exc:
        if until == since + timedelta(days=1):
            print(f"[daily] RSS failed ({exc}); trying AI HOT historical daily page")
            items = collect_daily_page_items(since)
        else:
            raise
    if not items and args.since and args.until and until == since + timedelta(days=1):
        print("[daily] RSS had no in-window items; trying AI HOT historical daily page")
        items = collect_daily_page_items(since)
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
