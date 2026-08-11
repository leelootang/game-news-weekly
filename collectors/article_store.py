from __future__ import annotations

import errno
import hashlib
import html
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ARTICLE_JSONL_NAME = "articles.jsonl"
ARTICLE_INDEX_NAME = "articles_index.md"
_PREVIEW_MARKERS = (
    "get the rest of this newsletter",
    "subscribe to continue reading",
    "sign in or subscribe to continue",
    "become a paid subscriber to read the rest",
    "this post is for paid subscribers",
)

# Each collector runs in its own subprocess (the runner launches them via
# subprocess.Popen), and many of them share one per-section articles.jsonl.
# write_article_record performs a read-modify-write of that shared file. Atomic
# replacement prevents torn files, but without serialization concurrent writers
# could still overwrite each other's rows. Guard the whole transaction with a
# cross-process lockfile keyed by the jsonl path.
_LOCK_STALE_SECONDS = 120.0
_LOCK_WAIT_SECONDS = 300.0


class _InterProcessLock:
    """Spin-wait exclusive lock backed by an O_EXCL lockfile (cross-platform)."""

    def __init__(self, target: Path) -> None:
        self.lockfile = Path(str(target) + ".lock")
        self.fd: int | None = None

    def __enter__(self) -> "_InterProcessLock":
        start = time.monotonic()
        while True:
            try:
                self.fd = os.open(str(self.lockfile), os.O_CREAT | os.O_EXCL | os.O_RDWR)
                os.write(self.fd, str(os.getpid()).encode("ascii"))
                return self
            except FileExistsError:
                try:
                    age = time.time() - self.lockfile.stat().st_mtime
                except OSError:
                    age = 0.0
                if age > _LOCK_STALE_SECONDS:
                    # Holder likely died without releasing; reclaim the lock.
                    try:
                        os.remove(self.lockfile)
                    except OSError:
                        pass
                    continue
                if time.monotonic() - start > _LOCK_WAIT_SECONDS:
                    # Never hang a collector forever; proceed unlocked as a last resort.
                    self.fd = None
                    return self
                time.sleep(0.05)

    def __exit__(self, *exc: Any) -> None:
        if self.fd is not None:
            os.close(self.fd)
            try:
                os.remove(self.lockfile)
            except OSError:
                pass
            self.fd = None


def _lock_for(path: Path) -> _InterProcessLock:
    return _InterProcessLock(path)


_IO_RETRY_ATTEMPTS = 6
_IO_RETRY_BASE_DELAY = 0.05


def _is_transient_io_error(exc: OSError) -> bool:
    """True for short-lived Windows filesystem errors worth retrying."""
    if isinstance(exc, PermissionError):
        return True
    if getattr(exc, "winerror", None) in (5, 32, 33, 87):
        # ERROR_INVALID_PARAMETER (87) has occasionally surfaced while several
        # collector processes replace the same section files. The exact same
        # payload succeeds immediately in isolation, so treat it as transient.
        return True
    if exc.errno == errno.EACCES:
        return True
    return os.name == "nt" and exc.errno == errno.EINVAL


def _retry_io(fn):
    """Run a file operation, retrying transient Windows failures.

    Collectors in the same section rewrite a shared articles.jsonl / index. The
    cross-process lockfile serializes intent, but on Windows the OS or AV can
    still briefly hold a handle just after another writer released the lock,
    surfacing as PermissionError(13) / ERROR_SHARING_VIOLATION. These clear in
    milliseconds, so retry with a short backoff instead of failing the record.
    """
    last: OSError | None = None
    for attempt in range(_IO_RETRY_ATTEMPTS):
        try:
            return fn()
        except OSError as exc:
            if not _is_transient_io_error(exc):
                raise
            last = exc
            time.sleep(_IO_RETRY_BASE_DELAY * (attempt + 1))
    assert last is not None
    raise last


def _atomic_write_text(path: Path, value: str) -> None:
    """Replace a UTF-8 text file atomically without sharing temp filenames."""
    tmp = path.with_name(f".{path.name}.{os.getpid()}.{time.time_ns()}.tmp")
    try:
        with tmp.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass


def save_pdf_enabled() -> bool:
    return os.environ.get("NEWS_SAVE_PDF", "").strip().lower() in {"1", "true", "yes", "on"}


def data_dir_for(out_dir: Path) -> Path:
    parts = list(out_dir.parts)
    for index, part in enumerate(parts):
        if part == "news_pdfs":
            parts[index] = "news_data"
            return Path(*parts)
        if part.endswith("news_pdfs"):
            parts[index] = part[: -len("news_pdfs")] + "news_data"
            return Path(*parts)
    return out_dir


def html_to_text(content_html: str) -> str:
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", content_html, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</(p|div|section|article|h[1-6]|li|tr)>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line).strip()


