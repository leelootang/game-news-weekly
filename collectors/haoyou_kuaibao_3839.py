"""
Fetch Haoyou Kuaibao (3839) timeline entries and store them as release-calendar records.

The page at https://www.3839.com/timeline.html renders its date cards in the
initial HTML. This collector parses those cards directly and writes structured
text records through article_store.py.
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
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from article_store import save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from playwright.async_api import async_playwright


TIMELINE_URL = "https://www.3839.com/timeline.html"
BASE_URL = "https://www.3839.com"
SOURCE_DOMAIN = "3839.com"
SOURCE_KEY = "haoyou_kuaibao_3839"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
PAGE_TIMEOUT = 30_000
PER_EVENT_DELAY = 0.2
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class TimelineEvent:
    event_id: str
    url: str
    game_name: str
    event_at: datetime
    day_label: str
    event_text: str
    action: str
    score: str
    tags: list[str]
    badges: list[str]
    image_url: str


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


def sanitize_filename(name: str, max_len: int = 90) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:max_len].rstrip(" .") or "untitled"


def strip_tags(value: str) -> str:
    text = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def extract_text(pattern: str, value: str) -> str:
    match = re.search(pattern, value, flags=re.I | re.S)
    return strip_tags(match.group(1)) if match else ""


def extract_attr(pattern: str, value: str) -> str:
    match = re.search(pattern, value, flags=re.I | re.S)
    return html.unescape(match.group(1)).strip() if match else ""


def fetch_timeline_html() -> str:
    request = Request(
        TIMELINE_URL,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": BASE_URL,
        },
    )
    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            with urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8-sig")
        except (OSError, URLError, UnicodeDecodeError) as exc:
            last_exc = exc
            if attempt < 3:
                print(f"[html] retry {attempt}/3 after 3839 timeline error: {exc}", file=sys.stderr)
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch 3839 timeline: {TIMELINE_URL}: {last_exc}") from last_exc


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


def card_date(label: str, since: datetime, until: datetime) -> datetime | None:
    match = re.search(r"(\d{1,2})月(\d{1,2})日", label)
    if not match:
        return None
    month, day = map(int, match.groups())
    candidates = []
    for year in sorted({since.year - 1, since.year, since.year + 1, until.year - 1, until.year, until.year + 1}):
        try:
            candidates.append(datetime(year, month, day))
        except ValueError:
            continue
    if not candidates:
        return None
    midpoint = since + (until - since) / 2
    return min(candidates, key=lambda item: abs(item - midpoint))


def event_time(text: str) -> tuple[int, int]:
    match = re.search(r"(\d{1,2}):(\d{2})", text)
    if not match:
        return 0, 0
    hour, minute = map(int, match.groups())
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        return hour, minute
    return 0, 0


def make_event_id(url: str, date_value: datetime, event_text: str) -> str:
    url_part = re.search(r"/a/(\d+)\.htm", url)
    stable = url_part.group(1) if url_part else url
    digest = hashlib.sha1(f"{stable}|{date_value.date()}|{event_text}".encode("utf-8")).hexdigest()[:10]
    return f"{stable}_{date_value:%Y%m%d}_{digest}"


def parse_card_events(card_html: str, date_value: datetime, day_label: str) -> list[TimelineEvent]:
    events = []
    for li_match in re.finditer(r"<li\b[^>]*>(.*?)</li>", card_html, flags=re.I | re.S):
        li_html = li_match.group(1)
        href = extract_attr(r"<a\b[^>]*href=[\"']([^\"']+)[\"']", li_html)
        game_name = extract_text(r"<div class=[\"']name[\"'][^>]*>(.*?)</div>", li_html)
        if not game_name:
            game_name = extract_attr(r"<img\b[^>]*alt=[\"']([^\"']+)[\"']", li_html)
        game_name = re.sub(r"\s+", " ", game_name).strip()
        if not href or not game_name:
            continue

        info_html = extract_attr(r"<div class=[\"']info[\"'][^>]*>(.*?)</div>", li_html)
        score = extract_text(r"<span class=[\"']score[\"'][^>]*>(.*?)</span>", info_html)
        event = strip_tags(re.sub(r"<span class=[\"']score[\"'][^>]*>.*?</span>", " ", info_html, flags=re.I | re.S))
        tags = [strip_tags(match.group(1)) for match in re.finditer(r"<span class=[\"']it[\"'][^>]*>(.*?)</span>", li_html, flags=re.I | re.S)]
        badges = [strip_tags(match.group(1)) for match in re.finditer(r"<span class=[\"']g-type[^\"']*[\"'][^>]*>(.*?)</span>", li_html, flags=re.I | re.S)]
        action = extract_text(r"<a class=[\"']btn[^\"']*[\"'][^>]*>(.*?)</a>", li_html)
        image_url = extract_attr(r"<img\b[^>]*(?:lz_src|src)=[\"']([^\"']+)[\"']", li_html)

        hour, minute = event_time(event)
        event_at = date_value.replace(hour=hour, minute=minute)
        url = urljoin(BASE_URL, href)
        event_id = make_event_id(url, event_at, event)
        events.append(
            TimelineEvent(
                event_id=event_id,
                url=url,
                game_name=game_name,
                event_at=event_at,
                day_label=day_label,
                event_text=event,
                action=action,
                score=score,
                tags=[tag for tag in tags if tag],
                badges=[badge for badge in badges if badge],
                image_url=urljoin("https:", image_url) if image_url.startswith("//") else image_url,
            )
        )
    return events


def collect_events(since: datetime, until: datetime) -> list[TimelineEvent]:
    source_html = fetch_timeline_html()
    cards = re.findall(r"(<div class=[\"']foreCard[\"'][^>]*>.*?)(?=<div class=[\"']foreCard[\"']|\Z)", source_html, flags=re.I | re.S)
    events: dict[str, TimelineEvent] = {}
    skipped_outside = 0
    skipped_bad_date = 0

    for card in cards:
        day_label = extract_text(r"<div class=[\"']foreCard-hd[\"'][^>]*>(.*?)</div>", card)
        date_value = card_date(day_label, since, until)
        if not date_value:
            skipped_bad_date += 1
            continue
        for event in parse_card_events(card, date_value, day_label):
            if since <= event.event_at < until:
                events[event.event_id] = event
            else:
                skipped_outside += 1

    selected = sorted(events.values(), key=lambda item: (item.event_at, item.game_name, item.event_id))
    print(
        f"[html] cards={len(cards)} selected={len(selected)} "
        f"outside_window={skipped_outside} bad_date_cards={skipped_bad_date}"
    )
    return selected


def event_text(event: TimelineEvent) -> str:
    rows = [
        ("Game", event.game_name),
        ("Event date", event.event_at.strftime("%Y-%m-%d %H:%M")),
        ("Timeline label", event.day_label),
        ("Event", event.event_text),
        ("Action", event.action),
        ("Score", event.score),
        ("Tags", " / ".join(event.tags)),
        ("Badges", " / ".join(event.badges)),
        ("Original URL", event.url),
    ]
    return "\n".join(f"{label}: {value}" for label, value in rows if value)


def build_printable_html(event: TimelineEvent) -> str:
    title = html.escape(f"{event.game_name} - {event.event_text or event.action or '快爆时间轴'}")
    image = f'<img class="cover" src="{html.escape(event.image_url)}" alt="">' if event.image_url else ""
    rows = [
        ("游戏名称", event.game_name),
        ("事件日期", event.event_at.strftime("%Y-%m-%d %H:%M")),
        ("时间轴标注", event.day_label),
        ("事件说明", event.event_text),
        ("按钮状态", event.action),
        ("评分", event.score),
        ("标签", " / ".join(event.tags)),
        ("标记", " / ".join(event.badges)),
        ("快爆链接", event.url),
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
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">好游快爆时间轴 / release_calendar / {event.event_at:%Y-%m-%d}</div>
    {image}
    <table>{table}</table>
  </main>
</body>
</html>"""


