# 本日报使用的数据来源｜2026-06-02

## 本地输入文件夹

- `news_data/ai_trends/2026-06-02/`
- `news_data/community_discourse/2026-06-02/`
- `news_data/deep_analysis/2026-06-02/`
- `news_data/industry_news/2026-06-02/`
- `news_data/release_calendar/2026-06-02/`

## 抽取产物

- `_intermediate/report_inputs.jsonl`（206 条记录，0 提取失败，1 条 text 为空：S0028 ChinaJoy 摄影区招募升级）
- `_intermediate/report_inputs_summary.md`
- `_intermediate/report_inputs_index.md`
- `_intermediate/event_candidates.md`
- `_intermediate/selection_decisions.md`

## Item Source Map

### 一、行业新闻

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | 《王者荣耀世界》S1 上线创开服畅销榜最高 + 原执行制作人李新平离职 | S0008, S0046, S0036, S0021, S0197 | gamelook.com.cn / NGA / cgames |
| 2 | 网易 Q1 游戏业务同比增长 7% 至 37 亿美元 | S0063, S0020 | pocketgamer.biz |
| 3 | 网易《破碎之地》制作人吴晓创业，首曝 PVE 搜打撤新作《逃离动物城》 | S0042, S0123 | gamelook.com.cn + release calendar 交叉互证 |
| 4 | 网易海外子公司 Quantic Dream 取消 MMO 项目并启动内部重组 | S0030 | youxichaguan.com (en) |
| 5 | 字节代理《境·界 刀鸣》折戟：研发商奥术亏 3146 万、需补偿名臣健康 1 亿 | S0004 | gamelook.com.cn |
| 6 | 加州州议会通过 AB1921 "Stop Killing Games / Protect Our Games Act" | S0038 | gamesindustry.biz |
| 7 | 抖音游戏特色人群白皮书：65.3% 流水增量来自上线超 1 年的成熟产品 | S0032 | youxichaguan.com |
| 8 | 联想被指 G02 复古掌机预装上千款任天堂游戏，公司称为第三方私自添加（borderline） | S0002 | gamelook.com.cn |
| 9 | PlayStation 一方游戏销量小幅回升，结束五年下滑（borderline） | S0047, S0062, S0079, S0041 | gamesindustry.biz / gamedeveloper.com / vgc |

### 二、AI 新闻

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | 智能体工具向具体业务场景渗透：Codex 知识工作 + Google AI Studio 应用集成 + Anthropic 关键基础设施扩容 | S0096, S0091, S0106 | openai.com / x.com (Google) / anthropic.com |
| 2 | 阶跃星辰 Step 3.7 Flash 发布，主打推理效率 | S0098 | x.com (StepFun_ai) |
| 3 | Alphabet 拟通过股权融资 800 亿美元用于 AI 资本支出（borderline） | S0089 | bloomberg.com |

### 三、新游发布 / 产品日历

| # | 游戏 | source_ids | 本地证据信号 |
| --- | --- | --- | --- |
| 1 | 产品日历 - 战双帕弥什 | S0112, S0120 | 两个 calendar 源同时记录新版本「长路归航」 |
| 2 | 产品日历 - 二重螺旋 | S0118, S0145 | 两个 calendar 源同时记录新版本「银星奔流」 |
| 3 | 产品日历 - 风之国世界 | S0125, S0173 | 两个 calendar 源记录 6/2 18:00 预下载、6/3 上线 |
| 4 | 产品日历 - 夜幕之下 | S0126, S0009 | 跨 section：release_calendar + industry_news《6月17款新游》专题重合 |

### 四、玩家舆论 / 社区动态

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | 《燕云十六声》新地图 NPC 文案被指阴阳岳飞，运营连续三次反复修改 | S0189, S0194, S0199 | bbs.nga.cn |
| 2 | 《鸣潮》Warframe 联动余波 + 联动池珊瑚获取门槛被指变相涨价 | S0182, S0195 | bbs.nga.cn |
| 3 | 异环 国际服宣传图删去蟑螂，与国服版本不符（borderline） | S0192 | bbs.nga.cn |
| 4 | 金山软件 Q1 业绩公告未提《尘白禁区》（borderline） | S0198 | bbs.nga.cn（含金山官方业绩公告 + 电话会议互证） |

