#!/usr/bin/env python3
"""Build readable Markdown indexes beside collected article JSONL files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from collectors.article_store import ARTICLE_JSONL_NAME, write_article_index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT / "news_data",
        help="Root folder containing section/date article JSONL files.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    jsonl_files = sorted(root.glob(f"*/*/{ARTICLE_JSONL_NAME}"))
    written = []
    for jsonl_file in jsonl_files:
        written.append(write_article_index(jsonl_file.parent))

    for path in written:
        print(path)
    print(f"Wrote {len(written)} article indexes under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
