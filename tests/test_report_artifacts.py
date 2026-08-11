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
            {"candidate_id": "C1", "section": "industry", "source_ids": ["S0001"], "entities": ["公司"], "event": "业绩披露", "decision": "include", "reason": "重要", "scores": {"event": 3, "relevance": 2, "hook": 1, "total": 7}},
            *[{"candidate_id": f"C{i}", "section": section, "source_ids": [f"S{i:04d}"], "entities": ["主体"], "event": "单一事件", "decision": "include", "reason": "可核验", **({"ai_tier": "direct_application", "game_stage": ["development"], "industry_reverse_scan": False} if section == "ai" else {"scores": {"relevance": 2, "insight": 2, "evidence": 2, "card": 2, "total": 8}} if section == "deep" else {"scores": {"event": 3, "source": 2, "total": 6}} if section == "release_calendar" else {})} for i, section in [(2, "ai"), (3, "release_calendar"), (4, "community"), (5, "deep")]],
        ]
        self.decisions.write_text(json.dumps({"decisions": decisions}, ensure_ascii=False), encoding="utf-8")
        self.audit.write_text(
            json.dumps(
                {
                    "schema_version": 3,
                    "nodes": [
                        {
                            "candidate_id": "C3",
                            "signal_type": "new_game_launch",
                            "event_date": "2026-07-15",
                            "source_ids": ["S0003", "S0001"],
                            "event_type_score": 3,
                            "source_strength_score": 2,
                            "priority_score": 6,
                            "appearance_count": 2,
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
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

    def test_industry_score_must_equal_e_times_r_plus_m(self) -> None:
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        data["decisions"][0]["scores"]["total"] = 8
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("total must equal E×R+M" in error for error in errors))

    def test_weekly_industry_requires_eight_points(self) -> None:
        weekly = self.root / "game_industry_weekly_2026-07-09_to_2026-07-15.md"
        self.report.rename(weekly)
        self.report = weekly
        errors, _ = self.validate()
        self.assertTrue(any("required >= 8" in error and "C1" in error for error in errors))

    def test_weekly_industry_accepts_eight_points(self) -> None:
        weekly = self.root / "game_industry_weekly_2026-07-09_to_2026-07-15.md"
        self.report.rename(weekly)
        self.report = weekly
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        data["decisions"][0]["scores"] = {"event": 3, "relevance": 2, "hook": 2, "total": 8}
        data["decisions"][-1]["card_designated"] = True
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertFalse(any("industry include fails" in error for error in errors))

    def test_release_calendar_caps_by_report_type(self) -> None:
        self.assertEqual(4, ARTIFACTS.release_cap_for_report(Path("game_industry_daily_2026-07-15.md")))
        self.assertEqual(4, ARTIFACTS.release_cap_for_report(Path("game_industry_weekend_2026-07-10_to_2026-07-12.md")))
        self.assertEqual(7, ARTIFACTS.release_cap_for_report(Path("game_industry_weekly_2026-07-09_to_2026-07-15.md")))
        self.assertEqual(12, ARTIFACTS.release_cap_for_report(Path("game_industry_monthly_2026-07.md")))

    def test_weekly_deep_below_nine_requires_manual_card_designation(self) -> None:
        weekly = self.root / "game_industry_weekly_2026-07-09_to_2026-07-15.md"
        self.report.rename(weekly)
        self.report = weekly
        errors, _ = self.validate()
        self.assertTrue(any("below 9 without manual card designation" in error for error in errors))

    def test_weekly_manual_card_designation_overrides_deep_threshold(self) -> None:
        weekly = self.root / "game_industry_weekly_2026-07-09_to_2026-07-15.md"
        self.report.rename(weekly)
        self.report = weekly
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        data["decisions"][-1]["card_designated"] = True
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertFalse(any("below 9 without manual card designation" in error for error in errors))

    def test_community_does_not_require_disclaimer_without_official_source(self) -> None:
        text = self.report.read_text(encoding="utf-8")
        self.report.write_text(text.replace("论坛帖围绕更新内容展开讨论，", "围绕更新内容，"), encoding="utf-8")
        errors, _ = self.validate()
        self.assertFalse(any("visibly attributed" in error for error in errors))

    def test_multi_source_candidate_requires_strict_cluster_basis(self) -> None:
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        data["decisions"][0]["source_ids"] = ["S0001", "S0002"]
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("strict same-subject/product/date/event" in error for error in errors))

    def test_release_audit_rejects_version_signal(self) -> None:
        self.audit.write_text(json.dumps({"nodes": [{"candidate_id": "C3", "title": "旧游新版本", "signal_type": "version_update"}]}, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("non-new-game signal" in error for error in errors))

    def test_include_decision_must_be_published(self) -> None:
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        data["decisions"].append(
            {
                "candidate_id": "C6",
                "section": "community",
                "source_ids": ["S0004"],
                "event": "另一个事件",
                "decision": "include",
                "reason": "错误地漏入正文",
            }
        )
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertIn("include decision is missing from final report: C6", errors)

    def test_daily_community_discourse_cap_is_blocking(self) -> None:
        current_report = self.root / "game_industry_daily_2026-08-11.md"
        self.report.replace(current_report)
        self.report = current_report
        text = self.report.read_text(encoding="utf-8")
        self.report.write_text(
            text.replace(
                "## 五、行业精选",
                "### 2. 社区事件二\n\n8月1日玩家质疑更新说明。\n\n"
                "### 3. 社区事件三\n\n8月2日玩家质疑活动规则。\n\n"
                "## 五、行业精选",
            ),
            encoding="utf-8",
        )
        errors, _ = self.validate()
        self.assertIn("community discourse exceeds report cap 2: 3", errors)

    def test_community_cap_grandfathers_older_reports(self) -> None:
        self.assertFalse(ARTIFACTS.community_cap_is_enforced(self.report))

    def test_community_caps_are_defined_by_report_kind(self) -> None:
        self.assertEqual(2, ARTIFACTS.community_cap_for_report(Path("game_industry_daily_2026-08-11.md")))
        self.assertEqual(
            2,
            ARTIFACTS.community_cap_for_report(
                Path("game_industry_weekend_2026-08-08_to_2026-08-09.md")
            ),
        )
        self.assertEqual(
            3,
            ARTIFACTS.community_cap_for_report(
                Path("game_industry_weekly_2026-08-07_to_2026-08-13.md")
            ),
        )

    def test_release_date_must_be_evidenced_and_in_window(self) -> None:
        data = json.loads(self.audit.read_text(encoding="utf-8"))
        data["nodes"][0]["event_date"] = "2026-08-13"
        self.audit.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("date is not evidenced" in error for error in errors))
        self.assertTrue(any("outside report window" in error for error in errors))

    def test_pipeline_metadata_in_published_body_is_blocking(self) -> None:
        text = self.report.read_text(encoding="utf-8")
        self.report.write_text(
            text.replace("公司公布关键数据。", "【GameLook专稿，禁止转载！】公司公布关键数据。"),
            encoding="utf-8",
        )
        errors, _ = self.validate()
        self.assertTrue(any("leaks source/pipeline metadata" in error for error in errors))

    def test_internal_carryover_label_in_published_title_is_blocking(self) -> None:
        text = self.report.read_text(encoding="utf-8")
        self.report.write_text(
            text.replace("### 1. 行业事件", "### 1. 【上期卡片未展示】行业事件"),
            encoding="utf-8",
        )
        errors, _ = self.validate()
        self.assertTrue(any("leaks source/pipeline metadata" in error for error in errors))

    def test_deep_item_must_start_with_observation(self) -> None:
        text = self.report.read_text(encoding="utf-8")
        self.report.write_text(
            text.replace("**观察：** 产品团队开始改变流程。", "原文摘要。\n\n**观察：** 产品团队开始改变流程。"),
            encoding="utf-8",
        )
        errors, _ = self.validate()
        self.assertTrue(any("deep item must start with 观察" in error for error in errors))

    def test_duplicate_source_set_in_one_section_is_blocking(self) -> None:
        self.report.write_text(
            self.report.read_text(encoding="utf-8").replace(
                "工具进入游戏流程。\n\n## 三、新游发布",
                "工具进入游戏流程。\n\n### 2. AI 重复事件\n\n工具进入游戏流程。\n\n## 三、新游发布",
            ),
            encoding="utf-8",
        )
        item_data = json.loads(self.items.read_text(encoding="utf-8"))
        item_data["items"].append(self.item("ai", "AI 重复事件", "C6", "S0002", "工具进入游戏流程。"))
        self.items.write_text(json.dumps(item_data, ensure_ascii=False), encoding="utf-8")
        decision_data = json.loads(self.decisions.read_text(encoding="utf-8"))
        decision_data["decisions"].append(
            {
                "candidate_id": "C6",
                "section": "ai",
                "source_ids": ["S0002"],
                "event": "重复事件",
                "decision": "include",
                "reason": "错误重复",
                "ai_tier": "direct_application",
                "game_stage": ["development"],
                "industry_reverse_scan": False,
            }
        )
        self.decisions.write_text(json.dumps(decision_data, ensure_ascii=False), encoding="utf-8")
        ARTIFACTS.generate_sources_used(self.report, self.inputs, self.items, self.sources)
        errors, _ = self.validate()
        self.assertTrue(any("duplicate source set in ai" in error for error in errors))

    def test_industry_items_must_be_sorted_by_score(self) -> None:
        self.report.write_text(
            self.report.read_text(encoding="utf-8").replace(
                "公司公布关键数据。\n\n## 二、AI 新闻",
                "公司公布关键数据。\n\n### 2. 更高分行业事件\n\n第二家公司公布关键数据。\n\n## 二、AI 新闻",
            ),
            encoding="utf-8",
        )
        with self.inputs.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "source_id": "S0006",
                        "source": "source6.example",
                        "title": "原文 6",
                        "url": "https://source6.example/article",
                        "path": "news/6.jsonl",
                        "text": "第二家公司公布关键数据。",
                        "fetch_status": "ok",
                        "body_status": "full",
                        "text_chars": 11,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
        item_data = json.loads(self.items.read_text(encoding="utf-8"))
        item_data["items"].append(
            self.item("industry", "更高分行业事件", "C6", "S0006", "第二家公司公布关键数据。")
        )
        self.items.write_text(json.dumps(item_data, ensure_ascii=False), encoding="utf-8")
        decision_data = json.loads(self.decisions.read_text(encoding="utf-8"))
        decision_data["decisions"].append(
            {
                "candidate_id": "C6",
                "section": "industry",
                "source_ids": ["S0006"],
                "event": "更高分事件",
                "decision": "include",
                "reason": "达到入选线",
                "scores": {"event": 3, "relevance": 2, "hook": 2, "total": 8},
            }
        )
        self.decisions.write_text(json.dumps(decision_data, ensure_ascii=False), encoding="utf-8")
        ARTIFACTS.generate_sources_used(self.report, self.inputs, self.items, self.sources)
        errors, _ = self.validate()
        self.assertTrue(any("industry items are not sorted by score" in error for error in errors))

    def test_schema_four_release_company_bonus_is_validated(self) -> None:
        audit = json.loads(self.audit.read_text(encoding="utf-8"))
        audit.update({"schema_version": 4, "focus_company_bonus": 3})
        audit["nodes"][0].update(
            {
                "focus_companies": ["网易"],
                "company_evidence_ids": ["S0003"],
                "company_bonus": 3,
                "priority_score": 9,
                "industry_bonus": 0,
                "first_seen_order": 0,
            }
        )
        self.audit.write_text(json.dumps(audit, ensure_ascii=False), encoding="utf-8")
        decisions = json.loads(self.decisions.read_text(encoding="utf-8"))
        release_decision = next(
            decision for decision in decisions["decisions"]
            if decision["candidate_id"] == "C3"
        )
        release_decision["scores"] = {"event": 3, "source": 2, "company": 3, "total": 9}
        self.decisions.write_text(json.dumps(decisions, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertFalse(any("release" in error and "company" in error for error in errors))

        audit["nodes"][0]["company_evidence_ids"] = []
        self.audit.write_text(json.dumps(audit, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertTrue(any("company bonus lacks company evidence" in error for error in errors))

    def test_source_details_title_may_contain_pipe(self) -> None:
        _items, details = ARTIFACTS.parse_sources_used(
            "# Sources Used\n\n## Source Details\n\n"
            "- S0001 | example.test | 原创 | 标题正文 | https://example.test/a\n"
        )
        self.assertEqual(
            ("example.test", "原创 | 标题正文", "https://example.test/a"),
            details["S0001"],
        )

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

    def test_roblox_industry_subject_requires_highest_relevance(self) -> None:
        data = json.loads(self.decisions.read_text(encoding="utf-8"))
        industry = data["decisions"][0]
        industry["entities"] = ["Roblox Corporation"]
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertIn(
            "Roblox industry subject must receive highest relevance R=3: C1",
            errors,
        )

        industry["scores"] = {"event": 3, "relevance": 3, "hook": 1, "total": 10}
        self.decisions.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        errors, _ = self.validate()
        self.assertFalse(any("Roblox industry subject" in error for error in errors))

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
