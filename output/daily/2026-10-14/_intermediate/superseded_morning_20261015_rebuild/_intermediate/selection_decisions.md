# Selection Decisions

- 卡片曝光去重：双周窗口 2026-09-30..2026-10-13；3 条历史同事件均已卡片曝光并判为 repeat_only；本期无 card_carryover，未占用补位名额。
- 维度覆盖自检：国内移动/国产产品与人才 8 张；市场数据 4 张；并购融资 5 张；平台政策 4 张；档期变动 6 张；资本组织 5 张；海外重大 7 张。
- AI 反扫：行业候选中的游族AI管线、Google Play AI推荐、Epic AI制作、AdSurge与AI游戏销量均已转入AI候选审计；同一事件不跨栏重复。
- 产品日历漏挂反查：已扫描 industry_news 与 release_calendar 全量输入；合并《不朽遗志》和《全面战争：幕府将军2 完全版》别名，但两者及《动物园之星2》缺正文绝对日期而排除；补入Gematsu的《1999 TOKOYO Building》结构化来源。
- 深度观察：优先读取本期 newsletter；D001 与上一期Velan工作室组合主题不撞题。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子2 = 11；国内厂商对海外休闲手游团队的重大投资，多源且含产品增长数据。 |
| I002 | include | industry_news | 事件3×相关3+钩子2 = 11；国内游戏公司首次公开投资AI企业，资本与董事会关系均有多源证据。 |
| I003 | include | industry_news | 事件3×相关2+钩子2 = 8；大型平台设立面向浏览器发行、移植与模组支持的正式研发机制。 |
| I004 | include | industry_news | 事件2×相关3+钩子2 = 8；最高关注主体的产品进入明确停运节点，多源覆盖下架与关服日期。 |
| I005 | include | industry_news | 事件2×相关3+钩子1 = 7；国内平台政策出现结构性变化，来源给出精品工程与优质内容供给方向。 |
| I006 | include | industry_news | 事件2×相关3+钩子1 = 7；国内PVP新品在外部导流结束后出现可核验的一月成绩与玩家付费案例。 |
| I007 | exclude | industry_news | 事件2×相关2+钩子2 = 6；海外工作室关闭与裁员有结构信号，但R=2时总分6，未达日报门槛。 |
| I008 | exclude | industry_news | 事件2×相关3+钩子0 = 6；同一三季度移动IAP下滑数据已在上一份日报订阅卡片展示。 |
| I009 | exclude | industry_news | 事件2×相关3+钩子0 = 6；同一5800万DAU事件已经完成卡片曝光，当前采访未形成可验证的新状态。 |
| I010 | exclude | industry_news | 事件2×相关2+钩子1 = 5；销量稿正文锚定2025年旧事件，PVE测试已在上一份日报曝光，无本期新状态。 |
| I011 | exclude | industry_news | 事件2×相关1+钩子1 = 3；海外小型商店关闭，迁移点有限，总分3。 |
| I012 | exclude | industry_news | 事件0×相关3+钩子1 = 1；固定关注主体，但事件属于例行赛事与社区推广，E=0。 |
| A001 | include | ai_trends | AI生成内容、角色对话与商业结果均由完整正文直接支持。 |
| A002 | include | ai_trends | AI已直接进入游戏研发、发行、运营与智能NPC，应用链条完整。 |
| A003 | include | ai_trends | 多源支持AI已直接用于游戏分发与个性化推荐。 |
| A004 | exclude | ai_trends | 同一事件已进入2026-10-13日报AI新闻，本期仅为重复覆盖。 |
| A005 | exclude | ai_trends | 平台事件完整，但AI具体机制只由受限摘要概括，证据密度低于本期三项。 |
| A006 | exclude | ai_trends | 直接应用成立，但在本期AI候选中优先级低于游戏产品、研发管线与移动分发平台。 |
| C001 | include | community_discourse | 触发文本、质疑逻辑、反方意见与窗口内延续时间均可核验。 |
| C002 | include | community_discourse | 报告日新事件，原图水印、替换动作与玩家争议路径均在帖子中留痕。 |
| D001 | include | deep_analysis | 单篇高质量newsletter提供跨产品比较、销量与CCU锚点，并形成明确留存机制。 |
| I900 | exclude | industry_news | 事件0×相关0+钩子0 = 0；逐条扫过完整索引与正文；均为E=0或缺少可核验的新事件，不进入独立高分候选。 |
| A900 | exclude | ai_trends | 未形成游戏研发、产品、发行或运营的直接作用，也缺少可解释的游戏迁移链条。 |
| C900 | exclude | community_discourse | 未同时满足触发、争议逻辑、窗口时间线和可核验后续，或价值低于本期两项上限。 |
| release-candidate-002 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-004 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-006 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | 多源但正文没有可直接支持10月14日事件日期的绝对日期文本，不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 多源但正文没有可直接支持10月14日事件日期的绝对日期文本，不具备正文资格 |
| release-candidate-001 | exclude | release_calendar | 多源但正文没有可直接支持10月14日事件日期的绝对日期文本，不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-009 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-018 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-041 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-043 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-044 | exclude | release_calendar | 事件日期不在报告窗口 |
