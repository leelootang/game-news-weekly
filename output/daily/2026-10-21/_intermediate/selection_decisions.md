# 2026-10-21 日报选材决策

卡片曝光去重：历史窗口2026-10-07至2026-10-20，114条记录；逐项读取card_exposed/card_rank/card_limit/card_exposure_source。Metacore等已曝光同事件排除；本期无card_carryover，故此前卡片排名不适用。

维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均覆盖全量输入；每个source_id至少一项决策，具体数量见run_summary。

评分版本：subject_genre_v2。行业E×主体R+品类M≥5；日期、来源与曝光去重独立执行。入选I036与I213均E3×R3+M0=9。

产品日历漏挂反查：全文反扫305条industry_news与37条release_calendar，逐句按产品/日期/状态召回；错误新品上线与历史/未来节点修正保留原始审计。66个节点均通过sync生成决策。可发布多源前缀为人间异想计划11分、掘地求财：铲友齐上阵6分、无光绝境6分；后两项为未来定档，不按实际发售/测试日期门禁排除。与行业同事件不作排除理由。

## 边界与风险复核

- I053腾讯生活模拟公开稿10分：本期日期元数据与同批大量2025镜像混杂，原文未提供绝对首曝日；保留候选排除，不能凭推测给中文正式名称。
- I213：基金募集完成是本期新增资本状态；112亿元是两支基金规模，完美世界认缴额分别5000万元和1亿元。
- I045：9月主机作品本期登陆Steam，不误写新品首次发售。
- I286 Dont Nod E3R1M0=3；I246 EA Fight Night E3R1M1=4；I289 PEGI E2R1M1=3；N_ECC E1R3M1=4；N_RIOT E1R3M0=3。
- C283反作弊变更与差评实际为20日，21日采集不等于21日新事件；本期排除。
- D_DISCOVERY新增newsletter复杂度、关键词与无公开构建仿制证据，不重复昨日单纯Demo曝光成本观点。
- 日历与行业不互斥；只要独立通过多源、日期、前缀规则即可分别收录。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |

## 日历跨期重复检查

