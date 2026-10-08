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
import datetime as dt
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
COMMUNITY_CAP_ENFORCEMENT_START = "2026-08-11"
DEEP_CARD_COPY_ENFORCEMENT_START = "2026-08-17"
SOURCE_ID_RE = re.compile(r"\bS\d{4}\b")
ABSOLUTE_DATE_CLAIM_RE = re.compile(
    r"(?:20\d{2}[年./-]\d{1,2}(?:[月./-]\d{1,2}日?)?|\d{1,2}\s*月\s*\d{1,2}\s*日)"
)
RELATIVE_3839_TIME_RE = re.compile(r"今天|今日|明天|明日|明早|后天")
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
COMMUNITY_COUNT = re.compile(
    r"(?:\d+\s*(?:条)?回复|\d+\s*页|浏览(?:量)?\s*\d+|热度\s*\d+|"
    r"回复\s*[：:]\s*\d+|页数\s*[：:]\s*\d+|综合热度分|收录依据|created\s*@)",
    re.IGNORECASE,
)
PIPELINE_LEAK = re.compile(
    r"(?:GameLook专稿|禁止转载|GameLook报道/|"
    r"\bSource\s*:\s*|回复\s*[：:]\s*\d+|页数\s*[：:]\s*\d+|"
    r"收录依据\s*[：:]|created\s*@|发布于\s+\S+\s+游戏新知|"
    r"(?:【|\[)\s*(?:补位|上期卡片未展示)\s*(?:】|\])|"
    r"上期卡片未展示|card_carryover)",
    re.IGNORECASE,
)
RELEASE_EVENT = re.compile(r"上线|公测|内测|首测|删档测试|不删档|付费测试|测试|抢先体验|EA|发售|发布|预约|开测|定档|上市|开服|重启|复活|停运|延期|跳票", re.I)
PRIORITY_TRACKS = {"pvp_competitive", "strategy_card_rpg", "life_simulation"}
IMPORTANT_INDUSTRY_SUBJECTS = {
    "Roblox": re.compile(r"^(?:roblox(?: corporation)?|罗布乐思)$", re.IGNORECASE),
    "Supercell": re.compile(r"^(?:supercell(?: oy)?|超级细胞)$", re.IGNORECASE),
    "Riot Games": re.compile(r"^(?:riot(?: games?)?|拳头(?:游戏|公司)?)$", re.IGNORECASE),
}
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


def invalid_3839_absolute_date_evidence(record: dict[str, Any], claim_text: str, evidence: str) -> bool:
    """Reject absolute claims backed only by a relative 3839 timeline phrase.

    The check is gated by the new collector audit fields so legacy report
    snapshots keep their historical validation behavior.
    """
    if str(record.get("source_key") or "") != "haoyou_kuaibao_3839":
        return False
    source_text = str(record.get("text") or "")
    if "Date resolution:" not in source_text:
        return False
    if not ABSOLUTE_DATE_CLAIM_RE.search(claim_text):
        return False
    return bool(
        RELATIVE_3839_TIME_RE.search(evidence)
        and not ABSOLUTE_DATE_CLAIM_RE.search(evidence)
    )


def release_cap_for_report(report_path: Path) -> int:
    if "game_industry_weekly_" in report_path.name:
        return 7
    if "game_industry_monthly_" in report_path.name:
        return 12
    return 4


def community_cap_for_report(report_path: Path) -> int | None:
    """Return the hard player-discourse cap for report kinds that define one."""
    name = report_path.name
    if "game_industry_weekly_" in name:
        return 3
    if "game_industry_daily_" in name or "game_industry_weekend_" in name:
        return 2
    return None


def community_cap_is_enforced(report_path: Path) -> bool:
    """Grandfather reports whose covered window ended before this rule shipped."""
    report_dates = re.findall(r"\d{4}-\d{2}-\d{2}", report_path.name)
    return bool(report_dates and max(report_dates) >= COMMUNITY_CAP_ENFORCEMENT_START)


