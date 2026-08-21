# 选择决策

- 卡片曝光去重：历史匹配项逐条读取 card_exposed/card_rank/card_limit/card_exposure_source；repeat_only 排除 6 条；card_carryover 选择 0 条。无从未曝光且本期再次召回、达到8分线的合格同事件。
- 维度覆盖自检：国内移动/国产产品与人才 19张候选 / 市场数据 9张候选 / 并购 5张候选 / 平台政策 5张候选 / 档期变动 10张候选 / 资本组织 7张候选 / 海外重大 9张候选
- 产品日历漏挂反查：已反扫 industry_news 的上线、定档、测试与首曝节点；合格项升入 release audit，其余显式 exclude。
- 行业新闻打分格式：事件3×相关3+钩子2 = 11；每条候选均按同一公式记录。
- 周报跨期去重：本周日报与周末报事件只合并一次；同一事实不拆条。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子2 = 11；国内成熟游戏资产的重大股权交易从待确认推进到正式协议，并确认管理团队留任。；本周窗口日报/周末报事件合并一次 |
| I002 | include | industry_news | 事件3×相关3+钩子2 = 11；国产在研产品完成首次大规模玩家试玩并披露团队与研发阶段，多源形成强窗口钩子。；本周窗口日报/周末报事件合并一次 |
| I003 | include | industry_news | 事件3×相关3+钩子2 = 11；国内厂商首次投资英国工作室；两家独立行业媒体报道同一融资与组建事件。；本周窗口日报/周末报事件合并一次 |
| I004 | include | industry_news | 事件3×相关3+钩子2 = 11；核心人才创业与明确在研项目同时成立；沉浸式模拟属于RPG优先赛道，多源覆盖。；本周窗口日报/周末报事件合并一次 |
| I005 | include | industry_news | 事件3×相关3+钩子1 = 10；国内平台与电竞集团的明确战略合作，覆盖直播、赛事、主播与商业化链路。；本周窗口日报/周末报事件合并一次 |
| I006 | include | industry_news | 事件3×相关3+钩子1 = 10；腾讯主体、移动PVP新品节点明确，产品与主应用并行且保留账号资产。；本周窗口日报/周末报事件合并一次 |
| I007 | include | industry_news | 事件3×相关3+钩子1 = 10；腾讯投资团队的PVP新品首曝并给出首轮验证日期，命中国内主体与竞技赛道。；本周窗口日报/周末报事件合并一次 |
| I008 | include | industry_news | 事件3×相关3+钩子1 = 10；国产女性向新品与核心人才创业信号，来源对项目归属使用推测措辞，正文保留归因。；本周窗口日报/周末报事件合并一次 |
| I009 | include | industry_news | 事件3×相关3+钩子1 = 10；移动端PVP新品已在菲律宾产生测试下载，产品状态明确。；本周窗口日报/周末报事件合并一次 |
| I010 | include | industry_news | 事件3×相关3+钩子1 = 10；国内手游厂商拓展PC独游投资与发行试验，新作有明确上线表现。；本周窗口日报/周末报事件合并一次 |
| I011 | include | industry_news | 事件3×相关3+钩子1 = 10；财报例外：归母净利润由上年同期2590万元转为-479万元，为2019年挂牌以来半年报首次亏损；来源将原因指向主力产品衰退和新品断档，非一次性会计因素。；本周窗口日报/周末报事件合并一次 |
| I012 | include | industry_news | 事件3×相关3+钩子1 = 10；国产独立团队首次公开新项目，产品进入公开验证阶段。；本周窗口日报/周末报事件合并一次 |
| I013 | include | industry_news | 事件3×相关3+钩子1 = 10；国内游戏公司进入破产清算，属于资本与组织状态变化。；本周窗口日报/周末报事件合并一次 |
| I014 | include | industry_news | 事件3×相关3+钩子0 = 9；国内上市游戏公司股东资本动作；事件发生于8月13日但未进入此前报告，本期来源首次召回。；本周窗口日报/周末报事件合并一次 |
| I015 | include | industry_news | 事件2×相关3+钩子2 = 8；Roblox为最高关注主体，联邦调查构成平台治理与合规的实质新阶段。；本周窗口日报/周末报事件合并一次 |
| I016 | include | industry_news | 事件3×相关2+钩子2 = 8；IP公司完成组织整合并建立中美约300人自研团队，对移动IP产品全球化有明确迁移点。；本周窗口日报/周末报事件合并一次 |
| I017 | include | industry_news | 事件2×相关3+钩子2 = 8；产品数据是财报中的独立生命周期里程碑，不按常规财报条目处理；多源同日覆盖。；本周窗口日报/周末报事件合并一次 |
| I018 | include | industry_news | 事件2×相关3+钩子2 = 8；移动分发平台政策直接改变支付和替代商店成本；两源覆盖。；本周窗口日报/周末报事件合并一次 |
| I019 | include | industry_news | 事件2×相关3+钩子2 = 8；国内小游戏平台政策调整，直接作用买量回流与长线经营；多源覆盖。；本周窗口日报/周末报事件合并一次 |
| I020 | include | industry_news | 事件3×相关3+钩子2 = 11；E3×R3+M2=11，达到周报阈值 |
| I021 | include | industry_news | 事件3×相关3+钩子1 = 10；E3×R3+M1=10，达到周报阈值 |
| I022 | include | industry_news | 事件3×相关2+钩子2 = 8；E3×R2+M2=8，达到周报阈值 |
| X001 | exclude | industry_news | 事件3×相关3+钩子1 = 10；日报已完成卡片曝光，本期未出现新的财务周期或产品状态。 |
| X002 | exclude | industry_news | 事件2×相关3+钩子1 = 7；同一停业清盘事件已在日报卡片曝光，本期只有转载与背景补充。 |
| X003 | exclude | industry_news | 事件3×相关3+钩子1 = 10；周末报与周报均已卡片曝光，本期社区帖子没有新的任职状态。 |
| X004 | exclude | industry_news | 事件3×相关3+钩子1 = 10；交易比例、价格与退出棋牌发行的信息已在日报及周报卡片曝光。 |
| X005 | exclude | industry_news | 事件3×相关3+钩子1 = 10；同一软启动事件已在双周历史卡片曝光，本期未提供新的实际上线结果。 |
| X006 | exclude | industry_news | 事件3×相关3+钩子2 = 11；项目首曝与核心产品形态已在历史卡片曝光，本期是访谈和周年背景，无新状态。 |
| X007 | exclude | industry_news | 事件2×相关2+钩子2 = 6；E2×R2+M2=6，周报边界候选，未达8分线 |
| X008 | exclude | industry_news | 事件3×相关1+钩子2 = 5；E3×R1+M2=5，周报边界候选，未达8分线 |
| X009 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X010 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X011 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X012 | exclude | industry_news | 事件2×相关2+钩子2 = 6；E2×R2+M2=6，周报边界候选，未达8分线 |
| X013 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X014 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X015 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X016 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X017 | exclude | industry_news | 事件3×相关1+钩子2 = 5；E3×R1+M2=5，周报边界候选，未达8分线 |
| X018 | exclude | industry_news | 事件2×相关3+钩子0 = 6；E2×R3+M0=6，周报边界候选，未达8分线 |
| X019 | exclude | industry_news | 事件3×相关1+钩子2 = 5；E3×R1+M2=5，周报边界候选，未达8分线 |
| X020 | exclude | industry_news | 事件2×相关2+钩子2 = 6；E2×R2+M2=6，周报边界候选，未达8分线 |
| X021 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X022 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，周报边界候选，未达8分线 |
| X023 | exclude | industry_news | 事件2×相关2+钩子2 = 6；市场数据多源但对国内移动与优先赛道迁移有限，周报未达8分线 |
| X024 | exclude | industry_news | 事件2×相关3+钩子1 = 7；平台范围变化由单一全文支持，未达周报8分线 |
| X025 | exclude | industry_news | 事件2×相关3+钩子1 = 7；产品档期变化成立但单源，未达周报8分线 |
| X026 | exclude | industry_news | 事件2×相关3+钩子1 = 7；两条记录正文同源，不能抬高多源钩子，未达周报8分线 |
| X027 | exclude | industry_news | 事件2×相关3+钩子1 = 7；唯一来源为短摘录，不作为周报正文证据 |
| X028 | exclude | industry_news | 事件1×相关2+钩子1 = 3；纯海外裁员统计按E1处理，未达周报阈值 |
| X029 | exclude | industry_news | 事件0×相关3+钩子0 = 0；常规财报未出现相对预期的异常，按财报例外排除 |
| X030 | exclude | industry_news | 事件0×相关1+钩子0 = 0；老品资料片与合集属于产品日历排除范围 |
| A001 | include | ai_trends | 直接作用于PVP教学与激活，并披露准确率、知识库和业务结果。 |
| A002 | include | ai_trends | AI已直接覆盖游戏美术、代码、适配、测试和发行决策。 |
| A003 | include | ai_trends | AI已直接作用研发生产，并开始改变人才评价和组织制度。 |
| A004 | include | ai_trends | 直接作用于角色对话、记忆、情绪与TTS，且有百万字训练标注和公开试玩反馈。 |
| A005 | include | ai_trends | 直接作用于关卡、资产、数据、QA和营销，并披露10周缩至3周、外包预算下降60%等结果。 |
| A006 | include | ai_trends | 模型已用于平台PII识别、儿童风险预警和实时语音治理，属于运营直接应用。 |
| A-BATCH-EXCLUDE | exclude | ai_trends | 未形成游戏直接作用或可由来源支撑的具体迁移链条；已逐条反扫 |
| C001 | include | community_discourse | 同一主题从8月13日持续到8月18日，触发点、玩家分歧和移动端反馈均可核验。 |
| C002 | include | community_discourse | 两帖围绕同一角色、同一1.3剧情争议及后续调整公告形成完整时间线。 |
| C003 | include | community_discourse | 8月19日新建帖形成明确消费事件，包含材质主张、玩家分歧和售后方案讨论。 |
| C-BATCH-EXCLUDE | exclude | community_discourse | 普通闲聊、重复帖、证据不足或优先级低于本期三条完整事件；已补扫官方回应与后续 |
| D001 | include | deep_analysis | 用户在目标ID selection中明确选择进入周报 |
| D002 | include | deep_analysis | 用户在目标ID selection中明确选择进入周报 |
| D003 | include | deep_analysis | 用户在目标ID selection中明确选择进入周报 |
| I-BATCH-E0 | exclude | industry_news | 事件0×相关0+钩子0 = 0；已按完整index与全量text反扫；不构成独立行业事件或E=0，允许批量审计 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-004 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-006 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-095 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-007 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-008 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-009 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-010 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-011 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-012 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-013 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-014 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-015 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-016 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-017 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-018 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-019 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-020 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-023 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-024 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-025 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-026 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-027 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-034 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-036 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-039 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-040 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-041 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-043 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-046 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-047 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-048 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-049 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-050 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-051 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-052 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-053 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-054 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-055 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-056 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-057 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-058 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-059 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-060 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-061 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-062 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-063 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-064 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-065 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-066 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-067 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-068 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-069 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-070 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-071 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-072 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-073 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-074 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-075 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-076 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-077 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-078 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-079 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-080 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-081 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-082 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-083 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-084 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-085 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-086 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-087 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-088 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-089 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-090 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-091 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-092 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-093 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-094 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-096 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-097 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-098 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-099 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-100 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-101 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-102 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-103 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-104 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-105 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-106 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-107 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-108 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-109 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-110 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-111 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-112 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-113 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-114 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-115 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-116 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-117 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-118 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-119 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-120 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-121 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-122 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-123 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-124 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-125 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-126 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-127 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-128 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-129 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-130 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-131 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-132 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-133 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-134 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-135 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-136 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-137 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-138 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-139 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-140 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-141 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-142 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-143 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-144 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-145 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-146 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-147 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-148 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-149 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-150 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-151 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-152 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-153 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-154 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-155 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-156 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-157 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-158 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-159 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-160 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-161 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-162 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-163 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-164 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-165 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-166 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-167 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-168 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-169 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-170 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-171 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-172 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-173 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-174 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-175 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-176 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-177 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-178 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-179 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-180 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-181 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-182 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-183 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-184 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-185 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-186 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-187 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-188 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-189 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-190 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-191 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-192 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-193 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-194 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-195 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-196 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-197 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-198 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-199 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-200 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-201 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-202 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-203 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-204 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-205 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-206 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-207 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-208 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-209 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-210 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-211 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-212 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-213 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-214 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-215 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-216 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-217 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-218 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-219 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-220 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-221 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-222 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-223 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-224 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-225 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-226 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-227 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-228 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-229 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-230 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-231 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-232 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-233 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-234 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-235 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-236 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-237 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-238 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-239 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-240 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-241 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-242 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-243 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-244 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-245 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-246 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-247 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-248 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-249 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-250 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-251 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-252 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-253 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-254 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-255 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-256 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-257 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-258 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-259 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-260 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-261 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-262 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-263 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-264 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-265 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-266 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-267 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-268 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-269 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-270 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-271 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-272 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-273 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-274 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-275 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-276 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-277 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-278 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-279 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-280 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-281 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-282 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-283 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-284 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-285 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-286 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-287 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-288 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-289 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-290 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-291 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-292 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-293 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-294 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-295 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-296 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-297 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-298 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-299 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-300 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-301 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-302 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-303 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-304 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-305 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-306 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-307 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-308 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-309 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-310 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-311 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-312 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-313 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-314 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-315 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-316 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-317 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-318 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-319 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-320 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-321 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-322 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-323 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-324 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-325 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-326 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-327 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-328 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-329 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-330 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-331 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-332 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-333 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-334 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-335 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-336 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-337 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-338 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-339 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-340 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-341 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-342 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-343 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-344 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-345 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-346 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-347 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-348 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-349 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-350 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-351 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-352 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-353 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-354 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-355 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-356 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-357 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-358 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-359 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-360 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-361 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-362 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-363 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-364 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-365 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-366 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-367 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-368 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-369 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-370 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-371 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-372 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-373 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-374 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-375 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-376 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-377 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-378 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-379 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-380 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-381 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-382 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-383 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-384 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-385 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-386 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-387 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-388 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-389 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-390 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-391 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-392 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-393 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-394 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-395 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-396 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-397 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-398 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-399 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-400 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-401 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-402 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-403 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-404 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-405 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-406 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-407 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-408 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-409 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-410 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-411 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-412 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-413 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-414 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-415 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-416 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-417 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-418 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-419 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-420 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-421 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-422 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-423 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-424 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-425 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-426 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-427 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-428 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-429 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-430 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-431 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-432 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-433 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-434 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-435 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-436 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-437 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-438 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-439 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-440 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-441 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-442 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-443 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-444 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-445 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-446 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-447 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-448 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-449 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-450 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-451 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-452 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-453 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-454 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-455 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-456 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-457 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-458 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-459 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-460 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-461 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-462 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-463 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-464 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-465 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-466 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-467 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-468 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-469 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-470 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-471 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-472 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-473 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-474 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-475 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-476 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-477 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-478 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-479 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-480 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-481 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-482 | exclude | release_calendar | 单源不具备正文资格 |
