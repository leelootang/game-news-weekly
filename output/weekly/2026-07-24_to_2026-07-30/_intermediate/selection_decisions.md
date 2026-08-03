# Selection Decisions

维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大事件 — 已审计。

产品日历排序公式：事件类型分 × 来源强度分 + 重点公司加分；重点公司新品节点加3分，但不绕过多源与日期窗口门槛。

产品日历漏挂反查：已扫描 industry_news 的上线、定档、测试节点；符合窗口、多源与事件边界的节点已升入产品日历，其余均显式排除。

行业新闻 E×R+M 打分记录：入选项按终分降序排列；11分项为事件3×相关3+钩子2 = 11，10分项为事件3×相关3+钩子1 = 10，8分项为事件2×相关3+钩子2 = 8。

| candidate_id | decision | section | reason |
|---|---|---|---|
| industry-001 | include | industry | E×R+M达到周报入选线 |
| industry-002 | include | industry | E×R+M达到周报入选线 |
| industry-003 | include | industry | E×R+M达到周报入选线 |
| industry-004 | merge | industry | 与industry-010为同一工作室、同一项目、同一日期的组织调整，合并多源呈现 |
| industry-005 | include | industry | E×R+M达到周报入选线 |
| industry-006 | include | industry | E×R+M达到周报入选线 |
| industry-007 | merge | industry | 与ai-005为同一发布事件，AI产品能力是更准确的栏目归属 |
| industry-008 | merge | industry | 与industry-001使用同一来源并描述同一份产业报告，去重合并 |
| industry-009 | include | industry | E×R+M达到周报入选线 |
| industry-010 | include | industry | 两条来源描述同一工作室、同一项目与同日调整，合并后保留 |
| ai-001 | include | ai | 游戏直接应用类AI事件 |
| ai-002 | include | ai | 游戏直接应用类AI事件 |
| ai-003 | include | ai | 游戏直接应用类AI事件 |
| ai-004 | include | ai | 游戏直接应用类AI事件 |
| ai-005 | include | ai | 游戏直接应用类AI事件 |
| community-001 | exclude | community | 来源未提供可核实的具体触发内容，无法建立争议逻辑与后续扫描基线 |
| community-002 | include | community | 具备触发、争议逻辑和窗口内讨论 |
| community-003 | include | community | 具备触发、争议逻辑和窗口内讨论 |
| deep-001 | include | deep | 人工selection明确选择 |
| deep-002 | include | deep | 人工selection明确选择 |

## 产品日历

