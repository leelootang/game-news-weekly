# Report Input Extraction Summary

- Records: 234
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 40
- `community_discourse`: 30
- `deep_analysis`: 2
- `industry_news`: 93
- `pc_rankings`: 1
- `release_calendar`: 68

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **仙界大掌门** [多源 calendar] — release: S0157, S0162
- **地下城堡2：黑暗觉醒** [多源 calendar] — release: S0142, S0169
- **斗兽战场** [多源 calendar] — release: S0137, S0158, S0180
