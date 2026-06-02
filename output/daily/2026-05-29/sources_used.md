# Sources Used

## Local Input Folders

- `news_data/industry_news/2026-05-29`
- `news_data/ai_trends/2026-05-29`
- `news_data/release_calendar/2026-05-29`
- `news_data/community_discourse/2026-05-29`
- `news_data/deep_analysis/2026-05-29`

## Extraction Summary

- Summary: `output/daily/2026-05-29/_intermediate/report_inputs_summary.md`
- Index: `output/daily/2026-05-29/_intermediate/report_inputs_index.md`
- Inputs: `output/daily/2026-05-29/_intermediate/report_inputs.jsonl`
- Event candidates: `output/daily/2026-05-29/_intermediate/event_candidates.md`
- Selection decisions: `output/daily/2026-05-29/_intermediate/selection_decisions.md`

## Item Source Map

| Report item | Source IDs | Local evidence / URLs |
| --- | --- | --- |
| 米哈游释放多项目预研矩阵 | S0014, S0024 | Gcores short item and GameLook long article; `https://www.gcores.com/articles/215097`, `http://www.gamelook.com.cn/2026/05/594256/` |
| 《王者荣耀世界》进入S1验证期 | S0028, S0080 | Industry-news article plus release-calendar overlap; `https://cgames.com/contents/2/11659.html`, `https://newgame.17173.com/game-info-1034888.html` |
| 巨人《超自然行动组》海外版登陆美日韩 | S0020 | GameLook industry article; `http://www.gamelook.com.cn/2026/05/594321/` |
| 网易Q1游戏收入同比增长6.9% | S0049 | GamesIndustry report; `https://www.gamesindustry.biz/netease-reports-69-increase-in-games-revenue-to-37bn-during-q1` |
| Playstack拟被IMC相关实体收购 | S0056, S0062, S0071 | PocketGamer.biz, Game Developer, VGC multi-source coverage; `https://www.pocketgamer.biz/vantageco-acquires-majority-stake-in-uk-games-publisher-playstack/`, `https://www.gamedeveloper.com/business/balatro-publisher-playstack-sold-to-gamespot-and-fandom-parent-company`, `https://www.videogameschronicle.com/news/balatro-owner-playstack-sold-to-parent-company-of-fandom-gamespot/` |
| OpenRouter推出Guardrails治理工具 | S0072 | AI HOT local record; `https://openrouter.ai/announcements/guardrails` |
| Kling AI展示长片级AI创作流程 | S0075 | AI HOT local record; `https://x.com/Kling_ai/status/2060375625404432757` |
| 《王者荣耀世界》S1“世界启程” | S0080, S0028 | Release-calendar local fact strengthened by industry-news overlap |
| 《鸣潮》3.4版本“The Dream Not Dreamed” | S0103, S0107, S0114, S0030 | Gematsu calendar local fact; same-game community heat and related industry context used only for importance signal |
| 《燕云十六声》新版本节点 | S0078, S0049 | Release-calendar record plus NetEase Q1 industry-news overlap |
| 《鸣潮》2077联动卡池规则引发抽卡机制争议 | S0107, S0114, S0103 | NGA high-heat discourse posts; local calendar backfill for same-game timeline |
| 《重返未来1999》周年庆回应未完全平息玩家不满 | S0116 | NGA discourse post with official-response discussion |
| 4月新作表现显示“强IP续作”和“差异化新IP”仍能穿透淡季 | S0126, S0048 | The Game Business monthly report plus GamesIndustry/Newzoo support |

## Release Calendar Local Evidence Signals

| Game / event | Signal | Source IDs | Decision |
| --- | --- | --- | --- |
| 王者荣耀世界 - S1世界启程 | `industry_news_overlap` | S0080, S0028 | Included |
| 鸣潮 - 3.4版本 | `single_calendar_source` plus same-game community heat | S0103, S0107, S0114 | Included |
| Fable - 延期至2027年2月 | `single_calendar_source` | S0100 | Excluded because delay was not material enough for this daily report |
| 燕云十六声 - 新版本 | `industry_news_overlap` | S0078, S0049 | Included |
| Inazuma Eleven: Cross - 日本6月9日上线 | `single_calendar_source` | S0101 | Excluded |
| 17173/16p small calendar items | `single_calendar_source` | S0078-S0099 | Excluded due weaker local importance signals |

## Excluded Notable Items

- 007 First Light sales milestone: strong product-performance story, but excluded from final industry section to keep daily industry news at five items and prioritize company strategy, overseas expansion, and M&A.
- Fable delay: overseas single-source calendar item; excluded because this daily report did not need a foreign calendar item for balance.
- Block Blast Google Play disappearance/return: local sources confirmed the app returned, but cause was unclear and no player/distribution follow-up was available in local records.
- 《绝区零》小游戏被指与Ouros相似: community heat was visible, but official response and external context were missing in local records.
- 《洛克王国世界》经济通胀: system-design issue was interesting but lower heat and more context-heavy than selected discourse events.
