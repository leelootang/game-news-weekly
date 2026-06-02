"""
Fetch TapTap app-calendar entries and store them as release-calendar records.

TapTap renders each date at /app-calendar/YYYY-MM-DD. Some entries are hidden
behind a fold card, so this collector uses Playwright to open the date route,
expand the folded list, then writes structured text records through
article_store.py.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin

from article_store import write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError, async_playwright


CALENDAR_BASE_URL = "https://www.taptap.cn/app-calendar"
BASE_URL = "https://www.taptap.cn"
SOURCE_DOMAIN = "taptap.cn"
SOURCE_KEY = "taptap_app_calendar"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
PAGE_TIMEOUT = 45_000
PER_DAY_DELAY = 0.3
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class CalendarEvent:
    event_id: str
    url: str
    game_name: str
    event_date: datetime
    event_type: str
    event_time: str
    rating: str
    tags: list[str]
    image_url: str
    raw_text: str


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        parsed = datetime.fromisoformat(raw)
        if end_of_day:
            return parsed + timedelta(days=1)
        return parsed
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


def iter_dates(since: datetime, until: datetime) -> list[datetime]:
    current = since.replace(hour=0, minute=0, second=0, microsecond=0)
    end = until.replace(hour=0, minute=0, second=0, microsecond=0)
    if until.time() != datetime.min.time():
        end += timedelta(days=1)

    days = []
    while current < end:
        if current.date() >= since.date() and current.date() <= (until - timedelta(microseconds=1)).date():
            days.append(current)
        current += timedelta(days=1)
    return days


def event_datetime(day: datetime, event_time: str) -> datetime:
    match = re.search(r"(\d{1,2}):(\d{2})", event_time or "")
    if not match:
        return day
    hour, minute = map(int, match.groups())
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        return day.replace(hour=hour, minute=minute)
    return day


def make_event_id(href: str, date_value: datetime, event_type: str) -> str:
    app_match = re.search(r"/app/(\d+)", href)
    app_id = app_match.group(1) if app_match else href
    digest = hashlib.sha1(f"{app_id}|{date_value.date()}|{event_type}".encode("utf-8")).hexdigest()[:10]
    return f"app_{app_id}_{date_value:%Y%m%d}_{digest}"


def record_title(event: CalendarEvent) -> str:
    event_type = event.event_type or "calendar event"
    suffix = f" ({event.event_time})" if event.event_time else ""
    return f"{event.game_name} - {event_type}{suffix}"


def event_text(event: CalendarEvent) -> str:
    rows = [
        ("Game", event.game_name),
        ("Event date", event.event_date.strftime("%Y-%m-%d %H:%M")),
        ("Event type", event.event_type),
        ("Event time", event.event_time),
        ("Rating", event.rating),
        ("Tags", " / ".join(event.tags)),
        ("Original URL", event.url),
    ]
    return "\n".join(f"{label}: {value}" for label, value in rows if value)


async def goto_calendar_day(page: Page, day: datetime) -> None:
    url = f"{CALENDAR_BASE_URL}/{day:%Y-%m-%d}"
    try:
        await page.goto(url, wait_until="networkidle", timeout=PAGE_TIMEOUT)
    except PlaywrightTimeoutError:
        print(f"[page] networkidle timeout for {url}; retrying with domcontentloaded", file=sys.stderr)
        await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
    await page.wait_for_selector(".daily-event-list__content, body", timeout=PAGE_TIMEOUT)


async def expand_folded_events(page: Page) -> int:
    expanded = 0
    for _ in range(8):
        fold = page.locator(".daily-event-fold-card").first
        if await fold.count() == 0:
            break
        try:
            await fold.click(timeout=5_000)
            expanded += 1
            await page.wait_for_timeout(600)
        except PlaywrightTimeoutError:
            break
    return expanded


async def extract_day_events(page: Page, day: datetime) -> list[CalendarEvent]:
    raw_events = await page.evaluate(
        """
        () => [...document.querySelectorAll('.daily-event-list__content a[href^="/app/"]')]
          .map((a) => ({
            href: a.getAttribute('href') || '',
            name: (
              a.querySelector('[itemprop="name"], .daily-event-app-info__title')?.textContent || ''
            ).trim(),
            eventType: (
              a.querySelector('.event-type-label__title')?.textContent || ''
            ).trim(),
            time: (
              a.querySelector('.daily-event-big-card__time')?.textContent || ''
            ).trim(),
            rating: (
              a.querySelector('.tap-rating__number')?.textContent || ''
            ).trim(),
            tags: [...a.querySelectorAll('.tap-label-tag')]
              .map((node) => (node.textContent || '').trim())
              .filter(Boolean),
            image: (
              a.querySelector('img')?.getAttribute('data-src') ||
              a.querySelector('img')?.getAttribute('src') ||
              ''
            ),
            rawText: (a.innerText || '').trim(),
          }))
        """
    )

    events: dict[str, CalendarEvent] = {}
    for item in raw_events:
        href = str(item.get("href") or "").strip()
        game_name = re.sub(r"\s+", " ", str(item.get("name") or "")).strip()
        if not href or not game_name:
            continue
        event_type = re.sub(r"\s+", " ", str(item.get("eventType") or "")).strip()
        event_time = re.sub(r"\s+", " ", str(item.get("time") or "")).strip()
        event_date = event_datetime(day, event_time)
        event_id = make_event_id(href, event_date, event_type)
        image_url = str(item.get("image") or "").strip()
        if image_url.startswith("//"):
            image_url = f"https:{image_url}"
        elif image_url.startswith("/"):
            image_url = urljoin(BASE_URL, image_url)
        event = CalendarEvent(
            event_id=event_id,
            url=urljoin(BASE_URL, href),
            game_name=game_name,
            event_date=event_date,
            event_type=event_type,
            event_time=event_time,
            rating=str(item.get("rating") or "").strip(),
            tags=[str(tag).strip() for tag in item.get("tags") or [] if str(tag).strip()],
            image_url=image_url,
            raw_text=str(item.get("rawText") or "").strip(),
        )
        events[event.event_id] = event
    return sorted(events.values(), key=lambda event: (event.event_date, event.game_name, event.event_id))


async def collect_events(since: datetime, until: datetime, *, headful: bool) -> list[CalendarEvent]:
    selected: dict[str, CalendarEvent] = {}
    days = iter_dates(since, until)
    print(f"[calendar] fetching {len(days)} day page(s)")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headful)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale="zh-CN",
            timezone_id="Asia/Shanghai",
            viewport={"width": 1365, "height": 1100},
        )
        page = await context.new_page()
        for day in days:
            await goto_calendar_day(page, day)
            expanded = await expand_folded_events(page)
            day_events = await extract_day_events(page, day)
            in_window = 0
            for event in day_events:
                if since <= event.event_date < until:
                    selected[event.event_id] = event
                    in_window += 1
            print(
                f"[calendar] {day:%Y-%m-%d}: extracted={len(day_events)} "
                f"in_window={in_window} folded_expanded={expanded}"
            )
            await asyncio.sleep(PER_DAY_DELAY)
        await page.close()
        await context.close()
        await browser.close()
    return sorted(selected.values(), key=lambda event: (event.event_date, event.game_name, event.event_id))


def save_event(out_dir: Path, manifest: dict, event: CalendarEvent) -> None:
    write_article_record(
        out_dir,
        manifest,
        event.event_id,
        {
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "title": record_title(event),
            "url": event.url,
            "text": event_text(event),
            "published_at": event.event_date.isoformat(timespec="seconds"),
            "extra": {
                "game_name": event.game_name,
                "event_type": event.event_type,
                "event_time": event.event_time,
                "event_date": event.event_date.isoformat(timespec="seconds"),
                "rating": event.rating,
                "tags": event.tags,
                "image_url": event.image_url,
                "raw_text": event.raw_text,
            },
        },
    )


async def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch TapTap app-calendar events.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-06-01")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-06-02")
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility")
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum events to export")
    parser.add_argument("--headful", action="store_true", help="Show browser window for debugging")
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

    if args.max_pages != 1:
        print("[calendar] TapTap app-calendar is date-routed; --max-pages is accepted for runner compatibility")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    print(f"[config] window: {since} <= event < {until}")
    print(f"[config] output: {args.out.resolve()}")

    started = time.monotonic()
    events = await collect_events(since, until, headful=args.headful)
    if args.limit > 0:
        events = events[: args.limit]
    print(f"[calendar] exporting {len(events)} event(s)")

    for event in events:
        save_event(args.out, manifest, event)
        print(f"[{event.event_id}] saved text record: {record_title(event)}")
    save_manifest(args.out, manifest)

    elapsed = time.monotonic() - started
    print(f"[done] ok={len(events)} fail=0 elapsed={elapsed:.1f}s output={args.out.resolve()}")


if __name__ == "__main__":
    asyncio.run(main())
