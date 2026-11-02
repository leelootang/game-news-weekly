from __future__ import annotations

import sys
import json
import subprocess
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch


COLLECTORS_DIR = Path(__file__).resolve().parents[1] / "collectors"
if str(COLLECTORS_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTORS_DIR))

import cubox as collector


class CuboxCollectorTests(unittest.TestCase):
    def cli_result(self, payload):
        return subprocess.CompletedProcess([], 0, json.dumps(payload), "")

    def test_list_accepts_upgrade_notice_envelope(self) -> None:
        payload = {"data": [{"id": "123"}], "_notice": {"update": {"latest": "new"}}}
        with patch.object(collector.subprocess, "run", return_value=self.cli_result(payload)):
            cards = collector.list_created_cards(Path("cubox-cli"), datetime(2026, 10, 26), datetime(2026, 10, 27))
        self.assertEqual([{"id": "123"}], cards)

    def test_wrapped_null_and_empty_list_are_valid_empty_windows(self) -> None:
        for value in (None, []):
            with self.subTest(value=value), patch.object(collector.subprocess, "run", return_value=self.cli_result({"data": value, "_notice": {"update": {}}})):
                self.assertEqual([], collector.list_created_cards(Path("cubox-cli"), datetime(2026, 10, 26), datetime(2026, 10, 27)))

    def test_detail_accepts_upgrade_notice_envelope(self) -> None:
        detail = {"id": "123", "content": "Complete article body"}
        with patch.object(collector.subprocess, "run", return_value=self.cli_result({"data": detail, "_notice": {"update": {}}})):
            self.assertEqual(detail, collector.get_card_detail(Path("cubox-cli"), "123"))

    def test_unknown_objects_are_not_silently_treated_as_empty(self) -> None:
        with patch.object(collector.subprocess, "run", return_value=self.cli_result({"unexpected": []})):
            with self.assertRaisesRegex(RuntimeError, "unexpected JSON shape"):
                collector.list_created_cards(Path("cubox-cli"), datetime(2026, 10, 26), datetime(2026, 10, 27))

    def test_error_envelope_remains_a_failure(self) -> None:
        with patch.object(collector.subprocess, "run", return_value=self.cli_result({"error": "unauthorized", "_notice": {"update": {}}})):
            with self.assertRaisesRegex(RuntimeError, "unauthorized"):
                collector.list_created_cards(Path("cubox-cli"), datetime(2026, 10, 26), datetime(2026, 10, 27))

    def test_raw_detail_without_notice_is_unchanged(self) -> None:
        detail = {"id": "123", "content": "Body", "data": "an article field"}
        with patch.object(collector.subprocess, "run", return_value=self.cli_result(detail)):
            self.assertEqual(detail, collector.get_card_detail(Path("cubox-cli"), "123"))

    def test_list_created_cards_treats_null_as_empty(self) -> None:
        with patch.object(collector, "run_cli_json", return_value=None):
            cards = collector.list_created_cards(
                Path("cubox-cli"),
                datetime(2026, 7, 23),
                datetime(2026, 7, 24),
            )
        self.assertEqual([], cards)

    def test_list_created_cards_uses_local_day_window(self) -> None:
        captured: list[str] = []

        def fake_run(cli: Path, arguments: list[str]):
            captured.extend(arguments)
            return []

        with patch.object(collector, "run_cli_json", side_effect=fake_run):
            collector.list_created_cards(
                Path("cubox-cli"),
                datetime(2026, 7, 23),
                datetime(2026, 7, 24),
            )
        self.assertEqual(
            [
                "card",
                "list",
                "--start-time",
                "2026-07-23T00:00:00+08:00",
                "--end-time",
                "2026-07-24T00:00:00+08:00",
                "--all",
                "-o",
                "json",
            ],
            captured,
        )

    def test_normalize_card_keeps_original_url_and_cubox_metadata(self) -> None:
        card = collector.normalize_card(
            {
                "id": "7451602344275345458",
                "title": "List title",
                "article_title": "Article title",
                "description": "A useful article",
                "domain": "example.com",
                "url": "https://example.com/post",
                "create_time": "2026-07-23T09:30:15.552+0800",
                "update_time": "2026-07-23T10:00:00.000+0800",
                "content": "# Article title\n\nFull Markdown body.",
                "author": "Author",
                "read": False,
                "starred": True,
                "tags": ["daily"],
                "folder": {"name": "Uncategorized", "uncategorized": True},
            }
        )

        self.assertEqual("7451602344275345458", card["id"])
        self.assertEqual("Article title", card["title"])
        self.assertEqual("https://example.com/post", card["url"])
        self.assertEqual("example.com", card["source"])
        self.assertEqual("2026-07-23T09:30:15", card["published_at"])
        self.assertEqual("# Article title\n\nFull Markdown body.", card["text"])
        self.assertIs(card["extra"]["via_cubox"], True)
        self.assertEqual("7451602344275345458", card["extra"]["cubox_card_id"])
        self.assertEqual(["daily"], card["extra"]["cubox_tags"])

    def test_normalize_card_rejects_empty_content(self) -> None:
        with self.assertRaisesRegex(ValueError, "no parsed content"):
            collector.normalize_card(
                {
                    "id": "1",
                    "title": "No body",
                    "url": "https://example.com",
                    "create_time": "2026-07-23T09:30:15+0800",
                    "content": "",
                }
            )


if __name__ == "__main__":
    unittest.main()
