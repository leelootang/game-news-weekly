# 选材决策｜日报2026-10-19

卡片曝光去重：历史窗口2026-10-05_to_2026-10-18，共104条；任一历史已曝光的同事件一律去重。I025为唯一card_carryover，历史未曝光、rank=null、limit=10、source=publish_log_manifest；Jagex7分低于I025的8分，其他未曝光旧事件不再入选。无material_update。

维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已逐条成卡；全量174条输入有映射，不设行业条数上限。

产品日历漏挂反查：已反扫全量industry_news/release_calendar正文，按产品+日期聚类并逐个落include/exclude。原始抽取raw保留；历史上线、普通宣传、非完整来源与旧体验版跨期重复均已排除；与行业新闻独立选材。

行业新闻 E×R+M：事件E×相关R+钩子M = 终分；日报阈值≥7，E0一票否决，按总分降序。

维度候选计数（可交叉计数）：国内移动10张 / 国产产品与人才16张 / 市场数据11张 / 并购4张 / 平台政策29张 / 档期变动22张 / 资本组织5张 / 海外重大14张。


| candidate | decision | target_section | scores | reason |
| --- | --- | --- | --- | --- |
| I001 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 现代战争故事收尾为既有产品生命周期表述，4分；同一内容已随新子系列报道曝光。 |
| I002 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 上古卷轴OL例行第二季地下城，非新品或重大商业状态。 |
| I003 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 战地皮肤质量回应转社区同事件，不在行业重复。 |
| I004 | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 经典模式收官与历史同事件；短讯27年1月口径与旧报道不一致，不能据24字短讯认定实质新阶段。 |
| I005 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 海外老作取消VR门槛后的预购，弱迁移3分；不是完整新品发售。 |
| I006 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | Steam成就整理功能是一般平台能力，5分，非重大分发或收费政策。 |
| I007 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 国产手柄常规预售宣传，无游戏商业状态变化。 |
| I008 | exclude | industry_news | 事件1×相关1+钩子1 = 2 | 联机试玩版累计下载50万，单产品里程碑E1；未证明国内主体、PVP或结构性赛道份额，2分。 |
| I009 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 格斗赛事赛果，非资本或电竞组织结构变化。 |
| I010 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 增量钓鱼PC试玩版；主体相关性未知，不能由模拟标签直接给R3，4分。 |
| I011 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 海外展会中的PC试玩版，未见移动/中国市场迁移，4分。 |
| I012 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 试玩版热门榜前十与新英雄，纯榜单/内容更新。 |
| I013 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 创作者患病信息不等于管理层离任或项目取消；不推测健康及项目后果。 |
| I014 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | Reshine未来PC档期与试玩，弱迁移3分；日历单独判断。 |
| I015 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | ACE接入内容检测的客户宣传案例；未披露新合作签署日或重大合作状态，不把既有接入宣传抬为E3。 |
| I016 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 综合稿拆分幕府重制版下架与RuneScape取消；前者5分，后者另作历史查重。 |
| I017 | include | industry_news | 事件2×相关3+钩子1 = 7 | 国产团队太吾授权衍生作的新经营案例数据，7分；不以报道日替代实际EA发售日。 |
| I018 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 欧盟草案公开征求意见始于10月1日；当前为影响解读，不是本期法律生效。R2、5分。 |
| I019 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | AI反编译综合评论反扫转AI候选；10月10日DMCA、13日Labs等明确旧日期逐件审计，不包装为19日新事件。 |
| I020 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 特斯拉汽车与游戏类比，非游戏行业独立新闻。 |
| I021 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 育碧裁员/工作室关闭5分；天美项目取消另与历史精确匹配。 |
| I022 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 校招调查转AI新闻；人才培养机制可支撑深度，泛招聘不按核心管理变动计E3。 |
| I023 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 9月24日上线、国庆后榜单的产品体验分析；没有19日新生命周期节点，日历不得回填上线。 |
| I024 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 捉宠横向分析，明确9月上线及10月7日结束测试均为前情；普通产品比较不作为本期首曝。 |
| I025 | include | industry_news | 事件2×相关3+钩子2 = 8 | 16日发布的Sensor Tower9月发行商收入结构，25/26为同数据事件；全部历史匹配未曝光，可竞争唯一补位。 |
| I026 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 周报综述按资本、平台、产品等独立事件拆分，不能整篇打包行业卡。 |
| I027 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | AI NPC记忆工程案例与成本测算转AI，估算不是实际运营账单。 |
| I028 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 丹青渡叙事版本评论，纯榜单Top3与普通版本不豁免E0；不按采集日重写版本上线。 |
| I029 | exclude | industry_news | 事件2×相关3+钩子2 = 8 | 天美刺客信条命运取消为同一历史事件。 |
| I030 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 金茶奖历届回顾与征集，非本期公司或产品新增状态。 |
| I031 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 海外已公开产品参加线下展会，国内首次参展不是新品首次首曝。 |
| I032 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 大会明确10月15日；合作平台和AI助手披露属窗口外，不作为19日新发布。 |
| I033 | merge into I028 | industry_news | 事件0×相关3+钩子1 = 1 | S0028英文镜像，同一媒体译文不得作独立来源。 |
| I034 | merge into I030 | industry_news | 事件0×相关3+钩子1 = 1 | S0030英文镜像，历史回顾。 |
| I035 | merge into I029 | industry_news | 事件2×相关3+钩子1 = 7 | S0029英文镜像，同项目取消，不独立增加来源数量。 |
| I036 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | Rain98体验版晚到报道；已进入周末产品日历，同产品同阶段跨期重复；行业纯海外单机R1。 |
| I037 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 禁止主体的常规赛事宣传，正文排除。 |
| I038 | merge into I009 | industry_news | 事件0×相关3+钩子1 = 1 | SCS决赛赛果，与S0009同一赛事，不是战略动作。 |
| I039 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | LAP能力展示明确在10月14日，AI反扫后按窗口外排除，未见本期新的部署里程碑。 |
| I040 | include | industry_news | 事件2×相关3+钩子1 = 7 | 国内厂商海外二合游戏最新月收入与社群经营案例，7分；不是把2月上线改成10月。 |
| I041 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | AI素材与游戏内短剧的直接应用案例，转AI分区，不在行业重复产品数据。 |
| I042 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | AI法律解读，转AI审计，与UKIE认证服务分属背景/新服务。 |
| I043 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | UKIE面向游戏工作室的新AI合规认证服务，转AI。 |
| I044 | include | industry_news | 事件3×相关2+钩子2 = 8 | Liquid Swords破产涉及资产出售、27人解雇、网易少数股权投资背景，8分；并非只给裁员E3。 |
| I045 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 克罗地亚行业会议宣传，非全球竞争格局或游戏新平台。 |
| I046 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | QA工会罢工授权，尚非实际罢工；一般海外劳资E1，3分。 |
| I047 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | GDCA参评流程与奖项调整，行业活动例行规则。 |
| I048 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | Flow融资摘要，历史卡片已曝光，重复排除。 |
| I049 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 墨西哥社交/流媒体保护法令短摘，没有游戏具体新要求，3分且非完整正文。 |
| I050 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | Pocket Gamer奖项报名宣传。 |
| I051 | exclude | industry_news | 事件2×相关3+钩子1 = 7 | EWC新增2027预选路径，7分但仅被阻断页面摘要，无可发布完整正文。 |
| I052 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 恋与深空联动事件转社区；摘要不足，正文采用完整社区原帖并保留玩家归因。 |
| I053 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 莉莉丝产品累计流水5000万美元里程碑，E1R3M1=4；完整报道不可读。 |
| I054 | merge into I060 | industry_news | 事件3×相关3+钩子2 = 11 | 同一主体、同一10月19日交割/破产事件；由完整正文候选承载。 |
| I055 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | 会议赞助商宣传。 |
| I056 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | 移动变现评论仅有摘要，不能支撑平台规则变化或深度。 |
| I057 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 每周播客摘要，Squad停运没有新增状态且未获得完整论证。 |
| I058 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | 人事综述拆分Apple渠道核心管理、其他高管和非核心岗位；不全篇打包。 |
| I059 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | Netflix约60名游戏员工裁员，纯裁员E1R2M1=3，未由本稿证明新增工作室关闭。 |
| I060 | include | industry_news | 事件3×相关3+钩子2 = 11 | Metacore于10月19日宣布交割完成、团队进入Supercell，11分；与此前5月计划属不同实质状态，本双周历史无匹配。 |
| I061 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 腾讯领投Flow4600万美元旧融资，再次报道不构成新融资。 |
| I062 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 使命召唤纪念内容短摘，非组织变动新闻。 |
| I063 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 马里奥铭牌趣闻，非商业或生产变迁。 |
| I064 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 小岛秀夫动画客串，普通宣传。 |
| I065 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | Saros新周目更新，非重大新模式证据。 |
| I066 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | 反编译社区关闭转AI候选，但仅171字摘要不能核验完整事件。 |
| I067 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 星球大战赛车后续内容采访仅短摘。 |
| I068 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 无畏契约赛事线下活动复盘；英雄公布与营销活动不构成独立行业商业新闻。 |
| I069 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | GTA6周边档期观察；重复引用既有发售档期、不是本期GTA6正式发售。 |
| I070 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 触乐澳门见闻，非游戏行业新闻。 |
| I071 | include | industry_news | 事件2×相关3+钩子1 = 7 | 本期发表的手工模拟游戏经营案例，7分；明确回本及在线峰值发生在9月21日和10月4日，非本期发行。 |
| I072 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 开测清单分产品判断；21日垂钓者为已曝光旧定档，23日篮球少女另计。 |
| I073 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | Game Pass常规游戏轮换，不是订阅定价或渠道政策。 |
| I074 | exclude | industry_news | 事件2×相关1+钩子2 = 4 | Faraway新档期，普通海外单机R1仅4分；且正文标snippet不采用。 |
| I075 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | MrBeast营销视频为常规宣传；DMZ预购提前访问单独日历审计，不写完整游戏已上线。 |
| I076 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 战地皮肤质量争议转社区，与S0091同事件。 |
| I077 | merge into I044 | industry_news | 事件3×相关2+钩子2 = 8 | 同一主体、同一10月19日交割/破产事件；由完整正文候选承载。 |
| I078 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | Lucasfilm合作对象从大厂延展中小团队的战略访谈，无本期新签合同，3分。 |
| I079 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 主机帧生成专利转AI审计；专利不等于正式产品规格。 |
| I080 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 普莱斯演员感谢好评属宣传与口碑，不是新产品状态。 |
| I081 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 合作恐怖PC试玩版，未证明PVP/国内主体，4分。 |
| I082 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | FFBE手游改编主机单机的开发采访有移动资产迁移，但当前为前瞻非新立项，3分。 |
| I083 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 最终幻想单机试玩前瞻；发行类型为海外主机单机，不能仅RPG给R3，4分。 |
| I084 | exclude | industry_news | 事件1×相关1+钩子1 = 2 | 赛博朋克电影原创故事路线表态，非新签影视合作，2分；Hadar旧进展不重复。 |
| I085 | exclude | industry_news | 事件2×相关3+钩子2 = 8 | 天美刺客信条命运取消画面同历史曝光。 |
| I086 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | NVIDIA App智能体控制转AI；更新日期明确13日，不按19日采集改写为新品。 |
| I087 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 羊蹄山单款主机续作销量估算，缺少移动或中国市场迁移，3分。 |
| I088 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | 悟空声优抗议AI声音转AI/社区审计，不以当事人愤怒替代确切授权或法律结论。 |
| I089 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 蝙蝠侠电影旧取消项目剧情，非游戏。 |
| I090 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 电影票房，非游戏。 |
| I091 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 战地皮肤官方回应与玩家反应转社区。 |
| I092 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | Slam Tank未来试玩，海外PC单机相关性未知仅4分；AI为世界观背景非生成式应用。 |
| I093 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | Brushland已有产品常规玩法预告，不证明首次曝光。 |
| I094 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | Crop概览预告，2027旧档期，非本期首曝证据。 |
| I095 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 剑星拍照模式宣传，11月5日旧跨平台安排，不当新定档。 |
| I096 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 快递员汤姆PC/Switch未来档期，普通海外单机R1，3分。 |
| I097 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 乐高合集老作Switch2移植，弱迁移3分。 |
| I098 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 银松镇海外单机已发售宣传，R1、4分。 |
| I099 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 恶意不息职业系统概览，既有2027年3月档期不证明本期新定档。 |
| I100 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 生化危机旧作Switch2移植体验，弱迁移3分；多游戏逐项留日历。 |
| I101 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | AI仿作担忧导致取消试玩，已在上一期AI披露；本期无新状态。 |
| I102 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 昆汀电影计划，非游戏。 |
| I103 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 街头霸王电影票房新数据，但纯海外游戏衍生电影与移动业务迁移弱，3分。 |
| I104 | exclude | industry_news | 事件1×相关1+钩子1 = 2 | Bloober维持实体版战略表态，未公布新项目或渠道政策，2分。 |
| I105 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 星球大战电影搁置，非游戏项目取消。 |
| I106 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 演员接戏经历，非游戏。 |
| I107 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 加菲猫评测，非新商业事实。 |
| I108 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | GTA6发售预告细节分析，不能把发售预告当正式发售。 |
| I109 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | Steam即将发行清单逐产品评分；不能全篇按模拟/RPGR3。 |
| I110 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | ARC2.0体验推荐，13日PVE测试为历史已曝光。 |
| I111 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 哈迪斯2音乐评论，非新品或公司变化。 |
| I112 | exclude | industry_news | 事件1×相关1+钩子1 = 2 | Outlast Trials六年开发复盘，无本期产品或组织变化，2分。 |
| I113 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | Anthropic安全草案泄露转AI审计，与游戏环节无具体迁移链。 |
| I114 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 黑魂2早期原型考古，无商业状态。 |
| I115 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 23位开发者免费音量小游戏合集，海外一般小主体，4分。 |
| I116 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | Steam新品节8011个试玩的供给数据有PC发行迁移，5分；不因提及Roblox背景提高主体R。 |
| I117 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 婚礼显卡趣闻。 |
| I118 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 显卡供应传闻与否认，未证明游戏市场竞争迁移。 |
| I119 | exclude | industry_news | 事件1×相关1+钩子1 = 2 | Outlast历史融资与抵押开发复盘，不是本期新一轮融资，2分。 |
| I120 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 非官方PS5模拟器运行恶魔之魂的技术演示，弱迁移3分；不是官方PC发售。 |
| I121 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 显卡机场货物失踪，非游戏行业事件。 |
| I122 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 手柄产品评测，无产业结构事件。 |
| I123 | exclude | industry_news | 事件0×相关2+钩子1 = 1 | 师父12日移植为历史事件；本期仅品类付费榜第一，不以纯榜单抬E2，未构成实质新状态。 |
| I124 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 阅文群星漫卡首曝为历史已曝光，晚到同事件解读不再入选。 |
| I125 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 电源硬件广告。 |
| I126 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 内存优化硬件广告。 |
| I127 | exclude | industry_news | 事件0×相关0+钩子1 = 1 | 主板硬件广告，AI参数调校宣传不足以单独构成AI游戏新闻。 |
| I128 | include | industry_news | 事件2×相关3+钩子1 = 7 | 本期制作人访谈披露帕鲁正式版新增数百万玩家、中国/美洲居前，经营数据与品类结构7分；不声称19日首发。 |
| I129 | merge into I007 | industry_news | 事件0×相关3+钩子1 = 1 | 手柄预售广告同S0007。 |
| I130 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 国产射击叙事趋势评论，案例均7月、9月等旧节点，不改写为当日新战略。 |
| I144 | include | industry_news | 事件3×相关3+钩子1 = 10 | HUNGER新品封闭测试，原文明确搜打撤/角色扮演与PC，10分。 |
| I058_APPLE | include | industry_news | 事件3×相关2+钩子1 = 7 | 全球移动分发核心管理层变动，报道为将升任，E3R2M1=7；不能写成已完成任命。 |
| I016_RS | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 历史同事件未曝光，7分；低于本期唯一未曝光候选ST8分，不能再占第二条。 |
| I021_AC | exclude | industry_news | 事件2×相关3+钩子2 = 8 | 历史卡片已曝光，原型素材与背景补充不构成新取消。 |
| I026_X | exclude | industry_news | 事件3×相关2+钩子1 = 7 | 历史任一已曝光，晚到综述排除。 |
| I026_K | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 虽然日报未曝光，周报已第4条曝光，不能再次使用补位。 |
| I026_F | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 历史已曝光，无新增资金或交割状态。 |
| I026_C | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 融资为半个月前背景且已有历史报道，无新增。 |
| I026_A | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 同一期市场报告已在日卡曝光。 |
| I026_N | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 国际服旧计划已曝光，综述未见新发行日。 |
| I026_D | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 停运公告已在12日日报卡曝光。 |
| I026_S | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 公测历史已曝光，重复。 |
| I026_G | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 公测历史已曝光，重复。 |
| I026_B | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 常规业绩预告，无原文一致预期/指引偏离、重大减值或流动性证据；财报例外未过。 |
| I026_CA | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 实际日期明确14日，窗口外；此前未入报告也不能把发行日改19日。 |
| I026_CV | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 普通海外单机纯发售R1，4分，日期亦窗口外。 |
| I026_YY | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 已有产品图像升级预告，普通技术更新，不按新品或平台政策。 |
| I058_X | exclude | industry_news | 事件3×相关2+钩子1 = 7 | 任命已随Xbox XP组织调整曝光，无实质变化。 |
| I058_SK | exclude | industry_news | 事件1×相关2+钩子1 = 3 | 非执行董事加入跨媒体集团，不等于游戏业务CEO或核心团队更换，3分。 |
| I058_M | exclude | industry_news | 事件3×相关2+钩子1 = 7 | 历史10月7日日卡已曝光。 |
| I058_SC | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 非核心管理层，常规岗位移动；R3不豁免E0。 |
| I058_SM | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 原文未说明新公司的移动广告业务，不能凭记忆补迁移关系，4分。 |
| I072_F | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 同首曝确定档期已在日卡曝光，未发生实际测试。 |
| I072_B | include | industry_news | 事件2×相关3+钩子1 = 7 | 本期清单明确灵犀发行与新公测安排，E2R3M1=7。 |
| I109_00 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_01 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_02 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_03 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_04 | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 即将发行清单不证明已发售；在线合作餐厅经营明确优先赛道，10月20日实际EA尚未发生；日程预排无独立新定档证据，7分仍按时点不明排除。 |
| I109_05 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_06 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_07 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_08 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_09 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_10 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_11 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_12 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| I109_13 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 即将发行清单不证明已发售；普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。 |
| A019 | exclude | ai_trends | {} | 综合评论含多项明确窗口外事件；无单一本期新进展，不把旧DMCA/Labs/Astrocade改为新发布。 |
| A022 | include | ai_trends | {} | 本期校招访谈直接反映AI研发岗位和工作流程，具体采访与岗位统计采用。 |
| A026 | exclude | ai_trends | {} | Epic/迪士尼AI优先工作流为周报回顾，已在前期AI报道；Character破产为12日旧背景。 |
| A027 | include | ai_trends | {} | NPC长期记忆的游戏直接应用，区分已实现案例与假设模型调用账单。 |
| A032 | exclude | ai_trends | {} | 10月15日大会明确窗口外，助手将上线不可改写已上线。 |
| A039 | exclude | ai_trends | {} | 10月14日峰会既有能力展示，窗口外。 |
| A041 | include | ai_trends | {} | 游戏内65集AI短剧/漫剧及广告素材的直接应用，正文不重复行业条目。 |
| A042 | exclude | ai_trends | {} | 法律解读主要提供制度背景；具体新认证服务由A043承担，不将解读拼成另一个新闻。 |
| A043 | include | ai_trends | {} | 新服务直接覆盖游戏研发工具、授权、玩家可见内容与融资尽调。 |
| A066 | exclude | ai_trends | {} | 页面被阻断，171字摘要不能核验社区关闭原因或日期。 |
| A079 | exclude | ai_trends | {} | 仅为索尼专利，尚未落地；硬件预测和手柄数据缺乏本期可验证游戏效果。 |
| A086 | exclude | ai_trends | {} | NVIDIA App11.0.9.565明确13日，窗口外。 |
| A088 | exclude | ai_trends | {} | 声优声音侵权指控，单次争议与拟议立法未形成可核验游戏生产规则变化。 |
| A101 | exclude | ai_trends | {} | 试玩公开改封闭已在周末报AI刊载，本期无新状态。 |
| A109 | exclude | ai_trends | {} | Hypernet只有AI生成内容标签，没有生产环节或可核验机制。 |
| A113 | exclude | ai_trends | {} | 泛AI安全草案与游戏无直接采用或具体迁移链。 |
| A116 | exclude | ai_trends | {} | AI仿作/试玩取消主要既有案例，Steam供给数据行业另评5分。 |
| A127 | exclude | ai_trends | {} | 消费主板AI参数宣传，无具体游戏研发/产品经营新机制。 |
| A131 | include | ai_trends | {} | 明确速度和任务成本跃迁及价格，迁移至游戏脚本原型、测试和工具自动化，事实与推断分开。 |
| A132 | exclude | ai_trends | {} | ADK非阻塞语音教程有NPC迁移，但作为既有框架教程，优先于本期已选直接案例之后；未采用。 |
| A133 | exclude | ai_trends | {} | 单榜排名与常规模型小版本，缺少本期实际游戏采用，优先级低于已选明确成本变化。 |
| A134 | exclude | ai_trends | {} | MIT语音模型有配音原型迁移，但当前未见游戏采用或实测成本；本期优先直接案例与成本突破。 |
| A135 | exclude | ai_trends | {} | COBOL/Fortran等低资源语言基准，不足以证明游戏主流研发环节变化。 |
| A136 | exclude | ai_trends | {} | Trainium后端属于基础设施，缺少游戏工作负载迁移证据。 |
| A137 | exclude | ai_trends | {} | 吉瓦级集群训练背景，无具体游戏环节及独立效率变化。 |
| A138 | exclude | ai_trends | {} | 仅572字工作流教程摘要，缺少可审核游戏案例。 |
| A139 | exclude | ai_trends | {} | 网站被智能体入侵，缺少游戏主体或具体游戏安全环节变化。 |
| A140 | exclude | ai_trends | {} | Disney/Character收购拟议状态与破产后诉讼，未落到具体游戏业务。 |
| A141 | exclude | ai_trends | {} | 健康教练评测方法可类比NPC，但不是本期游戏新应用，优先直接游戏材料。 |
| A142 | exclude | ai_trends | {} | 美国联邦文职采购限制，无游戏具体作用链，不作为游戏行业法律建议。 |
| A143 | exclude | ai_trends | {} | 数据管道编排复盘有开发工具迁移，但本期无游戏落地，优先级低于已选五条。 |
| C160 | exclude | community_discourse | {} | 水楼不构成可命名事件。 |
| C161 | exclude | community_discourse | {} | 15日广告量旧帖，19日仅延续商单猜测，无新触发。 |
| C162 | exclude | community_discourse | {} | 16日AIGC激励旧帖，19日为旧立场反讽，缺少新事实；不把截图政策当已证实官方规则。 |
| C163 | exclude | community_discourse | {} | 2日文本修改旧帖，19日仅一句情绪回复。 |
| C164 | exclude | community_discourse | {} | 14日错别字旧帖，19日无新增官方进展。 |
| C165 | exclude | community_discourse | {} | 生物命名讨论缺少具体物种/研究原文，正文无法准确说明对象。 |
| C166 | exclude | community_discourse | {} | 14日EN不同步旧帖，19日仍推测代理/资金，无新增状态。 |
| C167 | exclude | community_discourse | {} | 12日联动旧帖，仅泛论军武受众。 |
| C168 | exclude | community_discourse | {} | 健康信息引发关心，缺少游戏机制争议；不传播玩家医学推测。 |
| C169 | exclude | community_discourse | {} | 签证未过指控没有明确演出者/官方取消信息，事件关键对象不清。 |
| C170 | exclude | community_discourse | {} | 欠薪改单机仅截图标题，游戏主体不明确，不能补猜名称。 |
| C171 | exclude | community_discourse | {} | 16日角色计划旧帖，19日无新机制或官方证据。 |
| C172 | exclude | community_discourse | {} | 18日谋勇兼备联动旧帖，19日为声优旧梗，无新触发。 |
| C173 | include | community_discourse | {} | 联动中虚拟伴侣题材与付费情感沉浸的冲突，19日新事件；玩家解释与官方事实区分。 |
| C091 | include | community_discourse | {} | 行业外溢；官方承认质量不足并明确修复安排，回应构成本期新进展。正文采用完整S0091，不把玩家AI猜测写成官方确认。 |
| D174 | exclude | deep_analysis | {"relevance": 1, "insight": 0, "evidence": 0, "card": 1, "total": 2} | 已配置newsletter优先检查：付费节目正文缺失，现有内容是采访前言，不足以支持Zelda/GTA机制分析。 |
| D027 | include | deep_analysis | {"relevance": 3, "insight": 3, "evidence": 3, "card": 3, "total": 12} | 完整NPC记忆成本分析；来源包含架构、传播边界、假设估算及端云代价，核心来源已选A027；与上一期跨设备调查不撞题。 |
| D022 | include | deep_analysis | {"relevance": 3, "insight": 3, "evidence": 3, "card": 3, "total": 12} | 完整多采访校招调查；岗位统计、面试评价、带教实例形成生产门槛与判断门槛分离机制，核心来源已选A022。 |
| R_ADD_39 | include | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | exclude | release_calendar | {"event": 3, "source": 2, "company": 3, "total": 9} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-004 | exclude | release_calendar | {"event": 3, "source": 2, "company": 3, "total": 9} | 正文证据/事件资格复核排除：历届金茶奖回顾，不是新品上线。 |
| R_ADD_55 | exclude | release_calendar | {"event": 3, "source": 3, "company": 0, "total": 9} | 正文证据/事件资格复核排除：只开放新作单一模式的预购提前访问，非完整新品上线或独立测试；且S0075为snippet。 |
| release-candidate-005 | exclude | release_calendar | {"event": 2, "source": 2, "company": 3, "total": 7} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-006 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-002 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。腾讯ACE为服务供应方，不是鹅鸭杀研运主体，删除公司加分。 |
| release-candidate-008 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。 |
| release-candidate-009 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-010 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-011 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。 |
| release-candidate-012 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。 |
| release-candidate-013 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。 |
| release-candidate-035 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：原文明确14日首次EA，不是旧品跨平台，且在本期之前。 |
| release-candidate-014 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-015 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-016 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：同体验版已通过周末报刊载，日历跨期重复。 |
| release-candidate-017 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：正文仅今年2月上线；日未知，保留月份，不补造具体日期。 |
| R_ADD_51 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 事件日期不在报告窗口 |
| R_ADD_54 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_53 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-037 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_56 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_57 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_58 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_59 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_60 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_61 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_62 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_63 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_64 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_65 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_66 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_67 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_68 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| R_ADD_69 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-022 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| release-candidate-001 | exclude | release_calendar | {"event": 2, "source": 3, "company": 0, "total": 6} | 正文证据/事件资格复核排除：发售预告/档期分析不是正式上线，也未证明本期新定档。 |
| R_ADD_43 | exclude | release_calendar | {"event": 2, "source": 3, "company": 0, "total": 6} | 正文证据/事件资格复核排除：两来源日期一致，但S0074被标snippet，不能提供第二份完整发布证据。 |
| release-candidate-023 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 正文证据/事件资格复核排除：前者普通第二季内容，后者公开试玩已取消且前期已报道；非本期可发布实际事件。 |
| release-candidate-024 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。 |
| release-candidate-026 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 正文证据/事件资格复核排除：正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。 |
| release-candidate-027 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| R_ADD_52 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| R_ADD_75 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 正文证据/事件资格复核排除：普通宣传，仅保留原文月份/年份，不补造日期。 |
| R_ADD_73 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 正文证据/事件资格复核排除：普通宣传，仅保留原文月份/年份，不补造日期。 |
| R_ADD_74 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 正文证据/事件资格复核排除：普通宣传，仅保留原文月份/年份，不补造日期。 |
| release-candidate-030 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| R_ADD_42 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| R_ADD_48 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 正文证据/事件资格复核排除：编辑器工具演示不是新品游戏；Saros普通新周目不按重大新模式。 |
| release-candidate-032 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| R_ADD_44 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| R_ADD_45 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| R_ADD_46 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| R_ADD_47 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 正文证据/事件资格复核排除：历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。 |
| R_ADD_70 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 正文证据/事件资格复核排除：只有单源，实际发生日未明确；采集日期不证明当日上线。 |
| R_ADD_71 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 正文证据/事件资格复核排除：只有单源，实际发生日未明确；采集日期不证明当日上线。 |
| R_ADD_72 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 正文证据/事件资格复核排除：只有单源，实际发生日未明确；采集日期不证明当日上线。 |
| release-candidate-038 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 正文证据/事件资格复核排除：前者普通第二季内容，后者公开试玩已取消且前期已报道；非本期可发布实际事件。 |
| R_ADD_40 | exclude | release_calendar | {"event": 1, "source": 1, "company": 0, "total": 1} | 正文证据/事件资格复核排除：普通新区，不属于老品重大玩法更新；保留排除。 |
| R_ADD_49 | exclude | release_calendar | {"event": 1, "source": 1, "company": 0, "total": 1} | 单源不具备正文资格 |
| R_ADD_41 | exclude | release_calendar | {"event": 1, "source": 1, "company": 0, "total": 1} | 正文证据/事件资格复核排除：普通联动，不属于产品日历准入的重大玩法更新。 |
| R_ADD_50 | exclude | release_calendar | {"event": 1, "source": 1, "company": 0, "total": 1} | 正文证据/事件资格复核排除：编辑器工具演示不是新品游戏；Saros普通新周目不按重大新模式。 |
