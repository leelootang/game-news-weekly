# 2026-10-27 选择决策

卡片曝光去重：双周100条与更早1025条均查。Steam个人日历历史第5/10、Top Lords同月SLG报告第5/10、9月发行商榜第3/10及周报第8/10均card_exposed=true，repeat_only排除；篮球少女历史第7/10、Xbox任命历史第2/10已曝光，但本次分别有实际开服与负责人离职的实质更新。card_carryover=0，无此前排名需补位。
行业时间口径：source_window_v1；当前报道自身published_at优先，缺失回退date；旧事件不是门禁。Roco既往展会亮相按历史语态入选，使命召唤里程碑按E1评分而非因事件早排除。
维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已由全量输入成卡；各维度（允许交叉）候选数：国内移动11、国产产品与人才6、市场数据9、并购投融资1、平台政策与能力7、档期变动7、资本组织8、海外重大13；具体ID见run_summary.json。并购投融资的唯一召回为教育应用融资误入标题，未进入正文。名单外R按影响力开放分层，不按未列名封顶。
产品日历漏挂反查：无行业↔日历互斥；165条行业与日历输入反扫。保留原抽取审计快照并修正未来发售、旧上线、背景公司误归属；单源、日期与跨期门禁分别执行。
深度交接：星期三日报，无周五selection消费。newsletter优先审查，Meta与小团队AI案例主题级合并一条。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I022 | include | industry_news | E3×R3+M1=10；米哈游直接归属的在研生活模拟产品付费测试，不以国产标签赋R。 |
| I030 | include | industry_news | E3×R3+M1=10；来源以灵犀简称直接归属产品，提供畅销榜第4及成熟数值卡牌研发经验，结合重点主体参照判断R3；不为校验补写正文未出现的公司全称或关联。 |
| I025 | include | industry_news | E3×R3+M0=9；开发商收回成熟头部二次元IP日本发行运营权，来源证明约8亿美元全球流水、日本七成以上贡献及长期本地发行生态，具同档行业影响力。 |
| I063 | include | industry_news | E3×R3+M0=9；微软全球游戏平台业务；首任COO统管端到端盈亏并直接向CEO汇报，核心管理层离职。 |
| I064 | include | industry_news | E3×R3+M0=9；Xbox全IP影视独家许可涉及七年及5亿美元提案，是平台级IP经营的重大商业谈判；保留据报道归因，未称合同成交。 |
| I027 | include | industry_news | E2×R3+M1=7；来源明确宝可梦公司与天美共同研发；同一产品10月27日宣布国内外停运安排，按公告事件合并，不把国服和国际服停服日混同。 |
| I050 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I027 |
| I080 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I027 |
| I010 | include | industry_news | E2×R3+M0=6；微软游戏第一方工作室与重点IP的出售协商期限调整，来源证明工作室217人及微软直接协商安排；不按泛微软业务赋分。 |
| I090 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I010 |
| I068 | include | industry_news | E2×R3+M0=6；来源直接确认Tencent-owned Morefun及其Arena Breakout: Infinite项目；是既有产品进入西方市场的发行规划，不将较早展会亮相伪装为昨日首曝。 |
| I033 | include | industry_news | E2×R3+M0=6；2026年9月中国手游出海完整收入、增长与下载榜的结构性变化；与10月12日单独SLG赛道报告不是同一发布事件，不拆成产品流水快讯。 |
| I207 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I033 |
| I206 | include | industry_news | E2×R3+M0=6；QuestMobile全景生态报告包含中国小程序手机游戏数量结构；只写分类数量比例，不改写成游戏用户或收入份额。 |
| I208 | include | industry_news | E2×R3+M0=6；本期来源发布字段在窗口内，7月统计期本身不是门禁；全量双周及更早归档未找到38家、23亿美元、42.6%的同一7月发行商数据事件，既往7月出海产品榜为另一事件。 |
| I209 | exclude | industry_news | 已曝光同一9月发行商榜，新增来源没有说明统计家数和占比的差异原因；不把口径冲突自动写成实质更新。 |
| I008 | exclude | industry_news | 7月6日已曝光个人日历及推荐入口；本期没有可核验的新状态，不能凭正式发布标题再次计入。 |
| I021 | exclude | industry_news | E3×R1+M1=4；新发行团队代理海外长线FPS，来源证明基础声量，但未支持其自身达到R2/R3；360投资企业背景不自动抬档。 |
| I023 | exclude | industry_news | E3×R1+M0=3；早期国产二次元代表产品核心主创离世，来源证明代表性但不足以确认头部或R2规模。 |
| I034 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I023 |
| I028 | exclude | industry_news | E1×R3+M1=4；老产品国服注册用户破亿为重大生命周期里程碑，E1不改成市场报告E2。 |
| I029 | exclude | industry_news | E1×R3+M0=3；来源为工程技术分享，有具体优化数据但不是新产品、资本或平台政策事件。 |
| I031 | exclude | industry_news | E2×R1+M1=3；同一9月产品表现已随SLG报告曝光，新稿补充数据和设计背景不证明业务新状态。 |
| I038 | exclude | industry_news | E3×R1+M0=3；来源证明前作与150万愿望单的独立团队代表性，尚不足头部或R2同档；慢速越野不自动算生活模拟。 |
| I039 | exclude | industry_news | E3×R1+M1=4；新品节玩家第一和60万Demo体现代表性，但本文未证明发行研发生态达到R2；不能凭国产升R。 |
| I043 | exclude | industry_news | E2×R1+M0=2；262万首曝PV支持一定声量；制作人只被证明曾任策划，不是前核心制作人/主策，不能按库洛直属或核心人才创业取R2/R3。 |
| I046 | exclude | industry_news | E1×R2+M0=2；具Warhammer 40,000: Boltgun 2等授权IP和51至200人团队的有影响力开发商；当前事实是纯裁员，E1。 |
| I048 | exclude | industry_news | E1×R3+M0=3；Xbox参与自愿离职计划，纯用工调整E1；六万人为微软合资格人数，不是Xbox裁员数。 |
| I086 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I048 |
| I098 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I048 |
| I118 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I048 |
| I049 | exclude | industry_news | E1×R3+M0=3；索尼第一方工作室及千万级前作、数百万级新作有头部产品影响力；纯裁员E1，不把成功发售作为新品事件加分。 |
| I065 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I049 |
| I078 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I049 |
| I138 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I049 |
| I051 | exclude | industry_news | E1×R2+M0=2；英国游戏行业协会有区域行业代表性，但这里只是税收改革呼吁，不是生效政策。 |
| I052 | exclude | industry_news | E2×R1+M0=2；PC市场整体报道按R1，不能因受访公司名单抬档。 |
| I053 | exclude | industry_news | E1×R2+M0=2；Kingdom Come系列及已公布中土RPG支持较强工作室影响力；本期为安全事故及调查，未证实项目取消、停运或重大资本状态。 |
| I134 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I053 |
| I058 | exclude | industry_news | 季度同比增长没有一致预期/指引异常或资本结构异常证据，且正文被Cloudflare阻断。 |
| I060 | exclude | industry_news | E1×R2+M0=2；非洲与中东区域支付发行能力支持R2，但仅有访谈摘要，无法核验完整业务转型细节。 |
| I062 | exclude | industry_news | E3×R1+M0=3；标题涉及5000万美元项目和手机适配，但实际正文仅设备参数摘要，未支持项目状态或主体影响力。 |
| I066 | exclude | industry_news | E1×R2+M0=2；来源证明专业复刻发行生态和Atari收购组合，较强垂直行业影响力；本期为管理观点而非新收购。 |
| I069 | exclude | industry_news | E2×R0+M0=0；正文仅支持教育应用Buddy.ai融资，标题的游戏融资比较缺少可用数据，不据标题替代事实。 |
| I079 | exclude | industry_news | E2×R1+M1=3；新品节有一定代表性，但没有影响力证据支持R2；延期E2，生活与社区建造命中M1。 |
| I129 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I079 |
| I081 | exclude | industry_news | E1×R3+M1=4；400亿美元系列收入是头部IP生命周期里程碑E1，不是市场结构数据E2；不改写成新作收入。 |
| I137 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I081 |
| I083 | exclude | industry_news | E1×R3+M0=3；知名大厂IP电影仍在开发的导演表态，不是新的立项或合作签订。 |
| I110 | merge | industry_news | 同主体、同公告日期、同一事件；合并至I083 |
| I093 | exclude | industry_news | 报道明确设备尚未确定推出、仅幕后传闻；未证明拟议独占协议已达成。 |
| I097 | exclude | industry_news | E1×R3+M0=3；同一裁员事件英文正文24人与该中文稿26人不一致，英文较完整源保留审计；纯裁员均不过线。 |
| I115 | exclude | industry_news | E0普通硬件驱动补丁；来源明确不保证终端正式获得支持，不是平台政策或新品跨平台事件。 |
| I116 | exclude | industry_news | E2×R1+M0=2；来源只证明第三方早期alpha兼容项目，不是索尼或Valve官方跨平台发行；尚不足R2。 |
| I119 | exclude | industry_news | E1×R1+M0=1；经典作品创作者回顾访谈，没有新项目立项或公司变更。 |
| I123 | exclude | industry_news | E3×R0+M1=1；本文提供产品设想，未证明研发发行主体及行业影响力。 |
| I125 | exclude | industry_news | E0：普通DLC内容与评测，不作为新品事件。 |
| I128 | exclude | industry_news | E3×R1+M0=3；代表作创作者推出微型恐怖作品，影响力不足R2。 |
| I131 | exclude | industry_news | E2×R1+M0=2；PC平台活动榜单结构变化R1；不把四款AI声明解读为全部玩家拒绝AI的因果证据。 |
| I135 | exclude | industry_news | E1×R3+M0=3；已有作品社区版内容升级与Steam页面进展，不是本期首次立项或实际新平台发售。 |
| I140 | exclude | industry_news | E1×R1+M0=1；外围硬件供应访谈，不是游戏主体业务变化。 |
| I144 | exclude | industry_news | E3×R1+M0=3；有已发布AR产品与显示技术，但本来源缺少游戏业务影响力证据支持R2。 |
| I147 | exclude | industry_news | E3×R1+M0=3；Seoul2033与FAKEBOOK代表作可核验，但未支持R2同档规模，不因新产品自动入选。 |
| I006 | exclude | industry_news | AI NPC试玩信息只有48字，落地细节不足 |
| I007 | exclude | industry_news | 与10月26日已写外包审核说明重复，无新增 |
| I011 | exclude | industry_news | 请愿及线下广告诉求写入社区 |
| I045 | exclude | industry_news | 请愿及线下广告诉求写入社区 |
| I047 | exclude | industry_news | 平台AI披露争论转AI候选 |
| I073 | exclude | industry_news | 游戏研发AI采用实证转AI候选 |
| I091 | exclude | industry_news | 同一Steam AI披露争论转AI候选 |
| I092 | exclude | industry_news | 主机漏洞AI发现实证转AI候选 |
| I122 | exclude | industry_news | 线下广告延续请愿写入社区 |
| I136 | exclude | industry_news | AI采用预测转AI候选 |
| I142 | exclude | industry_news | AI制作观点转AI候选 |
| I002 | exclude | industry_news | E2×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I004 | exclude | industry_news | E3×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I012 | exclude | industry_news | E2×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I014 | exclude | industry_news | E2×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I017 | exclude | industry_news | E3×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I084 | exclude | industry_news | E2×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I102 | exclude | industry_news | E3×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I103 | exclude | industry_news | E3×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I104 | exclude | industry_news | E2×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I106 | exclude | industry_news | E3×R0+M0=0；当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。 |
| I001 | exclude | industry_news | E0：《英雄联盟》传奇选手Cyanide去世，终年31岁；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I003 | exclude | industry_news | E0：16款作品两日狂欢！CRITICAL REFLEX核聚变2026北京站收官回顾；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I005 | exclude | industry_news | E0：均分88：《影之刃零》媒体评分汇总；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I009 | exclude | industry_news | E0：《欧洲卡车模拟2》“冰岛”DLC将于11月11日发售；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I013 | exclude | industry_news | E0：《守墓人2》上线首次折扣10%；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I015 | exclude | industry_news | E0：《湮灭之潮》亮相核聚变试玩会与「核电波」：格雯面部效果迎来优化，主创揭秘幕后设计巧思；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I016 | exclude | industry_news | E0：《红色沙漠：增强版》获2026金摇杆奖“终极年度游戏”提名；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I018 | exclude | industry_news | E0：【抽奖】《抵抗者》将参展CPOPwave：用游戏为载体，讲好中国故事；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I019 | exclude | industry_news | E0：卡普空公布最新财报数据，《识质存在》等新作表现亮眼；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I020 | exclude | industry_news | E0：《影之刃零》倒计时2天，系列人气角色虚空高清海报公布；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I024 | exclude | industry_news | E0：马化腾丁磊财富合计缩水1640亿，米哈游创始人涨超978亿；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I026 | exclude | industry_news | E0：三王同台，相约百年的王者才刚开始；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I032 | exclude | industry_news | E0：“1，懂你意思”，王者荣耀2026周年庆与亿万玩家共创新体验；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I035 | exclude | industry_news | E0：S16热搜刷屏，LPL品牌赞助商玩转“第二赛场”；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I036 | exclude | industry_news | E0：专访法国被抢游戏店主：我们打算联合起诉相关部门；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I037 | exclude | industry_news | E0：万圣新品！魔域口袋版全新外观介绍；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I040 | exclude | industry_news | E0："Brawl Stars" Global Tournament Makes Its Debut in China: A Six-Year Journey of Mutual Commitment；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I041 | exclude | industry_news | E0：Everyone says Hangzhou is a culinary wasteland, so where should gamers go to eat?；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I042 | exclude | industry_news | E0：Unity 荣获「2026 年度出海增长价值服务奖」，AI 技术赋能广告表现，助力游戏出海破局；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I044 | exclude | industry_news | E0：Paris Games Biz showcased a guarded optimism in the face of turmoil, both locally and in the industry at large / Opinion；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I054 | exclude | industry_news | E0：Save up to $187: PG Connects Jordan Mid Term ends this week；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I055 | exclude | industry_news | E0：Roblox’s Mohamed El Sheakh joins the speaker line-up for Pocket Gamer Connects Jordan；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I056 | exclude | industry_news | E0：Microsoft offers voluntary buyouts to 60,000 employees；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I057 | exclude | industry_news | E0：Auroch Digital cuts quarter of staff；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I059 | exclude | industry_news | E0：Pokémon Unite ending service on mobile and Switch in 2027；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I061 | exclude | industry_news | E0：Discover the Aurora Nordics 2026 honourees；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I067 | exclude | industry_news | E0：Tencent’s big-brand MOBA Pokémon Unite is closing in March 2027；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I070 | exclude | industry_news | E0：最会守塔的玩家，遇到了最懂他们的《王者荣耀》；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I071 | exclude | industry_news | E0：触乐怪话：在音乐中来一场时空漫游；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I072 | exclude | industry_news | E0：从《影之刃零》完整版中能看到的，是审美、技术与匠心；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I074 | exclude | industry_news | E0：20年国民游戏平台，怎么就让两代人坐上了一张牌桌？；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I075 | exclude | industry_news | E0：Diablo 4’s War Plans Are Getting A Huge Upgrade In Season 16；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I076 | exclude | industry_news | E0：WoW: Forever Just Got Another Major Racial Ability Shakeup Before Launch；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I077 | exclude | industry_news | E0：Here’s Another Mass Effect 5 Leak To Break Your Heart；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I082 | exclude | industry_news | E0：Star Trek Enters Magic: The Gathering’s Secret Lair Next Month, Here Are The Cards；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I085 | exclude | industry_news | E0：Nintendo Announces Indie World Showcase For October 28；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I087 | exclude | industry_news | E0：Steam Next Fest Was Flooded With Slop. These 50 Demos Cut Through The Noise；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I088 | exclude | industry_news | E0：Check Out 46 Seconds Of New Final Fantasy 7 Revelation Gameplay (And A Pink Chocobo)；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I089 | exclude | industry_news | E0：IGN《赛博朋克：边缘行者 2》剧评：9 分；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I094 | exclude | industry_news | E0：《深渊尽头》评测；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I095 | exclude | industry_news | E0：《埋谷季》制作人访谈；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I096 | exclude | industry_news | E0：《潜行者2》2.1更新「变异区观察站」预告；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I099 | exclude | industry_news | E0：《漫威宇宙入侵》「杜姆城围城战」DLC游戏模式预告；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I100 | exclude | industry_news | E0：《时间旅者：重生曙光》拍照模式更新宣传视频；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I101 | exclude | industry_news | E0：《刺客信条：黑旗 记忆重置》最终大型内容更新预告；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I105 | exclude | industry_news | E0：《HumanitZ》1.1版本更新宣传视频；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I107 | exclude | industry_news | E0：Java版《我的世界》「RTX Remix」宣传视频；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I108 | exclude | industry_news | E0：据报《GTA6》发售日请假量增17%；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I109 | exclude | industry_news | E0：罗伯特·帕丁森赞索德伯格的出手协助「完全无私」；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I111 | exclude | industry_news | E0：《饥饿游戏》导演希望玩家兼顾《GTA6》与新片；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I112 | exclude | industry_news | E0：苹果承认iPhone Duo屏幕存在问题；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I113 | exclude | industry_news | E0：诺娃独立游戏通讯 2026-#43；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I114 | exclude | industry_news | E0：本周 Steam 值得关注的游戏 10.26 - 11.01（二）；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I117 | exclude | industry_news | E0：New Windows 11 Insider Experimental build adds the ability to check your internet speed without a browser；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I120 | exclude | industry_news | E0：What to play this Halloween, plus last-minute costume ideas and spooky movie recommendations；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I121 | exclude | industry_news | E0：CD Projekt marks the 19th anniversary of its first Witcher RPG with a tribute to BioWare: 'Their support helped turn our vision into Geralt’s first interactive adventure'；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I124 | exclude | industry_news | E0：Walter Koenig, Star Trek's Pavel Chekhov, has died；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I126 | exclude | industry_news | E0：Veteran game composer in talks to score Mass Effect 5 shares 20 minutes of music he wrote for the project: 'To even dream in your sandbox was a privilege'；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I127 | exclude | industry_news | E0：The developer of one of my favorite 2020s RPGs does it because of BioWare: 'Baldur's Gate 1 is the first game I truly loved'；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I130 | exclude | industry_news | E0：World of Warcraft: Forever's last-minute patch transforms its bovines into racecars capable of zooming 60% faster than everyone else；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I132 | exclude | industry_news | E0：Half-Life: Alyx patch adds foveated rendering support a mere 6 years after the game's release；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I133 | exclude | industry_news | E0：Bassist plays Halloween gig wearing a Steam Frame: 'Interestingly, only one guy asked me about the Frame'；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I139 | exclude | industry_news | E0：Deadline: Afterlife Processing lets you take morality into your own hands and judge who deserves eternal salvation or damnation；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I141 | exclude | industry_news | E0：Edge magazine went to Rockstar to see GTA 6, and will tell you all about it in lavish detail this Thursday, October 29；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I143 | exclude | industry_news | E0：四年无冠之后，LOL还能重新燃起来吗？；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I145 | exclude | industry_news | E0：LG显示器超级玩家嘉年华落地京东MALL，双十一“真电竞”显示器粉丝福利同步开启；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| I146 | exclude | industry_news | E0：落幕不散场！八位堂核聚变2026北京站活动圆满结束；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。 |
| J114-01 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-02 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-03 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-04 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-05 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-06 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-07 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-08 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-09 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-10 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-11 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-12 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-13 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-14 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-15 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-16 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-17 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-18 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-19 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-20 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-21 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-22 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-23 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-24 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-25 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-26 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-27 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-28 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-29 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-30 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-31 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-32 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-33 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-34 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-35 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-36 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-37 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J114-38 | exclude | industry_news | E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。 |
| J113-01 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-02 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-03 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-04 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-05 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-06 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-07 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-08 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-09 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-10 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-11 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-12 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-13 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-14 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-15 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| J113-16 | exclude | industry_news | E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。 |
| A148 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A149 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A150 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A151 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A152 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A153 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A154 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A155 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A156 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A157 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A158 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A159 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A160 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A161 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A162 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A163 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A164 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A165 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A166 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A167 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A168 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A169 | exclude | ai_trends | 优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。 |
| A170 | exclude | ai_trends | Mutable是运行时角色定制工具，本文222字未证明AI机制；不能凭原始AI分类入选。 |
| A006 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A007 | exclude | ai_trends | 与10月26日已写Creative Assembly外包审核说明同一内容，本期短摘无新增。 |
| A042 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A044 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A047 | exclude | ai_trends | Sweeney对既有披露政策继续表态，没有新政策或实证采用结果；低于本期实证案例优先级。 |
| A073 | include | ai_trends | 研发全流程采用与项目结果已有可核验自述 |
| A087 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A091 | exclude | ai_trends | Sweeney对既有披露政策继续表态，没有新政策或实证采用结果；低于本期实证案例优先级。 |
| A092 | include | ai_trends | AI已用于PS5漏洞发现并获得赏金，有采访证据 |
| A113 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A114 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A131 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A136 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A142 | exclude | ai_trends | 来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。 |
| A205 | include | ai_trends | Meta提示词制作及社交流分发已有具体工具与负责人访谈 |
| C189 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C190 | exclude | community_discourse | 同事件已在行业新闻处理，不重复入选社区。 |
| C191 | exclude | community_discourse | 当日讨论存在，但只有剪辑转述及宏观AI立场，缺少游戏层面具体采用；优先完整可归因事件。 |
| C192 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C193 | exclude | community_discourse | 同事件已在行业新闻处理，不重复入选社区。 |
| C194 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C195 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C196 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C197 | exclude | community_discourse | 同事件已在行业新闻处理，不重复入选社区。 |
| C198 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C199 | exclude | community_discourse | 同事件已在行业新闻处理，不重复入选社区。 |
| C200 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C201 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C202 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C203 | exclude | community_discourse | 旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。 |
| C204 | include | community_discourse | 本期新触发，有明确宣传内容与角色专属感的冲突机制；仅用玩家归因，不写未证实海外趋势或卡车行动为事实。 |
| C045 | include | community_discourse | 旧关闭事件在本期出现可核验的请愿及线下传播升级；与行业栏目不重复。 |
| D205 | include | deep_analysis | 本期newsletter优先；平台负责人访谈与实际小团队结果共同解释效率、获客、商业化之间的断点；与上期长青MMO服务器减负主题不同。 |
| D206 | exclude | deep_analysis | 数据事实可为新闻，独立深度缺少超过入选AI主题的完整机制链；206仅摘要，208为7月数据，209还与既往9月发行商口径有差异。 |
| D207 | exclude | deep_analysis | 数据事实可为新闻，独立深度缺少超过入选AI主题的完整机制链；206仅摘要，208为7月数据，209还与既往9月发行商口径有差异。 |
| D208 | exclude | deep_analysis | 数据事实可为新闻，独立深度缺少超过入选AI主题的完整机制链；206仅摘要，208为7月数据，209还与既往9月发行商口径有差异。 |
| D209 | exclude | deep_analysis | 数据事实可为新闻，独立深度缺少超过入选AI主题的完整机制链；206仅摘要，208为7月数据，209还与既往9月发行商口径有差异。 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | exclude | release_calendar | 周知未来发售日及请假调查，不是本期首次定档/上线；抽取将未来事件错绑当日。；超过本报告产品日历条数上限 |
| release-candidate-003 | exclude | release_calendar | 两源确认正式版，但正文未写绝对日期；当前校验要求绝对日期证据，保持审计不发布。；超过本报告产品日历条数上限 |
| release-candidate-004 | exclude | release_calendar | 11月6日是新棋手上线，不是新品定档。；单源不具备正文资格 |
| release-candidate-005 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-006 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-007 | exclude | release_calendar | 2025年10月历史上线，且米哈游只是对比对象，撤销错误公司加分。；单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | 国服上线三周年与注册用户里程碑，不是新品上线。；单源不具备正文资格 |
| release-candidate-009 | exclude | release_calendar | 今年7月上线为历史背景，不是本期新品。；单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 正文为现已登陆，没有抢先体验依据；仅单源。；单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-023 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-041 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-043 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-046 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-047 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-048 | exclude | release_calendar | 仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。；单源不具备正文资格 |
| release-candidate-049 | exclude | release_calendar | 旧试玩时间，单源；事件日期不在报告窗口 |
| release-candidate-050 | exclude | release_calendar | 仅单源招募；事件日期不在报告窗口 |
| release-candidate-051 | exclude | release_calendar | 单源，日期不够明确；单源不具备正文资格 |
| release-candidate-052 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-053 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-054 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-055 | exclude | release_calendar | 本期是停研报道，2024年首曝是背景；研发主体不是库洛。；单源不具备正文资格 |
| release-candidate-056 | exclude | release_calendar | 正文未来11月10日发售，修正当日已上线误判。；单源不具备正文资格 |
| release-candidate-057 | exclude | release_calendar | 单源；单源不具备正文资格 |
| release-candidate-058 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-059 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-060 | exclude | release_calendar | 单张五星思念的普通运营更新，不是新品上线。；单源不具备正文资格 |
| release-candidate-061 | exclude | release_calendar | 老产品地图更新，不是新品上线。；单源不具备正文资格 |
| release-candidate-062 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-063 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-064 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-065 | exclude | release_calendar | 单源标题摘要；单源不具备正文资格 |
| release-candidate-066 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-067 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-068 | exclude | release_calendar | 同产品同日预下载合并至规范产品名节点；不是另一次定档。；单源不具备正文资格 |
| release-candidate-069 | exclude | release_calendar | 仅单一来源；单源不具备正文资格 |
| release-candidate-070 | exclude | release_calendar | 只有Google News标题摘要；单源不具备正文资格 |
| release-candidate-071 | exclude | release_calendar | 只有Google News标题摘要；单源不具备正文资格 |
| release-candidate-072 | exclude | release_calendar | 裁员报道提到此前完全版与老发售，不是本期跨平台上线。；单源不具备正文资格 |
| release-candidate-073 | exclude | release_calendar | 周知未来发售日及请假调查，不是本期首次定档/上线；抽取将未来事件错绑当日。；事件日期不在报告窗口 |
| release-candidate-074 | exclude | release_calendar | 只有Google News标题摘要；单源不具备正文资格 |
| release-candidate-075 | exclude | release_calendar | 只有Google News标题摘要；单源不具备正文资格 |

采集覆盖警告：4个采集器失败、PocketGamer 9条受阻摘要、Sensor Tower清单4/正文3差异均已记录collection_coverage.md/json；缺少8月出海报告，未补造。
