每个工作日 10:30，把今天应发的游戏行业报告正式推送为飞书卡片和飞书云文档 docx，发给所有订阅者。工作目录 C:\Users\Admin\Documents\AI游戏行业周月报。只负责飞书推送，不生成或修改报告、不生成网页、不动 git。所有 Python 命令设置 PYTHONUTF8=1。

第 0 步：日期与星期硬门禁（必须最先执行，禁止凭语言模型心算星期）
- 必须先通过系统 API 取得 China Standard Time（等同 Asia/Shanghai）当前时间，例如在 PowerShell 运行：$cnNow = [System.TimeZoneInfo]::ConvertTimeBySystemTimeZoneId([DateTimeOffset]::UtcNow, 'China Standard Time'); $cnNow.ToString('yyyy-MM-dd HH:mm:ss zzz'); $cnNow.DayOfWeek。
- 日期、DayOfWeek、报告 kind、ID 和预期终稿路径必须全部由上述系统时间以程序方式计算，不得凭记忆、语言推断或手算星期。
- 固定映射：Monday=weekend；Tuesday/Wednesday/Thursday=daily；Friday=weekly；Saturday/Sunday=立即结束。
- 在检查文件前，必须明确输出并复核：当前上海日期、DayOfWeek、kind、ID、预期终稿路径。
- 若系统返回的 DayOfWeek、kind、ID、目录类型或文件名任一不一致，立即停止并报告“日期硬门禁失败”，不得预演、创建 docx 或群发。

每次按 Asia/Shanghai 当前日期独立重算目标；周末误触发直接结束：
- 周二/三/四：日报，ID=昨天 YYYY-MM-DD，目录 output/daily/<ID>/。
- 周五：周报，ID=<今天-7天>_to_<今天-1天>，目录 output/weekly/<ID>/。
- 周一：周末报，ID=<今天-3天>_to_<今天-1天>，目录 output/weekend/<ID>/。
publish_feishu_daily.py 会按 ID 形态定位报告，但仍须确认正确 kind 的 game_industry_<kind>_<ID>.md 存在；不存在则停止并报告，不得硬推。

推送前硬门禁（2026-07-22 起）：确认同目录 sources_used.md 及 _intermediate/report_inputs.jsonl、report_items.json、selection_decisions.json、release_calendar_audit.json 全部存在；运行 python scripts/report_artifacts.py validate --report <终稿> --inputs <inputs> --items <items> --decisions <decisions> --release-audit <audit> --sources <sources> --require-artifacts。任何缺失或 error 都立即停止，不预演、不创建 docx、不群发。2026-07-21 及以前旧报告不回溯。

步骤：
1. 确认终稿并通过上述 artifact gate。若 selection_decisions.json 存在 card_carryover=true，必须至多1条，且由 artifact gate 验证通过。card_carryover 仅是内部审计字段；卡片和 docx 不得显示“补位”“上期卡片未展示”、card_carryover 或任何区别性标记，补位项的标题、正文与样式必须和普通新闻完全一致。
2. 预演：python scripts/publish_feishu_daily.py --date <ID> --create-doc --max-items 10 --dry-run，记录订阅者数量、卡片总条数和 card carryover；为0则结束说明无人订阅。
3. 无需人工二次确认，正式执行：python scripts/publish_feishu_daily.py --date <ID> --create-doc --max-items 10。
4. 核对 data/feishu/publish_logs/daily_<ID>.json：doc_url 已生成，每个订阅者 ok=true；audience_scope=subscribers、card_exposure_schema_version=1、card_max_items_per_section=10、card_delivery_succeeded=true、card_items 非空。若本期有 card_carryover=true，其 candidate_id 必须出现在 card_items 的 industry 项且 card_carryover=true；否则视为推送链路失败并报告。
5. 日报、周末报、周报的 docx 已获长期授权采用外部链接只读，无需再次询问或暂停。对新建或复用的 docx 自动设置并回读：外部访问开启（V2 为 external_access_entity=open；若接口返回 V1 字段则 external_access=true）、link_share_entity=anyone_readable。严禁 anyone_editable、tenant_editable 或其他编辑权限；若不满足则自动 PATCH 为外部访问开启 + anyone_readable 并再次回读。权限设置与回读是技术校验，不是人工授权门禁；接口异常时如实报告，不撤回或阻塞已经成功完成的群发。
6. 摘要报告类型、ID、artifact gate、docx 链接、订阅者人数、成功/失败数、卡片条数与 card_carryover 曝光、权限回读结果；失败者逐一列出 open_id 和错误。

