# Selection Decisions

- 维度覆盖自检：国内移动 12 张 / 国产产品与人才 7 张 / 市场数据 8 张 / 并购 5 张 / 平台政策 6 张 / 档期变动 9 张 / 资本组织 8 张 / 海外重大 13 张。
- 输入注意：S0034 正文为空，22 条 snippet/short 记录禁止作为最终正文证据。
- 产品日历按规范化产品名+2026-07-22 聚类；同日测试、预下载、预约和首发标签不拆节点。
- 产品日历漏挂反查：已扫描 industry_news 全部上线、定档、首曝与测试信号；符合范围者已进入 release_calendar_audit.json，单源或非首次宣传均显式 exclude。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 事件3×相关3+钩子1 = 10；国内头部厂商海外休闲手游并购传闻，需明确归因，达到阈值 |
| I002 | include | industry_news | 事件3×相关3+钩子1 = 10；中国小游戏生态获得韩国平台级分发通道，达到阈值 |
| I003 | include | industry_news | 事件3×相关3+钩子1 = 10；国内厂商在研竞技射击项目曝光，达到阈值 |
| I004 | include | industry_news | 事件3×相关3+钩子1 = 10；国内厂商在研大DAU竞技手游公开，达到阈值 |
| I005 | include | industry_news | 事件3×相关3+钩子1 = 10；国产在研RPG进入公开试玩节点，达到阈值 |
| I006 | include | industry_news | 事件3×相关3+钩子1 = 10；Savvy体系主体的区域核心管理任命，达到阈值 |
| I007 | include | industry_news | 事件3×相关2+钩子2 = 8；被关停移动工作室重新取得独立所有权，多源同事件达到阈值 |
| I008 | include | industry_news | 事件3×相关2+钩子2 = 8；多个项目取消造成重大减值并收缩数字投资，符合财报异常例外 |
| I009 | include | industry_news | 事件2×相关3+钩子1 = 7；中国移动游戏大盘与小游戏结构数据，达到阈值 |
| I010 | include | industry_news | 事件2×相关3+钩子1 = 7；中国小游戏买量规模和供给密度数据，达到阈值 |
| I011 | include | industry_news | 事件2×相关3+钩子1 = 7；国内小游戏新品成绩与团队方法论，达到阈值 |
| I012 | include | industry_news | 事件2×相关3+钩子1 = 7；国内竞技手游与头部厂商数据，达到阈值 |
| I013 | include | industry_news | 事件2×相关3+钩子1 = 7；中国移动团队产品成绩与投放结构数据，达到阈值 |
| I014 | include | industry_news | 事件2×相关3+钩子1 = 7；PVP竞技移动产品首月商业化数据，达到阈值 |
| I015 | include | industry_news | 事件3×相关2+钩子1 = 7；游戏发行商D2C基础设施融资，存在明确渠道迁移点 |
| I016 | include | industry_news | 事件3×相关2+钩子1 = 7；全球平台组织重构与核心管理任命，达到阈值 |
| I017 | include | industry_news | 事件3×相关2+钩子2 = 8；平台核心工程管理变动，多源同事件达到阈值 |
| I018 | include | industry_news | 事件3×相关2+钩子1 = 7；移动游戏数据服务商并购带来情报工具格局迁移，达到阈值 |
| B001 | exclude | industry_news | 事件2×相关2+钩子2 = 6；E2×R2+M2=6，平台能力扩展但对优先市场迁移不足 |
| B002 | exclude | industry_news | 事件2×相关2+钩子2 = 6；E2×R2+M2=6，多源为同稿转载且偏营销方案 |
| B003 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，全球融资大盘有迁移价值但低于阈值 |
| B004 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，区域案例迁移点明确但低于阈值 |
| B005 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，且同一数据已在上一期使用，无新事件 |
| B006 | exclude | industry_news | 事件2×相关2+钩子1 = 5；E2×R2+M1=5，发行工具信号低于阈值 |
| X001 | exclude | excluded_batch | E=0或E1，例行宣传、老品活动、非核心事件，不逐条扩写 |
| X002 | exclude | excluded_batch | E0–2且R0–1，未达到阈值 |
| X003 | exclude | excluded_batch | 多数E=0；22条非完整正文也禁止作为最终证据 |
| X004 | exclude | excluded_batch | E0–2且R0–1，或无游戏迁移链条，未达到阈值 |
| A001 | include | ai_trends | 直接呈现AI在游戏研发、发行与商业表现中的应用结构 |
| A002 | include | ai_trends | AI已直接用于游戏原型生成、创作与分发 |
| A003 | include | ai_trends | AI直接构成玩法与运营成本，且有产品留存和付费调整证据 |
| A004 | exclude | ai_trends | 同一Unity 7事件已在上一期正文使用，本窗口无实质新进展 |
| A005 | exclude | ai_trends | 迁移到3D资产管线的路径成立，但游戏直接性弱于入选项 |
| A006 | exclude | ai_trends | 仅有摘要，且未证明已直接进入游戏业务 |
| A007 | exclude | ai_trends | 仅有二次摘要，游戏场景迁移证据不足 |
| A008 | exclude | ai_trends | 未落到具体游戏环节，或无法形成受来源支持的迁移链条 |
| Q001 | include | community_discourse | 当日有明确触发、玩家争议逻辑和后续节点 |
| Q002 | include | community_discourse | 当日新事件，审核链条与职业规范争议清晰 |
| Q003 | exclude | community_discourse | 上一期已报道同一调整，窗口内无新的官方进展 |
| Q004 | exclude | community_discourse | 7月13日旧帖，窗口内仅零散续回复且争议依据薄弱 |
| Q005 | exclude | community_discourse | 缺少窗口内实质新进展、事实链不足或无法归纳为合格事件 |
| D001 | include | deep_analysis | R3/I3/E3/C3=12；国内移动市场三组证据共同支持完整机制链 |
| D002 | exclude | deep_analysis | R1/I3/E3/C2=9；证据完整但偏海外PC，低于本期国内移动主题优先级 |
| D003 | exclude | deep_analysis | R2/I2/E3/C2=9；同一并购事件已进入行业新闻，避免跨栏重复 |
| release-candidate-012 | include | release_calendar | 事件3×来源4=12；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-001 | include | release_calendar | 事件3×来源3=9；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-009 | include | release_calendar | 事件3×来源2=6；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-010 | include | release_calendar | 事件3×来源2=6；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-002 | include | release_calendar | 事件3×来源2=6；多源候选按事件类型×来源强度排序进入报告上限 |
| release-candidate-003 | exclude | release_calendar | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-004 | exclude | release_calendar | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-005 | exclude | release_calendar | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-006 | exclude | release_calendar | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | 事件3×来源2=6；单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | 事件2×来源2=4；单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-023 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-041 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-043 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-046 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-047 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-048 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-049 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-050 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-051 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-052 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-053 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-054 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-055 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-056 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-057 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-058 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-059 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-060 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-061 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-062 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-063 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-064 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-065 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-066 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-067 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-068 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-069 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-070 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-071 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-072 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-073 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-074 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-075 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-076 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-077 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-078 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-079 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
| release-candidate-080 | exclude | release_calendar | 事件3×来源1=3；单源不具备正文资格 |
