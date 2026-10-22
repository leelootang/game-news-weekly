"""Shared subject/genre scoring policy for reports, extraction and lint.

The skill ships identical copies of this module and the policy JSON so it also
works outside this checkout. Tests check that the installed copies agree.
"""
from __future__ import annotations

import calendar
import json
import re
from pathlib import Path


_BASE = Path(__file__).resolve().parents[1]
_POLICY_PATH = _BASE / "config" / "game_report_policy.json"
if not _POLICY_PATH.exists():
    _POLICY_PATH = _BASE / "references" / "report-policy.json"
POLICY = json.loads(_POLICY_PATH.read_text(encoding="utf-8"))
SCORING_VERSION = POLICY["scoring_version"]
ENFORCEMENT_START = POLICY["enforcement_start"]
THRESHOLD = POLICY["industry_threshold"]
MAX_SCORE = 10
FOCUS_COMPANY_PATTERNS = {
    row["name"]: re.compile(row["pattern"], re.IGNORECASE)
    for row in POLICY["focus_companies"]
}
GENRES = set(POLICY["priority_genres"])
SUBJECT_TIERS = {
    "focus_subject": 3, "priority_mobile_market": 3, "major_internet_gaming": 3,
    "focus_affiliate": 2, "focus_alumni_startup": 2, "other_mobile_market": 2,
    "representative_subject": 1, "pc_console_market": 1, "other_or_unknown": 0,
}


def report_end(path: Path) -> str:
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", path.name)
    if dates:
        return dates[-1]
    month = re.search(r"monthly_(\d{4})-(\d{2})", path.name)
    if month:
        y, m = map(int, month.groups())
        return f"{y:04d}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"
    return ""


def uses_subject_genre(document: object, report_path: Path) -> bool:
    return (
        isinstance(document, dict) and document.get("scoring_version") == SCORING_VERSION
    ) or report_end(report_path) >= ENFORCEMENT_START


def _evidence_errors(assessment: dict, decision: dict, inputs: dict, label: str,
                     required: bool) -> list[str]:
    cid = decision.get("candidate_id", "?")
    quotes = assessment.get("evidence", [])
    if not isinstance(quotes, list) or (required and not quotes):
        return [f"{label} needs source evidence: {cid}"]
    errors = []
    for quote in quotes:
        if not isinstance(quote, dict):
            errors.append(f"{label} evidence must be an object: {cid}")
            continue
        sid, text = quote.get("source_id"), quote.get("evidence")
        if (sid not in decision.get("source_ids", []) or not isinstance(text, str)
                or not text.strip() or text not in str(inputs.get(sid, {}).get("text", ""))):
            errors.append(f"{label} evidence not found in candidate input: {cid}/{sid}")
    return errors


def validate_scoring_document(document: object, inputs: dict, report_path: Path) -> list[str]:
    """Enforce numeric rules and auditable judgments; never infer ownership.

    Source quotes allow review of the human/model judgment. They do not prove
    that an event is important, that ownership is direct, or that a genre fits.
    """
    if not uses_subject_genre(document, report_path):
        return []
    errors = []
    if not isinstance(document, dict) or document.get("scoring_version") != SCORING_VERSION:
        errors.append(f"new report requires scoring_version={SCORING_VERSION}")
    rows = document.get("decisions", []) if isinstance(document, dict) else document
    if not isinstance(rows, list):
        return errors + ["scoring decisions must be a list"]
    for decision in rows:
        if not isinstance(decision, dict) or decision.get("section") not in {"industry", "industry_news"}:
            continue
        cid = decision.get("candidate_id", "?")
        scores = decision.get("scores", {})
        if not isinstance(scores, dict):
            errors.append(f"industry scores must be an object: {cid}")
            continue
        e, r, m, total = (scores.get(key) for key in ("event", "relevance", "hook", "total"))
        if any(type(x) is not int for x in (e, r, m, total)):
            errors.append(f"industry scores must be integers: {cid}")
            continue
        if e not in range(4) or r not in range(4) or m not in (0, 1):
            errors.append(f"subject_genre_v2 score out of range (E/R 0-3, M 0-1): {cid}")
        if total != e * r + m:
            errors.append(f"industry total must equal E×R+M: {cid}")
        if decision.get("decision") == "include" and (e == 0 or total < THRESHOLD):
            errors.append(f"industry include fails E×R+M threshold (required >= {THRESHOLD}): {cid}")
        # Routine E0 signals may keep compact batch audit records.
        if e == 0:
            continue
        subject = decision.get("subject_assessment")
        if not isinstance(subject, dict):
            errors.append(f"industry decision needs subject_assessment: {cid}")
        else:
            kind = subject.get("kind")
            if not isinstance(kind, str) or kind not in SUBJECT_TIERS or SUBJECT_TIERS[kind] != r:
                errors.append(f"subject_assessment kind does not match R: {cid}")
            if not str(subject.get("subject") or "").strip() or not str(subject.get("basis") or "").strip():
                errors.append(f"subject_assessment needs subject and factual basis: {cid}")
            errors.extend(_evidence_errors(subject, decision, inputs, "subject_assessment", r > 0))
            companies = subject.get("focus_companies", [])
            if (not isinstance(companies, list) or any(not isinstance(x, str) or x not in FOCUS_COMPANY_PATTERNS for x in companies)):
                errors.append(f"subject_assessment has unknown focus_companies: {cid}")
            elif kind in {"focus_subject", "focus_affiliate", "focus_alumni_startup"} and not companies:
                errors.append(f"subject_assessment needs named focus_companies: {cid}")
            else:
                quote_text = "\n".join(str(q.get("evidence", "")) for q in subject.get("evidence", []) if isinstance(q, dict)) if isinstance(subject.get("evidence", []), list) else ""
                for company in companies:
                    if not FOCUS_COMPANY_PATTERNS[company].search(quote_text):
                        errors.append(f"focus company not supported by subject evidence: {cid}/{company}")
            if kind == "representative_subject" and not str(subject.get("representative_product") or "").strip():
                errors.append(f"representative_subject needs representative_product and source basis: {cid}")
            # A parent mentioned as background must not turn an affiliate into R3.
            named = str(subject.get("subject") or "").strip()
            if any(pattern.fullmatch(named) for pattern in FOCUS_COMPANY_PATTERNS.values()) and r != 3:
                errors.append(f"listed focus subject must receive R=3: {cid}")
        genre = decision.get("genre_assessment")
        if not isinstance(genre, dict):
            errors.append(f"industry decision needs genre_assessment: {cid}")
        else:
            matched = genre.get("matched_genres")
            if not isinstance(matched, list) or any(not isinstance(x, str) or x not in GENRES for x in matched):
                errors.append(f"genre_assessment has invalid matched_genres: {cid}")
            elif m != int(bool(matched)):
                errors.append(f"M must be 1 for a matched priority genre, otherwise 0: {cid}")
            if not str(genre.get("basis") or "").strip():
                errors.append(f"genre_assessment needs factual basis: {cid}")
            errors.extend(_evidence_errors(genre, decision, inputs, "genre_assessment", m == 1))
    return errors
