#!/usr/bin/env python3
"""Extract every PDF in a report window into JSONL for auditable report writing."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from pypdf import PdfReader
except Exception as exc:  # pragma: no cover - environment guard
    PdfReader = None
    PYPDF_IMPORT_ERROR = exc
else:
    PYPDF_IMPORT_ERROR = None


DEFAULT_SECTIONS = [
    "industry_news",
    "ai_trends",
    "release_calendar",
    "community_discourse",
    "deep_analysis",
]
ARTICLE_JSONL_NAME = "articles.jsonl"
BODY_STATUSES = {"full", "short_official", "snippet", "empty"}
NEW_GAME_LAUNCH = re.compile(r"首发|正式上线|全球上线|上线|公测|发售|正式发布|全球发布|上市|开服", re.IGNORECASE)
NEW_GAME_TEST = re.compile(r"抢先体验(?:测试)?|不删档测试|不限量测试|计费删档内测|付费删档测试|删档测试|限量测试|封闭测试|海外(?:封闭)?测试|海外封测|封测|终测|连接测试|测试资格|首测|内测|付费测试|公开测试|开启.{0,8}测试|开测|[AB]测|Beta(?:测试)?", re.IGNORECASE)
NEW_GAME_PRELOAD = re.compile(r"预下载", re.IGNORECASE)
NEW_GAME_REVEAL = re.compile(r"首曝|首次曝光|首次公开(?!测试|[AB]测|Beta)(?:实机|演示)?|正式公布新作|新作正式公布|官宣新作|新作官宣|立项公开", re.IGNORECASE)
NEW_GAME_SCHEDULE = re.compile(r"定档|公布发售日|发售日公布|确定发售日|延期|跳票", re.IGNORECASE)
OLD_MAJOR_SIGNAL = re.compile(r"二次\s*(?:OB|公测)|重启|回归|重新上线|跨平台上线|登陆(?:PC|Steam|主机|PS5|Xbox|Switch)|重大版本|重大模式|核心(?:玩法|系统).{0,8}(?:更新|重做)", re.IGNORECASE)
ROUTINE_OLD_SIGNAL = re.compile(r"普通版本|常规版本|\d+\.\d+版?|资料片|赛季|联动|活动|周年|DLC|补丁|皮肤|折扣|签到", re.IGNORECASE)
HISTORICAL_LAUNCH = re.compile(r"上线(?:后|首周|首月|[一二三四五六七八九十\d]+年)|发售(?:后|首周|首月)", re.IGNORECASE)
CALENDAR_DATE = re.compile(
    r"(?:20\d{2}年)?\d{1,2}月\d{1,2}日|(?:20\d{2}年)?\d{1,2}月(?!\d)|"
    r"(?:20\d{2}年|今年|明年)(?:春季|夏季|秋季|冬季|上半年|下半年|Q[1-4]|第[一二三四]季度)",
    re.IGNORECASE,
)
CURRENT_DATE_WORD = re.compile(r"今日|今天|昨日|昨天")
FUTURE_SCHEDULE_WORD = re.compile(r"将于|将在|计划于|计划在|预计于|预计在|定于|即将|定档")
HISTORICAL_CONTEXT = re.compile(
    r"去年|前年|此前|曾经|早在|过去|当时|回顾|上线后|发售后|公测后|测试后",
    re.IGNORECASE,
)
RECOMMENDATION_SECTION = re.compile(
    r"(?:^|[。！？!?\n])\s*(?:相关推荐|相关阅读|延伸阅读|猜你喜欢|更多推荐)\s*(?:[:：]|\n)",
    re.IGNORECASE,
)
ANAPHOR_SUBJECT = re.compile(
    r"^(?:而|此外|同时|随后|届时|目前|其中|官方)?\s*"
    r"(?:该作|本作|该游戏|本游戏|这款游戏|游戏|国服|国际版|海外版|国际服|海外服)"
)
SELECTION_URL = re.compile(r"https?://[^\s>]+")
FOCUS_COMPANY_BONUS = 3
FOCUS_COMPANY_INVESTMENT_BONUS = 2
INVESTMENT_RELATION = re.compile(
    r"投资|参投|持股|战略入股|战略投资|领投|跟投|被投|投资方|股东",
    re.IGNORECASE,
)
DIRECT_RELATION = re.compile(
    r"自研|自主研发|研发|开发|发行|运营|旗下(?:工作室|团队|子公司)|"
    r"内部工作室|工作室群|Publisher\s*:|Developer\s*:|发行商\s*:|开发商\s*:",
    re.IGNORECASE,
)
FOCUS_COMPANY_PATTERNS = {
    "腾讯": re.compile(r"腾讯(?:游戏)?|天美(?:工作室群)?|光子(?:工作室群)?", re.IGNORECASE),
    "网易": re.compile(r"网易(?:游戏)?", re.IGNORECASE),
    "米哈游": re.compile(r"米哈游|HoYoverse", re.IGNORECASE),
    "莉莉丝": re.compile(r"莉莉丝|Lilith", re.IGNORECASE),
    "哔哩哔哩": re.compile(r"哔哩哔哩|Publisher:\s*BILIBILI", re.IGNORECASE),
    "三七互娱": re.compile(r"三七互娱|三七游戏|37手游|37\s*Games?", re.IGNORECASE),
    "Garena": re.compile(r"\bGarena\b", re.IGNORECASE),
    "Supercell": re.compile(r"\bSupercell(?:\s+Oy)?\b|超级细胞", re.IGNORECASE),
    "Riot Games": re.compile(r"\bRiot\s+Games?\b|拳头(?:游戏|公司)?", re.IGNORECASE),
    "巨人网络": re.compile(r"巨人网络", re.IGNORECASE),
    "鹰角网络": re.compile(r"鹰角(?:网络)?|Hypergryph", re.IGNORECASE),
    "叠纸游戏": re.compile(r"叠纸(?:游戏)?|Papergames", re.IGNORECASE),
    "世纪华通/点点互动": re.compile(r"世纪华通|点点互动|Century\s+Games", re.IGNORECASE),
}


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def iter_dates(start: dt.date, end: dt.date) -> list[dt.date]:
    days: list[dt.date] = []
    cur = start
    while cur <= end:
        days.append(cur)
        cur += dt.timedelta(days=1)
    return days


def load_manifest_index(workspace: Path, dates: list[dt.date]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for day in dates:
        for run_dir in [
            workspace / "news_data" / "_collector_runs" / day.isoformat(),
            workspace / "news_pdfs" / "_collector_runs" / day.isoformat(),
        ]:
            if not run_dir.exists():
                continue
            for manifest in run_dir.glob("*_manifest.json"):
                try:
                    data = json.loads(manifest.read_text(encoding="utf-8"))
                except Exception:
                    continue
                for item in data.get("items", {}).values():
                    if not isinstance(item, dict):
                        continue
                    filename = item.get("file")
                    if isinstance(filename, str) and filename:
                        index[filename] = item
                        index[Path(filename).name] = item
    return index


def default_output(workspace: Path, report_type: str, start: dt.date, end: dt.date) -> Path:
    if report_type == "daily" and start == end:
        return workspace / "output" / "daily" / start.isoformat() / "_intermediate" / "report_inputs.jsonl"
    if report_type == "weekly":
        return workspace / "output" / "weekly" / f"{start.isoformat()}_to_{end.isoformat()}" / "_intermediate" / "report_inputs.jsonl"
    if report_type == "monthly":
        return workspace / "output" / "monthly" / start.strftime("%Y-%m") / "_intermediate" / "report_inputs.jsonl"
    return workspace / "output" / "reports" / f"{start.isoformat()}_to_{end.isoformat()}" / "_intermediate" / "report_inputs.jsonl"


def sha1_file(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_pdf(path: Path) -> tuple[str, int, str]:
    if PdfReader is None:
        return "", 0, f"pypdf_import_failed: {PYPDF_IMPORT_ERROR}"
    try:
        reader = PdfReader(str(path))
        parts = []
        for page in reader.pages:
            parts.append(page.extract_text() or "")
        return "\n".join(parts).strip(), len(reader.pages), "ok"
    except Exception as exc:
        return "", 0, f"extract_failed: {exc}"


def infer_title(path: Path, metadata: dict[str, Any] | None) -> str:
    if metadata:
        title = metadata.get("title")
        if isinstance(title, str) and title.strip():
            return title.strip()
    stem = path.stem
    parts = stem.split("_")
    if len(parts) >= 5:
        return parts[-1]
    return stem


def normalize_quality(row: dict[str, Any], text: str) -> tuple[str, str]:
    """Normalize legacy collectors into a transport/body quality contract.

    ``fetch_status`` is strictly transport success/failure.  ``body_status``
    describes whether the record is suitable as primary report evidence.
    """
    raw_fetch = str(row.get("fetch_status") or "ok").strip().lower()
    fetch_status = "failed" if raw_fetch in {"failed", "error"} or raw_fetch.startswith("extract_failed") else "ok"
    declared = str(row.get("body_status") or "").strip().lower()
    if declared in BODY_STATUSES:
        body_status = declared
    elif not text:
        body_status = "empty"
    elif raw_fetch == "partial":
        body_status = "snippet"
    else:
        body_status = "full"
    if fetch_status == "failed" and not text:
        body_status = "empty"
    return fetch_status, body_status


def collect_records(
    workspace: Path,
    dates: list[dt.date],
    sections: list[str],
) -> list[dict[str, Any]]:
    manifest_index = load_manifest_index(workspace, dates)
    records: list[dict[str, Any]] = []
    serial = 1
    seen_keys: set[tuple[str, str, str]] = set()

    for day in dates:
        day_str = day.isoformat()
        for section in sections:
            data_file = workspace / "news_data" / section / day_str / ARTICLE_JSONL_NAME
            if data_file.exists():
                for line in data_file.read_text(encoding="utf-8-sig").splitlines():
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    text = str(row.get("text") or "").strip()
                    title = str(row.get("title") or "").strip()
                    key_value = str(row.get("url") or title or row.get("id") or "")
                    record_key = (section, day_str, key_value)
                    if key_value and record_key in seen_keys:
                        continue
                    if key_value:
                        seen_keys.add(record_key)
                    fetch_status, body_status = normalize_quality(row, text)
                    record = {
                        "source_id": f"S{serial:04d}",
                        "date": day_str,
                        "section": section,
                        "title": title,
                        "url": row.get("url"),
                        "source": row.get("source"),
                        "source_key": row.get("source_key"),
                        "published_at": row.get("published_at"),
                        "path": str(data_file.resolve()),
                        "filename": data_file.name,
                        "sha1": row.get("content_sha1") or hashlib.sha1(text.encode("utf-8")).hexdigest(),
                        "page_count": 0,
                        "fetch_status": fetch_status,
                        "body_status": body_status,
                        "extract_status": fetch_status,  # legacy alias; use the two fields above.
                        "text_chars": len(text),
                        "text": text,
                    }
                    records.append(record)
                    serial += 1

            pdf_folders = [
                workspace / "news_data" / section / day_str,
                workspace / "news_pdfs" / section / day_str,
            ]
            pdfs = []
            for folder in pdf_folders:
                if folder.exists():
                    pdfs.extend(sorted(folder.glob("*.pdf")))
            for pdf in pdfs:
                meta = manifest_index.get(pdf.name)
                title = infer_title(pdf, meta)
                key_value = str((meta.get("url") if meta else "") or title)
                record_key = (section, day_str, key_value)
                if key_value and record_key in seen_keys:
                    continue
                if key_value:
                    seen_keys.add(record_key)
                text, page_count, status = extract_pdf(pdf)
                fetch_status, body_status = normalize_quality({"fetch_status": status}, text)
                record = {
                    "source_id": f"S{serial:04d}",
                    "date": day_str,
                    "section": section,
                    "title": title,
                    "url": meta.get("url") if meta else None,
                    "source": meta.get("source") if meta else None,
                    "source_key": meta.get("source_key") if meta else None,
                    "published_at": meta.get("published_at") if meta else None,
                    "path": str(pdf.resolve()),
                    "filename": pdf.name,
                    "sha1": sha1_file(pdf),
                    "page_count": page_count,
                    "fetch_status": fetch_status,
                    "body_status": body_status,
                    "extract_status": fetch_status,  # legacy alias; use the two fields above.
                    "text_chars": len(text),
                    "text": text,
                }
                records.append(record)
                serial += 1
    return records


def augment_deep_selection_records(
    workspace: Path,
    records: list[dict[str, Any]],
    selection_path: Path,
    report_start: dt.date,
    report_end: dt.date,
    sections: list[str],
) -> list[dict[str, Any]]:
    """Append selected deep sources outside the normal weekly window.

    Thursday selection scans Thu–Wed while the Friday weekly report scans
    Fri–Thu.  Only selected-source records from the one-day-earlier candidate
    window are supplemented, and they are reclassified as deep-only inputs so
    they cannot affect other weekly sections or the release-calendar queue.
    """
    expected_name = f"{report_start.isoformat()}_to_{report_end.isoformat()}_selection.md"
    if selection_path.name != expected_name:
        raise ValueError(f"deep selection filename must match target weekly ID: {selection_path.name} != {expected_name}")
    text = selection_path.read_text(encoding="utf-8")
    candidate_window = re.search(r"(?m)^-\s*候选数据窗口:\s*(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})\s*$", text)
    target_window = re.search(r"(?m)^-\s*目标周报窗口:\s*(\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2})\s*$", text)
    if not candidate_window or not target_window:
        raise ValueError("deep selection must declare 候选数据窗口 and 目标周报窗口")
    expected_target = f"{report_start.isoformat()}_to_{report_end.isoformat()}"
    if target_window.group(1) != expected_target:
        raise ValueError(f"deep selection target window mismatch: {target_window.group(1)} != {expected_target}")
    candidate_start = parse_date(candidate_window.group(1))
    candidate_end = parse_date(candidate_window.group(2))
    if candidate_start != report_start - dt.timedelta(days=1) or candidate_end != report_end - dt.timedelta(days=1):
        raise ValueError("deep selection candidate window must be exactly one day earlier than the target weekly window")
    selected_match = re.search(
        r"(?ms)^##\s+用户选择进入周报的条目\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        text,
    )
    if not selected_match:
        raise ValueError("deep selection has no 用户选择进入周报的条目 section")
    selected_urls = {
        url.rstrip(".,，。")
        for url in SELECTION_URL.findall(selected_match.group("body"))
    }
    if not selected_urls:
        raise ValueError("deep selection selected items have no source URLs")

    existing_urls = {str(record.get("url") or "") for record in records}
    candidate_records = collect_records(workspace, iter_dates(candidate_start, candidate_end), sections)
    by_url: dict[str, dict[str, Any]] = {}
    for record in candidate_records:
        url = str(record.get("url") or "")
        if url in selected_urls and url not in by_url:
            by_url[url] = record
    missing_urls = sorted(selected_urls - set(by_url))
    if missing_urls:
        raise ValueError(f"selected deep source URLs are absent from candidate-window inputs: {missing_urls}")

    augmented = list(records)
    for url in sorted(selected_urls):
        if url in existing_urls:
            continue
        record = dict(by_url[url])
        record["source_id"] = f"S{len(augmented) + 1:04d}"
        record["original_section"] = record.get("section")
        record["section"] = "deep_analysis"
        record["deep_selection_supplement"] = True
        augmented.append(record)
    return augmented


def _release_game_name(rec: dict[str, Any]) -> str:
    """Best-effort game name from a release_calendar record."""
    text = str(rec.get("text") or "")
    m = re.search(r"^Game:\s*(.+)$", text, flags=re.M)
    if m:
        return _normalize_product_name(m.group(1))
    title = str(rec.get("title") or "").strip()
    title = re.sub(r"\s*[-–—]\s*Gematsu\s*$", "", title)
    # CN calendar pattern: "游戏名 - 公测/上线/测试/资料片/新版本..."
    if " - " in title:
        return _normalize_product_name(title.split(" - ")[0])
    # EN gematsu pattern: "<Name> for ... / launches / delayed / coming ..."
    head = re.split(r"\s+(?:for|launches?|delayed|coming|gets|adds|now)\b", title, maxsplit=1)[0].strip()
    return _normalize_product_name(head or title)


def _normalize_product_name(value: str) -> str:
    value = value.strip().replace(":", "：")
    value = re.sub(r"[（(]官服[）)]", "", value, flags=re.I)
    value = re.sub(r"[（(](?:TapTap)?测试版[）)]$", "", value, flags=re.I)
    value = re.sub(r"(?:体验服|测试服)$", "", value)
    value = re.sub(r"\s+(?:招募中|预约中|已开服)$", "", value)
    value = re.sub(r"\s*-\s*[^-]{1,40}新作$", "", value)
    value = re.sub(r"\s*-\s*预下载(?:[（(]官服[）)])?$", "", value, flags=re.I)
    value = re.sub(r"\s*-\s*\d{1,2}月\d{1,2}日(?:正式)?上线$", "", value)
    value = re.sub(r"\s*-\s*正版[^-]{1,30}$", "", value)
    return value.strip()


def _event_date(rec: dict[str, Any]) -> str:
    text = str(rec.get("text") or "")
    match = re.search(r"^Event date:\s*(\d{4}-\d{2}-\d{2})", text, flags=re.M)
    if match:
        return match.group(1)
    if rec.get("section") == "industry_news":
        product = _industry_product(rec)
        product_positions = [
            match.start() for match in re.finditer(re.escape(product), text)
        ] if product else []
        date_matches = list(re.finditer(r"(\d{1,2})月(\d{1,2})日", text))
        if product_positions and date_matches:
            nearest = min(
                date_matches,
                key=lambda date_match: min(
                    abs(date_match.start() - product_position)
                    for product_position in product_positions
                ),
            )
            record_year = str(rec.get("date") or "")[:4]
            if len(record_year) == 4:
                return f"{record_year}-{int(nearest.group(1)):02d}-{int(nearest.group(2)):02d}"
    return str(rec.get("date") or "")


def _industry_product(rec: dict[str, Any]) -> str:
    title = str(rec.get("title") or "")
    match = re.search(r"《([^》]+)》", title)
    if not match:
        lead = str(rec.get("text") or "")[:600]
        match = re.search(r"《([^》]+)》", lead)
    return _normalize_product_name(match.group(1)) if match else ""


def _focus_company_relationships(rec: dict[str, Any], product: str) -> dict[str, str]:
    """Return direct/investment relationships supported by product-local text."""
    text = str(rec.get("text") or "")
    if rec.get("section") == "industry_news":
        contexts = [
            sentence
            for sentence in re.split(r"(?<=[。！？])|\n+", text)
            if product and product in sentence
        ]
        title = str(rec.get("title") or "")
        if product and product in title:
            contexts.insert(0, title)
    else:
        contexts = [str(rec.get("title") or ""), *text.splitlines()]

    relationships: dict[str, str] = {}
    for context in contexts:
        if not context.strip():
            continue
        structured = bool(re.search(r"Publisher\s*:|Developer\s*:|发行商\s*:|开发商\s*:", context, re.I))
        for company, pattern in FOCUS_COMPANY_PATTERNS.items():
            if not pattern.search(context):
                continue
            if INVESTMENT_RELATION.search(context):
                relationship = "investment"
            elif DIRECT_RELATION.search(context) or structured or (product and product in context):
                relationship = "direct"
            else:
                continue
            if relationship == "direct" or company not in relationships:
                relationships[company] = relationship
    return relationships


def _source_fingerprint(rec: dict[str, Any]) -> str:
    return str(rec.get("sha1") or rec.get("url") or rec.get("source_id") or "")


def _dated_future_signal(haystack: str, record_date: str) -> tuple[str, str, int] | None:
    """Classify a future launch/test date as a schedule announcement."""
    date_matches = list(CALENDAR_DATE.finditer(haystack))
    if not date_matches:
        return None
    has_future_word = bool(FUTURE_SCHEDULE_WORD.search(haystack))
    record_day = parse_date(record_date) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", record_date or "") else None
    has_future_date = False
    for match in date_matches:
        raw = match.group(0)
        absolute = re.fullmatch(r"(?:(20\d{2})年)?(\d{1,2})月(\d{1,2})日", raw)
        if absolute and record_day:
            year = int(absolute.group(1) or record_day.year)
            try:
                mentioned = dt.date(year, int(absolute.group(2)), int(absolute.group(3)))
            except ValueError:
                continue
            if mentioned > record_day:
                has_future_date = True
                break
        elif re.search(r"明年|冬季|春季|夏季|秋季|上半年|下半年|Q[1-4]|第[一二三四]季度", raw, re.I):
            has_future_date = True
            break
        elif record_day:
            month_only = re.fullmatch(r"(?:(20\d{2})年)?(\d{1,2})月", raw)
            if month_only:
                year = int(month_only.group(1) or record_day.year)
                if (year, int(month_only.group(2))) > (record_day.year, record_day.month):
                    has_future_date = True
                    break
    if not has_future_word and not has_future_date:
        return None
    date_label = date_matches[-1].group(0)
    if NEW_GAME_TEST.search(haystack):
        return "new_game_schedule", f"{date_label}测试定档", 2
    if NEW_GAME_LAUNCH.search(haystack):
        return "new_game_schedule", f"{date_label}上线定档", 2
    return None


def _sentence_units(text: str) -> list[str]:
    marker = RECOMMENDATION_SECTION.search(text)
    if marker:
        text = text[:marker.start()]
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[。！？!?])|\n+", text)
        if sentence.strip()
    ]


def _sentence_products(sentence: str) -> list[str]:
    products = []
    for raw in re.findall(r"《([^》]{2,100})》", sentence):
        product = _normalize_product_name(raw)
        if product and product not in products:
            products.append(product)
    return products


def _has_calendar_date(text: str) -> bool:
    return bool(CALENDAR_DATE.search(text) or CURRENT_DATE_WORD.search(text))


def _announcement_event_date(context: str, record_date: str) -> str:
    """Prefer an explicit current/past-near announcement date over crawl date."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", record_date or ""):
        return record_date
    record_day = parse_date(record_date)
    candidates = []
    for match in re.finditer(r"(?:(20\d{2})年)?(\d{1,2})月(\d{1,2})日", context):
        year = int(match.group(1) or record_day.year)
        try:
            mentioned = dt.date(year, int(match.group(2)), int(match.group(3)))
        except ValueError:
            continue
        if dt.timedelta(days=0) <= record_day - mentioned <= dt.timedelta(days=7):
            candidates.append(mentioned)
    return max(candidates).isoformat() if candidates else record_date


