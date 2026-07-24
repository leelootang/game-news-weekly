from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import feishu_subscribe_listener as listener
from feishu_common import build_daily_card


class FeishuReportFeedbackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.summary = {
            "kind": "weekly",
            "noun": "周报",
            "date": "2026-07-20_to_2026-07-26",
            "title": "游戏行业周报",
            "sections": [
                {
                    "name": "行业新闻",
                    "items": [{"title": "测试新闻", "body": "测试正文"}],
                }
            ],
        }

    def test_report_card_uses_v2_feedback_controls(self) -> None:
        card = build_daily_card(self.summary, doc_url="https://example.com/report")
        self.assertEqual(card["schema"], "2.0")
        elements = card["body"]["elements"]
        encoded = json.dumps(elements, ensure_ascii=False)
        self.assertIn("😊 很有帮助！", encoded)
        self.assertIn('"type": "danger_filled"', encoded)
        self.assertIn("😑 我有建议！", encoded)
        self.assertIn('"action": "report_feedback_expand"', encoded)
        self.assertNotIn('"input_type": "multiline_text"', encoded)

        expanded = build_daily_card(
            self.summary,
            doc_url="https://example.com/report",
            feedback_expanded=True,
        )
        expanded_json = json.dumps(expanded, ensure_ascii=False)
        self.assertIn('"input_type": "multiline_text"', expanded_json)
        self.assertIn('"action": "report_feedback_submit"', expanded_json)

    def test_feedback_events_append_to_backend(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            feedback_path = Path(tmp) / "report_feedback.jsonl"
            value = {
                "report_kind": "weekly",
                "report_date": "2026-07-20_to_2026-07-26",
                "report_title": "游戏行业周报",
            }
            with patch.object(listener, "REPORT_FEEDBACK_PATH", feedback_path):
                listener._save_report_feedback(
                    open_id="ou_test", value=value, rating="helpful"
                )
                listener._save_report_feedback(
                    open_id="ou_test",
                    value=value,
                    rating="needs_improvement",
                    feedback_text="希望增加数据图表。",
                )

            rows = [
                json.loads(line)
                for line in feedback_path.read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual([row["rating"] for row in rows], ["helpful", "needs_improvement"])
            self.assertEqual(rows[1]["feedback_text"], "希望增加数据图表。")
            self.assertEqual(rows[1]["report_kind"], "weekly")
            self.assertEqual(rows[1]["open_id"], "ou_test")


if __name__ == "__main__":
    unittest.main()
