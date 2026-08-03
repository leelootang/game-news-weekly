# Event Candidates

维度覆盖自检：国内市场与移动产品、PC/主机、组织资本、平台生态、AI研发/产品/运营、玩家舆论、新游档期、海外IP与商业模式均已扫描。

## industry-001 - 2026年上半年中国游戏市场增长12.17%，小游戏和PC游戏成为主要增速来源
- section: industry
- source_ids: S1497
- audit: include｜E×R+M达到周报入选线

## industry-002 - 抖音小游戏DAU增长130%、流水增长140%
- section: industry
- source_ids: S1511
- audit: include｜E×R+M达到周报入选线

## industry-003 - 夏思源团队获1.66亿元投资并推进《明末》续作
- section: industry
- source_ids: S1159
- audit: include｜E×R+M达到周报入选线

## industry-004 - 光子北美工作室调整并裁员80人
- section: industry
- source_ids: S1152
- audit: merge｜与industry-010为同一工作室、同一项目、同一日期的组织调整，合并多源呈现

## industry-005 - 世纪华通四名股东因与盛趣游戏利润事项被责令改正
- section: industry
- source_ids: S1543
- audit: include｜E×R+M达到周报入选线

## industry-006 - 《终末地》上半年移动端收入超过8亿元，6月收入回暖
- section: industry
- source_ids: S1518
- audit: include｜E×R+M达到周报入选线

## industry-007 - 抖音小游戏发布仔仔Agent、AI互动空间等产品能力
- section: industry
- source_ids: S1500
- audit: merge｜与ai-005为同一发布事件，AI产品能力是更准确的栏目归属

## industry-008 - 上半年中国游戏市场、小游戏与PC端数据集中披露
- section: industry
- source_ids: S1497
- audit: merge｜与industry-001使用同一来源并描述同一份产业报告，去重合并

## industry-009 - 《QQ宠物》宣布重启并引入AI能力
- section: industry
- source_ids: S1145
- audit: include｜E×R+M达到周报入选线

## industry-010 - LightSpeed LA调整《Last Sentinel》研发方向并进行组织调整
- section: industry
- source_ids: S1152, S1179
- audit: include｜两条来源描述同一工作室、同一项目与同日调整，合并后保留

## ai-001 - TapTap发布游戏开发AI工具Cindy，并披露平台新增AI游戏情况
- section: ai
- source_ids: S0548
- audit: include｜游戏直接应用类AI事件

## ai-002 - 《妹居物语》团队披露AI原生游戏的制作流程
- section: ai
- source_ids: S0555
- audit: include｜游戏直接应用类AI事件

## ai-003 - Unity中国发布团结引擎2.0及AI智能体开发能力
- section: ai
- source_ids: S0841
- audit: include｜游戏直接应用类AI事件

## ai-004 - 网易伏羲讨论AI工具与美术研发管线的结合
- section: ai
- source_ids: S1499
- audit: include｜游戏直接应用类AI事件

## ai-005 - 抖音小游戏公布AI互动空间与仔仔Agent能力
- section: ai
- source_ids: S1500
- audit: include｜游戏直接应用类AI事件

## community-001 - 《心动小镇》相关内容引发玩家对表达立场的争议
- section: community
- source_ids: S1812
- audit: exclude｜来源未提供可核实的具体触发内容，无法建立争议逻辑与后续扫描基线

## community-002 - 《FGO》国服服务异常引发玩家对稳定性的讨论
- section: community
- source_ids: S1449
- audit: include｜具备触发、争议逻辑和窗口内讨论

## community-003 - 玩家围绕《终末地》半年收入估算及产品表现展开讨论
- section: community
- source_ids: S1448
- audit: include｜具备触发、争议逻辑和窗口内讨论

## deep-001 - Steam评价不是售后附属，而是购买漏斗中的前置门槛
- section: deep
- source_ids: S0337
- audit: include｜人工selection明确选择

## deep-002 - 《后室》揭示网络原生IP的新范式：从集中所有权转向共同体共创
- section: deep
- source_ids: S0797
- audit: include｜人工selection明确选择

## 产品日历审计

- 全量节点：424
- 窗口内多源候选：23
- 正文入选：release-candidate-001、release-candidate-002、release-candidate-003、release-candidate-004、release-candidate-005、release-candidate-006、release-candidate-007
- 排序：先判断窗口内多源资格，再按“事件类型分 × 来源强度分 + 重点公司新品加3分”降序；同分依次比较事件类型、公司加分、独立来源数、行业新闻覆盖与首次出现顺序。
- 阻断：单源、重复来源、窗口外事件、公司证据缺失、分数或正文顺序漂移均不得发布。
