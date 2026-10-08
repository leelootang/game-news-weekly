from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(r"C:\Users\Admin\.codex\skills\game-industry-report\scripts\extract_report_inputs.py")
SPEC = importlib.util.spec_from_file_location("extract_report_inputs_contract", SCRIPT)
assert SPEC and SPEC.loader
EXTRACT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = EXTRACT
SPEC.loader.exec_module(EXTRACT)


def release_record(
    source_id: str,
    product: str,
    event: str,
    section: str = "release_calendar",
    company: str = "",
) -> dict:
    return {
        "source_id": source_id,
        "section": section,
        "date": "2026-07-20",
        "title": f"{product} - {event}" if section == "release_calendar" else f"《{product}》{event}",
        "text": (
            f"Game: {product}\nEvent date: 2026-07-20\nEvent type: {event}"
            f"\nPublisher: {company}"
        ),
    }


class ReleaseCalendarScoringTests(unittest.TestCase):
    def test_same_product_date_merges_test_labels(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "航海奇兵", "计费删档内测"),
            release_record("S0002", "航海奇兵", "删档测试"),
            release_record("S0003", "航海奇兵", "不限量测试"),
        ])
        self.assertEqual(1, len(rows))
        self.assertEqual(3, rows[0]["appearance_count"])
        self.assertEqual(3, rows[0]["event_type_score"])
        self.assertEqual(3, rows[0]["source_strength_score"])
        self.assertEqual(9, rows[0]["priority_score"])

    def test_industry_coverage_adds_one_to_source_strength(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "新品A", "首发"),
            release_record("S0002", "新品A", "正式上线", "industry_news"),
        ])
        self.assertEqual(2, rows[0]["appearance_count"])
        self.assertEqual(1, rows[0]["industry_bonus"])
        self.assertEqual(3, rows[0]["source_strength_score"])
        self.assertEqual(9, rows[0]["priority_score"])

    def test_event_types_receive_three_two_one(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "测试新品", "首测"),
            release_record("S0002", "曝光新品", "首曝"),
            release_record("S0003", "回归老品", "重启回归"),
            release_record("S0004", "发布新品", "正式发布"),
        ])
        scores = {row["product"]: row["event_type_score"] for row in rows}
        self.assertEqual(
            {"测试新品": 3, "曝光新品": 2, "回归老品": 1, "发布新品": 3},
            scores,
        )

    def test_ties_use_event_then_count_then_industry_then_first_seen(self) -> None:
        records = [
            release_record("S0001", "先出现", "首发"),
            release_record("S0002", "先出现", "正式上线"),
            release_record("S0003", "后出现", "首发"),
            release_record("S0004", "后出现", "正式上线"),
        ]
        rows = EXTRACT.build_release_candidates(records)
        self.assertEqual(["先出现", "后出现"], [row["product"] for row in rows])

    def test_routine_followup_promotion_is_not_recalled(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "宣传新品", "第二支PV公开"),
        ])
        self.assertEqual([], rows)

    def test_focus_company_adds_three_without_bypassing_multi_source_gate(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "网易新品", "正式上线", company="网易游戏"),
        ])
        self.assertEqual(3, rows[0]["company_bonus"])
        self.assertEqual(6, rows[0]["priority_score"])
        self.assertFalse(rows[0]["multi_source_eligible"])
        self.assertEqual(["网易"], rows[0]["focus_companies"])
        self.assertEqual("direct", rows[0]["company_relationship"])

    def test_focus_company_investment_adds_two(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-07-20",
            "title": "投资团队新品测试",
            "text": "7月20日，网易雷火投资的星汉明空研发游戏《骤影·绯月杀》开启首次公开测试。",
        }
        row = EXTRACT.build_release_candidates([record])[0]
        self.assertEqual(2, row["company_bonus"])
        self.assertEqual("investment", row["company_relationship"])
        self.assertEqual({"网易": "investment"}, row["focus_company_relationships"])

    def test_direct_company_relationship_wins_equal_score_tie(self) -> None:
        invested = [
            {
                "source_id": "S0001",
                "section": "industry_news",
                "date": "2026-07-20",
                "title": "投资产品开始测试",
                "text": "7月20日，网易投资的团队研发《投资产品》并开启首次公开测试。",
            },
            release_record("S0002", "投资产品", "首次公开测试"),
        ]
        direct = [
            release_record("S0003", "直属产品", "9月20日上线定档", company="米哈游"),
            release_record("S0004", "直属产品", "9月20日上线定档", company="米哈游"),
            release_record("S0005", "直属产品", "9月20日上线定档", section="industry_news", company="米哈游"),
        ]
        rows = EXTRACT.build_release_candidates([*invested, *direct])
        by_product = {row["product"]: row for row in rows}
        self.assertEqual(11, by_product["投资产品"]["priority_score"])
        self.assertEqual(11, by_product["直属产品"]["priority_score"])
        self.assertEqual(["直属产品", "投资产品"], [row["product"] for row in rows])

    def test_focus_company_bonus_reorders_eligible_candidates(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "普通新品", "正式上线"),
            release_record("S0002", "普通新品", "正式上线"),
            release_record("S0003", "重点新品", "正式上线", company="腾讯游戏"),
            release_record("S0004", "重点新品", "正式上线", company="腾讯游戏"),
        ])
        self.assertEqual(["重点新品", "普通新品"], [row["product"] for row in rows])
        self.assertEqual([9, 6], [row["priority_score"] for row in rows])

    def test_supercell_and_riot_receive_focus_company_bonus(self) -> None:
        for company, expected in (
            ("Supercell Oy", "Supercell"),
            ("拳头游戏", "Riot Games"),
        ):
            with self.subTest(company=company):
                rows = EXTRACT.build_release_candidates([
                    release_record("S0001", f"{expected}新品", "正式上线", company=company),
                ])
                self.assertEqual(3, rows[0]["company_bonus"])
                self.assertEqual([expected], rows[0]["focus_companies"])

    def test_duplicate_hash_counts_as_one_independent_source(self) -> None:
        first = release_record("S0001", "重复新品", "正式上线")
        second = release_record("S0002", "重复新品", "正式上线")
        first["sha1"] = second["sha1"] = "same-body"
        rows = EXTRACT.build_release_candidates([first, second])
        self.assertEqual(1, rows[0]["appearance_count"])
        self.assertFalse(rows[0]["multi_source_eligible"])

    def test_marketing_suffixes_normalize_to_one_product(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "王者万象棋-正版王者英雄自走棋", "正式上线"),
            release_record("S0002", "王者万象棋 招募中", "正式上线"),
            release_record("S0003", "诡秘之主-预下载(官服)", "预下载"),
            release_record("S0004", "诡秘之主", "预下载"),
        ])
        self.assertEqual(2, len(rows))
        self.assertEqual({"王者万象棋", "诡秘之主"}, {row["product"] for row in rows})

    def test_industry_lead_can_supply_product_and_beta_signal(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-07-20",
            "title": "格斗新品开启公开B测",
            "text": "7月20日，多平台格斗游戏《漫威斗魂》开启公开B测，可在PC及PS平台下载。",
        }
        rows = EXTRACT.build_release_candidates([record])
        self.assertEqual("漫威斗魂", rows[0]["product"])
        self.assertEqual("new_game_test", rows[0]["signal_type"])

    def test_industry_roundup_scans_full_text_and_builds_each_product(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-08-26",
            "title": "科隆展综合观察",
            "text": (
                ("展会背景信息。" * 250)
                + "《星布谷地》将于9月20日开启连接测试。"
                + "《洛克王国：世界》国际版将于10月27日开启海外封测。"
            ),
        }
        rows = EXTRACT.build_release_candidates([record])
        self.assertEqual({"星布谷地", "洛克王国：世界"}, {row["product"] for row in rows})
        self.assertEqual({"new_game_schedule"}, {row["signal_type"] for row in rows})

    def test_multi_product_sentence_only_recalls_self_contained_clause(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-08-26",
            "title": "展会新品汇总",
            "text": (
                "本次活动有《无日期产品》亮相，"
                "腾讯《洛克王国：世界》宣布10月开启海外测试，"
                "《归属不明产品》也公开了新画面。"
            ),
        }
        rows = EXTRACT.build_release_candidates([record])
        self.assertEqual(["洛克王国：世界"], [row["product"] for row in rows])
        self.assertEqual("new_game_schedule", rows[0]["signal_type"])

    def test_adjacent_sentence_requires_clear_anaphor(self) -> None:
        clear = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-08-26",
            "title": "新品动态",
            "text": "米哈游公布《星布谷地》的最新安排。该作将于9月20日开启终测。",
        }
        ambiguous = {
            "source_id": "S0002",
            "section": "industry_news",
            "date": "2026-08-26",
            "title": "更多新品动态",
            "text": "展台展示了《前一产品》。9月20日开启测试。《后一产品》也公布了新预告。",
        }
        self.assertEqual("星布谷地", EXTRACT.build_release_candidates([clear])[0]["product"])
        self.assertEqual([], EXTRACT.build_release_candidates([ambiguous]))

    def test_historical_and_recommendation_context_are_not_recalled(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-08-26",
            "title": "本周新品",
            "text": (
                "去年《历史产品》于9月20日开启测试。"
                "相关推荐：\n《推荐产品》将于10月27日开启海外封测。"
            ),
        }
        self.assertEqual([], EXTRACT.build_release_candidates([record]))

    def test_future_test_date_is_scored_as_schedule_announcement(self) -> None:
        record = {
            "source_id": "S0001",
            "section": "industry_news",
            "date": "2026-08-26",
            "title": "米哈游生活模拟新作公布测试安排",
            "text": "《星布谷地》“连接测试”将于9月20日开启。",
        }
        row = EXTRACT.build_release_candidates([record])[0]
        self.assertEqual("new_game_schedule", row["signal_type"])
        self.assertEqual(2, row["event_type_score"])
        self.assertEqual("2026-08-26", row["event_date"])

    def test_early_access_is_classified_as_test_not_launch(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "王者万象棋", "抢先体验测试", company="腾讯游戏"),
            release_record("S0002", "王者万象棋", "长期抢先体验测试", company="天美工作室群"),
        ])
        self.assertEqual("new_game_test", rows[0]["signal_type"])
        self.assertEqual("抢先体验测试", rows[0]["event"])
        self.assertEqual(3, rows[0]["company_bonus"])

    def test_early_access_beats_generic_store_open_label(self) -> None:
        rows = EXTRACT.build_release_candidates([
            release_record("S0001", "王者万象棋", "抢先体验测试", "industry_news", company="腾讯游戏"),
            release_record("S0002", "王者万象棋", "体验服已开服"),
        ])
        self.assertEqual("new_game_test", rows[0]["signal_type"])
        self.assertEqual("抢先体验测试", rows[0]["event"])

    def test_out_of_window_launch_is_audited_but_not_publish_eligible(self) -> None:
        records = [
            release_record("S0001", "窗口外新品", "正式上线"),
            release_record("S0002", "窗口外新品", "正式上线"),
        ]
        rows = EXTRACT.build_release_candidates(
            records,
            window_start="2026-07-21",
            window_end="2026-07-27",
        )
        self.assertFalse(rows[0]["window_eligible"])
        self.assertFalse(rows[0]["publish_eligible"])

    def test_next_day_launch_is_eligible_only_for_product_calendar_lookahead(self) -> None:
        records = [
            release_record("S0001", "及时新品", "正式上线"),
            release_record("S0002", "及时新品", "正式上线"),
        ]
        for record in records:
            record["date"] = "2026-07-28"
            record["text"] = record["text"].replace("2026-07-20", "2026-07-28")
        without_lookahead = EXTRACT.build_release_candidates(
            records, window_start="2026-07-21", window_end="2026-07-27"
        )
        with_lookahead = EXTRACT.build_release_candidates(
            records,
            window_start="2026-07-21",
            window_end="2026-07-27",
            release_lookahead_days=1,
        )
        self.assertFalse(without_lookahead[0]["publish_eligible"])
        self.assertTrue(with_lookahead[0]["publish_eligible"])
        self.assertEqual("next_day_lookahead", with_lookahead[0]["window_scope"])

    def test_normal_window_source_can_emit_distinct_next_day_launch_node(self) -> None:
        records = []
        for source_id in ("S0001", "S0002"):
            record = release_record(source_id, "次日新品-预下载(官服)", "预下载")
            record["date"] = "2026-07-27"
            record["text"] = (
                "Game: 次日新品-预下载(官服)\n"
                "Event date: 2026-07-27\n"
                "Event: 预下载已开启，7月28日正式上线"
            )
            records.append(record)
        rows = EXTRACT.build_release_candidates(
            records,
            window_start="2026-07-21",
            window_end="2026-07-27",
            release_lookahead_days=1,
        )
        by_date = {row["event_date"]: row for row in rows}
        self.assertEqual({"2026-07-27", "2026-07-28"}, set(by_date))
        self.assertEqual("new_game_launch", by_date["2026-07-28"]["signal_type"])
        self.assertTrue(by_date["2026-07-28"]["publish_eligible"])
        self.assertEqual("next_day_lookahead", by_date["2026-07-28"]["window_scope"])

    def test_two_days_after_window_remains_ineligible(self) -> None:
        records = [
            release_record("S0001", "更晚新品", "正式上线"),
            release_record("S0002", "更晚新品", "正式上线"),
        ]
        for record in records:
            record["date"] = "2026-07-29"
            record["text"] = record["text"].replace("2026-07-20", "2026-07-29")
        rows = EXTRACT.build_release_candidates(
            records,
            window_start="2026-07-21",
            window_end="2026-07-27",
            release_lookahead_days=1,
        )
        self.assertFalse(rows[0]["window_eligible"])
        self.assertEqual("outside", rows[0]["window_scope"])


if __name__ == "__main__":
    unittest.main()
