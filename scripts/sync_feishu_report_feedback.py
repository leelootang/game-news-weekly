from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
from pathlib import Path
from typing import Any

from feishu_common import (
    PUBLISH_LOG_DIR,
    REPORT_FEEDBACK_PATH,
    FeishuClient,
    load_dotenv,
    read_json,
    write_json,
)


ROOT = Path(__file__).resolve().parents[1]
SYNC_STATE_PATH = ROOT / "data" / "feishu" / "report_feedback_sync_state.json"
TARGET_CONFIG_PATH = ROOT / "data" / "feishu" / "report_feedback_target.json"
EXPECTED_HEADERS = (
    "日期",
    "类型",
    "飞书文档链接",
    "用户id",
    "反馈类型（点赞/建议）",
    "反馈详情（建议文字内容）",
)
KIND_LABELS = {"daily": "日报", "weekend": "周末报", "weekly": "周报"}
RATING_LABELS = {"helpful": "点赞", "needs_improvement": "建议"}


def _text_elements(block: dict[str, Any]) -> list[dict[str, Any]]:
    for key in (
        "text",
        "heading1",
        "heading2",
        "heading3",
        "heading4",
        "heading5",
        "heading6",
        "bullet",
        "ordered",
    ):
        data = block.get(key)
        if isinstance(data, dict):
            return data.get("elements") or []
    return []


def _block_text(block: dict[str, Any]) -> str:
    return "".join(
        (element.get("text_run") or {}).get("content", "")
        for element in _text_elements(block)
    ).strip()


def _record_id(record: dict[str, Any]) -> str:
    existing = str(record.get("feedback_id") or "").strip()
    if existing:
        return existing
    canonical = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def load_feedback() -> list[dict[str, Any]]:
    if not REPORT_FEEDBACK_PATH.exists():
        return []
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        REPORT_FEEDBACK_PATH.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid feedback JSONL at {REPORT_FEEDBACK_PATH}:{line_number}"
            ) from exc
        if isinstance(record, dict):
            records.append(record)
    return records


def feedback_row(record: dict[str, Any]) -> list[str]:
    report_date = str(record.get("report_date") or "")
    kind = str(record.get("report_kind") or "")
    log = read_json(PUBLISH_LOG_DIR / f"daily_{report_date}.json", {})
    return [
        report_date,
        KIND_LABELS.get(kind, kind),
        str(log.get("doc_url") or ""),
        str(record.get("open_id") or ""),
        RATING_LABELS.get(str(record.get("rating") or ""), str(record.get("rating") or "")),
        str(record.get("feedback_text") or ""),
    ]


def create_feedback_doc(client: FeishuClient, folder_token: str) -> dict[str, str]:
    title = "日报/周报/周末报反馈信息收集"
    import_path = ROOT / "tmp" / "feishu_report_feedback_table.md"
    import_path.parent.mkdir(parents=True, exist_ok=True)
    header = " | ".join(EXPECTED_HEADERS)
    separator = " | ".join("---" for _ in EXPECTED_HEADERS)
    import_path.write_text(
        f"# {title}\n\n| {header} |\n| {separator} |\n",
        encoding="utf-8",
    )
    file_token = client.upload_import_media(import_path, f"{title}.md")
    ticket = client.create_import_task(file_token, title, folder_token)
    result = client.poll_import_task(ticket, timeout=90)
    config = {
        "doc_token": result["token"],
        "doc_url": result["url"],
        "folder_token": folder_token,
        "title": title,
    }
    write_json(TARGET_CONFIG_PATH, config)
    return config


def resolve_target_doc() -> str:
    config = read_json(TARGET_CONFIG_PATH, {})
    doc_token = str(config.get("doc_token") or "")
    if doc_token:
        return doc_token
    raise RuntimeError(
        "Bot-owned feedback document is not configured. "
        "Run sync_feishu_report_feedback.py --create-doc first."
    )


