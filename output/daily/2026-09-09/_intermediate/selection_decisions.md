# Selection Decisions

- 卡片曝光去重：广州扶持、《旅行青蛙》停运、GungHo交易与《王者万象棋》档期均已有卡片曝光，按 repeat_only 排除；8月手游榜新增单品收入事实，按 material_update 入选；Double Fine历史周报 card_rank=null/10、card_exposed=false，本期使用唯一 card_carryover。
- 卡片曝光去重自检：card_carryover=1；此前卡片排名为 null/10，读者可见正文不含任何补位标记。
- 维度覆盖自检：国内移动/国产产品与人才 16张候选 / 市场数据 8张候选 / 并购与投资 5张候选 / 平台政策 6张候选 / 档期变动 35个产品节点 / 资本组织 6张候选 / 海外重大 31张候选。
- AI反扫：已检查全部行业来源；《洛克王国：世界》战斗AI、WorkBuddy玩家服务与AI编程边界进入AI新闻，EA配音与腾讯研发工具链因近期已刊发排除。
- 产品日历漏挂反查：已反扫 industry_news 与 release_calendar；《未眠野》首曝因已进入行业新闻而跨栏去重，《王者万象棋》旧档期与《沙丘：觉醒》宣传稿重提档期排除，其余节点未满足多源门槛。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 国内开放世界RPG首曝获多源覆盖。（事件3×相关3+钩子2 = 11） |
| I002 | include | industry_news | 国内厂商披露在研新品。（事件3×相关3+钩子1 = 10） |
| I003 | include | industry_news | 国内厂商新增可核验项目储备。（事件3×相关3+钩子1 = 10） |
| I004 | include | industry_news | 国内游戏公司重大基金投资。（事件3×相关3+钩子1 = 10） |
| I005 | include | industry_news | 模拟经营优先赛道出现明确在研项目。（事件3×相关3+钩子1 = 10） |
| I006 | include | industry_news | 中国移动游戏平台披露生态规模和用户价值数据。（事件2×相关3+钩子1 = 7） |
| I007 | include | industry_news | 相对既有Top 50总盘数据新增单品收入与排序事实。（事件2×相关3+钩子1 = 7） |
| I008 | include | industry_news | 明确的新项目与核心人才招聘信号。（事件3×相关2+钩子1 = 7） |
| I009 | include | industry_news | 历史完整报告已收录但订阅卡片未展示，本期仍达门槛。（事件3×相关2+钩子1 = 7） |
| I010 | exclude | industry_news | 历史卡片已曝光且无新增拨付状态。（事件2×相关3+钩子1 = 7） |
| I011 | exclude | industry_news | 上一日报卡片已曝光，无实质新增。（事件2×相关3+钩子2 = 8） |
| I012 | exclude | industry_news | 周末报卡片已曝光，同一交易无状态变化。（事件3×相关2+钩子1 = 7） |
| I013 | exclude | industry_news | 相同档期已进入历史卡片，无新状态。（事件3×相关3+钩子1 = 10） |
| I014 | exclude | industry_news | 全球结构迁移点明确但总分未达日报门槛。（事件2×相关2+钩子1 = 5） |
| I015 | exclude | industry_news | 单品数据有价值但国内移动相关性不足。（事件2×相关2+钩子1 = 5） |
| I016 | exclude | industry_news | 多源平台事故仍停留在6分边界。（事件2×相关2+钩子2 = 6） |
| I017 | exclude | industry_news | 组织整合有多源覆盖但迁移点不足。（事件2×相关2+钩子2 = 6） |
| I018 | exclude | industry_news | 移动长线数据未达到日报门槛。（事件2×相关2+钩子1 = 5） |
| I019 | exclude | industry_news | 市场预测迁移点不足。（事件2×相关2+钩子1 = 5） |
| I020 | exclude | industry_news | 区域预测缺少更强当日钩子。（事件2×相关2+钩子1 = 5） |
| I021 | exclude | industry_news | 单一案例总分未达门槛。（事件2×相关2+钩子1 = 5） |
| I022 | exclude | industry_news | 固定高关注主体但仍是战略表态。（事件1×相关3+钩子1 = 4） |
| I023 | exclude | industry_news | 老品周年运营与纯榜单不足以过线。（事件1×相关3+钩子1 = 4） |
| I024 | exclude | industry_news | 老品内容节奏调整未达到重大生命周期门槛。（事件1×相关3+钩子1 = 4） |
| I025 | exclude | industry_news | 海外人才支持事件迁移点较弱。（事件3×相关1+钩子1 = 4） |
| A001 | include | ai_trends | 强化学习AI已进入正式产品并披露部署规模。 |
| A002 | include | ai_trends | AI工具直接承接游戏攻略与战术查询。 |
| A003 | include | ai_trends | 直接作用研发流程并给出可核验的任务边界。 |
| A004 | merge | ai_trends | 与A002同主体、同日期、同一事件。 |
| A005 | exclude | ai_trends | 上一日报已完整报道同一事实。 |
| A006 | exclude | ai_trends | 周末报已完整报道同一事实。 |
| A007 | exclude | ai_trends | 直接应用成立，但本期优先级低于三项国内产品与研发事件。 |
| C001 | include | community_discourse | 同日触发、争议逻辑与对立观点完整。 |
| C002 | include | community_discourse | 窗口内新增回复把争议从主体归因推进到平台机制。 |
| D001 | include | deep_analysis | 样本、分布与机制链完整。 |
| I-S0001 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0002 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0003 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0005 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0006 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0007 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0008 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0009 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0010 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0011 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0012 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0013 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0014 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0015 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0016 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0017 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0018 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0019 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0020 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0021 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0022 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0023 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0024 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0028 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0030 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0032 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0034 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0040 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0041 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0044 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0049 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0051 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0053 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0054 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0055 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0056 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0057 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0058 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0059 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0060 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0062 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0065 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0066 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0069 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0070 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0071 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0072 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0073 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0074 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0075 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0076 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0077 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0078 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0079 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0080 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0081 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0082 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0083 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0084 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0085 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0086 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0087 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0088 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0089 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0090 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0091 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0092 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0093 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0094 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0095 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0096 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0097 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0098 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0099 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0100 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0101 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0102 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0103 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0104 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0105 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0106 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0107 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0108 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0109 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0111 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0112 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0113 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0115 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0116 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0117 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0118 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0119 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0120 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0121 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0122 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0123 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0124 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0125 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0126 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0127 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0128 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0129 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0130 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0131 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0132 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0134 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0135 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0137 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0139 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0140 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0141 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0142 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0143 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0144 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0146 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0147 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0148 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0149 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0150 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0151 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0153 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| I-S0155 | exclude | industry_news | 例行宣传、普通版本内容、纯榜单、非游戏或海外弱迁移事件，未达到日报门槛。（事件0×相关0+钩子0 = 0） |
| A-S0157 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0158 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0159 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0160 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0161 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0162 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0163 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0164 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0165 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0166 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0167 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0168 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0169 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0170 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0171 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0172 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0173 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0174 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0175 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0176 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0177 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0178 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| A-S0179 | exclude | ai_trends | 缺少优先于本期直接游戏应用的采用证据。 |
| C-S0218 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0219 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0221 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0222 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0223 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0224 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0225 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0226 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0227 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0229 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0230 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0231 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| C-S0232 | exclude | community_discourse | 触发、时效、争议逻辑或可核验后续不足。 |
| release-candidate-004 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-001 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-005 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-006 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-007 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-008 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-011 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-014 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-015 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-016 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-002 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-003 | exclude | release_calendar | 超过本报告产品日历条数上限 |
| release-candidate-017 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018 | exclude | release_calendar | 单源不具备正文资格 |
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
| release-candidate-030 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-033 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-035 | exclude | release_calendar | 事件日期不在报告窗口 |
