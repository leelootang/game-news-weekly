# Report Input Extraction Summary

- Records: 230
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 22
- `community_discourse`: 34
- `deep_analysis`: 1
- `industry_news`: 91
- `pc_rankings`: 1
- `release_calendar`: 81

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **地牢猎手6** [★ release+industry] — release: S0115, S0117, S0146, S0161 | industry: S0047
- **绝区零** [★ release+industry] — release: S0183 | industry: S0036 | community: S0201, S0203, S0206, S0214
- **三国：百将牌** [多源 calendar] — release: S0121, S0153
- **卡厄思梦境** [多源 calendar] — release: S0123, S0157
- **咪哇伊奇幻冒险** [多源 calendar] — release: S0116, S0145, S0159
