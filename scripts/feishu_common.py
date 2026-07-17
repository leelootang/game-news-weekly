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
REPORT_SUBSCRIPTION_KINDS = ("daily", "weekly", "weekend")


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


def subscription_preferences(subscriber: dict[str, Any] | None) -> dict[str, bool]:
    """Return the three report preferences, including a safe legacy fallback.

    Subscriber records written before preference controls only have the
    ``subscribed`` boolean.  Treat an old active subscriber as subscribed to
    all report types, so this rollout never drops an existing recipient.
    """
    if not subscriber:
        return {kind: False for kind in REPORT_SUBSCRIPTION_KINDS}
    stored = subscriber.get("subscriptions")
    if isinstance(stored, dict):
        return {kind: bool(stored.get(kind, False)) for kind in REPORT_SUBSCRIPTION_KINDS}
    enabled = bool(subscriber.get("subscribed"))
    return {kind: enabled for kind in REPORT_SUBSCRIPTION_KINDS}


def get_subscription_preferences(open_id: str) -> dict[str, bool]:
    data = load_subscribers()
    subscriber = next((row for row in data["subscribers"] if row.get("open_id") == open_id), None)
    return subscription_preferences(subscriber)


def set_subscription_preferences(open_id: str, preferences: dict[str, Any]) -> dict[str, Any]:
    """Persist a user's selected report types and keep the legacy total flag.

    An all-false choice is a full unsubscribe.  Creating a record here also
    lets a new user configure their preferences before using the old text
    subscribe command.
    """
    if not open_id:
        raise ValueError("open_id is required")
    normalized = {kind: bool(preferences.get(kind, False)) for kind in REPORT_SUBSCRIPTION_KINDS}
    data = load_subscribers()
    now = utc_now_iso()
    existing = next((row for row in data["subscribers"] if row.get("open_id") == open_id), None)
    if existing is None:
        existing = {
            "open_id": open_id,
            "user_id": None,
            "union_id": None,
            "name": None,
            "created_at": now,
            "last_pushed_date": None,
        }
        data["subscribers"].append(existing)
    existing.update(
        {
            "subscriptions": normalized,
            "subscribed": any(normalized.values()),
            "updated_at": now,
        }
    )
    write_json(SUBSCRIBERS_PATH, data)
    return existing


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
            "subscriptions": {kind: subscribed for kind in REPORT_SUBSCRIPTION_KINDS},
            "updated_at": now,
        }
    )
    write_json(SUBSCRIBERS_PATH, data)
    return existing


def active_subscribers(kind: str | None = None) -> list[dict[str, Any]]:
    """Return active recipients, optionally filtered to a report type."""
    if kind is not None and kind not in REPORT_SUBSCRIPTION_KINDS:
        raise ValueError(f"Unsupported subscription kind: {kind}")
    data = load_subscribers()
    return [
        row
        for row in data["subscribers"]
        if row.get("open_id")
        and row.get("subscribed")
        and (kind is None or subscription_preferences(row)[kind])
    ]


def mark_subscriber_pushed(open_id: str, date: str, kind: str | None = None) -> None:
    """Record that `open_id` already received `date`'s report so a same-day
    re-subscribe is not mistaken for a new subscriber and backfilled twice."""
    data = load_subscribers()
    row = next((r for r in data["subscribers"] if r.get("open_id") == open_id), None)
    if row is None:
        return
    row["last_pushed_date"] = date
    if kind in REPORT_SUBSCRIPTION_KINDS:
        pushed_by_kind = row.setdefault("last_pushed_by_kind", {})
        if isinstance(pushed_by_kind, dict):
            pushed_by_kind[kind] = date
    row["updated_at"] = utc_now_iso()
    write_json(SUBSCRIBERS_PATH, data)


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


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_RANGE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2}$")

# kind -> reader-facing noun used in card labels / fallback titles.
REPORT_NOUN = {"daily": "日报", "weekly": "周报", "weekend": "周末报", "monthly": "月报"}


