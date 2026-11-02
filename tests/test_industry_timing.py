import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import industry_timing as timing


class IndustryTimingTests(unittest.TestCase):
    def setUp(self):
        self.inputs = {"S1": {"date": "2026-10-27", "published_at": "2026-10-27T01:00:00Z"}}
        self.report = Path("game_industry_daily_2026-10-27.md")
        self.row = {"candidate_id": "GDC", "section": "industry", "source_ids": ["S1"],
                    "scores": {"event": 2, "relevance": 3, "hook": 0, "total": 6},
                    "decision": "include", "history_check": {"history_match": False, "prior_card_exposed": None}}
        self.refresh()

    def refresh(self):
        start, end = timing.report_window(self.report)
        self.row["time_check"] = timing.build_time_check(["S1"], self.inputs, start, end,
            event_date="2026-03-12", basis="当期发布的GDC复盘；事件日期仅用于陈述历史。")

    def errors(self):
        return timing.validate_timing_document({"industry_timing_version": timing.TIMING_VERSION,
            "decisions": [self.row]}, self.inputs, self.report)

    def test_old_unseen_event_is_eligible_in_all_report_types(self):
        for name in ["daily_2026-10-27", "weekly_2026-10-23_to_2026-10-29",
                     "weekend_2026-10-25_to_2026-10-27", "monthly_2026-10"]:
            self.report = Path(f"game_industry_{name}.md")
            self.refresh()
            self.assertEqual([], self.errors())

    def test_old_source_cannot_use_collection_date_to_pass(self):
        self.inputs["S1"]["published_at"] = "2026-03-12"
        self.refresh()
        self.assertTrue(any("current-window source" in x for x in self.errors()))

    def test_missing_publication_uses_audited_input_date(self):
        self.inputs["S1"].pop("published_at")
        self.refresh()
        self.assertEqual("input_date", self.row["time_check"]["sources"][0]["date_field"])
        self.assertEqual([], self.errors())

    def test_aware_timestamp_is_converted_to_shanghai(self):
        self.assertEqual(("2026-10-27", "published_at"), timing.source_window_date({"published_at": "2026-10-26T18:00:00Z"}))

    def test_date_only_exclusion_is_rejected(self):
        self.row.update(decision="exclude", exclusion_gates=["event_window"])
        self.assertTrue(self.errors())
        self.row["exclusion_gates"] = ["source_window"]
        self.assertTrue(self.errors())
        self.row["exclusion_gates"] = ["source_quality"]
        self.assertEqual([], self.errors())

    def test_previously_exposed_is_not_resurrected(self):
        self.row["history_check"].update(history_match=True, prior_card_exposed=True, novelty="new_event")
        self.assertTrue(self.errors())
        self.row["history_check"]["novelty"] = "material_update"
        self.assertEqual([], self.errors())

    def test_exclusion_gates_cannot_contradict_audit(self):
        self.row["decision"] = "exclude"
        for gate in ["score", "history_repeat"]:
            self.row["exclusion_gates"] = [gate]
            self.assertTrue(self.errors())

    def test_forged_source_date_and_event_gate_are_rejected(self):
        self.row["time_check"]["sources"][0]["date"] = "2026-10-26"
        self.assertTrue(self.errors())
        self.refresh()
        self.row["time_check"]["event_date_is_gate"] = True
        self.assertTrue(self.errors())

    def test_weekly_rollup_allows_only_daily_events_inside_own_window(self):
        self.report = Path("game_industry_weekly_2026-10-23_to_2026-10-29.md")
        self.refresh()
        self.row["history_check"].update(history_match=True, prior_card_exposed=True,
            novelty="new_event", prior_occurrences=["2026-10-26 日报：GDC复盘"])
        self.assertEqual([], self.errors())
        self.row["history_check"]["prior_occurrences"] = ["2026-10-23_to_2026-10-29 周报：GDC复盘"]
        self.assertTrue(self.errors())
        self.row["history_check"]["prior_occurrences"] = ["2026-10-20 日报：GDC复盘"]
        self.assertTrue(self.errors())

    def test_cutover_and_explicit_regeneration(self):
        old = Path("game_industry_daily_2026-10-26.md")
        self.assertEqual([], timing.validate_timing_document({}, {}, old))
        self.assertTrue(timing.validate_timing_document({}, {}, self.report))
        self.assertTrue(timing.validate_timing_document({"industry_timing_version": "legacy"}, {}, old))

    def test_calendar_is_not_subject_to_industry_timing(self):
        self.row["section"] = "release_calendar"
        self.row.pop("time_check")
        self.assertEqual([], self.errors())

    def test_bundled_timing_copy_agrees(self):
        installed = ROOT / "skills/game-industry-report/scripts/industry_timing.py"
        self.assertEqual((ROOT / "scripts/industry_timing.py").read_bytes(), installed.read_bytes())


if __name__ == "__main__":
    unittest.main()
