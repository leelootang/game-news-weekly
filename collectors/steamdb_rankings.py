"""
Fetch the current Steam global top-sellers ranking and enrich each title with
Gamalytic sales/owner estimates, storing one structured ranking record.

History
-------
This collector previously scraped SteamDB (steamdb.info). SteamDB sits behind a
Cloudflare anti-bot wall and additionally IP-bans scrapers, so automated
collection was blocked every day. It now relies entirely on stable HTTP/JSON
sources:

* Ranking spine  -> Steam store "Top Sellers" search results
  (store.steampowered.com/search/results/?filter=topsellers&json=1). This is the
  closest official equivalent of SteamDB's global top-sellers chart.
* Per-title data -> Gamalytic API (api.gamalytic.com/game/{appid}). Gamalytic is
  the same third-party sales estimator SteamDB used to embed, so we get real
  copiesSold / revenue / owners numbers plus publisher, genres, release date and
  review score in a single call. Hardware and bundles return HTTP 404 from
  Gamalytic and are skipped automatically.
* Live players  -> Steam GetMostPlayedGames (one call, optional enrichment for
  concurrent/peak players stored in each row's detail).

The Gamalytic API key is read from the GAMALYTIC_API_KEY environment variable (or
--gamalytic-key); it is never hard-coded.

The SOURCE_KEY is intentionally kept as "steamdb_rankings" so the runner
registration, section mapping and downstream report ids stay unchanged. The
record `text` (TOP10 markdown table + new-product bullets) and `extra.rows`
(structured per-title data) preserve the original shape so half-manual report
generation keeps working.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from article_store import ARTICLE_JSONL_NAME, data_dir_for, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths

# Console output carries CJK and trademark glyphs; force UTF-8 so logging never
# crashes on a Windows GBK console or when the runner captures subprocess output.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


STEAM_SEARCH_URL = "https://store.steampowered.com/search/results/"
STEAM_TOPSELLERS_PAGE = "https://store.steampowered.com/search/?filter=topsellers"
STEAM_WEEKLY_TOPSELLERS_URL = "https://api.steampowered.com/IStoreTopSellersService/GetWeeklyTopSellers/v1/"
STEAM_WEEKLY_CHART_PAGE = "https://store.steampowered.com/charts/topselling/global"
STEAM_MOST_PLAYED_URL = "https://api.steampowered.com/ISteamChartsService/GetMostPlayedGames/v1/"
GAMALYTIC_GAME_URL = "https://api.gamalytic.com/game/{appid}"

SOURCE_DOMAIN = "store.steampowered.com"
SOURCE_KEY = "steamdb_rankings"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"

# Daily uses the live rolling top-sellers list; weekly/monthly reports use Steam's
# official weekly top-sellers chart (Tuesday-reset), which returns the most recent
# finalized week automatically.
TOP_N_DAILY = 10
TOP_N_WEEKLY = 15
CANDIDATE_POOL = 60  # over-fetch the daily chart so hardware/bundles can be filtered out
WEEKLY_POOL = 30  # over-fetch the weekly chart for the same reason
HTTP_TIMEOUT = 30
HTTP_RETRIES = 3
GAMALYTIC_DELAY = 0.35  # be polite between Gamalytic calls
STEAM_CC = "us"
STEAM_LANG = "english"
LOCAL_TZ = timezone(timedelta(hours=8))
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
ROOT = Path(__file__).resolve().parent.parent


@dataclass
class RankingRow:
    rank: int
    app_id: str
    name: str
    url: str
    price: str = ""
    rating: str = ""
    release: str = ""
    sales: str = ""
    revenue: str = ""
    developer: str = ""
    publisher: str = ""
    genres: str = ""
    change: str = ""
    marker: str = ""
    detail: dict[str, object] = field(default_factory=dict)


# --------------------------------------------------------------------------- #
# Date helpers (kept compatible with the previous collector)
# --------------------------------------------------------------------------- #
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


def report_mode(since: datetime, until: datetime) -> str:
    if since.date() == (until - timedelta(seconds=1)).date():
        return "daily"
    return "periodic"


def daily_launch_window(reference: datetime) -> tuple[datetime, datetime]:
    month_start = reference.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if reference.day < 10:
        if month_start.month == 1:
            month_start = month_start.replace(year=month_start.year - 1, month=12)
        else:
            month_start = month_start.replace(month=month_start.month - 1)
    return month_start, reference.replace(hour=23, minute=59, second=59, microsecond=0)


# --------------------------------------------------------------------------- #
# Manifest IO (unchanged contract)
# --------------------------------------------------------------------------- #
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


def load_dotenv_value(root: Path, key: str) -> str:
    for name in (".env.local", ".env"):
        path = root / name
        if not path.exists():
            continue
        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            env_key, value = line.split("=", 1)
            if env_key.strip() != key:
                continue
            cleaned = value.strip().strip('"').strip("'")
            if cleaned:
                return cleaned
    return ""


def resolve_gamalytic_key(cli_value: str) -> str:
    if cli_value.strip():
        return cli_value.strip()
    env_value = os.environ.get("GAMALYTIC_API_KEY", "").strip()
    if env_value:
        return env_value
    file_value = load_dotenv_value(ROOT, "GAMALYTIC_API_KEY")
    if file_value:
        return file_value
    return ""


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def http_get(url: str, *, headers: dict[str, str] | None = None) -> bytes:
    request_headers = {"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
    if headers:
        request_headers.update(headers)
    last_exc: Exception | None = None
    for attempt in range(1, HTTP_RETRIES + 1):
        try:
            with urlopen(Request(url, headers=request_headers), timeout=HTTP_TIMEOUT) as resp:
                return resp.read()
        except HTTPError as exc:
            # 404 is a real answer (e.g. Gamalytic on hardware); don't retry it.
            if exc.code == 404:
                raise
            last_exc = exc
        except (URLError, TimeoutError) as exc:
            last_exc = exc
        if attempt < HTTP_RETRIES:
            time.sleep(1.0 * attempt)
    raise RuntimeError(f"GET failed after {HTTP_RETRIES} tries: {url} ({last_exc!r})")


def http_get_json(url: str, *, headers: dict[str, str] | None = None) -> dict:
    return json.loads(http_get(url, headers=headers).decode("utf-8", "replace"))


# --------------------------------------------------------------------------- #
# Steam top-sellers ranking spine
# --------------------------------------------------------------------------- #
def fetch_topsellers(pool: int = CANDIDATE_POOL) -> list[tuple[str, str]]:
    """Return [(app_id, name)] in chart order from Steam's Top Sellers search."""
    query = urlencode(
        {
            "query": "",
            "filter": "topsellers",
            "cc": STEAM_CC,
            "l": STEAM_LANG,
            "json": "1",
            "infinite": "1",
            "start": "0",
            "count": str(pool),
        }
    )
    data = http_get_json(f"{STEAM_SEARCH_URL}?{query}")
    html = data.get("results_html") or ""
    if not html:
        raise RuntimeError("Steam top-sellers search returned no results_html")

    results: list[tuple[str, str]] = []
    seen: set[str] = set()
    # Within each result row the app id (data-ds-appid) appears before the title
    # span, so pair each app id with the first title that follows it. A simple
    # split on the row class would misalign names by one row, because the app id
    # attribute precedes class="search_result_row" in the <a> tag.
    for app_id, raw_name in re.findall(
        r'data-ds-appid="(\d+)".*?<span class="title">([^<]+)</span>', html, flags=re.S
    ):
        if app_id in seen:
            continue
        name = re.sub(r"\s+", " ", raw_name).strip()
        if not name:
            continue
        seen.add(app_id)
        results.append((app_id, name))
    if not results:
        raise RuntimeError("Steam top-sellers parser produced zero rows; page structure may have changed")
    return results