def resolve_report(identifier: str) -> tuple[str, Path, Path]:
    """Locate a report by its identifier and return (kind, report_dir, md_path).

    A single date (`YYYY-MM-DD`) is a daily report; a range
    (`<start>_to_<end>`) is a weekly / weekend / monthly report — we pick the
    kind by which folder actually holds the markdown."""
    if _DATE_RE.match(identifier):
        report_dir = ROOT / "output" / "daily" / identifier
        return "daily", report_dir, report_dir / f"game_industry_daily_{identifier}.md"
    if _RANGE_RE.match(identifier):
        for kind in ("weekly", "weekend", "monthly"):
            report_dir = ROOT / "output" / kind / identifier
            md_path = report_dir / f"game_industry_{kind}_{identifier}.md"
            if md_path.exists():
                return kind, report_dir, md_path
        # Nothing on disk yet: point at the weekly path so errors are legible.
        report_dir = ROOT / "output" / "weekly" / identifier
        return "weekly", report_dir, report_dir / f"game_industry_weekly_{identifier}.md"
    raise ValueError(f"Unrecognized report identifier: {identifier!r}")


def report_paths(date: str) -> tuple[Path, Path, Path]:
    _, report_dir, md_path = resolve_report(date)
    return md_path, report_dir / "report_page_data.json", report_dir


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
    kind, report_dir, markdown_path = resolve_report(date)
    data_path = report_dir / "report_page_data.json"
    noun = REPORT_NOUN.get(kind, "日报")
    if not report_dir.exists():
        raise FileNotFoundError(f"Report folder not found: {report_dir}")
    if markdown_path.exists():
        text = markdown_path.read_text(encoding="utf-8")
        sections = _parse_markdown_sections(text)
        title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        title = title_match.group(1).strip() if title_match else f"游戏行业{noun} | {date}"
    elif data_path.exists():
        data = json.loads(data_path.read_text(encoding="utf-8"))
        sections = _sections_from_json(data)
        title = data.get("title") or f"游戏行业{noun} | {date}"
    else:
        raise FileNotFoundError(f"Report markdown not found: {markdown_path}")
    return {
        "date": date,
        "kind": kind,
        "noun": noun,
        "title": title,
        "sections": sections,
        "item_count": sum(len(s["items"]) for s in sections),
        "markdown_path": str(markdown_path),
    }


def _citation_md(srcs: list | None) -> str | None:
    """Render a Feishu quote line `> 来源：[标题](url) · ...` for a list of
    [sid, name, url] entries. Returns None when there is nothing to cite."""
    parts: list[str] = []
    for entry in srcs or []:
        sid = entry[0] if len(entry) > 0 else ""
        name = entry[1] if len(entry) > 1 else ""
        url = entry[2] if len(entry) > 2 else ""
        label = str(name or sid or "来源").strip()
        # full-width the brackets so they can't break the markdown link text
        label = label.replace("[", "【").replace("]", "】")
        if re.match(r"https?://", str(url or "")):
            parts.append(f"[{label}]({url})")
        else:
            parts.append(label)
    if not parts:
        return None
    return "> 来源：" + " · ".join(parts)


def build_docx_markdown(date: str) -> Path:
    """Produce a markdown variant for Feishu docx import that appends a
    `> 来源：[标题](url)` quote line after each item. The canonical report
    markdown stays untouched; the augmented file is written under
    `_intermediate/docx_import_<date>.md` and its path is returned.

    Source lookup + title mapping reuse build_report_html so the docx
    citations match the same sources the webpage would show.
    """
    import build_report_html as brh  # reuse parse_sources / sources_for

    md_path, _, report_dir = report_paths(date)
    md = md_path.read_text(encoding="utf-8")
    sources_path = report_dir / "sources_used.md"
    if sources_path.exists():
        title_ids, id_meta = brh.parse_sources(sources_path.read_text(encoding="utf-8"))
    else:
        title_ids, id_meta = {}, {}

    out: list[str] = []
    section_kind: str | None = None
    pending_title: str | None = None   # open news item awaiting its citation

    def flush_news() -> None:
        nonlocal pending_title
        if pending_title:
            line = _citation_md(brh.sources_for(pending_title, title_ids, id_meta))
            if line:
                out.append("")
                out.append(line)
        pending_title = None

    for ln in md.splitlines():
        s = ln.strip()
        h2 = re.match(r"^##\s+(.+)$", s)
        if h2:
            flush_news()
            section_kind = brh.heading_to_section(h2.group(1).strip())
            out.append(ln)
            continue
        h3 = re.match(r"^###\s+(?:\d+\.\s+)?(.+)$", s)
        if h3 and section_kind in ("industry", "ai", "discourse", "deep"):
            flush_news()
            pending_title = h3.group(1).strip()
            out.append(ln)
            continue
        if section_kind == "release" and s.startswith("- "):
            out.append(ln)
            body = s[2:].strip()
            gm = re.search(r"《([^》]+)》", body)
            gname = gm.group(1) if gm else body[:24]
            srcs = brh.sources_for(f"产品日历 - {gname}", title_ids, id_meta) or brh.sources_for(gname, title_ids, id_meta)
            line = _citation_md(srcs)
            if line:
                out.append(line)
            continue
        out.append(ln)

    flush_news()

    augmented = "\n".join(out) + "\n"
    out_path = report_dir / "_intermediate" / f"docx_import_{date}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(augmented, encoding="utf-8")
    return out_path


