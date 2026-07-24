from __future__ import annotations

import json
import sys
import uuid
from datetime import datetime, timezone
from typing import Any

from feishu_common import (
    PUBLISH_LOG_DIR,
    REPORT_FEEDBACK_PATH,
    FeishuClient,
    build_daily_card,
    get_subscription_preferences,
    load_report_summary,
    load_dotenv,
    read_json,
    set_subscription_preferences,
    upsert_subscriber,
)


SUBSCRIBE_WORDS = {"订阅", "订阅日报", "开始订阅", "subscribe"}
UNSUBSCRIBE_WORDS = {"退订", "退订日报", "取消订阅", "unsubscribe", "stop"}
HELP_TEXT = (
    "发送“订阅日报”即可订阅日报、周报和周末报；发送“修改订阅方式”可按类型选择；"
    "发送“退订日报”可全部退订。"
)
# 报告在 11 点群发；之后新订阅者已错过群发，立即给他补发今天群发的那份报告。
BACKFILL_AFTER_HOUR = 11
MENU_REPORTS = {
    "latest_daily": ("daily", "最新日报"),
    "latest_weekly": ("weekly", "最新周报"),
    "latest_weekend": ("weekend", "最新周末报"),
}
TEXT_REPORT_COMMANDS = {label: kind for kind, label in MENU_REPORTS.values()}
MANAGE_SUBSCRIPTIONS_MENU_KEY = "manage_subscriptions"
TEXT_PREFERENCES_COMMANDS = {"修改订阅方式", "订阅设置", "订阅偏好"}
REPORT_LABELS = {"daily": "日报", "weekly": "周报", "weekend": "周末报"}


