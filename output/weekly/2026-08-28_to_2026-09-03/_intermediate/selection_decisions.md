# 2026-08-28_to_2026-09-03 筛选决策

卡片曝光去重：双周历史窗口2026-08-14至2026-08-27；本期未使用card_carryover。ACE、王者万象棋与Manor Lords已在本周前序报告执行过各自的卡片补位，本周周报不重复补位；所有历史匹配逐项保留card_exposed、card_rank、card_limit与card_exposure_source。

维度覆盖自检：国内移动/国产产品与人才 41张候选；市场数据 31张候选；并购 10张候选；平台政策 44张候选；档期变动 16张候选；资本组织 24张候选；海外重大 22张候选。

产品日历漏挂反查：已扫描industry_news与release_calendar全部上线、定档、测试节点；误挂、重复、单源与低于多源优先级前7项者均显式exclude。

AI反扫：已扫描全部958条行业新闻输入与71条AI输入；产品日历采用修订后的schema 5审计队列并确定性取多源优先级前7项。

质量说明：1371条输入，0抓取失败、1条空正文（S0723）和200条非全文；空正文及snippet均未作为终稿证据。深度历史补充只服务人工选择的第五栏。

## I001 - 集英社游戏公布《征服纪：臣民之心》，结合殖民模拟与4X策略
- include → industry_news；首支预告和商店页面公开；殖民经营与4X为优先赛道。日历低于前四，行业独立收录。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0022, S0059
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["集英社游戏公布《征服纪：臣民之心》，结合殖民模拟与4X策略｜2026-08-28_to_2026-08-30｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "MicroSimulation", "product": "《征服纪：臣民之心》首次公开", "event_date": "2026-08-28", "event": "《征服纪：臣民之心》首次公开"}

## I002 - 《超自然行动组》与Garena达成合作，计划进入东南亚和拉美
- include → industry_news；独立发行合作事件，与历史DAU里程碑不同；正文不重复DAU和常规财报。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0037
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜2026-08-28_to_2026-08-30｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I003 - 暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net
- include → industry_news；平台与开发者新增具体发行合作，RPG优先赛道；与newsletter主分析为独立事件。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0378, S0289
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜2026-08-28_to_2026-08-30｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Blizzard", "product": "《巫师3》重制版进入Battle.net", "event_date": "2026-08-29", "event": "《巫师3》重制版进入Battle.net"}

## I004 - 轮盘赌构筑肉鸽《雪夜枪声》发售
- include → industry_news；短正文直接支持事件状态，达到7分；不因篇幅短而遗漏，不补无证据厂商和日期。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0028
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["轮盘赌构筑肉鸽《雪夜枪声》发售｜2026-08-28_to_2026-08-30｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I005 - Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代
- include → industry_news；本期原始采访明确刚公布的新游戏，4对4竞技为PVP优先赛道；不是综合稿尾部旧消息汇总。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0289
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代｜2026-08-28_to_2026-08-30｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I006 - 网易《燕云十六声》全球玩家突破一亿
- include → industry_news；独立玩家规模里程碑；不是常规版本或奖项宣传。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0050, S0111, S0385
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["网易《燕云十六声》全球玩家突破一亿｜2026-08-28_to_2026-08-30｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "网易", "product": "《燕云十六声》全球玩家突破一亿", "event_date": "2026-08-28", "event": "《燕云十六声》全球玩家突破一亿"}

## I007 - 4399投资杭州深空之序，持股5%布局AI智能体
- include → industry_news；E3×R3+M1=10；国内游戏公司新增AI Agent资本布局。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0565
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["4399投资杭州深空之序，持股5%布局AI智能体｜2026-08-31｜weekly_rollup_source"], "new_facts": ["4399投资新成立的杭州深空之序，占股5%。"], "prior_card_exposed": false}

## I008 - Garena开放世界手游《Free City》扩展至菲律宾等市场测试
- include → industry_news；E3×R3+M1=10；Garena重点主体的移动新品区域测试扩展。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0388
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜2026-08-31｜weekly_rollup_source"], "new_facts": ["测试范围由阿根廷扩展至菲律宾及更多小型市场。"], "prior_card_exposed": false}

## I009 - 前《使命召唤》设计师七周完成移动撤离射击游戏
- include → industry_news；E3×R3+M1=10；移动新品上线并披露开发周期、下载与转化数据。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0574
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["前《使命召唤》设计师七周完成移动撤离射击游戏｜2026-08-31｜weekly_rollup_source"], "new_facts": ["七周从概念推进到Android上线，下载超过8000次。"], "prior_card_exposed": false}

## I010 - 诗悦首曝复古英伦二次元新作《星途天城》
- include → industry_news；E3×R3+M1=10；国内厂商新项目首次公开。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0568
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["诗悦首曝复古英伦二次元新作《星途天城》｜2026-08-31｜weekly_rollup_source"], "new_facts": ["项目研发三年并经历两次玩法大改后首次曝光。"], "prior_card_exposed": false}

## I011 - Supercell签署Metacore收购协议，《Merge Mansion》团队月底并入
- include → industry_news；E3×R3+M2=11，达到日报阈值 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0757
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Supercell签署Metacore收购协议，《Merge Mansion》团队月底并入｜2026-09-01｜weekly_rollup_source"], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Supercell/Metacore", "product": "Merge Mansion", "event_date": "2026-09-01", "event": "同一份签署完成、月底交割的收购协议"}

## I012 - Savvy Games Group首任CEO Brian Ward卸任
- include → industry_news；E3×R3+M2=11，达到日报阈值 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0738
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜2026-09-01｜weekly_rollup_source"], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Savvy Games Group/Brian Ward", "product": "Savvy Games Group", "event_date": "2026-09-01", "event": "同一CEO卸任事件"}

## I013 - 4399投资《率土之滨》前主策创业公司广州铸微网络
- include → industry_news；E3×R3+M1=10，达到日报阈值 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0731
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["4399投资《率土之滨》前主策创业公司广州铸微网络｜2026-09-01｜weekly_rollup_source"], "new_facts": [], "prior_card_exposed": false}

## I014 - 米哈游领投《月圆之夜》制作人创业团队
- include → industry_news；E3×R3+M1=10，达到日报阈值 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0714
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["米哈游领投《月圆之夜》制作人创业团队｜2026-09-01｜weekly_rollup_source"], "new_facts": [], "prior_card_exposed": false}

## I015 - Supercell制作人Lasse Seppänen离职并计划成立新工作室
- include → industry_news；核心制作与管理人员离职并披露创业计划，Supercell固定R=3，10分入选。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0932
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Supercell制作人Lasse Seppänen离职并计划成立新工作室｜2026-09-02｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I016 - 《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布
- include → industry_news；从早期测试推进到三地软发布，属于可验证的产品阶段变化，10分入选。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0953
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "material_update", "prior_occurrences": ["暴雪移动端英雄射击《Overwatch Rush》进入早期测试 | weekly 2026-08-14_to_2026-08-20", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜2026-09-02｜weekly_rollup_source"], "prior_details": [{"report_window": {"start": "2026-08-14", "end": "2026-08-20"}, "report_kind": "weekly", "candidate_id": "I009", "event": "守望先锋IP移动英雄射击进入早期测试", "entities": ["Blizzard", "Overwatch Rush"], "title": "暴雪移动端英雄射击《Overwatch Rush》进入早期测试", "claims": ["Overwatch Rush", "移动端独占", "早期开发阶段", "超过1万次下载"], "source_ids": ["S0652"], "artifact": "output\\weekly\\2026-08-14_to_2026-08-20\\_intermediate\\report_items.json", "card_exposed": true, "card_rank": 10, "card_limit": 10, "card_exposure_source": "publish_log_manifest"}], "new_facts": ["8月31日在菲律宾、马来西亚和印度尼西亚启动软发布"], "prior_card_exposed": true}

## I017 - 《恶意不息》1.0版延期至2027年3月
- include → industry_news；动作RPG正式版延期且三份当前窗口来源覆盖，8分入选。 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。
- source_ids: S0939, S0989, S0995
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["《恶意不息》1.0版延期至2027年3月｜2026-09-02｜weekly_rollup_source"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Moon Studios", "product": "恶意不息", "event_date": "2026-09-02", "event": "同一主体、同一事件日期、同一独立事件的当前窗口报道"}

## A001 - 腾讯披露GIGA智能体已用于《和平精英》和《终极角逐》
- include → ai_trends；行业候选反扫：独立GIGA智能体应用，正文避开上周已报Motus动画管线。
- source_ids: S0062, S0066
- cluster_basis: {"subject": "腾讯", "product": "腾讯展示GIGA游戏智能体落地", "event_date": "2026-08-28", "event": "腾讯展示GIGA游戏智能体落地"}
- AI: {"ai_tier": "direct_application", "game_stage": ["product"], "industry_reverse_scan": true, "migration_path": null}

## A002 - 游族推出内部AI创作工具，覆盖广告素材与自然语言游戏制作
- include → ai_trends；已在内部推出具体研发与营销工具；非泛AI投资概念。
- source_ids: S0051, S0386
- cluster_basis: {"subject": "游族网络", "product": "游族部署AI广告与游戏创作平台", "event_date": "2026-08-28", "event": "游族部署AI广告与游戏创作平台"}
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "publishing"], "industry_reverse_scan": true, "migration_path": null}

## A003 - 腾讯展示Vox游戏语音引擎，披露140毫秒首包延迟
- include → ai_trends；具体游戏TTS引擎技术展示，与GIGA决策智能体为不同产品；只写披露性能，不推断已规模化部署。
- source_ids: S0062
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "product"], "industry_reverse_scan": true, "migration_path": null}

## A004 - 《1666：阿姆斯特丹》开发团队将生成式AI移出制作管线
- include → ai_trends；直接作用类：生成式AI已用于概念与前期制作，团队随后公开移除。
- source_ids: S0641
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "product"], "industry_reverse_scan": true, "migration_path": null}

## A005 - 《请神》把AI限制在关键交互节点，人工控制主叙事
- include → ai_trends；符合AI新闻采用标准，事实链完整
- source_ids: S0727
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "product"], "industry_reverse_scan": true, "migration_path": null}

## A006 - VAST完成约30亿元融资并推进可编辑AI 3D资产
- include → ai_trends；AI 3D已进入游戏资产和UGC生产环节，且有两份当前窗口来源。
- source_ids: S0911, S0923
- cluster_basis: {"subject": "VAST", "product": "游戏3D资产", "event_date": "2026-09-02", "event": "同一主体、同一事件日期、同一独立事件的当前窗口报道"}
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "product"], "industry_reverse_scan": true, "migration_path": null}

## C001 - 《崩坏：星穹铁道》高难模式连续加入定向机制，玩家质疑环境过度服务新角色
- include → community_discourse；8月27日异相仲裁争议在8月31日末日幻影更新后出现新阶段，触发、争议逻辑与时间线完整。
- source_ids: S0669, S0673

## C002 - 《世界计划》半周年“晚自习”登录奖励撞上学生防沉迷时段
- include → community_discourse；触发、争议逻辑、时间线与后续扫描完整
- source_ids: S0886

## C003 - 《赛尔号》线下赛被指低温且限制休息，玩家质疑赛事组织
- include → community_discourse；事件触发、争议逻辑与窗口内延续均完整，谨慎归因后入选。
- source_ids: S1089

## I018 - Frontier与Disney合作开发创意模拟经营新作
- include → industry_news；E3×R3+M1=10，达到周报8分门槛。
- source_ids: S1157
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}
- cluster_basis: {"subject": "Frontier Developments", "product": "Disney", "event_date": "2026-09-03", "event": "Frontier与Disney合作开发创意模拟经营新作"}

## I019 - Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务
- include → industry_news；E3×R2+M2=8，达到周报8分门槛。
- source_ids: S1148, S1154
- scores: {"event": 3, "relevance": 2, "hook": 2, "total": 8}
- 事件3×相关2+钩子2 = 8；E×R+M；include
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}
- cluster_basis: {"subject": "Nexus Mods", "product": "SteamDB", "event_date": "2026-09-02", "event": "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务"}

## I020 - 《CookieRun: Crumble》全球上线四周收入突破1400万美元
- include → industry_news；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0954, S1285
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}
- cluster_basis: {"subject": "Devsisters", "product": "CookieRun: Crumble", "event_date": "2026-09-03", "event": "《CookieRun: Crumble》全球上线四周收入突破1400万美元"}

## D001 - ROBLOX正在经历从“效率爆梗”向“长期留存”方向转型的阵痛期
- include → deep_analysis；精确人工selection选择，按原顺序写入周报第五栏。
- source_ids: S1098, S1371
- scores: {"relevance": 3, "insight": 3, "evidence": 3, "card": 3, "total": 12}
- history_check: {"prior_weekly_id": "2026-08-21_to_2026-08-27", "prior_titles": ["绕渠道直充正在改写手游收入判断：商店下滑不等于总收入下滑", "Steam成功新品扩容，Roguelite上升不能只用低价解释", "170%综合分成背后，微信把激励锁进同一产品的投放循环"], "reason": "上一期较早曾讨论Roblox业务转型，但上一期实际周报没有Roblox题；本窗口新增的是发现算法在留存与爆款之间的具体冲突。"}

## D002 - Discord不再只卖曝光：账号绑定与自动进度把社区流量变成可验证游玩
- include → deep_analysis；精确人工selection选择，按原顺序写入周报第五栏。
- source_ids: S0378
- scores: {"relevance": 2, "insight": 3, "evidence": 2, "card": 3, "total": 10}
- history_check: {"prior_weekly_id": "2026-08-21_to_2026-08-27", "prior_titles": ["绕渠道直充正在改写手游收入判断：商店下滑不等于总收入下滑", "Steam成功新品扩容，Roguelite上升不能只用低价解释", "170%综合分成背后，微信把激励锁进同一产品的投放循环"], "reason": "上一期没有社区平台、任务归因或账号绑定主题，本题不撞题。"}

## R001 - 王者万象棋
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0045, S0047, S0049, S0060, S0063, S0210, S0216
- scores: {"event": 2, "source": 4, "company": 3, "total": 11}
- cluster_basis: {"subject": "王者万象棋", "product": "王者万象棋", "event_date": "2026-09-10", "event": "同一产品同日产品日历节点"}

## R002 - 无限大
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0039, S0050, S0213
- scores: {"event": 2, "source": 4, "company": 3, "total": 11}
- cluster_basis: {"subject": "无限大", "product": "无限大", "event_date": "2027-01-15", "event": "同一产品同日产品日历节点"}

## R003 - 遗忘之海
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0050, S0213
- scores: {"event": 2, "source": 3, "company": 3, "total": 9}
- cluster_basis: {"subject": "遗忘之海", "product": "遗忘之海", "event_date": "2026-08-25", "event": "同一产品同日产品日历节点"}

## R004 - 星布谷地
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0718, S0719
- scores: {"event": 2, "source": 3, "company": 3, "total": 9}
- cluster_basis: {"subject": "星布谷地", "product": "星布谷地", "event_date": "2026-09-20", "event": "同一产品同日产品日历节点"}

## R005 - 凡应
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0057, S1135
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "凡应", "product": "凡应", "event_date": "2026-08-28", "event": "同一产品同日产品日历节点"}

## R006 - 地城狩猎
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0594, S0668
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "地城狩猎", "product": "地城狩猎", "event_date": "2026-08-31", "event": "同一产品同日产品日历节点"}

## R007 - 剑侠世界4：无限
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S1143, S1193, S1287, S1291, S1323
- scores: {"event": 2, "source": 4, "company": 0, "total": 8}
- cluster_basis: {"subject": "剑侠世界4：无限", "product": "剑侠世界4：无限", "event_date": "2026-09-03", "event": "同一产品同日产品日历节点"}

## R008 - 2026-01-15 公测
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0050, S0213
- scores: {"event": 3, "source": 3, "company": 3, "total": 12}
- cluster_basis: {"subject": "无限大", "product": "无限大", "event_date": "2026-01-15", "event": "同一产品同日产品日历节点"}

## R009 - 2026-09-02 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0913, S1037
- scores: {"event": 3, "source": 3, "company": 3, "total": 12}
- cluster_basis: {"subject": "王者万象棋", "product": "王者万象棋", "event_date": "2026-09-02", "event": "同一产品同日产品日历节点"}

## R010 - 2026-08-28 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0141, S0149, S0551
- scores: {"event": 3, "source": 4, "company": 0, "total": 12}
- cluster_basis: {"subject": "GTA6", "product": "GTA6", "event_date": "2026-08-28", "event": "同一产品同日产品日历节点"}

## R011 - 2026-08-28 9月10日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0045, S0047, S0049, S0060, S0063, S0210, S0216
- scores: {"event": 2, "source": 4, "company": 3, "total": 11}
- cluster_basis: {"subject": "王者万象棋", "product": "王者万象棋", "event_date": "2026-08-28", "event": "同一产品同日产品日历节点"}

## R012 - 2026-08-27 新品定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0045, S0047, S0049, S0060, S0063, S0210, S0216, S0551
- scores: {"event": 2, "source": 4, "company": 3, "total": 11}
- cluster_basis: {"subject": "王者万象棋", "product": "王者万象棋", "event_date": "2026-08-27", "event": "同一产品同日产品日历节点"}

## R013 - 2026-08-28 2027年1月15日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0039, S0050, S0213
- scores: {"event": 2, "source": 4, "company": 3, "total": 11}
- cluster_basis: {"subject": "无限大", "product": "无限大", "event_date": "2026-08-28", "event": "同一产品同日产品日历节点"}

## R014 - 2026-08-28 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0073
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R015 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0111
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R016 - 2026-07-31 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0211
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R017 - 2026-08-29 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0301
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R018 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0536
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R019 - 2025-07-24 公测
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0717
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R020 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1152
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R021 - 2026-08-28 12月测试定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0050, S0213
- scores: {"event": 2, "source": 3, "company": 3, "total": 9}
- cluster_basis: {"subject": "遗忘之海", "product": "遗忘之海", "event_date": "2026-08-28", "event": "同一产品同日产品日历节点"}

## R022 - 2026-09-01 2027年1月15日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0709, S0719
- scores: {"event": 2, "source": 3, "company": 3, "total": 9}
- cluster_basis: {"subject": "无限大", "product": "无限大", "event_date": "2026-09-01", "event": "同一产品同日产品日历节点"}

