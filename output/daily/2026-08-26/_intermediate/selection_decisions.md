# Selection Decisions

- 卡片曝光去重：历史匹配项均核对 card_exposed/card_rank/card_limit/card_exposure_source；本期选择《Gangstar Mirage City》为唯一 card_carryover（此前 card_exposed=false，rank=-/10），其余已曝光重复项排除，未曝光候选按分数与来源质量竞争。
- 维度覆盖自检：国内移动/国产产品与人才 8张候选 / 市场数据 5张候选 / 并购 3张候选 / 平台政策 4张候选 / 档期变动 6张候选 / 资本组织 4张候选 / 海外重大 7张候选
- 产品日历反扫：industry_news 与 release_calendar 全量输入均进入 schema 5 审计，别名与事件类型修复后由 sync_release_decisions.py 决定前缀。
- 产品日历漏挂反查：上线、定档、测试、预下载、首次首曝与老品重大节点均已逐个进入 release_calendar_audit.json 并显式 include/exclude。
- 行业新闻 E×R+M 打分记录：每条候选均逐条记录，例如事件3×相关3+钩子2 = 11；日报终分≥7才include，并按终分降序。
- AI反扫：全部行业候选已按直接作用类、迁移价值类复核；同一事件不跨行业与AI重复。
- 社区四要素：入选两项均完成触发、争议逻辑、时间线与后续扫描；不写免责尾注。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发 | include | industry_news | 新品正式公开、国内团队主导且同日多源覆盖，E3×R3+M2=11。 |
| I002 Paradox正式公布《Afterworld》，把科技树改为探索发现 | include | industry_news | 从未确认泄露推进为官方公布，策略赛道且新增玩法机制，E3×R3+M1=10。 |
| I003 上海英澈网络进入破产清算，《千年之旅ELF》移交运营权限 | include | industry_news | 国内游戏公司进入破产清算并影响在运产品，E3×R3+M1=10。 |
| I004 腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜 | include | industry_news | 历史完整周报已收录但未进入订阅卡片；本期再次召回且达到E3×R3+M1=10，为本期唯一card_carryover。 |
| I005 国产单机《只狗：路边一条》首曝，九人团队计划年底测试 | include | industry_news | 国产新品首曝与团队扩张信号明确，E3×R3+M1=10。 |
| I006 中手游停止大体量自研立项，转向轻量化双端产品 | include | industry_news | 国内主体出现明确的研发投入和产品结构迁移，多源覆盖，E2×R3+M2=8。 |
| I007 Roblox限制面向儿童的奖励驱动媒体流，不影响主动触发广告 | include | industry_news | 固定最高关注主体的平台政策变化且多源覆盖，E2×R3+M2=8。 |
| I008 《影之刃零》Steam愿望单突破200万，预购表现达《黑神话》同期73% | include | industry_news | 愿望单从历史160万推进至突破200万，属于可验证新增规模，E2×R3+M2=8。 |
| I009 53家以上中国厂商参加科隆展，包揽最佳移动游戏五项提名 | include | industry_news | 中国厂商全球展会覆盖与移动提名结构出现明确数据，E2×R3+M1=7。 |
| I010 《现代战争4》Beta峰值11.5万在线，Steam首轮好评率36.63% | include | industry_news | PVP竞技新品测试出现明确参与与口碑数据，E2×R3+M1=7。 |
| I011 Entity融资580万美元，拟推出免下载浏览器游戏平台 | include | industry_news | 平台型融资且存在跨设备分发迁移点，E3×R2+M1=7。 |
| I012 拳头与闪魂联合开发《符文战场》，首季进入美国TCG交易额前五 | include | industry_news | 固定最高关注主体进入实体竞技卡牌生态并披露经营数据，E2×R3+M1=7。 |
| I101 《渔力全开》两日销量破百万并冲至37万在线 | exclude | industry_news | 数据强但为海外一般主体，移动和优先赛道迁移不足，E2×R2+M2=6。 |
| I102 苹果扩展App Store创意素材与Apple Ads视频位 | exclude | industry_news | 移动分发相关但属于渐进式素材能力更新，E2×R2+M1=5。 |
| I103 《Hollywood Merge》7月收入810万美元并成为友塔月流水第一 | exclude | industry_news | 有新增数据但当前相关性不足，未达日报阈值，E2×R2+M1=5。 |
| I104 Nvidia在科隆公布光追Nanite、原生反作弊与DLSS 4.5 | exclude | industry_news | 海外PC技术更新迁移有限，E2×R2+M1=5。 |
| I105 拳头将在12月停止《2XKO》主动开发 | exclude | industry_news | 历史卡片已展示同一停更与退款事件，无新增状态，E3×R3+M1=10。 |
| I106 腾讯减持Netmarble的后续复述 | exclude | industry_news | 前一日报卡片已展示交易核心事实，本期无实质状态变化，E3×R3+M2=11。 |
| I107 《巫师4》2028年档期重复报道 | exclude | industry_news | 历史卡片已展示同一档期，无新增状态，E2×R3+M1=7。 |
| I108 《声探疑云》主创访谈的重复召回 | exclude | industry_news | 历史卡片已展示项目团队与开发阶段，本期长访谈没有新的状态节点，E3×R3+M1=10。 |
| I109 Supercell复盘《皇室战争》失败更新 | exclude | industry_news | 固定高关注主体但属于经验复盘而非新状态，E1×R3+M1=4。 |
| I110 Ubisoft推出Player Council测试反馈平台 | exclude | industry_news | 海外一般平台能力迁移有限，E2×R1+M2=4。 |
| I111 清华学生团队《21号空间站》获赛事人气奖 | exclude | industry_news | 人才信号明确但不是立项、首曝或融资节点，E1×R3+M1=4。 |
| I112 Roblox拟在利雅得设立中东北非总部 | exclude | industry_news | 固定高关注主体但唯一输入为短摘要，无法完成正文事实链，E3×R3+M1=10。 |
| I113 三七互娱上半年利润增长 | exclude | industry_news | 未给出相对一致预期或公司指引的异常，按财报例外门禁排除，E=0。 |
| I114 常规宣传、联动、奖项、硬件与版本更新批次 | exclude | industry_news | 普通宣传、活动、硬件或奖项，不进入正文。 |
| A001 腾讯披露Motus动画管线与GIGA跨游戏智能体架构 | include | ai_trends | 直接作用于动画生产与游戏内智能体。 |
| A002 腾讯混元端侧翻译模型压缩至440MB，落地直播弹幕实时翻译 | include | ai_trends | 可迁移到游戏直播、跨语种社区与运营沟通。 |
| A101 Ludo.ai新增关键帧动画与3D工具 | exclude | ai_trends | 直接作用类但正文仅为短摘要且全文抓取失败，不用于终稿。 |
| A102 Qwen3.8-Flash与GLM-5.3-Flash模型更新 | exclude | ai_trends | 缺少游戏直接应用或可验证的具体迁移链条。 |
| A103 OpenAI发布Hugging Face安全事件报告 | exclude | ai_trends | 与游戏研发、产品、发行或运营没有明确迁移路径。 |
| A104 《Humankind 2》团队回应AI宣传片质疑 | exclude | ai_trends | 事件核心是宣传片争议，不是AI直接应用或能力变化。 |
| C001 《鸣潮》周边规格两次对不上商品描述，玩家质疑售后与信息修改 | include | community_discourse | 同一周边履约事件在窗口内出现新的尺寸争议与售后回应。 |
| C002 《源初之结》首曝后被指与多款魂系游戏相似，玩家争论借鉴边界 | include | community_discourse | 当前窗口新帖形成明确争议机制，且与行业/日历仅共享首曝背景，不重复商业事实。 |
| C101 《未定事件簿》取消德芙联名 | exclude | community_discourse | 帖子图片和关键词被屏蔽，正文无法完整复原触发文案，不足以写清四要素。 |
| C102 《诡秘之主》PVP伤害与SAN值机制讨论 | exclude | community_discourse | 属于PVP数值与SAN值删号传闻两个独立事件，后者已在前一日报写入社区，不能合并或重复。 |
| C103 《晴空之下》旧关服帖重新活跃 | exclude | community_discourse | 原帖主体事件发生于1月，窗口内只有单条新增回复且无新进展。 |
| C104 《尘白禁区》活动空档与招聘传闻 | exclude | community_discourse | 上一日报已写同一活动空档与招聘线索，本期无新增可验证状态。 |
| C105 其余联动、账号、宣发与IP位置讨论 | exclude | community_discourse | 缺少完整事件四要素、后续扫描或独立事实链，未进入正文。 |
| D001 低价与随机性重排Steam命中结构：Roguelite上升背后是成功池扩容 | include | deep_analysis | 当前窗口高质量单篇数据分析形成完整变化—机制—影响链。 |
| release-candidate-005 无限大 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-001 源初之结 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-004 异克斯小队 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-006 七日世界（Once Human） | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-007 符文战场：英雄联盟对战卡牌 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-008 公路英雄 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-002 1666：阿姆斯特丹 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009 坦克狂途 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-010 1666：阿姆斯特丹 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-011 Nidhogg | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 共鸣：瘟疫传说传承 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013 Elta： Defy All Gods | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-014 巫师4 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 轨道双子星 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 背刺派对 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 ONTOS | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018 现代战争4 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-019 控制：共振 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 巫师3 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 三角洲行动 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-022 九阴真经：武侠 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023 小马岛2：熊猫马戏团 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-024 狂热运输3 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-025 Cosmo Tales | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-026 异形：火力小队2 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-027 使命召唤 现代战争 4 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 模拟火车世界7 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-029 The Wolf Among Us 复刻版 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-003 魔法门之英雄无敌III重制版 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-031 只狗：路边一条 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 控制：共振 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033 黎明门前的吹笛人 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034 科恩1939 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035 白银之城 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-036 地洞便利店 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037 我的勇者：末影城 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038 新月大陆 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-039 狂热运输3 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-040 伊莫 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-043 星眠 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-044 新月大陆 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-045 流明物语：特雷的回忆 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-046 渔力全开 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-047 影之刃零 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-048 源初之结 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-049 最终幻想 RESONANCE | exclude | release_calendar | 事件日期不在报告窗口 |
