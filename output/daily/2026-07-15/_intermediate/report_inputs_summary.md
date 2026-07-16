# Report Input Extraction Summary

- Records: 308
- Extraction failures: 22
- Empty text records: 1

## By Section

- `ai_trends`: 17
- `community_discourse`: 35
- `deep_analysis`: 1
- `industry_news`: 174
- `release_calendar`: 81

## Records Needing Attention

- `S0090` `industry_news` Assassin’s Creed Creator’s New Game Channels Fine Art And Slasher Cinema - partial (2664 chars)
- `S0091` `industry_news` Witcher 3 Director Says Next-Gen Console Delay Would Not Be Such A Bad Thing - partial (2842 chars)
- `S0092` `industry_news` Xbox’s Console Future Looks Bleak In New Industry Forecast - partial (3407 chars)
- `S0093` `industry_news` Exclusive: Mondo Reveals Masters Of The Universe 2002 Keldor And Flocked Panthor Figures - partial (3074 chars)
- `S0094` `industry_news` Beast Of Reincarnation’s Perfect Parry Ping Makes Me Want To Git Gud - partial (2071 chars)
- `S0095` `industry_news` Baseball’s Best Pitcher Put A Charizard Card In His Glove - partial (1578 chars)
- `S0096` `industry_news` Star Of 2026’s Biggest Movie Will Talk Call Of Duty: MW4 This Weekend - partial (1351 chars)
- `S0097` `industry_news` You Can Earn A $15,000 A Year For Mastering Your Favorite Game - partial (4121 chars)
- `S0098` `industry_news` EA Is Finally Trying to Save Your Sims 4 Saves - partial (3058 chars)
- `S0099` `industry_news` Why Are There So Many Benedict Cumberbatch Cards In Magic: The Gathering? - partial (2458 chars)
- `S0100` `industry_news` GOG Wants You To Make Your Own Physical Games - partial (1929 chars)
- `S0101` `industry_news` Path Of Titans Players Say Goodbye To Sam Neill With A Dinosaur March - partial (2594 chars)
- `S0102` `industry_news` Tony Hawk’s Pro Skater 1+2 Has Disappeared From Game Pass Without Explanation - partial (2135 chars)
- `S0103` `industry_news` Far Cry TV Show Adds Iconic, Veteran Actor Steve Buscemi - partial (1711 chars)
- `S0104` `industry_news` You Can Now Order Games And Consoles From GameStop With Uber Eats - partial (1630 chars)
- `S0105` `industry_news` PUBG Is Finally Fixing One Of Its Biggest New Player Hurdles - partial (2202 chars)
- `S0106` `industry_news` PlayStation Plus Extra/Premium Games For July 2026 Revealed - partial (3376 chars)
- `S0113` `industry_news` 《湮灭之潮》线下试玩招募宣传视频 - partial (99 chars)
- `S0119` `industry_news` 《绝地潜兵2》「极速拦截」宣传视频 - partial (89 chars)
- `S0120` `industry_news` 《战地风云6》第四赛季预告 - partial (75 chars)
- `S0124` `industry_news` 《逃生：试炼》第七赛季宣传视频 - partial (87 chars)
- `S0129` `industry_news` 《艾恩葛朗特 回荡新声》评测 - partial (77 chars)
- `S0036` `industry_news` 2026 ChinaJoy BTOB 展馆图正式公布 - ok (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **崩坏：星穹铁道** [★ release+industry] — release: S0193 | industry: S0021
- **拳皇全明星** [★ release+industry] — release: S0245 | industry: S0084, S0172
- **未定事件簿** [★ release+industry] — release: S0231 | industry: S0166
- **王国大作战：前线** [★ release+industry] — release: S0194, S0201, S0252 | industry: S0030
- **追逐卡蕾多** [★ release+industry] — release: S0232 | industry: S0022
- **三国：战策长河** [多源 calendar] — release: S0196, S0225
- **三国：百将牌** [多源 calendar] — release: S0192, S0209, S0233
- **世界之光** [多源 calendar] — release: S0197, S0235
- **拳皇·命运** [多源 calendar] — release: S0217, S0244
- **斗破苍穹：斗帝之路** [多源 calendar] — release: S0198, S0246
- **无畏骑士** [多源 calendar] — release: S0199, S0227
- **最终的梦幻岛** [多源 calendar] — release: S0200, S0228, S0247
- **王牌机甲** [多源 calendar] — release: S0202, S0229, S0253
