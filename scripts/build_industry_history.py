#!/usr/bin/env python3
"""Build a 14-day, cross-report memory for industry-news deduplication.

The output is evidence for the report-writing agent, not an automatic semantic
classifier.  It exposes previously published event names, entities, titles and
claims so the agent can distinguish a new source from a genuinely new event
stage.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Any


REPORT_DIR_RE = re.compile(
    r"output[\\/](daily|weekly|weekend|monthly)[\\/]"
    r"(\d{4}-\d{2}-\d{2})(?:_to_(\d{4}-\d{2}-\d{2}))?"
)
INDUSTRY_SECTION_RE = re.compile(
    r"(?ms)^##\s+(?:一、)?行业新闻\s*$\s*(.*?)(?=^##\s+|\Z)"
)
ITEM_RE = re.compile(r"(?ms)^###\s+\d+\.\s+(.+?)\s*$\s*(.*?)(?=^###\s+\d+\.|\Z)")
LEGACY_CARD_ITEMS_PER_SECTION = 10


def _rows(data: Any, key: str) -> list[dict[str, Any]]:
    if isinstance(data, dict):
        data = data.get(key, [])
    return data if isinstance(data, list) else []


def _window(path: Path) -> tuple[date, date] | None:
    match = REPORT_DIR_RE.search(str(path))
    if not match:
        return None
    start = date.fromisoformat(match.group(2))
    end = date.fromisoformat(match.group(3) or match.group(2))
    return start, end


def _publish_log(workspace: Path, report_id: str) -> dict[str, Any] | None:
    path = workspace / "data" / "feishu" / "publish_logs" / f"daily_{report_id}.json"
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def _broadcast_succeeded(log: dict[str, Any] | None) -> bool:
    if not log:
        return False
    if log.get("audience_scope") == "single_test":
        return False
    if isinstance(log.get("card_delivery_succeeded"), bool):
        return bool(log["card_delivery_succeeded"])
    results = log.get("results")
    return isinstance(results, list) and any(
        isinstance(row, dict) and row.get("ok") is True for row in results
    )


def _card_exposure(
    log: dict[str, Any] | None,
    *,
    candidate_id: str,
    title: str,
    report_rank: int,
) -> dict[str, Any]:
    """Resolve whether an industry item reached the subscriber broadcast card.

    New publish logs carry the exact rendered manifest.  Older logs are
    inferred using the historical ten-items-per-section contract so existing
    reports participate in exposure-aware deduplication immediately.
    """
    if not _broadcast_succeeded(log):
        return {
            "exposed": False,
            "card_rank": None,
            "card_limit": None,
            "source": "not_broadcast",
        }

    manifest = log.get("card_items") if log else None
    if isinstance(manifest, list):
        matched = next(
            (
                row for row in manifest
                if isinstance(row, dict)
                and str(row.get("section") or "") in {"industry", "industry_news", "行业新闻"}
                and (
                    (candidate_id and str(row.get("candidate_id") or "") == candidate_id)
                    or str(row.get("title") or "").strip() == title
                )
            ),
            None,
        )
        return {
            "exposed": matched is not None,
            "card_rank": int(matched.get("position")) if matched and matched.get("position") else None,
            "card_limit": int(log.get("card_max_items_per_section") or LEGACY_CARD_ITEMS_PER_SECTION),
            "source": "publish_log_manifest",
        }

    try:
        limit = int((log or {}).get("card_max_items_per_section") or LEGACY_CARD_ITEMS_PER_SECTION)
    except (TypeError, ValueError):
        limit = LEGACY_CARD_ITEMS_PER_SECTION
    return {
        "exposed": report_rank <= limit,
        "card_rank": report_rank if report_rank <= limit else None,
        "card_limit": limit,
        "source": "legacy_position_inference",
    }


def collect_history(workspace: Path, target_start: date, lookback_days: int = 14) -> dict[str, Any]:
    history_start = target_start - timedelta(days=lookback_days)
    history_end = target_start - timedelta(days=1)
    occurrences: list[dict[str, Any]] = []
    structured_report_dirs: set[Path] = set()

    for decisions_path in workspace.glob("output/*/*/_intermediate/selection_decisions.json"):
        window = _window(decisions_path)
        if not window:
            continue
        report_start, report_end = window
        if report_end < history_start or report_start > history_end:
            continue
        items_path = decisions_path.with_name("report_items.json")
        if not items_path.exists():
            continue
        structured_report_dirs.add(decisions_path.parent.parent.resolve())
        decisions = {
            str(row.get("candidate_id") or ""): row
            for row in _rows(json.loads(decisions_path.read_text(encoding="utf-8")), "decisions")
        }
        report_id = decisions_path.parent.parent.name
        publish_log = _publish_log(workspace, report_id)
        industry_rank = 0
        for item in _rows(json.loads(items_path.read_text(encoding="utf-8")), "items"):
            if str(item.get("section") or "") not in {"industry", "industry_news"}:
                continue
            candidate_id = str(item.get("candidate_id") or "")
            decision = decisions.get(candidate_id, {})
            if decision.get("decision") != "include":
                continue
            industry_rank += 1
            title = str(item.get("title") or "").strip()
            exposure = _card_exposure(
                publish_log,
                candidate_id=candidate_id,
                title=title,
                report_rank=industry_rank,
            )
            claims = [
                str(claim.get("claim") or "").strip()
                for claim in item.get("claims", [])
                if isinstance(claim, dict) and str(claim.get("claim") or "").strip()
            ]
            occurrences.append(
                {
                    "report_window": {
                        "start": report_start.isoformat(),
                        "end": report_end.isoformat(),
                    },
                    "report_kind": decisions_path.parts[-4],
                    "candidate_id": candidate_id,
                    "event": str(decision.get("event") or "").strip(),
                    "entities": [
                        str(value).strip()
                        for value in decision.get("entities", [])
                        if str(value).strip()
                    ],
                    "title": title,
                    "claims": claims,
                    "source_ids": item.get("source_ids", []),
                    "artifact": str(items_path.relative_to(workspace)),
                    "card_exposed": exposure["exposed"],
                    "card_rank": exposure["card_rank"],
                    "card_limit": exposure["card_limit"],
                    "card_exposure_source": exposure["source"],
                }
            )

    # Compatibility for legacy reports created before structured audit artifacts
    # became mandatory.  Their visible titles/bodies are still valuable history.
    for report_path in workspace.glob("output/*/*/game_industry_*.md"):
        report_dir = report_path.parent.resolve()
        if report_dir in structured_report_dirs:
            continue
        window = _window(report_path)
        if not window:
            continue
        report_start, report_end = window
        if report_end < history_start or report_start > history_end:
            continue
        section_match = INDUSTRY_SECTION_RE.search(report_path.read_text(encoding="utf-8"))
        if not section_match:
            continue
        publish_log = _publish_log(workspace, report_path.parent.name)
        for report_rank, item_match in enumerate(ITEM_RE.finditer(section_match.group(1)), 1):
            title = item_match.group(1).strip()
            body = re.sub(r"\s+", " ", item_match.group(2)).strip()
            exposure = _card_exposure(
                publish_log,
                candidate_id="",
                title=title,
                report_rank=report_rank,
            )
            occurrences.append(
                {
                    "report_window": {
                        "start": report_start.isoformat(),
                        "end": report_end.isoformat(),
                    },
                    "report_kind": report_path.parts[-3],
                    "candidate_id": "",
                    "event": title,
                    "entities": [],
                    "title": title,
                    "claims": [body] if body else [],
                    "source_ids": [],
                    "artifact": str(report_path.relative_to(workspace)),
                    "legacy_fallback": True,
                    "card_exposed": exposure["exposed"],
                    "card_rank": exposure["card_rank"],
                    "card_limit": exposure["card_limit"],
                    "card_exposure_source": exposure["source"],
                }
            )

    occurrences.sort(
        key=lambda row: (
            row["report_window"]["end"],
            row["report_kind"],
            row["title"],
        )
    )
    return {
        "schema_version": 2,
        "target_start": target_start.isoformat(),
        "enforce_history_check": target_start >= date(2026, 7, 28),
        "enforce_card_exposure_check": target_start >= date(2026, 8, 11),
        "lookback_days": lookback_days,
        "history_window": {
            "start": history_start.isoformat(),
            "end": history_end.isoformat(),
        },
        "policy": {
            "same_event_new_source_only": "exclude",
            "same_event_new_background_only": "exclude",
            "material_stage_change": "may_include",
            "same_event_prior_card_hidden": "may_include_once_as_card_carryover",
            "max_card_carryover_per_report": 1,
            "required_candidate_fields": [
                "history_match",
                "novelty",
                "prior_occurrences",
                "new_facts",
                "prior_card_exposed",
            ],
        },
        "occurrences": occurrences,
    }


def render_markdown(history: dict[str, Any]) -> str:
    window = history["history_window"]
    lines = [
        "# 行业新闻双周历史记忆",
        "",
        f"- 历史窗口: {window['start']} 至 {window['end']}",
        f"- 已发布行业条目: {len(history['occurrences'])}",
        "- 判定: 换来源或补背景不算新进展；只有事件状态或关键事实发生实质变化才可再次入选。",
        "- 卡片曝光: 历史正文已收录但订阅卡片未展示的同一事件，可按当前分数线竞争一次 card_carryover；每期最多 1 条。",
        "",
    ]
    for index, row in enumerate(history["occurrences"], 1):
        lines.extend(
            [
                f"## H{index:03d} - {row['title']}",
                f"- report: {row['report_kind']} {row['report_window']['start']} to {row['report_window']['end']}",
                f"- event: {row['event']}",
                f"- entities: {', '.join(row['entities'])}",
                f"- claims: {'；'.join(row['claims'])}",
                f"- card_exposed: {str(row.get('card_exposed')).lower()}"
                f" (rank={row.get('card_rank') or '-'}, limit={row.get('card_limit') or '-'}, source={row.get('card_exposure_source')})",
                f"- artifact: {row['artifact']}",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--target-start", required=True, type=date.fromisoformat)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--lookback-days", type=int, default=14)
    args = parser.parse_args()
    history = collect_history(args.workspace.resolve(), args.target_start, args.lookback_days)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.output.with_suffix(".md").write_text(render_markdown(history), encoding="utf-8")
    print(
        f"history={history['history_window']['start']}..{history['history_window']['end']} "
        f"occurrences={len(history['occurrences'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
