from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(r"C:\Users\Admin\.codex\skills\game-industry-report\scripts\extract_report_inputs.py")
SPEC = importlib.util.spec_from_file_location("extract_report_inputs_contract", SCRIPT)
assert SPEC and SPEC.loader
EXTRACT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = EXTRACT
SPEC.loader.exec_module(EXTRACT)


def release_record(
    source_id: str,
    product: str,
    event: str,
    section: str = "release_calendar",
    company: str = "",
) -> dict:
    return {
        "source_id": source_id,
        "section": section,
        "date": "2026-07-20",
        "title": f"{product} - {event}" if section == "release_calendar" else f"《{product}》{event}",
        "text": (
            f"Game: {product}\nEvent date: 2026-07-20\nEvent type: {event}"
            f"\nPublisher: {company}"
        ),
    }


class ReleaseCalendarScoringTests(unittest.TestCase):
    def test_same_product_date_merges_test_labels(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "航海奇兵", "计费删档内测"),
            release_record("S0002", "航海奇兵", "删档测试"),
            release_record("S0003", "航海奇兵", "不限量测试"),
        ])
        self.assertEqual(1, len(rows))
        self.assertEqual(3, rows[0]["appearance_count"])
        self.assertEqual(3, rows[0]["event_type_score"])
        self.assertEqual(3, rows[0]["source_strength_score"])
        self.assertEqual(9, rows[0]["priority_score"])

    def test_industry_coverage_adds_one_to_source_strength(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "新品A", "首发"),
            release_record("S0002", "新品A", "正式上线", "industry_news"),
        ])
        self.assertEqual(2, rows[0]["appearance_count"])
        self.assertEqual(1, rows[0]["industry_bonus"])
        self.assertEqual(3, rows[0]["source_strength_score"])
        self.assertEqual(9, rows[0]["priority_score"])

    def test_event_types_receive_three_two_one(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "测试新品", "首测"),
            release_record("S0002", "曝光新品", "首曝"),
            release_record("S0003", "回归老品", "重启回归"),
        ])
        scores = {row["product"]: row["event_type_score"] for row in rows}
        self.assertEqual({"测试新品": 3, "曝光新品": 2, "回归老品": 1}, scores)

    def test_ties_use_event_then_count_then_industry_then_first_seen(self) -> None:
        records = [
            release_record("S0001", "先出现", "首发"),
            release_record("S0002", "先出现", "正式上线"),
            release_record("S0003", "后出现", "首发"),
            release_record("S0004", "后出现", "正式上线"),
        ]
        rows = EXTRACT.build_release_candidates(records)
        self.assertEqual(["先出现", "后出现"], [row["product"] for row in rows])

    def test_routine_followup_promotion_is_not_recalled(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "宣传新品", "第二支PV公开"),
        ])
        self.assertEqual([], rows)

    def test_focus_company_adds_three_without_bypassing_multi_source_gate(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "网易新品", "正式上线", company="网易游戏"),
        ])
        self.assertEqual(3, rows[0]["company_bonus"])
        self.assertEqual(6, rows[0]["priority_score"])
        self.assertFalse(rows[0]["multi_source_eligible"])
        self.assertEqual(["网易"], rows[0]["focus_companies"])

    def test_focus_company_bonus_reorders_eligible_candidates(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "普通新品", "正式上线"),
            release_record("S0002", "普通新品", "正式上线"),
            release_record("S0003", "重点新品", "正式上线", company="腾讯游戏"),
            release_record("S0004", "重点新品", "正式上线", company="腾讯游戏"),
        ])
        self.assertEqual(["重点新品", "普通新品"], [row["product"] for row in rows])
        self.assertEqual([9, 6], [row["priority_score"] for row in rows])

    def test_duplicate_hash_counts_as_one_independent_source(self) -> None:
        first = release_record("S0001", "重复新品", "正式上线")
        second = release_record("S0002", "重复新品", "正式上线")
        first["sha1"] = second["sha1"] = "same-body"
        rows = EXTRACT.build_release_candidates([first, second])
        self.assertEqual(1, rows[0]["appearance_count"])
        self.assertFalse(rows[0]["multi_source_eligible"])

    def test_marketing_suffixes_normalize_to_one_product(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "王者万象棋-正版王者英雄自走棋", "正式上线"),
            release_record("S0002", "王者万象棋 招募中", "正式上线"),
        ])
        self.assertEqual(1, len(rows))
        self.assertEqual("王者万象棋", rows[0]["product"])

    def test_industry_lead_can_supply_product_and_beta_signal(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-07-20",
            "title": "格斗新品开启公开B测",
            "text": "7月20日，多平台格斗游戏《漫威斗魂》开启公开B测，可在PC及PS平台下载。",
        }
        rows = EXTRACT.build_release_candidates([record])
        self.assertEqual("漫威斗魂", rows[0]["product"])
        self.assertEqual("new_game_test", rows[0]["signal_type"])

    def test_early_access_is_classified_as_test_not_launch(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "王者万象棋", "抢先体验测试", company="腾讯游戏"),
            release_record("S0002", "王者万象棋", "长期抢先体验测试", company="天美工作室群"),
        ])
        self.assertEqual("new_game_test", rows[0]["signal_type"])
        self.assertEqual("抢先体验测试", rows[0]["event"])
        self.assertEqual(3, rows[0]["company_bonus"])

    def test_early_access_beats_generic_store_open_label(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "王者万象棋", "抢先体验测试", "industry_news", company="腾讯游戏"),
            release_record("S0002", "王者万象棋", "体验服已开服"),
        ])
        self.assertEqual("new_game_test", rows[0]["signal_type"])
        self.assertEqual("抢先体验测试", rows[0]["event"])

    def test_out_of_window_launch_is_audited_but_not_publish_eligible(self) -> None:
        records = [
            release_record("S0001", "窗口外新品", "正式上线"),
            release_record("S0002", "窗口外新品", "正式上线"),
        ]
        rows = EXTRACT.build_release_candidates(
            records,
            window_start="2026-07-21",
            window_end="2026-07-27",
        )
        self.assertFalse(rows[0]["window_eligible"])
        self.assertFalse(rows[0]["publish_eligible"])


if __name__ == "__main__":
    unittest.main()
