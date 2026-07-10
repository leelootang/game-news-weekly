# Report Input Extraction Summary

- Records: 1048
- Extraction failures: 0
- Empty text records: 1

## By Section

- `ai_trends`: 60
- `community_discourse`: 212
- `deep_analysis`: 7
- `industry_news`: 367
- `pc_rankings`: 7
- `release_calendar`: 395

## Records Needing Attention

- `S0524` `industry_news` ChinaJoy X 支付宝出行 联动福利来袭 - ok (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **QQ飞车** [★ release+industry] — release: S0228 | industry: S0218
- **一触即发** [★ release+industry] — release: S0572 | industry: S0358, S0864
- **三国志：王道天下** [★ release+industry] — release: S0418, S0920, S0929, S0966 | industry: S0282, S0358, S0367
- **三角洲行动** [★ release+industry] — release: S0089 | industry: S0025, S0039, S0282, S0353, S0358, S0364, S0511, S0518, S0519, S0672, S0844, S0859
- **卡厄思梦境** [★ release+industry] — release: S0727 | industry: S0029
- **合金弹头：指挥官** [★ release+industry] — release: S0722, S0740 | industry: S0358
- **咪哇伊奇幻冒险** [★ release+industry] — release: S0931, S0967, S0975 | industry: S0358
- **塔拉索纳：皇家对决** [★ release+industry] — release: S0941 | industry: S0282
- **失控进化** [★ release+industry] — release: S0928, S0932, S1005 | industry: S0282, S0358, S0856, S0870, S0873
- **崩坏：因缘精灵** [★ release+industry] — release: S0921, S0934 | industry: S0018, S0037, S0282, S0354, S0355, S0358, S0852, S0855
- **崩坏：星穹铁道** [★ release+industry] — release: S0090 | industry: S0021, S0029, S0282, S0852, S0855, S0857, S0874
- **庇护所** [★ release+industry] — release: S0447 | industry: S0353, S0693
- **怪物猎人：旅人** [★ release+industry] — release: S0139 | industry: S0044, S0347
- **恋与深空** [★ release+industry] — release: S0948 | industry: S0021, S0282, S0670, S0821 | community: S0182, S0183, S0186, S0187, S0190, S0194, S0195, S0302, S0304, S0307, S0309, S0310, S0316, S0317, S0318, S0319, S0454, S0455, S0459, S0461, S0465, S0468, S0470, S0610, S0613, S0617, S0620, S0621, S0622, S0791, S0794, S0795, S0797, S0800, S0802, S0804, S0805, S0806, S1019, S1021
- **恐龙快打·起源** [★ release+industry] — release: S0935 | industry: S0358
- **无畏契约：源能行动** [★ release+industry] — release: S0949 | industry: S0031, S0282
- **暗区突围** [★ release+industry] — release: S0148 | industry: S0353
- **未定事件簿** [★ release+industry] — release: S0922, S0953 | industry: S0857, S0874 | community: S0787
- **梦之形** [★ release+industry] — release: S0760 | industry: S0044, S0347
- **洛克王国：世界** [★ release+industry] — release: S0111 | industry: S0037, S0282, S0347, S0354, S0857
- **炉石传说** [★ release+industry] — release: S0719 | industry: S0521
- **燕云十六声** [★ release+industry] — release: S0091 | industry: S0025, S0347, S0848
- **猛兽派对** [★ release+industry] — release: S0155 | industry: S0347
- **王者荣耀世界** [★ release+industry] — release: S0956 | industry: S0282 | community: S0314, S0466
- **球比伦战记** [★ release+industry] — release: S0293 | industry: S0005
- **白银之城** [★ release+industry] — release: S0256 | industry: S0002, S0044, S0051, S0282, S0345, S0347
- **筑梦事务所** [★ release+industry] — release: S0407 | industry: S0358
- **舒舒服服小岛时光** [★ release+industry] — release: S0294 | industry: S0044
- **苏丹的游戏** [★ release+industry] — release: S0261 | industry: S0347, S0360, S0865
- **荒野乱斗** [★ release+industry] — release: S0960 | industry: S0282
- **落日战火** [★ release+industry] — release: S0122 | industry: S0358
- **诡影藏锋** [★ release+industry] — release: S0443, S0766 | industry: S0282, S0681, S0684, S0692, S0849
- **逆战：未来** [★ release+industry] — release: S0924 | industry: S0282, S0361
- **逆水寒** [★ release+industry] — release: S0925 | industry: S0692, S0849
- **造梦西游之黎尤浩劫篇** [★ release+industry] — release: S0094, S0119, S0168 | industry: S0358
- **遗忘之海** [★ release+industry] — release: S0926, S0936, S1000 | industry: S0044, S0282, S0347, S0358, S0839, S0853, S0864
- **金铲铲之战** [★ release+industry] — release: S0927, S0965 | industry: S0282, S0514
- **镇魂街王者归来** [★ release+industry] — release: S0937, S0969 | industry: S0860
- **霓虹深渊2** [★ release+industry] — release: S0265 | industry: S0044, S0347
- **龙族：卡塞尔之门** [★ release+industry] — release: S0233 | industry: S0842
- **一念逍遥** [多源 calendar] — release: S0097, S0125
- **仙逆：战天道** [多源 calendar] — release: S0566, S0574
- **决策三国** [多源 calendar] — release: S0093, S0130
- **剑侠情缘：重逢** [多源 calendar] — release: S0416, S0427
- **奥比岛：梦想国度** [多源 calendar] — release: S0105, S0135
- **封神之弈** [多源 calendar] — release: S0933, S0968, S0982
- **小花仙：拉贝尔之约** [多源 calendar] — release: S0106, S0137
- **崇祯直聘：明末官场沉浮模拟器** [多源 calendar] — release: S0945, S0983
- **我不是胖虎：小岛大当家** [多源 calendar] — release: S0406, S0446
- **晶核** [多源 calendar] — release: S0733, S0758
- **炼金与魔法** [多源 calendar] — release: S0112, S0173
- **终结之终结** [多源 calendar] — release: S0413, S0442
- **迷失之径** [多源 calendar] — release: S0738, S0778
- **音舞光年** [多源 calendar] — release: S0408, S0444
- **魔法森林大作战** [多源 calendar] — release: S0567, S0604
