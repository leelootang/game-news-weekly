"""
Fetch rising r/gaming Reddit posts and export player-discourse PDFs.

Reddit's Rising listing is already a platform-provided "gaining heat now"
ordering, so this collector preserves the source order instead of re-scoring
posts. It scans forward until several consecutive posts are older than the
requested window.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse

from article_store import html_to_text, save_pdf_enabled, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths
from playwright.async_api import async_playwright


SUBREDDIT = "gaming"
LISTING_URL = f"https://www.reddit.com/r/{SUBREDDIT}/rising/.json"
OLD_LISTING_URL = f"https://old.reddit.com/r/{SUBREDDIT}/rising/"
SOURCE_DOMAIN = "reddit.com"
SOURCE_KEY = "reddit_gaming_rising"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
DEFAULT_TOP_N = 20
OLD_STREAK_STOP = 3
PAGE_TIMEOUT = 30_000
USER_AGENT = "AI-Game-Industry-Report/0.1 by local collector"
OLD_REDDIT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)
REDDIT_BROWSER_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "DNT": "1",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}
PDF_RENDER_VERSION = 2


@dataclass(frozen=True)
class RedditPost:
    post_id: str
    fullname: str
    title: str
    author: str
    subreddit: str
    permalink: str
    url: str
    domain: str
    selftext: str
    created_at: datetime
    score: int
    num_comments: int
    upvote_ratio: float
    over_18: bool
    spoiler: bool
    stickied: bool
    rising_rank: int


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


def reddit_datetime(created_utc: float) -> datetime:
    return datetime.fromtimestamp(float(created_utc), timezone.utc).astimezone(LOCAL_TZ).replace(tzinfo=None)


async def fetch_json_browser(page, url: str) -> dict | list:
    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            response = await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
            if not response or response.status >= 400:
                raise RuntimeError(f"HTTP status {response.status if response else 'unknown'}")
            text = await page.locator("body").inner_text(timeout=PAGE_TIMEOUT)
            return json.loads(text)
        except Exception as exc:
            last_exc = exc
            if attempt < 3:
                print(f"[http] retry {attempt}/3 after Reddit error: {exc}", file=sys.stderr)
                await page.wait_for_timeout(int(1500 * attempt))
    raise RuntimeError(f"failed to fetch Reddit JSON: {url}: {last_exc}") from last_exc


def is_reddit_access_blocked(exc: Exception) -> bool:
    text = str(exc).lower()
    return "403" in text or "forbidden" in text or "blocked" in text


def listing_url(after: str | None, limit: int = 100) -> str:
    params = {"limit": str(limit), "raw_json": "1"}
    if after:
        params["after"] = after
    return f"{LISTING_URL}?{urlencode(params)}"


def post_from_child(child: dict, rank: int) -> RedditPost | None:
    data = child.get("data") or {}
    if data.get("is_created_from_ads_ui"):
        return None
    post_id = str(data.get("id") or "").strip()
    title = str(data.get("title") or "").strip()
    permalink = str(data.get("permalink") or "").strip()
    if not post_id or not title or not permalink:
        return None
    return RedditPost(
        post_id=post_id,
        fullname=str(data.get("name") or f"t3_{post_id}"),
        title=title,
        author=str(data.get("author") or "[deleted]"),
        subreddit=str(data.get("subreddit") or SUBREDDIT),
        permalink="https://www.reddit.com" + permalink,
        url=str(data.get("url_overridden_by_dest") or data.get("url") or ""),
        domain=str(data.get("domain") or ""),
        selftext=str(data.get("selftext") or ""),
        created_at=reddit_datetime(float(data.get("created_utc") or 0)),
        score=int(data.get("score") or 0),
        num_comments=int(data.get("num_comments") or 0),
        upvote_ratio=float(data.get("upvote_ratio") or 0.0),
        over_18=bool(data.get("over_18")),
        spoiler=bool(data.get("spoiler")),
        stickied=bool(data.get("stickied") or data.get("pinned")),
        rising_rank=rank,
    )


def post_from_old_listing(item: dict, rank: int) -> RedditPost | None:
    fullname = str(item.get("fullname") or "").strip()
    post_id = fullname.removeprefix("t3_")
    title = str(item.get("title") or "").strip()
    permalink = str(item.get("permalink") or "").strip()
    timestamp_ms = item.get("timestamp")
    if not post_id or not title or not permalink or not timestamp_ms:
        return None
    try:
        created_at = datetime.fromtimestamp(float(timestamp_ms) / 1000, timezone.utc).astimezone(LOCAL_TZ).replace(tzinfo=None)
    except (TypeError, ValueError, OSError):
        return None
    return RedditPost(
        post_id=post_id,
        fullname=fullname,
        title=html.unescape(title),
        author=str(item.get("author") or "[deleted]"),
        subreddit=str(item.get("subreddit") or SUBREDDIT),
        permalink="https://www.reddit.com" + permalink,
        url=str(item.get("url") or ""),
        domain=str(item.get("domain") or ""),
        selftext="",
        created_at=created_at,
        score=int(item.get("score") or 0),
        num_comments=int(item.get("comments_count") or 0),
        upvote_ratio=0.0,
        over_18=str(item.get("nsfw") or "").lower() == "true",
        spoiler=str(item.get("spoiler") or "").lower() == "true",
        stickied=str(item.get("stickied") or "").lower() == "true",
        rising_rank=rank,
    )


def in_window(value: datetime, since: datetime, until: datetime) -> bool:
    return since <= value < until


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


async def collect_posts(since: datetime, until: datetime, max_pages: int, top_n: int) -> tuple[list[RedditPost], bool]:
    selected: list[RedditPost] = []
    seen: set[str] = set()
    old_streak = 0
    skipped_future = 0
    after: str | None = None
    rank = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            user_agent=OLD_REDDIT_USER_AGENT,
            extra_http_headers=REDDIT_BROWSER_HEADERS,
            locale="en-US",
            viewport={"width": 1440, "height": 1024},
        )
        for page_num in range(1, max_pages + 1):
            url = listing_url(after)
            print(f"[listing] open page={page_num}: {url}")
            try:
                data = await fetch_json_browser(page, url)
            except Exception as exc:
                print(f"[listing] reddit JSON failed, falling back to old Reddit HTML: {exc}", file=sys.stderr)
                await browser.close()
                try:
                    return await collect_posts_old_html(since, until, max_pages, top_n), True
                except Exception as fallback_exc:
                    if is_reddit_access_blocked(fallback_exc):
                        print(
                            "[listing] Reddit blocked both JSON and old Reddit HTML fallback; "
                            "returning zero posts for this run.",
                            file=sys.stderr,
                        )
                    return [], True
                    raise
            listing = (data.get("data") if isinstance(data, dict) else {}) or {}
            children = listing.get("children") or []
            after = listing.get("after")
            print(f"[listing] page={page_num}: rows={len(children)} after={after or '-'}")
            if not children:
                break

            for child in children:
                rank += 1
                post = post_from_child(child, rank)
                if not post:
                    continue
                if post.post_id in seen:
                    continue
                seen.add(post.post_id)
                if post.stickied:
                    continue
                if post.created_at >= until:
                    skipped_future += 1
                    old_streak = 0
                    continue
                if post.created_at < since:
                    old_streak += 1
                    if old_streak >= OLD_STREAK_STOP:
                        print(f"[listing] stop: {old_streak} consecutive posts older than window")
                        print(f"[listing] skipped_future={skipped_future}")
                        await browser.close()
                        return selected[:top_n], False
                    continue
                old_streak = 0
                selected.append(post)
                if len(selected) >= top_n:
                    print(f"[listing] reached top_n={top_n}")
                    await browser.close()
                    return selected, False
            if not after:
                break
        await browser.close()

    print(f"[listing] skipped_future={skipped_future}")
    return selected[:top_n], False


async def collect_posts_old_html(since: datetime, until: datetime, max_pages: int, top_n: int) -> list[RedditPost]:
    selected: list[RedditPost] = []
    seen: set[str] = set()
    old_streak = 0
    skipped_future = 0
    rank = 0
    url: str | None = OLD_LISTING_URL

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            user_agent=OLD_REDDIT_USER_AGENT,
            extra_http_headers=REDDIT_BROWSER_HEADERS,
            locale="en-US",
            viewport={"width": 1440, "height": 1024},
        )
        for page_num in range(1, max_pages + 1):
            if not url:
                break
            print(f"[listing:fallback] open page={page_num}: {url}")
            response = await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
            if not response or response.status >= 400:
                await browser.close()
                status = response.status if response else "unknown"
                if status == 403:
                    print("[listing:fallback] old Reddit returned HTTP 403; returning zero posts.", file=sys.stderr)
                    return []
                raise RuntimeError(f"old Reddit fallback failed: HTTP status {status}")
            payload = await page.evaluate(
                """() => {
                    const rows = Array.from(document.querySelectorAll('#siteTable > .thing.link'));
                    const posts = rows.map((el) => {
                        const titleEl = el.querySelector('a.title');
                        return {
                            fullname: el.dataset.fullname || '',
                            title: titleEl ? titleEl.textContent.trim() : '',
                            author: el.dataset.author || '[deleted]',
                            subreddit: el.dataset.subreddit || 'gaming',
                            permalink: el.dataset.permalink || '',
                            url: el.dataset.url || '',
                            domain: el.dataset.domain || '',
                            timestamp: el.dataset.timestamp || '',
                            comments_count: el.dataset.commentsCount || '0',
                            score: el.dataset.score || el.querySelector('.score.unvoted')?.getAttribute('title') || '0',
                            nsfw: el.dataset.nsfw || 'false',
                            spoiler: el.dataset.spoiler || 'false',
                            stickied: el.classList.contains('stickied') ? 'true' : 'false',
                        };
                    });
                    const nextHref = document.querySelector('.next-button a')?.href || '';
                    return {posts, nextHref};
                }"""
            )
            posts = payload.get("posts") or []
            url = payload.get("nextHref") or None
            print(f"[listing:fallback] page={page_num}: rows={len(posts)} next={'yes' if url else '-'}")
            if not posts:
                break
            for item in posts:
                rank += 1
                post = post_from_old_listing(item, rank)
                if not post or post.post_id in seen:
                    continue
                seen.add(post.post_id)
                if post.stickied:
                    continue
                if post.created_at >= until:
                    skipped_future += 1
                    old_streak = 0
                    continue
                if post.created_at < since:
                    old_streak += 1
                    if old_streak >= OLD_STREAK_STOP:
                        print(f"[listing:fallback] stop: {old_streak} consecutive posts older than window")
                        print(f"[listing:fallback] skipped_future={skipped_future}")
                        await browser.close()
                        return selected[:top_n]
                    continue
                old_streak = 0
                selected.append(post)
                if len(selected) >= top_n:
                    print(f"[listing:fallback] reached top_n={top_n}")
                    await browser.close()
                    return selected
        await browser.close()
    print(f"[listing:fallback] skipped_future={skipped_future}")
    return selected[:top_n]


async def fetch_top_comments(page, post: RedditPost, limit: int = 8, force_old_reddit: bool = False) -> list[dict]:
    if force_old_reddit:
        return await fetch_top_comments_old_html(page, post, limit)
    url = f"{post.permalink}.json?{urlencode({'sort': 'top', 'limit': str(limit), 'raw_json': '1'})}"
    try:
        data = await fetch_json_browser(page, url)
    except Exception as exc:
        print(f"[comments] reddit JSON failed for {post.post_id}, falling back to old Reddit HTML: {exc}", file=sys.stderr)
        return await fetch_top_comments_old_html(page, post, limit)
    if not isinstance(data, list) or len(data) < 2:
        return []
    comments = []
    for child in (((data[1] or {}).get("data") or {}).get("children") or []):
        if child.get("kind") != "t1":
            continue
        item = child.get("data") or {}
        body = str(item.get("body") or "").strip()
        if not body or body in {"[deleted]", "[removed]"}:
            continue
        comments.append(
            {
                "author": str(item.get("author") or "[deleted]"),
                "score": int(item.get("score") or 0),
                "created_at": reddit_datetime(float(item.get("created_utc") or 0)).isoformat(timespec="minutes"),
                "body": body,
            }
        )
        if len(comments) >= limit:
            break
    return comments


async def fetch_top_comments_old_html(page, post: RedditPost, limit: int = 8) -> list[dict]:
    path = urlparse(post.permalink).path
    url = f"https://old.reddit.com{path}?sort=top"
    response = await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
    if not response or response.status >= 400:
        print(f"[comments] old Reddit fallback failed for {post.post_id}: HTTP status {response.status if response else 'unknown'}", file=sys.stderr)
        return []
    rows = await page.evaluate(
        """(limit) => Array.from(document.querySelectorAll('.commentarea .thing.comment')).slice(0, limit).map((el) => {
            const author = el.dataset.author || '[deleted]';
            const scoreText = el.querySelector('.score.unvoted')?.getAttribute('title') || el.querySelector('.score.unvoted')?.textContent || '0';
            const timeText = el.querySelector('time')?.getAttribute('datetime') || '';
            const body = Array.from(el.querySelectorAll('.usertext-body .md')).map((node) => node.innerText.trim()).filter(Boolean).join('\\n\\n');
            return {author, scoreText, timeText, body};
        })""",
        limit,
    )
    comments = []
    for row in rows:
        body = str(row.get("body") or "").strip()
        if not body or body in {"[deleted]", "[removed]"}:
            continue
        try:
            score = int(re.sub(r"[^0-9-]", "", str(row.get("scoreText") or "0")) or 0)
        except ValueError:
            score = 0
        created = str(row.get("timeText") or "")
        try:
            created_at = datetime.fromisoformat(created.replace("Z", "+00:00")).astimezone(LOCAL_TZ).replace(tzinfo=None).isoformat(timespec="minutes")
        except ValueError:
            created_at = created
        comments.append(
            {
                "author": str(row.get("author") or "[deleted]"),
                "score": score,
                "created_at": created_at,
                "body": body,
            }
        )
    return comments


def render_post_html(post: RedditPost, comments: list[dict]) -> str:
    selftext = post.selftext.strip() or "(link post)"
    comment_cards = []
    for comment in comments:
        comment_cards.append(
            f"""<article class="comment">
  <div class="comment-meta">u/{html.escape(comment['author'])} | score {comment['score']} | {html.escape(comment['created_at'])}</div>
  <div class="content">{html.escape(comment['body'])}</div>
