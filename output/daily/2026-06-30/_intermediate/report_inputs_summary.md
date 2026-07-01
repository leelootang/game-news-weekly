# Report Input Extraction Summary

- Records: 183
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 15
- `community_discourse`: 20
- `deep_analysis`: 1
- `industry_news`: 74
- `pc_rankings`: 1
- `release_calendar`: 72

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **力力普的工坊** [★ release+industry] — release: S0134 | industry: S0047
- **苍蓝避风港** [★ release+industry] — release: S0118 | industry: S0026
- **人类纪元：崛起** [多源 calendar] — release: S0092, S0129
- **史莱姆城堡** [多源 calendar] — release: S0094, S0123, S0159
- **少女机甲舰** [多源 calendar] — release: S0095, S0140
- **斗罗大陆：传承** [多源 calendar] — release: S0096, S0121, S0147
- **落日山丘** [多源 calendar] — release: S0122, S0157
