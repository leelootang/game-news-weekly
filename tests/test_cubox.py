from __future__ import annotations

import sys
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch


COLLECTORS_DIR = Path(__file__).resolve().parents[1] / "collectors"
if str(COLLECTORS_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTORS_DIR))

import cubox as collector


class CuboxCollectorTests(unittest.TestCase):
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
