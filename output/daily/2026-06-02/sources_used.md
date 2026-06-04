# 本日报使用的数据来源｜2026-06-02

## 本地输入文件夹

- `news_data/ai_trends/2026-06-02/`
- `news_data/community_discourse/2026-06-02/`
- `news_data/deep_analysis/2026-06-02/`
- `news_data/industry_news/2026-06-02/`
- `news_data/release_calendar/2026-06-02/`

## 抽取产物

- `_intermediate/report_inputs.jsonl`（198 条记录，0 提取失败，1 条 text 为空：S0033 ChinaJoy 摄影区招募）
- `_intermediate/report_inputs_summary.md`
- `_intermediate/report_inputs_index.md`
- `_intermediate/event_candidates.md`（C001–C021 + 17 项 exclude）
- `_intermediate/selection_decisions.md`

## Item Source Map

### 一、行业新闻

| # | 标题 | candidate | source_ids | 关键来源 |
| --- | --- | --- | --- | --- |
| 1 | 王者荣耀世界 S1 创开服畅销榜最高 + 制作人换人 | C001 | S0021, S0024, S0189 | gamelook.com.cn / cgames.com / bbs.nga.cn |
| 2 | 网易 Q1 游戏业务 +7% 至 37 亿美元 | C002 | S0050 | pocketgamer.biz |
| 3 | 网易 Quantic Dream 取消 MMO 项目 | C003 | S0035 | youxichaguan.com (en) |
| 4 | 字节代理《境·界 刀鸣》折戟，名臣健康补偿 1 亿 | C004 | S0018 | gamelook.com.cn |
| 5 | 加州 AB1921 通过 | C005 | S0038 | gamesindustry.biz |
| 6 | 抖音游戏特色人群白皮书 | C006 | S0036 | youxichaguan.com |
| 7 | 联想 G02 掌机预装任天堂游戏事件（borderline） | C007 | S0017 | gamelook.com.cn |
| 8 | PlayStation 一方销量回升（borderline） | C008 | S0043, S0062, S0071 | gamesindustry.biz / gamedeveloper.com / videogameschronicle.com |

### 二、AI 新闻

| # | 标题 | candidate | source_ids | 关键来源 |
| --- | --- | --- | --- | --- |
| 1 | 智能体工具向具体业务场景渗透 | C009 | S0083, S0088, S0098 | x.com (Google) / openai.com / anthropic.com |
| 2 | 阶跃星辰 Step 3.7 Flash | C010 | S0090 | x.com (StepFun_ai) |
| 3 | Alphabet 拟融资 800 亿 AI 资本支出（borderline） | C011 | S0081 | bloomberg.com |

### 三、新游发布 / 产品日历

| # | 游戏 | candidate | source_ids | 本地证据信号 |
| --- | --- | --- | --- | --- |
| 1 | 战双帕弥什《长路归航》 | C012 | S0104, S0112 | 两个 calendar 源（ceshibiao_17173 + haoyou_kuaibao_3839）同时记录 |
| 2 | 二重螺旋《银星奔流》 | C013 | S0110, S0137 | 两个 calendar 源（haoyou + TapTap）同时记录 |
| 3 | 风之国世界 6/3 上线 | C014 | S0117, S0165 | 两个 calendar 源（haoyou + TapTap），6/2 18:00 预下载 |
| 4 | 夜幕之下 公测前瞻直播（borderline） | C015 | S0118, S0022 | 跨 section：release_calendar（haoyou）+ industry_news（gamelook《6月17款新游》专题）重合 |

### 四、玩家舆论 / 社区动态

| # | 标题 | candidate | source_ids | 关键来源 |
| --- | --- | --- | --- | --- |
| 1 | 燕云十六声 NPC 文案争议第三波 | C016 | S0181, S0186, S0191 | bbs.nga.cn |
| 2 | 鸣潮 Warframe 联动余波 + 联动池珊瑚门槛 | C017 | S0174, S0187 | bbs.nga.cn |
| 3 | 异环 国际服宣传图无蟑螂（borderline） | C018 | S0184 | bbs.nga.cn |
| 4 | 金山软件 Q1 未提《尘白禁区》（borderline） | C019 | S0190 | bbs.nga.cn（含金山官方业绩公告 + 电话会议互证） |

