# Selection Decisions

- 维度覆盖自检：国内移动/国产产品与人才 42张候选 / 市场数据 15张候选 / 并购 2张候选 / 平台政策 36张候选 / 档期变动 22张候选 / 资本组织 15张候选 / 海外重大 95张候选
- 产品日历漏挂反查：已反扫全部 industry_news 与 release_calendar；修正《雾影猎人》实际事件日为7月30日，补并《鸡械绿洲》移动端行业来源，并补挂《代号：对决》《猫仙札》节点后执行确定性前缀。
- 行业阈值：周末报总分>=7，且双周历史去重门禁优先于分数。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| industry-candidate-001 | include | industry | 事件3×相关3+钩子2 = 11；国产移动端优先英雄射击新品首次公开，多源覆盖；history=new_event |
| industry-candidate-002 | include | industry | 事件3×相关3+钩子1 = 10；国内平台与央企游戏业务的系统性战略扩张；history=new_event |
| industry-candidate-003 | include | industry | 事件2×相关3+钩子2 = 8；中国电竞市场规模、用户和产品平台结构数据，多源覆盖；history=new_event |
| industry-candidate-004 | include | industry | 事件2×相关3+钩子2 = 8；中国手游出海市场与用户价值数据，多源覆盖；history=new_event |
| industry-candidate-005 | include | industry | 事件3×相关2+钩子2 = 8；云游戏与移动/电视跨平台开发能力发生实质扩展；history=new_event |
| industry-candidate-006 | include | industry | 事件2×相关3+钩子1 = 7；相对既往上线6天数据出现新的半年报告期变化；history=material_update |
| industry-candidate-007 | exclude | industry | 事件2×相关3+钩子1 = 7；常规财务与估值报告触发硬门禁；没有相对一致预期或公司指引的异常比较基准；history=new_event |
| industry-repeat-001 | exclude | industry | 事件2×相关3+钩子1 = 7；双周历史已报道同一报告期和同一组平台数据，repeat_only；history=repeat_only |
| industry-repeat-002 | exclude | industry | 事件2×相关3+钩子1 = 7；本周周报已报道同一上半年市场收入与增速，repeat_only；history=repeat_only |
| industry-repeat-003 | exclude | industry | 事件2×相关3+钩子1 = 7；同一市场报告已经日报报道，repeat_only；history=repeat_only |
| industry-repeat-004 | exclude | industry | 事件3×相关3+钩子2 = 11；同一投资、同一团队和同一项目已在日报及周报报道，repeat_only；history=repeat_only |
| industry-outside-001 | exclude | industry | 事件3×相关3+钩子1 = 10；事件发生于7月30日，早于本期窗口；history=new_event |
| industry-outside-002 | exclude | industry | 事件2×相关3+钩子1 = 7；演讲和数据发布发生于7月30日，早于本期窗口；history=new_event |
| industry-outside-003 | exclude | industry | 事件3×相关3+钩子2 = 11；正式发售与首日榜单发生于7月30日，早于本期窗口；history=new_event |
| industry-outside-004 | exclude | industry | 事件3×相关2+钩子2 = 8；相对欧盟批准属于实质状态变化，但全部审批取得日为7月30日，早于本期窗口；history=material_update |
| industry-outside-005 | exclude | industry | 事件3×相关3+钩子1 = 10；定档公告发生于7月30日，早于本期窗口；history=new_event |
| industry-borderline-001 | exclude | industry | 事件2×相关2+钩子1 = 5；事件2×相关2+钩子1 = 5，平台安全迁移点明确但未达7分；history=new_event |
| ai-candidate-001 | include | ai | AI Agent直接进入角色互动与叙事玩法 |
| ai-candidate-002 | include | ai | Agent直接调用引擎工具完成可编辑的空间构建 |
| ai-candidate-003 | include | ai | AI已直接作用于洞察、素材、KOL、投放和玩家运营 |
| industry-e0-001 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-002 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-003 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-004 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-005 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-006 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-007 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-008 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-009 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-010 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-011 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-012 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-013 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-014 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-015 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-016 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-017 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-018 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-019 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-020 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-021 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-022 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-023 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-024 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-025 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-026 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-027 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-028 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-029 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-030 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-031 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-032 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-033 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-034 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-035 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-036 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-037 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-038 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-039 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-040 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-041 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-042 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-043 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-044 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-045 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-046 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-047 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-048 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-049 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-050 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-051 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-052 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-053 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-054 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-055 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-056 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-057 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-058 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-059 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-060 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-061 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-062 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-063 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-064 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-065 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-066 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-067 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-068 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-069 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-070 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-071 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-072 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-073 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-074 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-075 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-076 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-077 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-078 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-079 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-080 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-081 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-082 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-083 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-084 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-085 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-086 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-087 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-088 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-089 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-090 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-091 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-092 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-093 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-094 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-095 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-096 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-097 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-098 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-099 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-100 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-101 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-102 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-103 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-104 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-105 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-106 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-107 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-108 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-109 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-110 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-111 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-112 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-113 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-114 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-115 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-116 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-117 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-118 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-119 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-120 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-121 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-122 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-123 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-124 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-125 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-126 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-127 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-128 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-129 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-130 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-131 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-132 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-133 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-134 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-135 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-136 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-137 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-138 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-139 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-140 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-141 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-142 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-143 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-144 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-145 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-146 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-147 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-148 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-149 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-150 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-151 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-152 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-153 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-154 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-155 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-156 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-157 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-158 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-159 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-160 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-161 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-162 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-163 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-164 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-165 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-166 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-167 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-168 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-169 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-170 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-171 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-172 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-173 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-174 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-175 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-176 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-177 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-178 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-179 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-180 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-181 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-182 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-183 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-184 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-185 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-186 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-187 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-188 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-189 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-190 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-191 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-192 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-193 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-194 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-195 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-196 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-197 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-198 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-199 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-200 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-201 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-202 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-203 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-204 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-205 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-206 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-207 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-208 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-209 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-210 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-211 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-212 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-213 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-214 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-215 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-216 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-217 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-218 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-219 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-220 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-221 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-222 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-223 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-224 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-225 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-226 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-227 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-228 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-229 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-230 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-231 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-232 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-233 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-234 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-235 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-236 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-237 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-238 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-239 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-240 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-241 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-242 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-243 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-244 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-245 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-246 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-247 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-248 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-249 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-250 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-251 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-252 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-253 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-254 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-255 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-256 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-257 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-258 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-259 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-260 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-261 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-262 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-263 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-264 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-265 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-266 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-267 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-268 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-269 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-270 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-271 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| industry-e0-272 | exclude | industry | 事件0×相关0+钩子0 = 0；普通版本、联动、展会宣传、纯榜单、常规财报、旧闻或弱迁移海外内容，E=0排除；history=new_event |
| ai-feed-001 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-002 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-003 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-004 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-005 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-006 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-007 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-008 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-009 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-010 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-011 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-012 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-013 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-014 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-015 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-016 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-017 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-018 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-019 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-020 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-021 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-022 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-023 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-024 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-025 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-026 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-027 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-028 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-029 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| ai-feed-030 | exclude | ai | 未形成比本期直接游戏研发/发行应用更具体的证据链，不用于凑数 |
| community-candidate-001 | include | community | 8月1日新建事件，触发、撤回、玩家分歧与时间线完整 |
| community-exclude-001 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-002 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-003 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-004 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-005 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-006 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-007 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-008 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-009 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-010 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-011 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-012 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-013 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-014 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-015 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-016 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-017 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-018 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-019 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-020 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-021 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-022 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-023 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-024 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-025 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-026 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-027 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-028 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-029 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-030 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-031 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-032 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-033 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-034 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-035 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-036 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-037 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-038 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-039 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-040 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-041 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-042 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-043 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-044 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-045 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-046 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-047 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-048 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-049 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-050 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-051 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-052 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-053 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-054 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-055 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-056 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-057 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-058 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-059 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-060 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-061 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-062 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-063 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-064 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-065 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-066 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-067 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-068 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-069 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-070 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-071 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-072 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-073 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-074 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-075 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-076 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-077 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-078 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-079 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-080 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-081 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-082 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| community-exclude-083 | exclude | community | 旧帖仅延续热度、事件信息不完整、与已报事件重复或缺少可核验的新进展 |
| deep-candidate-001 | include | deep | 单篇高质量研究给出完整数据、机制与下游投放含义 |
| deep-candidate-002 | exclude | deep | 可见正文仅为付费报告导语，缺少完整机制与证据链 |
| release-candidate-005 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-004 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-006 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-007 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-extra-001 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-008 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-002 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-014 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-017 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-018 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-019 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-021 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-024 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-025 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-026 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-030 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-031 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-032 | exclude | release_calendar | 事件日期不在报告窗口 |
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
| release-candidate-074 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-075 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-076 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-077 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-078 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-079 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-080 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-081 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-082 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-083 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-084 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-085 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-086 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-087 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-088 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-089 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-090 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-091 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-092 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-093 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-094 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-095 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-096 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-097 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-098 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-099 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-100 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-101 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-102 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-103 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-104 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-105 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-106 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-107 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-108 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-109 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-110 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-111 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-112 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-113 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-114 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-115 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-116 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-117 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-118 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-119 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-120 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-121 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-122 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-123 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-124 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-125 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-126 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-127 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-128 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-129 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-130 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-131 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-132 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-133 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-134 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-135 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-136 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-137 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-138 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-139 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-140 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-141 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-142 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-143 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-144 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-145 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-146 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-147 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-148 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-149 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-150 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-151 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-152 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-153 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-154 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-155 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-156 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-157 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-158 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-159 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-160 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-161 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-162 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-163 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-164 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-165 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-166 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-167 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-168 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-169 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-170 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-171 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-172 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-173 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-174 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-175 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-176 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-177 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-178 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-179 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-180 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-181 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-182 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-183 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-184 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-185 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-186 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-187 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-188 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-189 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-190 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-191 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-192 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-193 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-194 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-195 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-196 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-197 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-198 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-199 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-200 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-201 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-202 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-203 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-204 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-205 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-206 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-207 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-208 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-209 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-210 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-211 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-212 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-213 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-214 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-215 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-216 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-217 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-218 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-219 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-220 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-221 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-222 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-223 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-224 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-225 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-226 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-227 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-228 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-229 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-230 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-231 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-232 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-233 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-234 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-235 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-236 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-237 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-238 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-239 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-240 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-241 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-242 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-243 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-244 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-245 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-246 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-247 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-248 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-249 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-250 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-251 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-252 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-253 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-254 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-255 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-256 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-257 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-258 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-259 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-260 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-261 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-262 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-263 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-264 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-265 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-266 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-267 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-268 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-269 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-270 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-271 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-272 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-273 | exclude | release_calendar | 单源不具备正文资格 |
