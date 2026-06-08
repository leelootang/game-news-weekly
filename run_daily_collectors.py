"""
Run all configured news collectors for the AI game industry report pipeline.

Daily 08:00 usage:
    python run_daily_collectors.py --preset yesterday

Debug one source:
    python run_daily_collectors.py --collectors gcores --preset today --limit 1
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = ROOT / "news_data"
LEGACY_LOG_DIR = ROOT / "collector_logs"
RUN_SUMMARY_FILENAME = "run_summary.md"
RUN_SUMMARY_JSON_FILENAME = "run_summary.json"
COLLECTOR_RUNS_RETENTION_DAYS = 90
LEGACY_LOG_RETENTION_DAYS = 30

SECTION_ALIASES = {
    "market_news": "industry_news",
    "ai_news": "ai_trends",
    "product_launches": "release_calendar",
    "newsletter": "deep_analysis",
    "player_discourse": "community_discourse",
    "rankings": "pc_rankings",
    "pc_rankings": "pc_rankings",
}


@dataclass(frozen=True)
class Collector:
    key: str
    script: Path
    section: str = "industry_news"
    default_max_pages: int = 8


@dataclass
class ProgressRow:
    section: str
    collector: str
    status: str = "pending"
    articles: int | None = None
    elapsed: float = 0.0
    message: str = ""


COLLECTORS: dict[str, Collector] = {
    "gcores": Collector(
        key="gcores",
        script=ROOT / "collectors" / "gcores.py",
        section="industry_news",
        default_max_pages=8,
    ),
    "gamelook": Collector(
        key="gamelook",
        script=ROOT / "collectors" / "gamelook.py",
        section="industry_news",
        default_max_pages=5,
    ),
    "cgames": Collector(
        key="cgames",
        script=ROOT / "collectors" / "cgames.py",
        section="industry_news",
        default_max_pages=3,
    ),
    "youxiputao_sohu": Collector(
        key="youxiputao_sohu",
        script=ROOT / "collectors" / "youxiputao_sohu.py",
        section="industry_news",
        default_max_pages=3,
    ),
    "youxituoluo": Collector(
        key="youxituoluo",
        script=ROOT / "collectors" / "youxituoluo.py",
        section="industry_news",
        default_max_pages=3,
    ),
    "youxichaguan": Collector(
        key="youxichaguan",
        script=ROOT / "collectors" / "youxichaguan.py",
        section="industry_news",
        default_max_pages=5,
    ),
    "yystv": Collector(
        key="yystv",
        script=ROOT / "collectors" / "yystv.py",
        section="industry_news",
        default_max_pages=5,
    ),
    "youxixinzhi_qqnews": Collector(
        key="youxixinzhi_qqnews",
        script=ROOT / "collectors" / "youxixinzhi_qqnews.py",
        section="industry_news",
        default_max_pages=5,
    ),
    "gamesindustry": Collector(
        key="gamesindustry",
        script=ROOT / "collectors" / "gamesindustry.py",
        section="industry_news",
        default_max_pages=1,
    ),
    "pocketgamer": Collector(
        key="pocketgamer",
        script=ROOT / "collectors" / "pocketgamer.py",
        section="industry_news",
        default_max_pages=1,
    ),
    "gamedeveloper": Collector(
        key="gamedeveloper",
        script=ROOT / "collectors" / "gamedeveloper.py",
        section="industry_news",
        default_max_pages=1,
    ),
    "mobilegamer": Collector(
        key="mobilegamer",
        script=ROOT / "collectors" / "mobilegamer.py",
        section="industry_news",
        default_max_pages=1,
    ),
    "investgame": Collector(
        key="investgame",
        script=ROOT / "collectors" / "investgame.py",
        section="industry_news",
        default_max_pages=1,
    ),
    "vgc": Collector(
        key="vgc",
        script=ROOT / "collectors" / "vgc.py",
        section="industry_news",
        default_max_pages=12,
    ),
    "dataeye_36kr": Collector(
        key="dataeye_36kr",
        script=ROOT / "collectors" / "dataeye_36kr.py",
        section="industry_news",
        default_max_pages=3,
    ),
    "aihot": Collector(
        key="aihot",
        script=ROOT / "collectors" / "aihot.py",
        section="ai_trends",
        default_max_pages=1,
    ),
    "gamediscover": Collector(
        key="gamediscover",
        script=ROOT / "collectors" / "gamediscover.py",
        section="deep_analysis",
        default_max_pages=1,
    ),
    "naavik_digest": Collector(
        key="naavik_digest",
        script=ROOT / "collectors" / "naavik_digest.py",
        section="deep_analysis",
        default_max_pages=1,
    ),
    "thegamebusiness": Collector(
        key="thegamebusiness",
        script=ROOT / "collectors" / "thegamebusiness.py",
        section="deep_analysis",
        default_max_pages=1,
    ),
    "deconstructor_deconstructions": Collector(
        key="deconstructor_deconstructions",
        script=ROOT / "collectors" / "deconstructor_deconstructions.py",
        section="deep_analysis",
        default_max_pages=1,
    ),
    "ceshibiao_17173": Collector(
        key="ceshibiao_17173",
        script=ROOT / "collectors" / "ceshibiao_17173.py",
        section="release_calendar",
        default_max_pages=5,
    ),
    "wanjiang_16p_newgame": Collector(
        key="wanjiang_16p_newgame",
        script=ROOT / "collectors" / "wanjiang_16p_newgame.py",
        section="release_calendar",
        default_max_pages=5,
    ),
    "haoyou_kuaibao_3839": Collector(
        key="haoyou_kuaibao_3839",
        script=ROOT / "collectors" / "haoyou_kuaibao_3839.py",
        section="release_calendar",
        default_max_pages=1,
    ),
    "taptap_app_calendar": Collector(
        key="taptap_app_calendar",
        script=ROOT / "collectors" / "taptap_app_calendar.py",
        section="release_calendar",
        default_max_pages=1,
    ),
    "gematsu_release_dates": Collector(
        key="gematsu_release_dates",
        script=ROOT / "collectors" / "gematsu_release_dates.py",
        section="release_calendar",
        default_max_pages=1,
    ),
    "steamdb_rankings": Collector(
        key="steamdb_rankings",
        script=ROOT / "collectors" / "steamdb_rankings.py",
        section="pc_rankings",
        default_max_pages=1,
    ),
    "nga_mobile_gossip": Collector(
        key="nga_mobile_gossip",
        script=ROOT / "collectors" / "nga_mobile_gossip.py",
        section="community_discourse",
        default_max_pages=8,
    ),
    "reddit_gaming_rising": Collector(
        key="reddit_gaming_rising",
        script=ROOT / "collectors" / "reddit_gaming_rising.py",
        section="community_discourse",
        default_max_pages=5,
    ),
}


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def parse_collectors(value: str) -> list[Collector]:
    if value.strip().lower() == "all":
        return list(COLLECTORS.values())

    selected: list[Collector] = []
    unknown: list[str] = []
    for key in [part.strip() for part in value.split(",") if part.strip()]:
        collector = COLLECTORS.get(key)
        if collector:
            selected.append(collector)
        else:
            unknown.append(key)

    if unknown:
        known = ", ".join(sorted(COLLECTORS))
        raise SystemExit(f"Unknown collector(s): {', '.join(unknown)}. Known: {known}")
    return selected


def parse_sections(value: str) -> set[str] | None:
    raw = value.strip()
    if not raw or raw.lower() == "all":
        return None
    requested = {
        SECTION_ALIASES.get(part.strip(), part.strip())
        for part in raw.split(",")
        if part.strip()
    }
    known = {collector.section for collector in COLLECTORS.values()}
    unknown = sorted(requested - known)
    if unknown:
        raise SystemExit(f"Unknown section(s): {', '.join(unknown)}. Known: {', '.join(sorted(known))}")
    return requested


def filter_collectors_by_section(collectors: list[Collector], sections: set[str] | None) -> list[Collector]:
    if sections is None:
        return collectors
    selected = [collector for collector in collectors if collector.section in sections]
    if not selected:
        raise SystemExit(f"No collectors matched section filter: {', '.join(sorted(sections))}")
    return selected


def parse_runner_date(value: str) -> datetime:
    raw = value.strip()
    if not raw:
        raise ValueError("date value is empty")
    if len(raw) == 10:
        return datetime.fromisoformat(raw)
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).replace(tzinfo=None)


def runner_window(args: argparse.Namespace) -> tuple[datetime, datetime]:
    now = datetime.now().replace(microsecond=0)
    today = now.replace(hour=0, minute=0, second=0)

    if args.since or args.until:
        if not args.since or not args.until:
            raise SystemExit("--since and --until must be provided together for dated output folders")
        return parse_runner_date(args.since), parse_runner_date(args.until)

    if args.preset == "yesterday":
        return today - timedelta(days=1), today
    if args.preset == "today":
        return today, now
    if args.preset == "last-7-days":
        return now - timedelta(days=7), now
    raise SystemExit(f"Unsupported preset: {args.preset}")


def output_folder_name(since: datetime, until: datetime) -> str:
    if since.date() == until.date():
        return since.strftime("%Y-%m-%d")
    if since.time() == datetime.min.time() and until == since + timedelta(days=1):
        return since.strftime("%Y-%m-%d")
    return f"{since.strftime('%Y-%m-%d')}_to_{until.strftime('%Y-%m-%d')}"


def resolve_output_folder_name(args: argparse.Namespace) -> str:
    since, until = runner_window(args)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")
    return output_folder_name(since, until)


def build_command(args: argparse.Namespace, collector: Collector) -> list[str]:
    collector_out = args.out / collector.section / args.output_folder_name
    command = [
        sys.executable,
        str(collector.script),
        "--out",
        str(collector_out),
        "--max-pages",
        str(args.max_pages or collector.default_max_pages),
    ]

    if args.since or args.until:
        if args.since:
            command.extend(["--since", args.since])
        if args.until:
            command.extend(["--until", args.until])
    else:
        command.extend(["--preset", args.preset])

    if args.limit:
        command.extend(["--limit", str(args.limit)])
    if args.headful:
        command.append("--headful")
    return command


class ProgressPanel:
    def __init__(self, collectors: list[Collector], *, enabled: bool = True) -> None:
        self.rows = {
            collector.key: ProgressRow(section=collector.section, collector=collector.key)
            for collector in collectors
        }
        self.total = len(collectors)
        self.enabled = enabled
        self.interactive = enabled and sys.stdout.isatty()
        self.started_at = time.monotonic()
        self.current_section = ""
        self.current_collector = ""
        self.completed = 0
        self.failed = 0
        self.last_render = 0.0
        self._lock = threading.Lock()

    def start(self, collector: Collector) -> None:
        with self._lock:
            row = self.rows[collector.key]
            row.status = "running"
            row.message = "starting"
            row.elapsed = 0.0
            self.current_section = collector.section
            self.current_collector = collector.key
            self._update_counts()
            self.render(force=True)

    def message(self, collector: Collector, line: str) -> None:
        with self._lock:
            row = self.rows[collector.key]
            row.message = shorten(line.strip(), 88)
            self.render()

    def finish(self, collector: Collector, *, status: str, articles: int, elapsed: float) -> None:
        with self._lock:
            row = self.rows[collector.key]
            row.status = status
            row.articles = articles
            row.elapsed = elapsed
            row.message = f"articles={articles}"
            self._update_counts()
            self.render(force=True)

    def render(self, *, force: bool = False) -> None:
        if not self.enabled:
            return
        now = time.monotonic()
        if not force and now - self.last_render < 0.25:
            return
        self.last_render = now
        if self.interactive:
            print("\033[2J\033[H", end="")
            print(self._panel_text())
        elif force:
            print(
                "[runner] progress "
                f"{self.completed + self.failed}/{self.total} "
                f"current={self.current_section}/{self.current_collector or '-'} "
                f"ok={self.completed} failed={self.failed}"
            )
        sys.stdout.flush()

    def close(self) -> None:
        if self.interactive:
            self.render(force=True)
            print()

    def _update_counts(self) -> None:
        self.completed = sum(1 for row in self.rows.values() if row.status == "ok")
        self.failed = sum(1 for row in self.rows.values() if row.status == "failed")

    def _panel_text(self) -> str:
        done = self.completed + self.failed
        elapsed = format_elapsed(time.monotonic() - self.started_at)
        bar = progress_bar(done, self.total, width=28)
        lines = [
            "+--------------------------------------------------------------------------------+",
            "| Collector Progress                                                             |",
            "+--------------------------------------------------------------------------------+",
            f"| Current section : {shorten(self.current_section or '-', 58):<58} |",
            f"| Current source  : {shorten(self.current_collector or '-', 58):<58} |",
            f"| Overall         : {bar} {done:>2}/{self.total:<2} elapsed {elapsed:<8} |",
            "+----------------------+--------------------------------+----------+----------+--+",
            "| Section              | Source                         | Status   | Articles |  |",
            "+----------------------+--------------------------------+----------+----------+--+",
        ]
        for row in self.rows.values():
            article_text = "-" if row.articles is None else str(row.articles)
            marker = status_marker(row.status)
            lines.append(
                f"| {shorten(row.section, 20):<20} | "
                f"{shorten(row.collector, 30):<30} | "
                f"{row.status:<8} | {article_text:>8} |{marker} |"
            )
        last_running = next((row for row in self.rows.values() if row.status == "running"), None)
        if last_running and last_running.message:
            lines.extend(
                [
                    "+--------------------------------------------------------------------------------+",
                    f"| Last output: {shorten(last_running.message, 65):<65} |",
                ]
            )
        lines.append("+--------------------------------------------------------------------------------+")
        return "\n".join(lines)


def shorten(value: str, max_len: int) -> str:
    text = re.sub(r"\s+", " ", value or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def progress_bar(done: int, total: int, *, width: int) -> str:
    if total <= 0:
        return "[" + "-" * width + "]"
    filled = int(width * done / total)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def status_marker(status: str) -> str:
    if status == "ok":
        return "+"
    if status == "failed":
        return "!"
    if status == "running":
        return ">"
    return " "


def format_elapsed(seconds: float) -> str:
    total = max(0, int(seconds))
    minutes, secs = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def write_run_summary_json(out_dir: Path, summary: dict, filename: str = RUN_SUMMARY_JSON_FILENAME) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def prune_old_logs(out_root: Path, *, now: datetime | None = None) -> None:
    now = now or datetime.now()
    runs_root = out_root / "_collector_runs"
    if runs_root.exists():
        cutoff = now - timedelta(days=COLLECTOR_RUNS_RETENTION_DAYS)
        for child in runs_root.iterdir():
            if not child.is_dir():
                continue
            try:
                folder_date = datetime.strptime(child.name[:10], "%Y-%m-%d")
            except ValueError:
                continue
            if folder_date < cutoff:
                shutil.rmtree(child, ignore_errors=True)
    if LEGACY_LOG_DIR.exists():
        cutoff_ts = (now - timedelta(days=LEGACY_LOG_RETENTION_DAYS)).timestamp()
        for child in LEGACY_LOG_DIR.glob("daily_collectors_*.json"):
            try:
                if child.stat().st_mtime < cutoff_ts:
                    child.unlink()
            except OSError:
                continue


def write_output_markdown_summary(out_dir: Path, summary: dict, filename: str = RUN_SUMMARY_FILENAME) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    lines = [
        "# Collection Summary",
        "",
        f"- Generated at: {summary['finished_at']}",
        f"- Window: {summary['since']} <= published < {summary['until']}",
        f"- Output: `{summary['out']}`",
        "",
        "| Section | Collector | Status | Health | Articles |",
        "| --- | --- | --- | --- | ---: |",
    ]
    for result in summary["results"]:
        lines.append(
            f"| `{result['section']}` | `{result['collector']}` | {result['status']} | "
            f"{result.get('health', 'unknown')} | {result['in_window_article_count']} |"
        )

    lines.append("")
    for result in summary["results"]:
        lines.append(f"## {result['section']} / {result['collector']}")
        lines.append("")
        lines.append(f"- Status: {result['status']}")
        lines.append(f"- Health: {result.get('health', 'unknown')}")
        lines.append(f"- Health note: {result.get('health_note', '')}")
        lines.append(f"- In-window articles: {result['in_window_article_count']}")
        lines.append(f"- Output: `{result['out']}`")
        titles = result.get("in_window_titles") or []
        if titles:
            lines.append("")
            lines.extend(f"- {title}" for title in titles)
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def parse_manifest_datetime(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        return None


def count_collector_items(out_dir: Path, collector_key: str, since: datetime, until: datetime) -> dict:
    items: dict[str, dict] = {}
    run_manifest_dir = out_dir.parent.parent / "_collector_runs" / out_dir.name
    for manifest_file in sorted(run_manifest_dir.glob("*manifest.json")):
        try:
            manifest = json.loads(manifest_file.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError):
            continue

        for item_id, item in manifest.get("items", {}).items():
            if item.get("source_key") != collector_key:
                continue
            published_at = parse_manifest_datetime(item.get("published_at") or "")
            if not published_at or not (since <= published_at < until):
                continue
            data_file = item.get("data_file") or ""
            if not data_file or not (out_dir / Path(data_file).name).exists():
                continue
            items[str(item_id)] = item

    titles = [item.get("title") or item_id for item_id, item in sorted(items.items())]
    return {
        "count": len(items),
        "titles": titles,
    }


def prune_stale_manifest_entries(args: argparse.Namespace, selected: list[Collector]) -> int:
    """Drop manifest entries whose row is missing from articles.jsonl before collecting.

    Collectors skip re-fetching any item already recorded in their manifest. If a
    row was previously lost from the shared articles.jsonl (e.g. an old concurrent
    write before the cross-process lock existed), the manifest would keep claiming
    it and the collector would never re-add it. Pruning such stale entries lets the
    normal skip logic re-fetch them, so the manifest and jsonl self-heal.
    """
    folder = args.output_folder_name
    run_manifest_dir = args.out / "_collector_runs" / folder
    if not run_manifest_dir.exists():
        return 0
    pruned_total = 0
    for collector in selected:
        jsonl_path = args.out / collector.section / folder / "articles.jsonl"
        present_ids: set[str] = set()
        if jsonl_path.exists():
            for line in jsonl_path.read_text(encoding="utf-8-sig").splitlines():
                if not line.strip():
                    continue
                try:
                    present_ids.add(str(json.loads(line).get("id")))
                except json.JSONDecodeError:
                    continue
        for manifest_file in run_manifest_dir.glob(f"{collector.key}*manifest.json"):
            try:
                manifest = json.loads(manifest_file.read_text(encoding="utf-8-sig"))
            except (OSError, json.JSONDecodeError):
                continue
            items = manifest.get("items", {})
            stale = [
                item_id
                for item_id, item in items.items()
                if item.get("data_file") == "articles.jsonl" and str(item_id) not in present_ids
            ]
            if not stale:
                continue
            for item_id in stale:
                del items[item_id]
            manifest_file.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True),
                encoding="utf-8",
            )
            pruned_total += len(stale)
            print(
                f"[runner] pruned {len(stale)} stale manifest entries for "
                f"{collector.section}/{collector.key} (missing from articles.jsonl)"
            )
    if pruned_total:
        print(f"[runner] total stale manifest entries pruned for re-fetch: {pruned_total}")
    return pruned_total


def check_article_consistency(results: list[dict]) -> list[dict]:
    """Cross-check manifest-reported counts against rows actually in articles.jsonl.

    in_window_article_count is derived from per-collector manifests, which are
    written independently and therefore survive even when concurrent writers
    clobber rows in the shared section articles.jsonl. Comparing the manifest
    count against rows physically present in the jsonl surfaces that data loss
    instead of letting it pass silently.
    """
    rows_by_dir: dict[str, dict[str, int]] = {}
    mismatches: list[dict] = []
    for result in results:
        out_dir = result.get("out") or ""
        if out_dir not in rows_by_dir:
            counts: dict[str, int] = {}
            jsonl_path = Path(out_dir) / "articles.jsonl"
            if jsonl_path.exists():
                for line in jsonl_path.read_text(encoding="utf-8-sig").splitlines():
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    key = str(row.get("source_key") or row.get("source") or "")
                    counts[key] = counts.get(key, 0) + 1
            rows_by_dir[out_dir] = counts
        expected = int(result.get("in_window_article_count") or 0)
        actual = rows_by_dir[out_dir].get(result.get("collector", ""), 0)
        if actual < expected:
            mismatches.append(
                {
                    "section": result.get("section"),
                    "collector": result.get("collector"),
                    "manifest_count": expected,
                    "jsonl_rows": actual,
                    "out": out_dir,
                }
            )
    return mismatches


def collector_health(result_status: str, section: str, article_count: int, output: str) -> tuple[str, str]:
    output_lower = output.lower()
    if result_status != "ok":
        return "failed", "collector exited with a non-zero status"
    if "warning" in output_lower:
        return "warning", first_matching_line(output, "warning") or "collector reported a warning"
    if article_count == 0:
        if section == "deep_analysis":
            return "normal_zero", "deep-analysis source had no posts in this window"
        return "zero_articles", "no in-window items were saved; verify this is expected for the source"
    if "hit --max-pages" in output_lower or "cannot prove completeness" in output_lower:
        return "warning", "collector may not have proven date-window completeness"
    return "healthy", "saved one or more in-window items"


def first_matching_line(text: str, pattern: str) -> str:
    pattern_lower = pattern.lower()
    for line in text.splitlines():
        if pattern_lower in line.lower():
            return shorten(line, 160)
    return ""


def run_collector(args: argparse.Namespace, collector: Collector, panel: ProgressPanel | None = None) -> dict:
    collector_out = args.out / collector.section / args.output_folder_name
    collector_out.mkdir(parents=True, exist_ok=True)
    command = build_command(args, collector)
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    print(f"[runner] start {collector.section}/{collector.key}")
    if panel:
        panel.start(collector)
    started = time.monotonic()
    output_lines: list[str] = []
    process = subprocess.Popen(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    assert process.stdout is not None
    for line in process.stdout:
        output_lines.append(line)
        if args.show_collector_output:
            print(line, end="")
        if panel:
            panel.message(collector, line)
    returncode = process.wait()
    elapsed = time.monotonic() - started

    combined_output = "".join(output_lines)
    status = "ok" if returncode == 0 else "failed"
    collection_stats = count_collector_items(
        collector_out,
        collector.key,
        args.window_since,
        args.window_until,
    )
    health, health_note = collector_health(status, collector.section, collection_stats["count"], combined_output)
    if panel:
        panel.finish(
            collector,
            status=status,
            articles=collection_stats["count"],
            elapsed=elapsed,
        )
    if returncode != 0 and combined_output and not args.show_collector_output:
        print(f"[runner] {collector.section}/{collector.key} failed output:")
        print(combined_output.rstrip())
    print(f"[runner] {collector.section}/{collector.key}: {status}, in-window articles={collection_stats['count']}")
    return {
        "collector": collector.key,
        "section": collector.section,
        "command": command,
        "returncode": returncode,
        "status": status,
        "health": health,
        "health_note": health_note,
        "out": str(collector_out.resolve()),
        "in_window_article_count": collection_stats["count"],
        "in_window_titles": collection_stats["titles"],
        "stdout": combined_output,
        "stderr": "",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run configured news collectors.")
    parser.add_argument(
        "--collectors",
        default="all",
        help="Comma-separated collector keys, or all. Example: gcores",
    )
    parser.add_argument(
        "--sections",
        default="all",
        help="Comma-separated report sections, or all. Example: industry_news",
    )
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="yesterday",
        help="Date preset passed to collectors when --since/--until are not set.",
    )
    parser.add_argument("--since", default="", help="Start date/time override, inclusive.")
    parser.add_argument("--until", default="", help="End date/time override, exclusive.")
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Root output directory. The runner writes into a dated child folder.",
    )
    parser.add_argument("--max-pages", type=int, default=0, help="Override max list pages for every collector.")
    parser.add_argument("--limit", type=int, default=0, help="Debug limit passed to every collector.")
    parser.add_argument("--headful", action="store_true", help="Show browser windows for debugging.")
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of collectors to run in parallel. Use 1 for serial execution.",
    )
    parser.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable the live progress panel.",
    )
    parser.add_argument(
        "--show-collector-output",
        action="store_true",
        help="Print collector stdout live in addition to progress updates.",
    )
    args = parser.parse_args()

    args.window_since, args.window_until = runner_window(args)
    args.output_folder_name = resolve_output_folder_name(args)
    args.run_summary_out = args.out / "_collector_runs" / args.output_folder_name
    args.run_summary_out.mkdir(parents=True, exist_ok=True)
    prune_old_logs(args.out)
    selected = filter_collectors_by_section(parse_collectors(args.collectors), parse_sections(args.sections))
    prune_stale_manifest_entries(args, selected)
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    panel = ProgressPanel(selected, enabled=not args.no_progress)
    results: list[dict] = []
    workers = max(1, args.workers)
    try:
        if workers == 1 or len(selected) == 1:
            for collector in selected:
                results.append(run_collector(args, collector, panel))
        else:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(run_collector, args, collector, panel): collector
                    for collector in selected
                }
                for future in as_completed(futures):
                    results.append(future.result())
            results.sort(key=lambda item: (item["section"], item["collector"]))
    finally:
        panel.close()
    print("[runner] article counts for requested window:")
    for result in results:
        print(
            f"[runner]   {result['section']}/{result['collector']}: "
            f"{result['in_window_article_count']} ({result.get('health', 'unknown')})"
        )
    consistency_mismatches = check_article_consistency(results)
    if consistency_mismatches:
        print("[runner] CONSISTENCY WARNING: manifest count exceeds rows in articles.jsonl (possible lost writes):")
        for m in consistency_mismatches:
            print(
                f"[runner]   {m['section']}/{m['collector']}: "
                f"manifest={m['manifest_count']} jsonl_rows={m['jsonl_rows']}"
            )
    else:
        print("[runner] consistency check passed: articles.jsonl rows match manifest counts.")
    summary = {
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "consistency_mismatches": consistency_mismatches,
        "preset": args.preset,
        "since": args.window_since.isoformat(timespec="seconds"),
        "until": args.window_until.isoformat(timespec="seconds"),
        "out_root": str(args.out.resolve()),
        "out": str(args.run_summary_out.resolve()),
        "output_folder": args.output_folder_name,
        "sections": sorted({collector.section for collector in selected}),
        "collectors": [collector.key for collector in selected],
        "results": results,
    }
    selected_keys = [collector.key for collector in selected]
    all_keys = [collector.key for collector in filter_collectors_by_section(list(COLLECTORS.values()), parse_sections(args.sections))]
    if selected_keys == all_keys:
        markdown_filename = RUN_SUMMARY_FILENAME
        json_filename = RUN_SUMMARY_JSON_FILENAME
    else:
        slug = "_".join(selected_keys[:3])
        if len(selected_keys) > 3:
            slug += f"_plus_{len(selected_keys) - 3}"
        markdown_filename = f"run_summary_{slug}.md"
        json_filename = f"run_summary_{slug}.json"
    json_summary_path = write_run_summary_json(args.run_summary_out, summary, json_filename)
    markdown_summary_path = write_output_markdown_summary(args.run_summary_out, summary, markdown_filename)
    print(f"[runner] json summary: {json_summary_path}")
    print(f"[runner] markdown summary: {markdown_summary_path}")

    return 1 if any(result["returncode"] != 0 for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
