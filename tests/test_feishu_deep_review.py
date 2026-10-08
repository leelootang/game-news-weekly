from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from feishu_deep_review import parse_candidate_markdown, parse_choice_reply  # noqa: E402


class FeishuDeepReviewTests(unittest.TestCase):
    def test_parses_candidate_markdown(self) -> None:
        payload = parse_candidate_markdown(
            """# 候选\n- 候选数据窗口: 2026-09-17_to_2026-09-23\n- 目标周报窗口: 2026-09-18_to_2026-09-24\n\n### C001. 题目一\n- 评分: R3 / I3 / E3 / C3，总分12\n\n### C002. 题目二\n观察：内容\n"""
        )
        self.assertEqual(payload["target_weekly_id"], "2026-09-18_to_2026-09-24")
        self.assertEqual([row["candidate_id"] for row in payload["candidates"]], ["C001", "C002"])

    def test_parses_natural_merge_reply_in_either_order(self) -> None:
        parsed = parse_choice_reply(
            "卡片：把c005，c006，c014的信息整合成wardogs复盘\n正文：c005，c001"
        )
        self.assertEqual(parsed["body_candidate_ids"], ["C005", "C001"])
        self.assertEqual(parsed["card_base_candidate_id"], "C005")
        self.assertEqual(parsed["card_reference_candidate_ids"], ["C006", "C014"])

    def test_card_base_must_be_in_body(self) -> None:
        with self.assertRaisesRegex(ValueError, "必须同时出现在正文"):
            parse_choice_reply("正文：C001；卡片：C005")


if __name__ == "__main__":
    unittest.main()
