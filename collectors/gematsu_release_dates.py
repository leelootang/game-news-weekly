"""
Fetch Gematsu release-date posts and store them as release-calendar records.

Gematsu's front-end is protected by Cloudflare in this environment. This
collector therefore uses Google News RSS indexing by default, then falls back to
the official WordPress feeds and Jina Reader text rendering only if the index
returns no usable posts.
"""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import re
import ssl
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

from article_store import html_to_text, write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths


BASE_URL = "https://www.gematsu.com"
TAG_URL = "https://www.gematsu.com/tag/release-dates"
READER_TAG_URL = f"https://r.jina.ai/{TAG_URL}"
FEED_URLS = [
    "https://www.gematsu.com/tag/release-dates/feed",
    "https://www.gematsu.com/rss/",
    "https://www.gematsu.com/feed",
]
GOOGLE_NEWS_QUERIES = [
    "gematsu release date game",
    "gematsu launches game",
    "gematsu now available game",
    "gematsu delayed game",
]
SOURCE_DOMAIN = "gematsu.com"
SOURCE_KEY = "gematsu_release_dates"
FILE_PREFIX = f"{SOURCE_KEY}_{SOURCE_DOMAIN}"
MANIFEST_NAME = f"{FILE_PREFIX}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


@dataclass(frozen=True)
class ReleasePost:
    event_id: str
    url: str
    title: str
    published_at: datetime
    excerpt: str
    platforms: list[str]
    release_date_text: str
    release_date: datetime | None
    fetch_method: str


def parse_date(value: str, *, end_of_day: bool = False) -> datetime:
    raw = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        parsed = datetime.fromisoformat(raw)
        if end_of_day:
            return parsed + timedelta(days=1)
        return parsed
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


def load_manifest(out_dir: Path) -> dict:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    legacy_paths = legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_paths:
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


