# 选用决策｜日报2026-10-14

卡片曝光去重：历史窗口2026-09-30至2026-10-13；71次历史条目，逐条读取card_exposed/card_rank/card_limit/card_exposure_source。已有曝光的重复事件不入选；本期无合格card_carryover，无material_update，未伪造新增事实。
维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已对全量行业177条与综合稿子事件成卡审计；独立事件不放入低信号打包项。具体计数见下表。
维度召回卡计数（可交叉，按事件/原因中的主体与信号标签检索，不是各分区入选数）：国内移动 15张；国产产品与人才 14张；市场数据 17张；并购 9张；平台政策 24张；档期变动 64张；资本组织 18张；海外重大 47张。
重建说明：未读取早报report_items/decisions作为筛选依据；保留原始抽取日历审计，修正历史月份回填及普通活动误召回。三七互娱产品表现独立评分，不作为深度。
日期门禁：8月上线、2023年上线等不填成10月14日；报道日期只用于已明确的公告，不替代实际发售日。
产品日历漏挂反查：完整扫描行业177条及日历19条；保留44个机器召回节点并增补22个节点，共66个。历史事件、普通内容、实际日期未明、别名合并、单源节点均有显式exclude；唯一合格多源优先前缀为1999TOKOYO Building。
行业新闻 E×R+M 打分：事件E×相关R+钩子M = 终分，E=0排除，日报终分≥7；证据与时效门禁独立，按终分降序，无条数上限。
来源警告：抽取失败0、空正文0；38条snippet或短摘要不作为最终证据。部分full标记记录只有标题导语，另行证据门禁排除。部分翻译长稿含2025年旧事，未视为新事件。
采集覆盖警告：采集审计有4个failed源（dataeye_36kr、nadianshi、cubox、wanjiang_16p_newgame），pocketgamer/vgc为degraded。抽取0失败只描述已落库236条，不等于所有采集源健康；未联网补库。
AI数量说明：5条直接游戏应用（游族管线、不问凡尘、Epic客户端、Google Play发现、DLSS模型）+3条有明确迁移链的新能力（Argon开放、实时语音、ComfyUI后期节点）。8条超过1–3软目标，但不按条数硬截合格信号；不保留一般融资、纯跑分或无正文实测。
深度交接：星期四日报，不执行周五飞书回执流程；只使用当日优先来源分析，不读取用户周报selection。

