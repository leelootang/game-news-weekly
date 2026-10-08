from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from feishu_common import (
    PUBLISH_LOG_DIR,
    REPORT_FEEDBACK_PATH,
    FeishuClient,
    active_subscribers,
    load_dotenv,
    read_json,
    subscription_preferences,
    write_json,
)


ROOT = Path(__file__).resolve().parents[1]
SYNC_STATE_PATH = ROOT / "data" / "feishu" / "report_feedback_sync_state.json"
TARGET_CONFIG_PATH = ROOT / "data" / "feishu" / "report_feedback_target.json"
EXPECTED_HEADERS = (
    "日期",
    "类型",
    "飞书文档链接",
    "用户姓名",
    "反馈类型（点赞/建议）",
    "反馈详情（建议文字内容）",
)
LEGACY_HEADERS = (
    "日期",
    "类型",
    "飞书文档链接",
    "用户id",
    "反馈类型（点赞/建议）",
    "反馈详情（建议文字内容）",
)
SUPPORTED_HEADERS = (EXPECTED_HEADERS, LEGACY_HEADERS)
USER_COLUMN_INDEX = 3
SUBSCRIBER_HEADERS = (
    "用户姓名",
    "首次订阅时间",
    "订阅内容",
    "最近推送日期",
)
SUBSCRIBER_SECTION_TITLE = "当前订阅用户列表（每日 11:00 刷新）"
SHANGHAI_TZ = timezone(timedelta(hours=8), name="Asia/Shanghai")
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


def feedback_row(record: dict[str, Any], *, user_name: str = "") -> list[str]:
    report_date = str(record.get("report_date") or "")
    kind = str(record.get("report_kind") or "")
    log = read_json(PUBLISH_LOG_DIR / f"daily_{report_date}.json", {})
    return [
        report_date,
        KIND_LABELS.get(kind, kind),
        str(log.get("doc_url") or ""),
        user_name or str(record.get("open_id") or ""),
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
        if tuple(header_texts) in SUPPORTED_HEADERS:
            return block, by_id
    raise RuntimeError(
        "No feedback table found with the current or legacy headers"
    )


def _cell_text(cell: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> str:
    return "".join(
        _block_text(by_id.get(str(child_id)) or {})
        for child_id in (cell.get("children") or [])
    ).strip()


def _table_headers(
    table: dict[str, Any], by_id: dict[str, dict[str, Any]]
) -> tuple[str, ...]:
    cells = (table.get("table") or {}).get("cells") or []
    return tuple(
        _cell_text(by_id.get(str(cell_id)) or {}, by_id)
        for cell_id in cells[: len(EXPECTED_HEADERS)]
    )


def find_subscriber_table(
    blocks: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]] | None:
    by_id = {str(block.get("block_id")): block for block in blocks}
    candidates: list[dict[str, Any]] = []
    for block in blocks:
        table = block.get("table") or {}
        cells = table.get("cells") or []
        column_size = int((table.get("property") or {}).get("column_size") or 0)
        if column_size != len(SUBSCRIBER_HEADERS) or len(cells) < column_size:
            continue
        candidates.append(block)
        headers = tuple(
            _cell_text(by_id.get(str(cell_id)) or {}, by_id)
            for cell_id in cells[:column_size]
        )
        if headers == SUBSCRIBER_HEADERS:
            return block, by_id
    if len(candidates) == 1:
        return candidates[0], by_id
    return None


def resolve_user_names(
    client: FeishuClient, open_ids: list[str]
) -> dict[str, str]:
    """Resolve app-scoped open IDs using Feishu's name-only contact API."""
    unique_ids = list(dict.fromkeys(open_id for open_id in open_ids if open_id))
    resolved: dict[str, str] = {}
    for start in range(0, len(unique_ids), 10):
        batch = unique_ids[start : start + 10]
        response = client._request(
            "POST",
            "/contact/v3/users/basic_batch",
            {"user_ids": batch},
            query={"user_id_type": "open_id"},
        )
        for user in (response.get("data") or {}).get("users") or []:
            open_id = str(user.get("user_id") or "").strip()
            name = str(user.get("name") or "").strip()
            if open_id and name:
                resolved[open_id] = name
    return resolved


def user_display_name(open_id: str, resolved_name: str = "") -> str:
    if resolved_name:
        return resolved_name
    if open_id:
        return f"外部联系人（ID尾号 {open_id[-8:]}）"
    return "未知用户"


def format_subscription_time(value: Any) -> str:
    raw = str(value or "").strip()
    if not raw:
        return "未知"
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return raw
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=SHANGHAI_TZ)
    return parsed.astimezone(SHANGHAI_TZ).strftime("%Y-%m-%d %H:%M")


