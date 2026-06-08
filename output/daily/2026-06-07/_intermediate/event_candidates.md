# Event Candidates

## C001 - Steam 全球热销榜实时补充
- section: pc_rankings
- status: candidate
- source_ids: S0001
- entities: Steam / Counter-Strike 2 / Wuthering Waves / Forza Horizon 6 / 007 First Light / Path of Exile 2 / Halo: Campaign Evolved / Paralives / Subnautica 2 / Apex Legends / Gamble With Your Friends
- facts:
  - 2026-06-07 日报窗口内存在 `steamdb_rankings` 记录；采集说明写明这是 2026-06-08 的实时热销榜，用于补充 2026-06-07 日报。
  - TOP10 中被标记为近期新品的有 Forza Horizon 6、007 First Light、Paralives、Subnautica 2、Gamble With Your Friends。
  - 记录提供价格、好评率、上线日期、销量与营收估算；结构化 `extra.rows` 还包含峰值玩家字段。
- notes: 最新 skill 要求存在 pc_rankings 时在最终日报最前添加 `steam当日榜单`。

## C002 - 《归唐》19分钟实机演示与单机定位
- section: industry_news / release_calendar / community_discourse
- status: candidate
- source_ids: S0002, S0004, S0039, S0092
- entities: 归唐 / 网易雷火 / 24工作室
- facts:
  - S0002 写明《归唐》释出 19 分钟实机演示，内容涵盖剧情表演、潜行暗杀、正面战斗、追逐战；视频发布不到 2 小时，B 站播放破 100 万，同时在看人数超过 1 万。
  - S0002 记录视频简介称这是网易雷火旗下 24 工作室出品的叙事型单机动作冒险游戏，开发团队操作录制，仍在开发中。
  - S0039 的产品日历记录同日事件为《归唐 PC/主机》发布最新实机演示，标签为动作、冒险、剧情。
  - S0092 记录社区早前围绕“删去要做单机的动态表述、疑似转型手游”争论，6月7日仍有回复。
- notes: 行业新闻写产品事实与展示规格；社区动态写信任修复与玩家质疑，不重复正文角度。

## C003 - 《伊莫》亮相 Future Game Show 并开启三测招募
- section: industry_news / release_calendar
- status: candidate
- source_ids: S0006, S0037, S0083
- entities: 伊莫 / 爪印工作室 / Future Game Show
- facts:
  - S0006 写明 6月7日，爪印工作室研发的多人在线大世界捉宠 RPG《伊莫》亮相 2026 Future Game Show，公布最新官方 PV，并开启三测“握爪测试”招募。
  - S0006 写明测试支持移动端、PC端，全球测试招募同步开启；官方同步启动创作者征集招募计划。
  - S0037 记录《伊莫-开放世界抓宠》在 6月7日处于招募中，标签为高自由度、开放世界、抓宠。
  - S0083 的 TapTap 记录同日 10:00 开始“伊莫 - 测试招募”。
- notes: release_calendar 可用 industry_news 回填研发方和品类信息。

## C004 - 《007 First Light》官方销量达270万套
- section: industry_news / pc_rankings
- status: candidate
- source_ids: S0007, S0001
- entities: 007 First Light / IO Interactive / Amazon
- facts:
  - S0007 写明 IO Interactive CEO Hakan Abrak 称《007 First Light》正式宣布销量 270 万套，并“probably”已经超过 300 万套。
  - S0007 写明游戏尚未完全回本，但成本低于此前报道的 2 亿美元口径；首年大部分内容将免费更新，团队正与 Amazon 讨论后续合作。
  - S0001 中《007 First Light》位列 Steam 全球热销榜 TOP5，标记为近期新品，上线日期 2026-05-27，好评率 92%。
- notes: 行业新闻采用官方全口径销量；Steam 榜单保留榜单估算口径。

## C005 - 阅文收购艺画开天剩余腾讯持股
- section: industry_news
- status: candidate
- source_ids: S0009, S0022
- entities: 阅文集团 / 腾讯 / 艺画开天 / Bilibili / 凡应 / 灵笼
- facts:
  - S0009 写明阅文集团以 400.78 百万元从腾讯收购艺画开天 28.22% 股权，交易后持股从 31.48% 增至 59.70%，腾讯完全退出股东名单。
  - S0009 写明艺画开天继续独立运营，不并入阅文财务报表；Bilibili 仍持有约 14.02%。
  - S0022 将该交易概括为阅文斥资约 4.0078 亿元取得艺画开天控股权，并指出交易涉及《灵笼》《凡应》等 IP 资产。
