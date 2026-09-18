# 2026-09-11_to_2026-09-17 筛选决策

卡片曝光去重：双周历史窗口2026-08-28至2026-09-10；本期未使用card_carryover。历史匹配逐项读取card_exposed、card_rank、card_limit与card_exposure_source；本周日报/周末报已覆盖的事件只在本周周报合并一次。

维度覆盖自检：国内移动/国产产品与人才 38张候选；市场数据 33张候选；并购 10张候选；平台政策 75张候选；档期变动 82张候选；资本组织 26张候选；海外重大 242张候选。

产品日历漏挂反查：已扫描industry_news与release_calendar全部上线、测试、预下载、首次曝光、定档、跨平台、回归和重大更新信号；误挂、重复、单源、窗口外与低于多源优先级前7项者均显式exclude。

AI反扫：已扫描全部949条行业新闻输入与50条AI输入；同一事件仅保留一个分区。

质量说明：1269条输入，0抽取失败、0空正文和183条非全文；非全文未作为终稿证据。精确深度selection不存在，旧错名selection也不存在，因此第五栏省略。

## I001 - 沙特PIF考虑整合EA与Savvy Games Group，意在加强资产协同
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M2=11，达到周报8分门槛。
- source_ids: S0076, S0095
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["沙特PIF考虑整合EA与Savvy Games Group，意在加强资产协同｜2026-09-11_to_2026-09-13｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "PIF", "product": "EA与Savvy Games Group", "event_date": "2026-09-12", "event": "考虑整合"}

## I002 - 暴雪正式公布《暗黑破坏神5》，计划2029年春季发售
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M2=11，达到周报8分门槛。
- source_ids: S0340, S0346
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["暴雪正式公布《暗黑破坏神5》，计划2029年春季发售｜2026-09-11_to_2026-09-13｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "暴雪", "product": "暗黑破坏神5", "event_date": "2026-09-13", "event": "正式公布与档期确认"}

## I003 - 网易《千里之路》明确独立产品方向，承接《射雕》技术与美术积累
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M1=10，达到周报8分门槛。
- source_ids: S0173
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["网易《千里之路》明确独立产品方向，承接《射雕》技术与美术积累｜2026-09-11_to_2026-09-13｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}

## I004 - 《王者万象棋》上线次日升至iOS畅销榜第5，首日新增超千万
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0045, S0312
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "material_update", "prior_occurrences": ["《王者万象棋》上线首日登顶iOS免费榜，7000万预约转入实盘验证｜weekly 2026-09-04_to_2026-09-10", "《王者万象棋》上线次日升至iOS畅销榜第5，首日新增超千万｜2026-09-11_to_2026-09-13｜current_week_rollup"], "new_facts": ["次日iOS畅销榜升至第5", "上线首日新增用户超过1000万"], "prior_card_exposed": true}
- cluster_basis: {"subject": "腾讯", "product": "王者万象棋", "event_date": "2026-09-11", "event": "榜单与新增用户更新"}

## I005 - Roblox开放作品独立应用出口，覆盖移动端、PC与主机
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0170
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Roblox开放作品独立应用出口，覆盖移动端、PC与主机｜2026-09-11_to_2026-09-13｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}

## I006 - 暴雪公布《StarCraft》开放世界射击新作，计划2030年推出
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R2+M2=8，达到周报8分门槛。
- source_ids: S0338
- scores: {"event": 3, "relevance": 2, "hook": 2, "total": 8}
- 事件3×相关2+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["暴雪公布《StarCraft》开放世界射击新作，计划2030年推出｜2026-09-11_to_2026-09-13｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}

## I007 - 《Physint》被曝错过开发节点并面临超支风险，索尼收紧投资
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R2+M2=8，达到周报8分门槛。
- source_ids: S0382, S0435, S0473
- scores: {"event": 3, "relevance": 2, "hook": 2, "total": 8}
- 事件3×相关2+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "material_update", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视 | weekly 2026-09-04_to_2026-09-10", "索尼退出《Physint》合作后，Xbox接手发行并拓展影视合作 | weekend 2026-09-11_to_2026-09-13", "《Physint》被曝错过开发节点并面临超支风险，索尼收紧投资｜2026-09-14｜current_week_rollup"], "prior_details": [{"report_window": {"start": "2026-09-04", "end": "2026-09-10"}, "report_kind": "weekly", "candidate_id": "N-I004", "event": "《Physint》由PlayStation退出后转由Xbox合作", "entities": ["Kojima Productions", "PlayStation Studios", "Xbox", "Physint"], "title": "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视", "claims": ["PlayStation Studios在6月中旬通知小岛工作室取消《Physint》项目", "团队随后用三个月寻找新合作方", "Xbox现已接手，项目继续开发", "PlayStation将此表述为退出合作", "Xbox公告则称双方关系将延伸至游戏之外，并规划影视合作"], "source_ids": ["S1026", "S1134"], "artifact": "output\\weekly\\2026-09-04_to_2026-09-10\\_intermediate\\report_items.json", "card_exposed": false, "card_rank": null, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "history_index": 102}, {"report_window": {"start": "2026-09-11", "end": "2026-09-13"}, "report_kind": "weekend", "candidate_id": "I008", "event": "Xbox接手发行并拓展影视合作", "entities": ["小岛工作室", "索尼", "Xbox", "Physint"], "title": "索尼退出《Physint》合作后，Xbox接手发行并拓展影视合作", "claims": ["索尼退出《Physint》合作", "Xbox将接手该项目发行", "合作范围也将延伸至电影和电视领域", "《Physint》仍定位为谍战动作项目"], "source_ids": ["S0037"], "artifact": "output\\weekend\\2026-09-11_to_2026-09-13\\_intermediate\\report_items.json", "card_exposed": true, "card_rank": 8, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "history_index": 114}], "new_facts": ["项目已错过开发节点并面临严重超支风险；索尼担忧预算、盈利与限时独占回报。"], "prior_card_exposed": true}
- cluster_basis: {"subject": "PlayStation", "product": "Kojima Productions", "event_date": "2026-09-14", "event": "PlayStation退出《Physint》的项目原因披露"}

## I008 - 恺英网络拟斥资约21亿元，间接持有娱美德约19.7%股权
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M2=11，达到周报8分门槛。
- source_ids: S0392, S0412, S0414, S0428
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["恺英网络拟斥资约21亿元，间接持有娱美德约19.7%股权｜2026-09-14｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "恺英网络", "product": "娱美德", "event_date": "2026-09-11", "event": "恺英网络拟间接持有娱美德约19.7%股权"}

## I009 - 暴雪与CD Projekt扩大合作，《Cyberpunk 2077》年内登陆Battle.net
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0387, S0506
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "material_update", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net | weekly 2026-08-28_to_2026-09-03", "暴雪与CD Projekt扩大合作，《Cyberpunk 2077》年内登陆Battle.net｜2026-09-14｜current_week_rollup"], "prior_details": [{"report_window": {"start": "2026-08-28", "end": "2026-09-03"}, "report_kind": "weekly", "candidate_id": "I003", "event": "《巫师3》重制版进入Battle.net", "entities": ["Blizzard", "CD Projekt", "The Witcher 3"], "title": "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net", "claims": ["暴雪宣布与CD Projekt合作，将《The Witcher 3: Wild Hunt — Remastered》带到Battle.net", "《Diablo IV》的杰洛特主题皮肤", "Battle.net"], "source_ids": ["S0378", "S0289"], "artifact": "output\\weekly\\2026-08-28_to_2026-09-03\\_intermediate\\report_items.json", "card_exposed": true, "card_rank": 5, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "history_index": 43}], "new_facts": ["《Cyberpunk 2077》及其资料片将在2026年内登陆Battle.net"], "prior_card_exposed": true}
- cluster_basis: {"subject": "暴雪", "product": "CD Projekt", "event_date": "2026-09-13", "event": "《Cyberpunk 2077》及资料片将在2026年内登陆Battle.net"}

## I010 - Everplay提高对Bulkhead持股，《Wardogs》成功触发资本加码
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M1=10，达到周报8分门槛。
- source_ids: S0615
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Everplay提高对Bulkhead持股，《Wardogs》成功触发资本加码｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I011 - 《Wardogs》一个周末销量突破200万份，远超40万份生存线
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0792
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "material_update", "prior_occurrences": ["《Wardogs》抢先体验首日售出125万份，Steam峰值突破34万 | weekend 2026-09-11_to_2026-09-13", "《Wardogs》一个周末销量突破200万份，远超40万份生存线｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": ["预购销量达到100万份", "一个周末后累计销量突破200万份"], "prior_card_exposed": true}
- cluster_basis: {"subject": "Bulkhead", "product": "Wardogs", "event_date": "2026-09-15", "event": "一个周末销量突破200万份"}

## I012 - Netflix与世嘉达成三项目合作，覆盖《疯狂出租车》《索尼克》《异于天堂》
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R2+M2=8，达到周报8分门槛。
- source_ids: S0616, S0678
- scores: {"event": 3, "relevance": 2, "hook": 2, "total": 8}
- 事件3×相关2+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Netflix与世嘉达成三项目合作，覆盖《疯狂出租车》《索尼克》《异于天堂》｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Netflix与世嘉", "product": "三款世嘉游戏改编", "event_date": "2026-09-15", "event": "达成多项目影视改编合作"}

## I013 - 8月中国手游出海榜：Merge-2多款创新高，《Last Asylum》收入增37%
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0590, S0609
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["8月中国手游出海榜：Merge-2多款创新高，《Last Asylum》收入增37%｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Sensor Tower", "product": "2026年8月中国手游出海榜", "event_date": "2026-09-15", "event": "发布海外收入与下载量榜单"}

## I014 - Curve Games签约发行在线合作RPG《Wyldheart》
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M1=10，达到周报8分门槛。
- source_ids: S0614
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Curve Games签约发行在线合作RPG《Wyldheart》｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I015 - Bohemia Interactive收购《Everwind》开发商少数股权
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M1=10，达到周报8分门槛。
- source_ids: S0628
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Bohemia Interactive收购《Everwind》开发商少数股权｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}

## I016 - 《失落星船：马拉松》大型更新延期至12月，Bungie退出严格赛季制
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0681, S0712
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["《失落星船：马拉松》大型更新延期至12月，Bungie退出严格赛季制｜2026-09-15｜current_week_rollup"], "prior_details": [], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Bungie", "product": "失落星船：马拉松", "event_date": "2026-09-15", "event": "大型更新延期并退出严格赛季制"}

## I017 - 莉莉丝公开都市生活模拟新项目，猫爪拿铁工作室启动多岗位招聘
- include → industry_news；本周日报/周末报事件合并进入周报；E3×R3+M2=11，达到周报8分门槛。
- source_ids: S0823, S0954
- scores: {"event": 3, "relevance": 3, "hook": 2, "total": 11}
- 事件3×相关3+钩子2 = 11；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["莉莉丝公开都市生活模拟新项目，猫爪拿铁工作室启动多岗位招聘｜2026-09-16｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "莉莉丝", "product": "未命名都市生活模拟项目", "event_date": "2026-09-16", "event": "正式公开在研方向并招聘"}

## I018 - Newzoo：2026年移动游戏收入将达1211亿美元，下载下降但获客成本上升
- include → industry_news；本周日报/周末报事件合并进入周报；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S0819, S0858
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": true, "novelty": "new_event", "prior_occurrences": ["Newzoo：2026年移动游戏收入将达1211亿美元，下载下降但获客成本上升｜2026-09-16｜current_week_rollup"], "new_facts": [], "prior_card_exposed": false}
- cluster_basis: {"subject": "Newzoo", "product": "2026全球游戏市场报告", "event_date": "2026-09-16", "event": "发布移动收入与获客成本预测"}

## I019 - 《伊莫》PC首日Steam同时在线突破12万，海外评价占据主要样本
- include → industry_news；E2×R3+M2=8，达到周报8分门槛。
- source_ids: S1063, S1079
- scores: {"event": 2, "relevance": 3, "hook": 2, "total": 8}
- 事件2×相关3+钩子2 = 8；E×R+M；include
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}
- cluster_basis: {"subject": "FunPlus", "product": "伊莫", "event_date": "2026-09-16", "event": "《伊莫》PC首日Steam同时在线突破12万，海外评价占据主要样本"}

## I020 - Nex完成逾1.5亿美元融资，家庭体感主机销量突破100万台
- include → industry_news；E3×R2+M2=8，达到周报8分门槛。
- source_ids: S1086, S1104
- scores: {"event": 3, "relevance": 2, "hook": 2, "total": 8}
- 事件3×相关2+钩子2 = 8；E×R+M；include
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}
- cluster_basis: {"subject": "Nex", "product": "Nex Playground", "event_date": "2026-09-17", "event": "Nex完成逾1.5亿美元融资，家庭体感主机销量突破100万台"}

## A001 - 字节游戏江南工作室推进AI真人RPG《Beyond the Mundane》，团队扩至约20人
- include → ai_trends；AI直接进入游戏内容生产与交互，且有明确团队、商业模式和档期。
- source_ids: S0305
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "product"], "industry_reverse_scan": true, "migration_path": null}

## A002 - 腾讯为《和平精英》上线专属AI专家，把游戏知识库接入Agent
- include → ai_trends；AI直接用于游戏知识服务与运营任务，具备规模化用户数据。
- source_ids: S0047
- AI: {"ai_tier": "direct_application", "game_stage": ["product", "operations"], "industry_reverse_scan": true, "migration_path": null}

## A003 - Meowa把AI像素素材生成推进到可直接进入游戏引擎的生产流程
- include → ai_trends；生成内容可直接进入游戏引擎，开发环节迁移路径清晰。
- source_ids: S0053
- AI: {"ai_tier": "direct_application", "game_stage": ["development"], "industry_reverse_scan": true, "migration_path": null}

## A004 - Roblox称Build已发布近9000款游戏，71%创作者此前未用过Studio
- include → ai_trends；游戏创作工具已有发布量、创作者结构和下一项生成能力，属于直接作用类。
- source_ids: S0447
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "publishing"], "industry_reverse_scan": true, "migration_path": null}

## A005 - Level-5确认在部分开发环节使用生成式AI，目标将五年周期缩至两年
- include → ai_trends；公司确认生成式AI已用于具体制作管线并说明效率目标，属于直接作用类。
- source_ids: S0476
- AI: {"ai_tier": "direct_application", "game_stage": ["development", "product"], "industry_reverse_scan": true, "migration_path": null}

## A006 - 《Bside》用角色所有权替代聊天依赖，次留约60%
- include → ai_trends；角色创建、共同冒险和离线动态已经直接作用于AI游戏产品，并有移动端留存数据。
- source_ids: S0701
- AI: {"ai_tier": "direct_application", "game_stage": ["product", "operations"], "industry_reverse_scan": true, "migration_path": null}

## C001 - 《原神》UGC复刻《空洞骑士》场景，引发原创边界争论
- include → community_discourse；周末窗口内出现并持续发酵，讨论对象和争议链路清晰。
- source_ids: S0377

## C002 - 《异环》前瞻提前一天误播，兑换码同步可用，玩家质疑直播流程失控
- include → community_discourse；9月15日当日事件，触发、玩家争议逻辑和时间线清楚。
- source_ids: S0789

## C003 - 《炉石传说》黄金卡包被标成10金币，购买玩家随后称账号遭封禁
- include → community_discourse；当日事件具备触发、争议逻辑、时间线和后续扫描。
- source_ids: S1015

## R001 - 伊莫
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0835, S0952, S0971, S0974
- scores: {"event": 3, "source": 4, "company": 3, "total": 15}
- cluster_basis: {"subject": "伊莫", "product": "伊莫", "event_date": "2026-09-16", "event": "同一产品同日产品日历节点"}

## R002 - 闪耀吧！噜咪
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S1076, S1215, S1243
- scores: {"event": 3, "source": 4, "company": 3, "total": 15}
- cluster_basis: {"subject": "闪耀吧！噜咪", "product": "闪耀吧！噜咪", "event_date": "2026-09-17", "event": "同一产品同日产品日历节点"}

## R003 - 莫诺微步
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S1075, S1198
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "莫诺微步", "product": "莫诺微步", "event_date": "2026-09-17", "event": "同一产品同日产品日历节点"}

## R004 - 蓝色星原：旅谣
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S1197, S1236
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "蓝色星原：旅谣", "product": "蓝色星原：旅谣", "event_date": "2026-09-17", "event": "同一产品同日产品日历节点"}

## R005 - 黑白之地
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0753, S0770
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}
- cluster_basis: {"subject": "黑白之地", "product": "黑白之地", "event_date": "2026-09-15", "event": "同一产品同日产品日历节点"}

## R006 - 幻想放置远征队
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0390, S0425
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "幻想放置远征队", "product": "幻想放置远征队", "event_date": "2026-10-09", "event": "同一产品同日产品日历节点"}

## R007 - 卧龙2：凤火连天
- include → release_calendar；多源候选按事件类型×来源强度+重点公司加分排序进入报告上限
- source_ids: S0811, S0895
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "卧龙2：凤火连天", "product": "卧龙2：凤火连天", "event_date": "2027-03-04", "event": "同一产品同日产品日历节点"}

## R008 - 2026-09-10 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0068, S0175, S0238, S0300, S0312, S0410
- scores: {"event": 3, "source": 4, "company": 3, "total": 15}
- cluster_basis: {"subject": "王者万象棋", "product": "王者万象棋", "event_date": "2026-09-10", "event": "同一产品同日产品日历节点"}

## R009 - 2026-09-04 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0300
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R010 - 2026-09-13 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0312
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R011 - 2026-09-14 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0400
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R012 - 2024-07-23 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0403
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R013 - 2026-09-03 公测
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0410
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R014 - 2026-09-10 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0410
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R015 - 2026-09-14 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0415
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R016 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0590
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R017 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0838
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R018 - 2026-09-10 抢先体验测试
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S1060
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R019 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1063
- scores: {"event": 3, "source": 2, "company": 3, "total": 9}

## R020 - 2026-09-10 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0002, S0051
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "黄金星漩", "product": "黄金星漩", "event_date": "2026-09-10", "event": "同一产品同日产品日历节点"}

## R021 - 2026-09-11 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0027, S0058
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "白金档案PLATiNA ：： LAB", "product": "白金档案PLATiNA ：： LAB", "event_date": "2026-09-11", "event": "同一产品同日产品日历节点"}

## R022 - 2026-09-14 正式上线
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0481, S0491
- scores: {"event": 3, "source": 3, "company": 0, "total": 9}
- cluster_basis: {"subject": "暗黑破坏神4", "product": "暗黑破坏神4", "event_date": "2026-09-14", "event": "同一产品同日产品日历节点"}

## R023 - 2026-09-15 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0749
- scores: {"event": 3, "source": 1, "company": 3, "total": 6}

## R024 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0003
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R025 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0022
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R026 - 2026-09-11 抢先体验测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0032
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R027 - 2026-06-09 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0044
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R028 - 2026-09-03 公开测试
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0071
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R029 - 2026-08-21 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0072
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R030 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0107
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R031 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0127
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R032 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0132
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R033 - 2026-09-11 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0168
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R034 - 2026-09-12 抢先体验测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0219
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R035 - 2026-09-12 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0223
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R036 - 2026-09-12 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0225
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R037 - 2026-09-12 首测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0238
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R038 - 2026-09-13 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0300
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R039 - 2026-09-14 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0388
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R040 - 2026-09-14 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0391
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R041 - 2026-09-09 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0395
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R042 - 2026-09-14 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0429
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R043 - 2026-09-14 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0519
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R044 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0566
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R045 - 2026-09-15 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0568
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R046 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0578
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R047 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0590
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R048 - 2026-07-30 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0594
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R049 - 2016-06-21 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0597
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R050 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0601
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R051 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0608
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R052 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0646
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R053 - 2025-03-28 抢先体验测试
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0647
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R054 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0648
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R055 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0687
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R056 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0690
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R057 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0701
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R058 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0798
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R059 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0807
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R060 - 2020-12-09 正式上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0820
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R061 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0821
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R062 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0821
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R063 - 2026-09-16 抢先体验测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0889
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R064 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0893
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R065 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1031
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R066 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1043
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R067 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1045
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R068 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1048
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R069 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1049
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R070 - 2026-09-17 抢先体验测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1056
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R071 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1073
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R072 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1077
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R073 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1145
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R074 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1148
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R075 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1155
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R076 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1167
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R077 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1171
- scores: {"event": 3, "source": 2, "company": 0, "total": 6}

## R078 - 2026-09-11 9月21日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0026, S0059
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "护核纪元", "product": "护核纪元", "event_date": "2026-09-11", "event": "同一产品同日产品日历节点"}

