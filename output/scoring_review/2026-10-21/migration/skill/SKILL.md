---
name: game-industry-report
description: 从本工作区 news_data 的 JSONL、索引和采集审计记录生成可审计的游戏行业日报、周报、周末报或月报。用户要求游戏行业报告、AI 游戏新闻、新游产品日历、玩家舆论或深度观察时使用；必须先生成中间审计产物，再写正文并通过两道校验。
---

# Game Industry Report

## 必读路由

先读本文件。再按任务读取一层 reference，不要跳过适用文件：

- 行业新闻：`references/industry-scoring.md` 与 `references/focus-subjects.md`（主体与日历共用名单）
- AI 新闻：`references/ai-news.md`
- 产品日历：`references/release-calendar.md`
- 玩家舆论：`references/community-discourse.md`
- 深度观察或周报深度卡选择：`references/deep-observation.md`
- 中间产物、来源映射、JSON schema 与校验：`references/artifact-contract.md`

生成完整报告时五份都读；只处理单一分区时读对应 reference 与 `artifact-contract.md`。

## 报告类型与目录

时区默认 Asia/Shanghai。

| 类型 | 窗口 | 目录 | 文件名 |
| --- | --- | --- | --- |
| 日报 | 指定自然日 | `output/daily/<date>/` | `game_industry_daily_<date>.md` |
| 周报 | 指定起止日 | `output/weekly/<start>_to_<end>/` | `game_industry_weekly_<start>_to_<end>.md` |
| 周末报 | 指定起止日，采用日报式逐条判断 | `output/weekend/<start>_to_<end>/` | `game_industry_weekend_<start>_to_<end>.md` |
| 月报 | 指定自然月 | `output/monthly/<YYYY-MM>/` | `game_industry_monthly_<YYYY-MM>.md` |

数据缺失时写明实际覆盖范围；整个窗口无数据则停止，不补造、不联网补缺。

## 强制工作流

1. 锚定报告类型、窗口、输出目录和固定文件名。
2. 周五周报在抽取前先运行 `python scripts/feishu_deep_review.py status --weekly-id <目标周报ID> --json`。若有目标 ID 的有效回执而 selection 尚不存在，必须按回执原话与候选文件整理 selection，写齐飞书来源、回执 ID、正文/主卡/融合参考候选 ID，并通过 `deep_observation_handoff.py lint-selection`；已有回执但整理或 lint 失败时停止，不得降级为无选择。完全没有有效回执时不自动代选，允许省略深度栏继续周报。完整规则见 `references/deep-observation.md` 与 `references/artifact-contract.md`。
3. 运行 `scripts/extract_report_inputs.py`，生成全量 `report_inputs.jsonl`、summary、无截断 index、产品日历审计和来源质量审计。周报存在目标 ID selection 时必须传 `--deep-selection <selection.md>`，把候选窗口早一天的已选来源补入 deep-only 输入。
4. 阅读 summary 与完整 index；以全量 JSONL 为最终真源。提取失败、空正文或预期目录缺失时先处理，不能静默跳过。
5. 在写行业候选前运行 `<workspace>/scripts/build_industry_history.py`，同时阅读生成的 JSON 与 Markdown。除事件、事实和历史窗口外，必须读取每条历史项的 `card_exposed`；完整报告出现过不等于订阅卡片已经展示。具体去重与补位规则见 `references/industry-scoring.md`。
6. 对行业新闻做独立事件聚类：只有同一主体或产品、同一事件日期、同一事件才能合并；随后按 `references/ai-news.md` 反扫全部行业新闻候选，将符合 AI 采用标准的独立事件转入 AI 候选，行业新闻与 AI 新闻不得重复入选。产品日历改按规范化产品名 + 事件日期聚类，详见 reference。
   行业采用`subject_genre_v2`：E事件类型不变，R按主体重要性0–3，M命中重点品类取1否则0，各类型统一≥5。国内/手游/品类标签不自动取得R3；PC/主机产品按主体判断。新决策JSON根对象写评分版本，主体/品类逐字取证见`references/industry-scoring.md`。
   日报、周报、周末报仅对产品日历启用正常窗口结束日 +1 的及时性事件窗口；输入采集日期和其他分区窗口不得随之扩展。
