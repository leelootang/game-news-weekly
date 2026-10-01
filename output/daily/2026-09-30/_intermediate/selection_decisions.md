# Selection Decisions

- 卡片曝光去重：历史匹配的Circle Games融资、拳头广州公司、《伊莫》移动端事件均已有card_exposed=true，全部按repeat_only排除；《怪物猎人：旅人》有档期新增事实但同一产品日历节点已在上一期发布。无全部历史匹配均未曝光且达到门槛的事件，本期card_carryover=0。
- 维度覆盖自检：国内移动/国产产品与人才 8张；市场数据 2张；并购/资产变化 2张；平台政策 2张；档期变动 6张；资本组织 4张；海外重大 9张。
- 产品日历漏挂反查：industry_news与release_calendar全量输入均已扫描；《尼瓦利斯之夜》正文明确9月29日上线，已纠正相对日期误判；《风暴崛起：维提之怒》按老品重大资料片而非新品上线计分；本期无同时满足多源与绝对日期证据的可发布节点。
- 行业新闻 E×R+M 打分记录：I001 事件3×相关3+钩子2 = 11 include；I002 事件3×相关3+钩子1 = 10 include；I003 事件3×相关3+钩子1 = 10 include；I004 事件3×相关3+钩子1 = 10 include；I005 事件3×相关2+钩子2 = 8 include；I006 事件3×相关2+钩子1 = 7 include；IX001 事件2×相关2+钩子2 = 6 exclude；IX002 事件2×相关2+钩子2 = 6 exclude；IX003 事件2×相关2+钩子2 = 6 exclude；IX004 事件2×相关2+钩子1 = 5 exclude；IR001 事件3×相关3+钩子2 = 11 exclude；IR002 事件3×相关3+钩子1 = 10 exclude；IR003 事件2×相关3+钩子1 = 7 exclude；IM001 事件2×相关3+钩子2 = 8 exclude；IX005 事件0×相关3+钩子2 = 2 exclude

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | 行业新闻 | E3×R3+M2=11；国内厂商海外资产关系发生实质变化，多源确认工作室恢复独立。 |
| I002 | include | 行业新闻 | E3×R3+M1=10；国内厂商在研新品信号明确，岗位同时披露题材、赛季制与跨端方向。 |
| I003 | include | 行业新闻 | E3×R3+M1=10；国产独立团队首款产品公开试玩并出现可验证阶段表现。 |
| I004 | include | 行业新闻 | E3×R3+M1=10；国内移动硬件与主流引擎建立图形技术合作，命中移动游戏研发链。 |
| I005 | include | 行业新闻 | E3×R2+M2=8；高融资海外工作室进入破产管理并清空人员，对全球大型项目投资与组织扩张有明确迁移点。 |
| I006 | include | 行业新闻 | E3×R2+M1=7；移动益智新品恢复测试并披露产品结构变化，达到日报门槛。 |
| IX001 | exclude | - | E2×R2+M2=6；平台分发政策多源明确，但对中国移动与优先赛道迁移点不足，低于日报门槛。 |
| IX002 | exclude | - | E2×R2+M2=6；全球市场预测有结构信息但国内与移动迁移点不足。 |
| IX003 | exclude | - | E2×R2+M2=6；海外移动老品停运与累计收入数据不足以达到日报门槛。 |
| IX004 | exclude | - | E2×R2+M1=5；属于分析师预测且来源为snippet，证据与迁移强度均不足。 |
| IR001 | exclude | - | 历史同事件已进入2026-09-29日报并完成卡片曝光；本期仅为换源复述。 |
| IR002 | exclude | - | 历史同事件已进入2026-09-29日报并完成卡片曝光；本期没有实质状态变化。 |
| IR003 | exclude | - | 历史同一移动端上线与多市场榜位事件已有card_exposed=true记录；本期仅重复既有榜位事实。 |
| IM001 | exclude | - | 相对历史测试计划出现实质档期更新，但同一产品日历节点已在2026-09-29报告发布，本期跨报告去重。 |
| IX005 | exclude | - | E=0；版号信息按规则直接排除。 |
| A001 | include | AI 新闻 | 直接作用类；自然语言游戏生成、编辑、运营和分发形成完整链路。 |
| A002 | include | AI 新闻 | 直接作用类；来源给出研发资产进包、局内AI队友和长期记忆NPC等已落地环节。 |
| A003 | include | AI 新闻 | 直接作用类；AI工具已经改变游戏公司的招聘、外包与团队结构。 |
| AX001 | exclude | - | 直接作用信号存在，但主要证据集中直播与泛互动内容，游戏业务落地弱于前三项。 |
| AX002 | exclude | - | 直接作用于玩家剪辑工具，但行业生产与运营影响较弱。 |
| AX003 | exclude | - | 研究以游戏为评测环境，尚未形成游戏研发、产品或运营迁移链。 |
| AX004 | exclude | - | 未形成由本期来源直接支持的具体游戏研发、产品、发行或运营迁移路径。 |
| C001 | include | 玩家舆论 | 同日新帖，触发、玩家质疑与当时后续状态完整。 |
| C002 | include | 玩家舆论 | 付费限定、命座获取与首充重置形成可命名的变现争议，窗口内仍有新回复。 |
| CX001 | exclude | - | 同一事件已在2026-09-25_to_2026-09-27周末报及2026-09-28日报发布；本期只有延续回复。 |
| CX002 | exclude | - | 同一停服转单机与众筹争议已在2026-09-28日报发布；本期无实质新状态。 |
| CX003 | exclude | - | 9月19日旧帖，本期仅新增一条技术讨论回复，没有新的处罚或官方状态。 |
| D001 | include | 深度观察 | R2/I3/E3/C3=11；单篇高质量数据分析完整覆盖变化、机制与下游影响。 |
| DX001 | exclude | - | R1/I2/E3/C2=8；组织机制清楚，但国内、移动与优先赛道迁移点较弱。 |
| release-candidate-003 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-004 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | - | 单源不具备正文资格 |
| release-candidate-006 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-001 | exclude | - | 多源成立，但来源正文仅含‘今日/现已’相对时间，缺少绝对事件日期证据，不得发布 |
| release-candidate-007 | exclude | - | 单源不具备正文资格 |
| release-candidate-008 | exclude | - | 同一产品+事件日期+事件已进入2026-09-29已发布产品日历，跨报告重复 |
| release-candidate-009 | exclude | - | 单源不具备正文资格 |
| release-candidate-010 | exclude | - | 单源不具备正文资格 |
| release-candidate-011 | exclude | - | 单源不具备正文资格 |
| release-candidate-012 | exclude | - | 单源不具备正文资格 |
| release-candidate-013 | exclude | - | 单源不具备正文资格 |
| release-candidate-014 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-016 | exclude | - | 同一产品+事件日期+事件已进入2026-09-29已发布产品日历，跨报告重复 |
| release-candidate-017 | exclude | - | 单源不具备正文资格 |
| release-candidate-018 | exclude | - | 单源不具备正文资格 |
| release-candidate-019 | exclude | - | 单源不具备正文资格 |
| release-candidate-020 | exclude | - | 单源不具备正文资格 |
| release-candidate-021 | exclude | - | 单源不具备正文资格 |
| release-candidate-022 | exclude | - | 单源不具备正文资格 |
| release-candidate-023 | exclude | - | 单源不具备正文资格 |
| release-candidate-024 | exclude | - | 单源不具备正文资格 |
| release-candidate-025 | exclude | - | 单源不具备正文资格 |
| release-candidate-026 | exclude | - | 单源不具备正文资格 |
| release-candidate-027 | exclude | - | 单源不具备正文资格 |
| release-candidate-028 | exclude | - | 单源不具备正文资格 |
| release-candidate-029 | exclude | - | 单源不具备正文资格 |
| release-candidate-002 | exclude | - | 多源成立，但来源正文仅含‘今日/现已’相对时间，缺少绝对事件日期证据，不得发布 |
| release-candidate-030 | exclude | - | 单源不具备正文资格 |
| release-candidate-031 | exclude | - | 单源不具备正文资格 |
| release-candidate-032 | exclude | - | 单源不具备正文资格 |
| release-candidate-033 | exclude | - | 单源不具备正文资格 |
| release-candidate-034 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-035 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-036 | exclude | - | 单源不具备正文资格 |
