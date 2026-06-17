# Sources Used — 游戏行业日报 2026-06-14

## 缺数据说明（Missing Data，已查证）

2026-06-14 本地 industry_news 采集情况（按 `news_data/_collector_runs/2026-06-14/run_summary.md` + 事后复跑核实）：

- **采集器 failed**：gamelook、cgames
  - 复跑诊断：两者均重度依赖 Playwright（cgames 全流程；gamelook 用 urllib REST + Playwright 抓正文）；当日疑似 Playwright 实例瞬时崩溃/超时；今日同样命令再跑 EXIT 0，gamelook 回收 5 篇 6-14 文章、cgames 回收 1 篇。
  - 已补回：cgames `11880` 周报 + gamelook `595443` 9377/HDC 已追加进 `news_data/industry_news/2026-06-14/articles.jsonl` 并重新 extract。
  - gamelook 另 4 篇（V社停售实体卡 / Pokémon Go AR 数据 / 腾讯林哲 AI Agent / Switch 2 三方 3A）于 6-15 重采时被收回、归到 6-15 报告，未在本日重复列入。
- **zero_articles（正常周末无产出，本报告不补造）**：gcores、gamesindustry、pocketgamer、gamedeveloper、mobilegamer、vgc、youxituoluo、youxixinzhi_qqnews、dataeye_36kr、yystv、investgame
- **runner 行为**：`run_daily_collectors.py` 失败时只把 stderr 打到控制台未落盘，所以 6-14 原始堆栈已丢失；已在 PR 中加 `_collector_runs/<date>/<collector>_stderr.log` 持久化方案。

## 本地输入文件夹

- `news_data/industry_news/2026-06-14/`（含事后补回的 2 条 gamelook/cgames）
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
- 9377携塔防爆款《永远的蔚蓝星球》亮相 HDC 2026，押注鸿蒙生态做"长线经营" - S0004
- 腾讯 K9 合作部成立 + 育碧《彩虹六号：攻势》国服首测，与 Embark 联合的《弧光猎人》定档 6/24 - S0005
- 字节朝夕光年《雾影猎人》动作搜打撤 BETA4 在即，诗悦《望月》600 人重做版本 6/19 线下试玩 - S0005

### 三、新游发布 / 产品日历

- 产品日历 - 怪物火车2 - S0026
- 产品日历 - 异世界搜打撤 - S0024

### 四、玩家舆论 / 社区动态

- 米黑"番鼠鉴赏家"黎洋终审败诉，向米哈游实名道歉并赔偿50万元 - S0044
- 《绝区零》官方"明牌"告知需抽售前角色，引"售前强绑 vs 售后背刺"争论 - S0043
- 多款女性向/二游因角色"露肉"尺度引"集美内斗"：《夜幕之下》与《无限暖暖》 - S0054, S0046

### 五、行业精选 / 深度观察

- 灵犀《篮球少女》：当二次元手游绕开奇幻，回到"校园＋运动"的青春本源 - S0003

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-14 日报 · 采集于 2026-06-15） | https://store.steampowered.com/search/?filter=topsellers
- S0002 | m.sohu.com | 官宣销量5天破100万份，全系列300万：创造奇迹的国产新品，谁还没看懂？ | https://m.sohu.com/a/1036563624_204824
- S0003 | youxichaguan.com | When Basketball Meets Teen Girls: Is the Gaming Genre on the Verge of a Revival? | https://youxichaguan.com/en/archives/199500
- S0004 | gamelook.com.cn | 一款塔防爆款的增长样本：9377携《永远的蔚蓝星球》亮相HDC 2026 | http://www.gamelook.com.cn/2026/06/595443/
- S0005 | cgames.com | 腾讯字节诗悦新游混战；广深上海二游厂商接连受挫丨Fighting周报 | https://cgames.com/contents/2/11880.html
- S0024 | taptap.cn | 异世界搜打撤 - 首发 | https://www.taptap.cn/app/871045
- S0026 | taptap.cn | 怪物火车2 - 新游预约 (00:00 开始) | https://www.taptap.cn/app/743336
- S0043 | bbs.nga.cn | [绝区零]官方明牌告诉你要抽售前角色 | https://bbs.nga.cn/read.php?tid=46966285&forder_by=postdatedesc
- S0044 | bbs.nga.cn | [米哈游]著名米黑番鼠鉴赏家(黎洋)对米哈游实名道歉，并赔偿50万元 | https://bbs.nga.cn/read.php?tid=46921036
- S0046 | bbs.nga.cn | [暖暖]删沟大行动引发集美内斗 | https://bbs.nga.cn/read.php?tid=46982008&forder_by=postdatedesc
- S0054 | bbs.nga.cn | [夜幕之下]新角色pv男全裹女全漏被集美冲烂 | https://bbs.nga.cn/read.php?tid=46981964&forder_by=postdatedesc

## 排除的值得注意条目

- 米哈游2025营收或近1900亿（北华念影响力系数）：非官方"串子"估算、被玩家群嘲，证据薄
- 洛克王国再次无公告暗改图标后称bug：前几日已多次覆盖，本次为小图标改动
- 网易决斗链接"半龙女仆"变违禁词：小众、审查向
- 三角洲核电站任务违反物理、明日方舟×时尚芭莎广告标签：梗帖/旧瓜
- 海外：Capcom auteur→team-led、GTA6 生态、Xbox 子公司（已在 6-13 覆盖）：弱相关/重复
- 通用 AI（Nadella 生态 / Anthropic 上市 / Meta 撤 Manus / Suno / Fusion API）：非游戏相关