- notes: 属于并购 / 资产处置维度，应成卡。

## C006 - 夏日游戏节中日韩项目与西方大厂声量变化
- section: industry_news / deep_observation
- status: candidate
- source_ids: S0010, S0021
- entities: Summer Game Fest / 腾讯 / 网易 / 库洛 / 烛龙 / Capcom / Square Enix
- facts:
  - S0010 认为 Summer Game Fest 2026 中日本头部厂商表现突出，中国、韩国工作室同样显眼，而大型西方工作室存在感较弱。
  - S0021 写明今年夏日游戏节中腾讯、网易、库洛、烛龙都有项目亮相；文章同时记录 Geoff Keighley 开场展示 Steam 新游数量与百万销量潜力新游数据。
  - S0021 将腾讯《穿越火线：潜伏》、网易《归唐》、库洛《鸣潮》联动、烛龙《古剑》实机展示作为中国厂商高规格展示案例。
- notes: 适合做行业精选 / 深度观察，不单列为行业新闻以避免与 C002/C003 重复。

## C007 - 腾讯、网易、快手暑期档产品集中竞争
- section: industry_news
- status: candidate
- source_ids: S0022
- entities: 腾讯 / 网易 / 快手 / 失控进化 / 遗忘之海 / 诡秘之主
- facts:
  - S0022 写明腾讯《失控进化》定档 7月9日全平台上线，网易《遗忘之海》7月公测，快手《诡秘之主》6月26日首测。
  - S0022 写明《失控进化》官网预约已达 3200 万人，主打 Rust 正版玩法授权、生存对抗、建造攻防和多端互通。
- notes: 作为暑期档竞争卡保留，但最终正文空间让位给 C005 与 C006。

## C008 - NVIDIA RTX Spark 与游戏厂商适配
- section: ai_trends
- status: candidate
- source_ids: S0031
- entities: NVIDIA / KRAFTON / NC / Riot Games / T1 / RTX Spark
- facts:
  - S0031 写明 NVIDIA CEO Jensen Huang 在韩国向当地游戏社区介绍 RTX Spark 超芯片。
  - S0031 写明 KRAFTON、NC 与 Riot Games 正合作将旗下游戏适配 RTX Spark；Huang 与 Faker 在 T1 电竞场馆亮相，并在江南区网吧演示《PUBG: BATTLEGROUNDS》及基于 NVIDIA ACE 的 “PUBG Ally” AI 队友。
  - S0031 写明已有超过 100 家 Windows 软件与游戏开发商采纳 RTX Spark。
- notes: 游戏相关 AI / 硬件生态事件，适合入选 AI 新闻。

## C009 - Harness-1 强化学习检索子智能体
- section: ai_trends
- status: candidate
- source_ids: S0030
- entities: Harness-1 / UIUC / Chroma
- facts:
  - S0030 写明 UIUC 与 Chroma 联合推出 Harness-1，一个 20B 参数检索子智能体。
  - S0030 写明模型通过强化学习在有状态搜索框架中训练，维护候选池、重要性标注集、证据图和验证记录。
  - S0030 写明 Harness-1 在 8 个基准测试上达到 0.730 平均 curated recall，比下一个最佳开源子智能体高 11.4 个百分点。
- notes: 适合入选 AI 新闻，偏工具链与检索能力。

## C010 - 美国 AI 联邦监管草案
- section: ai_trends
- status: candidate
- source_ids: S0025
- entities: 美国众议院 / AI 监管
- facts:
  - S0025 写明美国众议院议员发布法案草案，旨在禁止各州自行制定人工智能相关法规，将 AI 监管权力集中到联邦层面。
- notes: 重要但与游戏行业直接关联弱，最终 exclude。

## C011 - 《洛克王国》手游座谈会招募性别限制争议
- section: community_discourse
- status: candidate
- source_ids: S0088
- entities: 洛克王国手游 / 时光研游
- facts:
  - trigger: S0088 记录“时光研游”发布洛克王国手游座谈会招募，5月30日公告标注仅限女性，6月1日重新订正。
  - complaint_logic: 玩家争议集中在“仅限女性”和后续改写之间的口径差异，也有玩家质疑承办方与官方关系、调研需求由谁提出。
  - timeline: 发帖 2026-06-03，最新回复 2026-06-07 02:34，窗口内仍活跃。
  - follow_up_scan: 同窗口 community_discourse 未发现更明确官方回应；S0088 内部末页讨论仍围绕承办方身份和招募口径。