def fetch_weekly_topsellers(
    pool: int = WEEKLY_POOL,
) -> tuple[datetime | None, list[tuple[str, str]], dict[str, dict[str, int]]]:
    """Return (week_start, [(app_id, name)], chart_meta) from Steam's official weekly chart.

    `chart_meta` maps app_id -> {"last_week_rank": int|None, "consecutive_weeks": int}.
    `last_week_rank` is absent (None) when the product was NOT on last week's chart,
    which—together with consecutive_weeks==1—is the authoritative signal for a genuine
    new chart entry. This is what drives the "★ 新上榜" marker; we no longer fall back to
    a release-date heuristic when this data is available.

    Uses IStoreTopSellersService/GetWeeklyTopSellers, the same data behind
    store.steampowered.com/charts/topselling. The chart resets on Tuesdays; the
    endpoint always returns the most recent finalized week, exposed as
    `start_date` (epoch seconds for that Tuesday).
    """
    payload = {
        "country_code": STEAM_CC.upper(),
        "context": {"language": STEAM_LANG, "country_code": STEAM_CC.upper(), "steam_realm": 1},
        "data_request": {"include_assets": False, "include_release": True},
        "page_count": pool,
    }
    url = f"{STEAM_WEEKLY_TOPSELLERS_URL}?input_json={quote(json.dumps(payload))}"
    response = http_get_json(url).get("response") or {}
    ranks = response.get("ranks") or []
    if not ranks:
        raise RuntimeError("Steam weekly top-sellers endpoint returned no ranks")

    week_start: datetime | None = None
    start_epoch = response.get("start_date")
    if isinstance(start_epoch, (int, float)) and start_epoch > 0:
        week_start = datetime.fromtimestamp(start_epoch, timezone.utc).replace(tzinfo=None)

    results: list[tuple[str, str]] = []
    chart_meta: dict[str, dict[str, int]] = {}
    seen: set[str] = set()
    for entry in ranks:
        app_id = str(entry.get("appid") or entry.get("item", {}).get("appid") or "")
        if not app_id or app_id in seen:
            continue
        name = re.sub(r"\s+", " ", str(entry.get("item", {}).get("name") or "")).strip()
        if not name:
            continue
        seen.add(app_id)
        results.append((app_id, name))
        lwr = entry.get("last_week_rank")
        chart_meta[app_id] = {
            "last_week_rank": int(lwr) if isinstance(lwr, (int, float)) else None,
            "consecutive_weeks": int(entry.get("consecutive_weeks") or 0),
        }
    return week_start, results, chart_meta


