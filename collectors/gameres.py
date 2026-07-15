"""
Fetch GameRes 游资网 (gameres.com) station-original articles from its homepage.

GameRes is a veteran Chinese game-industry site publishing original editorial /
deep-dive articles at https://www.gameres.com/<numeric-id>.html. The homepage
lists the most recent articles as <numeric-id>.html links; each article page
carries the title in <h1>, the publish date in a header <span> (YYYY-MM-DD), and
the full body inside <div class="contentdiv">. Plain urllib is enough — no
browser, no API.

Only same-host /<id>.html links are followed, so WeChat-mirror / external repost
links on the homepage (which point straight to mp.weixin.qq.com) are excluded by
construction: this collector stores station-original articles only. URLs already
fetched-and-dated are cached in the manifest under "seen_urls" so daily runs fetch
only articles new to the homepage.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
import time
from datetime import datetime, timedelta
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


HOME_URL = "https://www.gameres.com/"
SOURCE_DOMAIN = "gameres.com"
SOURCE_KEY = "gameres"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str) -> str | None:
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate", "Accept": "text/html,*/*"})
        try:
            with urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                raw = resp.read()
                if resp.headers.get("Content-Encoding") == "gzip":
                    try:
                        raw = gzip.decompress(raw)
                    except Exception:
                        pass
                return raw.decode("utf-8", "replace")
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


def make_item_id(url: str) -> str:
    m = re.search(r"/(\d{5,})\.html", url)
    if m:
        return m.group(1)
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


def extract_article_urls(home_html: str) -> list[str]:
    urls = set()
    for m in re.findall(r'href="(https?://www\.gameres\.com/\d{5,}\.html)"', home_html):
        urls.add(m)
    for m in re.findall(r'href="(/\d{5,}\.html)"', home_html):
        urls.add("https://www.gameres.com" + m)
    return sorted(urls)


def extract_div(html: str, open_pattern: str) -> str:
    m = re.search(open_pattern, html)
    if not m:
        return ""
    start = m.end()
    depth = 1
    for token in re.finditer(r"<(/?)div\b", html[start:]):
        if token.group(1) == "/":
            depth -= 1
            if depth == 0:
                return html[start:start + token.start()]
        else:
            depth += 1
    return html[start:]


def parse_article(html: str) -> dict:
    title = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    # publish date: header span with a bare YYYY-MM-DD, else first ISO date on page
    date_val = ""
    m = re.search(r"<span[^>]*>\s*(\d{4}-\d{2}-\d{2})\s*</span>", html)
    if m:
        date_val = m.group(1)
    else:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", html)
        if m:
            date_val = m.group(1)
    published = None
    if date_val:
        try:
            published = datetime.fromisoformat(date_val)
        except ValueError:
            published = None
    author = ""
    m = re.search(r"作者[:：]\s*([^<\s，,]{1,24})", html)
    if m:
        author = m.group(1).strip()
    body_html = extract_div(html, r'<div[^>]*class="contentdiv"[^>]*>')
    return {"title": title, "published_at": published, "author": author, "html": body_html}


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch GameRes 游资网 station-original articles.")
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

    home = http_get(HOME_URL)
    if home is None:
        raise SystemExit("[error] homepage fetch failed")
    urls = extract_article_urls(home)
    print(f"[home] {len(urls)} article url(s); {len(seen)} already seen")

    dated: list[tuple[str, datetime, dict]] = []
    fetched = 0
    for url in urls:
        cached = seen.get(url)
        if cached:
            try:
                dated.append((url, datetime.fromisoformat(cached), {}))
                continue
            except ValueError:
                pass
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
        if not art:
            html = http_get(url)
            if html is None:
                continue
            art = parse_article(html)
        body = html_to_text(art["html"]) if art.get("html") else ""
        write_article_record(
            args.out,
            manifest,
            make_item_id(url),
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": art.get("title") or make_item_id(url),
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
