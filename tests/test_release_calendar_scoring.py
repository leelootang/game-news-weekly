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


def release_record(source_id: str, product: str, event: str, section: str = "release_calendar") -> dict:
    return {
        "source_id": source_id,
        "section": section,
        "date": "2026-07-20",
        "title": f"{product} - {event}" if section == "release_calendar" else f"《{product}》{event}",
        "text": f"Game: {product}\nEvent date: 2026-07-20\nEvent type: {event}",
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


if __name__ == "__main__":
    unittest.main()
