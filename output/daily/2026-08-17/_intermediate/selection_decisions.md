# Selection Decisions

- 卡片曝光去重：双周历史共106条；本期历史匹配项均读取 card_exposed/card_rank/card_limit/card_exposure_source。无合格 card_carryover；已曝光重复项排除，实质更新单列新事实。
- 维度覆盖自检：国内移动/国产产品与人才 14 张；市场数据 5 张；并购 4 张；平台政策 4 张；档期变动 4 张；资本组织 5 张；海外重大 8 张。
- AI反扫：已反扫全部行业候选；吉比特AI应用与Saber AI披露转入AI新闻，行业与AI无重复发布。
- 产品日历漏挂反查：已覆盖 industry_news 与 release_calendar 全量输入；所有上线、定档、测试、预下载、首曝、跨平台、回归与重大更新节点均已进入 release_calendar_audit.json 并显式决策；《雾海之下》别名节点已合并，跨分区只保留产品日历。
- 社区补扫：已按产品名、角色名、调整、公告、回应与补丁词补扫同窗口社区池。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子2=11；国内成熟游戏资产的重大股权交易从待确认推进到正式协议，并确认管理团队留任。 |
| I002 | include | industry_news | 事件3×相关3+钩子1=10；腾讯主体、移动PVP新品节点明确，产品与主应用并行且保留账号资产。 |
| I003 | include | industry_news | 事件3×相关3+钩子1=10；腾讯投资团队的PVP新品首曝并给出首轮验证日期，命中国内主体与竞技赛道。 |
| I004 | include | industry_news | 事件3×相关3+钩子1=10；国产女性向新品与核心人才创业信号，来源对项目归属使用推测措辞，正文保留归因。 |
| I005 | include | industry_news | 事件3×相关3+钩子1=10；移动端PVP新品已在菲律宾产生测试下载，产品状态明确。 |
| I006 | include | industry_news | 事件2×相关3+钩子1=7；中国市场与手游增长结构直接命中最高优先级市场数据。 |
| I007 | include | industry_news | 事件2×相关3+钩子1=7；移动爆款以差异化版本进入订阅分发，构成渠道与商业模式变化。 |
| I008 | include | industry_news | 事件2×相关3+钩子1=7；生活模拟优先赛道出现可核验的全球销量与装机转化数据。 |
| I009 | include | industry_news | 事件2×相关3+钩子1=7；国产产品披露新的销量与愿望单里程碑，达到日报分数线。 |
| I010 | include | industry_news | 事件3×相关2+钩子1=7；内容平台向游戏研发资产延伸，资本动作对IP与游戏融合有明确迁移点。 |
| I101 | merge into release-candidate-001 | - | 事件3×相关3+钩子2=11；达到E3×R3+M2=11，但同一测试事件进入产品日历，跨分区只保留一次。 |
| I102 | exclude | - | 事件2×相关3+钩子1=7；同一调查、文件提交期限和安全指控已在上期周末报卡片曝光，本期无实质新状态。 |
| I103 | exclude | - | 事件3×相关2+钩子1=7；同一组织成立、近300人规模与杭州团队信息已在上期周末报卡片曝光。 |
| I104 | exclude | - | 事件3×相关3+钩子1=10；交易比例、价格与退出棋牌发行的信息已在日报及周报卡片曝光。 |
| I105 | exclude | - | 事件3×相关3+钩子2=11；150人团队、腾讯投资与试玩阶段均已在上期周末报卡片曝光，后续访谈未改变项目状态。 |
| I106 | exclude | - | 事件2×相关3+钩子1=7；相对历史两周数据形成实质更新并达7分，但输入仅为被拦截页面的短摘录，不作为终稿证据。 |
| I107 | exclude | - | 事件2×相关3+钩子1=7；E2×R3+M1=7，但仅有被拦截页面的短摘录，终稿不使用非完整正文。 |
| I108 | exclude | - | 事件2×相关3+钩子1=7；相对历史菲律宾软启动有可验证更新并达7分，但唯一来源与更高分的《Overwatch Rush》条目完全相同，受来源集合完整性门禁排除。 |
| I109 | exclude | - | 事件2×相关3+钩子1=7；E2×R3+M1=7，但唯一来源与更高分条目完全相同，且测试尚未在本期窗口实际开始。 |
| I110 | exclude | - | 事件2×相关2+钩子1=5；E2×R2+M1=5，开发融资匹配有迁移价值但未达日报7分线。 |
| I111 | exclude | - | 事件3×相关1+钩子1=4；E3×R1+M1=4，对国内、移动和优先赛道迁移较弱。 |
| I112 | exclude | - | 事件0×相关3+钩子2=2；同比增长和分红属于常规财报，缺少一致预期或指引异常基准；其中AI应用事实转入AI新闻。 |
| I113 | exclude | - | 事件0×相关3+钩子1=1；例行品牌活动与宣传复盘，E=0。 |
| I114 | exclude | - | 事件3×相关3+钩子1=10；同一软启动事件已在双周历史卡片曝光，本期未提供新的实际上线结果。 |
| I115 | exclude | - | 事件2×相关3+钩子1=7；定档事件发生在8月7日，早于本期窗口；本期访谈没有新的档期或上线状态。 |
| I116 | merge into I002 | - | 事件3×相关3+钩子1=10；同主体、同产品、同日同事件的短摘录，合并到完整正文来源。 |
| A001 | include | ai_news | AI已直接作用研发生产，并开始改变人才评价和组织制度。 |
| A002 | include | ai_news | 数据直接覆盖开发、发行、定价、评分和收入，能够评估AI在游戏供给侧的实际作用。 |
| A003 | include | ai_news | AI已进入具体游戏内容，披露清楚区分主线人工创作与可选生成内容。 |
| A101 | exclude | - | 没有具体游戏研发、产品、发行或运营落地。 |
| A102 | exclude | - | 可用于研发成本追踪，但来源没有游戏工作流实例。 |
| A103 | exclude | - | 安全框架和能源合作未形成具体游戏迁移链。 |
| A104 | exclude | - | 具备直接应用，但材料以赛事宣传为主，信息密度低于三条入选项。 |
| A105 | exclude | - | 输入为短摘录，无法核验完整案例和边界。 |
| C001 | include | community_discourse | 触发、玩家争议逻辑与窗口内调整转帖形成完整时间线。 |
| C002 | include | community_discourse | 角色调整细节清楚，社区同时呈现支持平衡与反对一刀切的意见。 |
| C101 | exclude | - | 主张主要来自玩家图像对比，缺少权利方回应或窗口内事实进展。 |
| C102 | exclude | - | 只有社区截图与玩家推测，触发原因和平台处理口径无法核验。 |
| C103 | exclude | - | 讨论以玩家体验和同类产品类比为主，缺少官方机制说明。 |
| C104 | exclude | - | 单一社区帖不足以确认事件范围和官方处理，不写成已证实事实。 |
| D001 | include | deep_analysis | Naavik文章提供完整的预订、活跃、变现、分发与安全机制链。 |
| D002 | exclude | - | 付费文章当前可读部分主要是工作室履历与作者推断，国内和移动迁移较弱。 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-003 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-004 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | - | 单源不具备正文资格 |
| release-candidate-006 | exclude | - | 单源不具备正文资格 |
| release-candidate-007 | exclude | - | 单源不具备正文资格 |
| release-candidate-008 | exclude | - | 单源不具备正文资格 |
| release-candidate-009 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-010 | exclude | - | 单源不具备正文资格 |
| release-candidate-011 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-012 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-013 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-014 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-015 | exclude | - | 单源不具备正文资格 |
| release-candidate-016 | exclude | - | 单源不具备正文资格 |
| release-candidate-017 | exclude | - | 单源不具备正文资格 |
| release-candidate-018 | exclude | - | 单源不具备正文资格 |
| release-candidate-019 | exclude | - | 单源不具备正文资格 |
| release-candidate-021 | exclude | - | 单源不具备正文资格 |
| release-candidate-022 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-023 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-024 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-025 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-026 | exclude | - | 事件日期不在报告窗口 |