| candidate_id | decision | score | company | product / reason |
|---|---|---:|---|---|
| release-candidate-001 | include | 15 | 网易 | 山海奇旅／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002 | include | 12 | 腾讯、三七互娱 | 斗破苍穹：斗帝之路／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003 | include | 12 | 腾讯 | 数字景德镇·瓷都小匠／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-004 | include | 12 | 腾讯 | 王者万象棋／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-005 | include | 12 | — | 雾影猎人／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-006 | include | 12 | — | 黄油猫／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-007 | include | 9 | — | 龙之谷：启程／多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-008 | exclude | 9 | — | 盗梦英雄2：幻野／超过本报告产品日历条数上限 |
| release-candidate-009 | exclude | 9 | — | 英雄防线／超过本报告产品日历条数上限 |
| release-candidate-010 | exclude | 9 | — | 仙界大掌门／超过本报告产品日历条数上限 |
| release-candidate-011 | exclude | 9 | — | 战意：三国／超过本报告产品日历条数上限 |
| release-candidate-012 | exclude | 9 | — | 伊莫／超过本报告产品日历条数上限 |
| release-candidate-013 | exclude | 9 | — | 静谧田园／超过本报告产品日历条数上限 |
| release-candidate-014 | exclude | 9 | 网易 | 光遇／超过本报告产品日历条数上限 |
| release-candidate-015 | exclude | 6 | — | 烽烟／超过本报告产品日历条数上限 |
| release-candidate-016 | exclude | 6 | — | 小城食光／超过本报告产品日历条数上限 |
| release-candidate-017 | exclude | 6 | — | 剑隐侠踪录／超过本报告产品日历条数上限 |
| release-candidate-018 | exclude | 6 | — | 烽烟／超过本报告产品日历条数上限 |
| release-candidate-019 | exclude | 6 | — | 饥饿派画家2：迷失／超过本报告产品日历条数上限 |
| release-candidate-020 | exclude | 6 | — | 你牛你来／超过本报告产品日历条数上限 |
| release-candidate-021 | exclude | 6 | — | 新三国：荣耀再起／超过本报告产品日历条数上限 |
| release-candidate-022 | exclude | 6 | — | 钓鱼：巨物猎手／超过本报告产品日历条数上限 |
| release-candidate-023 | exclude | 2 | — | 星球：重启／超过本报告产品日历条数上限 |
| release-candidate-024 | exclude | 15 | 腾讯、网易 | 遗忘之海／事件日期不在报告窗口 |
| release-candidate-025 | exclude | 12 | 网易、三七互娱 | 影之刃零／事件日期不在报告窗口 |
| release-candidate-026 | exclude | 9 | 腾讯 | 第七史诗／单源不具备正文资格 |
| release-candidate-027 | exclude | 9 | 网易 | 遗忘之海／事件日期不在报告窗口 |
| release-candidate-028 | exclude | 9 | 腾讯 | 无畏契约／单源不具备正文资格 |
| release-candidate-029 | exclude | 9 | 米哈游 | 绝区零／单源不具备正文资格 |
| release-candidate-030 | exclude | 9 | 鹰角网络 | 终末地／事件日期不在报告窗口 |
| release-candidate-031 | exclude | 9 | — | IGS 经典街机合集(IGS Classic Arcade Collection)／事件日期不在报告窗口 |
| release-candidate-032 | exclude | 9 | — | 战神：劳菲／事件日期不在报告窗口 |
| release-candidate-033 | exclude | 9 | — | 异环／事件日期不在报告窗口 |
| release-candidate-034 | exclude | 9 | — | 不同的冬天／事件日期不在报告窗口 |
| release-candidate-035 | exclude | 7 | 鹰角网络 | 明日方舟：终末地／单源不具备正文资格 |
| release-candidate-036 | exclude | 6 | — | 午夜轮班／单源不具备正文资格 |
| release-candidate-037 | exclude | 6 | — | 机械狂欢／单源不具备正文资格 |
| release-candidate-038 | exclude | 6 | — | 双点医院：满血痊愈典藏版／事件日期不在报告窗口 |
| release-candidate-039 | exclude | 6 | — | 异界宿帐／单源不具备正文资格 |
| release-candidate-040 | exclude | 6 | — | 漫威斗魂／单源不具备正文资格 |
| release-candidate-041 | exclude | 6 | — | 集合！浆果镇／单源不具备正文资格 |
| release-candidate-042 | exclude | 6 | — | 碧蓝航线／单源不具备正文资格 |
| release-candidate-043 | exclude | 6 | — | 暗区突围／事件日期不在报告窗口 |
| release-candidate-044 | exclude | 6 | — | 这龙带刀／单源不具备正文资格 |
| release-candidate-045 | exclude | 6 | — | 超级少女／事件日期不在报告窗口 |
| release-candidate-046 | exclude | 6 | — | 斯普拉遁 涂击队／单源不具备正文资格 |
| release-candidate-047 | exclude | 6 | — | 光环：战役进化／单源不具备正文资格 |
| release-candidate-048 | exclude | 6 | — | 饿狼传说：群狼之城／单源不具备正文资格 |
| release-candidate-049 | exclude | 6 | — | 降世神通 传奇：格斗游戏／事件日期不在报告窗口 |
| release-candidate-050 | exclude | 6 | — | 重返未来：1999／事件日期不在报告窗口 |
| release-candidate-051 | exclude | 6 | — | 漫威斗魂／单源不具备正文资格 |
| release-candidate-052 | exclude | 6 | — | 白银之城／事件日期不在报告窗口 |
| release-candidate-053 | exclude | 6 | — | 无尽废墟／单源不具备正文资格 |
| release-candidate-054 | exclude | 6 | — | 龙之剑／事件日期不在报告窗口 |
| release-candidate-055 | exclude | 6 | — | 杖剑传说／事件日期不在报告窗口 |
| release-candidate-056 | exclude | 6 | — | 明末／事件日期不在报告窗口 |
| release-candidate-057 | exclude | 6 | — | 内格利／事件日期不在报告窗口 |
| release-candidate-058 | exclude | 6 | — | 炎之鸟／事件日期不在报告窗口 |
| release-candidate-059 | exclude | 6 | — | 火柴盒小汽车大电影／事件日期不在报告窗口 |
| release-candidate-060 | exclude | 6 | — | Choppa： Rescue Rivals／单源不具备正文资格 |
| release-candidate-061 | exclude | 6 | — | 无尽废墟／单源不具备正文资格 |
| release-candidate-062 | exclude | 6 | — | 突击风暴：零点／单源不具备正文资格 |
| release-candidate-063 | exclude | 6 | — | 赛博朋克2077／单源不具备正文资格 |
| release-candidate-064 | exclude | 6 | — | 梦魇牌／事件日期不在报告窗口 |
| release-candidate-065 | exclude | 6 | — | 地牢大出血／事件日期不在报告窗口 |
| release-candidate-066 | exclude | 6 | — | 明末：渊虚之羽／单源不具备正文资格 |
| release-candidate-067 | exclude | 6 | — | 无尽虚空／事件日期不在报告窗口 |
| release-candidate-068 | exclude | 6 | — | 光环／单源不具备正文资格 |
| release-candidate-069 | exclude | 6 | — | BeastLink／事件日期不在报告窗口 |
| release-candidate-070 | exclude | 6 | — | 零度空间／单源不具备正文资格 |
| release-candidate-071 | exclude | 6 | — | 刺客信条／事件日期不在报告窗口 |
| release-candidate-072 | exclude | 6 | — | 赛博朋克2077／单源不具备正文资格 |
| release-candidate-073 | exclude | 6 | — | 突击风暴：零点／单源不具备正文资格 |
| release-candidate-074 | exclude | 6 | — | 无畏契约／单源不具备正文资格 |
| release-candidate-075 | exclude | 6 | — | 消逝的光芒2／事件日期不在报告窗口 |
| release-candidate-076 | exclude | 6 | — | Apex英雄／事件日期不在报告窗口 |
| release-candidate-077 | exclude | 6 | — | 足球教练／事件日期不在报告窗口 |
| release-candidate-078 | exclude | 6 | — | Shards of Order／单源不具备正文资格 |
| release-candidate-079 | exclude | 6 | — | 喂龙高手／事件日期不在报告窗口 |
| release-candidate-080 | exclude | 6 | — | 快乐树的朋友们／单源不具备正文资格 |
| release-candidate-081 | exclude | 4 | — | 渡渡鸭与折叠世界／单源不具备正文资格 |
| release-candidate-082 | exclude | 4 | — | 渡渡鸭与折叠世界／单源不具备正文资格 |
| release-candidate-083 | exclude | 4 | — | 龙之谷／单源不具备正文资格 |
| release-candidate-084 | exclude | 4 | — | 黑豹3／单源不具备正文资格 |
| release-candidate-085 | exclude | 4 | — | 古墓丽影：亚特兰蒂斯遗迹／单源不具备正文资格 |
| release-candidate-086 | exclude | 4 | — | 古墓丽影：亚特兰蒂斯遗迹／单源不具备正文资格 |
| release-candidate-087 | exclude | 4 | — | 杀死影子／单源不具备正文资格 |
| release-candidate-088 | exclude | 4 | — | 迈亚融解／单源不具备正文资格 |
| release-candidate-089 | exclude | 4 | — | 漫威斗魂／事件日期不在报告窗口 |
| release-candidate-090 | exclude | 3 | — | 拳皇全明星／单源不具备正文资格 |
| release-candidate-091 | exclude | 3 | — | 丹墨三国：弈／单源不具备正文资格 |
| release-candidate-092 | exclude | 3 | — | 使命召唤手游／单源不具备正文资格 |
| release-candidate-093 | exclude | 3 | — | 苏丹的游戏／单源不具备正文资格 |
| release-candidate-094 | exclude | 3 | — | MagicShooter／单源不具备正文资格 |
| release-candidate-095 | exclude | 3 | — | 万创修仙／单源不具备正文资格 |
| release-candidate-096 | exclude | 3 | — | 三国搜打撤・将星对决／单源不具备正文资格 |
| release-candidate-097 | exclude | 3 | — | 三脚猫行动／单源不具备正文资格 |
| release-candidate-098 | exclude | 3 | — | 专注农场／单源不具备正文资格 |
| release-candidate-099 | exclude | 3 | — | 乾坤袋大乱斗／单源不具备正文资格 |
| release-candidate-100 | exclude | 3 | — | 你来嘛英雄／单源不具备正文资格 |
| release-candidate-101 | exclude | 3 | — | 冒险之旅／单源不具备正文资格 |
| release-candidate-102 | exclude | 3 | — | 凡尘修道录／单源不具备正文资格 |
| release-candidate-103 | exclude | 3 | — | 十二生肖：决战牛顿／单源不具备正文资格 |
| release-candidate-104 | exclude | 3 | — | 友可赢／单源不具备正文资格 |
| release-candidate-105 | exclude | 3 | — | 回声地宫／单源不具备正文资格 |
| release-candidate-106 | exclude | 3 | — | 团子矿场／单源不具备正文资格 |
| release-candidate-107 | exclude | 3 | — | 夜话古今／单源不具备正文资格 |
| release-candidate-108 | exclude | 3 | — | 字不可挡／单源不具备正文资格 |
| release-candidate-109 | exclude | 3 | — | 弹弹收集家／单源不具备正文资格 |
| release-candidate-110 | exclude | 3 | — | 我即是天道／单源不具备正文资格 |
| release-candidate-111 | exclude | 3 | — | 我在废土当主播／单源不具备正文资格 |
| release-candidate-112 | exclude | 3 | — | 挂机刷装备／单源不具备正文资格 |
| release-candidate-113 | exclude | 3 | — | 挂机西游／单源不具备正文资格 |
| release-candidate-114 | exclude | 3 | — | 指点江山／单源不具备正文资格 |
| release-candidate-115 | exclude | 3 | — | 暗黑融合刷宝无限副本／单源不具备正文资格 |
| release-candidate-116 | exclude | 3 | — | 暗黑：深渊猎宝人／单源不具备正文资格 |
| release-candidate-117 | exclude | 3 | — | 木剑／单源不具备正文资格 |
| release-candidate-118 | exclude | 3 | — | 梦想英雄／单源不具备正文资格 |
| release-candidate-119 | exclude | 3 | — | 消消寻宝／单源不具备正文资格 |
| release-candidate-120 | exclude | 3 | — | 烧脑茬次元冒险／单源不具备正文资格 |
| release-candidate-121 | exclude | 3 | — | 王城守卫战／单源不具备正文资格 |
| release-candidate-122 | exclude | 3 | — | 疯人院之浮屠塔／单源不具备正文资格 |
| release-candidate-123 | exclude | 3 | — | 疯狂物理实验室／单源不具备正文资格 |
| release-candidate-124 | exclude | 3 | — | 百战天猫／单源不具备正文资格 |
| release-candidate-125 | exclude | 3 | — | 砍柴成为道祖／单源不具备正文资格 |
| release-candidate-126 | exclude | 3 | — | 给我守住！／单源不具备正文资格 |
| release-candidate-127 | exclude | 3 | — | 美梦物语／单源不具备正文资格 |
| release-candidate-128 | exclude | 3 | — | 脑力锻炼挑战／单源不具备正文资格 |
| release-candidate-129 | exclude | 3 | — | 荒野求生／单源不具备正文资格 |
| release-candidate-130 | exclude | 3 | — | 谁淹了我的世界／单源不具备正文资格 |
| release-candidate-131 | exclude | 3 | — | 贫僧略通拳脚／单源不具备正文资格 |
| release-candidate-132 | exclude | 3 | — | 资本航线商业人生／单源不具备正文资格 |
| release-candidate-133 | exclude | 3 | — | 赵云消消兵／单源不具备正文资格 |
| release-candidate-134 | exclude | 3 | — | 超市大亨／单源不具备正文资格 |
| release-candidate-135 | exclude | 3 | — | 金融投资模拟／单源不具备正文资格 |
| release-candidate-136 | exclude | 3 | — | 钢铁突击／单源不具备正文资格 |
| release-candidate-137 | exclude | 3 | — | 集装箱盲盒／单源不具备正文资格 |
| release-candidate-138 | exclude | 3 | — | 鲜活蝴蝶合集／单源不具备正文资格 |
| release-candidate-139 | exclude | 3 | — | 麒麟洲修心纪／单源不具备正文资格 |
| release-candidate-140 | exclude | 3 | — | 命运代码：侵入／单源不具备正文资格 |
| release-candidate-141 | exclude | 3 | — | 星际开荒模拟器／单源不具备正文资格 |
| release-candidate-142 | exclude | 3 | — | 我的奶茶屋／单源不具备正文资格 |
| release-candidate-143 | exclude | 3 | — | 追逐卡蕾多／单源不具备正文资格 |
| release-candidate-144 | exclude | 3 | — | 苍蓝避风港／单源不具备正文资格 |
| release-candidate-145 | exclude | 3 | — | 无职转生 ～到了异世界就拿出真本事～ 回响编年史-资讯服务／单源不具备正文资格 |
| release-candidate-146 | exclude | 3 | — | 王国保卫战6／单源不具备正文资格 |
| release-candidate-147 | exclude | 3 | — | 芙娅之魂-代号：魂游大世界／单源不具备正文资格 |
| release-candidate-148 | exclude | 3 | — | 苍蓝避风港(官服)／单源不具备正文资格 |
| release-candidate-149 | exclude | 3 | — | 一般武侠／单源不具备正文资格 |
| release-candidate-150 | exclude | 3 | — | 三脚猫行动／单源不具备正文资格 |
| release-candidate-151 | exclude | 3 | — | 为人方正闯江湖／单源不具备正文资格 |
| release-candidate-152 | exclude | 3 | — | 主簿别慌：汉末急务／单源不具备正文资格 |
| release-candidate-153 | exclude | 3 | — | 僵尸危机：校园封锁／单源不具备正文资格 |
| release-candidate-154 | exclude | 3 | — | 全球商业帝国／单源不具备正文资格 |
| release-candidate-155 | exclude | 3 | — | 再乱的货架我也能救回来／单源不具备正文资格 |
| release-candidate-156 | exclude | 3 | — | 友谊的小船／单源不具备正文资格 |
| release-candidate-157 | exclude | 3 | — | 反重力农场模拟器／单源不具备正文资格 |
| release-candidate-158 | exclude | 3 | — | 可蛙和嫑蛙的跳一跳／单源不具备正文资格 |
| release-candidate-159 | exclude | 3 | — | 周期／单源不具备正文资格 |
| release-candidate-160 | exclude | 3 | — | 地牢狂猎（删档测试版）／单源不具备正文资格 |
| release-candidate-161 | exclude | 3 | — | 墨刃斩群魔／单源不具备正文资格 |
| release-candidate-162 | exclude | 3 | — | 大明浮生志3／单源不具备正文资格 |
| release-candidate-163 | exclude | 3 | — | 奶茶店经营模拟器／单源不具备正文资格 |
| release-candidate-164 | exclude | 3 | — | 帝临：九霄梦回／单源不具备正文资格 |
| release-candidate-165 | exclude | 3 | — | 幻境大陆／单源不具备正文资格 |
| release-candidate-166 | exclude | 3 | — | 弹爆防线／单源不具备正文资格 |
| release-candidate-167 | exclude | 3 | — | 弹珠打砖块／单源不具备正文资格 |
| release-candidate-168 | exclude | 3 | — | 心乐计算器／单源不具备正文资格 |
| release-candidate-169 | exclude | 3 | — | 恋综模拟器／单源不具备正文资格 |
| release-candidate-170 | exclude | 3 | — | 拯救喵星／单源不具备正文资格 |
| release-candidate-171 | exclude | 3 | — | 拼豆工坊／单源不具备正文资格 |
| release-candidate-172 | exclude | 3 | — | 指尖仙守／单源不具备正文资格 |
| release-candidate-173 | exclude | 3 | — | 捂嘴战术／单源不具备正文资格 |
| release-candidate-174 | exclude | 3 | — | 方块创想家／单源不具备正文资格 |
| release-candidate-175 | exclude | 3 | — | 无序引力与空间／单源不具备正文资格 |
| release-candidate-176 | exclude | 3 | — | 明末御尸录／单源不具备正文资格 |
| release-candidate-177 | exclude | 3 | — | 浩瀚宇宙合集／单源不具备正文资格 |
| release-candidate-178 | exclude | 3 | — | 湮灭方程式／单源不具备正文资格 |
| release-candidate-179 | exclude | 3 | — | 灵魂秘境／单源不具备正文资格 |
| release-candidate-180 | exclude | 3 | — | 点点冒险团／单源不具备正文资格 |
| release-candidate-181 | exclude | 3 | — | 点点挖矿／单源不具备正文资格 |
| release-candidate-182 | exclude | 3 | — | 牛顿的苹果复仇记／单源不具备正文资格 |
| release-candidate-183 | exclude | 3 | — | 牛顿？胡言乱语！／单源不具备正文资格 |
| release-candidate-184 | exclude | 3 | — | 球球，滚吧！／单源不具备正文资格 |
| release-candidate-185 | exclude | 3 | — | 生物公司杀人案／单源不具备正文资格 |
| release-candidate-186 | exclude | 3 | — | 电摩公司模拟器／单源不具备正文资格 |
| release-candidate-187 | exclude | 3 | — | 疯狂竞拍／单源不具备正文资格 |
| release-candidate-188 | exclude | 3 | — | 砌长城／单源不具备正文资格 |
| release-candidate-189 | exclude | 3 | — | 禁汽年代：可乐贩卖师／单源不具备正文资格 |
| release-candidate-190 | exclude | 3 | — | 秦皇纪：天下一统／单源不具备正文资格 |
| release-candidate-191 | exclude | 3 | — | 精英部队／单源不具备正文资格 |
| release-candidate-192 | exclude | 3 | — | 肉鸽俄罗斯方块／单源不具备正文资格 |
| release-candidate-193 | exclude | 3 | — | 草木有灵／单源不具备正文资格 |
| release-candidate-194 | exclude | 3 | — | 越挖越有钱／单源不具备正文资格 |
| release-candidate-195 | exclude | 3 | — | 跨境电商／单源不具备正文资格 |
| release-candidate-196 | exclude | 3 | — | 金币推推乐／单源不具备正文资格 |
| release-candidate-197 | exclude | 3 | — | 问道山居／单源不具备正文资格 |
| release-candidate-198 | exclude | 3 | — | 高三最后300天／单源不具备正文资格 |
| release-candidate-199 | exclude | 3 | — | 高手来一局／单源不具备正文资格 |
| release-candidate-200 | exclude | 3 | — | 魔方五子棋／单源不具备正文资格 |
| release-candidate-201 | exclude | 3 | — | 黄油猫永动机／单源不具备正文资格 |
| release-candidate-202 | exclude | 3 | — | 大航海时代OL／单源不具备正文资格 |
| release-candidate-203 | exclude | 3 | — | 使命召唤手游／单源不具备正文资格 |
| release-candidate-204 | exclude | 3 | — | 大狗叫模拟器-玩家自制版／单源不具备正文资格 |
| release-candidate-205 | exclude | 3 | — | 没事甩两剑／单源不具备正文资格 |
| release-candidate-206 | exclude | 3 | — | 光阴之外／单源不具备正文资格 |
| release-candidate-207 | exclude | 3 | — | 魔神英雄传／单源不具备正文资格 |
| release-candidate-208 | exclude | 3 | — | 一刀就富／单源不具备正文资格 |
| release-candidate-209 | exclude | 3 | — | 一唱一和／单源不具备正文资格 |
| release-candidate-210 | exclude | 3 | — | 万灵之契／单源不具备正文资格 |
| release-candidate-211 | exclude | 3 | — | 三国无双／单源不具备正文资格 |
| release-candidate-212 | exclude | 3 | — | 丧尸校园／单源不具备正文资格 |
| release-candidate-213 | exclude | 3 | — | 乱世群英谱／单源不具备正文资格 |
| release-candidate-214 | exclude | 3 | — | 从一块田开始／单源不具备正文资格 |
| release-candidate-215 | exclude | 3 | — | 代码 vs Bug／单源不具备正文资格 |
| release-candidate-216 | exclude | 3 | — | 会计合伙人／单源不具备正文资格 |
| release-candidate-217 | exclude | 3 | — | 侏罗纪公园：失落之岛／单源不具备正文资格 |
| release-candidate-218 | exclude | 3 | — | 修仙割草：万法诛邪／单源不具备正文资格 |
| release-candidate-219 | exclude | 3 | — | 利维坦协议·奥德赛／单源不具备正文资格 |
| release-candidate-220 | exclude | 3 | — | 动物弹想曲／单源不具备正文资格 |
| release-candidate-221 | exclude | 3 | — | 反应闪击／单源不具备正文资格 |
| release-candidate-222 | exclude | 3 | — | 吐司JUMP／单源不具备正文资格 |
| release-candidate-223 | exclude | 3 | — | 哈萨克小羊换装工坊／单源不具备正文资格 |
| release-candidate-224 | exclude | 3 | — | 啵啵修复屋／单源不具备正文资格 |
| release-candidate-225 | exclude | 3 | — | 喵下留爪／单源不具备正文资格 |
| release-candidate-226 | exclude | 3 | — | 太空回收站／单源不具备正文资格 |
| release-candidate-227 | exclude | 3 | — | 奶蛙消消消／单源不具备正文资格 |
| release-candidate-228 | exclude | 3 | — | 实验结果：未知／单源不具备正文资格 |
| release-candidate-229 | exclude | 3 | — | 寿司点点消／单源不具备正文资格 |
| release-candidate-230 | exclude | 3 | — | 小说帝国物语／单源不具备正文资格 |
| release-candidate-231 | exclude | 3 | — | 异常来电中心／单源不具备正文资格 |
| release-candidate-232 | exclude | 3 | — | 弹幕幸存者／单源不具备正文资格 |
| release-candidate-233 | exclude | 3 | — | 恐龙冲刺／单源不具备正文资格 |
| release-candidate-234 | exclude | 3 | — | 拍蚊子／单源不具备正文资格 |
| release-candidate-235 | exclude | 3 | — | 拼少少／单源不具备正文资格 |
| release-candidate-236 | exclude | 3 | — | 挂机荒野塔防／单源不具备正文资格 |
| release-candidate-237 | exclude | 3 | — | 捡完就撤／单源不具备正文资格 |
| release-candidate-238 | exclude | 3 | — | 搞个毛球蛋呀／单源不具备正文资格 |
| release-candidate-239 | exclude | 3 | — | 暗区先锋／单源不具备正文资格 |
| release-candidate-240 | exclude | 3 | — | 次元召唤师／单源不具备正文资格 |
| release-candidate-241 | exclude | 3 | — | 残烬行者／单源不具备正文资格 |
| release-candidate-242 | exclude | 3 | — | 水墨五子 · 棋境／单源不具备正文资格 |
| release-candidate-243 | exclude | 3 | — | 治愈消消乐／单源不具备正文资格 |
| release-candidate-244 | exclude | 3 | — | 深山闲居／单源不具备正文资格 |
| release-candidate-245 | exclude | 3 | — | 港湾之夜空／单源不具备正文资格 |
| release-candidate-246 | exclude | 3 | — | 点石成金／单源不具备正文资格 |
| release-candidate-247 | exclude | 3 | — | 狗系统-末世后宫之旅／单源不具备正文资格 |
| release-candidate-248 | exclude | 3 | — | 猫猫罐头铺／单源不具备正文资格 |
| release-candidate-249 | exclude | 3 | — | 田园鲜蔬日记／单源不具备正文资格 |
| release-candidate-250 | exclude | 3 | — | 界行者：异兽觉醒／单源不具备正文资格 |
| release-candidate-251 | exclude | 3 | — | 番茄培育手记／单源不具备正文资格 |
| release-candidate-252 | exclude | 3 | — | 真实修仙模拟／单源不具备正文资格 |
| release-candidate-253 | exclude | 3 | — | 移动堡垒幸存者／单源不具备正文资格 |
| release-candidate-254 | exclude | 3 | — | 稳住别倒！／单源不具备正文资格 |
| release-candidate-255 | exclude | 3 | — | 绵软溪流合集／单源不具备正文资格 |
| release-candidate-256 | exclude | 3 | — | 翻箱倒柜／单源不具备正文资格 |
| release-candidate-257 | exclude | 3 | — | 胃袋之王／单源不具备正文资格 |
| release-candidate-258 | exclude | 3 | — | 萝卜耕植手记／单源不具备正文资格 |
| release-candidate-259 | exclude | 3 | — | 解压大炮／单源不具备正文资格 |
| release-candidate-260 | exclude | 3 | — | 谁出轨了／单源不具备正文资格 |
| release-candidate-261 | exclude | 3 | — | 财富时光机／单源不具备正文资格 |
| release-candidate-262 | exclude | 3 | — | 足球球星主理人／单源不具备正文资格 |
| release-candidate-263 | exclude | 3 | — | 钓鱼大亨：巨物猎手／单源不具备正文资格 |
| release-candidate-264 | exclude | 3 | — | 门楣：百世家书／单源不具备正文资格 |
| release-candidate-265 | exclude | 3 | — | 霓虹碰碰车／单源不具备正文资格 |
| release-candidate-266 | exclude | 3 | — | 领主无双／单源不具备正文资格 |
| release-candidate-267 | exclude | 3 | — | 飞往乌托邦／单源不具备正文资格 |
| release-candidate-268 | exclude | 3 | — | 飞机大战／单源不具备正文资格 |
| release-candidate-269 | exclude | 3 | — | 飞驰赛车／单源不具备正文资格 |
| release-candidate-270 | exclude | 3 | — | 魔法推币机／单源不具备正文资格 |
| release-candidate-271 | exclude | 3 | — | 麻将消消乐／单源不具备正文资格 |
| release-candidate-272 | exclude | 3 | — | Finovia Fish： Catch Simulator／单源不具备正文资格 |
| release-candidate-273 | exclude | 3 | — | 地下城与勇士：起源／单源不具备正文资格 |
| release-candidate-274 | exclude | 3 | — | 奥特曼英雄决战／单源不具备正文资格 |
| release-candidate-275 | exclude | 3 | — | 82胜／单源不具备正文资格 |
| release-candidate-276 | exclude | 3 | — | lovania叫叫／单源不具备正文资格 |
| release-candidate-277 | exclude | 3 | — | 一刀拿捏了／单源不具备正文资格 |
| release-candidate-278 | exclude | 3 | — | 不存在的404号房／单源不具备正文资格 |
| release-candidate-279 | exclude | 3 | — | 乱画猜猜看／单源不具备正文资格 |
| release-candidate-280 | exclude | 3 | — | 代号：暗影猎手／单源不具备正文资格 |
| release-candidate-281 | exclude | 3 | — | 修仙异闻录／单源不具备正文资格 |
| release-candidate-282 | exclude | 3 | — | 修仙模拟器-逍遥录／单源不具备正文资格 |
| release-candidate-283 | exclude | 3 | — | 像素备菜厨房／单源不具备正文资格 |
| release-candidate-284 | exclude | 3 | — | 先古之渊：遗迹／单源不具备正文资格 |
| release-candidate-285 | exclude | 3 | — | 养条锦鲤转个运吧／单源不具备正文资格 |
| release-candidate-286 | exclude | 3 | — | 冷冽折扇合集／单源不具备正文资格 |
| release-candidate-287 | exclude | 3 | — | 功夫足球模拟器／单源不具备正文资格 |
| release-candidate-288 | exclude | 3 | — | 历史大乱炖2／单源不具备正文资格 |
| release-candidate-289 | exclude | 3 | — | 县令的日常／单源不具备正文资格 |
| release-candidate-290 | exclude | 3 | — | 口袋方块／单源不具备正文资格 |
| release-candidate-291 | exclude | 3 | — | 命运骰子3D／单源不具备正文资格 |
| release-candidate-292 | exclude | 3 | — | 咯咯哒农场／单源不具备正文资格 |
| release-candidate-293 | exclude | 3 | — | 囚笼界限／单源不具备正文资格 |
| release-candidate-294 | exclude | 3 | — | 太空战机 SKY STRIKER／单源不具备正文资格 |
| release-candidate-295 | exclude | 3 | — | 太箭了／单源不具备正文资格 |
| release-candidate-296 | exclude | 3 | — | 宝石消消乐／单源不具备正文资格 |
| release-candidate-297 | exclude | 3 | — | 小怪物别追我／单源不具备正文资格 |
| release-candidate-298 | exclude | 3 | — | 小摊自动印钞机／单源不具备正文资格 |
| release-candidate-299 | exclude | 3 | — | 山海夜行录／单源不具备正文资格 |
| release-candidate-300 | exclude | 3 | — | 幻境领主／单源不具备正文资格 |
| release-candidate-301 | exclude | 3 | — | 引力弹弓·归星／单源不具备正文资格 |
| release-candidate-302 | exclude | 3 | — | 弹跃奇点／单源不具备正文资格 |
| release-candidate-303 | exclude | 3 | — | 心理年龄测试／单源不具备正文资格 |
| release-candidate-304 | exclude | 3 | — | 我的小孩／单源不具备正文资格 |
| release-candidate-305 | exclude | 3 | — | 抢车位：华夏崛起／单源不具备正文资格 |
| release-candidate-306 | exclude | 3 | — | 敢交技能／单源不具备正文资格 |
| release-candidate-307 | exclude | 3 | — | 无尽狂潮／单源不具备正文资格 |
| release-candidate-308 | exclude | 3 | — | 星渊共生体／单源不具备正文资格 |
| release-candidate-309 | exclude | 3 | — | 星铃小队的魔法塔／单源不具备正文资格 |
| release-candidate-310 | exclude | 3 | — | 极简幸存者／单源不具备正文资格 |
| release-candidate-311 | exclude | 3 | — | 每秒1属性，3天打爆星河／单源不具备正文资格 |
| release-candidate-312 | exclude | 3 | — | 海上60秒生存海上荒岛求生存／单源不具备正文资格 |
| release-candidate-313 | exclude | 3 | — | 海边钓鱼／单源不具备正文资格 |
| release-candidate-314 | exclude | 3 | — | 涂鸦战机／单源不具备正文资格 |
| release-candidate-315 | exclude | 3 | — | 潘多拉余烬／单源不具备正文资格 |
| release-candidate-316 | exclude | 3 | — | 灵雀迹／单源不具备正文资格 |
| release-candidate-317 | exclude | 3 | — | 皮总回来吧模拟器／单源不具备正文资格 |
| release-candidate-318 | exclude | 3 | — | 秘境之印／单源不具备正文资格 |
| release-candidate-319 | exclude | 3 | — | 称帝从选择开始／单源不具备正文资格 |
| release-candidate-320 | exclude | 3 | — | 程序员创业之游戏公司模拟器／单源不具备正文资格 |
| release-candidate-321 | exclude | 3 | — | 终场前：足球生涯／单源不具备正文资格 |
| release-candidate-322 | exclude | 3 | — | 脑力寻茬乐／单源不具备正文资格 |
| release-candidate-323 | exclude | 3 | — | 脑茬找梗／单源不具备正文资格 |
| release-candidate-324 | exclude | 3 | — | 芋圆炸弹斗地主／单源不具备正文资格 |
| release-candidate-325 | exclude | 3 | — | 荒镜生存／单源不具备正文资格 |
| release-candidate-326 | exclude | 3 | — | 萌宠对决自走棋／单源不具备正文资格 |
| release-candidate-327 | exclude | 3 | — | 裂隙连闪／单源不具备正文资格 |
| release-candidate-328 | exclude | 3 | — | 诡异搜打撤我能驾驭S级诡异／单源不具备正文资格 |
| release-candidate-329 | exclude | 3 | — | 轻功凌霄／单源不具备正文资格 |
| release-candidate-330 | exclude | 3 | — | 这块石头值千万／单源不具备正文资格 |
| release-candidate-331 | exclude | 3 | — | 防线出击／单源不具备正文资格 |
| release-candidate-332 | exclude | 3 | — | 魂环大陆／单源不具备正文资格 |
| release-candidate-333 | exclude | 3 | — | 麻将连连看／单源不具备正文资格 |
| release-candidate-334 | exclude | 3 | — | 黄金矿工：大乱斗／单源不具备正文资格 |
| release-candidate-335 | exclude | 3 | — | 三国策：万人策略对战／单源不具备正文资格 |
| release-candidate-336 | exclude | 3 | — | Bird Gone Wild： Fun Pigeon／单源不具备正文资格 |
| release-candidate-337 | exclude | 3 | — | 战斗吧！艾莉娜-拉比哩比Rabi·Ribi／单源不具备正文资格 |
| release-candidate-338 | exclude | 3 | — | 灰境行者 PC/主机／单源不具备正文资格 |
| release-candidate-339 | exclude | 3 | — | 米塔／单源不具备正文资格 |
| release-candidate-340 | exclude | 3 | — | 舞力全开：派对／单源不具备正文资格 |
| release-candidate-341 | exclude | 3 | — | 雾影猎人 PC/主机／单源不具备正文资格 |
| release-candidate-342 | exclude | 3 | — | 九界降魔／单源不具备正文资格 |
| release-candidate-343 | exclude | 3 | — | 三国合字塔防／单源不具备正文资格 |
| release-candidate-344 | exclude | 3 | — | 乐拾小记／单源不具备正文资格 |
| release-candidate-345 | exclude | 3 | — | 人物跳一跳／单源不具备正文资格 |
| release-candidate-346 | exclude | 3 | — | 今晚还有腿吗／单源不具备正文资格 |
| release-candidate-347 | exclude | 3 | — | 传奇文字大冒险／单源不具备正文资格 |
| release-candidate-348 | exclude | 3 | — | 侠义无双／单源不具备正文资格 |
| release-candidate-349 | exclude | 3 | — | 修仙／单源不具备正文资格 |
| release-candidate-350 | exclude | 3 | — | 像素贪吃蛇／单源不具备正文资格 |
| release-candidate-351 | exclude | 3 | — | 剑气之地／单源不具备正文资格 |
| release-candidate-352 | exclude | 3 | — | 动物增量斗兽场／单源不具备正文资格 |
| release-candidate-353 | exclude | 3 | — | 口袋百玩／单源不具备正文资格 |
| release-candidate-354 | exclude | 3 | — | 复古像素消消乐／单源不具备正文资格 |
| release-candidate-355 | exclude | 3 | — | 天地英雄／单源不具备正文资格 |
| release-candidate-356 | exclude | 3 | — | 山村校长日记／单源不具备正文资格 |
| release-candidate-357 | exclude | 3 | — | 弈阵／单源不具备正文资格 |
| release-candidate-358 | exclude | 3 | — | 彩色连连看／单源不具备正文资格 |
| release-candidate-359 | exclude | 3 | — | 战场风云／单源不具备正文资格 |
| release-candidate-360 | exclude | 3 | — | 拍卖大师／单源不具备正文资格 |
| release-candidate-361 | exclude | 3 | — | 数独征服者／单源不具备正文资格 |
| release-candidate-362 | exclude | 3 | — | 斗战斗魂／单源不具备正文资格 |
| release-candidate-363 | exclude | 3 | — | 无双战意／单源不具备正文资格 |
| release-candidate-364 | exclude | 3 | — | 星座大冒险／单源不具备正文资格 |
| release-candidate-365 | exclude | 3 | — | 星环守卫／单源不具备正文资格 |
| release-candidate-366 | exclude | 3 | — | 暗黑弹球：深渊守塔／单源不具备正文资格 |
| release-candidate-367 | exclude | 3 | — | 暗黑梦幻神兵／单源不具备正文资格 |
| release-candidate-368 | exclude | 3 | — | 末日喋血双雄／单源不具备正文资格 |
| release-candidate-369 | exclude | 3 | — | 松弛收纳馆／单源不具备正文资格 |
| release-candidate-370 | exclude | 3 | — | 格子别回头／单源不具备正文资格 |
| release-candidate-371 | exclude | 3 | — | 没事甩两剑／单源不具备正文资格 |
| release-candidate-372 | exclude | 3 | — | 渊海遗志／单源不具备正文资格 |
| release-candidate-373 | exclude | 3 | — | 溜溜的连连看／单源不具备正文资格 |
| release-candidate-374 | exclude | 3 | — | 猎影／单源不具备正文资格 |
| release-candidate-375 | exclude | 3 | — | 猫咪数独／单源不具备正文资格 |
| release-candidate-376 | exclude | 3 | — | 电商店长模拟器／单源不具备正文资格 |
| release-candidate-377 | exclude | 3 | — | 疯狂保卫战／单源不具备正文资格 |
| release-candidate-378 | exclude | 3 | — | 盖高楼／单源不具备正文资格 |
| release-candidate-379 | exclude | 3 | — | 签签入圣／单源不具备正文资格 |
| release-candidate-380 | exclude | 3 | — | 糟糕！我被女忍包围了！2／单源不具备正文资格 |
| release-candidate-381 | exclude | 3 | — | 素净梨花合集／单源不具备正文资格 |
| release-candidate-382 | exclude | 3 | — | 脑洞智多星／单源不具备正文资格 |
| release-candidate-383 | exclude | 3 | — | 蛊道无极／单源不具备正文资格 |
| release-candidate-384 | exclude | 3 | — | 西游记：灵山之后／单源不具备正文资格 |
| release-candidate-385 | exclude | 3 | — | 走，赶海去！／单源不具备正文资格 |
| release-candidate-386 | exclude | 3 | — | 越挖越有钱／单源不具备正文资格 |
| release-candidate-387 | exclude | 3 | — | 轨道铸造局／单源不具备正文资格 |
| release-candidate-388 | exclude | 3 | — | 转转修仙／单源不具备正文资格 |
| release-candidate-389 | exclude | 3 | — | 轻轻听／单源不具备正文资格 |
| release-candidate-390 | exclude | 3 | — | 进化失控／单源不具备正文资格 |
| release-candidate-391 | exclude | 3 | — | 重生之我在北上深／单源不具备正文资格 |
| release-candidate-392 | exclude | 3 | — | 闲着玩一下／单源不具备正文资格 |
| release-candidate-393 | exclude | 3 | — | 集装箱盲盒／单源不具备正文资格 |
| release-candidate-394 | exclude | 3 | — | 风投大亨／单源不具备正文资格 |
| release-candidate-395 | exclude | 3 | — | 魔力纪元／单源不具备正文资格 |
| release-candidate-396 | exclude | 3 | — | 魔王无限挂机吞噬／单源不具备正文资格 |
| release-candidate-397 | exclude | 3 | — | 麻酱消消／单源不具备正文资格 |
| release-candidate-398 | exclude | 2 | — | 英雄防线／单源不具备正文资格 |
| release-candidate-399 | exclude | 2 | — | 奥特曼英雄决战／单源不具备正文资格 |
| release-candidate-400 | exclude | 2 | — | 斗破苍穹：斗帝之路-预下载／单源不具备正文资格 |
| release-candidate-401 | exclude | 2 | — | 斗破苍穹：斗帝之路／单源不具备正文资格 |
| release-candidate-402 | exclude | 2 | — | 龙之谷：启程／单源不具备正文资格 |
| release-candidate-403 | exclude | 2 | — | 应征入伍-多人大战场射击／单源不具备正文资格 |
| release-candidate-404 | exclude | 2 | — | 代号：微光／单源不具备正文资格 |
| release-candidate-405 | exclude | 2 | — | 格斗对决／单源不具备正文资格 |
| release-candidate-406 | exclude | 2 | — | 深岩银河：幸存者／单源不具备正文资格 |
| release-candidate-407 | exclude | 2 | — | 热血江湖：觉醒-预下载／单源不具备正文资格 |
| release-candidate-408 | exclude | 2 | — | 梦幻足球-预下载／单源不具备正文资格 |
| release-candidate-409 | exclude | 2 | — | 热血江湖：觉醒／单源不具备正文资格 |
| release-candidate-410 | exclude | 2 | — | 梅莫莉：治愈物语／单源不具备正文资格 |
| release-candidate-411 | exclude | 2 | — | 神之一手／事件日期不在报告窗口 |
| release-candidate-412 | exclude | 2 | — | EA SPORTS FC 27／事件日期不在报告窗口 |
| release-candidate-413 | exclude | 2 | — | 漫威金刚狼／事件日期不在报告窗口 |
| release-candidate-414 | exclude | 2 | — | 控制：共振／事件日期不在报告窗口 |
| release-candidate-415 | exclude | 2 | — | 遗物：第一守护者／事件日期不在报告窗口 |
| release-candidate-416 | exclude | 2 | — | 加菲猫：逃离星期一／事件日期不在报告窗口 |
| release-candidate-417 | exclude | 2 | — | 潜行者2／事件日期不在报告窗口 |
| release-candidate-418 | exclude | 2 | — | 共鸣：瘟疫传说传承／事件日期不在报告窗口 |
| release-candidate-419 | exclude | 2 | — | 最终幻想14／事件日期不在报告窗口 |
| release-candidate-420 | exclude | 2 | — | 仁王3／事件日期不在报告窗口 |
| release-candidate-421 | exclude | 2 | — | 光环／单源不具备正文资格 |
| release-candidate-422 | exclude | 2 | 网易 | 抵抗者／单源不具备正文资格 |
| release-candidate-423 | exclude | 2 | — | 战锤40K：战争黎明4／事件日期不在报告窗口 |
| release-candidate-424 | exclude | 1 | — | 破碎之境：重启航线／单源不具备正文资格 |
