"""Industry freshness follows source publication, never the underlying event date."""
from __future__ import annotations

import calendar
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

_BASE = Path(__file__).resolve().parents[1]
_CONFIG = _BASE / "config/game_report_policy.json"
if not _CONFIG.exists():
    _CONFIG = _BASE / "references/report-policy.json"
_POLICY = json.loads(_CONFIG.read_text(encoding="utf-8"))
TIMING_VERSION = _POLICY["industry_timing_version"]
ENFORCEMENT_START = _POLICY["industry_timing_enforcement_start"]
SHANGHAI = timezone(timedelta(hours=8))


def report_window(path: Path) -> tuple[str, str]:
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", path.name)
    if dates:
        return dates[0], dates[-1]
    month = re.search(r"monthly_(\d{4})-(\d{2})", path.name)
    if month:
        year, number = map(int, month.groups())
        return f"{year:04d}-{number:02d}-01", f"{year:04d}-{number:02d}-{calendar.monthrange(year, number)[1]}"
    return "", ""


def source_window_date(record: dict) -> tuple[str, str]:
    """Prefer the current article's timestamp; missing dates use extraction date.

    This does not substitute the date of an older original article/event for
    the publication date of the actual source being consumed.
    """
    published = str(record.get("published_at") or "").strip()
    if published:
        try:
            parsed = datetime.fromisoformat(published.replace("Z", "+00:00"))
            if parsed.tzinfo:
                parsed = parsed.astimezone(SHANGHAI)
            return parsed.date().isoformat(), "published_at"
        except ValueError:
            return "", "invalid_published_at"
    value = str(record.get("date") or "")
    try:
        return datetime.strptime(value, "%Y-%m-%d").date().isoformat(), "input_date"
    except ValueError:
        return "", "missing_source_date"


def build_time_check(source_ids: list[str], inputs: dict, start: str, end: str,
                     *, event_date: str = "unknown", basis: str) -> dict:
    sources = []
    for sid in source_ids:
        value, field = source_window_date(inputs.get(sid, {}))
        sources.append({"source_id": sid, "date": value, "date_field": field,
                        "in_window": bool(value and start <= value <= end)})
    return {"report_window": {"start": start, "end": end}, "sources": sources,
            "event_date": event_date, "event_date_is_gate": False, "basis": basis}


def validate_timing_document(document: object, inputs: dict, report_path: Path) -> list[str]:
    start, end = report_window(report_path)
    explicit = isinstance(document, dict) and "industry_timing_version" in document
    if not explicit and (not end or end < ENFORCEMENT_START):
        return []
    if not isinstance(document, dict) or document.get("industry_timing_version") != TIMING_VERSION:
        return [f"new report requires industry_timing_version={TIMING_VERSION}"]
    errors = []
    rows = document.get("decisions", [])
    if not isinstance(rows, list):
        return ["timing decisions must be a list"]
    for row in rows:
        if not isinstance(row, dict) or row.get("section") not in {"industry", "industry_news"}:
            continue
        cid = row.get("candidate_id", "?")
        scores = row.get("scores") or {}
        if scores.get("event") == 0:
            continue
        check = row.get("time_check")
        if not isinstance(check, dict):
            errors.append(f"industry decision needs time_check: {cid}")
            continue
        ids = row.get("source_ids", [])
        expected = build_time_check(ids, inputs, start, end, basis="validation")
        if check.get("report_window") != expected["report_window"] or check.get("sources") != expected["sources"]:
            errors.append(f"time_check must match actual source dates/window: {cid}")
        if check.get("event_date_is_gate") is not False or not str(check.get("basis") or "").strip() or not str(check.get("event_date") or "").strip():
            errors.append(f"time_check must distinguish source window from event timeline: {cid}")
        current_source = any(x["in_window"] for x in expected["sources"])
        if row.get("decision") == "include" and not current_source:
            errors.append(f"industry include needs a current-window source: {cid}")
        gates = row.get("exclusion_gates")
        if row.get("decision") == "exclude":
            allowed = {"score", "source_quality", "history_repeat", "source_window", "financial_routine", "section_transfer", "factual_uncertainty", "carryover_limit"}
            if not isinstance(gates, list) or not gates or any(x not in allowed for x in gates):
                errors.append(f"industry exclusion needs specific exclusion_gates; event age is not a gate: {cid}")
            else:
                if current_source and "source_window" in gates:
                    errors.append(f"current source cannot be excluded for event being outside window: {cid}")
                total = scores.get("total")
                if "score" in gates and type(total) is int and total >= _POLICY["industry_threshold"]:
                    errors.append(f"above-threshold industry candidate cannot use score exclusion: {cid}")
                if "history_repeat" in gates and (row.get("history_check") or {}).get("history_match") is not True:
                    errors.append(f"history_repeat exclusion needs a matched prior event: {cid}")
        history = row.get("history_check") or {}
        prior = history.get("prior_occurrences", [])
        weekly_rollup = ("game_industry_weekly_" in report_path.name and isinstance(prior, list) and bool(prior)
            and all(isinstance(item, str) and not re.search(r"周报|weekly", item, re.I)
                    and (dates := re.findall(r"\d{4}-\d{2}-\d{2}", item))
                    and all(start <= value <= end for value in dates) for item in prior))
        if row.get("decision") == "include" and history.get("history_match") is True and history.get("prior_card_exposed") is True and history.get("novelty") != "material_update" and not weekly_rollup:
            errors.append(f"previously exposed event needs material_update: {cid}")
    return errors
