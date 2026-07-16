# Report Input Extraction Summary

- Records: 308
- Extraction failures: 0
- Empty text records: 1
- Non-full body records: 0

## By Section

- `ai_trends`: 17
- `community_discourse`: 35
- `deep_analysis`: 1
- `industry_news`: 174
- `release_calendar`: 81

## Records Needing Attention

- `S0036` `industry_news` 2026 ChinaJoy BTOB 展馆图正式公布 - fetch=ok body=empty (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **崩坏：星穹铁道** [★ release+industry] — release: S0193 | industry: S0021
- **拳皇全明星** [★ release+industry] — release: S0245 | industry: S0084, S0172
- **未定事件簿** [★ release+industry] — release: S0231 | industry: S0166
- **王国大作战：前线** [★ release+industry] — release: S0194, S0201, S0252 | industry: S0030
- **追逐卡蕾多** [★ release+industry] — release: S0232 | industry: S0022
- **三国：战策长河** [多源 calendar] — release: S0196, S0225
- **三国：百将牌** [多源 calendar] — release: S0192, S0209, S0233
- **世界之光** [多源 calendar] — release: S0197, S0235
- **拳皇·命运** [多源 calendar] — release: S0217, S0244
- **斗破苍穹：斗帝之路** [多源 calendar] — release: S0198, S0246
- **无畏骑士** [多源 calendar] — release: S0199, S0227
- **最终的梦幻岛** [多源 calendar] — release: S0200, S0228, S0247
- **王牌机甲** [多源 calendar] — release: S0202, S0229, S0253
