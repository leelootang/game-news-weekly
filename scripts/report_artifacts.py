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
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


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
COMMUNITY_ATTRIBUTION = re.compile(r"(论坛帖|论坛讨论|社区帖|玩家帖|玩家讨论|据.*?(论坛|社区)|玩家在.*?(讨论|帖))")
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
            required = {"trigger", "claim_scope", "complaint_logic", "timeline", "follow_up_scan", "official_source_ids"}
            if not isinstance(community, dict) or not required.issubset(community):
                errors.append(f"community item lacks structured community fields: {title}")
            elif not _ids(community.get("official_source_ids")) and not COMMUNITY_ATTRIBUTION.search(next((x.body for x in report_items if (x.section, x.title) == key), "")):
                errors.append(f"community item without official source must be visibly attributed: {title}")
        if section == "release_calendar":
            release = item.get("release")
            if not isinstance(release, dict) or not {"product", "event", "date", "platform", "company"}.issubset(release):
                errors.append(f"release calendar item lacks product/event/date/platform/company: {title}")
            elif len(source_ids) < 2 and not release.get("official_single_source"):
                errors.append(f"release calendar item needs multi-source evidence or official_single_source: {title}")

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
        if decision.get("decision") not in {"include", "exclude"}:
            errors.append(f"decision must be include/exclude: {cid}")
        if not str(decision.get("reason") or "").strip():
            errors.append(f"decision missing reason: {cid}")
        if not str(decision.get("event") or "").strip():
            errors.append(f"decision must identify one concrete event: {cid}")
        priority_tracks = decision.get("priority_tracks", [])
        if not isinstance(priority_tracks, list) or not all(isinstance(track, str) for track in priority_tracks):
            errors.append(f"priority_tracks must be a list of strings: {cid}")
        else:
            unknown_tracks = sorted(set(priority_tracks) - PRIORITY_TRACKS)
            if unknown_tracks:
                errors.append(f"decision has unknown priority_tracks {unknown_tracks}: {cid}")
        if canonical_section(str(decision.get("section") or "")) == "industry":
            scores = decision.get("scores")
            if not isinstance(scores, dict) or not {"event", "entity", "region", "hook", "total"}.issubset(scores):
                errors.append(f"industry decision lacks four-dimensional scores: {cid}")
            elif decision.get("decision") == "include" and int(scores.get("total", -1)) < 7:
                errors.append(f"industry include has score below 7: {cid}")
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
        if not cid or cid not in decisions_by_id:
            errors.append(f"release audit node lacks a decision: {node.get('title') or cid}")
        elif canonical_section(str(decisions_by_id[cid].get("section") or "")) != "release_calendar":
            errors.append(f"release audit node decision is not release_calendar: {cid}")

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
