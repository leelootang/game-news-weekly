from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import sync_feishu_report_feedback as sync


class FeishuFeedbackSyncTests(unittest.TestCase):
    def test_resolve_target_doc_uses_bot_created_document_config(self) -> None:
        with patch.object(sync, "read_json", return_value={"doc_token": "bot-doc-token"}):
            self.assertEqual(sync.resolve_target_doc(), "bot-doc-token")

    def test_resolve_target_doc_has_no_legacy_wiki_fallback(self) -> None:
        with patch.object(sync, "read_json", return_value={}):
            with self.assertRaisesRegex(RuntimeError, "Bot-owned feedback document"):
                sync.resolve_target_doc()

    def test_feedback_row_maps_requested_columns(self) -> None:
        record = {
            "report_date": "2026-07-22",
            "report_kind": "daily",
            "open_id": "ou_test",
            "rating": "needs_improvement",
            "feedback_text": "希望增加趋势图。",
        }
        with patch.object(
            sync,
            "read_json",
            return_value={"doc_url": "https://moonton.feishu.cn/docx/test"},
        ):
            self.assertEqual(
                sync.feedback_row(record),
                [
                    "2026-07-22",
                    "日报",
                    "https://moonton.feishu.cn/docx/test",
                    "ou_test",
                    "建议",
                    "希望增加趋势图。",
                ],
            )

    def test_find_feedback_table_matches_headers(self) -> None:
        cells = [f"cell_{index}" for index in range(6)]
        blocks = [
            {
                "block_id": "table_1",
                "block_type": 31,
                "table": {
                    "cells": cells,
                    "property": {"row_size": 1, "column_size": 6},
                },
            }
        ]
        for index, header in enumerate(sync.EXPECTED_HEADERS):
            blocks.extend(
                [
                    {
                        "block_id": cells[index],
                        "block_type": 32,
                        "children": [f"text_{index}"],
                    },
                    {
                        "block_id": f"text_{index}",
                        "block_type": 2,
                        "text": {
                            "elements": [{"text_run": {"content": header}}],
                        },
                    },
                ]
            )
        table, _by_id = sync.find_feedback_table(blocks)
        self.assertEqual(table["block_id"], "table_1")


if __name__ == "__main__":
    unittest.main()