| candidate | decision | section | score | reason/history |
| --- | --- | --- | --- | --- |
| I032 | include | industry_news | 事件3×相关3+钩子2 = 11 | 国内厂商战略投资及董事席位变化；AI为被投业务背景，不是已接入库洛产品的证明。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I034 | include | industry_news | 事件3×相关3+钩子2 = 11 | 同一Flow Games融资，多家媒体完整报道；昨日仅摘要候选被排除，不是已发布历史事件。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I125 | include | industry_news | 事件3×相关3+钩子2 = 11 | 新品正式发售、模拟经营优先赛道，两家来源相互支持；正文不猜测未明示的实际发售日。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I126 | include | industry_news | 事件3×相关3+钩子2 = 11 | 新品正式发售、魂类RPG优先赛道，两来源支持；非媒体评分事件，未凭报道日期补实际发售日。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I081 | include | industry_news | 事件3×相关3+钩子1 = 10 | 腾讯体系移动发行基础设施的新业务上线；只计一个独立全文源，相关摘要与同URL不额外抬高M。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I082S | include | industry_news | 事件3×相关2+钩子1 = 7 | 海外拼图手游融资，移动生产/发行有明确迁移点R2；不因手游标签自动等同中国移动市场或策略RPG优先赛道。融资是核心，AI产线为建设方向。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I059 | include | industry_news | 事件3×相关2+钩子2 = 8 | 新组织整合研发，浏览器分发等具有平台迁移点R2，不因海外大厂自动R3；并非新增大规模招聘或强制AI路线。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I058 | include | industry_news | 事件2×相关3+钩子1 = 7 | 国内重点厂商R3；当前榜位结合二合循环、女性向IP改编及近期社群运营构成产品经营信号E2，不是孤立纯榜单；历史上线不冒充新上线，用户明确不作深度。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I175 | include | industry_news | 事件2×相关3+钩子1 = 7 | 国产自走棋新品一个月成绩与轻量化机制，非纯榜单；未将未披露的留存率量化，不凭记忆添加厂商。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I084 | include | industry_news | 事件2×相关3+钩子1 = 7 | Supercell固定R3；停服日期明确，区别于去年已停止研发的旧阶段；同URL摘要不计独立M2。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I029 | include | industry_news | 事件2×相关3+钩子1 = 7 | MMORPG优先赛道R3；国会讨论付费主播营销与披露义务是监管信号，不写成已立法或公司已被认定违法。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I030 | include | industry_news | 事件2×相关3+钩子1 = 7 | 事件核心是多款游戏跨平台迁移而不是普通促销；移动分发直接相关R3。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I062 | include | industry_news | 事件2×相关3+钩子1 = 7 | 国内主体的游戏内容授权及渠道合规信号R3；名单建议不等于已列入或禁售。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I097 | include | industry_news | 事件2×相关3+钩子1 = 7 | PVP优先赛道R3；当前经营数据与经济系统问题，不将9月22日旧稿125万销量拼成同日多源。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I144 | include | industry_news | 事件2×相关3+钩子1 = 7 | 模拟经营优先赛道R3，当前销量估算及单人开发机制；不是把旧补丁当新品发布。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I236S | include | industry_news | 事件2×相关3+钩子1 = 7 | 深度源反扫发现国内重点发行商的产品数据，单列行业候选；不与下文深度的三款不同产品重复。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| A026 | include | ai_trends | direct_application | 具体游戏研发场景、模型网关及工具层，不将演示写成量产。 |
| A057 | include | ai_trends | direct_application | 游戏产品直接应用AI资产、音效和对话，且有当前销量披露；不把标价乘销量视为实收。 |
| A166 | include | ai_trends | direct_application | AI明确写新代码并参与审查，已公开预览；不重复AI射击项目旧新闻。 |
| A080 | include | ai_trends | direct_application | 推荐和玩家发现直接作用于移动游戏分发；不另将同次发布拆成行业政策条目。 |
| A133 | include | ai_trends | direct_application | 聚类的是同一次DLSS5模型更新公告，不是仅因技术相似合并不同事件；具体游戏接入仍为计划。 |
| A178 | include | ai_trends | transferable_frontier | 全面开放与编码/3D原型能力、成本共同构成迁移价值，区别于例行跑分；第三方比较不当作通用性能承诺。 |
| A187 | include | ai_trends | transferable_frontier | API可用、亚秒级延迟与语音打断机制对应明确实时角色交互迁移链，不写成已有游戏采用。 |
| A181 | include | ai_trends | transferable_frontier | 虽正文短但三个明确能力及本地管线均有直接文本证据，迁移到游戏营销视频后期而非凭空说赋能。 |
| I027 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 正文所链接规划为9月21日材料，未证明14日新增发布/生效状态；不将“近日”改成今日政策。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I031 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 已有档期与后续PV/玩法访谈，不是首次曝光或本日上线。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I035D | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 历史已有且曾进入订阅卡片；设计复盘、换媒体和补背景不是实质状态变化。；{"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《三角洲行动》国服日活突破5800万，半年增长800万  /  2026-10-02_to_2026-10-08  /  card_exposed=False, card_rank=None, card_limit=10, card_exposure_source=publish_log_manifest", "《三角洲行动》国服日活跃用户突破5800万  /  2026-10-09_to_2026-10-11  /  card_exposed=True, card_rank=4, card_limit=10, card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true} |
| I035S | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 专访具有设计解释但未证明本期新的重大组织或生命周期状态；与DAU旧事件分开评分。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I036 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 主要案例和爆发时间早于本窗口，没有可定位的本期市场新增状态；AI仅为推测，不能当成采用事实。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I037 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 同一Aream报告与同一组数据，历史已订阅曝光；新增媒体数与老产品年龄分布不构成material_update。；{"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["三季度游戏并购额达578亿美元，移动IAP同比下降7%  /  2026-10-13_to_2026-10-13  /  card_exposed=True, card_rank=7, card_limit=10, card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true} |
| I040 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 创作过程、本地化与未来功能意向；没有证明新的商业状态，不能把首次采访当新品首曝。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I060 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | 含实质跨媒介战略但无新增资本/项目/组织决定；不与不同日期的XP部门成立混成新事件。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I061 | exclude | industry_news | 事件2×相关2+钩子2 = 6 | 确有工作室关闭而非仅裁员；全球多工作室成本调整及移动业务迁移点R2，不因大厂升为R3；总分6未过线。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I063 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | 多年人员统计不是本期核心管理层变动或新增组织，平台型研发效率迁移点R2。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I064 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | PC休闲发行服务关闭，数字内容访问/付费所有权有迁移点R2，总分5。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I066 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 展示会与独游发现迁移点，数据取自此前4月活动；未达分数线，不将常规下一场活动抬成E3。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I071 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 重要主体R3、合作信号应成卡；但唯一正文为snippet，证据门禁排除，不能据摘要补写正式事实。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I072 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 与Aream不是同一机构同一报告，不机械合并；只有snippet且总分5，无完整证据。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I075 | exclude | industry_news | 事件3×相关2+钩子1 = 7 | 广告业务跨媒介迁移可评分7，但唯一来源snippet，不满足正文证据门槛。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I082G | exclude | industry_news | 事件3×相关3+钩子0 = 9 | 同一融资历史已曝光；未有最终关账等新增状态，不因本期再次摘要而入选。；{"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["社交RPG开发商Gardens获超3500万美元B轮融资  /  2026-10-12_to_2026-10-12  /  card_exposed=True, card_rank=7, card_limit=10, card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true} |
| I082R | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 双周历史已发同月全球市场结构；改用另一数据机构和补Roblox数字不是市场实质新阶段。；{"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["9月全球手游下载与收入榜分化，腾讯与Roblox维持头部但多款长线产品回落  /  2026-10-05_to_2026-10-05  /  card_exposed=True, card_rank=2, card_limit=10, card_exposure_source=publish_log_manifest", "9月全球手游下载与收入榜分化，腾讯与Roblox维持头部但多款长线产品回落  /  2026-10-02_to_2026-10-08  /  card_exposed=True, card_rank=9, card_limit=10, card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true} |
| I082A | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 广告代理对9月29日头部样本的商店页采样，移动分发迁移点R2，总分5；不与同稿融资打包。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I095 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 来源明确腾讯关系；具体开发方向但未有本期新上线/正式定档，不把假设性商业模式当已变更。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I096 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 正文明确写于9月22日，125万/200万份属于旧阶段；不与新300万稿冒充同日多源。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I118 | exclude | industry_news | 事件2×相关2+钩子2 = 6 | 跨平台发行有迁移点R2；非官方匿名消息，总分6，正文不把传言写成已定档。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I124 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 既有策略产品完全版更新，不是新品首发；R3但4分，不能把重打包提到E3。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I154 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | 重大人才讣告应独立评估；未证明现任核心管理职位变动，E1，设计人才迁移点R2。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I165 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 既有PVE测试增加体验描述，没有新增可验证生命周期变化；历史已有订阅曝光。；{"history_match": true, "novelty": "repeat_only", "prior_occurrences": ["《ARC Raiders》2.0带动Steam在线回升至18.5万，10月13日启动PVE测试  /  2026-10-13_to_2026-10-13  /  card_exposed=True, card_rank=8, card_limit=10, card_exposure_source=publish_log_manifest"], "new_facts": [], "prior_card_exposed": true} |
| I167 | include | industry_news | 事件2×相关3+钩子1 = 7 | PVP产品跨平台开发计划，未上线但已明确开发动作；不与AI商店客户端作为同一事件重复。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I169 | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 只保留标题和导航，缺实际正文；即使潜在7分也因证据不足排除，不编造反作弊事实。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I170 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | 实质战略表态但没有明确本期新项目正式立项/资本动作，3分。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I177 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 固定最高关注R3，但年度普通活动不是战略合作；E0排除。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I236P | exclude | industry_news | 事件2×相关2+钩子1 = 5 | 平台营销规则有全球分发迁移点R2，5分；与Steam不同UI更新、市场数据分成独立事件。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I236H | exclude | industry_news | 事件2×相关0+钩子1 = 1 | 海外区域主机硬件统计未证明移动/国产/竞争格局迁移点，R0。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I042 | exclude | industry_news | 事件3×相关1+钩子2 = 5 | 新品试玩E3、同事件多源M2；一般海外恐怖冒险弱迁移点R1，总分5。产品日历按多源优先级另行采用，不跨栏发布。；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I001 | merge | industry_news | 事件2×相关2+钩子1 = 5 | 同一主体/产品、同一日期、同一事件的重复覆盖；PC跨平台传言仅标题导语，未能取证，不写作正式定档；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I002 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I003 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I004 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I005 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I006 | exclude | industry_news | 事件3×相关1+钩子0 = 3 | 昨日产品日历已出现的上线信息，且仅标题导语；不补实际发售日；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I007 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I008 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 新品测试信号与竞技品类，但正文仅复述标题，缺少测试范围等事实，不据标题扩写；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I009 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I010 | exclude | industry_news | 事件3×相关1+钩子1 = 4 | 节奏动作新品上线，弱迁移点R1，4分；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I011 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I012 | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 定档信号非正式上线E2应修正，且全文只有标题和灵感导语；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I013 | exclude | industry_news | 事件2×相关3+钩子1 = 7 | 已存在产品NS2试玩属跨平台节点，但仅标题与存档导语，证据不足；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I014 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I015 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 模拟类Demo上线信号，但仅标题和未来发售导语，无法区分首次测试范围，不扩写；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I017 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 模拟类试玩信号，但实际只有标题，具体测试事实无法取证；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I018 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I020 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I022 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 预购开启非正式上线、首曝，弱迁移点R1；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I023 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | PVP新品EA信号，标题式会员推广而无实际正文，证据不足；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I024 | exclude | industry_news | 事件3×相关3+钩子1 = 10 | 多人竞技上线信号，但仅抽奖标题与玩法导语，完整发布事实不足，不写厂商和日期；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I025 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I028 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I033 | exclude | industry_news | 事件1×相关3+钩子0 = 3 | 国产二游十年回顾与历史周年，没有本期新状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I041 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I043 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I044 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I045 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I047 | exclude | industry_news | 事件1×相关2+钩子0 = 2 | 开放世界多年趋势回顾，无独立本期新事件；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I048 | exclude | industry_news | 事件1×相关3+钩子0 = 3 | 星铁叙事讨论为旧内容回顾，不把采集日当版本日；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I049 | exclude | industry_news | 事件3×相关3+钩子0 = 9 | 逆水寒海外上线材料提到11月，正文年份/时序与当前窗口不符，旧稿隔离；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I050 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 明确是2025年第三季度常规财报，旧稿且无异常财报例外；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I051 | exclude | industry_news | 事件1×相关3+钩子0 = 3 | 灵犀RO采访在2025年背景，无本窗口新增阶段；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I052 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 正文明确为2025年ARC Raiders销量，不与2026年PVE事件混为一谈；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I053 | exclude | industry_news | 事件1×相关3+钩子0 = 3 | 国产团队AI开发长篇旧采访，没有可定位的本窗口AI新采用或产品发布变化；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I054 | exclude | industry_news | 事件2×相关0+钩子0 = 0 | 索尼2025年第二季度旧财报及历史减值，不是本期异常财务事件；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I055 | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 网易旧工作室关闭文章时序不符，无法确认本期新关停；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I056 | exclude | industry_news | 事件1×相关2+钩子0 = 2 | AA制作长期方法访谈，无本窗口确定性战略动作；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I065 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I067 | merge | ai_trends | 事件2×相关3+钩子1 = 7 | 同一主体/产品、同一日期、同一事件的重复覆盖；Game Finder为S0080完整正文同事件，当前仅snippet，不重复采用；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I068 | exclude | industry_news | 事件3×相关2+钩子1 = 7 | MCP游戏发布工具信号有迁移点但只有snippet，不能由标题写已落地能力；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I069 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I070 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I073 | merge | industry_news | 事件3×相关3+钩子1 = 10 | 同一主体/产品、同一日期、同一事件的重复覆盖；AdSurge同事件的摘要/链接，不作为额外独立全文抬高M；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I074 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I076 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I077 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | Wooga设计访谈仅snippet，无法核实AI具体新用法；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I078 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | D2C访谈会议信息仅snippet，不是本期新平台政策；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I079 | merge | industry_news | 事件2×相关3+钩子1 = 7 | 同一主体/产品、同一日期、同一事件的重复覆盖；与S0084同URL停服摘要，不重复计来源或增加M；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I085 | merge | industry_news | 事件3×相关2+钩子1 = 7 | 同一主体/产品、同一日期、同一事件的重复覆盖；Xbox Labs同事件但snippet，不另计多源或重复正文；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I086 | exclude | industry_news | 事件2×相关0+钩子1 = 1 | 区域主机订阅目录无迁移点，且snippet；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I087 | merge | industry_news | 事件2×相关2+钩子1 = 5 | 同一主体/产品、同一日期、同一事件的重复覆盖；RedLynx关闭同事件的snippet，不额外补写；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I088 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I089 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | Rockstar开发周期言论为战略表态且snippet；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I090 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | ESRB评级不等于跨平台正式官宣，且snippet；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I091 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I092 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I093 | merge | ai_trends | 事件3×相关2+钩子1 = 7 | 同一主体/产品、同一日期、同一事件的重复覆盖；同一EGS预览客户端仅snippet，由完整S0166进入AI；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I094 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I098 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I099 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I100 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 付费解锁包是普通运营变化；玩家争议只有snippet无法满足社区证据门槛；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I101 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I102 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | Rockstar制作周期表态，snippet不可扩展成研发新状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I103 | merge | industry_news | 事件3×相关2+钩子1 = 7 | 同一主体/产品、同一日期、同一事件的重复覆盖；Xbox Labs同事件snippet，由两个完整来源承接；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I104 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I105 | merge | industry_news | 事件1×相关2+钩子1 = 3 | 同一主体/产品、同一日期、同一事件的重复覆盖；洛杉矶工作室旧NPC生产经历，不是本期组织新增；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I106 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | GTA6规模与费用传闻仅snippet，缺可核验动作；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I107 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I108 | exclude | industry_news | 事件2×相关2+钩子0 = 4 | GTA6既有延期回顾，无本期新延期；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I109 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I110 | exclude | industry_news | 事件1×相关2+钩子0 = 2 | GTA6旧制作规模回顾，snippet不足；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I111 | exclude | industry_news | 事件2×相关2+钩子1 = 5 | GTA6泄露传闻只有snippet，无可用正文和官方状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I112 | merge | industry_news | 事件2×相关2+钩子1 = 5 | 同一主体/产品、同一日期、同一事件的重复覆盖；育碧调整snippet且人数口径不同，依据完整61/83，不借此抬R；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I113 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I114 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I115 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I117 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I119 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I120 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I121 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I122 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I123 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I127 | exclude | industry_news | 事件2×相关1+钩子1 = 3 | 舞力全开NS2未来移植，迁移点弱R1，非当前新上线；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I128 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I129 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I130 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I131 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I132 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I134 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I136 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | GTA6当地宣传/地标讨论，非本期资本或政策动作；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I137 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I138 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I139 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I140 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I141 | exclude | industry_news | 事件3×相关3+钩子0 = 9 | 综合稿按10月5至11日回顾，多款首曝已在旧窗口发生；下列产品另列子候选，不能日期回填14日；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I142 | exclude | industry_news | 事件1×相关3+钩子0 = 3 | 综合推荐稿，本期不证明多产品首次官宣；Demo与定档子事件另列；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I143 | exclude | industry_news | 事件3×相关3+钩子0 = 9 | 再再启程10月9日官宣10月23日EA；非14日新首曝，不回填为本日上线；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I145 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I146 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I147 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I148 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I149 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I150 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I151 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I153 | exclude | industry_news | 事件0×相关3+钩子1 = 1 | 魔兽测试玩法体验不是新品首次测试；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I155 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I156 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I157 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I158 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I159 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I160 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | HelixSR属于非官方超分工具体验，没有明确本期首次发布，非官方兼容与轻微帧率代价不写成主流AI重大进展；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I161 | exclude | industry_news | 事件1×相关3+钩子1 = 4 | 巧克力游戏设计意向只有导航/标题，无有效正文；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I162 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I163 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I164 | exclude | industry_news | 事件1×相关2+钩子1 = 3 | Rockstar旧NPC生产经历不是新设组织；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I168 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I171 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I172 | exclude | industry_news | 事件0×相关1+钩子1 = 1 | 逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I174 | exclude | industry_news | 事件0×相关0+钩子0 = 0 | 非游戏行业事件，人物娱乐/通用科技/影视内容；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I141M | exclude | industry_news | 事件3×相关3+钩子0 = 9 | Triple-I首次曝光在10月9日旧窗口；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I141E | exclude | industry_news | 事件3×相关2+钩子0 = 6 | 已有10月9日展示会首曝，不能把14日回顾当新立项；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I141G | exclude | industry_news | 事件3×相关3+钩子0 = 9 | 既有RPG首曝旧窗口；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I141U | exclude | industry_news | 事件3×相关3+钩子0 = 9 | IP权利收回消息在旧窗口，不用回顾稿再造14日动作；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I142J | exclude | industry_news | 事件2×相关3+钩子0 = 6 | 公布11月12日EA时间的单源推荐条目，非正式新品上线；无新鲜度钩子总分6，留日历单源审计；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I142L | exclude | industry_news | 事件3×相关3+钩子0 = 9 | 仅描述已存在Demo，未证明14日首次测试；不把当前推荐当首次测试；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I142D | exclude | industry_news | 事件3×相关3+钩子0 = 9 | Demo存在信号但未证明本日首次测试，单源不足；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| I142A | exclude | industry_news | 事件1×相关3+钩子0 = 3 | 只有开发日记推荐摘要，无法提取可验证本期AI发布状态；{"history_match": false, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": null} |
| A028 | exclude | ai_trends | direct_application | 10月13日报已写同一项目与AI优先开发，14日换源补背景无新状态。 |
| A188 | exclude | ai_trends | transferable_frontier | 完整技术证据可迁移高并发NPC推理，但本期无游戏部署证据，较直接游戏应用及前沿交互优先级低，不以技术细节堆满日报。 |
| A189 | exclude | ai_trends | transferable_frontier | 技术文档一致性审阅可迁移，但属于较间接设计文档工具；本期优先游戏直接应用与明确新交互/资产处理变化。 |
| A192 | exclude | ai_trends | transferable_frontier | 维护工作流案例可迁移但非新游戏业务落地，优先级低于本期游戏公司管线与公开新能力；不复用通用案例当游戏实绩。 |
| A193 | exclude | ai_trends | transferable_frontier | 优化方法可迁移，但单一Qwen训练配置的6倍结果不是通用游戏效率变化，技术教程不因倍数高自动入选。 |
| A182 | exclude | ai_trends | transferable_frontier | 办公室窃听调查，不是游戏采用或可验证迁移能力变化 |
| A183 | exclude | ai_trends | transferable_frontier | 榜单名次与新旧模型比较，未证明游戏环节新能力，不因跑分热度收录 |
| A184 | exclude | ai_trends | transferable_frontier | 通用IDE安全补丁披露，没有本期游戏业务后果；不扩写为游戏事故 |
| A185 | exclude | ai_trends | transferable_frontier | 实测只有摘要式聚合页，且不作与发布同一事件的独立新闻 |
| A186 | exclude | ai_trends | transferable_frontier | 一般基础设施融资，无明确新增游戏迁移能力，融资规模不替代门槛 |
| A190 | merge | ai_trends | transferable_frontier | 同一主体/产品、同一日期、同一事件的重复覆盖；正文只有外链与导读，没有实测全文，不能采用作者结论 |
| A191 | exclude | ai_trends | transferable_frontier | Chrome漏洞赏金与通用安全研究，没有具体游戏迁移链条 |
| A194 | exclude | ai_trends | transferable_frontier | 增长工具导语截断，缺广告执行边界与游戏案例，不编写投放能力 |
| A195 | exclude | ai_trends | transferable_frontier | 天气预报研究，没有游戏研发或产品的明确迁移路径 |
| A196 | exclude | ai_trends | transferable_frontier | UEFN培训推广不等于AI采用事件 |
| C230 | include | community_discourse | - | 本窗口新触发、明确游戏归属、两方解释与跟进可读；按硬上限只选两条 |
| C231 | include | community_discourse | - | 本窗口新触发、明确游戏归属、两方解释与跟进可读；按硬上限只选两条 |
| C216 | exclude | community_discourse | - | 2024年日常水楼，非事件 |
| C217 | exclude | community_discourse | - | 旧明日方舟AI文字争议；14日摘录已漂移到其他游戏，不能混写 |
| C218 | exclude | community_discourse | - | 9月旧争议延续，未定位本日实质进展 |
| C219 | exclude | community_discourse | - | 纯网吧榜单讨论，不以热度作为事件 |
| C220 | exclude | community_discourse | - | Steam档期旧帖，14日主要阵营争吵，无可取证新官方变化 |
| C221 | exclude | community_discourse | - | 此前已写歌词争议，窗口内无实质新进展 |
| C222 | exclude | community_discourse | - | Mod帖首发12日，主体不明且靠猜公司，不与230硬并 |
| C223 | exclude | community_discourse | - | 9月代码争议旧帖，14日回复无新官方材料 |
| C224 | exclude | community_discourse | - | 用户估算日活旧帖，不写成官方420万 |
| C225 | exclude | community_discourse | - | 诡秘聚会旧争议已写，无本期新进展 |
| C226 | exclude | community_discourse | - | AI复活传闻旧帖，缺可核验新产品动作 |
| C227 | exclude | community_discourse | - | 错别字与删帖猜测，缺清晰新产品/业务触发 |
| C228 | exclude | community_discourse | - | 库洛投资事实已行业收录，不同栏重复事件 |
| C229 | exclude | community_discourse | - | 10月4日AI美术旧帖，无14日新动作 |
| C232 | exclude | community_discourse | - | 艾希众筹旧节点继续争论，无本期新状态 |
| C233 | exclude | community_discourse | - | 普通联动及日常玩笑，非实质舆论事件 |
| C234 | exclude | community_discourse | - | 成人二创控制传闻主体和证据不清，且最新回复越窗 |
| C235 | exclude | community_discourse | - | 暗区少女前线普通联动旧帖，无本期实质进展 |
| D236 | include | deep_analysis | {"relevance": 3, "insight": 3, "evidence": 3, "card": 3, "total": 12} | 优先配置的GameDiscoverCo原始分析，含数据、多个独立机制与边界；不复述行业已写Survival Log，不将三七普通报道拔高为深度 |
| release-candidate-002 | include | release_calendar | {"event": 3, "source": 4, "company": 0, "total": 12} | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | exclude | release_calendar | {"event": 3, "source": 2, "company": 3, "total": 9} | Disney Solitaire是融资稿中的历史案例，无本日上线 |
| release-candidate-004 | exclude | release_calendar | {"event": 3, "source": 2, "company": 3, "total": 9} | 5800万DAU公告不是上线 |
| release-candidate-005 | exclude | release_calendar | {"event": 3, "source": 2, "company": 3, "total": 9} | 正文只写约8月上线，不能回填采集日期 |
| release-candidate-006 | exclude | release_calendar | {"event": 3, "source": 2, "company": 3, "total": 9} | 扶摇一梦明确2023年11月上线，历史背景 |
| release-candidate-013 | exclude | release_calendar | {"event": 3, "source": 3, "company": 0, "total": 9} | 只有“现已”等状态、缺实际事件日期；不补成14日。行业已采用的新品不跨栏重复 |
| release-candidate-001 | exclude | release_calendar | {"event": 3, "source": 3, "company": 0, "total": 9} | 只有“现已”等状态、缺实际事件日期；不补成14日。行业已采用的新品不跨栏重复 |
| release-candidate-007 | exclude | release_calendar | {"event": 2, "source": 2, "company": 3, "total": 7} | 11月是DLSS技术计划而非新游测试 |
| release-candidate-008 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | GTA6 PC版是2027Q1传闻，不是本期上线 |
| release-candidate-009 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 疯狂出租车只是地图详情，不是新品上线 |
| release-candidate-010 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-011 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-012 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-014 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-016 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 事件日期不在报告窗口 |
| release-candidate-018 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 影之刃零是后续试玩/PV与既有10月29日档期 |
| release-candidate-019 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 山寨案例为历史市场背景 |
| release-candidate-020 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 旧产品背景，非本日新游 |
| release-candidate-021 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 流放者柯南仅旧业务背景 |
| release-candidate-023 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 王者万象棋已经上线一月，14日是表现报道 |
| release-manual-057 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | Demo已存在，未证明窗口内首次测试 |
| release-manual-058 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 只有现已Demo，实际事件日未知 |
| release-manual-059 | exclude | release_calendar | {"event": 3, "source": 2, "company": 0, "total": 6} | 最近招募无具体日，且单源 |
| release-candidate-024 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 堡垒之夜在旧项目稿中不是新品定档 |
| release-candidate-026 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 一千克拉女王是2020年12月旧背景 |
| release-candidate-027 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 那个游戏6是硬件配色文章梗，不是产品定档 |
| release-candidate-028 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 绝地潜兵战债为普通运营内容 |
| release-candidate-029 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 芭比是影视旧片，不是新游戏 |
| release-candidate-030 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | GTA3是旧封面设计回顾，不是当期定档 |
| release-candidate-031 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 单源不具备正文资格 |
| release-manual-055 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 预购开启没有首次定档证据，亦单源 |
| release-manual-056 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 推荐稿明确11月12日EA但单源 |
| release-manual-064 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 首次曝光在10月9日，旧窗口 |
| release-manual-065 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 旧窗口展示会首曝 |
| release-manual-066 | exclude | release_calendar | {"event": 2, "source": 2, "company": 0, "total": 4} | 旧窗口首曝 |
| release-candidate-032 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | {"event": 3, "source": 1, "company": 0, "total": 3} | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | {"event": 1, "source": 3, "company": 0, "total": 3} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-037 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源不具备正文资格 |
| release-manual-045 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-046 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-047 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-048 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-049 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-050 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-051 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-052 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-manual-053 | exclude | release_calendar | {"event": 2, "source": 1, "company": 0, "total": 2} | 单源，留审计不发布 |
| release-candidate-040 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-041 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 无法确认实际发生日，或仅标题式导语；不将采集日期当事件日 |
| release-candidate-042 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 事件日期不在报告窗口 |
| release-candidate-022 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 同产品别名合并至release-candidate-015；不是新品正式发售 |
| release-candidate-043 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 事件日期不在报告窗口 |
| release-candidate-044 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 事件日期不在报告窗口 |
| release-manual-054 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 单源试玩；不等同新品首发 |
| release-manual-060 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 单源跨平台业务稿，无明确实际迁移日 |
| release-manual-061 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 单源且原事件已被行业汇总，不跨栏重复 |
| release-manual-062 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 单源，无明确实际迁移日 |
| release-manual-063 | exclude | release_calendar | {"event": 1, "source": 2, "company": 0, "total": 2} | 单源，无明确实际迁移日 |
