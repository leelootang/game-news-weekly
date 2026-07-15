from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from feishu_common import (
    FeishuClient,
    PUBLISH_LOG_DIR,
    active_subscribers,
    add_date_arg,
    build_daily_card,
    build_docx_markdown,
    content_hash,
    load_dotenv,
    load_report_summary,
    mark_subscriber_pushed,
    read_json,
    report_paths,
    resolve_report,
    utc_now_iso,
    write_json,
)


def existing_doc_for_date(date: str) -> dict[str, str] | None:
    """Return {token, url} of the docx already created for this date (recorded
    in the publish log) so re-pushes reuse the same document instead of
    spawning a new one — we keep one docx per date and edit it in place
    (Feishu keeps edit history). Returns None when no doc exists yet."""
    log = read_json(PUBLISH_LOG_DIR / f"daily_{date}.json", None)
    if isinstance(log, dict) and log.get("doc_token") and log.get("doc_url"):
        return {"token": log["doc_token"], "url": log["doc_url"]}
    return None


def latest_broadcast_today() -> tuple[str, dict] | None:
    """Find the report broadcast to subscribers today (any kind: daily / weekly /
    weekend) by scanning publish logs for one whose published_at falls on today's
    local date. Returns (identifier, log) for the most recent, or None when no
    broadcast has happened yet today. Used to catch up late subscribers with
    exactly the report everyone else received today, not a guessed date."""
    today = datetime.now().strftime("%Y-%m-%d")
    best: tuple[str, dict] | None = None
    for log_path in PUBLISH_LOG_DIR.glob("daily_*.json"):
        log = read_json(log_path, None)
        if not isinstance(log, dict) or not log.get("doc_url"):
            continue
        if (log.get("published_at") or "")[:10] != today:
            continue
        identifier = log.get("date")
        if not identifier:
            continue
        if best is None or (log.get("published_at") or "") > (best[1].get("published_at") or ""):
            best = (identifier, log)
    return best


def latest_published_report(kind: str) -> tuple[str, dict] | None:
    """Return the most recently published report of *kind*.

    The menu should replay a report that was actually published, so its card
    keeps the same Feishu docx link as the original broadcast.  Publish logs
    are the source of truth for that distinction; scanning output folders
    alone could surface a report that has not been reviewed or sent yet.
    """
    if kind not in {"daily", "weekly", "weekend"}:
        raise ValueError(f"Unsupported report kind: {kind}")

    latest: tuple[str, dict] | None = None
    for log_path in PUBLISH_LOG_DIR.glob("daily_*.json"):
        log = read_json(log_path, None)
        if not isinstance(log, dict):
            continue
        identifier = str(log.get("date", "")).strip()
        if not identifier or not log.get("doc_url"):
            continue
        try:
            report_kind, _report_dir, markdown_path = resolve_report(identifier)
        except ValueError:
            continue
        if report_kind != kind or not markdown_path.exists():
            continue
        if latest is None or (log.get("published_at") or "", identifier) > (
            latest[1].get("published_at") or "", latest[0]
        ):
            latest = (identifier, log)
    return latest


def send_latest_report(
    client: FeishuClient, open_id: str, kind: str, *, max_items: int = 10
) -> str | None:
    """Send one user the latest already-published card of the requested kind."""
    latest = latest_published_report(kind)
    if latest is None:
        labels = {"daily": "日报", "weekly": "周报", "weekend": "周末报"}
        client.send_text(open_id, f"暂未找到可推送的最新{labels.get(kind, '报告')}。")
        return None

    identifier, log = latest
    summary = load_report_summary(identifier)
    card = build_daily_card(summary, doc_url=log["doc_url"], per_section=max_items)
    client.send_interactive_card(open_id, card)
    return identifier


def resolve_doc_url(date: str, explicit: str | None) -> str | None:
    if explicit:
        return explicit
    template = os.environ.get("FEISHU_DAILY_DOC_URL_TEMPLATE", "").strip()
    if template:
        return template.format(date=date)
    return None


def create_daily_doc(
    client: FeishuClient, date: str, summary: dict, folder_token: str
) -> dict[str, str]:
    markdown_path = Path(summary["markdown_path"])
    if not markdown_path.exists():
        raise FileNotFoundError(f"Daily report markdown not found: {markdown_path}")
    doc_name = summary.get("title") or f"游戏行业{summary.get('noun', '日报')} {date}"
    import_path = build_docx_markdown(date)
    file_token = client.upload_import_media(import_path, import_path.name)
    ticket = client.create_import_task(file_token, doc_name, folder_token)
    result = client.poll_import_task(ticket)
    client.set_doc_public_permission(result["token"], doc_type="docx")
    return result


def resolve_folder_token(explicit: str | None) -> str | None:
    if explicit:
        return explicit
    return os.environ.get("FEISHU_DAILY_FOLDER_TOKEN", "").strip() or None


