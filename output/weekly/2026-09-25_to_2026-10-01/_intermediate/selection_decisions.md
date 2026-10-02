# Selection Decisions

- 卡片曝光去重：所有历史匹配项均读取 card_exposed/card_rank/card_limit/card_exposure_source；本期无达到8分线且全部历史匹配均未曝光的候选，card_carryover=0。
- repeat_only：6 条，均排除。
- 维度覆盖自检：中国移动市场=3张 / 产品档期=12张 / 优先赛道=2张 / 国产产品=2张 / 国内厂商=12张 / 市场数据=3张 / 平台政策=5张 / 并购投融资=4张 / 最高优先级主体=5张 / 海外重大=9张 / 资本组织=9张
- 产品日历漏挂反查：industry_news 与 release_calendar 全量输入均已进入 release_calendar_audit.json；正文由同步脚本按多源前缀确定。
- 行业新闻 E×R+M 打分：每个行业候选均记录 E、R、M 与 total；周报仅纳入 total>=8，并按总分降序。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | E3×R3+M2=11，达到周报8分线。；事件3×相关3+钩子2 = 11 |
| I002 | include | industry_news | E3×R3+M2=11，达到周报8分线。；事件3×相关3+钩子2 = 11 |
| I003 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I004 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I005 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I006 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I007 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I008 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I009 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I010 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I011 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I012 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I013 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I014 | include | industry_news | E3×R3+M1=10，达到周报8分线。；事件3×相关3+钩子1 = 10 |
| I015 | include | industry_news | E3×R2+M2=8，达到周报8分线。；事件3×相关2+钩子2 = 8 |
| I016 | include | industry_news | E3×R3+M1=10，国内厂商产品组合进入集中披露阶段。；事件3×相关3+钩子1 = 10 |
| I017 | include | industry_news | E2×R3+M2=8，多源且覆盖Supercell、Riot等最高关注主体的平台规则变化。；事件2×相关3+钩子2 = 8 |
| IX001 | exclude | - | E2×R3+M1=7，低于周报8分线。；事件2×相关3+钩子1 = 7 |
| IX002 | exclude | - | E2×R3+M1=7，低于周报8分线。；事件2×相关3+钩子1 = 7 |
| IX003 | exclude | - | E3×R2+M1=7，低于周报8分线。；事件3×相关2+钩子1 = 7 |
| IX004 | exclude | - | 历史同一事件已有卡片曝光，本期仅为换来源、转载或后续评论，按repeat_only排除。；事件3×相关2+钩子1 = 7 |
| IX005 | exclude | - | 历史同一事件已有卡片曝光，本期仅为换来源、转载或后续评论，按repeat_only排除。；事件2×相关3+钩子1 = 7 |
| IX006 | exclude | - | 历史同一事件已有卡片曝光，本期仅为换来源、转载或后续评论，按repeat_only排除。；事件3×相关3+钩子1 = 10 |
| IX007 | exclude | - | 历史同一事件已有卡片曝光，本期仅为换来源、转载或后续评论，按repeat_only排除。；事件3×相关3+钩子1 = 10 |
| IX008 | exclude | - | 历史同一事件已有卡片曝光，本期仅为换来源、转载或后续评论，按repeat_only排除。；事件3×相关2+钩子1 = 7 |
| IX009 | exclude | - | 历史同一事件已有卡片曝光，本期仅为换来源、转载或后续评论，按repeat_only排除。；事件3×相关2+钩子1 = 7 |
| IX010 | exclude | - | 存在可核验新增事实，但E1×R3+M1=4低于周报8分线。；事件1×相关3+钩子1 = 4 |
| IX011 | exclude | - | E2×R2+M1=5，低于周报8分线。；事件2×相关2+钩子1 = 5 |
| IX012 | exclude | - | E2×R2+M2=6，低于周报8分线。；事件2×相关2+钩子2 = 6 |
| IX013 | exclude | - | E2×R2+M1=5，低于周报8分线。；事件2×相关2+钩子1 = 5 |
| IX014 | exclude | - | E2×R2+M1=5，低于周报8分线。；事件2×相关2+钩子1 = 5 |
| IX015 | exclude | - | E3×R2+M1=7，低于周报8分线。；事件3×相关2+钩子1 = 7 |
| A001 | include | ai_trends | AI已直接作用于游戏研发、产品或运营环节。 |
| A002 | include | ai_trends | AI已直接作用于游戏研发、产品或运营环节。 |
| A003 | include | ai_trends | AI已直接作用于游戏研发、产品或运营环节。 |
| A004 | include | ai_trends | AI已直接作用于游戏研发、产品或运营环节。 |
| A005 | include | ai_trends | AI已直接作用于游戏研发、产品或运营环节。 |
| A006 | include | ai_trends | AI已直接作用于游戏研发、产品或运营环节。 |
| AX001 | exclude | - | 直接应用成立，但本周同类高强度直接落地已达6条，证据与影响范围相对更窄。 |
| AX002 | exclude | - | 迁移价值成立，但优先保留六条直接作用类。 |
| C001 | include | community_discourse | 触发、争议逻辑、时间线与后续扫描完整。 |
| C002 | include | community_discourse | 触发、争议逻辑、时间线与后续扫描完整。 |
| C003 | include | community_discourse | 触发、争议逻辑、时间线与后续扫描完整。 |
| CX001 | exclude | - | 事件可命名，但周报3条上限内优先保留有产品机制或官方后续的事件。 |
| CX002 | exclude | - | 事件成立，但在周报3条上限内排序低于有连续时间线与明确产品机制的候选。 |
| D001 | include | deep_analysis | 飞书回执正文候选，按用户指定顺序进入周报。 |
| D002 | include | deep_analysis | 飞书回执正文候选，按用户指定顺序进入周报。 |
| D003 | include | deep_analysis | 飞书回执正文候选，按用户指定顺序进入周报。 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-005 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-006 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-007 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-008 | exclude | - | 单源不具备正文资格 |
| release-candidate-009 | exclude | - | 单源不具备正文资格 |
| release-candidate-010 | exclude | - | 单源不具备正文资格 |
| release-candidate-011 | exclude | - | 单源不具备正文资格 |
| release-candidate-012 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-013 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-002 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-004 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-014 | exclude | - | 单源不具备正文资格 |
| release-candidate-015 | exclude | - | 单源不具备正文资格 |
| release-candidate-016 | exclude | - | 单源不具备正文资格 |
| release-candidate-017 | exclude | - | 单源不具备正文资格 |
| release-candidate-018 | exclude | - | 单源不具备正文资格 |
| release-candidate-019 | exclude | - | 单源不具备正文资格 |
| release-candidate-020 | exclude | - | 单源不具备正文资格 |
| release-candidate-021 | exclude | - | 单源不具备正文资格 |
| release-candidate-022 | exclude | - | 单源不具备正文资格 |
| release-candidate-023 | exclude | - | 单源不具备正文资格 |
| release-candidate-024 | exclude | - | 单源不具备正文资格 |
| release-candidate-025 | exclude | - | 单源不具备正文资格 |
| release-candidate-026 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-027 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-028 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-029 | exclude | - | 单源不具备正文资格 |
| release-candidate-030 | exclude | - | 单源不具备正文资格 |
| release-candidate-031 | exclude | - | 单源不具备正文资格 |
| release-candidate-032 | exclude | - | 单源不具备正文资格 |
| release-candidate-033 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-034 | exclude | - | 单源不具备正文资格 |
| release-candidate-035 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-036 | exclude | - | 单源不具备正文资格 |
| release-candidate-037 | exclude | - | 单源不具备正文资格 |
| release-candidate-038 | exclude | - | 单源不具备正文资格 |
| release-candidate-039 | exclude | - | 单源不具备正文资格 |
| release-candidate-040 | exclude | - | 单源不具备正文资格 |
| release-candidate-041 | exclude | - | 单源不具备正文资格 |
| release-candidate-042 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-043 | exclude | - | 单源不具备正文资格 |
| release-candidate-044 | exclude | - | 单源不具备正文资格 |
| release-candidate-045 | exclude | - | 单源不具备正文资格 |
| release-candidate-046 | exclude | - | 单源不具备正文资格 |
| release-candidate-047 | exclude | - | 单源不具备正文资格 |
| release-candidate-048 | exclude | - | 单源不具备正文资格 |
| release-candidate-049 | exclude | - | 单源不具备正文资格 |
| release-candidate-050 | exclude | - | 单源不具备正文资格 |
| release-candidate-051 | exclude | - | 单源不具备正文资格 |
| release-candidate-052 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-053 | exclude | - | 单源不具备正文资格 |
| release-candidate-054 | exclude | - | 单源不具备正文资格 |
| release-candidate-055 | exclude | - | 单源不具备正文资格 |
| release-candidate-056 | exclude | - | 单源不具备正文资格 |
| release-candidate-057 | exclude | - | 单源不具备正文资格 |
| release-candidate-058 | exclude | - | 单源不具备正文资格 |
| release-candidate-059 | exclude | - | 单源不具备正文资格 |
| release-candidate-060 | exclude | - | 单源不具备正文资格 |
| release-candidate-061 | exclude | - | 单源不具备正文资格 |
| release-candidate-062 | exclude | - | 单源不具备正文资格 |
| release-candidate-063 | exclude | - | 单源不具备正文资格 |
| release-candidate-064 | exclude | - | 单源不具备正文资格 |
| release-candidate-065 | exclude | - | 单源不具备正文资格 |
| release-candidate-066 | exclude | - | 单源不具备正文资格 |
| release-candidate-067 | exclude | - | 单源不具备正文资格 |
| release-candidate-068 | exclude | - | 单源不具备正文资格 |
| release-candidate-069 | exclude | - | 单源不具备正文资格 |
| release-candidate-070 | exclude | - | 单源不具备正文资格 |
| release-candidate-071 | exclude | - | 单源不具备正文资格 |
| release-candidate-072 | exclude | - | 单源不具备正文资格 |
| release-candidate-073 | exclude | - | 单源不具备正文资格 |
| release-candidate-074 | exclude | - | 单源不具备正文资格 |
| release-candidate-075 | exclude | - | 单源不具备正文资格 |
| release-candidate-076 | exclude | - | 单源不具备正文资格 |
| release-candidate-077 | exclude | - | 单源不具备正文资格 |
| release-candidate-078 | exclude | - | 单源不具备正文资格 |
| release-candidate-079 | exclude | - | 单源不具备正文资格 |
| release-candidate-080 | exclude | - | 单源不具备正文资格 |
| release-candidate-081 | exclude | - | 单源不具备正文资格 |
| release-candidate-082 | exclude | - | 单源不具备正文资格 |
| release-candidate-083 | exclude | - | 单源不具备正文资格 |
| release-candidate-084 | exclude | - | 单源不具备正文资格 |
| release-candidate-085 | exclude | - | 单源不具备正文资格 |
| release-candidate-086 | exclude | - | 单源不具备正文资格 |
| release-candidate-087 | exclude | - | 单源不具备正文资格 |
| release-candidate-088 | exclude | - | 单源不具备正文资格 |
| release-candidate-089 | exclude | - | 单源不具备正文资格 |
| release-candidate-090 | exclude | - | 单源不具备正文资格 |
| release-candidate-091 | exclude | - | 单源不具备正文资格 |
| release-candidate-092 | exclude | - | 单源不具备正文资格 |
| release-candidate-093 | exclude | - | 单源不具备正文资格 |
| release-candidate-094 | exclude | - | 单源不具备正文资格 |
| release-candidate-095 | exclude | - | 单源不具备正文资格 |
| release-candidate-096 | exclude | - | 单源不具备正文资格 |
| release-candidate-097 | exclude | - | 单源不具备正文资格 |
| release-candidate-098 | exclude | - | 单源不具备正文资格 |
| release-candidate-099 | exclude | - | 单源不具备正文资格 |
| release-candidate-100 | exclude | - | 单源不具备正文资格 |
| release-candidate-101 | exclude | - | 单源不具备正文资格 |
| release-candidate-102 | exclude | - | 单源不具备正文资格 |
| release-candidate-103 | exclude | - | 单源不具备正文资格 |
| release-candidate-104 | exclude | - | 单源不具备正文资格 |
| release-candidate-105 | exclude | - | 单源不具备正文资格 |
| release-candidate-106 | exclude | - | 单源不具备正文资格 |
| release-candidate-107 | exclude | - | 单源不具备正文资格 |
| release-candidate-108 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-003 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-109 | exclude | - | 单源不具备正文资格 |
| release-candidate-110 | exclude | - | 单源不具备正文资格 |
| release-candidate-111 | exclude | - | 单源不具备正文资格 |
| release-candidate-112 | exclude | - | 单源不具备正文资格 |
| release-candidate-113 | exclude | - | 单源不具备正文资格 |
| release-candidate-114 | exclude | - | 单源不具备正文资格 |
| release-candidate-115 | exclude | - | 单源不具备正文资格 |
| release-candidate-116 | exclude | - | 单源不具备正文资格 |
| release-candidate-117 | exclude | - | 单源不具备正文资格 |
| release-candidate-118 | exclude | - | 单源不具备正文资格 |
| release-candidate-119 | exclude | - | 单源不具备正文资格 |
| release-candidate-120 | exclude | - | 单源不具备正文资格 |
| release-candidate-121 | exclude | - | 单源不具备正文资格 |
| release-candidate-122 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-123 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-124 | exclude | - | 单源不具备正文资格 |
| release-candidate-125 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-126 | exclude | - | 单源不具备正文资格 |
| release-candidate-127 | exclude | - | 单源不具备正文资格 |
| release-candidate-128 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-129 | exclude | - | 单源不具备正文资格 |
| release-candidate-130 | exclude | - | 单源不具备正文资格 |
| release-candidate-131 | exclude | - | 单源不具备正文资格 |
| release-candidate-132 | exclude | - | 单源不具备正文资格 |
| release-candidate-133 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-134 | exclude | - | 单源不具备正文资格 |
| release-candidate-135 | exclude | - | 单源不具备正文资格 |
| release-candidate-136 | exclude | - | 单源不具备正文资格 |
| release-candidate-137 | exclude | - | 单源不具备正文资格 |
