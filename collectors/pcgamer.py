"""
Fetch PC Gamer (pcgamer.com) articles from its full-text RSS feed.

PC Gamer exposes an RSS feed at https://www.pcgamer.com/rss/ whose <item>s carry
the title, article URL, RFC-822 pubDate, a <dc:creator> author, one or more
<category> tags and the COMPLETE article body as CDATA HTML in
<content:encoded>. A single HTTP GET therefore yields every recent article with
full text — no browser, no per-article fetch. The desktop UA below is used for
consistency with the other collectors.

PC Gamer is a high-volume English outlet (roughly 30–50 posts a day), so a daily
window can return dozens of items; that breadth is intentional — relevance
filtering happens downstream at the editorial/gloss stage, not here.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
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


FEED_URL = "https://www.pcgamer.com/rss/"
SOURCE_DOMAIN = "pcgamer.com"
SOURCE_KEY = "pcgamer"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
LOCAL_TZ = timezone(timedelta(hours=8))
CONTENT_NS = "{http://purl.org/rss/1.0/modules/content/}encoded"
DC_CREATOR = ("{https://purl.org/dc/elements/1.1/}creator", "{http://purl.org/dc/elements/1.1/}creator")
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str) -> str | None:
    last: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/rss+xml, application/xml, text/xml, */*",
            },
        )
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


def parse_pubdate(value: str) -> datetime | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if dt is None:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return dt.replace(microsecond=0)


def _text(elem: ET.Element | None) -> str:
    if elem is None or elem.text is None:
        return ""
    return elem.text.strip()


def _creator(item: ET.Element) -> str:
    for tag in DC_CREATOR:
        v = _text(item.find(tag))
        if v:
            return v
    return ""


def make_item_id(url: str) -> str:
    m = re.search(r"/([^/?#]+)/?$", url.rstrip("/"))
    slug = m.group(1) if m else url
    return re.sub(r"\W+", "-", slug).strip("-")[:80] or "unknown"


def parse_feed(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    channel = root.find("channel")
    if channel is None:
        return []
    out: list[dict] = []
    for item in channel.findall("item"):
        link = _text(item.find("link"))
        title = _text(item.find("title"))
        if not link or not title:
            continue
        enc = item.find(CONTENT_NS)
        body_html = enc.text if enc is not None and enc.text else (_text(item.find("description")))
        cats = [c.text.strip() for c in item.findall("category") if c.text and c.text.strip()]
        out.append(
            {
                "id": make_item_id(link),
                "url": link,
                "title": title,
                "author": _creator(item),
                "published_at": parse_pubdate(_text(item.find("pubDate"))),
                "html": body_html,
                "categories": cats,
            }
        )
    return out


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
    parser = argparse.ArgumentParser(description="Fetch PC Gamer articles from its RSS feed.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=1, help="Unused (feed is single-shot); CLI compatibility.")
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

    xml_text = http_get(FEED_URL)
    if not xml_text:
        raise SystemExit("failed to fetch feed")
    entries = parse_feed(xml_text)
    print(f"[feed] parsed {len(entries)} item(s)")

    in_window = []
    for e in entries:
        pub = e["published_at"]
        if pub is None or pub >= until or pub < since:
            continue
        in_window.append(e)
    in_window.sort(key=lambda x: x["published_at"])
    if args.limit > 0:
        in_window = in_window[: args.limit]
    print(f"[feed] in-window={len(in_window)}")

    ok = 0
    for e in in_window:
        text = html_to_text(e["html"])
        if not text:
            continue
        write_article_record(
            args.out,
            manifest,
            e["id"],
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": e["title"],
                "url": e["url"],
                "author": e["author"],
                "text": text,
                "html": e["html"],
                "published_at": e["published_at"].isoformat(timespec="seconds"),
                "extra": {"categories": e["categories"]},
            },
        )
        ok += 1
        print(f"[{e['id'][:40]}] saved  {e['published_at']:%Y-%m-%d}  {e['title'].strip()[:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
