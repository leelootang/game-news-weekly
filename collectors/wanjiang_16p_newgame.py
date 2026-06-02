"""
Fetch 16p/Wanjiang new-game test and launch calendar entries and export PDFs.

The page at https://www.16p.com/newgame loads its calendar from
https://www.16p.com/gamecenter/api/test_game. This collector intentionally
fetches only the domestic and overseas tabs, skipping the very noisy Steam tab.
"""

from __future__ import annotations

import argparse
import asyncio
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


API_URL = "https://www.16p.com/gamecenter/api/test_game"
SOURCE_DOMAIN = "16p.com"
SOURCE_KEY = "wanjiang_16p_newgame"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
PAGE_TIMEOUT = 30_000
PER_EVENT_DELAY = 0.2
TYPE_RANGES = {
    2: "国内游戏",
    1: "海外游戏",
}
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class CalendarEvent:
    event_id: str
    url: str
    game_id: str
    game_name: str
    test_type: str
    event_at: datetime
    area: str
    source_tab: str
    company_names: list[str]
    publisher_names: list[str]
    developer_names: list[str]
    icon_url: str
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


def fetch_json(params: dict) -> dict:
    url = f"{API_URL}?{urlencode(params)}"
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.16p.com/newgame",
            "X-Requested-With": "XMLHttpRequest",
        },
    )
    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            with urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8-sig"))
        except (OSError, URLError, json.JSONDecodeError) as exc:
            last_exc = exc
            if attempt < 3:
                print(f"[api] retry {attempt}/3 after 16p API error: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch 16p newgame API: {url}: {last_exc}") from last_exc


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


def parse_event_date(value: str) -> datetime | None:
    raw = (value or "").strip()
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def company_names(game: dict, role_id: str | None = None) -> list[str]:
    names: list[str] = []
    for company in game.get("companys") or []:
        if role_id is not None and str(company.get("company_role_id") or "") != role_id:
            continue
        name = str(company.get("name") or "").strip()
        if name and name not in names:
            names.append(name)
    return names


def row_to_event(row: dict, source_tab: str) -> CalendarEvent | None:
    game = row.get("game") or {}
    game_id = str(row.get("gameid") or game.get("gameid") or "").strip()
    game_name = str(game.get("gamename") or "").strip()
    test_type = str(row.get("testtype") or "").strip()
    event_at = parse_event_date(str(row.get("testdate") or ""))
    if not game_id or not game_name or not event_at:
        return None

    area = str(game.get("area") or "").strip()
    event_id = sanitize_filename(f"{source_tab}_{game_id}_{event_at:%Y-%m-%d}_{test_type}", 140)
    return CalendarEvent(
        event_id=event_id,
        url=f"https://www.16p.com/{game_id}.html",
        game_id=game_id,
        game_name=game_name,
        test_type=test_type,
        event_at=event_at,
        area=area,
        source_tab=source_tab,
        company_names=company_names(game),
        publisher_names=company_names(game, "1"),
        developer_names=company_names(game, "2"),
        icon_url=str(game.get("iconurl") or "").strip(),
        image_url=str(game.get("mainimg") or game.get("iconurl") or "").strip(),
    )


def collect_events(since: datetime, until: datetime, max_pages: int) -> list[CalendarEvent]:
    events: dict[str, CalendarEvent] = {}
    start_date = since.strftime("%Y-%m-%d")
    skipped_bad = 0

    for type_range, tab_name in TYPE_RANGES.items():
        for page in range(1, max_pages + 1):
            data = fetch_json({"date": start_date, "type_range": type_range, "p": page})
            date_groups = data.get("dates") or {}
            print(
                f"[api] tab={tab_name} page={page} dates={len(date_groups)} "
                f"first={data.get('first_date')} last={data.get('last_date')} next_end={data.get('next_end')}"
            )
            if not date_groups:
                break

            page_dates: list[datetime] = []
            for date_text, rows in date_groups.items():
                group_date = parse_event_date(date_text)
                if group_date:
                    page_dates.append(group_date)
                for row in rows or []:
                    event = row_to_event(row, tab_name)
                    if not event:
                        skipped_bad += 1
                        continue
                    if since <= event.event_at < until:
                        events[event.event_id] = event

            if page_dates and min(page_dates) >= until:
                break
            if data.get("next_end"):
                break

    selected = sorted(events.values(), key=lambda item: (item.event_at, item.source_tab, item.game_name, item.event_id))
    print(f"[api] selected {len(selected)} event(s), bad_rows={skipped_bad}")
    return selected


def chips(values: list[str]) -> str:
    return "".join(f"<span>{html.escape(value)}</span>" for value in values)


def build_printable_html(event: CalendarEvent) -> str:
    title = html.escape(f"{event.game_name} - {event.test_type or '新游动态'}")
    date_text = html.escape(event.event_at.strftime("%Y-%m-%d"))
    image = f'<img class="cover" src="{html.escape(event.image_url)}" alt="">' if event.image_url else ""
    rows = [
        ("游戏名称", event.game_name),
        ("事件日期", date_text),
        ("事件类型", event.test_type),
        ("版区", event.source_tab),
        ("地区", event.area),
        ("发行", " / ".join(event.publisher_names)),
        ("研发", " / ".join(event.developer_names)),
        ("相关公司", " / ".join(event.company_names)),
        ("16p 链接", event.url),
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
    <div class="meta">玩匠 16p 新游开测表 / release_calendar / {date_text}</div>
    {image}
    <table>{table}</table>
    <section>
      <strong>采集范围</strong>
      <div class="tags">{chips([event.source_tab, "不含 Steam 游戏"])}</div>
    </section>
  </main>
</body>
</html>"""


def event_text(event: CalendarEvent) -> str:
    rows = [
        ("Game", event.game_name),
        ("Event date", event.event_at.strftime("%Y-%m-%d")),
        ("Event type", event.test_type),
        ("Source tab", event.source_tab),
        ("Area", event.area),
        ("Publisher", " / ".join(event.publisher_names)),
        ("Developer", " / ".join(event.developer_names)),
        ("Companies", " / ".join(event.company_names)),
        ("Original URL", event.url),
    ]
    return "\n".join(f"{label}: {value}" for label, value in rows if value)


async def save_event_pdf(context, event: CalendarEvent, out_dir: Path, manifest: dict) -> bool:
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
        title_part = event.test_type or "新游动态"
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
                        "game_id": event.game_id,
                        "game_name": event.game_name,
                        "test_type": event.test_type,
                        "area": event.area,
                        "source_tab": event.source_tab,
                        "company_names": event.company_names,
                        "publisher_names": event.publisher_names,
                        "developer_names": event.developer_names,
                        "event_at": event.event_at.isoformat(timespec="seconds"),
                        "icon_url": event.icon_url,
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
        await page.set_content(build_printable_html(event), wait_until="load", timeout=PAGE_TIMEOUT)
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
            "game_id": event.game_id,
            "game_name": event.game_name,
            "test_type": event.test_type,
            "area": event.area,
            "source_tab": event.source_tab,
            "company_names": event.company_names,
            "publisher_names": event.publisher_names,
            "developer_names": event.developer_names,
            "published_at": event.event_at.isoformat(timespec="seconds"),
            "event_at": event.event_at.isoformat(timespec="seconds"),
            "icon_url": event.icon_url,
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
    parser = argparse.ArgumentParser(description="Fetch 16p new-game calendar events as PDFs.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=5, help="Maximum API pages to scan per tab")
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
    print(f"[config] tabs: {', '.join(TYPE_RANGES.values())}; Steam游戏 skipped")
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