def _industry_calendar_mentions(rec: dict[str, Any]) -> list[dict[str, Any]]:
    """Recall unambiguous product/date/event mentions from a full industry article."""
    title = str(rec.get("title") or "").strip()
    body = str(rec.get("text") or "")
    units = ([title] if title else []) + _sentence_units(body)
    mentions: list[dict[str, Any]] = []

    def add(product: str, context: str, *, title_context: bool = False) -> None:
        if HISTORICAL_CONTEXT.search(context):
            return
        if not title_context and not _has_calendar_date(context):
            return
        probe = {
            **rec,
            "section": "release_calendar",
            "title": context,
            "text": context,
        }
        signal = _calendar_signal(probe)
        if not signal:
            return
        record_date = str(rec.get("date") or "")
        event_date = _announcement_event_date(context, record_date)
        if signal[0] not in {"new_game_schedule", "new_game_first_reveal"}:
            absolute_dates = list(re.finditer(r"(?:(20\d{2})年)?(\d{1,2})月(\d{1,2})日", context))
            if absolute_dates:
                match = absolute_dates[-1]
                year = match.group(1) or event_date[:4]
                if len(year) == 4:
                    event_date = f"{year}-{int(match.group(2)):02d}-{int(match.group(3)):02d}"
        mentions.append({
            "product": product,
            "signal": signal,
            "event_date": event_date,
            "context": context,
        })

    for index, sentence in enumerate(units):
        products = _sentence_products(sentence)
        if len(products) == 1:
            same_sentence_signal = _calendar_signal({
                **rec,
                "section": "release_calendar",
                "title": sentence,
                "text": sentence,
            })
            if same_sentence_signal and (index == 0 or _has_calendar_date(sentence)):
                add(products[0], sentence, title_context=index == 0)
                continue

            if index + 1 < len(units):
                next_sentence = units[index + 1]
                if (
                    not _sentence_products(next_sentence)
                    and ANAPHOR_SUBJECT.search(next_sentence)
                    and _has_calendar_date(f"{sentence} {next_sentence}")
                ):
                    add(products[0], f"{sentence} {next_sentence}", title_context=index == 0)
        elif len(products) > 1:
            # A roundup sentence may still contain safe product-local clauses.
            # Each clause must independently contain one product, event and date;
            # shared or cross-clause ownership remains excluded.
            for clause in re.split(r"[，；;、]", sentence):
                clause_products = _sentence_products(clause)
                if len(clause_products) == 1 and _has_calendar_date(clause):
                    add(clause_products[0], clause, title_context=index == 0)

    unique_by_signal: dict[tuple[str, str], dict[str, Any]] = {}
    for mention in mentions:
        key = (mention["product"], mention["signal"][0])
        current = unique_by_signal.get(key)
        if current is None or mention["event_date"] < current["event_date"]:
            unique_by_signal[key] = mention
    return list(unique_by_signal.values())


