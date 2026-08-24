# Selection Decisions

**卡片曝光去重：** 苹果费率与灵犀交易均有历史卡片曝光，按repeat_only排除；Makers Fund历史card_exposed=false，但本期总分4低于门槛，不具备内部补位资格；本期补位=无。

**维度覆盖自检：** 国内移动 3张 / 国产产品与人才 2张 / 市场数据 5张 / 并购 3张 / 平台政策 5张 / 档期变动 2张 / 资本组织 3张 / 海外重大 6张。产品日历另由release_calendar_audit.json全量反扫。

**产品日历漏挂反查：** 已反扫industry_news全部上线、定档、测试、首曝与跨平台信号；合格节点均进入release_calendar_audit.json，越窗、单源和普通版本节点已显式排除。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 国内核心创作者离职并披露明确新项目，E3×R3+M1=10。 事件3×相关3+钩子1 = 10。 |
| I002 | include | industry_news | 国内游戏创业基础设施正式落地并给出明确扶持条件，E3×R3+M1=10。 事件3×相关3+钩子1 = 10。 |
| I003 | include | industry_news | 拳头固定R=3，项目停止开发获多源同日覆盖，E2×R3+M2=8。 事件2×相关3+钩子2 = 8。 |
| I004 | include | industry_news | 国产重度新品披露公测第二日经营数据，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I005 | include | industry_news | 国内小游戏披露日活、订单结构和团队规模，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I006 | include | industry_news | 国内厂商移动产品披露下载、IAP与投放变化，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I007 | include | industry_news | PVP优先赛道出现重大系统档期调整，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I101 | exclude | industry_news | 历史已有订阅卡片曝光，本期仅为换来源复述。 事件2×相关2+钩子1 = 5。 |
| I102 | exclude | industry_news | 正式协议已多次曝光；本期正文没有可验证的新交易事实。 事件3×相关3+钩子1 = 10。 |
| I103 | exclude | industry_news | 历史完整报告未进卡片，但当前总分4低于周末报门槛，不可竞争card_carryover。 事件3×相关1+钩子1 = 4。 |
| I104 | exclude | industry_news | 重大资本动作但与移动及优先赛道迁移较弱，总分5。 事件3×相关1+钩子2 = 5。 |
| I105 | exclude | industry_news | 移动市场数据具迁移价值，但当前报道缺少强窗口钩子，总分5。 事件2×相关2+钩子1 = 5。 |
| I106 | exclude | industry_news | 平台商业化变化对游戏直播有迁移点，但证据为snippet且总分5。 事件2×相关2+钩子1 = 5。 |
| I107 | exclude | industry_news | 移动广告结构信号但证据为snippet且总分5。 事件2×相关2+钩子1 = 5。 |
| I108 | exclude | industry_news | 移动赛道数据有迁移点但缺少独立状态变化，总分5。 事件2×相关2+钩子1 = 5。 |
| I109 | exclude | industry_news | 未证明相对一致预期或指引的显著异常，适用财报例外排除。 事件0×相关3+钩子1 = 1。 |
| I110 | exclude | industry_news | 海外泄露处置与移动及优先赛道迁移较弱，总分4。 事件2×相关1+钩子2 = 4。 |
| A001 | include | ai_news | 三套模型已直接用于游戏平台安全运营。 |
| A002 | include | ai_news | 工具直接覆盖原型、迭代、修Bug与素材流程。 |
| A003 | include | ai_news | 来源给出策划检索、美术生成、Agent协作与人工审核的完整链路。 |
| A101 | exclude | ai_news | 核心事件发生在7月28日，本期仅晚到整理，缺少窗口内新状态。 |
| A102 | exclude | ai_news | 没有来源证明已进入具体游戏环节，无法建立合格迁移链。 |
| C001 | include | community_discourse | 触发点、对立意见与两日时间线完整。 |
| C002 | include | community_discourse | 具体触发、玩家争议逻辑与帖主所称热修后续齐全。 |
| C101 | exclude | community_discourse | 原帖建于8月13日，本窗口仅零星回复，没有新裁判或退款进展。 |
| C102 | exclude | community_discourse | 帖子自身承认初始证据仅为少数评论，争议机制和后续不足。 |
| D001 | include | deep_analysis | 单篇高质量newsletter提供销量、愿望单、玩家重合与社交传播证据链。 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-006 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-007 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-013 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-014 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-015 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-019 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-025 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-041 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-042 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-043 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | 事件日期不在报告窗口 |
