# Sources Used

## Local Input Folders

- `news_data/ai_trends/2026-06-21/articles.jsonl`
- `news_data/community_discourse/2026-06-21/articles.jsonl`
- `news_data/industry_news/2026-06-21/articles.jsonl`
- `news_data/pc_rankings/2026-06-21/articles.jsonl`
- `news_data/release_calendar/2026-06-21/articles.jsonl`

## Extraction Summary

- Summary file: `output/daily/2026-06-21/_intermediate/report_inputs_summary.md`
- Index file: `output/daily/2026-06-21/_intermediate/report_inputs_index.md`
- Records extracted: 53
- Extraction failures: 0
- Empty text records: 0

## Notes

- Steam 当日榜单 `S0001` 明确写明该榜单为 2026-06-22 采集的实时热销榜快照，用于补充 2026-06-21 日报；正文未将其写成历史回溯榜单。
- `news_data/deep_analysis/2026-06-21/` 在本地窗口中缺失，因此“行业精选 / 深度观察”仅使用同日已抽取的本地行业与社区证据合成。
- 产品日历只保留了具备公司/玩法证据的条目；未在正文中补写缺失厂商信息。

## Item Source Map

### 零、steam当日榜单

- steam当日榜单 - S0001

### 一、行业新闻
- 《激战：大牌英雄》全球首曝并开放国服预约 - S0006
- 《宝可梦GO》研发商空间数据去向争议再发酵 - S0004
- 育碧联合创始人 Claude Guillemot 坠机身亡 - S0002, S0007

### 二、AI 新闻

- 美团 tabbit 国际版免费接入多家旗舰模型 - S0011
- Mythos 被称可在数小时内攻破机密系统 - S0012

### 三、新游发布 / 产品日历

- 产品日历 - 激战：大牌英雄 - S0006, S0027


### 四、玩家舆论 / 社区动态

- 《二重螺旋》1.4 强推联机并抬高独狼成本，玩家质疑新玩法利好工作室与外挂 - S0036
- 《卡厄斯梦境》国服追平国际服半年进度且未补偿，玩家争论资源缺口与代理节奏 - S0037
- 16 年前《使命召唤》移植版标价 80 美元，PlayStation 社区质疑“纯端口收复古税” - S0042

### 五、行业精选 / 深度观察

- 平台方在同一天同时收紧分发承诺与价格弹性测试 - S0008, S0009, S0042

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-21 日报 · 采集于 2026-06-22） | https://store.steampowered.com/search/?filter=topsellers
- S0002 | gcores.com | Ubisoft 共同创办人、营运执行副总裁因飞机坠机意外不幸辞世，享年69岁 | https://www.gcores.com/articles/216165
- S0004 | m.sohu.com | 究极背刺？《宝可梦GO》研发公司，把300亿张照片卖给了美国军方 | https://m.sohu.com/a/1039539207_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.1.1782086507356VDgyDvV_324
- S0006 | youxichaguan.com | CCG新游《激战：大牌英雄》全球首曝，国服预约抢先开启！ | https://youxichaguan.com/archives/200318
- S0007 | videogameschronicle.com | Ubisoft co-founder, Claude Guillemot, dies in plane accident | https://www.videogameschronicle.com/news/ubisoft-co-founder-claude-guillemot-dies-in-plane-accident/
- S0008 | videogameschronicle.com | PlayStation’s PC port era appears over as Sony scrubs key policy language | https://www.videogameschronicle.com/news/playstations-pc-port-era-appears-over-as-sony-scrubs-key-policy-language/
- S0009 | videogameschronicle.com | Ori director says Game Pass ‘could’ve worked’ if Xbox didn’t ‘slop out mediocre content like a factory’ | https://www.videogameschronicle.com/news/ori-director-says-game-pass-couldve-worked-if-xbox-didnt-slop-out-mediocre-content-like-a-factory/
- S0011 | aihot.virxact.com | 美团tabbit国际版免费接入GPT-5.5/Claude Opus 4.8等旗舰模型 | https://aihot.virxact.com/items/cmqnokdyn007jsl4nxazzzxp1
- S0012 | aihot.virxact.com | NSA局长：Mythos数小时内攻破其几乎所有机密系统 | https://aihot.virxact.com/items/cmqny6q7v0288slhkbzc8ob3u
- S0013 | 17173.com | 天堂 - 新版本 | https://newgame.17173.com/game-info-75.html
- S0027 | taptap.cn | 激战：大牌英雄 - 新游预约 (09:00 开始) | https://www.taptap.cn/app/859381
- S0036 | bbs.nga.cn | [英雄互娱] 二重螺旋新版本强推社交、强势回收掉率书，竞争型联机利好工作室与外挂，连续自刎归天 | https://bbs.nga.cn/read.php?tid=47010345&forder_by=postdatedesc
- S0037 | bbs.nga.cn | [新瓜]《卡厄斯梦境》开服仅一个月追平国际服半年游戏进度且0补偿 | https://bbs.nga.cn/read.php?tid=46997710&_fp=2&forder_by=postdatedesc
- S0042 | reddit.com | PlayStation Players Stung By $80 Price Tag For 16-Year-Old Call of Duty Ports | https://www.reddit.com/r/gaming/comments/1ubg93r/playstation_players_stung_by_80_price_tag_for/

## Notable Exclusions

- 《寒蝉鸣泣之时》新作 TV 动画（S0003）：有热度，但更偏泛娱乐 IP 动态，与当天游戏产业主线相比分量不足。
- 电竞乐园宣传稿（S0005）：营销文案属性过强，不构成当天有效产业新闻。
- 腾讯元宝父亲节合影活动（S0010）：节日促活意味更强，缺少行业级 AI 动态价值。
- 其余 TapTap 日历条目（S0015, S0017, S0020, S0021, S0023, S0025, S0026）：多数缺少来源文本中的厂商身份支撑，未进入最终正文。
- 《恋与深空》联名茶饮爆单（S0038）：讨论量不低，但主帖自带“疑似内容”标签，证据质量不足以写进正式舆论段。
- Xbox Handheld logo 讨论（S0041）：主要停留在社区猜测层面，未形成足够扎实的已发生事件。
