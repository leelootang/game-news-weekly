# 选择决策｜2026-10-23_to_2026-10-29

卡片曝光去重：先查2026-10-09至2026-10-22共110条，再查更早1011条，补查本周32条日报/周末报的实际广播。王者荣耀世界已在28日报曝光（第4/10）且5月周报收录，本期repeat_only；微信小游戏6分/R3保留唯一card_carryover，Atari6分/R2排序靠后。微信相关旧报告均未曝光，card_rank=null，card_limit=null或10，来源not_broadcast或publish_log_manifest。

行业时间口径：source_window_v1；所有非E0候选使用build_time_check核对published_at，缺失回退date；历史事件时间不作门槛。已纠正旧日报按事件时间和封闭名单产生的排除，不把旧理由直接带入本期。

维度覆盖自检：国内移动57张候选审计卡 / 国产产品与人才139张候选审计卡 / 市场数据127张候选审计卡 / 并购40张候选审计卡 / 平台政策73张候选审计卡 / 档期变动54张候选审计卡 / 资本组织122张候选审计卡 / 海外重大357张候选审计卡；交叉计数，逐卡列表见candidate_dimension_coverage.json。

产品日历漏挂反查：保留自动召回原始审计；反扫完整industry_news与release_calendar，按规范产品+日期重新聚类，纠正背景公司归属、普通运营和发售前宣传误判；每个原始信号均映射至节点或显式exclude，由sync_release_decisions.py --max-items 7确定排序前缀。

深度交接：2ff02addfe2f47d1a6c9789c6adb38c8；正文C001、C022；唯一主卡C001；无融合参考。

