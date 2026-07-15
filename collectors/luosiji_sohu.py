"""
Fetch 罗斯基 (游戏出海/买量观察) articles via its official Sohu-号 (搜狐号) mirror.

罗斯基's usual entries — the Tencent-News author page (React SPA + token API) and WeChat —
are not plain-HTTP scrapable. But the account mirrors the same posts on its Sohu 自媒体
account, which exposes a clean, urllib-friendly JSON API:

  https://v2.sohu.com/author-page-api/author-articles/pc/<authorId>?pageNumber=N&pageSize=20

authorId=100136645. Each item carries id/title/brief/link/publicTime; the article body is
read from the static page https://www.sohu.com/a/<id>_<authorId>. Pure urllib, no Playwright.

Same "find the account on another channel" tactic as qimai_sohu — a near-copy with a
different authorId/source key.
"""

from __future__ import annotations

import argparse
import gzip
import html as _html
import json
import re
import ssl
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


AUTHOR_ID = "100136645"
API_URL = "https://v2.sohu.com/author-page-api/author-articles/pc/{aid}?pageNumber={page}&pageSize=20"
SOURCE_DOMAIN = "mp.sohu.com"
SOURCE_KEY = "luosiji_sohu"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
LOCAL_TZ = timezone(timedelta(hours=8))
MAX_PAGES = 5
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
_SSL = ssl.create_default_context()
_SSL.check_hostname = False
_SSL.verify_mode = ssl.CERT_NONE


def http_get(url: str, accept: str = "application/json, text/html, */*") -> str:
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        req = Request(url, headers={
            "User-Agent": USER_AGENT, "Accept": accept,
            "Accept-Encoding": "gzip", "Referer": "https://mp.sohu.com/",
        })
        try:
            with urlopen(req, timeout=HTTP_TIMEOUT, context=_SSL) as resp:
                raw = resp.read()
                if resp.headers.get("content-encoding", "").lower() == "gzip":
                    try:
                        raw = gzip.decompress(raw)
                    except OSError:
                        pass
                return raw.decode("utf-8", "replace")
        except HTTPError as exc:
            last_exc = exc
            if exc.code == 404:
                break
        except (URLError, TimeoutError, OSError) as exc:
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


def parse_public_time(value) -> datetime | None:
    """Sohu publicTime 为 ISO-8601 字符串（如 2026-07-07T10:43:55.000+00:00）；也兼容毫秒时间戳。"""
    if value is None:
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value <= 0:
            return None
        return datetime.fromtimestamp(value / 1000, timezone.utc).astimezone(LOCAL_TZ).replace(tzinfo=None, microsecond=0)
    s = str(value).strip()
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return dt.replace(microsecond=0)


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


def article_url(article_id) -> str:
    return f"https://www.sohu.com/a/{article_id}_{AUTHOR_ID}"


_ARTICLE_RE = re.compile(r'<article\b[^>]*>([\s\S]*?)</article>', re.I)
_TEXTDIV_RE = re.compile(r'<div[^>]*\bclass="[^"]*\b(?:article-text|text)\b[^"]*"[^>]*>([\s\S]*?)</div>\s*(?:<div[^>]*class="[^"]*(?:statement|editor|resp)|<footer|</article)', re.I)


def extract_body(page_html: str) -> str:
    m = _ARTICLE_RE.search(page_html)
    frag = m.group(1) if m else ""
    if not frag:
        m2 = _TEXTDIV_RE.search(page_html)
        frag = m2.group(1) if m2 else ""
    if not frag:
        return ""
    frag = re.sub(r"<script\b[\s\S]*?</script>", "", frag, flags=re.I)
    frag = re.sub(r"<style\b[\s\S]*?</style>", "", frag, flags=re.I)
    return html_to_text(frag)


def fetch_articles(since: datetime, until: datetime, max_pages: int) -> list[dict]:
    out: list[dict] = []
    reached_older = False
    for page in range(1, max(1, max_pages) + 1):
        try:
            data = json.loads(http_get(API_URL.format(aid=AUTHOR_ID, page=page)))
        except (RuntimeError, json.JSONDecodeError) as exc:
            print(f"[api] page {page} failed: {exc}", file=sys.stderr)
            break
        vos = (data.get("data") or {}).get("pcArticleVOS") or []
        if not vos:
            reached_older = True
            break
        page_new = 0
        for v in vos:
            pub = parse_public_time(v.get("publicTime"))
            if pub is None:
                continue
            if pub >= until:
                continue
            if pub < since:
                reached_older = True
                continue
            out.append({
                "id": str(v.get("id")),
                "title": _html.unescape((v.get("title") or v.get("mobileTitle") or "").strip()),
                "brief": _html.unescape((v.get("brief") or "").strip()),
                "url": article_url(v.get("id")),
                "published_at": pub,
            })
            page_new += 1
        print(f"[api] page {page}: +{page_new} in-window, total={len(out)}")
        if reached_older:
            break
    out.sort(key=lambda x: x["published_at"])
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch 罗斯基 articles via its Sohu-号 mirror.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=MAX_PAGES, help="CLI compatibility / page cap")
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

    articles = fetch_articles(since, until, args.max_pages)
    if args.limit > 0:
        articles = articles[: args.limit]
    print(f"[feed] in-window={len(articles)}")

    ok = 0
    for a in articles:
        body = ""
        try:
            body = extract_body(http_get(a["url"], accept="text/html,*/*"))
        except RuntimeError as exc:
            print(f"[{a['id']}] body fetch failed ({exc}); using brief", file=sys.stderr)
        full_body = len(body) >= 120
        text = body if full_body else (a["brief"] or body)
        if not text:
            print(f"[{a['id']}] skipped: neither article body nor source brief was available", file=sys.stderr)
            continue
        write_article_record(
            args.out, manifest, a["id"],
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": a["title"],
                "url": a["url"],
                "excerpt": a["brief"],
                "text": text,
                "html": "",
                "published_at": a["published_at"].isoformat(timespec="seconds"),
                "fetch_status": "ok" if full_body else "partial",
                "fallback": "none" if full_body else "source_excerpt",
            },
        )
        ok += 1
        print(f"[{a['id']}] saved  {a['published_at']:%Y-%m-%d}  {a['title'][:40]}")
        time.sleep(0.6)

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} window={since:%Y-%m-%d}..{until:%Y-%m-%d} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
