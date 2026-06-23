from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "feishu"
SUBSCRIBERS_PATH = DATA_DIR / "subscribers.json"
PUBLISH_LOG_DIR = DATA_DIR / "publish_logs"
OPEN_FEISHU_BASE = "https://open.feishu.cn/open-apis"


def load_dotenv(path: Path | None = None) -> None:
    env_path = path or ROOT / ".env.local"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def require_env(*names: str) -> dict[str, str]:
    load_dotenv()
    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
    return {name: os.environ[name] for name in names}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_subscribers() -> dict[str, Any]:
    data = read_json(SUBSCRIBERS_PATH, {"subscribers": []})
    if "subscribers" not in data or not isinstance(data["subscribers"], list):
        raise ValueError(f"Invalid subscriber file: {SUBSCRIBERS_PATH}")
    return data


def upsert_subscriber(
    *,
    open_id: str,
    user_id: str | None = None,
    union_id: str | None = None,
    name: str | None = None,
    subscribed: bool,
) -> dict[str, Any]:
    if not open_id:
        raise ValueError("open_id is required")
    data = load_subscribers()
    now = utc_now_iso()
    existing = next((row for row in data["subscribers"] if row.get("open_id") == open_id), None)
    if existing is None:
        existing = {
            "open_id": open_id,
            "user_id": user_id,
            "union_id": union_id,
            "name": name,
            "created_at": now,
            "last_pushed_date": None,
        }
        data["subscribers"].append(existing)
    existing.update(
        {
            "user_id": user_id or existing.get("user_id"),
            "union_id": union_id or existing.get("union_id"),
            "name": name or existing.get("name"),
            "subscribed": subscribed,
            "updated_at": now,
        }
    )
    write_json(SUBSCRIBERS_PATH, data)
    return existing


def active_subscribers() -> list[dict[str, Any]]:
    data = load_subscribers()
    return [row for row in data["subscribers"] if row.get("subscribed") and row.get("open_id")]


class FeishuAPIError(RuntimeError):
    pass


