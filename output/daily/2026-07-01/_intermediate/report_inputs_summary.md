# Report Input Extraction Summary

- Records: 193
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 20
- `community_discourse`: 35
- `deep_analysis`: 1
- `industry_news`: 82
- `pc_rankings`: 1
- `release_calendar`: 54

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **选技大乱斗** [★ release+industry] — release: S0108, S0152 | industry: S0029