- notes: 独立舆情事件，适合入选社区动态。

## C012 - 《燕云十六声》NPC和文案改回最初版本争议
- section: community_discourse
- status: candidate
- source_ids: S0087
- entities: 燕云十六声
- facts:
  - trigger: S0087 标题和正文称《燕云十六声》又把 NPC 和文案改回最初版本，玩家称“版本回滚”。
  - complaint_logic: 玩家不满集中在文案与 NPC 调整反复，认为运营在玩家反馈和既有设计之间摇摆。
  - timeline: 发帖 2026-06-02，最新回复 2026-06-07 02:24，窗口内仍有追加回复。
  - follow_up_scan: 同窗口 community_discourse 发现 S0091 也讨论网易产品中的相关文案表达，但不是同一游戏事件；不并入正文。
- notes: 独立舆情事件，避免复述原帖攻击性措辞。

## C013 - 《归唐》单机表述删除引发玩家质疑
- section: community_discourse
- status: candidate
- source_ids: S0092, S0002, S0039
- entities: 归唐 / 网易雷火 / 24工作室
- facts:
  - trigger: S0092 记录玩家围绕《归唐》删去“要做单机”的动态表述展开争论，并猜测是否转型手游。
  - complaint_logic: 玩家不满的核心在于国内网游厂商做大型单机的信任基础薄弱，担心项目商业模式和平台方向变化。
  - timeline: S0092 发帖 2026-06-02，最新回复 2026-06-07 04:49；S0002 同窗口补充 6月7日 19 分钟演示与视频简介“叙事型单机动作冒险游戏”。
  - follow_up_scan: 同窗口 industry_news 与 release_calendar 均出现《归唐》实机演示，作为同一事件后续补充。
- notes: 社区正文应写信任修复，不重复行业新闻里的实机质量描述。

## C014 - 《绝区零》“太太杯”同人活动争议
- section: community_discourse
- status: candidate
- source_ids: S0090
- entities: 绝区零 / 小红书 / 同人活动
- facts:
  - S0090 记录玩家围绕《绝区零》官方小红书“太太杯”同人活动争论，争议集中在渠道活动和目标创作者群体。
  - 最新回复延续到 2026-06-07 19:13。
- notes: 可作为社区候选，但热度和业务相关性低于 C011/C012/C013，最终 exclude。

## C015 - 《终末地》官方漫画角色互动争议
- section: community_discourse
- status: candidate
- source_ids: S0089
- entities: 终末地
- facts:
  - S0089 记录玩家围绕官方漫画中的角色互动讨论，最新回复到 2026-06-07 22:35。
- notes: 事件触发点不够清晰，难以在不脑补的情况下写成完整公共舆情事件，最终 exclude。

## C016 - 《Gears of War: E-Day》PS5 版本传闻变化
- section: industry_news / release_calendar
- status: candidate
- source_ids: S0018, S0060
- entities: Gears of War: E-Day / Xbox / PS5
- facts:
  - S0018 写明 Jeff Grubb 称《Gears of War: E-Day》原本计划登陆 PS5，但相关决定刚刚改变；平台尚未正式公布。
  - S0060 记录同日 Gematsu 侧的发售日信息：Gears of War: E-Day launches October 6。
- notes: 重大产品档期 / 平台变化候选，但以海外主机生态为主且传闻口径强，最终 exclude。

## C017 - Bloober Team 开发 Star Trek 心理惊悚游戏
- section: industry_news
- status: candidate
- source_ids: S0019
- entities: Bloober Team / Paramount Games Studio / Star Trek: Shadow Frontier
- facts:
  - S0019 写明 Bloober Team 与 Paramount Games Studio 合作开发 Star Trek: Shadow Frontier，计划 2027 年登陆 PS5、Xbox Series X/S、PC。
- notes: 海外 IP 项目，信息完整但与日报优先级相比偏弱，最终 exclude。

## C018 - Wholesome Direct / Story Rich Showcase 等展示汇总
- section: industry_news
- status: candidate
- source_ids: S0011, S0013
- entities: Wholesome Direct / Story Rich Showcase
- facts:
  - S0011 记录 Wholesome Direct 展示 53 款 cozy game。
  - S0013 记录 Story Rich Showcase 首秀展示 26 款游戏。
- notes: 展示汇总类，缺少强单日商业钩子，最终 exclude。
