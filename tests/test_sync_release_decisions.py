from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sync_release_decisions_test", ROOT / "scripts/sync_release_decisions.py")
assert SPEC and SPEC.loader
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class ReleaseIndependentSelectionTests(unittest.TestCase):
    def test_sync_preserves_scoring_version_and_report_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            audit, decisions = root / "audit.json", root / "decisions.json"
            audit.write_text(json.dumps({"nodes": []}), encoding="utf-8")
            original = {"scoring_version": "subject_genre_v2", "industry_timing_version": "source_window_v1", "report_window": {"end": "2026-10-21"}, "decisions": []}
            decisions.write_text(json.dumps(original), encoding="utf-8")
            SYNC.sync(audit, decisions, 4)
            self.assertEqual(original, json.loads(decisions.read_text(encoding="utf-8")))

    def run_sync(self, industry_decision, nodes, cap=4):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            audit, decisions = root / "audit.json", root / "decisions.json"
            audit.write_text(json.dumps({"nodes": nodes}), encoding="utf-8")
            decisions.write_text(json.dumps({"decisions": [industry_decision]}), encoding="utf-8")
            SYNC.sync(audit, decisions, cap)
            return json.loads(decisions.read_text(encoding="utf-8"))["decisions"]

    def node(self, cid="R1", eligible=True, count=2):
        return {"candidate_id": cid, "product": "同一游戏", "event_date": "2026-10-15", "event": "正式上线",
                "source_ids": ["S0001", "S0002"][:count], "event_type_score": 3,
                "source_strength_score": count+1, "priority_score": 3*(count+1),
                "appearance_count": count, "window_eligible": eligible, "publish_eligible": eligible and count>=2}

    def test_industry_include_or_exclude_does_not_change_calendar_eligibility(self):
        for status in ("include", "exclude"):
            with self.subTest(status=status):
                original = {"candidate_id": "I1", "section": "industry_news", "source_ids": ["S0001", "S0002"],
                            "event": "同一游戏正式上线", "decision": status}
                result = self.run_sync(original, [self.node()])
                self.assertEqual(original, result[0])
                self.assertEqual("include", result[1]["decision"])
                self.assertTrue(result[1]["industry_overlap_allowed"])

    def test_single_source_and_outside_window_stay_excluded(self):
        nodes = [self.node("R1", count=1), self.node("R2", eligible=False)]
        result = self.run_sync({"candidate_id": "I1", "section": "industry", "decision": "include"}, nodes)
        self.assertEqual(["exclude", "exclude"], [x["decision"] for x in result[1:]])

    def test_calendar_keeps_ranked_prefix_and_cap(self):
        nodes = [self.node("R1"), self.node("R2"), self.node("R3")]
        result = self.run_sync({"candidate_id": "I1", "section": "industry", "decision": "include"}, nodes, cap=2)
        self.assertEqual(["R1", "R2"], [x["candidate_id"] for x in result[1:] if x["decision"] == "include"])


if __name__ == "__main__":
    unittest.main()
