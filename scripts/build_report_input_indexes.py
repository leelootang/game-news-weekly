#!/usr/bin/env python3
"""Build readable Markdown indexes beside report input JSONL files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPORT_INPUT_NAME = "report_inputs.jsonl"
REPORT_INDEX_NAME = "report_inputs_index.md"


def shorten_text(value: Any, max_len: int = 96) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def table_cell(value: Any) -> str:
    return shorten_text(value).replace("|", "\\|").replace("\n", " ")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return records


def write_report_input_index(jsonl_path: Path) -> Path:
    records = load_jsonl(jsonl_path)
    index_path = jsonl_path.with_name(REPORT_INDEX_NAME)

    by_section: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        section = str(record.get("section") or "unknown")
        by_section.setdefault(section, []).append(record)

    lines = [
        "# Report Input Index",
        "",
        f"- Records: {len(records)}",
        f"- Raw JSONL: `{REPORT_INPUT_NAME}`",
        "",
        "## Section Counts",
        "",
    ]
    for section, section_records in sorted(by_section.items()):
        failures = sum(1 for item in section_records if item.get("extract_status") != "ok")
        empty = sum(
            1
            for item in section_records
            if item.get("extract_status") == "ok" and int(item.get("text_chars") or 0) == 0
        )
        attention = f", failures {failures}, empty {empty}" if failures or empty else ""
        lines.append(f"- `{section}`: {len(section_records)}{attention}")

    for section, section_records in sorted(by_section.items()):
        section_records.sort(
            key=lambda item: (
                str(item.get("date") or ""),
                str(item.get("published_at") or ""),
                str(item.get("source_key") or item.get("source") or ""),
                str(item.get("title") or ""),
            ),
            reverse=True,
        )
        lines.extend(
            [
                "",
                f"## {section}",
                "",
                "| # | Source ID | Date | Source | Chars | Status | Title | URL |",
                "| ---: | --- | --- | --- | ---: | --- | --- | --- |",
            ]
        )
        for index, record in enumerate(section_records, start=1):
            url = str(record.get("url") or "")
            url_cell = f"[link]({url})" if url.startswith(("http://", "https://")) else table_cell(url)
            lines.append(
                "| "
                f"{index} | "
                f"`{table_cell(record.get('source_id'))}` | "
                f"{table_cell(record.get('date'))} | "
                f"`{table_cell(record.get('source_key') or record.get('source'))}` | "
                f"{int(record.get('text_chars') or 0)} | "
                f"{table_cell(record.get('extract_status'))} | "
                f"{table_cell(record.get('title'))} | "
                f"{url_cell} |"
            )

    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return index_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Specific report_inputs.jsonl files or folders to scan.",
    )
    args = parser.parse_args()

    roots = args.paths or [ROOT / "output"]
    jsonl_files: list[Path] = []
    for path in roots:
        resolved = path.resolve()
        if resolved.is_file():
            jsonl_files.append(resolved)
        elif resolved.is_dir():
            jsonl_files.extend(sorted(resolved.glob(f"**/_intermediate/{REPORT_INPUT_NAME}")))

    written = [write_report_input_index(path) for path in sorted(set(jsonl_files))]
    for path in written:
        print(path)
    print(f"Wrote {len(written)} report input indexes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