def deep_card_copy_is_enforced(report_path: Path) -> bool:
    """Require compact deep-card copy only for reports created under the new contract."""
    report_dates = re.findall(r"\d{4}-\d{2}-\d{2}", report_path.name)
    return bool(report_dates and max(report_dates) >= DEEP_CARD_COPY_ENFORCEMENT_START)


def normalize_deep_card_copy(
    value: Any, title: str = ""
) -> tuple[str, str, list[dict[str, str]]]:
    """Validate and normalize the compact copy used by standalone deep cards."""
    label = f": {title}" if title else ""
    if not isinstance(value, dict):
        raise ValueError(f"deep item lacks card_copy{label}")

    source_label = str(value.get("source_label") or "").strip()
    if not source_label:
        raise ValueError(f"deep card_copy source_label is empty{label}")
    if any(mark in source_label for mark in ("\n", "\r", "：", ":")):
        raise ValueError(f"deep card_copy source_label must be one line without a colon{label}")
    if len(source_label) > 40:
        raise ValueError(f"deep card_copy source_label exceeds 40 characters{label}")
    if PIPELINE_LEAK.search(source_label):
        raise ValueError(f"deep card_copy source_label leaks source/pipeline metadata{label}")

    summary = str(value.get("summary") or "").strip()
    if not summary:
        raise ValueError(f"deep card_copy summary is empty{label}")
    if "\n" in summary or "\r" in summary:
        raise ValueError(f"deep card_copy summary must be one line{label}")
    if len(summary) > 100:
        raise ValueError(f"deep card_copy summary exceeds 100 characters{label}")
    if re.search(r"观察\s*[：:]|分析\s*[：:]", summary):
        raise ValueError(f"deep card_copy summary must not reuse 观察/分析 labels{label}")
    if PIPELINE_LEAK.search(summary):
        raise ValueError(f"deep card_copy summary leaks source/pipeline metadata{label}")

    raw_insights = value.get("insights")
    if not isinstance(raw_insights, list) or not 3 <= len(raw_insights) <= 6:
        raise ValueError(f"deep card_copy insights must contain 3-6 items{label}")

    insights: list[dict[str, str]] = []
    seen_titles: set[str] = set()
    for index, insight in enumerate(raw_insights, 1):
        if not isinstance(insight, dict):
            raise ValueError(f"deep card_copy insight {index} must be an object{label}")
        insight_title = str(insight.get("title") or "").strip()
        detail = str(insight.get("detail") or "").strip()
        if not insight_title or not detail:
            raise ValueError(f"deep card_copy insight {index} needs title and detail{label}")
        if any(mark in insight_title or mark in detail for mark in ("\n", "\r")):
            raise ValueError(f"deep card_copy insight {index} must stay on one line per field{label}")
        if len(insight_title) > 30:
            raise ValueError(f"deep card_copy insight {index} title exceeds 30 characters{label}")
        if len(detail) > 160:
            raise ValueError(f"deep card_copy insight {index} detail exceeds 160 characters{label}")
        if insight_title in seen_titles:
            raise ValueError(f"deep card_copy insight titles must be unique{label}")
        if re.search(r"观察\s*[：:]|分析\s*[：:]", f"{insight_title}\n{detail}"):
            raise ValueError(f"deep card_copy insights must not reuse 观察/分析 labels{label}")
        if PIPELINE_LEAK.search(f"{insight_title}\n{detail}"):
            raise ValueError(f"deep card_copy insight {index} leaks source/pipeline metadata{label}")
        seen_titles.add(insight_title)
        insights.append({"title": insight_title, "detail": detail})
    return source_label, summary, insights


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


