# Selection Decisions

维度覆盖自检：国内移动/国产产品与人才 12 张；市场数据 6 张；并购/清算 3 张；平台政策与工具 6 张；档期变动 8 张；资本组织 7 张；海外重大 9 张。

行业新闻反扫结论：Unity 7、Studio Atelico、DLSS 5 转入AI新闻；Netflix事件核心仍为移动/云游戏市场数据，AI为背景，保留行业新闻。

产品日历反扫结论：已扫描industry_news与release_calendar全量输入，并修正《使命召唤：现代战争4》《仙境传说3》《机械启元》《遗忘之海》的同产品同日聚类，补入《DCKO》首次正式曝光。

产品日历漏挂反查：已逐条扫描industry_news中的上线、定档、测试、预下载与首次正式曝光信号；合格节点已升入release_calendar_audit.json，其余单源或非召回事件均在下表显式exclude。

行业新闻评分记法：事件3×相关3+钩子1 = 10；以下每条行业候选均按同一E×R+M口径逐条记录include/exclude。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| C001 | include | 行业新闻 | E3×R3+M1=10；国内长线手游核心策划离职，达到阈值 |
| C002 | include | 行业新闻 | E2×R3+M2=8；国内重度手游停运且全球发行取消，多源同事件达到阈值 |
| C003 | include | 行业新闻 | E2×R3+M1=7；国内移动与模拟经营赛道数据达到阈值 |
| C004 | include | 行业新闻 | E2×R3+M1=7；国内平台开放互动网页与小游戏能力，达到阈值 |
| C005 | include | 行业新闻 | E2×R3+M1=7；国内游戏团队解散及产品失去维护，达到阈值 |
| C006 | include | 行业新闻 | E2×R3+M1=7；全球移动及云游戏结构性数据达到阈值 |
| C007 | exclude | - | E2×R2+M2=6；总分6，全球平台迁移点明确但未达阈值 |
| C008 | exclude | - | E3×R1+M2=5；总分5，海外小型工作室关闭对国内移动迁移较弱 |
| C009 | exclude | - | E2×R3+M0=6；总分6，结构性资料丰富但缺少单日独立事件钩子 |
| C010 | exclude | - | E2×R3+M1=7；常规季度财务披露，无异常比较基准，按财报例外排除 |
| C011 | exclude | - | E3×R0+M2=2；影视并购为核心，游戏迁移点不足 |
| C012 | exclude | - | E3×R1+M1=4；总分4，海外小团队组织变化迁移点较弱 |
| C013 | exclude | - | E2×R1+M1=3；总分3，海外单机档期变化且迁移点弱 |
| C014 | exclude | - | E1×R3+M1=4；总分4，老品跨媒体内容动作不足以抬高事件类型 |
| C015 | exclude | - | E1×R3+M2=5；常规利润分配提议且尚待审批，按财报/资本例外排除 |
| C016 | exclude | - | E2×R2+M1=5；总分5，B2B工具发布影响尚未形成平台规则迁移 |
| A001 | include | AI新闻 |AI已直接作用于游戏产品与资产生成 |
| A002 | include | AI新闻 |引擎直接把编码智能体与AI图形优化接入游戏研发 |
| A003 | include | AI新闻 |AI图形功能直接进入游戏渲染与美术控制环节 |
| A004 | exclude | - |具游戏UI与美术迁移价值，但日报3条直接作用类优先 |
| A005 | exclude | - |通用软件工程迁移价值明确，但未落到具体游戏场景且直接作用候选已足 |
| Q001 | include | 玩家舆论 |同日两帖围绕同一公告形成具体且有后续的社区事件 |
| Q002 | include | 玩家舆论 |触发点、争议逻辑、时间线与对立观点完整 |
| Q003 | exclude | - |原帖未提供可核验数据且回复中出现明显质疑，证据不足 |
| Q004 | exclude | - |旧帖在窗口仅有零星续帖，且多数回复不认可争议前提 |
| Q005 | merge | merge into C002 |与行业新闻同产品、同日、同一停运事件，避免跨栏重复 |
| Q006 | exclude | - |主要依据玩家对内容储备的推断，缺少清晰官方节点 |
| Q007 | exclude | - |旧帖窗口内无实质新进展，且争议对象与逻辑分散 |
| Q008 | exclude | - |正向粉丝行动但未形成需要事件报道的争议或运营后续 |
| Q009 | exclude | - |外部媒体议题转发为主，游戏内触发与后续不足 |
| Q010 | exclude | - |帖子自身以不明原因为前提，缺少可核验事件链 |
| Q011 | exclude | - |事件较窄且与当日游戏产品运营关联有限 |
| Q012 | exclude | - |敏感指控缺少独立来源与可核验原图上下文 |
| Q013 | exclude | - |这些来源分属多个独立事件，不能聚成单一社区候选；逐项均弱于国内候选 |
| D001 | include | 行业精选 | R3/I3/E3/C3=12；国内MMO停运与新品首测共同支撑变化—机制—下游影响 |
| D002 | exclude | - | R2/I3/E3/C3=11；高质量分析源，但与当日国内入选事件的直接连接弱于D001 |
| D003 | exclude | - | R3/I1/E1/C2=7；原文只有大盘摘要，机制证据不足以独立成深度观察 |
| D004 | exclude | - | R1/I2/E3/C2=8；证据完整但主要讨论通用AI应用、购物与广告，游戏连接不足 |
| release-candidate-001 | include | 产品日历 | event3×source4=12，多源优先级前缀 |
| release-candidate-002 | include | 产品日历 | event3×source4=12，多源优先级前缀 |
| release-candidate-003 | include | 产品日历 | event3×source3=9，多源优先级前缀 |
| release-candidate-004 | include | 产品日历 | event3×source2=6，多源优先级前缀 |
| release-candidate-005 | include | 产品日历 | event3×source2=6，多源优先级前缀 |
| release-candidate-006 | exclude | - | 单源，不具备正文资格 |
| release-candidate-007 | exclude | - | 单源，不具备正文资格 |
| release-candidate-008 | exclude | - | 单源，不具备正文资格 |
| release-candidate-009 | exclude | - | 单源，不具备正文资格 |
| release-candidate-010 | exclude | - | event2×source3=6，超过日报5条上限 |
| release-candidate-011 | exclude | - | event2×source2=4，超过日报5条上限 |
| release-candidate-012 | exclude | - | 单源，不具备正文资格 |
| release-candidate-013 | exclude | - | 单源，不具备正文资格 |
| release-candidate-014 | exclude | - | 单源，不具备正文资格 |
| release-candidate-015 | exclude | - | 单源，不具备正文资格 |
| release-candidate-016 | exclude | - | 单源，不具备正文资格 |
| release-candidate-017 | exclude | - | 单源，不具备正文资格 |
| release-candidate-018 | exclude | - | 单源，不具备正文资格 |
| release-candidate-019 | exclude | - | 单源，不具备正文资格 |
| release-candidate-020 | exclude | - | 单源，不具备正文资格 |
| release-candidate-021 | exclude | - | 单源，不具备正文资格 |
| release-candidate-022 | exclude | - | 单源，不具备正文资格 |
| release-candidate-023 | exclude | - | 单源，不具备正文资格 |
| release-candidate-024 | exclude | - | 单源，不具备正文资格 |
| release-candidate-025 | exclude | - | 单源，不具备正文资格 |
| release-candidate-026 | exclude | - | 单源，不具备正文资格 |
| release-candidate-027 | exclude | - | 单源，不具备正文资格 |
| release-candidate-028 | exclude | - | 单源，不具备正文资格 |
| release-candidate-029 | exclude | - | 单源，不具备正文资格 |
| release-candidate-030 | exclude | - | 单源，不具备正文资格 |
| release-candidate-031 | exclude | - | 单源，不具备正文资格 |
| release-candidate-032 | exclude | - | 单源，不具备正文资格 |
| release-candidate-033 | exclude | - | 单源，不具备正文资格 |
| release-candidate-034 | exclude | - | 单源，不具备正文资格 |
| release-candidate-035 | exclude | - | 单源，不具备正文资格 |
| release-candidate-036 | exclude | - | 单源，不具备正文资格 |
| release-candidate-037 | exclude | - | 单源，不具备正文资格 |
| release-candidate-038 | exclude | - | 单源，不具备正文资格 |
| release-candidate-039 | exclude | - | 单源，不具备正文资格 |
| release-candidate-040 | exclude | - | 单源，不具备正文资格 |
| release-candidate-041 | exclude | - | 单源，不具备正文资格 |
| release-candidate-042 | exclude | - | 单源，不具备正文资格 |
| release-candidate-043 | exclude | - | 单源，不具备正文资格 |
| release-candidate-044 | exclude | - | 单源，不具备正文资格 |
| release-candidate-045 | exclude | - | 单源，不具备正文资格 |
| release-candidate-046 | exclude | - | 单源，不具备正文资格 |
| release-candidate-047 | exclude | - | 单源，不具备正文资格 |
| release-candidate-048 | exclude | - | 单源，不具备正文资格 |
| release-candidate-049 | exclude | - | 单源，不具备正文资格 |
| release-candidate-050 | exclude | - | 单源，不具备正文资格 |
| release-candidate-051 | exclude | - | 单源，不具备正文资格 |
| release-candidate-052 | exclude | - | 单源，不具备正文资格 |
| release-candidate-053 | exclude | - | 单源，不具备正文资格 |
| release-candidate-054 | exclude | - | 单源，不具备正文资格 |
| release-candidate-055 | exclude | - | 单源，不具备正文资格 |
| release-candidate-056 | exclude | - | 单源，不具备正文资格 |
| release-candidate-057 | exclude | - | 单源，不具备正文资格 |
| release-candidate-058 | exclude | - | 单源，不具备正文资格 |
| release-candidate-059 | exclude | - | 单源，不具备正文资格 |
| release-candidate-060 | exclude | - | 单源，不具备正文资格 |
| release-candidate-061 | exclude | - | 单源，不具备正文资格 |
| release-candidate-062 | exclude | - | 单源，不具备正文资格 |
| release-candidate-063 | exclude | - | 单源，不具备正文资格 |
| release-candidate-064 | exclude | - | 单源，不具备正文资格 |
| release-candidate-065 | exclude | - | 单源，不具备正文资格 |
| release-candidate-066 | exclude | - | 单源，不具备正文资格 |
| release-candidate-067 | exclude | - | 单源，不具备正文资格 |
| release-candidate-068 | exclude | - | 单源，不具备正文资格 |
| release-candidate-069 | exclude | - | 单源，不具备正文资格 |
| release-candidate-070 | exclude | - | 单源，不具备正文资格 |
| release-candidate-071 | exclude | - | 单源，不具备正文资格 |

## 边界候选（行业总分5–6）

- C007 TikTok小游戏增长工具：E2×R2+M2=6。
- C008 Midgar Studio清算：E3×R1+M2=5。
- C009 国内UGC生态资料：E2×R3+M0=6。
- C015 吉比特分红提议：E1×R3+M2=5，且按常规资本分配排除。
- C016 F2P收入估算模型：E2×R2+M1=5。
