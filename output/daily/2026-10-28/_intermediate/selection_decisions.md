# 卡片曝光去重
近14天与更早archive均检索；历史曝光字段含rank/limit/source。唯一card_carryover为I130：9分、此前未卡片曝光；Atari6分未获名额。

# 行业时间口径
source_window_v1：published_at优先，缺失回退input date；事件历史日期不作门禁。较早新品/数据保留真实日期，来源窗外不得用采集日期覆盖。

# 维度覆盖自检
国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均完成全量262条反扫；新闻与AI严格按事件聚类，日历独立反扫308条，详情见release_reverse_scan.json。
产品日历漏挂反查：逐源全文及结构化清单已扫，单产品+日期建节点，误召回保留排除记录；行业与日历不跨栏互斥。
行业评分记录：事件E×主体R+品类M，E/R为0–3、M为0/1，统一≥5。

| candidate | decision | section | score | reason |
| --- | --- | --- | --- | --- |
| I160 | include | industry_news | 9 | 核心制作人转岗为组织变化E3；来源明确腾讯天美与腾讯魔方，主体R3；公司人事不借MOBA背景加M。 |
<!-- I160 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I160_STOP | exclude | industry_news | 6 | 停运安排已于10月27日曝光；国服补全具体日不改变同一停运决定，不再次刊载。 |
<!-- I160_STOP {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["daily 2026-10-27_to_2026-10-27｜《宝可梦大集结》公布停运安排，国际服将于2027年3月关闭"], "new_facts": [], "prior_card_exposed": true, "exposure_details": [{"title": "《宝可梦大集结》公布停运安排，国际服将于2027年3月关闭", "report_window": {"start": "2026-10-27", "end": "2026-10-27"}, "card_exposed": true, "card_rank": 6, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-10-27\\_intermediate\\report_items.json"}], "archive_checked": true} -->
| I239 | include | industry_news | 9 | 统辖Magic、D&D、Duel Masters及数字游戏的头部IP与发行主体，任命为E3，影响力可比头部主体取R3；AI仅背景不加M。 |
<!-- I239 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I206 | include | industry_news | 9 | 来源确认双方去年已宣布初代重制，属于既有新品立项E3，当前报道可消费；科乐美多作系列与600万份重制作品证明头部产品矩阵，R3；不因项目较早降E。报道目标档期须保留爆料归因。 |
<!-- I206 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I130 | include | industry_news | 9 | 当前多语言报道回顾4月移动版正式上线，E3不因历史日期下降；腾讯直属R3；旧报告已记载4月公测但从未卡片曝光，竞争唯一card_carryover，9分高于Atari6分。 |
<!-- I130 {"history_match": true, "novelty": "card_carryover", "prior_occurrences": ["weekly 2026-05-28_to_2026-06-04｜《王者荣耀：世界》执行制作人李新平公测一月后离职"], "new_facts": [], "prior_card_exposed": false, "exposure_details": [{"title": "《王者荣耀：世界》执行制作人李新平公测一月后离职", "report_window": {"start": "2026-05-28", "end": "2026-06-04"}, "card_exposed": false, "card_rank": null, "card_limit": null, "card_exposure_source": "not_broadcast", "artifact": "output\\weekly\\2026-05-28_to_2026-06-04\\game_industry_weekly_2026-05-28_to_2026-06-04.md"}], "archive_checked": true} -->
| I059 | include | industry_news | 7 | 来源显示前作iOS累计收入超4亿元，新作半月iOS下载360万、收入逾1300万元，构成细分市场较强发行与研运影响力R2；新品上线E3；明确PvP竞技M1，不借背景点点互动取R3。 |
<!-- I059 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I030 | include | industry_news | 6 | 围绕小游戏平台开放、发行与支付进行正式战略合作E3；来源载明500万年活平台与过往100亿流水生态实战，具区域分发能力取R2；不凭蚂蚁背景自动当阿里R3。 |
<!-- I030 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I164 | include | industry_news | 6 | 游戏行业奖项与专业组织的委员会核心负责人任命E3；跨工作室与行业委员会的组织影响力R2，不借其曾任Microsoft/Sony职位抬R3。 |
<!-- I164 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I251 | include | industry_news | 6 | DRM-free商店与独立发行商正式联合发行E3；全球PC店面、营销与跨平台发行能力构成R2，名单外不封顶R1。 |
<!-- I251 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I241 | include | industry_news | 6 | 游戏工作室论坛和wiki迁入Discord造成知识封闭，来源直接说明其游戏社区基础设施作用；平台级公开内容可发现性规则E2，头部社区分发平台R3。 |
<!-- I241 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I157 | include | industry_news | 6 | 前作销量超过百万、历史AVG细分市场影响力支持R2；新品正式发售E3，首日约4万销量回本有制作者自述；不因清明历史日期降分，不把文化争议当官方事实。 |
<!-- I157 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I145 | include | industry_news | 6 | 实际新闻主体包含发行商Playstack，来源证明其发行TGA最佳独立游戏及首次中国团队合作，国际独立发行能力R2；新品发售E3，非单纯榜位；肉鸽推币不自动命中竞技/数值卡牌。 |
<!-- I145 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I229_BRUTAL | include | industry_news | 6 | 推出开放游戏开发基础设施为战略动作E3；DayZ资深开发者创立、已有商业产品并获边缘世界引擎迁移采用，实际研发影响力R2。 |
<!-- I229_BRUTAL {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I211 | include | industry_news | 6 | 非例行财报：保障程序、无力偿债风险及最坏年内清算情形构成流动性异常E3；奇异人生开发主体R2；不同于仅工会裁员表态E1。对照9月现金可撑至2027年1月底警告，本期新增保障程序与11月裁定/解雇节点，保留工会归因。 |
<!-- I211 {"history_match": true, "novelty": "material_update", "prior_occurrences": ["daily 2026-09-08_to_2026-09-08｜Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人", "weekly 2026-09-04_to_2026-09-10｜Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人"], "new_facts": ["本期报道公司已处于保障程序，工会披露最坏情形为2026年内清算。", "政府机构拟11月3日裁定，获批后员工可能11月25日收到解雇通知。"], "prior_card_exposed": true, "exposure_details": [{"title": "Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人", "report_window": {"start": "2026-09-08", "end": "2026-09-08"}, "card_exposed": true, "card_rank": 4, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-09-08\\_intermediate\\report_items.json"}, {"title": "Don't Nod警告现金或难支撑至2027年1月底，法国团队最多裁减90人", "report_window": {"start": "2026-09-04", "end": "2026-09-10"}, "card_exposed": false, "card_rank": null, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\weekly\\2026-09-04_to_2026-09-10\\_intermediate\\report_items.json"}], "archive_checked": true} -->
| I346_IOS | include | industry_news | 6 | 头部全球游戏的移动平台准入裁定E2R3；本期newsletter明确记录澳洲法院要求重新上架。较早全球iOS回归报道仍明确澳洲不可用，本期为可核验地区状态变化。 |
<!-- I346_IOS {"history_match": true, "novelty": "material_update", "prior_occurrences": ["daily 2026-05-28_to_2026-05-28｜《堡垒之夜》全球重返 iOS 七天下载约 340 万，创八年新高", "weekly 2026-05-28_to_2026-06-04｜Fortnite全球iOS回归首周340万下载，创八年新高"], "new_facts": ["本期来源记载澳大利亚法院要求Fortnite重返当地iOS App Store；历史记录明确该地区尚不可用。"], "prior_card_exposed": false, "exposure_details": [{"title": "《堡垒之夜》全球重返 iOS 七天下载约 340 万，创八年新高", "report_window": {"start": "2026-05-28", "end": "2026-05-28"}, "card_exposed": false, "card_rank": null, "card_limit": null, "card_exposure_source": "not_broadcast", "artifact": "output\\daily\\2026-05-28\\game_industry_daily_2026-05-28.md"}, {"title": "Fortnite全球iOS回归首周340万下载，创八年新高", "report_window": {"start": "2026-05-28", "end": "2026-06-04"}, "card_exposed": false, "card_rank": null, "card_limit": null, "card_exposure_source": "not_broadcast", "artifact": "output\\weekly\\2026-05-28_to_2026-06-04\\game_industry_weekly_2026-05-28_to_2026-06-04.md"}], "archive_checked": true} -->
| I012 | exclude | industry_news | 6 | 当前来源在窗口内；历史报告已收录并曝光同一已上线/任职变化状态，本期没有实质变化，仅复述或翻译，不因事件较早排除。 |
<!-- I012 {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["daily 2026-10-27_to_2026-10-27｜微软将Arkane Lyon寻找买家的协商期延长一个月"], "new_facts": [], "prior_card_exposed": true, "exposure_details": [{"title": "微软将Arkane Lyon寻找买家的协商期延长一个月", "report_window": {"start": "2026-10-27", "end": "2026-10-27"}, "card_exposed": true, "card_rank": 7, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-10-27\\_intermediate\\report_items.json"}], "archive_checked": true} -->
| I165 | exclude | industry_news | 9 | 当前来源在窗口内；历史报告已收录并曝光同一已上线/任职变化状态，本期没有实质变化，仅复述或翻译，不因事件较早排除。 |
<!-- I165 {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["daily 2026-10-27_to_2026-10-27｜Xbox首任首席运营官Helen Chiang任职三个月后离职"], "new_facts": [], "prior_card_exposed": true, "exposure_details": [{"title": "Xbox首任首席运营官Helen Chiang任职三个月后离职", "report_window": {"start": "2026-10-27", "end": "2026-10-27"}, "card_exposed": true, "card_rank": 4, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-10-27\\_intermediate\\report_items.json"}], "archive_checked": true} -->
| I260 | exclude | industry_news | 9 | 当前来源在窗口内；历史报告已收录并曝光同一已上线/任职变化状态，本期没有实质变化，仅复述或翻译，不因事件较早排除。 |
<!-- I260 {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["daily 2026-10-27_to_2026-10-27｜灵犀《篮球少女：飞跃巅峰》开服三天后进入游戏畅销榜第4"], "new_facts": [], "prior_card_exposed": true, "exposure_details": [{"title": "灵犀《篮球少女：飞跃巅峰》开服三天后进入游戏畅销榜第4", "report_window": {"start": "2026-10-27", "end": "2026-10-27"}, "card_exposed": true, "card_rank": 2, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-10-27\\_intermediate\\report_items.json"}], "archive_checked": true} -->
| I053 | exclude | industry_news | 9 | 当前来源在窗口内；历史报告已收录并曝光同一已上线/任职变化状态，本期没有实质变化，仅复述或翻译，不因事件较早排除。 |
<!-- I053 {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["daily 2026-06-04_to_2026-06-04｜《异环》日本版登顶畅销榜，引日本业界反思本土竞争力", "daily 2026-06-10_to_2026-06-10｜5月全球手游市场：王者荣耀月收10亿，Kingshot冲入全球前五", "daily 2026-07-14_to_2026-07-14｜完美世界《异环》流水超 14 亿，H1 却预亏至少 8000 万", "weekly 2026-07-10_to_2026-07-16｜完美世界《异环》Q2 流水超 14 亿,H1 因\"收入费用错配\"预亏 8000 万-1.2 亿"], "new_facts": [], "prior_card_exposed": true, "exposure_details": [{"title": "《异环》日本版登顶畅销榜，引日本业界反思本土竞争力", "report_window": {"start": "2026-06-04", "end": "2026-06-04"}, "card_exposed": false, "card_rank": null, "card_limit": null, "card_exposure_source": "not_broadcast", "artifact": "output\\daily\\2026-06-04\\game_industry_daily_2026-06-04.md"}, {"title": "5月全球手游市场：王者荣耀月收10亿，Kingshot冲入全球前五", "report_window": {"start": "2026-06-10", "end": "2026-06-10"}, "card_exposed": false, "card_rank": null, "card_limit": null, "card_exposure_source": "not_broadcast", "artifact": "output\\daily\\2026-06-10\\game_industry_daily_2026-06-10.md"}, {"title": "完美世界《异环》流水超 14 亿，H1 却预亏至少 8000 万", "report_window": {"start": "2026-07-14", "end": "2026-07-14"}, "card_exposed": true, "card_rank": 2, "card_limit": 10, "card_exposure_source": "legacy_position_inference", "artifact": "output\\daily\\2026-07-14\\game_industry_daily_2026-07-14.md"}, {"title": "完美世界《异环》Q2 流水超 14 亿,H1 因\"收入费用错配\"预亏 8000 万-1.2 亿", "report_window": {"start": "2026-07-10", "end": "2026-07-16"}, "card_exposed": true, "card_rank": 7, "card_limit": 10, "card_exposure_source": "legacy_position_inference", "artifact": "output\\weekly\\2026-07-10_to_2026-07-16\\game_industry_weekly_2026-07-10_to_2026-07-16.md"}], "archive_checked": true} -->
| I177 | exclude | industry_news | 6 | 收购后统筹移动开发的安排在5月28日至6月4日周报已记载，全部未曝光；E3R2=6，低于王者世界9分，唯一card_carryover名额不选择本条。正文与标题姓名不一致另记录，不消费摘要源补齐姓名。 |
<!-- I177 {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["weekly 2026-05-28_to_2026-06-04｜Atari以最高3930万美元收购《Crossy Road》开发商Hipster Whale"], "new_facts": [], "prior_card_exposed": false, "exposure_details": [{"title": "Atari以最高3930万美元收购《Crossy Road》开发商Hipster Whale", "report_window": {"start": "2026-05-28", "end": "2026-06-04"}, "card_exposed": false, "card_rank": null, "card_limit": null, "card_exposure_source": "not_broadcast", "artifact": "output\\weekly\\2026-05-28_to_2026-06-04\\game_industry_weekly_2026-05-28_to_2026-06-04.md"}], "archive_checked": true} -->
| I209 | exclude | industry_news | 6 | 常规财报及历史销量纪录，未证明相对指引/预期异常、重大减值或流动性变化；且源文销量增量与累计数据互相冲突，不引用矛盾数字。 |
<!-- I209 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I036 | exclude | industry_news | 4 | 长线既有产品用户里程碑E1；腾讯R3，爆破竞技M1，总分4。源文区分端游与已曝光的手游过亿，不将二者误并。 |
<!-- I036 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I124 | exclude | industry_news | 4 | 既有产品赛事生态与六年生命周期回顾E1，网易R3、明确电竞机制M1，总分4，不因4月赛事日期降分。 |
<!-- I124 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I166 | exclude | industry_news | 2 | 市场数据E2，PC/主机市场整体基准R1，M0，2分；其中Remedy项目成绩另建独立候选，不借其他榜内大公司抬整篇R3。 |
<!-- I166 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I166_REMEDY | exclude | industry_news | 4 | 首次自发行作品首月百万、成为自家最快销售作品，属于产品销售状态数据E2；成熟跨平台研发与发行能力R2，动作冒险无重点品类M，4分边界。 |
<!-- I166_REMEDY {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I201 | include | industry_news | 5 | E2正式定档×R2有较强声量的长期开发生活模拟产品+M1=5；行业与产品日历独立，两栏均可入选。 |
<!-- I201 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I040 | exclude | industry_news | 3 | 新品1.0正式发售，独立工作室代表作可核验，当前影响力R1，3分。 |
<!-- I040 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I041 | exclude | industry_news | 1 | 零售店损失及拟联合诉讼E1，实际主体为独立零售商R1。 |
<!-- I041 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I044 | exclude | industry_news | 1 | 外包工作室转原创开发经验访谈，属于既有战略与开发复盘E1，代表产品R1。 |
<!-- I044 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I047 | exclude | industry_news | 1 | 小众开发与获客经验讨论E1，PC市场整体R1。 |
<!-- I047 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I065 | exclude | industry_news | 3 | 2025年VR产品上线回顾E3，当前代表作品及创作者影响力R1，不能因历史日期改E0。 |
<!-- I065 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I071 | exclude | industry_news | 3 | 新品抢先体验及十万销量E3，代表独立作品R1，非竞技动作肉鸽M0。 |
<!-- I071 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I077 | exclude | industry_news | 3 | 4月2日新品发售回顾E3，代表独立视觉小说团队R1。 |
<!-- I077 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I089 | exclude | industry_news | 2 | 俄语区营销会议与既有能力宣传E1，区域广告平台能力R2，2分。 |
<!-- I089 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I095 | exclude | industry_news | 3 | 已发售新品及八年开发复盘E3，当前团队有代表作但R1，3分；剧情AI角色不是实际生成式AI应用。 |
<!-- I095 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I108 | exclude | industry_news | 4 | 小游戏发布及PvP养成结构，E3，当前实际主体有代表作品R1，竞技品类M1后4分。 |
<!-- I108 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I113 | exclude | industry_news | 3 | 3月小游戏新上线回顾E3，系列作品与榜位支持代表主体R1；塔防/跑道不自动竞技，M0。 |
<!-- I113 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I151 | exclude | industry_news | 0 | 既有手游赛季模式与内容运营E0，不以新模式当新品。 |
<!-- I151 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| A029 | include | ai_trends | — | 直接游戏产品与制作流程落地，完整开发者访谈提供交互、记忆、成本与边界。 |
| A161 | include | ai_trends | — | 一人核心研发及创作平台已有可量化产出，直接产品与研发应用；自述规模不外推行业效率。 |
| A247 | include | ai_trends | — | 引擎与游戏开发直接应用，提供人工架构控制和具体任务时长结果；厂商自述归因。 |
| A176 | include | ai_trends | — | 直接作用于游戏工具的训练授权，区分计划修改与现行禁止，不与编码应用合并。 |
| A181 | include | ai_trends | — | 直接游戏生成工具训练数据治理，站方指控和公司确认分别归因，属于完整且有处置结果的独立事件。 |
| A180 | exclude | ai_trends | — | 直接发行治理候选，来源有问题确认但没有新执行方案；在五条可核验产品/流程/授权/处置进展之后不另刊同类争论。 |
| A026 | exclude | ai_trends | — | 迁移价值类；当期有发布，但直接游戏应用优先，本期已有五条证据完整的直接应用，不用未规模落地的引擎替代叙事扩写。 |
| A027 | exclude | ai_trends | — | 直接产品应用，但核心开发于10月5日；与本期更完整的AI原生产品和管线案例相比，统计偏差/幻觉边界较多，未另刊。 |
| A032 | exclude | ai_trends | — | 不同受访者不聚合为一条新闻；本记录仅审计观点型池，未产生已部署游戏变化。 |
| A058 | exclude | ai_trends | — | 世界模型与AI创作社区长访谈，现有证据主要是较早经营指标与方法论；低于本期直接游戏落地优先级。 |
| A100 | exclude | ai_trends | — | 直接3D研发工具候选，含3月发布的模型与生产拓扑机制；本期优先具体游戏团队实际管线与新处置，不把厂商自述引擎可用性写成量产事实。 |
| A119 | exclude | ai_trends | — | 直接人才培养/创作支持候选，主要赛事方法与历史案例，不挤占本期更具体的产品/授权/研发变化。 |
| A0263 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0265 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0266 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0267 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0268 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0269 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0270 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0271 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0273 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0274 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0275 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0276 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0277 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0278 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| A0279 | exclude | ai_trends | — | 通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。 |
| C334 | include | community_discourse | — | 报告日新建、可命名的评测口径争论；只使用28日首页摘录，剔除29日回复。 |
| C345 | include | community_discourse | — | 旧帖在28日出现围绕收益方差和资产价值的新反驳，保留前情与对立意见；不把玩家估算写成概率或官方事实。 |
| C0326 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0327 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0328 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0329 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0330 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0331 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0332 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0333 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0335 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0336 | exclude | community_discourse | — | 文本或立绘调整旧争议，28日回复仍未明确关键改动或新增处置；不以旧热度凑数。 |
| C0337 | exclude | community_discourse | — | 与已发布的行业事件相同，当前只增加旧热度/意见，没有窗口内新进展。 |
| C0338 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0339 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0340 | exclude | community_discourse | — | 文本或立绘调整旧争议，28日回复仍未明确关键改动或新增处置；不以旧热度凑数。 |
| C0341 | exclude | community_discourse | — | 与已发布的行业事件相同，当前只增加旧热度/意见，没有窗口内新进展。 |
| C0342 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0343 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| C0344 | exclude | community_discourse | — | 旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。 |
| D346 | include | deep_analysis | 11 | 配置newsletter全文优先；同一统计口径比较6月/10月，具完整机制与边界；单篇高质量分析支撑独立主题。 |
| D347 | exclude | deep_analysis | 2 | 汽车或电商市场，不具本期游戏深度观察证据链。 |
| D348 | exclude | deep_analysis | 2 | 汽车或电商市场，不具本期游戏深度观察证据链。 |
| I001 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I001 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I002 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I002 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I004 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I004 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I005 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I005 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I006 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I006 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I007 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I007 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I008 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I008 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I009 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I009 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I010 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I010 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I011 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I011 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I013 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I013 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I014 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I014 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I015 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I015 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I016 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I016 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I017 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I017 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I018 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I018 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I019 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I019 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I020 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I020 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I021 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I021 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I022 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I022 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I023 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I023 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I024 | exclude | industry_news | 6 | 平台审核要求E2R3达线，但仅31字标题式源文，无审核适用范围与生效条件；转AI反扫后不把它当已验证新政策。 |
<!-- I024 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I028 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I028 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I031 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I031 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I033 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I033 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I034 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I034 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I035 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I035 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I037 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I037 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I038 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I038 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I039 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I039 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I042 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I042 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I043 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I043 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I083 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I083 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I084 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I084 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I085 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I085 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I086 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I086 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I087 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I087 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I088 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I088 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I158 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I158 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I159 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I159 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I162 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I162 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I163 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I163 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I167 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I167 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I168 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I168 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I169 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I169 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I170 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I170 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I171 | exclude | industry_news | 9 | 合作本可E3，但现有正文仅受阻摘要/99字引流，未获完整合作条款与事实链，不用残缺材料进入正文。 |
<!-- I171 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I172 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I172 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I173 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I173 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I174 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I174 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I175 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I175 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I178 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I178 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I179 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I179 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I182 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I182 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I183 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I183 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I184 | exclude | industry_news | 9 | 合作本可E3，但现有正文仅受阻摘要/99字引流，未获完整合作条款与事实链，不用残缺材料进入正文。 |
<!-- I184 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I185 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I185 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I186 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I186 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I187 | exclude | industry_news | 3 | 逆水寒制作人对MMO的既有战略与运营访谈E1，网易R3；没有新的立项、资本或平台状态，不按E2数据新闻计分。 |
<!-- I187 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I188 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I188 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I189 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I189 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I190 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I190 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I191 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I191 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I192 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I192 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I193 | exclude | industry_news | 3 | 开放角色预创建与名字预留属于发售前运营节点E1，尚非新品正式上线或首次测试；Blizzard主体R3，3分。 |
<!-- I193 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I195 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I195 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I196 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I196 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I197 | exclude | industry_news | 0 | 既有独立游戏节目发布汇编E0；各产品具体测试/定档已拆入日历，不给节目借所有参展作品累计E3。 |
<!-- I197 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I198 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I198 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I199 | exclude | industry_news | 3 | 项目研发多年原因回顾，未发生新品立项/上线或取消；实际为在研项目复盘E1，不能用“开发多年”当新立项。 |
<!-- I199 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I200 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I200 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I202 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I202 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I203 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I203 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I204 | exclude | industry_news | 0 | 普通订阅阵容公布/显示技术接入属于既有产品运营与宣传E0。 |
<!-- I204 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I205 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I205 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I207 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I207 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I208 | exclude | industry_news | 6 | 新书预订引发新一轮玩家反应，未改变此前已曝光的2028年实体光盘政策，行业不重复旧政策；社区外溢候选另记录。 |
<!-- I208 {"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["weekly 2026-06-26_to_2026-07-02｜索尼 Bungie 裁员 292 人，宣布 2028 年起停产实体光盘", "daily 2026-07-07_to_2026-07-07｜索尼确认 2028 年停产 PS 实体光盘，「别杀死光盘」请愿四天破 10 万签名", "weekly 2026-07-03_to_2026-07-09｜索尼宣布 2028 年停产实体光盘，工厂转型且未提前告知合作伙伴"], "new_facts": [], "prior_card_exposed": true, "exposure_details": [{"title": "索尼 Bungie 裁员 292 人，宣布 2028 年起停产实体光盘", "report_window": {"start": "2026-06-26", "end": "2026-07-02"}, "card_exposed": false, "card_rank": null, "card_limit": 10, "card_exposure_source": "legacy_position_inference", "artifact": "output\\weekly\\2026-06-26_to_2026-07-02\\game_industry_weekly_2026-06-26_to_2026-07-02.md"}, {"title": "索尼确认 2028 年停产 PS 实体光盘，「别杀死光盘」请愿四天破 10 万签名", "report_window": {"start": "2026-07-07", "end": "2026-07-07"}, "card_exposed": true, "card_rank": 3, "card_limit": 10, "card_exposure_source": "legacy_position_inference", "artifact": "output\\daily\\2026-07-07\\game_industry_daily_2026-07-07.md"}, {"title": "索尼宣布 2028 年停产实体光盘，工厂转型且未提前告知合作伙伴", "report_window": {"start": "2026-07-03", "end": "2026-07-09"}, "card_exposed": false, "card_rank": null, "card_limit": 10, "card_exposure_source": "legacy_position_inference", "artifact": "output\\weekly\\2026-07-03_to_2026-07-09\\game_industry_weekly_2026-07-03_to_2026-07-09.md"}], "archive_checked": true} -->
| I210 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I210 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I212 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I212 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I213 | exclude | industry_news | 3 | 已有系列规划与既有战略访谈表态E1，未单独确认新的立项/合作/政策生效。 |
<!-- I213 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I215 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I215 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I216 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I216 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I217 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I217 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I218 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I218 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I219 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I219 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I220 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I220 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I221 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I221 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I222 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I222 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I223 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I223 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I224 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I224 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I225 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I225 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I226 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I226 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I227 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I227 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I228 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I228 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I230 | exclude | industry_news | 3 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I230 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I232 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I232 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I233 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I233 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I234 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I234 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I235 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I235 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I236 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I236 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I237 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I237 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I238 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I238 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I240 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I240 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I242 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I242 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I243 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I243 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I244 | include | industry_news | 6 | Project Titan取消为E2，暴雪R3，6分；本期来源回顾既有项目取消，完整文本可核验，未检索到历史同事件，不因取消发生较早而降低E或排除。 |
<!-- I244 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I245 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I245 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I246 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I246 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I248 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I248 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I249 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I249 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I250 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I250 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I252 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I252 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I253 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I253 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I254 | exclude | industry_news | 0 | E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。 |
<!-- I254 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I255 | exclude | industry_news | 3 | 已有系列规划与既有战略访谈表态E1，未单独确认新的立项/合作/政策生效。 |
<!-- I255 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I256 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I256 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I257 | exclude | industry_news | 1 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I257 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I258 | exclude | industry_news | 0 | 普通订阅阵容公布/显示技术接入属于既有产品运营与宣传E0。 |
<!-- I258 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I259 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I259 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I261 | exclude | industry_news | 2 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I261 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I262 | exclude | industry_news | 4 | 独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。 |
<!-- I262 {"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null, "exposure_details": [], "archive_checked": true} -->
| I231 | include | industry_news | 6 | E2产品经营数据，来源直接归属莉莉丝R3；随机奖励/塔防/营地经营不足证明本事件数值卡牌RPG或竞技，M0。相对9月28日四个月4560万美元，当前双平台9500万美元、下载1800万为有口径说明的新数据，不以媒体数量作更新。 |
<!-- I231 {"history_match": true, "novelty": "material_update", "prior_occurrences": ["weekly 2026-07-31_to_2026-08-06｜莉莉丝《塔塔冒险队》海外上线两个月流水接近2亿元", "daily 2026-08-11_to_2026-08-11｜莉莉丝《塔塔冒险队》海外上线两个月流水达2亿元", "daily 2026-09-07_to_2026-09-07｜莉莉丝《塔塔冒险队》公测后进入iOS畅销榜前30", "weekly 2026-09-04_to_2026-09-10｜莉莉丝《塔塔冒险队》公测后进入iOS畅销榜前30", "daily 2026-09-16_to_2026-09-16｜《塔塔冒险队》8月内购收入升至890万美元，累计安装超1250万", "daily 2026-09-28_to_2026-09-28｜《塔塔冒险队》海外公测四个月累计流水达到4560万美元"], "new_facts": ["本期点点数据口径为海外iOS/安卓及国内iOS合计收入超过9500万美元、下载超过1800万次；9月28日报告四个月累计流水4560万美元。", "1.1亿美元含国内安卓推估，须与9500万美元观测口径区分。"], "prior_card_exposed": true, "exposure_details": [{"title": "莉莉丝《塔塔冒险队》海外上线两个月流水接近2亿元", "report_window": {"start": "2026-07-31", "end": "2026-08-06"}, "card_exposed": false, "card_rank": null, "card_limit": 10, "card_exposure_source": "legacy_position_inference", "artifact": "output\\weekly\\2026-07-31_to_2026-08-06\\_intermediate\\report_items.json"}, {"title": "莉莉丝《塔塔冒险队》海外上线两个月流水达2亿元", "report_window": {"start": "2026-08-11", "end": "2026-08-11"}, "card_exposed": true, "card_rank": 8, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-08-11\\_intermediate\\report_items.json"}, {"title": "莉莉丝《塔塔冒险队》公测后进入iOS畅销榜前30", "report_window": {"start": "2026-09-07", "end": "2026-09-07"}, "card_exposed": true, "card_rank": 3, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-09-07\\_intermediate\\report_items.json"}, {"title": "莉莉丝《塔塔冒险队》公测后进入iOS畅销榜前30", "report_window": {"start": "2026-09-04", "end": "2026-09-10"}, "card_exposed": true, "card_rank": 9, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\weekly\\2026-09-04_to_2026-09-10\\_intermediate\\report_items.json"}, {"title": "《塔塔冒险队》8月内购收入升至890万美元，累计安装超1250万", "report_window": {"start": "2026-09-16", "end": "2026-09-16"}, "card_exposed": true, "card_rank": 4, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-09-16\\_intermediate\\report_items.json"}, {"title": "《塔塔冒险队》海外公测四个月累计流水达到4560万美元", "report_window": {"start": "2026-09-28", "end": "2026-09-28"}, "card_exposed": true, "card_rank": 6, "card_limit": 10, "card_exposure_source": "publish_log_manifest", "artifact": "output\\daily\\2026-09-28\\_intermediate\\report_items.json"}], "archive_checked": true} -->
| A214 | exclude | ai_trends | — | 不同受访者不聚合为一条新闻；本记录仅审计观点型池，未产生已部署游戏变化。 |
| release-candidate-001 | include | release_calendar | 14 | 次日及时性候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | 8 | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-004 | include | release_calendar | 8 | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-005 | include | release_calendar | 8 | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-006 | exclude | release_calendar | 6 | 17173与3839两源一致的实际测试。；超过本报告产品日历条数上限 |
| release-candidate-007 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-008 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-009 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-010 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-011 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-012 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-013 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-014 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-015 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-016 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-017 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-018 | exclude | release_calendar | 6 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；超过本报告产品日历条数上限 |
| release-candidate-019 | exclude | release_calendar | 4 | Switch版当日可用；PC次日日期不与该Switch节点混并。；超过本报告产品日历条数上限 |
| release-candidate-002 | exclude | release_calendar | 9 | 现已可玩不等于10月28日首次开放测试，缺确切启用日；保留其11月10日多源正式定档节点。；超过本报告产品日历条数上限 |
| release-candidate-020 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 6 | 历史1.0上线，日历事件超窗。；事件日期不在报告窗口 |
| release-candidate-023 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | 6 | 历史3月上线，日历事件超窗；行业来源窗口独立可入选。；事件日期不在报告窗口 |
| release-candidate-026 | exclude | release_calendar | 6 | 历史EA上线，日历事件超窗。；事件日期不在报告窗口 |
| release-candidate-027 | exclude | release_calendar | 6 | 历史发售，日历事件超窗。；事件日期不在报告窗口 |
| release-candidate-028 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；事件日期不在报告窗口 |
| release-candidate-029 | exclude | release_calendar | 6 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 6 | 单源现已开放Demo；其未来定档为另一个日期节点。；单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 6 | 单源Demo不因未来定档多源而提升当日测试资格。；单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 6 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 6 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 6 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-041 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-043 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-046 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-047 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-048 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-049 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-050 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-051 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-052 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-053 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-054 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-055 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-056 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-057 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-058 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-059 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-060 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-061 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-062 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-063 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-064 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-065 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-066 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-067 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-068 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-069 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-070 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-071 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-072 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-073 | exclude | release_calendar | 6 | 新品发行结构化清单；单源，次日窗口不豁免多源门槛。；单源不具备正文资格 |
| release-candidate-074 | exclude | release_calendar | 6 | 历史起量与成绩复盘，不是当期新品上线。；事件日期不在报告窗口 |
| release-candidate-075 | exclude | release_calendar | 6 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-076 | exclude | release_calendar | 6 | 明确次日发售，仅单源。；单源不具备正文资格 |
| release-candidate-077 | exclude | release_calendar | 6 | 文章回顾4月上线，非当期新开服；版本前瞻不算新品。；事件日期不在报告窗口 |
| release-candidate-078 | exclude | release_calendar | 6 | 开服后畅销成绩不等于当日再次上线。；事件日期不在报告窗口 |
| release-candidate-079 | exclude | release_calendar | 6 | 上一期已发布同一PC预下载，不能因今日来源再次召回重复。；超过本报告产品日历条数上限 |
| release-candidate-080 | exclude | release_calendar | 4 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-081 | exclude | release_calendar | 4 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-082 | exclude | release_calendar | 4 | 新品首曝，仅单源。；单源不具备正文资格 |
| release-candidate-083 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-084 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-085 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-086 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-087 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-088 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-089 | exclude | release_calendar | 4 | 同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。；单源不具备正文资格 |
| release-candidate-090 | exclude | release_calendar | 4 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-091 | exclude | release_calendar | 4 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-092 | exclude | release_calendar | 4 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-093 | exclude | release_calendar | 4 | 网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。；单源不具备正文资格 |
| release-candidate-094 | exclude | release_calendar | 4 | 强化重置新品已于6月定档，只有本次单源回顾，非当前跨平台实际上线。；单源不具备正文资格 |
| release-candidate-095 | exclude | release_calendar | 3 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-096 | exclude | release_calendar | 3 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-097 | exclude | release_calendar | 3 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-098 | exclude | release_calendar | 3 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-099 | exclude | release_calendar | 3 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-100 | exclude | release_calendar | 3 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-101 | exclude | release_calendar | 2 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-102 | exclude | release_calendar | 2 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-103 | exclude | release_calendar | 2 | 复核原始节点；多源和事件日期门禁独立执行。；单源不具备正文资格 |
| release-candidate-104 | exclude | release_calendar | 2 | 只有开启预约、上线时间待定，不足确认实际上线或新定档。；单源不具备正文资格 |
| release-candidate-105 | exclude | release_calendar | 2 | 28日预下载与29日上线分别审计，当前仅一独立来源。；单源不具备正文资格 |
| release-candidate-106 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-107 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-108 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-109 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-110 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-111 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-112 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-113 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-114 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-115 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-116 | exclude | release_calendar | 2 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-117 | exclude | release_calendar | 2 | 老品Switch2移植；不按新品上线E3计日历。；单源不具备正文资格 |
| release-candidate-118 | exclude | release_calendar | 2 | 老品Switch2移植；不按新品上线E3计日历。；单源不具备正文资格 |
| release-candidate-119 | exclude | release_calendar | 2 | 停运非回归：保留误召回审计，禁止刊载。；事件日期不在报告窗口 |
| release-candidate-120 | exclude | release_calendar | 1 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-121 | exclude | release_calendar | 1 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-122 | exclude | release_calendar | 1 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |
| release-candidate-123 | exclude | release_calendar | 1 | 未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。；单源不具备正文资格 |

## 行业逐项评分复核（恢复终稿归位）
评分版本 subject_genre_v2；时间版本 source_window_v1。以下数值直接来自既有决策，不改变评分或入选。

### 行业入选评分

- I160：E3×R3+M0=9；宝可梦大集结制作人杨思勤已转岗腾讯魔方。
- I239：E3×R3+M0=9；Dan Ayoub升任Wizards of the Coast及Hasbro Digital Games负责人。
- I206：E3×R3+M0=9；寂静岭初代重制项目及据报2027年目标档期。
- I130：E3×R3+M0=9；王者荣耀世界4月17日移动端上线复盘。
- I059：E3×R2+M1=7；Shiyue Network新品Dream Guardians的3月上线及早期表现复盘。
- I030：E3×R2+M0=6；世佳朗新AlipayHK战略合作及LumiGames出海品牌。
- I164：E3×R2+M0=6；Charu Desodt接任BAFTA游戏委员会主席。
- I251：E3×R2+M0=6；GOG与Retrovibe启动Retrovibe by GOG发行业务。
- I241：E2×R3+M0=6；Discord可发现服务器消息将纳入网页搜索。
- I157：E3×R2+M0=6；Zero Creation Games复盘Ai Hong发售首日回本。
- I145：E3×R2+M0=6；Raccoon Coin Pusher首日十万销量及Playstack中国合作。
- I229_BRUTAL：E3×R2+M0=6；RocketWerkz开源C#游戏开发框架BRUTAL。
- I211：E3×R2+M0=6；Don't Nod保障程序与工会披露年内清算风险。
- I346_IOS：E2×R3+M0=6；澳大利亚法院要求Fortnite重返iOS App Store。
- I201：E2×R2+M1=5；Witchbrook正式定档2027年1月28日。
- I244：E2×R3+M0=6；Project Titan's end 'immediately instilled a culture of humility' in the Overwatch team which has helped them see the last decade through。
- I231：E2×R3+M0=6；塔塔冒险队截至本期累计下载和收入新状态。

### 3–4分边界候选

- I036：E1×R3+M1=4；无畏契约端游国服注册用户破亿。
- I124：E1×R3+M1=4；梦幻西游手游巅峰联赛六年运营复盘。
- I166_REMEDY：E2×R2+M0=4；Control Resonant首月百万与Remedy首次自发行。
- I040：E3×R1+M0=3；Teahouse Exclusive: A Year and a Half After Being Plagiarized, “Sarah’s Shady Shop” Opens Its Doors。
- I065：E3×R1+M0=3；Sun Yihan: The "Madman" of Mecha Battles and His Dream of VR Gaming。
- I071：E3×R1+M0=3；With sales topping 100,000 in just two weeks since its launch, how has this hardcore roguelike indie action game managed to captivate players?。
- I077：E3×R1+M0=3；Who Flayed the Migrant Workers? This Game Exposes the “Incurable Disease” of These Hardworking People。
- I095：E3×R1+M0=3；8年にわたる長い道のりの末、ベストセラーランキング7位を獲得。プレイヤー：「本当にグラフィックに脱帽だ」。
- I108：E3×R1+M1=4；Ein neuer Überraschungserfolg in den Bestsellerlisten, der einen regelrecht in seinen Bann zieht – kommt er einem nicht irgendwie bekannt vor?。
- I113：E3×R1+M0=3；차트 TOP 3를 휩쓴 이 게임은 트래픽 성공 공식을 제대로 파악한 셈입니다.。
- I001：E1×R3+M0=3；任天堂将于10月28日举行最新一期“独立世界”节目。
- I005：E3×R1+M0=3；《蕾卡的移动工坊》1.0 正式版现已发售，支持简体中文。
- I010：E1×R3+M0=3；超22万玩家请愿EA拯救《质量效应》系列。
- I013：E3×R1+M0=3；经典网页游戏《坏蛋冰淇淋》公布Steam页面。
- I017：E3×R1+M0=3；《神探狗狗：汪者归来》现已全平台发售。
- I022：E3×R1+M0=3；策略肉鸽游戏《天外来袭》定档11.26发售。
- I023：E3×R1+M0=3；城建自走棋《北境战场》现已开启抢先体验，售价48元。
- I042：E3×R1+M0=3；累计出货量突破10万份的《Culdcept BEGINS（卡片召唤师 起源）》 Steam版今日10。
- I159：E2×R2+M0=4；虽然有点晚，但《都市：天际线 扩展版》在NS2上找到了自己的位置。
- I163：E2×R2+M0=4；Gamescom Asia touts new records for international attendance and showfloor size。
- I178：E2×R2+M0=4；Warhorse Studios hit by an undetailed cybersecurity incident。
- I187：E1×R3+M0=3；对话《逆水寒》制作人：我们仍然非常相信MMO的未来。
- I193：E1×R3+M0=3；You Can Make Your WoW: Forever Character Now And Be Ready For Launch。
- I199：E1×R3+M0=3；Here’s Why State Of Decay 3 Has Taken 6 Years To Develop So Far。
- I202：E3×R1+M0=3；Nintendo Indie World’s Weirdest Game Got Me To Relax。
- I203：E3×R1+M0=3；Every October 2026 Nintendo Indie World Game You Can Play Right Now。
- I207：E2×R2+M0=4；《天国：拯救》开发商称遭严重网络攻击。
- I213：E1×R3+M0=3；竹内润：《生化危机》或十年内完结。
- I216：E1×R3+M0=3；暴雪公布《魔兽世界：无限》更新计划。
- I218：E3×R1+M0=3；Switch 2版《我的世界》发售宣传视频。
- I222：E3×R1+M0=3；《吸血鬼：避世血族 誓约与灰烬》发售日预告。
- I223：E3×R1+M0=3；《皮埃罗》试玩Demo宣传视频。
- I226：E3×R1+M0=3；主机版《布莱克庄园降神会》发售宣传视频。
- I230：E3×R1+M0=3；本周 Steam 值得关注的游戏 10.26 - 11.01（三）。
- I232：E2×R2+M0=4；放弃多款手游，烧掉数亿做单机，这家腾讯投资的公司要交卷了。
- I236：E2×R2+M0=4；Warhammer 40,000: Boltgun studio announces major layoffs。
- I243：E2×R2+M0=4；Here's the Phantom Blade Zero release time for your region。
- I248：E2×R2+M0=4；Monster Train 2 is getting a new clan, and they're edgy as h̶e̶l̶l heaven。
- I255：E1×R3+M0=3；硬刚苹果，Epic把赌注押在开放新秩序。
- I259：E2×R2+M0=4；对话10年“老炮儿”：中国游戏出口的“新蓝海”，该怎么进？。
- I262：E2×R2+M0=4；原创丨成立25年终于上Steam，专访制作人：越做越“上头”了。

AI软目标例外：保留5条证据完整、互不重复的直接游戏应用，分别涉及AI原生居民、游戏创作平台、引擎编码、训练授权与数据代理处置；不因软目标1–3条截断。
