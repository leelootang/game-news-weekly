# Selection Decisions

维度覆盖自检：国内移动/国产产品与人才10张/市场数据3张/并购3张/平台政策2张/档期变动3张/资本组织4张/海外重大16张
产品日历漏挂反查：已反扫industry_news与release_calendar全量输入，合并Palworld Online中英文别名，修正Plants on Fire同源转载与事件类型，并由sync_release_decisions.py确定优先级前缀。
行业历史窗口：2026-07-20_to_2026-08-02；89条既往行业新闻逐条参与history_check。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 资本关系和项目状态同时发生实质变化；事件3×相关3+钩子1 = 10；事件3×相关3+钩子1 = 10；history_match=false novelty=new_event |
| I002 | include | industry_news | 中国市场组织实体落地；事件3×相关3+钩子1 = 10；事件3×相关3+钩子1 = 10；history_match=false novelty=new_event |
| I003 | include | industry_news | 中国市场重大代理与IP生态合作；事件3×相关3+钩子1 = 10；事件3×相关3+钩子1 = 10；history_match=false novelty=new_event |
| I004 | include | industry_news | 国产策略RPG新品正式测试；事件3×相关3+钩子1 = 10；事件3×相关3+钩子1 = 10；history_match=false novelty=new_event |
| I005 | include | industry_news | 海外IP进入中国并形成正式联合发行合作；事件3×相关3+钩子1 = 10；事件3×相关3+钩子1 = 10；history_match=false novelty=new_event |
| I006 | include | industry_news | 相对既往欧盟单项批准，全部监管批准构成可验证状态变化；事件3×相关2+钩子2 = 8；事件3×相关2+钩子2 = 8；history_match=true novelty=material_update |
| I007 | include | industry_news | 全球创作者工具资产并购并有双源覆盖；事件3×相关2+钩子2 = 8；事件3×相关2+钩子2 = 8；history_match=false novelty=new_event |
| I008 | include | industry_news | 国产项目终止研发并解散团队；事件2×相关3+钩子1 = 7；事件2×相关3+钩子1 = 7；history_match=false novelty=new_event |
| I009 | include | industry_news | 移动竞技产品进入中国市场并披露国服主体；事件2×相关3+钩子1 = 7；事件2×相关3+钩子1 = 7；history_match=false novelty=new_event |
| I010 | include | industry_news | 移动RPG新报告期数据揭示首发衰减；事件2×相关3+钩子1 = 7；事件2×相关3+钩子1 = 7；history_match=false novelty=new_event |
| I011 | include | industry_news | 中国小游戏月度结构数据进入新报告期；事件2×相关3+钩子1 = 7；事件2×相关3+钩子1 = 7；history_match=false novelty=new_event |
| IX01 | exclude | industry_news | 已在7月29日日报及7月24日至30日周报发布；事件2×相关3+钩子1 = 7，但双周门禁优先；事件2×相关3+钩子1 = 7；history_match=true novelty=repeat_only |
| IX02 | exclude | industry_news | 同一报告期事实已在周报发布；事件2×相关3+钩子1 = 7，但为repeat_only；事件2×相关3+钩子1 = 7；history_match=true novelty=repeat_only |
| IX03 | exclude | industry_news | 半年DAU和流水事实已在日报及周报发布，新增内容为方法论背景；事件2×相关3+钩子1 = 7，但为repeat_only；事件2×相关3+钩子1 = 7；history_match=true novelty=repeat_only |
| IX04 | exclude | industry_news | 同一2025年市场规模事实已发布；事件2×相关3+钩子1 = 7，但为repeat_only；事件2×相关3+钩子1 = 7；history_match=true novelty=repeat_only |
| IX05 | exclude | industry_news | 同一里程碑已在日报发布；事件2×相关3+钩子1 = 7，但为repeat_only；事件2×相关3+钩子1 = 7；history_match=true novelty=repeat_only |
| IX06 | exclude | industry_news | 移动支付基础设施有迁移点，但文章所述功能6月30日已上线且当日无新状态；事件2×相关3+钩子0 = 6；事件2×相关3+钩子0 = 6；history_match=false novelty=new_event |
| IX07 | exclude | industry_news | 平台技术对移动有迁移点但未形成结构性政策或市场变化；事件2×相关2+钩子1 = 5；事件2×相关2+钩子1 = 5；history_match=false novelty=new_event |
| IX08 | exclude | industry_news | 海外硬件区域价格变化对目标业务迁移弱；事件2×相关1+钩子2 = 4；事件2×相关1+钩子2 = 4；history_match=false novelty=new_event |
| IX09 | exclude | industry_news | 老品生命周期节点但为常规周年更新；事件1×相关3+钩子1 = 4；事件1×相关3+钩子1 = 4；history_match=false novelty=new_event |
| IX10 | exclude | industry_news | 线下活动及老品榜单变化不构成独立高E事件；事件1×相关3+钩子1 = 4；事件1×相关3+钩子1 = 4；history_match=false novelty=new_event |
| A001 | include | ai_trends | 真实客户案例覆盖研发、产品与运营环节 |
| A002 | include | ai_trends | AI能力商品化压缩游戏营销工具公司的市场缺口，且双源覆盖 |
| A003 | include | ai_trends | 新模型的长视频与局部编辑能力可迁移到游戏宣发和影像资产生产 |
| AX01 | exclude | ai_trends | 同一首次试玩已进入2026-07-31至2026-08-02周末报，不重复发布 |
| AX02 | exclude | ai_trends | 企业展台汇总稿为例行展示，已选AI条目证据更具体 |
| AX03 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX04 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX05 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX06 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX07 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX08 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX09 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX10 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX11 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| AX12 | exclude | ai_trends | 无法从来源建立具体且优先级足够的游戏环节迁移链路 |
| C001 | include | community_discourse | 触发、争议逻辑和窗口内时间线完整 |
| C002 | include | community_discourse | 问卷触发明确，玩家围绕角色定制与玩法基础形成对立意见 |
| CX01 | exclude | community_discourse | 社区帖缺少可核验的官方时间线，唯一行业补充源S0101为snippet，不用于终稿 |
| CX02 | exclude | community_discourse | 仅有聊天记录转述，原因仍是玩家推测，证据链不足 |
| CX03 | exclude | community_discourse | 该事件已进入2026-07-31至2026-08-02周末报，不重复 |
| D001 | include | deep_analysis | 当前资本退出事件与高质量行业分析共同支持变化—机制—下游影响 |
| release-candidate-018 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-004 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-001 | exclude | release_calendar | 多源文本未写产品型态，无法形成满足正文契约的单产品bullet |
| release-candidate-007 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-008 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-010 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-011 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-012 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-013 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-016 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-003 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-019 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-025 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-027 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-030 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-036 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-039 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-040 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-041 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-042 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-043 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-044 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-045 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-046 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-047 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-048 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-049 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-050 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-051 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-052 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-053 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-054 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-055 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-056 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-057 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-058 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-059 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-060 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-061 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-062 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-063 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-064 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-065 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-066 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-067 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-068 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-069 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-070 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-071 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-072 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-073 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-074 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-075 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-076 | exclude | release_calendar | 事件日期不在报告窗口 |
