# 本日报使用的数据来源

## 本地输入文件夹

- `news_data/ai_trends/2026-06-01/`
- `news_data/community_discourse/2026-06-01/`
- `news_data/deep_analysis/2026-06-01/`
- `news_data/industry_news/2026-06-01/`
- `news_data/release_calendar/2026-06-01/`

## 抽取产物

- `_intermediate/report_inputs.jsonl`（218 条记录，0 提取失败）
- `_intermediate/report_inputs_summary.md`
- `_intermediate/report_inputs_index.md`
- `_intermediate/event_candidates.md`（C001–C028）
- `_intermediate/selection_decisions.md`

## Item Source Map

### 一、行业新闻

| # | 标题 | candidate | source_ids | 关键来源 / URL |
| --- | --- | --- | --- | --- |
| 1 | Atari 收购 Hipster Whale | C001 | S0050, S0060, S0062, S0064 | gamesindustry.biz / pocketgamer.biz / gamedeveloper.com / mobilegamer.biz |
| 2 | CD Projekt《巫师4》最密集开发 | C002 | S0047 | gamesindustry.biz |
| 3 | 腾讯《三角洲行动》UGC 平台 | C004 | S0055 | pocketgamer.biz |
| 4 | 诗悦网络《望月》新实机 PV + 广州线下试玩 | C030 | S0014, S0024, S0027 | gamelook.com.cn / youxituoluo.com / youxituoluo.com（陀螺周报） |
| 5 | 《Block Blast!》Google Play 下架 | C005 | S0022, S0052 | youxituoluo.com / pocketgamer.biz |
| 6 | 《神鬼寓言》延期至 2027/2 | C022 | S0006, S0046, S0061 | gcores.com / gamesindustry.biz / gamedeveloper.com |
| 7 | 美国法案：付费游戏停服后仍须可玩 | C027 | S0069 | videogameschronicle.com |
| 8 | 友谊时光首款乙游《心跳陷落》5/27 上线（borderline） | C024 | S0045 | new.qq.com (youxixinzhi_qqnews) |
| 9 | 网易雷火《归唐》将于夏日游戏节公布新消息（borderline） | C025 | S0003 | gcores.com |
| 10 | 灵犀互娱《宗师之上》冲入 iOS 畅销榜 TOP10（borderline） | C026 | S0013 | gamelook.com.cn |

### 二、AI 新闻

| # | 标题 | candidate | source_ids | 关键来源 / URL |
| --- | --- | --- | --- | --- |
| 1 | MiniMax M3 | C007 | S0081 | minimax.io |
| 2 | 智能体走向记忆 / 部署 / 服务入口 | C008 | S0092, S0093, S0098, S0103 | TencentHunyuan(X) / openai.com / ithome.com / huggingface.co |
| 3 | 一箭又一箭 AI 全自动生成关卡（borderline） | C028 | S0025 | youxituoluo.com |

### 三、新游发布 / 产品日历

calendar 内部排序信号：

| # | 游戏 | candidate | source_ids | 本地证据信号 |
| --- | --- | --- | --- | --- |
| 1 | 崩坏：星穹铁道 4.3 | C011 | S0115, S0145 | 两个 calendar 源（haoyou_kuaibao_3839、ceshibiao_17173）同时记录 |
| 2 | 明日方舟 × 怪物猎人 联动 | C012 | S0116, S0135 | 两个 calendar 源（haoyou_kuaibao_3839、taptap_app_calendar）同时记录，且为重要 IP 联动 |
| 3 | 最终的梦幻岛 删档/限量测试 | C013 | S0130, S0137, S0149 | 三个 calendar 源（haoyou_kuaibao_3839、taptap_app_calendar、wanjiang_16p_newgame）共同记录 |
| 4 | 代号：地心 预约 + 首测预告（borderline） | C014 | S0111, S0183 | 两个 calendar 源（haoyou_kuaibao_3839、taptap_app_calendar）同时记录，但 6/1 仅为预约/招募，首测在 6/12 |

### 四、玩家舆论 / 社区动态

| # | 标题 | candidate | source_ids | 关键来源 / URL |
| --- | --- | --- | --- | --- |
| 1 | 《重返未来：1999》240 万差评 + 长文致歉 | C021 | S0017 | gamelook.com.cn |
| 2 | 《燕云十六声》新地图 NPC 文案续争议 | C015 | S0197, S0200 | bbs.nga.cn |
| 3 | 《鸣潮》Warframe 联动 + 开发者访谈解读 | C016 | S0196, S0198 | bbs.nga.cn |

### 五、行业精选 / 深度观察

| # | 标题 | candidate | source_ids | 关键来源 / URL |
| --- | --- | --- | --- | --- |
| 1 | Scopely 移动帝国高集中度 | C019 | S0217 | naavik.co |
| 2 | 吉比特《杖剑传说》一周年案例（borderline） | C029 | S0020 | m.sohu.com (youxiputao_sohu) |
| 3 | Call of Duty 在 GTA 6 阴影下的反弹（borderline） | C020 | S0218 | thegamebusiness.com |

## 排除条目（值得审计留痕）

| candidate | 标题 | 排除理由 |
| --- | --- | --- |
| C003 | Rockstar 工会成立 | 用户反馈：西方主机 3A 劳资治理对沐瞳业务实操参考意义弱 |
| C006 | MLBB MSC/MWI 2026 EWC 赛制扩容 | Hard Stop：Moonton/MLBB 屏蔽规则 |
| C009 | OpenAI Stargate 1GW 数据中心开工 | 基础设施信号，与游戏直接相关度低 |
| C010 | 4 月全球 AI 应用下载收缩 | 市场背景，与游戏行业操作间接 |
| C017 | 《龙之谷：启程》宣传图疑似使用 LoL 素材 | 单源单线，玩家指控未证实 |
| C018 | 少女前线设定集 USB 缺录 OST | 售后小事件，体量不够 |
| C023 | 《铁拳8》总监池田离职 | 用户反馈：海外老 IP + 端/主机格斗作品的人事变动与用户业务弱相关 |

## 缺失目录 / 数据缺口

无。218 条记录全部成功提取，无 extract 失败、无空 text 记录。

## 备注

- 本次按新版 SKILL（2026-06-02 修订）"宁多勿少"原则执行：6 条 borderline 候选保留在正文，由读者最终筛选。
- 在审计中保留了 C006（沐瞳事件），但已按 Hard Stop 从正文排除。
- 老版本日报漏选《重返未来：1999》240 万差评事件，本次重做后已补入玩家舆论段首条。