| candidate | decision | target_section | E/R/M或其他评分 | reason |
| --- | --- | --- | --- | --- |
| W20261023_20261025_I039 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 吉比特业绩说明会披露代号M98已正式立项并确定制作人；单独产品立项E3，常规财报不作为入选依据。 |
| W20261023_20261025_I529 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 天美王者IP三产品同时包揽iOS免费榜前三，属于同IP产品矩阵结构变化E2，MOBA产品M1；不把常规周年活动抬E。 |
| W20261023_20261025_I528 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 米哈游投资的奥秘游戏首曝潜梦者；投资关系R2而非R3，多人合作搜躲撤不等于竞技。 |
| W20261026_I138 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 雷霆游戏投资上海火因山风并持股约30%；实际新闻主体为名单内投资方游戏业务，E3R3M0=9。 |
| W20261027_I022 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E3×R3+M1=10；米哈游直接归属的在研生活模拟产品付费测试，不以国产标签赋R。 |
| W20261027_I030 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E3×R3+M1=10；来源以灵犀简称直接归属产品，提供畅销榜第4及成熟数值卡牌研发经验，结合重点主体参照判断R3；不为校验补写正文未出现的公司全称或关联。 |
| W20261027_I025 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E3×R3+M0=9；开发商收回成熟头部二次元IP日本发行运营权，来源证明约8亿美元全球流水、日本七成以上贡献及长期本地发行生态，具同档行业影响力。 |
| W20261027_I063 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E3×R3+M0=9；微软全球游戏平台业务；首任COO统管端到端盈亏并直接向CEO汇报，核心管理层离职。 |
| W20261027_I064 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E3×R3+M0=9；Xbox全IP影视独家许可涉及七年及5亿美元提案，是平台级IP经营的重大商业谈判；保留据报道归因，未称合同成交。 |
| W20261027_I027 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2×R3+M1=7；来源明确宝可梦公司与天美共同研发；同一产品10月27日宣布国内外停运安排，按公告事件合并，不把国服和国际服停服日混同。 |
| W20261027_I010 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2×R3+M0=6；微软游戏第一方工作室与重点IP的出售协商期限调整，来源证明工作室217人及微软直接协商安排；不按泛微软业务赋分。 |
| W20261027_I068 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2×R3+M0=6；来源直接确认Tencent-owned Morefun及其Arena Breakout: Infinite项目；是既有产品进入西方市场的发行规划，不将较早展会亮相伪装为昨日首曝。 |
| W20261027_I033 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2×R3+M0=6；2026年9月中国手游出海完整收入、增长与下载榜的结构性变化；与10月12日单独SLG赛道报告不是同一发布事件，不拆成产品流水快讯。 |
| W20261027_I206 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2×R3+M0=6；QuestMobile全景生态报告包含中国小程序手机游戏数量结构；只写分类数量比例，不改写成游戏用户或收入份额。 |
| W20261027_I208 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2×R3+M0=6；本期来源发布字段在窗口内，7月统计期本身不是门禁；全量双周及更早归档未找到38家、23亿美元、42.6%的同一7月发行商数据事件，既往7月出海产品榜为另一事件。 |
| W20261028_I160 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 核心制作人转岗为组织变化E3；来源明确腾讯天美与腾讯魔方，主体R3；公司人事不借MOBA背景加M。 |
| W20261028_I239 | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 统辖Magic、D&D、Duel Masters及数字游戏的头部IP与发行主体，任命为E3，影响力可比头部主体取R3；AI仅背景不加M。 |
| W20261028_I206 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 科乐美既有重制项目的新目标档期报道，E2R3M0=6；爆料仍保留归因，未当作官方定档。 |
| W20261028_I130 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 4月移动版公测事实已在2026-05-28_to_2026-06-04周报记载，并在本周10月28日日报通过card_carryover正式曝光（第4/10）；已非未曝光事件，且曾进入已发布周报，本期无实质更新，repeat_only。 |
| W20261028_I059 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 1, 'total': 7} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 来源显示前作iOS累计收入超4亿元，新作半月iOS下载360万、收入逾1300万元，构成细分市场较强发行与研运影响力R2；新品上线E3；明确PvP竞技M1，不借背景点点互动取R3。 |
| W20261028_I241 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 游戏工作室论坛和wiki迁入Discord造成知识封闭，来源直接说明其游戏社区基础设施作用；平台级公开内容可发现性规则E2，头部社区分发平台R3。 |
| W20261028_I346_IOS | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 头部全球游戏的移动平台准入裁定E2R3；本期newsletter明确记录澳洲法院要求重新上架。较早全球iOS回归报道仍明确澳洲不可用，本期为可核验地区状态变化。 |
| W20261028_I244 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 Project Titan取消为E2，暴雪R3，6分；本期来源回顾既有项目取消，完整文本可核验，未检索到历史同事件，不因取消发生较早而降低E或排除。 |
| W20261028_I231 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2产品经营数据，来源直接归属莉莉丝R3；随机奖励/塔防/营地经营不足证明本事件数值卡牌RPG或竞技，M0。相对9月28日四个月4560万美元，当前双平台9500万美元、下载1800万为有口径说明的新数据，不以媒体数量作更新。 |
| W20261028_I030 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 围绕小游戏平台开放、发行与支付进行正式战略合作E3；来源载明500万年活平台与过往100亿流水生态实战，具区域分发能力取R2；不凭蚂蚁背景自动当阿里R3。 |
| W20261028_I164 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 游戏行业奖项与专业组织的委员会核心负责人任命E3；跨工作室与行业委员会的组织影响力R2，不借其曾任Microsoft/Sony职位抬R3。 |
| W20261028_I251 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 DRM-free商店与独立发行商正式联合发行E3；全球PC店面、营销与跨平台发行能力构成R2，名单外不封顶R1。 |
| W20261028_I157 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 前作销量超过百万、历史AVG细分市场影响力支持R2；新品正式发售E3，首日约4万销量回本有制作者自述；不因清明历史日期降分，不把文化争议当官方事实。 |
| W20261028_I145 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 实际新闻主体包含发行商Playstack，来源证明其发行TGA最佳独立游戏及首次中国团队合作，国际独立发行能力R2；新品发售E3，非单纯榜位；肉鸽推币不自动命中竞技/数值卡牌。 |
| W20261028_I229_BRUTAL | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 推出开放游戏开发基础设施为战略动作E3；DayZ资深开发者创立、已有商业产品并获边缘世界引擎迁移采用，实际研发影响力R2。 |
| W20261028_I211 | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 非例行财报：保障程序、无力偿债风险及最坏年内清算情形构成流动性异常E3；奇异人生开发主体R2；不同于仅工会裁员表态E1。对照9月现金可撑至2027年1月底警告，本期新增保障程序与11月裁定/解雇节点，保留工会归因。 |
| W20261028_I201 | include | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 E2正式定档×R2有较强声量的长期开发生活模拟产品+M1=5；行业与产品日历独立，两栏均可入选。 |
| N_CAPCOM | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 来源证明跨《Street Fighter 6》《Monster Hunter》《Resident Evil》产品组合的统一账户系统及1170万账户覆盖，属于全球头部发行研发主体，R3；账户安全状态E2。 |
| N_SIDE | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | Side跨美洲、EMEA和亚洲服务网络、逾500名美术师及多款AAA项目参与证明其具有较强行业影响力；收购及全球负责人任命E3R2。 |
| N_SYBO | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 来源证明49亿累计下载、1亿至1.5亿月活及长期全球移动产品经营规模，SYBO为名单外同等影响力手游主体；经营数据E2R3。 |
| N_DOUYIN | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 头部互联网平台的小游戏业务与中国移动市场数据，R3；2025年统计口径属于当期报道支持的历史数据，E2。 |
| N_WECHAT | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 腾讯旗下移动小游戏平台2025年生态数据E2R3；同事件历史均未曝光，按分数/R/顺序竞争本期唯一内部保留位。 |
| N_NEKODAY | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 来源明确Nekoday获Bilibili和NetEase投资，R2；续作众筹超过60万元是资本筹措E3，并保留春节前发起的历史语态。 |
| N_HIGHGUARD | include | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 来源证明Wildlight获Tencent投资及Respawn/Apex核心团队背景，按实际工作室R2；停运E2，FPS竞技M1。 |
| N_RE9 | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | Capcom全球头部IP与跨作商业规模直接取证，R3；本事件为具体销量数据E2，非例行公司财报。 |
| N_MOORE | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 实际接收人才的主体为网易直属Eggy团队，R3；前制作人加入产品团队的核心人才变化E3，M0不借派对标签加分。 |
| N_GENSHIN | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 米哈游直接产品的UGC数据E2R3；1.5亿指累计游玩次数，非收入、独立玩家或本月新增。 |
| N_ROCO_TEST | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 腾讯Magic Cube直属项目线下新品测试E3R3；不把收集/培养/战斗一般标签自动当作竞技或数值卡牌RPG。与西方发行规划为不同日期的独立事件。 |
| N_SPIRE | include | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 来源证明定义roguelike卡组构筑细分市场、长期Steam愿望单前五与续作28万峰值，具有较强行业影响力R2；EA实际发售E3；卡组构筑不自动等于数值卡牌RPG，M0。 |
| N_HELIX | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | Microsoft游戏主机平台业务R3；Asha Sharma公开新硬件代号与PC兼容目标属于战略项目公开E3。6月已刊的是硬件成本危机及商业模式表态，不是3月代号公布同一事件。 |
| N_FORGOTTEN | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 来源明确NetEase Games Joker的新作测试E3R3；本条2月测试与历史7月公测为不同事件日期和生命周期阶段，不伪造本周新开服。 |
| N_COD | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | Microsoft游戏业务与全球头部Activision系列的经营里程碑，R3；非公司例行财报E2；来源明确射击及battle royale产品形态M1。 |
| N_BIOWARE | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | EA全球头部研发发行主体R3，已确认工作室关闭与项目取消E2；以可用完整IGN正文取证，保留10月21日事件日期。 |
| N_ATARI | exclude | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 历史同事件均未曝光，但本期唯一card_carryover由同为6分、主体R3的微信小游戏获得；Atari主体R2，排序靠后。 |
| N_CARD_TEST | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 来源直接确认Tencent发行、Smilegate旗下SUPER CREATIVE研发，3月11日付费二测为新品测试E3R3；DBG与CRPG标签不足单独证明数值卡牌RPG，M0。 |
| N_HOK_SCHEDULE | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 腾讯头部IP直接项目的档期公布E2R3；来源明确1对1及4对4的PVP模式M1。该3月20日发布会与4月17日移动端上线为不同事件，不把相同事实重复拆条。 |
| N_MARATHON | include | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 来源证明Bungie以Halo、Destiny两代产品影响西方FPS，并直接研发Marathon，名单外头部主体R3；新品服务器压力测试E3，FPS竞技M1。 |
| N_TIANXIA | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | NetEase直属成熟IP跨平台版本上线与明确经营数据，E2R3；属于历史经营数据而非本周更新宣传，不因事件较早降低分值。 |
| N_WATER | include | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 来源证明Yishijie多款产品月收入过亿及国内外SLG发行能力，按具有较强影响力的主体R2；1月上线后跨渠道数据E2、明确SLGcasual M1。历史9月出海榜中的同名增长属不同统计期，不以产品名相同判作同一数据事件。 |
| N_LAST_ASYLUM | include | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 37 Interactive Entertainment直属产品的首月经营数据E2R3，明确休闲SLG加M1；统计期为2月11日上线后的首月，与历史8月海外收入榜为不同统计事件。 |
| A_SHOGUN | include | ai_trends |  | 当周同事件合并一次；采用本期Creative Assembly最新外包审核说明及处理状态；不把上周下架重写成26日下架。 |
| A_EPIC_CODE | include | ai_trends |  | 当周同事件合并一次；引擎与游戏开发直接应用，提供人工架构控制和具体任务时长结果；厂商自述归因。 |
| A_EPIC_EULA | include | ai_trends |  | 当周同事件合并一次；直接作用于游戏工具的训练授权，区分计划修改与现行禁止，不与编码应用合并。 |
| A_AILIAILI | include | ai_trends |  | 当周同事件合并一次；直接游戏产品与制作流程落地，完整开发者访谈提供交互、记忆、成本与边界。 |
| A_SCALING | include | ai_trends |  | 来源完整、游戏应用具体；当周独立事件按优先级采用。 |
| A_GENIE | include | ai_trends |  | 来源完整、游戏应用具体；当周独立事件按优先级采用。 |
| C_WUWA | include | community_discourse |  | 当周同事件合并一次；触发与争议逻辑清楚，并有窗口内补充或双方态度；严格玩家归因。 |
| C_END | include | community_discourse |  | 当周同事件合并一次；同窗口社区池已补扫；缺少明确新事件/可读后续、旧争议无新增、证据薄或相较已选事件优先级较低。 |
| C_DELTA | include | community_discourse |  | 当周同事件合并一次；旧帖在28日出现围绕收益方差和资产价值的新反驳，保留前情与对立意见；不把玩家估算写成概率或官方事实。 |
| D_C001 | include | deep_analysis | {'relevance': 2, 'insight': 3, 'evidence': 3, 'card': 3, 'total': 11} | 飞书周四备选 Bot回执明确选择，按C001、C022顺序写入正文；C001是唯一指定主卡。 |
| D_C022 | include | deep_analysis | {'relevance': 3, 'insight': 3, 'evidence': 2, 'card': 2, 'total': 10} | 飞书周四备选 Bot回执明确选择，按C001、C022顺序写入正文；C001是唯一指定主卡。 |
| AUD_0067 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0068 | merge → W20261028_I231 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0069 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0070 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0071 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0072 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0073 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0074 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0075 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0076 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0077 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0078 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0079 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0080 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0081 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 普通新增内容或综合发售清单E0；综合清单中的产品分别在产品日历反扫，不把无关产品打包成行业事件。 |
| AUD_0082 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0083 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0084 | merge → W20261028_I244 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0085 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0086 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0087 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0088 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0089 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0090 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 纯裁员/劳资事件按E1；没有工作室关停或项目取消新状态，当前分数低于5。 |
| AUD_0091 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0092 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0093 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0094 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0095 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 普通新增内容或综合发售清单E0；综合清单中的产品分别在产品日历反扫，不把无关产品打包成行业事件。 |
| AUD_0096 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0097 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0098 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0099 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0100 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0101 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0102 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0103 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0104 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0105 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0106 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0107 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0108 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0109 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0110 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0111 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0112 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0113 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0114 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0115 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0116 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0117 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0118 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0119 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0120 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0121 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0122 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0123 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0124 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0125 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0126 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0127 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0128 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0129 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0130 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0131 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0132 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0133 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0134 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | Unity与PvX融资合作按E3R3M0=9，但一源正文受阻、一源仅一句资金摘要，条款和适用条件不足，来源质量门禁排除。 |
| AUD_0135 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0136 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0137 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0138 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0139 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0140 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0141 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0142 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0143 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | Unity与PvX融资合作按E3R3M0=9，但一源正文受阻、一源仅一句资金摘要，条款和适用条件不足，来源质量门禁排除。 |
| AUD_0144 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0145 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0146 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0147 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0148 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0149 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0150 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0151 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0152 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0153 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0154 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0155 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0156 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0157 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0158 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0159 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0160 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0161 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0162 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0163 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0164 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0165 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0166 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0167 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0168 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 只有标题与“打击AI泛滥”短摘要，无审核新规适用范围和实施说明，来源质量不足。 |
| AUD_0169 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0170 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0171 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0172 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0173 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0174 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0175 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0176 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0177 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0178 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0179 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0180 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0181 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0182 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0183 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0184 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0185 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0186 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0187 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0188 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0189 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0190 | exclude | deep_analysis | {'relevance': 0, 'insight': 1, 'evidence': 1, 'card': 0, 'total': 2} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0191 | exclude | deep_analysis | {'relevance': 0, 'insight': 1, 'evidence': 1, 'card': 0, 'total': 2} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0192 | merge → D_C001 | deep_analysis | {'relevance': 2, 'insight': 3, 'evidence': 3, 'card': 3, 'total': 11} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0193 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0194 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0195 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0196 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0197 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0198 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0199 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0200 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0201 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0202 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0203 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0204 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0205 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0206 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0207 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0208 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0209 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0210 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0211 | merge → C_DELTA | community_discourse |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0212 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0213 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0214 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0215 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0216 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0217 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0218 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0219 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0220 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0221 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0222 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0223 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0224 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0225 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0226 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0227 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0228 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0229 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0230 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0231 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0232 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0233 | merge → A_GENIE | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0234 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0235 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0236 | merge → A_EPIC_EULA | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0237 | merge → A_EPIC_CODE | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0238 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0239 | merge → A_AILIAILI | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0240 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0241 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0242 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0243 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0244 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0245 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0246 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0247 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0248 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0249 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0250 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0251 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0252 | merge → W20261028_I201 | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0253 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0254 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0255 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0256 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0257 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 常规上半财年销量与数字化比例，无直接证明显著超预期、异常减值或资本结构变化，例行财报排除。 |
| AUD_0258 | merge → N_ATARI | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0259 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0260 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0261 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0262 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0263 | merge → W20261028_I346_IOS | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0264 | merge → W20261028_I211 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0265 | merge → W20261028_I229_BRUTAL | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0266 | merge → W20261028_I145 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0267 | merge → W20261028_I157 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0268 | merge → W20261028_I241 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0269 | merge → W20261028_I251 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0270 | merge → W20261028_I164 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0271 | merge → W20261028_I030 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0272 | merge → W20261028_I059 | industry_news | {'event': 3, 'relevance': 2, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0273 | merge → W20261028_I130 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0274 | merge → W20261028_I206 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0275 | merge → W20261028_I239 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0276 | merge → W20261028_I160 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0277 | merge → W20261028_I160 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0278 | exclude | deep_analysis | {'relevance': 3, 'insight': 1, 'evidence': 2, 'card': 1, 'total': 7} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0279 | exclude | deep_analysis | {'relevance': 3, 'insight': 1, 'evidence': 2, 'card': 1, 'total': 7} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0280 | exclude | deep_analysis | {'relevance': 3, 'insight': 1, 'evidence': 2, 'card': 1, 'total': 7} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0281 | exclude | deep_analysis | {'relevance': 3, 'insight': 1, 'evidence': 1, 'card': 1, 'total': 6} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0282 | exclude | deep_analysis | {'relevance': 3, 'insight': 3, 'evidence': 3, 'card': 3, 'total': 12} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0283 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0284 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0285 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0286 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0287 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0288 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0289 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0290 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0291 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0292 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0293 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0294 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0295 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0296 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0297 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0298 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0299 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0300 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0301 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0302 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0303 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0304 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0305 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0306 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0307 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0308 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0309 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0310 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0311 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0312 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0313 | merge → A_SHOGUN | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0314 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0315 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0316 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0317 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0318 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0319 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0320 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0321 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0322 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0323 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0324 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0325 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0326 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0327 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0328 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0329 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0330 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0331 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0332 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0333 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0334 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0335 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0336 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0337 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0338 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0339 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0340 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0341 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0342 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0343 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0344 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0345 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0346 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0347 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0348 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0349 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0350 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0351 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0352 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0353 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0354 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0355 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0356 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0357 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0358 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0359 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0360 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0361 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0362 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0363 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0364 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0365 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0366 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0367 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0368 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0369 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0370 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0371 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0372 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0373 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0374 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0375 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0376 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0377 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0378 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0379 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0380 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0381 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0382 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0383 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0384 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0385 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0386 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0387 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0388 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0389 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0390 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0391 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0392 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0393 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0394 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0395 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0396 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0397 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0398 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0399 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0400 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0401 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0402 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0403 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0404 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0405 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0406 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 普通新增内容或综合发售清单E0；综合清单中的产品分别在产品日历反扫，不把无关产品打包成行业事件。 |
| AUD_0407 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0408 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0409 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0410 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0411 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0412 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0413 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0414 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0415 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0416 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0417 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0418 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0419 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0420 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0421 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0422 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0423 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0424 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0425 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0426 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0427 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0428 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0429 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0430 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0431 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0432 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0433 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0434 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0435 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 纯裁员/劳资事件按E1；没有工作室关停或项目取消新状态，当前分数低于5。 |
| AUD_0436 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0437 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0438 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0439 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0440 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0441 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0442 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0443 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0444 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0445 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0446 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0447 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0448 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0449 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0450 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0451 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0452 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0453 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0454 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0455 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0456 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0457 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0458 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0459 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0460 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0461 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0462 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0463 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0464 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0465 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0466 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0467 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0468 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0469 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0470 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0471 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0472 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0473 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0474 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0475 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0476 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0477 | exclude | industry_news | {'event': 0, 'relevance': 1, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0478 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 1, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0479 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0480 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0481 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0482 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0483 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 已传闻掌机的芯片规格线索，不是新品首曝/立项确认或战略动作，E1R3M0=3。 |
| AUD_0484 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0485 | merge → N_COD | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0486 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 1, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0487 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0488 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0489 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0490 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0491 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0492 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0493 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0494 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0495 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0496 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0497 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 纯裁员/劳资事件按E1；没有工作室关停或项目取消新状态，当前分数低于5。 |
| AUD_0498 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0499 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0500 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0501 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 1, 'total': 3} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0502 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0503 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0504 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0505 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0506 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0507 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0508 | merge → W20261027_I208 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0509 | merge → W20261027_I206 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0510 | merge → W20261027_I033 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0511 | merge → W20261027_I068 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0512 | merge → W20261027_I010 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0513 | merge → W20261027_I027 | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0514 | merge → W20261027_I064 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0515 | merge → W20261027_I063 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0516 | merge → W20261027_I025 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0517 | merge → W20261027_I030 | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0518 | merge → W20261027_I022 | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0519 | exclude | deep_analysis | {'relevance': 3, 'insight': 3, 'evidence': 2, 'card': 3, 'total': 11} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0520 | exclude | deep_analysis | {'relevance': 1, 'insight': 0, 'evidence': 0, 'card': 0, 'total': 1} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0521 | exclude | deep_analysis | {'relevance': 2, 'insight': 1, 'evidence': 1, 'card': 1, 'total': 5} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0522 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0523 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0524 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0525 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0526 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0527 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0528 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0529 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0530 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0531 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0532 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0533 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0534 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0535 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0536 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0537 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0538 | merge → C_END | community_discourse |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0539 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0540 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0541 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0542 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0543 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0544 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0545 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0546 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0547 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0548 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0549 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0550 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0551 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0552 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0553 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0554 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0555 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0556 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0557 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0558 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0559 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0560 | merge → A_SHOGUN | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0561 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0562 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0563 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0564 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0565 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0566 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0567 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0568 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0569 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0570 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0571 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0572 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0573 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0574 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0575 | exclude | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0576 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0577 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0578 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0579 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 行业汇编仅提及10月21日伽马Q3报告，未给具体统计数值或完整报告正文，当前来源不足支持实质市场数据条目；不按事件日期排除。 |
| AUD_0580 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0581 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0582 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0583 | merge → W20261023_20261025_I529 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同一王者IP矩阵榜单事件合并；本篇未明确具体产品品类，单独M0，主候选按另一篇完整来源证据取M1。 |
| AUD_0584 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0585 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0586 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0587 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0588 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0589 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0590 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0591 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0592 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0593 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0594 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0595 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0596 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0597 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0598 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0599 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0600 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0601 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0602 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0603 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 普通新增内容或综合发售清单E0；综合清单中的产品分别在产品日历反扫，不把无关产品打包成行业事件。 |
| AUD_0604 | exclude | industry_news | {'event': 1, 'relevance': 2, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0605 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0606 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0607 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0608 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0609 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0610 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0611 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0612 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0613 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0614 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0615 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0616 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0617 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0618 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0619 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0620 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0621 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0622 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0623 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0624 | merge → N_BIOWARE | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0625 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0626 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0627 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0628 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0629 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0630 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0631 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0632 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0633 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0634 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0635 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0636 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0637 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0638 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0639 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0640 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0641 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0642 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0643 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0644 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0645 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0646 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0647 | merge → N_SIDE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0648 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0649 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0650 | merge → W20261027_I010 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0651 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0652 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0653 | merge → W20261026_I138 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0654 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0655 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0656 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0657 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0658 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0659 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0660 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0661 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0662 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0663 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0664 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0665 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0666 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0667 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0668 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0669 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0670 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0671 | merge → N_HELIX | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0672 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0673 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0674 | merge → N_HELIX | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0675 | merge → N_HELIX | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0676 | merge → N_HELIX | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0677 | merge → N_HELIX | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0678 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0679 | merge → N_SPIRE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0680 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0681 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0682 | merge → N_SPIRE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0683 | merge → N_SPIRE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0684 | merge → N_SPIRE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0685 | merge → N_SPIRE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0686 | merge → N_ROCO_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0687 | merge → N_ROCO_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0688 | merge → N_ROCO_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0689 | merge → N_ROCO_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0690 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0691 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0692 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0693 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0694 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0695 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0696 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0697 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0698 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0699 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0700 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0701 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0702 | merge → N_LAST_ASYLUM | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0703 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同篇多语言文本对千万元月消耗、月收入和月活混译，正文指标无法可靠统一；保留6分但以事实口径不确定排除。 |
| AUD_0704 | merge → N_LAST_ASYLUM | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0705 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同篇多语言文本对千万元月消耗、月收入和月活混译，正文指标无法可靠统一；保留6分但以事实口径不确定排除。 |
| AUD_0706 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同篇多语言文本对千万元月消耗、月收入和月活混译，正文指标无法可靠统一；保留6分但以事实口径不确定排除。 |
| AUD_0707 | merge → N_LAST_ASYLUM | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0708 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 同篇多语言文本对千万元月消耗、月收入和月活混译，正文指标无法可靠统一；保留6分但以事实口径不确定排除。 |
| AUD_0709 | merge → N_LAST_ASYLUM | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0710 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0711 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0712 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0713 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0714 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0715 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0716 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0717 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0718 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0719 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0720 | merge → N_HOK_SCHEDULE | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0721 | merge → N_HOK_SCHEDULE | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0722 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0723 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0724 | merge → N_HOK_SCHEDULE | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0725 | merge → N_HOK_SCHEDULE | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0726 | merge → N_GENSHIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0727 | merge → N_GENSHIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0728 | merge → N_GENSHIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0729 | merge → N_GENSHIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0730 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0731 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0732 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0733 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0734 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0735 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0736 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0737 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0738 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0739 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0740 | merge → N_MOORE | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0741 | merge → N_MOORE | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0742 | merge → N_MOORE | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0743 | merge → N_MOORE | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0744 | merge → N_CARD_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0745 | merge → N_CARD_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0746 | merge → N_CARD_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0747 | merge → N_CARD_TEST | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0748 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0749 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0750 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0751 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0752 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0753 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0754 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0755 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0756 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0757 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0758 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0759 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0760 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0761 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0762 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0763 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 蛮啾按实际产品覆盖和研发发行能力取R2；E2R2M0=4，行业未过线；产品日历独立通过多源排序。 |
| AUD_0764 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0765 | merge → W20261027_I030 | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0766 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 1, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0767 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0768 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0769 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0770 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0771 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0772 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0773 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0774 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0775 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0776 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0777 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0778 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0779 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0780 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0781 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0782 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0783 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0784 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0785 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0786 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0787 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0788 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0789 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0790 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0791 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0792 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0793 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0794 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0795 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0796 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0797 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0798 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0799 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0800 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0801 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0802 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0803 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0804 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0805 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0806 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0807 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0808 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0809 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0810 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0811 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 行业汇编仅提及10月21日伽马Q3报告，未给具体统计数值或完整报告正文，当前来源不足支持实质市场数据条目；不按事件日期排除。 |
| AUD_0812 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_0813 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0814 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0815 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0816 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0817 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0818 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0819 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0820 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0821 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0822 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0823 | merge → C_WUWA | community_discourse |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0824 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0825 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0826 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0827 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0828 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0829 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0830 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0831 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0832 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0833 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0834 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0835 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0836 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0837 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0838 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0839 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0840 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0841 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0842 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0843 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0844 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0845 | exclude | deep_analysis | {'relevance': 2, 'insight': 3, 'evidence': 2, 'card': 3, 'total': 10} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0846 | exclude | deep_analysis | {'relevance': 2, 'insight': 3, 'evidence': 3, 'card': 3, 'total': 11} | 本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。 |
| AUD_0847 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0848 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0849 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0850 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0851 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0852 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0853 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0854 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0855 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0856 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0857 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0858 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0859 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0860 | merge → C_WUWA | community_discourse |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0861 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0862 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0863 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0864 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0865 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0866 | exclude | community_discourse |  | 社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。 |
| AUD_0867 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0868 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0869 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0870 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0871 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0872 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0873 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0874 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0875 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0876 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0877 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0878 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0879 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0880 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0881 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0882 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0883 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0884 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0885 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0886 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0887 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0888 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0889 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0890 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0891 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0892 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0893 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0894 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0895 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0896 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0897 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0898 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0899 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0900 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0901 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0902 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0903 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0904 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0905 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0906 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0907 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0908 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0909 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0910 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0911 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0912 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0913 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0914 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0915 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0916 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0917 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0918 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0919 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0920 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0921 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0922 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0923 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0924 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0925 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0926 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0927 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0928 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0929 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0930 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0931 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0932 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0933 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0934 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0935 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0936 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0937 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0938 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0939 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0940 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0941 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0942 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0943 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0944 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0945 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0946 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0947 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0948 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0949 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0950 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0951 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0952 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0953 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0954 | merge → W20261023_20261025_I529 | industry_news | {'event': 2, 'relevance': 3, 'hook': 1, 'total': 7} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0955 | merge → W20261023_20261025_I528 | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_0956 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0957 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0958 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0959 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0960 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0961 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0962 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0963 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0964 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0965 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0966 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0967 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0968 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0969 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_0970 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0971 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0972 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0973 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0974 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0975 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0976 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0977 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0978 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0979 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0980 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0981 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0982 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0983 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0984 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0985 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0986 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0987 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0988 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0989 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0990 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0991 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0992 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | GameMaker商业许可变化E2R2M0=4；名单外主体按实际平台能力判断，不封顶R1。 |
| AUD_0993 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_0994 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0995 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0996 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0997 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0998 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_0999 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1000 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1001 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1002 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1003 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1004 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1005 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1006 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1007 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1008 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1009 | exclude | industry_news | {'event': 1, 'relevance': 1, 'hook': 0, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1010 | exclude | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 同一事件已见历史报告；本期未提供可验证的实质状态变化。 |
| AUD_1011 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1012 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1013 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1014 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1015 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1016 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1017 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1018 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1019 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1020 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1021 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1022 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1023 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1024 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1025 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1026 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1027 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1028 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1029 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1030 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1031 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1032 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1033 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1034 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1035 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1036 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1037 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1038 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1039 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1040 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1041 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1042 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1043 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1044 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1045 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1046 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1047 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1048 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1049 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1050 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1051 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1052 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1053 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1054 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1055 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1056 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1057 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1058 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1059 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1060 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1061 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1062 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1063 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1064 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1065 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1066 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1067 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1068 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1069 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1070 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1071 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1072 | merge → N_BIOWARE | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1073 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1074 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1075 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1076 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1077 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1078 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1079 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1080 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1081 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1082 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1083 | exclude | industry_news | {'event': 3, 'relevance': 1, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1084 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1085 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1086 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1087 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 蛮啾按实际产品覆盖和研发发行能力取R2；E2R2M0=4，行业未过线；产品日历独立通过多源排序。 |
| AUD_1088 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1089 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 0, 'total': 3} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1090 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1091 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1092 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1093 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1094 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1095 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1096 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1097 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1098 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1099 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1100 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1101 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1102 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | GameMaker商业许可变化E2R2M0=4；名单外主体按实际平台能力判断，不封顶R1。 |
| AUD_1103 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1104 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1105 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | GameMaker商业许可变化E2R2M0=4；名单外主体按实际平台能力判断，不封顶R1。 |
| AUD_1106 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1107 | merge → N_CAPCOM | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1108 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1109 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1110 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1111 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1112 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1113 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1114 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1115 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 1, 'total': 1} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1116 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1117 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1118 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1119 | merge → N_RE9 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1120 | merge → N_RE9 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1121 | merge → N_RE9 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1122 | merge → N_RE9 | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1123 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1124 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1125 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1126 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1127 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1128 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1129 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1130 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1131 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1132 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1133 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1134 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1135 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1136 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1137 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1138 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1139 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1140 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1141 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1142 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1143 | merge → N_FORGOTTEN | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1144 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1145 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1146 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1147 | merge → N_FORGOTTEN | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1148 | merge → N_FORGOTTEN | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1149 | merge → N_FORGOTTEN | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1150 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1151 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1152 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1153 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1154 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1155 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1156 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1157 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1158 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1159 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1160 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1161 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1162 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1163 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1164 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1165 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1166 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1167 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1168 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1169 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1170 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1171 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1172 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1173 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1174 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1175 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1176 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1177 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1178 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1179 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1180 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1181 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1182 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1183 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1184 | merge → N_HIGHGUARD | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1185 | merge → N_HIGHGUARD | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1186 | merge → N_HIGHGUARD | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1187 | merge → N_HIGHGUARD | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1188 | merge → N_HIGHGUARD | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1189 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1190 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1191 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1192 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1193 | merge → N_TIANXIA | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1194 | merge → N_TIANXIA | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1195 | merge → N_TIANXIA | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1196 | merge → N_TIANXIA | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1197 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1198 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1199 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1200 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1201 | merge → N_NEKODAY | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1202 | merge → N_NEKODAY | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1203 | merge → N_NEKODAY | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1204 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1205 | merge → N_NEKODAY | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1206 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1207 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1208 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1209 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1210 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1211 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1212 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1213 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1214 | exclude | industry_news | {'event': 2, 'relevance': 1, 'hook': 0, 'total': 2} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1215 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1216 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1217 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1218 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1219 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1220 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1221 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1222 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1223 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1224 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1225 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1226 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1227 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1228 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1229 | merge → N_SIDE | industry_news | {'event': 3, 'relevance': 2, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1230 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1231 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1232 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1233 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1234 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1235 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1236 | merge → N_WECHAT | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1237 | merge → N_WECHAT | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1238 | merge → N_WECHAT | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1239 | merge → N_WECHAT | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1240 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1241 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1242 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1243 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1244 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1245 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1246 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1247 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1248 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1249 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1250 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1251 | merge → N_MARATHON | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1252 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1253 | merge → N_MARATHON | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1254 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1255 | merge → N_MARATHON | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1256 | merge → N_MARATHON | industry_news | {'event': 3, 'relevance': 3, 'hook': 1, 'total': 10} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1257 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1258 | merge → N_DOUYIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1259 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1260 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1261 | merge → N_DOUYIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1262 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1263 | merge → N_DOUYIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1264 | merge → N_DOUYIN | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1265 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1266 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1267 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1268 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1269 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1270 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1271 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1272 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1273 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1274 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1275 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1276 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1277 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1278 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本期回顾八千万玩家，历史已曝光同产品全球玩家突破一亿；没有新的更高用户状态，repeat_only。 |
| AUD_1279 | exclude | industry_news | {'event': 1, 'relevance': 3, 'hook': 1, 'total': 4} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1280 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本期回顾八千万玩家，历史已曝光同产品全球玩家突破一亿；没有新的更高用户状态，repeat_only。 |
| AUD_1281 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1282 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1283 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1284 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1285 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本期回顾八千万玩家，历史已曝光同产品全球玩家突破一亿；没有新的更高用户状态，repeat_only。 |
| AUD_1286 | exclude | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 本期回顾八千万玩家，历史已曝光同产品全球玩家突破一亿；没有新的更高用户状态，repeat_only。 |
| AUD_1287 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1288 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1289 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1290 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1291 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1292 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1293 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1294 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1295 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1296 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1297 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1298 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1299 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1300 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1301 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1302 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1303 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1304 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1305 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1306 | merge → N_WATER | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1307 | merge → N_WATER | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1308 | merge → N_WATER | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1309 | merge → N_WATER | industry_news | {'event': 2, 'relevance': 2, 'hook': 1, 'total': 5} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1310 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1311 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1312 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1313 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1314 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1315 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1316 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1317 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1318 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1319 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 版号例行信息E0直接排除；不因历史日期排除。 |
| AUD_1320 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 版号例行信息E0直接排除；不因历史日期排除。 |
| AUD_1321 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 版号例行信息E0直接排除；不因历史日期排除。 |
| AUD_1322 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 版号例行信息E0直接排除；不因历史日期排除。 |
| AUD_1323 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 版号例行信息E0直接排除；不因历史日期排除。 |
| AUD_1324 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1325 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1326 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1327 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1328 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。 |
| AUD_1329 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1330 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1331 | merge → W20261023_20261025_I039 | industry_news | {'event': 3, 'relevance': 3, 'hook': 0, 'total': 9} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1332 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1333 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1334 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1335 | merge → A_SCALING | ai_trends |  | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1336 | exclude | industry_news | {'event': 2, 'relevance': 2, 'hook': 0, 'total': 4} | 蛮啾按实际产品覆盖和研发发行能力取R2；E2R2M0=4，行业未过线；产品日历独立通过多源排序。 |
| AUD_1337 | exclude | industry_news | {'event': 1, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1338 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1339 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1340 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1341 | merge → N_SYBO | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| AUD_1342 | exclude | industry_news | {'event': 0, 'relevance': 3, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1343 | exclude | ai_trends |  | 已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。 |
| AUD_1344 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1345 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1346 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1347 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1348 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1349 | exclude | industry_news | {'event': 2, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1350 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1351 | exclude | industry_news | {'event': 3, 'relevance': 0, 'hook': 0, 'total': 0} | 按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。 |
| AUD_1352 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1353 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1354 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1355 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。 |
| AUD_1356 | merge → N_CAPCOM | industry_news | {'event': 2, 'relevance': 3, 'hook': 0, 'total': 6} | 与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。 |
| SRC_S0445 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0446 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0447 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0448 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0449 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0450 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0451 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0452 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0453 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0454 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0455 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0456 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0457 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0522 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0523 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0765 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0880 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0881 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0882 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0883 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0884 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0885 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0886 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0887 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S0888 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1089 | exclude | deep_analysis | {'relevance': 2, 'insight': 2, 'evidence': 2, 'card': 2, 'total': 8} | 不在本周飞书正文选择中。 |
| SRC_S1091 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1092 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1093 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1094 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1095 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1096 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1097 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1098 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1099 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1100 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1101 | exclude | industry_news | {'event': 0, 'relevance': 0, 'hook': 0, 'total': 0} | 完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。 |
| SRC_S1438 | exclude | deep_analysis | {'relevance': 2, 'insight': 2, 'evidence': 2, 'card': 2, 'total': 8} | 不在本周飞书正文选择中。 |
| R001 | include | release_calendar | {'event': 3, 'source': 4, 'company': 3, 'total': 15} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R002 | include | release_calendar | {'event': 2, 'source': 4, 'company': 2, 'total': 10} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R003 | include | release_calendar | {'event': 3, 'source': 3, 'company': 0, 'total': 9} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R004 | include | release_calendar | {'event': 2, 'source': 4, 'company': 0, 'total': 8} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R005 | include | release_calendar | {'event': 2, 'source': 4, 'company': 0, 'total': 8} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R006 | include | release_calendar | {'event': 2, 'source': 4, 'company': 0, 'total': 8} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R007 | include | release_calendar | {'event': 2, 'source': 4, 'company': 0, 'total': 8} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| R008 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R009 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R010 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R011 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R012 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R013 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R014 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 超过本报告产品日历条数上限 |
| R015 | exclude | release_calendar | {'event': 1, 'source': 4, 'company': 0, 'total': 4} | 超过本报告产品日历条数上限 |
| R016 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 3, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R017 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 3, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R018 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 3, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R019 | exclude | release_calendar | {'event': 3, 'source': 3, 'company': 0, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R020 | exclude | release_calendar | {'event': 3, 'source': 3, 'company': 0, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R021 | exclude | release_calendar | {'event': 3, 'source': 3, 'company': 0, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R022 | exclude | release_calendar | {'event': 3, 'source': 3, 'company': 0, 'total': 9} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R023 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 3, 'total': 7} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R024 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 3, 'total': 7} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R025 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R026 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R027 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R028 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R029 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R030 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R031 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R032 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R033 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R034 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R035 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R036 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R037 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R038 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R039 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R040 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R041 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R042 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R043 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R044 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R045 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R046 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R047 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R048 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R049 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R050 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R051 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R052 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R053 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R054 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R055 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R056 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R057 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R058 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R059 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R060 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R061 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R062 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R063 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R064 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R065 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R066 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R067 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R068 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R069 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R070 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R071 | exclude | release_calendar | {'event': 3, 'source': 2, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R072 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R073 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R074 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R075 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R076 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R077 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R078 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R079 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R080 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R081 | exclude | release_calendar | {'event': 2, 'source': 3, 'company': 0, 'total': 6} | 事件日期不在报告窗口 |
| R082 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R083 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R084 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R085 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R086 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R087 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R088 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R089 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R090 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R091 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R092 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R093 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R094 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R095 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R096 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R097 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R098 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R099 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R100 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R101 | exclude | release_calendar | {'event': 2, 'source': 2, 'company': 0, 'total': 4} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R102 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R103 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R104 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R105 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R106 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R107 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R108 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R109 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R110 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R111 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R112 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R113 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R114 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R115 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R116 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R117 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R118 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R119 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R120 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R121 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R122 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R123 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R124 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R125 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R126 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R127 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R128 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R129 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R130 | exclude | release_calendar | {'event': 3, 'source': 1, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R131 | exclude | release_calendar | {'event': 1, 'source': 3, 'company': 0, 'total': 3} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R132 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R133 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R134 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R135 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R136 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R137 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R138 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R139 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R140 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R141 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R142 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R143 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R144 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R145 | exclude | release_calendar | {'event': 2, 'source': 1, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R146 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R147 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R148 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R149 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R150 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R151 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R152 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R153 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
| R154 | exclude | release_calendar | {'event': 1, 'source': 2, 'company': 0, 'total': 2} | 逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。 |
