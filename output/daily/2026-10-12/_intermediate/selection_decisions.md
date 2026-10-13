# Selection Decisions

- 卡片曝光去重：历史匹配逐条读取 card_exposed/card_rank/card_limit/card_exposure_source；《极限战场》(rank 7、1) / Exit Games(rank 5) / Minecraft Blast(rank 6) / mo.co(rank 1、3) / 三角洲行动(rank 4) 均已有 card_exposed=true，按 repeat_only 排除；RED LAND历史rank 2、10且已曝光，但本期新增20万人、82%与25亿结果，按 material_update 入选；本期无符合条件的 card_carryover。
- 双周历史窗口：2026-09-28_to_2026-10-11；repeat_only=5；material_update=1；card_carryover=0。
- 维度覆盖自检：国内移动/国产产品与人才 18 张候选；市场数据 6 张；并购/投融资 4 张；平台政策 3 张；档期变动 12 张；资本组织 6 张；海外重大 14 张。产品日历另以完整反扫审计为准。
- 产品日历漏挂反查：已覆盖原始release_calendar、英文软启动汇总、SLG测试汇总、GameRes开测汇总与Steam当日/次日清单；所有真实可发布节点均未满足两个独立来源，唯一自动多源节点为文章背景误召回，已人工复核排除。
- 行业新闻 E×R+M 打分：全部非E0独立事件逐条记录事件E、相关R、钩子M与总分；日报仅总分≥7且通过历史门禁者include。
- AI反扫：全部行业候选均检查直接应用与迁移价值；直接应用优先，行业与AI不重复入选。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子1 = 10；国内上市游戏公司法定代表人与主要股东持股结构发生明确变化。 |
| I002 | include | industry_news | 事件3×相关3+钩子1 = 10；国内重点厂商在研跨端策略产品出现公开招募与玩法信息。 |
| I003 | exclude | - | 事件1×相关3+钩子1 = 4；AppMagic仅显示未来软启动预备状态，尚未证明正式测试或完成官方首曝，总分4。 |
| I004 | include | industry_news | 事件3×相关3+钩子1 = 10；Garena重点主体的移动新游出现明确测试范围扩张。 |
| I005 | include | industry_news | 事件2×相关3+钩子2 = 8；国内代理射击产品进入明确停运节点，且有两个独立来源。 |
| I006 | include | industry_news | 事件2×相关3+钩子1 = 7；移动策略赛道出现可核验的大盘与新品结构变化。 |
| I007 | include | industry_news | 事件2×相关3+钩子1 = 7；相较历史扩容信息，本期新增实际到场人数、跨城参与占比与曝光结果。 |
| I008 | include | industry_news | 事件3×相关2+钩子1 = 7；游戏工作室获得重大融资并披露累计融资与估值。 |
| I101 | exclude | - | 事件3×相关3+钩子1 = 10；同一首曝与测试定档已在周末报订阅卡片展示，本期为晚到复述。 |
| I102 | exclude | - | 事件3×相关2+钩子0 = 6；同一5500万美元股权回购已在历史订阅卡片展示。 |
| I103 | exclude | - | 事件3×相关2+钩子0 = 6；同一重新软启动事件已在历史订阅卡片展示。 |
| I104 | exclude | - | 事件3×相关3+钩子0 = 9；同一回到beta的状态已在历史订阅卡片展示。 |
| I105 | exclude | - | 事件2×相关3+钩子0 = 6；同一数据已在周末报完成卡片曝光。 |
| I201 | exclude | - | 事件2×相关2+钩子2 = 6；移动产品停运且多源，但对国内/优先赛道迁移点有限，总分6。 |
| I202 | exclude | - | 事件2×相关2+钩子1 = 5；老品跨平台节点有移动迁移价值，但单源且总分5。 |
| I203 | exclude | - | 事件2×相关2+钩子1 = 5；平台供给规模数据有结构信号，但对移动与国内业务迁移点有限，总分5。 |
| I204 | exclude | - | 事件2×相关2+钩子1 = 5；全球长线产品数据重要，但本期核心是周年复盘且迁移点有限，总分5。 |
| I205 | exclude | - | 事件2×相关3+钩子0 = 6；9月17日版本后的数据为晚到复盘，缺少本期新状态，总分6。 |
| A001 | include | ai_trends | AI已直接作用于游戏生成、UGC分发和创作者变现，并披露规模数据。 |
| A002 | exclude | - | 直接应用成立，但同一综合来源优先保留业务相关性更高的Garena测试扩张，避免跨分区复用。 |
| A003 | include | ai_trends | 实践教程明确展示AI在资产生成、引擎编排与玩法迭代中的直接应用。 |
| A101 | exclude | - | 同一事件已进入上一份周末报AI栏，本期不重复。 |
| A102 | exclude | - | 核心发布已在上一周报深度观察中呈现，本期为延伸体验稿。 |
| A103 | exclude | - | 直接应用价值高，但正文仅为403后的摘要片段，证据不足以支撑完整条目。 |
| A104 | exclude | - | 只有100字二手摘要，缺少机制正文，证据不足。 |
| A105 | exclude | - | 模型评测完整，但未直接落到游戏环节，迁移链弱于本期三条直接应用。 |
| C001 | include | community_discourse | 触发、争议逻辑与跨日时间线完整，且是本窗口持续讨论的具体运营事件。 |
| C002 | include | community_discourse | 本期新建帖子，渠道变化、对立观点与延续时间线清楚。 |
| D001 | include | deep_analysis | R3/I3/E3/C3=12；R3/I3/E3/C3=12；单篇完整市场分析提供规模、区域、指标分解、替代品与供给响应证据链。 |
| D002 | exclude | - | R2/I0/E0/C1=3；付费墙仅提供节目导语，缺少问题、机制和证据正文，不通过深度来源门禁。 |
| C0135 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0136 | exclude | - | 旧帖在本窗口仅有延续回复，没有可验证的新进展，不作为新事件。 |
| C0138 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0139 | exclude | - | 本窗口新帖但核心材料依赖缺失图片与推测，无法确认涉事主体和具体处置。 |
| C0140 | exclude | - | 旧帖在本窗口仅有延续回复，没有可验证的新进展，不作为新事件。 |
| C0141 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0142 | exclude | - | 旧帖在本窗口仅有延续回复，没有可验证的新进展，不作为新事件。 |
| C0143 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0144 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0145 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0146 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| C0148 | exclude | - | 未形成可命名且有新进展的社区事件，或只有旧帖延续、新闻转述、联动/停运信息。 |
| X0001 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0002 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0003 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0004 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0005 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0006 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0007 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0008 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0010 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0011 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0012 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0014 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0019 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0020 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0023 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0026 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0027 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0032 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0033 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0034 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0035 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0036 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0037 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0039 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0040 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0047 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0048 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0049 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0050 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0051 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0052 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0053 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0054 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0055 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0056 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0057 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0058 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0059 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0060 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0061 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0062 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0063 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0064 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0065 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0066 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0067 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0068 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0069 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0070 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0071 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0072 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0073 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0074 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0075 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0076 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0077 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0078 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0079 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0080 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0081 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0082 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0083 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0084 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0085 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0086 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0087 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0088 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0089 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0090 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0091 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0092 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0093 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0094 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0095 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0096 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0097 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0098 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0099 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0100 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0101 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0102 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0104 | exclude | - | 事件0×相关0+钩子0 = 0；全量反扫排除：例行宣传、版本/联动/评测、非游戏内容、泛观点，或缺少可核验的新状态变化。 |
| X0106 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0107 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0108 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0109 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0110 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0111 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0112 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0113 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0115 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0116 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| X0117 | exclude | - | 全量AI反扫排除：未直接作用于游戏，且缺少可由来源支撑的具体游戏迁移链。 |
| release-candidate-002 | exclude | - | priority=9；事件日期不在报告窗口 |
| release-candidate-003 | exclude | - | priority=9；单源不具备正文资格 |
| release-candidate-004 | exclude | - | priority=9；单源不具备正文资格 |
| release-candidate-005 | exclude | - | priority=9；事件日期不在报告窗口 |
| release-candidate-006 | exclude | - | priority=9；事件日期不在报告窗口 |
| release-candidate-007 | exclude | - | priority=7；单源不具备正文资格 |
| release-candidate-008 | exclude | - | priority=6；事件日期不在报告窗口 |
| release-candidate-009 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-010 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-011 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-012 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-013 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-030 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-031 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-032 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-033 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-034 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-036 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-038 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-040 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-041 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-042 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-043 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-044 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-045 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-046 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-048 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-049 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-050 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-051 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-052 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-053 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-054 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-055 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-056 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-057 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-058 | exclude | - | priority=6；事件日期不在报告窗口 |
| release-candidate-059 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-060 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-061 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-062 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-063 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-064 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-065 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-066 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-067 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-068 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-069 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-070 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-071 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-072 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-073 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-074 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-075 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-076 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-077 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-078 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-079 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-080 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-081 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-082 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-083 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-084 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-085 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-086 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-087 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-088 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-089 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-090 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-091 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-092 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-093 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-094 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-095 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-096 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-097 | exclude | - | priority=6；单源不具备正文资格 |
| release-candidate-098 | exclude | - | priority=6；事件日期不在报告窗口 |
| release-candidate-099 | exclude | - | priority=6；事件日期不在报告窗口 |
| release-candidate-100 | exclude | - | priority=6；事件日期不在报告窗口 |
| release-candidate-001 | exclude | - | priority=6；事件日期不在报告窗口 |
| release-candidate-014 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-015 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-016 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-017 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-018 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-019 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-020 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-035 | exclude | - | priority=4；事件日期不在报告窗口 |
| release-candidate-037 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-039 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-047 | exclude | - | priority=4；单源不具备正文资格 |
| release-candidate-021 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-022 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-023 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-024 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-025 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-026 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-027 | exclude | - | priority=3；单源不具备正文资格 |
| release-candidate-028 | exclude | - | priority=2；单源不具备正文资格 |
| release-candidate-029 | exclude | - | priority=2；单源不具备正文资格 |
