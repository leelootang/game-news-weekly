#!/usr/bin/env python3
"""Structured audit artifacts for game-industry reports.

The report markdown remains the reader-facing source of truth.  This module adds
machine-checkable companions for new reports:

* ``report_items.json``: every published item, its candidate and evidence;
* ``selection_decisions.json``: include/exclude decisions for all candidates;
* ``release_calendar_audit.json``: automatically queued release signals.

It also generates ``sources_used.md`` from those artifacts, so source details
cannot drift from ``report_inputs.jsonl`` through copy/paste.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from deep_observation_handoff import validate_weekly_handoff
except ModuleNotFoundError:  # Imported as scripts.report_artifacts in tests/tools.
    _handoff_path = Path(__file__).with_name("deep_observation_handoff.py")
    _handoff_spec = importlib.util.spec_from_file_location("deep_observation_handoff", _handoff_path)
    if not _handoff_spec or not _handoff_spec.loader:
        raise
    _handoff_module = importlib.util.module_from_spec(_handoff_spec)
    sys.modules[_handoff_spec.name] = _handoff_module
    _handoff_spec.loader.exec_module(_handoff_module)
    validate_weekly_handoff = _handoff_module.validate_weekly_handoff


SCHEMA_VERSION = 1
SOURCE_ID_RE = re.compile(r"\bS\d{4}\b")
SECTION_HEADINGS = {
    "industry": "行业新闻",
    "ai": "AI 新闻",
    "release_calendar": "新游发布",
    "community": "玩家舆论",
    "deep": "行业精选",
}
SECTION_ALIASES = {
    "industry_news": "industry",
    "industry": "industry",
    "ai_trends": "ai",
    "ai": "ai",
    "release_calendar": "release_calendar",
    "release": "release_calendar",
    "community_discourse": "community",
    "community": "community",
    "deep_analysis": "deep",
    "deep": "deep",
}
COMMUNITY_COUNT = re.compile(r"(?:\d+\s*(?:条)?回复|\d+\s*页|浏览(?:量)?\s*\d+|热度\s*\d+)")
RELEASE_EVENT = re.compile(r"上线|公测|内测|首测|删档测试|不删档|付费测试|测试|抢先体验|EA|发售|发布|预约|开测|定档|上市|开服|重启|复活|停运|延期|跳票", re.I)
PRIORITY_TRACKS = {"pvp_competitive", "strategy_card_rpg", "life_simulation"}
# 新闻标题应陈述可核验事实，而非复用来源的宣传性修辞。具体规模
# 应以销量、预约量、榜单名次等数据写出；这些词不应作为事实替身。
PROMOTIONAL_INDUSTRY_TITLE_TERMS = ("爆红", "霸榜", "横扫", "席卷", "封神", "现象级", "杀疯了")


@dataclass(frozen=True)
class ReportItem:
    section: str
    title: str
    body: str


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc.msg}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_no}: record must be an object")
        rows.append(row)
    return rows


def release_cap_for_report(report_path: Path) -> int:
    if "game_industry_weekly_" in report_path.name:
        return 7
    if "game_industry_monthly_" in report_path.name:
        return 12
    return 4


def inputs_by_id(inputs_path: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for record in load_jsonl(inputs_path):
        sid = str(record.get("source_id") or "")
        if not SOURCE_ID_RE.fullmatch(sid):
            raise ValueError(f"input record has invalid source_id: {sid!r}")
        if sid in records:
            raise ValueError(f"duplicate source_id in inputs: {sid}")
        records[sid] = record
    return records


def canonical_section(value: str) -> str:
    return SECTION_ALIASES.get(value.strip().lower(), value.strip().lower())


def parse_report_items(report_text: str) -> list[ReportItem]:
    """Extract visible report items without interpreting their facts."""
    current: str | None = None
    chunks: list[tuple[str, list[str]]] = []
    for line in report_text.splitlines():
        if line.startswith("## "):
            header = line[3:].strip()
            current = None
            for section, marker in SECTION_HEADINGS.items():
                if marker in header:
                    current = section
                    break
            if current:
                chunks.append((current, []))
        elif current and chunks:
            chunks[-1][1].append(line)

    out: list[ReportItem] = []
    for section, lines in chunks:
        text = "\n".join(lines).strip()
        if section == "release_calendar":
            for line in lines:
                bullet = line.strip()
                if not bullet.startswith("- "):
                    continue
                body = bullet[2:].strip()
                matched = re.search(r"《([^》]+)》", body)
                out.append(ReportItem(section, matched.group(1).strip() if matched else body[:80], body))
            continue
        matches = list(re.finditer(r"(?m)^###\s+\d+\.\s+(.+)$", text))
        for index, match in enumerate(matches):
            body_start = match.end()
            body_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            out.append(ReportItem(section, match.group(1).strip(), text[body_start:body_end].strip()))
    return out


def _items_list(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict):
        data = data.get("items", [])
    if not isinstance(data, list):
        raise ValueError("report_items.json must be an array or {items: [...]}")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("report_items.json items must be objects")
    return data


def _decisions_list(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict):
        data = data.get("decisions", [])
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("selection_decisions.json must be an array or {decisions: [...]}")
    return data


def _ids(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(sid) for sid in value if isinstance(sid, str)]


def _detail_signature(record: dict[str, Any]) -> tuple[str, str, str]:
    return (str(record.get("source") or ""), str(record.get("title") or ""), str(record.get("url") or ""))


def parse_sources_used(text: str) -> tuple[dict[str, list[str]], dict[str, tuple[str, str, str]]]:
    """Return the visible item map and exact Source Details fields."""
    item_map: dict[str, list[str]] = {}
    details: dict[str, tuple[str, str, str]] = {}
    section = ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if "item source map" in section or "条目来源映射" in section:
            match = re.match(r"^-\s+(.+?)\s+[—–-]\s+(S\d{4}\b.*)$", line)
            if match:
                item_map[match.group(1).strip()] = SOURCE_ID_RE.findall(match.group(2))
        elif "source details" in section or "来源明细" in section:
            if not line.startswith("- S"):
                continue
            parts = [part.strip() for part in line[2:].split("|")]
            if len(parts) >= 4 and SOURCE_ID_RE.fullmatch(parts[0]):
                details[parts[0]] = (parts[1], parts[2], parts[3])
    return item_map, details


def _lookup_item_map(title: str, section: str, item_map: dict[str, list[str]]) -> list[str]:
    candidates = [title]
    if section == "release_calendar":
        candidates.insert(0, f"产品日历 - {title}")
    for key in candidates:
        if key in item_map:
            return item_map[key]
    normal = re.sub(r"[\s：:，,。.!！?？]", "", title)
    for key, ids in item_map.items():
        if re.sub(r"[\s：:，,。.!！?？]", "", key).endswith(normal):
            return ids
    return []


def validate_sources(report_items: list[ReportItem], sources_text: str, inputs: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    item_map, details = parse_sources_used(sources_text)
    mapped: set[str] = set()
    for item in report_items:
        ids = _lookup_item_map(item.title, item.section, item_map)
        if not ids:
            errors.append(f"published item has no source map: [{item.section}] {item.title}")
            continue
        mapped.update(ids)
        for sid in ids:
            if sid not in inputs:
                errors.append(f"item map references unknown source_id {sid}: {item.title}")
    for sid in sorted(mapped):
        if sid not in details:
            errors.append(f"mapped source has no Source Details entry: {sid}")
            continue
        if details[sid] != _detail_signature(inputs[sid]):
            errors.append(f"Source Details drift from report_inputs.jsonl: {sid}")
    for sid in sorted(details):
        if sid not in inputs:
            errors.append(f"Source Details references unknown source_id: {sid}")
        elif sid not in mapped:
            errors.append(f"Source Details contains unused source_id: {sid}")
    return errors


def validate_editorial_titles(report_items: list[ReportItem]) -> list[str]:
    """Reject promotional shorthand in visible industry-news titles."""
    errors: list[str] = []
    for item in report_items:
        if item.section != "industry":
            continue
        for term in PROMOTIONAL_INDUSTRY_TITLE_TERMS:
            if term in item.title:
                errors.append(
                    f"industry title uses promotional shorthand {term!r}: {item.title}; "
                    "state the observable event and its supporting metric instead"
                )
    return errors


def validate_contract(
    report_path: Path,
    inputs_path: Path,
    items_path: Path | None,
    decisions_path: Path | None,
    release_audit_path: Path | None,
    sources_path: Path | None = None,
    require_artifacts: bool = False,
) -> tuple[list[str], list[str]]:
    """Validate the publishable closure.  Returns ``(errors, warnings)``."""
    errors: list[str] = []
    warnings: list[str] = []
    report_items = parse_report_items(report_path.read_text(encoding="utf-8"))
    inputs = inputs_by_id(inputs_path)
    errors.extend(validate_editorial_titles(report_items))
    errors.extend(validate_weekly_handoff(report_path))
    industry_threshold = 8 if "game_industry_weekly_" in report_path.name else 7
    if sources_path and sources_path.exists():
        errors.extend(validate_sources(report_items, sources_path.read_text(encoding="utf-8"), inputs))

    structured_paths = (items_path, decisions_path)
    structured_started = any(path and path.exists() for path in structured_paths)
    if not structured_started:
        message = "structured audit artifacts absent (legacy report): report_items.json, selection_decisions.json, release_calendar_audit.json"
        (errors if require_artifacts else warnings).append(message)
        if release_audit_path and release_audit_path.exists():
            warnings.append("release_calendar_audit.json exists without structured report artifacts; treating report as legacy")
        return errors, warnings
    for path in (items_path, decisions_path, release_audit_path):
        if not path or not path.exists():
            errors.append(f"structured audit artifact missing: {path}")
    if errors:
        return errors, warnings

    items = _items_list(read_json(items_path))
    decisions = _decisions_list(read_json(decisions_path))
    audit = read_json(release_audit_path)
    audit_nodes = audit.get("nodes", []) if isinstance(audit, dict) else []
    if not isinstance(audit_nodes, list):
        errors.append("release_calendar_audit.json nodes must be a list")
        return errors, warnings

    visible = [(item.section, item.title) for item in report_items]
    visible_by_key = {(item.section, item.title): item for item in report_items}
    structured: dict[tuple[str, str], dict[str, Any]] = {}
    for item in items:
        section = canonical_section(str(item.get("section") or ""))
        title = str(item.get("title") or "").strip()
        key = (section, title)
        if not title or section not in SECTION_HEADINGS:
            errors.append(f"invalid report item identity: {item!r}")
            continue
        if key in structured:
            errors.append(f"duplicate report_items identity: {section}/{title}")
        structured[key] = item
        source_ids = _ids(item.get("source_ids"))
        if not source_ids:
            errors.append(f"report item has no source_ids: {section}/{title}")
        for sid in source_ids:
            record = inputs.get(sid)
            if not record:
                errors.append(f"report item uses unknown source_id {sid}: {title}")
            elif record.get("fetch_status", "ok") != "ok" or record.get("body_status", "full") in {"snippet", "empty"}:
                errors.append(f"published item uses unavailable/snippet source {sid}: {title}")
        claims = item.get("claims")
        if not isinstance(claims, list) or not claims:
            errors.append(f"report item has no claim evidence: {section}/{title}")
        else:
            for claim in claims:
                if not isinstance(claim, dict):
                    errors.append(f"claim is not an object: {title}")
                    continue
                sid = str(claim.get("source_id") or "")
                claim_text = str(claim.get("claim") or "").strip()
                evidence = str(claim.get("evidence") or "").strip()
                if not claim_text or claim_text not in visible_by_key[key].body:
                    errors.append(f"claim text is not present in final item: {title}")
                if sid not in source_ids:
                    errors.append(f"claim source_id is not item source: {title}/{sid}")
                elif evidence not in str(inputs.get(sid, {}).get("text") or ""):
                    errors.append(f"claim evidence not found in input text: {title}/{sid}")
        if section == "community":
            community = item.get("community")
            required = {"trigger", "claim_scope", "complaint_logic", "timeline", "follow_up_scan"}
            if not isinstance(community, dict) or not required.issubset(community):
                errors.append(f"community item lacks structured community fields: {title}")
        if section == "release_calendar":
            release = item.get("release")
            if not isinstance(release, dict) or not {"product", "event", "date", "platform", "company"}.issubset(release):
                errors.append(f"release calendar item lacks product/event/date/platform/company: {title}")
            elif len(source_ids) < 2:
                errors.append(f"release calendar item needs multi-source evidence: {title}")

    if set(visible) != set(structured):
        for section, title in sorted(set(visible) - set(structured)):
            errors.append(f"published item missing report_items entry: {section}/{title}")
        for section, title in sorted(set(structured) - set(visible)):
            errors.append(f"report_items entry not in final markdown: {section}/{title}")

    decisions_by_id: dict[str, dict[str, Any]] = {}
    for decision in decisions:
        cid = str(decision.get("candidate_id") or "").strip()
        if not cid:
            errors.append("decision missing candidate_id")
            continue
        if cid in decisions_by_id:
            errors.append(f"duplicate candidate_id in decisions: {cid}")
        decisions_by_id[cid] = decision
        source_ids = _ids(decision.get("source_ids"))
        if not source_ids:
            errors.append(f"decision has no source_ids: {cid}")
        if decision.get("decision") not in {"include", "exclude", "merge"}:
            errors.append(f"decision must be include/exclude/merge: {cid}")
        if decision.get("decision") == "merge" and not str(decision.get("merge_into") or "").strip():
            errors.append(f"merge decision missing merge_into: {cid}")
        if not str(decision.get("reason") or "").strip():
            errors.append(f"decision missing reason: {cid}")
        if not str(decision.get("event") or "").strip():
            errors.append(f"decision must identify one concrete event: {cid}")
        if len(source_ids) > 1 and canonical_section(str(decision.get("section") or "")) in {"industry", "release_calendar"}:
            cluster = decision.get("cluster_basis")
            required_cluster = {"subject", "product", "event_date", "event"}
            if not isinstance(cluster, dict) or not required_cluster.issubset(cluster) or not all(str(cluster.get(k) or "").strip() for k in required_cluster):
                errors.append(f"multi-source candidate lacks strict same-subject/product/date/event cluster_basis: {cid}")
        priority_tracks = decision.get("priority_tracks", [])
        if not isinstance(priority_tracks, list) or not all(isinstance(track, str) for track in priority_tracks):
            errors.append(f"priority_tracks must be a list of strings: {cid}")
        else:
            unknown_tracks = sorted(set(priority_tracks) - PRIORITY_TRACKS)
            if unknown_tracks:
                errors.append(f"decision has unknown priority_tracks {unknown_tracks}: {cid}")
        if canonical_section(str(decision.get("section") or "")) == "industry":
            scores = decision.get("scores")
            if not isinstance(scores, dict) or not {"event", "relevance", "hook", "total"}.issubset(scores):
                errors.append(f"industry decision lacks E×R+M scores: {cid}")
            else:
                try:
                    event = int(scores["event"])
                    relevance = int(scores["relevance"])
                    hook = int(scores["hook"])
                    total = int(scores["total"])
                except (TypeError, ValueError):
                    errors.append(f"industry E×R+M scores must be integers: {cid}")
                else:
                    if event not in range(4) or relevance not in range(4) or hook not in range(3):
                        errors.append(f"industry E×R+M score out of range: {cid}")
                    if total != event * relevance + hook:
                        errors.append(f"industry total must equal E×R+M: {cid}")
                    if decision.get("decision") == "include" and (event == 0 or total < industry_threshold):
                        errors.append(
                            f"industry include fails E×R+M threshold "
                            f"(required >= {industry_threshold}): {cid}"
                        )
        if canonical_section(str(decision.get("section") or "")) == "ai":
            tier = decision.get("ai_tier")
            stages = decision.get("game_stage")
            reverse_scan = decision.get("industry_reverse_scan")
            allowed_stages = {"development", "product", "publishing", "operations"}
            if tier not in {"direct_application", "transferable_frontier"}:
                errors.append(f"AI decision has invalid ai_tier: {cid}")
            if not isinstance(reverse_scan, bool):
                errors.append(f"AI decision must record boolean industry_reverse_scan: {cid}")
            if not isinstance(stages, list) or not all(stage in allowed_stages for stage in stages):
                errors.append(f"AI decision has invalid game_stage list: {cid}")
            elif tier == "direct_application" and not stages:
                errors.append(f"direct-application AI decision needs at least one game_stage: {cid}")
            if tier == "transferable_frontier" and not str(decision.get("migration_path") or "").strip():
                errors.append(f"transferable-frontier AI decision needs migration_path: {cid}")
        if canonical_section(str(decision.get("section") or "")) == "deep":
            scores = decision.get("scores")
            required_deep_scores = {"relevance", "insight", "evidence", "card", "total"}
            if not isinstance(scores, dict) or not required_deep_scores.issubset(scores):
                errors.append(f"deep decision lacks R/I/E/C scores: {cid}")
            else:
                try:
                    relevance = int(scores["relevance"])
                    insight = int(scores["insight"])
                    evidence = int(scores["evidence"])
                    card = int(scores["card"])
                    total = int(scores["total"])
                except (TypeError, ValueError):
                    errors.append(f"deep R/I/E/C scores must be integers: {cid}")
                else:
                    if any(value not in range(4) for value in (relevance, insight, evidence, card)):
                        errors.append(f"deep R/I/E/C score out of range: {cid}")
                    if total != relevance + insight + evidence + card:
                        errors.append(f"deep total must equal R+I+E+C: {cid}")
                    if decision.get("decision") == "include" and (insight == 0 or evidence == 0):
                        errors.append(f"deep include fails basic I/E eligibility: {cid}")
                    is_weekly = "game_industry_weekly_" in report_path.name
                    if is_weekly and decision.get("decision") == "include" and total < 9 and decision.get("card_designated") is not True:
                        errors.append(f"weekly deep include below 9 without manual card designation: {cid}")
    for key, item in structured.items():
        cid = str(item.get("candidate_id") or "")
        decision = decisions_by_id.get(cid)
        if not cid or not decision:
            errors.append(f"published item has no selection decision: {key[0]}/{key[1]}")
        elif decision.get("decision") != "include":
            errors.append(f"published item maps to non-include decision {cid}: {key[1]}")

    for node in audit_nodes:
        if not isinstance(node, dict):
            errors.append("release audit node must be an object")
            continue
        cid = str(node.get("candidate_id") or "")
        decision = decisions_by_id.get(cid)
        if not cid or not decision:
            errors.append(f"release audit node lacks a decision: {node.get('title') or cid}")
        elif canonical_section(str(decision.get("section") or "")) != "release_calendar":
            errors.append(f"release audit node decision is not release_calendar: {cid}")
        allowed_calendar_signals = {
            "new_game_launch", "new_game_test", "new_game_launch_or_test",
            "new_game_preload", "new_game_first_reveal", "new_game_schedule",
            "old_cross_platform_launch", "old_relaunch", "old_major_update",
        }
        if node.get("signal_type") not in allowed_calendar_signals:
            errors.append(f"release audit contains non-new-game signal: {node.get('title') or cid}")
        if decision:
            scores = decision.get("scores")
            if not isinstance(scores, dict) or not {"event", "source", "total"}.issubset(scores):
                errors.append(f"release decision lacks event×source scores: {cid}")
            else:
                expected_event = int(node.get("event_type_score") or 0)
                expected_source = int(node.get("source_strength_score") or 0)
                expected_total = int(node.get("priority_score") or 0)
                try:
                    actual = (int(scores["event"]), int(scores["source"]), int(scores["total"]))
                except (TypeError, ValueError):
                    errors.append(f"release event×source scores must be integers: {cid}")
                else:
                    if actual != (expected_event, expected_source, expected_total):
                        errors.append(f"release event×source scores drift from audit: {cid}")
                    if actual[2] != actual[0] * actual[1]:
                        errors.append(f"release total must equal event×source: {cid}")
            if decision.get("decision") == "include" and int(node.get("appearance_count") or 0) < 2:
                errors.append(f"release include must have multi-source evidence: {cid}")

    release_includes = [
        str(d.get("candidate_id") or "") for d in decisions_by_id.values()
        if canonical_section(str(d.get("section") or "")) == "release_calendar" and d.get("decision") == "include"
    ]
    release_cap = release_cap_for_report(report_path)
    if len(release_includes) > release_cap:
        errors.append(f"release calendar exceeds report cap {release_cap}: {len(release_includes)}")
    eligible_order = [
        str(node.get("candidate_id") or "") for node in audit_nodes
        if int(node.get("appearance_count") or 0) >= 2
    ]
    if release_includes != eligible_order[:len(release_includes)]:
        errors.append("release includes must be a priority-ranked prefix of multi-source candidates")

    for item in report_items:
        if item.section == "community" and COMMUNITY_COUNT.search(item.body):
            errors.append(f"community item contains reply/page/heat count: {item.title}")
        if item.section == "deep":
            if "观察：" not in item.body or "分析：" not in item.body:
                errors.append(f"deep item lacks 观察：/分析： labels: {item.title}")
            analysis = item.body.split("分析：", 1)[1] if "分析：" in item.body else ""
            if len([part for part in re.split(r"\n\s*\n", analysis) if part.strip()]) < 2:
                errors.append(f"deep item needs at least two analysis paragraphs: {item.title}")
    return errors, warnings


def generate_sources_used(report_path: Path, inputs_path: Path, items_path: Path, output_path: Path) -> None:
    """Render sources_used.md deterministically from selected report items."""
    inputs = inputs_by_id(inputs_path)
    items = _items_list(read_json(items_path))
    visible = parse_report_items(report_path.read_text(encoding="utf-8"))
    structured = {(canonical_section(str(x.get("section") or "")), str(x.get("title") or "").strip()): x for x in items}
    lines = ["# Sources Used", "", "## Local Inputs", ""]
    paths: list[str] = []
    used: list[str] = []
    for item in visible:
        meta = structured.get((item.section, item.title))
        if not meta:
            raise ValueError(f"cannot generate sources: missing report_items entry for {item.section}/{item.title}")
        for sid in _ids(meta.get("source_ids")):
            if sid not in inputs:
                raise ValueError(f"cannot generate sources: unknown source_id {sid}")
            used.append(sid)
            path = str(inputs[sid].get("path") or "")
            if path and path not in paths:
                paths.append(path)
    for path in paths:
        lines.append(f"- `{path}`")
    lines.extend(["", "## Item Source Map", ""])
    last_section = ""
    for item in visible:
        if item.section != last_section:
            lines.extend([f"### {SECTION_HEADINGS[item.section]}", ""])
            last_section = item.section
        meta = structured[(item.section, item.title)]
        label = f"产品日历 - {item.title}" if item.section == "release_calendar" else item.title
        lines.append(f"- {label} — {', '.join(_ids(meta.get('source_ids')))}")
    lines.extend(["", "## Source Details", ""])
    for sid in dict.fromkeys(used):
        source, title, url = _detail_signature(inputs[sid])
        lines.append(f"- {sid} | {source} | {title} | {url}")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    generate = sub.add_parser("generate-sources", help="Generate sources_used.md from report_items.json")
    generate.add_argument("--report", required=True)
    generate.add_argument("--inputs", required=True)
    generate.add_argument("--items", required=True)
    generate.add_argument("--output", required=True)
    validate = sub.add_parser("validate", help="Validate structured report closure")
    validate.add_argument("--report", required=True)
    validate.add_argument("--inputs", required=True)
    validate.add_argument("--items")
    validate.add_argument("--decisions")
    validate.add_argument("--release-audit")
    validate.add_argument("--sources")
    validate.add_argument("--require-artifacts", action="store_true")
    args = parser.parse_args()
    if args.command == "generate-sources":
        generate_sources_used(Path(args.report), Path(args.inputs), Path(args.items), Path(args.output))
        print(f"wrote {args.output}")
        return 0
    errors, warnings = validate_contract(
        Path(args.report), Path(args.inputs), Path(args.items) if args.items else None,
        Path(args.decisions) if args.decisions else None,
        Path(args.release_audit) if args.release_audit else None,
        Path(args.sources) if args.sources else None, args.require_artifacts,
    )
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