# --------------------------------------------------------------------------- #
# Live concurrent players (optional enrichment)
# --------------------------------------------------------------------------- #
def fetch_player_counts() -> dict[str, dict[str, int]]:
    try:
        data = http_get_json(STEAM_MOST_PLAYED_URL)
    except Exception as exc:  # non-fatal; players are a nice-to-have column
        print(f"[players] skipped: {exc!r}", file=sys.stderr)
        return {}
    out: dict[str, dict[str, int]] = {}
    for rank in data.get("response", {}).get("ranks", []):
        app_id = str(rank.get("appid"))
        out[app_id] = {
            "concurrent": rank.get("concurrent_in_game") or rank.get("last_week_peak") or 0,
            "peak": rank.get("peak_in_game") or 0,
        }
    return out


# --------------------------------------------------------------------------- #
# Gamalytic enrichment
# --------------------------------------------------------------------------- #
def gamalytic_game(app_id: str, api_key: str) -> dict | None:
    """Return Gamalytic record for a Steam app, or None if it is not a game."""
    url = GAMALYTIC_GAME_URL.format(appid=app_id)
    try:
        data = http_get_json(url, headers={"api-key": api_key})
    except HTTPError as exc:
        if exc.code == 404:
            return None  # hardware / bundle / unknown app
        raise
    if data.get("itemType") and data.get("itemType") != "game":
        return None
    return data


