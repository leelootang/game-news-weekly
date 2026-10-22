# 审计产物与校验

## 必需文件

每份新报告目录必须包含：

- 固定命名的最终 Markdown。
- `sources_used.md`。
- `_intermediate/report_inputs.jsonl`。
- `_intermediate/report_inputs_summary.md`。
- `_intermediate/report_inputs_index.md`。
- `_intermediate/release_calendar_audit.json`。
- `_intermediate/source_quality_audit.json`。
- `_intermediate/event_candidates.md`。
- `_intermediate/selection_decisions.md`。
- `_intermediate/report_items.json`。
- `_intermediate/selection_decisions.json`。

周报有人工 selection 时，报告目录必须另含 `deep_card_choice.txt`。selection 按目标周报 ID 命名；校验必须确认人工已选标题与第五栏完全一致，且 `deep_card_choice.txt` 等于唯一 `★卡片:` 标题。

目标周报结束日自 2026-09-24 起，selection 还必须有可追溯的飞书回执：`选择来源: 飞书周四备选 Bot`、32位 `飞书回执ID`、非空 `正文候选ID`、唯一 `指定卡片候选ID`，以及有融合需求时的 `卡片整合参考ID`。`deep_observation_handoff.py lint-selection` 必须核对 `data/feishu/deep_review/replies/<receipt_id>.json` 中目标周报 ID、正文 ID 与完整卡片 ID 顺序一致；正文标题数必须等于正文候选 ID 数。无回执时允许省略深度栏并继续周报，已有回执却无法闭环时必须报错，不能静默忽略。

抽取失败、正文为空、预期日期/section 目录缺失或 index 计数不一致时，先修复或明确失败，不能静默跳过。数据部分缺失时在结果摘要写明实际覆盖范围；整个窗口无数据则停止，不联网补造。

## event_candidates.md

每个独立事件一张卡，不得把多个无关事件打包。建议固定模板：

```markdown
## C001 - Event title
- section: industry_news / ai_trends / release_calendar / community_discourse / deep_analysis
- status: candidate
- source_ids: S0001, S0002
- entities: company / game / platform / market
- event_date: YYYY-MM-DD
- facts: 读过 source text 后提取的紧凑事实
- notes: 重复覆盖、不确定性、单独主张、跨 section 证据或待核验项
```

community 候选另含 `trigger`、`complaint_logic`、`timeline`、`follow_up_scan`；多源聚类写清依据。facts 不能只凭标题、常识或记忆填写。

## selection_decisions.md

必须覆盖全部候选并记录 `include`、`exclude` 或 `merge into Cxxx`、目标分区和短理由。行业分数、产品日历分数、深度分数及边界判断写在这里；排除项不进入 `sources_used.md`。

```markdown
| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| C001 | include | 行业新闻 | E3×R3+M1=10 |
| C002 | exclude | - | E=0，例行宣传 |
| C003 | merge into C001 | 行业新闻 | 同主体、同日期、同一事件的重复报道 |
```

## report_items.json

每个正文 item 写 `section`、`title`、`candidate_id`、`source_ids`、非空 `claims`。每个 claim 含 `claim`、`source_id`、`evidence`；evidence 必须逐字存在于对应 input `text`。

`claim` 必须实际出现在最终正文中。正文出现的公司、产品、数字、日期和事件状态均要有对应 claim/evidence；不能用模糊占位词规避取证。读取不到原文时补读或排除。

3839 时间轴来源若原摘要只有“今天、明天、明早、后天”等相对时间，绝对日期 claim 不得直接把该相对短语作为 evidence。必须引用采集记录中的 `Detail update evidence`（详情页明确日期优先）或 `Resolved event`（详情页无绝对日期时按 Asia/Shanghai 的 `Collected at` 解析）；解析链必须同时包含非空 `Date resolution`。

该证据门禁严格以 `source_key=haoyou_kuaibao_3839` 为前提；不得据此改变其他网站、新闻稿或推文来源的相对时间判断。

产品日历另写 `release`；社区另写 `community`；深度正文必须含“观察：”“分析：”且分析至少两段。深度 item 另写 `card_copy`：`source_label` 为来自真实 source 的“媒体/作者 + 内容类型”，不带冒号；`summary` 为单行完整结论；`insights` 为 3–6 个 `{title, detail}` 对象。卡片字段只能压缩正文已有结论和已取证事实。覆盖窗口结束日期自 2026-08-17 起强制校验；旧报告缺少该字段时继续按旧格式兼容。

## selection_decisions.json

每个候选写 `candidate_id`、`section`、`source_ids`、`entities`、`event`、`decision`、`reason`。merge 必须写 `merge_into`。