def _attr(obj: Any, name: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _sender_ids(sender: Any) -> dict[str, str | None]:
    sender_id = _attr(sender, "sender_id", {}) or {}
    return {
        "open_id": _attr(sender_id, "open_id"),
        "user_id": _attr(sender_id, "user_id"),
        "union_id": _attr(sender_id, "union_id"),
    }


def _message_text(message: Any) -> str:
    content = _attr(message, "content", "") or ""
    if isinstance(content, str):
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            return content.strip()
        return str(parsed.get("text", "")).strip()
    if isinstance(content, dict):
        return str(content.get("text", "")).strip()
    return ""


def _maybe_backfill_today(client: FeishuClient, open_id: str, prev_pushed_date: str | None) -> None:
    """After 11:00 local time, immediately send a freshly-subscribed user the report
    that was broadcast today — whichever kind it was (daily / weekly / weekend) —
    reusing the same docx everyone else got. Skips silently if it's still early,
    if nothing has been broadcast yet today, or if the user already got it."""
    now = datetime.now()
    if now.hour < BACKFILL_AFTER_HOUR:
        return
    try:
        from publish_feishu_daily import backfill_one, latest_broadcast_today

        broadcast = latest_broadcast_today()
        if broadcast is None:
            print("[feishu] backfill skipped: no broadcast yet today")
            return
        identifier, _log = broadcast
        if prev_pushed_date == identifier:
            return
        backfill_one(client, open_id, identifier)
    except FileNotFoundError:
        print("[feishu] backfill skipped: today's report folder missing")
    except Exception as exc:  # never let a backfill failure break the listener
        print(f"[feishu] backfill failed open_id={open_id}: {exc}")
    else:
        print(f"[feishu] backfilled {identifier} report to new subscriber open_id={open_id}")


def _send_latest_report(client: FeishuClient, open_id: str, kind: str, label: str) -> None:
    """Replay the latest published report without changing subscription state."""
    try:
        from publish_feishu_daily import send_latest_report

        identifier = send_latest_report(client, open_id, kind)
    except Exception as exc:
        print(f"[feishu] latest report failed kind={kind} open_id={open_id}: {exc}")
        client.send_text(open_id, f"{label}暂时无法发送，请稍后重试。")
    else:
        print(f"[feishu] sent latest {kind}={identifier} to open_id={open_id}")


def build_subscription_card(preferences: dict[str, bool]) -> dict[str, Any]:
    """Build a CardKit 2.0 preference card for the long-connection callback.

    ``card.action.trigger`` (the callback our listener receives) is the new
    card callback.  Its long-connection transport does not support old 1.0
    message-card callbacks, so this card must use the 2.0 schema as well.
    """
    selected = [REPORT_LABELS[kind] for kind, enabled in preferences.items() if enabled]
    current = "、".join(selected) if selected else "未订阅（不会再主动推送）"
    report_buttons = []
    for kind, label in REPORT_LABELS.items():
        enabled = bool(preferences.get(kind))
        report_buttons.append(
            {
                "tag": "button",
                "element_id": f"sub_{kind}",
                "text": {"tag": "plain_text", "content": f"{'✅' if enabled else '⬜'} {label}"},
                "type": "primary" if enabled else "default",
                "behaviors": [
                    {"type": "callback", "value": {"action": "toggle_subscription", "kind": kind}}
                ],
            }
        )

    def button_column(button: dict[str, Any]) -> dict[str, Any]:
        return {"tag": "column", "elements": [button]}

    all_buttons = [
        {
            "tag": "button",
            "element_id": "sub_all",
            "text": {"tag": "plain_text", "content": "订阅全部"},
            "behaviors": [{"type": "callback", "value": {"action": "subscribe_all"}}],
        },
        {
            "tag": "button",
            "element_id": "sub_none",
            "text": {"tag": "plain_text", "content": "全部退订"},
            "type": "danger",
            "behaviors": [{"type": "callback", "value": {"action": "unsubscribe_all"}}],
        },
    ]
    return {
        "schema": "2.0",
        "header": {
            "template": "blue",
            "title": {"tag": "plain_text", "content": "🔔 修改订阅方式"},
        },
        "body": {
            "elements": [
                {
                    "tag": "markdown",
                    "content": f"**当前接收：** {current}\n点击下方按钮即可增减对应推送类型。",
                },
                {"tag": "hr"},
                {"tag": "column_set", "columns": [button_column(button) for button in report_buttons]},
                {"tag": "column_set", "columns": [button_column(button) for button in all_buttons]},
            ]
        },
    }


def _send_subscription_card(client: FeishuClient, open_id: str) -> None:
    client.send_interactive_card(open_id, build_subscription_card(get_subscription_preferences(open_id)))


def _card_action_response(
    toast: str,
    preferences: dict[str, bool] | None = None,
    card: dict[str, Any] | None = None,
) -> Any:
    """Return the documented v2 callback response and optionally refresh the card."""
    from lark_oapi.event.callback.model.p2_card_action_trigger import P2CardActionTriggerResponse

    response: dict[str, Any] = {"toast": {"type": "success", "content": toast}}
    if preferences is not None:
        response["card"] = {"type": "raw", "data": build_subscription_card(preferences)}
    elif card is not None:
        response["card"] = {"type": "raw", "data": card}
    return P2CardActionTriggerResponse(response)


def _save_report_feedback(
    *, open_id: str, value: dict[str, Any], rating: str, feedback_text: str = ""
) -> None:
    """Append one auditable report-feedback event to the local backend."""
    REPORT_FEEDBACK_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "feedback_id": uuid.uuid4().hex,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "open_id": open_id,
        "rating": rating,
        "feedback_text": feedback_text.strip(),
        "report_kind": str(value.get("report_kind") or ""),
        "report_date": str(value.get("report_date") or ""),
        "report_title": str(value.get("report_title") or ""),
    }
    with REPORT_FEEDBACK_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def handle_card_action_event(data: Any) -> Any:
    """Persist subscription changes made from the preference card."""
    event = _attr(data, "event", {})
    operator = _attr(event, "operator", {})
    open_id = _attr(operator, "open_id")
    action = _attr(event, "action", {})
    value = _attr(action, "value", {}) or {}
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            value = {}
    if not open_id or not isinstance(value, dict):
        return _card_action_response("订阅设置未保存，请重新打开菜单后再试。")

    action_name = value.get("action")
    if action_name == "report_feedback_helpful":
        _save_report_feedback(open_id=open_id, value=value, rating="helpful")
        print(
            f"[feishu] report feedback saved rating=helpful "
            f"open_id={open_id} report={value.get('report_kind')}:{value.get('report_date')}"
        )
        return _card_action_response("谢谢你的认可，已收到！")
    if action_name == "report_feedback_expand":
        report_date = str(value.get("report_date") or "")
        try:
            summary = load_report_summary(report_date)
            log = read_json(PUBLISH_LOG_DIR / f"daily_{report_date}.json", {})
            expanded_card = build_daily_card(
                summary,
                doc_url=log.get("doc_url"),
                per_section=10,
                feedback_expanded=True,
            )
        except Exception as exc:
            print(f"[feishu] failed to expand report feedback form: {exc}", flush=True)
            return _card_action_response("输入框暂时无法展开，请稍后重试。")
        return _card_action_response("欢迎提出建议", card=expanded_card)
    if action_name == "report_feedback_submit":
        form_value = _attr(action, "form_value", {}) or {}
        if isinstance(form_value, str):
            try:
                form_value = json.loads(form_value)
            except json.JSONDecodeError:
                form_value = {}
        feedback_text = str(
            _attr(form_value, "feedback_text", "")
            or _attr(action, "feedback_text", "")
        ).strip()
        if not feedback_text:
            return _card_action_response("请先填写建议再提交。")
        _save_report_feedback(
            open_id=open_id,
            value=value,
            rating="needs_improvement",
            feedback_text=feedback_text[:500],
        )
        print(
            f"[feishu] report feedback saved rating=needs_improvement "
            f"open_id={open_id} report={value.get('report_kind')}:{value.get('report_date')}"
        )
        return _card_action_response("建议已提交，谢谢你帮助我们改进！")

    preferences = get_subscription_preferences(open_id)
    if action_name == "toggle_subscription":
        kind = value.get("kind")
        if kind not in REPORT_LABELS:
            return _card_action_response("未知的订阅类型，请重新打开菜单后再试。", preferences)
        preferences[kind] = not preferences[kind]
        saved = set_subscription_preferences(open_id, preferences)
        enabled = bool(saved["subscriptions"][kind])
        toast = f"已{'订阅' if enabled else '取消订阅'}{REPORT_LABELS[kind]}"
    elif action_name == "subscribe_all":
        saved = set_subscription_preferences(open_id, {kind: True for kind in REPORT_LABELS})
        toast = "已订阅日报、周报和周末报"
    elif action_name == "unsubscribe_all":
        saved = set_subscription_preferences(open_id, {kind: False for kind in REPORT_LABELS})
        toast = "已全部退订"
    else:
        return _card_action_response("未知操作，请重新打开菜单后再试。", preferences)

    updated_preferences = {kind: bool(saved["subscriptions"][kind]) for kind in REPORT_LABELS}
    print(f"[feishu] subscription preferences updated open_id={open_id} preferences={updated_preferences}")
    return _card_action_response(toast, updated_preferences)