# --------------------------------------------------------------------------- #
# Formatting helpers
# --------------------------------------------------------------------------- #
def fmt_count(value: object) -> str:
    try:
        n = int(value)
    except (TypeError, ValueError):
        return ""
    if n <= 0:
        return ""
    if n >= 100_000_000:
        return f"{n / 100_000_000:.2f}亿".replace(".00亿", "亿")
    if n >= 10_000:
        return f"{n / 10_000:.1f}万".replace(".0万", "万")
    return str(n)


def fmt_money(value: object) -> str:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return ""
    if n <= 0:
        return ""
    if n >= 100_000_000:
        return f"${n / 100_000_000:.2f}亿"
    if n >= 10_000:
        return f"${n / 10_000:.1f}万"
    return f"${n:,.0f}"


def fmt_price(value: object) -> str:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return ""
    if n <= 0:
        return "免费"
    return f"${n:.2f}"


def release_datetime(value: object) -> datetime | None:
    try:
        ms = int(value)
    except (TypeError, ValueError):
        return None
    if ms <= 0:
        return None
    return datetime.fromtimestamp(ms / 1000, timezone.utc).replace(tzinfo=None)


def fmt_release(value: object) -> str:
    dt = release_datetime(value)
    return dt.strftime("%Y-%m-%d") if dt else ""


def join_names(value: object, limit: int = 2) -> str:
    if isinstance(value, list):
        names = [str(item).strip() for item in value if str(item).strip()]
        return " / ".join(names[:limit])
    if isinstance(value, str):
        return value.strip()
    return ""


# --------------------------------------------------------------------------- #
# Row construction
# --------------------------------------------------------------------------- #
def build_row(rank: int, app_id: str, steam_name: str, game: dict, players: dict[str, dict[str, int]]) -> RankingRow:
    name = (game.get("name") or steam_name or "").strip() or steam_name
    review_score = game.get("reviewScore")
    rating = f"{int(review_score)}%" if isinstance(review_score, (int, float)) and review_score else ""
    player_stat = players.get(app_id, {})
    detail = {
        "publisher": join_names(game.get("publishers"), limit=3),
        "developer": join_names(game.get("developers"), limit=3),
        "release_date": fmt_release(game.get("releaseDate")),
        "genres": game.get("genres") if isinstance(game.get("genres"), list) else [],
        "tags": game.get("tags")[:6] if isinstance(game.get("tags"), list) else [],
        "review_score": review_score,
        "reviews": game.get("reviews"),
        "copies_sold": game.get("copiesSold"),
        "owners": game.get("owners"),
        "revenue": game.get("revenue"),
        "followers": game.get("followers"),
        "wishlists": game.get("wishlists"),
        "avg_playtime": game.get("avgPlaytime"),
        "price_usd": game.get("price"),
        "concurrent_players": player_stat.get("concurrent"),
        "peak_players": player_stat.get("peak"),
        "estimate_accuracy": game.get("accuracy"),
    }
    return RankingRow(
        rank=rank,
        app_id=app_id,
        name=name,
        url=f"https://store.steampowered.com/app/{app_id}/",
        price=fmt_price(game.get("price")),
        rating=rating,
        release=fmt_release(game.get("releaseDate")),
        sales=fmt_count(game.get("copiesSold")),
        revenue=fmt_money(game.get("revenue")),
        developer=join_names(game.get("developers"), limit=2),
        publisher=join_names(game.get("publishers"), limit=2),
        genres=join_names(game.get("genres"), limit=4),
        detail=detail,
    )


# --------------------------------------------------------------------------- #
# Marker logic
# --------------------------------------------------------------------------- #
def is_current_launch(row: RankingRow, reference: datetime) -> bool:
    released = release_datetime(row.detail.get("release_date_ms") or None)
    if released is None:
        # detail.release_date is already a formatted string; re-parse it
        text = str(row.detail.get("release_date") or row.release or "").strip()
        try:
            released = datetime.strptime(text, "%Y-%m-%d")
        except ValueError:
            return False
    start, end = daily_launch_window(reference)
    return start <= released <= end