docx 来源引用由 --create-doc 链路的 build_docx_markdown 处理；原报告 Markdown 不可改。日报、周末报、周报的所有飞书 docx 均必须保持“外部可访问、获得链接者只读”，不得收紧为 tenant_readable，也不得开放外部编辑。

评分版本与名单校验说明：
评分与主体统一规则（subject_genre_v2，覆盖旧评分描述）：
行业E保持原事件类型0–3；R为主体重要性0–3；M只在本条新闻命中竞技（射击、MOBA、自走棋策略、Clash of Clans-like策略竞技、体育竞技等）、休闲SLG、生活模拟、数值卡牌RPG时取1，其余0，多个标签不叠加。新鲜度、多源不再计入M，集团新闻不能借无关产品加分。行业日报/周末报/周报/月报统一E×R+M>=5，E0直接排除，满分10，不设硬性条数上限。
R3=统一名单重点游戏主体及其直接归属产品，或全球/中国/东南亚/中东北非移动游戏市场，或京东、阿里、腾讯等互联网头部主体的游戏业务；R2=重点主体投资/合研工作室、前制作人/主策/主美等核心人才创业主体，或其他区域移动游戏市场；R1=名单外有声量较大代表产品的国内外游戏主体/互联网游戏业务、PC/主机市场整体信息；其余或主体无法证实为R0。关系和代表产品声量必须取证。国内/手游/品类不自动取R3，重点主体的PC/主机项目按主体取分，背景提及重点公司不能把关联工作室抬为R3。
行业与产品日历共用的重点主体名单：国内：腾讯、网易、米哈游、莉莉丝、哔哩哔哩、三七互娱、巨人网络、鹰角网络、叠纸游戏、世纪华通/点点互动、库洛、西山居、心动网络、游族、完美世界、雷霆游戏、吉比特、搜狐畅游、盛趣游戏、FunPlus、祖龙、紫龙、恺英、友谊时光、创梦天地、电魂、灵犀互娱、字节朝夕光年。海外：Roblox、Supercell、Riot Games、Garena、Savvy Games Group、Scopely、Niantic。腾讯含天美/光子，哔哩哔哩游戏合并哔哩哔哩，Sea仅游戏业务、Savvy仅游戏与电竞主体。
名单真源为skill的references/focus-subjects.md、references/report-policy.json，工作区镜像config/game_report_policy.json。产品日历仍按事件×来源+公司加分，直属+3、投资+2，多源/日期/排序前缀/条数上限保持，不能套行业5分线。
新生成或重生成的selection_decisions.json根对象写scoring_version=subject_genre_v2，非E0行业候选写subject_assessment和genre_assessment及逐字来源取证，scores.relevance表示主体R、scores.hook表示品类M。sync_release_decisions.py必须保留根评分版本。产品日历审计写focus_company_policy_version=subject_genre_v2。覆盖窗口结束日2026-10-21起强制新版本；更早既有报告保留历史评分，新重生成则显式新版本。日期/来源/双周与卡片曝光去重仍独立执行。
本发布任务只消费并校验终稿及审计，不自行重评分或修改报告；新规则失败时停止并报告生成端修复。飞书行业卡片仅新版本满分10加粗首句，历史旧版本仍按满分11；不向读者展示分数或内部字段。