### 五、行业精选 / 深度观察

| # | 标题 | source_ids | 关键来源 |
| --- | --- | --- | --- |
| 1 | Embracer 把 Tomb Raider、Kingdom Come、Dead Island、Middle-earth 收拢成 Fellowship Entertainment | S0206 | thegamebusiness.com |
| 2 | 二游大厂过招：鸣潮 vs 原神的"路线对立"其实是生命周期错位（borderline） | S0010 | gamelook.com.cn |

## 排除条目（值得审计留痕）

| 标题 | 排除理由 |
| --- | --- |
| 铁拳8 总监池田离职 | 用户反馈：海外老 IP + 端/主机格斗作品的人事变动与用户业务弱相关 |
| Tomb Raider 推迟至 2027/2 | 海外主机 3A 跳票 + 同源 2 条 |
| Streets of Rage 电影编剧 | 影视改编新闻 |
| 雅达利收购天天过马路开发商 | 海外并购、与用户优先市场弱相关 |
| 华硕 ROG Xbox Ally X20 | 主机/掌机硬件规格更新 |
| OpenAI 佛州起诉 / Meta AI 被劫持 / Sam Altman AI 政治 | AI 法律/政治/安全话题与游戏直接迁移弱 |
| Krea / Holo3.1 / MiniCPM 等 AI 模型小更新 | AI 工具新版本但与游戏研发应用无落地 |
| Mattel Masters of the Universe 首款自研 | IP 改编小项目，体量不够 |
| Vietnamese / Nordic / NZ / 欧洲区域行业数据 | 区域市场报告，与用户优先市场相关性弱 |
| 杨国辉于泰国失联 | 个人安全事件而非行业舆情 |
| 第五人格亚运会版本立绘和谐 | 单源、范围窄 |
| Pokemon 鸭子坐视频被举报下架 | 单源争议、影响面小 |
| 米哈游星铁 fsn 联动强推双王 | 单源版本话题 |
| 战舰少女与南京舰联动疑非官方 | 单源、影响小 |
| 洛克王国流水跌出 20 名 | 单源数据流言 |
| 王世杰项目组执行制作人离职 | 单 NGA 源，项目身份在公开渠道未明确互证 |
| 归唐删去单机表述疑似转手游 | 单 NGA 源猜测，未经官方互证 |

## 缺失目录 / 数据缺口

无。206 条记录全部成功提取（0 失败），仅 1 条 text 为空（S0028 ChinaJoy 摄影区招募升级），未被选入正文。

## Hard Stops 自检

| # | 项 | 状态 |
|---|---|---|
| 1 | lint 零 error | ✅（industry 9 条、release/discourse 数量警告为 SKILL 上限放宽导致，预期；1 条 empty text 为 S0028，未入选）|
| 2 | 正文无沐瞳 / MLBB / 决胜巅峰 | ✅（S0042 原文提及沐瞳《头号禁区》，已在正文剔除）|
| 3 | 正文无"启发/建议动作" | ✅ |
| 4 | calendar 正文无 pipeline 语言 | ✅（4 条均只描述产品事件本身）|
| 5 | 每个正文 item 在 Item Source Map | ✅（22 项全部对应，标题逐字一致）|
| 6 | industry vs community 同事件不重复 | ✅（王者荣耀世界仅在 industry；鸣潮 industry 走分析 / community 走争议；燕云仅在 community）|
| 7 | 公司名 / 产品名 / 数字 / 日期都能在 source `text` 找到 | ✅（已通过 Bash + UTF-8 读取核对，规避 PowerShell GBK 问题）|

## 备注

- 本版基于 6/1 数据补跑后的重新抽取（206 条，较旧版 198 条新增 8 条），所有 S 编号已对齐新 `report_inputs.jsonl`。
- 较旧版正文新增「网易《破碎之地》制作人吴晓创业」一条（industry #3），由 industry_news S0042 + release_calendar S0123 跨 section 互证。
