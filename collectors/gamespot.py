"""
Fetch GameSpot (gamespot.com) news from its public RSS feed.

GameSpot's HTML pages return HTTP 403 to plain HTTP clients (bot protection), but the
news RSS feed at https://www.gamespot.com/feeds/news/ serves fine to urllib: ~30 items
with title, permalink, RFC-822 pubDate and a <description> summary. The feed carries
summaries (not full <content:encoded>), and detail pages are 403-gated, so this collector
ingests the RSS summary as the record body (headline + summary + link). That's
summary-level, which is enough to surface the story; downstream tagging/editorial curate.

Records go to the flat root articles.jsonl via write_article_record, keyed by URL slug/guid.
"""

from __future__ import annotations

import argparse
import hashlib
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


FEED_URL = "https://www.gamespot.com/feeds/news/"
SOURCE_DOMAIN = "gamespot.com"
SOURCE_KEY = "gamespot"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
LOCAL_TZ = timezone(timedelta(hours=8))
CONTENT_NS = "{http://purl.org/rss/1.0/modules/content/}encoded"
CREATOR_NS = "{http://purl.org/dc/elements/1.1/}creator"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str) -> str:
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/xml, text/xml, */*"})
        try:
            with urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                return resp.read().decode("utf-8", "replace")
        except HTTPError as exc:
            last_exc = exc
            if exc.code == 404:
                break
        except (URLError, TimeoutError) as exc:
            last_exc = exc
        if attempt < HTTP_RETRIES:
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"GET failed after {HTTP_RETRIES} tries: {url} ({last_exc!r})")


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


def make_item_id(url: str, guid: str) -> str:
    for candidate in (guid, url):
        if not candidate:
            continue
        m = re.search(r"/(\d{7,})/?", candidate)
        if m:
            return m.group(1)
    slug = re.sub(r"^https?://[^/]+/", "", url).strip("/")
    clean = re.sub(r"\W+", "_", slug).strip("_")
    if not clean:
        return hashlib.sha1((guid or url).encode("utf-8")).hexdigest()[:12]
    if len(clean) <= 48:
        return clean
    return f"{clean[:40].rstrip('_')}_{hashlib.sha1(url.encode('utf-8')).hexdigest()[:8]}"


def load_manifest(out_dir: Path) -> dict:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME):
        if not path.exists() and legacy_path.exists():
            path = legacy_path
            break
    if not path.exists():
        return {"items": {}}
    try:
        import json
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    import json
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def _text(elem: ET.Element | None) -> str:
    if elem is None or elem.text is None:
        return ""
    return elem.text.strip()


def parse_feed(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    channel = root.find("channel")
    items = channel.findall("item") if channel is not None else root.findall("item")
    out: list[dict] = []
    for item in items:
        link = _text(item.find("link"))
        title = _text(item.find("title"))
        if not link or not title:
            continue
        published = parse_pubdate(_text(item.find("pubDate")))
        author = _text(item.find(CREATOR_NS)) or _text(item.find("author"))
        content_elem = item.find(CONTENT_NS)
        body_html = content_elem.text if (content_elem is not None and content_elem.text) else ""
        if not body_html:
            desc = item.find("description")
            body_html = desc.text if desc is not None and desc.text else ""
        guid = _text(item.find("guid"))
        out.append({
            "id": make_item_id(link, guid),
            "url": link,
            "title": title,
            "published_at": published,
            "author": author,
            "html": body_html,
        })
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch GameSpot news from its RSS feed.")
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
    print(f"[config] output: {args.out.resolve()}")

    xml_text = http_get(FEED_URL)
    entries = parse_feed(xml_text)
    print(f"[feed] parsed {len(entries)} item(s) from {FEED_URL}")

    in_window = []
    skipped_nodate = 0
    for e in entries:
        pub = e["published_at"]
        if pub is None:
            skipped_nodate += 1
            continue
        if pub >= until or pub < since:
            continue
        in_window.append(e)
    in_window.sort(key=lambda x: x["published_at"])
    if args.limit > 0:
        in_window = in_window[: args.limit]
    print(f"[feed] in-window={len(in_window)} skipped_nodate={skipped_nodate}")

    ok = 0
    for e in in_window:
        text = html_to_text(e["html"])
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
                # GameSpot's RSS entries contain the article body.  Mark a
                # non-empty parsed entry as complete; `partial` is reserved
                # for records where the collector could not obtain readable
                # body text.
                "fetch_status": "ok" if text else "partial",
                # The site exposes only RSS summaries and blocks its detail
                # pages to our collector. These are discovery snippets, never
                # primary evidence for a report item.
                "body_status": "snippet" if text else "empty",
                "fallback": "none" if text else "source_excerpt",
            },
        )
        ok += 1
        print(f"[{e['id']}] saved  {e['published_at']:%Y-%m-%d}  {e['title'][:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} window={since:%Y-%m-%d}..{until:%Y-%m-%d} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