def important_industry_subjects(decision: dict[str, Any]) -> list[str]:
    """Return fixed highest-attention subjects explicitly named by the candidate."""
    entities = decision.get("entities", [])
    if not isinstance(entities, list):
        return []
    return [
        subject
        for subject, pattern in IMPORTANT_INDUSTRY_SUBJECTS.items()
        if any(
            isinstance(entity, str) and pattern.fullmatch(entity.strip())
            for entity in entities
        )
    ]


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
            detail_match = re.match(
                r"^-\s+(S\d{4})\s+\|\s+(.*?)\s+\|\s+(.*?)\s+\|\s+(https?://\S+)\s*$",
                line,
            )
            if detail_match:
                details[detail_match.group(1)] = (
                    detail_match.group(2),
                    detail_match.group(3),
                    detail_match.group(4),
                )
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


def validate_industry_history_check(
    decision: dict[str, Any],
    candidate_id: str,
    require_card_exposure: bool = False,
) -> list[str]:
    """Validate the semantic audit gate used with industry_history_14d.json."""
    errors: list[str] = []
    check = decision.get("history_check")
    required = {"history_match", "novelty", "prior_occurrences", "new_facts"}
    if require_card_exposure:
        required.add("prior_card_exposed")
    if not isinstance(check, dict) or not required.issubset(check):
        return [f"industry decision lacks 14-day history_check: {candidate_id}"]
    if not isinstance(check.get("history_match"), bool):
        errors.append(f"history_check.history_match must be boolean: {candidate_id}")
    novelty = check.get("novelty")
    if novelty not in {"new_event", "repeat_only", "material_update", "card_carryover"}:
        errors.append(f"history_check.novelty is invalid: {candidate_id}")
    prior = check.get("prior_occurrences")
    new_facts = check.get("new_facts")
    if not isinstance(prior, list) or not all(isinstance(value, str) and value.strip() for value in prior):
        errors.append(f"history_check.prior_occurrences must be a string list: {candidate_id}")
    if not isinstance(new_facts, list) or not all(isinstance(value, str) and value.strip() for value in new_facts):
        errors.append(f"history_check.new_facts must be a string list: {candidate_id}")
    if check.get("history_match") is True and isinstance(prior, list) and not prior:
        errors.append(f"history match must cite prior occurrences: {candidate_id}")
    if require_card_exposure:
        prior_card_exposed = check.get("prior_card_exposed")
        if check.get("history_match") is True and not isinstance(prior_card_exposed, bool):
            errors.append(f"history match must record boolean prior_card_exposed: {candidate_id}")
        if check.get("history_match") is False and prior_card_exposed is not None:
            errors.append(f"new event prior_card_exposed must be null: {candidate_id}")
    if novelty == "repeat_only" and decision.get("decision") == "include":
        errors.append(f"repeat-only industry event cannot be included: {candidate_id}")
    if novelty == "material_update" and decision.get("decision") == "include" and isinstance(new_facts, list) and not new_facts:
        errors.append(f"material-update include must identify new facts: {candidate_id}")
    if novelty == "card_carryover":
        if decision.get("decision") != "include":
            errors.append(f"card-carryover decision must be included: {candidate_id}")
        if decision.get("card_carryover") is not True:
            errors.append(f"card-carryover include must set card_carryover=true: {candidate_id}")
        if check.get("history_match") is not True:
            errors.append(f"card-carryover must match report history: {candidate_id}")
        if check.get("prior_card_exposed") is not False:
            errors.append(f"card-carryover requires prior_card_exposed=false: {candidate_id}")
    elif decision.get("card_carryover") is True:
        errors.append(f"card_carryover=true requires novelty=card_carryover: {candidate_id}")
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
    community_cap = community_cap_for_report(report_path)
    community_count = sum(item.section == "community" for item in report_items)
    if (
        community_cap is not None
        and community_cap_is_enforced(report_path)
        and community_count > community_cap
    ):
        errors.append(
            f"community discourse exceeds report cap {community_cap}: {community_count}"
        )
    history_path = inputs_path.parent / "industry_history_14d.json"
    industry_history_required = False
    card_exposure_required = False
    if history_path.exists():
        history_data = read_json(history_path)
        industry_history_required = (
            isinstance(history_data, dict)
            and history_data.get("enforce_history_check") is True
        )
        card_exposure_required = (
            isinstance(history_data, dict)
            and history_data.get("enforce_card_exposure_check") is True
        )
    for item in report_items:
        if PIPELINE_LEAK.search(f"{item.title}\n{item.body}"):
            errors.append(f"published item leaks source/pipeline metadata: {item.section}/{item.title}")
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
    try:
        audit_schema_version = int(audit.get("schema_version") or 0) if isinstance(audit, dict) else 0
    except (TypeError, ValueError):
        audit_schema_version = 0
    audit_nodes = audit.get("nodes", []) if isinstance(audit, dict) else []
    if not isinstance(audit_nodes, list):
        errors.append("release_calendar_audit.json nodes must be a list")
        return errors, warnings

    report_window_match = re.search(
        r"(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})",
        str(report_path),
    )
    if report_window_match:
        release_window_start, report_window_end = report_window_match.groups()
    else:
        daily_window_match = re.search(
            r"game_industry_daily_(\d{4}-\d{2}-\d{2})\.md$",
            report_path.name,
        )
        release_window_start = report_window_end = (
            daily_window_match.group(1) if daily_window_match else ""
        )
    expected_release_lookahead = (
        1
        if any(
            marker in report_path.name
            for marker in (
                "game_industry_daily_",
                "game_industry_weekly_",
                "game_industry_weekend_",
            )
        )
        else 0
    )
    release_window_end = report_window_end
    if report_window_end and expected_release_lookahead:
        release_window_end = (
            dt.date.fromisoformat(report_window_end)
            + dt.timedelta(days=expected_release_lookahead)
        ).isoformat()
    if audit_schema_version >= 5:
        try:
            actual_release_lookahead = int(audit.get("release_lookahead_days"))
        except (TypeError, ValueError):
            actual_release_lookahead = -1
        if actual_release_lookahead != expected_release_lookahead:
            errors.append(
                "release audit lookahead does not match report type: "
                f"{actual_release_lookahead}/{expected_release_lookahead}"
            )
        audit_report_window = audit.get("report_window")
        audit_release_window = audit.get("release_window")
        if (
            not isinstance(audit_report_window, dict)
            or audit_report_window.get("start") != release_window_start
            or audit_report_window.get("end") != report_window_end
        ):
            errors.append("release audit report_window does not match report filename")
        if (
            not isinstance(audit_release_window, dict)
            or audit_release_window.get("start") != release_window_start
            or audit_release_window.get("end") != release_window_end
        ):
            errors.append("release audit release_window does not match product-calendar window")

    visible = [(item.section, item.title) for item in report_items]
    visible_by_key = {(item.section, item.title): item for item in report_items}
    structured: dict[tuple[str, str], dict[str, Any]] = {}
    structured_by_candidate: dict[str, dict[str, Any]] = {}
    source_signatures: dict[tuple[str, tuple[str, ...]], str] = {}
    claim_lengths: list[int] = []
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
        candidate_id = str(item.get("candidate_id") or "").strip()
        if candidate_id:
            if candidate_id in structured_by_candidate:
                errors.append(f"duplicate published candidate_id: {candidate_id}")
            structured_by_candidate[candidate_id] = item
        source_ids = _ids(item.get("source_ids"))
        if not source_ids:
            errors.append(f"report item has no source_ids: {section}/{title}")
        source_signature = (section, tuple(sorted(source_ids)))
        if source_ids and source_signature in source_signatures:
            errors.append(
                f"duplicate source set in {section}: "
                f"{source_signatures[source_signature]} / {title}"
            )
        elif source_ids:
            source_signatures[source_signature] = title
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
                if claim_text:
                    claim_lengths.append(len(claim_text))
                if not claim_text or claim_text not in visible_by_key[key].body:
                    errors.append(f"claim text is not present in final item: {title}")
                if sid not in source_ids:
                    errors.append(f"claim source_id is not item source: {title}/{sid}")
                claim_record = inputs.get(sid, {})
                if sid in source_ids and evidence not in str(claim_record.get("text") or ""):
                    errors.append(f"claim evidence not found in input text: {title}/{sid}")
                elif sid in source_ids and invalid_3839_absolute_date_evidence(
                    claim_record, claim_text, evidence
                ):
                    errors.append(
                        f"3839 absolute date claim uses relative-only evidence: {title}/{sid}"
                    )
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
        if section == "deep" and (deep_card_copy_is_enforced(report_path) or "card_copy" in item):
            try:
                normalize_deep_card_copy(item.get("card_copy"), title)
            except ValueError as exc:
                errors.append(str(exc))

    if len(claim_lengths) >= 5:
        dominant = max(set(claim_lengths), key=claim_lengths.count)
        if dominant >= 60 and claim_lengths.count(dominant) / len(claim_lengths) >= 0.8:
            errors.append(
                "claim evidence appears mechanically truncated: "
                f"{claim_lengths.count(dominant)}/{len(claim_lengths)} claims are exactly {dominant} characters"
            )

    if set(visible) != set(structured):
        for section, title in sorted(set(visible) - set(structured)):
            errors.append(f"published item missing report_items entry: {section}/{title}")
        for section, title in sorted(set(structured) - set(visible)):
            errors.append(f"report_items entry not in final markdown: {section}/{title}")

    decisions_by_id: dict[str, dict[str, Any]] = {}
    included_card_carryovers: list[str] = []
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
            if industry_history_required:
                errors.extend(
                    validate_industry_history_check(
                        decision,
                        cid,
                        require_card_exposure=card_exposure_required,
                    )
                )
            if decision.get("decision") == "include" and decision.get("card_carryover") is True:
                included_card_carryovers.append(cid)
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
                    for subject in important_industry_subjects(decision):
                        if relevance != 3:
                            errors.append(
                                f"{subject} industry subject must receive highest relevance R=3: {cid}"
                            )
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
    if len(included_card_carryovers) > 1:
        errors.append(
            "at most one industry card_carryover may be included per report: "
            + ", ".join(included_card_carryovers)
        )
    for key, item in structured.items():
        cid = str(item.get("candidate_id") or "")
        decision = decisions_by_id.get(cid)
        if not cid or not decision:
            errors.append(f"published item has no selection decision: {key[0]}/{key[1]}")
        elif decision.get("decision") != "include":
            errors.append(f"published item maps to non-include decision {cid}: {key[1]}")

    published_candidate_ids = set(structured_by_candidate)
    for cid, decision in decisions_by_id.items():
        if decision.get("decision") == "include" and cid not in published_candidate_ids:
            errors.append(f"include decision is missing from final report: {cid}")

    industry_sources: dict[str, str] = {}
    ai_sources: dict[str, str] = {}
    for (section, title), item in structured.items():
        destination = industry_sources if section == "industry" else ai_sources if section == "ai" else None
        if destination is not None:
            for sid in _ids(item.get("source_ids")):
                destination[sid] = title
    for sid in sorted(set(industry_sources) & set(ai_sources)):
        errors.append(
            f"same source is published in both industry and AI: "
            f"{sid} ({industry_sources[sid]} / {ai_sources[sid]})"
        )

    industry_score_order: list[tuple[str, int]] = []
    for report_item in report_items:
        if report_item.section != "industry":
            continue
        structured_item = structured.get((report_item.section, report_item.title), {})
        decision = decisions_by_id.get(str(structured_item.get("candidate_id") or ""), {})
        scores = decision.get("scores") if isinstance(decision, dict) else None
        if isinstance(scores, dict):
            try:
                industry_score_order.append((report_item.title, int(scores.get("total"))))
            except (TypeError, ValueError):
                pass
    for (previous_title, previous_score), (title, score) in zip(
        industry_score_order, industry_score_order[1:]
    ):
        if score > previous_score:
            errors.append(
                f"industry items are not sorted by score: "
                f"{previous_title} ({previous_score}) before {title} ({score})"
            )

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
        if audit_schema_version >= 5:
            event_date = str(node.get("event_date") or "")
            signal_type = str(node.get("signal_type") or "")
            expected_scope = (
                "report_window"
                if release_window_start and report_window_end and release_window_start <= event_date <= report_window_end
                else "next_day_lookahead"
                if report_window_end and release_window_end and report_window_end < event_date <= release_window_end
                else "future_announcement"
                if signal_type in {"new_game_schedule", "new_game_first_reveal"}
                else "outside"
            )
            if node.get("window_scope") != expected_scope:
                errors.append(
                    f"release window_scope drift from audit window: {cid}/"
                    f"{node.get('window_scope')}/{expected_scope}"
                )
        if audit_schema_version >= 4:
            company_bonus = int(node.get("company_bonus") or 0)
            configured_bonus = int(audit.get("focus_company_bonus") or 0)
            configured_investment_bonus = int(
                audit.get("focus_company_investment_bonus") or 0
            )
            focus_companies = node.get("focus_companies")
            company_evidence_ids = _ids(node.get("company_evidence_ids"))
            allowed_company_bonuses = {0, configured_bonus}
            if configured_investment_bonus:
                allowed_company_bonuses.add(configured_investment_bonus)
            if company_bonus not in allowed_company_bonuses:
                errors.append(f"release company bonus is not configured value: {cid}/{company_bonus}")
            if company_bonus:
                if not isinstance(focus_companies, list) or not all(
                    isinstance(value, str) and value.strip() for value in focus_companies
                ):
                    errors.append(f"release company bonus lacks focus_companies: {cid}")
                if not company_evidence_ids:
                    errors.append(f"release company bonus lacks company evidence: {cid}")
                elif not set(company_evidence_ids).issubset(set(_ids(node.get("source_ids")))):
                    errors.append(f"release company evidence is outside node sources: {cid}")
                if not str(node.get("signal_type") or "").startswith("new_game_"):
                    errors.append(f"old-product release signal cannot receive company bonus: {cid}")
                relationship = str(node.get("company_relationship") or "")
                if configured_investment_bonus and company_bonus == configured_investment_bonus:
                    if relationship != "investment":
                        errors.append(f"release investment bonus lacks investment relationship: {cid}")
                elif relationship and relationship != "direct":
                    errors.append(f"release direct bonus has invalid company relationship: {cid}")
        if decision:
            scores = decision.get("scores")
            required_release_scores = {"event", "source", "total"}
            if audit_schema_version >= 4:
                required_release_scores.add("company")
            if not isinstance(scores, dict) or not required_release_scores.issubset(scores):
                errors.append(f"release decision lacks event×source+company scores: {cid}")
            else:
                expected_event = int(node.get("event_type_score") or 0)
                expected_source = int(node.get("source_strength_score") or 0)
                expected_company = int(node.get("company_bonus") or 0)
                expected_total = int(node.get("priority_score") or 0)
                try:
                    actual_event = int(scores["event"])
                    actual_source = int(scores["source"])
                    actual_company = int(scores.get("company") or 0)
                    actual_total = int(scores["total"])
                except (TypeError, ValueError):
                    errors.append(f"release event×source+company scores must be integers: {cid}")
                else:
                    expected = (
                        expected_event,
                        expected_source,
                        expected_company if audit_schema_version >= 4 else 0,
                        expected_total,
                    )
                    actual = (actual_event, actual_source, actual_company, actual_total)
                    if actual != expected:
                        errors.append(f"release event×source+company scores drift from audit: {cid}")
                    expected_formula_total = actual_event * actual_source + (
                        actual_company if audit_schema_version >= 4 else 0
                    )
                    if actual_total != expected_formula_total:
                        errors.append(f"release total must equal event×source+company: {cid}")
            if decision.get("decision") == "include" and int(node.get("appearance_count") or 0) < 2:
                errors.append(f"release include must have multi-source evidence: {cid}")
            if decision.get("decision") == "include":
                event_date = str(node.get("event_date") or "").strip()
                date_match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", event_date)
                if not date_match:
                    errors.append(f"release include has invalid event_date: {cid}/{event_date}")
                else:
                    _year, month, day = date_match.groups()
                    date_forms = (
                        event_date,
                        f"{int(month)}月{int(day)}日",
                        f"{int(month)} 月 {int(day)} 日",
                    )
                    source_texts = [
                        str(inputs.get(sid, {}).get("text") or "")
                        for sid in _ids(node.get("source_ids"))
                    ]
                    if not any(
                        any(date_form in source_text for date_form in date_forms)
                        for source_text in source_texts
                    ):
                        errors.append(
                            f"release include date is not evidenced by any source: "
                            f"{cid}/{event_date}"
                        )
                    signal_type = str(node.get("signal_type") or "")
                    if (
                        release_window_start
                        and signal_type not in {"new_game_schedule", "new_game_first_reveal"}
                        and not (release_window_start <= event_date <= release_window_end)
                    ):
                        errors.append(
                            f"release include event is outside product-calendar window: "
                            f"{cid}/{event_date}/{signal_type}"
                        )

    if audit_schema_version >= 4:
        relationship_tier_enabled = bool(audit.get("focus_company_investment_bonus"))
        expected_audit_order = sorted(
            audit_nodes,
            key=lambda node: (
                -int(bool(node.get("publish_eligible"))),
                -int(node.get("priority_score") or 0),
                -int(node.get("company_bonus") or 0),
                -int(node.get("event_type_score") or 0),
                -int(node.get("appearance_count") or 0),
                -int(node.get("industry_bonus") or 0),
                int(node.get("first_seen_order") or 0),
            ) if relationship_tier_enabled else (
                -int(bool(node.get("publish_eligible"))),
                -int(node.get("priority_score") or 0),
                -int(node.get("event_type_score") or 0),
                -int(node.get("company_bonus") or 0),
                -int(node.get("appearance_count") or 0),
                -int(node.get("industry_bonus") or 0),
                int(node.get("first_seen_order") or 0),
            ),
        )
        if [
            str(node.get("candidate_id") or "") for node in audit_nodes
        ] != [
            str(node.get("candidate_id") or "") for node in expected_audit_order
        ]:
            errors.append("release audit nodes are not sorted by the configured priority rule")

    release_includes = [
        str(d.get("candidate_id") or "") for d in decisions_by_id.values()
        if canonical_section(str(d.get("section") or "")) == "release_calendar" and d.get("decision") == "include"
    ]
    release_cap = release_cap_for_report(report_path)
    if len(release_includes) > release_cap:
        errors.append(f"release calendar exceeds report cap {release_cap}: {len(release_includes)}")
    eligible_order = [
        str(node.get("candidate_id") or "") for node in audit_nodes
        if (
            bool(node.get("publish_eligible"))
            if "publish_eligible" in node
            else int(node.get("appearance_count") or 0) >= 2
        )
    ]
    if release_includes != eligible_order[:len(release_includes)]:
        errors.append("release includes must be a priority-ranked prefix of multi-source candidates")

    for item in report_items:
        if item.section == "community" and COMMUNITY_COUNT.search(item.body):
            errors.append(f"community item contains reply/page/heat count: {item.title}")
        if item.section == "deep":
            normalized_deep = re.sub(
                r"^\*{0,2}(观察：)\*{0,2}",
                r"\1",
                item.body.lstrip(),
            )
            if not normalized_deep.startswith("观察："):
                errors.append(f"deep item must start with 观察： {item.title}")
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