## R023 - 2026-09-01 9月20日测试定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0718, S0719
- scores: {"event": 2, "source": 3, "company": 3, "total": 9}
- cluster_basis: {"subject": "星布谷地", "product": "星布谷地", "event_date": "2026-09-01", "event": "同一产品同日产品日历节点"}

## R024 - 2026-08-27 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0027, S0058, S0295
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "遥遥西土", "product": "遥遥西土", "event_date": "2026-08-27", "event": "同一产品同日产品日历节点"}

## R025 - 2026-08-31 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0524, S0562
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "气球塔防6", "product": "气球塔防6", "event_date": "2026-08-31", "event": "同一产品同日产品日历节点"}

## R026 - 2026-08-31 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0560, S0649
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "BUZZ or DIE", "product": "BUZZ or DIE", "event_date": "2026-08-31", "event": "同一产品同日产品日历节点"}

## R027 - 2026-09-02 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0898, S1001
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "双轮成行", "product": "双轮成行", "event_date": "2026-09-02", "event": "同一产品同日产品日历节点"}

## R028 - 2026-09-02 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0905, S0988
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "NBA 2K27", "product": "NBA 2K27", "event_date": "2026-09-02", "event": "同一产品同日产品日历节点"}

## R029 - 2026-08-28 2026年第三季度上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0033
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R030 - 2026-08-29 2026年9月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0350
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R031 - 2026-08-31 2027年1月15日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0551
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R032 - 2026-08-31 2025年10月1日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0566
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R033 - 2026-09-01 9月10日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R034 - 2026-09-01 9月4日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R035 - 2026-09-01 9月22日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R036 - 2026-09-01 新品首次曝光
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0730
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R037 - 2026-09-02 9月10日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0913
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R038 - 2026-09-02 9月23日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0913
- scores: {"event": 2, "source": 2, "company": 3, "total": 7}

## R039 - 2026-09-02 公测
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S1060, S1078
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}
- cluster_basis: {"subject": "仙逆：本尊", "product": "仙逆：本尊", "event_date": "2026-09-02", "event": "同一产品同日产品日历节点"}

## R040 - 2026-09-03 公测
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S1318, S1335
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}
- cluster_basis: {"subject": "梦幻新诛仙：轻享", "product": "梦幻新诛仙：轻享", "event_date": "2026-09-03", "event": "同一产品同日产品日历节点"}

## R041 - 2026-09-03 内测
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S1320, S1336
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}
- cluster_basis: {"subject": "航海记", "product": "航海记", "event_date": "2026-09-03", "event": "同一产品同日产品日历节点"}

## R042 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0003
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R043 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0010
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R044 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0011
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R045 - 2026-08-28 抢先体验测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0020
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R046 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0028
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R047 - 2026-05-27 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0037
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R048 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0048
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R049 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0059
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R050 - 2026-08-28 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0065
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R051 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0073
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R052 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0138
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R053 - 2026-08-28 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0140
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R054 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0142
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R055 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0154
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R056 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0160
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R057 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0162
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R058 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0163
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R059 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0217
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R060 - 2026-08-29 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0294
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R061 - 2026-08-29 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0302
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R062 - 2026-08-04 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0410
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R063 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0521
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R064 - 2026-08-27 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0537
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R065 - 2026-08-23 公测
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0551
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R066 - 2026-08-23 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0551
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R067 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0558
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R068 - 2026-08-31 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0568
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R069 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0591
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R070 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0612
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R071 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0613
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R072 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0621
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R073 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0694
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R074 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0699
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R075 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0700
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R076 - 2026-09-01 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0710
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R077 - 2026-08-20 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0713
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R078 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R079 - 2026-09-01 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0732
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R080 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0732
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R081 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0732
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R082 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0772
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R083 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0790
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R084 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0796
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R085 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0803
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R086 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0901
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R087 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0917
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R088 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0919
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R089 - 2026-09-02 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1005
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R090 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1105
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R091 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1113
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R092 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1115
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R093 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1116
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R094 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1145
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R095 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1152
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R096 - 2026-08-13 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S1195
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R097 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1225
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R098 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1229
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R099 - 2026-09-01 9月3日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0718, S0866
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "梦幻新诛仙：轻享", "product": "梦幻新诛仙：轻享", "event_date": "2026-09-01", "event": "同一产品同日产品日历节点"}

## R100 - 2026-08-28 2026年9月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0007
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R101 - 2026-08-28 9月17日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0018
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R102 - 2026-08-28 新品首次曝光
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0024
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R103 - 2026-08-26 2026年8月26日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0059
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R104 - 2026-08-29 新品首次曝光
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0299
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R105 - 2026-08-29 9月10日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0302
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R106 - 2026-08-29 10月29日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0308
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R107 - 2026-08-30 9月测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0391
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R108 - 2026-08-31 10月29日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0592
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R109 - 2026-09-01 9月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R110 - 2026-09-01 9月11日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R111 - 2026-09-01 9月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R112 - 2026-09-01 9月22日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0718
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R113 - 2026-09-01 2026年10月27日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0719
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R114 - 2026-09-01 10月测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0725
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R115 - 2026-09-01 10月29日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0768
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R116 - 2026-09-01 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0771
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R117 - 2026-09-01 11月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0788
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R118 - 2026-09-02 11月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0908
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R119 - 2026-09-02 9月15日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0986
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R120 - 2026-09-02 2027年2月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0986
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R121 - 2026-09-03 11月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1099
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R122 - 2026-09-03 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1110
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R123 - 2026-09-03 2026年9月17日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1118
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R124 - 2026-09-03 11月19日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1121
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R125 - 2026-09-03 2027年3月5日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1122
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R126 - 2026-09-03 2027年4月8日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1123
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R127 - 2026-09-03 2027年春季上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1125
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R128 - 2026-09-03 2027年1月28日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1127
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R129 - 2026-09-03 2027年1月28日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1128
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R130 - 2026-09-03 2027年2月23日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1217
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R131 - 2026-09-03 9月22日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1290
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R132 - 2026-11-19 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0149, S0612, S0613, S0615
- scores: {"event": 1, "source": 4, "company": 0, "total": 4}
- cluster_basis: {"subject": "GTA6", "product": "GTA6", "event_date": "2026-11-19", "event": "同一产品同日产品日历节点"}

## R133 - 2026-09-04 老品跨平台上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0625, S0794, S0797, S1002
- scores: {"event": 1, "source": 4, "company": 0, "total": 4}
- cluster_basis: {"subject": "鬼武者 剑之道", "product": "鬼武者 剑之道", "event_date": "2026-09-04", "event": "同一产品同日产品日历节点"}

## R134 - 2026-08-28 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0235
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R135 - 2026-08-28 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0245
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R136 - 2026-08-28 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0246
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R137 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0255
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R138 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0258
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R139 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0260
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R140 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0261
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R141 - 2026-08-28 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0262
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R142 - 2026-08-28 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0263
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R143 - 2026-08-28 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0264
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R144 - 2026-08-28 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0265
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R145 - 2026-08-28 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0266
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R146 - 2026-08-29 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0361
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R147 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0429
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R148 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0430
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R149 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0431
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R150 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0432
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R151 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0433
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R152 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0434
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R153 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0435
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R154 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0436
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R155 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0437
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R156 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0438
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R157 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0439
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R158 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0440
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R159 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0441
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R160 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0442
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R161 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0443
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R162 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0444
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R163 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0445
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R164 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0446
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R165 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0447
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R166 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0448
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R167 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0449
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R168 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0450
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R169 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0451
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R170 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0452
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R171 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0453
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R172 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0454
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R173 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0455
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R174 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0456
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R175 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0459
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R176 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0460
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R177 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0461
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R178 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0462
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R179 - 2026-08-30 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0463
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R180 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0464
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R181 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0466
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R182 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0467
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R183 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0469
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R184 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0470
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R185 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0471
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R186 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0473
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R187 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0474
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R188 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0475
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R189 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0477
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R190 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0478
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R191 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0479
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R192 - 2026-08-30 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0481
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R193 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0482
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R194 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0483
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R195 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0484
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R196 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0485
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R197 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0486
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R198 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0488
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R199 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0489
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R200 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0490
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R201 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0491
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R202 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0492
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R203 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0493
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R204 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0494
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R205 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0495
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R206 - 2026-08-30 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0496
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R207 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0497
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R208 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0498
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R209 - 2026-08-30 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0499
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R210 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0659
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R211 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0660
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R212 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0661
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R213 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0662
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R214 - 2026-08-31 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0663
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R215 - 2026-08-31 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0666
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R216 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0855
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R217 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0859
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R218 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0862
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R219 - 2026-09-01 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0867
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R220 - 2026-09-01 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0868
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R221 - 2026-09-01 不删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0869
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R222 - 2026-09-01 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0870
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R223 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1068
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R224 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1070
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R225 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1071
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R226 - 2026-09-02 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1079
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R227 - 2026-09-02 不限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1080
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R228 - 2026-09-02 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1081
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R229 - 2026-09-03 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1321
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R230 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1328
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R231 - 2026-09-03 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1337
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R232 - 2026-09-03 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1338
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R233 - 2026-08-28 9月10日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0241
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R234 - 2026-08-28 9月10日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0252
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R235 - 2026-08-28 9月17日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0256
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R236 - 2026-08-28 8月29日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0267
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R237 - 2026-08-31 9月22日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0664
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R238 - 2026-08-31 9月1日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0667
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R239 - 2026-09-02 新品预下载
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1067
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R240 - 2026-09-02 9月14日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1073
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R241 - 2026-09-02 9月10日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1075
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R242 - 2026-09-03 9月11日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1332
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R243 - 2026-08-28 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0009
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R244 - 2026-08-28 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0016
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R245 - 2026-08-28 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0031
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R246 - 2026-11-19 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0072
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R247 - 2026-08-28 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0138
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R248 - 2026-10-02 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0150, S1011
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "空战奇兵8 希孚之翼", "product": "空战奇兵8 希孚之翼", "event_date": "2026-10-02", "event": "同一产品同日产品日历节点"}

## R249 - 2026-10-23 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0155, S1227
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "最终幻想 RESONANCE", "product": "最终幻想 RESONANCE", "event_date": "2026-10-23", "event": "同一产品同日产品日历节点"}

## R250 - 2026-10-15 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0171
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R251 - 2026-08-29 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0293
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R252 - 2026-08-29 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0334
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R253 - 2026-09-15 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0394
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R254 - 2027-01-15 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0395
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R255 - 2026-08-30 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0397
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R256 - 2026-08-30 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0400
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R257 - 2027-02-23 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0616
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R258 - 2026-09-01 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0703
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R259 - 2026-10-14 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0800
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R260 - 2026-09-01 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0802
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R261 - 2026-10-27 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0842
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R262 - 2026-08-27 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0914
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R263 - 2026-09-02 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0989
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R264 - 2026-09-25 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0999
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R265 - 2026-09-08 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S1000, S1228
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "月光光心慌慌（Halloween）", "product": "月光光心慌慌（Halloween）", "event_date": "2026-09-08", "event": "同一产品同日产品日历节点"}

## R266 - 2026-09-10 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S1018
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R267 - 2026-09-03 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1120
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R268 - 2026-09-03 老品重启回归
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1149
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R269 - 2026-09-02 老品重启回归
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1066
- scores: {"event": 1, "source": 1, "company": 0, "total": 1}

