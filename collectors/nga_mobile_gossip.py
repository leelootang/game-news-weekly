"""
Fetch hot NGA mobile-game gossip threads and export them to PDF.

Forum threads are selected by activity rather than publication date alone:
new threads and still-active old threads are collected from separate sorted
entry points, deduplicated, scored, and saved under player_discourse.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import html
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urljoin, urlparse

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from playwright.async_api import Page, TimeoutError as PWTimeout
from playwright.async_api import async_playwright


BASE = "https://bbs.nga.cn"
FID = "-61285727"
SOURCE_DOMAIN = "bbs.nga.cn"
SOURCE_KEY = "nga_mobile_gossip"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
PAGE_TIMEOUT = 30_000
LOCAL_TZ = timezone(timedelta(hours=8))
DEFAULT_TOP_N = 20
PDF_RENDER_VERSION = 4
NGA_UID = "64937443"
NGA_CID = "X9ffgip36vc3v1tqdb7ato89i8e5gu1ufsn1h82m"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


@dataclass
class ThreadItem:
    tid: str
    url: str
    title: str
    replies: int
    page_count: int
    author: str
    last_reply_author: str
    created_at: datetime | None
    last_reply_at: datetime | None
    raw_created_at: str
    raw_last_reply_at: str
    discovered_from: set[str]
    score: float = 0.0
    activity_basis: str = "replied"


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        dt = datetime.fromisoformat(raw)
        return dt + timedelta(days=1) if end_of_day else dt
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).replace(tzinfo=None)


def preset_window(name: str) -> tuple[datetime, datetime]:
    now = datetime.now().replace(microsecond=0)
    today = now.replace(hour=0, minute=0, second=0)
    if name == "last-7-days":
        return now - timedelta(days=7), now
    if name == "yesterday":
        return today - timedelta(days=1), today
    if name == "today":
        return today, now
    raise ValueError(f"unknown preset: {name}")


def sanitize_filename(name: str, max_len: int = 90) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:max_len].rstrip(" .") or "untitled"


def parse_nga_time(value: str, now: datetime) -> datetime | None:
    text = re.sub(r"\s+", " ", (value or "").replace("\xa0", " ")).strip()
    if not text:
        return None
    match = re.search(r"(\d+)\s*分钟前", text)
    if match:
        return now - timedelta(minutes=int(match.group(1)))
    match = re.search(r"(\d+)\s*小时前", text)
    if match:
        return now - timedelta(hours=int(match.group(1)))
    match = re.search(r"今天\s*(\d{1,2}):(\d{2})", text)
    if match:
        hour, minute = map(int, match.groups())
        return now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    match = re.search(r"昨天\s*(\d{1,2}):(\d{2})", text)
    if match:
        hour, minute = map(int, match.groups())
        return (now - timedelta(days=1)).replace(hour=hour, minute=minute, second=0, microsecond=0)
    match = re.search(r"前天\s*(\d{1,2}):(\d{2})", text)
    if match:
        hour, minute = map(int, match.groups())
        return (now - timedelta(days=2)).replace(hour=hour, minute=minute, second=0, microsecond=0)
    match = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})", text)
    if match:
        year, month, day, hour, minute = map(int, match.groups())
        return datetime(year, month, day, hour, minute)
    match = re.search(r"(?<!\d)(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})", text)
    if match:
        month, day, hour, minute = map(int, match.groups())
        candidate = datetime(now.year, month, day, hour, minute)
        if candidate > now + timedelta(days=2):
            candidate = candidate.replace(year=now.year - 1)
        return candidate
    return None


def thread_id_from_url(url: str) -> str:
    query = parse_qs(urlparse(url).query)
    tid = (query.get("tid") or [""])[0].strip()
    if tid:
        return tid
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    return f"thread_{digest}"


def safe_int(value, default: int = 0) -> int:
    if value is None:
        return default
    if isinstance(value, float) and math.isnan(value):
        return default
    try:
        return int(value)
    except (TypeError, ValueError, OverflowError):
        return default


def load_manifest(out_dir: Path) -> dict:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME):
        if not path.exists() and legacy_path.exists():
            path = legacy_path
            break
    if not path.exists():
        return {"items": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        backup = path.with_suffix(path.suffix + ".broken")
        path.replace(backup)
        print(f"[manifest] manifest broken, moved to {backup.name}", file=sys.stderr)
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def forum_url(order_by: str, page_num: int) -> str:
    params = {"fid": FID, "order_by": order_by}
    if page_num > 1:
        params["page"] = str(page_num)
    return f"{BASE}/thread.php?{urlencode(params)}"


async def add_nga_cookies(context) -> None:
    await context.add_cookies(
        [
            {"name": "ngaPassportUid", "value": NGA_UID, "domain": ".nga.cn", "path": "/", "secure": True},
            {"name": "ngaPassportCid", "value": NGA_CID, "domain": ".nga.cn", "path": "/", "secure": True},
        ]
    )


async def open_nga_page(page: Page, url: str) -> None:
    await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
    await page.wait_for_timeout(2500)
    if "adpage_insert" in page.url:
        try:
            await page.get_by_text("点此跳过广告").first.click(timeout=3000)
            await page.wait_for_load_state("domcontentloaded", timeout=PAGE_TIMEOUT)
        except PWTimeout:
            pass
        await page.wait_for_timeout(2500)


async def parse_thread_rows(page: Page, source: str, now: datetime) -> list[ThreadItem]:
    rows = await page.locator("tr.topicrow").evaluate_all(
        """rows => rows.map(row => {
            const cells = Array.from(row.querySelectorAll('td'));
            const topic = row.querySelector('a.topic');
            const replies = row.querySelector('a.replies');
            const pager = Array.from(row.querySelectorAll('.pager a'))
                .map(a => parseInt(a.innerText.trim(), 10))
                .filter(n => Number.isFinite(n));
            const c3 = cells[2]?.innerText || '';
            const c4 = cells[3]?.innerText || '';
            const lines3 = c3.split(/\\n+/).map(s => s.trim()).filter(Boolean);
            const lines4 = c4.split(/\\n+/).map(s => s.trim()).filter(Boolean);
            return {
                title: topic?.innerText || '',
                url: topic?.href || '',
                replies: replies ? parseInt(replies.innerText.trim(), 10) : 0,
                pageCount: pager.length ? Math.max(...pager) : 1,
                author: lines3[0] || '',
                createdText: lines3.slice(1).join(' '),
                lastReplyText: lines4[0] || '',
                lastReplyAuthor: lines4.slice(1).join(' '),
            };
        })"""
    )
    items: list[ThreadItem] = []
    for row in rows:
        url = row.get("url") or ""
        title = re.sub(r"\s+", " ", row.get("title") or "").strip()
        if not url or not title:
            continue
        url = urljoin(BASE, url)
        raw_created = row.get("createdText") or ""
        raw_last = row.get("lastReplyText") or ""
        replies = safe_int(row.get("replies"), 0)
        page_count = max(safe_int(row.get("pageCount"), 1), math.ceil((replies + 1) / 20))
        items.append(
            ThreadItem(
                tid=thread_id_from_url(url),
                url=url,
                title=title,
                replies=replies,
                page_count=page_count,
                author=(row.get("author") or "").strip(),
                last_reply_author=(row.get("lastReplyAuthor") or "").strip(),
                created_at=parse_nga_time(raw_created, now),
                last_reply_at=parse_nga_time(raw_last, now),
                raw_created_at=raw_created,
                raw_last_reply_at=raw_last,
                discovered_from={source},
            )
        )
    return items


def merge_item(items: dict[str, ThreadItem], item: ThreadItem) -> None:
    existing = items.get(item.tid)
    if not existing:
        items[item.tid] = item
        return
    existing.discovered_from.update(item.discovered_from)
    existing.replies = max(existing.replies, item.replies)
    existing.page_count = max(existing.page_count, item.page_count)
    if not existing.created_at and item.created_at:
        existing.created_at = item.created_at
        existing.raw_created_at = item.raw_created_at
    if not existing.last_reply_at and item.last_reply_at:
        existing.last_reply_at = item.last_reply_at
        existing.raw_last_reply_at = item.raw_last_reply_at


def in_window(value: datetime | None, since: datetime, until: datetime) -> bool:
    return bool(value and since <= value < until)


def eligible_item(item: ThreadItem, since: datetime, until: datetime) -> bool:
    created = in_window(item.created_at, since, until)
    active = in_window(item.last_reply_at, since, until)
    if created and item.replies >= 10:
        return True
    if active and (item.replies >= 20 or item.page_count >= 2):
        return True
    return False


def score_item(item: ThreadItem, since: datetime, until: datetime) -> float:
    created = in_window(item.created_at, since, until)
    active = in_window(item.last_reply_at, since, until)
    basis_at = item.created_at if created else item.last_reply_at
    item.activity_basis = "created" if created else "replied"
    recency = 0.0
    if basis_at:
        hours = max(0.0, (until - basis_at).total_seconds() / 3600)
        recency = max(0.0, 48.0 - hours) * 1.5
    return (
        item.replies * 2.0
        + min(item.page_count, 10) * 8.0
        + (30.0 if created else 0.0)
        + (20.0 if active else 0.0)
        + recency
    )


async def collect_threads(since: datetime, until: datetime, max_pages: int, top_n: int, headless: bool) -> list[ThreadItem]:
    now = datetime.now().replace(microsecond=0)
    merged: dict[str, ThreadItem] = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context(user_agent=USER_AGENT, locale="zh-CN", timezone_id="Asia/Shanghai")
        await add_nga_cookies(context)
        page = await context.new_page()
        for order_by, source, date_attr in [
            ("postdatedesc", "new_threads", "created_at"),
            ("lastpostdesc", "active_threads", "last_reply_at"),
        ]:
            for page_num in range(1, max_pages + 1):
                url = forum_url(order_by, page_num)
                print(f"[list] open {source} page={page_num}: {url}")
                await open_nga_page(page, url)
                rows = await parse_thread_rows(page, source, now)
                if not rows:
                    print(f"[list] {source} page={page_num}: no rows")
                    break
                for item in rows:
                    merge_item(merged, item)
                older_seen = any((getattr(item, date_attr) and getattr(item, date_attr) < since) for item in rows)
                in_window_seen = any(in_window(getattr(item, date_attr), since, until) for item in rows)
                print(f"[list] {source} page={page_num}: rows={len(rows)} in_window={in_window_seen} older={older_seen}")
                if older_seen and not in_window_seen:
                    break
        await browser.close()

    selected = [item for item in merged.values() if eligible_item(item, since, until)]
    for item in selected:
        item.score = score_item(item, since, until)
    selected.sort(key=lambda item: item.score, reverse=True)
    return selected[:top_n]


async def render_thread_pdf(item: ThreadItem, out_dir: Path, file_name: str, headless: bool) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless)
        context = await browser.new_context(user_agent=USER_AGENT, locale="zh-CN", timezone_id="Asia/Shanghai")
        await add_nga_cookies(context)
        page = await context.new_page()
        await open_nga_page(page, item.url)
        first_posts = await extract_posts(page, limit=8)
        last_posts: list[dict] = []
        if item.page_count > 1:
            last_url = add_page_param(item.url, item.page_count)
            await open_nga_page(page, last_url)
            last_posts = await extract_posts(page, limit=8, tail=True)
        await page.set_content(render_excerpt_html(item, first_posts, last_posts), wait_until="domcontentloaded")
        await page.pdf(path=str(out_dir / file_name), format="A4", print_background=True, margin={"top": "10mm", "right": "8mm", "bottom": "10mm", "left": "8mm"})
        await browser.close()


def add_page_param(url: str, page_num: int) -> str:
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params["page"] = [str(page_num)]
    query = urlencode({key: values[-1] for key, values in params.items()})
    return parsed._replace(query=query).geturl()


async def extract_posts(page: Page, limit: int, *, tail: bool = False) -> list[dict]:
    return await page.locator("tr.postrow").evaluate_all(
        """(rows, args) => {
            const [limit, tail] = args;
            const selected = tail ? rows.slice(-limit) : rows.slice(0, limit);
            return selected.map(row => {
            const id = row.id || '';
            const floor = (row.innerText.match(/#\\d+/) || [''])[0];
            const author = row.querySelector('.posterinfo .author, .posterinfo a.author')?.innerText || '';
            const date = row.querySelector('.postdatec')?.innerText || '';
            const subject = row.querySelector('h3')?.innerText || '';
            const content = row.querySelector('.postcontent')?.innerText || '';
            const good = row.querySelector('.ogoodbtn')?.innerText || '';
            return {id, floor, author, date, subject, content, good};
            }).filter(post => post.content || post.subject);
        }""",
        [limit, tail],
    )


def render_excerpt_html(item: ThreadItem, first_posts: list[dict], last_posts: list[dict]) -> str:
    basis = item_basis_datetime(item).strftime("%Y-%m-%d %H:%M")
    sections = [
        post_section("首页摘录", first_posts),
    ]
    if last_posts:
        sections.append(post_section(f"末页摘录 (第 {item.page_count} 页)", last_posts))
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: "Microsoft YaHei", Arial, sans-serif; color: #222; line-height: 1.55; }}
    h1 {{ font-size: 22px; margin: 0 0 10px; }}
    h2 {{ font-size: 17px; margin: 22px 0 8px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }}
    .meta {{ color: #555; font-size: 12px; margin-bottom: 14px; }}
    .heat {{ border: 2px solid #b94a30; background: #fff6f2; padding: 10px 12px; margin: 12px 0 16px; }}
    .heat-title {{ font-weight: 700; color: #8f321e; margin-bottom: 6px; }}
    .heat-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; font-size: 12px; }}
    .heat-metric {{ background: #fff; border: 1px solid #e4c5ba; padding: 6px; }}
    .heat-value {{ display: block; font-size: 18px; font-weight: 700; color: #222; }}
    .post {{ border: 1px solid #ddd; border-radius: 4px; padding: 9px 11px; margin: 8px 0; page-break-inside: avoid; }}
    .post-meta {{ color: #666; font-size: 12px; margin-bottom: 6px; }}
    .subject {{ font-weight: 700; margin-bottom: 6px; }}
    .content {{ white-space: pre-wrap; font-size: 13px; }}
    a {{ color: #1f5f9f; text-decoration: none; }}
  </style>
</head>
<body>
  <h1>{html.escape(item.title)}</h1>
  <div class="meta">
    来源：NGA 手游瓜事件 |
    回复：{item.replies} |
    页数：{item.page_count} |
    收录依据：{html.escape(item.activity_basis)} @ {html.escape(basis)}<br>
    发帖：{html.escape(item.created_at.isoformat(timespec="minutes") if item.created_at else item.raw_created_at)} |
    最新回复：{html.escape(item.last_reply_at.isoformat(timespec="minutes") if item.last_reply_at else item.raw_last_reply_at)} |
    <a href="{html.escape(item.url)}">{html.escape(item.url)}</a>
  </div>
  <section class="heat">
    <div class="heat-title">热度概览：优先关注高回复、多页、窗口内仍活跃的主题</div>
    <div class="heat-grid">
      <div class="heat-metric"><span class="heat-value">{item.replies}</span>回复数</div>
      <div class="heat-metric"><span class="heat-value">{item.page_count}</span>页数</div>
      <div class="heat-metric"><span class="heat-value">{item.score:.1f}</span>综合热度分</div>
      <div class="heat-metric"><span class="heat-value">{html.escape(item.activity_basis)}</span>收录依据</div>
    </div>
  </section>
  {''.join(sections)}
</body>
</html>"""


def post_section(title: str, posts: list[dict]) -> str:
    cards = []
    for post in posts:
        meta_parts = [
            post.get("floor") or "",
            post.get("author") or "",
            post.get("date") or "",
        ]
        if post.get("good"):
            meta_parts.append(f"赞 {post['good']}")
        meta = " | ".join(html.escape(part.strip()) for part in meta_parts if part.strip())
        subject = post.get("subject") or ""
        subject_html = f'<div class="subject">{html.escape(subject)}</div>' if subject.strip() else ""
        content = html.escape((post.get("content") or "").strip())
        cards.append(
            f'<article class="post"><div class="post-meta">{meta}</div>{subject_html}<div class="content">{content}</div></article>'
        )
    if not cards:
        cards.append('<article class="post"><div class="content">未能解析到帖子内容。</div></article>')
    return f"<h2>{html.escape(title)}</h2>{''.join(cards)}"


def item_basis_datetime(item: ThreadItem) -> datetime:
    if item.activity_basis == "created" and item.created_at:
        return item.created_at
    if item.last_reply_at:
        return item.last_reply_at
    if item.created_at:
        return item.created_at
    return datetime.now().replace(microsecond=0)


async def save_threads(items: list[ThreadItem], out_dir: Path, headless: bool) -> tuple[int, int]:
    manifest = load_manifest(out_dir)
    manifest.setdefault("items", {})
    ok = 0
    fail = 0
    text_context = None
    text_browser = None
    text_page = None
    if not save_pdf_enabled() and items:
        playwright = await async_playwright().start()
        text_browser = await playwright.chromium.launch(headless=headless)
        text_context = await text_browser.new_context(user_agent=USER_AGENT, locale="zh-CN", timezone_id="Asia/Shanghai")
        await add_nga_cookies(text_context)
        text_page = await text_context.new_page()
    for item in items:
        basis_at = item_basis_datetime(item)
        file_name = (
            f"{FILE_PREFIX}_{basis_at.strftime('%Y-%m-%d')}_{item.tid}_"
            f"{sanitize_filename(item.title)}.pdf"
        )
        existing = manifest["items"].get(item.tid)
        if existing and existing.get("data_file"):
            print(f"[{item.tid}] already saved, skip")
            ok += 1
        elif not save_pdf_enabled():
            try:
                print(f"[{item.tid}] extract text replies={item.replies} pages={item.page_count} score={item.score:.1f}")
                assert text_page is not None
                await open_nga_page(text_page, item.url)
                first_posts = await extract_posts(text_page, limit=8)
                last_posts: list[dict] = []
                if item.page_count > 1:
                    await open_nga_page(text_page, add_page_param(item.url, item.page_count))
                    last_posts = await extract_posts(text_page, limit=8, tail=True)
                html_text = render_excerpt_html(item, first_posts, last_posts)
                write_article_record(
                    out_dir,
                    manifest,
                    item.tid,
                    {
                        "source": SOURCE_DOMAIN,
                        "source_key": SOURCE_KEY,
                        "title": item.title,
                        "url": item.url,
                        "author": item.author,
                        "text": html_to_text(html_text),
                        "html": html_text,
                        "published_at": basis_at.isoformat(timespec="seconds"),
                        "extra": {
                            "thread_created_at": item.created_at.isoformat(timespec="seconds") if item.created_at else "",
                            "last_reply_at": item.last_reply_at.isoformat(timespec="seconds") if item.last_reply_at else "",
                            "raw_created_at": item.raw_created_at,
                            "raw_last_reply_at": item.raw_last_reply_at,
                            "activity_basis": item.activity_basis,
                            "reply_count": item.replies,
                            "page_count": item.page_count,
                            "last_reply_author": item.last_reply_author,
                            "discovered_from": sorted(item.discovered_from),
                            "score": round(item.score, 2),
                        },
                    },
                )
                ok += 1
            except Exception as exc:
                print(f"[{item.tid}] failed: {exc}", file=sys.stderr)
                fail += 1
                continue
        elif existing and existing.get("pdf_render_version") == PDF_RENDER_VERSION and (out_dir / existing.get("file", "")).exists():
            print(f"[{item.tid}] already saved, skip")
            ok += 1
        else:
            try:
                print(f"[{item.tid}] render replies={item.replies} pages={item.page_count} score={item.score:.1f}")
                await render_thread_pdf(item, out_dir, file_name, headless)
                ok += 1
            except Exception as exc:
                print(f"[{item.tid}] failed: {exc}", file=sys.stderr)
                fail += 1
                continue
        if not save_pdf_enabled():
            save_manifest(out_dir, manifest)
            continue
        manifest["items"][item.tid] = {
            "file": file_name,
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "title": item.title,
            "url": item.url,
            "published_at": basis_at.isoformat(timespec="seconds"),
            "thread_created_at": item.created_at.isoformat(timespec="seconds") if item.created_at else "",
            "last_reply_at": item.last_reply_at.isoformat(timespec="seconds") if item.last_reply_at else "",
            "raw_created_at": item.raw_created_at,
            "raw_last_reply_at": item.raw_last_reply_at,
            "activity_basis": item.activity_basis,
            "reply_count": item.replies,
            "page_count": item.page_count,
            "author": item.author,
            "last_reply_author": item.last_reply_author,
            "discovered_from": sorted(item.discovered_from),
            "score": round(item.score, 2),
            "pdf_render_version": PDF_RENDER_VERSION,
            "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        save_manifest(out_dir, manifest)
    if text_browser is not None:
        await text_browser.close()
        await playwright.stop()
    return ok, fail


async def amain(args: argparse.Namespace) -> int:
    if args.since or args.until:
        if not args.since or not args.until:
            raise SystemExit("--since and --until must be provided together")
        since = parse_date(args.since)
        until = parse_date(args.until)
    else:
        since, until = preset_window(args.preset)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    top_n = args.limit or DEFAULT_TOP_N
    print(f"[config] window: {since} <= activity < {until}")
    print(f"[config] output: {out_dir}")
    print("[config] popularity: new replies>=10; active replies>=20 or pages>=2; no view count on NGA list")
    items = await collect_threads(since, until, args.max_pages, top_n, not args.headful)
    print(f"[list] selected {len(items)} thread(s)")
    ok, fail = await save_threads(items, out_dir, not args.headful)
    print(f"[done] ok={ok} fail={fail} output={out_dir}")
    return 1 if fail else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect NGA mobile-game gossip hot threads.")
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="yesterday")
    parser.add_argument("--since", default="")
    parser.add_argument("--until", default="")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--max-pages", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0, help="Debug/top-N limit. Defaults to 20.")
    parser.add_argument("--headful", action="store_true")
    args = parser.parse_args()
    return asyncio.run(amain(args))


if __name__ == "__main__":
    raise SystemExit(main())
