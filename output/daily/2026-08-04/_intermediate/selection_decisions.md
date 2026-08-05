# Selection Decisions

- 维度覆盖自检：国内移动/国产产品与人才 12 张；市场数据 7 张；并购 4 张；平台政策 3 张；档期变动 5 张；资本组织 7 张；海外重大 8 张。
- 双周历史窗口：2026-07-21 至 2026-08-03，共96条已发布行业条目。
- 行业门槛：E×R+M>=7；双周repeat_only门禁优先于评分。
- 产品日历漏挂反查：已反扫industry_news与release_calendar全部上线/定档/测试/首曝信号；补入《阴阳师：云图》《Palworld Online》《Crownstone Survival》《Caliber》《朵拉的环球旅行》《Tennis Tycoon》，并由确定性脚本完成include/exclude。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 国产重点项目团队补齐发行负责人；事件3×相关3+钩子2=11；history=new_event；prior=0；new_facts=1 |
| I002 | exclude | industry_news | 事件3×相关3+钩子2=11，但同一事件交由产品日历呈现，避免跨栏重复；history=new_event；prior=0；new_facts=2 |
| I003 | include | industry_news | 国内游戏公司资本动作；事件3×相关3+钩子1=10；history=new_event；prior=0；new_facts=2 |
| I004 | include | industry_news | 国产女性向休闲新品进入测试前阶段；事件3×相关3+钩子1=10；history=new_event；prior=0；new_facts=2 |
| I005 | include | industry_news | 腾讯海外发行品牌切入休闲SLG新品；事件3×相关3+钩子1=10；history=new_event；prior=0；new_facts=2 |
| I006 | include | industry_news | 海外竞技产品经本地伙伴合规进入中国；事件3×相关3+钩子1=10；history=new_event；prior=0；new_facts=2 |
| I007 | include | industry_news | 移动优先赛道新报告期数据且双源覆盖；事件2×相关3+钩子2=8；history=new_event；prior=0；new_facts=3 |
| I008 | include | industry_news | 移动市场与腾讯、Garena竞争格局；事件2×相关3+钩子1=7；history=new_event；prior=0；new_facts=2 |
| I009 | include | industry_news | 移动商业化渠道结构新数据；事件2×相关3+钩子1=7；history=new_event；prior=0；new_facts=2 |
| I010 | include | industry_news | 中国手游出海渠道新报告期数据；事件2×相关3+钩子1=7；history=new_event；prior=0；new_facts=2 |
| I010M | merge into I010 | industry_news | 同正文哈希的重复采集，合并至I010；history=new_event；prior=0；new_facts=1 |
| I011 | include | industry_news | 国内移动UGC平台发布开发者激励政策；事件2×相关3+钩子1=7；history=new_event；prior=0；new_facts=3 |
| I012 | include | industry_news | PVP优先赛道关键产品数据；事件2×相关3+钩子1=7；history=new_event；prior=0；new_facts=2 |
| I013 | include | industry_news | 移动游戏集团调整3亿美元级交易结构；事件3×相关2+钩子1=7；history=new_event；prior=0；new_facts=2 |
| I014 | include | industry_news | 移动游戏集团核心管理层变动；事件3×相关2+钩子1=7；history=new_event；prior=0；new_facts=2 |
| IX001 | exclude | industry_news | 事件3×相关3+钩子2=11，但8月3日日报产品日历已发布，新增报道仅补充玩法与来源数量；history=repeat_only；prior=1；new_facts=0 |
| IX002 | exclude | industry_news | 事件3×相关2+钩子2=8，但仍是预计完成，未出现相对昨日的官方成交状态变化；history=repeat_only；prior=1；new_facts=0 |
| IX003 | exclude | industry_news | 事件3×相关3+钩子1=10，但为昨日同一事实的晚到转载；history=repeat_only；prior=1；new_facts=0 |
| IX004 | exclude | industry_news | 事件2×相关3+钩子2=8，但昨日已发布，新增来源没有状态变化；history=repeat_only；prior=1；new_facts=0 |
| IX005 | exclude | industry_news | 事件3×相关3+钩子1=10，但昨日已发布同一资本与项目状态；history=repeat_only；prior=1；new_facts=0 |
| IX006 | exclude | industry_news | 事件2×相关3+钩子1=7，但同一报告期的王者荣耀与腾讯移动收入已发布，新增榜单为补充旧背景；history=repeat_only；prior=1；new_facts=0 |
| IX007 | exclude | industry_news | 事件1×相关3+钩子1=4，且一周年用户与续作投资均已发布，访谈未带来状态变化；history=repeat_only；prior=2；new_facts=0 |
| IX008 | exclude | industry_news | 事件2×相关2+钩子1=5，东南亚迁移点明确但低于日报阈值；history=new_event；prior=0；new_facts=2 |
| IX009 | exclude | industry_news | 事件2×相关2+钩子2=6，双源但平台迁移分不足；history=new_event；prior=0；new_facts=1 |
| IX010 | exclude | industry_news | 事件2×相关2+钩子1=5，仍处于潜在认定阶段且低于阈值；history=new_event；prior=0；new_facts=1 |
| IX011 | exclude | industry_news | 事件2×相关1+钩子2=4，海外一般组织事件迁移弱；history=new_event；prior=0；new_facts=1 |
| IX012 | exclude | industry_news | 常规财报且核心利润改善受一次性会计收益影响，不满足财报例外；E=0；history=new_event；prior=0；new_facts=1 |
| A001 | include | ai_trends | AI已直接进入手游内容生产与运营成本结构 |
| A002 | include | ai_trends | 国内游戏公司披露可核验的研发管线落地 |
| A003 | include | ai_trends | AI直接进入游戏玩法、创作、资产与渲染环节 |
| AX001 | exclude | ai_trends | 案例较多但稿件为单一服务商综合宣传，优先级低于三项更聚焦的直接应用 |
| AX002 | exclude | ai_trends | 直接应用成立，但影响范围较小，排在本期三项成熟管线之后 |
| AX003 | exclude | ai_trends | 直接用于营销但事件核心是玩家争议，且不进入本期社区优先序列 |
| AX004 | exclude | ai_trends | 实时语音对NPC有迁移路径，但尚无游戏落地，弱于直接应用 |
| AX005 | exclude | ai_trends | 语音识别可迁移至游戏语音交互与运营转写，但来源未证明游戏落地 |
| C001 | include | community_discourse | 触发、受影响范围、争议逻辑与官方后续均可核验 |
| C002 | include | community_discourse | 国内手游窗口内出现明确恢复更新节点与分歧讨论 |
| CX001 | exclude | community_discourse | 原帖始于7月15日，8月4日仅有零散旧帖回复，没有可核验的新状态 |
| CX002 | exclude | community_discourse | 讨论对机制是否一次性存在冲突表述，且国内候选证据链更完整 |
| CX003 | exclude | community_discourse | 海外老品争议成立，但与本期国内社区事件相比优先级较低，不为软目标凑数 |
| CX004 | exclude | community_discourse | 核心是技术保护移除事实，玩家争议机制不够集中 |
| CX005 | exclude | community_discourse | 单帖转述且缺少可核验成交与官方后续 |
| D001 | include | deep_analysis | 单篇高质量官方市场洞察可支撑完整机制分析 |
| DX001 | exclude | deep_analysis | 当前输入只有短摘要，难以支撑两段机制分析 |
| release-candidate-025 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-003 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-026 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-004 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-006 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-007 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-008 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-023 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-024 | exclude | release_calendar | 事件日期不在报告窗口 |