7. 先写 `event_candidates.md` 和 `selection_decisions.md`，再写 `report_items.json` 与 `selection_decisions.json`。周四深度候选在评分前必须先通过 `references/deep-observation.md` 的来源质量、主题级合并、证据密度与首读清晰度门禁；数量不是目标，不得靠拆题、降门槛或堆普通新闻增加候选数。行业历史审计须区分 `repeat_only`、`material_update` 与 `card_carryover`；每期最多一条达到分数线且从未在订阅卡片展示的历史同事件可标 `card_carryover=true`。每条深度 item 同时写 `card_copy`，包含来源标签、一句话总结与 3–6 条核心洞察；具体规则见 `references/deep-observation.md`。用 `<workspace>/scripts/sync_release_decisions.py` 从审计 JSON 确定性同步产品日历决策（日报/周末 `--max-items 4`，周报 7，月报 12）；不要手算或重排。每条正文事实必须先读 source 的 `text`，禁止凭标题、常识或记忆补写。
8. 写最终 Markdown。行业新闻与社区舆论同一事件不得重复：前者写商业/产品事实，后者写玩家反应和后续。行业新闻与产品日历不做跨栏去重：同一产品/事件可以分别通过两栏门槛；不得仅因已进入行业新闻而排除产品日历。日历内部同产品同日期聚类、跨期重复、多源、时间窗口、排序与上限仍按原规则执行。
9. 用 `scripts/report_artifacts.py generate-sources` 自动生成 `sources_used.md`；禁止手写来源映射。
10. 运行 `report_lint.py` 与 `report_artifacts.py validate --require-artifacts`，两者均须零 error。warning 在结果摘要中说明。

## 报告结构

```markdown
# 游戏行业{报告类型}｜{日期或窗口}

## 一、行业新闻
### 1. 标题

## 二、AI 新闻
### 1. 标题

## 三、新游发布 / 产品日历
- 单产品 bullet

## 四、玩家舆论 / 社区动态
### 1. 标题

## 五、行业精选 / 深度观察
### 1. 标题
```

新闻、AI、社区、深度条目只能用连续的 `### N. 标题`。产品日历只能用单产品 `- ` bullet，禁止小标题和多产品合并。

## 飞书卡片呈现边界

报告 Markdown 的“标题 + 正文”是审计与长文结构，不得原样映射成飞书卡片的视觉分行。飞书报告卡片由 `<workspace>/scripts/feishu_common.py` 转换，并遵守：

- 主卡片每个分区默认最多展示 10 条；玩家舆论采用更严格的分区上限：日报/周末报最多 2 条，周报最多 3 条。预演、正式群发、订阅补发、菜单重发和反馈展开必须共用同一常量与同一选择函数，禁止各路径自行设置不同默认值。

- 行业新闻：每项只占一个 bullet、一个 Markdown 行；从当期 `_intermediate/selection_decisions.json` 读取 E×R+M 总分，只对新评分版本满分10（历史旧版本满分11）的条目加粗标题第一个短句，其他分数或缺失分数不加粗。补充事实若保留，必须在同一行接续且不加粗；分数本身不得显示在卡片中。
- 行业新闻 `card_carryover=true` 时必须保证进入前 10；若原位置在截断线外，则替换第 10 条普通行业新闻。`card_carryover` 只是内部筛选与审计状态，报告 Markdown、网页、飞书卡片和飞书文档中的标题、正文及视觉样式必须与普通行业新闻完全一致，禁止显示“补位”“上期卡片未展示”、`card_carryover` 或任何同义标记。每份报告最多一条内部补位。
- 产品日历：每项只占一个 bullet、一个 Markdown 行，并保留“厂商/品类/型态 + 产品名 + 日期/平台/事件”的原句顺序，不得把“产品名 + 日期 + 事件”抽到句首；卡片中省略产品名与日期之间的“于”。日报、周末报、周报均将前 2 项整条加粗，其余条目不加粗。
- AI 新闻：与行业新闻保持相同信息密度，每项一个 bullet、一个 Markdown 行，使用“标题 + 一条不重复的事实补充”；全部不加粗。
- 玩家舆论：保留“加粗标题 + 下一行摘要”的两层结构；日报/周末报最多 2 条，周报最多 3 条。
- 独立深度卡：不得原样展示长段“观察 / 分析”。从 `report_items.json` 的 `card_copy` 读取来源标签、一句话总结和 3–6 条核心洞察；正文标题显示“来源标签：原标题”，洞察区标题固定为“核心洞察”且不显示条数。每条使用“加粗短标题 + 一句解释”，数量按独立机制决定，不拆句凑数。