### 五、行业精选 / 深度观察

| # | 标题 | candidate | source_ids | 关键来源 |
| --- | --- | --- | --- | --- |
| 1 | Embracer / Fellowship Entertainment 重组 | C020 | S0198 | thegamebusiness.com |
| 2 | 二游大厂过招分析：鸣潮 vs 原神（borderline） | C021 | S0023 | gamelook.com.cn |

## 排除条目（值得审计留痕）

| candidate | 标题 | 排除理由 |
| --- | --- | --- |
| - | 铁拳8 总监池田离职 | 用户反馈：海外老 IP + 端/主机格斗作品的人事变动与用户业务弱相关 |
| - | Tomb Raider 推迟至 2027/2 | 海外主机 3A 跳票 + 同源 2 条 |
| - | Streets of Rage 电影编剧 | 影视改编新闻 |
| - | 联想 ROG Xbox Ally X20 | 主机/掌机硬件规格更新 |
| - | OpenAI 佛州起诉 / Meta AI 被劫持 / Sam Altman AI 政治 | AI 法律/政治/安全话题与游戏直接迁移弱 |
| - | Krea / Cosmos / Holo3.1 等 AI 模型小更新 | AI 工具新版本但与游戏研发应用无落地 |
| - | Skeletor: Until Next Time（Mattel 首款自研） | IP 改编小项目，体量不够 |
| - | Vietnamese / Nordic / Morocco / NZ 区域行业数据 | 区域市场报告，与用户优先市场相关性弱 |
| - | 杨国辉于泰国失联 | 个人安全事件而非行业舆情 |
| - | 第五人格亚运会版本立绘和谐 | 单源、范围窄 |
| - | Pokemon 鸭子坐视频被举报下架 | 单源争议、影响面小 |
| - | 米哈游星铁 fsn 联动强推双王 | 单源版本话题 |
| - | 战舰少女与南京舰联动疑非官方 | 单源、影响小 |
| - | 洛克王国流水跌出 20 名 | 单源数据流言 |
| - | 腾讯王世杰项目组执行制作人离职 | 单 NGA 源，"王世杰"项目身份在公开渠道未明确互证 |
| - | 归唐删去单机表述疑似转手游 | 单 NGA 源猜测，未经官方互证 |

## 缺失目录 / 数据缺口

无。198 条记录全部成功提取（0 失败），仅 1 条 text 为空（S0033 ChinaJoy 摄影区招募），未被选入正文。

## Hard Stops 自检

| # | 项 | 状态 |
|---|---|---|
| 1 | lint 零 error | ✅（4 条 WARN 是新 SKILL 上限放宽导致，预期；1 条 empty text 是 S0033，未入选）|
| 2 | 正文无沐瞳 / MLBB | ✅ |
| 3 | 正文无"启发/建议动作" | ✅ |
| 4 | calendar 正文无 pipeline 语言 | ✅（4 条均只描述产品事件本身）|
| 5 | 每个正文 item 在 Item Source Map | ✅（21 项全部对应）|
| 6 | industry vs community 同事件不重复 | ✅（王者荣耀世界仅在 industry；鸣潮 industry 走分析 / community 走争议；燕云仅在 community）|
| 7 | 公司名 / 产品名 / 数字 / 日期都能在 source `text` 找到 | ✅（已通过 Bash + UTF-8 读取关键 26 条 source 原文核对，规避 PowerShell GBK 问题）|

## 备注

- 多源前置扫描（SKILL workflow 第 4 步）识别出 6 组多源事件：王者荣耀世界 / PlayStation 一方 / 燕云十六声 / 鸣潮 / 4 款新游日历，全部按规则形成候选卡。
- 排除 17 项中 16 项有显式理由，铁拳8 一项继承 6/1 用户反馈的弱相关清单决定。
