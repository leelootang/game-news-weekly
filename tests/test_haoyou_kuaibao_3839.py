from __future__ import annotations

import sys
import unittest
from datetime import datetime
from pathlib import Path


COLLECTORS_DIR = Path(__file__).resolve().parents[1] / "collectors"
if str(COLLECTORS_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTORS_DIR))

import haoyou_kuaibao_3839 as collector  # noqa: E402


DETAIL_HTML = """
<div class="popwp gameUdLog" id="gameUdLog" style="display: none;">
  <div class="log-bd">
    <ul>
      <li>
        <span>2026.08.19</span>
        <p>预下载已开启，参与预创角抢注昵称，将于8月21日上午10点正式上线</p>
      </li>
      <li><span>2026.08.13</span><p>定档8月21日正式上线</p></li>
    </ul>
  </div>
</div>
"""


def sample_event(text: str = "预下载已开启！明早10点开服上线") -> collector.TimelineEvent:
    return collector.TimelineEvent(
        event_id="150321_20260819_test",
        url="https://www.3839.com/a/150321.htm",
        game_name="诡秘之主-预下载(官服)",
        event_at=datetime(2026, 8, 19),
        day_label="08月19日 昨天",
        event_text=text,
        action="下载",
        score="7.5",
        tags=["多平台", "角色扮演"],
        badges=[],
        image_url="",
    )


class HaoyouKuaibaoRelativeDateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.observed_at = datetime(2026, 8, 20, 8, 16, tzinfo=collector.SHANGHAI_TZ)

    def test_detail_update_with_absolute_date_has_priority(self) -> None:
        event = collector.enrich_relative_event(
            sample_event(),
            self.observed_at,
            detail_fetcher=lambda _url, *, label: DETAIL_HTML,
        )

        self.assertEqual(event.date_resolution_method, "detail_update")
        self.assertEqual(event.detail_update_date, "2026.08.19")
        self.assertIn("8月21日上午10点正式上线", event.resolved_event_text)
        self.assertNotIn("8月20日", event.resolved_event_text)

    def test_collection_time_is_fallback_anchor(self) -> None:
        event = collector.enrich_relative_event(
            sample_event(),
            self.observed_at,
            detail_fetcher=lambda _url, *, label: "<html>没有更新动态</html>",
        )

        self.assertEqual(event.date_resolution_method, "collection_time")
        self.assertIn("2026年8月21日早上10点", event.resolved_event_text)
        self.assertNotIn("2026年8月20日", event.resolved_event_text)

    def test_absolute_timeline_text_does_not_need_detail_lookup(self) -> None:
        def fail_if_called(_url: str, *, label: str) -> str:
            raise AssertionError("detail page should not be fetched")

        text = "预下载已开启，将于8月21日上午10点正式上线，明天开服"
        event = collector.enrich_relative_event(
            sample_event(text),
            self.observed_at,
            detail_fetcher=fail_if_called,
        )

        self.assertEqual(event.date_resolution_method, "timeline_absolute")
        self.assertEqual(event.resolved_event_text, text)

    def test_audit_text_keeps_source_and_resolution_chain(self) -> None:
        event = collector.enrich_relative_event(
            sample_event(),
            self.observed_at,
            detail_fetcher=lambda _url, *, label: DETAIL_HTML,
        )
        text = collector.event_text(event)

        self.assertIn("Event: 预下载已开启！明早10点开服上线", text)
        self.assertIn("Collected at: 2026-08-20T08:16:00+08:00", text)
        self.assertIn("Date resolution: detail_update", text)
        self.assertIn("Detail update evidence:", text)
        self.assertIn("8月21日上午10点正式上线", text)


if __name__ == "__main__":
    unittest.main()