def fetch_text(url: str, *, insecure_tls: bool = False) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,text/plain;q=0.8,*/*;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    context = ssl._create_unverified_context() if insecure_tls else None
    with urlopen(request, timeout=45, context=context) as response:
        return response.read().decode("utf-8-sig", errors="replace")


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def parse_datetime(value: str) -> datetime | None:
    if not value:
        return None
    parsed = email.utils.parsedate_to_datetime(value)
    if parsed is None:
        return None
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone(timezone.utc).replace(tzinfo=None)
    return parsed.replace(microsecond=0)


def relative_datetime(value: str, *, now: datetime) -> datetime | None:
    text = re.sub(r"\d+$", "", clean_text(value).lower()).strip()
    if text in {"now", "just now"}:
        return now
    match = re.search(r"(\d+)\s+(minute|hour|day|week|month|year)s?\s+ago", text)
    if not match:
        return None
    amount = int(match.group(1))
    unit = match.group(2)
    if unit == "minute":
        return now - timedelta(minutes=amount)
    if unit == "hour":
        return now - timedelta(hours=amount)
    if unit == "day":
        return now - timedelta(days=amount)
    if unit == "week":
        return now - timedelta(weeks=amount)
    if unit == "month":
        return now - timedelta(days=30 * amount)
    if unit == "year":
        return now - timedelta(days=365 * amount)
    return None


def extract_release_date(text: str, *, reference: datetime) -> tuple[str, datetime | None]:
    compact = clean_text(text)
    explicit = re.search(
        r"\b("
        + "|".join(MONTHS)
        + r")\s+(\d{1,2})(?:st|nd|rd|th)?(?:,\s*(20\d{2}))?\b",
        compact,
        flags=re.I,
    )
    if explicit:
        month_name, day_text, year_text = explicit.groups()
        month = MONTHS[month_name.lower()]
        day = int(day_text)
        year = int(year_text) if year_text else reference.year
        try:
            date_value = datetime(year, month, day)
        except ValueError:
            date_value = None
        return explicit.group(0), date_value

    year_only = re.search(r"\b(20\d{2})\b", compact)
    if year_only:
        return year_only.group(1), None
    vague = re.search(r"\b(Q[1-4]|early|spring|summer|fall|autumn|winter)\s+(20\d{2})\b", compact, flags=re.I)
    if vague:
        return vague.group(0), None
    return "", None


def make_event_id(url: str, title: str, published_at: datetime) -> str:
    slug = url.rstrip("/").rsplit("/", 1)[-1] if url else title
    digest = hashlib.sha1(f"{url}|{title}|{published_at:%Y-%m-%dT%H:%M:%S}".encode("utf-8")).hexdigest()[:10]
    return f"{slug[:64]}_{published_at:%Y%m%d}_{digest}"


def release_signal(title: str) -> bool:
    return bool(
        re.search(
            r"\b(launches|launch|release date|now available|delayed|due out|set for|coming|physical edition)\b",
            title,
            flags=re.I,
        )
    )


def parse_feed_items(xml_text: str, *, fetch_method: str = "feed", require_release_signal: bool = False) -> list[ReleasePost]:
    root = ET.fromstring(xml_text)
    posts: list[ReleasePost] = []
    for item in root.findall(".//item"):
        title = clean_text(item.findtext("title") or "")
        url = clean_text(item.findtext("link") or "")
        pub_date = parse_datetime(item.findtext("pubDate") or "")
        if not title or not url or pub_date is None:
            continue
        if require_release_signal and not release_signal(title):
            continue
        description = html_to_text(item.findtext("description") or "")
        categories = [
            clean_text(category.text or "")
            for category in item.findall("category")
            if clean_text(category.text or "")
        ]
        release_text, release_date = extract_release_date(f"{title}. {description}", reference=pub_date)
        posts.append(
            ReleasePost(
                event_id=make_event_id(url, title, pub_date),
                url=url,
                title=title,
                published_at=pub_date,
                excerpt=description,
                platforms=categories,
                release_date_text=release_text,
                release_date=release_date,
                fetch_method=fetch_method,
            )
        )
    return posts


def parse_reader_markdown(markdown: str, *, now: datetime) -> list[ReleasePost]:
    lines = markdown.splitlines()
    posts: list[ReleasePost] = []
    platforms: list[str] = []
    relative_line = ""
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if line.startswith("* "):
            platforms.append(line[2:].strip())
            index += 1
            continue
        if re.search(r"\b(?:minute|hour|day|week|month|year)s?\s+ago\d*$", line.lower()):
            relative_line = line
            index += 1
            continue

        heading = re.match(r"##\s+(?:\[([^\]]+)\]\(([^)]+)\)|(.+))$", line)
        if heading:
            title = clean_text(heading.group(1) or heading.group(3) or "")
            href = clean_text(heading.group(2) or "")
            excerpt_lines: list[str] = []
            index += 1
            while index < len(lines):
                next_line = lines[index].strip()
                if next_line.startswith("* ") or next_line.startswith("## ") or re.match(r"^\d+\s+\d+", next_line):
                    break
                if next_line and not next_line.startswith("#"):
                    excerpt_lines.append(next_line)
                index += 1
            published_at = relative_datetime(relative_line, now=now) or now
            url = urljoin(BASE_URL, href) if href else TAG_URL
            excerpt = clean_text(" ".join(excerpt_lines))
            release_text, release_date = extract_release_date(f"{title}. {excerpt}", reference=published_at)
            posts.append(
                ReleasePost(
                    event_id=make_event_id(url, title, published_at),
                    url=url,
                    title=title,
                    published_at=published_at,
                    excerpt=excerpt,
                    platforms=list(dict.fromkeys(platforms)),
                    release_date_text=release_text,
                    release_date=release_date,
                    fetch_method="reader",
                )
            )
            platforms = []
            relative_line = ""
            continue

        if line and not line.startswith("#"):
            platforms = []
        index += 1
    return posts


def collect_posts() -> list[ReleasePost]:
    errors: list[str] = []
    google_posts: dict[str, ReleasePost] = {}
    for query in GOOGLE_NEWS_QUERIES:
        url = "https://news.google.com/rss/search?" + urlencode(
            {"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"}
        )
        try:
            feed_text = fetch_text(url)
            posts = parse_feed_items(
                feed_text,
                fetch_method="google_news",
                require_release_signal=True,
            )
            print(f"[google_news] {query}: parsed={len(posts)}")
            for post in posts:
                normalized_title = re.sub(r"\s+-\s+Gematsu\s*$", "", post.title, flags=re.I).strip()
                key = normalized_title.lower()
                google_posts[key] = ReleasePost(
                    event_id=post.event_id,
                    url=post.url,
                    title=normalized_title or post.title,
                    published_at=post.published_at,
                    excerpt=post.excerpt,
                    platforms=post.platforms,
                    release_date_text=post.release_date_text,
                    release_date=post.release_date,
                    fetch_method=post.fetch_method,
                )
        except (HTTPError, URLError, ET.ParseError, OSError, UnicodeDecodeError) as exc:
            errors.append(f"Google News query={query}: {type(exc).__name__}: {exc}")
            print(f"[google_news] failed {query}: {exc}", file=sys.stderr)
    if google_posts:
        return list(google_posts.values())

    for feed_url in FEED_URLS:
        try:
            feed_text = fetch_text(feed_url)
            posts = parse_feed_items(feed_text)
            print(f"[feed] {feed_url}: parsed={len(posts)}")
            if posts:
                return posts
        except (HTTPError, URLError, ET.ParseError, OSError, UnicodeDecodeError) as exc:
            errors.append(f"{feed_url}: {type(exc).__name__}: {exc}")
            print(f"[feed] failed {feed_url}: {exc}", file=sys.stderr)

    for insecure_tls in (False, True):
        try:
            markdown = fetch_text(READER_TAG_URL, insecure_tls=insecure_tls)
            posts = parse_reader_markdown(markdown, now=datetime.now().replace(microsecond=0))
            print(f"[reader] {READER_TAG_URL}: parsed={len(posts)} insecure_tls={insecure_tls}")
            if posts:
                return posts
        except (HTTPError, URLError, OSError, UnicodeDecodeError) as exc:
            errors.append(f"{READER_TAG_URL} insecure_tls={insecure_tls}: {type(exc).__name__}: {exc}")
            print(f"[reader] failed insecure_tls={insecure_tls}: {exc}", file=sys.stderr)

    print("[warning] Gematsu fetch failed. " + " | ".join(errors[-4:]), file=sys.stderr)
    return []


def post_text(post: ReleasePost) -> str:
    rows = [
        ("Title", post.title),
        ("Announcement date", post.published_at.strftime("%Y-%m-%d %H:%M")),
        ("Release date text", post.release_date_text),
        ("Parsed release date", post.release_date.strftime("%Y-%m-%d") if post.release_date else ""),
        ("Platforms", " / ".join(post.platforms)),
        ("Source method", post.fetch_method),
        ("Original URL", post.url),
        ("Excerpt", post.excerpt),
    ]
    return "\n".join(f"{label}: {value}" for label, value in rows if value)


def save_post(out_dir: Path, manifest: dict, post: ReleasePost) -> None:
    write_article_record(
        out_dir,
        manifest,
        post.event_id,
        {
            "source": SOURCE_DOMAIN,
            "source_key": SOURCE_KEY,
            "title": post.title,
            "url": post.url,
            "text": post_text(post),
            "published_at": post.published_at.isoformat(timespec="seconds"),
            "extra": {
                "platforms": post.platforms,
                "release_date_text": post.release_date_text,
                "release_date": post.release_date.isoformat(timespec="seconds") if post.release_date else "",
                "fetch_method": post.fetch_method,
                "excerpt": post.excerpt,
            },
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Gematsu release-date posts.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"), help="Output directory")
    parser.add_argument(
        "--preset",
        choices=("last-7-days", "yesterday", "today"),
        default="last-7-days",
        help="Date window preset. Ignored by --since/--until overrides.",
    )
    parser.add_argument("--since", type=str, default="", help="Start date/time, inclusive. Example: 2026-06-01")
    parser.add_argument("--until", type=str, default="", help="End date/time, exclusive. Example: 2026-06-02")
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility")
    parser.add_argument("--limit", type=int, default=0, help="Optional maximum posts to export")
    parser.add_argument("--headful", action="store_true", help="Accepted for runner compatibility")
    args = parser.parse_args()

    try:
        since, until = preset_window(args.preset)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if args.since:
        since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    if args.max_pages != 1:
        print("[config] Gematsu release-dates feed is a recency stream; --max-pages is accepted for compatibility")

    args.out.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(args.out)
    print(f"[config] window: {since} <= published < {until}")
    print(f"[config] output: {args.out.resolve()}")

    started = time.monotonic()
    posts = [post for post in collect_posts() if since <= post.published_at < until]
    posts.sort(key=lambda item: (item.published_at, item.title), reverse=True)
    if args.limit > 0:
        posts = posts[: args.limit]
    print(f"[gematsu] exporting {len(posts)} post(s)")

    for post in posts:
        save_post(args.out, manifest, post)
        print(f"[{post.event_id}] saved text record: {post.title}")
    save_manifest(args.out, manifest)
    elapsed = time.monotonic() - started
    print(f"[done] ok={len(posts)} fail=0 elapsed={elapsed:.1f}s output={args.out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
