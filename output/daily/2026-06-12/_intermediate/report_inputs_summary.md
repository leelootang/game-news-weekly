# Report Input Extraction Summary

- Records: 250
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 20
- `community_discourse`: 34
- `industry_news`: 114
- `pc_rankings`: 1
- `release_calendar`: 81

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **Heave Ho 2** [★ release+industry] — release: S0216 | industry: S0073
- **三角洲行动** [★ release+industry] — release: S0144 | industry: S0054
- **仙帝神兵** [多源 calendar] — release: S0137, S0176
- **代号：地心** [多源 calendar] — release: S0138, S0147
- **割据天下** [多源 calendar] — release: S0139, S0169
- **基地：银河纵横** [多源 calendar] — release: S0140, S0168, S0182
- **泉愈** [多源 calendar] — release: S0170, S0196
- **灵契** [多源 calendar] — release: S0171, S0198
- **真魂修仙** [多源 calendar] — release: S0141, S0172, S0199
- **超阈限空间-中文正版手游** [多源 calendar] — release: S0142, S0165
