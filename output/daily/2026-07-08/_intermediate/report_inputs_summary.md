# Report Input Extraction Summary

- Records: 172
- Extraction failures: 0
- Empty text records: 0

## By Section

- `community_discourse`: 32
- `deep_analysis`: 1
- `industry_news`: 69
- `pc_rankings`: 1
- `release_calendar`: 69

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **诡影藏锋** [★ release+industry] — release: S0119 | industry: S0034, S0037, S0045
- **合金弹头：指挥官** [多源 calendar] — release: S0075, S0093
- **晶核** [多源 calendar] — release: S0086, S0111
- **迷失之径** [多源 calendar] — release: S0091, S0131