def handle_message_event(data: Any) -> None:
    event = _attr(data, "event", data)
    message = _attr(event, "message", {})
    sender = _attr(event, "sender", {})
    text = _message_text(message)
    ids = _sender_ids(sender)
    open_id = ids["open_id"]
    if not open_id:
        print("[feishu] ignored message without open_id")
        return

    client = FeishuClient.from_env()
    normalized = text.lower()
    if text in TEXT_REPORT_COMMANDS:
        kind = TEXT_REPORT_COMMANDS[text]
        _send_latest_report(client, open_id, kind, text)
    elif text in TEXT_PREFERENCES_COMMANDS:
        _send_subscription_card(client, open_id)
    elif normalized in SUBSCRIBE_WORDS:
        record = upsert_subscriber(
            open_id=open_id, user_id=ids["user_id"], union_id=ids["union_id"], subscribed=True
        )
        prev_pushed_date = record.get("last_pushed_date")
        client.send_text(open_id, "已订阅游戏行业报告：日报、周报和周末报都会私聊推送卡片和完整文档链接。")
        print(f"[feishu] subscribed open_id={open_id}")
        _maybe_backfill_today(client, open_id, prev_pushed_date)
    elif normalized in UNSUBSCRIBE_WORDS:
        upsert_subscriber(open_id=open_id, user_id=ids["user_id"], union_id=ids["union_id"], subscribed=False)
        client.send_text(open_id, "已全部退订游戏行业报告。之后不会再主动推送。")
        print(f"[feishu] unsubscribed open_id={open_id}")
    else:
        client.send_text(open_id, HELP_TEXT)
        print(f"[feishu] replied help open_id={open_id} text={text!r}")


def handle_bot_menu_event(data: Any) -> None:
    """Handle the three custom bot-menu buttons configured in Feishu.

    Each button's event_key is configured in the developer console and maps
    to a report kind in ``MENU_REPORTS``.  This event is only emitted in a
    bot's one-to-one chat, which is exactly where Feishu renders its bottom
    custom menu.
    """
    event = _attr(data, "event", {})
    event_key = _attr(event, "event_key", "")
    operator = _attr(event, "operator", {})
    operator_id = _attr(operator, "operator_id", {})
    open_id = _attr(operator_id, "open_id")
    if not open_id:
        print(f"[feishu] ignored bot menu event without open_id event_key={event_key!r}")
        return

    client = FeishuClient.from_env()
    if event_key == MANAGE_SUBSCRIPTIONS_MENU_KEY:
        _send_subscription_card(client, open_id)
        return

    target = MENU_REPORTS.get(event_key)
    if target is None:
        print(f"[feishu] ignored unknown bot menu event_key={event_key!r}")
        return
    kind, label = target
    _send_latest_report(client, open_id, kind, label)


def main() -> int:
    load_dotenv()
    try:
        import lark_oapi as lark
        from lark_oapi.api.im.v1 import P2ImMessageReceiveV1
    except ImportError:
        print("Missing dependency: lark-oapi")
        print("Install it with: python -m pip install lark-oapi")
        return 1

    client = FeishuClient.from_env()
    event_handler = (
        lark.EventDispatcherHandler.builder("", "")
        .register_p2_im_message_receive_v1(lambda data: handle_message_event(data))
        .register_p2_application_bot_menu_v6(lambda data: handle_bot_menu_event(data))
        .register_p2_card_action_trigger(lambda data: handle_card_action_event(data))
        .build()
    )
    ws_client = lark.ws.Client(
        client.app_id,
        client.app_secret,
        event_handler=event_handler,
        log_level=lark.LogLevel.INFO,
    )
    print("[feishu] subscribe listener started. Send “订阅日报” to the bot in Feishu.")
    ws_client.start()
    return 0


if __name__ == "__main__":
    sys.exit(main())
