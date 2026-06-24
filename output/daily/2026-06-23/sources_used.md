# Sources Used

## Local Input Folders

- `news_data/ai_trends/2026-06-23/articles.jsonl`
- `news_data/community_discourse/2026-06-23/articles.jsonl`
- `news_data/deep_analysis/2026-06-23/articles.jsonl`
- `news_data/industry_news/2026-06-23/articles.jsonl`
- `news_data/pc_rankings/2026-06-23/articles.jsonl`
- `news_data/release_calendar/2026-06-23/articles.jsonl`

## Extraction Summary

- Summary file: `output/daily/2026-06-23/_intermediate/report_inputs_summary.md`
- Index file: `output/daily/2026-06-23/_intermediate/report_inputs_index.md`
- Records extracted: 195
- Extraction failures: 0
- Empty text records: 1

## Notes

- Steam当日榜单 `S0001` 明确写明该榜单为 `2026-06-24` 采集的实时热销榜快照，用于补充 `2026-06-23` 日报；正文未将其写成历史回溯榜单。
- `industry_news/S0062` 为 0 字空文本记录，本次未进入候选或正文。
- 产品日历保留 2 条，是因为本窗口内满足“新品/强节点”门槛的条目有限；`不休的勇士` 虽有多源重复，但主体与事件强度不足，未因多源日历重复而自动入选。
- 灵犀线索同时出现出售传闻与 UE5 三国 SLG 项目储备，最终在正文里以资产处置主线吸收，避免同公司同日重复占位。

## Item Source Map

### Steam当日榜单

- Steam当日榜单 - S0001

### 一、行业新闻

- 阿里拟出售灵犀互娱，交易价传至 70-90 亿元 - S0046, S0047, S0065
- 快手首度披露《诡秘之主》研发班底，624 人团队与超 10 亿元投入曝光 - S0053
- 字节《雾影猎人》临近发售，动作搜打撤赛道进入正面卡位 - S0045
- 《三角洲行动》全面战场国际邀请赛扩至全球八队，中国自研 FPS 跑通海外赛事链路 - S0058
- 《Neverness to Everness》两个月手游流水达 4210 万美元，日本贡献最高 - S0082
- 叠纸用 48 秒 PV 推出《恋与深空》新男主，头部乙游再做长线变量 - S0049
- Valve 公布 Steam Machine 定价超千美元，同步进一步开放 SteamOS - S0067, S0025, S0002
- 腾讯被曝考虑退出 Marvelous 等日本工作室股权，称游戏仍是核心业务 - S0037, S0072, S0106
- EA 被曝再启裁员，主要波及招聘、客服、信任安全与 IT 等支持岗 - S0031, S0070, S0090

### 二、AI 新闻

- 米哈游《BSide: Olivia Lin》上线 Steam 页面，AI 陪伴产品继续前探 - S0007, S0051
- 豆包音频生成模型 1.0 发布，单次可编排多角色两分钟音频 - S0118
- 网易有道开源 Confucius4-TTS，3 秒即可做 14 语种跨语种语音克隆 - S0122

### 三、新游发布 / 产品日历

- 产品日历 - 崩坏：因缘精灵 - S0008, S0096
- 产品日历 - Dinkum手游 - S0130

### 四、玩家舆论 / 社区动态

- 《二重螺旋》1.4 强推联机并抬高独狼成本，玩家质疑新玩法利好外挂与工作室 - S0183
- 《洛克王国》家园生蛋机制被指每次回家都重置倒计时，玩家认为社交设计反成负收益 - S0190

### 五、行业精选 / 深度观察

