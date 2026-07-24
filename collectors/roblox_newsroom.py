"""Fetch full-text posts from the official Roblox Newsroom.

The newsroom is server-rendered, so the collector can discover article URLs and
extract their metadata/body with the Python standard library.  Records are
written through the shared article store used by the daily collector runner.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from article_store import html_to_text, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths


NEWSROOM_URL = "https://about.roblox.com/newsroom"
SOURCE_DOMAIN = "about.roblox.com"
SOURCE_KEY = "roblox_newsroom"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        try:
            with urlopen(request, timeout=HTTP_TIMEOUT) as response:
                # The site is UTF-8 HTML. Some edge responses advertise a
                # Latin-1-compatible default, which would mojibake curly quotes.
                return response.read().decode("utf-8-sig", "replace")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_exc = exc
            if isinstance(exc, HTTPError) and exc.code == 404:
                break
            if attempt < HTTP_RETRIES:
                print(f"[http] retry {attempt}/{HTTP_RETRIES}: {url} ({exc})", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"GET failed after {HTTP_RETRIES} tries: {url} ({last_exc!r})")


def parse_date(value: str) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return datetime.fromisoformat(raw)
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


def parse_published_at(value: str) -> datetime | None:
    try:
        published = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        return None
    if published.tzinfo is not None:
        published = published.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return published.replace(microsecond=0)


def meta_content(page_html: str, *, property_name: str = "", name: str = "") -> str:
    key = "property" if property_name else "name"
    value = property_name or name
    pattern = rf'<meta\b(?=[^>]*\b{key}=["\']{re.escape(value)}["\'])[^>]*\bcontent=["\']([^"\']*)["\'][^>]*>'
    match = re.search(pattern, page_html, re.I)
    if not match:
        # Attribute order is not guaranteed.
        pattern = rf'<meta\b(?=[^>]*\bcontent=["\']([^"\']*)["\'])[^>]*\b{key}=["\']{re.escape(value)}["\'][^>]*>'
        match = re.search(pattern, page_html, re.I)
    return html.unescape(match.group(1)).strip() if match else ""


def discover_article_urls(page_html: str) -> list[str]:
    paths = re.findall(r'href=["\'](/newsroom/\d{4}/\d{2}/[^"\'#?]+)["\']', page_html, re.I)
    seen: set[str] = set()
    urls: list[str] = []
    for path in paths:
        url = urljoin(NEWSROOM_URL, html.unescape(path)).rstrip("/")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def extract_body_html(page_html: str) -> str:
    sections = re.findall(
        r'<section\b[^>]*\bid=["\']section-text-[^"\']+["\'][^>]*>(.*?)</section>',
        page_html,
        re.I | re.S,
    )
    if not sections:
        return ""
    return "\n".join(sections)


def make_item_id(url: str) -> str:
    slug = urlparse(url).path.rstrip("/").split("/")[-1]
    clean = re.sub(r"\W+", "_", slug).strip("_") or "article"
    if len(clean) <= 56:
        return clean
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return f"{clean[:47].rstrip('_')}_{digest}"


def parse_article(url: str, page_html: str) -> dict | None:
    published_at = parse_published_at(meta_content(page_html, property_name="article:published_time"))
    title = meta_content(page_html, property_name="og:title")
    author = meta_content(page_html, property_name="article:author")
    body_html = extract_body_html(page_html)
    text = html_to_text(body_html)
    if not title or published_at is None or not text:
        return None
    return {
        "id": make_item_id(url),
        "url": url,
        "title": re.sub(r"\s*\|\s*Roblox\s*$", "", title, flags=re.I).strip(),
        "author": author,
        "published_at": published_at,
        "html": body_html,
        "text": text,
    }


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
    except (OSError, json.JSONDecodeError):
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch full-text posts from the Roblox Newsroom.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility; the newsroom is one server-rendered catalog page.")
    parser.add_argument("--headful", action="store_true", help="Unused; CLI compatibility.")
    args = parser.parse_args()

    since, until = preset_window(args.preset)
    if args.since:
        since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    print(f"[config] window: {since} <= published < {until}")
    print(f"[catalog] open {NEWSROOM_URL}")
    urls = discover_article_urls(fetch_text(NEWSROOM_URL))
    print(f"[catalog] discovered={len(urls)}")

    selected: list[dict] = []
    failures = 0
    for url in urls:
        try:
            article = parse_article(url, fetch_text(url))
        except RuntimeError as exc:
            failures += 1
            print(f"[article] failed: {url} ({exc})", file=sys.stderr)
            continue
        if article is None:
            failures += 1
            print(f"[article] missing metadata/body: {url}", file=sys.stderr)
            continue
        if since <= article["published_at"] < until:
            selected.append(article)

    selected.sort(key=lambda item: item["published_at"], reverse=True)
    if args.limit > 0:
        selected = selected[: args.limit]

    for article in selected:
        write_article_record(
            args.out,
            manifest,
            article["id"],
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "section": "industry_news",
                "title": article["title"],
                "url": article["url"],
                "author": article["author"],
                "text": article["text"],
                "html": article["html"],
                "published_at": article["published_at"].isoformat(timespec="seconds"),
                "extra": {"official_source": True},
            },
        )
        print(f"[{article['id']}] saved {article['published_at']:%Y-%m-%d} {article['title'][:60]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={len(selected)} failures={failures} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
