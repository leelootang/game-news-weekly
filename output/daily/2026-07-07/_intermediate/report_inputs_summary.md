# Report Input Extraction Summary

- Records: 164
- Extraction failures: 0
- Empty text records: 1

## By Section

- `ai_trends`: 3
- `community_discourse`: 39
- `deep_analysis`: 1
- `industry_news`: 78
- `pc_rankings`: 1
- `release_calendar`: 42

## Records Needing Attention

- `S0041` `industry_news` ChinaJoy X 支付宝出行 联动福利来袭 - ok (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **仙逆：战天道** [多源 calendar] — release: S0083, S0091
- **魔法森林大作战** [多源 calendar] — release: S0084, S0121
