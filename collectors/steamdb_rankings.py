"""
Fetch SteamDB PC bestseller rankings and store one structured ranking record.

Daily windows use the live global top sellers page and mark current-month
launches. Multi-day windows use the weekly top sellers page and mark products
whose change implies they were outside last week's top 10.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin

from article_store import write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright


BASE_URL = "https://steamdb.info"
DAILY_URL = f"{BASE_URL}/stats/globaltopsellers/"
WEEKLY_URL = f"{BASE_URL}/topsellers/"
SOURCE_DOMAIN = "steamdb.info"
SOURCE_KEY = "steamdb_rankings"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
TOP_N = 10
PAGE_TIMEOUT = 45_000
DETAIL_DELAY = 0.7
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass
class RankingRow:
    rank: int
    app_id: str
    name: str
    url: str
    price: str = ""
    rating: str = ""
    release: str = ""
    follows: str = ""
    online: str = ""
    peak: str = ""
    change: str = ""
    developer: str = ""
    marker: str = ""
    detail: dict[str, str | list[str]] = field(default_factory=dict)


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


def report_mode(since: datetime, until: datetime) -> str:
    if since.date() == (until - timedelta(seconds=1)).date():
        return "daily"
    return "periodic"


def parse_release_date(value: str, *, reference: datetime) -> datetime | None:
    text = re.sub(r"\s+", " ", value or "").strip()
    if not text or text in {"-", "—"}:
        return None
    formats = [
        "%d %B %Y",
        "%d %b %Y",
        "%B %Y",
        "%b %Y",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            parsed = datetime.strptime(text, fmt)
            if fmt in {"%B %Y", "%b %Y"}:
                parsed = parsed.replace(day=1)
            return parsed
        except ValueError:
            pass
    match = re.search(
        r"\b(\d{1,2})\s+([A-Za-z]+)\s+(20\d{2})\b|"
        r"\b([A-Za-z]+)\s+(20\d{2})\b|"
        r"\b([A-Za-z]{3})\s+(20\d{2})\b",
        text,
    )
    if match:
        return parse_release_date(match.group(0), reference=reference)
    match = re.fullmatch(r"([A-Za-z]{3,9})\s+(\d{4})", text)
    if match:
        return parse_release_date(match.group(0), reference=reference)
    return None


def daily_launch_window(reference: datetime) -> tuple[datetime, datetime]:
    month_start = reference.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if reference.day < 10:
        if month_start.month == 1:
            month_start = month_start.replace(year=month_start.year - 1, month=12)
        else:
            month_start = month_start.replace(month=month_start.month - 1)
    return month_start, reference.replace(hour=23, minute=59, second=59, microsecond=0)


def is_current_launch(row: RankingRow, reference: datetime) -> bool:
    released_at = parse_release_date(str(row.detail.get("release_date") or row.release), reference=reference)
    if not released_at:
        return False
    start, end = daily_launch_window(reference)
    return start <= released_at <= end


def change_number(value: str) -> int | None:
    text = re.sub(r"\s+", " ", value or "").strip()
    match = re.search(r"\d+", text)
    return int(match.group(0)) if match else None


def is_new_topn(row: RankingRow) -> bool:
    text = re.sub(r"\s+", " ", row.change or "").strip().lower()
    if text in {"new", "re-entry", "reentry"}:
        return True
    moved = change_number(text)
    if moved is None:
        return False
    return row.rank + moved > TOP_N


def is_steamdb_challenge(text: str) -> bool:
    normalized = re.sub(r"\s+", " ", text or "").strip().lower()
    return (
        "checking your browser" in normalized
        or "enable javascript and cookies to continue" in normalized
        or "cf-error" in normalized
    )


async def rows_from_daily_page(page) -> list[RankingRow]:
    rows = await page.evaluate(
        """() => {
            const table = document.querySelector('table');
            if (!table) return [];
            return [...table.querySelectorAll('tbody tr')].slice(0, 10).map(tr => {
                const cells = [...tr.querySelectorAll('td, th')].map(td => ({
                    text: (td.innerText || td.textContent || '').trim(),
                    html: td.innerHTML || ''
                }));
                const link = tr.querySelector('a[href^="/app/"]');
                return {
                    cells,
                    href: link ? link.getAttribute('href') : '',
                    name: link ? (link.innerText || link.textContent || '').trim() : ''
                };
            });
        }"""
    )
    parsed: list[RankingRow] = []
    for item in rows:
        cells = [re.sub(r"\s+", " ", cell.get("text", "")).strip() for cell in item.get("cells", [])]
        rank_match = re.search(r"\d+", cells[0] if cells else "")
        href = item.get("href") or ""
        app_match = re.search(r"/app/(\d+)", href)
        name = item.get("name") or (cells[1] if len(cells) > 1 else "")
        if not rank_match or not app_match or not name:
            continue
        data = cells[2:]
        parsed.append(
            RankingRow(
                rank=int(rank_match.group(0)),
                app_id=app_match.group(1),
                name=name,
                url=urljoin(BASE_URL, href),
                price=data[0] if len(data) > 0 else "",
                rating=data[1] if len(data) > 1 else "",
                release=data[2] if len(data) > 2 else "",
                follows=data[3] if len(data) > 3 else "",
                online=data[4] if len(data) > 4 else "",
                peak=data[5] if len(data) > 5 else "",
            )
        )
    return parsed[:TOP_N]


async def rows_from_weekly_page(page) -> list[RankingRow]:
    rows = await page.evaluate(
        """() => {
            const table = document.querySelector('table');
            if (!table) return [];
            return [...table.querySelectorAll('tbody tr')].slice(0, 10).map(tr => {
                const cells = [...tr.querySelectorAll('td, th')].map(td => ({
                    text: (td.innerText || td.textContent || '').trim(),
                    html: td.innerHTML || '',
                    cls: td.className || ''
                }));
                const link = tr.querySelector('a[href^="/app/"]');
                return {
                    cells,
                    href: link ? link.getAttribute('href') : '',
                    name: link ? (link.innerText || link.textContent || '').trim() : ''
                };
            });
        }"""
    )
    parsed: list[RankingRow] = []
    for item in rows:
        cells = [re.sub(r"\s+", " ", cell.get("text", "")).strip() for cell in item.get("cells", [])]
        rank_match = re.search(r"\d+", cells[0] if cells else "")
        href = item.get("href") or ""
        app_match = re.search(r"/app/(\d+)", href)
        name = item.get("name") or (cells[1] if len(cells) > 1 else "")
        if not rank_match or not app_match or not name:
            continue
        tail = cells[2:]
        release = tail[-1] if tail else ""
        developer = tail[-2] if len(tail) >= 2 else ""
        change = " ".join(tail[:-2]).strip() if len(tail) > 2 else ""
        parsed.append(
            RankingRow(
                rank=int(rank_match.group(0)),
                app_id=app_match.group(1),
                name=name,
                url=urljoin(BASE_URL, href),
                change=change,
                developer=developer,
                release=release,
            )
        )
    return parsed[:TOP_N]


def regex_value(text: str, label: str) -> str:
    match = re.search(rf"^{re.escape(label)}\s+(.+)$", text, flags=re.MULTILINE)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""


async def fetch_detail(context, row: RankingRow) -> dict[str, str | list[str]]:
    page = await context.new_page()
    url = f"{BASE_URL}/app/{row.app_id}/charts/"
    try:
        print(f"[detail] open {row.rank}. {row.name} {url}")
        await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        body_text = await page.locator("body").inner_text(timeout=10_000)
        if is_steamdb_challenge(body_text):
            raise RuntimeError(
                "SteamDB returned a browser verification challenge; automated detail collection is blocked."
            )
        try:
            await page.wait_for_selector("h1", timeout=15_000)
        except PWTimeout:
            pass
        return await page.evaluate(
            """() => {
                const text = document.body.innerText || '';
                const links = [...document.querySelectorAll('a')];
                const tags = links
                    .filter(a => /^\\/tag\\//.test(a.getAttribute('href') || ''))
                    .map(a => (a.innerText || a.textContent || '').trim())
                    .filter(Boolean);
                const review = links
                    .map(a => (a.innerText || a.textContent || '').trim())
                    .find(t => /%\\s+.*reviews?/i.test(t)) || '';
                function afterHeading(heading) {
                    const idx = text.indexOf(heading);
                    if (idx < 0) return [];
                    const rest = text.slice(idx + heading.length).split(/\\n(?=##|###|How many players|SteamDB does not own)/)[0];
                    return rest.split('\\n').map(s => s.trim()).filter(Boolean);
                }
                function value(label) {
                    const escaped = label.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
                    const m = text.match(new RegExp('^' + escaped + '\\\\s+(.+)$', 'm'));
                    return m ? m[1].replace(/\\s+/g, ' ').trim() : '';
                }
                return {
                    title: (document.querySelector('h1')?.innerText || '').trim(),
                    publisher: value('Publisher'),
                    developer: value('Developer'),
                    release_date: value('Release Date') || value('Steam Release Date') || value('Store Release Date'),
                    primary_genre: value('Primary Genre'),
                    store_genres: value('Store Genres'),
                    review: review,
                    owners: afterHeading('Owner estimations').filter(s => /^~/.test(s)),
                    review_breakdown: afterHeading('User reviews history').slice(0, 4),
                    tags: [...new Set(tags)].slice(0, 6),
                    page_text: text
                };
            }"""
        )
    except Exception as exc:
        print(f"[detail] failed {row.name}: {exc!r}", file=sys.stderr)
        return {}
    finally:
        await page.close()


def clean_detail_value(value: str) -> str:
    text = re.sub(r"\s+", " ", value or "").strip()
    text = re.sub(r"\s*\(\)\s*$", "", text)
    return text


def detail_field(row: RankingRow, key: str, fallback: str = "") -> str:
    value = row.detail.get(key)
    if isinstance(value, str):
        return clean_detail_value(value)
    return fallback


def detail_tags(row: RankingRow) -> str:
    tags = row.detail.get("tags")
    if isinstance(tags, list) and tags:
        return " / ".join(str(tag) for tag in tags[:4])
    genre = detail_field(row, "store_genres") or detail_field(row, "primary_genre")
    return genre


def owners_text(row: RankingRow) -> str:
    owners = row.detail.get("owners")
    if isinstance(owners, list) and owners:
        return "；".join(str(item) for item in owners[:3])
    return ""


def preferred_sales_text(row: RankingRow) -> str:
    owners = row.detail.get("owners")
    if not isinstance(owners, list) or not owners:
        return ""
    ordered_names = ("gamalytic", "vg insights")
    normalized = [str(item).strip() for item in owners if str(item).strip()]
    def sales_only(item: str) -> str:
        text = re.sub(r"\s+by\s+.+$", "", item, flags=re.I).strip()
        return re.sub(r"^~\s*", "", text).strip()

    for source_name in ordered_names:
        for item in normalized:
            if source_name in item.lower():
                return sales_only(item)
    return sales_only(normalized[0])


def rating_text(row: RankingRow) -> str:
    review = detail_field(row, "review") or row.rating
    if review:
        return review
    breakdown = row.detail.get("review_breakdown")
    if isinstance(breakdown, list) and breakdown:
        return "；".join(str(item) for item in breakdown[:2])
    return ""


def product_bullet(row: RankingRow, mode: str) -> str:
    publisher = detail_field(row, "publisher") or "SteamDB未列发行商"
    release_date = detail_field(row, "release_date") or row.release or "SteamDB未列上线时间"
    tags = detail_tags(row) or "SteamDB未列品类"
    sales = preferred_sales_text(row) or "暂无销量估算"
    rating = rating_text(row) or "暂无好评率"
    marker = "近期新品" if mode == "daily" else "新上榜"
    return (
        f"- ★ #{row.rank} 《{row.name}》为{marker}，发行商 {publisher}，"
        f"上线时间 {release_date}，品类 {tags}，销量约 {sales}，好评率/评价：{rating}。"
    )


def markdown_table(rows: list[RankingRow], mode: str) -> str:
    if mode == "daily":
        lines = [
            "| Rank | 标记 | Name | Price | Rating | Release | Online | Peak |",
            "| ---: | --- | --- | --- | --- | --- | ---: | ---: |",
        ]
        for row in rows:
            lines.append(
                "| "
                f"{row.rank} | {row.marker} | [{row.name}]({row.url}) | {row.price or '-'} | "
                f"{row.rating or '-'} | {row.release or '-'} | {row.online or '-'} | {row.peak or '-'} |"
            )
        return "\n".join(lines)

    lines = [
        "| Rank | 标记 | Name | Change | Developer | Release Date |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| "
            f"{row.rank} | {row.marker} | [{row.name}]({row.url}) | {row.change or '-'} | "
            f"{row.developer or '-'} | {row.release or '-'} |"
        )
    return "\n".join(lines)


def build_record_text(rows: list[RankingRow], mode: str, source_url: str, since: datetime, until: datetime) -> str:
    marked = [row for row in rows if row.marker]
    title = "SteamDB 当前全球热销榜 TOP10" if mode == "daily" else "SteamDB 周度全球热销榜 TOP10"
    lines = [
        title,
        f"Source page: {source_url}",
        f"Window: {since.isoformat(timespec='seconds')} <= collected < {until.isoformat(timespec='seconds')}",
        "",
        "榜单新品信息:",
    ]
    if marked:
        lines.extend(product_bullet(row, mode) for row in marked)
    else:
        lines.append("- 本次 TOP10 未识别到符合规则的新品/新上榜产品。")
    lines.extend(["", "TOP10 表格:", markdown_table(rows, mode)])
    return "\n".join(lines).rstrip()


async def collect_rankings(since: datetime, until: datetime, *, headful: bool = False) -> tuple[str, list[RankingRow]]:
    mode = report_mode(since, until)
    source_url = DAILY_URL if mode == "daily" else WEEKLY_URL
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headful)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            locale="en-US",
            timezone_id="Asia/Shanghai",
            viewport={"width": 1280, "height": 900},
        )
        page = await context.new_page()
        print(f"[list] open {source_url}")
        await page.goto(source_url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        body_text = await page.locator("body").inner_text(timeout=10_000)
        if is_steamdb_challenge(body_text):
            raise RuntimeError(
                "SteamDB returned a browser verification challenge; automated ranking collection is blocked."
            )
        try:
            await page.wait_for_selector("table tbody tr", timeout=20_000)
        except PWTimeout as exc:
            raise RuntimeError("SteamDB ranking table was not found; site structure may have changed") from exc
        rows = await (rows_from_daily_page(page) if mode == "daily" else rows_from_weekly_page(page))
        await page.close()
        if not rows:
            raise RuntimeError("SteamDB ranking parser returned zero rows")

        candidates = rows if mode == "daily" else [row for row in rows if is_new_topn(row)]
        if mode == "daily":
            # Detail pages are needed before current-month matching because the
            # list only carries month-level release dates.
            candidates = rows
        for row in candidates:
            row.detail = await fetch_detail(context, row)
            await asyncio.sleep(DETAIL_DELAY)

        reference = since if mode == "daily" else until - timedelta(seconds=1)
        for row in rows:
            if mode == "daily":
                row.marker = "★ 近期新品" if is_current_launch(row, reference) else ""
            else:
                row.marker = "★ 新上榜" if is_new_topn(row) else ""
        await context.close()
        await browser.close()
    return mode, rows


def record_id(mode: str, since: datetime, until: datetime) -> str:
    if mode == "daily":
        return f"steamdb_rankings_daily_{since:%Y-%m-%d}"
    return f"steamdb_rankings_periodic_{since:%Y-%m-%d}_to_{(until - timedelta(seconds=1)):%Y-%m-%d}"


def title_for(mode: str, since: datetime, until: datetime) -> str:
    if mode == "daily":
        return f"SteamDB 当前全球热销榜 TOP10（{since:%Y-%m-%d}）"
    return f"SteamDB 周度全球热销榜 TOP10（{since:%Y-%m-%d} 至 {(until - timedelta(seconds=1)):%Y-%m-%d}）"


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch SteamDB bestseller rankings.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="yesterday",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-06-01")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-06-02")
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility")
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum rows to keep from TOP10 for debugging")
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
    if args.max_pages != 1:
        print("[config] SteamDB rankings are single ranking pages; --max-pages is accepted for compatibility")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    started = time.monotonic()
    print(f"[config] window: {since} <= collected < {until}")
    print(f"[config] output: {args.out.resolve()}")

    mode, rows = asyncio.run(collect_rankings(since, until, headful=args.headful))
    if args.limit > 0:
        rows = rows[: args.limit]
    source_url = DAILY_URL if mode == "daily" else WEEKLY_URL
    text = build_record_text(rows, mode, source_url, since, until)
    item_id = record_id(mode, since, until)
    write_article_record(
        args.out,
        manifest,
        item_id,
        {
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "section": "pc_rankings",
            "title": title_for(mode, since, until),
            "url": source_url,
            "published_at": (until - timedelta(seconds=1)).isoformat(timespec="seconds"),
            "text": text,
            "extra": {
                "mode": mode,
                "top_n": len(rows),
                "marked_count": sum(1 for row in rows if row.marker),
                "rows": [
                    {
                        "rank": row.rank,
                        "app_id": row.app_id,
                        "name": row.name,
                        "url": row.url,
                        "marker": row.marker,
                        "change": row.change,
                        "release": row.release,
                        "detail": row.detail,
                    }
                    for row in rows
                ],
            },
        },
    )
    save_manifest(args.out, manifest)
    elapsed = time.monotonic() - started
    print(f"[done] ok=1 fail=0 mode={mode} marked={sum(1 for row in rows if row.marker)} elapsed={elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