# Section name (markdown 中文标题或 json code) -> (emoji, 卡片显示名, 是否在卡片中略去)
_DROP_KEYWORDS = ("深度", "精选")
_WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def _section_meta(name: str) -> tuple[str, str, bool]:
    codes = {
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


def _industry_card_detail(body: str) -> str:
    """Return one non-redundant factual extension for an industry-card line."""
    sentences = [
        sentence.strip().rstrip("\u3002\uff01\uff1f")
        for sentence in re.split(r"(?<=[\u3002\uff01\uff1f])", re.sub(r"\s+", " ", body or ""))
        if sentence.strip()
    ]
    factual_markers = re.compile(r"(\d|《|计划|将|新增|测试|上线|发布|收入|玩家|市场|模式|系统)")
    editorial_markers = ("值得", "仍是", "仍需", "需看", "能否", "有待", "取决于")

    def trim_editorial_tail(candidate: str) -> str:
        for marker in editorial_markers:
            position = candidate.find(marker)
            if position > 0:
                cut = max(candidate.rfind("，", 0, position), candidate.rfind("；", 0, position))
                return candidate[:cut].rstrip("，； ") if cut > 0 else ""
        return candidate

    def usable(candidate: str) -> bool:
        return bool(factual_markers.search(candidate)) and not any(
            marker in candidate for marker in editorial_markers
        )

    # Industry item titles already carry the lead event. Select the strongest
    # non-lead clause with a concrete product, timing, market, or mechanism
    # fact; never append a generic reporter conclusion just to make it longer.
    clauses = [
        clause.strip()
        for sentence in sentences[1:]
        for clause in re.split(r"[\uff1b;]", sentence)
        if clause.strip()
    ]

    def detail_score(candidate: str) -> int:
        weights = {
            r"《": 6,
            r"\d": 5,
            r"计划|将": 4,
            r"测试|上线|发布": 3,
            r"收入|玩家|市场": 3,
            r"模式|系统": 2,
        }
        return sum(weight for pattern, weight in weights.items() if re.search(pattern, candidate))

    usable_clauses = [trim_editorial_tail(candidate) for candidate in clauses]
    usable_clauses = [candidate for candidate in usable_clauses if usable(candidate)]
    if not usable_clauses and sentences:
        lead_clauses = [
            clause.strip()
            for clause in re.split(r"[\uff1b;]", sentences[0])[1:]
            if clause.strip()
        ]
        usable_clauses = [trim_editorial_tail(candidate) for candidate in lead_clauses]
        usable_clauses = [candidate for candidate in usable_clauses if usable(candidate)]
    detail = max(usable_clauses, key=detail_score, default="")
    if not detail:
        return ""
    if len(detail) <= 88:
        return detail
    breakpoint = max(detail.rfind(mark, 0, 88) for mark in ("，", "；", "、"))
    return detail[: breakpoint if breakpoint >= 36 else 85].rstrip("，、；： ") + "…"


def _item_one_liner(item: dict[str, str], *, industry_detail: bool = False) -> str:
    title = (item.get("title") or "").replace("\n", " ").strip()
    if item.get("kind") == "bullet":
        return _first_clause(title)
    title = _strip_item_number(title)
    detail = _industry_card_detail(item.get("body", "")) if industry_detail else ""
    return f"{title}，{detail}" if detail else title


def _emphasize(line: str) -> str:
    """Bold the scannable key phrase of a card line so readers get the point
    fast. Prefer a leading 《产品名》 title; else bold the lead clause before
    the first Chinese comma; else bold a short whole line. Never split inside
    a 《...》 (titles can contain ：), so we bold the bracketed span as a unit."""
    m = re.search(r"《[^》]+》", line)
    if m and m.start() <= 24 and (m.end() - m.start()) <= 26:
        s, e = m.start(), m.end()
        return f"{line[:s]}**{line[s:e]}**{line[e:]}"
    idx = -1
    for sep in ("，", ","):
        pos = line.find(sep)
        if pos > 0 and (idx < 0 or pos < idx):
            idx = pos
    if 4 <= idx <= 26:
        return f"**{line[:idx]}**{line[idx:]}"
    if len(line) <= 26:
        return f"**{line}**"
    return line


def build_daily_card(
    summary: dict[str, Any], doc_url: str | None = None, per_section: int = 6
) -> dict[str, Any]:
    noun = summary.get("noun", "日报")
    weekday = _weekday_label(summary["date"])
    header_title = f"🤖 {summary['title']}"
    if weekday:
        header_title += f" {weekday}"

    elements: list[dict[str, Any]] = []
    for section in summary.get("sections", []):
        emoji, display, drop = _section_meta(section.get("name", ""))
        if drop:
            continue
        industry_detail = display == "行业新闻"
        one_liners = [
            line
            for line in (
                _item_one_liner(item, industry_detail=industry_detail)
                for item in section.get("items", [])
            )
            if line
        ]
        if not one_liners:
            continue
        lines = [f"**{emoji} {display}**"]
        lines.extend(f"• {_emphasize(line)}" for line in one_liners[:per_section])
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": "\n".join(lines)}})

    if doc_url:
        elements.append({"tag": "hr"})
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": f"📄 查看完整{noun}"},
                        "type": "primary",
                        "url": doc_url,
                    }
                ],
            }
        )
    elements.append(
        {
            "tag": "note",
            "elements": [{"tag": "plain_text", "content": f"AI 自动整理 · 每条详情见完整{noun}"}],
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


def build_deep_observation_card(
    summary: dict[str, Any],
    doc_url: str | None = None,
    source_url: str | None = None,
    max_items: int = 1,
) -> dict[str, Any] | None:
    """Build the standalone deep-observation card paired with a report card.

    Keep this separate from ``build_daily_card``: the report card is a scan of
    all sections, while this card gives one selected observation enough room
    for a compact observation-and-analysis read.
    """
    items: list[dict[str, str]] = []
    for section in summary.get("sections", []):
        _emoji, _display, is_deep = _section_meta(section.get("name", ""))
        if is_deep:
            items.extend(section.get("items", []))
    if not items:
        return None

    elements: list[dict[str, Any]] = []
    for item in items[:max_items]:
        title = _strip_item_number(item.get("title", ""))
        body = re.sub(r"\s+", " ", item.get("body", "")).strip()
        if len(body) > 900:
            body = body[:897].rstrip("，、；： ") + "……"
        # Cards intentionally keep the body compact, but the two analytical
        # layers need visible hierarchy.  Do not let whitespace normalization
        # flatten `观察：` / `分析：` into ordinary inline prose.
        body = re.sub(r"\*{0,2}(观察：|分析：)\*{0,2}", r"**\1**", body)
        body = re.sub(r"(?<!^)(\*\*(?:观察|分析)：\*\*)", r"\n\n\1", body)
        # The 分析 layer often carries an ①②③… enumeration crammed into one
        # block; break each point onto its own line so it reads as a list.
        body = re.sub(r"\s*([①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮])", r"\n\1", body)
        body = re.sub(r"[ \t]+\n", "\n", body)
        body = re.sub(r"[ \t]+\n\n", "\n\n", body)
        content = f"**{title}**"
        if body:
            content += f"\n\n{body}"
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": content}})

    actions: list[dict[str, Any]] = []
    if doc_url:
        noun = summary.get("noun") or "周报"
        actions.append(
            {
                "tag": "button",
                "text": {"tag": "plain_text", "content": f"查看{noun}飞书文档"},
                "type": "primary",
                "url": doc_url,
            }
        )
    if source_url:
        actions.append(
            {
                "tag": "button",
                "text": {"tag": "plain_text", "content": "查看原文链接"},
                "type": "default",
                "url": source_url,
            }
        )
    if actions:
        elements.append({"tag": "hr"})
        elements.append(
            {
                "tag": "action",
                "actions": actions,
            }
        )
    elements.append(
        {
            "tag": "note",
            "elements": [
                {"tag": "plain_text", "content": "独立深度观察 · 观察与分析分层呈现"}
            ],
        }
    )
    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "template": "purple",
            "title": {"tag": "plain_text", "content": f"🧠 {summary['title']}｜深度观察"},
        },
        "elements": elements,
    }


