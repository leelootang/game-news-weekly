"""
Fetch QuestMobile (questmobile.com.cn) research reports from its JSON API.

QuestMobile is a Chinese mobile-internet market-research house. Its public
report list at /research/report-list is a client-rendered SPA whose per-report
pages carry NO machine-readable body — the actual report is an image-based slide
deck, and the visible <div> containers hold only product-menu boilerplate. The
only structured text lives behind the list API:

    /api/v2/report/article-list?version=0&pageSize=N&pageNo=1&industryId=-1&labelId=-1

which returns clean JSON: each record has an id, title, a ~100-200 char Chinese
`introduction` (the report's headline finding), a date-only `publishTime`, and
`industryList` / `labelList` tag arrays. `content` is always null (the deck is
imagery), so we use `introduction` as the body text and stash the tag arrays in
`extra`. A single API GET yields every recent report — no browser, no per-page
fetch.

QuestMobile publishes roughly one or two reports a week (market-research cadence,
not news), so a daily window commonly returns zero items; that is expected, not a
fault. This is a market-research signal source, not a games-news source, so it
enters gloss / search / deep-track but is intentionally outside the deep-read
lock.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from article_store import write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


API_URL = (
    "https://www.questmobile.com.cn/api/v2/report/article-list"
    "?version=0&pageSize={page_size}&pageNo=1&industryId=-1&labelId=-1"
)
REPORT_URL = "https://www.questmobile.com.cn/research/report/{id}"
SOURCE_DOMAIN = "questmobile.com.cn"
SOURCE_KEY = "questmobile"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
DEFAULT_PAGE_SIZE = 30
AUTHOR = "QuestMobile"
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
                "Accept": "application/json, text/plain, */*",
                "Referer": "https://www.questmobile.com.cn/research/report-list",
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


def parse_publish_time(value: str) -> datetime | None:
    raw = (value or "").strip()
    if not raw:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", raw)
    if not m:
        return None
    return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))


def parse_reports(json_text: str) -> list[dict]:
    try:
        obj = json.loads(json_text)
    except (ValueError, TypeError):
        return []
    rows = obj.get("data") if isinstance(obj, dict) else None
    if not isinstance(rows, list):
        return []
    out: list[dict] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        rid = str(row.get("id") or "").strip()
        title = (row.get("title") or "").strip()
        if not rid or not title:
            continue
        intro = (row.get("introduction") or "").strip()
        industries = [x for x in (row.get("industryList") or []) if isinstance(x, str)]
        labels = [x for x in (row.get("labelList") or []) if isinstance(x, str)]
        out.append(
            {
                "id": rid,
                "url": REPORT_URL.format(id=rid),
                "title": title,
                "introduction": intro,
                "published_at": parse_publish_time(row.get("publishTime") or ""),
                "industry_list": industries,
                "label_list": labels,
                "cover": (row.get("coverImgUrl") or "").strip(),
            }
        )
    return out


def build_text(entry: dict) -> str:
    parts: list[str] = []
    if entry["introduction"]:
        parts.append(entry["introduction"])
    if entry["industry_list"]:
        parts.append("涉及行业：" + "、".join(entry["industry_list"]))
    if entry["label_list"]:
        parts.append("标签：" + "、".join(entry["label_list"]))
    return "\n\n".join(parts).strip()


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
    parser = argparse.ArgumentParser(description="Fetch QuestMobile reports from its list API.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--page-size", type=int, default=DEFAULT_PAGE_SIZE)
    parser.add_argument("--max-pages", type=int, default=1, help="Unused (single API call); CLI compatibility.")
    parser.add_argument("--headful", action="store_true", help="Unused; CLI compatibility.")
    args = parser.parse_args()

    try:
        since, until = preset_window(args.preset)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if args.since:
        since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until, end_of_day=True)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    print(f"[config] window: {since} <= published < {until}")

    page_size = max(1, args.page_size)
    json_text = http_get(API_URL.format(page_size=page_size))
    if not json_text:
        raise SystemExit("failed to fetch report list")
    entries = parse_reports(json_text)
    print(f"[api] parsed {len(entries)} report(s)")

    in_window = []
    for e in entries:
        pub = e["published_at"]
        if pub is None or pub >= until or pub < since:
            continue
        in_window.append(e)
    in_window.sort(key=lambda x: x["published_at"])
    if args.limit > 0:
        in_window = in_window[: args.limit]
    print(f"[api] in-window={len(in_window)}")

    ok = 0
    for e in in_window:
        text = build_text(e)
        if not text:
            continue
        html = f"<p>{e['introduction']}</p>" if e["introduction"] else ""
        write_article_record(
            args.out,
            manifest,
            e["id"],
            {
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": e["title"],
                "url": e["url"],
                "author": AUTHOR,
                "text": text,
                "html": html,
                "published_at": e["published_at"].isoformat(timespec="seconds"),
                "fetch_status": "partial",
                "fallback": "source_excerpt",
                "extra": {
                    "industry_list": e["industry_list"],
                    "label_list": e["label_list"],
                    "cover": e["cover"],
                    "body_kind": "introduction_only",
                },
            },
        )
        ok += 1
        print(f"[{e['id']}] saved  {e['published_at']:%Y-%m-%d}  {e['title'].strip()[:40]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={ok} output={args.out.resolve()}")


if __name__ == "__main__":
    main()
