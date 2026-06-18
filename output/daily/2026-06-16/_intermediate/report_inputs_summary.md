# Report Input Extraction Summary

- Records: 232
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 27
- `community_discourse`: 31
- `deep_analysis`: 1
- `industry_news`: 111
- `pc_rankings`: 1
- `release_calendar`: 61

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **光与夜之恋** [★ release+industry] — release: S0147, S0166 | industry: S0043
- **排兵布阵** [★ release+industry] — release: S0142, S0156, S0184 | industry: S0042
- **万界绮园：逐光筑梦手札** [多源 calendar] — release: S0141, S0146, S0159
