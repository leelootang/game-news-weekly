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

    def test_feedback_row_prefers_resolved_user_name(self) -> None:
        record = {
            "report_date": "2026-07-22",
            "report_kind": "daily",
            "open_id": "ou_test",
            "rating": "helpful",
        }
        with patch.object(sync, "read_json", return_value={}):
            row = sync.feedback_row(record, user_name="张三")
        self.assertEqual(row[3], "张三")

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

    def test_find_feedback_table_accepts_legacy_id_header(self) -> None:
        cells = [f"legacy_cell_{index}" for index in range(6)]
        blocks = [
            {
                "block_id": "legacy_table",
                "block_type": 31,
                "table": {
                    "cells": cells,
                    "property": {"row_size": 1, "column_size": 6},
                },
            }
        ]
        for index, header in enumerate(sync.LEGACY_HEADERS):
            blocks.extend(
                [
                    {
                        "block_id": cells[index],
                        "block_type": 32,
                        "children": [f"legacy_text_{index}"],
                    },
                    {
                        "block_id": f"legacy_text_{index}",
                        "block_type": 2,
                        "text": {
                            "elements": [{"text_run": {"content": header}}],
                        },
                    },
                ]
            )
        table, _by_id = sync.find_feedback_table(blocks)
        self.assertEqual(table["block_id"], "legacy_table")

    def test_resolve_user_names_uses_name_only_contact_api(self) -> None:
        client = unittest.mock.Mock()
        client._request.return_value = {
            "data": {
                "users": [
                    {"user_id": "ou_one", "name": "张三"},
                    {"user_id": "ou_two", "name": "李四"},
                ]
            }
        }
        self.assertEqual(
            sync.resolve_user_names(client, ["ou_one", "ou_two", "ou_one"]),
            {"ou_one": "张三", "ou_two": "李四"},
        )
        client._request.assert_called_once_with(
            "POST",
            "/contact/v3/users/basic_batch",
            {"user_ids": ["ou_one", "ou_two"]},
            query={"user_id_type": "open_id"},
        )

    def test_resolve_user_names_batches_at_ten_users(self) -> None:
        client = unittest.mock.Mock()
        client._request.side_effect = [
            {
                "data": {
                    "users": [
                        {"user_id": f"ou_{index}", "name": f"用户{index}"}
                        for index in range(10)
                    ]
                }
            },
            {"data": {"users": [{"user_id": "ou_10", "name": "用户10"}]}},
        ]
        names = sync.resolve_user_names(
            client, [f"ou_{index}" for index in range(11)]
        )
        self.assertEqual(len(names), 11)
        self.assertEqual(client._request.call_count, 2)

    def test_user_display_name_labels_unresolvable_external_contact(self) -> None:
        self.assertEqual(
            sync.user_display_name("ou_123456789a3ae813"),
            "外部联系人（ID尾号 9a3ae813）",
        )

    def test_subscriber_row_includes_name_first_subscription_and_preferences(self) -> None:
        row = sync.subscriber_row(
            {
                "open_id": "ou_test",
                "created_at": "2026-07-23T03:30:00+00:00",
                "subscribed": True,
                "subscriptions": {
                    "daily": True,
                    "weekly": True,
                    "weekend": False,
                },
                "last_pushed_date": "2026-08-16",
            },
            user_name="张三",
        )
        self.assertEqual(
            row,
            ["张三", "2026-07-23 11:30", "日报、周报", "2026-08-16"],
        )

    def test_format_subscription_time_handles_missing_legacy_value(self) -> None:
        self.assertEqual(sync.format_subscription_time(None), "未知")


if __name__ == "__main__":
    unittest.main()
