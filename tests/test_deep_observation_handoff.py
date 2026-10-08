from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "deep_observation_handoff", ROOT / "scripts" / "deep_observation_handoff.py"
)
assert SPEC and SPEC.loader
HANDOFF = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HANDOFF)


class DeepObservationHandoffTests(unittest.TestCase):
    def test_thursday_candidate_window_and_target_report_window_are_distinct(self) -> None:
        candidate, target = HANDOFF.selection_windows(date(2026, 7, 23))
        self.assertEqual("2026-07-16_to_2026-07-22", candidate)
        self.assertEqual("2026-07-17_to_2026-07-23", target)

    def test_complete_handoff_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report_dir = root / "output" / "weekly" / "2026-07-17_to_2026-07-23"
            review_dir = root / "output" / "deep_observation_review"
            report_dir.mkdir(parents=True)
            review_dir.mkdir(parents=True)
            report = report_dir / "game_industry_weekly_2026-07-17_to_2026-07-23.md"
            report.write_text(
                "# 周报\n\n## 五、行业精选 / 深度观察\n\n### 1. 主题甲\n\n观察：变化。\n\n分析：机制。\n",
                encoding="utf-8",
            )
            (review_dir / "2026-07-17_to_2026-07-23_selection.md").write_text(
                """# 深度观察人工选择

- 候选数据窗口: 2026-07-16_to_2026-07-22
- 目标周报窗口: 2026-07-17_to_2026-07-23

## 用户选择进入周报的条目

### 1. ★卡片:主题甲

观察：变化。

分析：机制。

## 未选候选
""",
                encoding="utf-8",
            )
            (report_dir / "deep_card_choice.txt").write_text("主题甲\n", encoding="utf-8")
            self.assertEqual([], HANDOFF.validate_weekly_handoff(report))

    def test_missing_choice_is_blocking_when_selection_designates_card(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report_dir = root / "output" / "weekly" / "2026-07-17_to_2026-07-23"
            review_dir = root / "output" / "deep_observation_review"
            report_dir.mkdir(parents=True)
            review_dir.mkdir(parents=True)
            report = report_dir / "game_industry_weekly_2026-07-17_to_2026-07-23.md"
            report.write_text(
                "# 周报\n\n## 五、深度观察\n\n### 1. 主题甲\n\n观察：变化。\n\n分析：机制。\n",
                encoding="utf-8",
            )
            (review_dir / "2026-07-17_to_2026-07-23_selection.md").write_text(
                """# 深度观察人工选择

- 候选数据窗口: 2026-07-16_to_2026-07-22
- 目标周报窗口: 2026-07-17_to_2026-07-23

## 用户选择进入周报的条目

### 1. ★卡片:主题甲
""",
                encoding="utf-8",
            )
            errors = HANDOFF.validate_weekly_handoff(report)
            self.assertTrue(any("deep_card_choice.txt missing" in error for error in errors))

    def test_legacy_candidate_window_filename_is_not_silently_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report_dir = root / "output" / "weekly" / "2026-07-17_to_2026-07-23"
            review_dir = root / "output" / "deep_observation_review"
            report_dir.mkdir(parents=True)
            review_dir.mkdir(parents=True)
            report = report_dir / "game_industry_weekly_2026-07-17_to_2026-07-23.md"
            report.write_text("# 周报\n", encoding="utf-8")
            (review_dir / "2026-07-16_to_2026-07-22_selection.md").write_text(
                "# legacy selection\n", encoding="utf-8"
            )
            errors = HANDOFF.validate_weekly_handoff(report)
            self.assertTrue(any("legacy candidate-window selection" in error for error in errors))

    def test_weekend_report_does_not_require_weekly_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report_dir = root / "output" / "weekend" / "2026-07-24_to_2026-07-26"
            report_dir.mkdir(parents=True)
            report = report_dir / "game_industry_weekend_2026-07-24_to_2026-07-26.md"
            report.write_text(
                "# 周末报\n\n## 五、行业精选 / 深度观察\n\n### 1. 周末观察\n\n观察：变化。\n\n分析：机制。\n",
                encoding="utf-8",
            )
            self.assertEqual([], HANDOFF.validate_weekly_handoff(report))

    def test_future_selection_requires_matching_feishu_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            review_dir = root / "output" / "deep_observation_review"
            review_dir.mkdir(parents=True)
            selection = review_dir / "2026-09-18_to_2026-09-24_selection.md"
            selection.write_text(
                """# selection
- 候选数据窗口: 2026-09-17_to_2026-09-23
- 目标周报窗口: 2026-09-18_to_2026-09-24
- 选择来源: 飞书周四备选 Bot
- 飞书回执ID: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- 正文候选ID: C005, C001
- 指定卡片候选ID: C005
- 卡片整合参考ID: C006, C014

## 用户选择进入周报的条目

### 1. ★卡片: Wardogs复盘
观察：x
分析：y

### 2. 第二题
观察：x
分析：y
""",
                encoding="utf-8",
            )
            receipt_dir = root / "data" / "feishu" / "deep_review" / "replies"
            receipt_dir.mkdir(parents=True)
            receipt = {
                "receipt_id": "a" * 32,
                "target_weekly_id": "2026-09-18_to_2026-09-24",
                "body_candidate_ids": ["C005", "C001"],
                "card_candidate_ids": ["C005", "C006", "C014"],
            }
            (receipt_dir / f"{receipt['receipt_id']}.json").write_text(
                json.dumps(receipt), encoding="utf-8"
            )
            self.assertEqual(
                [],
                HANDOFF.validate_feishu_selection_receipt(
                    selection, selection.read_text(encoding="utf-8"), receipt["target_weekly_id"]
                ),
            )

    def test_future_selection_rejects_missing_feishu_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            selection = Path(temp) / "selection.md"
            text = "- 目标周报窗口: 2026-09-18_to_2026-09-24\n"
            errors = HANDOFF.validate_feishu_selection_receipt(
                selection, text, "2026-09-18_to_2026-09-24"
            )
            self.assertTrue(any("选择来源" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