def subscriber_row(
    subscriber: dict[str, Any], *, user_name: str = ""
) -> list[str]:
    open_id = str(subscriber.get("open_id") or "")
    preferences = subscription_preferences(subscriber)
    subscriptions = [
        KIND_LABELS[kind]
        for kind in ("daily", "weekly", "weekend")
        if preferences.get(kind)
    ]
    return [
        user_display_name(open_id, user_name),
        format_subscription_time(subscriber.get("created_at")),
        "、".join(subscriptions) or "无",
        str(subscriber.get("last_pushed_date") or "暂无"),
    ]


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


def _create_subscriber_table(
    client: FeishuClient,
    doc_token: str,
) -> str:
    blocks = client.get_all_blocks(doc_token)
    root = next(
        (block for block in blocks if str(block.get("block_id")) == doc_token),
        None,
    )
    if not root:
        raise RuntimeError("Could not find the feedback document root block")
    root_children = root.get("children") or []
    response = client._request(
        "POST",
        f"/docx/v1/documents/{doc_token}/blocks/{doc_token}/children",
        {
            "children": [
                {
                    "block_type": 4,
                    "heading2": {
                        "elements": [_text_element(SUBSCRIBER_SECTION_TITLE)]
                    },
                },
                {
                    "block_type": 31,
                    "table": {
                        "property": {
                            "row_size": 1,
                            "column_size": len(SUBSCRIBER_HEADERS),
                        }
                    },
                },
            ],
            "index": max(0, len(root_children) - 1),
        },
        query={"document_revision_id": "-1"},
    )
    created = (response.get("data") or {}).get("children") or response.get("children") or []
    table_block = next((block for block in created if block.get("table")), None)
    if table_block and table_block.get("block_id"):
        return str(table_block["block_id"])

    refreshed = client.get_all_blocks(doc_token)
    candidates = [
        block
        for block in refreshed
        if int(((block.get("table") or {}).get("property") or {}).get("column_size") or 0)
        == len(SUBSCRIBER_HEADERS)
    ]
    if len(candidates) != 1:
        raise RuntimeError("Could not identify the newly created subscriber table")
    return str(candidates[0]["block_id"])


def refresh_subscriber_table(client: FeishuClient, doc_token: str) -> int:
    subscribers = sorted(
        active_subscribers(),
        key=lambda row: (str(row.get("created_at") or ""), str(row.get("open_id") or "")),
    )
    open_ids = [str(row.get("open_id") or "") for row in subscribers]
    names = resolve_user_names(client, open_ids)
    desired_rows = [
        list(SUBSCRIBER_HEADERS),
        *[
            subscriber_row(row, user_name=names.get(str(row.get("open_id") or ""), ""))
            for row in subscribers
        ],
    ]

    blocks = client.get_all_blocks(doc_token)
    found = find_subscriber_table(blocks)
    if found is None:
        table_id = _create_subscriber_table(
            client,
            doc_token,
        )
        current_rows = 1
    else:
        table_id = str(found[0]["block_id"])
        current_rows = int(((found[0].get("table") or {}).get("property") or {}).get("row_size") or 0)

    desired_count = len(desired_rows)
    if current_rows > desired_count:
        client._request(
            "PATCH",
            f"/docx/v1/documents/{doc_token}/blocks/{table_id}",
            {
                "delete_table_rows": {
                    "row_start_index": desired_count,
                    "row_end_index": current_rows,
                }
            },
            query={"document_revision_id": "-1"},
        )
    for _index in range(current_rows, desired_count):
        client._request(
            "PATCH",
            f"/docx/v1/documents/{doc_token}/blocks/{table_id}",
            {"insert_table_row": {"row_index": -1}},
            query={"document_revision_id": "-1"},
        )

    blocks = client.get_all_blocks(doc_token)
    by_id = {str(block.get("block_id")): block for block in blocks}
    table = by_id.get(table_id)
    if not table:
        raise RuntimeError("Subscriber table disappeared during refresh")
    cells = (table.get("table") or {}).get("cells") or []
    flat_values = [value for row in desired_rows for value in row]
    if len(cells) != len(flat_values):
        raise RuntimeError(
            f"Subscriber table cell mismatch: cells={len(cells)} values={len(flat_values)}"
        )
    updated_cells = 0
    for cell_id, value in zip(cells, flat_values):
        cell = by_id.get(str(cell_id))
        if not cell:
            raise RuntimeError(f"Missing subscriber table cell block: {cell_id}")
        if _cell_text(cell, by_id) == value:
            continue
        _write_cell(client, doc_token, cell, value)
        updated_cells += 1

    external_count = sum(open_id not in names for open_id in open_ids)
    print(
        f"[feedback-sync] subscribers active={len(subscribers)} "
        f"external_fallbacks={external_count} updated_cells={updated_cells}"
    )
    return len(subscribers)


