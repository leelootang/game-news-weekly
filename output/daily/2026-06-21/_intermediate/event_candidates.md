# Event Candidates

## C001 - Steam 2026-06-21 TOP10 snapshot
- section: pc_rankings
- status: candidate
- source_ids: S0001
- entities: Steam / MECCHA CHAMELEON / Counter-Strike 2 / Marvel Rivals / Dead by Daylight / Path of Exile 2 / Destiny 2 / Cyberpunk 2077 / Warframe / Forza Horizon 6 / Stellaris
- facts:
  - Steam source marks `MECCHA CHAMELEON` as the only `★ 近期新品` in the TOP10, ranked #1.
  - Source gives concrete fields for release date, price, rating, sales, and revenue for each TOP10 row.
  - Daily snapshot is explicitly collected on 2026-06-22 for the 2026-06-21 daily report.
- notes: ranking section mandatory; no historical delta field in daily source, so no synthetic change column.

## C002 - Ubisoft co-founder Claude Guillemot dies in plane accident
- section: industry_news
- status: candidate
- source_ids: S0002, S0007
- entities: Ubisoft / Claude Guillemot
- facts:
  - Gcores and VGC both report Claude Guillemot died in a plane accident.
  - Source text supports age `69`.
  - Event is a real executive/founder signal, not a routine promo item.
- notes: strong multi-source entity cluster; candidate should be retained even if ultimately excluded.

## C003 - Pokémon GO spatial data controversy resurfaces around Niantic Spatial
- section: industry_news
- status: candidate
- source_ids: S0004
- entities: Pokémon GO / Niantic / Niantic Spatial / Scopely / Vantor
- facts:
  - Source text says players uploaded more than `30 billion` AR photos/scans.
  - Niantic sold game operations to Scopely for `$3.5 billion` while retaining data and AI assets in Niantic Spatial.
  - Source says Niantic Spatial later partnered with Vantor for 3D map / visual positioning usage.
- notes: single-source but high-weight data-rights / game-to-defense crossover story.

## C004 - 《激战：大牌英雄》全球首曝并开放国服预约
- section: industry_news
- status: candidate
- source_ids: S0006, S0027
- entities: 激战：大牌英雄 / Guild Wars / NC / ArenaNet / bilibili 游戏
- facts:
  - Source text says global reveal happened on `2026-06-21`.
  - TapTap source records `09:00` national-server reservation start and `卡牌` tag.
  - Industry source names NC and ArenaNet supervision plus bilibili global publishing.
- notes: release_calendar + industry_news overlap; mandatory candidate under clustering rule.

## C005 - Sony annual report removes explicit first-party PC deployment language
- section: industry_news
- status: candidate
- source_ids: S0008
- entities: Sony / PlayStation / Ghost of Yotei / Saros / Marvel's Wolverine
- facts:
  - VGC says Sony removed last year's line about deploying first-party titles to PC from a new SEC annual report.
  - Source text links the change to a pullback in upcoming single-player PC plans.
  - Same source names Ghost of Yotei, Saros, and Marvel's Wolverine as titles expected to remain PS5 exclusives.
- notes: high-value platform strategy item.

## C006 - Ori director criticizes Game Pass strategy amid slowdown discussion
- section: industry_news
- status: candidate
- source_ids: S0009
- entities: Game Pass / Xbox / Thomas Mahler / Ori / Double Fine / Compulsion / Ninja Theory
- facts:
  - Source quotes Thomas Mahler arguing Game Pass could have worked if Xbox shipped stronger content.
  - Article says last known Game Pass figure remains `34 million` from `February 2024`.
  - Source says a prior price increase shed `millions of subscribers`.
- notes: opinion-led but tied to subscription economics and rumored studio cuts; borderline include candidate.

## C007 - 《寒蝉鸣泣之时》新作 TV 动画制作决定
- section: industry_news
- status: candidate
- source_ids: S0003
- entities: 寒蝉鸣泣之时 / Studio DEEN
- facts:
  - Source title supports a new TV anime production decision.
  - Source names Studio DEEN.
- notes: adjacent IP entertainment news; weak for game-industry daily unless window is empty.

## C008 - 电竞乐园宣传稿
- section: industry_news
- status: candidate
- source_ids: S0005
- entities: 电竞乐园
- facts:
  - Source title is promotional and descriptive.
- notes: routine promo copy; likely exclude.

## C009 - 腾讯元宝父亲节合影活动
- section: ai_trends
- status: candidate
- source_ids: S0010
- entities: 腾讯元宝
- facts:
  - Source text describes a Father's Day photo-generation activity.
  - Function is consumer-facing image generation, not industry infrastructure.
- notes: lightweight marketing activation; weak AI-news value.

## C010 - 美团 tabbit 国际版免费接入多家旗舰模型
- section: ai_trends
- status: candidate
- source_ids: S0011
- entities: 美团 / tabbit / GPT-5.5 / Claude Opus 4.8 / Gemini 3.5 Flash / Kimi-2.6 / GLM-5.1 / MiniMax-M3
- facts:
  - Source text says the international app is free and bundles multiple flagship models.
  - Source text explicitly distinguishes international vs domestic model availability.
  - Item is about AI-entry competition and model distribution, not a one-off prompt tutorial.
- notes: qualifies as meaningful AI product-distribution signal.

