# 筛选决策

- 维度覆盖自检: industry_news 163 条 / release_calendar 106 条 / ai_news 0 条 / community 0 条 / deep_observation 0 条。
- 产品日历漏挂反查: 已扫描 industry_news 与 release_calendar 全量输入；补入《漫威斗魂》三日公开测试多源节点，完成同名/别名聚类并运行 sync_release_decisions.py；所有召回节点均有 include/exclude。
- AI反扫: 已扫描全部行业候选，直接作用类优先转入AI新闻。
- 双周去重门禁: 行业候选逐条记录 history_check；repeat_only 一律排除，material_update 仅以本期新增事实入选。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| industry-001 | include | 行业新闻 | 事件3×相关3+钩子1 = 10；Garena与角川共同投资的全球跨媒体战略动作；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-002 | include | 行业新闻 | 事件2×相关3+钩子1 = 7；直接影响11家中国游戏公司的韩国发行合规；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-003 | include | 行业新闻 | 事件2×相关3+钩子1 = 7；国产移动RPG进入新的半年数据报告期；history_match=true；novelty=material_update；prior=H039｜鹰角《终末地》「向渊行」版本 + 反常规设计｜weekly 2026-07-10_to_2026-07-16；new_facts=移动端上线六个月累计收入估算为1.267亿美元；日本贡献41%、中国贡献28%；第六个月收入环比增长72% |
| industry-004 | include | 行业新闻 | 事件2×相关3+钩子1 = 7；中国游戏细分市场与用户结构数据；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-005 | include | 行业新闻 | 事件2×相关3+钩子1 = 7；国产单机产品新增全球用户里程碑；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-006 | include | 行业新闻 | 事件2×相关3+钩子1 = 7；国内社交竞技产品披露用户与内容增长机制；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-007 | include | 行业新闻 | 事件2×相关3+钩子1 = 7；中国社交平台成为海外独游低成本获客渠道；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-008 | include | 行业新闻 | 事件3×相关2+钩子1 = 7；全球PC分发与在线服务平台的核心管理层变动；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-009 | include | 行业新闻 | 事件3×相关2+钩子1 = 7；新游戏引擎团队试图挑战双寡头并原生适配智能体工具；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-repeat-001 | exclude | 行业新闻 | 事件2×相关3+钩子1 = 7；历史报告已披露同一14亿元事实，本期仅换来源和补背景；history_match=true；novelty=repeat_only；prior=H005｜完美世界《异环》流水超14亿，H1却预亏至少8000万｜daily 2026-07-14；H029｜完美世界《异环》Q2流水超14亿｜weekly 2026-07-10_to_2026-07-16；new_facts=无 |
| industry-boundary-001 | exclude | 行业新闻 | 事件2×相关2+钩子2 = 6；官方解释是新增事实，但总分6未达日报阈值；且上一期社区已覆盖同一中断；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-002 | exclude | 行业新闻 | 事件3×相关1+钩子2 = 5；海外管理层变动缺少国内、移动或全球格局迁移点；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-003 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；全球组织数据具结构性但总分5未达线；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-004 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；移动竞技诉讼判决具事实变化但相关性总分5未达线；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-005 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；UGC平台发现与创作入口变化总分5未达线；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-006 | exclude | 行业新闻 | 事件3×相关2+钩子0 = 6；来源未提供本期新日期或新交易状态，缺少新鲜度钩子；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-007 | exclude | 行业新闻 | 事件3×相关1+钩子2 = 5；海外IP影视合作缺少明确移动或中国市场迁移点；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-boundary-008 | exclude | 行业新闻 | 事件2×相关1+钩子2 = 4；常规财报且未证明相对指引的异常，财报例外不成立；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| ai-001 | include | AI新闻 | AI Agent已进入游戏工程、测试与发行链路 |
| ai-002 | include | AI新闻 | 来源给出已落地的制作、买量、客服与运营环节 |
| ai-003 | include | AI新闻 | AI陪伴产品发生明确生命周期状态变化 |
| ai-exclude-001 | exclude | AI新闻 | 直接应用成立，但证据仍处小范围beta，优先级低于本期三条 |
| ai-exclude-002 | exclude | AI新闻 | 聚合招聘线索混合多个主体，未形成一个可独立核验的产品事件 |
| ai-raw-0164 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0165 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0166 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0167 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0168 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0169 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0170 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0171 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0172 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0173 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0174 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0175 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| ai-raw-0176 | exclude | AI新闻 | 未落到具体游戏业务，或仅能形成弱迁移链条，不用于凑数 |
| community-001 | include | 玩家舆论 | 同一抽卡机制变更在7月28日出现官方后续方案，玩家围绕双UP成本继续分歧 |
| community-raw-0284 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0285 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0286 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0287 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0288 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0289 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0291 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0292 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0293 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0294 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0295 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0296 | exclude | 玩家舆论 | 2024年旧帖仅被挖起，本期无新的诉讼或事件状态 |
| community-raw-0297 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0298 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0299 | exclude | 玩家舆论 | 玩家称游戏与官网无法访问，但缺少官方状态确认，保留候选不写成停运事实 |
| community-raw-0301 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0302 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0303 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0304 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0305 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0306 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0309 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0310 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0311 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0312 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0313 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0314 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0315 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| community-raw-0316 | exclude | 玩家舆论 | 未形成报告日可核验的新事件，或属于泛讨论、旧帖延续、弱争议与跨栏重复 |
| deep-001 | include | 深度观察 | relevance=2/insight=3/evidence=3/card=3/total=11；单篇高质量访谈完整支持增长、组织缓冲与第二产品孵化机制 |
| deep-exclude-001 | exclude | 深度观察 | relevance=0/insight=1/evidence=1/card=1/total=3；非游戏行业，且正文仅有摘要 |
| industry-raw-0002 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0004 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0005 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0006 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0007 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0008 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0009 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0010 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；平台或分发变化具迁移点，但总分5未达日报阈值；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0011 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0012 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0015 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0019 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0023 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0025 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0026 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0029 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0030 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0032 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0035 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0036 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0037 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0038 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0039 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0040 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0041 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0043 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0046 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0049 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0051 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0053 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0055 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0057 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0058 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；平台监管讨论未提供可独立采纳的新决定，总分5；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0059 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0061 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0066 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0069 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0070 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0072 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0073 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0075 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0077 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0078 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0079 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0082 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0084 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0085 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0086 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0088 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0089 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0091 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0094 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0095 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0096 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0097 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0099 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0100 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0101 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0102 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0105 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0107 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0110 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0111 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0112 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；平台或分发变化具迁移点，但总分5未达日报阈值；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0114 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0115 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0116 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0117 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0118 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0119 | exclude | 行业新闻 | 事件2×相关2+钩子0 = 4；5月发布的趋势报告被本期重新收录，无新鲜度钩子；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0120 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0123 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0124 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0126 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0127 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0130 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0131 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0132 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0133 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0134 | exclude | 行业新闻 | 事件2×相关2+钩子1 = 5；平台或分发变化具迁移点，但总分5未达日报阈值；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0135 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0136 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0138 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0141 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0142 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0144 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0145 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0146 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0147 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0148 | exclude | 行业新闻 | 事件1×相关1+钩子1 = 2；芯片走私执法与游戏行业迁移链条不足；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0149 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0150 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0151 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0152 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0153 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0154 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0155 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0156 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0157 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0159 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-raw-0163 | exclude | 行业新闻 | 事件0×相关0+钩子0 = 0；评测、攻略、例行宣传、普通版本/活动、硬件或非游戏内容，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-myst | exclude | 行业新闻 | 事件3×相关1+钩子2 = 5；海外在研项目有多源确认，但相关性总分5未达线；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-stillfront | exclude | 行业新闻 | 事件2×相关2+钩子2 = 6；常规季度数据，财报例外不成立；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-ubisoft | exclude | 行业新闻 | 事件2×相关2+钩子2 = 6；跨平台权益变化总分6未达日报阈值；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-pokemon-face | exclude | 行业新闻 | 事件2×相关1+钩子2 = 4；区域零售防黄牛措施缺少游戏产业迁移点；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-gog-linux | exclude | 行业新闻 | 事件2×相关2+钩子2 = 6；PC分发平台能力变化总分6未达日报阈值；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-chaoxi-chinajoy | exclude | 行业新闻 | 事件0×相关3+钩子2 = 2；展会阵容与例行宣传，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-nioh-dlc | exclude | 行业新闻 | 事件0×相关1+钩子2 = 2；老品普通DLC与宣传视频，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| industry-cluster-spiderman-update | exclude | 行业新闻 | 事件0×相关1+钩子2 = 2；老品普通免费更新，E=0；history_match=false；novelty=new_event；prior=无；new_facts=无 |
| release-manual-005 | include | 产品日历 | 事件类型3×来源强度4 = 12；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-001 | include | 产品日历 | 事件类型3×来源强度3 = 9；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-014 | include | 产品日历 | 事件类型3×来源强度3 = 9；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-015 | include | 产品日历 | 事件类型3×来源强度2 = 6；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-075 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；超过本报告产品日历条数上限 |
| release-candidate-016 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；超过本报告产品日历条数上限 |
| release-candidate-002 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-candidate-003 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-candidate-005 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-candidate-006 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-candidate-007 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-candidate-008 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-manual-002 | exclude | 产品日历 | 事件类型3×来源强度2 = 6；单源不具备正文资格 |
| release-candidate-083 | exclude | 产品日历 | 事件类型2×来源强度2 = 4；超过本报告产品日历条数上限 |
| release-candidate-009 | exclude | 产品日历 | 事件类型2×来源强度2 = 4；单源不具备正文资格 |
| release-manual-003 | exclude | 产品日历 | 事件类型2×来源强度2 = 4；单源不具备正文资格 |
| release-candidate-010 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-011 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-012 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-013 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-017 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-018 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-019 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-020 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-021 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-022 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-023 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-024 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-025 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-026 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-027 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-028 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-029 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-030 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-031 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-032 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-033 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-034 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-035 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-036 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-037 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-038 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-039 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-040 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-041 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-042 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-043 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-044 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-045 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-046 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-047 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-048 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-049 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-050 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-051 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-052 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-053 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-054 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-055 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-056 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-057 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-058 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-059 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-060 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-061 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-062 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-063 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-064 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-065 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-066 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-067 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-068 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-069 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-070 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-071 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-072 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-073 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-074 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-076 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-077 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-078 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-079 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-candidate-080 | exclude | 产品日历 | 事件类型3×来源强度1 = 3；单源不具备正文资格 |
| release-manual-001 | exclude | 产品日历 | 事件类型1×来源强度3 = 3；超过本报告产品日历条数上限 |
| release-candidate-081 | exclude | 产品日历 | 事件类型2×来源强度1 = 2；单源不具备正文资格 |
| release-candidate-084 | exclude | 产品日历 | 事件类型2×来源强度1 = 2；单源不具备正文资格 |
| release-manual-004 | exclude | 产品日历 | 事件类型1×来源强度1 = 1；单源不具备正文资格 |
