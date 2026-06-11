# Sources Used — 2026-06-10 日报

## 本地输入文件夹

- `news_data/ai_trends/2026-06-10/articles.jsonl` — 35 条
- `news_data/community_discourse/2026-06-10/articles.jsonl` — 31 条
- `news_data/deep_analysis/2026-06-10/articles.jsonl` — 1 条
- `news_data/industry_news/2026-06-10/articles.jsonl` — 105 条
- `news_data/pc_rankings/2026-06-10/articles.jsonl` — 1 条
- `news_data/release_calendar/2026-06-10/articles.jsonl` — 73 条

## 抽取 Summary 路径

`output/daily/2026-06-10/_intermediate/report_inputs_summary.md`
`output/daily/2026-06-10/_intermediate/report_inputs.jsonl`

---

## Item Source Map

### Steam 当日榜单

| 报告条目 | Source ID | 文件/来源 | URL |
|---|---|---|---|
| Steam TOP10 全表 + 近期新品亮点 | S0001 | `pc_rankings/2026-06-10/articles.jsonl` | https://store.steampowered.com/search/?filter=topsellers（排名）+ Gamalytic（估算）|
| 命运2 #1 背景说明 | S0041 | `industry_news/2026-06-10/articles.jsonl` | gcores.com |

> 说明：Steam 日榜无历史查询能力，S0001 的快照实际采集于 2026-06-11，用于补充 2026-06-10 日报。`extra.snapshot_date` = 2026-06-11。

---

### 一、行业新闻

| 报告条目 | Source ID | 文件/来源 | URL |
|---|---|---|---|
| 《鸣潮》×边缘行者联动刷新纪录 | S0049, S0043, S0056 | `industry_news/2026-06-10/articles.jsonl` | gamelook.com.cn, gamelook.com.cn, youxituoluo.com |
| 5月手游市场数据（王者/Kingshot/Nikke/鸣潮/异环） | S0043, S0056, S0095 | `industry_news/2026-06-10/articles.jsonl` | gamelook.com.cn, youxituoluo.com, mobilegamer.biz |
| EA $55B 收购 LBO 分析 | S0077 | `industry_news/2026-06-10/articles.jsonl` | gamesindustry.biz |
| Xbox CEO 硬件危机+Activision存疑+Helix | S0073, S0093, S0100 | `industry_news/2026-06-10/articles.jsonl` | gamesindustry.biz, gamedeveloper.com, videogameschronicle.com |
| 宝可梦财报创纪录（$33亿/+70%/TCG Pocket） | S0050 | `industry_news/2026-06-10/articles.jsonl` | gamelook.com.cn |
| 《黑色信标》停运（408天/腾讯/前库洛） | S0051 | `industry_news/2026-06-10/articles.jsonl` | cgames.com |
| Jin Universe Studios《Aether Dawn》披露 | S0070 | `industry_news/2026-06-10/articles.jsonl` | new.qq.com |
| 任天堂欧洲Joy-Con被罚€3500万 | S0068, S0092 | `industry_news/2026-06-10/articles.jsonl` | yystv.net, gamedeveloper.com |

---

### 二、AI 新闻

| 报告条目 | Source ID | 文件/来源 | URL |
|---|---|---|---|
| 腾讯光子 Light AI 首次亮相 | S0045 | `industry_news/2026-06-10/articles.jsonl` | gamelook.com.cn |
| 疯狂出租车新作 AI 标注争议 | S0067 | `industry_news/2026-06-10/articles.jsonl` | yystv.net |
| 火山方舟版权商业化平台上线 | S0127 | `ai_trends/2026-06-10/articles.jsonl` | aihot.virxact.com（原始来源：火山引擎官方公众号）|

---

### 三、新游发布 / 产品日历

| 报告条目 | Source ID | 文件/来源 | 本地证据信号 |
|---|---|---|---|
| 产品日历 - 苍蓝前线 | S0145（16p，开发商），S0166（3839，时间），S0206（TapTap，评分7.8） | `release_calendar/2026-06-10/articles.jsonl` | 多源 calendar（16p + 3839 + TapTap）；无 industry_news 重合 |
| 产品日历 - 文字密室逃脱 | S0144（16p，开发商），S0183（TapTap，评分8.8） | `release_calendar/2026-06-10/articles.jsonl` | 多源 calendar（16p + TapTap）；无 industry_news 重合 |
| 产品日历 - 天元突破红莲螺岩 | S0142（16p，开发商），S0162（3839，时间），S0176（TapTap，评分4.0） | `release_calendar/2026-06-10/articles.jsonl` | 多源 calendar（16p + 3839 + TapTap）；无 industry_news 重合 |
| 产品日历 - 饥荒：联机版 | S0030（gcores，宣布上线日期），S0160（3839，定档确认） | `industry_news` + `release_calendar/2026-06-10/articles.jsonl` | industry_news（S0030）+ release_calendar（S0160）双来源 |
| 产品日历 - 火焰审判 | S0153（3839，定档+Tags），S0205（TapTap，评分8.5） | `release_calendar/2026-06-10/articles.jsonl` | 多源 calendar（3839 + TapTap）；无 industry_news 重合；开发商原文信息不详，正文未写厂商 |

---

### 四、玩家舆论 / 社区动态

| 报告条目 | Source ID | 文件/来源 | URL |
|---|---|---|---|
| 崩铁×UBW联动远坂凛缝合伊什塔尔争议 | S0218（主帖），S0215（相关联动争议帖） | `community_discourse/2026-06-10/articles.jsonl` | bbs.nga.cn |
| 《终末地》官号加速掉粉 | S0216 | `community_discourse/2026-06-10/articles.jsonl` | bbs.nga.cn |
| 鸣潮联动编剧辟谣非正史 | S0224 | `community_discourse/2026-06-10/articles.jsonl` | bbs.nga.cn |

---

### 五、行业精选 / 深度观察

| 报告条目 | Source ID | 文件/来源 | URL |
|---|---|---|---|
| Project Zomboid 长线销售分析 | S0246 | `deep_analysis/2026-06-10/articles.jsonl` | newsletter.gamediscover.co |

---

## 排除的值得注意条目

| 条目 | 排除原因 |
|---|---|
| 决胜巅峰新皮肤（S0149）| Hard Stop 2：正文不得出现相关产品名称，仅在中间文件留审计痕迹 |
| 《妖灵打工团》上线（S0164, S0178）| 无开发商原文证据，两源标签严重不一致（策略/割草 vs 合成/Roguelike） |
| 《奇门》上线（S0143, S0163）| 3839评分5.7偏低，无industry_news重合，未成入选门槛 |
| Warhammer 40K: Space Marine II Switch 2（S0208, S0097）| 无具体上线日期（"holiday 2026"），主机向，移动相关性低 |
| Fire Emblem $80 定价新闻（S0099）| 已并入《饥荒》/产品日历节说明语境；$80定价钩子本身在正文中未单独展开，属 borderline 留存标记 |
| EA $55B 新闻仅收入分析层（S0077）| 已 include，非排除 |
| Nintendo Switch 2 Direct 大量公告（S0097）| 主机向，筛选仅保留有移动/跨平台或重大定价信号的条目 |

## 缺失数据说明

- 无缺失：本日所有6个 section（ai_trends/community_discourse/deep_analysis/industry_news/pc_rankings/release_calendar）均有本地 JSONL 数据，共246条，提取失败0条。
