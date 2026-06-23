# Report Input Extraction Summary

- Records: 158
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 7
- `community_discourse`: 20
- `deep_analysis`: 2
- `industry_news`: 87
- `pc_rankings`: 1
- `release_calendar`: 41

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **崩坏：因缘精灵** [★ release+industry] — release: S0131 | industry: S0018
- **激战：大牌英雄** [★ release+industry] — release: S0123 | industry: S0036
- **三角洲行动** [多源 calendar] — release: S0098, S0107
- **雪松** [多源 calendar] — release: S0099, S0132
