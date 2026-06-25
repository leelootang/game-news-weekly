# Sources Used

## Local Input Folders

- `news_data/ai_trends/2026-06-24/articles.jsonl`
- `news_data/community_discourse/2026-06-24/articles.jsonl`
- `news_data/deep_analysis/2026-06-24/articles.jsonl`
- `news_data/industry_news/2026-06-24/articles.jsonl`
- `news_data/pc_rankings/2026-06-24/articles.jsonl`
- `news_data/release_calendar/2026-06-24/articles.jsonl`

## Extraction Summary

- Summary file: `output/daily/2026-06-24/_intermediate/report_inputs_summary.md`
- Index file: `output/daily/2026-06-24/_intermediate/report_inputs_index.md`
- Records extracted: 219
- Extraction failures: 0
- Empty text records: 0

## Notes

- `steam当日榜单` 对应的 `S0001` 明确写明该榜单为 `2026-06-25` 采集的 Steam 实时热销榜快照，用于补充 `2026-06-24` 日报；正文未将其写成历史可回查榜单。
- 本次产品日历保留 3 条，优先级来自 `release_calendar ∩ industry_news` 强交叉或明确的跨端测试节点，未因日历多源重复而机械扩充条数。
- `《恋与深空》` 社区条目使用 `community_discourse` 记录承接争议主线，并借 `industry_news/S0040` 回填角色 PV 与争议背景，未与行业新闻正文重复叙事。

## Item Source Map

### steam当日榜单

- steam当日榜单 - S0001

### 一、行业新闻

- 腾讯拟退出部分日本工作室少数股权，投资重心转向共研与 UGC - S0045, S0048, S0067
- Valve 公布 Steam Machine 1049 美元起售，称硬件成本高于预期 - S0035, S0061, S0016
- 手游 D2C 市场被估至 170 亿美元，头部采用者收入提升中位数达 35% - S0062, S0072, S0077
- 快手《诡秘之主》披露 624 人团队与超 10 亿元投入，二测前主动亮出研发底牌 - S0039, S0138
- 市场传出阿里拟出售灵犀互娱，国内 SLG 资产或迎来重新定价 - S0046

### 二、AI 新闻

- 豆包专业版正式上线，国内通用 AI 开始把订阅卖点转向可执行 Agent - S0098
- 火山引擎推出 Agent Ready 基础设施，企业 Agent 竞争转向身份、沙箱和接入层 - S0104
- ChatGPT 双向语音模型 Bidi 1 进入测试，实时打断式交互开始落地 - S0100

### 三、新游发布 / 产品日历

- 产品日历 - 诡秘之主 - S0138, S0039
- 产品日历 - Honkai: Nexus Anima - S0066
- 产品日历 - 弧光猎人（ARC Raiders） - S0134

### 四、玩家舆论 / 社区动态

- 《恋与深空》公布狼人男主并声明“所有男主都是异性恋”，玩家质疑角色审美与受众判断 - S0207, S0040
- 《明日方舟：终末地》危机合约头像框国服限时 30 天、外服永久，玩家把争议扩大到森空岛服务差异 - S0210, S0217

### 五、行业精选 / 深度观察