## C011 - Mythos security capability claim reaches NSA-level systems
- section: ai_trends
- status: candidate
- source_ids: S0012
- entities: Mythos / NSA / Google Project Zero / Apple / macOS
- facts:
  - Source text says an NSA director claimed Mythos breached nearly all classified systems in hours.
  - Same text says Mythos previously cracked macOS in `5 days`, while Project Zero would need `6 months`.
  - Source text says Apple previously assumed only `10-20` teams had this capability.
- notes: strong claim from a single social-source relay; if included, should be treated as borderline and written cautiously.

## C012 - 《天堂》经典版首次攻城战新版本
- section: release_calendar
- status: candidate
- source_ids: S0013
- entities: 天堂 / 腾讯 / NCsoft
- facts:
  - Source records a `新版本` event on `2026-06-21`.
  - Source names `腾讯` as publisher and `NCsoft` as developer.
  - Source provides platform `PC` and features `2D / 奇幻 / 角色扮演 / 动作 / 怀旧`.
- notes: one of the few calendar items with company + genre support in-source.

## C013 - 《激战：大牌英雄》09:00 新游预约
- section: release_calendar
- status: candidate
- source_ids: S0027, S0006
- entities: 激战：大牌英雄 / bilibili 游戏 / NC / ArenaNet
- facts:
  - TapTap source records `09:00 开始` and `卡牌` tag.
  - Industry source backfills publisher/supervision and Guild Wars IP relationship.
- notes: strong calendar item because company/genre can be fully supported from same-window local evidence.

## C014 - TapTap single-source launches without company support
- section: release_calendar
- status: candidate
- source_ids: S0015, S0017, S0020, S0021, S0023, S0025, S0026
- entities: 2048修仙奇谭 / 幸运奶茶店 / 影之大陆 / 我的修仙人生模拟 / 沉默的宅邸 / 英雄霸业 / 败家喵
- facts:
  - These records provide event type and tags.
  - Most do not provide developer/publisher in the extracted text.
- notes: keep scanned, but many should be excluded from final body because company evidence is missing.

## C015 - 《二重螺旋》1.4 新玩法强推联机并放大独狼成本
- section: community_discourse
- status: candidate
- source_ids: S0036
- entities: 二重螺旋 / 英雄互娱
- facts:
  - Thread says 1.4 two new modes were criticized for forced grouping and consuming倍率书.
  - Source text states solo players face roughly `3x` ticket cost vs grouped players in one mode.
  - Thread also records an official follow-up limited to future ticket/material adjustments, without solving forced social and cheating complaints.
  - follow_up_scan: no separate same-window community thread in extracted pool adds materially new official clarification.
- notes: clear trigger + complaint logic + follow-up in-source; strong community item.

## C016 - 《卡厄斯梦境》国服追平国际服半年进度且无补偿
- section: community_discourse
- status: candidate
- source_ids: S0037
- entities: 卡厄斯梦境 / 腾讯代理
- facts:
  - Source text says national server will synchronize card pools/content with international server in early next month.
  - Thread frames this as compressing roughly half a year of progress into about one month after launch.
  - Complaint logic centers on skipped daily/event gacha resources and loss of future-knowledge advantage.
  - follow_up_scan: no added compensation signal appears elsewhere in the same extracted pool.
- notes: valid event-scale controversy, not just routine complaining.

## C017 - PlayStation community reacts to $80 price for old Call of Duty ports
- section: community_discourse
- status: candidate
- source_ids: S0042
- entities: PlayStation / Call of Duty / Activision / Microsoft
- facts:
  - Source title says `16-year-old` Call of Duty ports are priced at `$80`.
  - Top comments repeatedly describe them as straight ports, not remakes or remasters.
  - Complaint logic centers on missing texture/server/frame-rate upgrades despite high pricing.
  - follow_up_scan: no second same-window thread in the extracted pool materially changes the dispute.
- notes: strong cross-platform pricing backlash item.

## C018 - 《恋与深空》联名茶饮爆单与履约混乱
- section: community_discourse
- status: candidate
- source_ids: S0038
- entities: 恋与深空 / 茉莉奶白
- facts:
  - Source text claims orders surged, queues hit thousands of cups, and delivery riders argued on site.
  - Thread is labeled `疑似内容`.
  - Discussion spills into labor and platform-dispatch complaints.
- notes: sizeable discussion but verification quality is weaker; likely exclude or only borderline.

## C019 - Xbox handheld logo appears on Microsoft game pages
- section: community_discourse
- status: candidate
- source_ids: S0041
- entities: Xbox / Asus / ROG Ally
- facts:
  - Reddit thread centers on a new handheld logo appearing on official Microsoft pages.
  - Comments largely speculate it refers to partner handheld branding rather than a first-party device.
- notes: community heat exists, but the event remains largely speculative.

## C020 - Deep observation: platform holders are tightening ecosystem control and pricing
- section: deep_analysis
- status: candidate
- source_ids: S0008, S0009, S0042
- entities: Sony / PlayStation / Xbox / Game Pass / Call of Duty
- facts:
  - Sony public filing removed explicit PC deployment language.
  - Game Pass discussion in VGC focuses on content quality, subscriber plateau, and churn after price increases.
  - Community backlash around $80 legacy ports highlights rising willingness to test catalog monetization.
- notes: synthesized from same-day local evidence only; no external backfill required.
