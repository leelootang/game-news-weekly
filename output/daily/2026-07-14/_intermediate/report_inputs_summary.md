# Report Input Extraction Summary

- Records: 198
- Extraction failures: 0
- Empty text records: 1

## By Section

- `ai_trends`: 14
- `community_discourse`: 35
- `deep_analysis`: 1
- `industry_news`: 78
- `release_calendar`: 70

## Records Needing Attention

- `S0035` `industry_news` 2026 ChinaJoy 京东美妆薅羊毛攻略 - ok (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **ChinaJoy** [★ release+industry] — release: S0098 | industry: S0035, S0038, S0039, S0040, S0041, S0044, S0045, S0046
- **一梦九霄** [多源 calendar] — release: S0096, S0105, S0112
- **圣垣** [多源 calendar] — release: S0100, S0121