def find_feedback_table(
    blocks: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    by_id = {str(block.get("block_id")): block for block in blocks}
    for block in blocks:
        table = block.get("table") or {}
        cells = table.get("cells") or []
        column_size = int((table.get("property") or {}).get("column_size") or 0)
        if column_size != len(EXPECTED_HEADERS) or len(cells) < column_size:
            continue
        header_texts: list[str] = []
        for cell_id in cells[:column_size]:
            cell = by_id.get(str(cell_id)) or {}
            child_text = "".join(
                _block_text(by_id.get(str(child_id)) or {})
                for child_id in (cell.get("children") or [])
            )
            header_texts.append(child_text.strip())
        if tuple(header_texts) == EXPECTED_HEADERS:
            return block, by_id
    raise RuntimeError(
        "No table found with headers: " + " / ".join(EXPECTED_HEADERS)
    )


def _text_element(content: str, *, url: str = "") -> dict[str, Any]:
    style: dict[str, Any] = {}
    if url:
        style["link"] = {"url": urllib.parse.quote(url, safe="")}
    return {
        "text_run": {
            "content": content,
            "text_element_style": style,
        }
    }


def _write_cell(
    client: FeishuClient,
    doc_token: str,
    cell: dict[str, Any],
    content: str,
    *,
    url: str = "",
) -> None:
    elements = [_text_element(content, url=url)]
    children = cell.get("children") or []
    if children:
        child_id = str(children[0])
        client._request(
            "PATCH",
            f"/docx/v1/documents/{doc_token}/blocks/{child_id}",
            {"update_text_elements": {"elements": elements}},
            query={"document_revision_id": "-1"},
        )
        return
    client._request(
        "POST",
        f"/docx/v1/documents/{doc_token}/blocks/{cell['block_id']}/children",
        {
            "children": [
                {
                    "block_type": 2,
                    "text": {"elements": elements},
                }
            ],
            "index": 0,
        },
        query={"document_revision_id": "-1"},
    )


def append_feedback_row(
    client: FeishuClient,
    doc_token: str,
    table_id: str,
    values: list[str],
) -> None:
    client._request(
        "PATCH",
        f"/docx/v1/documents/{doc_token}/blocks/{table_id}",
        {"insert_table_row": {"row_index": -1}},
        query={"document_revision_id": "-1"},
    )
    blocks = client.get_all_blocks(doc_token)
    table, by_id = find_feedback_table(blocks)
    cells = (table.get("table") or {}).get("cells") or []
    new_cell_ids = cells[-len(EXPECTED_HEADERS) :]
    if len(new_cell_ids) != len(values):
        raise RuntimeError("Inserted table row did not return six cells")
    for index, (cell_id, value) in enumerate(zip(new_cell_ids, values)):
        cell = by_id.get(str(cell_id))
        if not cell:
            raise RuntimeError(f"Missing inserted table cell block: {cell_id}")
        link = value if index == 2 and value.startswith(("http://", "https://")) else ""
        _write_cell(
            client,
            doc_token,
            cell,
            "查看报告" if link else value,
            url=link,
        )


def sync_feedback(*, dry_run: bool = False) -> int:
    records = load_feedback()
    state = read_json(SYNC_STATE_PATH, {"synced_feedback_ids": []})
    synced = set(state.get("synced_feedback_ids") or [])
    pending = [record for record in records if _record_id(record) not in synced]
    if not pending:
        print("[feedback-sync] no new feedback")
        return 0
    if dry_run:
        for record in pending:
            print(json.dumps(feedback_row(record), ensure_ascii=False))
        print(f"[feedback-sync] dry-run pending={len(pending)}")
        return len(pending)

    load_dotenv()
    client = FeishuClient.from_env()
    doc_token = resolve_target_doc()
    blocks = client.get_all_blocks(doc_token)
    table, _by_id = find_feedback_table(blocks)
    table_id = str(table["block_id"])

    for record in pending:
        feedback_id = _record_id(record)
        append_feedback_row(client, doc_token, table_id, feedback_row(record))
        synced.add(feedback_id)
        write_json(
            SYNC_STATE_PATH,
            {
                "synced_feedback_ids": sorted(synced),
            },
        )
        print(
            f"[feedback-sync] synced id={feedback_id} "
            f"report={record.get('report_kind')}:{record.get('report_date')}"
        )
    print(f"[feedback-sync] complete synced={len(pending)}")
    return len(pending)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Append new Feishu report feedback to the configured Wiki doc table."
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--create-doc",
        action="store_true",
        help="Create the Bot-owned feedback table document in FEISHU_DAILY_FOLDER_TOKEN.",
    )
    args = parser.parse_args()
    if args.create_doc:
        load_dotenv()
        client = FeishuClient.from_env()
        from feishu_common import require_env

        folder_token = require_env("FEISHU_DAILY_FOLDER_TOKEN")["FEISHU_DAILY_FOLDER_TOKEN"]
        result = create_feedback_doc(client, folder_token)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    sync_feedback(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
