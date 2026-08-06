# Selection Decisions

- 维度覆盖自检：国内移动/国产产品与人才 13张候选 / 市场数据 8张候选 / 并购 3张候选 / 平台政策 1张候选 / 档期变动 4张候选 / 资本组织 5张候选 / 海外重大 6张候选
- AI反扫：已扫描全部行业候选；A001、A002转入AI分区，行业与AI无重复入选。
- 产品日历反扫：已扫描全量 industry_news 与 release_calendar；别名与漏挂节点已修复后由 sync_release_decisions.py 确定性排序。
- 产品日历漏挂反查：补入《杀死影子》与 Big Walk 的行业来源，合并火线战姬、航海奇兵别名，并补记《小鸡与小马：超级派对》双源终测节点。
- 社区补扫：已按主体、产品、机制与争议词扫描同窗口社区池；旧事件无新状态均排除。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 国产重点公司新品首测；事件3×相关3+钩子1=10；E3×R3+M1=10 |
| I002 | include | industry_news | 国内大厂游戏业务重组后的产品组合正式集中展示；事件3×相关3+钩子1=10；E3×R3+M1=10 |
| I003 | include | industry_news | 国内手游发行商披露合作新品与年内全球上线计划；事件3×相关3+钩子1=10；E3×R3+M1=10 |
| I004 | include | industry_news | 面向中国市场的新射击产品进入正式展示与试玩阶段；事件3×相关3+钩子1=10；E3×R3+M1=10 |
| I005 | include | industry_news | 交易从已获批准进入正式交割，属于可验证状态变化；事件3×相关2+钩子2=8；E3×R2+M2=8 |
| I006 | include | industry_news | 国产SLG进入停运阶段并伴随研发资源转向；事件2×相关3+钩子1=7；E2×R3+M1=7 |
| I007 | include | industry_news | 国内研发分部关闭且涉及多条在研产品线；事件2×相关3+钩子1=7；E2×R3+M1=7 |
| I008 | include | industry_news | 国产移动RPG披露新的全球用户里程碑；事件2×相关3+钩子1=7；E2×R3+M1=7 |
| I009 | include | industry_news | 国内行业展会发布新的市场与国际交流结构数据；事件2×相关3+钩子1=7；E2×R3+M1=7 |
| I010 | include | industry_news | 国产小团队新品取得可核验首发数据；事件2×相关3+钩子1=7；E2×R3+M1=7 |
| I011 | exclude | - | 前一日报产品日历已报道同一首曝事实，换来源无新增状态；E3×R3+M1=10 |
| I012 | exclude | - | 历史已报道项目组解散，本期仅为换来源重述；E2×R3+M1=7 |
| I013 | exclude | - | 同一7月榜单结构已报道，新增媒体解读不构成新报告期变化；E2×R3+M1=7 |
| I014 | exclude | - | 与前一日报同一产品数据和软启动状态，无实质更新；E2×R3+M1=7 |
| I015 | exclude | - | 前一日报已报道同一激励额度与90天结构，本期仅补充采访背景；E2×R3+M1=7 |
| I016 | exclude | - | 同一上半年电竞收入与移动端占比已进入周末报；E2×R3+M1=7 |
| I017 | exclude | - | 注册、DAU与内容消费等核心事实已进入周末报，本期为复盘文章；E2×R3+M1=7 |
| I018 | exclude | - | 全球3亿下载与中国市场进入状态已在8月3日报告；E2×R3+M1=7 |
| I019 | exclude | - | 8月3日报告产品日历已报道同一首次公布和2026年上线计划；E3×R3+M1=10 |
| I020 | exclude | - | 8月1日版本表现的晚到复盘，缺少本报告日新钩子；事件2×相关3+钩子0=6；E2×R3+M0=6 |
| I021 | exclude | - | 海外消费品授权对移动或全球游戏竞争格局迁移点弱；事件3×相关1+钩子1=4；E3×R1+M1=4 |
| I022 | exclude | - | 海外一般工作室扩张且与优先市场迁移点弱；事件3×相关1+钩子1=4；E3×R1+M1=4 |
| I023 | exclude | - | 平台安全表态尚未形成可验证的新政策节点；事件2×相关2+钩子1=5；E2×R2+M1=5 |
| I024 | exclude | - | 全球移动数据有迁移价值但单源摘要钩子较弱；事件2×相关2+钩子1=5；E2×R2+M1=5 |
| I025 | exclude | - | 尚未确认的裁员预期，事件类型按纯裁员1计；事件1×相关2+钩子2=4；E1×R2+M2=4 |
| I026 | exclude | - | 履新发生于去年底，本期主要为访谈与旧背景；事件1×相关3+钩子1=4；E1×R3+M1=4 |
| I027 | exclude | - | 按规则属于E=0的例行宣传、活动、硬件或非游戏内容；其中S0144另有独立候选I010；E0×R0+M0=0 |
| A001 | include | ai_trends | AI已直接作用于手游发行与广告运营 |
| A002 | include | ai_trends | AI世界构建团队已参与移动优先游戏创作工具Build上线 |
| A003 | include | ai_trends | 实时多模态交互可迁移到游戏NPC与陪伴交互 |
| A004 | exclude | - | 包含多个不同产品与观点，不能合并为单一独立事件 |
| A005 | exclude | - | 缺少直接游戏应用，或无法形成具体且足够实质的游戏迁移链条 |
| C001 | include | community_discourse | 触发、争议逻辑与同日时间线完整 |
| C002 | exclude | - | 同一社区事件已进入2026-08-04日报，新增回复未带来官方回应或机制变化 |
| C003 | exclude | - | 同一问卷事件已进入2026-08-03日报，本期仅为延续回复 |
| C004 | exclude | - | 7月29日旧帖且周末候选已审计，本期没有新的官方回应或状态变化 |
| C005 | exclude | - | 正文未提供品牌、原始公号内容或解雇声明，无法核验标题主张 |
| C006 | exclude | - | 普通外观调整且讨论主要为轻度猜测，不足以占用社区分区 |
| C007 | exclude | - | 海外主机产品常规补丁反馈，国内移动候选优先 |
| C008 | exclude | - | 缺少清晰事件、窗口内新增状态或可核验的四要素 |
| D001 | include | deep_analysis | 三条本期入选事件共同支撑变化—机制—下游影响 |
| release-candidate-001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-012 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-011 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-079 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-004 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-073 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-074 | exclude | - | 超过本报告产品日历条数上限 |
| release-candidate-005 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-006 | exclude | - | 事件日期不在报告窗口 |
| release-candidate-007 | exclude | - | 单源不具备正文资格 |
| release-candidate-008 | exclude | - | 单源不具备正文资格 |
| release-candidate-009 | exclude | - | 单源不具备正文资格 |
| release-candidate-010 | exclude | - | 事件日期不在报告窗口 |
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
| release-candidate-028 | exclude | - | 单源不具备正文资格 |
| release-candidate-029 | exclude | - | 单源不具备正文资格 |
| release-candidate-030 | exclude | - | 单源不具备正文资格 |
| release-candidate-031 | exclude | - | 单源不具备正文资格 |
| release-candidate-032 | exclude | - | 单源不具备正文资格 |
| release-candidate-033 | exclude | - | 单源不具备正文资格 |
| release-candidate-034 | exclude | - | 单源不具备正文资格 |
| release-candidate-035 | exclude | - | 单源不具备正文资格 |
| release-candidate-036 | exclude | - | 单源不具备正文资格 |
| release-candidate-037 | exclude | - | 单源不具备正文资格 |
| release-candidate-038 | exclude | - | 单源不具备正文资格 |
| release-candidate-039 | exclude | - | 单源不具备正文资格 |
| release-candidate-040 | exclude | - | 单源不具备正文资格 |
| release-candidate-041 | exclude | - | 单源不具备正文资格 |
| release-candidate-042 | exclude | - | 单源不具备正文资格 |
| release-candidate-043 | exclude | - | 单源不具备正文资格 |
| release-candidate-044 | exclude | - | 单源不具备正文资格 |
| release-candidate-045 | exclude | - | 单源不具备正文资格 |
| release-candidate-046 | exclude | - | 单源不具备正文资格 |
| release-candidate-047 | exclude | - | 单源不具备正文资格 |
| release-candidate-048 | exclude | - | 单源不具备正文资格 |
| release-candidate-049 | exclude | - | 单源不具备正文资格 |
| release-candidate-050 | exclude | - | 单源不具备正文资格 |
| release-candidate-051 | exclude | - | 单源不具备正文资格 |
| release-candidate-052 | exclude | - | 单源不具备正文资格 |
| release-candidate-053 | exclude | - | 单源不具备正文资格 |
| release-candidate-054 | exclude | - | 单源不具备正文资格 |
| release-candidate-055 | exclude | - | 单源不具备正文资格 |
| release-candidate-056 | exclude | - | 单源不具备正文资格 |
| release-candidate-057 | exclude | - | 单源不具备正文资格 |
| release-candidate-058 | exclude | - | 单源不具备正文资格 |
| release-candidate-059 | exclude | - | 单源不具备正文资格 |
| release-candidate-060 | exclude | - | 单源不具备正文资格 |
| release-candidate-061 | exclude | - | 单源不具备正文资格 |
| release-candidate-062 | exclude | - | 单源不具备正文资格 |
| release-candidate-063 | exclude | - | 单源不具备正文资格 |
| release-candidate-064 | exclude | - | 单源不具备正文资格 |
| release-candidate-065 | exclude | - | 单源不具备正文资格 |
| release-candidate-066 | exclude | - | 单源不具备正文资格 |
| release-candidate-067 | exclude | - | 单源不具备正文资格 |
| release-candidate-068 | exclude | - | 单源不具备正文资格 |
| release-candidate-069 | exclude | - | 单源不具备正文资格 |
| release-candidate-070 | exclude | - | 单源不具备正文资格 |
| release-candidate-071 | exclude | - | 单源不具备正文资格 |
| release-candidate-072 | exclude | - | 单源不具备正文资格 |
| release-candidate-077 | exclude | - | 单源不具备正文资格 |
| release-candidate-078 | exclude | - | 事件日期不在报告窗口 |

## 历史去重摘要

- repeat_only: I011 阴阳师：云图、I012 剑心雕龙、I013 7月微信小游戏榜、I014 GTA式移动开放世界、I015 绿洲启元UGC激励、I016 中国电竞产业、I017 鹅鸭杀、I018 对峙2、I019 Palworld Online。
- material_update: I005 EA交易由‘取得全部监管批准、预计完成’进入‘8月4日正式完成’，新增PIF 93.4%持股和管理层调整。