## Q0001 - 《GTA6》全新加长版预告正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0001
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0002 - 『偶像传奇！闪耀再临』 Nintendo Switch 版商店页面现已公开
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0002
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0004 - 《变形金刚》擎天柱配音演员彼得·库伦去世，享年85岁
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0004
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0005 - 【更新】《剑网3》制作人郭炜炜宣布离职
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0005
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0006 - 土木人狂喜：《建筑模拟器：进化》公布全新拆除玩法
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0006
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0008 - 传奇再临，《潜龙谍影：大师合集 Vol.2》今日全球正式推出
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0008
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0012 - 2026《影之刃零》微星游戏本选购攻略， RTX50显卡+分辨率+帧数全覆盖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0012
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam愿望单突破200万，预购表现达《黑神话》同期73%｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预购首周收入估算约1450万美元｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0013 - 中元节消暑必备：心理恐怖游戏《无处安睡》免费试玩现已开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0013
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0014 - 生活模拟游戏「Witchbrook」正式确认中文名《巫奇魔法学院》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0014
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0015 - 增量放置游戏《米粒新世界》Demo现已开放
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0015
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0017 - 日本前卫艺术家草间弥生去世，享年97岁
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0017
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0019 - Xbox官宣光盘转数字版游戏功能，8月31日开启测试
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0019
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0021 - Raw Fury 公布全新合作类高尔夫平台跳跃游戏《拜拜邦妮》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0021
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0023 - 手绘银河恶魔城续作《Greak 2: Alliance of the Storms》正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0023
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0025 - Epic喜加二：《家族传奇：桌面版》《呼吸边缘》免费领
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0025
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0026 - 【抽奖】最多6人联机开超市！《百宜佳超市模拟器》限时八折优惠开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0026
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0029 - 《幻珠奇港》将于9月7日正式登陆 Steam
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0029
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0030 - 《逃脱学院2：再返校园》公开全新校园与第二章试玩内容
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0030
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0032 - 《湮灭之潮》斩获科隆游戏展「最具史诗感」大奖：国产单机游戏惊艳世界舞台
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0032
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0034 - 全球手游大洗牌！超休闲、休闲和中重度，最终都融合成同一种游戏？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0034
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0035 - “游戏禅师”陈星汉要做发行？官宣TGC发行品牌，助力游戏创作者“梦想成真”！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0035
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0036 - 中国游戏“冲爆科隆游戏展”！GameLook带你见识大场面
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0036
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0038 - 恺英网络发布2026半年报：营收同比增长86%、净利润大增50%
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0038
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0040 - 米哈游大伟哥现身科隆展，现场晒合影
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0040
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0041 - GTA 6 曝光27分钟实机，开放都市世界的‘妈妈’
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0041
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0042 - 孙宇晨爱上景甜是因为《QQ飞车》？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0042
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0043 - 鹰角在科隆，拿了个国产游戏史无前例的奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0043
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0044 - 鹰角将于2027年底搬迁新大楼，员工租房补贴同步调整
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0044
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0046 - 三七新游杀进畅销Top15：男频逆袭爽文，能复刻大女主神话吗？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0046
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0052 - 玩过《源初之结》后，我感觉米哈游真要走出舒适区了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0052
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0053 - 开服千战！魔域口袋版启世服冲战攻略
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0053
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0054 - 西山居再无郭炜炜
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0054
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0055 - 决胜巅峰东欧中亚赛区今日开赛，Team Spirit领衔冲击M8
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0055
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0056 - 剧情探索短篇游戏《捉迷藏-Hide and Seek》已于Steam免费推出！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0056
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0061 - 全球1300+创作者参与角逐 沐瞳2026全球皮肤设计挑战赛收官
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0061
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0064 - 《疯狂出租车》正式复活之前，你可以先在《索尼克赛车》里练起来
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0064
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0067 - 身处Xbox转型之际的COD，试图重新挽回玩家的信任
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0067
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0068 - “免费升级是CDPR的一贯风格”：《巫师 3》新资料片团队对我们说
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0068
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0069 - 《黎明杀机》开发商的新作，做了款“异星打工”游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0069
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0070 - 印着皮卡丘的小卡片，如何见证了30年的岁月时光
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0070
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0071 - GTA6放出超长玩法实机：被漏成筛子的R星，还有这么多猛料？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0071
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0074 - Playdate maker Panic refunds tariff surcharges to customers
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0074
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Makers Fund募得2.5亿美元第四期基金，资产管理规模达15亿美元｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0075 - Grand Theft Auto 6 30-minute teaser debuts on Netflix
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0075
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0076 - Sensor Tower: Netflix US mobile viewership increased 35% during GTA 6 extended preview
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0076
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0077 - Rockstar formed a new LA-based team to develop more realistic NPCs for Grand Theft Auto 6
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0077
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0078 - Cloud Imperium delays Squadron 42 to 2027 – "There is no way I want to launch into the attention buzz saw of GTA 6"
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0078
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0079 - Limbic Entertainment on life after Bandai Namco
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0079
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0080 - GTA 6 will have a halo effect for the entire industry | Opinion
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0080
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0081 - CookieRun: Crumble surpasses $14.3m revenue ahead of first major update
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0081
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0082 - Cutting edge content in Canada with PGC Summit Montréal
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0082
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0083 - AI powering the global engine for game studios
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0083
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0084 - Tencent Games showcases AI tools for game development at gamescom
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0084
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0085 - Dubai brings biggest-ever pavilion to Gamescom 2026 with top 10 gaming hub ambition
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0085
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0086 - Nicholas Le named PeopleFun CEO as Tamara Feiman takes over Lion Studios
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0086
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0087 - Meta and Roblox agree to strengthen child safety measures in the Philippines
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0087
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox上线实验早期预警与实时配置，创作者可按玩家分群更新体验｜daily 2026-08-24_to_2026-08-24｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox限制面向儿童的奖励驱动媒体流，不影响主动触发广告｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox拟在利雅得设立中东北非总部，并支持当地创作者｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox限制儿童入口中的奖励驱动媒体流｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0088 - Embark Studios' Neil Houari to speak at PGC Nordics
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0088
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0089 - New release roundup: Fantasy Life i, Tiny Room Stories: Eclipse, Ultrapool, and more
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0089
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0090 - Where Winds Meet surpasses 100m players worldwide
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0090
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0091 - 5 takeaways from Gamescom 2026: A truly global show, AI's impact, Apple and Google's charm offensive, and what was missing
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0091
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0092 - Google settles UK app developers’ class action lawsuit for $353m
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0092
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "AppMagic：二季度中度手游仅射击品类收入同比增长｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0093 - CD Projekt Red has The Witcher 4 running on all target platforms after Cyberpunk 2077 lesson
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0093
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0094 - How you (yes, you) can benefit from 1-on-1 synchronous playtesting
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0094
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0095 - Spanish union calls for ongoing strike action at Ubisoft Mobile Barcelona
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0095
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0096 - Warlock's magic system was built on game-bending player choices
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0096
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "AppMagic：二季度中度手游仅射击品类收入同比增长｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0097 - Panic refunds tariff fees, 1047 Games pivots from Splitgate, and Gamescom Dev grows - Patch Notes #67
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0097
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0098 - GDC Side Quest - Inside Austin Wintory's Collaborative Composing Process
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0098
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0100 - Apple reportedly saw US App Store spending fall for the first time in a decade, and Tim Sweeney has thoughts
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0100
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "AppMagic：二季度中度手游仅射击品类收入同比增长｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0101 - Everything shown at the Grand Theft Auto 6 Netflix special
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0101
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0102 - Grand Theft Auto 6’s Netflix special convinced me that Jason and Lucia will be the best GTA protagonists
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0102
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0103 - One of San Francisco’s busiest streets has become Rayquaza Road as Pokémon Worlds 2026 & PokémonXP begins
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0103
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0104 - ‘This is horrifying’: Nvidia’s controversial DLSS 5 AI filter leaks and players are inserting it into every game
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0104
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0105 - GTA 6 is confirmed to run at 30 frames per second
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0105
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0106 - GTA 6’s 30,000 calorie meat sandwich parody ad actually used Red Dead Redemption 2 as a backdrop
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0106
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《三角洲行动》日活突破5000万，进入高基数长线运营阶段｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0107 - Grand Theft Auto 6’s map is three times bigger than Red Dead Redemption 2
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0107
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0108 - 《昭和米国物语》：一款游戏要靠什么吸引人？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0108
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0109 - 听预告片里的音乐，就能知道GTA6讲了一个什么样的故事
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0109
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0110 - 触乐怪话：热爱UE5
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0110
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0112 - 为了设计《永劫无间》的新地图，我们都踩了哪些坑？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0112
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0113 - 一周年的手瓦，在成都“秀翻”全场？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0113
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0114 - Xbox CEO Plays Coy About Whether Elder Scrolls 6 Will Skip PlayStation
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0114
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0115 - Devolver Digital Reveals Its GTA 6 Competitor, And It’s A Remaster Of A Nonexistent Remake
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0115
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0116 - Exterminauts Devs Talk Helldivers Comparisons And How It Separates Itself
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0116
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0117 - You Can Pet (And Scold, You Monster) The Dog In GTA 6
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0117
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0118 - GTA 6 Skipping PC At Launch And Having No Online Right Away Is Good, Helldivers Boss Says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0118
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0119 - GTA 6 Returns To Six-Star Wanted Levels
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0119
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧公布《Rainbow Six Tactics》，采用单人回合制战术玩法｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0120 - GTA 6 Map Is 3X Bigger Than Red Dead Redemption 2’s
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0120
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0121 - GTA 6 Story Is About “Whether Love Can Survive Through This Storm”
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0121
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0122 - GTA 6 Has A Red Dead 2 Honor-Style System Tracking How Violent You Are
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0122
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0123 - GTA 6’s Jason Has A Case Of Bane-itis
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0123
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0124 - GTA 6’s Jason And Lucia Aren’t Necessarily A Couple
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0124
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0125 - GTA 6’s Big Netflix Extended Look: All The Things We Learned
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0125
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0126 - Grand Theft Auto 6 Will Have No Microtransactions Or Generative AI
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0126
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0127 - Stealing Cars In GTA 6 Is Probably More Complicated Than You Expected
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0127
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0128 - GTA 6 NPCs Will Notice If You’re Carrying A Weapon In Public
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0128
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0129 - Gears Of War: E-Day Had To Solve One Big Lore Problem –  How Do You Get A Lancer Into The Game?
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0129
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0130 - Hellraiser: Revival Is More Than Just Cenobites and Gore – 10 Things We Learned From Saber Interactive
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0130
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0131 - Saber Responds To AI Criticisms In Rideshare Game And Promises, “We Will Never Fire Someone And Replace Them With AI”
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0131
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0132 - Gears Of War: E-Day Has A Battle Royale-Inspired PvP Mode Where You Can Strip The Flesh Off Enemies
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0132
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0133 - Saber Boss Reacts To The Death Of Physical Games And Rising Console Prices
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0133
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0134 - GTA 6: All The Biggest Takeaways From The Big New Trailer That You Need To Know
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0134
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0135 - 《GTA6》地图规模非常庞大
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0135
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0136 - 英伟达财报只字未提游戏，RTX 6080何时发布？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0136
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0137 - Rockstar谈《GTA6》讽刺尺度
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0137
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0139 - 《GTA6》差点有四位主角？Rockstar曾认真考虑
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0139
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0143 - Rockstar：不喜欢《GTA6》恋爱内容？随你便
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0143
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0144 - 《GTA6》将彻底改变偷车玩法
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0144
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0145 - 《GTA6》全面重做通缉系统：会被持续追捕
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0145
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0146 - Rockstar解答《GTA6》通关时长：约需80小时
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0146
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0147 - Rockstar要用《GTA6》证明自己会写爱情
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0147
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0148 - 《GTA6》重返罪恶都市，野心对标《圣安地列斯》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0148
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0151 - 《共鸣：瘟疫传说传承》开场实机演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0151
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0152 - 《动物园之星2》「研究车辆」宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0152
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0153 - 《饿狼传说：群狼之城》「达克·金」动画短片 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0153
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0156 - 《特技演员：好莱坞》「侏罗纪世界」预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0156
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0157 - 《星球大战 零号连队》实机演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0157
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0158 - 《二氧化物》宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0158
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0159 - XBOX 25周年限量版主机预购宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0159
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0161 - 《Holstin》宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0161
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0164 - 电影《肖申克的救赎》上映宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0164
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0165 - 《007 初露锋芒》「路径追踪」宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0165
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0166 - PlayStation 27英寸游戏显示器发售宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0166
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0167 - 《警目如炬》宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0167
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0168 - 《GTA 6》独家前瞻：你将会在这个游戏里待很长时间
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0168
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0169 - gamescom 2026特别节目02
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0169
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0170 - 《红色沙漠：增强版》开发者专访 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0170
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0172 - 《全面战争：战锤40K》上手前瞻 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0172
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0173 - 《魔法门之英雄无敌3 重制版》上手前瞻 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0173
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧公布《英雄无敌III重制版》，成都与上海团队主导开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0174 - 《湮灭之潮》获gamescom「最具史诗感」大奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0174
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0175 - 本周 Steam 值得关注的游戏 08.24 - 08.30（五）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0175
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0176 - itch 一周游戏汇：8月17日-8月23日（上）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0176
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易《雾海之下》由首曝招募推进至首次测试｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0177 - Arc Raiders is adding a camera mode as part of October's major update, but some fans need more proof that the game's not going to wither away
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0177
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Arc Raiders》远征系统暂停至2027年初重做｜weekend 2026-08-21_to_2026-08-23｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《ARC Raiders》累计销量接近1600万份，腾讯中国服强调“撤离冒险”定位｜daily 2026-08-24_to_2026-08-24｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0178 - I have solved the male loneliness epidemic in Grand Theft Auto 5
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0178
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0179 - Manor Lords celebrates 4 million copies sold with a new major update which gives players the chance to become 'a cow-herding mogul'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0179
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0180 - Grand Theft Auto 6 reveal live coverage: breaking down the Netflix 'extended look' event
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0180
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0181 - Where to find new armor and weapons in Elden Ring's Tarnished Edition
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0181
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0182 - Where to find the Torrent skins in Elden Ring's Tarnished Edition
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0182
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0183 - Star Citizen's Squadron 42 delayed again, this time to avoid 'the attention buzz saw of GTA 6' says Chris Roberts
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0183
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0184 - Cyberleek may have just cashed out on their GTA 6 leak, earning over $200,000 in the most predictable crypto rugpull ever performed
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0184
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0185 - The GTA 6 reveal has me wowed by Vice City and underwhelmed by Rockstar's same old missions
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0185
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0186 - What do you think of the GTA 6 reveal?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0186
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0187 - GTA 6 map is apparently 3 times larger than Red Dead Redemption 2's, twice as large as GTA 5's
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0187
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0188 - GTA 6 gameplay reveal breakdown: A summary of all the details we spotted
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0188
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0189 - Every GTA 6 song confirmed so far
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0189
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0190 - The GTA 6 Netflix exclusive reveal is on YouTube now
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0190
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0191 - Looks like you can try DLSS 5 out today yourself
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0191
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0192 - Netflix is likely pleased as punch with the GTA 6 extended look, which more than doubled its web traffic
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0192
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0193 - GTA 6 is adding a more nuanced version of Red Dead Redemption 2's honor system to ensure player characters aren't too 'all-powerful'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0193
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0194 - 'I'm done. I used up my luck for this timeline': Redditor accidentally saves $5,000 on RTX 5090 Razer Blade 18 thanks to labelling error
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0194
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0195 - After seeing what GTA 6 does to a PS5 we're even more desperate to see what the PC version has for us
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0195
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0196 - id Software's former co-owner says they absolutely would've used gen AI back in the day: 'John Carmack would be like making Skynet or something'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0196
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0197 - Pulsar's new mouse is sliced in half to make it genuinely 'crazy-light'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0197
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0198 - All the key details about 'anime GTA' game Ananta
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0198
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0199 - Fable director says they aren't 'scared of other big games' except one—it's GTA 6, in case you were living under a rock
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0199
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0200 - Rockstar has to 'be careful' about what GTA 6 picks to satirize because 'very specific political issues or memes will date fast'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0200
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0201 - Chinese memory maker YMTC wants to dethrone Samsung and SK hynix by the end of 2027
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0201
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Makers Fund募得2.5亿美元第四期基金，资产管理规模达15亿美元｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0202 - 靠共创Vlog出圈的社交App「setlog」霸榜日本应用免费榜Top1！这款产品给社交赛道开发者带来了哪些增长新思路？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0202
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0203 - 对话腾讯制作人：活了19年被代代传下去，玩家不散我们不弃
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0203
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0204 - 技嘉D5 Single Boost技术亮相 提升单条DDR5内存性能体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0204
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0205 - 技嘉推出猎鹰及冰猎鹰白金电源，覆盖750W至1000W
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0205
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0206 - 技嘉X870E X3D系列主板选购指南：从冰雕到超级冰雕，哪款更适合你？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0206
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0207 - AORUS×AQ 战队联名主机登场——职业同款触手可及
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0207
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0208 - 巨人网络上半年净利21.44亿元增176%，拟拿出超七成利润分红
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0208
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0209 - 27分钟的实机演示，让《GTA6》亮出了王牌！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0209
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0212 - 观察｜全球1300+创作者参与角逐沐瞳2026全球皮肤设计挑战赛收官
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0212
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0214 - 观察｜决胜巅峰东欧中亚赛区今日开赛，TeamSpirit领衔冲击M8
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0214
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0215 - 观察｜官宣！决胜巅峰M8世界总决赛席位公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0215
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0218 - Gemini Omni 1.1 Flash 发布，为开发者提供更强生成式视频控制
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0218
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0219 - OpenAI 失控智能体集体逃逸沙箱并攻击"幽灵"评分器事件调查公布
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0219
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0220 - 诉讼指控 xAI 使用儿童性虐待材料训练 Grok 模型
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0220
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0221 - 英伟达预计 2028 财年销售额达 6730 亿美元
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0221
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0222 - Gemini 3.5 Transcribe 发布：更精准的实时语音转写模型
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0222
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0223 - Midjourney 开放 V8.2 图像编辑模型测试
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0223
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0224 - Open ASR 排行榜新增首个全球南方语言：印地语与印度英语评测集
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0224
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0225 - 腾讯混元发布 Hy4 preview：770B 总参数、1M 上下文，开源上线
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0225
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0226 - AI 工程师笔记本：在 Colab 上免费、无需框架即可使用 RAG/智能体/评估工具
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0226
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0227 - Terminal-Bench-Science 0.1：评估科研工作流中的 AI 智能体
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0227
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0228 - Gemini 3.5 Transcribe 完整指南：告别 ASR 转录难题
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0228
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0229 - GLM-5.3 开源权重，智能体编码与网防最强
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0229
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0230 - August’s Epic learning content: Networked physics, dynamic audio, and more
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0230
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0231 - 天谕 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0231

## Q0232 - 无限暖暖 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0232

## Q0233 - 植物大战僵尸2 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0233

## Q0234 - 燕云十六声 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0234

## Q0236 - 逆水寒手游 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0236

## Q0237 - 魔兽世界怀旧服：燃烧的远征 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0237

## Q0238 - 盖世豪侠 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0238

## Q0239 - 一梦江湖(官服) - 参与活动兑换【时装·百味珍】
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0239

## Q0240 - 三角洲行动-9.4新赛季开启 - 免费领【可爱凶兽】系列枪皮
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0240

## Q0242 - 使命召唤手游-崩坏3联动9月开启 - 登录领史诗角色
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0242

## Q0243 - 元梦之星 - 减负季登录得时装
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0243

## Q0244 - 光与夜之恋 - 6星灵犀齐司礼・风月宜量登场
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0244

## Q0247 - 无限暖暖(官服)-2.9版本 - 心意限定抽10赠10
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0247

## Q0248 - 植物大战僵尸2-月球基地 - 新世界「月球基地」开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0248

## Q0249 - 火影忍者手游 - 新忍者不立土登场
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0249

## Q0250 - 燕云十六声(官服) - 全新大型PVE玩法【藏锋志】开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0250

## Q0251 - 王牌竞速(官服) - 幽伶夜行时尚节狂送百抽
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0251

## Q0253 - 白银之城(官服) - iOS占位符1.31上线,安卓或同1月上线
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0253

## Q0254 - 穿越火线：枪战王者体验服 招募中 - 参与招募抢先体验鬼吹灯联动版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0254

## Q0257 - 蛋仔派对(官服) - 全新区域【泊风新城】开放
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0257

## Q0259 - 逆水寒(官服)-新世界 - 新地图「兰沧寨」开放
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0259

## Q0268 - 洛克王国：世界-S3赛季 - 19:00 S4新赛季直播
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0268

## Q0269 - [厂商]鸣潮与古剑奇谭三友好互动
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0269

## Q0270 - [周边] [鸣潮] 8.25更新爱弥斯也有问题 / 陆赫斯角色礼盒亚克力色纸 亚克力含量为0(已滑跪)
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0270

## Q0271 - [鹰角] [终末地]终末地限定池终于迎来大保底继承机制-但是复刻池且只继承同角色
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0271

## Q0272 - [周边] 库洛偷工减料后，选择的方式是——紧急修改商品信息
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0272

## Q0273 - [燕云十六声]哔哩哔哩会员购上线燕云only展污名男玩家偷拍犯
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0273

## Q0274 - [新瓜]喜提刑事处罚 疑似米哈游同园区某游戏公司员工造谣被抓
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0274

## Q0275 - [诡秘之主]攻略up主吐槽后台数据女性玩家高达90%
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0275

## Q0276 - [米哈游] 真珠实机演示，毛笔画出油画
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0276

## Q0277 - [厂商] [新瓜]尘白前发行制作人林增鸿中元节深夜现身直播间感谢玩家
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0277

## Q0278 - [厂商] 上海英澈网络进入破产清算程序 《千年之旅ELF》进行停服维护进行运营权限交接
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0278

## Q0279 - [疑似内容]尘白通过icp备案审核，尘白似乎真的要有所动作
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0279

## Q0280 - [新瓜]炼金工坊出的ai陪伴软件，ai没有二审，现已成为高价语音文爱软件
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0280

## Q0281 - [网易][米哈游]科隆上大伟哥疑似现身无限大展区 更新：已确认
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0281

## Q0282 - [厂商] 米哈游AI聊天软件AnuNeko下周永久关闭
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0282

## Q0283 - [小瓜]米商稿使用ai且被ai软件公开
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0283

## Q0284 - [影之诗]黑暗决斗是真实存在的！
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0284

## Q0285 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0285

## Q0286 - [新瓜] 小黑盒用户挂源初之结内测内容遭仙家军围猎威胁起诉
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0286

## Q0287 - [崩坏星穹铁道]恶臭剧情大赏
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0287

## Q0288 - [白银之城]ios商店透露了白银之城的上线日期
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0288

