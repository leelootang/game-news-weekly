# Event Candidates

- 全量输入：1826 条；industry_news 872、ai_trends 94、community_discourse 216、deep_analysis 9、release_calendar 635。
- 全量正文与无截断 index 已反扫；E=0/非候选行业记录在 selection_decisions.json 逐源留痕。
- 产品日历全部节点以 release_calendar_audit.json 为真源，并由 sync_release_decisions.py 确定性决策。

## industry-001 - 昆仑万维拟出售闲徕互娱控股权
- section: industry_news
- status: candidate
- source_ids: S0927, S1067
- entities: 昆仑万维, 闲徕互娱, 北京星澜互娱
- facts: 已读 source text；E3×R3+M2=11，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-002 - 新品首次公开并开启首测招募
- section: industry_news
- status: candidate
- source_ids: S0550, S0731
- entities: 网易, 雾海之下
- facts: 已读 source text；E3×R3+M2=11，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-003 - Tripledot收购Supersonic
- section: industry_news
- status: candidate
- source_ids: S0056, S0070, S0150, S0180
- entities: Tripledot, Supersonic, Unity
- facts: 已读 source text；E3×R3+M2=11，达到周报阈值；历史完整报告已收录但订阅卡片未曝光，本期唯一内部卡片补位
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-004 - 核心发行人员任职状态变化
- section: industry_news
- status: candidate
- source_ids: S0524, S0550
- entities: 西山居, 尘白禁区, 林增鸿
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-005 - 国产叙事独立游戏进入配音与测试准备阶段
- section: industry_news
- status: candidate
- source_ids: S0553
- entities: Suspense Games, 声探疑云, 魏嘉
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-006 - 国产单机项目首次公开试玩并切换研发阶段
- section: industry_news
- status: candidate
- source_ids: S0577
- entities: 浩汤科技, 抵抗者
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-007 - 核心主创公开确认项目终止研发
- section: industry_news
- status: candidate
- source_ids: S0040, S0731
- entities: 网易, 剑心雕龙, 工长君
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值；相对历史新增当事人确认与团队规模
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-008 - 国产微恐模拟经营新作进入测试
- section: industry_news
- status: candidate
- source_ids: S0748
- entities: 厦门泡游, 代号：城中村
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-009 - 董事会修改ADS回购计划期限
- section: industry_news
- status: candidate
- source_ids: S0732
- entities: 搜狐
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-010 - 完美世界认购新兴科技创投基金
- section: industry_news
- status: candidate
- source_ids: S1266
- entities: 完美世界, 深圳市机智登月贰号创业投资企业
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-011 - 穿越火线IP首次公开买断制3A叙事单机
- section: industry_news
- status: candidate
- source_ids: S1258
- entities: 腾讯, Smilegate, That's No Moon, 穿越火线：潜伏
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-012 - 莉莉丝披露多个在研与上线产品节点
- section: industry_news
- status: candidate
- source_ids: S1268
- entities: 莉莉丝, Beboo Bash, Rangelords: Last Stand, Warline: Sniper Strike
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-013 - 上市公司收购游戏公司控股权并设置业绩承诺
- section: industry_news
- status: candidate
- source_ids: S1626
- entities: 嘉耀控股, 九万里科技
- facts: 已读 source text；E3×R3+M1=10，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-014 - Sensor Tower发布2026年7月全球手游收入与下载数据
- section: industry_news
- status: candidate
- source_ids: S0912, S1224
- entities: Sensor Tower, 王者荣耀, Roblox, 全球手游市场
- facts: 已读 source text；E2×R3+M2=8，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-015 - 腾讯发布2026年第二季度游戏业务数据
- section: industry_news
- status: candidate
- source_ids: S1267
- entities: 腾讯, 洛克王国：世界, 三角洲行动, Miniclip
- facts: 已读 source text；E2×R3+M2=8，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## industry-016 - Roblox推出课堂游戏开发资源
- section: industry_news
- status: candidate
- source_ids: S1269
- entities: Roblox, Digital Schoolhouse, Roblox Studio
- facts: 已读 source text；E2×R3+M2=8，达到周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## repeat-ea - EA私有化后披露年度成本削减计划
- section: industry_news
- status: candidate
- source_ids: S0013
- entities: Electronic Arts
- facts: 已读 source text；总分7，低于周报阈值；历史同一私有化事件已有卡片曝光
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## repeat-devolver - Devolver退市私有化方案晚到转载
- section: industry_news
- status: candidate
- source_ids: S0158
- entities: Devolver Digital
- facts: 已读 source text；总分7，低于周报阈值；历史同一事件未卡片曝光但不满足本期分数线
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## repeat-lastsentinel - Last Sentinel裁员事件晚到转载
- section: industry_news
- status: candidate
- source_ids: S0413
- entities: 腾讯光子, Last Sentinel
- facts: 已读 source text；历史同一事件已卡片曝光，无实质新状态
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## repeat-kaleido - 追逐卡蕾多首测与团队定位重复报道
- section: industry_news
- status: candidate
- source_ids: S0033
- entities: 腾讯, 追逐卡蕾多
- facts: 已读 source text；历史同一事件已卡片曝光，无实质新增事实
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## repeat-sega - 世嘉上海公司设立背景回顾
- section: industry_news
- status: candidate
- source_ids: S1263
- entities: 世嘉, 世嘉上海
- facts: 已读 source text；历史同一事件已卡片曝光，新增内容为旧背景
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## repeat-tata - 塔塔冒险队两个月流水重复报道
- section: industry_news
- status: candidate
- source_ids: S1066
- entities: 莉莉丝, 塔塔冒险队
- facts: 已读 source text；历史同一事件未卡片曝光但总分7，低于周报阈值
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## boundary-taketwo - 取消未公开核心IP项目
- section: industry_news
- status: candidate
- source_ids: S0058
- entities: Take-Two
- facts: 已读 source text；E2×R2+M2=6，低于周报阈值8
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## boundary-blizzard - 泄露邮件披露暴雪为Xbox表现最佳工作室
- section: industry_news
- status: candidate
- source_ids: S0947
- entities: Blizzard, Xbox
- facts: 已读 source text；E2×R2+M2=6，低于周报阈值8
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## boundary-valve - Steam硬件客户数据在物流商网络攻击中暴露
- section: industry_news
- status: candidate
- source_ids: S0949
- entities: Valve, Steam
- facts: 已读 source text；E2×R2+M2=6，低于周报阈值8
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## boundary-pokemon - 十周年月收入达到四年高点
- section: industry_news
- status: candidate
- source_ids: S1285
- entities: Pokémon Go
- facts: 已读 source text；E1×R3+M2=5，低于周报阈值8
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## boundary-amazon - Amazon退出两款MMO发行职责
- section: industry_news
- status: candidate
- source_ids: S1639
- entities: Amazon Games, Lost Ark, Throne and Liberty
- facts: 已读 source text；E2×R2+M2=6，低于周报阈值8
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## cross-release-wanxiangqi - 新品定档9月并披露预约数据
- section: industry_news
- status: candidate
- source_ids: S0551
- entities: 腾讯, 王者万象棋
- facts: 已读 source text；同一事件转入产品日历，避免跨栏重复
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## cross-release-xiaobingbing - 新品不删档测试
- section: industry_news
- status: candidate
- source_ids: S0746
- entities: 莉莉丝, 小冰冰斗蛐蛐
- facts: 已读 source text；同一事件转入产品日历，避免跨栏重复
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## cross-ai-bside - AI互动产品停止运营
- section: industry_news
- status: candidate
- source_ids: S0928
- entities: 米哈游, BSide: Olivia Lin
- facts: 已读 source text；事件核心为AI互动产品生命周期，转入AI新闻
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## ai-001 - 腾讯披露游戏AI的直接应用
- section: ai_trends
- status: candidate
- source_ids: S1250, S1253
- entities: 腾讯, 混元, 和平精英, 三角洲行动
- facts: 已读 source text；AI直接作用于游戏研发、产品、发行或运营，证据完整
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## ai-002 - 游戏确认AI生成式NPC对话功能
- section: ai_trends
- status: candidate
- source_ids: S1275, S1359
- entities: Saber Interactive, Rideshare Stimulator
- facts: 已读 source text；AI直接作用于游戏研发、产品、发行或运营，证据完整
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## ai-003 - 大模型团队招聘游戏研发人才参与训练数据与评测
- section: ai_trends
- status: candidate
- source_ids: S0035
- entities: DeepSeek招聘游戏开发数据工程师，让游戏研发经验进入模型训练与评测
- facts: 已读 source text；AI直接作用于游戏研发、产品、发行或运营，证据完整
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## ai-004 - 在实时虚拟经济中研究自主智能体
- section: ai_trends
- status: candidate
- source_ids: S0755
- entities: Fenris Creations, EVE Frontier
- facts: 已读 source text；AI直接作用于游戏研发、产品、发行或运营，证据完整
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## ai-005 - AI音乐互动陪伴产品停止运营
- section: ai_trends
- status: candidate
- source_ids: S0922, S0928, S1206
- entities: 米哈游, BSide: Olivia Lin
- facts: 已读 source text；AI直接作用于游戏研发、产品、发行或运营，证据完整
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## ai-006 - AI广告平台直接作用于游戏增长业务
- section: ai_trends
- status: candidate
- source_ids: S0754
- entities: Unity, Vector AI
- facts: 已读 source text；AI直接作用于游戏研发、产品、发行或运营，证据完整
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## community-001 - 联动素材水印引发AI审校争议
- section: community_discourse
- status: candidate
- source_ids: S0348, S0539
- entities: 《重返未来：1999》联动素材残留豆包水印，玩家质疑AI素材审校流程
- facts: 已读 source text；触发、争议逻辑、时间线与后续扫描完整，进入周报3条上限
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## community-002 - 第二赛季延期后的社区担忧
- section: community_discourse
- status: candidate
- source_ids: S1202
- entities: 王者荣耀世界
- facts: 已读 source text；触发、争议逻辑、时间线与后续扫描完整，进入周报3条上限
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## community-003 - 周年限定角色技能文本调整争议
- section: community_discourse
- status: candidate
- source_ids: S1546
- entities: 无期迷途
- facts: 已读 source text；触发、争议逻辑、时间线与后续扫描完整，进入周报3条上限
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## deep-C003 - Friendslop游戏颠覆了LiveOps等于长期重投入的认知
- section: deep_analysis
- status: candidate
- source_ids: S0901
- entities: Friendslop游戏颠覆了LiveOps等于长期重投入的认知
- facts: 已读 source text；目标周报精确selection中的用户明确选择
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## deep-C004 - 工具与分发都被“民主化”后，游戏发现的瓶颈从准入转向穿透过滤泡
- section: deep_analysis
- status: candidate
- source_ids: S0547
- entities: 工具与分发都被“民主化”后，游戏发现的瓶颈从准入转向穿透过滤泡
- facts: 已读 source text；目标周报精确selection中的用户明确选择
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。

## deep-C002 - 大额外包订单退潮后，全流程开发商从规模扩张转向预算适配与风险共担
- section: deep_analysis
- status: candidate
- source_ids: S1222
- entities: 大额外包订单退潮后，全流程开发商从规模扩张转向预算适配与风险共担
- facts: 已读 source text；目标周报精确selection中的用户明确选择
- notes: 最终 include/exclude 与历史曝光判断见 selection_decisions.md/json。
