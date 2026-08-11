from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from scripts.build_industry_history import collect_history
from scripts.report_artifacts import validate_industry_history_check


def _write_report(root: Path, day: str, event: str, decision: str = "include") -> None:
    intermediate = root / "output" / "daily" / day / "_intermediate"
    intermediate.mkdir(parents=True)
    (intermediate / "selection_decisions.json").write_text(
        json.dumps(
            {
                "decisions": [
                    {
                        "candidate_id": "I001",
                        "section": "industry_news",
                        "event": event,
                        "entities": ["腾讯", "SuperPlay"],
                        "decision": decision,
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (intermediate / "report_items.json").write_text(
        json.dumps(
            {
                "items": [
                    {
                        "section": "industry",
                        "title": event,
                        "candidate_id": "I001",
                        "source_ids": ["S0001"],
                        "claims": [{"claim": "仍处于谈判阶段"}],
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def _write_ranked_report(root: Path, day: str, count: int = 12) -> None:
    intermediate = root / "output" / "daily" / day / "_intermediate"
    intermediate.mkdir(parents=True)
    decisions = []
    items = []
    for index in range(1, count + 1):
        candidate_id = f"I{index:03d}"
        title = f"行业事件{index:02d}"
        decisions.append(
            {
                "candidate_id": candidate_id,
                "section": "industry_news",
                "event": title,
                "entities": [title],
                "decision": "include",
            }
        )
        items.append(
            {
                "section": "industry",
                "title": title,
                "candidate_id": candidate_id,
                "source_ids": [f"S{index:04d}"],
                "claims": [{"claim": title}],
            }
        )
    (intermediate / "selection_decisions.json").write_text(
        json.dumps({"decisions": decisions}, ensure_ascii=False), encoding="utf-8"
    )
    (intermediate / "report_items.json").write_text(
        json.dumps({"items": items}, ensure_ascii=False), encoding="utf-8"
    )


def _write_publish_log(root: Path, day: str, **extra: object) -> None:
    log_dir = root / "data" / "feishu" / "publish_logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "date": day,
        "subscriber_count": 2,
        "results": [{"open_id": "a", "ok": True}, {"open_id": "b", "ok": True}],
        **extra,
    }
    (log_dir / f"daily_{day}.json").write_text(
        json.dumps(payload, ensure_ascii=False), encoding="utf-8"
    )


def test_collects_only_included_industry_items_inside_prior_14_days(tmp_path: Path) -> None:
    _write_report(tmp_path, "2026-07-20", "腾讯洽购SuperPlay")
    _write_report(tmp_path, "2026-07-21", "排除事件", decision="exclude")
    _write_report(tmp_path, "2026-07-01", "窗口外旧闻")

    history = collect_history(tmp_path, date(2026, 7, 28))

    assert history["history_window"] == {"start": "2026-07-14", "end": "2026-07-27"}
    assert [row["event"] for row in history["occurrences"]] == ["腾讯洽购SuperPlay"]
    assert history["occurrences"][0]["claims"] == ["仍处于谈判阶段"]


def test_reads_legacy_report_markdown_when_structured_artifacts_are_absent(tmp_path: Path) -> None:
    report_dir = tmp_path / "output" / "daily" / "2026-07-20"
    report_dir.mkdir(parents=True)
    (report_dir / "game_industry_daily_2026-07-20.md").write_text(
        "# 游戏行业日报\n\n"
        "## 一、行业新闻\n"
        "### 1. 腾讯洽购SuperPlay\n\n"
        "交易仍处谈判阶段。\n\n"
        "## 二、AI 新闻\n",
        encoding="utf-8",
    )

    history = collect_history(tmp_path, date(2026, 7, 28))

    assert history["occurrences"][0]["legacy_fallback"] is True
    assert history["occurrences"][0]["event"] == "腾讯洽购SuperPlay"


def test_history_gate_rejects_repeat_include_and_empty_material_update() -> None:
    repeat = {
        "decision": "include",
        "history_check": {
            "history_match": True,
            "novelty": "repeat_only",
            "prior_occurrences": ["2026-07-20 日报"],
            "new_facts": [],
        },
    }
    update = {
        "decision": "include",
        "history_check": {
            "history_match": True,
            "novelty": "material_update",
            "prior_occurrences": ["2026-07-20 日报"],
            "new_facts": [],
        },
    }

    assert any("repeat-only" in error for error in validate_industry_history_check(repeat, "I001"))
    assert any("new facts" in error for error in validate_industry_history_check(update, "I002"))


def test_legacy_publish_log_infers_first_ten_card_exposures(tmp_path: Path) -> None:
    _write_ranked_report(tmp_path, "2026-07-20")
    _write_publish_log(tmp_path, "2026-07-20")

    history = collect_history(tmp_path, date(2026, 7, 28))
    by_id = {row["candidate_id"]: row for row in history["occurrences"]}

    assert by_id["I010"]["card_exposed"] is True
    assert by_id["I010"]["card_rank"] == 10
    assert by_id["I011"]["card_exposed"] is False
    assert by_id["I011"]["card_exposure_source"] == "legacy_position_inference"


def test_publish_manifest_is_exact_card_exposure_source(tmp_path: Path) -> None:
    _write_ranked_report(tmp_path, "2026-07-20")
    manifest = [
        {
            "section": "industry",
            "candidate_id": f"I{index:03d}",
            "title": f"行业事件{index:02d}",
            "position": position,
            "card_carryover": index == 12,
        }
        for position, index in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 12], 1)
    ]
    _write_publish_log(
        tmp_path,
        "2026-07-20",
        audience_scope="subscribers",
        card_delivery_succeeded=True,
        card_exposure_schema_version=1,
        card_max_items_per_section=10,
        card_items=manifest,
    )

    history = collect_history(tmp_path, date(2026, 7, 28))
    by_id = {row["candidate_id"]: row for row in history["occurrences"]}

    assert by_id["I010"]["card_exposed"] is False
    assert by_id["I012"]["card_exposed"] is True
    assert by_id["I012"]["card_rank"] == 10
    assert by_id["I012"]["card_exposure_source"] == "publish_log_manifest"


def test_card_carryover_requires_hidden_prior_card_and_audit_flag() -> None:
    valid = {
        "decision": "include",
        "card_carryover": True,
        "history_check": {
            "history_match": True,
            "novelty": "card_carryover",
            "prior_occurrences": ["2026-07-20 周报"],
            "new_facts": [],
            "prior_card_exposed": False,
        },
    }
    assert validate_industry_history_check(valid, "I001", True) == []

    exposed = json.loads(json.dumps(valid, ensure_ascii=False))
    exposed["history_check"]["prior_card_exposed"] = True
    assert any(
        "prior_card_exposed=false" in error
        for error in validate_industry_history_check(exposed, "I002", True)
    )

    missing_flag = json.loads(json.dumps(valid, ensure_ascii=False))
    missing_flag.pop("card_carryover")
    assert any(
        "card_carryover=true" in error
        for error in validate_industry_history_check(missing_flag, "I003", True)
    )