</article>"""
        )
    if not comment_cards:
        comment_cards.append('<article class="comment"><div class="content">No top comments parsed.</div></article>')
    flags = " ".join(part for part in ["NSFW" if post.over_18 else "", "spoiler" if post.spoiler else ""] if part)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: Arial, "Microsoft YaHei", sans-serif; color: #202124; line-height: 1.55; }}
    h1 {{ font-size: 22px; margin: 0 0 10px; }}
    h2 {{ font-size: 17px; margin: 22px 0 8px; border-bottom: 1px solid #ddd; padding-bottom: 4px; }}
    .meta {{ color: #555; font-size: 12px; margin-bottom: 14px; }}
    .heat {{ border: 2px solid #cc4b21; background: #fff6f0; padding: 10px 12px; margin: 12px 0 16px; }}
    .heat-title {{ font-weight: 700; color: #9d3718; margin-bottom: 6px; }}
    .heat-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; font-size: 12px; }}
    .heat-metric {{ background: #fff; border: 1px solid #e5c6b7; padding: 6px; }}
    .heat-value {{ display: block; font-size: 18px; font-weight: 700; color: #202124; }}
    .content {{ white-space: pre-wrap; font-size: 13px; }}
    .post, .comment {{ border: 1px solid #ddd; border-radius: 4px; padding: 9px 11px; margin: 8px 0; page-break-inside: avoid; }}
    .comment-meta {{ color: #666; font-size: 12px; margin-bottom: 6px; }}
    a {{ color: #1f5f9f; text-decoration: none; overflow-wrap: anywhere; }}
  </style>
</head>
<body>
  <h1>{html.escape(post.title)}</h1>
  <div class="meta">
    Source: r/{html.escape(post.subreddit)} rising rank #{post.rising_rank} {html.escape(flags)}<br>
    Created: {post.created_at.isoformat(timespec="minutes")} |
    Score: {post.score} |
    Comments: {post.num_comments} |
    Upvote ratio: {post.upvote_ratio:.2f}<br>
    Author: u/{html.escape(post.author)} |
    Domain: {html.escape(post.domain)}<br>
    Reddit: <a href="{html.escape(post.permalink)}">{html.escape(post.permalink)}</a><br>
    Link: <a href="{html.escape(post.url)}">{html.escape(post.url)}</a>
  </div>
  <section class="heat">
    <div class="heat-title">Heat Overview: prioritize low Rising rank, high comments, and strong score</div>
    <div class="heat-grid">
      <div class="heat-metric"><span class="heat-value">#{post.rising_rank}</span>Rising rank</div>
      <div class="heat-metric"><span class="heat-value">{post.num_comments}</span>comments</div>
      <div class="heat-metric"><span class="heat-value">{post.score}</span>score</div>
      <div class="heat-metric"><span class="heat-value">{post.upvote_ratio:.2f}</span>upvote ratio</div>
    </div>
  </section>
  <h2>Post</h2>
  <article class="post"><div class="content">{html.escape(selftext)}</div></article>
  <h2>Top Comments</h2>
  {''.join(comment_cards)}
</body>
</html>"""