@dataclass
class FeishuClient:
    app_id: str
    app_secret: str
    base_url: str = OPEN_FEISHU_BASE
    _tenant_access_token: str | None = None
    _token_expires_at: float = 0

    @classmethod
    def from_env(cls) -> "FeishuClient":
        env = require_env("FEISHU_APP_ID", "FEISHU_APP_SECRET")
        return cls(app_id=env["FEISHU_APP_ID"], app_secret=env["FEISHU_APP_SECRET"])

    def tenant_access_token(self) -> str:
        if self._tenant_access_token and time.time() < self._token_expires_at - 60:
            return self._tenant_access_token
        payload = {"app_id": self.app_id, "app_secret": self.app_secret}
        data = self._request(
            "POST",
            "/auth/v3/tenant_access_token/internal",
            payload,
            auth=False,
        )
        token = data.get("tenant_access_token")
        if not token:
            raise FeishuAPIError(f"tenant_access_token missing in response: {data}")
        self._tenant_access_token = token
        self._token_expires_at = time.time() + int(data.get("expire", 7200))
        return token

    def _request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        *,
        query: dict[str, str] | None = None,
        auth: bool = True,
    ) -> dict[str, Any]:
        url = self.base_url + path
        if query:
            url += "?" + urllib.parse.urlencode(query)
        body = None
        headers = {"Content-Type": "application/json; charset=utf-8"}
        if payload is not None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        if auth:
            headers["Authorization"] = f"Bearer {self.tenant_access_token()}"
        request = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                text = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            text = exc.read().decode("utf-8", errors="replace")
            raise FeishuAPIError(f"{method} {path} failed: HTTP {exc.code}: {text}") from exc
        except urllib.error.URLError as exc:
            raise FeishuAPIError(f"{method} {path} failed: {exc}") from exc
        data = json.loads(text) if text else {}
        if data.get("code", 0) != 0:
            raise FeishuAPIError(f"{method} {path} returned code={data.get('code')}: {data}")
        return data

    def send_text(self, open_id: str, text: str) -> dict[str, Any]:
        return self._send_message(open_id, "text", {"text": text})

    def send_interactive_card(self, open_id: str, card: dict[str, Any]) -> dict[str, Any]:
        return self._send_message(open_id, "interactive", card)

    def _send_message(self, open_id: str, msg_type: str, content: dict[str, Any]) -> dict[str, Any]:
        return self._request(
            "POST",
            "/im/v1/messages",
            {
                "receive_id": open_id,
                "msg_type": msg_type,
                "content": json.dumps(content, ensure_ascii=False),
            },
            query={"receive_id_type": "open_id"},
        )

    def _request_multipart(
        self,
        path: str,
        fields: dict[str, str],
        file_field: str,
        file_name: str,
        file_bytes: bytes,
    ) -> dict[str, Any]:
        boundary = f"----feishu{uuid.uuid4().hex}"
        parts: list[bytes] = []
        for key, value in fields.items():
            parts.append(f"--{boundary}\r\n".encode("utf-8"))
            parts.append(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"))
            parts.append(value.encode("utf-8"))
            parts.append(b"\r\n")
        parts.append(f"--{boundary}\r\n".encode("utf-8"))
        parts.append(
            f'Content-Disposition: form-data; name="{file_field}"; filename="{file_name}"\r\n'.encode("utf-8")
        )
        parts.append(b"Content-Type: application/octet-stream\r\n\r\n")
        parts.append(file_bytes)
        parts.append(f"\r\n--{boundary}--\r\n".encode("utf-8"))
        body = b"".join(parts)
        url = self.base_url + path
        headers = {
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Authorization": f"Bearer {self.tenant_access_token()}",
        }
        request = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                text = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            text = exc.read().decode("utf-8", errors="replace")
            raise FeishuAPIError(f"POST {path} failed: HTTP {exc.code}: {text}") from exc
        except urllib.error.URLError as exc:
            raise FeishuAPIError(f"POST {path} failed: {exc}") from exc
        data = json.loads(text) if text else {}
        if data.get("code", 0) != 0:
            raise FeishuAPIError(f"POST {path} returned code={data.get('code')}: {data}")
        return data

    def upload_import_media(self, file_path: Path, file_name: str) -> str:
        file_bytes = file_path.read_bytes()
        fields = {
            "parent_type": "ccm_import_open",
            "file_name": file_name,
            "size": str(len(file_bytes)),
            "extra": json.dumps({"obj_type": "docx", "file_extension": "md"}, ensure_ascii=False),
        }
        data = self._request_multipart(
            "/drive/v1/medias/upload_all", fields, "file", file_name, file_bytes
        )
        token = data.get("data", {}).get("file_token") or data.get("data", {}).get("token")
        if not token:
            raise FeishuAPIError(f"upload_import_media missing file token: {data}")
        return token

    def create_import_task(self, file_token: str, file_name: str, folder_token: str) -> str:
        payload = {
            "file_extension": "md",
            "file_token": file_token,
            "type": "docx",
            "file_name": file_name,
            "point": {"mount_type": 1, "mount_key": folder_token},
        }
        data = self._request("POST", "/drive/v1/import_tasks", payload)
        ticket = data.get("data", {}).get("ticket")
        if not ticket:
            raise FeishuAPIError(f"create_import_task missing ticket: {data}")
        return ticket

    def poll_import_task(self, ticket: str, timeout: int = 60, interval: float = 2.0) -> dict[str, str]:
        deadline = time.time() + timeout
        while True:
            data = self._request("GET", f"/drive/v1/import_tasks/{ticket}")
            result = data.get("data", {}).get("result", {})
            status = result.get("job_status")
            if status == 0:
                token = result.get("token")
                url = result.get("url")
                if not token or not url:
                    raise FeishuAPIError(f"import task succeeded but missing token/url: {result}")
                return {"token": token, "url": url}
            if status in (1, 2):
                if time.time() >= deadline:
                    raise FeishuAPIError(f"import task {ticket} timed out (last status={status})")
                time.sleep(interval)
                continue
            raise FeishuAPIError(
                f"import task {ticket} failed: job_status={status} msg={result.get('job_error_msg')}"
            )

    def set_doc_public_permission(self, token: str, doc_type: str = "docx") -> dict[str, Any]:
        return self._request(
            "PATCH",
            f"/drive/v2/permissions/{token}/public",
            {"link_share_entity": "tenant_readable"},
            query={"type": doc_type},
        )


def report_paths(date: str) -> tuple[Path, Path, Path]:
    report_dir = ROOT / "output" / "daily" / date
    return (
        report_dir / f"game_industry_daily_{date}.md",
        report_dir / "report_page_data.json",
        report_dir,
    )


def _strip_item_number(text: str) -> str:
    return re.sub(r"^\s*\d+[.、)]\s*", "", text or "").strip()


def _first_clause(text: str) -> str:
    """Trim a bullet to its leading clause (drop trailing detail after ；/。)."""
    t = (text or "").strip()
    for sep in ("；", ";"):
        idx = t.find(sep)
        if idx > 0:
            return t[:idx].strip()
    idx = t.find("。")
    if idx > 0:
        return t[:idx].strip()
    return t.rstrip("。").strip()


def _parse_markdown_sections(text: str) -> list[dict[str, Any]]:
    """Parse a daily report markdown into ordered sections.

    Each section: {"name", "items": [{"title", "body", "kind"}]}.
    "kind" is "heading" for `### N. ...` entries (title is the headline) or
    "bullet" for `- ...` entries (title is the one-sentence line itself).
    """
    sections: list[dict[str, Any]] = []
    cur: dict[str, Any] | None = None
    pending: dict[str, str] | None = None

    def flush() -> None:
        nonlocal pending
        if pending is not None and cur is not None:
            cur["items"].append(pending)
        pending = None

    for raw in text.splitlines():
        line = raw.rstrip()
        h2 = re.match(r"^##\s+(.+)$", line)
        if h2:
            flush()
            name = re.sub(r"^[一二三四五六七八九十]+、\s*", "", h2.group(1)).strip()
            cur = {"name": name, "items": []}
            sections.append(cur)
            continue
        if cur is None:
            continue
        h3 = re.match(r"^###\s+(.+)$", line)
        if h3:
            flush()
            pending = {"title": _strip_item_number(h3.group(1)), "body": "", "kind": "heading"}
            continue
        bullet = re.match(r"^[-*]\s+(.+)$", line)
        if bullet and pending is None:
            cur["items"].append({"title": bullet.group(1).strip(), "body": "", "kind": "bullet"})
            continue
        stripped = line.strip()
        if pending is not None and stripped and not stripped.startswith("|"):
            pending["body"] = (pending["body"] + " " + stripped).strip()
    flush()
    return sections


def _sections_from_json(data: dict[str, Any]) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    for item in data.get("items", []):
        if not item.get("title"):
            continue
        section = item.get("section", "") or "其他"
        if section not in groups:
            groups[section] = {"name": section, "items": []}
            order.append(section)
        groups[section]["items"].append(
            {
                "title": item.get("title", "").strip(),
                "body": item.get("body", "").strip(),
                "kind": "heading",
            }
        )
    return [groups[section] for section in order]


def load_report_summary(date: str, max_items: int | None = None) -> dict[str, Any]:
    markdown_path, data_path, report_dir = report_paths(date)
    if not report_dir.exists():
        raise FileNotFoundError(f"Daily report folder not found: {report_dir}")
    if markdown_path.exists():
        text = markdown_path.read_text(encoding="utf-8")
        sections = _parse_markdown_sections(text)
        title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        title = title_match.group(1).strip() if title_match else f"游戏行业日报 | {date}"
    elif data_path.exists():
        data = json.loads(data_path.read_text(encoding="utf-8"))
        sections = _sections_from_json(data)
        title = data.get("title") or f"游戏行业日报 | {date}"
    else:
        raise FileNotFoundError(f"Daily report markdown not found: {markdown_path}")
    return {
        "date": date,
        "title": title,
        "sections": sections,
        "item_count": sum(len(s["items"]) for s in sections),
        "markdown_path": str(markdown_path),
    }


# Section name (markdown 中文标题或 json code) -> (emoji, 卡片显示名, 是否在卡片中略去)
_DROP_KEYWORDS = ("深度", "精选")
_WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def _section_meta(name: str) -> tuple[str, str, bool]:
    codes = {
        "rankings": ("🛒", "Steam 榜单", False),
        "industry": ("📰", "行业新闻", False),
        "ai": ("🤖", "AI 动态", False),
        "release": ("🎮", "新游 / 产品", False),
        "discourse": ("💬", "玩家舆论", False),
        "deep": ("🧠", "深度观察", True),
    }
    if name in codes:
        return codes[name]
    lowered = name.lower()
    if any(k in name for k in _DROP_KEYWORDS):
        return ("🧠", name, True)
    if "榜单" in name or "steam" in lowered:
        return ("🛒", "Steam 榜单", False)
    if "ai" in lowered:
        return ("🤖", "AI 动态", False)
    if any(k in name for k in ("新游", "产品", "发布", "日历")):
        return ("🎮", "新游 / 产品", False)
    if any(k in name for k in ("舆论", "社区")):
        return ("💬", "玩家舆论", False)
    if "行业" in name or "新闻" in name:
        return ("📰", "行业新闻", False)
    return ("📰", name or "其他", False)


def _weekday_label(date: str) -> str:
    try:
        return _WEEKDAYS[datetime.strptime(date, "%Y-%m-%d").weekday()]
    except ValueError:
        return ""


def _item_one_liner(item: dict[str, str]) -> str:
    title = (item.get("title") or "").replace("\n", " ").strip()
    if item.get("kind") == "bullet":
        return _first_clause(title)
    return _strip_item_number(title)


# Steam 榜单里"长线/成熟产品稳定把持榜单"这类总体叙述,卡片不需要(只留新品与异动产品),完整叙述仍保留在 docs。
_STEAM_NOISE = ("长线产品", "榜单主体", "稳定主体", "成熟产品", "把住榜单", "把持榜单")


def _keep_steam_line(line: str) -> bool:
    return not any(keyword in line for keyword in _STEAM_NOISE)


def build_daily_card(
    summary: dict[str, Any], doc_url: str | None = None, per_section: int = 6
) -> dict[str, Any]:
    weekday = _weekday_label(summary["date"])
    header_title = f"🤖 {summary['title']}"
    if weekday:
        header_title += f" {weekday}"

    elements: list[dict[str, Any]] = []
    for section in summary.get("sections", []):
        emoji, display, drop = _section_meta(section.get("name", ""))
        if drop:
            continue
        one_liners = [line for line in (_item_one_liner(it) for it in section.get("items", [])) if line]
        if emoji == "🛒":
            one_liners = [line for line in one_liners if _keep_steam_line(line)]
        if not one_liners:
            continue
        lines = [f"**{emoji} {display}**"]
        lines.extend(f"• {line}" for line in one_liners[:per_section])
        if len(one_liners) > per_section:
            lines.append(f"• …等共 {len(one_liners)} 条，详见完整日报")
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": "\n".join(lines)}})

    if doc_url:
        elements.append({"tag": "hr"})
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "📄 查看完整日报"},
                        "type": "primary",
                        "url": doc_url,
                    }
                ],
            }
        )
    elements.append(
        {
            "tag": "note",
            "elements": [{"tag": "plain_text", "content": "AI 自动整理 · 每条详情见完整日报"}],
        }
    )

    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "template": "blue",
            "title": {"tag": "plain_text", "content": header_title},
        },
        "elements": elements,
    }


def content_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add_date_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--date", required=True, help="Daily report date, e.g. 2026-06-23.")


def main_check_config() -> int:
    load_dotenv()
    names = ["FEISHU_APP_ID", "FEISHU_APP_SECRET"]
    for name in names:
        print(f"{name}: {'ok' if os.environ.get(name) else 'missing'}")
    return 0 if all(os.environ.get(name) for name in names) else 1


if __name__ == "__main__":
    sys.exit(main_check_config())
