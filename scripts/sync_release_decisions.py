#!/usr/bin/env python3
"""Deterministically replace release-calendar decisions from the extractor audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def decisions_list(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict) and isinstance(data.get("decisions"), list):
        return data["decisions"]
    if isinstance(data, list):
        return data
    raise ValueError("selection_decisions.json must be a list or {'decisions': [...]}")


def build_release_decision(node: dict[str, Any], include: bool) -> dict[str, Any]:
    sources = [str(x) for x in node.get("source_ids", []) if str(x)]
    product = str(node.get("product") or "").strip()
    event_date = str(node.get("event_date") or "").strip()
    event = str(node.get("event") or node.get("signal_type") or "产品日历节点").strip()
    decision: dict[str, Any] = {
        "candidate_id": str(node.get("candidate_id") or ""),
        "section": "release_calendar",
        "source_ids": sources,
        "entities": [product] if product else [],
        "event": f"{event_date} {event}".strip(),
        "decision": "include" if include else "exclude",
        "reason": (
            "多源候选按事件类型×来源强度排序进入报告上限"
            if include
            else "单源不具备正文资格" if int(node.get("appearance_count") or 0) < 2
            else "超过本报告产品日历条数上限"
        ),
        "scores": {
            "event": int(node.get("event_type_score") or 0),
            "source": int(node.get("source_strength_score") or 0),
            "total": int(node.get("priority_score") or 0),
        },
    }
    if len(sources) > 1:
        decision["cluster_basis"] = {
            "subject": product,
            "product": product,
            "event_date": event_date,
            "event": "同一产品同日产品日历节点",
        }
    return decision


def sync(audit_path: Path, decisions_path: Path, max_items: int) -> None:
    audit = read_json(audit_path)
    nodes = audit.get("nodes", []) if isinstance(audit, dict) else []
    current_raw = read_json(decisions_path)
    current = decisions_list(current_raw)
    non_release = [x for x in current if str(x.get("section") or "") not in {"release", "release_calendar"}]

    eligible_seen = 0
    release: list[dict[str, Any]] = []
    for node in nodes:
        eligible = int(node.get("appearance_count") or 0) >= 2
        include = eligible and eligible_seen < max_items
        if eligible:
            eligible_seen += 1
        release.append(build_release_decision(node, include))

    output = {"decisions": non_release + release}
    decisions_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", required=True, type=Path)
    parser.add_argument("--decisions", required=True, type=Path)
    parser.add_argument("--max-items", required=True, type=int)
    args = parser.parse_args()
    if args.max_items < 0:
        parser.error("--max-items must be non-negative")
    sync(args.audit, args.decisions, args.max_items)
    print(f"synced release decisions: {args.decisions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
