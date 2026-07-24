from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from feishu_common import _attach_industry_scores, build_daily_card  # noqa: E402


class FeishuCardEmphasisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.summary = {
            "title": "测试周报",
            "date": "2026-07-17_to_2026-07-23",
            "noun": "周报",
            "kind": "weekly",
            "sections": [
                {
                    "name": "行业新闻",
                    "items": [
                        {
                            "kind": "heading",
                            "title": "行业标题，后半句",
                            "body": "主体公布进展。\n产品计划7月上线。",
                            "score_total": 11,
                        },
                        {
                            "kind": "heading",
                            "title": "第二条标题",
                            "body": "",
                            "score_total": 10,
                        },
                        {
                            "kind": "heading",
                            "title": "第三条标题，后半句",
                            "body": "",
                            "score_total": 11,
                        },
                        {"kind": "heading", "title": "第四条标题，后半句", "body": ""},
                    ],
                },
                {
                    "name": "AI 新闻",
                    "items": [{"kind": "heading", "title": "AI标题", "body": ""}],
                },
                {
                    "name": "新游发布 / 产品日历",
                    "items": [
                        {
                            "kind": "bullet",
                            "title": "甲公司开发的RPG《游戏甲》于7月1日正式上线；覆盖移动端。",
                            "body": "",
                        },
                        {
                            "kind": "bullet",
                            "title": "乙公司开发的开放世界游戏《游戏乙》于7月2日开启限量删档测试；覆盖PC。",
                            "body": "",
                        },
                        {
                            "kind": "bullet",
                            "title": "卡牌游戏《游戏丙》于7月3日正式上线。",
                            "body": "",
                        },
                    ],
                },
                {
                    "name": "玩家舆论 / 社区动态",
                    "items": [
                        {
                            "kind": "heading",
                            "title": "玩家争议标题",
                            "body": "玩家围绕更新方案展开讨论。",
                        }
                    ],
                },
            ],
        }

    def markdown_blocks(self) -> list[str]:
        card = build_daily_card(self.summary, doc_url="https://example.com/report", per_section=10)
        return [
            element["content"]
            for element in card["body"]["elements"]
            if element.get("tag") == "markdown" and "content" in element
        ]

    def test_section_specific_emphasis_rules(self) -> None:
        text = "\n".join(self.markdown_blocks())
        self.assertIn("• **行业标题**，后半句；产品计划7月上线", text)
        self.assertIn("• 第二条标题", text)
        self.assertNotIn("**第二条标题**", text)
        self.assertIn("• **第三条标题**，后半句", text)
        self.assertIn("• 第四条标题，后半句", text)
        self.assertNotIn("**第四条标题", text)
        self.assertIn("• AI标题", text)
        self.assertNotIn("**AI标题**", text)
        self.assertIn("• **甲公司开发的RPG《游戏甲》7月1日正式上线**", text)
        self.assertIn(
            "• **乙公司开发的开放世界游戏《游戏乙》7月2日开启限量删档测试**",
            text,
        )
        self.assertIn("• 卡牌游戏《游戏丙》7月3日正式上线", text)
        self.assertNotIn("**《游戏丙》", text)
        self.assertIn("• **玩家争议标题**\n  玩家围绕更新方案展开讨论", text)

    def test_bold_markers_are_balanced_without_nested_or_orphan_markers(self) -> None:
        for block in self.markdown_blocks():
            for line in block.splitlines():
                if "**" not in line:
                    continue
                self.assertEqual(0, line.count("**") % 2, line)
                self.assertNotIn("***", line)

    def test_industry_and_product_items_have_no_continuation_lines(self) -> None:
        blocks = self.markdown_blocks()
        compact_blocks = [
            block
            for block in blocks
            if block.startswith("**📰 行业新闻**") or block.startswith("**🎮 新游 / 产品**")
        ]
        self.assertEqual(2, len(compact_blocks))
        for block in compact_blocks:
            self.assertFalse(any(line.startswith("  ") for line in block.splitlines()), block)
            for line in block.splitlines()[1:]:
                self.assertTrue(line.startswith("• "), line)

    def test_product_bold_limit_applies_to_daily_weekend_and_weekly(self) -> None:
        dates = {
            "daily": "2026-07-23",
            "weekend": "2026-07-17_to_2026-07-19",
            "weekly": "2026-07-17_to_2026-07-23",
        }
        for kind, report_date in dates.items():
            with self.subTest(kind=kind):
                self.summary["kind"] = kind
                self.summary["date"] = report_date
                text = "\n".join(self.markdown_blocks())
                product_block = next(
                    block
                    for block in self.markdown_blocks()
                    if block.startswith("**🎮 新游 / 产品**")
                )
                product_lines = product_block.splitlines()[1:]
                self.assertTrue(product_lines[0].startswith("• **"))
                self.assertTrue(product_lines[0].endswith("**"))
                self.assertTrue(product_lines[1].startswith("• **"))
                self.assertTrue(product_lines[1].endswith("**"))
                self.assertFalse(product_lines[2].startswith("• **"))
                self.assertNotIn("》于", text)

    def test_industry_scores_are_loaded_from_audit_artifacts_by_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report_dir = Path(temp_dir)
            intermediate = report_dir / "_intermediate"
            intermediate.mkdir()
            (intermediate / "report_items.json").write_text(
                json.dumps(
                    {
                        "items": [
                            {
                                "section": "industry",
                                "candidate_id": "C001",
                                "title": "十一分标题，后半句",
                            },
                            {
                                "section": "industry",
                                "candidate_id": "C002",
                                "title": "十分标题",
                            },
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (intermediate / "selection_decisions.json").write_text(
                json.dumps(
                    {
                        "decisions": [
                            {
                                "section": "industry",
                                "candidate_id": "C001",
                                "scores": {"total": 11},
                            },
                            {
                                "section": "industry",
                                "candidate_id": "C002",
                                "scores": {"total": 10},
                            },
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            sections = [
                {
                    "name": "行业新闻",
                    "items": [
                        {"title": "十一分标题，后半句"},
                        {"title": "十分标题"},
                        {"title": "无审计标题"},
                    ],
                }
            ]

            _attach_industry_scores(sections, report_dir)

            self.assertEqual(11, sections[0]["items"][0]["score_total"])
            self.assertEqual(10, sections[0]["items"][1]["score_total"])
            self.assertNotIn("score_total", sections[0]["items"][2])


if __name__ == "__main__":
    unittest.main()
