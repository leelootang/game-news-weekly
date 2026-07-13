# Report Input Extraction Summary

- Records: 368
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 39
- `community_discourse`: 88
- `deep_analysis`: 1
- `industry_news`: 90
- `pc_rankings`: 3
- `release_calendar`: 147

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **七日世界** [★ release+industry] — release: S0086, S0136 | industry: S0031
- **三角洲行动** [★ release+industry] — release: S0087 | industry: S0030, S0217
- **初音未来：缤纷舞台** [★ release+industry] — release: S0251 | industry: S0217
- **幻兽帕鲁** [★ release+industry] — release: S0089 | industry: S0010, S0020, S0025
- **无畏契约：源能行动** [★ release+industry] — release: S0112, S0239 | industry: S0034
- **明日方舟** [★ release+industry] — release: S0113 | industry: S0019, S0026, S0030, S0034, S0209, S0217, S0309 | community: S0345
- **洛克王国：世界** [★ release+industry] — release: S0115 | industry: S0030, S0217
- **火影忍者** [★ release+industry] — release: S0158 | industry: S0046, S0217
- **燕云十六声** [★ release+industry] — release: S0091, S0160 | industry: S0030, S0308
- **蓝色星原：旅谣** [★ release+industry] — release: S0092, S0171 | industry: S0217
- **梦幻足球** [多源 calendar] — release: S0098, S0131, S0154
- **泞之翼3：玉碎篇** [多源 calendar] — release: S0236, S0242, S0265
- **热力无限赛车** [多源 calendar] — release: S0099, S0132, S0159
