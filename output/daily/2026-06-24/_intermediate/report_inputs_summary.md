# Report Input Extraction Summary

- Records: 219
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 16
- `community_discourse`: 17
- `deep_analysis`: 1
- `industry_news`: 90
- `pc_rankings`: 1
- `release_calendar`: 94

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **诡秘之主** [★ release+industry] — release: S0138 | industry: S0039
- **三国大冒险** [多源 calendar] — release: S0111, S0132
- **国王棋** [多源 calendar] — release: S0123, S0152
- **天堂2：盟约** [多源 calendar] — release: S0108, S0113, S0131, S0190
- **火焰审判-正版移植手游** [多源 calendar] — release: S0116, S0135
- **真・三国无双 天下** [多源 calendar] — release: S0117, S0136, S0194
