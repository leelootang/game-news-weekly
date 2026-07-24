"""
Fetch Video Games Chronicle articles from the public WordPress RSS feed and export PDFs.

The feed exposes stable URLs, titles, authors, categories, images, and UTC
publication timestamps. Detail pages are opened for full article body extraction
before rendering a clean local PDF.
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

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from urllib.error import URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright


RSS_URL = "https://www.videogameschronicle.com/feed/"
BASE = "https://www.videogameschronicle.com"
SOURCE_DOMAIN = "videogameschronicle.com"
SOURCE_KEY = "vgc"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 30_000
PER_ARTICLE_DELAY = 0.8
EXCLUDED_PATH_PREFIXES = ("/guide/",)
EXCLUDED_CATEGORIES = {"guides", "guide"}
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
CONTENT_NS = "{http://purl.org/rss/1.0/modules/content/}"
DC_NS = "{http://purl.org/dc/elements/1.1/}"
_DIAGNOSTIC_EMITTED = False
_STRUCTURED_ENDPOINT_AVAILABLE: bool | None = None


@dataclass(frozen=True)
class NewsItem:
    news_id: str
    url: str
    title: str
    author: str
    categories: list[str]
    summary: str
    image_url: str
    published_at: datetime
    raw_published_at: str
    content_html: str = ""


class ArticleBlockedError(RuntimeError):
    """The detail endpoint returned an anti-bot/interstitial response."""

    def __init__(self, reason: str, diagnostic: dict[str, object]) -> None:
        super().__init__(reason)
        self.diagnostic = diagnostic


@dataclass(frozen=True)
class SaveResult:
    saved: bool
    body_status: str
    reason: str = ""


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


def make_news_id(url: str) -> str:
    parsed = urlparse(url)
    slug = parsed.path.strip("/").split("/")[-1]
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
                print(f"[rss] retry {attempt}/3 after VGC RSS error: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch VGC RSS: {url}: {last_exc}") from last_exc


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


def description_image(description: str) -> str:
    match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', description, re.I)
    return html.unescape(match.group(1)) if match else ""


def description_summary(description: str) -> str:
    without_img = re.sub(r"<img\b[^>]*>", "", description, flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", "", without_img)).strip()


def is_excluded_feed_item(url: str, categories: list[str]) -> bool:
    parsed = urlparse(url)
    if any(parsed.path.startswith(prefix) for prefix in EXCLUDED_PATH_PREFIXES):
        return True
    normalized_categories = {category.strip().lower() for category in categories}
    return bool(normalized_categories & EXCLUDED_CATEGORIES)


def clean_content_html(content_html: str) -> str:
    content_html = re.sub(r"<script\b[^>]*>.*?</script>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"<iframe\b[^>]*>.*?</iframe>", "", content_html, flags=re.I | re.S)
    content_html = re.sub(r"<style\b[^>]*>.*?</style>", "", content_html, flags=re.I | re.S)
    return content_html.strip()


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


def parse_manifest_datetime(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        return None


def prune_excluded_manifest_items(out_dir: Path, manifest: dict, since: datetime, until: datetime) -> None:
    items = manifest.setdefault("items", {})
    removed: list[str] = []
    for item_id, item in list(items.items()):
        url = item.get("url") or ""
        categories = item.get("categories") or []
        published_at = parse_manifest_datetime(item.get("published_at") or "")
        if not published_at or not (since <= published_at < until):
            continue
        if not is_excluded_feed_item(url, categories):
            continue
        file_name = item.get("file") or ""
        if file_name:
            stale_pdf = out_dir / file_name
            if stale_pdf.exists():
                stale_pdf.unlink()
        removed.append(str(item_id))
        items.pop(item_id, None)
    if removed:
        save_manifest(out_dir, manifest)
        print(f"[filter] removed {len(removed)} stale VGC guide item(s) from manifest/output")


def collect_feed_items(since: datetime, until: datetime, max_pages: int) -> list[NewsItem]:
    items: list[NewsItem] = []
    seen: set[str] = set()
    reached_older_boundary = False
    skipped_future = 0
    skipped_excluded = 0

    for page_no in range(1, max_pages + 1):
        feed_url = RSS_URL if page_no == 1 else f"{RSS_URL}?paged={page_no}"
        print(f"[rss] open {feed_url}")
        root = ET.fromstring(fetch_text(feed_url))
        nodes = root.findall("./channel/item")
        if not nodes:
            reached_older_boundary = True
            break

        page_new = 0
        page_older = 0
        for node in nodes:
            title = html.unescape(item_text(node, "title"))
            url = item_text(node, "link")
            raw_published = item_text(node, "pubDate")
            published_at = parse_rss_datetime(raw_published)
            if not url or not title or not published_at:
                continue
            news_id = make_news_id(url)
            if news_id in seen:
                continue
            seen.add(news_id)
            description = item_text(node, "description")
            categories = [child.text.strip() for child in node.findall("category") if child.text and child.text.strip()]
            if published_at >= until:
                skipped_future += 1
                continue
            if published_at < since:
                page_older += 1
                continue
            if is_excluded_feed_item(url, categories):
                skipped_excluded += 1
                continue
            items.append(
                NewsItem(
                    news_id=news_id,
                    url=url,
                    title=title,
                    author=item_text(node, f"{DC_NS}creator"),
                    categories=categories,
                    summary=description_summary(description) or description_summary(item_text(node, f"{CONTENT_NS}encoded")),
                    image_url=description_image(description),
                    published_at=published_at,
                    raw_published_at=raw_published,
                )
            )
            page_new += 1

        print(f"[rss] page {page_no}: +{page_new}, older={page_older}, total={len(items)}")
        if page_older:
            reached_older_boundary = True
            break

    print(
        f"[rss] collected {len(items)} article(s), "
        f"future_or_today={skipped_future}, excluded_guides={skipped_excluded}"
    )
    if not reached_older_boundary:
        raise RuntimeError(f"hit --max-pages={max_pages} before proving VGC RSS moved older than requested window")
    items.sort(key=lambda x: x.published_at)
    return items


async def fetch_article_content(context, item: NewsItem) -> NewsItem:
    page = await context.new_page()
    try:
        print(f"[{item.news_id}] open {item.url}")
        response = await page.goto(item.url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        status = response.status if response else None
        title = (await page.title()).strip()
        final_url = page.url
        challenge = (
            status in {401, 403, 429, 503}
            or "just a moment" in title.lower()
            or "__cf_chl_" in final_url
            or "cf-chl-" in (await page.locator("html").get_attribute("class") or "").lower()
        )
        if challenge:
            body_preview = re.sub(r"\s+", " ", (await page.locator("body").inner_text())[:240]).strip()
            diagnostic = {
                "kind": "blocked_cloudflare" if "__cf_chl_" in final_url or "just a moment" in title.lower() else "blocked_http",
                "status": status,
                "title": title[:120],
                "final_url": final_url[:500],
                "body_preview": body_preview,
            }
            raise ArticleBlockedError(str(diagnostic["kind"]), diagnostic)
        try:
            await page.wait_for_selector("#content_body, .post__content-body, article .entry-content, .entry-content", timeout=15_000)
        except PWTimeout as exc:
            raise RuntimeError("article content selector not found; source structure may have changed") from exc

        meta = await page.evaluate(
            """() => {
                const text = selector => document.querySelector(selector)?.innerText?.trim() || '';
                const title = text('article h1') || text('h1');
                const summary = text('.post__header-main p');
                const body = document.querySelector('#content_body') || document.querySelector('.post__content-body') || document.querySelector('article .entry-content') || document.querySelector('.entry-content');
                if (body) {
                    body.querySelectorAll('img').forEach(img => {
                        const src = img.getAttribute('data-src') || img.getAttribute('data-original') || img.getAttribute('src');
                        if (src) img.setAttribute('src', new URL(src, location.href).href);
                        img.removeAttribute('data-src');
                        img.removeAttribute('data-original');
                        img.removeAttribute('srcset');
                        img.removeAttribute('sizes');
                    });
                    body.querySelectorAll('script, iframe, style, .advert, .ad, .related-posts, [class*="share"], [class*="comment"], [class*="newsletter"]').forEach(el => el.remove());
                }
                return { title, summary, content_html: body ? body.innerHTML : '' };
            }"""
        )
        content_html = clean_content_html(meta.get("content_html") or "")
        if not content_html:
            raise RuntimeError("article content was empty")
        summary = html.escape(meta.get("summary") or item.summary)
        if summary:
            content_html = f'<p class="summary">{summary}</p>\n{content_html}'
        return NewsItem(
            news_id=item.news_id,
            url=item.url,
            title=meta.get("title") or item.title,
            author=item.author,
            categories=item.categories,
            summary=meta.get("summary") or item.summary,
            image_url=item.image_url,
            published_at=item.published_at,
            raw_published_at=item.raw_published_at,
            content_html=content_html,
        )
    finally:
        await page.close()


async def fetch_structured_content(context, item: NewsItem) -> NewsItem | None:
    """Try the public WordPress JSON endpoint once before falling back to RSS."""
    global _STRUCTURED_ENDPOINT_AVAILABLE
    if _STRUCTURED_ENDPOINT_AVAILABLE is False:
        return None
    slug = urlparse(item.url).path.strip("/").split("/")[-1]
    api_url = f"{BASE}/wp-json/wp/v2/posts?slug={slug}&_fields=title,excerpt,content"
    try:
        response = await context.request.get(api_url, timeout=PAGE_TIMEOUT, fail_on_status_code=False)
        if response.status != 200:
            if response.status in {401, 403, 429, 503}:
                _STRUCTURED_ENDPOINT_AVAILABLE = False
            return None
        payload = await response.json()
        if not isinstance(payload, list) or not payload:
            return None
        row = payload[0]
        content_html = clean_content_html(str((row.get("content") or {}).get("rendered") or ""))
        if not html_to_text(content_html):
            return None
        _STRUCTURED_ENDPOINT_AVAILABLE = True
        title = html_to_text(str((row.get("title") or {}).get("rendered") or "")) or item.title
        summary = html_to_text(str((row.get("excerpt") or {}).get("rendered") or "")) or item.summary
        return NewsItem(
            news_id=item.news_id, url=item.url, title=title, author=item.author,
            categories=item.categories, summary=summary, image_url=item.image_url,
            published_at=item.published_at, raw_published_at=item.raw_published_at,
            content_html=content_html,
        )
    except Exception as exc:
        print(f"[{item.news_id}] structured endpoint unavailable: {exc!r}", file=sys.stderr)
        return None


def emit_diagnostic_once(item: NewsItem, exc: Exception) -> None:
    global _DIAGNOSTIC_EMITTED
    if _DIAGNOSTIC_EMITTED:
        return
    if isinstance(exc, ArticleBlockedError):
        diagnostic = exc.diagnostic
    else:
        diagnostic = {
            "kind": "detail_retrieval_error",
            "error_type": type(exc).__name__,
            "message": str(exc)[:240],
            "url": item.url[:500],
        }
    print(f"[{item.news_id}] diagnostic {json.dumps(diagnostic, ensure_ascii=False)}", file=sys.stderr)
    _DIAGNOSTIC_EMITTED = True


def rss_fallback_html(item: NewsItem, reason: str) -> str:
    summary = html.escape(item.summary or "No RSS summary was supplied.")
    return (
        f'<p class="summary">{summary}</p>\n'
        f'<p><em>Full article retrieval unavailable ({html.escape(reason)}); '
        f'<a href="{html.escape(item.url)}">open the source article</a>.</em></p>'
    )


def write_text_record(out_dir: Path, manifest: dict, item: NewsItem, *, body_status: str,
                      fallback: str, reason: str = "") -> None:
    content_html = item.content_html if body_status == "full" else rss_fallback_html(item, reason)
    write_article_record(out_dir, manifest, item.news_id, {
        "source_key": SOURCE_KEY,
        "source": SOURCE_DOMAIN,
        "title": item.title,
        "url": item.url,
        "published_at": item.published_at.isoformat(timespec="seconds"),
        "author": item.author,
        "excerpt": item.summary,
        "text": html_to_text(content_html),
        "html": content_html,
        "fetch_status": "ok" if body_status == "full" else "partial",
        "body_status": body_status,
        "fallback": fallback,
        "extra": {
            "categories": item.categories,
            "image_url": item.image_url,
            "raw_published_at": item.raw_published_at,
            "retrieval_error": reason,
        },
    })
    save_manifest(out_dir, manifest)


def build_printable_html(item: NewsItem) -> str:
    title = html.escape(item.title)
    author = html.escape(item.author)
    categories = html.escape(", ".join(item.categories[:6]))
    published = html.escape(item.published_at.isoformat(sep=" ", timespec="minutes"))
    hero = f'<img class="hero" src="{html.escape(urljoin(BASE, item.image_url))}" alt="">' if item.image_url else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    body {{
      margin: 0;
      background: #fff;
      color: #111;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
      line-height: 1.68;
    }}
    main {{
      max-width: 820px;
      margin: 0 auto;
      padding: 24px 10px 44px;
    }}
    h1 {{
      font-size: 30px;
      line-height: 1.28;
      margin: 0 0 12px;
      font-weight: 750;
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
      font-size: 18px;
      font-weight: 600;
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
      padding-left: 16px;
      border-left: 4px solid #ddd;
      color: #333;
    }}
    figure {{
      margin: 0 0 1.2em;
    }}
    figcaption {{
      color: #777;
      font-size: 13px;
      line-height: 1.45;
      margin-top: 6px;
    }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">VGC {author} {categories} {published}</div>
    {hero}
    <article>{item.content_html}</article>
  </main>
</body>
</html>"""


