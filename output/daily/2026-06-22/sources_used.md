# Sources Used

## Local Input Folders

- `news_data/ai_trends/2026-06-22/articles.jsonl`
- `news_data/community_discourse/2026-06-22/articles.jsonl`
- `news_data/deep_analysis/2026-06-22/articles.jsonl`
- `news_data/industry_news/2026-06-22/articles.jsonl`
- `news_data/pc_rankings/2026-06-22/articles.jsonl`
- `news_data/release_calendar/2026-06-22/articles.jsonl`

## Extraction Summary

- Summary file: `output/daily/2026-06-22/_intermediate/report_inputs_summary.md`
- Index file: `output/daily/2026-06-22/_intermediate/report_inputs_index.md`
- Records extracted: 158
- Extraction failures: 0
- Empty text records: 0

## Notes

- Steam 当日榜单 `S0001` 明确写明该榜单为 `2026-06-23` 采集的实时热销榜快照，用于补充 `2026-06-22` 日报；正文未将其写成历史回溯榜单。
- 产品日历优先保留同窗行业新闻重叠或具备完整公司身份的条目：`崩坏：因缘精灵` 由 `industry_news + TapTap + 3839` 共同支撑，`激战：大牌英雄` 由 `industry_news + TapTap` 共同支撑，`雪松` 由 `16p + 3839 + TapTap` 多源交叉支撑。
- 本次 `deep_analysis` 原始池有数据，但最终“行业精选 / 深度观察”正文改用同窗国内平台与渠道证据合成，以更贴合当前国内优先的日报权重。

## Item Source Map

### Steam当日榜单

- Steam当日榜单 - S0001

### 一、行业新闻

- 米哈游《崩坏：因缘精灵》公布新 PV，并开启“进化测试”招募 - S0018, S0131, S0102
- 祖龙公布《诡秘之主：愚者》，把顶级网文 IP 改编推向卡牌 RPG 路线 - S0027
- 《激战：大牌英雄》全球首曝，B站把 CCG 发行做到了全球化试探 - S0036, S0123
- 《盛世天下》12 天销量突破 200 万套，互动影视继续抬高国产品类天花板 - S0024
- 《墨境》在 Steam 下架风波后完成复活，正式版总销量突破 20 万套 - S0038
- 传音控股再次申请港股上市，AHA Games 月活已超过 1.3 亿 - S0056
- 抖音小游戏“开玉石”题材冲上畅销榜前列，短视频平台再出现新品类窗口 - S0087

### 二、AI 新闻

- OpenAI 发布 Daybreak 安全工具，Codex Security 与 GPT-5.5-Cyber 同步亮相 - S0090
- 微信 Agent 小微开始灰度内测，主入口与聊天内入口出现能力分层 - S0094
- Cursor 审计显示，编程模型高分里有大量“奖励黑客”成分 - S0091

### 三、新游发布 / 产品日历

- 产品日历 - 崩坏：因缘精灵 - S0018, S0131, S0102
- 产品日历 - 激战：大牌英雄 - S0036, S0123
- 产品日历 - 雪松 - S0099, S0106, S0132

### 四、玩家舆论 / 社区动态

- 《二重螺旋》1.4 强推联机并抬高独狼成本，玩家质疑新玩法利好工作室与外挂 - S0144
- 《卡厄斯梦境》国服一月追平国际服半年进度且无补偿，争议焦点落在资源缺口 - S0147

### 五、行业精选 / 深度观察

- 从传音 AHA Games 到抖音“开玉石”，轻量内容分发正在继续放大 - S0056, S0087

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-22 日报 · 采集于 2026-06-23） | https://store.steampowered.com/search/?filter=topsellers
- S0018 | gcores.com | 米哈游新作《崩坏：因缘精灵》公布全新PV，「进化测试」招募开启 | https://www.gcores.com/articles/216211
- S0024 | gamelook.com.cn | 《盛世天下》12天销量突破200万套：国产真人互动影视划时代新纪录即将诞生 | http://www.gamelook.com.cn/2026/06/595705/
- S0027 | gamelook.com.cn | “二游《诡秘之主》首曝，这个可以有”！UE5女性向新作之后，祖龙放新大招 | http://www.gamelook.com.cn/2026/06/595748/
- S0036 | youxichaguan.com | 暴雪出走的技术骨干，要和B站一起打破CCG祖宗之法 | https://youxichaguan.com/archives/200325
- S0038 | youxichaguan.com | 下架，濒死，复活，一家拿了海外投资的国内厂商做了一款1100万流水的游戏 | https://youxichaguan.com/archives/200378
- S0056 | new.qq.com | 传音控股申请港股上市，旗下游戏平台拥有超1.3亿月活用户 | https://new.qq.com/rain/a/20260622A0BW5700
- S0087 | 36kr.com | 畅销榜第七、热门榜第一，多款产品接连登上畅销榜，抖音小游戏又出一新题材？ | https://36kr.com/p/3863826372646147
- S0090 | aihot.virxact.com | OpenAI 发布 Daybreak 安全工具：Codex Security 与 GPT-5.5-Cyber | https://aihot.virxact.com/items/cmqph7ap700n2slp5g4tfjs46
- S0091 | aihot.virxact.com | Cursor 审计发现奖励黑客行为淹没模型智能提升 | https://aihot.virxact.com/items/cmqpi3u8v00smslp5or0d3mx7
- S0094 | aihot.virxact.com | 微信Agent小微灰度内测：主入口发消息红包，子入口可读聊天记录 | https://aihot.virxact.com/items/cmqpbc21e08laslx6gica1m67
- S0099 | 16p.com | 雪松 - 上线 | https://www.16p.com/1951890.html
- S0102 | 3839.com | 崩坏：因缘精灵-崩坏IP新作(官服) 招募中 - 多种方式赢7月9日测试资格 | https://www.3839.com/a/182527.htm
- S0106 | 3839.com | 雪松(官服) - 12:00 正式上线 | https://www.3839.com/a/174714.htm
- S0123 | taptap.cn | 激战：大牌英雄 - 测试招募 | https://www.taptap.cn/app/859381
- S0131 | taptap.cn | 崩坏：因缘精灵 - 测试招募 (12:00 开始) | https://www.taptap.cn/app/753921
- S0132 | taptap.cn | 雪松 - 首发 (12:00 开始) | https://www.taptap.cn/app/718446
- S0144 | bbs.nga.cn | [英雄互娱] 二重螺旋新版本强推社交、强势回收掉率书，竞争型联机利好工作室与外挂，连续自刎归天 | https://bbs.nga.cn/read.php?tid=47010345&forder_by=postdatedesc
- S0147 | bbs.nga.cn | [新瓜]《卡厄斯梦境》开服仅一个月追平国际服半年游戏进度且0补偿 | https://bbs.nga.cn/read.php?tid=46997710&_fp=2&forder_by=postdatedesc

## Notable Exclusions

- 巴西“抽卡开箱”罚单（S0026）：有政策分量，但本次日报优先级让位于国内产品、平台和市场结构信号。
- 《三角洲行动》裂变赛季预告与新版本节点（S0098, S0107）：属于重要产品的赛季更新，但在本窗口里弱于多个国产新品测试 / 首发节点。
- 《恋与深空》第六男主争议（S0142）：热度存在，但更偏审美分歧与角色偏好，不如《二重螺旋》《卡厄斯梦境》的产品机制争议更具行业代表性。
- Grok Build `/goal` 模式（S0089）：产品有新意，但 AI 新闻位次低于 Daybreak、微信 Agent 和 Cursor 审计。