def backfill_feedback_user_names() -> int:
    """Replace legacy open IDs with names, then rename the table header.

    The header is changed last so a failed or incomplete lookup leaves the
    existing ID-based table and scheduled sync behavior intact.
    """
    load_dotenv()
    client = FeishuClient.from_env()
    doc_token = resolve_target_doc()
    blocks = client.get_all_blocks(doc_token)
    table, by_id = find_feedback_table(blocks)
    headers = _table_headers(table, by_id)
    cells = (table.get("table") or {}).get("cells") or []
    column_count = len(EXPECTED_HEADERS)
    user_cells: list[tuple[dict[str, Any], str]] = []
    for offset in range(column_count + USER_COLUMN_INDEX, len(cells), column_count):
        cell = by_id.get(str(cells[offset]))
        if not cell:
            raise RuntimeError(f"Missing user table cell block: {cells[offset]}")
        current_value = _cell_text(cell, by_id)
        if current_value.startswith("ou_"):
            user_cells.append((cell, current_value))

    names = resolve_user_names(client, [open_id for _cell, open_id in user_cells])

    for cell, open_id in user_cells:
        _write_cell(
            client,
            doc_token,
            cell,
            user_display_name(open_id, names.get(open_id, "")),
        )

    if headers == LEGACY_HEADERS:
        header_cell = by_id.get(str(cells[USER_COLUMN_INDEX]))
        if not header_cell:
            raise RuntimeError("Missing feedback user header cell")
        _write_cell(client, doc_token, header_cell, EXPECTED_HEADERS[USER_COLUMN_INDEX])

    fallback_count = sum(open_id not in names for _cell, open_id in user_cells)
    print(
        f"[feedback-sync] backfilled user names={len(user_cells) - fallback_count} "
        f"external_fallbacks={fallback_count}"
    )
    return len(user_cells)


def sync_feedback(*, dry_run: bool = False) -> int:
    records = load_feedback()
    state = read_json(SYNC_STATE_PATH, {"synced_feedback_ids": []})
    synced = set(state.get("synced_feedback_ids") or [])
    pending = [record for record in records if _record_id(record) not in synced]
    if dry_run:
        for record in pending:
            print(json.dumps(feedback_row(record), ensure_ascii=False))
        print(f"[feedback-sync] dry-run pending={len(pending)}")
        print(f"[feedback-sync] dry-run active_subscribers={len(active_subscribers())}")
        return len(pending)

    load_dotenv()
    client = FeishuClient.from_env()
    doc_token = resolve_target_doc()
    if pending:
        blocks = client.get_all_blocks(doc_token)
        table, by_id = find_feedback_table(blocks)
        table_id = str(table["block_id"])
        headers = _table_headers(table, by_id)
        user_names: dict[str, str] = {}
        if headers == EXPECTED_HEADERS:
            open_ids = [str(record.get("open_id") or "") for record in pending]
            user_names = resolve_user_names(client, open_ids)

        for record in pending:
            feedback_id = _record_id(record)
            open_id = str(record.get("open_id") or "")
            append_feedback_row(
                client,
                doc_token,
                table_id,
                feedback_row(
                    record,
                    user_name=user_display_name(open_id, user_names.get(open_id, "")),
                ),
            )
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
    else:
        print("[feedback-sync] no new feedback")

    refresh_subscriber_table(client, doc_token)
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
    parser.add_argument(
        "--backfill-user-names",
        action="store_true",
        help="Replace historical open IDs with Feishu contact names.",
    )
    parser.add_argument(
        "--refresh-subscribers",
        action="store_true",
        help="Refresh the active subscriber table in the feedback document.",
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
    if args.backfill_user_names:
        backfill_feedback_user_names()
        return 0
    if args.refresh_subscribers:
        load_dotenv()
        refresh_subscriber_table(FeishuClient.from_env(), resolve_target_doc())
        return 0
    sync_feedback(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
