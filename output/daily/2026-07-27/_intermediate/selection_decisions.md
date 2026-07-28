# Selection Decisions

- 维度覆盖自检：国内移动9张 / 国产产品与人才12张 / 市场数据8张 / 并购3张 / 平台政策6张 / 档期变动9张 / 资本组织8张 / 海外重大11张。
- 产品日历漏挂反查：已反扫 industry_news 与 release_calendar 全量输入，合并《苍蓝避风港》别名，并补入《航海王：集结》《潜行者2》多源节点。
- 产品日历仅取多源候选确定性优先级前4项，不设最低分、不跳项。
- AI已反扫全部行业候选；行业、AI、社区与产品日历之间的同一独立事件不重复入选。

## 行业新闻 E×R+M 打分

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| industry-candidate-014 TapTap发布Cindy并披露AI游戏供给数据 | include | industry | 事件3×相关3+钩子2=11；国内游戏分发平台发布AI Agent，并披露AI游戏供给与分发机制调整 |
| industry-candidate-001 腾讯洽谈收购SuperPlay | exclude | - | 事件3×相关3+钩子2=11；用户确认该事件已在前期报告讲过，报告日无新增进展 |
| industry-candidate-002 梦幻西游手游主策划叶家离职 | exclude | - | 事件3×相关3+钩子1=10；用户确认该人事变动已在前期报告讲过，报告日无新增进展 |
| industry-candidate-003 莉莉丝Project F1预研项目曝光 | include | industry | 事件3×相关3+钩子1=10；国内厂商面向欧美的PVPVE新品预研信号 |
| industry-candidate-004 仙境传说3首曝并开放首次测试预约 | include | industry | 事件3×相关3+钩子1=10；国内发行的重点MMORPG新品首次正式曝光 |
| industry-candidate-005 龙之剑觉醒转买断后的四日市场表现 | include | industry | 事件2×相关3+钩子1=7；RPG从抽卡手游转买断后的当日新增市场数据 |
| industry-candidate-006 杖剑传说欧美版带动吉比特境外流水增长 | include | industry | 事件2×相关3+钩子1=7；国内厂商RPG出海取得明确收入与区域榜单数据 |
| industry-candidate-007 镇邪人进入微信小游戏畅销榜前三 | include | industry | 事件2×相关3+钩子1=7；国内小游戏新品取得连续榜单表现 |
| industry-candidate-008 遗忘之海移动端公测两日后的榜单表现 | include | industry | 事件2×相关3+钩子1=7；国内移动新品在报告日形成新的多平台榜单快照 |
| industry-candidate-009 QuestMobile披露中国手游与小游戏月活规模 | include | industry | 事件2×相关3+钩子1=7；中国手游APP与小游戏大盘数据 |
| industry-candidate-010 无畏契约源能行动注册用户突破一亿 | include | industry | 事件2×相关3+钩子1=7；国内PVP手游披露明确注册规模 |
| industry-candidate-011 Dragon Quest Smash Grow前三个月移动端收入 | include | industry | 事件2×相关3+钩子1=7；移动RPG披露前三个月区域收入结构 |
| industry-candidate-012 Pokémon Champions首月移动端收入 | include | industry | 事件2×相关3+钩子1=7；PVP手游披露首月收入与日峰值 |
| industry-candidate-013 Neon完成1300万美元A轮融资 | include | industry | 事件3×相关2+钩子1=7；游戏发行商D2C基础设施完成融资，具备全球渠道迁移点 |
| industry-boundary-001 AppMagic休闲解谜市场结构报告 | exclude | - | 事件2×相关2+钩子2=6；全球休闲手游结构迁移明确，但不属于中国市场或优先赛道 |
| industry-boundary-002 Xbox测试广告支持的免费云游戏 | exclude | - | 事件2×相关2+钩子1=5；平台实验具迁移点但证据正文过短且总分未达线 |
| industry-boundary-003 欧盟AI深度伪造透明度规则适用于游戏 | exclude | - | 事件2×相关2+钩子1=5；游戏合规迁移链条明确但事件发生在7月21日且总分未达线 |
| industry-boundary-004 TikTok小游戏Growth Max全球开放 | exclude | - | 事件2×相关2+钩子1=5；小游戏出海渠道迁移点明确但总分未达线 |
| industry-boundary-005 育碧移动端净预订占比上升 | exclude | - | 事件2×相关2+钩子2=6；常规季报披露且只略高于指引，财报例外不成立 |
| industry-boundary-006 Xbox向PC和掌机扩展向后兼容 | exclude | - | 事件2×相关2+钩子1=5；平台能力有迁移点但总分未达线 |

