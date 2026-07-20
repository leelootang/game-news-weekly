# Report Input Extraction Summary

- Records: 603
- Extraction failures: 0
- Empty text records: 0
- Non-full body records: 24

## By Section

- `ai_trends`: 26
- `community_discourse`: 92
- `deep_analysis`: 1
- `industry_news`: 270
- `release_calendar`: 214

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **冒险之旅** [★ release+industry] — release: S0398, S0523 | industry: S0129
- **和平精英** [★ release+industry] — release: S0190 | industry: S0077, S0170, S0471
- **心动小镇** [★ release+industry] — release: S0251 | industry: S0471
- **无畏契约：源能行动** [★ release+industry] — release: S0211 | industry: S0170, S0471
- **蛋仔派对** [★ release+industry] — release: S0192 | industry: S0471
- **城主别慌张** [多源 calendar] — release: S0194, S0228, S0244
- **奈里** [多源 calendar] — release: S0207, S0245
- **宝石战争** [多源 calendar] — release: S0195, S0229, S0276
- **小小武神** [多源 calendar] — release: S0230, S0247
- **放开那妖怪** [多源 calendar] — release: S0197, S0231
- **无悔华夏** [多源 calendar] — release: S0210, S0256
