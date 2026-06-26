# Report Input Extraction Summary

- Records: 1110
- Extraction failures: 0
- Empty text records: 1

## By Section

- `ai_trends`: 84
- `community_discourse`: 157
- `deep_analysis`: 6
- `industry_news`: 471
- `pc_rankings`: 7
- `release_calendar`: 385

## Records Needing Attention

- `S0530` `industry_news` 2026 ChinaJoy Live · AniSonic星尘十周年演唱会正式官宣 - ok (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **Sonic Frontiers: Definitive Edition** [★ release+industry] — release: S0645 | industry: S0743, S0744
- **三国火凤燎原** [★ release+industry] — release: S0854 | industry: S0947
- **三角洲行动** [★ release+industry] — release: S0082, S0408, S0417 | industry: S0031, S0508, S0526, S0701, S0718, S0932, S0941
- **冒险之路** [★ release+industry] — release: S0109 | industry: S0361
- **天堂2：盟约** [★ release+industry] — release: S0771, S0776, S0794, S0853 | industry: S0929
- **崩坏：因缘精灵** [★ release+industry] — release: S0441 | industry: S0326, S0476
- **彩虹六号：围攻** [★ release+industry] — release: S0406 | industry: S0687, S0898
- **暗区突围** [★ release+industry] — release: S0089 | industry: S0508
- **月圆之夜** [★ release+industry] — release: S1029 | industry: S0703, S0932
- **梦幻西游** [★ release+industry] — release: S0078 | industry: S0923
- **洛克王国：世界** [★ release+industry] — release: S0093 | industry: S0342
- **激战：大牌英雄** [★ release+industry] — release: S0282, S0433 | industry: S0261, S0344
- **童话师** [★ release+industry] — release: S0081, S0104, S0124 | industry: S0932
- **诡秘之主** [★ release+industry] — release: S0801, S1035 | industry: S0335, S0521, S0702
- **领主争霸** [★ release+industry] — release: S0640 | industry: S0709
- **FC足球梦剧场** [多源 calendar] — release: S1017, S1045
- **三国大冒险** [多源 calendar] — release: S0774, S0795
- **不休的勇士** [多源 calendar] — release: S0418, S0597, S0606, S0611
- **中国式地雷女** [多源 calendar] — release: S0271, S0410
- **叠入深渊** [多源 calendar] — release: S1007, S1037
- **国王棋** [多源 calendar] — release: S0786, S0815
- **山海烬墟** [多源 calendar] — release: S0212, S1008, S1038, S1058
- **栖云异梦3：溯源** [多源 calendar] — release: S0790, S1065
- **海域重启** [多源 calendar] — release: S1011, S1040, S1070
- **火焰审判-正版移植手游** [多源 calendar] — release: S0779, S0798
- **盛夏离与合** [多源 calendar] — release: S1041, S1083
- **真・三国无双 天下** [多源 calendar] — release: S0643, S0780, S0799, S0857
- **绿梦：时空之声** [多源 calendar] — release: S0603, S0858
- **芙娅之魂** [多源 calendar] — release: S0781, S1076
- **菲尼西雅战记** [多源 calendar] — release: S1012, S1077
- **闪之轨迹：北方战役** [多源 calendar] — release: S0859, S1013, S1044, S1085
- **雪松** [多源 calendar] — release: S0409, S0442
- **高能探宝团** [多源 calendar] — release: S1014, S1042
