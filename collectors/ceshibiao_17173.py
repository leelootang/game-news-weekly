"""
Fetch 17173 new-game launch/test/version schedule events and export PDFs.

The 17173 test schedule exposes a JSON endpoint used by the page itself. It is
sorted by test_time, so the collector paginates until it reaches events older
than the requested window.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import html
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from article_store import save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from playwright.async_api import async_playwright


API_URL = "https://www.17173.com/d/ceshibiao/index"
SOURCE_DOMAIN = "17173.com"
SOURCE_KEY = "ceshibiao_17173"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
PAGE_TIMEOUT = 30_000
PER_EVENT_DELAY = 0.2
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class LaunchEvent:
    event_id: str
    url: str
    game_name: str
    test_type: str
    test_name: str
    platforms: list[str]
    publisher: str
    developer: str
    features: list[str]
    languages: list[str]
    score: str
    event_at: datetime
    raw_test_time: int
    image_url: str


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


def sanitize_filename(name: str, max_len: int = 90) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:max_len].rstrip(" .") or "untitled"


def normalize_url(value: str) -> str:
    raw = (value or "").strip()
    if raw.startswith("//"):
        return "https:" + raw
    return raw


def make_event_id(row: dict) -> str:
    raw_id = str(row.get("id") or row.get("test_id") or "")
    game_code = str(row.get("game_code") or "")
    test_time = str(row.get("test_time") or "")
    base = "_".join(part for part in [game_code, raw_id, test_time] if part)
    if base:
        return re.sub(r"\W+", "_", base).strip("_")
    digest = hashlib.sha1(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:12]
    return f"event_{digest}"


def fetch_json(params: dict) -> dict:
    url = f"{API_URL}?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json,*/*"})
    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            with urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8-sig"))
        except (OSError, URLError, json.JSONDecodeError) as exc:
            last_exc = exc
            if attempt < 3:
                print(f"[api] retry {attempt}/3 after 17173 API error: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch 17173 schedule API: {url}: {last_exc}") from last_exc


def event_datetime(raw_ts: int) -> datetime:
    return datetime.fromtimestamp(raw_ts, LOCAL_TZ).replace(tzinfo=None)


def row_to_event(row: dict) -> LaunchEvent | None:
    raw_test_time = row.get("test_time")
    if not raw_test_time:
        return None
    try:
        raw_ts = int(raw_test_time)
    except (TypeError, ValueError):
        return None

    game_name = str(row.get("game_name") or "").strip()
    url = normalize_url(str(row.get("game_url") or ""))
    if not game_name or not url:
        return None

    score = row.get("game_score")
    return LaunchEvent(
        event_id=make_event_id(row),
        url=url,
        game_name=game_name,
        test_type=str(row.get("test_type") or "").strip(),
        test_name=str(row.get("test_name") or "").strip(),
        platforms=[str(x) for x in row.get("game_platform_name") or [] if str(x).strip()],
        publisher=str(row.get("pub_company") or "").strip(),
        developer=str(row.get("dev_company") or "").strip(),
        features=[str(x) for x in row.get("game_feature_name") or [] if str(x).strip()],
        languages=[str(x) for x in row.get("game_lang_name") or [] if str(x).strip()],
        score="" if score in (None, "", 0, "0") else str(score),
        event_at=event_datetime(raw_ts),
        raw_test_time=raw_ts,
        image_url=normalize_url(str(row.get("show_pic") or row.get("logo_pic") or "")),
    )


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


def collect_events(since: datetime, until: datetime, max_pages: int) -> list[LaunchEvent]:
    page_size = 100
    events: list[LaunchEvent] = []
    seen: set[str] = set()
    older_seen = False
    skipped_future = 0
    skipped_bad = 0

    for page in range(1, max_pages + 1):
        data = fetch_json(
            {
                "page": page,
                "page_size": page_size,
                "sort": "test_time",
                "is_ajax": "true",
            }
        )
        rows = data.get("dataSet") or []
        print(f"[api] page={page} rows={len(rows)} total={data.get('total')} hasMore={data.get('hasMore')}")
        if not rows:
            break

        page_has_older = False
        for row in rows:
            event = row_to_event(row)
            if not event:
                skipped_bad += 1
                continue
            if event.event_at >= until:
                skipped_future += 1
                continue
            if event.event_at < since:
                page_has_older = True
                older_seen = True
                continue
            if event.event_id in seen:
                continue
            seen.add(event.event_id)
            events.append(event)

        if page_has_older:
            break
        if not data.get("hasMore"):
            break

    if not older_seen:
        raise RuntimeError(
            f"reached --max-pages={max_pages} before seeing an event older than --since; "
            "increase --max-pages to prove completeness"
        )

    events.sort(key=lambda x: (x.event_at, x.game_name, x.event_id))
    print(f"[api] selected {len(events)} event(s), future_or_later={skipped_future}, bad_rows={skipped_bad}")
    return events


def chips(values: list[str]) -> str:
    return "".join(f"<span>{html.escape(value)}</span>" for value in values)


def build_printable_html(event: LaunchEvent) -> str:
    title = html.escape(f"{event.game_name} - {event.test_type or event.test_name or '新游动态'}")
    date_text = html.escape(event.event_at.strftime("%Y-%m-%d"))
    image = f'<img class="cover" src="{html.escape(event.image_url)}" alt="">' if event.image_url else ""
    rows = [
        ("游戏名称", event.game_name),
        ("事件日期", date_text),
        ("测试类型", event.test_type),
        ("测试名称", event.test_name),
        ("平台", " / ".join(event.platforms)),
        ("发行商", event.publisher),
        ("开发商", event.developer),
        ("语言", " / ".join(event.languages)),
        ("评分", event.score),
        ("17173 链接", event.url),
    ]
    table = "\n".join(
        f"<tr><th>{html.escape(label)}</th><td>{html.escape(value)}</td></tr>"
        for label, value in rows
        if value
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>
    body {{
      margin: 0;
      background: #fff;
      color: #111;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
      line-height: 1.65;
    }}
    main {{
      max-width: 820px;
      margin: 0 auto;
      padding: 28px 12px 44px;
    }}
    h1 {{
      font-size: 30px;
      line-height: 1.28;
      margin: 0 0 10px;
      font-weight: 750;
    }}
    .meta {{
      color: #666;
      font-size: 14px;
      margin-bottom: 22px;
    }}
    .cover {{
      display: block;
      width: 100%;
      max-height: 360px;
      object-fit: contain;
      margin: 0 0 22px;
      background: #f5f5f5;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 22px;
    }}
    th, td {{
      border-bottom: 1px solid #e8e8e8;
      padding: 10px 8px;
      text-align: left;
      vertical-align: top;
      font-size: 15px;
    }}
    th {{
      width: 110px;
      color: #555;
      font-weight: 650;
    }}
    .tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
    }}
    .tags span {{
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 3px 8px;
      font-size: 13px;
      color: #333;
    }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">17173 新游测试表 / product_launches / {date_text}</div>
    {image}
    <table>{table}</table>
    <section>
      <strong>类型标签</strong>
      <div class="tags">{chips(event.features)}</div>
    </section>
  </main>
</body>
</html>"""


