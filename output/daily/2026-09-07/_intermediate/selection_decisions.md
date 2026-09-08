# Selection Decisions

卡片曝光去重：匹配《黎明行者之血》历史卡片已曝光，本期仅以百万销量新事实作为 material_update；App Store 管理交接历史已曝光，本期新增提高利润率与经常性收入方向；《2XKO》历史匹配项 card_exposed=false、card_rank=-/10，本期以总分7获得唯一 card_carryover；其余已曝光旧事件按 repeat_only 排除。

维度覆盖自检：国内移动/国产产品与人才 24 张；市场数据 9 张；并购 6 张；平台政策 8 张；档期变动 15 张；资本组织 10 张；海外重大 27 张。已以完整 index 与全量 JSONL 反扫，无信号因预判低分而静默丢弃。

产品日历漏挂反查：已反扫 industry_news 与 release_calendar 全量输入，20 个节点全部进入 release_calendar_audit.json；没有节点同时满足多源、事件窗口与可核验日期，故正文 0 条。

行业新闻 E×R+M 打分：每条候选按‘事件E×相关R+钩子M = 终分’记录；日报总分 ≥7 才入选，正文按总分降序，同分优先国内与高 R。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子1 = 10；国产前大厂人才创业与新项目进展，达到日报门槛。 |
| I002 | include | industry_news | 事件3×相关3+钩子1 = 10；同文转载只计一个独立信号，合作本身仍是国内手游安全能力落地。 |
| I003 | include | industry_news | 事件3×相关3+钩子1 = 10；国产手游新品上线表现与海外先行商业化数据。 |
| I004 | include | industry_news | 事件2×相关3+钩子2 = 8；国内市场规模和小游戏结构数据获得多源覆盖。 |
| I005 | include | industry_news | 事件3×相关2+钩子2 = 8；游戏产业资本参投生成式3D工具公司，具备研发管线迁移点。 |
| I006 | include | industry_news | 事件3×相关2+钩子2 = 8；移动游戏团队收购案有两家独立媒体覆盖。 |
| I007 | include | industry_news | 事件2×相关3+钩子1 = 7；相对周末报的发售首日表现新增百万销量里程碑。 |
| I008 | include | industry_news | 事件2×相关3+钩子1 = 7；覆盖技术、原创研发、运营、出海和电竞等国内产业链环节。 |
| I009 | include | industry_news | 事件2×相关3+钩子1 = 7；相对管理交接新增明确商业化方向，影响移动开发者渠道成本。 |
| I010 | include | industry_news | 事件2×相关3+钩子1 = 7；历史同事件未进入订阅卡片，本期再次召回且达到门槛，使用唯一补位。 |
| A001 | include | ai_trends |国内UGC平台披露直接研发应用、产能和商业结果。 |
| A002 | include | ai_trends |AI直接作用于游戏UGC和发行传播环节。 |
| A003 | include | ai_trends |三款产品提供玩家、销量、活跃与成本机制证据。 |
| D001 | include | deep_analysis | R2/I3/E3/C3=11；单篇完整数据分析具备变化、机制和下游影响链。 |
| B001 | exclude | industry_news | 事件2×相关2+钩子1 = 5；总分5，未达日报门槛；转入深度观察解释结构。 |
| B002 | exclude | industry_news | 事件2×相关2+钩子2 = 6；总分6，海外服务型项目调整对当前业务迁移有限。 |
| B003 | exclude | industry_news | 事件1×相关2+钩子2 = 4；总分4，展会安保处置不构成高相关行业结构事件。 |
| B004 | exclude | industry_news | 事件2×相关2+钩子1 = 5；总分5，品类迁移点存在但海外小型发行事件权重不足。 |
| B005 | exclude | industry_news | 事件2×相关1+钩子2 = 4；总分4，海外单机销量点与当前业务迁移较弱。 |
| X0002 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0004 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0005 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0006 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0007 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0008 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0013 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0015 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0016 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0017 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0019 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0020 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0021 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0022 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0023 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0024 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0025 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0026 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0028 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0030 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0034 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0037 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0038 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0039 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0040 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0042 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0043 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0044 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0045 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0046 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0048 | exclude | industry_news | 事件0×相关3+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0052 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0054 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0056 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0057 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0058 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0059 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0060 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0061 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0062 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0063 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0064 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0065 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0066 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0067 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0068 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0069 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0070 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0071 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0072 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0073 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0074 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0075 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0076 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0077 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0078 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0079 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0080 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0081 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0082 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0083 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0084 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0085 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0086 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0087 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0088 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0089 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0091 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0092 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0093 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0094 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0095 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0096 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0097 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0098 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0100 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0101 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0102 | exclude | industry_news | 事件0×相关3+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0103 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0104 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0106 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0107 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0108 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0110 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0111 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0112 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0113 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0114 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0115 | exclude | industry_news | 事件0×相关1+钩子0 = 0；完整扫描后排除：例行宣传、传言、纯榜单、弱迁移观点或非独立事件。 |
| X0116 | exclude | ai_trends |泛AI动态缺少足够具体的游戏落地或可核验迁移链。 |
| X0117 | exclude | ai_trends |泛AI动态缺少足够具体的游戏落地或可核验迁移链。 |
| C0132 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0133 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0134 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0135 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0136 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0137 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0138 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0139 | include | community_discourse |触发点、争议逻辑与窗口内时间线完整。 |
| C0140 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0141 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0142 | include | community_discourse |触发点、争议逻辑与窗口内时间线完整。 |
| C0143 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0144 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| C0145 | exclude | community_discourse |旧闻延续、事实归属不清、单一帖子缺少可命名事件或与已发周末报重复。 |
| X0146 | exclude | deep_analysis | R1/I1/E1/C2=5；付费墙仅提供节目导语，证据不足以展开结构分析。 |
| release-candidate-001 | exclude | release_calendar | event3×source2+company3=9；单源不具备正文资格 |
| release-candidate-002 | exclude | release_calendar | event3×source2+company3=9；单源不具备正文资格 |
| release-candidate-003 | exclude | release_calendar | event3×source2+company3=9；事件日期不在报告窗口 |
| release-candidate-004 | exclude | release_calendar | event3×source2+company3=9；单源不具备正文资格 |
| release-candidate-005 | exclude | release_calendar | event3×source2+company2=8；事件日期不在报告窗口 |
| release-candidate-006 | exclude | release_calendar | event3×source2+company0=6；单源不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | event3×source2+company0=6；单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | event3×source2+company0=6；单源不具备正文资格 |
| release-candidate-009 | exclude | release_calendar | event3×source2+company0=6；单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | event2×source2+company0=4；单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | event2×source2+company0=4；单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | event3×source1+company0=3；单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | event3×source1+company0=3；单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | event3×source1+company0=3；单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | event3×source1+company0=3；单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | event1×source2+company0=2；单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | event1×source2+company0=2；事件日期不在报告窗口 |
| release-candidate-018 | exclude | release_calendar | event1×source2+company0=2；事件日期不在报告窗口 |
| release-candidate-019 | exclude | release_calendar | event1×source2+company0=2；事件日期不在报告窗口 |
| release-candidate-020 | exclude | release_calendar | event1×source2+company0=2；事件日期不在报告窗口 |
