from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from feishu_common import (  # noqa: E402
    CARD_ITEMS_PER_SECTION,
    _attach_industry_scores,
    _parse_markdown_sections,
    _validate_card_report_artifacts,
    build_daily_card,
    build_deep_observation_card,
    card_item_manifest,
)


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
                    "items": [
                        {
                            "kind": "heading",
                            "title": "AI标题",
                            "body": "主体宣布AI工具进入游戏流程。该工具计划8月用于自动化测试。",
                        }
                    ],
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

    def test_card_report_preflight_blocks_contract_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report_dir = Path(temp_dir)
            intermediate = report_dir / "_intermediate"
            intermediate.mkdir()
            (intermediate / "report_items.json").write_text("{}", encoding="utf-8")
            markdown = report_dir / "report.md"
            markdown.write_text("# 报告\n", encoding="utf-8")
            import report_artifacts

            original = report_artifacts.validate_contract
            report_artifacts.validate_contract = lambda *args, **kwargs: (["排序漂移"], [])
            try:
                with self.assertRaisesRegex(ValueError, "card report preflight failed"):
                    _validate_card_report_artifacts(report_dir, markdown)
            finally:
                report_artifacts.validate_contract = original

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
        self.assertIn("• AI标题；该工具计划8月用于自动化测试", text)
        self.assertNotIn("**AI标题**", text)
        self.assertIn("• **甲公司开发的RPG《游戏甲》7月1日正式上线**", text)
        self.assertIn(
            "• **乙公司开发的开放世界游戏《游戏乙》7月2日开启限量删档测试**",
            text,
        )
        self.assertIn("• 卡牌游戏《游戏丙》7月3日正式上线", text)
        self.assertNotIn("**《游戏丙》", text)
        self.assertIn("• **玩家争议标题**\n  玩家围绕更新方案展开讨论", text)

    def test_player_discourse_card_cap_depends_on_report_kind(self) -> None:
        discourse = next(
            section for section in self.summary["sections"]
            if "舆论" in section["name"]
        )
        discourse["items"] = [
            {
                "kind": "heading",
                "candidate_id": f"C{index:03d}",
                "title": f"玩家争议标题{index}",
                "body": f"8月{index}日玩家围绕更新方案展开讨论。",
            }
            for index in range(1, 6)
        ]
        expected = {"daily": 2, "weekend": 2, "weekly": 3}
        for kind, cap in expected.items():
            with self.subTest(kind=kind):
                self.summary["kind"] = kind
                block = next(
                    item
                    for item in self.markdown_blocks()
                    if item.startswith("**💬 玩家舆论**")
                )
                self.assertEqual(cap, sum(line.startswith("• ") for line in block.splitlines()))
                manifest = [
                    row for row in card_item_manifest(self.summary)
                    if row["section"] == "玩家舆论"
                ]
                self.assertEqual(cap, len(manifest))

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
                                "card_carryover": True,
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
            self.assertEqual("C001", sections[0]["items"][0]["candidate_id"])
            self.assertTrue(sections[0]["items"][0]["card_carryover"])
            self.assertEqual(10, sections[0]["items"][1]["score_total"])
            self.assertNotIn("score_total", sections[0]["items"][2])

    def test_card_carryover_replaces_last_industry_item_and_is_logged(self) -> None:
        items = [
            {
                "kind": "heading",
                "candidate_id": f"I{index:03d}",
                "title": f"行业标题{index:02d}",
                "body": "",
                "card_carryover": index == 12,
            }
            for index in range(1, 13)
        ]
        summary = {
            "title": "测试周报",
            "date": "2026-08-01_to_2026-08-07",
            "noun": "周报",
            "kind": "weekly",
            "sections": [{"name": "行业新闻", "items": items}],
        }

        card = build_daily_card(summary)
        block = next(
            element["content"]
            for element in card["body"]["elements"]
            if element.get("tag") == "markdown" and element["content"].startswith("**📰 行业新闻**")
        )
        self.assertEqual(CARD_ITEMS_PER_SECTION, len(block.splitlines()) - 1)
        self.assertIn("行业标题09", block)
        self.assertNotIn("行业标题10", block)
        self.assertNotIn("行业标题11", block)
        self.assertIn("• 行业标题12", block)
        self.assertNotIn("上期卡片未展示", block)
        self.assertNotIn("补位", block)

        manifest = [row for row in card_item_manifest(summary) if row["section"] == "industry"]
        self.assertEqual(10, len(manifest))
        self.assertEqual("I012", manifest[-1]["candidate_id"])
        self.assertEqual(10, manifest[-1]["position"])
        self.assertTrue(manifest[-1]["card_carryover"])

    def test_card_blocks_internal_carryover_labels_from_visible_copy(self) -> None:
        self.summary["sections"][0]["items"][0]["title"] = "【补位】行业标题"
        with self.assertRaisesRegex(ValueError, "pipeline/source metadata"):
            build_daily_card(self.summary)

    def test_card_blocks_source_and_pipeline_metadata(self) -> None:
        self.summary["sections"][0]["items"][0]["body"] = "【GameLook专稿，禁止转载！】原文片段"
        with self.assertRaisesRegex(ValueError, "pipeline/source metadata"):
            build_daily_card(self.summary)

    def test_deep_card_preserves_paragraphs_and_uses_schema_two(self) -> None:
        markdown = """# 周报

## 五、行业精选 / 深度观察

### 1. 深度标题

观察：这是观察。

分析：这是第一段分析。

这是第二段分析。
"""
        sections = _parse_markdown_sections(markdown)
        summary = {
            "title": "测试周报",
            "date": "2026-07-17_to_2026-07-23",
            "noun": "周报",
            "sections": sections,
        }
        card = build_deep_observation_card(
            summary,
            doc_url="https://example.com/report",
            source_url="https://example.com/source",
        )
        self.assertIsNotNone(card)
        assert card is not None
        self.assertEqual("2.0", card["schema"])
        self.assertEqual("fill", card["config"]["width_mode"])
        content = card["body"]["elements"][0]["content"]
        self.assertIn("**观察：**这是观察。\n\n**分析：**这是第一段分析。\n\n这是第二段分析。", content)
        buttons = next(
            element for element in card["body"]["elements"]
            if element.get("tag") == "column_set"
        )
        self.assertTrue(
            all(
                column["elements"][0]["behaviors"][0]["type"] == "open_url"
                for column in buttons["columns"]
            )
        )

    def test_deep_card_rejects_prefixed_source_excerpt(self) -> None:
        summary = {
            "title": "测试周报",
            "date": "2026-07-17_to_2026-07-23",
            "noun": "周报",
            "sections": [
                {
                    "name": "深度观察",
                    "items": [
                        {
                            "title": "深度标题",
                            "body": "Backrooms | Source: A24\n\n观察：事实。\n\n分析：第一段。\n\n第二段。",
                        }
                    ],
                }
            ],
        }
        with self.assertRaises(ValueError):
            build_deep_observation_card(summary)


if __name__ == "__main__":
    unittest.main()