async def save_article_pdf(context, item: NewsItem, out_dir: Path, manifest: dict) -> SaveResult:
    if not save_pdf_enabled():
        try:
            full_item = await fetch_article_content(context, item)
            write_text_record(out_dir, manifest, full_item, body_status="full", fallback="none")
            print(f"[{full_item.news_id}] saved text record")
            return SaveResult(True, "full")
        except Exception as exc:
            emit_diagnostic_once(item, exc)
            structured_item = await fetch_structured_content(context, item)
            if structured_item is not None:
                write_text_record(out_dir, manifest, structured_item, body_status="full", fallback="wordpress_json")
                print(f"[{item.news_id}] detail unavailable; saved structured endpoint record")
                return SaveResult(True, "full", repr(exc))
            reason = str(exc) or type(exc).__name__
            try:
                write_text_record(out_dir, manifest, item, body_status="rss_summary", fallback="rss_summary", reason=reason)
                print(f"[{item.news_id}] detail unavailable; saved RSS summary fallback")
                return SaveResult(True, "rss_summary", reason)
            except Exception as fallback_exc:
                print(f"[{item.news_id}] RSS fallback failed: {fallback_exc!r}", file=sys.stderr)
                return SaveResult(False, "empty", repr(fallback_exc))

    recorded = manifest.setdefault("items", {}).get(item.news_id)
    if recorded and recorded.get("data_file"):
        print(f"[{item.news_id}] already saved, skip")
        return SaveResult(True, recorded.get("body_status") or "full")
    if save_pdf_enabled() and recorded and recorded.get("file") and (out_dir / recorded["file"]).exists():
        print(f"[{item.news_id}] already saved, skip")
        return SaveResult(True, "full")

    page = await context.new_page()
    tmp_path = out_dir / f".tmp_{item.news_id}.pdf"
    try:
        full_item = await fetch_article_content(context, item)
        final_name = f"{FILE_PREFIX}_{full_item.published_at:%Y-%m-%d}_{full_item.news_id}_{sanitize_filename(full_item.title)}.pdf"
        final_path = out_dir / final_name

        print(f"[{full_item.news_id}] render {full_item.url}")
        await page.set_content(build_printable_html(full_item), wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.emulate_media(media="screen")
        await page.pdf(
            path=str(tmp_path),
            format="A4",
            print_background=True,
            margin={"top": "12mm", "right": "10mm", "bottom": "12mm", "left": "10mm"},
        )
        tmp_path.replace(final_path)

        manifest["items"][full_item.news_id] = {
            "file": final_name,
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "title": full_item.title,
            "url": full_item.url,
            "author": full_item.author,
            "categories": full_item.categories,
            "published_at": full_item.published_at.isoformat(timespec="seconds"),
            "raw_published_at": full_item.raw_published_at,
            "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        save_manifest(out_dir, manifest)
        print(f"[{full_item.news_id}] saved {final_name}")
        return SaveResult(True, "full")
    except Exception as exc:
        emit_diagnostic_once(item, exc)
        structured_item = await fetch_structured_content(context, item)
        body_status = "full" if structured_item is not None else "rss_summary"
        fallback_name = "wordpress_json" if structured_item is not None else "rss_summary"
        reason = str(exc) or type(exc).__name__
        render_item = structured_item or NewsItem(
            news_id=item.news_id, url=item.url, title=item.title, author=item.author,
            categories=item.categories, summary=item.summary, image_url=item.image_url,
            published_at=item.published_at, raw_published_at=item.raw_published_at,
            content_html=rss_fallback_html(item, reason),
        )
        try:
            final_name = f"{FILE_PREFIX}_{render_item.published_at:%Y-%m-%d}_{render_item.news_id}_{sanitize_filename(render_item.title)}.pdf"
            final_path = out_dir / final_name
            await page.set_content(build_printable_html(render_item), wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
            await page.emulate_media(media="screen")
            await page.pdf(
                path=str(tmp_path), format="A4", print_background=True,
                margin={"top": "12mm", "right": "10mm", "bottom": "12mm", "left": "10mm"},
            )
            tmp_path.replace(final_path)
            manifest["items"][render_item.news_id] = {
                "file": final_name, "source": SOURCE_DOMAIN, "source_key": SOURCE_KEY,
                "title": render_item.title, "url": render_item.url, "author": render_item.author,
                "categories": render_item.categories,
                "published_at": render_item.published_at.isoformat(timespec="seconds"),
                "raw_published_at": render_item.raw_published_at,
                "fetch_status": "ok" if body_status == "full" else "partial",
                "body_status": body_status, "fallback": fallback_name,
                "retrieval_error": reason,
                "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
            save_manifest(out_dir, manifest)
            print(f"[{item.news_id}] detail unavailable; saved {fallback_name} PDF fallback")
            return SaveResult(True, body_status, reason)
        except Exception as fallback_exc:
            print(f"[{item.news_id}] PDF fallback failed: {fallback_exc!r}", file=sys.stderr)
            if tmp_path.exists():
                tmp_path.unlink(missing_ok=True)
            return SaveResult(False, "empty", repr(fallback_exc))
    finally:
        await page.close()


async def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Video Games Chronicle articles and save them as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=20, help="Maximum RSS pages to scan")
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
    prune_excluded_manifest_items(args.out, manifest, since, until)

    items = collect_feed_items(since, until, args.max_pages)
    if args.limit > 0:
        items = items[: args.limit]
    print(f"[rss] selected {len(items)} article(s)")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not args.headful)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale="en-US",
            timezone_id="Asia/Shanghai",
            viewport={"width": 1280, "height": 900},
        )

        ok = 0
        full = 0
        fallback = 0
        fail = 0
        for item in items:
            result = await save_article_pdf(context, item, args.out, manifest)
            if result.saved:
                ok += 1
                if result.body_status == "full":
                    full += 1
                else:
                    fallback += 1
            else:
                fail += 1
            await asyncio.sleep(PER_ARTICLE_DELAY)

        await context.close()
        await browser.close()

    if fallback:
        print(f"[health] degraded reason=detail_unavailable full={full} rss_summary={fallback}")
    print(f"[done] ok={ok} full={full} fallback={fallback} fail={fail} output={args.out.resolve()}")
    if fail:
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())
