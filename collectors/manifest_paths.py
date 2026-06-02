from __future__ import annotations

from pathlib import Path


RUNS_DIR_NAME = "_collector_runs"


def collector_run_manifest_dir(out_dir: Path, manifest_dir_name: str) -> Path:
    return out_dir.parent.parent / RUNS_DIR_NAME / out_dir.name


def collector_manifest_path(out_dir: Path, manifest_dir_name: str, manifest_name: str) -> Path:
    return collector_run_manifest_dir(out_dir, manifest_dir_name) / manifest_name


def legacy_manifest_paths(out_dir: Path, manifest_dir_name: str, manifest_name: str) -> list[Path]:
    legacy_root = Path(
        *[
            "news_pdfs"
            if part == "news_data"
            else part[: -len("news_data")] + "news_pdfs"
            if part.endswith("news_data")
            else part
            for part in out_dir.parent.parent.parts
        ]
    )
    return [
        out_dir.parent.parent / RUNS_DIR_NAME / out_dir.name / manifest_dir_name / manifest_name,
        legacy_root / RUNS_DIR_NAME / out_dir.name / manifest_name,
        legacy_root / RUNS_DIR_NAME / out_dir.name / manifest_dir_name / manifest_name,
        out_dir / manifest_dir_name / manifest_name,
        out_dir / manifest_name,
    ]
