---
name: feishu-report-card
description: 把已生成好的游戏行业日报/周报/月报 markdown 发布成飞书卡片 + 飞书云文档(docx,每条信息附引用格式来源链接),并同步刷新 GitHub Pages 网页。当用户要求"推送/生成 飞书卡片""把日报推到飞书""按最新日报推送卡片""更新 docs 并推送""文档里加来源链接"时使用。覆盖完整发布链路、卡片生成技巧、docx 来源引用、以及发布前必须逐条核对的 Hard No 验收标准。
---

# Feishu Report Card 发布技能

把一份**已经写好且 lint 通过**的报告 markdown,发布成:① GitHub Pages 网页 ② 飞书云文档 docx ③ 飞书订阅卡片(带文档链接按钮)。

> 报告正文怎么写不在本技能范围内——那是 codex 的 `game-industry-report` 技能。本技能假定 markdown 已存在于 `output/daily|weekly|monthly/<date>/`。但发布前仍要确认它 lint 干净(见 Hard No #1)。

## Before You Respond — Hard No 验收标准

发卡前、回复用户前,逐条主动比对。任一条违反 → 回到对应步骤修正,**不要带病推送**(卡片发出去无法撤回)。

1. **markdown 必须 lint 干净再发卡**。卡片直接从 markdown 解析(`load_report_summary` → `_parse_markdown_sections` → `build_daily_card`),markdown 是唯一真相源。若刚改过正文,先重跑 `report_lint.py`(三参数 `--report --sources --inputs` 缺一不可),零 error 再继续。
2. **行业新闻每条正文 ≤ 200 个中文字符(CJK)**。这是 lint 硬限制,2026-06-22 翻车点(巴西 261/Epic 238/西山居 208 全超标,逐条裁剪才过)。裁剪时先砍引语、修饰词、英文括注,保留公司名/数字/日期等硬事实。
3. **发布顺序不能乱**:先 `build_report_html.py <md>` 生成 HTML → 再 `build_docs.py` 刷新网页 → 最后 `publish_feishu_daily.py --create-doc` 建 docx 发卡。卡片里的"查看完整日报"按钮指向 docx,网页与卡片必须基于同一份 markdown,否则用户看到的网页和卡片对不上。
4. **正式群发前必须先 `--dry-run`**,确认 `subscribers` 数量与将要执行的动作无误;再用 `--to-open-id` 给自己单测一次看渲染;最后才去掉两者正式群发。
5. **所有 python 命令带 `PYTHONUTF8=1`**(或用 Bash 工具)。Windows PowerShell 默认 GBK,中文会 UnicodeEncodeError。
6. **卡片不出现"…等共 N 条,详见完整日报"这类截断提示语**(用户明确不要)。已从 `build_daily_card` 删除。但删除截断提示带来副作用:若某节条目数 > `per_section`(默认 6),第 7 条会**静默丢失**且无任何提示。因此当某节(尤其行业新闻常有 7 条)超过 6 条时,**必须传 `--max-items <足够大的数,如 10>`** 让该节完整显示。发卡前先数一下最长的那节有几条。
7. **docx 权限必须设为 `tenant_readable`(组织内凭链接可读)**,否则订阅同事点按钮打不开。`--create-doc` 链路里 `set_doc_public_permission` 已处理,但若改动该链路要保留这一步。
8. **FeishuClient 永远走纯 urllib + tenant_access_token REST,禁止 import lark_oapi**。
9. **同一时间只能有一个 `feishu_subscribe_listener` 实例在跑**(订阅靠长连接捕获)。不要为了测试再起第二个。
10. **正文里的禁区词照样适用到卡片**(卡片是 markdown 的子集,不会引入新词,但若手工编辑卡片文案要遵守):不得提及 Moonton / 沐瞳 / Mobile Legends / 决胜巅峰;不得有业务建议性语言(对我司启发/建议动作/值得借鉴/启示);产品日历不得有流程语言(本地证据/多源记录/source ids/JSONL/pipeline)。
11. **docs 改动是本地的**。`build_docs.py` 只改本地 `docs/`,不会自动 commit/push 到 GitHub Pages。是否提交推送要**先问用户**,不要擅自 git push。
12. **飞书文档(docx)每条信息后必须带引用格式来源链接**。`--create-doc` 会先用 `build_docx_markdown(date)` 生成 `_intermediate/docx_import_<date>.md`(在每个 item 后插一行 `> 来源：[标题](url)` 引用块),再导入这份、**不是原报告 markdown**。来源取自 `sources_used.md`(`parse_sources` + `sources_for`,复用 `build_report_html`)。两条铁律:① **绝不把引用行写回原报告 markdown**——原 md 是 lint / 网页 / 卡片的唯一真相源,污染它会破坏 lint 和字数检查;② 来源标题里的 `[ ]` 方括号(NGA 标题常见 `[新瓜]`/`[英雄互娱]`)必须转全角 `【 】`,否则会破坏 markdown 链接文字解析。`docx_import_*.md` 是生成物,已加入 .gitignore,不提交。

13. **每个日期只保留一篇 docx**。`publish_feishu_daily.py` 不再每次推送都新建文档——`existing_doc_for_date(date)` 先查 `publish_logs/daily_<date>.json` 的 `doc_token`/`doc_url`,**有则复用同一篇**(dry-run 会打印 `would REUSE existing docx`,正式跑打印 `[doc] reusing existing docx`)。用户要求:同一天内容要改就**在原文档里手改**(飞书有编辑历史),不要堆一堆新文档。只有 `--new-doc` 才强制新建。注意复用意味着文档内容停留在首次创建那一版,后续改报告正文不会自动回灌进 docx——这是有意为之(用户手动维护)。验收:同一天重复推送后,飞书云空间该日期下**只有一篇** docx,链接不变。

> 注:用户已明确**不要改 `docs/` 网页里的来源展示**(网页保留原有"查看来源"抽屉)。来源引用只加在**飞书文档(docx)**里。2026-06-24 我曾误改 `report_template.html` 的网页渲染,被纠正——不要重犯。

## 完整发布链路(命令)

设 `DATE=2026-06-22`、报告类型为日报。所有命令在仓库根目录 `C:\Users\Admin\Documents\AI游戏行业周月报` 下运行,前面带 `PYTHONUTF8=1`(PowerShell 用 `$env:PYTHONUTF8='1';`,Bash 用前缀)。

```bash
# 0. (若刚改过正文) 重跑 lint,零 error 再继续
python scripts/report_lint.py \
  --report output/daily/$DATE/game_industry_daily_$DATE.md \
  --sources output/daily/$DATE/sources_used.md \
  --inputs <采集输入目录>

# 1. markdown → HTML(写在 md 旁边)
python scripts/build_report_html.py output/daily/$DATE/game_industry_daily_$DATE.md

# 2. 刷新 GitHub Pages 网页(读 HTML,生成 docs/daily/<date>/ + docs/index.html)
python scripts/build_docs.py

# 3. 预演:看订阅者数量与动作,不发不建
python scripts/publish_feishu_daily.py --date $DATE --create-doc --dry-run

# 4. 单测:只发给自己,建 docx + 发卡;行业新闻 7 条所以 max-items 给 10
python scripts/publish_feishu_daily.py --date $DATE --create-doc \
  --to-open-id ou_3bed51022efdc8499c9e23d74ab32445 --max-items 10

# 5. 正式群发(确认单测渲染 OK 后):去掉 --to-open-id
python scripts/publish_feishu_daily.py --date $DATE --create-doc --max-items 10
```

周报/月报:把路径与 `--date` 换成对应文件名约定(`game_industry_weekly_<start>_to_<end>.md` / `game_industry_monthly_YYYY-MM.md`),其余链路一致。

发完核对 `data/feishu/publish_logs/daily_$DATE.json`:应记录 docx url、doc_token、每个订阅者的发送结果。

## 卡片生成技巧(都在 `scripts/feishu_common.py` 的 `build_daily_card`)

- **卡片从 markdown 解析,不另写数据源**。改卡片内容 = 改 markdown 后重发,不要在卡片里手填文案。
- **每节取每条的一句话**:`_item_one_liner` → `### N.` 标题取标题本身;`- ` bullet 用 `_first_clause` 截到第一个 `；` 前的主句。所以 markdown 里 bullet 的主信息要放在第一个分号前。
- **重点短句加粗 `_emphasize`**:每条卡片行自动加粗一个可扫读的关键短语,方便快速 get 重点,**只插入 `**` 标记、不删任何字符**(2026-06-24 我曾按全角冒号裁短某行,被用户纠正:"我只需要加粗高亮,不需要删改"——`_emphasize` 只能插 `**`,不许动原文)。优先加粗行内**第一个《产品名》**(整体加粗,绝不在 `《X:Y》` 里截断);无《》则加粗**首个中文逗号前的主语短句**(长度 4–26 字);再不行就整行加粗(≤26 字);过长且无可锚定短语则原样返回。改动在 `feishu_common._emphasize`,验收:发卡前肉眼扫一遍,确认①每行有且仅有一处合理加粗、《》没被拆断;②对比原 markdown,卡片每行文字**一字不少**(只多了 `**`)。
- **节的映射与取舍**在 `_section_meta`:industry📰 / ai🤖 / release🎮 / discourse💬 / deep🧠;含"深度/精选"关键词的节 `drop=True`,**卡片里整节略去**(只在网页/docx 出现)。(Steam 榜单板块已下线,`rankings` 节不再产生。)
- **文档按钮**:传入 `doc_url` 时卡片底部加一个 primary 按钮"📄 查看完整日报",指向 docx。
- **`per_section` / `--max-items`** 控制每节最多显示几条;见 Hard No #6,务必大于最长节的条目数。

## 飞书文档(docx)来源引用(`build_docx_markdown`)

- **触发**:`publish_feishu_daily.py --create-doc` → `create_daily_doc` 调 `build_docx_markdown(date)` 生成带引用的 markdown,导入这份生成 docx。**原报告 markdown 不动**。
- **插入逻辑**(`feishu_common.build_docx_markdown`,按节走行):
  - 行业新闻 / AI / 玩家舆论 / 深度:每个 `### N. 标题` item 结束处插 `> 来源：[标题](url)`,标题→来源用 `sources_for(标题)` 查。
  - 产品日历:每条 `- ` bullet 后插来源;key 用 `产品日历 - <《》游戏名>`,回退到游戏名。
- **来源标签**:取 `sources_used.md` 的标题(`id_meta` 的 name),多源用「·」连接;无 url 的退化成纯文本。`[ ]`→`【 】` 防链接解析错乱(`_citation_md`)。
- **验收(发文档后逐条看)**:① docx 里每条信息下方都有「来源」引用块且链接可点;② 引用块没有把 `[新瓜]` 这类括号显示成断裂链接;③ 原 `game_industry_daily_<date>.md` 的 `git diff` 为空(没被污染);④ `_intermediate/docx_import_<date>.md` 未被 git 跟踪。

## 常见问题速查

- 卡片某节整段不见了 → 该节被 `_section_meta` 判为 drop(深度/精选),或节内条目标题不是 `### N.`(被 `_parse_markdown_sections` 漏掉)。
- 卡片少了最后一两条 → `per_section`/`--max-items` 太小,静默截断(Hard No #6)。
- 按钮打开报无权限 → docx 没设 `tenant_readable`(Hard No #7)。
- 中文乱码/UnicodeEncodeError → 没设 `PYTHONUTF8=1`(Hard No #5)。
- 网页和卡片内容对不上 → 漏了 `build_report_html.py` 或 `build_docs.py`,或两者基于不同 markdown(Hard No #3)。
- docx 里某条没有来源引用 → 该 item 标题在 `sources_used.md` 的 Item Source Map 里查不到(标题对不上,或 release 没用 `产品日历 - 名称` key)。
- docx 引用链接断裂/显示成纯文本 → 标题里有未转全角的 `[ ]`,或 `sources_used.md` 的 Source Details 缺 URL(Hard No #12)。
