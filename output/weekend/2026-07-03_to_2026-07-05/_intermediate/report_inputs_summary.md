# Report Input Extraction Summary

- Records: 332
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 27
- `community_discourse`: 78
- `deep_analysis`: 1
- `industry_news`: 80
- `pc_rankings`: 3
- `release_calendar`: 143

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **QQ飞车** [★ release+industry] — release: S0228 | industry: S0218
- **三角洲行动** [★ release+industry] — release: S0089 | industry: S0025, S0039, S0282
- **崩坏：星穹铁道** [★ release+industry] — release: S0090 | industry: S0021, S0029, S0282
- **怪物猎人：旅人** [★ release+industry] — release: S0139 | industry: S0044
- **洛克王国：世界** [★ release+industry] — release: S0111 | industry: S0037, S0282
- **燕云十六声** [★ release+industry] — release: S0091 | industry: S0025
- **球比伦战记** [★ release+industry] — release: S0293 | industry: S0005
- **白银之城** [★ release+industry] — release: S0256 | industry: S0002, S0044, S0051, S0282
- **舒舒服服小岛时光** [★ release+industry] — release: S0294 | industry: S0044
- **霓虹深渊2** [★ release+industry] — release: S0265 | industry: S0044
- **一念逍遥** [多源 calendar] — release: S0097, S0125
- **决策三国** [多源 calendar] — release: S0093, S0130
- **奥比岛：梦想国度** [多源 calendar] — release: S0105, S0135
- **小花仙：拉贝尔之约** [多源 calendar] — release: S0106, S0137
- **炼金与魔法** [多源 calendar] — release: S0112, S0173
- **造梦西游之黎尤浩劫篇** [多源 calendar] — release: S0094, S0119, S0168
