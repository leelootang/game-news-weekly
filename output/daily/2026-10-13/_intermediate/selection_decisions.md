# Selection Decisions

- 卡片曝光去重：历史匹配共4个独立行业事件，全部存在 `card_exposed=true` 记录，均按 `repeat_only` 排除；本期无可竞争的 `card_carryover`。
- 维度覆盖自检：国内移动/国产产品与人才 9 张；市场数据 4 张；并购/投融资 3 张；平台政策 2 张；档期变动 6 张；资本组织 4 张；海外重大 7 张。其余例行宣传、评测、联动、硬件与非游戏记录归入 I900 批量审计。
- 产品日历漏挂反查：完整扫描 industry_news 与 release_calendar；按规范化产品名+事件日期聚类，只有多源候选前缀可入选，日报上限4条；《连城绝：大唐》两条记录同属一个来源域，不计独立多源。
- 行业新闻 E×R+M 打分记录：每条行业候选均按“事件E×相关R+钩子M = 终分”记录，日报终分≥7且通过证据与历史门禁方可入选。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 移动广告平台完成直接影响游戏与应用变现的渠道合作。 事件3×相关3+钩子1 = 10。 |
| I002 | exclude | industry_news | 事件达到分数线，但唯一正文为受限站点摘要，禁止把snippet作为终稿证据。 事件3×相关3+钩子1 = 10。 |
| I003 | include | industry_news | 香港游戏硬件公司完成重大融资，并披露百万销量与订阅规模。 事件3×相关3+钩子1 = 10。 |
| I004 | include | industry_news | 国内游戏生态服务商启用核心研发载体并披露转型业务结构。 事件3×相关3+钩子1 = 10。 |
| I005 | include | industry_news | 国内厂商新品首曝，命中模拟经营/生活模拟邻近赛道且含测试形态。 事件3×相关3+钩子1 = 10。 |
| I006 | include | industry_news | 腾讯长青PVP手游出现明确全球化发行节点。 事件3×相关3+钩子1 = 10。 |
| I007 | include | industry_news | 多源覆盖中国移动渠道、开发者出海与DTC支付结构数据。 事件2×相关3+钩子2 = 8。 |
| I008 | include | industry_news | 多源市场报告同时揭示并购资本集中和移动IAP下滑。 事件2×相关3+钩子2 = 8。 |
| I009 | include | industry_news | 腾讯代理的PVPVE产品出现可核验在线回升与运营节奏变化。 事件2×相关3+钩子1 = 7。 |
| I010 | exclude | industry_news | 同一治理结构变更已在上一份日报订阅卡片展示。 事件3×相关3+钩子1 = 10。 |
| I011 | exclude | industry_news | 同一9月榜单结构已经进入日报与周报订阅卡片。 事件2×相关3+钩子2 = 8。 |
| I012 | exclude | industry_news | 同一DAU数据已在周末报完成卡片曝光。 事件2×相关3+钩子0 = 6。 |
| I013 | exclude | industry_news | 场地、IP、NPC与到场传播数据均已进入历史订阅卡片，无新增状态。 事件2×相关3+钩子1 = 7。 |
| I014 | exclude | industry_news | 海外移动IP经营数据有迁移价值，但核心数据为季度复盘且单源，总分5。 事件2×相关2+钩子1 = 5。 |
| I015 | exclude | industry_news | 移动厂商重组策略有迁移点，但属于单篇访谈与渐进调整，总分5。 事件2×相关2+钩子1 = 5。 |
| I016 | exclude | industry_news | 老品跨平台有移动迁移价值，但事件类型较低，总分5。 事件1×相关3+钩子2 = 5。 |
| I017 | exclude | industry_news | 国内品类研究有价值，但核心数据止于2025年、无本期新钩子，总分6。 事件2×相关3+钩子0 = 6。 |
| I018 | exclude | industry_news | 多源战略表态缺少新项目、资本或组织状态变化，总分4。 事件1×相关2+钩子2 = 4。 |
| I019 | exclude | industry_news | 标题显示技术迁移，但抓取正文未包含事件细节，证据不足；按边界总分5留档。 事件2×相关2+钩子1 = 5。 |
| I900 | exclude | industry_news | 逐条标题与正文反扫后均为E=0，或缺少可核验新状态；按规则允许批量审计。 事件0×相关0+钩子0 = 0。 |
| A001 | include | ai_trends | AI已直接进入游戏代码、美术和试玩迭代流程，且有多源交叉覆盖。 |
| A002 | include | ai_trends | AI已直接作用于角色聊天、约会、语音、动作、表情与长期记忆。 |
| A003 | include | ai_trends | 可玩的游戏成品直接验证自然语言生成对个人开发门槛的影响。 |
| A004 | exclude | ai_trends | 长篇人物叙事有观察价值，但没有单一可核验的产品或业务状态变化。 |
| A005 | exclude | ai_trends | 案例更偏互动影视，游戏化链条弱于本期三条直接游戏应用。 |
| C001 | include | community_discourse | 当日新帖形成围绕网络梗开放传播与商业收编边界的可命名争议。 |
| C002 | include | community_discourse | 旧内容在窗口内被重新发现并持续讨论，争议机制清晰。 |
| C003 | exclude | community_discourse | 同一事件已进入上一份日报，窗口内只有讨论延续、无新状态。 |
| C004 | exclude | community_discourse | 核心为停服事实与零散玩笑，缺少足够完整的当日争议机制。 |
| C005 | exclude | community_discourse | 帖子始于10月8日，窗口内仅有单条延续回复，缺少新进展。 |
| D001 | include | deep_analysis | 单篇高质量访谈提供项目组合、核心团队、外包效率和IP合作的完整机制链；相较9月29日与10月6日相邻主题，新增“授权IP双A+小团队原创”的错峰组合证据。 |
| D002 | exclude | deep_analysis | 正文仅244字，无法支撑完整机制、前提与下游影响链。 |
| D003 | exclude | deep_analysis | 榜单事件已在历史报告与卡片曝光，且本期没有新的机制证据。 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-004 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-002 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-006 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-009 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-012 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-013 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-014 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 单源不具备正文资格 |
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
| release-candidate-038 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-039 | exclude | release_calendar | 事件日期不在报告窗口 |
