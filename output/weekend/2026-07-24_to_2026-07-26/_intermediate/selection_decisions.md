# Selection Decisions

- 维度覆盖自检: 国内移动9张 / 国产产品与人才8张 / 市场数据5张 / 并购3张 / 平台政策4张 / 档期变动7张 / 资本组织6张 / 海外重大8张。
- 产品日历漏挂反查: 已反扫 industry_news 与 release_calendar 的上线/定档/测试节点；修复7组聚类，所有召回信号均进入 release_calendar_audit.json 与决策表。
- 产品日历多源候选按事件分×来源强度排序，只取前4项，不设最低分、不跳项。
- AI已反扫全部行业候选；行业与AI同一独立事件不重复入选。

## 行业新闻 E×R+M 打分

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| industry-candidate-001 Hololive Dreams全球上线并取得首日榜单表现 | include | industry | 事件3×相关3+钩子1 = 10；新品全球上线，移动RPG赛道且有明确首日市场数据 |
| industry-candidate-002 Super Creative两名联席CEO提交辞呈 | include | industry | 事件3×相关3+钩子1 = 10；核心管理层变动，涉及中国上线中的移动RPG产品 |
| industry-candidate-003 伊莫测试结束并披露全球预约数据 | include | industry | 事件2×相关3+钩子2 = 8；国内移动RPG测试节点与多源市场数据 |
| industry-candidate-004 乐信圣文披露产品矩阵与二合手游收入数据 | include | industry | 事件2×相关3+钩子1 = 7；中国手游公司产品矩阵与移动市场结构数据 |
| industry-candidate-005 Ludus Merge Arena披露净收入与用户里程碑 | include | industry | 事件2×相关3+钩子1 = 7；移动策略RPG达到明确收入和用户里程碑 |
| industry-candidate-006 孩之宝确认游戏资产减值并收缩远期投资 | include | industry | 事件3×相关2+钩子1 = 7；重大减值来自项目取消，并伴随远期投资与产品组合调整 |
| industry-candidate-007 Xbox测试广告支持的云游戏串流 | exclude | - | 事件2×相关2+钩子2 = 6；E×R+M=6，平台实验对全球竞争有迁移点但未达7分 |
| industry-candidate-008 Steam改版愿望单与跨区送礼 | exclude | - | 事件2×相关2+钩子2 = 6；E×R+M=6，渠道能力更新未达7分 |
| industry-candidate-009 越南提出未成年人游戏时长与实名新规 | exclude | - | 事件2×相关2+钩子1 = 5；E×R+M=5，草案尚未定稿且中国市场迁移点有限 |
| industry-candidate-010 Unity游戏在虚幻引擎中原生渲染演示 | exclude | - | 事件3×相关2+钩子1 = 7；事件日期为7月21日，早于本期窗口；不以采集日替代事件日 |
| industry-candidate-011 欧盟批准EA私有化交易 | exclude | - | 事件3×相关3+钩子2 = 11；批准事件发生于7月23日，早于本期窗口 |
| industry-candidate-012 Floaty Studio完成100万美元融资 | exclude | - | 事件3×相关3+钩子1 = 10；融资事件已落在上一周报窗口，不重复计入周末报 |
| industry-candidate-013 集合浆果镇开启国内首测 | exclude | - | 事件3×相关3+钩子1 = 10；来源明确写为7月23日开启测试，早于本期窗口 |
| industry-candidate-014 遗忘之海移动端上线并披露首日榜单 | exclude | - | 事件3×相关3+钩子2 = 11；移动端上线与首日榜单均发生于7月23日，早于本期窗口 |
| industry-candidate-015 龙之剑觉醒转为买断制并登上Steam畅销榜 | exclude | - | 事件3×相关3+钩子1 = 10；正式发售日期为7月23日，早于本期窗口 |
| industry-candidate-016 Black Flag Resynced披露上市两周销量表现 | exclude | - | 事件2×相关1+钩子1 = 3；E×R+M=3，海外单一产品数据缺少明确迁移点 |
| industry-candidate-017 Vermila Studios裁员并面临关闭 | exclude | - | 事件2×相关1+钩子1 = 3；E×R+M=3，海外小型工作室组织事件迁移点弱 |
| industry-candidate-018 Thick as Thieves停止内容更新 | exclude | - | 事件2×相关1+钩子1 = 3；E×R+M=3，海外单一产品停止更新迁移点弱 |
| industry-candidate-019 Steam Deck销量同比下滑82% | exclude | - | 事件2×相关0+钩子1 = 1；E×R+M=1，纯海外硬件销量且无明确竞争格局迁移点 |
| industry-candidate-020 工会就贝塞斯达裁员提起法律行动 | exclude | - | 事件1×相关1+钩子2 = 3；E×R+M=3，纯海外劳资事件 |
| industry-e0-001 E=0记录审计：“哈利·波特的魔法世界”全新灯光秀首次登陆北京环球度假区，8月3日起限时亮相 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-002 E=0记录审计：《影之刃 零》过审：2026年7月份网络游戏审批信息公布 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-003 E=0记录审计：引擎轰鸣特工就位《坦克世界：征程》参展2026ChinaJoy | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-004 E=0记录审计：360游戏亮相2026ChinaJoy：开启射击游戏的同频共振 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-005 E=0记录审计：《昭和米国物语》确认参展26年科隆游戏展，带来全新预告及现场试玩 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-006 E=0记录审计：【抽奖】与魔法使一同工作吧！异世界工作陪伴冒险游戏《梅莫莉：治愈物语》今日登陆Steam平台 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-007 E=0记录审计：《饿狼传说：群狼之城》季票3 首发DLC角色“瑞克·斯托德”现已上线！ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-008 E=0记录审计：【抽奖】三人合作恐怖游戏《午夜轮班》现已正式发售，上夜班还得鉴“伪人”？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-009 E=0记录审计：《机械狂欢》将于 7 月 30 日发售，失败即暴毙的暴力派对游戏即将上线 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-010 E=0记录审计：与古神做交易 策略卡牌自走棋《神之一手》8月6日登陆Steam | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-011 E=0记录审计：经典异色战棋 SRPG《幻世录 重制版》Steam 试玩版即日起免费开放下载！ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-012 E=0记录审计：《双点医院：满血痊愈典藏版》主机版定于9月15日发售 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-013 E=0记录审计：分析师：美国年内仅有七款PS5实体游戏版销售超过10万 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-014 E=0记录审计：温泉恐怖模拟游戏《异界宿帐》正式公布，将于年内发售 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-015 E=0记录审计：《NBA 2K27》现已开启预购，国区售价298元起 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-016 E=0记录审计：《苏丹的游戏》移动版今日推出 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-017 E=0记录审计：暴雪嘉年华2026终极纪念典藏礼包现已上架 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-018 E=0记录审计：喜加一：《又一个僵尸塔防HD》免费领 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-019 E=0记录审计：扎克·克雷格执导，电影《生化危机:爆发夜》公布正式预告片 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-020 E=0记录审计：电影《哆啦A梦 大雄的蒸汽时间车》2027年春季上映 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-021 E=0记录审计：来自印度的2/3D视角切换的解谜新游——《渡渡鸭与折叠世界》售价与发售日公布 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-022 E=0记录审计：《这龙带刀》——魂系恐龙动作 RPG 登场 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-023 E=0记录审计：格斗游戏《漫威斗魂》现已开启公开B测 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-024 E=0记录审计：《空之轨迹 the 2nd》中文版公开追加首批暨预购特典详情，及更多系统与角色的相关情报 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-025 E=0记录审计：微星神影16 魔龙姬限定款 锐龙版上市：首发到手低至8499+双重礼盒 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-026 E=0记录审计：献血赠暗源战锤40k系列模型：上海开启“酷暑热血潮玩季”第一波活动 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-027 E=0记录审计：《三国志14 with 威力加强传承版》现已开放Steam版预购 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-028 E=0记录审计：英伟达听劝！DLSS 5给出三种方案，游戏公司可以不选“AI脸”了？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-029 E=0记录审计：玩家集体上头！Steam试玩在线人数破万，PVE自走棋《裂隙远征》是下个爆款？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-030 E=0记录审计：193国产4款进口游戏获版号：《影之刃零》过审，网易三七B站勇仕在列 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-031 E=0记录审计：2026年，如何让欧美发行商看上你的游戏？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-032 E=0记录审计：研发3年，初代团队，网易新游制作人：我们的游戏很下饭 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-033 E=0记录审计：沉寂近两年，网易生活模拟新作首测：赶个晚集？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-034 E=0记录审计：H2 Interactive，《IGS 经典街机合集(IGS Classic Arcade Collection)》PC STEAM 版 8月 13日正式上线 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-035 E=0记录审计：易中天第一次和游戏合作？他给《战意：三国》出了一套“历史考卷” | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-036 E=0记录审计：因为一场开发者沙龙，我和《异环》发行制作人聊了聊 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-037 E=0记录审计：7月197款版号下发，AI乙游拿到版号、《影之刃零》在列 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-038 E=0记录审计：高难攻略！魔域口袋版12星副本通关指南 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-039 E=0记录审计：二游界终于来了个最对味的侦探悬疑剧 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-040 E=0记录审计：韩国文化产业振兴院的KOREA GAME PAVILION将于7月31日至8月3日参展2026 ChinaJoy BTOC，精彩不容错过！ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-041 E=0记录审计：西班牙Games from Spain官方展团首次亮相ChinaJoy | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-042 E=0记录审计：沉浸式开店《 奶茶店模拟器》正式发售！首发全年最低价 6.5 折 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-043 E=0记录审计：开启盛夏狂欢！《碧蓝航线》新版本上线清凉节广州站今日启幕 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-044 E=0记录审计：版本大热、线下火爆，这款走过四年的搜打撤先驱还在进步？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-045 E=0记录审计：Ubisoft Q1 net bookings down 9.2%, attributes drop to "high comparison base" from same period last year | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-046 E=0记录审计：Meccha Chameleon ranks second behind Fortnite in PC revenue for June | Newzoo charts | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-047 E=0记录审计：Ubisoft expects "superior financial performance" from Black Flag remake, but won't increase guidance due to "strong competitive lineup" | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-048 E=0记录审计：The games industry is stifled by a culture of fear | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-049 E=0记录审计：Ash Games Studio secures $1.5m seed funding for Saudi-inspired games | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-050 E=0记录审计：New release roundup: Poinpy, Don’t Starve Together, Tiny Bookshop, and more | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-051 E=0记录审计：Get key insights on the Nordic games market in 2026 with our free region report | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-052 E=0记录审计：Rovio's Anastasiya Kara on how live ops took over mobile's biggest games | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-053 E=0记录审计：Playtika's future, parents embracing games, Pokémon Champions and China's games market | Week in Views | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-054 E=0记录审计：Saudi-led EA buyout receives EU approval, Xbox trials ad-supported game streaming, and Poinpy is eternal - Patch Notes #62 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-055 E=0记录审计：How Jackbox Games navigated the post-pandemic sales slump ft. Mike Bilder | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-056 E=0记录审计：New game digest: Don’t Starve, DCKO, Toca Boca, Poinpy, Gangstar and more | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-057 E=0记录审计：重磅，TikTok在美测试付费短剧APP，专注真人短剧 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-058 E=0记录审计：《金铲铲之战》把已经“封神”的赛季又更新了一遍 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-059 E=0记录审计：触乐怪话：如果在雨夜，一根黄瓜 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-060 E=0记录审计：《这龙带刀》发售宣传视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-061 E=0记录审计：宫本茂谈任天堂重置经典作品：可引向未来开发 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-062 E=0记录审计：开发者：索尼早知停产实体盘将引发巨大公关危机 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-063 E=0记录审计：前育碧总监：大型游戏开发如同躲避燃烧木桶 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-064 E=0记录审计：《魔界战记》创作者抨击索尼放弃光盘 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-065 E=0记录审计：《宝可梦 钻石／珍珠》泄露逾百个废弃设计 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-066 E=0记录审计：《超级少女》院线失利后将于7月28日上线流媒体平台 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-067 E=0记录审计：电影《生化危机：爆发夜》预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-068 E=0记录审计：《EA SPORTS FC 27》公布预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-069 E=0记录审计：动画《机动战士高达RG XARX-ZERO》预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-070 E=0记录审计：PS5 Pro版《光环：战役进化》实机演示 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-071 E=0记录审计：《街头霸王6》「亚思敏」角色指南 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-072 E=0记录审计：《漫威斗魂》开场动画 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-073 E=0记录审计：电影《寒夜怪谈》预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-074 E=0记录审计：《漫威金刚狼》剧情预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-075 E=0记录审计：《控制：共振》「踏入新世界」开发者日志 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-076 E=0记录审计：《斯普拉遁 涂击队》发售宣传视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-077 E=0记录审计：《光环：战役进化》发售预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-078 E=0记录审计：《漫威斗魂》「黑豹」角色指南 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-079 E=0记录审计：《007：初露锋芒》高级授权项目负责人专访｜IGN 中国 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-080 E=0记录审计：《沉没之城2》上手前瞻 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-081 E=0记录审计：《Big Walk》上手前瞻 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-082 E=0记录审计：《斯普拉遁 涂击队》评测 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-083 E=0记录审计：《影之刃零》版号已至，WeGame 预约正式开启 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-084 E=0记录审计：《影之刃零》WeGame端宣传视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-085 E=0记录审计：《七龙珠 电光炸裂！ZERO》极限超突破DLC「NEO」发售日预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-086 E=0记录审计：《漫威斗魂》「危境」角色指南 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-087 E=0记录审计：《饿狼传说：群狼之城》「瑞克·斯托德」上线宣传视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-088 E=0记录审计：电影《歪心狼对阵ACME》预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-089 E=0记录审计：《遗物：第一守护者》「战斗」介绍视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-090 E=0记录审计：《降世神通 传奇：格斗游戏》发售宣传视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-091 E=0记录审计：《漫威斗魂》「Phoenix Cyclops」角色预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-092 E=0记录审计：《灾厄堡垒》「古老王国」DLC公布预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-093 E=0记录审计：《苏丹的游戏》移动版今日正式推出 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-094 E=0记录审计：Switch 2版《异度神剑2》介绍视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-095 E=0记录审计：本周 Steam 值得关注的游戏 07.20 - 07.26（五） | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-096 E=0记录审计：itch 一周游戏汇：7月13日-7月19日（上） | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-097 E=0记录审计：MSI celebrates 40 year anniversary by unveiling a SEVEN GRAND LAPTOP | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-098 E=0记录审计：FromSoftware reveals final stats of new Elden Ring classes, and one of them already got a tiny nerf | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-099 E=0记录审计：AMD calls CUDA a 'non-event', says companies are programming at levels where the Nvidia tech doesn't really matter | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-100 E=0记录审计：Ubisoft chief says Sony's decision to kill game discs isn't going to be a big deal | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-101 E=0记录审计：Atari signs 10-game deal with Universal for movies based on Pong, Breakout, Centipede, and yes, really, Pong | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-102 E=0记录审计：A new expansion and the ability to be a crow wizard has me enjoying a 10-year-old action RPG for the first time | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-103 E=0记录审计：The full trailer for Zach Cregger's Resident Evil is here, and holy cow I think this one might actually be good | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-104 E=0记录审计：Blizzard fires World of Warcraft game master who insta-killed bosses for friends | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-105 E=0记录审计：Star Wars Zero Company reveals cast, including fan favorite actors from Clone Wars animated series | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-106 E=0记录审计：The best Palworld 1.0 pals for running your base like a well-oiled machine | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-107 E=0记录审计：Forget Ultra settings, Halo: Campaign Evolved looks nearly as good with everything set to Low | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-108 E=0记录审计：You have 3 days to obtain Big Boss rating in Metal Gear Solid 1's free-to-play period on Steam | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-109 E=0记录审计：Is Intel back? Company's latest earnings report remarkably different in tone to 12 months ago | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-110 E=0记录审计：Halo: Campaign Evolved early adopters were unable to play the game on Steam as it kept forcing them to look at the art book instead | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-111 E=0记录审计：We now have independent testing confirming Razer's latest innovative mouse sensor tech does what it says it does | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-112 E=0记录审计：Halo remake reviews totter as fans lament the 3 horsemen of 2026 game releases: Bugs, pointless logins, and duff servers | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-113 E=0记录审计：Bethesda says layoffs haven't affected 'the roadmap' for The Elder Scrolls 6, it hasn't forgotten Oblivion Remastered, and it's not telling you this because Asha Sharma forced it to | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-114 E=0记录审计：The fourth biggest memory manufacturer could break into America soon, and chances are you've never heard of it | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-115 E=0记录审计：AMD Zen 6 server processors have me hopeful for some beefy desktop chips—it shouldn't be too long before Zen 7 and 8 drop either | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-116 E=0记录审计：Where to find Naruo Golf Course in Forza Horizon 6 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-117 E=0记录审计：OpenAI全面开放ChatGPT Health功能！通用AI助手切入医疗健康赛道，垂类App是否还有突围机会？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-118 E=0记录审计：半年过去，鹰角把“南墙”撞破了 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-119 E=0记录审计：二游美学巅峰还是太“猛”了 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-120 E=0记录审计：爆肝20小时后，我觉得二游赛道要变天了 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-121 E=0记录审计：TATA木门明确首个行业静音标准 “静有级·竞无限”引领好房子新赛道 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-122 E=0记录审计：腾讯想给搜打撤“换个活法” | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-123 E=0记录审计：微星机箱再添新作 VIXTA 300维斯塔机箱双版本齐发 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-124 E=0记录审计：《战意：三国》今日上线：七年坚守，打造独一份的古代战争 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-125 E=0记录审计：轻量化电竞服务新选择，知悦电竞小程序凭合规与硬核实力站稳护航赛道 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-126 E=0记录审计：2026年7月电竞椅品牌推荐：平价档三场景选购梳理 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-127 E=0记录审计：H2 Interactive，《IGS 经典街机合集(IGS Classic Arcade Collection)》PC STEAM 版 8月 13日正式上线 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-128 E=0记录审计：投稿丨集你所爱，2026 ChinaJoy 骁龙主题馆在N5馆等你 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-129 E=0记录审计：对话 | 网易新作：闭关1年多，项目终于冒泡 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-130 E=0记录审计：原创 | 腾讯头牌今日出手：仅凭两把「钥匙」，就让赛季活起来了 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-131 E=0记录审计：三七互娱：上新速度，遥遥领先 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-132 E=0记录审计：《三国志14 with 威力加强传承版》现已开放Steam版预购 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-133 E=0记录审计：献血赠暗源战锤40k系列模型：上海开启“酷暑热血潮玩季”第一波活动 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-134 E=0记录审计：格斗游戏《漫威斗魂》现已开启公开B测 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-135 E=0记录审计：《空之轨迹 the 2nd》中文版公开追加首批暨预购特典详情，及更多系统与角色的相关情报 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-136 E=0记录审计：微星神影16 魔龙姬限定款 锐龙版上市：首发到手低至8499+双重礼盒 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-137 E=0记录审计：来自印度的2/3D视角切换的解谜新游——《渡渡鸭与折叠世界》售价与发售日公布 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-138 E=0记录审计：《这龙带刀》——魂系恐龙动作 RPG 登场 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-139 E=0记录审计：扎克·克雷格执导，电影《生化危机:爆发夜》公布正式预告片 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-140 E=0记录审计：电影《哆啦A梦 大雄的蒸汽时间车》2027年春季上映 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-141 E=0记录审计：《苏丹的游戏》移动版今日推出 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-142 E=0记录审计：暴雪嘉年华2026终极纪念典藏礼包现已上架 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-143 E=0记录审计：喜加一：《又一个僵尸塔防HD》免费领 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-144 E=0记录审计：《战神：劳菲》将于27年2月16日在PS5发售 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-145 E=0记录审计：《骑马与砍杀》开发商联合创始人、“骑砍之母”İpek Yavuz去世，终年54岁 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-146 E=0记录审计：走过16年，全球第一的竞技游戏打算“回到过去” | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-147 E=0记录审计：这家上海厂商打响了二游次世代战争第一枪 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-148 E=0记录审计：游戏行业到底有多少天才被埋没了？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-149 E=0记录审计：2026ChinaJoy开展倒计时！咪咕游戏焕新亮相，JDG无畏空降、1元抢PC新品等你来 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-150 E=0记录审计：景德镇成功列入世界遗产名录，全球首款申遗小游戏《数字景德镇·瓷都小匠》上线 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-151 E=0记录审计：网易最离谱的新品，《遗忘之海》吓到我了 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-152 E=0记录审计：《女神异闻录4 Revival》配音演员访谈：如何用中文诠释经典角色 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-153 E=0记录审计：不失忆的二游主角，《白银之城》是真在试些新东西 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-154 E=0记录审计：《静谧田园》制作人访谈：在治愈的田园生活中打造“致郁”体验 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-155 E=0记录审计：牌佬COS成自己最爱的角色，赢下了全国第一 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-156 E=0记录审计：一部关于蒙古帝国的“历史同人”，怎么就成了七月新番的超级黑马？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-157 E=0记录审计：After half a decade of job losses, there is no "business as usual" | Opinion | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-158 E=0记录审计：The PG Connects World Tour 2026 continues with Shanghai, Montréal, Helsinki and more! | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-159 E=0记录审计：Thanks to the sponsors of PG Connects Summit Shanghai | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-160 E=0记录审计：触乐本周行业大事：7月版号下发，《遗忘之海》移动端正式公测，《明末：渊虚之羽》游戏全球玩家总量突破500万 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-161 E=0记录审计：一款游戏和它背后的世界遗产 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-162 E=0记录审计：《三国志14 with 威力加强传承版》宣传视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-163 E=0记录审计：剧集《银翼杀手2099》先导预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-164 E=0记录审计：《异于天堂》战斗演示视频 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-165 E=0记录审计：《战神：劳菲》发售日预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-166 E=0记录审计：《数字景德镇·瓷都小匠》前瞻：掌中一瞬，瓷都千年 | IGN 中国 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-167 E=0记录审计：网易的第一款大世界2游终于公测！从策划视角带你解构《遗忘之海》 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-168 E=0记录审计：背包塔防已经让玩家疲劳，《功夫老六》为什么还能跑出来？ | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-169 E=0记录审计：Minecraft Java Edition system requirements want 8/16 GB RAM for the first time, but it isn't more demanding now, Microsoft just hadn't updated the specs in a while | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-170 E=0记录审计：I suck at fighting games, but Marvel Tōkon has the sauce | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-171 E=0记录审计：Asus ROG Azoth Extreme Edition 20 review | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-172 E=0记录审计：Amazon Gaming boss says high hardware prices could be good news for its Luna cloud gaming program | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-173 E=0记录审计：Saudi Arabia's takeover of EA gets approval from European Commission | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-174 E=0记录审计：Tomb Raider: Catalyst delayed to 2028 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-175 E=0记录审计：Warhorse trademarks 'Kingdom Come Salvation' as fans pray in unison for another open-world RPG | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-176 E=0记录审计：Even Japan's patent officials seem exhausted with Nintendo's antics as they refuse its 'absurd' defense of a rejected Pokémon patent | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-177 E=0记录审计：MMO life sim Seed's AI-powered avatars prove once again that nothing shatters immersion quicker than crappy chatbot dialogue | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-178 E=0记录审计：Hell Let Loose: Vietnam is open to all this weekend for a free playtest | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-179 E=0记录审计：MindsEye has multiplayer and a grenade football mode now, which the handful of people still playing it will no doubt be thrilled to hear | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-180 E=0记录审计：Modding wizard creates Grand Theft Auto multiverse that lets players travel instantly between Rockstar's first three games: 'We got inter-GTA portals before GTA 6' | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-181 E=0记录审计：There's only one Jedi Operator in Star Wars Zero Company, and reckless players may end up with none at all: 'Be careful that nothing unfortunate happens to her!' | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-182 E=0记录审计：Discussion time: Have you ever said goodbye to an MMO you've played for 1,000s of hours? | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-183 E=0记录审计：Modders finally got a high-quality third-person camera working in Baldur's Gate 3 for all you Dragon Age sickos | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-184 E=0记录审计：It's taken 13 years, but Final Fantasy 14 has finally broken the Sephiroth-shaped emergency glass | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-185 E=0记录审计：景德镇成功列入世界遗产名录，全球首款申遗小游戏《数字景德镇·瓷都小匠》上线 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-186 E=0记录审计：2026ChinaJoy开展倒计时！咪咕游戏焕新亮相，JDG无畏空降、1元抢PC新品等你来 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-187 E=0记录审计：游戏日报发布2026年7月UGC平台排行榜 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-188 E=0记录审计：《骑马与砍杀》开发商联合创始人、“骑砍之母”İpek Yavuz去世，终年54岁 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-189 E=0记录审计：《战神：劳菲》将于27年2月16日在PS5发售 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-190 E=0记录审计：《最终幻想14》8.0版本公布「银海之天舟」加长先导预告片 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-191 E=0记录审计：今天，鹰角在上海干了件大事 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-192 E=0记录审计：腾网盛趣巨人大战上海滩；杭州二次元百人团队解散 丨 HOT周报 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-193 E=0记录审计：上线不满一年，蔡浩宇的AI产品AnuNeko宣布永久停运 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-194 E=0记录审计：运营《问道》私服被判赔近300万；用百万公民信息套利，获刑三年 | 一周说「法」 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-195 E=0记录审计：发行泡汤、V社警告，却流水超6亿，制作人：我本来最不看好它…… | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-196 E=0记录审计：爬了900多万条高校招生数据，我发现游戏行业越来越不相信创意了 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-197 E=0记录审计：开发者详解《黎明行者之血》中的吸血鬼氏族：“我很反感为了坏而坏的反派”| IGN First | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-198 E=0记录审计：《最终幻想14》「银海之天舟」先导预告 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-199 E=0记录审计：itch 一周游戏汇：7月13日-7月19日（下） | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-200 E=0记录审计：Conceived in a secure military facility, this Jedi Knight fansite has been running consistently for almost 30 years: 'It looks really close to what it did back in 1998' | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-201 E=0记录审计：Silent Hill f producer says its writers were pushed 'to read at least 100 to 200 books a year' | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-202 E=0记录审计：One excellent, unforgettable expansion has fixed Doom: The Dark Ages | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-203 E=0记录审计：New report alleges it took a week for OpenAI to realize a prototype had gone rogue and hacked another company | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-204 E=0记录审计：Final Fantasy 14 has finally added the class I'm always asking for: a Viking with two shields, laser cannons, and Wolverine claws | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-205 E=0记录审计：Games industry analyst says Meccha Chameleon's June revenue on PC was second only to Fortnite | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-206 E=0记录审计：Videogame villains who sing at you are the best | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-207 E=0记录审计：Larian once again reminds us it's 'not involved in any BG3-related projects' in response to Karlach comic reveal | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-208 E=0记录审计：A crossover between Dungeons & Dragons and World of Warcraft has leaked | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-209 E=0记录审计：A classic Giger-inspired adventure game just got a sequel | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-210 E=0记录审计：Steam may be celebrating the railway experience with its Train Fest, but let's remember how rubbish the typical train trip is with some Train Sim World DLC | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-211 E=0记录审计：Call of Duty: Modern Warfare 4's beta will have low-SBMM playlists, as Activision continues to 'learn a lot about multiplayer matchmaking' | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-212 E=0记录审计：Helldivers 2 is giving players a free car in October, except for those who already earned it in June | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-213 E=0记录审计：Rockstar co-founder says 'I don't know if I personally care' if games release on disc, adds 'I love physical media' | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-214 E=0记录审计：Marvel confirmed a Nova movie after its San Diego Comic-Con panel ended | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-215 E=0记录审计：Splatoon Raiders endgame turns it into Nintendo’s Vampire Survivors | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-216 E=0记录审计：Dungeons & Dragons: Honor Among Thieves 2 might never get made | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-217 E=0记录审计：Star Trek: Strange New Worlds cast reveal why Kirk and Spock still aren't best friends in season 4 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-218 E=0记录审计：TATA木门明确行业首个静音标准，“静有级·竞无限”引领好房子新赛道 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-e0-219 E=0记录审计：观察｜一家在战争中创立的游戏公司：从6人到近50人，别丢了乐趣和自己 | exclude | - | 事件0×相关0+钩子0 = 0；版号、普通版本、活动、宣传、纯榜单或非游戏记录，E=0排除 |
| industry-unavailable-001 不可用正文记录：2026年ChinaJoy京东美妆游乐园 领鸡蛋&出片 剧透 | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-002 不可用正文记录：2026 ChinaJoy BTOB 展前预览公布！ | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-003 不可用正文记录：Xbox has started testing the option to stream games for free with ads at the start | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-004 不可用正文记录：Ubisoft CEO Yves Guillemot says Sony scrapping discs won’t disturb the industry too much | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-005 不可用正文记录：Assassin’s Creed Black Flag Resynced ‘exceeded annual expectations’ in its first two weeks, Ubisoft says | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-006 不可用正文记录：Marvel Tokon: Fighting Souls open beta available now on PC and PS5 | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-007 不可用正文记录：Previously cancelled Age of Empires 3 DLC expansion has been re-announced and releases in September | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-008 不可用正文记录：Kingdom Come Salvation trademark filed in the EU | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-009 不可用正文记录：Podcast: It’s hard to get excited about the future of Fallout | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-010 不可用正文记录：007: First Light’s first content update is available now | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-011 不可用正文记录：PSN still down several hours after Marvel Tokon open beta goes live | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-012 不可用正文记录：EA Sale To Saudi Arabia Clears A Major Hurdle | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-013 不可用正文记录：Microsoft Brings Ads To Xbox In A Big New Way, Promises No Gameplay Interruption | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-014 不可用正文记录：With $1,000 Consoles On The Horizon, Amazon Games Boss Offers A Solution That Absolutely No One Asked For | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-015 不可用正文记录：Halo Remake Players On Xbox Who Paid More To Play Early Can’t | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-016 不可用正文记录：Avatar Legends: The Fighting Game Delayed At Last Moment On Xbox | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-017 不可用正文记录：Ex-PlayStation Boss Calls For A Return To The Good Old Days Of AA Gaming | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-018 不可用正文记录：Batman Is Finally Getting A New Game, Just Not The One You Were Expecting | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-019 不可用正文记录：Ubisoft Boss Has A Hot Take On Sony Killing Game Discs | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-020 不可用正文记录：EA Sports FC 27 Has A New $150 Edition, Because Ultimate Wasn’t Ultimate Enough | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-021 不可用正文记录：Resident Evil Movie Star Nearly Died During Filming After 150-Pound Blood Bag Almost Hit Him | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-022 不可用正文记录：Atari Announces 10-Movie Deal With Universal But Don’t Expect Them All To Get Made | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-023 不可用正文记录：Reacher Star Alan Ritchson Loves Call Of Duty, Would Be Up For Being In The Movie | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-024 不可用正文记录：Resident Evil 4 Has Sold More Than Twice As Much As Any Other Current-Gen Remake | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-025 不可用正文记录：Here’s Why The New Resident Evil Movie Has Snow And Smartphones | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-026 不可用正文记录：Is PSN Down? It Was For Hours Today, But It’s Back Up Now | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-027 不可用正文记录：Rhythm Heaven Groove review: Nintendo’s musical paradise makes a much needed return | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-028 不可用正文记录：GTA 6 download codes expire only 170 days after launch in Japan | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-029 不可用正文记录：PlayStation confirms God of War Laufey release date and return of Kratos in next game | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-030 不可用正文记录：Rockstar co-founder Dan Houser says if people want games on disc ‘companies should provide it’ | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-031 不可用正文记录：Tomb Raider Catalyst Quietly Gets Delayed To 2028 | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-032 不可用正文记录：Sega Won’t Ditch Physical Media, But Says Digital Expansion Is Vital | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-033 不可用正文记录：GTA 6 Is The First Game I’ve Seen With A Best-Before Date | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-034 不可用正文记录：Halo: Campaign Evolved Secret Ending Seems To Tease A Halo 2 Remake | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-035 不可用正文记录：Blizzard Employee Out Of A Job After Allegedly Helping Friends Cheat In WoW | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-036 不可用正文记录：Resident Evil Movie Trailer On PlayStation’s YouTube Page Is Full Of People Asking Sony To Change Course On Discs | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-037 不可用正文记录：Jimothy, The Viral Raccoon, Is Becoming An Earnable WoW Pet | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-038 不可用正文记录：Surprise: God Of War Laufey Has A Release Date, And Its Kratos-Led Sequel Has Been Announced | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| industry-unavailable-039 不可用正文记录：Kratos’ Next God Of War Game Will Pick Up Where Laufey Leaves Off | exclude | - | 事件0×相关0+钩子0 = 0；正文不可用，禁止作为事实证据 |
| ai-candidate-001 英伟达公开DLSS 5生成增强层工作方式 | include | ai | AI直接作用于游戏渲染管线 |
| ai-candidate-002 AnuNeko宣布永久停运并调整研发资源 | include | ai | AI陪伴产品生命周期与游戏角色交互研发资源调整 |
| ai-candidate-003 Seed实装AI角色对话并出现体验问题 | include | ai | AI已直接作用于生活模拟MMO的NPC与教程交互 |
| ai-candidate-004 FLUX 3与mimic发布视频生成能力 | exclude | - | 通用视频生成更新，缺少游戏场景直接落地证据 |
| ai-candidate-005 通用创意工具例行更新 | exclude | - | 能力变化偏例行，缺少可核验的游戏迁移结果 |
| ai-candidate-006 与游戏迁移链条不足的AI记录批量审计 | exclude | - | 无游戏直接应用，且无法从来源建立具体迁移链条 |
| community-candidate-001 蔚蓝档案卡池机制调整引发成本争议 | include | community | 窗口内新建的具体社区事件，触发与争议逻辑完整 |
| community-candidate-002 代号鸢二创奖励到付引发创作者质疑 | include | community | 窗口内发生并延续的具体创作者激励争议 |
| community-candidate-003 白银之城短裤设计与拉黑指控继续讨论 | exclude | - | 核心触发已在上一周报处理；本窗口新增主播拉黑仅为玩家推测，证据不足 |
| community-candidate-004 卡厄思梦境新赛季削弱成型卡组 | exclude | - | 触发事件发生于上一窗口且已在周报报道，本窗口无实质新增进展 |
| community-candidate-005 2024年派克特歌曲争议旧帖恢复回复 | exclude | - | 原始触发发生于2024年，仅有旧帖新回复，不构成新事件 |
| community-candidate-006 剧情中的隐私越界设定引发安全讨论 | exclude | - | 触发发生于7月22日，窗口内只有延续回复且无新进展 |
| community-candidate-007 抗洪物资归属与诈捐标签形成罗生门 | exclude | - | 帖子明确标注多处存疑，无法核验主体和时间线 |
| deep-candidate-001 AI角色交互从无限对话转向可信体验与持续运营约束 | include | deep | R3/I3/E3/C3=12；两条本期AI入选事件共同支持变化—机制—下游影响 |
| deep-candidate-002 Steam评价门槛如何影响购买转化 | include | deep | R2/I3/E3/C3=11；单篇高质量调查提供完整可核验数据与平台机制分析 |
| community-candidate-008 无法命名为单一新事件或缺乏窗口内进展的社区记录批量审计 | exclude | - | 重复快照、泛讨论、梗图或缺少完整事件四要素 |
| release-candidate-001 山海奇旅｜2026-07-24 首次测试 | include | release_calendar | 事件3×来源4=12；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-002 盗梦英雄2：幻野｜2026-07-24 正式上线 | include | release_calendar | 事件3×来源3=9；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-003 漫威斗魂｜2026-07-24 公开B测 | include | release_calendar | 事件3×来源3=9；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-004 数字景德镇·瓷都小匠｜2026-07-25 正式上线 | include | release_calendar | 事件3×来源3=9；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-005 战神：劳菲｜2027-02-16 定档 | exclude | - | 事件2×来源4=8；超过本报告产品日历条数上限 |
| release-candidate-006 午夜轮班｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-007 机械狂欢｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-008 双点医院：满血痊愈典藏版｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-009 异界宿帐｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-010 碧蓝航线｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-011 这龙带刀｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-012 超级少女｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-013 斯普拉遁 涂击队｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-014 光环：战役进化｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-015 饿狼传说：群狼之城｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-016 降世神通 传奇：格斗游戏｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-017 战意：三国｜2026-07-24 正式上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-018 Hololive Dreams｜2026-07-24 全球上线 | exclude | - | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-019 IGS 经典街机合集(IGS Classic Arcade Collection)｜2026-08-13 定档 | exclude | - | 事件2×来源3=6；超过本报告产品日历条数上限 |
| release-candidate-020 渡渡鸭与折叠世界｜2026-07-24 新品定档 | exclude | - | 事件2×来源2=4；单源不具备正文资格 |
| release-candidate-021 渡渡鸭与折叠世界｜2026-07-25 新品定档 | exclude | - | 事件2×来源2=4；单源不具备正文资格 |
| release-candidate-022 苏丹的游戏｜2026-07-24 移动版上线 | exclude | - | 事件1×来源4=4；超过本报告产品日历条数上限 |
| release-candidate-023 拳皇全明星｜2026-07-24 删档测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-024 丹墨三国：弈 招募中｜2026-07-24 首测 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-025 使命召唤手游｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-026 MagicShooter｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-027 万创修仙｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-028 三国搜打撤・将星对决｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-029 三脚猫行动｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-030 专注农场｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-031 乾坤袋大乱斗｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-032 你来嘛英雄｜2026-07-24 限量测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-033 冒险之旅｜2026-07-24 限量测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-034 凡尘修道录｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-035 十二生肖：决战牛顿｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-036 友可赢｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-037 回声地宫｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-038 团子矿场｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-039 夜话古今｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-040 字不可挡｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-041 弹弹收集家｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-042 我即是天道｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-043 我在废土当主播｜2026-07-24 限量测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-044 挂机刷装备｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-045 挂机西游｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-046 指点江山｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-047 暗黑融合刷宝无限副本｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-048 暗黑：深渊猎宝人｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-049 木剑｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-050 梦想英雄｜2026-07-24 限量测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-051 消消寻宝｜2026-07-24 不限量测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-052 烧脑茬次元冒险｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-053 王城守卫战｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-054 疯人院之浮屠塔｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-055 疯狂物理实验室｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-056 百战天猫｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-057 砍柴成为道祖｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-058 给我守住！｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-059 美梦物语｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-060 脑力锻炼挑战｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-061 荒野求生｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-062 谁淹了我的世界｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-063 贫僧略通拳脚｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-064 资本航线商业人生｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-065 赵云消消兵｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-066 超市大亨｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-067 金融投资模拟｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-068 钢铁突击｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-069 集装箱盲盒｜2026-07-24 不限量测试 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-070 鲜活蝴蝶合集｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-071 麒麟洲修心纪｜2026-07-24 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-072 命运代码：侵入｜2026-07-25 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-073 星际开荒模拟器｜2026-07-25 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-074 我的奶茶屋｜2026-07-25 正式上线 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-075 追逐卡蕾多｜2026-07-26 首测 | exclude | - | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-076 梅莫莉：治愈物语｜2026-07-24 老品跨平台上线 | exclude | - | 事件1×来源2=2；单源不具备正文资格 |
| release-candidate-077 神之一手｜2026-07-24 老品跨平台上线 | exclude | - | 事件1×来源2=2；单源不具备正文资格 |
