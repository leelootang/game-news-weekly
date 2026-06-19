# Report Input Extraction Summary

- Records: 268
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 30
- `community_discourse`: 38
- `deep_analysis`: 1
- `industry_news`: 102
- `pc_rankings`: 1
- `release_calendar`: 96

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **气球塔防6** [★ release+industry] — release: S0205 | industry: S0003
- **潜水员戴夫** [★ release+industry] — release: S0206 | industry: S0028, S0054 | community: S0239
- **三国杀：天命棋局** [多源 calendar] — release: S0137, S0177
- **九天绘卷** [多源 calendar] — release: S0174, S0183
- **夜幕之下** [多源 calendar] — release: S0134, S0189 | community: S0230, S0236
- **情感反诈模拟器** [多源 calendar] — release: S0157, S0225
