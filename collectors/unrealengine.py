"""
Fetch Unreal Engine (unrealengine.com) news/spotlight posts from its public RSS feed.

Epic exposes an RSS feed at https://www.unrealengine.com/rss carrying the official
UE news, developer interviews and spotlights, with full body inside <content:encoded>.
Notably the HTML news page (/zh-CN/news) is Cloudflare-gated (HTTP 403 even to headless
browsers), but the RSS endpoint serves fine to plain urllib — so the feed is the only
reliable, low-noise entry. Low-frequency, high-signal engine/tech source.

Records go to the flat root articles.jsonl via write_article_record, keyed by the URL slug.
"""

from __future__ import annotations

import argparse
import hashlib
import html as _html
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


FEED_URL = "https://www.unrealengine.com/rss"
SOURCE_DOMAIN = "unrealengine.com"
SOURCE_KEY = "unrealengine"
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
    dt = None
    # Atom 用 ISO-8601（2026-06-26T00:00:00Z）；RSS 用 RFC-822。两种都试。
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            dt = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
    if dt is None:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return dt.replace(microsecond=0)


ATOM = "{http://www.w3.org/2005/Atom}"


def _sanitize_feed(xml_text: str) -> str:
    """UE 的 Atom feed 在 </feed> 之后被注入了 <script> 分析代码，属"文档元素之后的垃圾"，
    会让 XML 解析报错。截断到根闭合标签为止；顺带剥掉开头可能的 BOM/前导空白。"""
    xml_text = xml_text.lstrip("﻿ \t\r\n")
    for close in ("</feed>", "</rss>"):
        idx = xml_text.rfind(close)
        if idx != -1:
            return xml_text[: idx + len(close)]
    return xml_text


def make_item_id(url: str, guid: str) -> str:
    slug = re.sub(r"^https?://[^/]+/", "", url).strip("/")
    slug = re.sub(r"^(zh-CN|en-US|[a-z]{2}-[A-Z]{2})/", "", slug)
    clean = re.sub(r"\W+", "_", slug).strip("_")
    if not clean:
        base = guid or url
        return hashlib.sha1(base.encode("utf-8")).hexdigest()[:12]
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
    root = ET.fromstring(_sanitize_feed(xml_text))
    tag = root.tag.lower()
    out: list[dict] = []
    if tag.endswith("feed"):  # Atom
        for entry in root.findall(f"{ATOM}entry"):
            # UE 的 <title> 文本内嵌 <p>…</p> 等 HTML 标签，需剥标签、反转义后作纯标题。
            title = _html.unescape(re.sub(r"<[^>]+>", "", _text(entry.find(f"{ATOM}title")))).strip()
            link = ""
            for ln in entry.findall(f"{ATOM}link"):
                rel = ln.get("rel", "alternate")
                if rel in ("alternate", ""):
                    link = ln.get("href", ""); break
            if not link and entry.find(f"{ATOM}link") is not None:
                link = entry.find(f"{ATOM}link").get("href", "")
            if not link or not title:
                continue
            published = parse_pubdate(_text(entry.find(f"{ATOM}published")) or _text(entry.find(f"{ATOM}updated")))
            author_el = entry.find(f"{ATOM}author")
            author = _text(author_el.find(f"{ATOM}name")) if author_el is not None else ""
            content_el = entry.find(f"{ATOM}content")
            body_html = (content_el.text or "") if content_el is not None else ""
            if not body_html:
                body_html = _text(entry.find(f"{ATOM}summary"))
            gid = _text(entry.find(f"{ATOM}id"))
            out.append({
                "id": make_item_id(link, gid),
                "url": link,
                "title": title,
                "published_at": published,
                "author": author,
                "html": body_html,
            })
        return out
    # RSS 回退
    channel = root.find("channel")
    items = channel.findall("item") if channel is not None else root.findall("item")
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
    parser = argparse.ArgumentParser(description="Fetch Unreal Engine news from its RSS feed.")
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
            },
        )
        ok += 1
        print(f"[{e['id']}] saved  {e['published_at']:%Y-%m-%d}  {e['title'][:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} window={since:%Y-%m-%d}..{until:%Y-%m-%d} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