def event_text(event: LaunchEvent) -> str:
    rows = [
        ("Game", event.game_name),
        ("Event date", event.event_at.strftime("%Y-%m-%d")),
        ("Test type", event.test_type),
        ("Test name", event.test_name),
        ("Platforms", " / ".join(event.platforms)),
        ("Publisher", event.publisher),
        ("Developer", event.developer),
        ("Features", " / ".join(event.features)),
        ("Languages", " / ".join(event.languages)),
        ("Score", event.score),
        ("Original URL", event.url),
    ]
    return "\n".join(f"{label}: {value}" for label, value in rows if value)


async def save_event_pdf(context, event: LaunchEvent, out_dir: Path, manifest: dict) -> bool:
    recorded = manifest.setdefault("items", {}).get(event.event_id)
    if recorded and recorded.get("data_file"):
        print(f"[{event.event_id}] already saved, skip")
        return True
    if save_pdf_enabled() and recorded and recorded.get("file") and (out_dir / recorded["file"]).exists():
        print(f"[{event.event_id}] already saved, skip")
        return True

    page = await context.new_page()
    tmp_path = out_dir / f".tmp_{event.event_id}.pdf"
    try:
        title_part = event.test_type or event.test_name or "新游动态"
        if not save_pdf_enabled():
            write_article_record(
                out_dir,
                manifest,
                event.event_id,
                {
                    "source": SOURCE_DOMAIN,
                    "source_key": SOURCE_KEY,
                    "title": f"{event.game_name} - {title_part}",
                    "url": event.url,
                    "text": event_text(event),
                    "published_at": event.event_at.isoformat(timespec="seconds"),
                    "extra": {
                        "game_name": event.game_name,
                        "test_type": event.test_type,
                        "test_name": event.test_name,
                        "platforms": event.platforms,
                        "publisher": event.publisher,
                        "developer": event.developer,
                        "features": event.features,
                        "languages": event.languages,
                        "score": event.score,
                        "event_at": event.event_at.isoformat(timespec="seconds"),
                        "raw_test_time": event.raw_test_time,
                        "image_url": event.image_url,
                    },
                },
            )
            save_manifest(out_dir, manifest)
            print(f"[{event.event_id}] saved text record")
            return True

        final_name = (
            f"{FILE_PREFIX}_{event.event_at:%Y-%m-%d}_{event.event_id}_"
            f"{sanitize_filename(event.game_name + '_' + title_part)}.pdf"
        )
        final_path = out_dir / final_name
        print(f"[{event.event_id}] render {event.game_name}")
        await page.set_content(build_printable_html(event), wait_until="networkidle", timeout=PAGE_TIMEOUT)
        await page.emulate_media(media="screen")
        await page.pdf(
            path=str(tmp_path),
            format="A4",
            print_background=True,
            margin={"top": "12mm", "right": "10mm", "bottom": "12mm", "left": "10mm"},
        )
        tmp_path.replace(final_path)

        manifest["items"][event.event_id] = {
            "file": final_name,
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "title": f"{event.game_name} - {title_part}",
            "url": event.url,
            "game_name": event.game_name,
            "test_type": event.test_type,
            "test_name": event.test_name,
            "platforms": event.platforms,
            "publisher": event.publisher,
            "developer": event.developer,
            "features": event.features,
            "languages": event.languages,
            "score": event.score,
            "published_at": event.event_at.isoformat(timespec="seconds"),
            "event_at": event.event_at.isoformat(timespec="seconds"),
            "raw_test_time": event.raw_test_time,
            "image_url": event.image_url,
            "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        save_manifest(out_dir, manifest)
        print(f"[{event.event_id}] saved {final_name}")
        return True
    except Exception as exc:
        print(f"[{event.event_id}] failed: {exc!r}", file=sys.stderr)
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
        return False
    finally:
        await page.close()


async def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch 17173 new-game launch/test schedule events as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=5, help="Maximum API pages to scan")
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum events to export")
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
    print(f"[config] window: {since} <= event < {until}")
    print(f"[config] output: {args.out.resolve()}")

    events = collect_events(since, until, args.max_pages)
    if args.limit > 0:
        events = events[: args.limit]
    print(f"[api] exporting {len(events)} event(s)")

    if not events:
        save_manifest(args.out, manifest)
        print(f"[done] ok=0 fail=0 output={args.out.resolve()}")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not args.headful)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale="zh-CN",
            timezone_id="Asia/Shanghai",
            viewport={"width": 1280, "height": 900},
        )

        ok = 0
        fail = 0
        for event in events:
            if await save_event_pdf(context, event, args.out, manifest):
                ok += 1
            else:
                fail += 1
            await asyncio.sleep(PER_EVENT_DELAY)

        await context.close()
        await browser.close()

    print(f"[done] ok={ok} fail={fail} output={args.out.resolve()}")
    if fail:
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())
