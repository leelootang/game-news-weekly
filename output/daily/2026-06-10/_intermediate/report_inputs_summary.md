# Report Input Extraction Summary

- Records: 246
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 35
- `community_discourse`: 31
- `deep_analysis`: 1
- `industry_news`: 105
- `pc_rankings`: 1
- `release_calendar`: 73

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **Fire Emblem: Fortune’s Weave** [★ release+industry] — release: S0210 | industry: S0097, S0099
- **Warhammer 40,000: Space Marine II** [★ release+industry] — release: S0208 | industry: S0097
- **天元突破红莲螺岩** [多源 calendar] — release: S0142, S0162, S0176
- **奇门** [多源 calendar] — release: S0143, S0163
- **妖灵打工团** [多源 calendar] — release: S0164, S0178
- **文字密室逃脱** [多源 calendar] — release: S0144, S0183
- **苍蓝前线** [多源 calendar] — release: S0145, S0166, S0206
- **赛尔号** [多源 calendar] — release: S0158, S0199
