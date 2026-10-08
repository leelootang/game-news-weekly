#!/usr/bin/env python3
"""Send Thursday candidates and receive the user's Feishu selection reply."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from feishu_common import FeishuClient, load_dotenv, read_json, write_json


ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data" / "feishu" / "deep_review"
BINDING_PATH = REVIEW_DIR / "binding.json"
CURRENT_DELIVERY_PATH = REVIEW_DIR / "current_delivery.json"
CURRENT_REPLY_PATH = REVIEW_DIR / "current_reply.json"
DELIVERY_DIR = REVIEW_DIR / "deliveries"
REPLY_DIR = REVIEW_DIR / "replies"
CANDIDATE_DIR = ROOT / "output" / "deep_observation_review"
APP_ID_ENV = "FEISHU_DEEP_REVIEW_APP_ID"
APP_SECRET_ENV = "FEISHU_DEEP_REVIEW_APP_SECRET"
CANDIDATE_RE = re.compile(
    r"(?ms)^###\s+(?P<id>C\d{3})\.\s+(?P<title>.+?)\s*$\n(?P<body>.*?)(?=^###\s+C\d{3}\.|^##\s+|\Z)"
)
WINDOW_RE = re.compile(r"(?m)^-\s*(?P<label>候选数据窗口|目标周报窗口):\s*(?P<value>\S+)\s*$")
CHOICE_LABEL_RE = re.compile(r"(?i)(正文|卡片)\s*[:：]")
ID_RE = re.compile(r"(?i)(?<![A-Z0-9])C\d{3}(?!\d)")
MAX_CARD_MARKDOWN = 10500


def _attr(obj: Any, name: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def review_client() -> FeishuClient:
    load_dotenv()
    app_id = os.environ.get(APP_ID_ENV, "").strip()
    app_secret = os.environ.get(APP_SECRET_ENV, "").strip()
    if not app_id or not app_secret:
        raise SystemExit(f"Missing required environment variables: {APP_ID_ENV}, {APP_SECRET_ENV}")
    return FeishuClient(app_id=app_id, app_secret=app_secret)


def parse_candidate_markdown(text: str) -> dict[str, Any]:
    windows = {m.group("label"): m.group("value") for m in WINDOW_RE.finditer(text)}
    candidates = [
        {
            "candidate_id": match.group("id").upper(),
            "title": match.group("title").strip(),
            "markdown": f"### {match.group('id').upper()}. {match.group('title').strip()}\n{match.group('body').strip()}",
        }
        for match in CANDIDATE_RE.finditer(text)
    ]
    if not windows.get("候选数据窗口") or not windows.get("目标周报窗口"):
        raise ValueError("候选文件缺少候选数据窗口或目标周报窗口")
    if not candidates:
        raise ValueError("候选文件没有可发送的 Cxxx 条目")
    ids = [item["candidate_id"] for item in candidates]
    if len(ids) != len(set(ids)):
        raise ValueError("候选文件包含重复 candidate_id")
    return {
        "candidate_window": windows["候选数据窗口"],
        "target_weekly_id": windows["目标周报窗口"],
        "candidates": candidates,
    }


def ordered_ids(text: str) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for match in ID_RE.finditer(text):
        candidate_id = match.group(0).upper()
        if candidate_id not in seen:
            result.append(candidate_id)
            seen.add(candidate_id)
    return result


def parse_choice_reply(text: str) -> dict[str, Any] | None:
    labels = list(CHOICE_LABEL_RE.finditer(text))
    if not labels:
        return None
    values: dict[str, str] = {}
    for index, match in enumerate(labels):
        end = labels[index + 1].start() if index + 1 < len(labels) else len(text)
        values[match.group(1)] = text[match.end():end].strip(" \t\r\n;；")
    body_ids = ordered_ids(values.get("正文", ""))
    card_ids = ordered_ids(values.get("卡片", ""))
    if not body_ids or not card_ids:
        raise ValueError("回复必须同时包含“正文：Cxxx”和“卡片：Cxxx”")
    if card_ids[0] not in body_ids:
        raise ValueError("卡片第一项是主卡候选，必须同时出现在正文选择中")
    return {
        "body_candidate_ids": body_ids,
        "card_candidate_ids": card_ids,
        "card_base_candidate_id": card_ids[0],
        "card_reference_candidate_ids": card_ids[1:],
    }


def _message_text(message: Any) -> str:
    content = _attr(message, "content", "") or ""
    if isinstance(content, str):
        try:
            content = json.loads(content)
        except json.JSONDecodeError:
            return content.strip()
    return str(_attr(content, "text", "") or "").strip()


def _sender_ids(sender: Any) -> dict[str, str | None]:
    sender_id = _attr(sender, "sender_id", {}) or {}
    return {
        "open_id": _attr(sender_id, "open_id"),
        "user_id": _attr(sender_id, "user_id"),
        "union_id": _attr(sender_id, "union_id"),
    }


def bind_sender(ids: dict[str, str | None]) -> dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    prior = read_json(BINDING_PATH, {})
    binding = {
        "open_id": ids.get("open_id"),
        "user_id": ids.get("user_id"),
        "union_id": ids.get("union_id"),
        "created_at": prior.get("created_at") or now,
        "updated_at": now,
    }
    write_json(BINDING_PATH, binding)
    return binding


def _candidate_cards(payload: dict[str, Any]) -> list[dict[str, Any]]:
    groups: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_size = 0
    for candidate in payload["candidates"]:
        size = len(candidate["markdown"])
        if current and current_size + size > MAX_CARD_MARKDOWN:
            groups.append(current)
            current, current_size = [], 0
        current.append(candidate)
        current_size += size
    if current:
        groups.append(current)

    cards: list[dict[str, Any]] = []
    total = len(groups)
    for index, group in enumerate(groups, 1):
        elements: list[dict[str, Any]] = []
        for pos, candidate in enumerate(group):
            if pos:
                elements.append({"tag": "hr"})
            elements.append({"tag": "markdown", "content": candidate["markdown"]})
        cards.append(
            {
                "schema": "2.0",
                "header": {
                    "template": "blue",
                    "title": {"tag": "plain_text", "content": f"周四深度观察候选 {index}/{total}"},
                },
                "body": {"elements": elements},
            }
        )
    return cards


def _instructions_card(payload: dict[str, Any]) -> dict[str, Any]:
    count = len(payload["candidates"])
    content = (
        f"已发送 **{count} 条全部合格候选**。\n\n"
        "请直接回复：\n"
        "`正文：C005，C001`\n"
        "`卡片：C005`\n\n"
        "如需融合多个候选，也可以写：\n"
        "`卡片：把 C005、C006、C014 的信息整合成 Wardogs 成绩复盘`\n"
        "`正文：C005，C001`\n\n"
        "卡片字段中的第一个编号是主卡，必须同时在正文里；后续编号仅作为整合参考。最新一条有效回复会覆盖此前选择。"
    )
    return {
        "schema": "2.0",
        "header": {
            "template": "green",
            "title": {"tag": "plain_text", "content": "请回复本周选择"},
        },
        "body": {"elements": [{"tag": "markdown", "content": content}]},
    }


def resolve_candidate_path(weekly_id: str | None, explicit: Path | None) -> Path:
    if explicit:
        return explicit
    if not weekly_id:
        raise ValueError("send 需要 --weekly-id 或 --candidates")
    return CANDIDATE_DIR / f"{weekly_id}_candidates.md"


def send_candidates(path: Path, *, dry_run: bool = False) -> dict[str, Any]:
    payload = parse_candidate_markdown(path.read_text(encoding="utf-8"))
    binding = read_json(BINDING_PATH, {})
    open_id = str(binding.get("open_id") or "")
    if not dry_run and not open_id:
        raise RuntimeError("新 Bot 尚未绑定；请先在飞书私聊该 Bot 发送任意消息")
    cards = _candidate_cards(payload)
    if not dry_run:
        client = review_client()
        for card in cards:
            client.send_interactive_card(open_id, card)
        client.send_interactive_card(open_id, _instructions_card(payload))
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    delivery = {
        "delivery_id": uuid.uuid4().hex,
        "created_at": now,
        "candidate_path": str(path.resolve()),
        "candidate_window": payload["candidate_window"],
        "target_weekly_id": payload["target_weekly_id"],
        "candidate_ids": [item["candidate_id"] for item in payload["candidates"]],
        "candidate_count": len(payload["candidates"]),
        "card_count": len(cards) + 1,
        "dry_run": dry_run,
    }
    if not dry_run:
        write_json(DELIVERY_DIR / f"{delivery['delivery_id']}.json", delivery)
        write_json(CURRENT_DELIVERY_PATH, delivery)
    return delivery


def save_reply(text: str, ids: dict[str, str | None], message_id: str) -> dict[str, Any]:
    choice = parse_choice_reply(text)
    if choice is None:
        raise ValueError("未识别到“正文：…”与“卡片：…”选择格式")
    delivery = read_json(CURRENT_DELIVERY_PATH, {})
    if not delivery or delivery.get("dry_run"):
        raise ValueError("当前没有已正式发送的候选批次")
    valid_ids = set(delivery.get("candidate_ids") or [])
    chosen_ids = choice["body_candidate_ids"] + choice["card_candidate_ids"]
    unknown = [candidate_id for candidate_id in chosen_ids if candidate_id not in valid_ids]
    if unknown:
        raise ValueError(f"回复包含不在本周候选中的编号：{', '.join(dict.fromkeys(unknown))}")
    receipt_id = uuid.uuid4().hex
    receipt = {
        "receipt_id": receipt_id,
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "message_id": message_id,
        "sender": ids,
        "delivery_id": delivery["delivery_id"],
        "candidate_window": delivery["candidate_window"],
        "target_weekly_id": delivery["target_weekly_id"],
        "candidate_path": delivery["candidate_path"],
        "raw_reply": text,
        **choice,
        "status": "pending_materialization",
    }
    write_json(REPLY_DIR / f"{receipt_id}.json", receipt)
    write_json(CURRENT_REPLY_PATH, receipt)
    return receipt


def handle_message_event(data: Any) -> None:
    event = _attr(data, "event", data)
    message = _attr(event, "message", {}) or {}
    sender = _attr(event, "sender", {}) or {}
    text = _message_text(message)
    ids = _sender_ids(sender)
    open_id = ids.get("open_id")
    if not open_id:
        print("[deep-review] ignored message without open_id", flush=True)
        return
    bind_sender(ids)
    client = review_client()
    message_id = str(_attr(message, "message_id", "") or "")
    try:
        choice = parse_choice_reply(text)
        if choice is None:
            client.send_text(
                open_id,
                "周四备选 Bot 已绑定。候选发出后，请同时回复“正文：Cxxx”和“卡片：Cxxx”；卡片可列多个编号供整合。",
            )
            print("[deep-review] sender bound", flush=True)
            return
        receipt = save_reply(text, ids, message_id)
    except ValueError as exc:
        client.send_text(open_id, f"这条选择还不能保存：{exc}\n请按“正文：C005，C001；卡片：C005”重发。")
        print(f"[deep-review] invalid reply: {exc}", flush=True)
        return
    body = "、".join(receipt["body_candidate_ids"])
    card = "、".join(receipt["card_candidate_ids"])
    client.send_text(
        open_id,
        f"已保存本周选择。正文：{body}；卡片：{card}。周五生成任务会按你的原话整理并先通过交接校验。",
    )
    print(f"[deep-review] reply saved receipt_id={receipt['receipt_id']} body={body} card={card}", flush=True)


def listen() -> int:
    try:
        import lark_oapi as lark
    except ImportError:
        print("Missing dependency: lark-oapi")
        return 1
    client = review_client()
    event_handler = (
        lark.EventDispatcherHandler.builder("", "")
        .register_p2_im_message_receive_v1(lambda data: handle_message_event(data))
        .build()
    )
    ws_client = lark.ws.Client(
        client.app_id,
        client.app_secret,
        event_handler=event_handler,
        # INFO logs include the ephemeral websocket access URL. Keep credentials
        # and connection tokens out of persistent task logs.
        log_level=lark.LogLevel.ERROR,
    )
    print("[deep-review] listener started; send any direct message to bind this bot", flush=True)
    ws_client.start()
    return 0


def status(weekly_id: str | None = None) -> dict[str, Any]:
    binding = read_json(BINDING_PATH, {})
    delivery = read_json(CURRENT_DELIVERY_PATH, {})
    reply = read_json(CURRENT_REPLY_PATH, {})
    reply_matches = bool(reply) and (weekly_id is None or reply.get("target_weekly_id") == weekly_id)
    return {
        "bound": bool(binding.get("open_id")),
        "binding_updated_at": binding.get("updated_at"),
        "delivery": {
            key: delivery.get(key)
            for key in ("delivery_id", "created_at", "candidate_window", "target_weekly_id", "candidate_count")
        } if delivery else None,
        "reply": {
            key: reply.get(key)
            for key in (
                "receipt_id", "created_at", "target_weekly_id", "body_candidate_ids",
                "card_base_candidate_id", "card_reference_candidate_ids", "status",
            )
        } if reply_matches else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("listen")
    send = sub.add_parser("send")
    send.add_argument("--weekly-id")
    send.add_argument("--candidates", type=Path)
    send.add_argument("--dry-run", action="store_true")
    show = sub.add_parser("status")
    show.add_argument("--weekly-id")
    show.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.command == "listen":
        return listen()
    if args.command == "send":
        path = resolve_candidate_path(args.weekly_id, args.candidates)
        delivery = send_candidates(path, dry_run=args.dry_run)
        print(json.dumps(delivery, ensure_ascii=False, indent=2))
        return 0
    payload = status(args.weekly_id)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
