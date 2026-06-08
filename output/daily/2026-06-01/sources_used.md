# 本日报使用的数据来源｜2026-06-01

## 本地输入文件夹

- `news_data/ai_trends/2026-06-01/`
- `news_data/community_discourse/2026-06-01/`
- `news_data/deep_analysis/2026-06-01/`
- `news_data/industry_news/2026-06-01/`
- `news_data/release_calendar/2026-06-01/`

## 抽取产物

- `_intermediate/report_inputs.jsonl`（197 条记录，0 提取失败，0 条 text 为空）
- `_intermediate/report_inputs_summary.md`
- `_intermediate/report_inputs_index.md`
- `_intermediate/event_candidates.md`
- `_intermediate/selection_decisions.md`

## Item Source Map
### 一、行业新闻

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | Atari 收购《Crossy Road》开发商 Hipster Whale，补强移动端 | S0037, S0042, S0044, S0068 | gamesindustry.biz / mobilegamer.biz / pocketgamer.biz / gamedeveloper.com |
| 2 | CD Projekt 将《巫师4》推进到"最密集"开发阶段 | S0030 | gamesindustry.biz |
| 3 | 腾讯据称为《三角洲行动》筹备 UGC 平台 | S0034 | pocketgamer.biz |
| 4 | 诗悦网络《望月》公布新实机 PV，6/19—21 在广州开线下试玩 | S0002, S0017 | gamelook.com.cn / youxituoluo.com（陀螺周报）|
| 5 | 《Block Blast!》遭 Google Play 下架，超大 DAU 出海产品平台风险被放大 | S0008 | youxituoluo.com |
| 6 | 《神鬼寓言》延期至 2027 年 2 月，Xbox 一方独占节奏再被推迟 | S0048, S0027, S0067 | gcores.com / gamesindustry.biz / gamedeveloper.com |
| 7 | 美国"付费游戏在服务停运后仍须可玩"法案过初投票 | S0051 | videogameschronicle.com |
| 8 | 友谊时光端出首款乙游《心跳陷落》（borderline） | S0031 | new.qq.com |
| 9 | 网易雷火《归唐》将于夏日游戏节释出新消息（borderline） | S0033 | gcores.com |
| 10 | 灵犀互娱《宗师之上》冲入 iOS 畅销榜 TOP10（borderline） | S0001 | gamelook.com.cn |

### 二、AI 新闻

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | 智能体从模型能力走向记忆、部署和服务入口 | S0080, S0081, S0086 | x.com (腾讯混元) / openai.com / ithome.com |
| 2 | 微短小游戏《一箭又一箭》：AI 全自动生成关卡（borderline） | S0012 | youxituoluo.com |

### 三、新游发布 / 产品日历

| # | 游戏 | source_ids | 本地证据信号 |
| --- | --- | --- | --- |
| 1 | 产品日历 - 崩坏：星穹铁道 | S0108, S0110 | 两个 calendar 源（17173 + 3839）同时记录 4.3 版本「沉于生者的忘川」|
| 2 | 产品日历 - 明日方舟 | S0114, S0149 | 两个 calendar 源（3839 + taptap）同时记录《怪物猎人》联动 |
| 3 | 产品日历 - 最终的梦幻岛 | S0111, S0166 | 两个 calendar 源（16p + 3839）记录 6/1 删档计费/限量测试 |
| 4 | 产品日历 - 代号：地心 | S0100, S0180 | 两个 calendar 源（3839 + taptap）记录 6/1 预约 + 招募、6/12 首测（borderline）|

### 四、玩家舆论 / 社区动态

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | 《重返未来：1999》3.7 版本 PV 收 240 万差评，制作组长文致歉 | S0004 | gamelook.com.cn |
| 2 | 《燕云十六声》新地图 NPC 文案争议延续到修改后 | S0189 | bbs.nga.cn |

### 五、行业精选 / 深度观察

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | Scopely 的移动帝国显示出"高集中度组合"的机会与风险 | S0196 | naavik.co |
| 2 | 吉比特《杖剑传说》一周年案例：小团队、长周期、轻量 MMO 的反向跑通（borderline） | S0005 | m.sohu.com（游戏葡萄）|
| 3 | Call of Duty 在 GTA 6 阴影下的反弹尝试（borderline） | S0197 | thegamebusiness.com |

## 排除条目（值得审计留痕）

| 标题 | source_ids | 排除理由 |
| --- | --- | --- |
| Rockstar 工会成立 | S0032, S0035 | 用户反馈：西方主机 3A 劳资治理与用户业务实操参考意义弱 |
| 决胜巅峰 MSC/MWI 2026 电竞世俱杯赛制扩容 | S0064 | Hard Stop：决胜巅峰 / Moonton / MLBB 屏蔽规则 |
| OpenAI Stargate 1GW 数据中心开工 | S0084 | 基础设施信号，与游戏直接相关度低 |
| 4 月全球 AI 应用下载收缩 | S0050 | 市场背景，与游戏行业操作间接 |
| 《龙之谷：启程》宣传图疑似使用 LoL 龙王皮肤 | S0194 | 单源单线，玩家指控未证实 |
| 少女前线设定集 U 盘缺录 OST | S0195 | 售后小事件，体量不够 |
| 《铁拳8》总监池田离职 | S0047 | 用户反馈：海外老 IP + 端/主机格斗作品的人事变动与用户业务弱相关 |
| 卡厄斯梦境开服 BUG 封号（已确认假瓜）| S0188 | up 主已承认造谣，信息不实 |
| Asus ROG Xbox Ally X20 掌机 | S0052 | 主机/掌机硬件规格更新 |
| China approves 158 games in May | S0058 | 常规版号发放，按 SKILL 排除 |

## 缺失目录 / 数据缺口

- 本版基于 6/1 采集器补跑后的重新抽取（197 条记录，0 失败 / 0 空 text）。
- 较旧版（218 条）AI 与社区源构成发生变化：旧版正文的「MiniMax M3」（minimax.io）与「鸣潮 Warframe + 开发者访谈」在补跑后的本地数据中已无对应记录，按 Hard Stop（每条事实须可在 source text 找到）从正文剔除，AI 段由 3 条收为 2 条、社区段由 3 条收为 2 条。

## Hard Stops 自检

| # | 项 | 状态 |
|---|---|---|
| 1 | lint 零 error | ✅（industry 10 条为高新闻密度日的高价值例外，count 警告预期）|
| 2 | 正文无沐瞳 / MLBB / 决胜巅峰 | ✅（决胜巅峰 EWC 候选 S0064 已排除）|
| 3 | 正文无"启发/建议动作" | ✅ |
| 4 | calendar 正文无 pipeline 语言 | ✅ |
| 5 | 每个正文 item 在 Item Source Map | ✅（21 项全部对应，标题逐字一致）|
| 6 | industry vs community 同事件不重复 | ✅ |
| 7 | 公司名 / 产品名 / 数字 / 日期都能在 source text 找到 | ✅（已通过 Bash + UTF-8 读取核对 S0004/S0005/S0012/S0080/S0081/S0086/S0196/S0197 等原文）|

## 备注

- 应用 SKILL"宁多勿少"原则：borderline 候选保留在正文，由读者最终筛选。
- 老版本日报漏选《重返未来：1999》240 万差评事件，重做后已补入玩家舆论段首条，本次重抽取后仍保留（S0004 gamelook 原文确认）。
- 深度观察 #2 杖剑传说（S0005）、#1 Scopely（S0196）与 6/2 的 Embracer / Fellowship 形成"发行 / 控股组合管理"系列对位。
