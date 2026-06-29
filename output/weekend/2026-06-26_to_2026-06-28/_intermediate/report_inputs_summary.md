# Report Input Extraction Summary

- Records: 413
- Extraction failures: 0
- Empty text records: 0

## By Section

- `ai_trends`: 38
- `community_discourse`: 47
- `deep_analysis`: 1
- `industry_news`: 150
- `pc_rankings`: 3
- `release_calendar`: 174

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **三角洲行动** [★ release+industry] — release: S0148, S0183 | industry: S0057, S0061, S0358 | community: S0412
- **剑侠情缘：重逢** [★ release+industry] — release: S0192 | industry: S0071
- **战术小队：破晓攻势** [★ release+industry] — release: S0131, S0143 | industry: S0358
- **洛克王国：世界** [★ release+industry] — release: S0163 | industry: S0358
- **燕云十六声** [★ release+industry] — release: S0139 | industry: S0056, S0061, S0358 | community: S0403
- **诡秘之主** [★ release+industry] — release: S0137, S0145, S0170 | industry: S0283, S0358
- **追逐卡蕾多** [★ release+industry] — release: S0332 | industry: S0358
- **逆水寒手游** [★ release+industry] — release: S0134 | industry: S0054 | community: S0345
- **大富翁：全球首富** [多源 calendar] — release: S0152, S0197
- **奥奇传说** [多源 calendar] — release: S0154, S0199
- **幻想之刃** [多源 calendar] — release: S0140, S0175, S0203
- **幻灵召唤** [多源 calendar] — release: S0141, S0176
- **怨楼** [多源 calendar] — release: S0142, S0177, S0205
- **我要当老祖** [多源 calendar] — release: S0178, S0207
- **星梦养成记** [多源 calendar] — release: S0144, S0209
- **最强蜗牛** [多源 calendar] — release: S0161, S0210
- **足球冠军杯大世界** [多源 calendar] — release: S0146, S0179, S0224
- **飞飞：无限宇宙** [多源 calendar] — release: S0135, S0147, S0180, S0226