def _calendar_signal(rec: dict[str, Any]) -> tuple[str, str, int] | None:
    """Return a normalized calendar event and its event-type factor."""
    title = str(rec.get("title") or "")
    text = str(rec.get("text") or "")
    if rec["section"] == "industry_news":
        # Always consider the title.  Add only dated/current-time lead sentences
        # that name a product, so a current test below an editorial headline is
        # recalled without pulling undated historical launches from the article.
        lead_sentences = re.split(r"(?<=[。！？])|\n+", text[:1200])
        current_sentences = [
            sentence
            for sentence in lead_sentences
            if "《" in sentence
            and re.search(r"\d{1,2}月\d{1,2}日|今日|今天|昨日|昨天", sentence)
        ]
        haystack = "\n".join([title, *current_sentences])
    else:
        haystack = f"{title}\n{text}"
    if OLD_MAJOR_SIGNAL.search(haystack):
        raw = OLD_MAJOR_SIGNAL.search(haystack).group(0)
        if re.search(r"跨平台|登陆", raw, re.I):
            return "old_cross_platform_launch", "老品跨平台上线", 1
        if re.search(r"重启|回归|重新上线", raw, re.I):
            return "old_relaunch", "老品重启回归", 1
        return "old_major_update", "老品重大版本更新", 1
    if ROUTINE_OLD_SIGNAL.search(title) or HISTORICAL_LAUNCH.search(title):
        return None
    scheduled = _dated_future_signal(haystack, str(rec.get("date") or ""))
    if scheduled:
        return scheduled
    if NEW_GAME_REVEAL.search(haystack):
        return "new_game_first_reveal", "新品首次曝光", 2
    if NEW_GAME_PRELOAD.search(haystack):
        return "new_game_preload", "新品预下载", 2
    if NEW_GAME_SCHEDULE.search(haystack):
        return "new_game_schedule", "新品定档", 2
    launch = NEW_GAME_LAUNCH.search(haystack)
    test = NEW_GAME_TEST.search(haystack)
    if test and "抢先体验" in test.group(0):
        return "new_game_test", "抢先体验测试", 3
    if launch:
        event = "公测" if "公测" in launch.group(0) else "正式上线"
        return "new_game_launch", event, 3
    if test:
        raw = test.group(0)
        if "抢先体验" in raw:
            event = "抢先体验测试"
        elif re.search(r"计费.*删档|付费.*删档", haystack):
            event = "计费删档测试"
        elif "不删档" in raw:
            event = "不删档测试"
        elif "删档" in raw:
            event = "删档测试"
        elif "不限量" in raw:
            event = "不限量测试"
        elif "限量" in raw:
            event = "限量测试"
        elif "首测" in raw:
            event = "首测"
        elif "内测" in raw:
            event = "内测"
        else:
            event = "公开测试"
        return "new_game_test", event, 3
    return None