def _deep_item_source_url(summary: dict[str, Any], item: dict[str, str]) -> str | None:
    """Find the first auditable source URL for one deep-observation item."""
    markdown_path = Path(str(summary.get("markdown_path") or ""))
    sources_path = markdown_path.parent / "sources_used.md"
    if not sources_path.exists():
        return None
    try:
        import build_report_html as brh

        title_ids, id_meta = brh.parse_sources(sources_path.read_text(encoding="utf-8"))
        title = _strip_item_number(item.get("title", ""))
        for _source_id, _name, url in brh.sources_for(title, title_ids, id_meta):
            if isinstance(url, str) and re.match(r"https?://", url):
                return url
    except (ImportError, OSError, ValueError):
        return None
    return None


def _designated_deep_card_title(summary: dict[str, Any]) -> str | None:
    """Read the human-designated deep-observation card title, if any.

    The Thursday human-curation step decides which single deep observation
    becomes a card; the Friday generation writes that title to
    ``deep_card_choice.txt`` in the report directory. Absent file → no card is
    pushed (the deep card is human-gated, there is no auto-fallback).
    """
    markdown_path = summary.get("markdown_path")
    if not markdown_path:
        return None
    choice_path = Path(str(markdown_path)).parent / "deep_card_choice.txt"
    try:
        title = choice_path.read_text(encoding="utf-8").strip()
    except OSError:
        return None
    return _strip_item_number(title) or None