- Steam Next Fest 的头部 demo 不再指向单一爆款公式 - S0219

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-24 日报 · 采集于 2026-06-25） | https://store.steampowered.com/search/?filter=topsellers
- S0016 | gcores.com | V社进一步开放SteamOS，官方解释硬件产品定价逻辑 | https://www.gcores.com/articles/216244
- S0035 | gamelook.com.cn | Steam主机“太贵”玩家吵翻天！比PS5价格高75%、配置更低！ | http://www.gamelook.com.cn/2026/06/595973/
- S0039 | gamelook.com.cn | 《诡秘之主》MMO急了？自证实力：624人花了10亿，制作人“真·前网易大佬” | http://www.gamelook.com.cn/2026/06/595980/
- S0040 | gamelook.com.cn | 《恋与深空》第六男主“狼人”，玩家不买单？ | http://www.gamelook.com.cn/2026/06/595986/
- S0045 | youxituoluo.com | 准备抛售多家日本工作室股份，腾讯游戏全球投资大洗牌 | https://www.youxituoluo.com/534606.html
- S0046 | youxituoluo.com | 阿里卖游戏，谁将接盘？ | https://www.youxituoluo.com/534607.html
- S0048 | youxichaguan.com | 腾讯拟退出多家日本游戏工作室投资，Marvelous等多家厂商在列 | https://youxichaguan.com/archives/200557
- S0061 | gamesindustry.biz | Valve admits Steam Machine is "more expensive" than it hoped | https://www.gamesindustry.biz/valve-admits-steam-machine-is-more-expensive-than-it-hoped
- S0062 | gamesindustry.biz | Appcharge: Direct-to-consumer market worth around $17bn today | https://www.gamesindustry.biz/appcharge-direct-to-consumer-market-worth-around-17bn-today
- S0066 | pocketgamer.biz | HoYoverse’s new game Honkai: Nexus Anima gets closed beta test in July | https://www.pocketgamer.biz/hoyoverses-new-game-honkai-nexus-anima-gets-closed-beta-test-in-july/
- S0067 | pocketgamer.biz | Tencent explores exits from Japanese game studio investments amid portfolio review | https://www.pocketgamer.biz/tencent-explores-exits-from-japanese-game-studio-investments-amid-portfolio-review/
- S0072 | pocketgamer.biz | Report: Mobile game D2C revenues reach $17bn as publishers push beyond app stores | https://www.pocketgamer.biz/report-mobile-game-d2c-revenues-reach-17bn-as-publishers-push-beyond-app-stores/
- S0077 | mobilegamer.biz | Data digest: World Cup numbers, DTC hits $17bn, UEFN payouts, May’s top game ads, more | https://mobilegamer.biz/data-digest-world-cup-numbers-dtc-hits-17bn-uefn-payouts-mays-top-ads-more/
- S0098 | aihot.virxact.com | 今天，豆包正式推出专业版 | https://aihot.virxact.com/items/cmqrdmylf0iyeslp50lteppvq
- S0100 | aihot.virxact.com | OpenAI ChatGPT 语音最大规模升级：双向AI语音模型 Bidi 1 已上线测试 | https://aihot.virxact.com/items/cmqrl73460l9gslp5w33pryqi
- S0104 | aihot.virxact.com | 火山引擎推出Agent Ready基础设施，AgentKit与ArkClaw企业版升级 | https://aihot.virxact.com/items/cmqrxnmqg0p2zslp51p8cc1ln
- S0134 | haoyou_kuaibao_3839 | 弧光猎人（ARC Raiders） PC/主机 - 10:00 国服限量首测 | https://www.3839.com/a/181984.htm
- S0138 | haoyou_kuaibao_3839 | 诡秘之主 - 11:00 测试预下载，6月26日开测 | https://www.3839.com/a/150321.htm
- S0207 | nga_mobile_gossip | [新瓜] 乙游乐子小瓜一则，恋与深空首次声明所有男主都是异性恋 | https://bbs.nga.cn/read.php?tid=47033193&forder_by=postdatedesc
- S0210 | nga_mobile_gossip | [厂商] 鹰角社区森空岛国服外服区别对待 | https://bbs.nga.cn/read.php?tid=47041801&forder_by=postdatedesc
- S0217 | nga_mobile_gossip | [新瓜][鹰角]明日方舟终末地，森空岛危机合约[纪念]头像框，外服永久，国服限时30天 | https://bbs.nga.cn/read.php?tid=47041941&forder_by=postdatedesc
- S0219 | gamediscover | Who 'won' June 2026's Steam Next Fest? | https://newsletter.gamediscover.co/p/who-won-june-2026s-steam-next-fest

## Notable Exclusions

- GTA 6 标准版 79.99 美元且首发仅提供下载码（S0063, S0083, S0084）：全球意义明确，但本日报优先保留对国内移动与平台结构更直接的行业信号。
- Oracle 因 AI 应用裁员 21000 人（S0094）：与游戏行业直接相关性偏弱，未进入 AI 新闻正文。
- 《天堂2：盟约》与《真・三国无双 天下》多源上线（S0108, S0113, S0131, S0190；S0117, S0136, S0194）：多源日历只证明事件存在，缺少更强主体与节点价值，未因重复覆盖直接入选。