## AI 新闻

| candidate | decision | reason |
| --- | --- | --- |
| ai-candidate-002 妹居物语公开AI Native玩法循环与成本管理 | include | AI决策、记忆状态与玩法反馈构成产品核心循环 |
| ai-candidate-003 Sunrise Village用AI将运营团队从25人缩至3人 | include | AI已直接进入长线手游内容生产与运营流程 |
| ai-candidate-004 代号Craft开发者先锋营展示端到端生成流程 | exclude | 直接应用成立，但活动已于7月26日结束，优先级低于报告日三个更实质案例 |
| ai-candidate-005 Steam AI游戏供给与商业成功率统计 | exclude | 数据用于深度观察，避免与AI新闻分区重复 |
| ai-source-S0155 Suno 推出多项新功能，含MIDI导出等 | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0156 浪费20亿Token后，我开源了帮Agent定义目标的Leader.skill | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0157 用AI Skill自动生成可协作HTML PPT | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0158 NVIDIA 等多家行业领袖联合成立 Open Secure AI Alliance，推动 AI 安全与防御开源化 | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0159 Kimi K3 开源：2.8T MoE 模型与技术报告 | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0160 Kimi K3 开源分布式智能体环境 AgentENV | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0161 Kimi K3 上线 Modal，支持无损加速推理 | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |
| ai-source-S0162 Google AI Overviews 搜索结果出现率升至43% | exclude | 未证明已直接作用于游戏，或缺少具体游戏环节迁移链条 |

## 产品日历

| candidate | decision | reason |
| --- | --- | --- |
| release-candidate-001 苍蓝避风港 | include | 多源候选按事件类型×来源强度排序进入报告上限；总分6 |
| release-candidate-002 烽烟 | include | 多源候选按事件类型×来源强度排序进入报告上限；总分6 |
| release-candidate-003 无尽废墟 | exclude | 单源不具备正文资格；总分6 |
| release-candidate-004 明末 | exclude | 单源不具备正文资格；总分6 |
| release-candidate-005 炎之鸟 | exclude | 单源不具备正文资格；总分6 |
| release-candidate-006 Choppa： Rescue Rivals | exclude | 单源不具备正文资格；总分6 |
| release-candidate-007 航海王：集结 | include | 多源候选按事件类型×来源强度排序进入报告上限；总分6 |
| release-candidate-008 潜行者2：切尔诺贝利之心 | include | 多源候选按事件类型×来源强度排序进入报告上限；总分4 |
| release-candidate-009 无职转生 ～到了异世界就拿出真本事～ 回响编年史-资讯服务 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-010 王国保卫战6 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-011 芙娅之魂-代号：魂游大世界 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-012 一般武侠 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-013 三脚猫行动 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-014 为人方正闯江湖 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-015 主簿别慌：汉末急务 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-016 僵尸危机：校园封锁 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-017 全球商业帝国 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-018 再乱的货架我也能救回来 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-019 友谊的小船 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-020 反重力农场模拟器 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-021 可蛙和嫑蛙的跳一跳 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-022 周期 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-023 地牢狂猎（删档测试版） | exclude | 单源不具备正文资格；总分3 |
| release-candidate-024 墨刃斩群魔 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-025 大明浮生志3 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-026 奶茶店经营模拟器 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-027 帝临：九霄梦回 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-028 幻境大陆 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-029 弹爆防线 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-030 弹珠打砖块 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-031 心乐计算器 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-032 恋综模拟器 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-033 拯救喵星 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-034 拼豆工坊 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-035 指尖仙守 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-036 捂嘴战术 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-037 方块创想家 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-038 无序引力与空间 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-039 明末御尸录 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-040 浩瀚宇宙合集 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-041 湮灭方程式 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-042 灵魂秘境 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-043 点点冒险团 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-044 点点挖矿 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-045 牛顿的苹果复仇记 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-046 牛顿？胡言乱语！ | exclude | 单源不具备正文资格；总分3 |
| release-candidate-047 球球，滚吧！ | exclude | 单源不具备正文资格；总分3 |
| release-candidate-048 生物公司杀人案 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-049 电摩公司模拟器 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-050 疯狂竞拍 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-051 砌长城 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-052 禁汽年代：可乐贩卖师 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-053 秦皇纪：天下一统 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-054 精英部队 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-055 肉鸽俄罗斯方块 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-056 草木有灵 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-057 越挖越有钱 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-058 跨境电商 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-059 金币推推乐 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-060 问道山居 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-061 高三最后300天 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-062 高手来一局 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-063 魔方五子棋 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-064 黄油猫永动机 | exclude | 单源不具备正文资格；总分3 |
| release-candidate-065 英雄防线 | exclude | 单源不具备正文资格；总分2 |
| release-candidate-066 破碎之境：重启航线 | exclude | 单源不具备正文资格；总分1 |

