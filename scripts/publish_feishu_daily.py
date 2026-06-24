from __future__ import annotations

import argparse
import os
import sys
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
    read_json,
    report_paths,
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
    doc_name = summary.get("title") or f"游戏行业日报 {date}"
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


def publish(args: argparse.Namespace) -> int:
    load_dotenv()
    summary = load_report_summary(args.date)
    markdown_path, _, _ = report_paths(args.date)
    folder_token = resolve_folder_token(args.folder_token) if args.create_doc else None

    subscribers = [{"open_id": args.to_open_id}] if args.to_open_id else active_subscribers()
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
