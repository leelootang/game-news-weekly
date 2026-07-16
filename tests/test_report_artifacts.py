from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("report_artifacts", ROOT / "scripts" / "report_artifacts.py")
assert SPEC and SPEC.loader
ARTIFACTS = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ARTIFACTS
SPEC.loader.exec_module(ARTIFACTS)
sys.path.insert(0, str(ROOT / "collectors"))
from article_store import infer_body_status, write_article_record  # noqa: E402


class ReportArtifactContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.report = self.root / "game_industry_daily_2026-07-15.md"
        self.inputs = self.root / "report_inputs.jsonl"
        self.items = self.root / "report_items.json"
        self.decisions = self.root / "selection_decisions.json"
        self.audit = self.root / "release_calendar_audit.json"
        self.sources = self.root / "sources_used.md"
        self.report.write_text(
            """# 日报

## 一、行业新闻

### 1. 行业事件

公司公布关键数据。

## 二、AI 新闻

### 1. AI 事件

工具进入游戏流程。

## 三、新游发布

- 《测试游戏》手游于 7 月 15 日正式上线；由测试公司发行。

## 四、玩家舆论

### 1. 社区事件

论坛帖围绕更新内容展开讨论，玩家认为说明不够清晰。

## 五、行业精选

### 1. 深度事件

**观察：** 产品团队开始改变流程。

**分析：** 这改变了验证成本。

第二段分析说明前提会如何松动。
""",
            encoding="utf-8",
        )
        records = []
        evidence = ["公司公布关键数据。", "工具进入游戏流程。", "《测试游戏》手游于 7 月 15 日正式上线", "玩家认为说明不够清晰。", "产品团队开始改变流程。"]
        for index, text in enumerate(evidence, 1):
            records.append({
                "source_id": f"S{index:04d}", "source": f"source{index}.example", "title": f"原文 {index}",
                "url": f"https://source{index}.example/article", "path": f"news/{index}.jsonl", "text": text,
                "fetch_status": "ok", "body_status": "full", "text_chars": len(text),
            })
        self.inputs.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in records), encoding="utf-8")
        items = [
            self.item("industry", "行业事件", "C1", "S0001", evidence[0]),
            self.item("ai", "AI 事件", "C2", "S0002", evidence[1]),
            {**self.item("release_calendar", "测试游戏", "C3", "S0003", evidence[2]), "source_ids": ["S0003", "S0001"], "release": {"product": "测试游戏", "event": "上线", "date": "2026-07-15", "platform": "mobile", "company": "测试公司"}},
            {**self.item("community", "社区事件", "C4", "S0004", evidence[3]), "community": {"trigger": "更新", "claim_scope": "玩家反馈", "complaint_logic": "说明不清", "timeline": "当日", "follow_up_scan": "已扫描", "official_source_ids": []}},
            self.item("deep", "深度事件", "C5", "S0005", evidence[4]),
        ]
        self.items.write_text(json.dumps({"items": items}, ensure_ascii=False), encoding="utf-8")
        decisions = [
            {"candidate_id": "C1", "section": "industry", "source_ids": ["S0001"], "entities": ["公司"], "event": "业绩披露", "decision": "include", "reason": "重要", "scores": {"event": 2, "entity": 2, "region": 2, "hook": 1, "total": 7}},
            *[{"candidate_id": f"C{i}", "section": section, "source_ids": [f"S{i:04d}"], "entities": ["主体"], "event": "单一事件", "decision": "include", "reason": "可核验"} for i, section in [(2, "ai"), (3, "release_calendar"), (4, "community"), (5, "deep")]],
        ]
        self.decisions.write_text(json.dumps({"decisions": decisions}, ensure_ascii=False), encoding="utf-8")
        self.audit.write_text(json.dumps({"schema_version": 1, "nodes": []}), encoding="utf-8")
        ARTIFACTS.generate_sources_used(self.report, self.inputs, self.items, self.sources)

    def tearDown(self) -> None:
        self.temp.cleanup()

    @staticmethod
    def item(section: str, title: str, candidate_id: str, source_id: str, evidence: str) -> dict:
        return {"section": section, "title": title, "candidate_id": candidate_id, "source_ids": [source_id], "claims": [{"claim": evidence, "source_id": source_id, "evidence": evidence}]}

    def validate(self):
        return ARTIFACTS.validate_contract(self.report, self.inputs, self.items, self.decisions, self.audit, self.sources, True)

    def test_valid_contract_and_generated_sources(self) -> None:
        errors, warnings = self.validate()
        self.assertEqual([], errors)
        self.assertEqual([], warnings)
        self.assertIn("- S0003 | source3.example | 原文 3 | https://source3.example/article", self.sources.read_text(encoding="utf-8"))

    def test_claim_evidence_must_match_input(self) -> None:
        data = json.loads(self.items.read_text(encoding="utf-8"))
        data["items"][0]["claims"][0]["evidence"] = "不存在的原文"
        self.items.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("claim evidence not found" in error for error in errors))

    def test_source_details_drift_is_blocking(self) -> None:
        self.sources.write_text(self.sources.read_text(encoding="utf-8").replace("原文 1", "过期标题", 1), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("Source Details drift" in error for error in errors))

    def test_industry_title_rejects_promotional_shorthand(self) -> None:
        original = self.report.read_text(encoding="utf-8")
        title = "".join(map(chr, [0x884c, 0x4e1a, 0x4e8b, 0x4ef6]))
        replacement = "".join(map(chr, [0x4ea7, 0x54c1, 0x6d77, 0x5916, 0x7206, 0x7ea2]))
        self.report.write_text(original.replace(title, replacement, 1), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("promotional shorthand" in error for error in errors))

    def test_priority_tracks_must_use_the_controlled_vocabulary(self) -> None:
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        data["decisions"][0]["priority_tracks"] = ["unknown_track"]
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("unknown priority_tracks" in error for error in errors))

    def test_article_store_preserves_body_quality(self) -> None:
        out = self.root / "news_data" / "deep_analysis" / "2026-07-15"
        manifest = {"items": {}}
        write_article_record(out, manifest, "teaser", {
            "source_key": "example", "source": "example.test", "title": "Teaser", "url": "https://example.test",
            "text": "RSS preview only", "fetch_status": "ok", "body_status": "snippet", "fallback": "source_excerpt",
        })
        row = json.loads((out / "articles.jsonl").read_text(encoding="utf-8").strip())
        self.assertEqual("snippet", row["body_status"])
        self.assertEqual("snippet", manifest["items"]["teaser"]["body_status"])

    def test_article_store_detects_unlabelled_paid_preview(self) -> None:
        self.assertEqual("snippet", infer_body_status({}, "Preview. Subscribe to continue reading."))


if __name__ == "__main__":
    unittest.main()
