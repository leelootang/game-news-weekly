# Sources Used — 游戏行业日报 2026-06-14

## 缺数据说明（Missing Data）

2026-06-14 本地 industry_news 采集情况（按 `news_data/_collector_runs/2026-06-14/run_summary.md`）：

- **采集器 failed**：gamelook、cgames
- **zero_articles**：gcores、gamesindustry、pocketgamer、gamedeveloper、mobilegamer、vgc、youxituoluo、youxixinzhi_qqnews、dataeye_36kr、yystv、investgame
- **有效产出**：youxiputao_sohu（1 条）、youxichaguan（1 条）

周末英美 biz 本就不更，叠加国内两家采集器 failed，industry_news 当日仅 2 条入库。本报告按 SKILL Missing Data 处理：不联网补缺、不编造，行业新闻"无显著X则写少"。

## 本地输入文件夹

- `news_data/industry_news/2026-06-14/`
- `news_data/ai_trends/2026-06-14/`（均为通用大模型动态，无游戏相关条目入正文）
- `news_data/release_calendar/2026-06-14/`
- `news_data/community_discourse/2026-06-14/`
- `news_data/pc_rankings/2026-06-14/`
- 抽取 summary：`output/daily/2026-06-14/_intermediate/report_inputs_summary.md`

## Item Source Map

### 零、steam当日榜单

- steam当日榜单 - S0001

### 一、行业新闻

- 互动影视《盛世天下》女帝篇5天破百万，全系列累计破300万 - S0002

### 三、新游发布 / 产品日历

- 产品日历 - 怪物火车2 - S0024
- 产品日历 - 异世界搜打撤 - S0022

### 四、玩家舆论 / 社区动态

- 米黑"番鼠鉴赏家"黎洋终审败诉，向米哈游实名道歉并赔偿50万元 - S0042
- 《绝区零》官方"明牌"告知需抽售前角色，引"售前强绑 vs 售后背刺"争论 - S0041
- 多款女性向/二游因角色"露肉"尺度引"集美内斗"：《夜幕之下》与《无限暖暖》 - S0052, S0044

### 五、行业精选 / 深度观察

- 灵犀《篮球少女》：当二次元手游绕开奇幻，回到"校园＋运动"的青春本源 - S0003

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-14 日报 · 采集于 2026-06-15） | https://store.steampowered.com/search/?filter=topsellers
- S0002 | m.sohu.com | 官宣销量5天破100万份，全系列300万：创造奇迹的国产新品，谁还没看懂？ | https://m.sohu.com/a/1036563624_204824
- S0042 | bbs.nga.cn | [米哈游]著名米黑番鼠鉴赏家(黎洋)对米哈游实名道歉，并赔偿50万元 | https://bbs.nga.cn/read.php?tid=46921036
- S0041 | bbs.nga.cn | [绝区零]官方明牌告诉你要抽售前角色 | https://bbs.nga.cn/read.php?tid=46966285&forder_by=postdatedesc
- S0052 | bbs.nga.cn | [夜幕之下]新角色pv男全裹女全漏被集美冲烂 | https://bbs.nga.cn/read.php?tid=46981964&forder_by=postdatedesc
- S0044 | bbs.nga.cn | [暖暖]删沟大行动引发集美内斗 | https://bbs.nga.cn/read.php?tid=46982008&forder_by=postdatedesc
- S0003 | youxichaguan.com | When Basketball Meets Teen Girls: Is the Gaming Genre on the Verge of a Revival? | https://youxichaguan.com/en/archives/199500
- S0024 | taptap.cn | 怪物火车2 - 新游预约 (00:00 开始) | https://www.taptap.cn/app/743336
- S0022 | taptap.cn | 异世界搜打撤 - 首发 | https://www.taptap.cn/app/871045

## 排除的值得注意条目

- 米哈游2025营收或近1900亿（北华念影响力系数，S0046）：非官方"串子"估算、被玩家群嘲，证据薄
- 洛克王国再次无公告暗改图标后称bug（S0050）：前几日已多次覆盖，本次为小图标改动
- 网易决斗链接"半龙女仆"变违禁词（S0047）：小众、审查向
- 三角洲核电站任务违反物理（S0045）、明日方舟×时尚芭莎广告标签（S0049）：梗帖/旧瓜
- 海外：Capcom auteur→team-led（S0062）、GTA6 生态（S0055）、Xbox 子公司（S0057/S0060，已在 6/13 覆盖）：弱相关/重复
- 通用 AI（Nadella 生态 / Anthropic 上市 / Meta 撤 Manus / Suno / Fusion API）：非游戏相关，AI 节不收