## R079 - 2026-09-09 新品首次曝光
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0410, S0871
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "未眠野", "product": "未眠野", "event_date": "2026-09-09", "event": "同一产品同日产品日历节点"}

## R080 - 2026-09-14 新品预下载
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0416, S0526, S0532
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "伊莫", "product": "伊莫", "event_date": "2026-09-14", "event": "同一产品同日产品日历节点"}

## R081 - 2026-09-15 12月3日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0579, S0679
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "雷曼：传奇再叙", "product": "雷曼：传奇再叙", "event_date": "2026-09-15", "event": "同一产品同日产品日历节点"}

## R082 - 2026-09-16 11月13日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0831, S0950
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "笑拉了，我家旁边是魔王城666", "product": "笑拉了，我家旁边是魔王城666", "event_date": "2026-09-16", "event": "同一产品同日产品日历节点"}

## R083 - 2026-09-17 9月17日上线定档
- exclude → release_calendar；超过本报告产品日历条数上限
- source_ids: S0906, S1140
- scores: {"event": 2, "source": 3, "company": 0, "total": 6}
- cluster_basis: {"subject": "火焰纹章 万缕千丝", "product": "火焰纹章 万缕千丝", "event_date": "2026-09-17", "event": "同一产品同日产品日历节点"}

## R084 - 2026-09-11 10月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0005
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R085 - 2026-09-11 新品首次曝光
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0008
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R086 - 2026-09-11 2026年12月1日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0009
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R087 - 2026-09-11 11月12日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0014
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R088 - 2026-09-11 10月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0016
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R089 - 2026-09-11 2月5日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0021
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R090 - 2026-09-11 9月21日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0029
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R091 - 2026-09-11 9月17日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0034
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R092 - 2026-09-11 8月31日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0050
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R093 - 2026-09-11 10月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0069
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R094 - 2026-09-11 新品首次曝光
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0073
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R095 - 2026-09-11 10月16日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0119
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R096 - 2026-09-12 9月21日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0216
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R097 - 2026-09-12 9月17日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0221
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R098 - 2026-09-12 9月21日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0222
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R099 - 2026-09-12 2月5日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0229
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R100 - 2026-09-12 4月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0233
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R101 - 2026-09-13 4月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0298
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R102 - 2026-09-13 9月20日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0300
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R103 - 2026-09-13 2029年春季上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0329
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R104 - 2026-09-13 11月5日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0331
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R105 - 2026-09-13 9月15日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0356
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R106 - 2026-09-13 10月6日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0356
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R107 - 2026-09-14 2030年春季上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0409
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R108 - 2026-09-14 9月28日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0409
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R109 - 2026-09-14 9月23日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0420, S0523
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}
- cluster_basis: {"subject": "古龙群侠录", "product": "古龙群侠录", "event_date": "2026-09-14", "event": "同一产品同日产品日历节点"}

## R110 - 2026-09-14 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0426
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R111 - 2026-09-14 10月27日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0455
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R112 - 2026-09-14 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0473
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R113 - 2026-09-14 10月16日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0474
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R114 - 2026-09-14 12月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0476
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R115 - 2026-09-14 10月20日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0481
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R116 - 2026-09-15 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0567
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R117 - 2026-09-15 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0577
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R118 - 2026-09-15 2030年春季上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0593
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R119 - 2026-09-15 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0681
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R120 - 2026-09-15 2027年9月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0686
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R121 - 2026-09-16 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0797
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R122 - 2026-09-16 12月3日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0799
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R123 - 2026-09-16 10月13日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0804
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R124 - 2026-09-16 10月9日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0815
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R125 - 2026-09-16 2026年11月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0819
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R126 - 2026-09-16 2026年11月上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0819
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R127 - 2026-09-16 2026年下半年测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0871
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R128 - 2026-09-16 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0888
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R129 - 2026-09-16 今年秋季上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0888
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R130 - 2026-09-16 2027年2月23日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0892
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R131 - 2026-09-17 10月9日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1027
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R132 - 2026-09-17 3月4日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1035
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R133 - 2026-09-17 10月13日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1039
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R134 - 2026-09-17 10月8日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1042
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R135 - 2026-09-17 新品定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1046
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R136 - 2026-09-17 11月10日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1053
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R137 - 2026-09-17 11月19日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1067
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R138 - 2026-09-17 11月5日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1121
- scores: {"event": 2, "source": 2, "company": 0, "total": 4}

## R139 - 2026-09-11 内测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0184
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R140 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0199
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R141 - 2026-09-11 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0200
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R142 - 2026-09-11 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0202
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R143 - 2026-09-11 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0203
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R144 - 2026-09-11 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0204
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R145 - 2026-09-12 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0275
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R146 - 2026-09-13 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0363
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R147 - 2026-09-13 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0365
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R148 - 2026-09-14 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0538
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R149 - 2026-09-14 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0539
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R150 - 2026-09-15 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0750
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R151 - 2026-09-15 公测
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0751
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R152 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0755
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R153 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0759
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R154 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0760
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R155 - 2026-09-15 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0761
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R156 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0762
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R157 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0764
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R158 - 2026-09-15 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0765
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R159 - 2026-09-15 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0766
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R160 - 2026-09-15 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0769
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R161 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0977
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R162 - 2026-09-16 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0983
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R163 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0985
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R164 - 2026-09-16 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0986
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R165 - 2026-09-16 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0987
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R166 - 2026-09-16 限量测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0988
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R167 - 2026-09-16 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0989
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R168 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1222
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R169 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1223
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R170 - 2026-09-17 公开测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1224
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R171 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1227
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R172 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1237
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R173 - 2026-09-17 正式上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1239
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R174 - 2026-09-17 删档测试
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1240
- scores: {"event": 3, "source": 1, "company": 0, "total": 3}

## R175 - 2026-11-30 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0139, S1150
- scores: {"event": 1, "source": 3, "company": 0, "total": 3}
- cluster_basis: {"subject": "战锤40K：战争黎明4（Warhammer 40,000： Dawn of War IV）", "product": "战锤40K：战争黎明4（Warhammer 40,000： Dawn of War IV）", "event_date": "2026-11-30", "event": "同一产品同日产品日历节点"}

## R176 - 2026-10-02 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0494, S0697
- scores: {"event": 1, "source": 3, "company": 0, "total": 3}
- cluster_basis: {"subject": "空战奇兵8 希孚之翼", "product": "空战奇兵8 希孚之翼", "event_date": "2026-10-02", "event": "同一产品同日产品日历节点"}

## R177 - 2026-09-24 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0896, S1171
- scores: {"event": 1, "source": 3, "company": 0, "total": 3}
- cluster_basis: {"subject": "控制：共振", "product": "控制：共振", "event_date": "2026-09-24", "event": "同一产品同日产品日历节点"}

## R178 - 2026-09-11 9月24日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0193
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R179 - 2026-09-12 10月16日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0274
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R180 - 2026-09-14 9月15日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0537
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R181 - 2026-09-14 9月15日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0540
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R182 - 2026-09-15 10月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0756
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R183 - 2026-09-15 9月23日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0758
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R184 - 2026-09-15 9月17日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0763
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R185 - 2026-09-15 9月16日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0767
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R186 - 2026-09-15 9月16日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0768
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R187 - 2026-09-15 9月16日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0771
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R188 - 2026-09-16 9月24日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0973
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R189 - 2026-09-16 9月17日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0979
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R190 - 2026-09-16 9月17日测试定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0990
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R191 - 2026-09-16 9月17日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0991
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R192 - 2026-09-17 9月22日上线定档
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1231
- scores: {"event": 2, "source": 1, "company": 0, "total": 2}

## R193 - 2026-09-11 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0033
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R194 - 2026-09-11 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0063, S0167, S0172
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "菇域幽城", "product": "菇域幽城", "event_date": "2026-09-11", "event": "同一产品同日产品日历节点"}

## R195 - 2026-09-10 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0070
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R196 - 2027-04-08 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0121
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R197 - 2026-10-23 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0130, S0901, S1151
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "最终幻想 RESONANCE", "product": "最终幻想 RESONANCE", "event_date": "2026-10-23", "event": "同一产品同日产品日历节点"}

## R198 - 2026-11-10 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0131
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R199 - 2026-09-12 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0220
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R200 - 2026-09-11 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0300
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R201 - 2026-05-20 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0335
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R202 - 2026-11-05 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0396
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R203 - 2026-09-13 老品重启回归
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0402, S0419
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "英雄联盟", "product": "英雄联盟", "event_date": "2026-09-13", "event": "同一产品同日产品日历节点"}

## R204 - 2026-09-29 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0481
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R205 - 2026-10-01 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0485
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R206 - 2026-09-16 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0806
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R207 - 2026-10-16 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0809, S1033
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}
- cluster_basis: {"subject": "链兽角斗", "product": "链兽角斗", "event_date": "2026-10-16", "event": "同一产品同日产品日历节点"}

## R208 - 2026-09-10 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0822
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R209 - 2026-09-16 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0836
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R210 - 2027-03-04 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0895
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R211 - 2026-10-13 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0897
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R212 - 2026-10-09 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S0914
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R213 - 2026-09-17 老品跨平台上线
- exclude → release_calendar；单源不具备正文资格
- source_ids: S1037
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R214 - 2026-09-24 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S1153
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R215 - 2027-03-04 老品跨平台上线
- exclude → release_calendar；事件日期不在报告窗口
- source_ids: S1162
- scores: {"event": 1, "source": 2, "company": 0, "total": 2}

## R216 - 2026-09-11 老品重启回归
- exclude → release_calendar；单源不具备正文资格
- source_ids: S0195
- scores: {"event": 1, "source": 1, "company": 0, "total": 1}