def content_hash(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def infer_body_status(record: dict[str, Any], text: str) -> str:
    """Conservatively distinguish full article text from an RSS/paywall teaser."""
    declared = str(record.get("body_status") or "").strip()
    if declared:
        return declared
    if not text:
        return "empty"
    compact = re.sub(r"\s+", " ", text).lower()
    if any(marker in compact for marker in _PREVIEW_MARKERS):
        return "snippet"
    return "full"


def shorten_text(value: Any, max_len: int = 96) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def table_cell(value: Any) -> str:
    return shorten_text(value).replace("|", "\\|").replace("\n", " ")


def write_article_index(data_dir: Path) -> Path:
    jsonl_path = data_dir / ARTICLE_JSONL_NAME
    index_path = data_dir / ARTICLE_INDEX_NAME
    records: list[dict[str, Any]] = []
    if jsonl_path.exists():
        for line in jsonl_path.read_text(encoding="utf-8-sig").splitlines():
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    records.sort(
        key=lambda item: (
            str(item.get("published_at") or ""),
            str(item.get("source_key") or item.get("source") or ""),
            str(item.get("title") or ""),
        ),
        reverse=True,
    )

    by_source: dict[str, int] = {}
    for record in records:
        source = str(record.get("source_key") or record.get("source") or "unknown")
        by_source[source] = by_source.get(source, 0) + 1

    section = data_dir.parent.name
    date = data_dir.name
    lines = [
        f"# Article Index - {section} / {date}",
        "",
        f"- Records: {len(records)}",
    ]
    if by_source:
        source_counts = ", ".join(f"`{source}` {count}" for source, count in sorted(by_source.items()))
        lines.append(f"- By source: {source_counts}")
    lines.extend(
        [
            f"- Raw JSONL: `{ARTICLE_JSONL_NAME}`",
            "",
            "| # | ID | Source | Published | Chars | Status | Title | URL |",
            "| ---: | --- | --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for index, record in enumerate(records, start=1):
        text_chars = len(str(record.get("text") or ""))
        url = str(record.get("url") or "")
        url_cell = f"[link]({url})" if url.startswith(("http://", "https://")) else table_cell(url)
        lines.append(
            "| "
            f"{index} | "
            f"`{table_cell(record.get('id'))}` | "
            f"`{table_cell(record.get('source_key') or record.get('source'))}` | "
            f"{table_cell(record.get('published_at'))} | "
            f"{text_chars} | "
            f"{table_cell(record.get('fetch_status') or record.get('fallback'))} | "
            f"{table_cell(record.get('title'))} | "
            f"{url_cell} |"
        )

    _retry_io(lambda: _atomic_write_text(index_path, "\n".join(lines).rstrip() + "\n"))
    return index_path


def write_article_record(
    out_dir: Path,
    manifest: dict[str, Any],
    item_id: str,
    record: dict[str, Any],
) -> dict[str, Any]:
    data_dir = data_dir_for(out_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = data_dir / ARTICLE_JSONL_NAME

    text = str(record.get("text") or "").strip()
    normalized = {
        "source_key": record.get("source_key"),
        "source": record.get("source"),
        "section": record.get("section") or (out_dir.parent.name if out_dir.parent else ""),
        "title": record.get("title") or "",
        "url": record.get("url") or "",
        "published_at": record.get("published_at") or "",
        "author": record.get("author") or "",
        "excerpt": record.get("excerpt") or "",
        "text": text,
        "html": record.get("html") or "",
        "content_sha1": record.get("content_sha1") or content_hash(text),
        "fetch_status": record.get("fetch_status") or "ok",
        # Transport success and usable-body quality are distinct.  A collector
        # may successfully obtain only an RSS teaser or a source excerpt.
        "body_status": infer_body_status(record, text),
        "fallback": record.get("fallback") or "none",
        "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "extra": record.get("extra") or {},
    }

    with _lock_for(jsonl_path):
        existing = manifest.setdefault("items", {}).get(item_id)
        if existing and existing.get("content_sha1") == normalized["content_sha1"]:
            data_file = existing.get("data_file")
            if data_file and (data_dir / Path(data_file).name).exists():
                jsonl_has_item = False
                if jsonl_path.exists():
                    for line in _retry_io(lambda: jsonl_path.read_text(encoding="utf-8-sig")).splitlines():
                        if not line.strip():
                            continue
                        try:
                            if json.loads(line).get("id") == item_id:
                                jsonl_has_item = True
                                break
                        except json.JSONDecodeError:
                            continue
                if jsonl_has_item:
                    return existing

        records: list[dict[str, Any]] = []
        if jsonl_path.exists():
            for line in _retry_io(lambda: jsonl_path.read_text(encoding="utf-8-sig")).splitlines():
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if row.get("id") != item_id:
                    records.append(row)

        row = {"id": item_id, **normalized}
        records.append(row)

        def _flush() -> None:
            payload = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records)
            _atomic_write_text(jsonl_path, payload)
            write_article_index(data_dir)

        _retry_io(_flush)

    manifest_item = {
        "data_file": ARTICLE_JSONL_NAME,
        "source": normalized["source"],
        "source_key": normalized["source_key"],
        "title": normalized["title"],
        "url": normalized["url"],
        "published_at": normalized["published_at"],
        "content_sha1": normalized["content_sha1"],
        "fetch_status": normalized["fetch_status"],
        "body_status": normalized["body_status"],
        "fallback": normalized["fallback"],
        "saved_at": normalized["saved_at"],
    }
    manifest["items"][item_id] = manifest_item
    return manifest_item
