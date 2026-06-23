from __future__ import annotations

import json
import sys
from typing import Any

from feishu_common import FeishuClient, load_dotenv, upsert_subscriber


SUBSCRIBE_WORDS = {"订阅", "订阅日报", "开始订阅", "subscribe"}
UNSUBSCRIBE_WORDS = {"退订", "退订日报", "取消订阅", "unsubscribe", "stop"}
HELP_TEXT = "发送“订阅日报”即可每天收到游戏行业日报；发送“退订日报”可取消。"


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
    if normalized in SUBSCRIBE_WORDS:
        upsert_subscriber(open_id=open_id, user_id=ids["user_id"], union_id=ids["union_id"], subscribed=True)
        client.send_text(open_id, "已订阅游戏行业日报。每天日报生成后，我会私聊推送卡片和完整文档链接。")
        print(f"[feishu] subscribed open_id={open_id}")
    elif normalized in UNSUBSCRIBE_WORDS:
        upsert_subscriber(open_id=open_id, user_id=ids["user_id"], union_id=ids["union_id"], subscribed=False)
        client.send_text(open_id, "已退订游戏行业日报。之后不会再主动推送。")
        print(f"[feishu] unsubscribed open_id={open_id}")
    else:
        client.send_text(open_id, HELP_TEXT)
        print(f"[feishu] replied help open_id={open_id} text={text!r}")


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