def _lookahead_calendar_signal(
    rec: dict[str, Any],
    target_date: dt.date,
) -> tuple[str, str, int] | None:
    """Return a release signal explicitly tied to the one-day lookahead date.

    Only absolute dates in the normal-window source text qualify. Relative
    3839 wording must already have been resolved by the collector and exposed
    as an absolute ``Resolved event`` line.
    """
    text = str(rec.get("text") or "")
    date_forms = (
        target_date.isoformat(),
        f"{target_date.year}年{target_date.month}月{target_date.day}日",
        f"{target_date.month}月{target_date.day}日",
        f"{target_date.month} 月 {target_date.day} 日",
    )
    for line in re.split(r"[\r\n。！？]+", text):
        positions = [line.find(form) for form in date_forms if form in line]
        if not positions:
            continue
        # Start at the date so an earlier same-line preload does not mask a
        # dated next-day launch/test/reveal signal.
        dated_tail = line[min(positions):]
        probe = dict(rec)
        probe["title"] = dated_tail
        probe["text"] = dated_tail
        probe["date"] = target_date.isoformat()
        signal = _calendar_signal(probe)
        if signal:
            return signal
    return None


def build_release_candidates(
    records: list[dict[str, Any]],
    window_start: str | None = None,
    window_end: str | None = None,
    release_lookahead_days: int = 0,
) -> list[dict[str, Any]]:
    """Build calendar candidates and deterministically score/rank them."""
    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    lookahead_end = (
        parse_date(window_end) + dt.timedelta(days=release_lookahead_days)
        if window_end and release_lookahead_days > 0
        else None
    )
    for rec in records:
        if rec["section"] not in {"industry_news", "release_calendar"}:
            continue
        if rec["section"] == "industry_news":
            mentions = _industry_calendar_mentions(rec)
        else:
            primary_signal = _calendar_signal(rec)
            product = _release_game_name(rec)
            mentions = [] if not primary_signal or not product or len(product) < 2 else [{
                "product": product,
                "signal": primary_signal,
                "event_date": _event_date(rec),
            }]
            if lookahead_end and mentions:
                lookahead_signal = _lookahead_calendar_signal(rec, lookahead_end)
                if lookahead_signal and (lookahead_signal[0], lookahead_end.isoformat()) not in {
                    (primary_signal[0], mentions[0]["event_date"])
                }:
                    mentions.append({
                        "product": product,
                        "signal": lookahead_signal,
                        "event_date": lookahead_end.isoformat(),
                    })

        for mention in mentions:
            product = mention["product"]
            signal = mention["signal"]
            event_date = mention["event_date"]
            signal_type, event, event_type_score = signal
            # Product calendars use a section-specific clustering rule: one
            # normalized product on one date is one calendar node. Sources may call
            # that node launch, public test, closed test, paid wipe test, etc.; those
            # labels are evidence variants and must not split the node.
            key = (product, event_date)
            node = grouped.setdefault(key, {
                "product": product,
                "event_date": event_date,
                "signal_type": signal_type,
                "event": event,
                "event_type_score": event_type_score,
                "first_seen_order": len(grouped),
                "observed_signal_types": [],
                "observed_events": [],
                "industry_ids": [],
                "release_ids": [],
                "source_fingerprints": [],
                "focus_companies": [],
                "focus_company_relationships": {},
                "company_evidence_ids": [],
            })
            if signal_type not in node["observed_signal_types"]:
                node["observed_signal_types"].append(signal_type)
            if event_type_score > node["event_type_score"]:
                node["signal_type"] = signal_type
                node["event"] = event
                node["event_type_score"] = event_type_score
            elif len(node["observed_signal_types"]) > 1 and set(node["observed_signal_types"]) <= {"new_game_launch", "new_game_test"}:
                if event == "抢先体验测试" or "抢先体验测试" in node["observed_events"]:
                    # Store pages often call an early-access test "开服"; the
                    # editorial source's more specific event label wins.
                    node["signal_type"] = "new_game_test"
                    node["event"] = "抢先体验测试"
                else:
                    node["signal_type"] = "new_game_launch_or_test"
                    node["event"] = "新品上线/测试节点"
            if event not in node["observed_events"]:
                node["observed_events"].append(event)
            target = "industry_ids" if rec["section"] == "industry_news" else "release_ids"
            node[target].append(rec["source_id"])
            fingerprint = _source_fingerprint(rec)
            if fingerprint and fingerprint not in node["source_fingerprints"]:
                node["source_fingerprints"].append(fingerprint)
            company_relationships = _focus_company_relationships(rec, product)
            for company, relationship in company_relationships.items():
                if company not in node["focus_companies"]:
                    node["focus_companies"].append(company)
                current = node["focus_company_relationships"].get(company)
                if current != "direct" or relationship == "direct":
                    node["focus_company_relationships"][company] = relationship
            if company_relationships and rec["source_id"] not in node["company_evidence_ids"]:
                node["company_evidence_ids"].append(rec["source_id"])

    rows = []
    for node in grouped.values():
        industry_ids = list(dict.fromkeys(node["industry_ids"]))
        release_ids = list(dict.fromkeys(node["release_ids"]))
        coverage_rank = 3 if industry_ids and release_ids else 2 if industry_ids else 1
        coverage = "industry+release" if coverage_rank == 3 else "industry_only" if coverage_rank == 2 else "release_only"
        source_ids = industry_ids + release_ids
        appearance_count = len(node["source_fingerprints"])
        appearance_score = 3 if appearance_count >= 3 else 2 if appearance_count == 2 else 1
        industry_bonus = 1 if industry_ids else 0
        source_strength_score = appearance_score + industry_bonus
        base_priority_score = int(node["event_type_score"]) * source_strength_score
        relationship_values = set(node["focus_company_relationships"].values())
        company_relationship = (
            "direct" if "direct" in relationship_values
            else "investment" if "investment" in relationship_values
            else "none"
        )
        company_bonus = 0
        if str(node["signal_type"]).startswith("new_game_"):
            if company_relationship == "direct":
                company_bonus = FOCUS_COMPANY_BONUS
            elif company_relationship == "investment":
                company_bonus = FOCUS_COMPANY_INVESTMENT_BONUS
        priority_score = base_priority_score + company_bonus
        signal_type = str(node["signal_type"])
        release_window_end = (
            (parse_date(window_end) + dt.timedelta(days=release_lookahead_days)).isoformat()
            if window_end
            else None
        )
        window_eligible = (
            not window_start
            or not window_end
            or signal_type in {"new_game_schedule", "new_game_first_reveal"}
            or window_start <= str(node["event_date"]) <= str(release_window_end)
        )
        window_scope = (
            "report_window"
            if window_start and window_end and window_start <= str(node["event_date"]) <= window_end
            else "next_day_lookahead"
            if window_end and release_window_end and window_end < str(node["event_date"]) <= release_window_end
            else "future_announcement"
            if signal_type in {"new_game_schedule", "new_game_first_reveal"}
            else "outside"
        )
        publish_eligible = appearance_count >= 2 and window_eligible
        rows.append({
            **node,
            "industry_ids": industry_ids,
            "release_ids": release_ids,
            "source_ids": source_ids,
            "appearance_count": appearance_count,
            "appearance_score": appearance_score,
            "industry_bonus": industry_bonus,
            "source_strength_score": source_strength_score,
            "base_priority_score": base_priority_score,
            "company_relationship": company_relationship,
            "company_bonus": company_bonus,
            "priority_score": priority_score,
            "multi_source_eligible": appearance_count >= 2,
            "window_eligible": window_eligible,
            "window_scope": window_scope,
            "publish_eligible": publish_eligible,
            "coverage": coverage,
            "coverage_rank": coverage_rank,
            "status": "pending_decision",
        })
    rows.sort(key=lambda x: (
        -int(x["publish_eligible"]),
        -x["priority_score"],
        -x["company_bonus"],
        -x["event_type_score"],
        -x["appearance_count"],
        -x["industry_bonus"],
        x["first_seen_order"],
    ))
    for index, node in enumerate(rows, 1):
        node["candidate_id"] = f"release-candidate-{index:03d}"
    return rows