- 行业：`scores: {event, relevance, hook, total}`，total=E×R+M；启用卡片曝光门禁后，`history_check` 另含 `prior_card_exposed`（无历史匹配时为 `null`，有匹配时为布尔值）。允许的 `novelty` 为 `new_event`、`repeat_only`、`material_update`、`card_carryover`。
- 行业PC／主机发售候选另写 `pc_release_scope: {classification, basis, evidence: [{source_id, evidence}]}`，分类及R约束见 `industry-scoring.md`；普通海外单机纯发售不能凭RPG/模拟经营取得R3。覆盖日期2026-10-15起强制检查可识别候选；旧报告缺字段保持兼容，显式字段始终校验。
- AI：记录 `ai_tier`、`game_stage`、`industry_reverse_scan`；迁移价值类另须填写非空 `migration_path`。具体定义见 `references/ai-news.md`。
- 产品日历：记录抽取审计中的事件因子、独立来源数、来源强度、重点公司主体、公司加分和优先级总分；`total = event × source + company`，多源才可 include。
- 深度：`scores: {relevance, insight, evidence, card, total}`；周报低于 9 分的 include 必须 `card_designated: true`。
- 多源行业候选写严格 `cluster_basis`。产品日历 cluster_basis 按产品名+日期特例解释。

所有候选至少包含 `candidate_id`、`section`、`source_ids`、`entities`、`event`、`decision`、`reason`；merge 必须有 `merge_into`。同一 `candidate_id` 不能重复，正文 item 必须映射到一个 include 决策。

行业新闻与产品日历允许共享产品、事件和来源，但须分别有唯一candidate_id与各自include决策、claims和分区字段。不得用行业已入选作为日历exclude理由；日历sync不读取行业include/exclude来决定资格。日历内部聚类、独立来源数、时间窗口、排序前缀、上限和跨期检查不变；行业与AI或社区的互斥也不变。

日历sync在每条决策写 `industry_overlap_allowed: true`。覆盖日期2026-10-15起或显式带此字段的新决策，不允许以行业重合为exclude理由；缺字段的旧报告不追溯改变。

产品日历审计 schema 5 另写 `report_window`、`release_window`、`release_lookahead_days` 和节点级 `window_scope`。日报、周报、周末报的 `release_lookahead_days=1`，月报为 0；只有 `release_calendar` 可以使用 `next_day_lookahead`。次日节点的日期和事件必须由正常报告窗口内的来源正文直接支持，且仍须满足多源门槛、排序前缀和条数上限。若相同“规范化产品名 + 事件日期 + 事件”已通过次日窗口进入上一份已发布报告，本期产品日历 decision 必须 exclude 并说明跨报告重复；此前仅为候选或因上限排除时不视为已发布。

`card_carryover` 仅用于“历史完整报告已收录、但订阅卡片未展示”的行业事件：必须 `decision=include`、顶层 `card_carryover=true`、`history_check.history_match=true`、`history_check.novelty=card_carryover`、`history_check.prior_card_exposed=false`。每份报告最多一条；它仍须达到当前报告的 E×R+M 分数线。`repeat_only` 仍不得 include，`material_update` 仍必须有非空 `new_facts`。

`card_carryover` 是纯内部审计字段。最终 Markdown、网页、飞书卡片和飞书文档不得出现“【补位】”“上期卡片未展示”、`card_carryover` 或任何用于向读者区分该条目的标签；其发布标题、正文和视觉格式必须与普通行业新闻一致。lint、发布前契约校验和卡片渲染校验均须阻止这些内部标记泄漏到可见内容。

飞书正式群发日志必须记录 `audience_scope`、`card_exposure_schema_version`、`card_max_items_per_section`、`card_delivery_succeeded` 与按实际卡片选择生成的 `card_items`。只有面向订阅者且成功数过半的群发才计入 `card_exposed=true`；单人测试和补发不改变全局曝光状态。旧日志无 `card_items` 时，历史构建脚本按每分区前 10 条作兼容推断。

正文与卡片均须执行玩家舆论硬上限：日报/周末报最多 2 条，周报最多 3 条。正文硬校验从 2026-08-11 起按报告覆盖窗口的结束日期生效，旧报告保留原正文；卡片上限立即适用于全部新旧报告。校验按报告文件名识别类型并阻止超限；卡片的预演、正式群发、补发、菜单重发与反馈展开共用同一选择函数。

排除项只留在 `selection_decisions.md/json`，不写入 `sources_used.md`。

## sources_used.md 唯一格式契约

只允许由 `report_artifacts.py generate-sources` 生成。必须包含：

```markdown
## Item Source Map
- {正文标题} - S0001, S0002
- 产品日历 - {产品名} - S0003, S0004

## Source Details
- S0001 | {source字段} | {title字段} | {url字段}
```

禁止用 Markdown 表格替代短横线映射；source、title、URL 必须来自 input，不得手写猜测。

## 强制校验

所有新报告均运行：

1. `report_lint.py --report --sources --inputs`；日报/周报附相应 report type，周末报不传。
2. `report_artifacts.py validate ... --require-artifacts`。

任一 error 都必须修正。无法修正时任务失败，不留下会被发布任务误判为完成的新终稿。