def build_deep_observation_cards(
    summary: dict[str, Any], doc_url: str | None = None, max_cards: int = 1
) -> list[dict[str, Any]]:
    """Build the single human-designated weekly deep-observation card.

    The report body may carry two or three deep-observation items, but only the
    one the user designated on Thursday (recorded in ``deep_card_choice.txt``)
    becomes a card. If no designation exists, no deep card is pushed.
    """
    if not doc_url:
        return []
    chosen_title = _designated_deep_card_title(summary)
    if not chosen_title:
        return []

    items: list[dict[str, str]] = []
    deep_name = "深度观察"
    for section in summary.get("sections", []):
        _emoji, display, is_deep = _section_meta(section.get("name", ""))
        if is_deep:
            deep_name = section.get("name") or display
            items.extend(section.get("items", []))

    cards: list[dict[str, Any]] = []
    for item in items:
        if _strip_item_number(item.get("title", "")) != chosen_title:
            continue
        source_url = _deep_item_source_url(summary, item)
        if not source_url:
            continue
        card_summary = {**summary, "sections": [{"name": deep_name, "items": [item]}]}
        card = build_deep_observation_card(
            card_summary,
            doc_url=doc_url,
            source_url=source_url,
            max_items=1,
        )
        if card:
            cards.append(card)
        if len(cards) >= max_cards:
            break
    return cards


def content_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add_date_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--date",
        required=True,
        help="Report identifier: a date for daily (2026-06-23) or a range for "
        "weekly/weekend (2026-06-20_to_2026-06-26).",
    )


def main_check_config() -> int:
    load_dotenv()
    names = ["FEISHU_APP_ID", "FEISHU_APP_SECRET"]
    for name in names:
        print(f"{name}: {'ok' if os.environ.get(name) else 'missing'}")
    return 0 if all(os.environ.get(name) for name in names) else 1


if __name__ == "__main__":
    sys.exit(main_check_config())
