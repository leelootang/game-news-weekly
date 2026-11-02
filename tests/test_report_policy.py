from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import report_policy as POLICY


class SubjectGenrePolicyTests(unittest.TestCase):
    def setUp(self):
        self.report = Path("game_industry_daily_2026-10-21.md")
        self.inputs = {"S0001": {"text": "库洛投资的新工作室公布竞技射击产品收入。"}}
        self.decision = {
            "candidate_id": "C1", "section": "industry", "source_ids": ["S0001"],
            "decision": "include", "scores": {"event": 2, "relevance": 2, "hook": 1, "total": 5},
            "subject_assessment": {
                "subject": "新工作室", "kind": "focus_affiliate", "focus_companies": ["库洛"],
                "basis": "来源证明投资关系", "evidence": [{"source_id": "S0001", "evidence": "库洛投资的新工作室"}],
            },
            "genre_assessment": {
                "matched_genres": ["competitive"], "basis": "明确竞技射击",
                "evidence": [{"source_id": "S0001", "evidence": "竞技射击产品"}],
            },
        }

    def errors(self, decision=None, report=None, version=POLICY.SCORING_VERSION):
        return POLICY.validate_scoring_document(
            {"scoring_version": version, "decisions": [decision or self.decision]}, self.inputs, report or self.report
        )

    def test_five_point_boundary_all_report_types(self):
        for name in ["daily_2026-10-21", "weekly_2026-10-16_to_2026-10-22", "weekend_2026-10-23_to_2026-10-25", "monthly_2026-10"]:
            with self.subTest(name=name):
                self.assertEqual([], self.errors(report=Path(f"game_industry_{name}.md")))
        d = copy.deepcopy(self.decision)
        d["scores"].update(hook=0, total=4)
        d["genre_assessment"].update(matched_genres=[], evidence=[], basis="无重点品类")
        self.assertTrue(any("required >= 5" in x for x in self.errors(d)))

    def test_macro_without_genre_and_e0_veto(self):
        d = copy.deepcopy(self.decision)
        d["scores"].update(event=2, relevance=3, hook=0, total=6)
        d["subject_assessment"].update(subject="中国移动游戏市场", kind="priority_mobile_market", focus_companies=[])
        d["genre_assessment"].update(matched_genres=[], evidence=[], basis="宏观市场没有具体品类")
        self.assertEqual([], self.errors(d))
        d["scores"].update(event=0, total=0)
        self.assertTrue(any("threshold" in x for x in self.errors(d)))

    def test_m_two_and_coerced_types_are_rejected(self):
        for value in (2, True, "1", 1.0):
            d = copy.deepcopy(self.decision)
            d["scores"]["hook"] = value
            self.assertTrue(self.errors(d))

    def test_genre_bonus_requires_exact_source_quote_and_allowed_genre(self):
        d = copy.deepcopy(self.decision)
        d["genre_assessment"]["evidence"][0]["evidence"] = "MOBA"
        self.assertTrue(any("evidence not found" in x for x in self.errors(d)))
        d["genre_assessment"].update(matched_genres=["roguelike"])
        self.assertTrue(any("invalid matched_genres" in x for x in self.errors(d)))

    def test_parent_mention_does_not_promote_affiliate(self):
        self.assertEqual([], self.errors())
        d = copy.deepcopy(self.decision)
        d["subject_assessment"]["subject"] = "库洛"
        self.assertTrue(any("listed focus subject" in x for x in self.errors(d)))

    def test_unknown_subject_cannot_claim_r3(self):
        d = copy.deepcopy(self.decision)
        d["scores"].update(relevance=3, total=7)
        d["subject_assessment"].update(kind="other_or_unknown", focus_companies=[])
        self.assertTrue(any("does not match R" in x for x in self.errors(d)))

    def test_unlisted_subject_can_receive_equivalent_r3_or_r2(self):
        for tier, kind in [(3, "comparable_major_subject"), (2, "comparable_significant_subject")]:
            with self.subTest(tier=tier):
                d = copy.deepcopy(self.decision)
                self.inputs["S0001"]["text"] = "星海工作室拥有面向全球的游戏用户与发行网络，公布竞技射击产品。"
                d["scores"].update(relevance=tier, total=2*tier+1)
                d["subject_assessment"].update(subject="星海工作室", kind=kind, focus_companies=[],
                    basis="结合其用户覆盖与发行影响力，判断与该档主体相当，不以名单内外决定分数。",
                    evidence=[{"source_id":"S0001", "evidence":"星海工作室拥有面向全球的游戏用户与发行网络"}])
                self.assertEqual([], self.errors(d))

    def test_comparable_influence_still_needs_real_source_evidence(self):
        d = copy.deepcopy(self.decision)
        d["scores"].update(relevance=3, total=7)
        d["subject_assessment"].update(subject="新公司", kind="comparable_major_subject", focus_companies=[], evidence=[])
        self.assertTrue(any("needs source evidence" in x for x in self.errors(d)))
        d["subject_assessment"]["evidence"] = [{"source_id":"S0001", "evidence":"全球最大游戏集团"}]
        self.assertTrue(any("evidence not found" in x for x in self.errors(d)))

    def test_comparable_kind_must_match_actual_r(self):
        d = copy.deepcopy(self.decision)
        d["subject_assessment"].update(subject="新工作室", kind="comparable_major_subject", focus_companies=[])
        self.assertTrue(any("does not match R" in x for x in self.errors(d)))

    def test_policy_version_cannot_be_downgraded_after_cutover(self):
        self.assertTrue(any("scoring_version" in x for x in self.errors(version="legacy")))
        legacy = Path("game_industry_daily_2026-10-20.md")
        self.assertEqual([], POLICY.validate_scoring_document({"decisions": []}, {}, legacy))
        self.assertTrue(self.errors(report=legacy, version=POLICY.SCORING_VERSION) == [])

    def test_bundled_skill_policy_copies_agree(self):
        skill = ROOT / "skills/game-industry-report"
        self.assertEqual((ROOT / "scripts/report_policy.py").read_text(encoding="utf-8"), (skill / "scripts/report_policy.py").read_text(encoding="utf-8"))
        self.assertEqual(POLICY.POLICY, json.loads((skill / "references/report-policy.json").read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