读取此前日报/周末报/周报release_calendar条目，未发现本期三个规范化产品+日期+事件已发表。RV There Yet?两条Gematsu RSS属于同一公告，只算一源；炉石两源仍为普通卡包更新；10月14日无光绝境Playtest与12月2日EA定档分别留痕。
| I001 | exclude | industry_news | 新品发售信号，但正文仅32字、无已取证重点主体或代表作，R0。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I002 | exclude | industry_news | Demo信号，不能以国产标签证明主体；无主体证据R0。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I003 | exclude | industry_news | 两款产品新品节参展宣传，不能证明首次测试。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I004 | exclude | industry_news | 试玩实际日期为10月20日；主体证据不足，不能作为本期首测。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I005 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I006 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I007 | exclude | industry_news | 新品定档，主体未证实；日历独立召回。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I008 | exclude | industry_news | 试玩节点，来源未证明研运主体层级。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I009 | exclude | industry_news | Demo开放但主体无法确认。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I010 | exclude | industry_news | 定档是日历信号，主体未证实。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I011 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I012 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I013 | exclude | industry_news | 10月20日既有新品节参展，不证明21日首次测试。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I014 | exclude | industry_news | 试玩节点，无主体重要性证据。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I015 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I016 | exclude | industry_news | 生活向联机试玩信号；网飞不在统一游戏名单，来源未证明代表产品声量，R0。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I017 | exclude | industry_news | Demo节点，无重点主体或代表作声量证据。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I018 | exclude | industry_news | 合作RPG不等于竞技；无研运主体取证，R0、M0。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I019 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I020 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I021 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I022 | exclude | industry_news | 新品试玩但来源极短、主体未证实。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I023 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I024 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I025 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I026 | exclude | industry_news | 反作弊普通工具调整；社区反应另建事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I027 | exclude | industry_news | 定档10月22日，日历独立召回，主体不明。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I028 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I029 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I030 | exclude | industry_news | 定档12月4日，行业主体不明。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I031 | exclude | industry_news | 测试开启，但正文来源49明确为10月14日开始且已有单人测试，不是21日新品首测。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I032 | exclude | industry_news | 全新试玩信号，研运主体未取证。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I033 | exclude | industry_news | 两款新作公开，未具名且无主体分层证据。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I034 | exclude | industry_news | 11月6日发售定档，R0。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I035 | exclude | industry_news | 俱乐部解散；短文未证明名单关系或代表作声量，R0。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I036 | include | industry_news | 正式公开产品名与22分钟实机，不是旧招聘复述；腾讯直属光子R3；普通开放世界ARPG不等于指定竞技品类，M0。；{"event": 3, "relevance": 3, "hook": 0, "total": 9} |
| I037 | exclude | industry_news | 仿生机器人公司与AI硬件招聘，没有已落实游戏应用，非游戏事件E0。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I038 | exclude | industry_news | MMO节奏与未来方向访谈；不是21日正式上线或新平台政策，不凭旧活动抬E。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I040 | merge into I036 | industry_news | 同日同产品正式公开事件；文中明确部分对话虚构，不使用员工数、狗主策等戏谑表述作事实。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I042 | exclude | industry_news | 米哈游《源初之结》设计评论，正文首支PV为8月26日；无本期首曝/测试状态变化。；{"event": 1, "relevance": 3, "hook": 0, "total": 3} |
| I043 | exclude | industry_news | Supercell完成Metacore收购，但已在10月19日报卡片曝光；无新状态，重复排除。 14日内同事件已收录且至少一次卡片曝光，无实质新增事实。；{"event": 3, "relevance": 3, "hook": 0, "total": 9} |
| I044 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I045 | exclude | industry_news | 9月17日既有作品10月21日扩展Steam；研运IzanagiGames已证实，但来源没有较大声量量化依据，不凭有作品即给R1。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I046 | exclude | industry_news | 公布未来12月4日发售；独立日历召回，R0。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I047 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I048 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I049 | exclude | industry_news | 10月14日开始的合作测试晚到报道；不把合作当竞技、不把采集日当首测日。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I050 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I053 | exclude | industry_news | 腾讯生活模拟新作公开稿，算分10；英文镜像与同批2025旧稿混杂，正文没有绝对首曝日期，保留候选但暂不发表以免把旧公开当新公开。；{"event": 3, "relevance": 3, "hook": 1, "total": 10} |
| I054 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I055 | exclude | industry_news | 超自然游戏旧成绩复盘，正文明确2025年；非本期新增状态。 当前译名未完成名单专名核验，R保守0，原初评留translation_unverified_original_scores。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I056 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I057 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I058 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I059 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I060 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I061 | exclude | industry_news | 版号常规审批，且正文11月不在窗口。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I062 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I063 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I064 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I065 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I066 | exclude | industry_news | 例行股东回报/分红计划，正文1日晚及2025—2027，非当前窗口异常资本事件。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I067 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I068 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I069 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I070 | exclude | industry_news | 创作历程、旧财务困难复盘，不能把过去账户见底写成本期流动性异常。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I071 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I072 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I073 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I074 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I075 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I076 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I077 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I078 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I079 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I080 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I081 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I082 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I083 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I084 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I085 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I086 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I087 | exclude | industry_news | 旧产品表现与玩法案例，正文11月上线后语境，与21日窗口不一致。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I088 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I089 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I090 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I091 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I092 | exclude | industry_news | 下周11月24—30日清单，不能把镜像采集日期改成实际测试日期。 当前译名未完成名单专名核验，R保守0，原初评留translation_unverified_original_scores。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I093 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I094 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I095 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I096 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I097 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I098 | exclude | industry_news | 终末地测试与工业设计复盘，非本期首次曝光或测试发生。 当前译名未完成名单专名核验，R保守0，原初评留translation_unverified_original_scores。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I099 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I100 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I101 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I102 | exclude | industry_news | 和平精英文旅活动案例，不是新的资本/平台或产品状态。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I103 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I104 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I105 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I106 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I107 | exclude | industry_news | 鹰角参投团队Demo报道，正文11月10日与10月17日互相冲突，无法核验本期事件日期，来源日期门禁排除。 当前译名未完成名单专名核验，R保守0，原初评留translation_unverified_original_scores。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I108 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I109 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I110 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I111 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I112 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I113 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I114 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I115 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I116 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I117 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I118 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I119 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I120 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I121 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I122 | exclude | industry_news | X-Clash孵化复盘明确为2025年10月表现，不能当2026本期市场变化。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I123 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I124 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I125 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I126 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I127 | exclude | industry_news | 制作人讲述既有作品文化、战斗与品质设计，主体层级不明。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I128 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I129 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I130 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I131 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I132 | exclude | industry_news | 独立游戏孵化空间公开与合作案例，但未证实符合重点主体关系或代表作声量，R0。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I133 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I134 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I135 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I136 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I137 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I138 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I139 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I140 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I141 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I142 | exclude | industry_news | 前字节成员独游访谈；半次元创始身份不等于重点游戏项目制作人/主策/主美，不自动R2。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I143 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I144 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I145 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I146 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I147 | exclude | industry_news | 搜打撤小游戏旧案例，原文2025；背景腾讯网易不能把实际小团队抬为R3。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I148 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I149 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I150 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I151 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I152 | exclude | industry_news | 腾讯CF手游十周年公开与国际服计划，但正文明确2025年，旧稿不因翻译采集而入选。 14日内同事件已收录且至少一次卡片曝光，无实质新增事实。；{"event": 2, "relevance": 3, "hook": 0, "total": 6} |
| I153 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I154 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I155 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I156 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I157 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I158 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I159 | exclude | industry_news | 王者荣耀歌曲文旅联动，E0。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I160 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I161 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I162 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I163 | exclude | industry_news | Unite Shanghai 2025技术分享，旧技术复盘非本期状态新闻。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I164 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I165 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I166 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I167 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I170 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I179 | exclude | industry_news | 网易历史文化联动与公益宣传，非本期高E事件。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I180 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I181 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I182 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I183 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I189 | exclude | industry_news | 项目失败机制复盘，不是新项目取消公告，主体不能由背景公司推导。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I192 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I193 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I194 | exclude | industry_news | Steam主题促销节，且正文为22日；非产品新发售。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I195 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I196 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I198 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I199 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I200 | exclude | industry_news | 独游成绩与创业历程，正文2025半年榜；没有本期新状态。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I201 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I202 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I203 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I204 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I205 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I206 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I208 | exclude | industry_news | Epic平台与UE6方向来自Unreal Fest Tokyo 2025，旧活动，PC市场R1不因UE名气变R3。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I209 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I211 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I212 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I213 | include | industry_news | 完美世界本期公告：两支已认购基金完成募资，资本状态从募资转完成；E3R3M0=9。；{"event": 3, "relevance": 3, "hook": 0, "total": 9} |
| I214 | exclude | industry_news | 工会制度解释稿，非具体资本/组织变更。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I216 | exclude | industry_news | GTA6分流预测及调查；PC/主机市场整体R1，E2R1M1=3，不因大IP提高主体。；{"event": 2, "relevance": 1, "hook": 1, "total": 3} |
| I217 | exclude | industry_news | 独游与原创IP市场评论，PC/主机市场整体R1、4?实际E2R1=2，未过线。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I218 | exclude | industry_news | Xbox未来硬件价格/档期传闻，名单外PC/主机市场R1，来源是预测并非正式决策。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I219 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I220 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I221 | exclude | industry_news | 挪威拟将Roblox纳入未成年人社交限制，但仅snippet，缺完整正文不得发表。；{"event": 2, "relevance": 3, "hook": 0, "total": 6} |
| I222 | exclude | industry_news | 演唱会取消，仅snippet；社区声明范围需另核验。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I223 | exclude | industry_news | Rotate Rings下载成绩，仅snippet且未取证主体层级。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I224 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I225 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I226 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I227 | exclude | industry_news | Innersloth合同经验访谈，主体代表作有证据但无新资本状态，E1低于线。；{"event": 1, "relevance": 1, "hook": 0, "total": 1} |
| I228 | exclude | industry_news | Fuse联合开发模式复盘，不能把流程讲解视作新重大合作；不凭发布商常识补归属。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I229 | exclude | industry_news | 发行榜短摘要，E0及snippet。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I230 | exclude | industry_news | 季度授权收入常规财报，snippet且无异常基准。；{"event": 0, "relevance": 3, "hook": 0, "total": 0} |
| I231 | exclude | industry_news | Mika融资短摘要100字；无全文、无名单关系取证。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I232 | exclude | industry_news | 创作访谈包含历史旧发售，不能作为本期新品。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I233 | exclude | industry_news | 试玩评论与设计评价，不是当期首次公开或上线。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I234 | exclude | industry_news | 作曲家职业与裁员应对复盘，无具体新公司变更。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I235 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I236 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I237 | exclude | industry_news | 常规Game Pass入库名单。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I238 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I240 | exclude | industry_news | Xbox技术升级，PC/主机平台信息R1。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I241 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I242 | exclude | industry_news | 下一代Xbox价格与档期传闻，R1未达线。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I243 | exclude | industry_news | PS5实体与数字销售结构，PC/主机市场R1。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I244 | exclude | industry_news | 潜在买方估值报道，不是成交；Xbox市场业务R1。；{"event": 3, "relevance": 1, "hook": 0, "total": 3} |
| I245 | exclude | industry_news | Game Pass服务调整传闻，R1。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I246 | exclude | industry_news | EA重启Fight Night制作消息，EA名单外，来源有代表系列与15年空窗，E3R1M1=4。；{"event": 3, "relevance": 1, "hook": 1, "total": 4} |
| I247 | exclude | industry_news | PS5安全系统更新，非游戏业务新政策。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I248 | exclude | industry_news | Xbox Labs浏览器试验演示，非新业务发布状态，且旧Labs背景已曝光。 14日内同事件已收录且至少一次卡片曝光，无实质新增事实。；{"event": 1, "relevance": 1, "hook": 0, "total": 1} |
| I249 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I251 | exclude | industry_news | 作品结束更新支持，但名单归属及代表产品声量没有本候选证据。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I252 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I253 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I255 | exclude | industry_news | 使命召唤撤离玩法开发复盘；竞技M1，但E1R1M1=2。；{"event": 1, "relevance": 1, "hook": 1, "total": 2} |
| I256 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I257 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I258 | exclude | industry_news | Xbox价格传闻重复来源。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I259 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I260 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I261 | exclude | industry_news | 复刻产品预告及未来档期，来源未证实重点主体。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I262 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I263 | exclude | industry_news | 复刻作品未来发售预告，未证实主体重要性。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I264 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I265 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I266 | exclude | industry_news | 新品发售日预告，不是现在发售，日历单独召回。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I267 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I268 | exclude | industry_news | 既有作品Switch2演示，未证明本期上线。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I269 | exclude | industry_news | Xbox FSR图形技术升级，主机整体信息R1。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I270 | exclude | industry_news | Game Pass未来调整传闻。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I271 | exclude | industry_news | GTA6啤酒品牌线下营销传闻，不是游戏跨平台上线。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I272 | exclude | industry_news | 真人宣传片拍摄猜测，不是GTA6上线或跨平台。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I274 | exclude | industry_news | 试玩前瞻与访谈；无可证主体重要性。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I275 | exclude | industry_news | 竞技战斗试玩前瞻，不证明首次测试/立项；主体重要性未证实。；{"event": 1, "relevance": 0, "hook": 1, "total": 1} |
| I276 | exclude | industry_news | 试玩前瞻，不证明本期首测。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I277 | exclude | industry_news | 杂志综合旧消息；下述逐条补卡审查，招聘不入选。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I278 | exclude | industry_news | 独游通讯与招募，非当期行业事件；日历信号逐项另审。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I279 | exclude | industry_news | 第三方升级器常规版本。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I280 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I281 | exclude | industry_news | 守望地图设计访谈；有代表作声量但非本期状态变化。；{"event": 1, "relevance": 1, "hook": 1, "total": 2} |
| I282 | exclude | industry_news | 新品节试玩推荐，不证明首测节点。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I283 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I285 | exclude | industry_news | 鬼武者复刻可能性采访，未正式公布项目。；{"event": 1, "relevance": 1, "hook": 0, "total": 1} |
| I286 | exclude | industry_news | Dont Nod启动保护程序属于异常流动性状态；代表作虽可证，但名单外R1，E3R1M0=3。；{"event": 3, "relevance": 1, "hook": 0, "total": 3} |
| I287 | exclude | industry_news | 普通既有肉鸽更新，不因借用Diablo概念升级事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I289 | exclude | industry_news | PEGI付费随机物品评级实施，报道以PC/主机EA足球案例为主，未证实移动市场整体范围，E2R1M1=3。；{"event": 2, "relevance": 1, "hook": 1, "total": 3} |
| I290 | exclude | industry_news | 复刻游戏评论，非当期明确首曝/上线。；{"event": 1, "relevance": 0, "hook": 0, "total": 0} |
| I291 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I292 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I293 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I294 | exclude | industry_news | Deadlock角色内容更新与投票，E0。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I295 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I296 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I298 | exclude | industry_news | FSR图形兼容技术扩展，PC/主机市场整体信息R1。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| I299 | exclude | industry_news | 使命召唤PC启动配置指导，普通技术说明。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I301 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I302 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I303 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I305 | exclude | industry_news | E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| A039 | include | ai_trends | 测试服务商披露人工Review、有效执行率与证据回溯的实际业务环节，属直接研发采用。 |
| A041 | exclude | ai_trends | Demo风险综合稿，所述酒鬼女神取消试玩已是旧事件；本期优先采用288的新采访细节与375的新分析，不重复普通事件摘要。 |
| A051 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A052 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A168 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A169 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A171 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A172 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A173 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A174 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A175 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A176 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A177 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A178 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A184 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A185 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A186 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A187 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A188 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A190 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A191 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A197 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A207 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A210 | exclude | ai_trends | 原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。 |
| A215 | include | ai_trends | 101次访谈的游戏研发AI采用调查，时间范围、定义与流程深度清楚。 |
| A239 | exclude | ai_trends | 创意与AI一般立场表述，没有已发生的具体使用管线或能力变化，非直接应用新闻。 |
| A250 | exclude | ai_trends | 泛AI/硬件或宽泛立场，未形成有足够证据的本期游戏直接应用；优先采用本期直接研发案例。 |
| A254 | exclude | ai_trends | 创意与AI一般立场表述，没有已发生的具体使用管线或能力变化，非直接应用新闻。 |
| A273 | exclude | ai_trends | 泛AI/硬件或宽泛立场，未形成有足够证据的本期游戏直接应用；优先采用本期直接研发案例。 |
| A284 | exclude | ai_trends | 创始人计划下一次创业使用AI原型/重复任务/测试，尚未实际落地；破产旧事实不在AI栏重复。 |
| A288 | include | ai_trends | 新采访量化ReVamp从数万Steam测试报名缩至Discord数百人，并披露人工准入与保密协议机制，区别于昨日公告。 |
| A297 | exclude | ai_trends | 泛AI/硬件或宽泛立场，未形成有足够证据的本期游戏直接应用；优先采用本期直接研发案例。 |
| A300 | exclude | ai_trends | 泛AI/硬件或宽泛立场，未形成有足够证据的本期游戏直接应用；优先采用本期直接研发案例。 |
| A304 | include | ai_trends | 恺英旗下SoonPlay20日公测，本期披露视频生成、边玩边改与私有反馈机制；报告按来源陈述，不背书全球首个等宣传。 |
| A306 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A307 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A308 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A309 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A310 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A311 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A312 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A313 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A314 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A315 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A316 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A317 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A318 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A319 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A320 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A321 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A322 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A323 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| A324 | exclude | ai_trends | 未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。 |
| I325 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I326 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I327 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I328 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I329 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I330 | merge into I036 | industry_news | 同产品同日正式公开事件，行业证据并入I036；日历仍独立评审。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I331 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I332 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I333 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I334 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I335 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I336 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I337 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I338 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I339 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I340 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I341 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I342 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I343 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I344 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I345 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I346 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I347 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 3, "relevance": 0, "hook": 1, "total": 1} |
| I348 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I349 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I350 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 3, "relevance": 0, "hook": 1, "total": 1} |
| I351 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I352 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I353 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 0, "relevance": 0, "hook": 0, "total": 0} |
| I354 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I355 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 3, "relevance": 0, "hook": 0, "total": 0} |
| I356 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I357 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I358 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I359 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I360 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| I361 | exclude | industry_news | 单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| C362 | exclude | community_discourse | 长期水楼，无可命名独立新事件。 |
| C363 | exclude | community_discourse | 旧AI复活讨论，本期仅一句联机需求延续，缺新进展。 |
| C364 | exclude | community_discourse | 标题称日本游戏普遍维护，正文当日主要是网友推测，不能写成已证实全行业事故。 |
| C365 | exclude | community_discourse | 流水榜单观察及玩家预测，不作为独立社区争议事件。 |
| C366 | exclude | community_discourse | 16日素材相似旧争议，21日两回复未提供新进展，且20日已改说法仅玩家转述。 |
| C367 | exclude | community_discourse | 创作者健康近况，非游戏业务/社区机制焦点；不依据回复补医疗判断。 |
| C368 | exclude | community_discourse | 主播来电营销趣闻，未产生足够独立争议机制，留候选。 |
| C369 | exclude | community_discourse | 19日联动争议已发表，本期仅旧争议延续，排除重复。 |
| C370 | exclude | community_discourse | 正式公开已进产业栏，同一事件不重复进入社区。 |
| C371 | include | community_discourse | 停更后周年更新计划触发回流期待与盈利/运营顾虑，完整社区事件。 |
| C372 | exclude | community_discourse | 18日跨作角色落地旧讨论，本期无新阶段。 |
| C373 | include | community_discourse | 21日晚新帖讨论演唱会取消后的住宿/交通报销范围；准确归因帖子和网友，不能把“符合条件”泛化成全额。 |
| C374 | exclude | community_discourse | 京东新主体已在20日产业卡片展示，21日只有玩家猜测，未成新事件。 |
| C283 | exclude | community_discourse | 正文明确EAC切换及差评发生于October20，虽21日采集也不能改成21日社区新事件；排除日期错位。 |
| N_PEGI | exclude | industry_news | newsletter单条线索独立评审；普通泛PC/主机市场R1或例行/存量产品成绩不足资格。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| N_STEAM_PRICE | exclude | industry_news | newsletter单条线索独立评审；普通泛PC/主机市场R1或例行/存量产品成绩不足资格。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| N_GDC | exclude | industry_news | newsletter单条线索独立评审；普通泛PC/主机市场R1或例行/存量产品成绩不足资格。；{"event": 2, "relevance": 0, "hook": 0, "total": 0} |
| N_CIRCANA | exclude | industry_news | newsletter单条线索独立评审；普通泛PC/主机市场R1或例行/存量产品成绩不足资格。；{"event": 2, "relevance": 1, "hook": 0, "total": 2} |
| N_RIOT | exclude | industry_news | newsletter单条线索独立评审；普通泛PC/主机市场R1或例行/存量产品成绩不足资格。；{"event": 1, "relevance": 3, "hook": 0, "total": 3} |
| N_ECC | exclude | industry_news | 仅约10万愿望单的既有测试后成绩快照，不是本期首曝、上线或结构性市场变化，复核E从2改1。；{"event": 1, "relevance": 3, "hook": 1, "total": 4} |
| D_DISCOVERY | include | deep_analysis | 本期newsletter完整核心正文可读；新增无公开构建也出现模仿的关键词案例及复杂产品边界，与20日泛Demo曝光成本的观察形成实质新机制。；{"relevance": 2, "insight": 3, "evidence": 3, "card": 3, "total": 11} |
| D_QA | include | deep_analysis | 两条本期已入选AI新闻共同支持：采用广不等于整合深，生成增加Review及体验判断需求；区别于20日资产导入引擎的工具可用性。；{"relevance": 2, "insight": 3, "evidence": 3, "card": 3, "total": 11} |
| R001 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限；{"event": 2, "source": 4, "company": 3, "total": 11} |
| R002 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限；{"event": 2, "source": 3, "company": 0, "total": 6} |
| R003 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限；{"event": 2, "source": 3, "company": 0, "total": 6} |
| R004 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 4, "company": 0, "total": 12} |
| R005 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 4, "company": 0, "total": 12} |
| R006 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 4, "company": 0, "total": 12} |
| R007 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 3, "company": 0, "total": 9} |
| R008 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R009 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R010 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R011 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R012 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R013 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R014 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R015 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R016 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R017 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R018 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R019 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R020 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R021 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R022 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R023 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R024 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 2, "company": 0, "total": 6} |
| R025 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R026 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R027 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R028 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R029 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R030 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R031 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R032 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R033 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 2, "source": 2, "company": 0, "total": 4} |
| R034 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R035 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R036 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R037 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R038 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R039 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R040 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R041 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R042 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R043 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R044 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R045 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R046 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R047 | exclude | release_calendar | 单源不具备正文资格；{"event": 3, "source": 1, "company": 0, "total": 3} |
| R048 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 3, "company": 0, "total": 3} |
| R049 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R050 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R051 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R052 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R053 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R054 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R055 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R056 | exclude | release_calendar | 单源不具备正文资格；{"event": 2, "source": 1, "company": 0, "total": 2} |
| R057 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R058 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R059 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R060 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R061 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R062 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R063 | exclude | release_calendar | 单源不具备正文资格；{"event": 1, "source": 2, "company": 0, "total": 2} |
| R064 | exclude | release_calendar | 单源不具备正文资格；{"event": 1, "source": 1, "company": 0, "total": 1} |
| R065 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 1, "company": 0, "total": 1} |
| R066 | exclude | release_calendar | 事件日期不在报告窗口；{"event": 1, "source": 1, "company": 0, "total": 1} |