卡片格式测试必须断言行业新闻与产品日历没有缩进续行；不得因报告 Markdown 使用 `###` 标题而恢复“标题一行、正文下一行”的旧展示。

正式订阅者群发后，发布日志必须记录实际卡片条目清单和每分区上限。仅面向订阅者且成功数过半的群发算作 `card_exposed=true`；预演、单人测试、菜单重发或个别补发不改变全局曝光状态。

## 飞书文档权限

日报、周末报、周报的飞书 docx 默认并长期授权为外部链接只读：开启外部访问并设置 `link_share_entity=anyone_readable`。创建、复用或群发这三类文档时直接应用该权限，不得为公开只读权限再次请求人工确认或暂停发布。

权限设置与回读只作为自动技术校验，防止文档意外不可访问或获得编辑权限；严禁 `anyone_editable`、`tenant_editable` 等编辑权限。权限接口异常时如实报告，不把“是否允许公开只读”作为人工门禁。

## 分区数量

| 分区 | 日报 | 周末报 | 周报 | 月报 |
| --- | --- | --- | --- | --- |
| 行业新闻 | E×R+M ≥5 即入选 | E×R+M ≥5 即入选 | E×R+M ≥5 即入选 | E×R+M ≥5 即入选 |
| AI 新闻 | 1–3 | 1–3 | 2–6 | 4–8 |
| 产品日历 | 最多 4 | 最多 4 | 最多 7 | 最多 12 |
| 玩家舆论 | 1–2 | 1–2 | 2–3 | 3–6 |
| 深度观察 | 默认 1–2 | 默认 1–2 | 只消费用户周四选择，无固定条数 | 1–3 |

除行业新闻绝对阈值、产品日历上限，以及玩家舆论的日报/周末报最多 2 条、周报最多 3 条外，其余均为软目标；没有合格内容可以少写。行业新闻不设硬性条数上限，也不为凑目标条数降分或截断同分项；各报告行业阈值统一为5；周报通过独立事件合并与跨期规则汇总。周报没有有效深度 selection 时允许省略第五节，不自动替用户选择。周四候选数据固定覆盖上周四至本周三，但 selection 按目标周报“上周五至本周四”的 ID 命名；具体双窗口交接与卡片门禁见 `references/deep-observation.md`。

## 最终正文硬停止

提交前逐项确认：

1. 正文不出现 Moonton、沐瞳、Mobile Legends: Bang Bang、MLBB、决胜巅峰。
2. 正文不出现“对我司启发、建议动作、值得借鉴、可借鉴、启示”等业务指令。
3. 每个公司名、产品名、数字和日期均有对应 source `text` 原文证据；读不到原文就排除。
4. 产品日历不出现 source id、JSONL、本地证据、多源记录等流程语言。
5. 每个正文 item 均存在于自动生成的 Item Source Map，并有真实 Source Details URL。
6. 行业新闻、AI、社区、深度标题格式正确；产品日历为单产品 bullet。
7. 深度 item 的 `card_copy` 含真实来源标签、只有一行总结且包含 3–6 条非空、互不重复的洞察；卡片文案不新增正文和来源不支持的事实。
8. 两道校验零 error；不得以人工目测替代。

## 命令

所有 Python 命令设置 `PYTHONUTF8=1`。

```powershell
python "<skill_root>\scripts\extract_report_inputs.py" --workspace "<workspace>" --report-type daily --date YYYY-MM-DD
python "<skill_root>\scripts\extract_report_inputs.py" --workspace "<workspace>" --report-type weekly --start YYYY-MM-DD --end YYYY-MM-DD --deep-selection "<workspace>\output\deep_observation_review\<weekly-id>_selection.md"
python "<skill_root>\scripts\report_lint.py" --report "<report.md>" --sources "<sources_used.md>" --inputs "<report_inputs.jsonl>" --report-type daily
python "<workspace>\scripts\report_artifacts.py" validate --report "<report.md>" --sources "<sources_used.md>" --inputs "<report_inputs.jsonl>" --items "<report_items.json>" --decisions "<selection_decisions.json>" --release-audit "<release_calendar_audit.json>" --require-artifacts
```

周报传 `--report-type weekly`；周末报 lint 不传 report type。周末报抽取必须显式指定 `--output output/weekend/<ID>/_intermediate/report_inputs.jsonl`。
