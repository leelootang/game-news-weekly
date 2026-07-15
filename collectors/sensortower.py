"""
Fetch Sensor Tower 中文博客 (sensortower.com/zh-CN/blog) market-intelligence posts.

Sensor Tower's site is a client-rendered Next.js/MUI app: the blog listing loads
its post list via a client-side API, so there is no server-rendered index and no
RSS feed. But the site publishes a sitemap. The Chinese blog sitemap at
https://sensortower.com/zh-CN-blog-sitemap.xml enumerates every post URL with a
<lastmod> timestamp, and each article PAGE *is* server-rendered — the body lives
in a `…-Blog-blogBodyRoot` container and the title in og:title / <h1>. So this
collector reads the sitemap for the recent post list (windowing on <lastmod>),
then opens each in-window post to pull its title and full text. urllib + regex.

Sensor Tower publishes at a low, report-driven cadence (a handful of posts per
month: monthly Top-10 charts, State-of reports, China market breakdowns), so a
typical daily window yields zero or one item — that is expected, not a failure.
"""

from __future__ import annotations

import argparse
import html as _html
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from article_store import html_to_text, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


SITEMAP_URL = "https://sensortower.com/zh-CN-blog-sitemap.xml"
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
SOURCE_DOMAIN = "sensortower.com"
SOURCE_KEY = "sensortower"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
PER_ARTICLE_DELAY = 0.5
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str) -> str | None:
    last: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "zh-CN,zh;q=0.9"})
        try:
            with urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                return resp.read().decode("utf-8", "replace")
        except HTTPError as exc:
            last = exc
            if exc.code == 404:
                return None
        except (URLError, TimeoutError) as exc:
            last = exc
        if attempt < HTTP_RETRIES:
            time.sleep(1.2 * attempt)
    print(f"[warn] GET failed: {url} ({last!r})", file=sys.stderr)
    return None


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        dt = datetime.fromisoformat(raw)
        return dt + timedelta(days=1) if end_of_day else dt
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


def parse_lastmod(value: str) -> datetime | None:
    raw = (value or "").strip()
    if not raw:
        return None
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        m = re.match(r"(\d{4}-\d{2}-\d{2})", raw)
        return datetime.fromisoformat(m.group(1)) if m else None
    if dt.tzinfo is not None:
        dt = dt.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return dt.replace(microsecond=0)


def extract_balanced_div(html_text: str, classname: str) -> str:
    m = re.search(r'<div[^>]*class="[^"]*\b' + re.escape(classname) + r'\b[^"]*"[^>]*>', html_text)
    if not m:
        return ""
    start = m.end()
    depth = 1
    for mm in re.finditer(r"<(/?)div\b", html_text[start:]):
        depth += -1 if mm.group(1) else 1
        if depth == 0:
            return html_text[start:start + mm.start()]
    return html_text[start:]


def parse_sitemap(xml_text: str) -> list[tuple[str, datetime | None]]:
    root = ET.fromstring(xml_text)
    out: list[tuple[str, datetime | None]] = []
    for u in root.findall(SITEMAP_NS + "url"):
        loc = u.findtext(SITEMAP_NS + "loc")
        if not loc:
            continue
        out.append((loc.strip(), parse_lastmod(u.findtext(SITEMAP_NS + "lastmod") or "")))
    return out


def extract_title(html_text: str) -> str:
    m = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', html_text)
    if not m:
        m = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]*property=["\']og:title["\']', html_text)
    if m:
        return _html.unescape(m.group(1)).strip()
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html_text, re.S)
    return _html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else ""


def make_item_id(url: str) -> str:
    m = re.search(r"/blog/([^/?#]+)", url)
    slug = m.group(1) if m else url
    return re.sub(r"\W+", "-", slug).strip("-")[:80] or "unknown"


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
    except Exception:
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Sensor Tower 中文博客 posts.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=1, help="Unused (sitemap is single-shot); CLI compatibility.")
    parser.add_argument("--headful", action="store_true", help="Unused; CLI compatibility.")
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

    sm = http_get(SITEMAP_URL)
    if not sm:
        raise SystemExit("failed to fetch sitemap")
    entries = parse_sitemap(sm)
    print(f"[sitemap] {len(entries)} post URL(s)")

    in_window = [(loc, lm) for loc, lm in entries if lm is not None and since <= lm < until]
    in_window.sort(key=lambda x: x[1])
    print(f"[sitemap] in-window={len(in_window)}")

    ok = 0
    for loc, lm in in_window:
        if args.limit and ok >= args.limit:
            break
        page = http_get(loc)
        time.sleep(PER_ARTICLE_DELAY)
        if not page:
            continue
        body_html = extract_balanced_div(page, "blogBodyRoot")
        text = html_to_text(body_html)
        title = extract_title(page)
        if not title or not text:
            continue
        item_id = make_item_id(loc)
        write_article_record(
            args.out,
            manifest,
            item_id,
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": title,
                "url": loc,
                "author": "Sensor Tower",
                "text": text,
                "html": body_html,
                "published_at": lm.isoformat(timespec="seconds"),
            },
        )
        ok += 1
        print(f"[{item_id}] saved  {lm:%Y-%m-%d}  {title[:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
