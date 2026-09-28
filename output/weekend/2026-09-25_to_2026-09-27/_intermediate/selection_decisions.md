# Selection Decisions

- 卡片曝光去重：读取历史121条的 card_exposed/card_rank/card_limit/card_exposure_source；本期历史召回项均存在 card_exposed=true 匹配，或未达到分数线，因此 card_carryover=0。
- 维度覆盖自检：国内移动/国产产品与人才 8 张；市场数据 1 张；并购 2 张；平台政策 2 张；档期变动 3 张；资本组织 5 张；海外重大 6 张；其余为E=0批量审计。
- 产品日历漏挂反查：已反扫265条 industry_news 与32条 release_calendar；27个审计节点全部为单一独立来源或窗口外，确定性同步后正文0条。
- AI反扫：已反扫全部行业候选；Meta、Hyper3D、《千夜之书1001》转入AI新闻，网易《蛋仔派对》AI 3D因事件窗口外排除。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子1 = 10；国内研发主体与Savvy体系资本动作。 |
| I002 | include | industry_news | 事件3×相关3+钩子1 = 10；腾讯移动产品公开测试节点。 |
| I003 | include | industry_news | 事件3×相关3+钩子1 = 10；Supercell产品重新进入验证阶段。 |
| I004 | include | industry_news | 事件2×相关3+钩子1 = 7；中国移动分发生态出现结构性扩张。 |
| I005 | include | industry_news | 事件3×相关2+钩子1 = 7；移动模拟品类并购与系列化扩张。 |
| I006 | exclude | - | 事件1×相关3+钩子1 = 4；属于material_update但普通宣传演示未达7分线。 |
| I007 | exclude | - | 事件2×相关3+钩子1 = 7，但事件发生于9月24日，早于本期窗口；晚到转载不纳入正文。 |
| I008 | exclude | - | 事件2×相关3+钩子1 = 7；历史匹配项已进入订阅卡片，本期无新状态，repeat_only。 |
| I009 | exclude | - | 事件2×相关3+钩子1 = 7；历史任一匹配项card_exposed=true且无新状态，repeat_only。 |
| I010 | exclude | - | 事件1×相关2+钩子1 = 3；既有重组事实已进入订阅卡片，仅新增态度表述，repeat_only。 |
| I011 | exclude | - | 事件2×相关3+钩子1 = 7；历史任一匹配项card_exposed=true，无实质新状态，repeat_only。 |
| I012 | exclude | - | 事件1×相关2+钩子0 = 2；历史匹配项已曝光且当前仅补充旧背景，repeat_only。 |
| I013 | exclude | - | 事件1×相关2+钩子2 = 4；海外一般劳资事件低于7分线。 |
| I014 | exclude | - | 事件2×相关1+钩子1 = 3；海外单一工作室事件迁移点弱。 |
| I015 | exclude | - | 事件3×相关1+钩子1 = 4；海外一般管理层变动低于7分线。 |
| I016 | exclude | - | 事件3×相关1+钩子1 = 4；实验性海外小工作室信号低于7分线。 |
| I017 | exclude | - | 事件2×相关2+钩子1 = 5；专利尚未落地，低于7分线。 |
| I018 | exclude | - | 事件0×相关0+钩子0 = 0；逐条复核为普通版本/活动/宣传、评测观点、硬件影视、同源多语种重复或低相关海外事件；不进入正文。 |
| A001 | include | ai_trends | 直接作用于游戏创作、发布和分发。 |
| A002 | include | ai_trends | 直接作用于游戏3D资产生产与后续编辑。 |
| A003 | include | ai_trends | 大模型直接参与游戏角色、叙事与玩法反馈。 |
| A004 | exclude | - | 直接作用类但事件发生于9月上旬，本期为同源多语种晚到稿，无本窗口新状态。 |
| A005 | exclude | - | 通用开发安全工具，来源未提供具体游戏研发应用。 |
| A006 | exclude | - | 没有来源直接支持的具体游戏应用或清晰迁移链条。 |
| C001 | include | community_discourse | 触发、争议逻辑、时间线与后续扫描完整。 |
| C002 | exclude | - | 核心处罚与反作弊更新发生于本期窗口前，窗口内仅有零散续帖，无实质新进展。 |
| C003 | exclude | - | 同一事件已进入上一份周末报，本期没有可核验的正式方案变化，避免重复。 |
| C004 | exclude | - | 同一事件已进入上一份周末报，9月27日仅有新增回复，无新状态。 |
| C005 | exclude | - | 缺少独立事件闭环、可靠时间线或跨来源后续；不把玩家推测改写为事实。 |
| D001 | include | deep_analysis | R3/I3/E3/C3=12，移动游戏资本结构与产品经营形成完整机制链。 |
| D002 | include | deep_analysis | R2/I3/E3/C3=11，数据完整且形成品类—场景—跨平台链条。 |
| release-candidate-001 | exclude | - | 单源不具备正文资格 |
| release-candidate-002 | exclude | - | 单源不具备正文资格 |
| release-candidate-003 | exclude | - | 单源不具备正文资格 |
| release-candidate-004 | exclude | - | 单源不具备正文资格 |
| release-candidate-005 | exclude | - | 单源不具备正文资格 |
| release-candidate-006 | exclude | - | 单源不具备正文资格 |
| release-candidate-007 | exclude | - | 单源不具备正文资格 |
| release-candidate-008 | exclude | - | 单源不具备正文资格 |
| release-candidate-009 | exclude | - | 单源不具备正文资格 |
| release-candidate-010 | exclude | - | 单源不具备正文资格 |
| release-candidate-011 | exclude | - | 单源不具备正文资格 |
| release-candidate-012 | exclude | - | 单源不具备正文资格 |
| release-candidate-013 | exclude | - | 单源不具备正文资格 |
| release-candidate-014 | exclude | - | 单源不具备正文资格 |
| release-candidate-015 | exclude | - | 单源不具备正文资格 |
| release-candidate-016 | exclude | - | 单源不具备正文资格 |
| release-candidate-017 | exclude | - | 单源不具备正文资格 |
| release-candidate-018 | exclude | - | 单源不具备正文资格 |
| release-candidate-019 | exclude | - | 单源不具备正文资格 |
| release-candidate-020 | exclude | - | 单源不具备正文资格 |
| release-candidate-021 | exclude | - | 单源不具备正文资格 |
| release-candidate-022 | exclude | - | 单源不具备正文资格 |
| release-candidate-023 | exclude | - | 单源不具备正文资格 |
| release-candidate-024 | exclude | - | 单源不具备正文资格 |
| release-candidate-025 | exclude | - | 单源不具备正文资格 |
| release-candidate-026 | exclude | - | 单源不具备正文资格 |
| release-candidate-027 | exclude | - | 单源不具备正文资格 |