async def save_event_pdf(context, event: TimelineEvent, out_dir: Path, manifest: dict) -> bool:
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
        title_part = event.event_text or event.action or "快爆时间轴"
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
                        "event_text": event.event_text,
                        "action": event.action,
                        "score": event.score,
                        "tags": event.tags,
                        "badges": event.badges,
                        "day_label": event.day_label,
                        "event_at": event.event_at.isoformat(timespec="seconds"),
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
            "game_name": event.game_name,
            "event_text": event.event_text,
            "action": event.action,
            "score": event.score,
            "tags": event.tags,
            "badges": event.badges,
            "published_at": event.event_at.isoformat(timespec="seconds"),
            "event_at": event.event_at.isoformat(timespec="seconds"),
            "day_label": event.day_label,
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
    parser = argparse.ArgumentParser(description="Fetch Haoyou Kuaibao timeline events.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-05-21")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-05-28")
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility; static page is single-page")
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum events to export")
    parser.add_argument("--headful", action="store_true", help="Show browser window when rendering PDFs")
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
    if args.max_pages != 1:
        print("[html] 3839 timeline is a single HTML page; --max-pages is accepted for runner compatibility")

    events = collect_events(since, until)
    if args.limit > 0:
        events = events[: args.limit]
    print(f"[html] exporting {len(events)} event(s)")

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
