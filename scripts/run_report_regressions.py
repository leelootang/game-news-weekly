"""Run offline report/collector regressions without requiring pytest."""
from __future__ import annotations

import argparse
import importlib.util
import inspect
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNITTEST_FILES = (
    "test_industry_timing.py", "test_report_policy.py", "test_report_artifacts.py",
    "test_release_calendar_scoring.py", "test_sync_release_decisions.py",
    "test_feishu_card_emphasis.py", "test_cubox.py", "test_collector_resilience.py",
    "test_deep_observation_handoff.py", "test_feishu_report_feedback.py",
)
FUNCTION_FILES = (
    "test_build_industry_history.py", "test_nadianshi.py", "test_gamespot.py",
    "test_pocketgamer_fulltext.py",
)


def build_suite() -> unittest.TestSuite:
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    suite = unittest.TestSuite()
    for filename in UNITTEST_FILES:
        suite.addTests(unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern=filename))
    for filename in FUNCTION_FILES:
        spec = importlib.util.spec_from_file_location("regression_" + Path(filename).stem, ROOT / "tests" / filename)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        for name, function in vars(module).items():
            if not name.startswith("test_") or not inspect.isfunction(function):
                continue

            def run(function=function):
                with tempfile.TemporaryDirectory() as temporary:
                    parameters = inspect.signature(function).parameters
                    if not parameters:
                        function()
                    elif list(parameters) == ["tmp_path"]:
                        function(Path(temporary))
                    else:
                        raise RuntimeError(f"Unsupported fixture: {parameters}")

            suite.addTest(unittest.FunctionTestCase(run, description=f"{filename}::{name}"))
    return suite


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, help="Optional directory for log and JSON results")
    args = parser.parse_args()
    suite = build_suite()
    start = time.perf_counter()
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        with (args.output_dir / "regression_checks.log").open("w", encoding="utf-8") as log:
            result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
    else:
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    summary = dict(tests=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                   skipped=len(result.skipped), seconds=round(time.perf_counter() - start, 3))
    if args.output_dir:
        (args.output_dir / "regression_results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
