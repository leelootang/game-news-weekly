# Report Input Extraction Summary

- Records: 151
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 15
- `community_discourse`: 28
- `deep_analysis`: 3
- `industry_news`: 56
- `pc_rankings`: 1
- `release_calendar`: 48

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **三国志：王道天下** [★ release+industry] — release: S0086 | industry: S0026, S0035
- **庇护所** [★ release+industry] — release: S0115 | industry: S0021
- **筑梦事务所** [★ release+industry] — release: S0075 | industry: S0026
- **剑侠情缘：重逢** [多源 calendar] — release: S0084, S0095
- **我不是胖虎：小岛大当家** [多源 calendar] — release: S0074, S0114
- **终结之终结** [多源 calendar] — release: S0081, S0110
- **音舞光年** [多源 calendar] — release: S0076, S0112