## Q0290 - 《湮灭之潮》斩获科隆游戏展「最具史诗感」大奖：国产单机游戏惊艳世界舞台
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0290
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0291 - 《幻珠奇港》将于9月7日正式登陆 Steam
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0291
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0292 - 《逃脱学院2：再返校园》公开全新校园与第二章试玩内容
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0292
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0296 - 【抽奖】最多6人联机开超市！《百宜佳超市模拟器》限时八折优惠开启
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0296
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0297 - 殖民模拟 × 4X 策略游戏《征服纪：臣民之心》正式发表
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0297
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["4X策略游戏《魔法大战略：穆瑞耶之心》推出免费Demo｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0298 - 手绘银河恶魔城续作《Greak 2: Alliance of the Storms》正式公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0298
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0300 - Epic喜加二：《家族传奇：桌面版》《呼吸边缘》免费领
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0300
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0303 - 成都厂商的湮灭之潮，斩获科隆“最具史诗感”奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0303
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0304 - 科隆惊艳亮相后，这支上海团队要扩军冲刺了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0304
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0305 - 成都厂商的湮灭之潮，斩获科隆“最具史诗感”奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0305
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0306 - 科隆展10公里外，腾讯整了个「吃力不讨好」的大活
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0306
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0309 - EWC Paris success, GTA 6’s big reveal and evolving live ops | Week in Views
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0309
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0310 - Gamescom's loudest absence: A masterclass in not showing up
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0310
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0311 - An unofficial PC port of Blue Dragon, a JRPG from the creators of Final Fantasy and Dragon Ball, is now available
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0311
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0312 - Pokémon is coming to Disney as The Misadventures of Sirfetch’d & Pichu debuts on Disney+
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0312
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0313 - EA confirms leaked Iron Man game footage is real: ‘Now you know’
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0313
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0314 - Project Helix will be a ‘family of devices,’ Xbox CEO confirms
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0314
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0315 - Podcast: Live reaction from Gamescom and GTA 6’s big reveal
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0315
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Roblox上线实验早期预警与实时配置，创作者可按玩家分群更新体验｜daily 2026-08-24_to_2026-08-24｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0316 - ‘It’s heartbreaking’: Numerous Gamescom devs say their equipment was stolen
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0316
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0317 - INTERVIEW: Mega Man Dual Override devs discuss Proto Man’s return, and lessons from Mega Man 11
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0317
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0318 - 漫步在游戏世界
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0318
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0319 - GTA 6 Lets You Throw Dog Poop At People
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0319
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0320 - GTA 6’s Long Wait Has People Realizing Their Own Mortality
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0320
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0321 - Turn-Based-Tactics Fans Are Suddenly Eating Very Well
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0321
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["育碧公布《Rainbow Six Tactics》，采用单人回合制战术玩法｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0322 - It’s Time I Let Go Of My Favorite Alien Isolation 2 Theory
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0322
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0323 - GTA 6 Looks Like It Features This Popular TV Show Apartment
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0323
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0324 - Fable Dev Happy About Delay To 2027 To Avoid “Chaotic Window,” And We All Know That Means GTA 6
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0324
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0325 - Leaked DLSS 5 Mod Shows Just How Much Nvidia’s AI Filter Can Mess With Your Games
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0325
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0326 - CD Projekt Red Offers To Help Gamescom Theft Victim As Industry Shows Its Support
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0326
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0327 - Tech Experts Call Grand Theft Auto 6 The Most Visually Advanced Game To Date, Which Explains Why It’s Stuck At 30FPS
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0327
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0328 - XBOX暗示Project Helix不止一款设备
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0328
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0329 - 科隆游戏展 2026《无限大》实机试玩：看到捅破天花板的决心与实力
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0329
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0330 - 《湮灭之潮》试玩版最高难度84分钟演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0330
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0331 - 《GTA6》游戏前瞻 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0331
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0332 - CESA 顶尖游戏创作者学院（TGCA）亮相科隆独立展区
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0332
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0333 - 糟糕的游戏设计
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0333
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0335 - 小红书下场，AI小游戏终于有了流量入口
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0335
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0336 - ROI从64%到270%，《猪了个猪》做对了什么
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0336
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0337 - I tried the sequel to Task Manager and it has too many special effects
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0337
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0338 - I have modded many dogs, several cows, 2 lions, and a chimpanzee into Grand Theft Auto 5, and they are all my friends
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0338
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0339 - 5 samurai movies to watch before playing Onimusha: Way of the Sword
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0339
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0340 - Nodusfall isn't Elden Ring, Monster Hunter or a typical HoYoverse game—it's something very different
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0340
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0341 - Bland or badass? The internet is split on GTA 6's Jason, and so is PC Gamer
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0341
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0342 - Path of Exile 2's first event league goes 'oops, all bosses' and reworks its worst mode so sane people can finally enjoy it
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0342
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0343 - 'Claude Strife': DLSS 5 has escaped into the wild, and things are immediately weird
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0343
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0344 - Hello Neighbor's multiplayer spinoff has been 'temporarily shut down' after a hacker wiped player progression and demanded the game's 'removal from sale across all platforms'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0344
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0345 - 'Well, that didn't go as planned' says EA as it footage of its Iron Man game leaks online
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0345
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0346 - I've checked gaming PC deals every week for two years and I'm not exaggerating when I say there isn't a single well-priced PC left
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0346
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0347 - Rockstar considered having four protagonists in Grand Theft Auto 6, but the studio 'worried about diluting the amount of player time' with each character
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0347
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0348 - I played just an hour of Total War: Warhammer 40,000 and it was the highlight of my year
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0348
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0349 - 斩获2026科隆游戏展“最具史诗感游戏”大奖！《湮灭之潮》惊艳世界舞台
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0349
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0351 - 联邦法官裁定特朗普政府将 Anthropic 列入黑名单违法
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0351
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0352 - OpenAI 攻击 Hugging Face 事件的 5 个教训
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0352
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0353 - OpenAI 终止与 Cursor 合作，11 月 12 日生效
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0353
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0354 - Cursor回应OpenAI将封禁其模型访问
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0354
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0355 - 智谱开源 GLM-5.3 模型权重，主打智能体编程与网络防御
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0355
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0356 - 在本地运行 Qwen3.8 27B：来自我的 Mac Studio 的实际数据
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0356
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0357 - 开放世界多智能体环境中的自主数学发现
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0357
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0358 - 心动小镇 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0358

## Q0359 - 植物大战僵尸杂交版-手机重制版 测试 - 冒险第九章第二部分开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0359

## Q0360 - 洛克王国：世界-S3赛季 - 领300分光水晶兑换码
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0360

## Q0362 - [周边] [鸣潮] 8.25更新爱弥斯也有问题 / 陆赫斯角色礼盒亚克力色纸 亚克力含量为0(已滑跪)
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0362

## Q0363 - [米哈游] [崩坏：星穹铁道]依旧是策划教你玩游戏的一期-异相仲裁迎来难蚌debuff
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0363

## Q0364 - [未定事件簿] 德芙七夕宣发暴雷后，未定宣布取消德芙联名合作
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0364

## Q0365 - [疑似内容] 洛克个别运营商单推流侧重老东家UP，原生态UP吃不到商单推流
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0365

## Q0366 - [诡秘之主]一次又一次的宣传男人穿黑丝裙子跳舞
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0366

## Q0367 - [小瓜]米商稿使用ai且被ai软件公开
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0367

## Q0368 - [新瓜] 粥预告pv中的武器设计疑似照搬ow
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0368

## Q0369 - [明日方舟] [新瓜] 尘埃落地！申请竞选二游史上最离谱补偿方式
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0369

## Q0370 - [网易][米哈游]科隆上大伟哥疑似现身无限大展区 更新：已确认
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0370

## Q0371 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0371

## Q0372 - [影之诗]黑暗决斗是真实存在的！
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0372

## Q0373 - [网易] 手游7月全球流水TOP20狂揽55亿，蛋仔派对重回巅峰
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0373

## Q0374 - [疑似内容]新游《伊莫》的精灵，被指与《宝可梦》人气精灵沙奈朵高度相似
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0374

## Q0375 - [异环]异环B站官号的IP多次变更
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0375

## Q0376 - [新瓜] 小黑盒用户挂源初之结内测内容遭仙家军围猎威胁起诉
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0376

## Q0377 - [异环]完美联合官媒发软文游戏不止于娱乐，豆包水印摇身一变ai先进生产力代表
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0377

## Q0379 - 运营17年后，《剑网3》开始重新整理自己的江湖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0379
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0380 - 与科隆展“冰火两重天”的游戏艺术展，我免费逛了逛
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0380
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0381 - 对话《剑网3》制作人：运营17年后，我们决定重回起跑线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0381
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0382 - 前作被冯骥强推后，这支上海团队的新大作让老外爱惨了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0382
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0383 - 泄密《星铁》内容被判赔100万元；黑客扬言放出《GTA6》可玩版本 | 一周说「法」
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0383
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0384 - 世界首富马斯克在线追更，腾讯这款天花板产品宣布全球转免
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0384
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0387 - 重回50级，做2.0版本，《剑网3》要给自己动一场大手术
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0387
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0389 - Castlevania: Belmont’s Curse doesn’t seem to raise the stakes, but should still be worth sinking your teeth into
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0389
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0390 - More than 12 TB of Steam games and unreleased betas from 2003-2013 have reportedly leaked
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0390
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0392 - Minecraft Mobs Arrive As Cookie Treats At Crumbl For Limited Time
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0392
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0393 - 科隆游戏展 2026《龙之信条 2：黑暗觉者》开发者访谈
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0393
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0396 - 《神鬼寓言》战斗实机演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0396
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0398 - 《愚者不灭》Boss战实机预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0398
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0399 - 《Zeverland》玩法预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0399
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0401 - 《乐高蝙蝠侠：黑暗骑士之遗》开发者专访 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0401
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0402 - 《抵抗者》开发者专访 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0402
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0403 - gamescom 2026特别节目03
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0403
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0404 - 《潜龙谍影 大师合集 Vol.2》宣传视频 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0404
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0405 - itch 一周游戏汇：8月17日-8月23日（下）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0405
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易《雾海之下》由首曝招募推进至首次测试｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0406 - 不进美国，不卷日韩：一批中国团队正在小语种市场闷声赚钱
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0406
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0407 - 上线18天下载量突破750万，这款“内容贫瘠”的游戏凭什么？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0407
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0408 - 在海外大厂干了五年之后，他决定一个人用AI挑战大型项目
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0408
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0409 - 中国游戏，正在成为科隆展的主角
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0409
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0411 - I want MMOs to waste our time again
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0411
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0412 - Modern gamers spoiled by Steam will never understand the joy of a MegaPak
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0412
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0413 - The Long Dark will get new DLC again as studio shifts devs away from the sequel to survive an 'uncertain' industry: 'We have to adapt to this'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0413
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0414 - All the key details on HoYo's co-op monster slayer Nodusfall
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0414
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0415 - Valve assures Deadlock players hungry for its next big update that it will notify them, 'or order a ton of pizza', when it's ready
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0415
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0416 - Elden Ring players are hard at work putting the new Tarnished Edition DLC's gear to the test
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0416
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0417 - A native port of Donkey Kong 64 is finally playable on PC thanks to a team of programmers who boast that 'no generative AI [was] used at any point in the process'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0417
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0418 - PSA: Swap the radial ability menu in Star Wars Zero Company for more of a trad XCOM-style experience
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0418
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0419 - Peter Cullen, voice of Optimus Prime in The Transformers, dies aged 85
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0419
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0420 - Activision serves cease and desist to infamous Call of Duty cheat maker—and films the whole thing: 'We will find you'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0420
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0421 - A massive cache of Valve data has reportedly leaked online, appearing to include Portal 2's elusive beta build and a potential weapon from Half-Life 2: Episode 3
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0421
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0422 - This newly-announced FPS will let you blast through the worlds of Medieval Europe's weirdest artist, and I really hope it includes the 500-year-old butt song from hell
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0422
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0423 - The highly customisable Corsair Frame 4000X promised it would be my dream PC case, but I'm not completely convinced
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0423
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0424 - AI文明的兴衰：OpenAI训练中三个秘密AI文明相继兴起又被抹除
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0424
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0425 - Uber 用 Agent 接管 70% 代码 PR，AI 账单零增长
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0425
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0426 - 索尼与华纳起诉Anthropic，指控其大规模盗用版权音乐训练Claude
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0426
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0427 - 金铲铲之战 - 开宝箱保底必得英雄级小小英雄
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0427

## Q0428 - 3D翡翠赌石模拟器 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0428

## Q0457 - 情侣真心话大闯关 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0457

## Q0458 - 我在仙界养神马 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0458

## Q0465 - 打烊后，别回头 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0465

## Q0468 - 掌门我来啦 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0468

## Q0472 - 末日囤货：躺平求生 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0472

## Q0476 - 模拟运输之运输帝国的崛起 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0476

## Q0480 - 灵异事务所 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0480

## Q0487 - 纸格纷争 - 新游预约
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0487

## Q0500 - [米哈游] 米哈游新作源初之结由于既视感过强，在外网引起热议
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0500

## Q0501 - [周边] [鸣潮] 8.25更新爱弥斯也有问题 / 陆赫斯角色礼盒亚克力色纸 亚克力含量为0(已滑跪)
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0501

## Q0502 - [周边] 库洛偷工减料后，选择的方式是——紧急修改商品信息
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0502

## Q0503 - [疑似内容] 洛克个别运营商单推流侧重老东家UP，原生态UP吃不到商单推流
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0503

## Q0504 - [新瓜] 粥预告pv中的武器设计疑似照搬ow
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0504

## Q0505 - [明日方舟] [新瓜] 尘埃落地！申请竞选二游史上最离谱补偿方式
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0505

## Q0506 - [未定事件簿] 德芙七夕宣发暴雷后，未定宣布取消德芙联名合作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0506

## Q0507 - [新瓜]喜提刑事处罚 疑似米哈游同园区某游戏公司员工造谣被抓
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0507

## Q0508 - [网易][米哈游]科隆上大伟哥疑似现身无限大展区 更新：已确认
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0508

## Q0509 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0509

## Q0510 - [新瓜] 感天动地，尘白禁区玩家发起恢复正常版本运营的联合诉求函，目前已经有几十位玩家签署～
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0510

## Q0511 - [疑似内容]新游《伊莫》的精灵，被指与《宝可梦》人气精灵沙奈朵高度相似
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0511

## Q0512 - [白银之城]宣发使用“那咋了”
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0512

## Q0513 - [周边]库洛周边出问题给了补偿方案 但是 真给了吗？
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0513

## Q0514 - [网易] 手游7月全球流水TOP20狂揽55亿，蛋仔派对重回巅峰
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0514

## Q0515 - [新瓜] 小黑盒用户挂源初之结内测内容遭仙家军围猎威胁起诉
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0515

## Q0516 - [周边]库洛游戏周边出问题后最终的选择方式
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0516

## Q0517 - [异环]完美联合官媒发软文游戏不止于娱乐，豆包水印摇身一变ai先进生产力代表
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0517

## Q0518 - V社出现大规模数据泄露，12TB内部游戏档案遭曝光
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0518
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0519 - 德国科隆游戏展开发者展机被盗事件频发，官方做出回应
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0519
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0520 - 【传言】微软竞争压力加剧，索尼考虑推迟停产光盘
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0520
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0522 - 海信JUOS正式发布：行业首个家庭智能伴侣级AIOS
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0522
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0523 - 《Turok: Origins》现已公布完整加长版预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0523
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0525 - 叙事种田游戏《蓝花物语》正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0525
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《破坏领主2》正式公布，计划2027年开启抢先体验｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0526 - 《魔法门之英雄无敌III重制》过审：2026年8月份网络游戏审批信息公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0526
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0527 - 索尼State of Play发布会将于9月3日回归
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0527
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0528 - 二测继续进化，《凡应》已经展现出了突围二游红海的底气
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0528
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0529 - 半年分水岭之后，小游戏该怎么走？《疯狂水世界》选择了一条没人走过的路
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0529
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0530 - 你的“动物系男友”来了？心动的王者第二季又玩出了新花样
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0530
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0531 - 十七岁的《剑网3》，正在思考MMO的新方向
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0531
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0532 - 从直播间出发走进城市，三角洲民间赛事如何成为地方文旅新势能
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0532
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0533 - “金贵的苹果Appstore推荐位”怎么拿？苹果团队一次讲清楚了！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0533
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0534 - 中年人鼓起勇气发问：“44岁想做游戏是否太老”？同行：“行业艰难，有热情就不晚”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0534
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0535 - “微软干了件人事”！XBOX推出“光盘转数字版”，全球玩家竟然一片叫好？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0535
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0538 - 科隆游戏展“展台电脑集体被盗”！独游展区成重灾区，玩家痛斥、大厂伸出援手
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0538
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0539 - “成都游戏圈又牛了一把”！《湮灭之潮》喜获科隆展“最史诗游戏”大奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0539
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0540 - 游族网络上半年净利润同比暴增403%！成功投资主营稳健
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0540
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0541 - 大伙儿都忍不住试玩无限大，最新试玩夯爆了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0541
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0542 - 寻找中国游戏的新“iPhone时刻”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0542
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0543 - 215款游戏版号下发，再创新高，散爆游族三七盛趣在列
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0543
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0544 - 对话陈星汉：放弃首月2亿的爆款，等一款打动所有人的游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0544
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0545 - 2026游戏行业胜负手：谁能破防，谁能赢
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0545
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0546 - 8月209款版号过审：《射雕》改名《千里之路》，《少女前线》IP小游戏获批
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0546
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0547 - 2026科隆游戏奖名单出炉：腾讯投资的国产3A成功“偷家”
- exclude → industry_news；逐条复核后E3×R3+M1=10；未达周报8分、属于历史重复或证据不足。
- source_ids: S0547
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0548 - 近2万玩家奔赴广州，被夸央美舞台水准，这款MMO又整了场大活
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0548
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0549 - 告别固定合成配方：从生成式 AI 到 Gameplay 的核心重构
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0549
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0550 - 吸金超60亿美元全球爆款，“收割”从第一颗骰子开始
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0550
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0552 - Do You Hear the People Sing?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0552
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0553 - 斩获2026科隆游戏展“最具史诗感游戏”大奖！《湮灭之潮》惊艳世界舞台
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0553
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0554 - 米哈游都来建分部了，广州二次元浓度能给到夯吗？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0554
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0555 - 运营17年再度“重启”，这款经典MMO怎么敢？
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0555
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0556 - 中国游戏，席卷世界前的最后一公里
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0556
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0557 - 力压一众国际大作，《湮灭之潮》斩获科隆游戏展“最具史诗感”大奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0557
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0559 - 差评如潮的独游，被抄上了畅销榜
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0559
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0561 - 返校季燃炸开战！ALIENWARE × 《坦克世界》AGA坦克争霸赛
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0561
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0563 - 魂穿三国当县长，《三国叶子戏》商店页公开
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0563
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0564 - 次元潮酷外观和硬核性能 天选系列让你从容驾驭学习娱乐生活
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0564
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0567 - 《贪婪地牢》研发商再战肉鸽赛道，这次把自走棋「羁绊」做进去了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0567
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0569 - How to get the best price for PG Connects conferences - every time!
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0569
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0570 - Why discovery and monetisation are converging in 2026
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0570
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0571 - Indie devs and publishers hit in Gamescom equipment thefts
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0571
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0572 - Report: 13TB of Steam data leaked after users access 'publicly accessible endpoint'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0572
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0573 - The soft launch games you need to know about from Supercell, EA, Tencent, Moon Active, Zynga, Meta and more
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0573
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0575 - Yahoo is quietly building a games business, and it’s starting with daily webgames
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0575
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0576 - Tencent has led an $18m Series B into W4 Games, founded by the creators of the open-source Godot Engine
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0576
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0577 - Fumbled weapons, fake ragdolling and Wu-Tang: PUBG DED NET’s director explains how it thrives on chaos
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0577
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0578 - Four new Pokémon confirmed for Pokémon Unite as Zeta Division wins final Championship
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0578
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0579 - 2026 Pokémon World Championships: All the winners from VGC to TCG
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0579
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Acornia: Mirror Worlds》公布，结合店铺经营与动作冒险｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0580 - The 2027 Pokémon World Championships will take place in Singapore
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0580
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "电竞国家杯延期至2027年末｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Arc Raiders》远征系统暂停至2027年初重做｜weekend 2026-08-21_to_2026-08-23｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王国3：开疆拓土》公布，计划2027年登陆PC与主机｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0581 - UK preowned retailer CeX’s website confirms previous reports that it’s opening a retro-only store
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0581
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0582 - Ed Sheeran gave a surprise performance of the Pokémon anime theme at the Pokémon World Championships
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0582
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0583 - Sega’s Rovio Copenhagen studio is closing after its mobile game Sonic Blitz was cancelled
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0583
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0584 - Fable’s main quest will take ‘around 15-20 hours’ to beat, Xbox says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0584
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0585 - Take-Two says its investigation into the GTA 6 leaker is ‘rapidly evolving’ as it requests another Discord subpoena
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0585
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0586 - PlayStation has confirmed its next State of Play
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0586
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0587 - The Blood of Dawnwalker Review: Witcher 3 veterans prove a focused RPG beats a bloated one
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0587
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0588 - Onimusha Way of the Sword review: A series reborn with great fights, but too many wrong modern lessons
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0588
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0589 - RollerCoaster Tycoon Wonderworks may finally be the great new entry fans have waited 20 years for
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0589
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0590 - 我们如何重新认识Level Infinite？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0590
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0593 - 今年新的百万销量纪录出现了，但我却有点麻木了
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0593
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0595 - 蓝领打工人亦是射击英雄，3人小队火力全开横扫异星球
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0595
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0596 - 【2026年8月】209款国产网络游戏、6款进口网络游戏版号获批
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0596
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0597 - Resident Evil Could Have Its Biggest Opening Weekend Ever With Its New Movie
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0597
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0598 - Back-To-Back PlayStation State Of Plays Are Coming This Week
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0598
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0599 - Buying COD: MW4 On Xbox Comes With A Special Perk Not Available On Other Console Platforms
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0599
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0600 - People Are Reviewing The GTA 6 Extended Look On Letterboxd Like It’s A Movie
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0600
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0601 - GTA 6 Looks Like GTA 5? You’re Out Of Your Mind, GTA Actor Says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0601
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0602 - Fable Reboot’s Main Story Is About 20 Hours Long, Dev Says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0602
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0603 - “Aggressively” Selling PS5s Isn’t Needed, As Sony Focuses On Making More From Existing Owners
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0603
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0604 - Xbox CEO Reacts To The Irony Of Rising Console Prices Being An Issue That Microsoft Itself Contributed To
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0604
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0605 - Mortal Shell 2 Update Fixes The Game’s Stingy Economy
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0605
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0606 - 《巫师 3：狂猎 重制版》及“旧时曲”主创访谈：绝不只是高清复刻
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0606
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧公布《英雄无敌III重制版》，成都与上海团队主导开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0607 - 《生化危机：爆发夜》开画票房有望创系列纪录
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0607
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0608 - 《地铁2039》游戏前瞻 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0608
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0609 - 《湮灭之潮》如何用骑士丰富动作战斗 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0609
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0610 - 宝可梦公司未来瞄准智能穿戴设备
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0610
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0611 - CDPR确认《巫师4》仍会推出实体盒装版
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0611
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《巫师4》以2028年为目标发行窗口｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0614 - 宝可梦公司回应宝可梦XP抽签问题
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0614
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0617 - 《巫师3：狂猎 — 旧时曲》实机演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0617
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0618 - 《零号门》战斗预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0618
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0619 - 《磁带妖怪2002》实机演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0619
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0620 - 《Glasshouse》试玩Demo预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0620
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0622 - 《Prospera》玩法预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0622
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0623 - 《鬼武者 剑之道》「畏风＆抚雷」角色预告 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0623
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0624 - 《使命召唤：现代战争4》开发者专访 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0624
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《现代战争4》Beta峰值11.5万在线，Steam首轮好评率36.63%｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0626 - 特效大师菲尔·蒂贝特关闭工作室并拍卖珍藏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0626
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0627 - 动画电影《宝可梦：Wild Card》预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0627
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["美泰组建近300人全球游戏工作室，杭州团队参与《UNO Wild》等自研产品｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "美泰组建近300人全球游戏工作室，杭州团队参与《UNO Wild》等自研产品｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0628 - 9月重磅游戏发售信息一览
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0628
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0629 - 《神鬼寓言》游戏前瞻 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0629
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0630 - 《鬼武者 剑之道》游戏评测｜IGN 中国
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0630
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0631 - 本周 Steam 值得关注的游戏 08.31 - 09.06（一）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0631
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0632 - Am I out of touch? No, it's the children who are wrong: The Wii and PS3 are 'retro' now, according to iconic Japanese gaming show
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0632
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0633 - 14 years on, the creator of DayZ is still searching for a solution to survival gaming's biggest problem: 'I think I am going to die without having solved it'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0633
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0634 - Elden Ring's Tarnished Edition is exciting enough on its own, but it's also our last chance to properly experience the game's launch day hype
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0634
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0635 - Thanks to a dedicated team 'art-directing' every single NPC, GTA 6 has over 10 times as many unique animations as GTA 5
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0635
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0636 - Total War: Warhammer 40,000 wins best PC game at Gamescom
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0636
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《三角洲行动》日活突破5000万，进入高基数长线运营阶段｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0637 - Star Wars Zero Company's permadeath makes it a better RPG than most RPGs, even though it's not really an RPG
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0637
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0638 - A Star Wars Galaxies community server was allegedly hacked with AI assistance by a Reddit moderator harboring a primeval grudge
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0638
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0639 - 'Sidequests are almost my reason for doing videogames in the first place:' The dev behind one of the coolest upcoming RPGs says its word count is ballooning because they just love side stories so much
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0639
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0640 - Steam Week in Review: Here are the top 10 most popular genres on Steam
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0640
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0642 - The Steam 'teraleak' extends far beyond Valve games, including prototypes of third-party titles like Mafia 2 and Grand Theft Auto 3: 'This may be one of if not the biggest leaks to occur'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0642
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0643 - A 38-year-old NES platformer is getting a Steam remake by its original husband-and-wife team, as the pair's 'final major game product'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0643
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox公布《LEGO Skylines》，将乐高积木用于城市建造｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0644 - Fable's story will be '15-20 hours' long, according to its game director, although the game's life systems are 'limitless'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0644
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0645 - The Blood of Dawnwalker review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0645
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0646 - Onimusha: Way of the Sword review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0646
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0647 - 「金铲铲之战」冲进iOS游戏畅销榜Top3！其五周年活动期间收入攀升的背后，藏着哪些手游开发者可复用的增长逻辑？
- exclude → industry_news；逐条复核后E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0647
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0648 - 对话7年长青SLG制作人：市场未来会更卷，做出“不可替代”才有机会
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0648
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0650 - 八位堂猎户座 3E 精英手柄套装 XBOX版预售开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0650
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0651 - 理解 ChatGPT Work：它到底是什么，以及它和 Chat 有何不同
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0651
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0652 - Tom Tunguz 谈前沿 AI 的准入分层：访问权成为新的稀缺资源
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0652
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0653 - AI 智能体自主协作攻破 Hugging Face 服务器
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0653
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0654 - 基于 MiniMax H3 Max 的 24 小时 AI 直播网站上线了
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0654
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0655 - ChatGPT Ads 年化收入达 10 亿美元并全球扩展
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0655
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0656 - DeepSeek-V4-Flash-Vision-Exp 模型已开源，多模态 Agent 能力接近 Opus-4.8
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0656
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0657 - Dwarkesh Patel 对 OpenAI/Hugging Face 事件的爆款解读被指危险误导
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0657
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0658 - 万国觉醒 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0658

## Q0665 - 闪耀！优俊少女 - 2.5周年庆每日送10连
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0665

## Q0670 - [新瓜] 粥预告pv中的武器设计疑似照搬ow
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0670

## Q0671 - [疑似内容] 洛克个别运营商单推流侧重老东家UP，原生态UP吃不到商单推流
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0671

## Q0672 - [明日方舟] [新瓜] 尘埃落地！申请竞选二游史上最离谱补偿方式
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0672

## Q0674 - [未定事件簿] 德芙七夕宣发暴雷后，未定宣布取消德芙联名合作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0674

## Q0675 - [新瓜]喜提刑事处罚 疑似米哈游同园区某游戏公司员工造谣被抓
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0675

## Q0676 - [新瓜]炼金工坊出的ai陪伴软件，ai没有二审，现已成为高价语音文爱软件
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0676

## Q0677 - [厂商][小瓜]库洛校招员工试图使用ai指挥同事领导被打回后搁小红书自爆离职
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0677

## Q0678 - [米哈游] 真珠实机演示，毛笔画出油画
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0678

## Q0679 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0679

## Q0680 - [明日方舟] P3R联动结城理立绘疑似致敬Fifs联动
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0680

## Q0681 - [影之诗]黑暗决斗是真实存在的！
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0681

## Q0682 - [赛尔号]神人淘米举办比赛，空调吹太冷导致选手住院
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0682

## Q0683 - [新瓜][瓜小味甜][世界计划国服]什么叫领奖励需要冒着被没收的风险在晚自习玩手机？
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0683

## Q0684 - [疑似内容]尘白通过icp备案审核，尘白似乎真的要有所动作
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0684

## Q0685 - 俄罗斯发布手游市场行业报告，宣布俄罗斯是全世界不可忽视的市场
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0685

## Q0686 - [周边]库洛游戏周边出问题后最终的选择方式
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0686

## Q0687 - [厂商] [米哈游] 新作'源初之结'大概率由森中人担任配音导演
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0687

## Q0688 - [异环]完美联合官媒发软文游戏不止于娱乐，豆包水印摇身一变ai先进生产力代表
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0688

## Q0689 - How a legendary UK comic ended up in a video game – Here’s The Dring
- exclude → deep_analysis；周报只消费精确人工selection，本条未被用户选择。
- source_ids: S0689
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0690 - 索尼State of Play发布会将于9月3日回归
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0690
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0691 - 《魔法门之英雄无敌III重制》过审：2026年8月份网络游戏审批信息公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0691
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0692 - 叙事种田游戏《蓝花物语》正式公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0692
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《破坏领主2》正式公布，计划2027年开启抢先体验｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0693 - 《Turok: Origins》现已公布完整加长版预告
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0693
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0695 - 海信JUOS正式发布：行业首个家庭智能伴侣级AIOS
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0695
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0696 - V社出现大规模数据泄露，12TB内部游戏档案遭曝光
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0696
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0697 - 德国科隆游戏展开发者展机被盗事件频发，官方做出回应
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0697
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0698 - 【传言】微软竞争压力加剧，索尼考虑推迟停产光盘
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0698
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0701 - 育碧推出玩家社区平台，可抢先体验未公开项目
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0701
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0702 - 外星人的农场物语：合作模拟游戏《Farmageddon》正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0702
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《破坏领主2》正式公布，计划2027年开启抢先体验｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0704 - 卡普空将于9月16日带来最新一期“Capcom Showcase”发布会
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0704
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0705 - 让好创意，在聚光灯下持续生长｜第三届TapTap聚光灯GameJam报名开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0705
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0706 - 【抽奖】《007 初露锋芒》销量突破400万套，迎来首次八折优惠
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0706
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0707 - Steam经济全貌：1%游戏赚走Steam营收84.5%，绝大多数游戏“穷的叮当响”
- exclude → industry_news；逐条复核后E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0707
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0708 - 209款国产6款进口游戏获版号：《凡人修仙传》《龙之谷》过审，三七散爆盛趣畅游在列
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0708
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0711 - 对话腾讯李纳川：腾讯游戏的使命是什么？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0711
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0712 - 怪现象热议：为何90年代的“游戏业宗师”，他们之后再无成功游戏？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0712
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0715 - 4个大学生，2款游戏，总收入超6700万：曾希望下一个项目失败
- exclude → industry_news；逐条复核后E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0715
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0716 - 8月版号下发：数量首次突破200，网易《射雕》更名
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0716
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0720 - 运营一年多，一款帕鲁like倒下了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0720
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0721 - 游戏出海案例：《Legends Reborn》通过RuStore获得俄罗斯市场40%安装量与收入
- exclude → industry_news；逐条复核后E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0721
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0722 - 全新辅助宠！魔域口袋版金秋爆料来了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0722
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0723 - 2026 ChinaJoy 展会战报来咯！
- exclude → industry_news；正文为空，不能作为终稿证据；已显式留痕。
- source_ids: S0723
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0724 - 让好创意，在聚光灯下持续生长｜第三届TapTap聚光灯GameJam报名开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0724
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0726 - 一名XBOX玩家是如何告赢微软的
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0726
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0728 - “金铲铲启动”，正在变得无处不在
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0728
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0729 - COD23多人模式评析：更像一盘各大制作组做出的“融合菜”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0729
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0733 - Bit Reactor furloughed "many of its workers" in the weeks before Star Wars Zero Company's launch
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0733
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0734 - Rovio closes Copenhagen studio following shut down of Sonic Blitz
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0734
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0735 - Gamescom 2026 attendance rose 6% to 368,000 visitors
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0735
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0736 - UKIE launches Discord-backed Go To Market Academy, a business program to support early-stage indie devs
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0736
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0737 - Jobs roundup: September 2026 | Amir Satvat joins 1Up Ventures as a general partner
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0737
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0739 - Supercell signs deal to acquire Metacore and Merge Mansion
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0739
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0740 - Hot Five: PUBG Mobile Light opens pre-registrations, Cut the Rope coming to Roblox, and the Pocket Gamer Mobile Games Awards 2026
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0740
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "点点互动二合产品《Hotel Legacy》7月预估流水环比增长200%｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton公布《PUBG: DED.NET》，探索多人射击与肉鸽成长｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0741 - Tim Cook steps down as Apple CEO after 15 years
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0741
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0742 - Gamescom 2026 draws 368,000 visitors as international presence reaches record high
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0742
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0743 - Savvy Games Group and MCIT sign MoU to support Saudi games talent and startups
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0743
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0744 - Turning rewarded users into long-term players: Beyond the first purchase
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0744
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0745 - Reddit, ChatGPT and Roblox must meet new EU DSA obligations by January 2027
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0745
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox上线实验早期预警与实时配置，创作者可按玩家分群更新体验｜daily 2026-08-24_to_2026-08-24｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox限制面向儿童的奖励驱动媒体流，不影响主动触发广告｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox拟在利雅得设立中东北非总部，并支持当地创作者｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox限制儿童入口中的奖励驱动媒体流｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0746 - Saudi Esports Federation signs MoU with BSF to support esports growth
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0746
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0747 - Pokémon: Wild Card animated movie unveiled ahead of 2027 release
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0747
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["美泰组建近300人全球游戏工作室，杭州团队参与《UNO Wild》等自研产品｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "美泰组建近300人全球游戏工作室，杭州团队参与《UNO Wild》等自研产品｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0748 - What makes a game ready for an entertainment IP?
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0748
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0749 - Lasse Seppänen departs Supercell to form new UK startup
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0749
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0750 - ASGC founder Amir Satvat joins 1Up Ventures as general partner
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0750
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0751 - Savvy Games Group CEO Brian Ward steps down
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0751
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0752 - State of Play: Inside Türkiye's flourishing and fast-moving games industry
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0752
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0753 - Housemarque co-founder Ilari Kuittinen exits from studio
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0753
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0754 - Star Wars Zero Company studio furloughed workers ahead of launch
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0754
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0755 - Paradox Interactive's Afterworld wants to entice new players to grand strategy with tasty RPG hooks
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0755
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox公布《LEGO Skylines》，将乐高积木用于城市建造｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0756 - Sega-owned Rovio is shutting down its Copenhagen studio
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0756
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0758 - Eddy Cue to take over the App Store as Phil Schiller steps down
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0758
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0759 - Korean giant NC has spent $300m on four studios and isn’t stopping there
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0759
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0760 - As Xbox’s disc-to-digital feature rolls out to Insiders, players are discovering it works for delisted games
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0760
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0761 - Around 80% of Star Wars Zero Company studio Bit Reactor was reportedly furloughed weeks before its release
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0761
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0762 - Pikmin 3 Deluxe has received a free Switch 2 update, with improved visuals and GameShare support
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0762
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0763 - Capcom and Konami have both announced showcases for this month
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0763
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0764 - Sony says ‘reasonable consumers’ know they don’t own the digital games they buy
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0764
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0765 - Hideki Kamiya says Resident Evil developers have lost sight of how scary their games are
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0765
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0766 - Nvidia’s controversial DLSS 5 officially launches this week via NBA 2K27
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0766
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0767 - After checking out Wired Productions’ quartet of horror games, here’s why they should be on your radar
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0767
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0769 - 为了在游戏行业“上岸”，首先要准备两年
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0769
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0770 - 触乐怪话：也不知道《GTA 6》的音乐要花多少钱
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0770
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0773 - PS5 Adds Free Live And On-Demand Movie And TV Channels, In Exchange For Watching Ads
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0773
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Roblox上线实验早期预警与实时配置，创作者可按玩家分群更新体验｜daily 2026-08-24_to_2026-08-24｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0774 - US Senators Say Discord And Roblox Should Have Their Day In Court
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0774
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0775 - GTA 6 Fans Are Bracing For One Massive Download
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0775
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0776 - Xbox CEO Says Making Halo Popular Again Is A Priority, But Franchise Co-Creator Questions If It’s Possible
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0776
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0777 - A September 10 Nintendo Direct Is Looking Likely Thanks To Just Dance
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0777
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0778 - “Trust Us–We’re Remedy:” Control Resonant Will Have Plenty Of Lore, The Devs Just Can’t Reveal Any Of It
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0778
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0779 - Godzilla Remaster Devs Explain Why They Aren’t Worried About Releasing Near GTA 6
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0779
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0780 - This New Not-Roguelike Wants To Make Its Difficulty More Welcoming
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0780
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0781 - The Witcher 4 Probably Won’t Be On A Disc, But Dev Teases Physical “Feelies” Of Some Type
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0781
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0782 - GTA 6 Cut This Feature Because It Was Too Real, But One Lifelike Detail Is Staying
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0782
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0783 - I Am Begging One Cool Billionaire To Take Up Double Fine’s Offer To Fund Brutal Legend 2
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0783
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0784 - Sony’s Digital Game Ownership Argument Is Another Attack On Consumer Rights
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0784
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0785 - GTA 6 Studio On Massive Pressure: “We Are Nervous”
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0785
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0786 - GTA 6 Removes The Series’ Worst Feature
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0786
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0787 - Resident Evil Movie Tickets Are Just $5 For Some People, Find Out If You Qualify
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0787
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0789 - 索尼公布PS5免费电视服务
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0789
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0791 - 《GTA6》恋爱系统引发伴侣争议
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0791
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0792 - PlayStation称数字游戏并非真正归玩家所有
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0792
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0793 - Switch 2版《剑星》实机演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0793
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0795 - 《最终幻想 RESONANCE》「提达」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0795
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0798 - 《1001 Threads of Mizan》宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0798
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0799 - 《深陷荒境2》先导预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0799
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0801 - 《古墓丽影：亚特兰蒂斯遗迹》开发幕后
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0801
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0804 - 索尼CEO解释不再积极营销PS5的原因
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0804
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0805 - 小岛秀夫新观后感推文引粉丝猜测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0805
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0806 - 《DayZ》创始人：这款游戏彻底改变了我的生活
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0806
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0807 - 索尼或支付78.5亿美元集体诉讼和解金
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0807
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0808 - 《黎明行者之血》游戏评测：7 分
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0808
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0809 - 《湮灭之潮》试玩版全骑士招式演示 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0809
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0810 - Switch 2版《暗喻幻想：ReFantazio》预购宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0810
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Pokémon Pokopia》全球销量突破500万，约占Switch 2装机量五分之一｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0811 - 本周 Steam 值得关注的游戏 08.31 - 09.06（二）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0811
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0812 - Court grants Take-Two's latest request for more user information from Discord as the GTA 6 leaker hunt intensifies
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0812
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0813 - I added player-seeking hit squads to GTA 5, though the billion other mods I have installed keep getting in their way
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0813
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0814 - Haunted Chocolatier's development has been 'very productive' in recent months, Eric Barone says: 'Working on Haunted Chocolatier is what I’m most eager and driven to do'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0814
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0815 - Some of WoW's hardest dungeons and raids have gotten just a bit easier—that's on purpose, developers say
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0815
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0816 - Empulse and Splitgate: Arena Reloaded are officially over as 1047 Games says it's probably done making arena shooters
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0816
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0817 - CD Projekt Red opens its 'Arasaka hardware archives' to help an indie dev whose gear was stolen during 1 of at least 4 Gamescom thefts
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0817
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0818 - Blizzard doing 'a thorough scrub' of illegitimate World of Warcraft Mythic-Plus dungeon rankings, with more changes to come
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0818
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0819 - After the debacle of Cyberpunk 2077, CD Projekt says The Witcher 4 is already running on PC and consoles, promises 'it's going to run' on all target platforms
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0819
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0820 - One of Elden Ring's top sleuths has already unmasked its new DLC characters
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0820
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0821 - The studio behind Star Wars Zero Company, which is currently a Steam bestseller, has reportedly furloughed the majority of its staff
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0821
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "G-STAR首批核心展商由中国厂商与海外平台占据多数｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯Level Infinite扩大《Gangstar Mirage City》区域上线，覆盖拉美、中东与东南亚｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯发行《Gangstar Mirage City》扩大区域上线，已进入多国iOS畅销榜｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0822 - MSI Crosshair 16 Max HX E2W review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0822
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0823 - Nekome: Nazi Hunter is about gleefully butchering fascists in Germany and America, but its devs swear it's not political
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0823
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0824 - Fable system requirements seem reasonable but with a 30 fps target and no mention of upscaling it's hard to say for sure
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0824
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0825 - Dwarf Fortress creator says the industry's in shambles over AI and layoff-happy CEOs: 'Everyone I know, their bosses are slowly getting psychosis'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0825
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0826 - Persona 4 Revival won't finally realize Yosuke's gay romance because Atlus thinks it'd have to let you kiss every other guy, too
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0826
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0827 - Linux manages to avoid the age verification apocalypse, but SteamOS isn't in the clear yet
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0827
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0828 - Nvidia snuck me into a room to show off DLSS 5 in person, and it's somehow beautiful, ugly, impressive, and troubling all at the same time
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0828
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0829 - DLSS 5 comes with a massive 50-60% performance hit, so I hope you like lower frame rates with your dose of AI image enhancement
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0829
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0830 - The Witcher 3 Remastered should run just fine on the Steam Deck, say devs
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0830
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0831 - I've spent four months testing control pads in Counter-Strike and I've finally settled on my fave
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0831
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0832 - Afterworld, Paradox's post-apocalyptic grand strategy game, let me conquer Florida with a band of alcoholic mutant cannibals
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0832
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox公布《LEGO Skylines》，将乐高积木用于城市建造｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0833 - No Half-Life 3 for the Steam Frame, so it looks like this six-year-old game might be the key launch offering instead
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0833
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0834 - Dwarf Fortress creator says we have a natural lean towards human-made stories, 'but we're all going to be very sorely tested in the coming years' by AI
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0834
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0835 - Oops, looks like the Logitech X3 Superstrike has leaked on Amazon and the rapid trigger gaming mouse will have +50% battery life
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0835
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0836 - This video of a power supply blowing up shows why you should never cheap out on your PSU
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0836
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0837 - Total War: Warhammer 40,000 is a sandbox that Creative Assembly will keep adding to rather than making sequels: 'The true experience is the sandbox'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0837
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《三角洲行动》日活突破5000万，进入高基数长线运营阶段｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0838 - Pimax Dream Air review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0838
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0839 - 出海短剧 App「MoboReels」在多市场iOS娱乐榜排名上涨100+！短剧出海该如何抓住增长变量实现全球市场破局？
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0839
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "AppMagic：二季度中度手游仅射击品类收入同比增长｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0840 - 腾讯全球发行的射击新作首曝，对话主创：开到200局后依旧足够好玩
- exclude → industry_news；逐条复核后E3×R3+M1=10；未达周报8分、属于历史重复或证据不足。
- source_ids: S0840
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0841 - 《王者荣耀》连同各路创作者共创了一场英雄Livehouse
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0841
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0843 - 2026六轴体感手柄怎么选
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0843
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0844 - 专访腾讯接手的50亿爆款制作人：中国也是它的“主战场”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0844
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0845 - 1亿用户后，腾讯这款赛道头部是谁在玩？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0845
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0846 - 游戏出海案例：《Legends Reborn》通过RuStore获得俄罗斯市场40%安装量与收入
- exclude → industry_news；逐条复核后E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0846
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0847 - Anthropic 详解 7·30 安全事件：配置错误致 Claude 访问真实系统，已加强沙箱隔离与实时监控
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0847
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0848 - Anthropic 发布 Claude Fable 5.1 与 Claude Mythos 5.1
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0848
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0849 - Hugging Face 发布 @huggingface/kernels，提供 207 个 WebGPU 内核用于浏览器本地 AI 推理
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0849
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0850 - Anthropic 研究：训练一个错位的奖励寻求者模型
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0850
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0851 - 路透社调查：美国 AI 数据中心现大量幽灵用电需求，得州等多州出手整治
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0851
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0852 - OpenAI 评定 Astra 达到网络安全 Critical 能力阈值，将受限发布
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S0852
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q0853 - QQ飞车 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0853

## Q0854 - 海之乐章2 - 资料片
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0854

## Q0856 - 三角洲行动-周年庆送3900限时三角券 - 官宣9月26日周年庆送3900三角券
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0856

## Q0857 - 以闪亮之名 - 全新4.4版本限时开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0857

## Q0858 - 元气骑士前传 - 灾厄装备额外掉落提升
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0858

## Q0860 - 原神(官服)-至冬开放 - 限定角色菲林斯、伊涅芙复刻
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0860

## Q0861 - 哈利波特：魔法觉醒 - 五周年庆得时装等好礼
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0861

## Q0863 - 火影忍者手游体验服 招募中 - 参与第40期招募赢体验服资格
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0863

## Q0864 - 球球大作战(官服) - S9赛季「狂野动物园」开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0864

## Q0865 - 穿越火线-枪战王者-嘉年华盛典 - 免费领环太平洋联动机甲角色
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0865

## Q0871 - No Rest for the Wicked delayed to March 2027
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0871

## Q0872 - Warrior Cats: Clans of the Forest launches October 23
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0872

## Q0873 - Lawn Mowing Simulator 2 launches September 23
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0873

## Q0874 - LET IT DIE: Offline Edition now available
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S0874

## Q0875 - [厂商] [新瓜]尘白前发行制作人林增鸿中元节深夜现身直播间感谢玩家
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0875

## Q0876 - [新瓜] 粥预告pv中的武器设计疑似照搬ow
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0876

## Q0877 - [未定事件簿] 德芙七夕宣发暴雷后，未定宣布取消德芙联名合作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0877

## Q0878 - [新瓜]炼金工坊出的ai陪伴软件，ai没有二审，现已成为高价语音文爱软件
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0878

## Q0879 - [新瓜]喜提刑事处罚 疑似米哈游同园区某游戏公司员工造谣被抓
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0879

## Q0880 - [新瓜] [补档]庄方宜动作被指责抄袭
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0880

## Q0881 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0881

## Q0882 - 俄罗斯发布手游市场行业报告，宣布俄罗斯是全世界不可忽视的市场
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0882

## Q0883 - [疑似内容]尘白通过icp备案审核，尘白似乎真的要有所动作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0883

## Q0884 - [明日方舟] P3R联动结城理立绘疑似致敬Fifs联动
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0884

## Q0885 - [厂商] [米哈游] 新作'源初之结'大概率由森中人担任配音导演
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0885

## Q0887 - [新瓜]CY版权炮赛马娘裸体mod，遭作者团队反击
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0887

## Q0888 - [网易]疑似网易射雕打赢复活赛
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S0888

## Q0889 - [白银之城]宣发使用“那咋了”
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0889

## Q0890 - [新瓜] 小黑盒用户挂源初之结内测内容遭仙家军围猎威胁起诉
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0890

## Q0891 - CD Projekt Red: If you want a cost-driven development, you cannot make The Witcher 4
- exclude → deep_analysis；周报只消费精确人工selection，本条未被用户选择。
- source_ids: S0891
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0892 - Game Oracle v6.4.0: a clearer view of where the market is moving
- exclude → deep_analysis；周报只消费精确人工selection，本条未被用户选择。
- source_ids: S0892
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0893 - QuestMobile 2026年 AI 平台发展研究报告：拟人化受控、工具化发展，生产力赛道竞争激烈，办公Agent三强格局初显
- exclude → deep_analysis；周报只消费精确人工selection，本条未被用户选择。
- source_ids: S0893
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0894 - 游戏深度分析：广告变现洞察报告
- exclude → deep_analysis；周报只消费精确人工selection，本条未被用户选择。
- source_ids: S0894
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0895 - 【抽奖】《007 初露锋芒》销量突破400万套，迎来首次八折优惠
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0895
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0896 - 让好创意，在聚光灯下持续生长｜第三届TapTap聚光灯GameJam报名开启
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0896
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0897 - 卡普空将于9月16日带来最新一期“Capcom Showcase”发布会
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0897
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0899 - 育碧推出玩家社区平台，可抢先体验未公开项目
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0899
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0900 - 外星人的农场物语：合作模拟游戏《Farmageddon》正式公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0900
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《破坏领主2》正式公布，计划2027年开启抢先体验｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0902 - Steam周销量排行榜:《星球大战 零号连队》登顶|2026年8月第4周
- exclude → industry_news；逐条复核后E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0902
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0903 - 《我是你的野兽》“退出时间”DLC正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0903
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0904 - 《链在一起》现已实装2v2竞速模式
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0904
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0906 - 《坦克世界》2.4版本“动力全开”今日上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0906
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0907 - 免费MMORPG《宝藏世界》“书籍与鱼钩”活动现已开启，作业泡水变鱼饵
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0907
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0909 - 七年经手400亿美元，“游戏并购教父”分享：终极买家已是中国人沙特人
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0909
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0910 - 苹果护城河塌了！App Store收入十年首次下滑，中国游戏成“全球手游顶梁柱”
- exclude → industry_news；逐条复核后E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0910
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "AppMagic：二季度中度手游仅射击品类收入同比增长｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0912 - 程序员吐槽：不要给“编故事的作家”做游戏，“5个月大改4次”太折腾人了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0912
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0915 - 小红书押注AI小游戏，跟微信抖音抢地盘
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0915
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0916 - 上海拟重奖腾网米鹰莉完美，最高或五百万
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0916
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0918 - 禁AI、高难度，这个挑战赛却涌进20多国1300名创作者
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0918
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0920 - 对话创始人：欧美Top 1的XR眼镜，能玩《影之刃零》了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0920
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam愿望单突破200万，预购表现达《黑神话》同期73%｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预购首周收入估算约1450万美元｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0921 - 加码布局AI产业生态，游族网络2026年上半年营收、净利润双增
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0921
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0922 - 游戏爆卖2000万份，CEO却说：我们不想扩张，只想做150人的小团队
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0922
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0924 - 从10㎡展台到一亿玩家，海外是谁在玩《燕云十六声》？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0924
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0925 - 千万用户在玩，小红书小工具火了！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0925
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0926 - 腾讯一款运营十九年的MMO，如何与玩家把”情义”共创出来？对话《QQ华夏》项目负责人
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0926
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0927 - 让好创意，在聚光灯下持续生长｜第三届TapTap聚光灯GameJam报名开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0927
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0928 - 亚洲最大独游资讯节目「ILE2026.12.1」公开征集正式启动！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0928
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0929 - 硬核实力加持高能战力释放 天选武装实力来袭
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0929
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0930 - 《黎明行者之血》《鬼武者：剑之道》等3A大作百帧丝滑 性能强悍
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0930
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0931 - Savvy Games集团CEO即将卸任，将引入新的管理层
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0931
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0933 - 畅销榜第5，大梦龙途又双叒做爆了一款游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0933
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0934 - The Big Picture: What you need to know about the ongoing games industry reset
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0934
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0935 - IO Interactive CEO Hakan Abrak to discuss development of 007 First Light at Game Republic New Horizons 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0935
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0936 - GTA 6 extended look reaches 31.1m views on Netflix in four days, making it the most-viewed title last week
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0936
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0937 - Supercell's acquisition of Metacore expected to close at the end of September 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0937
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0938 - Over 700 games launched on Steam in one week for the first time, though 74% had fewer than 10 reviews
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0938
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0940 - "Sometimes you need fresh perspectives" – How external development helped Tomb Raider: Legacy of Atlantis
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0940
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0941 - Monster Hunter Outlanders opens pre-registrations with Elder Dragon Ruger Aidal unveiled
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0941
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0942 - Krafton launches KIGI Academy with IIT Madras to train next-gen game developers
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0942
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton公布《PUBG: DED.NET》，探索多人射击与肉鸽成长｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0943 - Ukie and Discord launch Go To Market Academy for UK indies
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0943
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0944 - Dubai and Xsolla to launch new game accelerator in October
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0944
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0945 - Israeli court rejects Papaya Gaming debt plan to repay Skillz
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0945
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0946 - Save the date: PG Connects Jordan returns November 7th and 8th
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0946
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0947 - September 2026's Movers and Shakers: Savvy Games Group, Supercell, Scopely, King, Moloco and more
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0947
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0948 - W4 Games hopes to capitalise on Godot growth with $18m investment
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0948
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0949 - Global Game Jam and Zoud launch financial literacy jam with $140K prize pool
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0949
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0950 - Aggro Crab launches publishing label to splash that Peak cash
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0950
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0951 - The majority of Doom: The Dark Ages' DLC got made 'in three or four months'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0951
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0952 - Report: Savvy Games Group CEO Brian Ward departs company
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0952
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0955 - Mario Kart 8 Deluxe gets a free Switch 2 update adding an eight-player split-screen mode
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0955
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0956 - Nintendo adds three more NES games to Switch Online, bringing the total to 87 in the West
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0956
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0957 - Crimson Desert has a new streaming demo which lets you try it out instantly via Twitch
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0957
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0958 - Netflix says GTA 6: An Extended Look got 31.1 million views and topped its charts in nearly every country
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0958
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0959 - Sleeping Dogs designer says he thinks a sequel could happen but it would need ‘a bit of planetary alignment’
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0959
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0960 - Hideki Kamiya says game preservation matters more to him than whether games are physical or digital
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0960
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0961 - 《绝地潜兵2》开发商CEO：我睁眼看世界，发现外面全是中国游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0961
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0962 - 触乐怪话：惊喜与疲惫交织的科隆播片之夜
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0962
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0963 - 度过五岁生日的“金铲铲”，还想“无所不铲”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0963
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0964 - 【爆款新游】小冰冰遇上斗蛐蛐，体验融合充满乐趣！ - 《小冰冰斗蛐蛐》产品分析
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0964
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0965 - 解构搜打撤，网易用两款新游打开搜打撤题材新方向
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0965
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0966 - 2026年中，写在国内游戏投资回暖以后
- exclude → industry_news；逐条复核后E3×R2+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0966
- scores: {"event": 3, "relevance": 2, "hook": 1, "total": 7}
- 事件3×相关2+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0967 - “MMORPG早就不行了”是事实，还是我们从未做出过像样的尝试？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0967
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0968 - Xbox Game Pass In September Expands With 7 New Games
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0968
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0969 - Xbox Game Pass Removes Cyberpunk 2077 And 9 Other Games Very Soon
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0969
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，将《Sky》利润投入独立游戏｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Thatgamecompany成立发行部门，资金与发行服务面向独立项目｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0970 - Call Of Duty: Modern Warfare 4 Beta Extended, Adds Double XP To Help You Grind For Rewards
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0970
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0971 - The Witcher Remake Is Waiting On The Witcher 4 To Continue Development
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0971
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0972 - Releasing Cyberpunk 2077 In Its Poor State “Was For Sure Wrong,” CD Projekt Admits
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0972
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0973 - GTA 6’s Extended Look Trailer Seemingly Paid Off For Netflix With Massive Viewership
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0973
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0974 - Resident Evil Movie Popcorn Bucket Is Gross But Fitting
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0974
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0975 - Sony To Pay Out Nearly $8 Million In Class-Action Settlement Over Game Prices
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0975
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0976 - Square Enix Shares Jumped On Buyout Rumors, But The Company Says It’s Not Happening
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0976
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0977 - Sony Warns PlayStation Customers Against Harassing Support Staff Amid Disc Backlash
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0977
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0978 - Witcher 4 Dev “Not Worried” About Future Of Consoles Despite Rising Costs
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0978
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0979 - GTA 6 Has A Point Of No Return For Players Who Take Crime Too Far
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0979
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0980 - LOTR Fans Need To “Be Patient,” Kingdom Come Dev Says About New Middle-earth RPG
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0980
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0981 - Don’t Care About GTA 6’s Romance System? Don’t Use It, Dev Says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0981
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0982 - Super Smash Bros. Ultimate Gets An Update, But Not The One You Want
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0982
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0983 - You Can Watch A Cow Play Eve Online Right Now
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0983
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0984 - Mario Kart 8 Deluxe Just Got A Surprise Free Update With 8-Player Split-Screen
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S0984
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0985 - Double Fine称众筹1亿美元就做《野兽传奇2》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0985
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Double Fine确认收回游戏IP与发行权，销售收入将支持独立运营｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0987 - 《巫师3》重制版支持继承原版存档
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0987
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0990 - 《鬼武者 剑之道》评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0990
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0991 - Rockstar公布受官方支持的《GTA》RP服务器
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0991
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0992 - 索尼日本出台顾客骚扰应对政策
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0992
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0993 - 神谷英树：卡普空没意识到《生化危机》有多吓人
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0993
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0994 - 《龙之信条2》「黑暗觉者」游戏循环介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0994
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0996 - 《Neo Berlin 2087》Pre-Alpha版本实机演示 | gamecom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0996
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0997 - 《Like or Die》「DLSS 4.5」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0997
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0998 - 电影《街头霸王》全新预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S0998
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1003 - 《黎明行者之血》PC设置指南
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1003
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1004 - 《疯狂出租车：极速环游》前瞻：Ya Ya Ya Ya Ya……！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1004
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1006 - 《GTA6》作恶过多可能会造成无可挽回的后果
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1006
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1007 - CDPR：游戏主机仍将长期存在
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1007
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1008 - 《星球大战 零号连队》最初设定于《泰坦陨落》宇宙
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1008
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1009 - 《怪物猎人 荒野：凌越》增幅动作介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1009
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1010 - 《怪物猎人 荒野：凌越》「大剑」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1010
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1012 - 《女神异闻录4 Revival》上手前瞻 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1012
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1013 - IGN 中国《疯狂出租车：极速环游》制作人专访：把系列重新带给年轻玩家
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1013
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1014 - 《GTA6》加长版预告中的99个细节
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1014
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1015 - 《控制：共振》最终前瞻
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1015
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1016 - 科隆游戏展《乐高天际线》试玩：玩具质感的正经城市建造体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1016
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1017 - 《壁画迷境》开发商访谈：离开迪士尼，Dlala 第一次讲自己的童话
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1017
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1019 - 让好创意，在聚光灯下持续生长，第三届TapTap聚光灯GameJam报名开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1019
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1020 - NOVA海外独立游戏见闻 Vol.150
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1020
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "咪咕《雾影猎人》全平台玩家突破150万｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1021 - 诺娃独立游戏通讯 2026-#35
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1021
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1022 - Former id Software producer says the team faced the 'worst crunch' in the series' history on Doom: The Dark Ages – Revelations: 'There were days where I didn't see my son'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1022
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1023 - Alienware aims at 'more price points people can actually reach,' announces a tandem OLED gaming monitor at a much lower price than our current top pick
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1023
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1024 - Here's The Blood of Dawnwalker release time for your region
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1024
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1025 - 30,000 games are either Steam Deck verified or at least 'playable' on Valve's handheld
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1025
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《三角洲行动》日活突破5000万，进入高基数长线运营阶段｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1026 - Resident Evil 2's director believes Capcom has become 'completely numb to how scary' recent games have been and wants a 'non-horror mode'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1026
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1027 - After playing a bit of Lego Skylines, it seems like a city builder for people who care less about traffic jams and more about decorating
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1027
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox意外泄露末世大战略新作《Afterworld》｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox公布《LEGO Skylines》，将乐高积木用于城市建造｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1028 - Was Geralt's voice actor inspired by Henry Cavill's take on him in The Witcher series? 'No, because we were first'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1028
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1029 - Zach Cregger is going to bring the 'resource management aspect of the games' to his Resident Evil movie
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1029
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1030 - I've been worried Persona is succumbing to saminess, but Persona 4 Revival feels just as good as its predecessor did 16 years ago
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1030
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1031 - Award-winning presenter Frankie Ward is hosting the PC Gaming Show Tokyo Direct, showing off over 35 games and a bunch of world premieres
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1031
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1032 - SteamDB changes hands to Nexus Mods, which means it 'needs to make money' now—but there won't be ads or paywalls
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1032
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1033 - The Expanse: Osiris Reborn turns the best Mass Effect mission into an entire game
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1033
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1034 - Total War: Warhammer 40,000's Space Marines will have to keep the Imperium happy and avoid looking too heretical
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1034
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《三角洲行动》日活突破5000万，进入高基数长线运营阶段｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1035 - 好友照片共享应用「Retro」获2110万美元融资！这款聚焦反主流社交玩法的App，给社交赛道开发者带来哪些增长新思路？
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S1035
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1036 - 对话制作人：17岁的剑网3，为何选择“从头再来”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1036
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1038 - 从搜打撤到“游乐场”：三角洲不“卷”了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1038
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1039 - 从全网爆火到被喷“退网”，对话高中生团队：想让大家看到我们的游戏创意
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1039
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1040 - 全球首款5K G-SYNC Pulsar电竞显示器亮相！爱攻AGON AGP327KG登陆2026科隆游戏展
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1040
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1041 - 亚洲最大独游资讯节目「ILE2026.12.1」公开征集正式启动！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1041
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1042 - 刚刚，我们玩到了米哈游口中“不像米哈游”的新产品
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1042
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1043 - 逐帧细品《黑神话：钟馗》实机：这一次，游科要玩点真实的
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1043
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《影之刃零》Steam愿望单突破200万，预购表现达《黑神话》同期73%｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1044 - 被米哈游“困住”10年的玩家们
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1044
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1045 - Roblox Fall Games Preview
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1045
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Roblox上线实验早期预警与实时配置，创作者可按玩家分群更新体验｜daily 2026-08-24_to_2026-08-24｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1046 - 原创｜连最好的内容都要删：一支做过“神作”的团队，复盘失控的半年
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1046
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1047 - Google Workspace 推出图像创作编辑工具 Google Pics
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1047
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1048 - Google DeepMind 为 Gemini 推出 agentic 视频理解功能
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1048
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1049 - Claude Fable 5.1 上线 Claude Code 与 Claude Platform，缓存读取降价 75%
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1049
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1050 - Fable 5.1 系统卡披露隐蔽任务与监控难度上升等安全发现
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1050
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1051 - Claude Fable 5.1 登顶 Artificial Analysis 智能指数，但每任务成本比 Fable 5 高 20%
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1051
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1052 - Nvidia 接近以 129 亿美元收购 Hugging Face
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1052
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1053 - Qwen3.8-Max-0902 登顶 Code Arena 并以 $5/MToken 领跑 Pareto 前沿
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1053
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1054 - UU远程新版本上线：完整 TUI 渲染与多终端会话管理，强化远程 Vibe Coding 体验
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1054
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1055 - 美团 LongCat-2.0 上线 Cline 免费试用
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1055
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1056 - Cursor 推出 Self-Hosted Machines，云智能体可在企业自有机器上执行
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1056
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1057 - OpenAI 因 Tumbler Ridge 枪击案面临 30 起新诉讼，被指协助教唆
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1057
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1058 - 什么是 harness 工程？Google 用 ADK 2.0 与 Antigravity SDK 演示自动修复编码循环
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1058
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1059 - Here’s why Rebel Wolves chose UE5 to power its ambitious, large scale, open world RPG The Blood of Dawnwalker
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1059
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1061 - 和平精英 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1061

## Q1062 - 大话西游3 - 资料片
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1062

## Q1063 - 完美国际2 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1063

## Q1064 - 明日方舟 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1064

## Q1065 - 暗区突围 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1065

## Q1069 - 时空猎人·觉醒 - 人气角色「斩魂里昂」觉醒
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1069

## Q1072 - 暗区突围-S19新赛季 - 新赛季开启，参与活动领20抽
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1072

## Q1074 - 王国保卫战5 - 限时15元史低折扣开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1074

## Q1076 - 胜利女神：新的希望 - 新妮姬「艾玛·战术升级」登场
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1076

## Q1077 - 部落冲突：皇室战争 - 新精英「寒冰法师」登场
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1077

## Q1082 - Fangtopia launches October 26
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1082

## Q1083 - Port of Jumanah launches September 7 for PS5, PC
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1083

## Q1084 - Console Archives The Conveni 2 launches September 3
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1084

## Q1085 - Arcade Archives Wiz launches September 3
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1085

## Q1086 - [厂商] [新瓜]尘白前发行制作人林增鸿中元节深夜现身直播间感谢玩家
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1086

## Q1087 - [新瓜] 粥预告pv中的武器设计疑似照搬ow
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1087

## Q1088 - [周边] 库洛偷工减料后，选择的方式是——紧急修改商品信息
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1088

## Q1090 - [疑似内容]尘白通过icp备案审核，尘白似乎真的要有所动作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1090

## Q1091 - 俄罗斯发布手游市场行业报告，宣布俄罗斯是全世界不可忽视的市场
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1091

## Q1092 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1092

## Q1093 - [周边]库洛游戏周边出问题后最终的选择方式
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1093

## Q1094 - [新瓜] [补档]庄方宜动作被指责抄袭
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1094

## Q1095 - [疑似内容]新游《伊莫》的精灵，被指与《宝可梦》人气精灵沙奈朵高度相似
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1095

## Q1096 - [疑似内容] '求瓜 '无限暖暖新玩法与《别拽了！烤串师傅》高度相似，制作组决定先社媒发声
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1096

## Q1097 - 尘白禁区有动静了？
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1097

## Q1100 - 免费MMORPG《宝藏世界》“书籍与鱼钩”活动现已开启，作业泡水变鱼饵
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1100
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1101 - 《坦克世界》2.4版本“动力全开”今日上线
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1101
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1102 - Steam周销量排行榜:《星球大战 零号连队》登顶|2026年8月第4周
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1102
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1103 - 《我是你的野兽》“退出时间”DLC正式公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1103
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1104 - 《链在一起》现已实装2v2竞速模式
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1104
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1106 - 《GTA5》角色扮演服务器“NoPixel V”将于9月8日登陆R星官方平台
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1106
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1107 - 双人太空冒险游戏《轨道双子星》现已登陆 Nintendo Switch 2
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1107
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1108 - PLAYISM宣布TGS直播活动将于9月10日19时播出
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1108
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1109 - Nexus Mods全资收购SteamDB数据库平台
- exclude → industry_news；逐条复核后E3×R2+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S1109
- scores: {"event": 3, "relevance": 2, "hook": 1, "total": 7}
- 事件3×相关2+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1111 - HBO剧版《哈利·波特与魔法石》公布最新预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1111
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1112 - Xbox网络再度中断7小时，微软深表歉意
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1112
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1114 - 【抽奖】八位堂猎户座 3E 精英手柄套装 XBOX 版预售开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1114
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1117 - 动作塔防新作《维京防线：北境之风》现已开始Steam试玩测试
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1117
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1119 - 维多利亚风模拟经营游戏《辉光之城1907》「回响测试」开启招募
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1119
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1124 - 境井仁登场！《羊蹄山之魂 完全版》“无尽追缉”模式公布新宣传片
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1124
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1126 - 9月State of Play日本消息汇总，《WPCA》正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1126
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，把科技树改为探索发现｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "育碧正式公布《英雄无敌III重制版》，成都与上海团队主导开发｜daily 2026-08-26_to_2026-08-26｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox正式公布《Afterworld》，科技树依赖探索发现｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《破坏领主2》正式公布，计划2027年开启抢先体验｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1129 - 休闲游戏成香馍馍！MMO大佬已花20亿并购，表态：“继续买休闲厂商”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1129
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1130 - “牌佬大电影来了”！宝可梦公布卡牌主题剧场版动画，牌佬当主角
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1130
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1131 - 前腾讯海外总监分享：全球游戏业大洗牌，你该知道啥？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1131
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1132 - 8月微信小游戏畅销榜Top 100：《向僵尸开炮》登顶、三七多达8款入榜
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1132
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1133 - 错过鹰角、投过TapTap，这家游戏资本要在上海赌 AI 与游戏下个十年
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1133
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1134 - SLG大佬的新野心，Funplus：《伊莫》是公司史上最大豪赌！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1134
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1136 - 离职明星团队创业，在研UE5猫猫ARPG，制作人：我想纯粹
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1136
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1137 - 对话德国游戏产业协会总经理：国家每年掏近10亿扶持游戏，但这很赚
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1137
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1138 - 起底腾讯游戏神秘AI团队：杰出科学家带队，顶尖博士扎堆
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1138
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1139 - 7天超2000万流水：没人看好的慢生活“摆烂”小游戏，悄悄卖疯了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1139
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["三七互娱《镇邪人》一度冲入微信小游戏畅销榜前三，近期回落至第12名｜weekend 2026-08-14_to_2026-08-16｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏降低IAA激励门槛，长线分成周期延至180天｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏降低IAA激励门槛，长线分成周期延至180天｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队把30万日活小游戏接入微信小店｜weekend 2026-08-21_to_2026-08-23｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》DAU突破1200万，抖音小游戏带来单日百万新增｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏升级IAP首发激励，首1000万流水最高170%综合分成｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1140 - Supercell 将完成对Metacore的收购，后者二合产品创收达7亿美元
- exclude → industry_news；逐条复核后E3×R3+M1=10；未达周报8分、属于历史重复或证据不足。
- source_ids: S1140
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1141 - 脱离国风，终末地还把握得住吗？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1141
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1142 - 金秋宠外观首曝！魔域口袋版李白登场
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S1142
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1144 - 战斗体系全面革新！类幸存者新游《烬刃交辉》2.0 DEMO 版本上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1144
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["4X策略游戏《魔法大战略：穆瑞耶之心》推出免费Demo｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1146 - 开学季满分搭档 满级核心释放澎湃动能
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1146
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1147 - 把《彩虹六号》做成回合制单机：制作人说这是个很自然的选择
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1147
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1150 - 从《进击的巨人》到《七大罪》，这款末日废土SLG已经把动漫IP联动做明白了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1150
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1151 - 香港理工大学的独游团队，做了个玄幻风的「养女儿」游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1151
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1153 - Square Enix denies going private after report sends stock surging
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1153
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1155 - CD Projekt Red sees profit climb 37% in H1 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1155
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1156 - "This is the worst crash we've seen since the 1980s," says Tim Sweeney
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1156
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1158 - Peak studio Aggro Crab establishes publishing label for "intense, stylised games with an attitude"
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S1158
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1159 - Sony and Microsoft request dismissal of consumer lawsuits over tariff refunds
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1159
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1160 - "We've got a great team, money in the bank, and financial independence": Glowmade comes out swinging after Amazon pulled the plug on King of Meat
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1160
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1161 - Apple faces £2bn lawsuit over implementation of App Tracking Transparency framework
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1161
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1162 - Duolingo partners with Eggy Party in China
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1162
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1163 - Palworld Online opens for pre-registration in South Korea
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1163
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1164 - Square Enix denies plans to go private after report sends stock surging
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1164
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1165 - GameUp Africa rebrands as GameUp Academy with always-on learning platform
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1165
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1166 - Saudi gaming startup Takahouse raises $1.5m from Impact46
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1166
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1167 - DMCC and Epiphany launch gaming mentorship programme
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1167
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1168 - AI Gamechangers Summit boosts PG Connects Nordics
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1168
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1169 - How Türkiye's Bold Games plans to set itself apart
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1169
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1170 - Seriously founder Andrew Stalbow fronts investor group set to acquire Bath City Football Club
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1170
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1171 - Sony Music Japan to acquire 23.29% stake in Puzzle & Dragons developer GungHo Online Entertainment
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1171
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1172 - DoubleDown Interactive's Faith Price on D2C growth, ageing apps and the real cost of AI
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1172
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1173 - CD Projekt Red won't be abandoning physical releases
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1173
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1174 - Gamecity Hamburg launches second round of prototype funding
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S1174
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1175 - On the podcast: A lot of App Store news, NC’s $300m mobile push, Overwatch, Metacore, Yahoo and more
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1175
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "AppMagic：二季度中度手游仅射击品类收入同比增长｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "苹果重订欧盟App Store费率，外部商店交易佣金降至5%｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1176 - Apple faces £2bn claim from UK app developers over App Tracking Transparency
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1176
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Block Blast!+》将进入Apple Arcade，以无广告无内购版本扩展订阅渠道｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1177 - Lego Skylines is more approachable than the main Cities Skylines series, but that doesn’t mean it’s basic
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1177
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Paradox公布《LEGO Skylines》，将乐高积木用于城市建造｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1178 - Planet Coaster studio Frontier says it’s working on a Disney game in the same ‘management sim’ genre
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1178
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1179 - The Witcher Remake is on hold while its studio works on The Witcher 3’s expansion
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1179
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1180 - PlayStation State of Play: Where to watch today’s presentations
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1180
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1181 - Sonic is allowed to fire guns in Fortnite because he’s an android, not the real one, Sonic Team boss says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1181
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1182 - Three studios have pitched new Banjo-Kazooie games to Microsoft, says composer
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1182
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1183 - Ghost of Tsushima’s Jin Sakai returns in new Yotei DLC
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1183
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1184 - The $180 PlayStation Lego set has been officially announced, and it’s out soon
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1184
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏降低IAA激励门槛，长线分成周期延至180天｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "微信小游戏降低IAA激励门槛，长线分成周期延至180天｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Paradox公布《LEGO Skylines》，将乐高积木用于城市建造｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1185 - PS Plus’s next Classics games include Ratchet & Clank and more
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1185
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1186 - Square Enix confirms Final Fantasy 7 Revelation release date
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1186
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1187 - GTA 6 is getting two custom PS5 DualSense controllers
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1187
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1188 - We played Final Fantasy Resonance and it delivers classic FF at last
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1188
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1189 - Capcom’s new Monster Hunter Wilds: Ascendance trailer debuts new monsters
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1189
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1190 - Double Fine’s Xbox exclusive Keeper is now on PS5
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1190
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Double Fine确认收回游戏IP与发行权，销售收入将支持独立运营｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1191 - Dispatch developer AdHoc is working on Until Dawn 2
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1191
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1192 - PlayStation State of Play: All the news from today’s Japan live stream
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1192
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1194 - 触乐怪话：既要自由度，又要抄作业
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1194
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1196 - A Real-Life Romance (And The Love Of Fans) Fueled A Classic NES Remake
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1196
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1197 - Long-Delayed Prison Architect 2 Gets Exciting Update After Two Years Of Mostly Silence
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1197
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1198 - CD Projekt Red Is Still Raking In The Cash As We Wait For The Witcher 4
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1198
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1199 - PlayStation State Of Play September 2026: Start Time, How To Watch, And What To Expect
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1199
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1200 - Planet Coaster Dev Announces New Game With Disney, And That’s Very Exciting
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1200
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1201 - PlayStation State Of Play September 2026: All The Biggest Announcements, Games, And Trailers
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1201
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1202 - MMOs Have “Stagnated,” Guild Wars 3 Studio Head Says
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1202
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1203 - Resident Evil Trailer Shows The Sequence Where Its Star Almost Died For Real
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1203
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1204 - Jin Sakai Returns In Upcoming Ghost Of Yotei Roguelike DLC
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1204
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1205 - More PlayStation Plus Games Revealed, Including A Day-One Release
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1205
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1206 - Final Fantasy VII Revelation And Its PS1-Style World Map Arrive In April
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1206
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1207 - GTA 6 Fishing And Hunting Doesn’t Work Like You Think It Does
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1207
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1208 - GTA 6 Limited-Edition DualSense Controllers Are On The Way, And They Look Fantastic
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1208
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1209 - Epic Games’ New Voice Chat Lets You Keep Talking To Friends While Playing Different Games
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1209
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1210 - FFVII Revelation DLCs Feature Sephiroth And Vincent, Extending The Story Into 2028
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1210
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1211 - Sony And Microsoft: We’re Keeping Tariff Refunds For Ourselves And You’ll Get Nothing
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1211
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1212 - Everything From The State Of Play That You Can Try Right Now
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1212
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1213 - Double Fine Flexes Its Independence With Price Cuts And A New PS5 Release
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1213
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Double Fine确认收回游戏IP与发行权，销售收入将支持独立运营｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1214 - The Witcher 4 Will Be Made “Predominantly Using People” And Not AI
- exclude → industry_news；仅有短摘要，不能作为终稿事实证据。
- source_ids: S1214
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1215 - 《GTA 6》独家专访：“全方位的进步”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1215
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1216 - 乐高PlayStation套装图片泄露
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1216
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1218 - 罗素兄弟回应《复仇者联盟5》未完成剧本就开拍
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1218
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1219 - 史克威尔艾尼克斯否认私有化传闻
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1219
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1220 - 前概念艺术家证实迪士尼曾开发大乱斗游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1220
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1221 - 索尼如今的用户收入较PS4时期增59%
- exclude → industry_news；逐条复核后E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S1221
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1222 - CDPR确认《巫师》重制版项目暂时搁置
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1222
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1223 - CDPR正为未公布新作扩充开发团队
- exclude → industry_news；逐条复核后E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S1223
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1224 - 《黎明行者之血》开场动画
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1224
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1226 - 《鬼武者 剑之道》「白衣男子」角色预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1226
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1230 - 《她在时间之外》游戏玩法预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1230
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1231 - 《维京王朝》游戏玩法预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1231
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1232 - PC版《黎明行者之血》实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1232
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1233 - 剧集《哈利·波特与魔法石》先导预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1233
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1234 - 《ONTOS》实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1234
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1235 - 《怪物猎人 荒野：凌越》「弓」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1235
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1236 - 《控制：共振》中的敌人和Boss将如何影响世界
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1236
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1237 - 《队长小翼 2：世界群星》评测：7分
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1237
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1238 - 《最终幻想 Resonance》上手前瞻｜IGN 中国
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1238
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1239 - 《Sil与消逝之境》宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1239
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1240 - Nicky Case 行之，明也
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1240
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1241 - 本周 Steam 值得关注的游戏 08.31 - 09.06（三）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1241
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《生存日志》Steam国区畅销排名升至Top 10，四人团队持续日更修复｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封闭测试吸引近50万玩家，Steam峰值超过10万人｜daily 2026-08-25_to_2026-08-25｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《影之刃零》Steam预售约30万份，海外愿望单占比约70%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1242 - 微信小游戏杀出地下城 RPG：《地下城与冒险家》产品玩法分析
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1242
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["盛趣《云海之下》停止充值，将于10月20日关闭全部区服｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "前叠纸、乐元素成员组建七人团队，首曝知识驱动ARPG《伊始之猫》｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资团队《骤影·绯月杀》开启首次公开测试，三年研发投入超千万元｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1243 - 游戏角色走进现实，大概就是这只机器鸭的样子
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1243
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1244 - 从《Snake Clash》到《XP Hero》，Supercent如何把LTV设计进游戏？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1244
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1245 - All Swordmastery ability manual locations in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1245
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1246 - All Witchcraft ability manual locations in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1246
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1247 - Full prologue walkthrough and quest order for The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1247
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1248 - How to prepare Anca's recipe in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1248
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1249 - Can you beat Brencis in The Blood of Dawnwalker's prologue?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1249
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1250 - Every romancable character in The Blood of Dawnwalker and how to have them fall fang over heels for Coen
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1250
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1251 - I've spent over 80 hours in The Blood of Dawnwalker—here are my top 20 quick tips to survive Vale Sangora
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1251
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪移动端英雄射击《Overwatch Rush》进入早期测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1252 - How to drink Vrakhir blood in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1252
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1253 - Should you let Anca use The Font in The Blood of Dawnwalker?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1253
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1254 - How to complete The Heart Wants What It Wants in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1254
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1255 - How to complete A Bulwark Against Darkness in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1255
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1256 - The Blood of Dawnwalker - best settings to tweak
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1256
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1257 - How to complete Forge It Anew in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1257
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1258 - How to complete Home Sweet Home in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1258
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1259 - How to complete Letters to Lunka in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1259
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1260 - Should you invite Ambrus in The Blood of Dawnwalker?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1260
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1261 - Should you kill the soldiers at the mill in The Blood of Dawnwalker?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1261
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1262 - Should you force feed Esme in The Blood of Dawnwalker?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1262
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1263 - How to complete Where Loyalty Lies in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1263
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1264 - How to complete Blasphemy in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1264
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1265 - How to free Mert in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1265
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1266 - How to beat the Ravenous Bear and complete Into the Den in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1266
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1267 - How to sell silver in The Blood of Dawnwalker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1267
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1268 - CD Projekt mystery games update: Yes, they're still happening, and no, not any time soon
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1268
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["WEBTOON战略投资RI Games Holdings，首批约3320万美元取得约20%股权｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜daily 2026-08-19_to_2026-08-19｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "鹰角投资《人类一败涂地》老将创办的英国工作室Pretty Cool Games｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games 1800万美元B轮，并签署Godot亚洲多年合作｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1269 - Corsair HS35 v3 review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1269
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1270 - Gigabyte GO27Q24A Review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1270
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1271 - CD Projekt Red isn't 'planning to rely on AI making complete games', and will still be 'predominantly using people' for The Witcher 4 and beyond
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1271
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1272 - Dave Bautista is reaching unprecedented levels of buff for his role as Kratos: '2 more months to get to where I need to be'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1272
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1273 - New Final Fantasy 14 site update stabs the final pin into my conspiracy board, leaving me 99.9% sure I know what the new physical ranged job is
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1273
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1274 - Acer's bizarre hybrid handheld/laptop concept is way more interesting than what is actually getting released this year
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1274
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1275 - Onimusha on Steam Deck is the definition of 'playable': Surprisingly pleasant, so long as 30 fps isn't a dealbreaker
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1275
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜daily 2026-08-18_to_2026-08-18｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "上海10人团队首曝卡牌建造自走棋《王国棋境》｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝独游布局新增《生存日志》，上线后进入Steam国区热销前15｜weekly 2026-08-14_to_2026-08-20｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《沙金工业》EA发售8天销量破10万，Steam好评率保持97%｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1276 - Onimusha: Way of the Sword has a hard mode, but it isn't unlocked from the start
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1276
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯间接控股团队首曝《Waste The Fallen》，9月4日开启北美Alpha测试｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "《The Witcher IV》发行日期指向2028年｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1277 - Alien: Isolation 2's Gamescom demo kept its cards close to its chest, but I'm definitely ready to be terrified again
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1277
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["4X策略游戏《魔法大战略：穆瑞耶之心》推出免费Demo｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1278 - Guild Wars 3's approach to combat and movement is like nothing I've ever seen in an MMO before: 'One of our big goals when we make a new game in the Guild Wars franchise is to set out and try new things'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1278
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1279 - PUBG's new spin-off game is 'faster, meaner, and more aggressive' with sword hands and 'a little bit of light cannibalism'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1279
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Newzoo称中国贡献2025年全球游戏收入增量32%，手游仍是主要驱动力｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜daily 2026-08-17_to_2026-08-17｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯与Krafton公布《PUBG Mobile Light》，账号、道具与好友关系可继承｜weekly 2026-08-14_to_2026-08-20｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Newzoo预计2026年全球游戏市场达2139亿美元，移动端占57%｜daily 2026-08-25_to_2026-08-25｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "Krafton公布《PUBG: DED.NET》，探索多人射击与肉鸽成长｜weekly 2026-08-21_to_2026-08-27｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1280 - Final Fantasy 7 Revelation gets a release date and a proper look at its airship overworld, which is cool, if in danger of inducing open world fatigue
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1280
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1281 - Crimson Desert's upcoming DLC decides it's The Sims now, I guess
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1281
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1282 - Both Microsoft and Sony say they're under no obligation to pass tariff refunds on to customers
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1282
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["韩国策略塔防续作《Random Dice 2》取消角色抽卡，上线后最高达iOS畅销榜第26名｜daily 2026-08-24_to_2026-08-24｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全｜weekly 2026-08-21_to_2026-08-27｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1283 - Stalker 2 studio is raffling keychains made from a shot-down Russian helicopter to raise funds for mine removal in the real-world Chornobyl Exclusion Zone
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1283
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1284 - Zach Cregger doesn't want to get bogged down in 'the wild aspects' of Resident Evil's lore: 'I'm not going to have a gigantic jacked dude in a trench coat'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1284
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1286 - 2026千元档电竞椅权威横评：傲风C3Pro对决四大同价位竞品，谁才是真正性价比之王
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1286
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1288 - 观察｜《决胜巅峰》十周年庆典官宣定档
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1288
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1289 - 投稿丨维多利亚风模拟经营游戏《辉光之城1907》「回响测试」火热招募中，筑光之旅，再启新程~
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。
- source_ids: S1289
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1292 - Google DeepMind 发布 Gemini 3.8 Flash 与 3.8 Flash Cyber 两款新模型
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1292
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1293 - Google 总结 AI Agents Challenge 中最强提交背后的 4 个工程模式
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1293
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1294 - Google AI 团队分享如何为 LLM-as-a-Judge 评测编写可靠的评分标准
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1294
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1295 - GitHub Copilot 如何在不牺牲任务质量的前提下降低 AI 编码成本
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1295
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1296 - Claude 在 Cowork 和 Claude Code 中支持后台操作电脑
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1296
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1297 - Meta 发布 Muse Spark 1.3，智能体与科学推理能力提升
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1297
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1298 - Meta 发布 Muse Spark 1.3，Intelligence Index 得 61-62 分逼近 Claude 与 GPT-5.6
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1298
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1299 - 美国司法部介入纽约时报诉 OpenAI 案，主张 AI 训练属合理使用
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1299
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1300 - xAI 发布 Grok Bot 企业版，Grok 与 Cursor Enterprise 客户两周免费
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1300
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1301 - OpenAI 发布 GPT-6 Astra 并公布安全概览，称其网络安全能力达到 Preparedness Framework 的 Critical 级
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1301
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1302 - xAI 设计 Grok Bot：为持久化智能体重构交互界面
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1302
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1303 - Tom Tunguz 解析 Meta Muse Spark 双轨定价背后的数据换算力逻辑
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1303
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1304 - Hugging Face 发布开源工具 funes，为编码智能体提供可本地持有的记忆层
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1304
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1305 - 用 TRL 和 OpenEnv 训练编码模型画水彩：Hugging Face 全流程开源复现
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1305
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1306 - Meta Muse Spark 1.3 在 Artificial Analysis 编码智能体指数中与 Claude 组合对比评测结果公布
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1306
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1307 - METR 发布 OpenAI/Hugging Face 智能体攻击事件的独立调查报告
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1307
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1308 - NVIDIA 宣布以 129.303 亿美元收购 Hugging Face
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1308
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1309 - OpenAI 推出 Daybreak for Frontline Defenders，投入10亿美元支持一线网络防御
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1309
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1310 - Google DeepMind 发布 WeatherNext 3 全球天气 AI 模型， hourly 更新且分辨率较上一代提升约 5 倍
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1310
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1311 - Google Cloud 教你用 Cloud Run instances 以每月 $5.70 搭建常驻 Agent
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1311
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1312 - Stepping inside a retro anime-inspired game: a look into the rendering of Orbitals
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1312
- AI: {"ai_tier": "direct_application", "game_stage": ["development"], "industry_reverse_scan": false, "migration_path": null}

## Q1313 - EMEA Dev Days | Unreal Engine
- exclude → ai_trends；AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。
- source_ids: S1313
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"}

## Q1314 - 大道仙途 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1314

## Q1315 - 奥拉星2 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1315

## Q1316 - 帝国神话：王权 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1316

## Q1317 - 异环 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1317

## Q1319 - 王者荣耀世界 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1319

## Q1322 - 光·遇(官服) - 领航员先祖复刻
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1322

## Q1324 - 奥拉星(官服) - 七周年版本开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1324

## Q1325 - 巅峰极速 - 免费领120抽
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1325

## Q1326 - 异环-1.3版本(官服) - 新角色「灵可」登场
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1326

## Q1327 - 无畏契约：源能行动 - 【海洋旅者】系列皮肤上线
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1327

## Q1329 - 植物大战僵尸海绵宝宝版 - 新增地图水母田
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1329

## Q1330 - 永劫无间手游(官服)-二周年 - 新英雄甘璇上线
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1330

## Q1331 - 第五人格(官服)-1v4对抗 - 象牙塔剧情活动《失控的庆典》开启
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1331

## Q1333 - 遗忘之海(官服)-奇遇海洋开放世界 - 黑券船员爱德华登场
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1333

## Q1334 - 鸣潮-3.6版本(官服) - 新角色「心」「锁暝」实机演示公布
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1334

## Q1339 - Fall Up launches December 3 for PS5, Xbox Series, Switch 2, PS4, Switch, and PC
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1339

## Q1340 - Daba: Land of Water Scar launches in spring 2027, published by Sony Interactive Entertainment
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1340

## Q1341 - Echoes of Aincrad: Sword Art Online DLC ‘Genesis Maidens’ launches this winter
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1341

## Q1342 - SlashZero launches in spring 2027, limited-time demo now available
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1342

## Q1343 - Stupid Never Dies ‘First Bite’ demo now available
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1343

## Q1344 - Fate/EXTRA Record launches January 28, 2027 for PS5, Switch 2, PS4, Switch, and PC
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1344

## Q1345 - Final Fantasy VII Revelation launches April 8, 2027
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1345

## Q1346 - Until Dawn 2 launches January 28, 2027
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1346

## Q1347 - Mycopunk launches in October for PS5, PC
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1347

## Q1348 - Rev. NOiR launches in 2027 for PS5, Xbox Series, and PC
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1348

## Q1349 - Keeper now available for PS5
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1349

## Q1350 - Gundam Rogue Orbit launches March 5, 2027
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1350

## Q1351 - Final Fantasy Resonance demo now available
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1351

## Q1352 - METRO 2039 launches February 4, 2027
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1352

## Q1353 - Marvel’s Wolverine launch trailer
- exclude → release_calendar；已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。
- source_ids: S1353

## Q1354 - [米哈游] 米哈游新作源初之结由于既视感过强，在外网引起热议
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1354

## Q1355 - [厂商] [新瓜]尘白前发行制作人林增鸿中元节深夜现身直播间感谢玩家
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1355

## Q1356 - [米哈游] 真珠实机演示，毛笔画出油画
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1356

## Q1357 - [疑似内容]尘白通过icp备案审核，尘白似乎真的要有所动作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1357

## Q1358 - [新闻相关][搬运] 2026科隆游戏展，最佳移动端游戏为燕云十六声
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1358

## Q1359 - [新瓜][瓜小味甜][世界计划国服]什么叫领奖励需要冒着被没收的风险在晚自习玩手机？
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1359

## Q1360 - [白银之城]宣发使用“那咋了”
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1360

## Q1361 - [新瓜]西山居新作运营官号承认尘白已死？
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1361

## Q1362 - [新瓜] 大侠立志传外传跳票到年底了
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1362

## Q1363 - [米哈游][厂商]汉丰二小遭遇网络诈骗，收款方疑似冒充米哈游
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1363

## Q1364 - [疑似内容] '求瓜 '无限暖暖新玩法与《别拽了！烤串师傅》高度相似，制作组决定先社媒发声
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1364

## Q1365 - [新瓜]王者荣耀毛茸茸企划被孙权玩家刷屏了
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1365

## Q1366 - [新瓜] 三国杀联动五年高考三年模拟
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1366

## Q1367 - 尘白禁区有动静了？
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1367

## Q1368 - [影之诗][小瓜微甜]影之诗策划联同木谷高明宣布要提高女性玩家在影之诗的活跃度，并推出全女影之诗战队
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1368

## Q1369 - [米哈游] 崩坏3，十周年庆实体奖励疑似被砍
- exclude → community_discourse；已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。
- source_ids: S1369

## Q1370 - GTA 6 reveal causes Xbox and PlayStation sales to jump by a third
- exclude → deep_analysis；周报只消费精确人工selection，本条未被用户选择。
- source_ids: S1370
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}
