"""Run the relevant regressions without requiring a pytest installation."""
import importlib.util
import inspect
import json
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
patterns = [
    "test_report_policy.py", "test_report_artifacts.py",
    "test_release_calendar_scoring.py", "test_sync_release_decisions.py",
    "test_feishu_card_emphasis.py", "test_deep_observation_handoff.py",
    "test_feishu_report_feedback.py",
]
suite = unittest.TestSuite()
for pattern in patterns:
    suite.addTests(unittest.defaultTestLoader.discover(str(ROOT / "tests"), pattern=pattern))
spec = importlib.util.spec_from_file_location("history_policy_regression", ROOT / "tests/test_build_industry_history.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
for name, function in vars(module).items():
    if name.startswith("test_") and callable(function):
        def run(function=function):
            with tempfile.TemporaryDirectory() as temporary:
                if inspect.signature(function).parameters:
                    function(Path(temporary))
                else:
                    function()
        suite.addTest(unittest.FunctionTestCase(run, description=name))
start = time.perf_counter()
with (HERE / "regression_checks.log").open("w", encoding="utf-8") as log:
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
summary = dict(tests=result.testsRun, failures=len(result.failures), errors=len(result.errors),
               skipped=len(result.skipped), seconds=round(time.perf_counter() - start, 3))
(HERE / "regression_results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary))
raise SystemExit(0 if result.wasSuccessful() else 1)
