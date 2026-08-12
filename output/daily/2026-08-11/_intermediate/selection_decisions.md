# 2026-08-11 选择决策

- 卡片曝光去重：I008匹配H085，历史唯一匹配项card_exposed=false、card_rank为空（周报行业卡片前10之外），本期E2×R3+M1=7，获唯一card_carryover；I009匹配H092且card_exposed=true，按repeat_only排除；I010匹配H061/H083，其中H061 card_exposed=true，按repeat_only排除。无第二条补位。
- 维度覆盖自检：国内移动/国产产品与人才 12张；市场数据 8张；并购/资产处置 3张；平台政策 6张；档期变动 6张；资本组织 9张；海外重大 15张。其余例行宣传与低事件类型记录进入I199批量审计。
- AI反扫：全部行业候选均已复核；BSide停运、Aivilization成本边界、游密语音4.0转入AI新闻。
- 产品日历漏挂反查：industry_news与release_calendar全量输入已进入release_calendar_audit.json；由sync_release_decisions.py按多源优先级前缀确定2条include，其余全部留痕排除。


## 行业新闻 E×R+M 打分

- I001: 事件3×相关3+钩子2 = 11；include；国内游戏资产发生重大剥离，双来源覆盖且达到日报阈值。
- I002: 事件2×相关3+钩子2 = 8；include；中国移动产品与Roblox同时出现新的全球月度市场数据，双来源覆盖。
- I003: 事件2×相关3+钩子1 = 7；include；国内英雄战术射击手游披露新的亿级注册用户节点。
- I004: 事件2×相关3+钩子1 = 7；include；国内小游戏市场出现新的月度品类与厂商结构数据。
- I005: 事件2×相关3+钩子1 = 7；include；国产移动新品披露首周可验证市场表现。
- I006: 事件2×相关3+钩子1 = 7；include；国内竞技产品出现用户、ARPU和新模式的同阶段实质数据。
- I007: 事件2×相关3+钩子1 = 7；include；国产移动产品在合成赛道出现新的全球市场表现。
- I008: 事件2×相关3+钩子1 = 7；include；历史同事件此前未进入订阅卡片，本期再次召回且仍达到日报阈值，获唯一内部补位。
- I009: 事件2×相关3+钩子1 = 7；exclude；同一月度出海数据已在昨日完整报告与订阅卡片发布，本期仅换来源重述。
- I010: 事件3×相关3+钩子1 = 10；exclude；同一首测、团队规模和产品定位已发布，且历史匹配项曾进入订阅卡片。
- I011: 事件3×相关3+钩子2 = 11；exclude；同一事件转入产品日历，避免跨栏重复。
- I012: 事件2×相关3+钩子2 = 8；exclude；事件核心是AI陪伴产品的生命周期变化，转入AI新闻。
- I013: 事件2×相关2+钩子2 = 6；exclude；E2×R2+M2=6，未达日报阈值。
- I014: 事件2×相关2+钩子2 = 6；exclude；E2×R2+M2=6，未达日报阈值。
- I015: 事件2×相关2+钩子2 = 6；exclude；E2×R2+M2=6，组织品牌调整未达日报阈值。
- I016: 事件2×相关2+钩子1 = 5；exclude；E2×R2+M1=5，平台迁移信号未达日报阈值。
- I017: 事件2×相关1+钩子2 = 4；exclude；E2×R1+M2=4，海外一般产品数据迁移点有限。
- I018: 事件1×相关1+钩子2 = 3；exclude；E1×R1+M2=3，纯海外裁员未达日报阈值。
- I019: 事件3×相关1+钩子2 = 5；exclude；E3×R1+M2=5，未达日报阈值且尚无交易落地。
- I020: 事件2×相关2+钩子1 = 5；exclude；E2×R2+M1=5，区域政策讨论未达日报阈值。
- I021: 事件2×相关1+钩子1 = 3；exclude；E2×R1+M1=3，海外一般独立产品数据迁移点有限。
- I022: 事件0×相关1+钩子1 = 1；exclude；常规财报与同比变化，不满足财报例外。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | 行业新闻 | 国内游戏资产发生重大剥离，双来源覆盖且达到日报阈值。 |
| I002 | include | 行业新闻 | 中国移动产品与Roblox同时出现新的全球月度市场数据，双来源覆盖。 |
| I003 | include | 行业新闻 | 国内英雄战术射击手游披露新的亿级注册用户节点。 |
| I004 | include | 行业新闻 | 国内小游戏市场出现新的月度品类与厂商结构数据。 |
| I005 | include | 行业新闻 | 国产移动新品披露首周可验证市场表现。 |
| I006 | include | 行业新闻 | 国内竞技产品出现用户、ARPU和新模式的同阶段实质数据。 |
| I007 | include | 行业新闻 | 国产移动产品在合成赛道出现新的全球市场表现。 |
| I008 | include | 行业新闻 | 历史同事件此前未进入订阅卡片，本期再次召回且仍达到日报阈值，获唯一内部补位。 |
| I009 | exclude | - | 同一月度出海数据已在昨日完整报告与订阅卡片发布，本期仅换来源重述。 |
| I010 | exclude | - | 同一首测、团队规模和产品定位已发布，且历史匹配项曾进入订阅卡片。 |
| I011 | exclude | - | 同一事件转入产品日历，避免跨栏重复。 |
| I012 | exclude | - | 事件核心是AI陪伴产品的生命周期变化，转入AI新闻。 |
| I013 | exclude | - | E2×R2+M2=6，未达日报阈值。 |
| I014 | exclude | - | E2×R2+M2=6，未达日报阈值。 |
| I015 | exclude | - | E2×R2+M2=6，组织品牌调整未达日报阈值。 |
| I016 | exclude | - | E2×R2+M1=5，平台迁移信号未达日报阈值。 |
| I017 | exclude | - | E2×R1+M2=4，海外一般产品数据迁移点有限。 |
| I018 | exclude | - | E1×R1+M2=3，纯海外裁员未达日报阈值。 |
| I019 | exclude | - | E3×R1+M2=5，未达日报阈值且尚无交易落地。 |
| I020 | exclude | - | E2×R2+M1=5，区域政策讨论未达日报阈值。 |
| I021 | exclude | - | E2×R1+M1=3，海外一般独立产品数据迁移点有限。 |
| I022 | exclude | - | 常规财报与同比变化，不满足财报例外。 |
| I199 | exclude | - | 逐条反扫后为E=0、财报例外不成立或E×R+M低于5；不扩写完整候选卡。 |
| A001 | include | AI新闻 | AI直接作用于虚拟角色陪伴，产品生命周期变化由公告与两家行业来源覆盖。 |
| A002 | include | AI新闻 | 来源直接披露AI原生游戏从角色智能扩展到世界智能后的成本、玩法和团队变化。 |
| A003 | include | AI新闻 | 来源明确AI在游戏语音降噪、声音增强与设备识别中的直接应用和测试状态。 |
| A004 | exclude | - | 调查反映预期而非已经发生的能力或游戏业务落地。 |
| A005 | exclude | - | 没有来源支持的具体游戏迁移链条。 |
| A099 | exclude | - | 缺少游戏直接应用或可由来源支撑的具体迁移链条。 |
| C001 | include | 玩家舆论 | 报告日新帖，触发、玩家担忧、补偿获取争议与时间线清楚。 |
| C002 | include | 玩家舆论 | 报告日新帖，技术主张、争议逻辑、不同观点与时间线完整。 |
| C003 | exclude | - | 同一事件已进入AI新闻，避免跨栏重复。 |
| C004 | exclude | - | 同一社区事件已在昨日完整报告发布，本期只有后续回复，没有新官方状态。 |
| C005 | exclude | - | 原帖始于8月3日，报告日仅单条延续回复，没有新的官方动作或状态变化。 |
| C006 | exclude | - | 正文未抽取判决书原文，关键法律事实仅来自玩家转述，证据链不足。 |
| C099 | exclude | - | 未同时满足触发、争议逻辑、窗口内时间线与后续扫描。 |
| D001 | include | 深度观察 | 单篇高质量访谈提供完整的变化—机制—下游影响证据链。 |
| D002 | exclude | - | 抽取正文仅375字，未展开游戏小程序机制，证据不足以支撑两段分析。 |
| D003 | exclude | - | 核心数据已进入行业新闻，单一报告不足以再构成独立综合深度主题。 |
| release-candidate-001 | include | 产品日历 | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | include | 产品日历 | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | exclude | - | 单源不具备正文资格 |
| release-candidate-004 | exclude | - | 单源不具备正文资格 |
| release-candidate-005 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-006 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-007 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-008 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-010 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-011 | exclude | - | 单源不具备正文资格 |
| release-candidate-012 | exclude | - | 单源不具备正文资格 |
| release-candidate-013 | exclude | - | 单源不具备正文资格 |
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
| release-candidate-026 | exclude | - | 单源不具备正文资格 |
| release-candidate-027 | exclude | - | 单源不具备正文资格 |
| release-candidate-028 | exclude | - | 单源不具备正文资格 |
| release-candidate-029 | exclude | - | 单源不具备正文资格 |
| release-candidate-030 | exclude | - | 单源不具备正文资格 |
| release-candidate-031 | exclude | - | 单源不具备正文资格 |
| release-candidate-032 | exclude | - | 单源不具备正文资格 |
| release-candidate-033 | exclude | - | 单源不具备正文资格 |
| release-candidate-034 | exclude | - | 单源不具备正文资格 |
| release-candidate-035 | exclude | - | 单源不具备正文资格 |
| release-candidate-036 | exclude | - | 单源不具备正文资格 |
| release-candidate-037 | exclude | - | 单源不具备正文资格 |
| release-candidate-038 | exclude | - | 单源不具备正文资格 |
| release-candidate-039 | exclude | - | 单源不具备正文资格 |
| release-candidate-040 | exclude | - | 单源不具备正文资格 |
| release-candidate-041 | exclude | - | 单源不具备正文资格 |
| release-candidate-042 | exclude | - | 单源不具备正文资格 |
| release-candidate-043 | exclude | - | 单源不具备正文资格 |
| release-candidate-044 | exclude | - | 单源不具备正文资格 |
| release-candidate-045 | exclude | - | 单源不具备正文资格 |
| release-candidate-046 | exclude | - | 单源不具备正文资格 |
| release-candidate-047 | exclude | - | 单源不具备正文资格 |
| release-candidate-048 | exclude | - | 单源不具备正文资格 |
| release-candidate-049 | exclude | - | 单源不具备正文资格 |
| release-candidate-050 | exclude | - | 单源不具备正文资格 |
| release-candidate-051 | exclude | - | 单源不具备正文资格 |
| release-candidate-052 | exclude | - | 单源不具备正文资格 |
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
| release-candidate-094 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-095 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-096 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-097 | exclude | - | 单源不具备正文资格 |