async def render_pdf(post: RedditPost, out_dir: Path, file_name: str, comments: list[dict]) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.set_content(render_post_html(post, comments), wait_until="domcontentloaded")
        await page.pdf(path=str(out_dir / file_name), format="A4", print_background=True, margin={"top": "10mm", "right": "8mm", "bottom": "10mm", "left": "8mm"})
        await browser.close()


async def save_posts(posts: list[RedditPost], out_dir: Path, *, force_old_reddit_comments: bool = False) -> tuple[int, int]:
    manifest = load_manifest(out_dir)
    manifest.setdefault("items", {})
    ok = 0
    fail = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        comments_page = await browser.new_page(user_agent=USER_AGENT)
        for post in posts:
            file_name = (
                f"{FILE_PREFIX}_{post.created_at.strftime('%Y-%m-%d')}_{post.post_id}_"
                f"{sanitize_filename(post.title)}.pdf"
            )
            existing = manifest["items"].get(post.post_id)
            if existing and existing.get("data_file"):
                print(f"[{post.post_id}] already saved, skip")
                ok += 1
            elif not save_pdf_enabled():
                try:
                    print(f"[{post.post_id}] extract text rank={post.rising_rank} score={post.score} comments={post.num_comments}")
                    comments = await fetch_top_comments(comments_page, post, force_old_reddit=force_old_reddit_comments)
                    html_text = render_post_html(post, comments)
                    write_article_record(
                        out_dir,
                        manifest,
                        post.post_id,
                        {
                            "source": SOURCE_DOMAIN,
                            "source_key": SOURCE_KEY,
                            "title": post.title,
                            "url": post.permalink,
                            "author": post.author,
                            "text": html_to_text(html_text),
                            "html": html_text,
                            "published_at": post.created_at.isoformat(timespec="seconds"),
                            "extra": {
                                "external_url": post.url,
                                "created_at": post.created_at.isoformat(timespec="seconds"),
                                "subreddit": post.subreddit,
                                "rising_rank": post.rising_rank,
                                "score": post.score,
                                "num_comments": post.num_comments,
                                "upvote_ratio": post.upvote_ratio,
                                "domain": post.domain,
                                "over_18": post.over_18,
                                "spoiler": post.spoiler,
                            },
                        },
                    )
                    ok += 1
                except Exception as exc:
                    print(f"[{post.post_id}] failed: {exc}", file=sys.stderr)
                    fail += 1
                    continue
            elif existing and existing.get("pdf_render_version") == PDF_RENDER_VERSION and (out_dir / existing.get("file", "")).exists():
                print(f"[{post.post_id}] already saved, skip")
                ok += 1
            else:
                try:
                    print(f"[{post.post_id}] render rank={post.rising_rank} score={post.score} comments={post.num_comments}")
                    comments = await fetch_top_comments(comments_page, post, force_old_reddit=force_old_reddit_comments)
                    await render_pdf(post, out_dir, file_name, comments)
                    ok += 1
                except Exception as exc:
                    print(f"[{post.post_id}] failed: {exc}", file=sys.stderr)
                    fail += 1
                    continue
            if not save_pdf_enabled():
                save_manifest(out_dir, manifest)
                continue
            manifest["items"][post.post_id] = {
                "file": file_name,
                "source": SOURCE_DOMAIN,
                "source_key": SOURCE_KEY,
                "title": post.title,
                "url": post.permalink,
                "external_url": post.url,
                "published_at": post.created_at.isoformat(timespec="seconds"),
                "created_at": post.created_at.isoformat(timespec="seconds"),
                "subreddit": post.subreddit,
                "rising_rank": post.rising_rank,
                "score": post.score,
                "num_comments": post.num_comments,
                "upvote_ratio": post.upvote_ratio,
                "author": post.author,
                "domain": post.domain,
                "over_18": post.over_18,
                "spoiler": post.spoiler,
                "pdf_render_version": PDF_RENDER_VERSION,
                "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
            save_manifest(out_dir, manifest)
        await browser.close()
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
    print(f"[config] window: {since} <= created < {until}")
    print(f"[config] output: {out_dir}")
    print(f"[config] listing: /r/{SUBREDDIT}/rising, preserving Reddit rising order")
    posts, json_blocked = await collect_posts(since, until, args.max_pages, top_n)
    print(f"[listing] selected {len(posts)} post(s)")
    if not posts:
        print("[listing] no Reddit posts collected; source may be quiet or temporarily blocked")
    if json_blocked:
        print("[comments] listing JSON was blocked; using old Reddit HTML for comment extraction")
    ok, fail = await save_posts(posts, out_dir, force_old_reddit_comments=json_blocked)
    print(f"[done] ok={ok} fail={fail} output={out_dir}")
    return 1 if fail else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect rising r/gaming Reddit posts.")
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="yesterday")
    parser.add_argument("--since", default="")
    parser.add_argument("--until", default="")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--max-pages", type=int, default=5)
    parser.add_argument("--limit", type=int, default=0, help="Debug/top-N limit. Defaults to 20.")
    parser.add_argument("--headful", action="store_true", help="Accepted for runner compatibility; ignored.")
    args = parser.parse_args()
    return asyncio.run(amain(args))


if __name__ == "__main__":
    raise SystemExit(main())
