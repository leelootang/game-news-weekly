"""
Fetch Game Oracle (game-oracle.com) blog deep-dives via its XML sitemap.

Game Oracle is a Steam market-data analytics site whose /blog section publishes
low-frequency long-form deep dives (roughly one or two posts a month: monthly
Steam reports, genre analyses, release-timing studies). There is no RSS feed, but
the site exposes a full sitemap at https://www.game-oracle.com/sitemap.xml listing
every /blog/<slug> article URL. Each article page embeds a schema.org JSON-LD
BlogPosting with headline, description, datePublished and author, plus the full
body inside a large <article> element — so title/date come from JSON-LD and the
body from that article region, no browser needed (plain urllib).

Because publish dates live only on the article pages (the sitemap carries no
per-URL date), the collector caches every URL it has already fetched-and-dated in
the manifest under "seen_urls" (url -> iso date). Daily runs then fetch only URLs
new to the sitemap, keeping the per-run cost to at most a handful of GETs. An
empty window is the normal case for this low-frequency source and never an error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
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


SITEMAP_URL = "https://www.game-oracle.com/sitemap.xml"
ARTICLE_BASE = "https://www.game-oracle.com/blog/"
SOURCE_DOMAIN = "game-oracle.com"
SOURCE_KEY = "gameoracle"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str) -> str | None:
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*"})
        try:
            with urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                return resp.read().decode("utf-8", "replace")
        except HTTPError as exc:
            last_exc = exc
            if exc.code == 404:
                return None
        except (URLError, TimeoutError) as exc:
            last_exc = exc
        if attempt < HTTP_RETRIES:
            time.sleep(1.2 * attempt)
    print(f"[warn] GET failed after {HTTP_RETRIES} tries: {url} ({last_exc!r})")
    return None


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


def parse_iso(value: str) -> datetime | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return dt.replace(microsecond=0)


def make_item_id(url: str) -> str:
    slug = re.search(r"/blog/(.+?)/?$", url)
    if slug:
        return re.sub(r"\W+", "_", slug.group(1)).strip("_")[-48:] or "unknown"
    return re.sub(r"\W+", "_", url).strip("_")[-24:] or "unknown"


def load_manifest(out_dir: Path) -> dict:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME):
        if not path.exists() and legacy_path.exists():
            path = legacy_path
            break
    if not path.exists():
        return {"items": {}, "seen_urls": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        data.setdefault("seen_urls", {})
        return data
    except Exception:
        return {"items": {}, "seen_urls": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def extract_article_urls(sitemap_xml: str) -> list[str]:
    urls = re.findall(r"<loc>\s*(.*?)\s*</loc>", sitemap_xml)
    out = []
    for raw in urls:
        u = raw.replace("&amp;", "&").strip()
        if not u.startswith(ARTICLE_BASE):
            continue
        rest = u[len(ARTICLE_BASE):]
        if not rest or rest.startswith("category/"):
            continue
        out.append(u)
    return out


def parse_article(html: str) -> dict:
    headline = ""
    description = ""
    published = None
    author = ""
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    if m:
        try:
            data = json.loads(m.group(1))
            graph = data.get("@graph", [data]) if isinstance(data, dict) else [data]
            for node in graph:
                if not isinstance(node, dict):
                    continue
                if node.get("@type") in ("BlogPosting", "Article", "NewsArticle"):
                    headline = node.get("headline", "") or headline
                    description = node.get("description", "") or description
                    published = published or parse_iso(node.get("datePublished", ""))
                    auth = node.get("author")
                    if isinstance(auth, dict):
                        author = auth.get("name", "") or author
                    elif isinstance(auth, str):
                        author = auth or author
        except Exception:
            pass
    if not headline:
        m2 = re.search(r'property="og:title"\s+content="(.*?)"', html)
        if m2:
            headline = m2.group(1)
    if published is None:
        m3 = re.search(r'article:published_time"\s+content="([^"]+)"', html)
        if m3:
            published = parse_iso(m3.group(1))
    # Body: the main content lives in the largest <article> block.
    blocks = re.findall(r"<article[^>]*>(.*?)</article>", html, re.S)
    body_html = max(blocks, key=len) if blocks else ""
    return {
        "title": headline.strip(),
        "description": description.strip(),
        "published_at": published,
        "author": author.strip(),
        "html": body_html,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Game Oracle blog deep-dives via sitemap.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=1, help="Unused; kept for CLI compatibility.")
    parser.add_argument("--headful", action="store_true", help="Unused; kept for CLI compatibility.")
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
    seen = manifest.setdefault("seen_urls", {})
    print(f"[config] window: {since} <= published < {until}")
    print(f"[config] output: {args.out.resolve()}")

    sitemap = http_get(SITEMAP_URL)
    if sitemap is None:
        raise SystemExit("[error] sitemap fetch failed")
    urls = extract_article_urls(sitemap)
    print(f"[sitemap] {len(urls)} blog article url(s); {len(seen)} already seen")

    # Collect (url, published_at) pairs: from cache when known, else fetch page.
    dated: list[tuple[str, datetime, dict]] = []
    fetched = 0
    for url in urls:
        cached = seen.get(url)
        if cached:
            pub = parse_iso(cached)
            if pub is not None:
                dated.append((url, pub, {}))
                continue
        html = http_get(url)
        fetched += 1
        if html is None:
            continue
        art = parse_article(html)
        pub = art["published_at"]
        if pub is None:
            print(f"[skip] no date: {url}")
            continue
        seen[url] = pub.isoformat(timespec="seconds")
        dated.append((url, pub, art))
    print(f"[fetch] fetched {fetched} new page(s)")

    in_window = [(u, p, a) for (u, p, a) in dated if since <= p < until]
    in_window.sort(key=lambda x: x[1])
    if args.limit > 0:
        in_window = in_window[: args.limit]
    print(f"[window] {len(in_window)} article(s) in window")

    ok = 0
    for url, pub, art in in_window:
        if not art:  # cached-but-in-window: fetch full body now
            html = http_get(url)
            if html is None:
                continue
            art = parse_article(html)
        body = html_to_text(art["html"]) if art.get("html") else ""
        if not body:
            body = art.get("description", "")
        write_article_record(
            args.out,
            manifest,
            make_item_id(url),
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": art.get("title") or url.rsplit("/", 1)[-1],
                "url": url,
                "author": art.get("author", ""),
                "text": body,
                "html": art.get("html", ""),
                "published_at": pub.isoformat(timespec="seconds"),
            },
        )
        ok += 1
        print(f"[{make_item_id(url)}] saved  {pub:%Y-%m-%d}  {(art.get('title') or '')[:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} window={since:%Y-%m-%d}..{until:%Y-%m-%d} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
