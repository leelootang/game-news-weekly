# Report Input Extraction Summary

- Records: 1344
- Extraction failures: 0
- Empty text records: 2
- Non-full body records: 18

## By Section

- `ai_trends`: 99
- `community_discourse`: 219
- `deep_analysis`: 7
- `industry_news`: 580
- `release_calendar`: 439

## Records Needing Attention

- `S0553` `industry_news` 2026 ChinaJoy 京东美妆薅羊毛攻略 - fetch=ok body=empty (0 chars)
- `S0752` `industry_news` 2026 ChinaJoy BTOB 展馆图正式公布 - fetch=ok body=empty (0 chars)

## 跨 section 强信号 — release_calendar ∩ industry_news / 多源 calendar（必须成卡）

> 以下产品在产品日历出现，且同时被行业新闻报道（最强信号）或跨多个日历源覆盖。**每一条都必须在 `event_candidates.md` 形成候选卡**（最终可 exclude，但不得在提取阶段静默漏掉）。名称按结构化字段/标题启发式提取，2 字以内的名称不做正文匹配，可能有少量遗漏，自行复核。

- **ChinaJoy** [★ release+industry] — release: S0616 | industry: S0055, S0397, S0416, S0425, S0553, S0556, S0557, S0558, S0559, S0562, S0563, S0564, S0752, S0754, S0755, S0756, S0771, S0886, S1050, S1078, S1081, S1100
- **Dispatch** [★ release+industry] — release: S0979 | industry: S1075 | community: S1342
- **Machine Party** [★ release+industry] — release: S0981 | industry: S1146
- **七日世界** [★ release+industry] — release: S0085, S0135 | industry: S0030, S0383, S0398
- **三国：百将牌** [★ release+industry] — release: S0908, S0925, S0949 | industry: S0215
- **三角洲行动** [★ release+industry] — release: S0086 | industry: S0029, S0215, S0397, S0398, S0403, S0542, S0794, S0882, S0885
- **初音未来：缤纷舞台** [★ release+industry] — release: S0249 | industry: S0215, S0558
- **崩坏：星穹铁道** [★ release+industry] — release: S0909 | industry: S0045, S0215, S0306, S0392, S0397, S0542, S0737, S1051, S1190
- **幻兽帕鲁** [★ release+industry] — release: S0088 | industry: S0009, S0019, S0024, S0389, S0538, S0848, S1155
- **拳皇全明星** [★ release+industry] — release: S0961 | industry: S0800, S0888
- **无畏契约：源能行动** [★ release+industry] — release: S0111, S0237, S1232 | industry: S0033
- **明日方舟** [★ release+industry] — release: S0112 | industry: S0018, S0025, S0029, S0033, S0207, S0215, S0306, S0384, S0395, S0397, S0404, S0542, S0570, S0882, S1051, S1054, S1058, S1190 | community: S0342, S0490, S0491, S0505, S0688, S0696, S1003, S1313, S1319
- **明日方舟：终末地** [★ release+industry] — release: S1216, S1276 | industry: S0018, S0025, S0207, S0215, S0306, S0384, S0395, S0397, S0404, S0542, S0570, S1051, S1054, S1190 | community: S0490, S1313
- **未定事件簿** [★ release+industry] — release: S0947 | industry: S0882
- **杖剑传说** [★ release+industry] — release: S1235 | industry: S0398, S0746, S0748
- **梦战：剑之海** [★ release+industry] — release: S1281 | industry: S1060, S1069, S1070
- **洛克王国：世界** [★ release+industry] — release: S0114, S1217, S1283 | industry: S0029, S0215, S0389, S0392, S0397
- **火影忍者** [★ release+industry] — release: S0157 | industry: S0045, S0215, S0545, S0884
- **燕云十六声** [★ release+industry] — release: S0090, S0159 | industry: S0029, S0305, S0383, S0384, S1049 | community: S1324
- **王国大作战：前线** [★ release+industry] — release: S0910, S0917, S0968 | industry: S0746
- **王者万象棋** [★ release+industry] — release: S0621 | industry: S0215, S0397
- **第五人格** [★ release+industry] — release: S1218 | industry: S0215, S0218, S0739, S0882, S1052
- **纸嫁衣9罗浮梦** [★ release+industry] — release: S1221, S1296 | industry: S1052, S1059
- **蓝色星原：旅谣** [★ release+industry] — release: S0091, S0170 | industry: S0215, S0389, S0392, S0397, S0400, S0571, S0796, S0882, S1049
- **蔚蓝档案** [★ release+industry] — release: S1245 | industry: S0215
- **诡秘之主** [★ release+industry] — release: S0164 | industry: S0390, S0398, S0407
- **追逐卡蕾多** [★ release+industry] — release: S0948, S1222, S1250 | industry: S0738, S1049
- **镭明闪击** [★ release+industry] — release: S0092 | industry: S0558
- **问剑长生** [★ release+industry] — release: S0167 | industry: S0746, S0748
- **龙之谷** [★ release+industry] — release: S1219 | industry: S0799
- **一梦九霄** [多源 calendar] — release: S0614, S0623, S0630
- **三国杀：天命棋局** [多源 calendar] — release: S1215, S1225
- **三国：战策长河** [多源 calendar] — release: S0912, S0941
- **世界之光** [多源 calendar] — release: S0632, S0913, S0951
- **元气骑士** [多源 calendar] — release: S0443, S0448, S0453
- **噗噗的冒险乐园** [多源 calendar] — release: S1246, S1259
- **圣垣** [多源 calendar] — release: S0618, S0639, S0942
- **塔塔冒险队** [多源 calendar] — release: S0977, S1228, S1297
- **情感反诈模拟器** [多源 calendar] — release: S0978, S1248, S1294
- **拳皇·命运** [多源 calendar] — release: S0933, S0960
- **斗破苍穹：斗帝之路** [多源 calendar] — release: S0914, S0962
- **无畏骑士** [多源 calendar] — release: S0915, S0943
- **最终的梦幻岛** [多源 calendar] — release: S0916, S0944, S0963
- **梦幻足球** [多源 calendar] — release: S0097, S0130, S0153
- **汤姆猫跑酷** [多源 calendar] — release: S1237, S1282
- **泞之翼3：玉碎篇** [多源 calendar] — release: S0234, S0240, S0263
- **热力无限赛车** [多源 calendar] — release: S0098, S0131, S0158
- **猫猫钓游记** [多源 calendar] — release: S1220, S1295
- **王座守护者** [多源 calendar] — release: S0444, S0450, S0474
- **王牌机甲** [多源 calendar] — release: S0660, S0918, S0945, S0969
- **皇帝成长计划2** [多源 calendar] — release: S1239, S1287
- **镇邪人** [多源 calendar] — release: S1223, S1251, S1288
