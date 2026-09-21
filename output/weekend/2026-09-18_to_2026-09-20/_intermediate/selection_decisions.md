# Selection Decisions

- 卡片曝光去重：历史匹配中，Wardogs、Physint、马拉松、未眠野均已有 card_exposed=true，按 repeat_only 排除；《伊莫》历史同事件仅见 card_exposed=false（周报卡片 rank=null/10），本期以 E3×R3+M1=10 竞争并成为唯一 card_carryover；无其他补位入选。
- 维度覆盖自检：国内移动/国产产品与人才 10 张候选；市场数据 5 张；并购/投资 2 张；平台政策 3 张；档期变动 4 张；资本组织 4 张；海外重大 8 张。无信号维度均已在批量E=0卡说明。
- AI反扫：已反扫全部行业候选；日本开发者AI采用率、AI游戏UGC平台与AI互动影游管线转入AI分区，同一事件不跨栏重复。
- 产品日历漏挂反查：已扫描 industry_news + release_calendar 全量输入；所有测试、上线、预下载、首次正式首曝、定档、跨平台、重启和重大更新节点均已升入产品日历审计或显式排除。
- 产品日历反扫：已扫描 industry_news + release_calendar 全量输入；修正《沙丘：觉醒》主机上线日期为9月22日（超出9月21日及时性边界），修正GTA6节点为单源，随后由 sync_release_decisions.py 确定性同步。
- 行业新闻 E×R+M 打分记录：逐条按『事件E×相关R+钩子M = 终分』记录；E、R均为0–3，M为0–2，E=0一票否决，周末报终分≥7才include，并按终分降序排列。
- 证据质量：40条 non-full 输入全部未用于最终正文证据。

| candidate | decision | target_section | score | reason |
| --- | --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子2 = 11 | E3×R3+M2=11。 |
| I002 | include | industry_news | 事件3×相关3+钩子2 = 11 | E3×R3+M2=11。 |
| I003 | include | industry_news | 事件3×相关3+钩子1 = 10 | E3×R3+M1=10。 |
| I004 | include | industry_news | 事件3×相关3+钩子1 = 10 | E3×R3+M1=10。 |
| I005 | include | industry_news | 事件3×相关3+钩子1 = 10 | E3×R3+M1=10。 |
| I006 | include | industry_news | 事件3×相关3+钩子1 = 10 | E3×R3+M1=10；历史完整报告收录但订阅卡片未展示，本期唯一卡片曝光补位。 |
| I007 | include | industry_news | 事件2×相关3+钩子2 = 8 | E2×R3+M2=8。 |
| I008 | include | industry_news | 事件2×相关3+钩子2 = 8 | E2×R3+M2=8。 |
| I009 | include | industry_news | 事件2×相关3+钩子1 = 7 | E2×R3+M1=7。 |
| I010 | include | industry_news | 事件2×相关3+钩子1 = 7 | E2×R3+M1=7。 |
| I011 | include | industry_news | 事件2×相关3+钩子1 = 7 | E2×R3+M1=7。 |
| I012 | include | industry_news | 事件2×相关3+钩子1 = 7 | E2×R3+M1=7。 |
| I013 | exclude | industry_news | 事件2×相关3+钩子2 = 8 | 历史任一匹配项card_exposed=true，未出现足以构成新阶段的新增事实，repeat_only。 |
| I014 | exclude | industry_news | 事件3×相关2+钩子1 = 7 | 历史任一匹配项card_exposed=true；新增演员属于例行宣传，核心合作变化为repeat_only。 |
| I015 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 历史匹配项已进入订阅卡片，当前来源未提供实质状态变化，repeat_only。 |
| I016 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 首次公开已在历史卡片展示，本期仅为社区重复召回，repeat_only。 |
| I017 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | E2×R2+M1=5，低于周末报7分线。 |
| I018 | exclude | industry_news | 事件2×相关2+钩子2 = 6 | E2×R2+M2=6，低于周末报7分线；主机版实际日期为9月22日，也超出产品日历及时性窗口。 |
| I019 | exclude | industry_news | 事件1×相关1+钩子2 = 3 | E1×R1+M2=3，海外一般劳资事件且迁移点弱。 |
| I020 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | E=0：普通版本、联动、宣传视频、促销或纯榜单；其余来源见event_candidates批量审计卡。 |
| I021 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | E=0：非游戏、影视、硬件或泛职场内容；其余来源见event_candidates批量审计卡。 |
| A001 | include | ai_trends | - | 直接作用于游戏研发流程，样本与比例完整。 |
| A002 | include | ai_trends | - | 直接作用于游戏创作、发布和分发，含可核验业务数据。 |
| A003 | include | ai_trends | - | 已有上线作品与在研项目，属于直接游戏生产应用。 |
| A004 | exclude | ai_trends | - | 核心赛事于9月13日结束，晚到稿未提供本窗口新增状态。 |
| A005 | exclude | ai_trends | - | 没有可由来源事实支撑的具体游戏迁移链条。 |
| C001 | include | community_discourse | - | 触发、争议逻辑、时间线与补扫均完整。 |
| C002 | include | community_discourse | - | 同一事件内同时保留缩水质疑与总量核算反方证据。 |
| C003 | exclude | community_discourse | - | 停运事实已在行业新闻呈现，社区侧新增机制与后续不足，避免跨栏重复。 |
| C004 | exclude | community_discourse | - | 核心事件已进入行业新闻，社区帖子以情绪表达为主，缺少独立后续。 |
| D001 | include | deep_analysis | - | R2/I3/E3/C3=11，证据链完整且可形成变化—机制—下游影响。 |
| release-candidate-001 | include | release_calendar | - | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | - | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-005 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-006 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-010 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-011 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-023 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-024 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-025 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-030 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-031 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-034 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-036 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-038 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-039 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-041 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-043 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-046 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-004 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-047 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-048 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-049 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-050 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-051 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-052 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-053 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-054 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-055 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-056 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-057 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-058 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-059 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-060 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-061 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-062 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-063 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-064 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-065 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-066 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-067 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-068 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-069 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-070 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-002 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-071 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-072 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-073 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-074 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-075 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-076 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-077 | exclude | release_calendar | - | 单源不具备正文资格 |
| release-candidate-078 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-079 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-080 | exclude | release_calendar | - | 事件日期不在报告窗口 |
| release-candidate-081 | exclude | release_calendar | - | 事件日期不在报告窗口 |
