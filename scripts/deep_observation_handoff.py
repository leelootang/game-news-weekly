#!/usr/bin/env python3
"""Deterministic Thursday-selection to Friday-weekly-report handoff."""
from __future__ import annotations

import argparse
import re
from datetime import date, timedelta
from pathlib import Path


WEEKLY_ID_RE = re.compile(r"(?P<start>\d{4}-\d{2}-\d{2})_to_(?P<end>\d{4}-\d{2}-\d{2})")
ITEM_HEADING_RE = re.compile(r"(?m)^###\s+\d+\.\s+(?P<title>.+?)\s*$")


def selection_windows(thursday: date) -> tuple[str, str]:
    """Return (candidate_window, target_weekly_id) for a Thursday run."""
    candidate_start = thursday - timedelta(days=7)
    candidate_end = thursday - timedelta(days=1)
    report_start = thursday - timedelta(days=6)
    return (
        f"{candidate_start.isoformat()}_to_{candidate_end.isoformat()}",
        f"{report_start.isoformat()}_to_{thursday.isoformat()}",
    )


def weekly_id_from_report(report_path: Path) -> str | None:
    match = WEEKLY_ID_RE.search(report_path.name)
    if not match:
        match = WEEKLY_ID_RE.fullmatch(report_path.parent.name)
    return match.group(0) if match else None


def workspace_from_report(report_path: Path) -> Path:
    for parent in report_path.resolve().parents:
        if parent.name == "output":
            return parent.parent
    raise ValueError(f"report is not under an output directory: {report_path}")


def selection_path_for_report(report_path: Path) -> Path:
    weekly_id = weekly_id_from_report(report_path)
    if not weekly_id:
        raise ValueError(f"cannot infer weekly ID from report path: {report_path}")
    return workspace_from_report(report_path) / "output" / "deep_observation_review" / f"{weekly_id}_selection.md"


def _strip_card_prefix(title: str) -> str:
    return re.sub(r"^\s*★卡片[:：]\s*", "", title).strip()


def parse_selection(text: str) -> tuple[list[str], str | None]:
    """Return selected report titles and the single designated card title."""
    selected_block = ""
    block_match = re.search(
        r"(?ms)^##\s+用户选择进入周报的条目\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        text,
    )
    if block_match:
        selected_block = block_match.group("body")
    selected_titles = [_strip_card_prefix(match.group("title")) for match in ITEM_HEADING_RE.finditer(selected_block)]
    designated = [
        _strip_card_prefix(match.group("title"))
        for match in ITEM_HEADING_RE.finditer(text)
        if re.match(r"^\s*★卡片[:：]", match.group("title"))
    ]
    return selected_titles, designated[0] if len(designated) == 1 else None


def parse_deep_titles(report_text: str) -> list[str]:
    block_match = re.search(
        r"(?ms)^##\s+[^\n]*(?:行业精选|深度观察)[^\n]*\n(?P<body>.*?)(?=^##\s+|\Z)",
        report_text,
    )
    if not block_match:
        return []
    return [_strip_card_prefix(match.group("title")) for match in ITEM_HEADING_RE.finditer(block_match.group("body"))]


def validate_weekly_handoff(report_path: Path) -> list[str]:
    """Validate selection → report deep section → deep_card_choice.txt closure."""
    errors: list[str] = []
    weekly_id = weekly_id_from_report(report_path)
    if not weekly_id:
        return errors
    report_text = report_path.read_text(encoding="utf-8")
    deep_titles = parse_deep_titles(report_text)
    choice_path = report_path.parent / "deep_card_choice.txt"
    choice = choice_path.read_text(encoding="utf-8").strip() if choice_path.exists() else ""
    try:
        selection_path = selection_path_for_report(report_path)
    except ValueError:
        # Standalone fixtures and legacy exports outside output/ have no
        # deterministic workspace-level selection location.
        return errors

    if not selection_path.exists():
        match = WEEKLY_ID_RE.fullmatch(weekly_id)
        assert match
        report_start = date.fromisoformat(match.group("start"))
        report_end = date.fromisoformat(match.group("end"))
        legacy_id = (
            f"{(report_start - timedelta(days=1)).isoformat()}_to_"
            f"{(report_end - timedelta(days=1)).isoformat()}"
        )
        legacy_path = selection_path.with_name(f"{legacy_id}_selection.md")
        if legacy_path.exists():
            errors.append(
                "legacy candidate-window selection exists but target-weekly selection is missing: "
                f"{legacy_path} -> expected {selection_path}"
            )
        if deep_titles:
            errors.append(f"weekly deep section exists without exact selection file: {selection_path}")
        if choice:
            errors.append(f"deep_card_choice.txt exists without exact selection file: {selection_path}")
        return errors

    selection_text = selection_path.read_text(encoding="utf-8")
    selected_titles, designated = parse_selection(selection_text)
    star_count = len(re.findall(r"(?m)^###\s+\d+\.\s+★卡片[:：]", selection_text))
    if not selected_titles:
        errors.append(f"selection has no user-selected weekly items: {selection_path}")
    if star_count != 1 or not designated:
        errors.append(f"selection must contain exactly one designated card heading: {selection_path}")

    candidate_match = re.search(r"(?m)^-\s*候选数据窗口:\s*(\S+)\s*$", selection_text)
    target_match = re.search(r"(?m)^-\s*目标周报窗口:\s*(\S+)\s*$", selection_text)
    if not candidate_match or not target_match:
        errors.append(f"selection must declare 候选数据窗口 and 目标周报窗口: {selection_path}")
    else:
        target_id = target_match.group(1)
        if target_id != weekly_id:
            errors.append(f"selection target weekly ID mismatch: {target_id} != {weekly_id}")
        match = WEEKLY_ID_RE.fullmatch(weekly_id)
        assert match
        report_start = date.fromisoformat(match.group("start"))
        report_end = date.fromisoformat(match.group("end"))
        expected_candidate = (
            f"{(report_start - timedelta(days=1)).isoformat()}_to_"
            f"{(report_end - timedelta(days=1)).isoformat()}"
        )
        if candidate_match.group(1) != expected_candidate:
            errors.append(
                f"selection candidate window mismatch: {candidate_match.group(1)} != {expected_candidate}"
            )

    if selected_titles != deep_titles:
        errors.append(
            "weekly deep titles do not exactly match the user-selected titles: "
            f"selection={selected_titles!r}, report={deep_titles!r}"
        )
    if not choice:
        errors.append(f"deep_card_choice.txt missing for designated weekly card: {choice_path}")
    elif designated and _strip_card_prefix(choice) != designated:
        errors.append(f"deep_card_choice.txt does not match designated card: {choice!r} != {designated!r}")
    if choice and _strip_card_prefix(choice) not in deep_titles:
        errors.append(f"deep_card_choice.txt title is absent from weekly deep section: {choice!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    windows = sub.add_parser("windows")
    windows.add_argument("--thursday", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("--report", required=True)
    args = parser.parse_args()
    if args.command == "windows":
        candidate_window, weekly_id = selection_windows(date.fromisoformat(args.thursday))
        print(f"candidate_window={candidate_window}")
        print(f"target_weekly_id={weekly_id}")
        print(f"selection_filename={weekly_id}_selection.md")
        return 0
    errors = validate_weekly_handoff(Path(args.report))
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