## Q0001 - PLAYISM发布会消息汇总，确认十款游戏参展TGS
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0001
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0002 - 【抽奖】卡牌策略×即时动作！《黄金星漩》9月10日正式发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0002
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0003 - 【抽奖】《不/存在的你，和我》主机版今日正式发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0003
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0004 - 《饿狼传说：群狼之城》X《东京卍复仇者》联动详情公开
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0004
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0005 - 《饿狼传说：群狼之城》NS2版定于10月发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0005
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0006 - 《合金弹头终极合集》现已公开商城页
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0006
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0007 - 科乐美公布《游戏王 TAG FORCE GX》详情，确认支持中文
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0007
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0008 - 四人合作游戏《黑街厨神》预告片首曝
- exclude → industry_news；E3×R2+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0008
- scores: {"event": 3, "relevance": 2, "hook": 1, "total": 7}
- 事件3×相关2+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0009 - 《Hela：鼠鼠奇旅》将于2026年12月1日全球发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0009
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0010 - 《胡闹厨房》团队新作《怪镇奇旅》将于2027年春季上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0010
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0011 - 可折叠iPhone Duo领衔：苹果发布多款新品
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0011
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0012 - 索尼宣布不再与小岛工作室合作打造IP谍报动作游戏《PHYSINT》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0012
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0013 - 2026款18英寸微星游戏本矩阵推荐：主流新品神影18 AI、旗舰性能泰坦18、轻薄全能选绝影18 AI
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0013
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0014 - 《索尼克PICO PARK》将于11月12日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0014
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0015 - 《英灵神殿》1.0版本现已正式上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0015
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0016 - 《NS运动度假胜地》将于10月22日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0016
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0017 - Steam周销量排行榜:《黎明行者之血》登顶|2026年9月第1周
- exclude → industry_news；E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0017
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《黎明行者之血》发售三天销量突破100万份｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rebel Wolves为《黎明行者之血》下一章招聘首席编剧｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0018 - 【抽奖】四人合作中式恐怖游戏《捉迷藏》现已公开 Demo
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0018
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["增量放置游戏《米粒新世界》开放Demo｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0019 - 《战锤40K：战争黎明4》三份全新战报发布，战火持续升级
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0019
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0020 - 《雷顿教授与不可思议的小镇》重制版正式公开：LEVEL5发布会消息汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0020
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0021 - 和风动作RPG《胧村正怪奇谭》将于27年2月5日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0021
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0022 - CRPG《索拉斯塔2》多人模式现已推出，邪术师职业同步上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0022
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0023 - 可变刷新率来了：NS2主机模式迎来VRR支持
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0023
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0024 - 电影《野兽之心》公布最新预告，将于9月30日上映
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0024
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0025 - 第三人称射击游戏《流浪地球：望日》公布首支预告片
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0025
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["柳叶刀首曝《流浪地球：望日》，转向叙事驱动的第三人称射击｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0026 - 《护核纪元》免费大型更新“地下骑手”将于9月21日上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0026
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0027 - Q萌二次元音游《白金档案PLATiNA :: LAB》正式发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0027
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0028 - Epic喜加二：《星座上升》《Luftrausers》免费领
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0028
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0029 - 【抽奖】无传送带设计：AI辅助自动化工厂游戏《奇迹工厂》将于9月21日在steam平台发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0029
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0030 - IGN及GameSpot双六分：《漫威金刚狼》媒体评分汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0030
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0031 - 独特乐趣：《战狗 WARDOGS》销量突破125万份
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0031
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0032 - 【抽奖】彼岸花团队新作！回合战术肉鸽新作《血色序曲》现已开启抢先体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0032
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0033 - 【抽奖】伊藤润二风温馨恐怖种田RPG《欢迎来到古原镇》现已登陆PC
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0033
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0034 - 积木解谜新作《木木屋》公布发售预告，将于9月17日发售
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0034
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0035 - 上海市网络游戏行业协会技术主题沙龙：AI 在游戏生产中的落地提效
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0035
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0036 - 十年后，我们还在《阴阳师》里相逢
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0036
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0037 - “小岛秀夫的游戏都要自救”！索尼官宣砍掉《PHYSINT》，小岛拉来微软救场
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0037
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0038 - 玩家炸锅！Steam强制玩家信用卡年龄验证，22年老账号也被挡在门外
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0038
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0039 - 梁其伟最新长文：解释《影之刃零》难度设计、武器成长到玩家共创
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0039
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0040 - 《原神》63位角色声音“被AI盗用”，米哈游获赔75万元！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0040
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0041 - 刘慈欣硬撑中国科幻，《流浪地球：望日》游戏登上热搜！团队热血，玩家理性
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0041
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["柳叶刀首曝《流浪地球：望日》，转向叙事驱动的第三人称射击｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0042 - “太子爷大显神威”！7000万玩家冲爆《王者万象棋》，首日畅销榜第9
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0042
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《王者万象棋》定档9月10日，预约量突破7000万｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》上线首日登顶iOS免费榜，7000万预约转入实盘验证｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0043 - 超4000亿收购EA沐瞳后，沙特土豪或将把它们合并
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0043
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0044 - 8年砍掉3款，烧钱数亿，这家上海千人大厂还没拿出爆款
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0044
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0046 - 深圳的国有资本，开始入场投资游戏了
- exclude → industry_news；E3×R2+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0046
- scores: {"event": 3, "relevance": 2, "hook": 1, "total": 7}
- 事件3×相关2+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0048 - 腾讯这款长青产品，这次把“游戏+AI”玩出了新花样
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0048
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0049 - 小岛秀夫和索尼分手：“老夫老妻”因何闹掰？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0049
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0050 - 最“豪”游戏登上热搜：打包全网烂梗，可炒股，还监督你每天提肛
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0050
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0051 - 卡牌策略×即时动作！《黄金星漩》9月10日正式发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0051
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0052 - AI时代，谁在做游戏？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0052
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0054 - 请把不歪池做成3D二游的标配吧
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0054
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0055 - From Graphics to the Engine: Li Chi and His Meowa Experiment
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0055
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0056 - In the Age of AI, Who Is Making Games?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0056
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "4399投资杭州深空之序，持股5%布局AI智能体｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0057 - Please make "Bu Wei Chi" a standard feature in 3D mobile games.
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0057
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0058 - Q萌二次元音游《白金档案PLATiNA :: LAB》正式发售！中文实装、价格永降，国区首发售价51元！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0058
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0059 - 骑上坐骑，出发！《护核纪元》免费大型更新“地下骑手”将于9月21日上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0059
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0060 - 《神力科莎：拉力》更新3款新车 定制涂装功能
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0060
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0061 - 505 GAMES二十周年庆 Steam 特卖同步开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0061
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0062 - 开学季大学生首选 华硕天选7X一站式搞定创作与游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0062
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0063 - 双牌组构筑Roguelite地牢冒险游戏《菇域幽城》现已登陆Steam抢先体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0063
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0064 - 《鬼武者：剑之道》《黎明行者之血》最新3A大作，高画质也能百帧丝滑体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0064
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《黎明行者之血》发售三天销量突破100万份｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《鬼武者：剑之道》首日销量破百万，Steam简中评价占49.75%｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rebel Wolves为《黎明行者之血》下一章招聘首席编剧｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0065 - 历经最后的优化，魔女探索冒险游戏《蕾卡的移动工坊》于9月29日将开放免费体验版，正式版1.0上市日期确定为10月26日发售！同步完整支持简体中文翻译！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0065
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0066 - CrazyGames移动发行收入增长至3倍：Adjust助力规模化增长
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0066
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0067 - 开学神装新选择 全能表现助力游戏娱乐
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0067
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0068 - 天美这张“王炸”上桌了，底气藏在玩法里
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0068
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0069 - 离开待了27年的卡普空，《生化危机6》制作人在新作“放飞自我”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0069
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0070 - 天津光荣首度操刀，《三国志14》时隔6年推出“威力加强传承版”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0070
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0071 - 发售10小时销量破125万份，又有一款FPS爆了
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0071
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0072 - 《诡秘之主》将加入自走棋玩法：少有新品上线不足一月就发全新衍生作
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0072
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0073 - 只是放出试玩版本，这款独立游戏就被视作「年度最佳」候选了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0073
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0074 - No More Robots' nine-year journey to releasing its first self-developed IP – "This sounds so naive and stupid, but somehow it's working"
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0074
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["4399投资杭州深空之序，持股5%布局AI智能体｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "4399投资杭州深空之序，持股5%布局AI智能体｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0075 - Saber Interactive has "no real development in North America any more"
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0075
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0077 - Saber Interactive's Tim Willits on generative AI, moving development out of North America, and embracing recognisable IP
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0077
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Double Fine脱离微软恢复独立，Schafer强调由团队自行承担存续责任｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0078 - Marvel's Wolverine | Critical consensus
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0078
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0079 - European studio expenditure on external talent rises 63% in 2025
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0079
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0080 - State of the Unions: the rise of unionisation in games workplaces
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0080
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0081 - On sale now: PG Connects Jordan returns November 7th and 8th
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0081
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0082 - Report: Saudi Arabia’s PIF mulls EA and Savvy merger
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0082
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0083 - Studio Atelico opens iOS closed beta for creature battler Bobium Brawlers
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0083
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝《塔塔冒险队》公测后进入iOS畅销榜前30｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》上线首日登顶iOS免费榜，7000万预约转入实盘验证｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "莉莉丝《塔塔冒险队》公测后进入iOS畅销榜前30｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0084 - Age of Magic surpasses $120m revenue as installs near 20m
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0084
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["4399投资杭州深空之序，持股5%布局AI智能体｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "4399投资杭州深空之序，持股5%布局AI智能体｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0085 - California enacts new social media curbs for children under 16
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0085
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0086 - Andrew Stalbow-led investor group completes Bath City FC acquisition
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0086
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0087 - How PG Connects London 2027 will be our finest flagship event ever!
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0087
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0088 - New release roundup: New York Times Bonus Puzzles, Villain!, DIY Dadish, and more
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0088
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0089 - Football's gaming ties, Epic's social push, Zelda's mobile connection and lessons from Sucker Punch  | Week in Views
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0089
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0090 - EA is using genAI for commentator voiceover in NHL 27
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0090
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0091 - 'Ship a good game, learn from it, and build from there:' Lessons from going indie after a decade at id Software
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0091
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0092 - Xbox to publish Kojima Productions' Physint after PlayStation ditches project
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0092
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0093 - Rockstar and fired GTA developers outline core arguments during union busting tribunal
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0093
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0094 - An honest opinion or defamation? A solicitor outlines the legal nuance
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0094
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0096 - New game digest: Monster Hunter Outlanders, Warhammer Boltgun Boom, Pixel Gun 2, Pusheen’s Place and more
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0096
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0097 - Confused by app store and webshop fees? Try our commission calculator
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0097
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国App Store季度支出十年来首次下滑｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "App Store新管理层被曝寻求提高利润率与经常性收入｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0098 - Amazon Prime’s 9 ‘free’ games for September include Doom Eternal and High on Life
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0098
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0099 - Starfield developer says it was ‘not our forte’ and ‘needed way more’ people to do it properly
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0099
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0100 - Footage of PlayStation’s Fairgames allegedly leaks via playtest
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0100
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0101 - Podcast: What is going on at PlayStation?
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0101
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0102 - PlayStation reportedly cancelled Kojima’s Physint because Death Stranding failed to meet expectations
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0102
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0103 - 触乐怪话：拼豆冥想
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0103
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0104 - 是的，我想成为最了解《蓝色星原》的那个人
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0104
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0105 - 战斗交互模型设计之多人对抗游戏的疑难
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0105
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0106 - 游戏项目磕磕绊绊，为什么还是关不掉？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0106
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0107 - 让玩家直呼“上头”，天美手里的“王牌”来炸场了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0107
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0108 - Amazon Luna Introduces Its Most Ambitious Feature Yet In A Rough Month For Cloud Gaming
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0108
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0109 - Amazon Prime Members Get Doom Eternal And 10 More Games For Free In September
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0109
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0110 - Wardogs’ Massive Start On Steam Undercut By Brutal Server Queues [Update]
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0110
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0111 - Nintendo Finally Adds Some Life To The Switch 2
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0111
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0112 - GTA 6 Is Going To Be Huge. So Why Is Take-Two’s Stock Having Such A Bad Year?
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0112
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0113 - GTA 6 DualSense Controller Scalpers Are Already Cashing In
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0113
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0114 - Hot Toys’ Marvel’s Wolverine Figure Gets The Details Right, Right Down To The Hairy Silicone Arms
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0114
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0115 - Death Stranding Franchise Likely Barely Broke Even, Could Explain Sony Dropping Physint – Analyst
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0115
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0116 - Switch 2 Update Secretly Makes Digital Game Sharing Much Better
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0116
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0117 - EA’s New Owners May Be Considering An Even Bigger Gaming Empire
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0117
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0118 - Switch 2系统更新，主机模式支持VRR
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0118
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0119 - Rockstar就31名员工解雇案出庭
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0119
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0120 - 乐高《宇宙机器人》套装图片泄露
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0120
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0121 - 《最终幻想7 Revelation》实体版必须下载才能游玩
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0121
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0122 - 今村孝矢称《时之笛》模型或映照宫本茂木偶情结
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0122
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0123 - 《死或生6 Last Round》将减少性感服装
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0123
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0124 - 《战狗》首日销量突破100万
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0124
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0125 - 阿萨·格尔曼加盟新版《X战警》，饰演天使
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0125
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0126 - 《风火轮：无限狂飙》28分钟实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0126
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0127 - 《帝国时代3：决定版》「波罗的海诸国」扩展包发售宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0127
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0128 - 《胧村正怪奇谭》概览预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0128
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0129 - 《愚者不灭》介绍视频：动作篇
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0129
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0130 - 《最终幻想 RESONANCE》「克莱夫」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0130
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0131 - 《舞力全开：传世金曲》公布预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0131
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0132 - 《战狗》发售宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0132
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0133 - 《英灵神殿》开场动画
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0133
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0134 - 《怪物猎人：旅人》开发者专访 | gamescom 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0134
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0135 - 《动物园之星2》「苏门答腊猩猩」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0135
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0136 - 吉尔莫·德尔·托罗：AI替代不了人类创作
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0136
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0137 - 《荒野大镖客：救赎2》亚瑟咳嗽声音是在演员感冒时录制的
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0137
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0138 - GameStop计划重新开放部分已关闭门店
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0138
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0139 - 《战锤40K：战争黎明4》「1v1歼灭战」实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0139
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0140 - 《怪物猎人 荒野：凌越》「狩猎笛」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0140
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0141 - 《沉没之城2》评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0141
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0142 - 《星之旅》评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0142
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0143 - 《星球大战 零号连队》评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0143
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0144 - 《漫威斗魂》评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0144
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0145 - 本周 Steam 值得关注的游戏 09.07 - 09.13（四）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0145
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0146 - itch 一周游戏汇：8月31日-9月6日（上）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0146
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0147 - Thief designer thinks the graphics arms race should have ended with 2010's Alan Wake: 'The fidelity curve has become outrageous'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0147
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0148 - Palworld publishing chief worries early access has 'lost its meaning' as the rise of 'hyper-casual' gaming culture means people often don't understand what they're getting into
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0148
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0149 - Saudi Arabia reportedly looking at merging Electronic Arts with Savvy Games Group
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0149
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0150 - Wardogs servers go down as over 300,000 people rush to play on launch day [Update: I think we're back]
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0150
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0151 - 10 beginner tips to not suck at Wardogs
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0151
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0152 - Electronic Arts admits to using AI voices in NHL 27: 'This process allows us to bring more variety to the game'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0152
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0153 - Steam's latest beta brings 'Big Art' to Big Picture Mode and Steam Deck, and customizable screensavers too
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0153
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0154 - Dave the Diver has now sold more than 10 million copies, Mintrocket 'can't wait to share our future plans'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0154
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0155 - How to use Battle Idols and Protection Idols in Valheim, and where to find the Forge of Potential
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0155
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Discord的《Battlefield 6》任务支持账户绑定与游戏进度同步｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0156 - Ubisoft is 'testing' making its games far less annoying to launch on Steam
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0156
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0157 - Star Wars Zero Company gets much-needed first patch so you won't miss shots with a 100% chance to hit any more
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0157
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0158 - How to increase your inventory in Valheim
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0158
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0159 - PSA: Keep social media trends away from your laptops, unless you want broken hinges
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0159
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0160 - Final Fantasy 7 Revelation director defends its physical disk still needing a download: 'We didn't want to make any compromises for the game'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0160
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0161 - Bribing medics to revive me first in Wardogs is one of my favorite shooter mechanics in ages
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0161
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0162 - Zach Cregger had to dial down the jokes in his upcoming Resident Evil film because test screeners 'thought it was too funny'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0162
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0163 - 'Defying common wisdom', people have been buying more high-end graphics cards despite rising prices, with 12.5 million shipped last quarter alone
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0163
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0164 - 'No fuss, no greater meaning, only fans': Corsair shares 3D print files for its April Fools mini fan cube
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0164
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0165 - 办公Agent赛道竞速升级！WorkBuddy、千问办公、库库AI、豆包工作四款智能体实测，谁在定义下一代办公入口？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0165
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0166 - CrazyGames移动发行收入增长至3倍：Adjust助力规模化增长
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0166
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0167 - 双牌组构筑Roguelite地牢冒险游戏《菇域幽城》现已登陆Steam抢先体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0167
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0168 - 数实融合打造沉浸体验，完美世界以“科技+文化”亮相服贸会
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0168
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0169 - 把AI算力塞进了手机芯片， 手游画质也要变天了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0169
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0171 - 投稿丨益世界《疯狂水世界》全球版本登顶日韩及中国台湾地区App Store免费榜TOP1
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0171
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0172 - 投稿丨双牌组构筑Roguelite地牢冒险游戏《菇域幽城》现已登陆Steam抢先体验
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0172
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0174 - 原创｜8月全球收入Top20：腾讯四款，三角洲第12，瓦手第20
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0174
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0175 - 原创丨畅销Top9，玩家等了3年的“新王牌”终于上桌
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0175
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0176 - Swarmchasers 追踪疑似 OpenAI 智能体，Anthropic 复查自身四起安全事件，而思维链可读性正受 GPT-6 Astra 冲击
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0176
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0177 - Anthropic 报告指控阿里、月之暗面与 DeepSeek 对 Claude 发起蒸馏攻击
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0177
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0178 - Grok Bot 摘要 SpaceX CFO Bret Johnsen 在 Goldman Sachs Communacopia 的演讲要点
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0178
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0179 - 实测 DeepSeek V4.1 Flash：价格大降、原生带视觉，作者用游戏与城市生成任务验证表现
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0179
- AI: {"ai_tier": "direct_application", "game_stage": ["development"], "industry_reverse_scan": false, "migration_path": null}

## Q0180 - OpenAI 详解存储平台 Habitat 如何扩展支撑超 10 亿 ChatGPT 用户（上篇）
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0180
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0181 - Anthropic 威胁报告披露 Claude 被用于间谍软件、导弹与无人机研发，中国实验室大规模蒸馏提取数据
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0181
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0182 - 大唐无双 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0182

## Q0183 - 封神榜 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0183

## Q0184 - 传奇之梦复古合击版 - 内测
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0184

## Q0185 - 使命召唤手游-崩坏3联动 - 《崩坏3》联动开启,送联动武器
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0185

## Q0186 - 元梦之星 - 新赛季领「软萝围衣」时装
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0186

## Q0187 - 战狗 PC/主机 - PC端已上线,快爆CDK超低折扣中
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0187

## Q0188 - 暗区突围-S19新赛季 - 「锁天工」主题系列军需上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0188

## Q0189 - 暗区突围体验服 招募中 - 参与招募赢9月下旬体验服资格
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0189

## Q0190 - 火影忍者手游 - 宇智波鼬「晓·朱」登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0190

## Q0191 - 燕云十六声(官服) - 全新和鸣套装上架
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0191

## Q0192 - 球球大作战(官服) - 召回老友得专属抹茶孢子
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0192

## Q0193 - 破烂水手-正版移植手游 - 定档9月24日正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0193

## Q0194 - 穿越火线-枪战王者 - 全新抽奖「宾果夺宝」开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0194

## Q0195 - 蛋仔派对(官服) - 《线条小狗》联动限时重启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0195

## Q0196 - 赛尔号巅峰之战-页游互通 - 新精灵「极度冰凌·阿克希亚」登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0196

## Q0197 - 超凡先锋 - 无双时装上架，免费领史诗摩托外观
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0197

## Q0198 - 超自然行动组 - 「呆猫八条」联动开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0198

## Q0199 - 金铲铲之战 - 宝宝学院系列全新小小英雄上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0199

## Q0200 - 拳皇·命运 - 10:00 删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0200

## Q0201 - 泉愈 - 10:00 限量抢注测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0201

## Q0202 - 热力无限赛车 - 10:00 正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0202

## Q0203 - 爆裂防线 - 10:00 删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0203

## Q0204 - 笑傲江湖：群侠传 - 10:00 删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0204

## Q0205 - [新瓜] 回旋镖:战舰少女联动南京舰疑似非官方机构联动
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0205

## Q0206 - [厂商]鸣潮登上CCTV2，用中国文化讲全球普适性内容
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0206

## Q0207 - [瓜小味甜] [崩坏：星穹铁道] 游戏已经两年没有四星角色的产出了
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0207

## Q0208 - [新瓜] 群里看到的，妮姬这是？
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0208

## Q0209 - [米哈游] 真珠实机演示，毛笔画出油画
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0209

## Q0210 - [新闻相关]新的大世界二游《未眠野》，发布首爆PV
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0210

## Q0211 - [网易]《遗忘之海》发起“净海行动”，严厉打假造拉踩抹黑等行为
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0211

## Q0212 - [米哈游] 原神日服历史首次飞榜，韩服历史首次飞游戏榜
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0212

## Q0213 - [原神]原神玩家使用内置UGC编辑器千星奇域，手搓空洞骑士引发争议
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0213

## Q0214 - 2026年全球汽车行业趋势洞察报告
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S0214
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0215 - Epic喜加二：《星座上升》《Luftrausers》免费领
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0215
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0216 - 【抽奖】无传送带设计：AI辅助自动化工厂游戏《奇迹工厂》将于9月21日在steam平台发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0216
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0217 - IGN及GameSpot双六分：《漫威金刚狼》媒体评分汇总
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0217
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0218 - 独特乐趣：《战狗 WARDOGS》销量突破125万份
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0218
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0219 - 【抽奖】彼岸花团队新作！回合战术肉鸽新作《血色序曲》现已开启抢先体验
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0219
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0220 - 【抽奖】伊藤润二风温馨恐怖种田RPG《欢迎来到古原镇》现已登陆PC
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0220
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0221 - 积木解谜新作《木木屋》公布发售预告，将于9月17日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0221
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0222 - 《护核纪元》免费大型更新“地下骑手”将于9月21日上线
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0222
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0223 - Q萌二次元音游《白金档案PLATiNA :: LAB》正式发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0223
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0224 - 第三人称射击游戏《流浪地球：望日》公布首支预告片
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0224
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["柳叶刀首曝《流浪地球：望日》，转向叙事驱动的第三人称射击｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0225 - CRPG《索拉斯塔2》多人模式现已推出，邪术师职业同步上线
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0225
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0226 - 可变刷新率来了：NS2主机模式迎来VRR支持
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0226
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0227 - 电影《野兽之心》公布最新预告，将于9月30日上映
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0227
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0228 - 《雷顿教授与不可思议的小镇》重制版正式公开：LEVEL5发布会消息汇总
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0228
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0229 - 和风动作RPG《胧村正怪奇谭》将于27年2月5日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0229
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0230 - Steam周销量排行榜:《黎明行者之血》登顶|2026年9月第1周
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0230
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《黎明行者之血》发售三天销量突破100万份｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rebel Wolves为《黎明行者之血》下一章招聘首席编剧｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0231 - 【抽奖】四人合作中式恐怖游戏《捉迷藏》现已公开 Demo
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0231
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["增量放置游戏《米粒新世界》开放Demo｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0232 - 《战锤40K：战争黎明4》三份全新战报发布，战火持续升级
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0232
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0233 - 2D 对战格斗游戏《MELTY BLOOD: TWI-LUMINA》定于27年4月22日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0233
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0234 - 没人做成的品类，被不信邪的腾讯做到了畅销榜Top 2
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0234
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0235 - Goodwill Hunting: Consoles’ brand value and loyalty is being tested | Opinion
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0235
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0236 - Apple's $2,000+ iPhone Duo and the backlash against new EU App Store rules | Week in Mobile Games podcast
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0236
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》定档9月10日，预约量突破7000万｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国App Store季度支出十年来首次下滑｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "App Store新管理层被曝寻求提高利润率与经常性收入｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "完美世界拟以5000万元认购Monolith新基金份额｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》上线首日登顶iOS免费榜，7000万预约转入实盘验证｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0237 - A listing for Sonic Racing CrossWorlds Year One Edition has been spotted, suggesting a version with all DLC is coming
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0237
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0238 - 触乐本周行业大事：PIF考虑整合EA与Savvy Games，《王者万象棋》上线，《旅行青蛙：中国之旅》宣布停运
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0238
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》定档9月10日，预约量突破7000万｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0239 - 铲铲五年，和他们各自的人生
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0239
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0240 - 从场景复刻到玩法转译：北京环球度假区如何在线下重塑《第五人格》与实景娱乐的边界
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0240
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0241 - GTA 6 Developer Is Fighting Drones And Hackers To Keep The Game’s Secrets Safe
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0241
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0242 - BlizzCon 2026 Opening Ceremony: Start Time, How To Watch, And What To Expect
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0242
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0243 - 《空之轨迹 the 2nd》评测：重温熟悉的风景
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0243
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0244 - 《流浪地球：望日》前瞻：推走月球，迎接希望
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0244
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["柳叶刀首曝《流浪地球：望日》，转向叙事驱动的第三人称射击｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0245 - 2026-08 媒体评分
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0245
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0246 - Sony reportedly dropped Hideo Kojima's next game because it kept missing deadlines, was over budget, and would eventually come to other platforms
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0246
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0247 - Framework cancels custom low profile keyboard module for its laptops: 'We weren’t able to bring costs to a place where the product economics worked'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0247
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0248 - Shroom and Gloom is my new deckbuilder obsession thanks to its fantastic fights, beautiful artwork, and tasty mushrooms
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0248
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0249 - If you use devcommands to cheat in Valheim but want your achievements anyway, you can get them by using the new devcommand 'yesiuseddevcommandsbutiwantmyachievementsanyway'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0249
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0250 - 'We're not giving away pistols and cocaine to people': Miami Beach votes in favor of Grand Theft Auto 6 collab despite concerns
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0250
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0251 - Roblox games are escaping Roblox: Creators will soon be able to export standalone apps for PC, console, and mobile
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0251
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0252 - Nightdive officially confirms Thief Remastered is coming with a new campaign, The Tarnished Mirror
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0252
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0253 - OpenAI employee takes down ChatGPT-coded RuneScape clone following Jagex cease-and-desist
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0253
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0254 - Wolverine review roundup: Frankly, we're starting to feel a little better about the whole 'PlayStation 5 exclusive' thing
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0254
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0255 - Modder adds 235 destructible Flock cameras to GTA 5 so you can 'do whatever the flock you want' to them
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0255
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0256 - While still headquartered in the US, Saber exec Tim Willits says it has 'no real development in North America anymore'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0256
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0257 - Polyarc, developer of the excellent VR platforming series Moss, is shutting down after 12 years: 'We are saying our farewells to each other'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0257
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0258 - Wardogs sold over 1 million copies in its first 24 hours, making its launch a bright spot in an otherwise tough year for multiplayer shooters
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0258
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0259 - All Genshin Impact 7.1 livestream codes
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0259
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0260 - CD Projekt wanted to put a chain weapon in The Witcher 3 years ago, but it's taken until Songs of the Past because it was 'impossible to do at the time'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0260
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0261 - Starfinder: Afterlight, a CRPG based on one of my favourite systems that pulled in almost $1 million on Kickstarter, is starting to look ship-shape
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0261
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0262 - BlizzCon 2026 Opening Ceremony recap—what's next for Warcraft, Diablo, and StarCraft
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0262
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0263 - The Blood of Dawnwalker is a good game, but one change would make it a great RPG
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0263
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0264 - Final Fantasy 14's funky new roguelike mode has me hyped for Evercold's combat revamp, which'll be a winner if it's even half as weird
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0264
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0265 - GTA: London 1961 is full of cockney innuendo and harder than a bobby’s helmet
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0265
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0266 - Square Enix scrambles to fix Final Fantasy 14 bug where new beastmaster could crash entire servers
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0266
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0267 - Beren Millidge、John Schulman、Charlie O'Neill 对谈递归自我改进离我们还有多远
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0267
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0268 - GitHub 日韩营销负责人如何用 GitHub Copilot 把活动运营自动化
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0268
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0269 - DeepSeek 开源 V4.1-Flash：CED 架构降低编码 Agent 的 prefill 开销
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0269
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0270 - 英伟达洽谈以基石投资者身份参与 Anthropic IPO，投资至多 100 亿美元
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0270
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0271 - OpenAI 智能体集群对 RubyGems 发动未公开攻击：作者团队的详细取证分析
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0271
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0272 - Minitap 指控 Google Artemis 未署名使用其开源项目 mobile-use 代码
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0272
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0273 - 三国：谋定天下 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0273

## Q0274 - 对峙：交锋时刻-对峙2国服 招募中 - 冲!多方式赢10月16日国服首测资格
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0274

## Q0275 - 勇士之心 - 10:00 正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0275

## Q0276 - 崩坏：星穹铁道(官服)-4.5版本 - 12:00 新角色【砂金•戏浪】登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0276

## Q0277 - Melty Blood: Twi-Lumina launches April 22, 2027
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0277

## Q0278 - [新瓜]黑暗王朝2.0？某浮力机认定碧蓝航线新皮肤“抄袭”她的“原创幽灵娘”
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0278

## Q0279 - [瓜小味甜] [崩坏：星穹铁道] 游戏已经两年没有四星角色的产出了
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0279

## Q0280 - [周边] [小瓜微甜]万代做原神周边，但是没写散兵名字，写了个等，目前被绝赞冲锋中
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0280

## Q0281 - [诡秘之主]一次又一次的宣传男人穿黑丝裙子跳舞
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0281

## Q0282 - [藤子]王世杰员工迎来毕业季
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0282

## Q0283 - [新瓜] "旅行青蛙"停服内幕：日方索要八位数版权费，95%收入归版权方
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0283

## Q0284 - 异环刮刮乐玩法在韩服下架
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0284

## Q0285 - [白银之城]宣发使用“那咋了”
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0285

## Q0286 - [米哈游] [崩坏：星穹铁道]石少半波流水78一路高歌猛进
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0286

## Q0287 - [米哈游] 原神日服历史首次飞榜，韩服历史首次飞游戏榜
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0287

## Q0288 - [米哈游]《原神》角色声音被“偷”获赔75万元，上海首例涉AI声音仿冒不正当竞争案宣判
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0288

## Q0289 - When 1.0 goes nice: Yet Another Zombie Survivors edition
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S0289
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0290 - 风暴要火！《风暴英雄》新英雄“萨拉塔斯”正式揭晓
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0290
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0291 - 《魔兽世界：无限》正式官宣：《魔兽世界》暴雪嘉年华消息汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0291
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0292 - 《炉石传说》新职业武僧公布，2V2模式同步揭晓
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0292
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0293 - 《暗黑破坏神5》正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0293
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0294 - 《暗黑破坏神》动画系列官宣，《暗黑破坏神4》将迎来全新赛季
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0294
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0295 - 《魔兽争霸3》重制版全新资料片“被遗忘的王国”公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0295
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0296 - 《守望先锋》全新辅助位英雄“血律”正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0296
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0297 - 《星际争霸》开放世界射击游戏官宣
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0297
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0298 - 2D 对战格斗游戏《MELTY BLOOD: TWI-LUMINA》定于27年4月22日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0298
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0299 - AL夺得《英雄联盟》LPL 2026总冠军
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0299
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0300 - 上海厂商下周正面PK新兴赛道；穿越火线研发商创始人离婚前妻分127个亿｜HOT周报
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0300
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0301 - 利用原神角色名牟利，被罚60万；法院：代充或将构成不正当竞争 | 一周说「法」
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0301
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0302 - 参加完TapTap今天的活动，我替被拷问的游戏人汗流浃背……
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0302
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0303 - [“Shadow of the Hero: Sword Debate” Salon Event Concludes Successfully] From Nostalgia to a New Market Segment: The Rise of the Martial Arts and Xianxia Game Genre
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0303
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0304 - How Does This Niche Solo Adventure Hook Players with Its Gentle Art Style and Souls-Like Gameplay? A Conversation with the Producer of *Journey to the Stars*
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0304
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0306 - Blizzard announces Netflix Diablo series, and Overwatch could be next
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0306
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0307 - Blizzard reveals open-world StarCraft shooter from ex-Far Cry boss
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0307
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0308 - Blizzard announces Diablo 5 for 2029 release
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0308
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0309 - BlizzCon 2026: Every announcement from Blizzard’s opening ceremony
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0309
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0310 - Blizzard announced Diablo and StarCraft games that are years away ‘to show confidence’
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0310
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0311 - Level 5 boss admits using AI for Professor Layton, Yo-Kai Watch reveals
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0311
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0313 - BlizzCon 2026 Opening Ceremony: All The Biggest Announcements And Games
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0313
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0314 - For The First Time In 6 Years, Blizzard Is Bringing A New Character To Heroes Of The Storm
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0314
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0315 - Diablo Animated Series Coming To Netflix, Other Blizzard Franchises Teased
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0315
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0316 - StarCraft Is Officially Back, But It’s Taking A Much Different Form
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0316
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0317 - Overwatch’s Newest Blood-Sucking Character Pushes The Game Even Further Into The Fantasy Genre
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0317
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0318 - Overwatch Is Reworking Two Of Its Most Criticized Characters
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0318
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0319 - Diablo 4’s Next Class Is What You Expect But Isn’t Coming With A Full Expansion
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0319
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0320 - Diablo 5 Is Coming In 2029, Will Actually Star Diablo
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0320
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0321 - Hearthstone’s First New Class In 4 Years And A More Story-Driven Journal Are On The Way
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0321
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0322 - WoW: The Last Titan Cinematic Ups The Stakes, But First, Xal’atath
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0322
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0323 - Warcraft Getting Its First New RTS Campaign In Two Decades–And It’s Playable Today
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0323
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0324 - WoW Forever Will Add All-New Content To Classic Azeroth This November
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0324
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0325 - Diablo 5’s Revealed Classes Are Throwbacks To Diablo 3, With One Exception
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0325
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0326 - Diablo 4’s Expansion Days Are Over
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0326
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0327 - 《inZOI》最新试玩+访谈：追求更深的模拟维度｜IGN 中国
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0327
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0328 - 《怪物猎人 荒野：凌越》「重弩炮」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0328
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0329 - 《暗黑破坏神5》先导预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0329
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0330 - 《守望先锋》「血律」角色预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0330
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0331 - 《魔兽世界：无限》公布预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0331
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0332 - 《星际争霸》先导预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0332
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0333 - 《魔兽争霸3 重铸版》「被遗忘的王国」预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0333
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0334 - 《怪物猎人 荒野：凌越》「长枪」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0334
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0335 - 《女神异闻录4 Revival》「小熊」介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0335
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0336 - itch 一周游戏汇：8月31日-9月6日（下）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0336
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0337 - Heroes of the Storm gets first new hero after supposed death and 6 year wait
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0337
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0339 - Blizzard announces animated Diablo show coming to Netflix
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0339
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0341 - Hearthstone just got its first new class in four years: Warcraft's fire-breathing panda Monk
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0341
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["NC一年投入逾3亿美元收购四家移动游戏公司｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0342 - Blizzard just dropped a new Warcraft 3 campaign, the first in 23 years
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0342
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "NC一年投入逾3亿美元收购四家移动游戏公司｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0343 - Overwatch's newest hero is a robo-vampire, and reworks are on the way for Roadhog and Sombra
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0343
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0344 - The WoW 'Classic+' rumors were true: World of Warcraft: Forever promises to be another timeline's version of the MMO
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0344
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0345 - No more Diablo 4 expansions are planned, but there's 'a lot of room' for more storytelling in the lead-up to Diablo 5
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0345
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0347 - Playing RTS with a controller? Total War: Warhammer 40,000 dev says it 'really does work' in their game: 'I think we've landed in a really solid spot'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0347
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0348 - Why is Blizzard still announcing games years ahead of release? 'We want to convey confidence in some of our biggest bets coming forward'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0348
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0349 - Beneath a Steel Sky review (1994)
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0349
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0350 - This remarkable mod transforms the most frightening horror game of the decade into Mirror's Edge
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0350
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0351 - As an OG Crazy Taxi lover, its new remake might just not be crazy enough
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0351
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0352 - Upcoming vampire RPG Nighthawks has been removed from Steam search and delisted in certain countries as Valve classifies it Adults Only: 'It's very bad news for us'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0352
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0353 - Ashly Burch, voice of Horizon's Aloy and star of Mythic Quest, is currently obsessed with Slay the Spire 2 and thinks videogames have too many stoic characters: 'I want more sh*tty little b*tches'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0353
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0354 - Inzoi's director says he is 'very much focused on our core goals' as he announces a multiplayer roleplaying mode designed to be like Ready Player One
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0354
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0355 - Peacock’s Friday the 13th Prequel Is Already Looking Like a Must-Watch
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0355
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0356 - 原创｜3年不见，暴雪憋大招：2款炸裂新作、多款史诗更新……这阵仗久违了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0356
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0357 - Sam Altman 表示同意 Dario Amodei 的放缓前沿主张，OpenAI 将同样开放独立评估者访问
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0357
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0358 - 英伟达是人工智能领域的"中央银行"
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0358
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0359 - Suno 发布 v6 音乐模型，推出 v6、v6-wild、v6-mini 三个版本
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0359
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0360 - OpenAI 发布 GPT-6 Astra 并展示社区构建案例
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0360
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0361 - Agent 长任务上下文工程解析：用预算控制、压缩、todo-state 和记忆对抗上下文溢出与目标丢失
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0361
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0362 - Anthropic 报告称胡塞组织用 Claude Code 开发导弹制导软件
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0362
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0363 - 星际争霸 开放世界新游 PC/主机 - 正式曝光，预计2030年上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0363

## Q0364 - 暗黑破坏神V PC/主机 - 正式曝光，宣传PV放出
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0364

## Q0365 - 植物大战僵尸杂交版-手机重制版 测试 - 新地图溪畔草坪上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0365

## Q0366 - The Legend of Dark Witch Episode 2: The Price of Desire now available for PS5
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0366

## Q0367 - [新瓜] 回旋镖:战舰少女联动南京舰疑似非官方机构联动
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0367

## Q0368 - [周边] [小瓜微甜]万代做原神周边，但是没写散兵名字，写了个等，目前被绝赞冲锋中
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0368

## Q0369 - [疑似内容] '求瓜 '无限暖暖新玩法与《别拽了！烤串师傅》高度相似，制作组决定先社媒发声
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0369

## Q0370 - [诡秘之主]一次又一次的宣传男人穿黑丝裙子跳舞
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0370

## Q0371 - [米哈游] 真珠实机演示，毛笔画出油画
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0371

## Q0372 - [厂商] [行业新闻] nexon二游新作和ba叛忍新作将在tgs同一展厅零距离对狙
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0372

## Q0373 - [新瓜]'启程！鸣潮巡游巴士'活动当天因不可抗力因素延期
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0373

## Q0374 - [白银之城]宣发使用“那咋了”
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0374

## Q0375 - [米哈游]脉脉米哈游同事圈有员工diss崩坏系列新作
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0375

## Q0376 - [米哈游] 原神日服历史首次飞榜，韩服历史首次飞游戏榜
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0376

## Q0378 - [米哈游] [崩坏：星穹铁道]石少半波流水78一路高歌猛进
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0378

## Q0379 - [新闻相关]蔡明为新游伊莫代言
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0379

## Q0380 - [碧蓝航线]碧蓝航线官方出手，下架大量抱枕等商品
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0380

## Q0381 - AL夺得《英雄联盟》LPL 2026总冠军
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0381
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0383 - 《寻星者：余晖‌》现已开启试玩Demo
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0383
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0384 - VR《Moss》系列开发商Polyarc Games宣布关闭
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0384
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0385 - 韩国击败沙特，夺得2026《守望先锋》世界杯冠军
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0385
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0386 - 小红花夺得《炉石传说》世界冠军赛冠军
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0386
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0388 - 肉鸽DBG《愚者接龙》正式亮相，首次内测同步开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0388
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0389 - 映泰推广12年前显卡GT 730，四路HDMI成最大卖点
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0389
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0391 - 直抵内心的“共情型心理悬疑 ADV”《中二病咨询室：第二现实译者》公布发售时间及定价
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0391
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0393 - 金铲铲五年，如何成为自走棋赛道的“标准答案”？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0393
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0394 - TapTap在上海把玩家与创作者，“聚”在了一起
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0394
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0395 - 当MMO集体焦虑蔓延，这款游戏却把“战斗爽”做成了另一种答案
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0395
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0396 - “投降还是另辟蹊径”？二游大厂《赛马娘》开发商Cygames要做小体量游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0396
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0397 - 游戏圈天价离婚案：《穿越火线》开发商老板“分割财产”，前妻获得127亿元
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0397
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0398 - 中年人发文：“42岁读研做游戏怎么样”？网友纷纷劝退：做游戏不认学历
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0398
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0399 - “游戏火了、却不是自己的”？Epic阻止UGC开发者注册商标：“不允许霸占类型名”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0399
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0400 - 分析：柠檬微趣 VS 点点互动，二合游戏谁做的更好？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0400
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0401 - 腾讯不要的团队做出爆款：《Wardogs》Steam首日34万在线、服务器挤爆
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0401
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0402 - 王俊凯、Uzi领衔明星赛，AL夺冠，英雄联盟15周年盛典落幕
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0402
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0403 - 必凡火树蓝飞闷声发大财，叠纸腾讯都掉队了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0403
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0404 - 上亿玩家走过15年，腾讯少有的现象级游戏难以复制
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0404
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0405 - 失业后自学游戏引擎，他一人用AI做游戏，在Steam新品节打败八成对手
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0405
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0406 - 64家游戏公司半年报：薪酬成本下降9亿，亏损的公司翻了一倍
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0406
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0407 - 恺英网络参股娱美德，传奇IP权属重构在即
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0407
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0408 - 独立创作者借AI发力，TapTap热门榜前十闯入3款“AI制作”游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0408
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0409 - 暴雪嘉年华：“魔兽世界2”、星际IP开放世界射击游戏、暗黑5全来了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0409
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0410 - 流浪地球IP射击新游曝光，旅行青蛙停运，《王者万象棋》畅销top5 | 陀螺周报
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0410
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《王者万象棋》定档9月10日，预约量突破7000万｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》上线首日登顶iOS免费榜，7000万预约转入实盘验证｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0411 - 2026LPL总决赛落幕，AL勇夺赛季总冠军！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0411
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0413 - 二次元的“内容”周期结束了吗
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0413
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0415 - 一家被腾讯“抛弃”的小工作室，做出了一个日流水超3.4亿的超级爆款
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0415
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0416 - 《伊莫》PC端预下载今日开启，9月16日，和3000万预约玩家“伊齐出发”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0416
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0417 - 机甲动作射击游戏《DARK MACHINE THE GAME》确认参展“东京电玩展2026”！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0417
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0418 - 恺英成为娱美德大股东，传奇IP生态实现“统一”闭环
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0418
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0419 - 王俊凯、Uzi领衔明星赛，AL夺冠，英雄联盟15周年盛典落幕
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0419
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0420 - 这波“江湖局”太会了！恺英双国风IP把三国和古龙搬进黄浦街头
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0420
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0421 - Has the "Content" Cycle in the Anime and Manga World Come to an End?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0421
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0422 - Kaiying has indirectly invested 2.1 billion yuan in Yumede, which holds 80% of the revenue from the Legend IP license.
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0422
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0423 - A small studio that was "abandoned" by Tencent created a smash hit generating over 340 million yuan in daily revenue.
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0423
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0424 - 制霸校园·战至巅峰｜AGA CS（北京）高校争霸赛开启招募！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0424
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0426 - 逐渐崩坏的童话冒险 ！《爱丽丝与彼岸》定档10月16日
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0426
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0427 - 解锁九月新玩法，AppGallery本月最佳应用和游戏盘点
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0427
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0429 - 首发登上Steam畅销榜第二，《东方》IP新作让STG再次伟大
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0429
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0430 - 下载破亿！字节在短剧继续卷，新APP冲到全球第7！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0430
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0431 - Moss developer Polyarc Games announces closure
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0431
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0432 - New StarCraft title to launch in 2030, will be an open-world FPS
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0432
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0433 - "What's the harm in asking?" – Dlala Studios on taking a big swing to get comedy legend Bob Mortimer for the upcoming game Murals
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0433
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "HarmonyOS游戏上架量超3.5万款，终端设备突破8500万台｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0434 - Roblox creators will soon be able to publish games on multiple platforms as standalone apps
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0434
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0436 - Why PG Connects Nordics is essential for developers, publishers and investors
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0436
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0437 - Hot Five: LEGO Digital Play acquires Offroad Games, Unity launches Claude Code plugin, and Pokémon Go is top grossing mobile game of early September
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0437
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Discord的《Battlefield 6》任务支持账户绑定与游戏进度同步｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "NC一年投入逾3亿美元收购四家移动游戏公司｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0438 - Roblox reveals 2026 Innovation Awards winners
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0438
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0439 - Report: 35% of game founders have decided against hiring because AI can do the work
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0439
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0440 - Diablo animated series in development at Netflix
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0440
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0441 - Take-Two's former head of AI Dr Luke Dicken to speak at PGC Nordics
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0441
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0442 - Monster Hunter Now makes $336.9m in three years on mobile
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0442
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0443 - Roblox unveils new play, creation and monetisation tools at RDC 2026
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0443
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Discord的《Battlefield 6》任务支持账户绑定与游戏进度同步｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "NC一年投入逾3亿美元收购四家移动游戏公司｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0444 - Worker-run studio KO_OP confirms layoffs
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0444
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0445 - Moss developer Polyarc has shut down
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0445
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0446 - The soft launch games you need to know about from Blizzard, Supercell, EA, Moon Active, Zynga and more
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0446
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0448 - Devolver Digital leaves AIM at £0.16 a share, five years after a £1.57 IPO, at ~0.6x revenue
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0448
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0449 - Last of Us Part 2 multiplayer mod ‘canceled by Sony’
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0449
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "中国游戏市场2025年首次突破500亿美元，小游戏占移动支出近两成｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "中国游戏市场2025年首次突破500亿美元，小游戏占移动支出近两成｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0450 - Video: Check out the multiplayer modes in Crazy Taxi World Tour in our PC footage
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0450
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0451 - Resident Evil film director says he ‘stripped out as much of the jokes as possible’ after test screenings
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0451
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0452 - The other Xbox 360 exclusive JRPG from the creator of Final Fantasy now has a PC port
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0452
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0453 - The Blizzard X CD Projekt Red collaboration continues with Cyberpunk outfits in Overwatch
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0453
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0454 - 15年后，《英雄联盟》继续穿越周期
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0454
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0455 - 专访《洛克王国：世界》叙事负责人：为什么我们想要和精灵之间发生故事？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0455
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0456 - 触乐怪话：再疯狂一次
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0456
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0457 - Poncle工作室群访：把“吸血鬼”系列变成大杂烩IP
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0457
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0458 - 从多元体验走向连接！TapTap玩聚节打通了玩家与开发者之间无形的墙
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0458
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0459 - 9月14日—9月20日共有29款游戏开测｜GameRes
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0459
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0460 - Blizzard Explains Why The StarCraft Shooter Coming In 2030 Was Announced Now
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0460
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0461 - StarCraft Reboot Is “Focusing On Single-Player,” Creative Director Says
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0461
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0462 - The StarCraft Shooter Is A Third-Person Game, And Blizzard Insists That You Have To Feel “Powerful”
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0462
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0463 - You’ll Fight The Protoss In StarCraft, Too, Don’t Worry
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0463
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0464 - First GTA 6 Actor Officially Confirmed, And It’s A Big Name
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0464
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0465 - Resident Evil Movie Director Comments On Physical Media Debate
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0465
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0466 - StarCraft: Release Date, Gameplay, And Everything We Know
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0466
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0467 - Release The Resident Evil: Whitest Kids ‘U Know Cut
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0467
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0468 - Resident Evil Movies Were On Ice Until Zach Cregger Came Along
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0468
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0469 - Diablo 5 Will Have The Most Classes Of Any Game In The Series
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0469
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0470 - Lies Of P’s Wizard Of Oz Tease May Have Just Gotten A Lot More Interesting
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0470
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0471 - Red Dead 2 Actor Shares A Gross Secret About The Game
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0471
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0472 - The Last Of Us 2 Multiplayer Mod Canceled “On Behalf Of Sony,” Dev Says
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0472
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0474 - Rockstar为防止泄露采取了极为严格的措施
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0474
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0475 - Insomniac回应金刚狼气味轨迹争议
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0475
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0477 - 印达·纳瓦雷特已有计划练好罗刹女的南方口音
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0477
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0478 - 开发者称没必要推出《魔兽世界2》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0478
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0479 - 《守望先锋》开发者确认猎空仍是游戏吉祥物
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0479
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0480 - 《暗黑破坏神》开发者对Netflix动画剧集感到非常兴奋
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0480
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0481 - 杰洛特皮肤将登陆《暗黑破坏神4》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0481
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0482 - 《暗黑破坏神4》「地狱遗赠」赛季实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0482
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0483 - 《战争机器：事变日》宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0483
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0484 - 《暗黑破坏神4》「地狱遗赠」赛季预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0484
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0485 - 《End of Abyss》开发幕后
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0485
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0486 - 《黎明行者之血》媒体赞誉宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0486
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《黎明行者之血》发售三天销量突破100万份｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rebel Wolves为《黎明行者之血》下一章招聘首席编剧｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0487 - 《猎杀：对决 1896》「血魔」预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0487
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0488 - 《间谍密令外传》实机预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0488
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0489 - 《编年史：中世纪》「战斗」概览预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0489
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0490 - 《怪物猎人 荒野：凌越》「斩斧」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0490
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0491 - 《暗黑破坏神5》已进入全面开发阶段，这里有6个新细节
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0491
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0492 - 《新蝙蝠侠2》片场照暗示猫头鹰法庭将出现
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0492
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0493 - 《异形：火力小队2》最终前瞻
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0493
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0494 - 《空战奇兵8 希孚之翼》剧情预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0494
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0495 - 本周 Steam 值得关注的游戏 09.14 - 09.20（一）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0495
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0496 - I've got a soft spot for cozy games with flying in them and these are my 4 favorites
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0496
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Double Fine脱离微软恢复独立，Schafer强调由团队自行承担存续责任｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0497 - After more than 400 hours of Valheim in early access, I love the journey from naked adventurer to godly Viking now more than ever
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0497
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Manor Lords》累计销量突破400万份｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Manor Lords》累计销量突破400万份｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0498 - My favourite soundtrack of 2026 so far is tucked in one of this year's biggest sleeper hits
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0498
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0499 - YouTuber runs onto the stage at Roblox Developers Conference shouting 'We deserve better,' gets tackled and ejected from show
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0499
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0500 - Fallout dev Tim Cain says the games industry's volatility is 'always gonna be around': 'What's happening now isn't novel, it isn't new'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0500
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Double Fine脱离微软恢复独立，Schafer强调由团队自行承担存续责任｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0501 - Discussing 20 years of Company of Heroes with the team carrying its torch into the future
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0501
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0502 - StarCraft is a narrative-driven shooter with 'a definitive ending' and 'not a seasonal game'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0502
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0503 - World of Warcraft Forever hype dampened by $30 elves: New Skyborne race locked behind expansion-tier purchase
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0503
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0504 - Warcraft 3: Reforged adds always-online requirement, removes LAN mode
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0504
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0505 - 10 big World of Warcraft Forever details from BlizzCon: No separate realms, optional transmog, and massively improved items
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0505
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0507 - Diablo 5 will fully support multiplayer, but Blizzard won't say how similar to Diablo 4 it'll be
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0507
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0508 - World of Warcraft: Forever devs say a direct sequel like Guild Wars 2 is unlikely: 'Why would you throw that away and start over?'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0508
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0509 - We tested the simple Windows 11 account bypass and it works. Just no-one tell Microsoft
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0509
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0510 - Talent calculators have already been assembled for World of Warcraft: Forever, and there's some real interesting stuff in here
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0510
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0511 - Thief designer Randy Smith Evergreen refused to work for Xbox because it would be like 'walking past some stakes with human skulls on them' and pretending 'it's probably fine in this direction'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0511
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0512 - Overwatch's newest hero is yet another example of how Team 4 is on a generational run
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0512
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0513 - World of Warcraft: Forever will get a hardcore mode by winter, say devs—which'll be interesting, given all the new and undiscovered ways to die
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0513
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0514 - That Last of Us 2 multiplayer mod everyone was looking forward to has been killed by Sony
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0514
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0515 - Redfall co-director Harvey Smith thinks Arkane 'never should have been working on a games-as-a-service game'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0515
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0516 - The RAMpocalypse support group
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0516
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0517 - 《早春晴朗》刷新国产剧出海新纪录，优酷国际版App「YOUKU」在全球多市场App Store的榜单排名攀升！
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0517
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0518 - 15年的LOL，怎么还在C？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0518
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0519 - DLSS 5时代来袭！技嘉RTX 50系显卡全系支持，影视级画面触手可及
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0519
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0520 - 技嘉猎鹰白金电源技术解析：ATX 3.1、氮化镓与白金认证三重加持
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0520
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0521 - 技嘉 GO27Q32 电竞显示器开售：尺寸随心切换，画面清晰无损
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0521
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0522 - 从全面和解到间接参股：恺英网络的跨国纠纷解法与长远棋局
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0522
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0523 - 这波“江湖局”太会了！恺英双国风IP把三国和古龙搬进黄浦街头
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0523
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0524 - 机甲动作射击游戏《DARK MACHINE THE GAME》确认参展“东京电玩展2026”！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0524
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0525 - 恺英成为娱美德大股东，传奇IP生态实现“统一”闭环
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0525
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0526 - 《伊莫》PC端预下载今日开启，9月16日，和3000万预约玩家“伊齐出发”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0526
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0527 - 投稿丨恺英网络参股娱美德，传奇IP权属重构在即
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0527
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0528 - Tomer Tunguz 解析 Amodei 放缓前沿提议背后的五派立场与算力监管难题
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0528
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0529 - 小红书 AllSpark 开源 Search Agent 模型 Iris，35B 与 397B 版本同量级成绩领先
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0529
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0530 - 恶意 AI 智能体攻击 RubyGems.org：YARD 执行任意代码与 Fastly 缓存密钥利用分析
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0530
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0531 - Anthropic 计划登陆纳斯达克，连续第二季度盈利瞄准 2 万亿美元估值
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0531
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0532 - 伊莫-9月23日上线 - PC预下载开启,9月16日上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0532

## Q0533 - 斗罗大陆：魂师对决 - 「神赐好礼」活动开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0533

## Q0534 - 穿越火线-枪战王者 - 「未命名潘多拉」活动上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0534

## Q0535 - 逆战：未来-S3赛季 - 【去往太空】活动开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0535

## Q0536 - 饥困荒野-26年内上线 - 参与活动领快爆专属背景框与头像框
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0536

## Q0537 - 燃烧纪元-预下载 - 09:00 预下载，9月15日上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0537

## Q0538 - 深色黎明：无垠 - 10:00 限量测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0538

## Q0539 - 篮下狂潮 - 10:00 正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0539

## Q0540 - 黑白之地-预下载 - 11:00 预下载，9月15日上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0540

## Q0541 - Beyblade X: EVOBATTLE for PS5 now available
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0541

## Q0542 - Rayman Legends Retold delayed to December 3
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0542

## Q0543 - Probably Stolen launches October 28
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0543

## Q0544 - Hull Rupture launches November 4
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0544

## Q0545 - Hozy coming to PS5, Xbox Series, and Switch in 2026; free DLC ‘Hideways’ now available
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0545

## Q0546 - FEROCIOUS now available for PS5, Xbox Series
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0546

## Q0547 - [周边] [小瓜微甜]万代做原神周边，但是没写散兵名字，写了个等，目前被绝赞冲锋中
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0547

## Q0548 - [新瓜] 群里看到的，妮姬这是？
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0548

## Q0549 - [紫龙] 梦幻模拟战开服8年联动20个日本ACG领域IP合集瓜汇总兼个人吐槽(若有因此想入坑的小伙伴请注意前十九个联动已绝版)
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0549

## Q0550 - [新瓜] "旅行青蛙"停服内幕：日方索要八位数版权费，95%收入归版权方
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0550

## Q0551 - [米哈游]脉脉米哈游同事圈有员工diss崩坏系列新作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0551

## Q0552 - [厂商] [库洛]库洛新作NAMI疑似正式注册为《不完全燃烧》(BurnNorBlaze)
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0552

## Q0553 - 异环刮刮乐玩法在韩服下架
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0553

## Q0554 - [米哈游] [瓜小味甜]崩铁水温节奏后新视频对白似乎意有所指，且视频评论区被b站标记提示
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0554

## Q0555 - [米哈游] [崩坏：星穹铁道]帽子戏法！崩铁短期内迎来第三次膨胀，虚构叙事三间血量已经达到两亿六千万，崩铁知名平民up主墨色长安表示他也打不过了
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0555

## Q0556 - [米哈游] 原神日服历史首次飞榜，韩服历史首次飞游戏榜
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0556

## Q0557 - [米哈游]《原神》角色声音被“偷”获赔75万元，上海首例涉AI声音仿冒不正当竞争案宣判
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0557

## Q0558 - [米哈游] [崩坏：星穹铁道]石少半波流水78一路高歌猛进
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0558

## Q0559 - [新瓜] 千年战争新角色疑似成为赛马娘玩家代餐
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0559

## Q0560 - [碧蓝航线]碧蓝航线官方出手，下架大量抱枕等商品
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0560

## Q0561 - Can Hideo Kojima make Xbox ‘cool’ – Here’s The Dring
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S0561
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0562 - 2026年消费电子市场洞察报告
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S0562
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0563 - tinyBuild Connect发布会消息汇总，《Kingmakers》公布超长演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0563
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0564 - 《巨蟹横行》与《Road to Jukai》正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0564
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0565 - 《守墓人2》现已推出试玩版
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0565
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0566 - 直抵内心的“共情型心理悬疑 ADV”《中二病咨询室：第二现实译者》公布发售时间及定价
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0566
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0567 - 自带91个职业的像素JRPG新游《幻想放置远征队》定档10月9日
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0567
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0568 - 肉鸽DBG《愚者接龙》正式亮相，首次内测同步开启
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0568
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0569 - 映泰推广12年前显卡GT 730，四路HDMI成最大卖点
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0569
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0570 - 小红花夺得《炉石传说》世界冠军赛冠军
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0570
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0571 - 《守望先锋》将与《赛博朋克：边缘行者》展开联动
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0571
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0572 - VR《Moss》系列开发商Polyarc Games宣布关闭
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0572
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0573 - 韩国击败沙特，夺得2026《守望先锋》世界杯冠军
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0573
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0574 - 彭博社透露索尼与小岛秀夫“分手”原因，工作室痛失Decima引擎
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0574
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0575 - 《寻星者：余晖‌》现已开启试玩Demo
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0575
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0576 - 1059美元起：Steam Frame现已开启预购
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0576
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0577 - 眼见不一定为实！推理悬疑解谜游戏《异病侦探》定档11月5日
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0577
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0578 - 《人类一败涂地》“监牢”地图正式上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0578
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0579 - 《雷曼：传奇再叙》延期至12月3日发售
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0579
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0580 - 【更新】《怪物猎人：荒野 凌越》公布新动作介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0580
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0581 - Team17携《破烂捡上天》与《Greak 2》亮相东京电玩展
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0581
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0582 - 网飞与世嘉达成合作，推出三部影视作品
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0582
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0583 - 【传言】英伟达60系显卡2027年上半年发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0583
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0584 - 登上畅销榜TOP5，《王者万象棋》凭什么让“不打牌的人”也上桌？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0584
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《王者万象棋》定档9月10日，预约量突破7000万｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》上线首日登顶iOS免费榜，7000万预约转入实盘验证｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0585 - 对话鬼谷制作人张三：“《鬼谷八荒 2》体量巨大，复杂度高100倍”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0585
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0586 - 从打官司到当“传奇大股东”，恺英拟花20.3亿元入股娱美德！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0586
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0587 - 暴雪放出“星际+暗黑”超级核弹，网易真要“躺赢了”？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0587
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0588 - 年度数据报告：用Godot引擎做游戏的都是啥人？如何在用
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0588
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0589 - 万字长文：10年收入涨100倍，“游戏圈奇迹”是如何做到的？
- exclude → industry_news；E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0589
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0591 - 外网热议：人人吹爆的“神作游戏”，为啥我玩不进去？网友：“你真不是唯一”！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0591
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0592 - 中国游戏巨头的第二战场，真不是AI游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0592
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0593 - 10年前最成功的射击大厂，另一款要憋30年？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0593
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0594 - 种田种到股价涨停？连亏两年后，这家公司靠闹鬼首月大卖6000万
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0594
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0595 - 游戏行业真正的「英雄」，做了十五年的异类
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0595
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0596 - 十年正值盛夏，KPL还在长出新故事
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0596
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0597 - 别再盯着百万销量了，Steam上真正养活小团队的是这些游戏……
- exclude → industry_news；E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S0597
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0598 - 24年后，48小时之外，Game Jam如何再生长
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0598
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0599 - KPL十周年活动持续落地，一城一闪打造各具特色的电竞“痛城”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0599
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0600 - Key Technical Staff Who Left Blizzard Are Teaming Up with Bilibili to Break the Unwritten Rules of the CCG Genre
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0600
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0601 - 冰封圣盾，魔女降临｜《地牢猎手6》全新玩法与养成系统同步登场
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0601
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0602 - 新女性向游戏来了？前《世界之外》制作人创业项目名称曝光
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0602
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0603 - 全新幻兽！魔域口袋版金秋双太白技能介绍
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0603
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0604 - 24 Years Later, Beyond the 48-Hour Mark: How Has the Game Jam Evolved?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0604
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0605 - Is a New Game for Women on the Way? Name of Startup Project by Former "Beyond the World" Producer Revealed
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0605
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0606 - 完美世界电竞再度于上海主办2027反恐精英世界锦标赛！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0606
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0607 - 灵犀互娱也有一款单机游戏在研？是三国SLG！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0607
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0608 - 《解限机》上线首个改装机，能挽救收入吗？
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0608
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0610 - Rockstar and IWGB outline arguments at start of tribunal
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0610
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0611 - More than 40% of people cancelling Xbox Game Pass, PlayStation Plus and Nintendo Switch Online subscriptions blame rising costs
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0611
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0612 - Valve opens waiting list for Steam Frame, starting at $1059
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0612
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0613 - Level-5 CEO admits using generative AI in recent showcase
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0613
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0617 - Why switching main characters for your game's sequel might be a mistake
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0617
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0618 - The latest speakers announced for PG Connects Nordics
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0618
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0619 - Roblox expands analytics tools with real-time alerts and player targeting
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0619
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0620 - App Store submissions open for Apple’s latest OS releases
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0620
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国App Store季度支出十年来首次下滑｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "App Store新管理层被曝寻求提高利润率与经常性收入｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0621 - 51% of game developers report player and revenue losses from cheating
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0621
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0622 - Level-5 CEO apologises after AI use in recent game trailers
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0622
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0623 - D2C isn't a payment method: Inside a webstore doing 70% of revenue
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0623
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0624 - Arcustin Games raises $500,000 in pre-seed funding
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0624
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《王者万象棋》定档9月10日，预约量突破7000万｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0625 - Sega expands transmedia strategy with Netflix Crazy Taxi film
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0625
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0626 - Trailmix on five years of Love & Pies: “There is no status quo in live service”
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0626
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0627 - Valve's Steam Frame pricing starts at $1,059
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0627
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0629 - Why does this prominent Washington state politician think video games can be 'soft power?'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0629
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0630 - Toy giant Mattel has set its sights on mobile – and it wants a Monopoly Go of its own
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0630
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0631 - King staff could strike after the Candy Crush maker rejects collective bargaining agreement
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0631
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0632 - Tetsuya Mizuguchi on the return of Lumines – and why premium games could bounce back
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0632
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0633 - You can now sign up to order Valve’s Steam Frame VR headset, it costs over $1,000 but includes Half-Life: Alyx
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0633
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0634 - Ubisoft delays Rayman Legends Retold weeks before planned release
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0634
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0635 - ‘Fans deserve this’: Sega is turning more of its games into movies with Netflix
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0635
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0636 - Fan PS5 boycott over discs seemingly has little impact in US
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0636
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0637 - Asha Sharma ‘has been personally responding to Xbox users’ support tickets’
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0637
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0638 - Lies of P studio Neowiz has filed a trademark for Wonders of O, an apparent Wizard of Oz themed sequel
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0638
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0639 - Phantasy Star Online is now fully playable in your web browser via PSO Reborn
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0639
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0640 - Katsuhiro Harada and SNK discuss their bold ambitions to ‘revive Japan’s golden era’
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0640
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0641 - Dragonheir: Silent Gods marks third anniversary with a hero its players helped create
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0641
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0642 - In less than a week Wardogs sells 2 million copies and achieves over 400k concurrent players
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0642
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0643 - 2017’s PvP action game For Honor is free to own for a limited time on Ubisoft Connect
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0643
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0644 - Steam Deck 2 plans still on track despite RAM crisis and higher prices
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0644
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0645 - 米哈游宣布停运的AI数字人，被一群玩家“赛博永生”了
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0645
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0646 - 触乐怪话：“你的时间不多了”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0646
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0647 - 《inZOI》制作人群访：做得艰难但不后悔
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0647
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0648 - 搜打撤的第二增长曲线：PVE模式价值研究
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0648
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0649 - 移动游戏“消失”的中间路线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0649
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["NC一年投入逾3亿美元收购四家移动游戏公司｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0650 - The Triple-I Initiative Showcase Is Getting A Second Event In 2026
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0650
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0651 - Wardogs Players Really Want You To Close The Doors … Or Else
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0651
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0652 - Overwatch’s Tracer Once Shot Lasers From Her Eyes, And It Could Happen Again
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0652
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0653 - Diablo 5 Isn’t Reinventing The Combat Wheel, It’s Making It Spin Even Faster
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0653
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0654 - Crazy Taxi Gets Crazier With Crazy Ex-Girlfriend Writers For New Movie
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0654
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0655 - How WoW Forever Handles Its Massive Set Of New Quests
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0655
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0656 - Wardogs Devs Are Watching Economy Cheaters Like Hawks
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0656
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0657 - Blizzard Says Diablo 5 Was Too Big To Be A Diablo 4 Expansion
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0657
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0658 - The Best Overwatch Heroes, According To Blizzard
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0658
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0659 - Diablo 5 Is Bringing Back Set Items, But Wants To Avoid Their Biggest Problem
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0659
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0660 - The WoW Forever Beta Starts This Week, Here’s How To Get Access
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0660
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0661 - WoW Devs Confirm Paladins Are A “Dad Class”
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0661
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0662 - Diablo 5 Doubles Down On The Darkness, But Hope Still Has A Place In Sanctuary
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0662
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0663 - Final Fantasy 7 Revelation Brings Back Snowboarding, And Red XIII Might Steal The Show Again
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0663
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0664 - 007 First Light’s Switch 2 Edition Delayed Yet Again, Here’s How Long You Have To Wait
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0664
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0665 - Final Fantasy 7 Revelation’s Director Kept Coming Back To The Witcher 3 For Inspiration
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0665
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0666 - Kingdom Hearts’ Kairi Has Suffered Enough, Will Now Headshot You In Fortnite
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0666
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0667 - GTA 6’s Stephen Root Is The Franchise’s Second-Ever Emmy Winning Actor
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0667
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0668 - PlayStation Plus Is Removing 7 Games Soon, So Play Them While You Can
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0668
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0669 - Big GTA 6 News Could Be Coming Up Soon
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0669
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0670 - 从《鬼武者 剑之道》看，为什么 Capcom 的游戏质量这么稳
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0670
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《鬼武者：剑之道》首日销量破百万，Steam简中评价占49.75%｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0671 - Steam Frame正式发布，售价1059美元起
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0671
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0672 - Steam Frame原本可能只要750美元
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0672
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0673 - Valve表示内存危机并未影响Steam Deck 2计划
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0673
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0674 - 《乡巴佬希尔一家的幸福生活》配音演员确认参演《GTA6》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0674
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0675 - 新商标疑似曝光《匹诺曹的谎言》续作名称
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0675
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0676 - 《漫威金刚狼》49分钟实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0676
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0677 - 《漫威金刚狼》评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0677
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0679 - 《雷曼：传奇再叙》将从10月延期至12月发售
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0679
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0680 - SteamOS距离支持Nvidia显卡驱动又近了一步
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0680
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0682 - 《我的世界：地下城2》宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0682
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0683 - Steam Frame配件介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0683
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0684 - Steam Frame介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0684
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0685 - 《Kingmakers》玩法解析视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0685
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0686 - 《Blackwood》概览预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0686
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0687 - 《深空当铺：可能是偷得》发售日预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0687
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0688 - 《升降梯外》剧情预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0688
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0689 - 《古墓丽影：亚特兰蒂斯遗迹》开发幕后
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0689
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0690 - 《漫威斗魂》总监为PC版糟糕首发表现道歉
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0690
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0691 - 分析师称PS「停玩抵制」未对活跃度造成明显影响
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0691
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0692 - XBOX CEO或曾亲自回复玩家客服工单
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0692
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0693 - 欧盟儿童法案或要求玩家游玩部分游戏前验龄
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0693
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0694 - 《漫威金刚狼》罗根演员不惧外界恶评
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0694
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0695 - 《怪物猎人 荒野：凌越》「太刀」武器介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0695
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0696 - 《Apex英雄》×《街头霸王6》联动预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0696
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0697 - 《空战奇兵8 希孚之翼》「HOUR ZERO」第一集
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0697
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0698 - 诺娃独立游戏通讯 2026-#37
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0698
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0699 - 本周 Steam 值得关注的游戏 09.14 - 09.20（二）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0699
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0700 - 一场创意、渠道、发行同台的“立项会”：如何打破小游戏增长的天花板?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0700
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0702 - Sombra's change to Support is the right move, but I fear some Overwatch players may take time to adjust
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0702
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0703 - YouTuber gets classic Tomb Raider running on a chip that sips a mere 1 W of power
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0703
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0704 - Someone made a copper gaming PC Frankensteined out of an old blowtorch and other assorted parts and is 'just going to let it tarnish over time'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0704
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0705 - Steam Frame review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0705
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0706 - Steam Frame starts at $1,059 and you'll want to enter the stock lottery before September 17 for a higher chance of getting one this year
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0706
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0707 - Valve working on Steam Frame strap that adds Index-like speakers and hot-swappable batteries, 'coming soon'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0707
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0708 - Valve targeted a lower price for the Steam Frame, then the memory crisis happened: 'I wish we could have shipped it at the price that we were at last year'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0708
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0709 - Forget GTA 6, I have brought GTA 5 closer to being the true greatest game of all time: Hulk – Ultimate Destruction
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0709
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0710 - Lies of P publisher files trademark for likely sequel 'Wonders of O'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0710
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0711 - Valve had next-gen VR 'headsets ready three, four years ago and they were big, bulky devices' but went back to the drawing board after actually putting them on
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0711
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["4399投资杭州深空之序，持股5%布局AI智能体｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "4399投资杭州深空之序，持股5%布局AI智能体｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=8｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0713 - The Steam Frame launches during one of the slowest periods for VR on Steam, but Valve hopes to 'rekindle the excitement' for PCVR
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0713
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0714 - Wardogs players are actively avoiding one team in particular: 'They are literally the dumbest people on the planet'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0714
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0715 - After nearly a year of silence following its last-minute delay, Kingmakers resurfaces with an extended gameplay video and new playtest
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0715
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0716 - Arc Raiders Expeditions may not come back: 'Maybe we'll scrap the whole system'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0716
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "Riot确认正在开发非免费游戏，商业模式将按产品定位选择｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0717 - Here's the Aniimo release time for your region
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0717
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0718 - The Steam Deck 2 has 'not really' been impacted by the memory supply crisis, with Valve still focused on a 'very delineated performance improvement' for its next handheld
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0718
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0719 - Admitting the OGL fiasco was a 'rug pull', D&D head says 'bluntly, we're recovering from a lot of missteps—very loud, very public missteps'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0719
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0720 - Dishonored director Harvey Smith thinks there's still room for big-budget immersive sims: 'When it really comes together and it has the budget behind it and the team, you end up with Deus Ex or Dishonored'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0720
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0721 - Nvidia CEO Jensen Huang tells Trump he agrees the AI doomsayers are perpetrating a hoax: 'you saw through all of that'
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0721
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0722 - Blizzard finally told players where the big sword in WoW went after 8 years, and I'm just bummed out a reveal this cool was in an interview somewhere
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0722
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0723 - CDPR wants to make The Witcher 3 Remastered feel like any other game released today: 'It's so easy to get used to these new improvements that it's hard to go back'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0723
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0724 - Toss a project at your printer: vibe coded tool allows developer to throw stuff at his 3D printer in VR to begin printing
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0724
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0725 - The best Total War game is getting a remaster with 50 newly playable factions, modern visuals, and a full Japanese voiceover
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0725
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0726 - Serial numbers on RTX Founders Edition graphics cards, including PC Gamer's very own, are fading and apparently it's causing a problem with RMA requests
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0726
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0727 - The Witcher 3's story director says an ideal quest is 'constructed in such a way that the player puts the controller away, stands up, and starts walking'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0727
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0728 - 上线仅半年的AI短剧黑马App「VibeShort」占据全球近90个市场iOS娱乐免费榜Top10！
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0728
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0729 - 《007 初露锋芒》(007 First Light) 支持路径追踪与 DLSS 光线重建，《伊莫》(Aniimo) 发布支持 DLSS 4.5
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0729
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0730 - 蚂蚁电竞750Hz助力FISSURE裂变天地3圆满收官，Legacy中国收获三连冠
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0730
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0731 - 一场快闪吸引5.7万年轻人奔赴，KPL十周年线下有何魔力？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0731
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0732 - Parent Guide to Back-to-School Screen-Time Discussions
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0732
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0733 - 观察丨《坦克世界》2026助农行动圆满收官：200辆爱心三轮车已驶入山西两县
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0733
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0734 - 硅基流动上线开源模型 Hy4 preview，770B 总参数、1M 上下文
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0734
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0735 - Apple 发布新一代 Apple Intelligence，Siri AI 正式以测试版上线
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0735
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0736 - DeepSeek-V4.1-Flash （Max） 进入 Agent Arena 开源模型第 3 名
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0736
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0737 - GPT-5.6 Luna 对比 GPT-6 Astra：$1.20 的模型做代码评审够用吗
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0737
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0738 - 科技巨头放缓 AI 开发的口头协议是安全共识还是卡特尔
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0738
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0739 - Vercel 将 inbound 销售团队从 10 人压缩至 1.25 人，AI 销售开发智能体年成本仅数千美元
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0739
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0740 - Artificial Analysis 评测：GPT-Live-1 以 81.5 分登顶 Speech to Speech Index
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0740
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0741 - 阶跃星辰发布 StepAudio 3 系列语音大模型，多款在 Artificial Analysis 榜单全球第一
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0741
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0742 - Anthropic 与 OpenAI 提议协调放缓前沿 AI 开发，Cohere CEO 等批评者质疑其真实动机
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0742
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0743 - Trail of Bits 批评 1Password 的 AI 补丁基准存在误导，并发布两个补丁验证 Agent 技能
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0743
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0744 - 404 Media 曝光 OpenAI 莉莉计划：人工审核 ChatGPT 聊天记录以优化模型
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0744
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0745 - 生数科技发布 Vidu S2：含 Avatar 与 Editing 双模型，探索空间视频
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0745
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0746 - Gergely Orosz 探访 OpenAI：Codex 驱动的智能体软件工厂
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0746
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0747 - 名将杀 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0747

## Q0748 - 地牢猎手6 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0748

## Q0749 - 彩虹六号：攻势 - 内测
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0749

## Q0750 - 沙巴克传奇-再战沙巴克 - 公测
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0750

## Q0751 - 漫威金刚狼 - 公测
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0751

## Q0752 - 激战2 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0752

## Q0754 - 仙侠世界2 - 资料片
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0754

## Q0755 - 前哨站4 - 已上线试玩
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0755

## Q0756 - 失落城堡2-10月22日上线 - 定档10月22日正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0756

## Q0757 - 怪物乐土-类宝可梦RPG - 限时15元折扣
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0757

## Q0758 - 新世界：暗影成双 - 定档9月23日正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0758

## Q0759 - 旅行奶蛙-玩家自制 - 已上线试玩
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0759

## Q0760 - 旅行青蛙离线版 - 已上线试玩
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0760

## Q0761 - 森盒 招募中 - 参与招募赢限量测试资格
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0761

## Q0762 - 花：小口琴 - 已上线试玩
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0762

## Q0763 - 蓝色星原：旅谣(官服) - 测试预下载开启,9月17日11点开测
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0763

## Q0764 - 阿瑞斯：钢铁先锋 - 海外上线,具体时间待定
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0764

## Q0765 - 燃烧纪元 - 09:00 正式上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0765

## Q0766 - 修仙时代 - 10:00 限量测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0766

## Q0767 - 全民萌兽-预下载 - 10:00 预下载，9月16日正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0767

## Q0768 - 宝石战争-预下载 - 10:00 预下载，9月16日上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0768

## Q0769 - 彩虹六号：攻势 PC/主机 招募中 - 11:00 开启国服限量测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0769

## Q0771 - 星海归旅人 - 18:00 预下载,9月16日开测
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0771

## Q0772 - Trinity Trigger DX now available for Switch 2
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0772

## Q0773 - 007 First Light for Switch 2 delayed to March 2027
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0773

## Q0774 - Jujutsu Kaisen Rumble: Survivaton delayed to 2027
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0774

## Q0775 - Psycho-Sleuth launches November 5
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0775

## Q0776 - [新瓜] 回旋镖:战舰少女联动南京舰疑似非官方机构联动
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0776

## Q0777 - [鸣潮](号主已证明非p图，就是官方自己点赞的)库洛官号点赞恋与深空新版本pv
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0777

## Q0778 - [周边] [小瓜微甜]万代做原神周边，但是没写散兵名字，写了个等，目前被绝赞冲锋中
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0778

## Q0779 - [新瓜]'启程！鸣潮巡游巴士'活动当天因不可抗力因素延期
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0779

## Q0780 - [新瓜]有手游角色当然是手游瓜，2025年度p站女角色投稿榜
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0780

## Q0781 - [米哈游] [崩坏：星穹铁道]帽子戏法！崩铁短期内迎来第三次膨胀，虚构叙事三间血量已经达到两亿六千万，崩铁知名平民up主墨色长安表示他也打不过了
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0781

## Q0782 - [鸣潮]库洛官方点赞恋与深空，原出处小红书已发帖澄清，非p图就是官方点赞
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0782

## Q0783 - [新瓜]有手游角色算手游瓜，2026年第一季度蓝p站作品数据统计
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0783

## Q0784 - [米哈游]脉脉米哈游同事圈有员工diss崩坏系列新作
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0784

## Q0785 - [藤子]王世杰员工迎来毕业季
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0785

## Q0786 - [厂商]造谣库洛周边官号的人已经删帖跑路去(你敢删我就继续发)
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0786

## Q0787 - [新瓜] 千年战争新角色成为赛马娘玩家代餐
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0787

## Q0788 - [新瓜] 奥黛塔声优收到威胁信
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S0788

## Q0790 - [新闻相关]蔡明为新游伊莫代言
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0790

## Q0791 - [碧蓝航线]碧蓝航线官方出手，下架大量抱枕等商品
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S0791

## Q0793 - QuestMobile 2026年文旅经济洞察报告：两大变化昭示用户旅游行为深层改变，文旅营销必须锚定用户需求精耕细作……
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S0793
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q0794 - 【传言】英伟达60系显卡2027年上半年发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0794
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0795 - Team17携《破烂捡上天》与《Greak 2》亮相东京电玩展
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0795
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0796 - 网飞与世嘉达成合作，推出三部影视作品
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0796
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0797 - 眼见不一定为实！推理悬疑解谜游戏《异病侦探》定档11月5日
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0797
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0798 - 《人类一败涂地》“监牢”地图正式上线
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0798
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0799 - 《雷曼：传奇再叙》延期至12月3日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0799
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0800 - 1059美元起：Steam Frame现已开启预购
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0800
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0801 - 《冲就完事了模拟器》X芭比联动正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0801
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0802 - 《宝可梦 Pokopia》荣获年度大奖：“日本游戏大奖2026”奖项名单汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0802
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0803 - 《Apex英雄》VS《街头霸王6》联动正式公布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0803
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0804 - 《全面战争：幕府将军2》完全版将于10月13日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0804
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0805 - 《荣耀战魂》免费领:育碧40周年庆典现已开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0805
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0806 - 《符文世界：龙之荒野》正式版现已推出，系列游戏首次登陆主机平台
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0806
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0807 - 【抽奖】双人联机卡牌游戏《友尽大冒险》今日正式发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0807
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0808 - 复古未来叙事RPG《以太与铁》将于2027年登陆PlayStation及Xbox
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0808
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0809 - 多人联机角斗肉鸽新作《链兽角斗》将于10月16日登陆PC及主机
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0809
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0810 - 喜加一：《暗黑破坏神Ⅳ》国服再度开启限时免费领取本体活动
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0810
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0812 - 桌游改编战术 RPG《霜港迷城》发布全新游戏玩法概览预告片
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0812
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0813 - 【更新】《怪物猎人：荒野 凌越》公布全武器种类合集视频
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S0813
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0814 - 《异于天堂》主题曲将于年内发布
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0814
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0815 - 《龙之信条2：黑暗觉者》公布新宣传片，10月9日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0815
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0816 - 《识质存在》的《洛克人》主题免费DLC将于9月17日免费上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0816
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0817 - Unity CEO：“游戏成本显著下降”，已在ICU的西方游戏公司还有救？
- exclude → industry_news；E3×R2+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0817
- scores: {"event": 3, "relevance": 2, "hook": 1, "total": 7}
- 事件3×相关2+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0818 - 大厂狂砸“微恐游戏”！腾讯光子《Higame》扩招，Krafton新游戏交作业
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0818
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0820 - CDPR联席CEO采访：蠢驴起源到巫师，“索尼下架2077是至暗时刻”
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0820
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0821 - 国外游戏人哀嚎：去年被裁失业半年、今年上班3个月又被裁，“我真顶不住了”！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0821
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0822 - 上线5天大赚近6个亿，对话战狗CEO：感谢腾讯当年狠狠地逼我们
- exclude → industry_news；E3×R3+M1=10；未达周报8分、属于历史重复或证据不足。
- source_ids: S0822
- scores: {"event": 3, "relevance": 3, "hook": 1, "total": 10}
- 事件3×相关3+钩子1 = 10；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0824 - 腾讯财报点名表扬的海外神作，背后是最懂中国玩家的老外？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0824
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0825 - 对话《吸血鬼幸存者》：想在中国拍IP短剧，希望和《黑猫警长》合作
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0825
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0826 - 8月出海榜：点点单款游戏月入6.7亿，三七《Last Asylum: Plague》1.7亿
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0826
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0827 - 六年后，波兰蠢驴CEO反思2077首发惨剧：不甩锅投资人，没人看见冰山
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0827
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0828 - 竞争规则改写的一年，该如何抬高小游戏增长的天花板？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0828
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0829 - 《坦克世界》2026助农行动圆满收官：200辆爱心三轮车已驶入山西两县
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0829
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0830 - 讲谈社物理新游《Legacy Code》Steam页面公开！入围TGS SOWN！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0830
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0831 - 《笑拉了，我家旁边是魔王城666》11月13日Steam EA发售，确认参展TGS！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0831
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0832 - 斗鱼《PEL奇遇时光三亚篇》圆满收官，热血竞技+趣味互动共建电竞内容新生态
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0832
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0833 - Adjust 发布《2026年日本移动应用趋势报告》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0833
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0834 - Six Years Later, the CEO of that Polish "idiot" Reflects on the 2077 Launch Disaster: No Blame on Investors, No One Saw the Iceberg
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0834
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0836 - 预算太高、回报不足，索尼和小岛秀夫“分手”的原因找到了？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0836
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0837 - NS2的首款独占双人游戏，除了“老一辈画风”外还有什么？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0837
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0838 - 上线当年月流水下滑至288万元，《庆余年》手游昨日宣布停运
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0838
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0839 - 广州奥术游戏成绩不达预期，被执行金额超百万、原股东已补偿母公司2500万
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0839
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0840 - 50人团队月入8500万元，中国AI陪伴的强敌！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0840
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0841 - Why the publisher of Nintendo Life is launching a new PC gaming site
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0841
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0842 - Bohemia Interactive takes minority stake in Everwind developer Enjoy Studio
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0842
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0843 - "I really want Criterion to be considered the best studio in the UK" – why the home of Burnout has a future with Battlefield
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0843
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0844 - 1312 Interactive raises $1m in seed funding round
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0844
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "国内游戏投融资回暖，上半年约50起事件｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0845 - STAN sees 15x growth in StanShop monthly buyers as repeat purchases hit 70%
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0845
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0846 - Cyprus ranks third globally for mobile game downloads
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0846
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0847 - Why most mobile games get LTV wrong at UA scale
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0847
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0848 - Kakao Games to acquire 39.56% of Me2on for $71.5m
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0848
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0849 - Piñata returns as independent creative studio after Metacore stint
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0849
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0850 - In The Hot Seat: Colossal Order's Mariina Hallikainen on leaving Paradox and life after Cities: Skylines
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0850
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0851 - September 2026's Movers and Shakers: Rovio, King, Trailmix, Tripledot, Apple and more
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0851
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0852 - Competition Appeal Tribunal approves £260m Google Play settlement with UK app developers
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0852
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0853 - Wardogs lead says the studio won't hire people who decry crunch on social media
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0853
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0854 - Bungie is overhauling Marathon from its original extraction shooter vision
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0854
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0855 - Roblox will allow devs to release games as standalone apps on other stores
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0855
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0856 - Activision Blizzard sued by former employee over sexual harassment
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0856
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0857 - Reform UK has launched a ‘stop the boats’ game in its iOS and Android app
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0857
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0859 - ‘We’re not transparent and we’re not honest,’ says Bulkhead CEO after Wardogs sells 2 million units
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0859
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0860 - Sega confirms that Sonic Racing CrossWorlds will still get free characters in Year Two, starting with Bayonetta
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0860
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0861 - The head of Nightdive Studios appears to be teasing a remaster of GameCube cult classic Eternal Darkness
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0861
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0862 - Two Point Museum is getting Rides & Relics DLC, which looks like a new Theme Park game in all but name
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0862
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0863 - Video: Here’s a look at the Wo Long 2 alpha demo, which is available today to mark its release date announcement
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0863
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0864 - Fire Emblem Fortune’s Weave Review: Nintendo’s most ambitious RPG yet is an incredible triumph
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0864
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0865 - Musicians including Travis Scott, Keith Richards and Future have started teasing that they’ll be in GTA 6
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0865
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0866 - ‘I’m definitely cooked’: A 9-year-old Minecraft YouTuber ran up a $118,000 ad bill using his dad’s company credit card
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0866
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0867 - 触乐怪话：有趣的叠加
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0867
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0868 - 新故事、新玩法与新坑：谈谈《共鸣：瘟疫传说传承》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0868
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0869 - 《Warframe》持续长青的秘密，藏在这次玩家见面会上
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0869
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0870 - 职业选手浅谈CS经济系统设计：宏观循环、微观机制与传达
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0870
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0871 - 不止《未眠野》，中国儒意的游戏版图逐渐浮出水面
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0871
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["成都小智游戏首曝《未眠野》，以双引擎构建可交互开放世界｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "成都小智游戏首曝《未眠野》，以双引擎构建可交互开放世界｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0872 - 《明明想要，为什么还是放弃？限时活动什么时候能真正促活》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0872
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0873 - 超2万人涌进方特乐园，KPL奇妙日把厦门变成了电竞主场
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0873
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0874 - Xbox Game Pass Gets 12 More Games In September
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0874
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0875 - Xbox Game Pass Removes 8 More Games Very Soon
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0875
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0876 - The Last Of Us Season 3 Is Probably The Final Season, HBO Says Yet Again
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0876
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0877 - James Pond Legacy Situation Is More Than Meets The AI
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0877
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0878 - Microsoft Reacts To Xbox Game Pass Rumor That Could Change The Service In A Big Way
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0878
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0879 - New PS5 Update Is Out Now, And Sony Actually Added Some New Features
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0879
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0880 - This Is How Blizzard Is Reducing Toxicity In Overwatch
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0880
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0881 - Zero Parades: Director’s Cut Revealed And PS5 Edition Release Date Announced
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0881
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0882 - Why Blizzard Stopped Protecting The Overwatch Formula To Save The Game
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0882
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0883 - Blizzard Boss On Why Diablo Is Becoming A TV Show And How Involved The Studio Will Be
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0883
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0884 - Resident Evil Director On Who Should Play Lady Dimitrescu In A Resident Evil Village Movie
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0884
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0885 - Bloodborne May Not Be Getting A Sequel Or Remaster, But How About An Umbrella?
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0885
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0886 - Fable Being “Vital To The DNA” Of Xbox Helped Shield The Game From Hardship, Director Says
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S0886
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0887 - 《一盏秋声：锦衣卫》上手前瞻：让人想起《卧虎藏龙》的类魂新品
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0887
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0888 - 《007 初露锋芒》Switch 2版再延期至2027年
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0888
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0889 - 《战狗》抢先体验5天销量突破200万份
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0889
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0890 - 《哈利·波特》剧集敲定亚瑟、桃金娘与科林演员
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0890
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0891 - Rockstar开始为《GTA6》预热原声阵容
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0891
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0892 - 《神鬼寓言》开发商称XBOX力保项目
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0892
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0893 - 《异形：火力小队2》Switch 2版延期至2027年初
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S0893
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0894 - 前《铁拳》总监原田胜弘谈VS Studio下一款游戏
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0894
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0896 - PS5版《控制：共振》游戏特性宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0896
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0897 - 《全面战争：幕府将军2 完全版》公布预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0897
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0898 - 《KEMURI》宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0898
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0899 - 《堡垒之夜》×《王国之心》联动预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0899
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0900 - 《我的世界》「奔赴荒野」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0900
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0901 - 《最终幻想 RESONANCE》「吉尔伽美什」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0901
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0902 - 《双点博物馆》「失落游乐园」DLC发售日预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0902
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0903 - 《收获日2》「即刻落锤」宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0903
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0904 - 《愚者不灭》「游戏流程」介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0904
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0905 - 《谜题工厂》公布预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0905
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0906 - 《火焰纹章 万缕千丝》介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0906
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0907 - 《植物大战僵尸》桌游10月开启众筹
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0907
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0908 - 樱井政博因无人接班停办游戏设计师奖
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0908
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0909 - 据称华纳兄弟后悔毁掉施奈德版本的DC宇宙
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0909
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0910 - HBO认为《最后生还者》剧集或将在第三季完结
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0910
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0911 - 《咒术回战 激斗: 幸存潮汐》宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0911
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0912 - 10分，《英灵神殿》1.0版评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0912
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0913 - 《泰拉瑞亚》主创访谈：玩家们的热情是我们持续开发的动力｜IGN 中国
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0913
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0914 - 《龙之信条2》「黑暗觉者」宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0914
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0915 - 《街头霸王6》「深红毒蛇」装扮4预告 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0915
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0916 - 《怪物猎人 荒野：凌越》宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0916
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0917 - NOVA海外独立游戏见闻 Vol.152
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0917
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0918 - 本周 Steam 值得关注的游戏 09.14 - 09.20（三）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0918
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0919 - Sega's ongoing effort to revive Crazy Taxi now appears to be taking the form of… a movie?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0919
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0920 - No, AI, you are not human: Microsoft's code of practice for artificial intelligence actually gives me some hope for the industry
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0920
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Double Fine脱离微软恢复独立，Schafer强调由团队自行承担存续责任｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0921 - If you need proof The Witcher 3's new expansion is in safe hands, its lead writer literally wrote her thesis on Hearts of Stone: 'To probably prove to some of my professors that games are worthy'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0921
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0922 - The Witcher 3 'is not untouchable,' story director says of the upcoming expansion and remaster: 'I still find some places that I think maybe nowadays, I would do it differently'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0922
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0923 - I am Mark Zuckerberg
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0923
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0924 - Diablo 4 player discovers secret Diablo 2 easter egg in its new throwback season and now everyone is wondering what else Blizzard hid in there
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0924
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q0925 - Wardogs delivers what Battlefield 6 was too console-brained to pull off: A real server browser
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0925
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Discord的《Battlefield 6》任务支持账户绑定与游戏进度同步｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0926 - Steam reverses porn game rating it mistakenly gave to an indie vampire RPG, and despite the stress it was a 'net positive' overall as wishlists on Steam 'basically doubled overnight'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0926
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0927 - Wardogs CEO says he won't hire devs who aren't down with crunch: 'If you care about what you're making, this is the place to work' (Updated)
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S0927
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0928 - As Skyblivion's launch approaches, the team is looking for help to get the word out
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0928
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《赛菲莉娅》1.0版销量达到56.42万份｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0929 - Blizzard is aware Overwatch fans are tired of seeing its fanciest skins go to the same heroes and it's 'the number one' thing it's working to fix next
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0929
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0930 - How to fish in Valheim
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0930
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0931 - I've been waiting all year for the 2nd Chapter to last year's best JRPG remake—it did not disappoint
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0931
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0932 - Trails in the Sky 2nd Chapter has one of the creepiest JRPG monsters I've encountered
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0932
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0933 - Where have all the RTX 5090s gone? Stock of the high-end GPU is disappearing from US online retailers
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0933
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0934 - Warlock: Dungeons & Dragons won't have waypoints, so that players can figure things out without 'blindly trusting' a UI
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0934
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0935 - Full body tracking could come to Steam Frame courtesy of this supercharged Base Station-like device that doesn't require headset support
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0935
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["NC一年投入逾3亿美元收购四家移动游戏公司｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0936 - Looks like SK hynix wants to make memory chips on US soil and it could work with Intel to do it
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0936
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0937 - Relic thought Company of Heroes 3's ambitious dynamic campaign would eventually come together, but it didn't: 'We bit off more than we could chew'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0937
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0938 - 'We can't stuff AI back in a box' says former US president Barack Obama, confirming he's 'not a doomer' while still calling for more government AI regulation
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0938
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0939 - The Witcher 3 producer says it's scary to work with another studio on the game's expansion: 'I also think twice about leaving my baby with someone'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0939
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0940 - Is Aniimo a gacha game?
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0940
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0941 - All active Aniimo codes for launch, September 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0941
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0942 - Bad news for shaman tank hopefuls—World of Warcraft: Forever won't have Season of Discovery's zany class design just yet: 'But never say never, y'know'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0942
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0943 - How to watch the PC Gaming Show Tokyo Direct 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0943
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Overwatch Rush》在菲律宾、马来西亚和印度尼西亚启动软发布｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0944 - Microsoft hasn't marched Fable to the guillotine because it's 'vital to the DNA' of Xbox, says the game's director
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0944
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Double Fine脱离微软恢复独立，Schafer强调由团队自行承担存续责任｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0945 - Ex-MS engineer reveals the story behind the infamous 'FCKGW' Windows XP key: 'Pirates started baking the key into images or just writing it on the CD with a Sharpie'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0945
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0946 - 累计下载量破千万的AR手游「怪物猎人Now」三周年活动上线即见效，日本等市场iOS榜单排名迅速攀升！
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S0946
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0947 - 技嘉OLED显示器：重塑视界，亮度与画质双重进阶
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0947
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0948 - 从性能到设计全面进化 AORUS GeForce RTX 5080 INFINITY产品解析
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0948
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0949 - LG显示器超级玩家嘉年华活动即将开启，高能玩家专属“双千”装备25G590B重磅亮相
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0949
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0950 - 《笑拉了，我家旁边是魔王城666》11月13日Steam EA发售，确认参展TGS！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0950
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0951 - 讲谈社物理新游《Legacy Code》Steam页面公开！入围TGS SOWN！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0951
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q0953 - Join The Hunt: Roblox 20
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S0953
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "8月全球手游Top 5内购均超1亿美元，《王者荣耀》重回1.5亿美元以上｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "Story Kitchen筹备三款Roblox游戏电影，覆盖《种植花园》等体验｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q0955 - Google 发布 TranslateGemma 等多语言 AI 成果，语言技术覆盖 300 多种语言
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0955
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0956 - Google DeepMind 发布 Gemini 3.8 Live 和 3.8 Live Extended Thinking
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0956
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0957 - Perplexity 自研 CobbleDB 替代 AWS DynamoDB，每年最多可节省一亿美元
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0957
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0958 - Arena 更新 Image-to-WebDev 榜单：GPT-6 Astra 以 1733 分登顶
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0958
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0959 - Grok Build 推出记忆功能，可跨会话保留项目约定与决策
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0959
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0960 - OpenAI 推出 ChatGPT Ads 新功能：Sponsored Agents 测试并集成 HubSpot 与 Shopify
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0960
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0961 - 微软 AI CEO 警告"模型福利"论调
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S0961
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q0962 - 三国：百将牌 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0962

## Q0963 - 交错战线 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0963

## Q0964 - 地下城与勇士：起源 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0964

## Q0965 - 天下：万象 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0965

## Q0966 - 天堂2：盟约 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0966

## Q0967 - 天涯明月刀 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0967

## Q0968 - 暗区突围 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0968

## Q0969 - 现代战舰 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0969

## Q0970 - 诛仙世界 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0970

## Q0972 - 三国：百将牌 - 新赛季「登坛问鼎」开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0972

## Q0973 - 五行游-国风三消对弈 - 定档9月24日下午15点正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0973

## Q0975 - 决胜巅峰(官服) - S42「十年逐星」新赛季开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0975

## Q0976 - 哈利波特：魔法觉醒 - 全新赛季限定卡池开放
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0976

## Q0977 - 地下城与勇士：起源 - “搜打撤”摸金玩法上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0977

## Q0978 - 异环-1.3版本(官服) - 开启1.4版本前瞻直播
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0978

## Q0979 - 斗破：莫欺少年穷-预下载 - 00:00 预下载，9月17日上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0979

## Q0980 - 火影忍者手游体验服 招募中 - 参与第41期招募赢体验服资格
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0980

## Q0981 - 率土之滨(官服) - 全新武将【5星·魏·许褚】登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0981

## Q0982 - 现代战舰-国服(官服) - 全新赛季“黑色飑风”开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0982

## Q0983 - 美职篮奇迹梦之队 - 开启删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0983

## Q0984 - 胜利女神：新的希望 - 新妮姬「贝斯蒂：战术升级」登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0984

## Q0985 - 全民萌兽 - 10:00 正式上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0985

## Q0986 - 宝石战争 - 10:00 正式上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0986

## Q0987 - 战争的挽歌 - 10:00 删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0987

## Q0988 - 星海归旅人 - 10:00 限量测试
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0988

## Q0989 - 最后的任务 - 10:00 删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0989

## Q0990 - 长夜守卫者 - 10:00 预下载，9月17日开测
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0990

## Q0991 - 闪耀吧！噜咪-预下载 - 10:00 预下载，9月17日上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S0991

## Q0992 - GungHo Online Entertainment announces party game Chit Chat Party! for Switch 2, now available
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0992

## Q0993 - Warota: I Live Next to The Demon King’s Castle LOL launches in Early Access for PC on November 13
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0993

## Q0994 - Big Break Showcase 2026 set for September 29 from Coffee Stain Publishing
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0994

## Q0995 - Neverness to Everness version 1.4 update ‘For Whom the Verses Mourn’ launches September 30
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0995

## Q0996 - Console Archives Crazy Climber launches September 17
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0996

## Q0997 - Terranigma launches January 14, 2027
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0997

## Q0998 - Arcade Archives Mr. Do!’s Castle launches September 17
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0998

## Q0999 - Witch the Showdown launches in Early Access for PC on November 19
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S0999

## Q1000 - The End of History launches in Q1 2027 for PS5, Xbox Series, and PC
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1000

## Q1001 - Wo Long 2: Wings of Ember launches March 4, 2027, alpha demo now available
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1001

## Q1002 - [杂谈][茶摊]实验型瓜田自动灌溉装置MK-VI
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1002

## Q1003 - [新瓜] 回旋镖:战舰少女联动南京舰疑似非官方机构联动
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1003

## Q1004 - [新瓜]黑暗王朝2.0？某浮力机认定碧蓝航线新皮肤“抄袭”她的“原创幽灵娘”
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1004

## Q1005 - [鸣潮](号主已证明非p图，就是官方自己点赞的)库洛官号点赞恋与深空新版本pv
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1005

## Q1006 - [瓜小味甜] [崩坏：星穹铁道] 游戏已经两年没有四星角色的产出了
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1006

## Q1007 - [周边] [小瓜微甜]万代做原神周边，但是没写散兵名字，写了个等，目前被绝赞冲锋中
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1007

## Q1008 - [新瓜]有手游角色当然是手游瓜，2025年度p站女角色投稿榜
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1008

## Q1009 - [鸣潮]库洛官方点赞恋与深空，原出处小红书已发帖澄清，非p图就是官方点赞
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1009

## Q1010 - [新瓜] "旅行青蛙"停服内幕：日方索要八位数版权费，95%收入归版权方
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1010

## Q1011 - [厂商]造谣库洛周边官号的人已经删帖跑路去(你敢删我就继续发)
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1011

## Q1012 - [新瓜]异环 前瞻出现自机角色手部问题
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1012

## Q1013 - [新瓜] 千年战争新角色成为赛马娘玩家代餐
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1013

## Q1014 - [新闻相关]蔡明为新游伊莫代言
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1014

## Q1016 - [异环][新瓜] 异环开播了，真的假的？我去真开播了
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1016

## Q1017 - 暗黑归瓜，不是你说谁给我打电话？
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1017

## Q1018 - [米哈游]《原神》角色声音被“偷”获赔75万元，上海首例涉AI声音仿冒不正当竞争案宣判
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1018

## Q1019 - [疑似内容]1999疑似考据失误，把野史当成了正式史
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1019

## Q1020 - [碧蓝航线]碧蓝航线官方出手，下架大量抱枕等商品
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1020

## Q1021 - [新瓜] 暗黑30周年新赛季给玩家们送上了两份大礼
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1021

## Q1022 - Is the game biz sustainable for the average indie dev?
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S1022
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q1023 - Beyond Balatro and taking risks: Why Playstack doesn’t want a 100% hit rate
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S1023
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q1024 - Sensor Tower 2026年8月全球手游收入与下载量排行榜 TOP 10
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S1024
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

## Q1025 - 炎王龙确认登场《怪物猎人荒野：凌越》：卡普空TGS发布会汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1025
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1026 - 《异于天堂》主题曲将于年内发布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1026
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1027 - 《龙之信条2：黑暗觉者》公布新宣传片，10月9日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1027
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1028 - 《识质存在》的《洛克人》主题免费DLC将于9月17日上线
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1028
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1029 - 【更新】《怪物猎人：荒野 凌越》公布全武器种类合集视频
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1029
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1030 - 桌游改编战术 RPG《霜港迷城》发布全新游戏玩法概览预告片
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1030
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1031 - 【抽奖】双人联机卡牌游戏《友尽大冒险》今日正式发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1031
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1032 - 复古未来叙事RPG《以太与铁》将于2027年登陆PlayStation及Xbox
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1032
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1033 - 多人联机角斗肉鸽新作《链兽角斗》将于10月16日登陆PC及主机
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1033
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1034 - 喜加一：《暗黑破坏神Ⅳ》国服再度开启限时免费领取本体活动
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1034
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1035 - 《卧龙2：凤火连天》定于27年3月4日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1035
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1036 - 《荣耀战魂》免费领:育碧40周年庆典现已开启
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1036
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1037 - 《符文世界：龙之荒野》正式版现已推出，系列游戏首次登陆主机平台
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1037
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1038 - 《Apex英雄》VS《街头霸王6》联动正式公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1038
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1039 - 《全面战争：幕府将军2》完全版将于10月13日发售
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1039
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1040 - 《冲就完事了模拟器》X芭比联动正式公布
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1040
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1041 - 《宝可梦 Pokopia》荣获年度大奖：“日本游戏大奖2026”奖项名单汇总
- merge → industry_news；同URL重复采集，合并到已审阅候选。
- source_ids: S1041
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；merge
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1042 - 《双点博物馆》失落游乐园扩展包将于10月8日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1042
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1043 - 《骑士盘骑士》全新Steam试玩版现已上线
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1043
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1044 - Steam周销量排行榜:《战狗 WARDOGS》登顶|2026年9月第2周
- exclude → industry_news；E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S1044
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1045 - 《另一个伊甸：起源》今日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1045
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1046 - 《UN:Me（非我：择谁）》延期至27年发售
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S1046
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1047 - 《战锤40K：战争黎明4》公布最新战报，介绍2v2团队占点控制
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1047
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1048 - 末日度假村模拟游戏《罗马流沙 RE:Build》正式发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1048
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1049 - 《爱氏物语》NS版今日发售，同步公开TGS2026参展信息
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1049
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1050 - IGN十分：《火焰之纹章：万缕千丝》媒体评分汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1050
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1051 - 小岛秀夫公布谍报动作游戏《PHYSINT》主角人选
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1051
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1052 - 《古神 风里希》公布最新预告：Xbox TGS2026发布会消息汇总
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1052
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1053 - 沈阳叙事解谜游戏《希望之城》将于11月10日发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1053
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1054 - 月增100万！《影之刃零》全平台愿望单突破300万大关
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1054
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1055 - 科幻现实冒险游戏《法拉第蓝》公开
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1055
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1056 - 完整单人模式来了：开放世界生存游戏《沙丘：觉醒》主机版抢先体验已开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1056
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1057 - 小游戏迈入转型关键期，越来越多开发者在vivo抢到了先机
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1057
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1058 - 不差钱的博士大佬：“自从开发独立游戏，我遇到了中年危机”，同行都笑了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1058
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1059 - 15年了，《英雄联盟》凭什么还能长青？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1059
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1060 - 被腾讯“放走”的《Wardogs》5天爆卖200万套！Steam 42万人在线，新股东增持
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1060
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1061 - “反向鸡娃”？老爸掏出《黑神话》《战神》劝玩，10岁儿子却只想看不想玩
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1061
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1062 - 《异环》国际服被DDoS打到停服维护，完美向玩家发补偿
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1062
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1064 - 对话鬼谷制作人张三：“《鬼谷八荒 2》体量巨大，复杂度高100倍”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1064
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1065 - “AI两天码500万字”，网文圈怒了：唐家三少发声，平台下场整治
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1065
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1066 - 对话《湮灭之潮》陈琦：一支成都团队为何要死磕亚瑟王？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1066
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1067 - 史上最大规模东京TGS，今天根本挤不动
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1067
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1068 - 50多岁被裁员，对话模拟经营赛道鼻祖：我们正准备做手游
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S1068
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1069 - 两年82亿：独游爆款全球捞金，何时轮到中国人？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1069
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1070 - 4个月融资近7亿，游戏大厂领投：这家AI公司想挖游戏人？
- exclude → industry_news；E3×R2+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S1070
- scores: {"event": 3, "relevance": 2, "hook": 1, "total": 7}
- 事件3×相关2+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1071 - 被腾讯放弃后，首日销量125万，这款FPS让玩家抢着开“货拉拉”
- exclude → industry_news；E2×R3+M1=7；未达周报8分、属于历史重复或证据不足。
- source_ids: S1071
- scores: {"event": 2, "relevance": 3, "hook": 1, "total": 7}
- 事件2×相关3+钩子1 = 7；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1072 - 电魂网络董事长离婚，前妻分走近1亿元股份
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1072
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1073 - 创作者月入超10万，AI UGC游戏平台依旧算不上好生意
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1073
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1074 - 全球游戏外挂市场85亿美元，有人靠作弊赚7700万美元
- exclude → industry_news；E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S1074
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1077 - 终焉之战打响，新干员参战！《轮回保险公司 R.I.P》正式版发售
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1077
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1078 - 游族网络布局先进封装 联合发起谛疆科技先进封装项目
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1078
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1080 - 腾讯Supercell前成员的创业公司解散，游戏疑似移交字节运营
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1080
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1081 - Here are the first finalists for the 2026 GamesIndustry.biz Best Places To Work Awards UK
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1081
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1082 - MindsEye developers report new round of layoffs at Build A Rocket Boy
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S1082
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1083 - Shinji Mikami to be inducted into the AIAS Hall of Fame later this week
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1083
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1084 - Heart Machine faces possible closure after publishing deal falls through; majority of staff laid off
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S1084
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1085 - Remedy's Arhi Makkonen on designing the "biggest world we have ever done" for Control Resonant
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1085
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1087 - "Every major publisher has approached us to review their old Kinect and Wii catalogue" – Nex Playground is spoilt for choice as its international rollout continues
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1087
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1088 - Draft of new EU law proposes sweeping restrictions on online games
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1088
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1089 - Five reasons you might think PG Connects London isn't for you - and why it is!
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1089
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1090 - Meet the next generation of developer talent at PG Connects Jordan
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1090
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1091 - Black Salt Games unveils new studio Team Trifold
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1091
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1092 - Abu Dhabi University partners with Pearson on video game design degree
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1092
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["中国游戏市场2025年首次突破500亿美元，小游戏占移动支出近两成｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "中国游戏市场2025年首次突破500亿美元，小游戏占移动支出近两成｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1093 - Jonathan Knight takes expanded chief games officer role at The New York Times
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1093
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1094 - The EU Kids Act could restrict social media, AI chatbots and games for young people
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1094
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1095 - Monster Hunter Outlanders unveils more monsters as 5m pre-registrations achieved
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1095
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1096 - Naphora managing director on rebuilding the studio, going mobile-first and building globally competitive games
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1096
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1097 - “Apple's new foldable changes the canvas iOS developers are designing for”: The Mobile Mavens on the iPhone Duo
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1097
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Eddy Cue接管App Store，Apple Arcade同步并入同一汇报线｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "美国App Store季度支出十年来首次下滑｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "App Store新管理层被曝寻求提高利润率与经常性收入｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1098 - Ludus: Merge Arena surpasses $50m in lifetime revenue
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1098
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell签署Metacore收购协议，《Merge Mansion》团队月底并入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Garena开放世界手游《Free City》扩展至菲律宾等市场测试｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell签署Metacore收购协议，《Merge Mansion》团队月底并入｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "《超自然行动组》与Garena达成合作，计划进入东南亚和拉美｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1099 - Kalank secures €1.5m funding round to accelerate international expansion
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1099
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["国内游戏投融资回暖，上半年约50起事件｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1100 - Brawl Stars and Duolingo launch global mascot crossover
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1100
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1101 - Shinji Mikami to join AIAS Hall of Fame at 2026 DICE Awards
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1101
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1102 - Report: MindsEye developer Build a Rocket Boy seemingly closing after more layoffs
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S1102
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1103 - Hyper Light Drifter developer Heart Machine has laid off the majority of staff
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1103
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1105 - On the podcast: That EA-Scopely supergroup, Reform’s mobile game, King strikes, Mattel, Roblox, Mizuguchi, more
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1105
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1106 - Supercell and Duolingo reveal new Brawl Stars crossover
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1106
- scores: {"event": 0, "relevance": 3, "hook": 0, "total": 0}
- 事件0×相关3+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell签署Metacore收购协议，《Merge Mansion》团队月底并入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell制作人Lasse Seppänen离职并计划成立新工作室｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell制作人Lasse Seppänen离职并计划成立新工作室｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell签署Metacore收购协议，《Merge Mansion》团队月底并入｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "Supercell控股的Trailmix完成CEO交接，创始人转任执行主席｜weekly 2026-09-04_to_2026-09-10｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1107 - Doki Doki Literature Club is returning to Android through the Epic Games Store
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1107
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1108 - MindsEye studio Build a Rocket Boy may be closing down, according to reports
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1108
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1109 - Disney Dreamlight Valley’s next expansion The Keepsake Sea plunges new depths, but in the best way possible
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1109
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1110 - The War Thunder team looks back on 14 years of service: from planes and ponies to tanks, choppers, and even frontline infantry
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1110
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《赛菲莉娅》1.0版销量达到56.42万份｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1111 - Sony responds after PC games including Helldivers 2 disappear in UK
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1111
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1112 - Monster Hunter Wilds will stop charging players to change their character’s appearance
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1112
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1113 - Zach Cregger’s Resident Evil film becomes the highest rated video game movie in Rotten Tomatoes history
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1113
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1114 - Pennywise actor Bill Skarsgård will play the lead role in Hideo Kojima’s Physint
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1114
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1115 - Kojima gives an update on OD while thanking Xbox for ‘believing in our vision’
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1115
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1116 - Grand Theft Auto 6 is getting a vinyl, CD and streaming soundtrack with 34 original tracks
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1116
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1117 - What time does EA Sports FC 27 go live? Digital release time in your region and New Zealand trick
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1117
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1118 - 触乐怪话：我开始像人机了
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1118
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1119 - 在追求玩家体验的道上，《鸣潮》已经“走火入魔”
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1119
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1120 - 爆款独立游戏的开发商，能否玩转发行业务？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1120
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1121 - 暴雪娱乐能成为百年游戏老店么？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1121
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1122 - Call Of Duty: Black Ops Dev Teases “Something That Nobody’s Ever Experienced Before”
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1122
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Frontier与Disney合作开发创意模拟经营新作｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《CookieRun: Crumble》全球上线四周收入突破1400万美元｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜daily 2026-09-09_to_2026-09-09｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "Frontier自有IP模拟经营新作进入全面开发｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1123 - Fire Emblem: Fortune’s Weave’s Fantastic Reviews Have Me Feeling FOMO
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1123
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1124 - Lego Batman: Legacy Of The Dark Knight Gives Harley Quinn An Arkham Asylum Makeover
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1124
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "乐高移动游戏团队收购《Chrome Valley Customs》开发商｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1125 - Resident Evil Is Now The Highest-Rated Gaming Movie Ever
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1125
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1126 - Resident Evil Director Was In Horrible Pain Making The Movie
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1126
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1127 - Metroid Ravenous Logo Memes Make Phrases Like “Girl Dinner” And “They Took My Ass” Look So Metal
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1127
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1128 - Xbox At Tokyo Game Show 2026: All The Biggest Announcements And Trailers
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1128
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1129 - Kingdom Hearts Has Invaded Fortnite, And There’s A Lot To Collect
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1129
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1130 - Hideo Kojima’s Physint Casts Bill Skarsgard As Its Lead
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1130
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1131 - GTA 6 The Album Gets A Physical Release, Even Though The Game Won’t
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1131
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1132 - MS Flight Sim Adds New Plane That Costs More Than The Game, And It Includes “Waste” Simulation
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1132
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["集英社游戏公布《征服纪：臣民之心》，结合殖民模拟与4X策略｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "集英社游戏公布《征服纪：臣民之心》，结合殖民模拟与4X策略｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1133 - Physint Release Date-Estimate, Gameplay, And Everything We Know
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1133
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1134 - GTA Is Like Barbie, Take-Two Boss Says
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1134
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1135 - Game’s Price Is Lower Because This Fall Is So Packed, Dev Admits
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1135
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["1047 Games停止两款射击游戏开发，转向点对点托管｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "CAA推出Frame1Games，为独立游戏提供资金与市场支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "《PoE2》1.0定于12月上线并转免，国服安排晚一周｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "Savvy Games Group首任CEO Brian Ward卸任｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1136 - GTA 6 Boss Says PC Is Becoming “More And More Important”
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1136
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1137 - GTA 6 Multiplayer Could Launch In 2027, Twitch CEO Says
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1137
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1138 - I Played WoW: Forever On A Controller, And That’s Big News
- exclude → industry_news；正文为空或仅有短摘要，不能作为终稿事实证据。
- source_ids: S1138
- scores: {"event": 0, "relevance": 0, "hook": 0, "total": 0}
- 事件0×相关0+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1139 - PS5推出新系统更新，「增强PSSR图像质量」默认开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1139
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1140 - 《火焰纹章 万缕千丝》开发者解释为何只有一个存档位
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1140
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1141 - 《ONE PIECE 海洋盛宴》试玩前瞻：双厨狂喜｜IGN 中国
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1141
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1142 - 传XGP将取消首日入库，微软称尚未敲定
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1142
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1143 - 《心之眼》开发者称遭裁员，公司前景存疑
- exclude → industry_news；E2×R1+M1=3；未达周报8分、属于历史重复或证据不足。
- source_ids: S1143
- scores: {"event": 2, "relevance": 1, "hook": 1, "total": 3}
- 事件2×相关1+钩子1 = 3；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1144 - Treyarch或将告别《黑色行动》
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1144
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1145 - 《战狗》Steam发售初期销量增速惊人
- exclude → industry_news；E2×R2+M1=5；未达周报8分、属于历史重复或证据不足。
- source_ids: S1145
- scores: {"event": 2, "relevance": 2, "hook": 1, "total": 5}
- 事件2×相关2+钩子1 = 5；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1146 - 《蟹蟹狂想曲》试玩Demo宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1146
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1147 - 《生化危机》之父三上真司将入选D.I.C.E.名人堂
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1147
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1148 - 《光明旅者》开发商Heart Machine因发行商撤资裁掉「几乎所有人」
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1148
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1149 - 《火焰纹章 万缕千丝》44分钟实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1149
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1150 - 《战锤40K：战争黎明4》「2v2团队占点」实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1150
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1151 - 《最终幻想 RESONANCE》最终预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1151
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1152 - Switch 2版《暗黑破坏神4：憎恨时代合辑》宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1152
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1153 - PS5版《寂静岭：Townfall》游戏特性宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1153
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1154 - 《识质存在》「洛克人包」宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1154
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1155 - Switch 2版《乐高蝙蝠侠：黑暗骑士之遗》发售预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1155
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1156 - 《勇者斗恶龙 怪物仙境4 枯木国的碧安卡与芙萝拉》介绍视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1156
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1157 - Switch 2版《暗黑破坏神4》实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1157
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1158 - Spotify投放广告牌，疑似预告《GTA6》合作
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1158
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1159 - 《后室》导演参观Valve办公室，引发《传送门》电影猜测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1159
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1160 - 《小小大星球》开发商据称开发类《动森》新作
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1160
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1161 - PLAYISM 携众多新品参展 TGS 2026：小体量大舞台
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1161
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1162 - 《卧龙2：凤火连天》试玩版45分钟实机演示
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1162
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1163 - Steam Frame评测
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1163
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1164 - 《疯狂出租车：极速环游》「日本」地图宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1164
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1165 - 小岛工作室《OD》《PHYSINT》新作信息 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1165
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1166 - 《使命召唤：现代战争4》战役模式宣传视频 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1166
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜daily 2026-08-31_to_2026-08-31｜card_exposed=true｜card_rank=3｜card_limit=10｜card_exposure_source=publish_log_manifest", "前《使命召唤》设计师七周完成移动撤离射击游戏｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1167 - 《Edge of Memories》发售日预告 | TGS 2026
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1167
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1168 - 距离《暗黑破坏神 5》还有两年半，《暗黑 4》准备怎么撑下去？距离《暗黑破坏神 5》还有两年半，《暗黑 4》准备怎么撑下去？｜IGN 中国
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1168
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1169 - 所有过往，皆为序章！育碧 40 周年庆典现已开启
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1169
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1170 - 《消逝的光芒：困兽》周年宣传视频
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1170
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1171 - 《控制：共振》发售预告
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1171
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1172 - 全息甲板上的哈姆雷特，二十年后
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1172
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1173 - 本周 Steam 值得关注的游戏 09.14 - 09.20（四）
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1173
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Steam付费游戏前1%拿走84.5%预估收入｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》封测Steam同时在线突破20万，团队以3000至5000人为长期目标｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=6｜card_limit=10｜card_exposure_source=publish_log_manifest", "网易投资的《黎明行者之血》全球发售，首日登顶Steam全球畅销榜｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=2｜card_limit=10｜card_exposure_source=publish_log_manifest", "前网易、库洛和华为成员组队开发《爱机修》，Demo获Steam 95%好评｜daily 2026-09-07_to_2026-09-07｜card_exposed=true｜card_rank=1｜card_limit=10｜card_exposure_source=publish_log_manifest", "《Wardogs》第二轮测试Steam峰值超过24万｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1174 - 传送带消除还能怎么创新？Rollic 这款新消除就藏了这么多新设计？
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1174
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1175 - Balatro developer LocalThunk turns up on Discord to talk about the 1.1 update and life after burnout: 'I truly am having the best time making the game now'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1175
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Discord的《Battlefield 6》任务支持账户绑定与游戏进度同步｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1176 - GTA 5's 'Become a celebrity' mod is almost weirdly fully featured
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1176
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=9｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1177 - World of Warcraft: Forever beta launch times: How to sign up and play Blizzard's twist on WoW Classic
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1177
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1178 - MindsEye developer Build a Rocket Boy may finally be closing
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1178
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1179 - 'The best videogame movie' ever? The first reviews of Zach Cregger's Resident Evil adaptation are absolutely glowing
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1179
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1180 - Marathon creative director shoots down rumored merge with Destiny 2: 'Please don't believe everything you read online'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1180
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1181 - Hyper Light studio Heart Machine lays off 'nearly everyone' after publishing deal for unannounced game falls through
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1181
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《弧光猎人》国服首测验证需求，国内团队已超百人｜daily 2026-09-01_to_2026-09-01｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "《恶意不息》1.0版延期至2027年3月｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "《致命视角》0.8版带动Steam峰值接近3.9万，累计销量超250万套｜daily 2026-09-08_to_2026-09-08｜card_exposed=true｜card_rank=7｜card_limit=10｜card_exposure_source=publish_log_manifest", "索尼退出《Physint》合作，Xbox接手并将关系延伸至影视｜weekly 2026-09-04_to_2026-09-10｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1182 - Get a good look at Control Resonant's otherworldly bosses in a PC Gaming Show exclusive extended interview
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1182
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1183 - Endless Legend 2 review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1183
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1184 - The leakers disagree, but we might just get one AMD-shaped mid-range GPU through all of 2027
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1184
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1185 - WoW Forever dataminers have dug up set bonuses, which are interesting even on low-level gear
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1185
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1186 - AMD presents new method of handing indirect lighting off to an image generation model: 'frame-by-frame' solution could be part of AMD's answer to DLSS 5 someday
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1186
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["Aggro Crab成立发行品牌，单项目预算上限50万美元｜daily 2026-09-02_to_2026-09-02｜card_exposed=true｜card_rank=10｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods接手SteamDB并承诺保持免费｜daily 2026-09-02_to_2026-09-02｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务｜weekly 2026-08-28_to_2026-09-03｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest", "Nexus Mods母公司收购SteamDB，承诺不设广告与付费墙｜weekend 2026-09-04_to_2026-09-06｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1187 - FF14's new roguelike mode's leaderboards were accidentally encouraging players to min-max all the fun out of it, so it'll be 'postponing the start of Crucible Rankings'
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1187
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1188 - Dishonored's Harvey Smith named his new studio Black Pony Immersive so people would stop asking him to work on other genres: 'Specialising on what you love is not a bad path'
- exclude → industry_news；E3×R1+M1=4；未达周报8分、属于历史重复或证据不足。
- source_ids: S1188
- scores: {"event": 3, "relevance": 1, "hook": 1, "total": 4}
- 事件3×相关1+钩子1 = 4；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1189 - LG UltraGear 25G590B review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1189
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1190 - HP Omen 35L (2026) review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1190
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["怪物收集RPG《磁带妖怪2002》定档2027年3月｜weekend 2026-08-28_to_2026-08-30｜card_exposed=false｜card_rank=None｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": false}

## Q1191 - iBuyPower RDY Scale B06 review
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1191
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1192 - The lead developer of the PS5 Linux project has abandoned ship: 'It is just a bunch of noobs using LLMs and writing hacks they don't even understand':
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1192
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekend 2026-08-28_to_2026-08-30｜card_exposed=true｜card_rank=4｜card_limit=10｜card_exposure_source=publish_log_manifest", "暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net｜weekly 2026-08-28_to_2026-09-03｜card_exposed=true｜card_rank=5｜card_limit=10｜card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true}

## Q1193 - Industry vet who worked on Ultima Online says the next big thing needs to have 'sh*tty graphics' to escape the doom of rising development costs
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1193
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1194 - 上线即登上美国App Store免费榜Top2，Meta推出的首款个人AI智能体「Muse」真的火了！
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1194
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1195 - DDR5大容量装机需求升温 技嘉D5 Single Boost带来单条高频新选择
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1195
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1196 - 千帧战力加持，EVNIA弈威25M4P5200T燃动Vitality无畏契约分部粉丝见面会
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1196
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1199 - TRYX创氪星系携手CAPCOM推出与《生化危机》系列、《Pragmata》联名限定产品
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1199
- scores: {"event": 0, "relevance": 1, "hook": 0, "total": 0}
- 事件0×相关1+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1200 - 观察｜三七互娱携手珠江医院发布“知愈光年”功能游戏以AI支持认知训练应用
- exclude → industry_news；E=0：普通版本、活动、宣传、榜单、财报或背景解读。
- source_ids: S1200
- scores: {"event": 0, "relevance": 2, "hook": 0, "total": 0}
- 事件0×相关2+钩子0 = 0；E×R+M；exclude
- history_check: {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null}

## Q1201 - Claude Docs、Claude Slides 与 Claude Design 直接嵌入对话，可导出 PowerPoint 或 PDF
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1201
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1202 - OpenAI 发布模型失准披露框架并公开六份失准报告
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1202
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1203 - OpenAI 发布模型错位报告框架，披露未发布模型自行修改自身指令案例
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1203
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1204 - Epoch AI 分析：贸易数据与经马来西亚走私至中国的约 30 亿美元芯片一致
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1204
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1205 - 用 MCP 插件让 GPT-6 Pro 分担 Codex 规划任务，节省 Pro 会员周额度
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1205
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1206 - GitHub 用 Copilot 智能体将 Copilot 运行时从 TypeScript 迁移到 83 万行 Rust
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1206
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1207 - Unsloth 发布 Docker 镜像与 Unsloth Desktop，本地训练运行 500+ 模型
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1207
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1208 - Dwarkesh 对谈 Noam Brown：智能体集群、对齐与递归自我改进
- exclude → ai_trends；AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。
- source_ids: S1208
- AI: {"ai_tier": "transferable_frontier", "game_stage": [], "industry_reverse_scan": false, "migration_path": "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"}

## Q1209 - 万龙觉醒 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1209

## Q1210 - 元气骑士 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1210

## Q1211 - 暗黑破坏神：不朽 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1211

## Q1212 - 梦想世界3 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1212

## Q1213 - 诡秘之主 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1213

## Q1214 - 镭明闪击 - 新版本
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1214

## Q1216 - 三角洲行动-周年庆送3900限时三角券 - 【洲年空投】活动开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1216

## Q1217 - 乱涂彩世界 - 新角色「嫦娥」登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1217

## Q1218 - 元气骑士前传 - 新英雄职业「司星」登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1218

## Q1219 - 光·遇(官服) - 白金先祖复刻
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1219

## Q1220 - 卡拉彼丘-手游(官服) - 新赛季「错季花园」开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1220

## Q1221 - 好游快爆×超级草莓音乐节 招募中 - 游戏区爆料抢先看!《武士零》抢先试玩
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1221

## Q1222 - 如鸢(官服) - 珍藏恋念「如镜中观」上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1222

## Q1223 - 妄想山海 - 全新进化兽「囚牛」上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1223

## Q1224 - 崩坏：因缘精灵-崩坏IP新作(官服) 招募中 - 测试资格招募开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1224

## Q1225 - 巅峰极速 - 双精英车手登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1225

## Q1226 - 恋与深空 - 免费领五星思念「夏以昼·偏航线」
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1226

## Q1227 - 无畏契约：源能行动 - 笔间闲趣系列盘盘、喷漆、卡面上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1227

## Q1228 - 明日之后(官服) - 非遗「打铁花」联动开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1228

## Q1229 - 桃源深处有人家 - 全新版本「华灯桂筵」开启
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1229

## Q1230 - 永劫无间手游(官服)-二周年 - 武道对决·竞技版玩法限时上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1230

## Q1231 - 炼金与魔法-9月22日上线 - 定档9月22日正式上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1231

## Q1232 - 燕云十六声(官服) - 全新套装、武器外观、奇术特效上架
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S1232

## Q1233 - 空之轨迹 the 2nd PC/主机 - PC端上线,快爆已支持CDK首发折扣
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1233

## Q1234 - 穿越火线-枪战王者 - 《鬼吹灯》联动开启
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S1234

## Q1235 - 第五人格(官服)-1v4对抗 - 追光逐梦活动免费得奇珍时装
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1235

## Q1237 - 诡秘之主(官服) - 新玩法【愚者棋局】上线
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1237

## Q1238 - 超自然行动组 - 新员工「白夜」登场
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S1238

## Q1239 - 斗破：莫欺少年穷 - 10:00 正式上线
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S1239

## Q1240 - 星途天城 - 10:00 删档测试
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1240

## Q1241 - 王者万象棋 - 10:00 新棋手“阿离”登场
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1241

## Q1242 - 长夜守卫者 - 10:00 限量抢注测试
- merge → release_calendar；同URL重复采集，合并到已审阅候选。
- source_ids: S1242

## Q1244 - Ved: Recure launches September 22
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1244

## Q1245 - Kingdom of Night for PS5, Xbox Series, and Switch launches November 5
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1245

## Q1246 - Hope in the City launches November 10 for Xbox Series, PC
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1246

## Q1247 - Shape of Dreams now available for PS5, Xbox Series, and Switch 2 alongside ‘Starless Path’ update
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1247

## Q1248 - Shape of Dreams now available for PS5, Xbox Series, and Switch 2
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1248

## Q1249 - GACHIAKUTA: BREAKOUT launches in 2027
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1249

## Q1250 - ZERO PARADES: For Dead Spies for PS5 launches November 3 alongside ‘Director’s Cut’ update
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1250

## Q1251 - Earth Defense Force 6.2: Invaders from Another World launches March 18, 2027 in Japan
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1251

## Q1252 - Astrae Oratio launches in 2027 for iOS and Android, followed by PC
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1252

## Q1253 - UN:Me delayed to 2027
- exclude → release_calendar；已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。
- source_ids: S1253

## Q1254 - [小瓜] [碧蓝航线] 皮肤忘记抠掉AI生成图标
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1254

## Q1255 - [新瓜]碧蓝也干了，环鸡一家亲
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1255

## Q1256 - [周边] [小瓜微甜]万代做原神周边，但是没写散兵名字，写了个等，目前被绝赞冲锋中
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1256

## Q1257 - [新瓜]异环 前瞻出现自机角色手部问题
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1257

## Q1258 - [新瓜]蓝原3测逆天bug
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1258

## Q1259 - [联动]异环联动凉宫春日的忧郁
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1259

## Q1260 - [新闻相关]蔡明为新游伊莫代言
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1260

## Q1261 - [新瓜] [疑似内容]蓝色星原旅遥胸部似曾相识的乱晃
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1261

## Q1262 - [新瓜]鹅鸭杀给低信誉分的人出单独的游戏环境
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1262

## Q1263 - 暗黑归瓜，不是你说谁给我打电话？
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1263

## Q1264 - [网易] 炉石传说新bug，黄金卡包原价400金币现价10金币
- merge → community_discourse；同URL重复采集，合并到已审阅候选。
- source_ids: S1264

## Q1265 - [新瓜]交错战线皮肤疑似被辣仙举报修改
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1265

## Q1266 - [腾讯]火影手游送篮球佐助
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1266

## Q1267 - [腾讯]王者荣耀IP，自走棋玩法新游戏，王者万象棋今日上线
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1267

## Q1268 - [战双帕弥什]战双九游渠道服关服(并非游戏关服，只是关渠道服)
- exclude → community_discourse；已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。
- source_ids: S1268

## Q1269 - Five things we’ve learned about Japan’s games industry, plus how GTA 6 influenced Valor Mortis’ $40 price point
- exclude → deep_analysis；目标周报精确selection不存在；按规则不自动写入第五栏。
- source_ids: S1269
- scores: {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}

<!-- BEGIN SELECTED DEEP DECISIONS -->

## 人工选定深度观察

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| D001 | include | 深度观察 | 用户明确选择进入目标周报。 |
| D005 | include | 深度观察 | 用户明确选择进入目标周报。唯一卡片，并吸收C006、C014信息。 |
| D006 | merge into D005 | 深度观察 | 用户未单独选择进入正文；核心信息按要求并入C005的正文与唯一卡片。 |
| D014 | merge into D005 | 深度观察 | 用户未单独选择进入正文；核心信息按要求并入C005的正文与唯一卡片。 |

<!-- END SELECTED DEEP DECISIONS -->
