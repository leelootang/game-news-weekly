#!/usr/bin/env python3
"""Install the dedicated Thursday-review Feishu credentials without echoing them."""
from __future__ import annotations

import argparse
import os
import re
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env.local"
ENV_KEYS = ("FEISHU_DEEP_REVIEW_APP_ID", "FEISHU_DEEP_REVIEW_APP_SECRET")


def parse_attachment(path: Path) -> tuple[str, str]:
    lines = [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    values: dict[str, str] = {}
    for index, line in enumerate(lines[:-1]):
        normalized = re.sub(r"[\s_:-]+", "", line).lower()
        if normalized == "appid":
            values[ENV_KEYS[0]] = lines[index + 1]
        elif normalized == "appsecret":
            values[ENV_KEYS[1]] = lines[index + 1]
    if not all(values.get(key) for key in ENV_KEYS):
        raise ValueError("附件必须包含 App ID 与 App Secret 两个字段")
    return values[ENV_KEYS[0]], values[ENV_KEYS[1]]


def install(source: Path, destination: Path = ENV_PATH) -> None:
    app_id, app_secret = parse_attachment(source)
    existing = destination.read_text(encoding="utf-8-sig").splitlines() if destination.exists() else []
    kept = [
        line
        for line in existing
        if not any(re.match(rf"^\s*{re.escape(key)}\s*=", line) for key in ENV_KEYS)
    ]
    if kept and kept[-1].strip():
        kept.append("")
    kept.extend((f"{ENV_KEYS[0]}={app_id}", f"{ENV_KEYS[1]}={app_secret}"))
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=destination.name + ".", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(kept) + "\n")
        os.replace(temp_name, destination)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    install(args.source)
    print(f"Dedicated Feishu review credentials installed in ignored file: {ENV_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
