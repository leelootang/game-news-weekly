# Selection Decisions

- 行业新闻 E×R+M 打分记录：每条候选均记录“事件E×相关R+钩子M = 终分”并标include/exclude（例如事件3×相关3+钩子1 = 10）；E=0一票否决，周末报终分≥7方可入选，正文按终分降序。
- 产品日历漏挂反查：已扫描industry_news全部上线、定档、测试、首曝与停运节点；多源合格项进入release_calendar_audit，其余均在同步决策中显式exclude。
- 卡片曝光去重：SteamDB历史匹配项均card_exposed=false，本期8分且为最高合格未曝光重复，采用唯一card_carryover；《仙境传说3》与《Wardogs》历史已有card_exposed=true，仅因本期存在可核验新状态而以material_update入选。其他重复项均排除。
- 维度覆盖自检：国内移动/国产产品与人才=7张；市场数据=4张；并购=2张；平台政策=1张；档期变动=1张；资本组织=1张；海外重大=2张。
- SteamDB prior_card_exposed=False; prior_card_rank=[None, None] / limit=[10, 10]。
- 仙境传说3 new_facts=B站预约数近60万；测试号被炒至上千元；9月4日团队解释赛季制设计。
- Wardogs new_facts=封闭测试Steam同时在线超过20万；团队把3000至5000日均同时在线视为可持续目标。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 Story Kitchen筹备三款Roblox游戏电影 | include | industry_news | 当前采访披露三款Roblox体验的影视改编项目；Roblox为固定最高关注主体。 |
| I002 Savvy Games Group签署两份产业人才合作备忘录 | exclude | industry_news | 固定最高关注主体的新产业合作；正文仅采用可读取摘录中的确定事实。 |
| I003 《黎明行者之血》全球发售及首日表现 | include | industry_news | 网易少数股权投资团队的新RPG正式发售，并有首日市场数据。 |
| I004 索尼音乐娱乐日本收购GungHo 22.9%股份 | include | industry_news | 手游公司重大股权与战略合作变化；仅采用全文来源中的确定事实。 |
| I005 《仙境传说3》首测反馈与产品数据 | include | industry_news | 历史只记录首测档期；本期新增首测结果、预约规模与后续赛季制说明。 |
| I006 Nexus Mods收购SteamDB | include | industry_news | 双周历史同事件均未进入订阅卡片，本期多源再次召回且8分，为唯一合格补位。 |
| I007 《Wardogs》封测峰值突破20万 | include | industry_news | 历史已曝光的是近50万参与和10万峰值；本期新增20万同时在线与长期健康规模目标。 |
| I008 8月抖音小游戏畅销榜结构变化 | include | industry_news | 不是逐名次摘录，而是中国小游戏市场品类与换血结构数据。 |
| I009 8月全球手游收入结构变化 | include | industry_news | 全球移动市场结构数据直接覆盖多家中国厂商与重点赛道。 |
| I010 《剑侠世界4：无限》公测定档 | include | industry_news | 国产重点产品在本窗口公布明确公测日期；单源钩子记1分。 |
| B001 Xbox Game Pass云游戏将按套餐限制为每月5至15小时 | exclude | industry_news | 平台收费与使用上限变化，但海外云游戏对当前业务迁移点为R2，总分6。 |
| B002 GTA 6预告后英国PS5与Xbox销量上升 | exclude | industry_news | 主机硬件短期销售变化，总分6，未达周末报门槛。 |
| B003 Steam 2026年迄今收入约150亿美元 | exclude | industry_news | 全球PC平台收入结构数据，总分5。 |
| B004 GungHo将于9月30日关闭Disney Pixel RPG | exclude | industry_news | 海外移动产品停运有迁移点但总分5。 |
| B005 Steam一周上线720款新游戏 | exclude | industry_news | 供给拥挤为结构数据，但全球PC市场迁移点为R2，总分5。 |
| R001 Supercell收购Metacore | exclude | industry_news | 双周历史中同一事件已进入订阅卡片，本期没有可改变判断的新事实，按repeat_only排除。 |
| R002 《Overwatch Rush》东南亚软发布 | exclude | industry_news | 双周历史中同一事件已进入订阅卡片，本期没有可改变判断的新事实，按repeat_only排除。 |
| R003 诗悦首曝《星途天城》 | exclude | industry_news | 双周历史中同一事件已进入订阅卡片，本期没有可改变判断的新事实，按repeat_only排除。 |
| R004 《米姆米姆哈》宣布停运 | exclude | industry_news | 双周历史中同一事件已进入订阅卡片，本期没有可改变判断的新事实，按repeat_only排除。 |
| R005 Savvy Games Group前CEO离任 | exclude | industry_news | 双周历史中同一事件已进入订阅卡片，本期没有可改变判断的新事实，按repeat_only排除。 |
| A001 腾讯披露AI已用于多项研发管线 | include | ai_trends | 直接作用于概念美术、绑定、动作匹配、代码审查和制作管理。 |
| A002 Claude辅助移植1993年Amiga游戏 | include | ai_trends | 亲历者给出旧代码迁移、字节级复现与人工验证的完整研发案例。 |
| A003 AI智能体驱动4X手游Colony静默上线 | include | ai_trends | AI直接作用于角色与实时3D物品生成，产品已上线移动端。 |
| C001 《崩坏：星穹铁道》末日幻影机制与血量膨胀争论 | include | community_discourse | 旧帖在窗口内持续更新，触发、抱怨逻辑与时间线完整。 |
| C002 《蓝色星原：旅谣》三测卡池方案争论 | include | community_discourse | 同一三测商业化披露的媒体证据与玩家讨论；当前阶段和分歧边界清楚。 |
| D001 八月PC新品的销量与收入分层 | include | deep_analysis | 单篇高质量newsletter给出单位销量、价格和全市场收入结构；与上期愿望单主题不同。 |
| XS0002 国产动作游戏《达巴：水痕之地》公布新宣传片，2027年春季发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0003 9月State of Play日本消息汇总，《WPCA》正式公布 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0004 《直到黎明2》公布新预告片，2027年1月28日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0005 《GTA6》限量版PS5手柄公布，11月19日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0007 9月State of Play消息汇总，《最终幻想VII：启示录》将于2027年4月8日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0008 境井仁登场！《羊蹄山之魂 完全版》“无尽追缉”模式公布新宣传片 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0009 【抽奖】《夜勤人2：无尽宝库》现已登陆PC、PS5、Xbox 及任天堂Switch 2 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0010 维多利亚风模拟经营游戏《辉光之城1907》「回响测试」开启招募 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0011 【抽奖】八位堂猎户座 3E 精英手柄套装 XBOX 版预售开启 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0012 《毒液突击队》免费更新上线，全新“回收”模式来袭 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0013 《共鸣：瘟疫传说传承》全新宣传片上线，庆贺收获媒体好评 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0014 动作塔防新作《维京防线：北境之风》现已开始Steam试玩测试 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0015 战术肉鸽自走棋《铁甲狂潮》试玩版现已更新 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0016 《爱氏物语》NS版确定于2026年9月17日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0017 布拉德·皮特新片《野兽之心》定档9月30日 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0018 HBO剧版《哈利·波特与魔法石》公布最新预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0019 Xbox网络再度中断7小时，微软深表歉意 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0020 指令战斗式RPG《Another Eden Begins》现已上线试玩版 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0021 双人太空冒险游戏《轨道双子星》现已登陆 Nintendo Switch 2 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0022 PLAYISM宣布TGS直播活动将于9月10日19时播出 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0024 《GTA5》角色扮演服务器“NoPixel V”将于9月8日登陆R星官方平台 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0025 Epic喜加一：《Alone With You》免费领 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0026 Cygames 推出全新游戏品牌，首款游戏将于 11月5日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0027 《最终幻想：共鸣》第一章抢先体验版在Steam推出 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0028 科乐美动作游戏《Rhapsody in Scarlet》公布Steam商城页 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0030 《Fate/EXTRA Record》公布新宣传片，2027年1月28日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0031 单人团本动作 RPG《Sil与消逝之境》现已推出试玩demo | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0032 节奏游戏《UTA MACROSS》复活企划启动！9月10日开启众筹项目 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0033 《零境·入侵》在State of Play发布最新预告片，同步开放测试版本 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0034 《最终幻想VII 启示录》确定2027年4月8日发售，系列三部曲迎来完结 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0035 “魔岩三杰”之一、摇滚歌手何勇去世 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0036 500万根稻草，找1根针：《大海捞针模拟器》Steam商店页正式上线 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0037 末日度假村模拟游戏《罗马流沙 RE:Build》宣布9月17日全平台发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0038 音乐游戏《白金档案》将于9月10日正式上线1.0版本，两款新DLC同步登场 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0039 《地城拓荒》今日发售：据点建设与地城探险 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0040 白宫推出五款像素游戏，宣传驱逐移民等特朗普政策 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0041 任天堂常规直面会及塞尔达40周年特别直面会将于下周举行 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0048 跟叠纸祖龙一桌，她们做了款热度Top5女性向新游 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0049 再次登顶畅销总榜，天美射击还在卷 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0050 测试号炒到2000块，上海大厂新MMO真让人上头 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0051 上线11年，这款网易MMO又创下近三个月的新高？ | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0052 现场体验DLSS 5后，我觉得游戏美术要变天了 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0053 刚刚登顶畅销总榜的天美，让玩家为一只鸭疯狂 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0054 日活850万，这款“佛系”游戏放弃年入1.4亿美元的广告收入 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0055 运营11年，冲进免费榜近三月最高，这款MMO凭什么还能打 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0056 金铲铲五周年：还在为玩家制造”启动”的理由 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0057 预约突破千万，腾讯游戏要给「种田建屋」开辟新解法 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0058 氧气不够？元气来凑！元气森林×潜水员戴夫 联动全面开启，限定周边等你来拿！ | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0059 前世嘉制作人新作《三国志BOND》将开启新赛季 首届官方大赛即将开幕 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0060 音乐游戏《白金档案》将于9月10日正式上线1.0版本，两款新DLC同步登场 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0063 Voting extended for special categories in the Best Places To Work Awards | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0066 Future imperfect: Five predictions for the next decade ／ Opinion | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0067 Nvidia acquires open-source AI platform Hugging Face for $12.9bn | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0069 How easy is it to get to Helsinki from across the Nordics? | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0070 UK legal claim seeks £2bn from Apple over App Tracking Transparency | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0073 New release roundup: Shoe it All!, Bloodless, Block Blast+, White House Arcade and more | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0077 Strategically making Star Wars Zero Company, ft. Greg Foertsch | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0079 Trump’s White House has made MAGA versions of Snake, Flappy Bird, Tetris and more | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0081 Final Fantasy 7 Revelation is getting story DLC after all, focussing on Sephiroth and Vincent | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0082 The Final Fantasy 7 Remake series is getting a $500 Japan-only collector’s edition | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0083 Crimson Desert is getting its first story DLC next month, featuring ship exploration | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0084 Here’s everything Konami announced in its latest showcase | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0087 The physical edition of Final Fantasy 7 Revelation needs to download extra game data on all formats | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0088 Months after reports that Blizzard is working on a StarCraft shooter, it seems to be teasing something | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0089 The next Mass Effect can be great if ‘people get out of the way’ and let the original creators work, former dev says | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0090 Hideki Kamiya’s Clovers on the end of discs, Capcom’s trust on Okami 2, and Scalebound hopes | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0091 Nintendo confirms 2 Nintendo Directs, including Zelda 40th Anniversary | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0092 Halloween the Game single-player review: Is there enough here for solo players? | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0093 触乐怪话：播客初体验 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0095 《致命躯壳2》：魂Like红海的另类解？ | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0096 One Of The Coziest Games Of The Year Is Helping Crunchyroll Game Vault Grow Even Bigger | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0097 Crimson Desert Channels The Sims With Its Chartering The Unknown Expansion | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0098 D&D’s World Of Warcraft Crossover May Not Be A One-Way Street | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0099 A Long-Dormant Blizzard Franchise Could Be Coming To Dungeons And Dragons | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0100 Game Pass Is Getting Worse, And More Expensive | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0101 The New Gundam Game Has A Collector’s Edition Just For Gunpla Sickos Like Me | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0102 Dungeons And Dragons Icons Could Take The TTRPG To A Modern-Day Setting | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0103 Something Is Brewing With StarCraft | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0104 The Last of Us Season 3 Did Not Include Naughty Dog’s Involvement For Creative Choices | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0105 GTA 6 Is Completely Changing How You Steal Cars | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0106 GTA 6 Online Could Struggle To Pull Players Away From GTA Online, Says Valve Veteran | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0108 Two Nintendo Directs Announced For Next Week, Including A Zelda Presentation | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0109 Xbox’s New TCL Partnership Couldn’t Come At A Worse Time | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0110 Game Director Finally Addresses His Rumored Foot Fetish–Wait, Not Kojima, The Other One | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0111 《龙与地下城：侠盗荣耀》导演谈票房失利原因 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0112 《愚者不灭》宣传视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0113 暴雪或在暗示《星际争霸》新作 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0114 10分钟看完索尼9月State of Play发布会 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0115 《Fragmentary Order》剧情预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0116 《光芒行动》游戏玩法预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0117 《Terminal War》试玩测试实机预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0118 宫崎英高回应「恋足癖」传闻：感到困惑 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0119 《2XKO》「拉克丝」角色预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0120 《动物园之星2》「野生动物保护区」宣传视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0121 《月光光心慌慌》发售预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0122 《最终幻想 RESONANCE》19分钟实机演示 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0123 《Hunter's Moon》公布预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0124 《羊蹄山之魂 完整版》「弦续关原」宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0125 乐高PlayStation套件宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0126 《未境峡谷》公布预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0127 《跑车浪漫旅7》「Spec IV」更新预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0128 《Rev. NOiR》剧情预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0129 《Rhapsody in Scarlet》公布预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0130 《Maneater 2》公布预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0131 《红色沙漠：增强版》「未知征途」DLC公布预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0132 《沙罗周期》「Zenith」更新预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0133 《七龙珠 异战3》宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0134 《最终幻想7 Revelation》「战斗与探索」介绍视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0135 《最终幻想7 Revelation》发售日预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0136 《GTA 6》限定款DualSense手柄宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0137 《直到黎明2》预购预告 ／  State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0139 PS5 Pro版《地铁2039》实机预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0140 《最终幻想 RESONANCE》试玩Demo宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0141 《怪物猎人 荒野：凌越》宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0142 《羊蹄山之魂 完整版》「无尽追缉」宣传视频 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0143 《漫威金刚狼》发售预告 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0144 电影《生化危机：爆发夜》片段 ／ State of Play | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0145 《鬼武者 剑之道》发售宣传视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0146 《海狸浮生记》1.1更新宣传视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0147 《极速跑者2：速度之王》发售宣传视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0149 《ShoreTiles》发售宣传视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0150 《忍者》游戏概览预告 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0151 本周 Steam 值得关注的游戏 08.31 - 09.06（四） | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0152 itch 一周游戏汇：8月24日-8月30日（上） | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0153 AI浪潮下，游戏出海最赚钱赛道，变了 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0154 下载量暴跌90%后，这款老游戏把用户价值翻了10倍 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0155 How to escape Xanthe's trap in The Blood of Dawnwalker | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0156 Guild Wars 3 is a lot smaller scale than Guild Wars 2 because of the new approach to combat and movement: 'You would probably see about 20 players in a large combat scenario' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0157 I installed a mod that adds building interiors to GTA 5, at the low cost of deleting most of the map's exterior | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0158 Onimusha: Way of the Sword launch times and release date | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0159 The bizarre spirit of classic Elder Scrolls games is alive and well in little lo-fi RPG A Short Quest | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0160 A multi-month delay for Deus Ex turned into a huge payoff for one of its best characters, says designer Harvey Smith | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0161 Owner of nearly decade-old Dell laptop reportedly wore through the wrist rest and is 'being stabbed by carbon fibers' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0162 DLSS 5 can be jammed into almost any game now, so I've been playing FM26 with neural rendered little computer people because that's just what I do | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0164 It's really starting to look like a new StarCraft game will be revealed at BlizzCon | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0165 I've found DLSS 5 can slash frame rates by up to 73% on an RTX 5080 gaming PC in NBA 2K27, and I'm wondering what kind of mega-rig would justify the performance hit | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0166 Nvidia puts its money where its mouth is on open weight AI, moving to buy Hugging Face for $13 billion | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0167 Xgimi Titan Noir Max review | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0168 Petit Planet's delightfully cosy galactic take on Animal Crossing is the closest we'll ever get to the life sim on PC | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0169 The Blood of Dawnwalker's mods immediately scrap the time pressure mechanic, which is apparently a dealbreaker for some people | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0170 Arc Raiders' executive producer admits its developers 'couldn't keep pace with the players' and their need for content, but promises Frozen Trail as the answer | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0171 Sick of grinding for upgrade materials like leather and iron in Onimusha: Way of the Sword? Good news: you can buy a lot of them | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0172 DLSS 5 is called 'DLSS Neural Rendering' in the NBA 2K27 graphics options, and I think I smell a rebrand of Nvidia's controversial graphics tech | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0173 Age Twisters is a simple yet charming spin on the co-op adventure that aims to feel like watching a Pixar movie | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0174 In a sea of failed live service games, I'm shocked to see someone trying to make a MOBA | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0175 'That criticism is justified': Gamescom apologizes for its callous response to developer hardware thefts | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0176 Silent Hill: Townfall is the most Scottish game I've ever played and the most effective horror game I've seen in ages: 'It made sense for us to dig deep into our upbringings, into our past, and try and build a place that felt believable' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0177 Great, now motherboard prices might be next to spike thanks to component costs increasing by up to 50% | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0180 千元档久坐刚需之选：傲风 C3Pro 电竞椅深度实测，读懂一把高性价比座椅的必要性 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0181 仅2999元，微星27英寸2K 320Hz 第四代面板QD-OLED显示器X32流光开售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0183 How Roblox Scaled Its Kafka Platform to Over 18 Trillion Messages a Day | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0184 IFM 发布 K2 Horizon 六款开源模型，覆盖 0.9B 到 375B-A23B 并开放完整训练生命周期 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0185 OpenAI 发布新模型 Astra，主打计算机与浏览器操作但因 opaque recurrence 引发争议 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0186 Artificial Analysis 评测 GPT-6 Astra：编码智能体追平 Fable 5 但价格涨至 2.5 倍 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0187 François Chollet 评 GPT-6 Astra 在 ARC-AGI-3 上的表现 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0188 ARC-AGI-3 发布仅半年即被 Astra 饱和，进展快于 François Chollet 预期一倍 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0189 Rohan Paul 解读 OpenAI GPT-6 Astra 117 页系统卡中的安全发现 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0190 Perplexity 宣布将接入 OpenAI GPT-6 Astra，称其在 WANDR 评测中居首 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0191 Greg Brockman 转发：GPT-6 Astra 在 ARC-AGI-3 达到 SOTA，基准趋于饱和 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0192 Gary Marcus 评 GPT-6 Astra：进步明显但鲁棒性与可监控性存疑 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0193 xAI 让 Grok Bot 承担采购工作，Haggle Bot 找出超 10 万美元直接节省 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0194 Tom Tunguz 分析 4 万亿美元 AI 数据中心债务浪潮 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0196 OpenAI GPT-6 Astra 在 ARC-AGI-3 上取得 SOTA 并超越人类动作效率基线 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0197 GPT-6 Astra 上线 Microsoft Foundry，早期客户已在 Azure 上使用 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0198 GPT-6 Astra 基准表现分歧，ARC-AGI-3 效率超人类令 Chollet 提前 AGI 预测 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0199 Reuters 报道 OpenAI 智能体逃出测试环境并劫持德国 wiki 交换规避限制的方法 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0200 英伟达两年从零建起近千亿美元股权投资组合 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0237 [厂商] [新瓜]尘白前发行制作人林增鸿中元节深夜现身直播间感谢玩家 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0238 [原神]武汉法院散兵进校园 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0239 [新瓜]CY版权炮赛马娘裸体mod，遭作者团队反击 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0240 [诡秘之主]一次又一次的宣传男人穿黑丝裙子跳舞 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0241 [疑似内容] '求瓜 '无限暖暖新玩法与《别拽了！烤串师傅》高度相似，制作组决定先社媒发声 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0242 [新瓜][瓜小味甜][世界计划国服]什么叫领奖励需要冒着被没收的风险在晚自习玩手机？ | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0243 [米哈游][厂商]汉丰二小遭遇网络诈骗，收款方疑似冒充米哈游 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0244 [白银之城]宣发使用“那咋了” | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0245 [新瓜] [补档]庄方宜动作被指责抄袭 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0246 [新瓜]鸣潮在日本，被评选为10大催泪游戏 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0247 [米哈游] [瓜小味甜]崩铁水温节奏后新视频对白似乎意有所指，且视频评论区被b站标记提示 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0248 [异环]异环B站官号的IP多次变更 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0249 [原神]武汉法院已多次美化散兵为受霸凌者向小学生宣传 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0250 [米哈游] 崩坏3，十周年庆实体奖励疑似被砍 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0251 [新瓜]王者荣耀毛茸茸企划被孙权玩家刷屏了 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0252 [厂商]由于《仙剑世界》亏损严重，其公司表示不会再做大体量、长期投入产品 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0253 [新瓜] 三国杀联动五年高考三年模拟 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0254 [联动]星铁与初音联动，发布新曲《唯有追赶风的方向》 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0255 [新瓜]赛尔号再曝设计事故，环源羁绊唐突削弱退养成 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0256 任天堂常规直面会及塞尔达40周年特别直面会将于下周举行 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0257 白宫推出五款像素游戏，宣传驱逐移民等特朗普政策 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0258 《地城拓荒》今日发售：据点建设与地城探险 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0259 音乐游戏《白金档案》将于9月10日正式上线1.0版本，两款新DLC同步登场 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0260 “魔岩三杰”之一、摇滚歌手何勇去世 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0261 500万根稻草，找1根针：《大海捞针模拟器》Steam商店页正式上线 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0262 末日度假村模拟游戏《罗马流沙 RE:Build》宣布9月17日全平台发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0263 《最终幻想VII 启示录》确定2027年4月8日发售，系列三部曲迎来完结 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0264 单人团本动作 RPG《Sil与消逝之境》现已推出试玩demo | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0265 节奏游戏《UTA MACROSS》复活企划启动！9月10日开启众筹项目 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0266 《零境·入侵》在State of Play发布最新预告片，同步开放测试版本 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0267 《最终幻想：共鸣》第一章抢先体验版在Steam推出 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0268 科乐美动作游戏《Rhapsody in Scarlet》公布Steam商城页 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0270 《Fate/EXTRA Record》公布新宣传片，2027年1月28日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0271 Epic喜加一：《Alone With You》免费领 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0272 Cygames 推出全新游戏品牌，首款游戏将于 11月5日发售 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0274 PAX Unplugged Houston to debut in June 2027: "It's a chance to bring PAX back to the PAX South fans that missed us" | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0275 Cloud gaming's broken promises, inside DoubleDown, and Pokémon's new movie ／ Week in Views | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0276 Podcast: GTA 6 boosts console sales… but will it last? | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0278 单人PvE高自由度、中世纪沙盒策略游戏设计分享（丹麦团队） | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0279 当 AI 成为玩法本身：三位制作人的实战手册 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0280 十万少年逐梦电竞赛场，「一加杯」 2026 全国电竞赛总决赛燃情收官 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0281 Before HBO’s The Last Of Us, An Entirely Different Adaptation Was Proposed | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0282 借鉴Steam爆款玩法做小游戏，新进畅销榜小游戏《俱乐大玩家》产品分析 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0283 背包玩法进入2.0？4人韩国团队，连出两个爆款、累计收入超6000万 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0284 D&D is getting a Netflix series about Strahd, involving the director of The Prisoner of Azkaban, and I honestly think this could work great | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0285 A popular streamer turned down a 6-figure deal to play Arc Raiders because 'the game frustrated me so much' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0286 I have filled GTA 5 with realistic Los Angeles snow | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0287 The Blood of Dawnwalker endings and how to get each one | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0288 Me: You can now run DLSS 5 on AMD GPUs. My RX 9070 XT: Please stop, it hurts us | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0289 The White House launches online 'arcade' with its own takes on Tetris and other popular games, and it's as rotten as you'd expect | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0290 After a massive 2021 office expansion, Bungie is now trying to sublease its 211,000 square foot headquarters | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0291 'Grand Theft Auto is a videogame franchise built around criminal activity': Miami-Dade County Sheriff comes out hard against a proposed GTA 6 collab with Rockstar | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0292 Celebrate Labor Day by playing Civilization 7 for free | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0294 September's schedule of new games, events, and updates refuses to let 2026 go down in history as a slow year for new releases | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0295 Left 4 Dead 2 writer says Valve intentionally 'leaked' its cinematic trailer to get around ESRB rules: 'I think we can't get trouble for that now' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0296 Grand Theft Auto 6's controversial refuelling action reportedly takes about 10 seconds to perform, which Rockstar's co-studio head says is 'pretty fast for a fill-up' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0297 Gaming monitors are one of the only good things about PC hardware right now, but one niche feature is underloved | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0298 This free lockpicking puzzler you can play in your browser is unexpectedly one of the most thrilling games I've encountered this year | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0299 Half of France's premier FPS sibling duo just put out the most exhilarating parkour game I've ever played, and it's only $8 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0300 Confession time: Alright, come clean—how tidy are your bags in your MMOs? | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0301 群星集结海岛逐浪，9月11日《PEL奇遇时光三亚篇》斗鱼直播重磅开启 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0302 GitHub 发布 Project HydraFusion 研究预览，用多模型运行时编排降低 Copilot 成本 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0303 GPT-6 Astra 幻觉更少但仍易受隐藏提示词注入攻击 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0304 OpenAI 训练中的智能体被发现通过公共 Wiki 互相通信 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0305 OpenAI 智能体被曝劫持德国网站用作共享公告板，研究者称其源自 reward-hacking | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0306 Claude 完成 Fermat 大定理的形式化证明，生成超 1300 万行 Lean 代码 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0307 OpenAI 发布 GPT-6 Astra，面向 Pro、Enterprise 和 Business Premium 用户开放 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0308 Claude 完成 Fermat 大定理的首个全机器校验形式化证明 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0309 GPT-6 Astra 开始向 Plus 和 Business 用户推出 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0310 Anthropic IPO 推迟至中期选举前，最早 10 月中旬启动路演，目标估值 2 万亿美元 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0311 Anthropic 宣布 Claude 用 11 天完成费马大定理首个端到端形式化证明 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0312 奥尔特曼致歉 GPT-6 Astra 发布混乱，现已面向所有 Plus / Pro 等用户推出 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0313 OpenAI 说明 wiki 事件并着手制定对齐事故披露框架 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0314 OpenAI 向 Pro、Enterprise 和 Business Premium 用户推出 GPT-6 Astra，消息额度约为 GPT-5.6 Sol 的一半 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0315 塔姆布勒岭校园枪击案受害者追加 30 起诉讼，OpenAI 面临诉讼超 50 起 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0316 费马大定理的 Lean 4 机器检查完整证明开源发布 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0317 OpenAI 承认德国 wiki 事件并承诺改革智能体错位事件报告机制 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0318 实测GPT-6 Astra：速度、前端与代码能力对比GPT-5.6 Sol的全面升级 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0319 OpenAI 回应智能体接管德语维基网站事件，称将改革 AI 误对齐事件披露机制 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0320 OpenAI 发布 GPT-6 Astra 提示词指南，含 slop 词屏蔽清单 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0327 [米哈游] 米哈游新作源初之结由于既视感过强，在外网引起热议 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0328 [新瓜]西山居新作运营官号承认尘白已死？ | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0329 [米哈游] 真珠实机演示，毛笔画出油画 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0330 [新瓜]鸣潮在日本，被评选为10大催泪游戏 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0331 俄罗斯发布手游市场行业报告，宣布俄罗斯是全世界不可忽视的市场 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0332 [原神]武汉法院已多次美化散兵为受霸凌者向小学生宣传 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0333 [米哈游] [瓜小味甜]崩铁水温节奏后新视频对白似乎意有所指，且视频评论区被b站标记提示 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0334 [米哈游] 崩坏3，十周年庆实体奖励疑似被砍 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0335 [厂商]由于《仙剑世界》亏损严重，其公司表示不会再做大体量、长期投入产品 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0336 [腾讯]受三角洲新赛季影响，请同学们错峰下载 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0340 多位家长被骗缴费648元充游戏；游戏平台歌曲侵权被罚款 ／ 一周说「法」 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0341 对话《大厂病》：面对制度铁笼与内卷，牛马怎么活得更像人？ | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0342 《文明VII》三大更新即将到来，真！未来可期！ | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0344 Gamescom 2026 insights and Sony Music's shock Puzzle & Dragons investment ／ Week in Mobile Games podcast | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0345 Project ZETA’s main aim is to take the ‘running away’ part out of Capture the Flag | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0346 2026年科隆游戏展：当中国游戏开始提供经验 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0347 《月光光心慌慌》21分钟实机演示 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0348 《异于天堂》执行总监横山昌义访谈视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0349 《NBA 2K27》DLSS 5画面对比 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0350 《怪物猎人 荒野：凌越》「大锤」武器介绍视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0351 《怪物猎人 荒野：凌越》「轻弩炮」武器介绍视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0352 《女神异闻录4 Revival》「巽完二」介绍视频 | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0353 itch 一周游戏汇：8月24日-8月30日（下） | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0354 Onimusha: Way of the Sword starts off slow, but stick with it: You'll be rewarded with some of the best action combat of the decade | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0355 Kingdom Come: Deliverance director says DLSS 5 does right by KCD 2, 'people are crazy' for thinking it's AI slop | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0356 Saber CCO Tim Willits blames layoffs on games industry overspecialization: 'Studios that have a couple hundred employees that work on one game are going to struggle' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0357 8-year Old School RuneScape saga comes to a close with former dev sentenced for stealing $400K in gold and items from players | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0358 Go grandmaster becomes first human to win series against advanced AI engine in 3-hour match | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0359 Dwarf Fortress co-creator Tarn Adams was amazed other devs had heard of his game the first time he went to a convention: 'I didn't know that anyone knew what we were doing' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0360 Saber CCO says the studio isn't changing up its comms strategy after recent controversies: 'There's always some dust up' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0361 Peak studio Aggro Crab is publishing a sick-looking platformer about a blue collar guy doing dirty work on an alien world | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0362 Ex-BioWare designer says doom and gloom about the next Mass Effect is overstated: 'I think that they can do it' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0363 Civilization 7 will finally enter the atomic age in 2027, via a free update Firaxis says will be 'even bigger in scope' than last year's Test of Time | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0364 Here's 10 more minutes of the most interesting game shown at this year's Opening Night Live | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0365 Blending Deus Ex with Escape from Butcher Bay, Deficit is one of the best-feeling indie immersive sims I've played—even if the stealth system needs serious work | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0366 I never thought a fishing sim could be this fun, but How to Fish proves me wrong with its ridiculous physics, killer spider crabs, and classic co-op chaos | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0367 Onimusha: Way of the Sword proves the parry formula is far from stale, you just need to get freaky with it | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0368 Persona 4 Revival Finds Its Kanji, And It Isn't Troy Baker Or Matt Mercer | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0369 51 Years Later, Sylvester Stallone's Gritty Action Sci-Fi Classic Is Officially Free on Streaming | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0370 Final Fantasy 7 Revelation Devs Say Ending Is Best 'Not Explained To You By Someone Else' | exclude | industry_news | 全量正文反扫：常规预告/更新/体验/回顾、纯榜单、旧事件、非游戏或证据不足；未形成达到7分且位于本窗口的独立事件。 |
| XS0371 OpenAI 承认 wiki 事件，称正在制定更透明的事故披露框架 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0372 OpenAI 承认 wiki 事件，称将建立智能体异常行为披露框架 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0373 OpenAI GPT-6 Astra 登顶 Code Arena WebDev 榜首，领先 Claude Fable 5.1 达 35 分 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0374 Fortune 报道 OpenAI 多次修改 GPT-6 Astra 基准测试数据，部分成绩大幅变化 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0375 OpenAI 发布内部研究加速报告：已达成自动化研究实习生目标，推进 2028 年 3 月自动化 AI 研究员 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0376 OpenAI 长文阐述对齐与监测困境，称 CoT 监控能力正在减弱 | exclude | ai_trends | 全量AI反扫：通用模型/融资/基准/安全事件未给出具体游戏迁移环节，或优先级低于三条直接游戏应用。 |
| XS0378 [厂商] [新瓜]尘白前发行制作人林增鸿中元节深夜现身直播间感谢玩家 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0379 [新瓜]黑暗王朝2.0？某浮力机认定碧蓝航线新皮肤“抄袭”她的“原创幽灵娘” | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0380 [新瓜] 粥预告pv中的武器设计疑似照搬ow | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0381 [新瓜]西山居新作运营官号承认尘白已死？ | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0382 [原神]原神外网遭遇版权打击，cv直播被中断，新版本音乐版权也不是自己 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0383 [新瓜]CY版权炮赛马娘裸体mod，遭作者团队反击 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0385 [米哈游][厂商]汉丰二小遭遇网络诈骗，收款方疑似冒充米哈游 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| XS0386 [藤子]王世杰员工迎来毕业季 | exclude | community_discourse | 社区全池补扫：重复帖、旧热度、单方推测或四要素不完整；优先级低于两条入选事件。 |
| release-candidate-001 2026-09-04 正式上线 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 2027-03-05 2027年3月5日发售定档 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-043 2026-09-17 9月17日三测定档 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 2026-09-04 正式上线 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-004 2026-09-03 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-006 2026-09-06 9月10日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-007 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-008 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-009 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 2026-09-04 抢先体验测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013 2026-09-02 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-014 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-019 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 2026-09-05 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 2026-09-05 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023 2026-09-05 抢先体验测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-024 2026-08-27 首测 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-025 2026-09-03 首测 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-026 2026-07-13 抢先体验测试 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-027 2026-09-06 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 2026-09-04 2027年春季上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 2026-09-04 2027年1月28日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-030 2026-09-04 11月19日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031 2026-09-04 2027年4月8日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 2026-09-04 2026年9月17日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033 2026-09-04 新品定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034 2026-09-04 2027年1月28日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035 2026-09-04 2027年4月8日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-036 2026-09-04 9月17日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037 2026-09-03 10月15日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038 2026-09-04 今年上半年上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-039 2026-09-04 9月上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-040 2026-09-05 9月17日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-041 2026-09-05 2027年4月8日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-042 2026-09-05 2027年1月28日上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-044 2026-09-06 2025年7月上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-045 2026-09-04 公测 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-046 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-047 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-048 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-049 2026-09-04 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-050 2026-09-06 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-051 2026-09-08 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-052 2026-10-23 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-053 2027-04-08 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-054 2026-09-04 10月上线定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-055 2026-09-05 新品首次曝光 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-056 2026-09-04 老品跨平台上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-057 2027-01-28 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-058 2027-02-04 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-059 2026-09-15 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-060 2027-01-15 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