def load_previous_appids(out_dir: Path, mode: str, before: datetime) -> set[str]:
    """Read the most recent stored ranking (same mode) before `before`."""
    data_dir = data_dir_for(out_dir)
    jsonl_path = data_dir / ARTICLE_JSONL_NAME
    if not jsonl_path.exists():
        return set()
    best_published = ""
    best_appids: set[str] = set()
    for line in jsonl_path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("source_key") != SOURCE_KEY:
            continue
        extra = row.get("extra") or {}
        if extra.get("mode") != mode:
            continue
        published = str(row.get("published_at") or "")
        try:
            published_dt = datetime.fromisoformat(published.replace("Z", "+00:00")).replace(tzinfo=None)
        except ValueError:
            continue
        if published_dt >= before:
            continue
        if published > best_published:
            best_published = published
            best_appids = {str(r.get("app_id")) for r in extra.get("rows", []) if r.get("app_id")}
    return best_appids


# --------------------------------------------------------------------------- #
# Record text
# --------------------------------------------------------------------------- #
def product_bullet(row: RankingRow, mode: str) -> str:
    publisher = row.publisher or "未列发行商"
    release = row.release or "未列上线时间"
    genres = row.genres or "未列品类"
    sales = row.sales or "暂无销量估算"
    revenue = row.revenue or "暂无营收估算"
    rating = row.rating or "暂无好评率"
    marker = "近期新品" if mode == "daily" else "新上榜"
    return (
        f"- ★ #{row.rank} 《{row.name}》为{marker}，发行商 {publisher}，"
        f"上线 {release}，品类 {genres}，销量约 {sales}，营收约 {revenue}，好评率 {rating}。"
    )


def markdown_table(rows: list[RankingRow]) -> str:
    lines = [
        "| Rank | 标记 | Name | 价格 | 好评率 | 上线 | 销量 | 营收 |",
        "| ---: | --- | --- | --- | --- | --- | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            "| "
            f"{row.rank} | {row.marker or ''} | [{row.name}]({row.url}) | {row.price or '-'} | "
            f"{row.rating or '-'} | {row.release or '-'} | {row.sales or '-'} | {row.revenue or '-'} |"
        )
    return "\n".join(lines)


def build_record_text(
    rows: list[RankingRow],
    mode: str,
    since: datetime,
    until: datetime,
    week_start: datetime | None,
    snapshot_at: datetime,
) -> str:
    marked = [row for row in rows if row.marker]
    top_label = f"TOP{len(rows)}"
    target_day = (until - timedelta(seconds=1)).date()
    note_line = None
    if mode == "daily":
        title = f"Steam 全球热销榜 {top_label}（{target_day} 日报 · 实时榜采集于 {snapshot_at:%Y-%m-%d}）"
        source_line = f"Source: {STEAM_TOPSELLERS_PAGE} (排名) + Gamalytic (销量/营收估算)"
        note_line = (
            f"说明：Steam 日榜无历史查询，此为采集日 {snapshot_at:%Y-%m-%d} 的实时热销榜，"
            f"用于补充 {target_day} 日报。"
        )
    else:
        week_text = f"（周 of {week_start:%Y-%m-%d}，周二重置）" if week_start else ""
        title = f"Steam 官方周销量榜 {top_label}{week_text}"
        source_line = f"Source: {STEAM_WEEKLY_CHART_PAGE} (官方周榜) + Gamalytic (销量/营收估算)"
    lines = [
        title,
        source_line,
        f"Window: {since.isoformat(timespec='seconds')} <= collected < {until.isoformat(timespec='seconds')}",
    ]
    if note_line:
        lines.append(note_line)
    lines.extend(["", "榜单新品信息:"])
    if marked:
        lines.extend(product_bullet(row, mode) for row in marked)
    else:
        lines.append(f"- 本次 {top_label} 未识别到符合规则的新品/新上榜产品。")
    lines.extend(["", f"{top_label} 表格:", markdown_table(rows)])
    return "\n".join(lines).rstrip()