def write_summary(
    path: Path,
    records: list[dict[str, Any]],
    window_start: str,
    window_end: str,
    release_lookahead_days: int = 0,
) -> None:
    summary = path.with_name("report_inputs_summary.md")
    by_section: dict[str, int] = {}
    failures = []
    empty = []
    for rec in records:
        by_section[rec["section"]] = by_section.get(rec["section"], 0) + 1
        if rec.get("fetch_status") != "ok":
            failures.append(rec)
        elif rec.get("body_status") == "empty":
            empty.append(rec)

    lines = [
        "# Report Input Extraction Summary",
        "",
        f"- Records: {len(records)}",
        f"- Extraction failures: {len(failures)}",
        f"- Empty text records: {len(empty)}",
        f"- Non-full body records: {sum(1 for rec in records if rec.get('body_status') in {'short_official', 'snippet'})}",
        "",
        "## By Section",
        "",
    ]
    for section, count in sorted(by_section.items()):
        lines.append(f"- `{section}`: {count}")
    if failures or empty:
        lines.extend(["", "## Records Needing Attention", ""])
        for rec in failures + empty:
            lines.append(f"- `{rec['source_id']}` `{rec['section']}` {rec['title']} - fetch={rec.get('fetch_status')} body={rec.get('body_status')} ({rec['text_chars']} chars)")

    crossref = build_release_candidates(
        records, window_start, window_end, release_lookahead_days
    )
    lines.extend([
        "",
        "## 产品日历候选（按事件类型 × 来源强度排序，必须逐条决策）",
        "",
        "> 只列新品上线与新品测试；新版本、资料片、赛季、联动和老品运营不入队。"
        "按来源出现次数降序；次数相同时，行业新闻+产品日历 > 仅行业新闻 > 仅产品日历。",
        "",
    ])
    if crossref:
        for row in crossref:
            lines.append(
                f"- **{row['product']}** [{row['signal_type']}] — priority={row['priority_score']} "
                f"(event={row['event_type_score']} × source={row['source_strength_score']} "
                f"+ company={row['company_bonus']}) | count={row['appearance_count']} "
                f"| focus={','.join(row['focus_companies']) or '-'} | coverage={row['coverage']} "
                f"| sources: {', '.join(row['source_ids'])}"
            )
    else:
        lines.append("- （本窗口无产品日历候选）")

    summary.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_audits(
    path: Path,
    records: list[dict[str, Any]],
    window_start: str,
    window_end: str,
    release_lookahead_days: int = 0,
) -> None:
    """Write deterministic quality and industry→calendar candidate queues."""
    quality = {
        "schema_version": 1,
        "records": [
            {
                "source_id": rec["source_id"], "section": rec["section"], "title": rec["title"],
                "fetch_status": rec.get("fetch_status"), "body_status": rec.get("body_status"),
                "text_chars": rec["text_chars"],
            }
            for rec in records
        ],
    }
    nodes = build_release_candidates(
        records, window_start, window_end, release_lookahead_days
    )
    (path.parent / "source_quality_audit.json").write_text(
        json.dumps(quality, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (path.parent / "release_calendar_audit.json").write_text(
        json.dumps(
            {
                "schema_version": 5,
                "report_window": {"start": window_start, "end": window_end},
                "release_lookahead_days": release_lookahead_days,
                "release_window": {
                    "start": window_start,
                    "end": (
                        parse_date(window_end) + dt.timedelta(days=release_lookahead_days)
                    ).isoformat(),
                },
                "ranking": (
                    "publish_eligible desc, priority_score desc; tie company_bonus desc, event_type_score desc, "
                    "appearance_count desc, industry_bonus desc, first_seen_order asc"
                ),
                "formula": "priority_score = event_type_score * source_strength_score + company_bonus",
                "focus_company_bonus": FOCUS_COMPANY_BONUS,
                "focus_company_investment_bonus": FOCUS_COMPANY_INVESTMENT_BONUS,
                "nodes": nodes,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def write_index(path: Path, records: list[dict[str, Any]]) -> None:
    """Emit report_inputs_index.md listing EVERY record per section (no cap).

    This is the global overview the generation step scans before drilling into
    the JSONL. It MUST be complete: the per-section header count equals the
    number of bullet lines under it. Never truncate — a missing row here is a
    silently dropped candidate at generation time.
    """
    index = path.with_name("report_inputs_index.md")
    by_section: dict[str, list[dict[str, Any]]] = {}
    for rec in records:
        by_section.setdefault(rec["section"], []).append(rec)

    lines = [
        "# Report Inputs Index",
        "",
        f"- Total records: {len(records)}",
        "- 本文件列出每个 section 的**全部**记录（无截断）；表头计数 == 该节列出的行数。",
        "- 用途：生成阶段先扫这里做全局标题/来源/日期覆盖，再按 source_id 下钻 JSONL 细节。",
        "- **禁止截断**：任何一节的行数少于表头计数即为漏召回缺陷。",
        "",
    ]
    for section in sorted(by_section):
        recs = by_section[section]
        lines.append(f"## {section} ({len(recs)} records)")
        lines.append("")
        for rec in recs:
            src = rec.get("source") or rec.get("source_key") or "-"
            title = (rec.get("title") or "").replace("\n", " ").strip() or "(无标题)"
            lines.append(
                f"- `{rec['source_id']}` [{rec['date']}] ({src}) {title} "
                f"— {rec['text_chars']} chars, body={rec.get('body_status')}"
            )
        lines.append("")

    index.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".", help="Workspace root containing news_data")
    parser.add_argument("--date", help="Single report date, YYYY-MM-DD")
    parser.add_argument("--start", help="Inclusive start date, YYYY-MM-DD")
    parser.add_argument("--end", help="Inclusive end date, YYYY-MM-DD")
    parser.add_argument("--report-type", choices=["daily", "weekly", "monthly", "custom"], default="daily")
    parser.add_argument("--sections", nargs="*", default=DEFAULT_SECTIONS)
    parser.add_argument("--output", help="Output JSONL path. Defaults to report output _intermediate folder.")
    parser.add_argument(
        "--deep-selection",
        help="Weekly-only selection file named for the target weekly ID; selected sources from the "
        "one-day-earlier candidate window are added as deep-only inputs.",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    if args.date:
        start = end = parse_date(args.date)
    else:
        if not args.start or not args.end:
            parser.error("Use --date or both --start and --end")
        start = parse_date(args.start)
        end = parse_date(args.end)
    if end < start:
        parser.error("--end must be >= --start")

    output = Path(args.output).resolve() if args.output else default_output(workspace, args.report_type, start, end)
    output.parent.mkdir(parents=True, exist_ok=True)

    records = collect_records(workspace, iter_dates(start, end), args.sections)
    if args.deep_selection:
        if args.report_type != "weekly":
            parser.error("--deep-selection is only valid with --report-type weekly")
        records = augment_deep_selection_records(
            workspace, records, Path(args.deep_selection).resolve(), start, end, args.sections
        )
    with output.open("w", encoding="utf-8", newline="\n") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    release_lookahead_days = 1 if args.report_type in {"daily", "weekly", "custom"} else 0
    write_summary(
        output, records, start.isoformat(), end.isoformat(), release_lookahead_days
    )
    write_index(output, records)
    write_audits(
        output, records, start.isoformat(), end.isoformat(), release_lookahead_days
    )

    failed = sum(1 for rec in records if rec.get("fetch_status") != "ok")
    empty = sum(1 for rec in records if rec.get("body_status") == "empty")
    print(f"Wrote {len(records)} records to {output}")
    print(f"Failures: {failed}; empty text records: {empty}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
