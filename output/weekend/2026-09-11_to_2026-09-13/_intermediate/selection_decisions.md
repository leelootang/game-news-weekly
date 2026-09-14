# Selection Decisions

## 审计摘要

- 候选决策：98 条；include 16，exclude 82，merge 0。
- 卡片曝光去重：历史匹配 4 个；3 个此前已曝光且无新增事实的候选归入 repeat_only，I008 为唯一 card_carryover。其上期 prior_card_exposed=false、card_rank=未进入/10，本期不在正文暴露内部补位标记。
- 实质更新：I004 新增 iOS 畅销榜第5与首日新增超千万；I006 新增抢先体验首日125万美元与Steam峰值超34万。
- 维度覆盖自检：已覆盖并购整合、国产产品实盘、组织调整、平台分发、海外重点新品、发行数据与研发方向；未为凑维度纳入低分项。
- 产品日历漏挂反查：对行业源、产品排期源和周讯进行反扫；将 White Platinum 的实际发售日纠正为9月10日，将 Core Keeper 纠正为9月21日老品重大更新。确定性同步后，本期产品日历 0 条。
- 深度观察：D001 为本期唯一入选；周末报不执行周五下期接力检查。

## 决策明细

| ID | 栏目 | 决策 | 标题 | 依据 |
|---|---|---|---|---|
| I001 | industry_news | include | 沙特PIF考虑整合EA与Savvy Games Group，意在加强资产协同 | 并购与资产协同状态变化，事件3×相关3+钩子2 = 11。 |
| I002 | industry_news | include | 暴雪正式公布《暗黑破坏神5》，计划2029年春季发售 | 头部RPG新作官宣并给出明确档期，事件3×相关3+钩子2 = 11。 |
| I003 | industry_news | include | 网易《千里之路》明确独立产品方向，承接《射雕》技术与美术积累 | 国产新项目定位与研发承接信息完整，事件3×相关3+钩子1 = 10。 |
| I004 | industry_news | include | 《王者万象棋》上线次日升至iOS畅销榜第5，首日新增超千万 | 前期上线信息已报道，本期新增实盘榜单与新增用户量，构成实质更新，事件2×相关3+钩子2 = 8。 |
| I005 | industry_news | include | Roblox开放作品独立应用出口，覆盖移动端、PC与主机 | 平台分发能力出现明确扩展，事件2×相关3+钩子2 = 8。 |
| I006 | industry_news | include | 《Wardogs》抢先体验首日售出125万份，Steam峰值突破34万 | 此前测试热度已报道，本期进入商业化并出现销量与峰值新数据，事件2×相关3+钩子2 = 8。 |
| I007 | industry_news | include | 暴雪公布《StarCraft》开放世界射击新作，计划2030年推出 | 经典IP跨品类新作官宣，事件3×相关2+钩子2 = 8。 |
| I008 | industry_news | include | 索尼退出《Physint》合作后，Xbox接手发行并拓展影视合作 | 事件已进入上期候选但未做卡片展示，本期按单张补位口径纳入，事件3×相关2+钩子2 = 8。 |
| I009 | industry_news | include | 游卡上海近期裁减近两个项目组，研发转向“小而精” | 国内厂商组织与研发策略变化，事件2×相关3+钩子1 = 7。 |
| I010 | industry_news | include | CrazyGames移动发行月收入一年内增至原来3倍 | 渠道与数据基础设施带来可量化增长，事件2×相关3+钩子1 = 7。 |
| I011 | industry_news | exclude | 《旅行青蛙》中国版停止运营 | 历史上已有卡片曝光，且本期没有新状态或新事实，归为repeat_only，事件3×相关2+钩子1 = 7。 |
| I012 | industry_news | exclude | 《流浪地球》手游首次实机公布 | 上期已进行卡片曝光，本期聚合周讯未提供实质新事实，归为repeat_only，事件2×相关2+钩子1 = 5。 |
| I013 | industry_news | exclude | 2026年8月全球手游收入榜更新 | 此前已发布相同统计周期卡片，当前来源没有新增口径，归为repeat_only，事件2×相关2+钩子1 = 5。 |
| I014 | industry_news | exclude | Saber称北美团队已无实际开发 | 公司口径变化但与核心观察方向关联有限，事件2×相关2+钩子2 = 6，未达周末阈值。 |
| I015 | industry_news | exclude | 欧洲游戏公司外部人才支出增长63% | 区域性调查可用但缺少重点品类与公司关联，事件2×相关2+钩子1 = 5，未达阈值。 |
| I016 | industry_news | exclude | 《潜水员戴夫》销量突破1000万 | 里程碑明确但对当前优先方向关联偏弱，事件2×相关2+钩子1 = 5，未达阈值。 |
| I017 | industry_news | exclude | Ubisoft测试Steam免启动器体验 | 平台体验优化尚处测试阶段，事件2×相关2+钩子1 = 5，未达阈值。 |
| I018 | industry_news | exclude | Steam在英国测试信用卡年龄验证 | 政策测试影响有限且区域较窄，事件2×相关2+钩子1 = 5，未达阈值。 |
| I019 | industry_news | exclude | 《Age of Magic》累计收入超过1.2亿美元 | 正文仅为摘要片段，无法满足全文证据要求；即便事件2×相关3+钩子1 = 7，也不发布。 |
| I020 | industry_news | exclude | Polyarc工作室关闭 | 事件成立但规模和业务关联有限，事件2×相关1+钩子1 = 3，未达阈值。 |
| A001 | ai_news | include | 字节游戏江南工作室推进AI真人RPG《Beyond the Mundane》，团队扩至约20人 | AI直接进入游戏内容生产与交互，且有明确团队、商业模式和档期。 |
| A002 | ai_news | include | 腾讯为《和平精英》上线专属AI专家，把游戏知识库接入Agent | AI直接用于游戏知识服务与运营任务，具备规模化用户数据。 |
| A003 | ai_news | include | Meowa把AI像素素材生成推进到可直接进入游戏引擎的生产流程 | 生成内容可直接进入游戏引擎，开发环节迁移路径清晰。 |
| A004 | ai_news | exclude | 《原神》AI声音仿冒案获赔75万元 | 属于治理与权利边界案例，本期优先保留直接生产和产品应用。 |
| A005 | ai_news | exclude | EA在《NHL 27》使用生成式AI解说声音 | 有直接应用，但单点海外内容生产案例的可迁移价值低于入选三项。 |
| A006 | ai_news | exclude | 上海游戏AI生产力沙龙举行 | 以会议观点汇总为主，缺少具体产品或可验证生产结果。 |
| C001 | community_discourse | include | 《原神》UGC复刻《空洞骑士》场景，引发原创边界争论 | 周末窗口内出现并持续发酵，讨论对象和争议链路清晰。 |
| C002 | community_discourse | include | 《异环》韩服刮刮乐调整传闻，放大固定货币消耗与随机奖励争议 | 讨论在窗口内延续，且能拆解为固定成本与随机返还的机制争议。 |
| C003 | community_discourse | exclude | 《无限暖暖》BBQ玩法相似度讨论 | 原始讨论早于窗口，周末仅有零散回复且无官方更新。 |
| C004 | community_discourse | exclude | 《崩坏：星穹铁道》两年未新增四星角色讨论 | 话题起于9月9日，窗口内未出现独立新触发点；名额优先给周末新发酵事件。 |
| D001 | deep_analysis | include | 《Yet Another Zombie Survivors》1.0为何更像放大器，而不是第二次首发 | 有完整数据链和可迁移的版本发布判断，相关3+洞察3+证据3+卡片3 = 12。 |
| D002 | deep_analysis | exclude | 美国汽车市场报告 | 非游戏行业议题，相关0+洞察0+证据2+卡片0 = 2。 |
| release-candidate-003 | release_calendar | exclude | 王者万象棋 | 事件日期不在报告窗口 |
| release-candidate-004 | release_calendar | exclude | 塔塔冒险队 | 事件日期不在报告窗口 |
| release-candidate-005 | release_calendar | exclude | 王者万象棋 | 单源不具备正文资格 |
| release-candidate-006 | release_calendar | exclude | 黄金星漩 | 事件日期不在报告窗口 |
| release-candidate-001 | release_calendar | exclude | 白金档案PLATiNA ：： LAB | 事件日期不在报告窗口 |
| release-candidate-007 | release_calendar | exclude | 不/存在的你，和我 | 单源不具备正文资格 |
| release-candidate-008 | release_calendar | exclude | 索拉斯塔2 | 单源不具备正文资格 |
| release-candidate-009 | release_calendar | exclude | 血色序曲 | 单源不具备正文资格 |
| release-candidate-010 | release_calendar | exclude | 月相计划 | 事件日期不在报告窗口 |
| release-candidate-011 | release_calendar | exclude | WARDOGS | 事件日期不在报告窗口 |
| release-candidate-012 | release_calendar | exclude | 诡秘之主 | 事件日期不在报告窗口 |
| release-candidate-013 | release_calendar | exclude | 王者万象棋 | 单源不具备正文资格 |
| release-candidate-014 | release_calendar | exclude | 帝国时代3：决定版 | 单源不具备正文资格 |
| release-candidate-015 | release_calendar | exclude | 战狗 | 单源不具备正文资格 |
| release-candidate-016 | release_calendar | exclude | 异环 | 单源不具备正文资格 |
| release-candidate-017 | release_calendar | exclude | 血色序曲 | 单源不具备正文资格 |
| release-candidate-018 | release_calendar | exclude | 白金档案PLATiNA ：： LAB | 单源不具备正文资格 |
| release-candidate-019 | release_calendar | exclude | 索拉斯塔2 | 单源不具备正文资格 |
| release-candidate-020 | release_calendar | exclude | 辉光之城1907 | 单源不具备正文资格 |
| release-candidate-021 | release_calendar | exclude | 诡秘之主 | 单源不具备正文资格 |
| release-candidate-022 | release_calendar | exclude | 饿狼传说：群狼之城 | 单源不具备正文资格 |
| release-candidate-023 | release_calendar | exclude | 黑街厨神 | 单源不具备正文资格 |
| release-candidate-024 | release_calendar | exclude | Hela：鼠鼠奇旅 | 单源不具备正文资格 |
| release-candidate-025 | release_calendar | exclude | 索尼克PICO PARK | 单源不具备正文资格 |
| release-candidate-026 | release_calendar | exclude | NS运动度假胜地 | 单源不具备正文资格 |
| release-candidate-027 | release_calendar | exclude | 胧村正怪奇谭 | 单源不具备正文资格 |
| release-candidate-028 | release_calendar | exclude | 奇迹工厂 | 单源不具备正文资格 |
| release-candidate-029 | release_calendar | exclude | 木木屋 | 单源不具备正文资格 |
| release-candidate-030 | release_calendar | exclude | 嘉豪 | 单源不具备正文资格 |
| release-candidate-031 | release_calendar | exclude | 愚者不灭 | 单源不具备正文资格 |
| release-candidate-032 | release_calendar | exclude | Probably Stolen： Cyberpunk Pawnshop Simulator | 单源不具备正文资格 |
| release-candidate-033 | release_calendar | exclude | GTA6 | 单源不具备正文资格 |
| release-candidate-034 | release_calendar | exclude | 奇迹工厂 | 单源不具备正文资格 |
| release-candidate-035 | release_calendar | exclude | 木木屋 | 单源不具备正文资格 |
| release-candidate-036 | release_calendar | exclude | 护核纪元 | 单源不具备正文资格 |
| release-candidate-037 | release_calendar | exclude | 胧村正怪奇谭 | 单源不具备正文资格 |
| release-candidate-038 | release_calendar | exclude | MELTY BLOOD： TWI-LUMINA | 单源不具备正文资格 |
| release-candidate-039 | release_calendar | exclude | MELTY BLOOD： TWI-LUMINA | 单源不具备正文资格 |
| release-candidate-040 | release_calendar | exclude | 蓝色星原：旅谣 | 单源不具备正文资格 |
| release-candidate-041 | release_calendar | exclude | 暗黑破坏神5 | 单源不具备正文资格 |
| release-candidate-042 | release_calendar | exclude | 魔兽世界：无限 | 单源不具备正文资格 |
| release-candidate-043 | release_calendar | exclude | 暗黑破坏神4 | 单源不具备正文资格 |
| release-candidate-044 | release_calendar | exclude | 魔兽世界 | 单源不具备正文资格 |
| release-candidate-045 | release_calendar | exclude | 传奇之梦复古合击版 | 单源不具备正文资格 |
| release-candidate-046 | release_calendar | exclude | 金铲铲之战 | 单源不具备正文资格 |
| release-candidate-047 | release_calendar | exclude | 拳皇·命运 | 单源不具备正文资格 |
| release-candidate-048 | release_calendar | exclude | 热力无限赛车 | 单源不具备正文资格 |
| release-candidate-049 | release_calendar | exclude | 爆裂防线 | 单源不具备正文资格 |
| release-candidate-050 | release_calendar | exclude | 笑傲江湖：群侠传 | 单源不具备正文资格 |
| release-candidate-051 | release_calendar | exclude | 勇士之心 | 单源不具备正文资格 |
| release-candidate-052 | release_calendar | exclude | 星际争霸 开放世界新游 PC/主机 | 单源不具备正文资格 |
| release-candidate-053 | release_calendar | exclude | 植物大战僵尸杂交版-手机重制版 测试 | 单源不具备正文资格 |
| release-candidate-002 | release_calendar | exclude | 护核纪元 | 事件日期不在报告窗口 |
| release-candidate-054 | release_calendar | exclude | 破烂水手 | 单源不具备正文资格 |
| release-candidate-055 | release_calendar | exclude | 对峙：交锋时刻-对峙2国服 | 单源不具备正文资格 |
| release-candidate-056 | release_calendar | exclude | 欢迎来到古原镇 | 单源不具备正文资格 |
| release-candidate-057 | release_calendar | exclude | 菇域幽城 | 单源不具备正文资格 |
| release-candidate-058 | release_calendar | exclude | 三国志14 with威力加强传承版 | 事件日期不在报告窗口 |
| release-candidate-059 | release_calendar | exclude | 最终幻想7 Revelation | 事件日期不在报告窗口 |
| release-candidate-060 | release_calendar | exclude | 最终幻想 RESONANCE | 事件日期不在报告窗口 |
| release-candidate-061 | release_calendar | exclude | 舞力全开：传世金曲（Just Dance： Decades of Hits） | 事件日期不在报告窗口 |
| release-candidate-062 | release_calendar | exclude | 战锤40K：战争黎明4（Warhammer 40,000： Dawn of War IV） | 事件日期不在报告窗口 |
| release-candidate-063 | release_calendar | exclude | 欢迎来到古原镇 | 单源不具备正文资格 |
| release-candidate-064 | release_calendar | exclude | WARDOGS | 单源不具备正文资格 |
| release-candidate-065 | release_calendar | exclude | 女神异闻录4 Revival | 事件日期不在报告窗口 |
| release-candidate-066 | release_calendar | exclude | 蛋仔派对 | 单源不具备正文资格 |