# --------------------------------------------------------------------------- #
# Collection
# --------------------------------------------------------------------------- #
def collect_rankings(
    since: datetime, until: datetime, api_key: str, out_dir: Path, snapshot_at: datetime
) -> tuple[str, list[RankingRow], datetime | None]:
    mode = report_mode(since, until)
    week_start: datetime | None = None
    chart_meta: dict[str, dict[str, int]] = {}
    if mode == "daily":
        top_n = TOP_N_DAILY
        print(f"[list] fetch daily top sellers: {STEAM_TOPSELLERS_PAGE}")
        candidates = fetch_topsellers()
    else:
        top_n = TOP_N_WEEKLY
        print(f"[list] fetch weekly top sellers: {STEAM_WEEKLY_CHART_PAGE}")
        week_start, candidates, chart_meta = fetch_weekly_topsellers()
        if week_start:
            print(f"[list] weekly chart week of {week_start:%Y-%m-%d} (Tuesday reset)")
    print(f"[list] {len(candidates)} chart entries before filtering (target TOP{top_n})")
    players = fetch_player_counts()

    rows: list[RankingRow] = []
    for app_id, steam_name in candidates:
        if len(rows) >= top_n:
            break
        try:
            game = gamalytic_game(app_id, api_key)
        except Exception as exc:
            print(f"[gamalytic] {app_id} {steam_name}: {exc!r}", file=sys.stderr)
            continue
        if game is None:
            print(f"[skip] {app_id} {steam_name}: not a game (hardware/bundle)")
            continue
        rank = len(rows) + 1
        row = build_row(rank, app_id, steam_name, game, players)
        rows.append(row)
        print(f"[row] #{rank} {row.name} sales={row.sales or '-'} revenue={row.revenue or '-'}")
        time.sleep(GAMALYTIC_DELAY)

    if not rows:
        raise RuntimeError("No games resolved from the Steam top-sellers chart via Gamalytic")

    if mode == "daily":
        # The Steam daily top-sellers list has no historical query: it always
        # returns the live chart at run time. Reports are produced "today for
        # yesterday", so this live snapshot (captured on snapshot_at) is filed
        # under the target day as a supplement. Use the capture date as the
        # launch-window reference, since that is what the list actually reflects.
        reference = snapshot_at
        for row in rows:
            row.marker = "★ 近期新品" if is_current_launch(row, reference) else ""
    else:
        # Preferred: the official weekly chart exposes last_week_rank /
        # consecutive_weeks per entry. A genuine new chart entry has no
        # last_week_rank (and consecutive_weeks == 1). Persist both onto each row
        # so the table can show last-week movement; only mark true new entries.
        reference = week_start or (until - timedelta(seconds=1))
        previous = load_previous_appids(out_dir, mode, since)  # legacy fallback only
        have_chart_meta = bool(chart_meta)
        for row in rows:
            meta = chart_meta.get(row.app_id, {})
            lwr = meta.get("last_week_rank")
            consec = meta.get("consecutive_weeks")
            row.detail["last_week_rank"] = lwr
            row.detail["consecutive_weeks"] = consec
            if have_chart_meta:
                is_new = (lwr is None) or (consec == 1)
            elif previous:
                is_new = row.app_id not in previous
            else:
                # last resort when neither chart meta nor a prior snapshot exists
                is_new = is_current_launch(row, reference)
            row.marker = "★ 新上榜" if is_new else ""
            row.change = "new" if is_new else (f"上周{lwr}" if lwr is not None else "")
    return mode, rows, week_start


def record_id(mode: str, since: datetime, until: datetime) -> str:
    if mode == "daily":
        return f"steamdb_rankings_daily_{since:%Y-%m-%d}"
    return f"steamdb_rankings_periodic_{since:%Y-%m-%d}_to_{(until - timedelta(seconds=1)):%Y-%m-%d}"