def backfill_one(
    client: FeishuClient, open_id: str, date: str | None = None, *, max_items: int = 6
) -> str | None:
    """Send a single subscriber the card+doc for `date` (default: today),
    reusing the docx already created for that date. Used to immediately catch up
    a subscriber who joined after the daily broadcast. Raises FileNotFoundError
    when the report for the date has not been generated yet. Marks the
    subscriber pushed and returns the doc_url used (may be None)."""
    load_dotenv()
    date = date or datetime.now().strftime("%Y-%m-%d")
    summary = load_report_summary(date)
    existing = existing_doc_for_date(date)
    if existing:
        doc_url = existing["url"]
    else:
        folder_token = resolve_folder_token(None)
        if folder_token:
            doc_url = create_daily_doc(client, date, summary, folder_token)["url"]
        else:
            doc_url = resolve_doc_url(date, None)
    card = build_daily_card(summary, doc_url=doc_url, per_section=max_items)
    client.send_interactive_card(open_id, card)
    mark_subscriber_pushed(open_id, date, summary["kind"])
    return doc_url


def publish(args: argparse.Namespace) -> int:
    load_dotenv()
    summary = load_report_summary(args.date)
    markdown_path, _, _ = report_paths(args.date)
    folder_token = resolve_folder_token(args.folder_token) if args.create_doc else None

    subscribers = (
        [{"open_id": args.to_open_id}]
        if args.to_open_id
        else active_subscribers(summary["kind"])
    )
    if args.dry_run:
        print(f"[dry-run] date: {args.date}")
        print(f"[dry-run] title: {summary['title']}")
        print(f"[dry-run] subscribers: {len(subscribers)}")
        print(f"[dry-run] markdown: {markdown_path}")
        if args.create_doc:
            existing = None if args.new_doc else existing_doc_for_date(args.date)
            if existing:
                print(f"[dry-run] would REUSE existing docx: {existing['url']}")
            else:
                print(f"[dry-run] would create docx in folder: {folder_token or '(MISSING folder token!)'}")
        else:
            print(f"[dry-run] doc_url: {resolve_doc_url(args.date, args.doc_url) or '(none)'}")
        return 0

    if not subscribers:
        print("No active subscribers found. Ask a user to send “订阅日报” first.")
        return 0

    client = FeishuClient.from_env()

    doc_token = None
    if args.create_doc:
        existing = None if args.new_doc else existing_doc_for_date(args.date)
        if existing:
            doc_url = existing["url"]
            doc_token = existing["token"]
            print(f"[doc] reusing existing docx token={doc_token} url={doc_url}")
        else:
            if not folder_token:
                print("--create-doc requires a folder token (pass --folder-token or set FEISHU_DAILY_FOLDER_TOKEN).")
                return 1
            created = create_daily_doc(client, args.date, summary, folder_token)
            doc_url = created["url"]
            doc_token = created["token"]
            print(f"[doc] created docx token={doc_token} url={doc_url}")
    else:
        doc_url = resolve_doc_url(args.date, args.doc_url)

    card = build_daily_card(summary, doc_url=doc_url, per_section=args.max_items)
    results = []
    for subscriber in subscribers:
        open_id = subscriber["open_id"]
        try:
            response = client.send_interactive_card(open_id, card)
            results.append({"open_id": open_id, "ok": True, "response": response})
            print(f"[sent] {open_id}")
        except Exception as exc:
            results.append({"open_id": open_id, "ok": False, "error": str(exc)})
            print(f"[failed] {open_id}: {exc}")

    if not args.to_open_id:
        for row in results:
            if row["ok"]:
                mark_subscriber_pushed(row["open_id"], args.date, summary["kind"])

    log = {
        "date": args.date,
        "published_at": utc_now_iso(),
        "doc_url": doc_url,
        "doc_token": doc_token,
        "content_hash": content_hash(Path(summary["markdown_path"])) if markdown_path.exists() else None,
        "subscriber_count": len(subscribers),
        "results": results,
    }
    write_json(PUBLISH_LOG_DIR / f"daily_{args.date}.json", log)
    failed = [row for row in results if not row["ok"]]
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a daily report card to Feishu subscribers.")
    add_date_arg(parser)
    parser.add_argument("--doc-url", help="Feishu document URL to attach to the card.")
    parser.add_argument(
        "--create-doc",
        action="store_true",
        help="Import the daily markdown into a Feishu docx and use its URL (overrides --doc-url).",
    )
    parser.add_argument(
        "--folder-token",
        help="Target Feishu drive folder token for --create-doc (defaults to FEISHU_DAILY_FOLDER_TOKEN).",
    )
    parser.add_argument(
        "--new-doc",
        action="store_true",
        help="Force a brand-new docx even if one already exists for the date (default: reuse).",
    )
    parser.add_argument("--to-open-id", help="Send to one open_id for testing instead of all subscribers.")
    parser.add_argument("--max-items", type=int, default=6, help="Max items shown per section in the card.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without sending anything.")
    return publish(parser.parse_args())


if __name__ == "__main__":
    sys.exit(main())