- 《Command & Conquer Rivals》争议让 EA 重学“先照顾核心玩家” - S0195

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-23 日报 · 采集于 2026-06-24） | https://store.steampowered.com/search/?filter=topsellers
- S0007 | gcores.com | 米哈游公布PC应用《BSide：Olivia Lin》，为AI陪伴型软件 | https://www.gcores.com/articles/216213
- S0008 | gcores.com | 米哈游新作《崩坏：因缘精灵》公布全新PV，「进化测试」招募开启 | https://www.gcores.com/articles/216211
- S0045 | cgames.com | 字节游戏70人抢跑动作搜打撤，制作人：赛道没有标准答案 | https://cgames.com/contents/2/11959.html
- S0046 | cgames.com | 阿里拟出售灵犀互娱，价格超10亿美金 | https://cgames.com/contents/2/11961.html
- S0047 | m.sohu.com | 阿里出售游戏业务幕后：三大买家，谁能拿下灵犀互娱？ | https://m.sohu.com/a/1040554709_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.3.1782259581416S4U8YcV_324
- S0049 | m.sohu.com | 仅用48秒，叠纸刷屏全网 | https://m.sohu.com/a/1040592033_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.2.1782259581416S4U8YcV_324
- S0051 | youxituoluo.com | 只是一个音乐播放器？米哈游AI新作Steam页面今日上线 | https://www.youxituoluo.com/534600.html
- S0053 | youxituoluo.com | 快手自曝新游阵容：原《逆水寒》制作人带队，624人团队，开发成本超十亿 | https://www.youxituoluo.com/534602.html
- S0058 | youxichaguan.com | 这款腾讯自研游戏跑通了一条无人踏足的路 | https://youxichaguan.com/archives/200494
- S0065 | new.qq.com | 消息称阿里巴巴计划出售游戏业务，交易价约70-90亿元 | https://new.qq.com/rain/a/20260623A06YMK00
- S0082 | pocketgamer.biz | Neverness to Everness steers towards $50m in two months on mobile | https://www.pocketgamer.biz/neverness-to-everness-steers-towards-50m-in-two-months-on-mobile/
- S0096 | mobilegamer.biz | Honkai: Nexus Anima is Hoyoverse’s take on the Pokémon formula | https://mobilegamer.biz/honkai-nexus-anima-is-hoyoverses-take-on-the-pokemon-formula/
- S0118 | aihot.virxact.com | 豆包音频生成模型1.0发布，重新定义AI音频创作 | https://aihot.virxact.com/items/cmqq876yf07gsslp5eix31xaq
- S0122 | aihot.virxact.com | 网易有道发布 Confucius4-TTS：14 语种跨语种无口音语音克隆开源模型 | https://aihot.virxact.com/items/cmqqjmnoj0af8slp5kb7ky21w
- S0130 | 3839.com | Dinkum手游 - 已开启海外首测 | https://www.3839.com/a/163383.htm
- S0183 | bbs.nga.cn | [英雄互娱] 二重螺旋新版本强推社交、强势回收掉率书，竞争型联机利好工作室与外挂，连续自刎归天 | https://bbs.nga.cn/read.php?tid=47010345&forder_by=postdatedesc
- S0190 | bbs.nga.cn | [腾讯] [洛克王国]对于离谱的生蛋机制，小洛克们表示"有家不能回"(6.20更新，官方把生蛋时间代码删掉了) | https://bbs.nga.cn/read.php?tid=47003276&_fp=2&forder_by=postdatedesc
- S0195 | thegamebusiness.com | Fans were so angry about a Command & Conquer mobile game that it changed EA | https://www.thegamebusiness.com/p/fans-were-so-angry-about-a-command
- S0067 | gamesindustry.biz | Valve's Steam Machine price starts at $1049 / £879; original pricing "no longer viable" due to hardware supply issues | https://www.gamesindustry.biz/valves-steam-machine-price-starts-at-1049-879-original-pricing-no-longer-viable-due-to-hardware-supply-issues
- S0025 | gcores.com | V社进一步开放SteamOS，官方解释硬件产品定价逻辑 | https://www.gcores.com/articles/216244
- S0002 | gcores.com | Valve 正式公布 Steam Machine 价格与首批出货时间 | https://www.gcores.com/articles/216243
- S0037 | gcores.com | 据彭博社报道，腾讯正计划退出对 Marvelous 等少数股权投资 | https://www.gcores.com/articles/216278
- S0072 | gamesindustry.biz | Report: Tencent plans to exit investments in Japanese studios like Story of Seasons developer Marvelous | https://www.gamesindustry.biz/report-tencent-plans-to-exit-investments-in-japanese-studios-like-story-of-seasons-developer-marvelous
- S0106 | videogameschronicle.com | Tencent is reportedly in talks to sell its shares in some Japanese studios, even if that means taking a loss | https://www.videogameschronicle.com/news/tencent-is-reportedly-in-talks-to-sell-its-shares-in-some-japanese-studios-even-if-that-means-taking-a-loss/
- S0031 | gcores.com | EA 被曝再次裁员，涉及招聘、客服、安全与 IT 团队 | https://www.gcores.com/articles/216249
- S0070 | gamesindustry.biz | EA is reportedly laying off recruitment, customer support, safety, and IT staff | https://www.gamesindustry.biz/ea-is-reportedly-laying-off-recruitment-customer-support-safety-and-it-staff
- S0090 | gamedeveloper.com | Report: EA conducts layoffs in Hyderabad, India and the US | https://www.gamedeveloper.com/business/report-ea-conducts-layoffs-in-hyderabad-india-and-the-us

## Notable Exclusions

- AppsFlyer 获逾 10 亿美元投资（S0075, S0095）：偏广告技术生态，未进入正文。
- 不休的勇士多源上线（S0129, S0138, S0143）：多源日历只证明事件存在，主体与节点分量不足。
- 《尘白禁区》延期引发社区“欢呼胜利”（S0180）：热度高但更像圈层内情绪与梗，不如机制争议类事件清晰。
