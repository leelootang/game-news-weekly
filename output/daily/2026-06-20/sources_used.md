# Sources Used

## Local Input Folders

- `news_data/ai_trends/2026-06-20/articles.jsonl`
- `news_data/community_discourse/2026-06-20/articles.jsonl`
- `news_data/deep_analysis/2026-06-20/articles.jsonl`
- `news_data/industry_news/2026-06-20/articles.jsonl`
- `news_data/pc_rankings/2026-06-20/articles.jsonl`
- `news_data/release_calendar/2026-06-20/articles.jsonl`

## Extraction Summary

- Summary file: `output/daily/2026-06-20/_intermediate/report_inputs_summary.md`
- Index file: `output/daily/2026-06-20/_intermediate/report_inputs_index.md`
- Records extracted: 88
- Extraction failures: 0
- Empty text records: 0

## Notes

- Steam 当日榜 source `S0001` 明确写明该榜单为 2026-06-21 采集的实时热销榜快照，用于补充 2026-06-20 日报；最终正文未把它写成历史查询结果。
- 本窗口 `release_calendar` 与 `industry_news` 没有同名强重合，也没有跨多个日历源的同名产品；因此产品日历只保留了单源但具备明确测试 / 更新信号的 borderline 条目，且正文没有补写缺失厂商。

## Item Source Map

### 零、steam当日榜单

- steam当日榜单 - S0001

### 一、行业新闻

- 《望月》线下试玩曝光一年半重做与数亿投入 - S0008
- 米哈游周边侵权案二审维持 298 万赔偿 - S0010
- 《终末地》危机合约首开即成核心留存话题 - S0009
- 育碧联合创始人 Claude Guillemot 坠机身亡 - S0007, S0011, S0076

### 二、AI 新闻

- AlphaFold 负责人 John Jumper 转投 Anthropic - S0014
- 微软被曝双向转售 GPT 与 DeepSeek - S0021
- NVIDIA SpatialClaw 以免训练框架冲高空间推理准确率 - S0020

### 三、新游发布 / 产品日历

- 产品日历 - 植物大战僵尸杂交版-手机重制版 - S0029
- 产品日历 - 宠物星球 - S0043

### 四、玩家舆论 / 社区动态

- 《洛克王国》生蛋计时会被家园操作刷新，玩家为保收益反而不回家园 - S0069
- 《太吾绘卷》2.0 结局补丁未平旧怨，玩家再指剧情仍在袒护“制作组皮套” - S0072
- 《崩坏：星穹铁道》“爻光”动态手指出错后被带入 AI 作画争论 - S0066

### 五、行业精选 / 深度观察

- Steam 把“预发售发现”前移到了首页日历层 - S0088
- 游戏业谈 AI 的口径开始从能力想象转向成本审计 - S0012

## Source Details

- S0001 | store.steampowered.com | Steam 全球热销榜 TOP10（2026-06-20 日报 · 采集于 2026-06-21） | https://store.steampowered.com/search/?filter=topsellers
- S0007 | gcores.com | Ubisoft 共同创办人、营运执行副总裁因飞机坠机意外不幸辞世，享年69岁 | https://www.gcores.com/articles/216165
- S0008 | m.sohu.com | 重做一年半，成本数亿：对话科韵路600人做的开放世界 | https://m.sohu.com/a/1039206729_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.4.1782000098456wAjfFVs_324
- S0009 | m.sohu.com | 鹰角，难了 | https://m.sohu.com/a/1039252734_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.2.1782000098456wAjfFVs_324
- S0010 | m.sohu.com | 米哈游诉周边店侵权获赔298万；某司高管贪腐获刑五年 | 一周说「法」 | https://m.sohu.com/a/1039251997_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.3.1782000098456wAjfFVs_324
- S0011 | m.sohu.com | 育碧联合创始人坠机辞世：传奇背后的关键人物 | https://m.sohu.com/a/1039305619_204824?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334&spm=smwp.channel_247.block2_307_epwR4p_1_fd.1.1782000098456wAjfFVs_324
- S0012 | gamesindustry.biz | As AI costs rise, there’s little evidence of major utility in game development | Opinion | https://www.gamesindustry.biz/as-ai-costs-rise-theres-little-evidence-of-major-utility-in-game-development-opinion
- S0014 | aihot.virxact.com | AlphaFold 负责人 John Jumper 离职 Google DeepMind，加入 Anthropic | https://x.com/demishassabis/status/2068002732250640603
- S0020 | aihot.virxact.com | NVIDIA Research 发布 SpatialClaw：免训练空间推理框架 | https://www.marktechpost.com/2026/06/19/nvidia-ai-introduce-spatialclaw-a-training-free-agent-that-treats-code-as-the-action-interface-for-spatial-reasoning
- S0021 | aihot.virxact.com | 微软双向转售GPT与DeepSeek成全球最大AI中间商 | https://x.com/AYi_AInotes/status/2068218661710512231
- S0029 | 3839.com | 植物大战僵尸杂交版-手机重制版 测试 - 寒冰菇王、云小鬼僵尸等上线 | https://www.3839.com/a/184258.htm
- S0043 | taptap.cn | 宠物星球 - 限量测试 | https://www.taptap.cn/app/759171
- S0066 | bbs.nga.cn | [新瓜]崩铁最新动态爻光手指出现问题，被指ai作画，目前已修改 | https://bbs.nga.cn/read.php?tid=46994775
- S0069 | bbs.nga.cn | [腾讯] [洛克王国]对于离谱的生蛋机制，小洛克们表示"有家不能回"(6.20更新，官方把生蛋时间代码删掉了) | https://bbs.nga.cn/read.php?tid=47003276&forder_by=postdatedesc
- S0072 | bbs.nga.cn | [新瓜]太吾绘卷更拖剧情4年，依旧保护制作组皮套(有手游) | https://bbs.nga.cn/read.php?tid=47018308&forder_by=postdatedesc
- S0076 | reddit.com | Ubisoft Co-Founder Dies in Tragic Plane Crash | https://www.reddit.com/r/gaming/comments/1uatrwg/ubisoft_cofounder_dies_in_tragic_plane_crash/
- S0088 | newsletter.gamediscover.co | How Steam's personal calendar is supercharging pre-launch discovery... | https://newsletter.gamediscover.co/p/how-steams-personal-calendar-is-supercharging

## Notable Exclusions

- CDPR / 《巫师 4》口碑修复表态（S0002, S0082）：有讨论度，但新增信息仅为单句高管表态，分量不足以挤进当天正文。
- 《Deep Agents 实战》教程（S0022）：偏教程发布，不够成当天 AI 新闻。
- 《尘白禁区》延期贴（S0060）：窗口内仍活跃，但核心触发已在更早日期出现，纳入会与前一日报高度重复。
- 《合合梦幻岛》《巅峰极速》《山海烬墟》等日历项（S0023, S0028, S0045）：要么属于常规奖励 / 招募，要么缺少足够的厂商 / 品类支撑，未进最终日历正文。
