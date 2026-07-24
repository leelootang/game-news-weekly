"""Collect cards added to Cubox during the requested local-time window.

Cubox is used as a personal curation inbox. Discovery is based on the card's
``create_time`` while the full parsed Markdown body comes from
``cubox-cli card detail``. Records keep the original page URL as their
auditable source URL and store Cubox-specific metadata under ``extra``.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from article_store import write_article_record
from manifest_paths import collector_manifest_path, collector_run_manifest_dir, legacy_manifest_paths


SOURCE_KEY = "cubox"
SOURCE_DOMAIN = "cubox.pro"
SECTION = "industry_news"
MANIFEST_NAME = f"{SOURCE_KEY}_{SOURCE_DOMAIN}_manifest.json"
MANIFEST_DIR_NAME = "_collector_manifests"
LOCAL_TZ = timezone(timedelta(hours=8))
CLI_TIMEOUT_SECONDS = 120


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


def parse_date(value: str) -> datetime:
    raw = value.strip()
    if not raw:
        raise ValueError("date value is empty")
    parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return parsed


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


def parse_cubox_datetime(value: str) -> datetime | None:
    raw = (value or "").strip()
    if not raw:
        return None
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone(LOCAL_TZ).replace(tzinfo=None)
    return parsed


def format_cli_datetime(value: datetime) -> str:
    aware = value.replace(tzinfo=LOCAL_TZ) if value.tzinfo is None else value.astimezone(LOCAL_TZ)
    return aware.isoformat(timespec="seconds")


def find_cubox_cli() -> Path:
    configured = os.environ.get("CUBOX_CLI", "").strip()
    candidates: list[Path] = []
    if configured:
        candidates.append(Path(configured))

    for command in ("cubox-cli", "cubox-cli.cmd"):
        resolved = shutil.which(command)
        if resolved:
            candidates.append(Path(resolved))

    npm = shutil.which("npm.cmd") or shutil.which("npm")
    if npm:
        try:
            result = subprocess.run(
                [npm, "prefix", "-g"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            result = None
        if result and result.returncode == 0 and result.stdout.strip():
            prefix = Path(result.stdout.strip())
            candidates.extend((prefix / "cubox-cli.cmd", prefix / "cubox-cli"))

    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise RuntimeError(
        "cubox-cli was not found. Install it with 'npm install -g cubox-cli', "
        "or set CUBOX_CLI to the executable path."
    )


def run_cli_json(cli: Path, arguments: list[str]) -> Any:
    try:
        result = subprocess.run(
            [str(cli), *arguments],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=CLI_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"cubox-cli timed out after {CLI_TIMEOUT_SECONDS}s") from exc
    except OSError as exc:
        raise RuntimeError(f"failed to start cubox-cli: {exc}") from exc

    output = result.stdout.strip()
    if result.returncode != 0:
        message = result.stderr.strip() or output or f"exit code {result.returncode}"
        raise RuntimeError(f"cubox-cli failed: {message}")
    try:
        return json.loads(output or "null")
    except json.JSONDecodeError as exc:
        raise RuntimeError("cubox-cli returned invalid JSON") from exc


def list_created_cards(
    cli: Path,
    since: datetime,
    until: datetime,
    *,
    limit: int = 0,
) -> list[dict[str, Any]]:
    arguments = [
        "card",
        "list",
        "--start-time",
        format_cli_datetime(since),
        "--end-time",
        format_cli_datetime(until),
    ]
    if limit > 0:
        arguments.extend(["--limit", str(limit)])
    else:
        arguments.append("--all")
    arguments.extend(["-o", "json"])

    payload = run_cli_json(cli, arguments)
    if payload is None:
        return []
    if not isinstance(payload, list):
        raise RuntimeError("cubox-cli card list returned an unexpected JSON shape")
    return [item for item in payload if isinstance(item, dict)]


def get_card_detail(cli: Path, card_id: str) -> dict[str, Any]:
    payload = run_cli_json(cli, ["card", "detail", "--id", card_id, "-o", "json"])
    if not isinstance(payload, dict):
        raise RuntimeError(f"cubox-cli card detail returned an unexpected JSON shape for {card_id}")
    return payload


def normalize_card(detail: dict[str, Any]) -> dict[str, Any]:
    card_id = str(detail.get("id") or "").strip()
    title = str(detail.get("article_title") or detail.get("title") or "").strip()
    url = str(detail.get("url") or "").strip()
    content = str(detail.get("content") or "").strip()
    created_at = parse_cubox_datetime(str(detail.get("create_time") or ""))
    if not card_id:
        raise ValueError("missing card id")
    if not title:
        raise ValueError(f"card {card_id} has no title")
    if not url:
        raise ValueError(f"card {card_id} has no original URL")
    if not content:
        raise ValueError(f"card {card_id} has no parsed content")
    if created_at is None:
        raise ValueError(f"card {card_id} has invalid create_time")

    parsed_url = urlparse(url)
    source = (detail.get("domain") or parsed_url.netloc or SOURCE_DOMAIN).strip().lower()
    folder = detail.get("folder") if isinstance(detail.get("folder"), dict) else {}
    tags = detail.get("tags") if isinstance(detail.get("tags"), list) else []
    return {
        "id": card_id,
        "source": source,
        "source_key": SOURCE_KEY,
        "section": SECTION,
        "title": title,
        "url": url,
        "author": str(detail.get("author") or "").strip(),
        "excerpt": str(detail.get("description") or "").strip(),
        "text": content,
        "html": "",
        # The daily window is intentionally the time this card entered Cubox.
        "published_at": created_at.isoformat(timespec="seconds"),
        "extra": {
            "via_cubox": True,
            "cubox_card_id": card_id,
            "cubox_create_time": detail.get("create_time") or "",
            "cubox_update_time": detail.get("update_time") or "",
            "cubox_read": bool(detail.get("read")),
            "cubox_starred": bool(detail.get("starred")),
            "cubox_folder": folder.get("nested_name") or folder.get("name") or "",
            "cubox_tags": [str(tag) for tag in tags],
        },
    }


def load_manifest(out_dir: Path) -> dict[str, Any]:
    path = collector_manifest_path(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME)
    for legacy_path in legacy_manifest_paths(out_dir, MANIFEST_DIR_NAME, MANIFEST_NAME):
        if not path.exists() and legacy_path.exists():
            path = legacy_path
            break
    if not path.exists():
        return {"items": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {"items": {}}


def save_manifest(out_dir: Path, manifest: dict[str, Any]) -> None:
    manifest_dir = collector_run_manifest_dir(out_dir, MANIFEST_DIR_NAME)
    manifest_dir.mkdir(parents=True, exist_ok=True)
    path = manifest_dir / MANIFEST_NAME
    tmp = manifest_dir / f".{MANIFEST_NAME}.tmp"
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect cards added to Cubox in a local-time window.")
    parser.add_argument("--out", type=Path, default=Path("./news_data"))
    parser.add_argument("--preset", choices=("last-7-days", "yesterday", "today"), default="last-7-days")
    parser.add_argument("--since", type=str, default="")
    parser.add_argument("--until", type=str, default="")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-pages", type=int, default=1, help="Accepted for runner compatibility.")
    parser.add_argument("--headful", action="store_true", help="Unused; CLI compatibility.")
    args = parser.parse_args()

    since, until = preset_window(args.preset)
    if args.since:
        since = parse_date(args.since)
    if args.until:
        until = parse_date(args.until)
    if since >= until:
        raise SystemExit("--since must be earlier than --until")

    args.out.mkdir(parents=True, exist_ok=True)
    try:
        cli = find_cubox_cli()
        cards = list_created_cards(cli, since, until, limit=args.limit)
    except RuntimeError as exc:
        raise SystemExit(f"[cubox] {exc}") from exc

    manifest = load_manifest(args.out)
    print(f"[config] window: {since} <= Cubox create_time < {until}")
    print(f"[cubox] discovered={len(cards)}")

    saved = 0
    failures = 0
    for card in cards:
        card_id = str(card.get("id") or "").strip()
        if not card_id:
            failures += 1
            print("[cubox] list item missing id", file=sys.stderr)
            continue
        try:
            normalized = normalize_card(get_card_detail(cli, card_id))
            created_at = parse_cubox_datetime(normalized["extra"]["cubox_create_time"])
            if created_at is None or not (since <= created_at < until):
                raise ValueError(f"card {card_id} create_time fell outside the requested window")
            write_article_record(args.out, manifest, card_id, normalized)
        except (RuntimeError, ValueError) as exc:
            failures += 1
            print(f"[cubox] failed card {card_id}: {exc}", file=sys.stderr)
            continue
        saved += 1
        print(f"[{card_id}] saved {normalized['published_at']} {normalized['title'][:60]}")

    save_manifest(args.out, manifest)
    print(f"[done] saved={saved} failures={failures} output={args.out.resolve()}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