def title_for(
    mode: str, since: datetime, until: datetime, week_start: datetime | None, snapshot_at: datetime
) -> str:
    if mode == "daily":
        target_day = (until - timedelta(seconds=1)).date()
        return f"Steam 全球热销榜 TOP{TOP_N_DAILY}（{target_day} 日报 · 采集于 {snapshot_at:%Y-%m-%d}）"
    if week_start:
        return f"Steam 官方周销量榜 TOP{TOP_N_WEEKLY}（周 of {week_start:%Y-%m-%d}）"
    return f"Steam 官方周销量榜 TOP{TOP_N_WEEKLY}（{since:%Y-%m-%d} 至 {(until - timedelta(seconds=1)):%Y-%m-%d}）"


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Steam top-sellers ranking enriched with Gamalytic data.")
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
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum rows to keep for debugging")
    parser.add_argument("--headful", action="store_true", help="Accepted for runner compatibility (no longer used)")
    parser.add_argument(
        "--gamalytic-key",
        type=str,
        default="",
        help="Gamalytic API key; falls back to GAMALYTIC_API_KEY env var.",
    )
    args = parser.parse_args()

    api_key = resolve_gamalytic_key(args.gamalytic_key)
    if not api_key:
        raise SystemExit(
            "Gamalytic API key missing. Set GAMALYTIC_API_KEY in the environment, "
            "store it in .env.local/.env, or pass --gamalytic-key."
        )

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
    started = time.monotonic()
    print(f"[config] window: {since} <= collected < {until}")
    print(f"[config] output: {args.out.resolve()}")

    snapshot_at = datetime.now().replace(microsecond=0)
    mode, rows, week_start = collect_rankings(since, until, api_key, args.out, snapshot_at)
    if args.limit > 0:
        rows = rows[: args.limit]
    text = build_record_text(rows, mode, since, until, week_start, snapshot_at)
    item_id = record_id(mode, since, until)
    ranking_source = (
        "store.steampowered.com/search?filter=topsellers"
        if mode == "daily"
        else "IStoreTopSellersService/GetWeeklyTopSellers"
    )
    source_url = STEAM_TOPSELLERS_PAGE if mode == "daily" else STEAM_WEEKLY_CHART_PAGE
    write_article_record(
        args.out,
        manifest,
        item_id,
        {
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "section": "pc_rankings",
            "title": title_for(mode, since, until, week_start, snapshot_at),
            "url": source_url,
            "published_at": (until - timedelta(seconds=1)).isoformat(timespec="seconds"),
            "text": text,
            "extra": {
                "mode": mode,
                "top_n": len(rows),
                "marked_count": sum(1 for row in rows if row.marker),
                "snapshot_at": snapshot_at.isoformat(timespec="seconds"),
                "snapshot_date": snapshot_at.strftime("%Y-%m-%d"),
                "is_supplement": mode == "daily" and snapshot_at.date() != (until - timedelta(seconds=1)).date(),
                "week_start": week_start.strftime("%Y-%m-%d") if week_start else None,
                "ranking_source": ranking_source,
                "enrichment_source": "api.gamalytic.com",
                "rows": [
                    {
                        "rank": row.rank,
                        "app_id": row.app_id,
                        "name": row.name,
                        "url": row.url,
                        "marker": row.marker,
                        "change": row.change,
                        "price": row.price,
                        "rating": row.rating,
                        "release": row.release,
                        "sales": row.sales,
                        "revenue": row.revenue,
                        "developer": row.developer,
                        "publisher": row.publisher,
                        "genres": row.genres,
                        "detail": row.detail,
                    }
                    for row in rows
                ],
            },
        },
    )
    save_manifest(args.out, manifest)
    elapsed = time.monotonic() - started
    print(f"[done] ok=1 fail=0 mode={mode} rows={len(rows)} marked={sum(1 for row in rows if row.marker)} elapsed={elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