## 玩家舆论与深度观察

| candidate | decision | reason |
| --- | --- | --- |
| community-candidate-001 Xbox服务数日内第二次中断引发数字所有权争论 | include | 报告日新事件，触发、玩家争议逻辑与时间线完整 |
| community-candidate-002 玩家提议PS5停用行动抗议实体介质决策 | exclude | 与Xbox数字所有权议题重叠；用户确认无需保留，不为社区栏软目标凑数 |
| community-source-S0248 [米哈游] 崩铁联动FATE，远坂凛称自己和妹妹踏上魔术师的道路，辜负了父亲留下的自由选择人生的开拓精神。 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0249 [明日方舟]知名画师anmi因画明日方舟皮肤推特遭国女围攻开启保护 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0250 [新瓜]反邪教也出手打击乙游了 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0251 [公主连结]大肥猪臀部重压！ | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0252 [网易]游戏葡萄：爬上Top 1，网易《遗忘之海》被低估了？ | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0253 [疑似内容][求瓜]鹰角开拓芯和猫咪狂梦前编剧怎么了 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0254 [厂商] [新瓜] 《代号鸢》给创作者发活动奖励用顺丰到付66元 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0255 [新瓜] [恋与深空]rapper派克特发歌diss乙游遭群嘲，叠纸准备起诉 | exclude | 2024年旧帖仅被挖起，报告日无实质新进展 |
| community-source-S0256 [新瓜] [绝区零]KFC联动角色签名与 主播女孩重度依赖 中的超天酱签名近似 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0257 [新瓜]燕云十六声4000块时装惊现超绝粽子装 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0258 [厂商] 如何评价腾讯企鹅岛(新腾讯总部)在没有装修完的情况下就开始大规模搬迁 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0259 NEXON的现任CEO是著名前EA高管嘲讽哥 | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0260 The Pokémon Company Announces Facial Recognition System to Help Kill Scalping at Japanese Card Stores, Mandatory From Elementary School Age | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0263 Rockstar Co-Founder Dan Houser Says if People Want Physical Game Releases Then Companies Should Provide It | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0264 Nintendo Legend Shigeru Miyamoto Says the Console Power Race Is Over | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0265 Peak gaming (Persona 3) | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0266 What's a game that was so terrifying you actually had to stop playing? What made you throw in the towel? | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0267 Final Fantasy 16 is making me happy again | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0268 What video game quote is stuck with you, even after years? | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0269 What’s a game moment that made you physically pause and just sit there for a minute before continuing? | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0270 What game did you bounce off after playing for a short time? | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0271 The need to check every area in a game | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| community-source-S0272 Small idea I've been thinking about: good games inspired by terrible ones | exclude | 未形成报告日新事件，或缺少可核验触发/时间线/争议逻辑 |
| deep-candidate-001 AI供给扩张后稀缺环节转向筛选与玩法闭环 | include | 平台供给、产品实践与跨平台统计共同构成完整机制链 |
| deep-candidate-002 Toon Blast在用户规模收缩后以留存和变现重建增长 | include | 单篇高质量分析完整解释变化、机制与下游影响 |
| deep-source-S0273 网络原生IP由社区共创扩展到影视 | exclude | 合格但与本期国内移动及AI生产主轴相比优先级较低 |
| deep-source-S0274 多家平台继续尝试云游戏入口 | exclude | 观察成立但机制证据偏薄，优先级低于入选项 |

## E=0 与其余排除项

- 其余行业、AI、社区记录均已逐条写入 `selection_decisions.json`；不进入 `sources_used.md`。
