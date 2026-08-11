from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "pdf" / "AI游戏行业报告工作流全景说明.pdf"

pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\msyh.ttc", subfontIndex=0))
pdfmetrics.registerFont(TTFont("CN-B", r"C:\Windows\Fonts\msyhbd.ttc", subfontIndex=0))

NAVY = colors.HexColor("#17233D")
BLUE = colors.HexColor("#3975D7")
CYAN = colors.HexColor("#18A999")
ORANGE = colors.HexColor("#F29E4C")
INK = colors.HexColor("#26344E")
MUTED = colors.HexColor("#68758C")
PALE = colors.HexColor("#F4F7FB")
LINE = colors.HexColor("#D8E3F1")
WHITE = colors.white

S = getSampleStyleSheet()
S.add(ParagraphStyle(name="Cover", fontName="CN-B", fontSize=28, leading=39, textColor=WHITE, spaceAfter=12))
S.add(ParagraphStyle(name="CoverSub", fontName="CN", fontSize=11.5, leading=19, textColor=colors.HexColor("#D9E5FA")))
S.add(ParagraphStyle(name="H1", fontName="CN-B", fontSize=20, leading=27, textColor=NAVY, spaceBefore=2, spaceAfter=8))
S.add(ParagraphStyle(name="H2", fontName="CN-B", fontSize=12.5, leading=19, textColor=BLUE, spaceBefore=8, spaceAfter=4))
S.add(ParagraphStyle(name="Body", fontName="CN", fontSize=8.9, leading=14.7, textColor=INK, spaceAfter=4))
S.add(ParagraphStyle(name="Small", fontName="CN", fontSize=7.5, leading=11.8, textColor=INK))
S.add(ParagraphStyle(name="Tiny", fontName="CN", fontSize=6.7, leading=10, textColor=INK))
S.add(ParagraphStyle(name="TH", fontName="CN-B", fontSize=7.5, leading=11, textColor=WHITE))
S.add(ParagraphStyle(name="Callout", fontName="CN-B", fontSize=9.3, leading=15.5, textColor=NAVY,
                     backColor=colors.HexColor("#EDF3FC"), borderColor=LINE, borderWidth=.6,
                     borderPadding=7, spaceBefore=4, spaceAfter=7))
S.add(ParagraphStyle(name="Flow", fontName="CN-B", fontSize=8, leading=11, textColor=WHITE, alignment=TA_CENTER))
S.add(ParagraphStyle(name="Metric", fontName="CN-B", fontSize=18, leading=22, textColor=WHITE, alignment=TA_CENTER))
S.add(ParagraphStyle(name="MetricSub", fontName="CN", fontSize=7.5, leading=11, textColor=WHITE, alignment=TA_CENTER))


def P(text, style="Body"):
    return Paragraph(text, S[style])


def bullets(items):
    return [P("• " + item) for item in items]


def table(rows, widths, header=True, small=False):
    data = []
    for r, row in enumerate(rows):
        data.append([P(str(v), "TH" if header and r == 0 else ("Tiny" if small else "Small")) for v in row])
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    st = [
        ("VALIGN",(0,0),(-1,-1),"TOP"), ("GRID",(0,0),(-1,-1),.4,LINE),
        ("LEFTPADDING",(0,0),(-1,-1),4), ("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),3.5), ("BOTTOMPADDING",(0,0),(-1,-1),3.5),
    ]
    if header:
        st += [("BACKGROUND",(0,0),(-1,0),NAVY)]
    for r in range(1 if header else 0, len(rows)):
        if r % 2 == 0:
            st += [("BACKGROUND",(0,r),(-1,r),PALE)]
    t.setStyle(TableStyle(st))
    return t


def flow(labels):
    cells = []
    widths = []
    for i, label in enumerate(labels):
        cells.append(P(label, "Flow")); widths.append(25*mm)
        if i < len(labels)-1:
            cells.append(P("→", "Flow")); widths.append(5*mm)
    t = Table([cells], colWidths=widths, rowHeights=15*mm, hAlign="CENTER")
    cmds = [("VALIGN",(0,0),(-1,-1),"MIDDLE")]
    for i in range(len(cells)):
        cmds.append(("BACKGROUND",(i,0),(i,0), BLUE if i % 4 == 2 else (CYAN if i % 2 else NAVY)))
    t.setStyle(TableStyle(cmds))
    return t


def metrics(items):
    data = []
    for value, label, color in items:
        cell = Table([[P(value,"Metric")],[P(label,"MetricSub")]], colWidths=[38*mm], rowHeights=[12*mm,10*mm])
        cell.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),color),("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
        data.append(cell)
    t = Table([data], colWidths=[42*mm]*len(data), hAlign="CENTER")
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
    return t


def hf(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(LINE); canvas.line(18*mm,282*mm,192*mm,282*mm)
        canvas.setFont("CN",7); canvas.setFillColor(MUTED)
        canvas.drawString(18*mm,287*mm,"AI 游戏行业报告工作流全景说明 · 分享型白皮书")
        canvas.drawString(18*mm,11*mm,"基于当前工作区脚本、配置与规则 · 2026-07-28")
        canvas.drawRightString(192*mm,11*mm,str(doc.page))
    canvas.restoreState()


story = []

# Cover
cover = Table([
    [P("从 47 个信息源到一份<br/>可审计的游戏行业报告","Cover")],
    [P("一套 AI 信息采集、判断、发布与反馈工作流的搭建实践","CoverSub")],
    [Spacer(1,48*mm)],
    [P("适合内部复盘 · 外部方法分享 · 工作流设计参考<br/>版本：2026-07-28","CoverSub")],
], colWidths=[174*mm], rowHeights=[None,None,50*mm,None])
cover.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),NAVY), ("LEFTPADDING",(0,0),(-1,-1),17*mm),
    ("RIGHTPADDING",(0,0),(-1,-1),17*mm), ("TOPPADDING",(0,0),(-1,0),30*mm),
    ("BOTTOMPADDING",(0,-1),(-1,-1),23*mm),
]))
story += [Spacer(1,9*mm),cover,PageBreak()]

# 1 WHY + design + summary
story += [
    P("1. 为什么要做这套工具？","H1"),
    P("真正困难的不是“找到新闻”，而是把大量、重复、质量不一的信息，稳定地变成团队可以直接使用、可以解释、可以追溯的判断材料。","Callout"),
    table([
        ["原始问题","具体表现","对应设计"],
        ["信息分散","国内外媒体、Newsletter、产品日历和社区讨论分布在几十个入口。","建立多板块采集器注册表和统一调度。"],
        ["噪声与重复","热门不等于重要；同一事件被多家重复报道，同一主体也可能同时发生多个事件。","先聚类成独立事件，再评分与跨板块去重。"],
        ["AI 事实漂移","模型容易把标题、记忆、推断和来源事实混在一起。","正文事实逐条绑定 source text 原文证据。"],
        ["多端内容分叉","报告、网页与飞书分别制作，造成重复劳动和内容不一致。","Markdown 作为唯一内容真源，确定性生成各渠道。"],
    ],[30*mm,69*mm,71*mm]),
    P("四个设计目标","H2"),
    table([
        ["全","准","稳","可追溯"],
        ["覆盖足够多的行业信号，不因来源或语言提前漏掉候选。","先识别事件，再按业务价值筛选，而非直接按热度排序。","固定窗口、结构和失败策略；局部异常可降级但不能静默。","关键事实、决策与正式条目均可回到本地原文和真实链接。"],
    ],[42.5*mm]*4),
    Spacer(1,5*mm),
    metrics([("47","生产信息源",BLUE),("5","内容信息池",CYAN),("4","报告类型",ORANGE),("1","证据链",NAVY)]),
    PageBreak(),
]

# 2 BUILD and architecture
story += [
    P("2. 这个工具是怎么一步步做出来的","H1"),
    P("建设顺序很重要：先保证“信息能稳定拿到”，再把编辑判断写成规则，最后才把生成、发布和反馈接成闭环。","Callout"),
    flow(["选源与采集","统一结构","事件系统","规则筛选","证据校验","多端发布"]),
    Spacer(1,5*mm),
    table([
        ["阶段","要解决的问题","关键做法","形成的能力"],
        ["1. 选源与采集","信息从哪里来，能否拿到可用正文？","优先 API、RSS、站点地图与静态 HTML；浏览器抓取仅用于必要来源。","覆盖国内外行业、AI、新游、社区和深度分析。"],
        ["2. 统一数据结构","不同网站字段、时间和正文质量不一致。","所有采集器写入同一 JSONL 契约；正文不足显式标 partial。","后续抽取、索引、审计可共用。"],
        ["3. 事件系统","文章数量不等于独立事件数量。","按主体/产品、事件日期和事件本身严格聚类。","把文章列表升级为事件候选池。"],
        ["4. 规则体系","“重要”不能只靠模型感觉。","把行业评分、AI 边界、日历多源门槛、社区四要素写成契约。","筛选可解释、可复核、可持续迭代。"],
        ["5. 证据与校验","如何阻止模型补事实和规则漂移？","claim → source_id → evidence；两套校验共同阻断错误终稿。","每句话都能沿证据链回去。"],
        ["6. 发布与反馈","同一内容如何适配不同阅读场景？","Markdown 单一真源；生成网页、飞书 docx、摘要卡，并记录反馈。","一次成稿、多端复用、闭环运营。"],
    ],[20*mm,42*mm,67*mm,41*mm]),
    P("整体 Workflow","H2"),
    flow(["定时采集","结构化落盘","报告抽取","候选与评分","审计与校验"]),
    Spacer(1,3*mm),
    flow(["Markdown终稿","互动网页","站点归档","飞书文档/卡","反馈回流"]),
    PageBreak(),
]

# 3 Sources and collection
story += [
    P("3. 信息采集：47 个生产源如何分工","H1"),
    P("注册表共有 48 个采集器；Steam 排名采集器仍保留在代码中，但 PC 排名板块已退出生产报告，因此实际启用 47 个源。","Callout"),
    table([
        ["信息池","数量","主要任务","来源"],
        ["行业新闻","28","市场、公司、产品、平台、资本与组织变化。","gcores、gamelook、cgames、youxiputao_sohu、youxituoluo、youxichaguan、yystv、youxixinzhi_qqnews、gamesindustry、pocketgamer、gamedeveloper、mobilegamer、investgame、vgc、dataeye_36kr、chuapp、gameres、gamespot、ign_cn、indienova、luosiji_sohu、pcgamer、polygon、qimai_sohu、yxrb、roblox_newsroom、nadianshi、cubox"],
        ["AI 趋势","3","直接作用于游戏的 AI，以及具有明确游戏迁移价值的能力变化。","aihot、baoyu、unrealengine"],
        ["深度分析","9","Newsletter、长文、市场与战略分析。","gamediscover、naavik_digest、thegamebusiness、deconstructor_deconstructions、gameoracle、matthewball、necromanov、questmobile、sensortower"],
        ["产品日历","5","上线、测试、首曝、定档与重大产品节点。","ceshibiao_17173、wanjiang_16p_newgame、haoyou_kuaibao_3839、taptap_app_calendar、gematsu_release_dates"],
        ["社区舆论","2","玩家争议、社区事件与论坛讨论。","nga_mobile_gossip、reddit_gaming_rising"],
    ],[23*mm,12*mm,49*mm,86*mm],small=True),
    P("采集运行规则","H2"),
]
story += bullets([
    "每天 08:00 默认采集前一自然日，窗口采用左闭右开：since ≤ published_at < until。",
    "生产任务当前使用 workers=1 串行执行，以减少共享目录与浏览器资源冲突；运行器本身支持线程池并行。",
    "采集阶段不生成 AI 摘要，只保存来源事实。标准字段包括标题、URL、来源、发布时间、正文、抓取状态、fallback 与 extra。",
    "只有来源摘要时必须标 fetch_status=partial、fallback=source_excerpt；不能把摘要伪装成全文。",
    "同分区同日期按 URL/标题去重，新 JSONL 优先于历史 PDF；无法证明完整性时应显式失败。",
])
story += [
    P("落盘与运行审计","H2"),
    table([
        ["产物","用途"],
        ["news_data/<section>/<date>/articles.jsonl","机器可读真源，一行一条内容。"],
        ["articles_index.md","标题、来源、发布时间、状态、正文长度和链接的人类 QA 索引。"],
        ["_collector_runs/<date>/run_summary.md/json","全局运行状态、来源健康度、窗口内条数与标题。"],
        ["单采集器 manifest","记录发现、抓取与失败详情。"],
    ],[68*mm,102*mm]),
    PageBreak(),
]

# 4 report workflow and report types
story += [
    P("4. 报告生成：从全量输入到可发布终稿","H1"),
    P("报告不是从搜索结果直接生成。每期必须先形成完整输入和审计产物，再写正文；整个窗口无数据则停止，不联网补造。","Callout"),
    table([
        ["步骤","动作","硬边界"],
        ["1","锁定报告类型、时间窗口、输出目录与固定文件名。","避免窗口和产物命名漂移。"],
        ["2","抽取全量 report_inputs.jsonl，同时生成 summary、index、日历审计和来源质量审计。","抽取失败、空正文或计数不一致先修复。"],
        ["3","行业新闻独立事件聚类，并反扫全部候选，把符合条件的 AI 事件转区。","同一事件不能在行业与 AI 重复。"],
        ["4","先写 event_candidates 与 selection_decisions，再写结构化 report_items / decisions JSON。","先决策后正文，不能倒推理由。"],
        ["5","运行确定性产品日历排序与选择。","不能跳过更高优先级候选。"],
        ["6","逐条读取 source.text 后写 Markdown。","公司、产品、数字、日期和状态均需原文支持。"],
        ["7","脚本自动生成 sources_used.md。","禁止手写来源映射。"],
        ["8","运行 report_lint 与 artifact validate。","任一 error 均阻断发布。"],
    ],[12*mm,91*mm,67*mm],small=True),
    P("四类报告与数量边界","H2"),
    table([
        ["类型","窗口","行业阈值","AI","产品日历","社区","深度"],
        ["日报","自然日","≥7","1–2","≤4","1–2","默认1–2"],
        ["周末报","指定区间","≥7","1–2","≤4","1–2","默认1–2"],
        ["周报","指定区间","≥8","2–3","≤7","2–3","只消费人工选择"],
        ["月报","自然月","≥7","4–6","≤12","3–5","1–2"],
    ],[22*mm,31*mm,24*mm,20*mm,24*mm,20*mm,29*mm]),
    P("行业新闻采用绝对阈值，产品日历采用上限；其余数量为软目标。没有合格内容可以少写，禁止为了凑数降低标准。","Small"),
    PageBreak(),
]

# 5 core rules with proper table (fix screenshot)
story += [
    P("5. 核心规则：系统如何做判断","H1"),
    P("规则的作用不是替代编辑，而是把编辑判断变成团队可以讨论、系统可以校验的共同语言。","Callout"),
    P("5.1 行业新闻：E × R + M","H2"),
    table([
        ["维度","分值","定义与判断重点"],
        ["E · 事件重要性","0–3","新品正式上线/测试/首曝、并购融资、核心管理层变化、重大合作、平台政策、市场结构、停运或项目取消等事件类型。E=0 直接排除。"],
        ["R · 业务相关性","0–3","国内厂商和中国移动市场、Roblox、Garena / Savvy 体系、PVP 竞技、策略/卡牌/RPG、生活模拟等优先赛道，以及对移动或全球竞争格局的明确迁移点；Roblox 固定按最高关注主体取 R=3。"],
        ["M · 新鲜度钩子","0–2","强单日/单周钩子且多源覆盖为 2；有明确新鲜度为 1；无钩子或炒冷饭为 0。"],
        ["总分","E × R + M","日报、周末报、月报总分 ≥7；周报 ≥8。正文按总分降序，不设硬性条数上限。"],
    ],[40*mm,23*mm,107*mm]),
    P("5.2 其他四个板块","H2"),
    table([
        ["板块","最重要的采用规则","防止什么问题"],
        ["AI 新闻","必须是已直接作用于游戏研发/产品/发行/运营，或能说明“能力变化 → 游戏环节 → 效率、成本、体验或竞争条件”的迁移链。","防止只因带有 AI 标签就收录泛科技新闻。"],
        ["产品日历","从行业新闻和日历池反扫；按“规范化产品名 + 事件日期”聚类；appearance_count ≥2 才能进入正文。","防止单一来源误报和人工跳选低优先级项目。"],
        ["玩家舆论","每条必须有触发与前情、玩家态度/争议逻辑、时间线、后续扫描四要素。","防止把单帖观点写成玩家共识，或把论坛摘要当事件报道。"],
        ["深度观察","采用“观察 / 分析”两层；R/I/E/C 各 0–3。周报正文只消费周四人工选择，并唯一指定一张深度卡。","让 AI 扩大候选处理能力，同时由人保留议程设置权。"],
    ],[25*mm,91*mm,54*mm]),
    P("六条不可破坏的底线","H2"),
]
story += bullets([
    "AI 不创造事实；读不到 source text 就不写。",
    "先判断独立事件，再总结文章；同一主体不代表同一事件。",
    "同一独立事件只能进入行业或 AI 之一。",
    "产品日历正式条目必须满足多源门槛。",
    "周报深度内容和唯一卡片由用户选择，不自动替换。",
    "评分和审计过程只存在于内部产物，不进入网页、飞书或正式正文。",
])
story += [PageBreak()]

# 6 Evidence and example
story += [
    P("6. 证据链：如何让每句话都能回到原文","H1"),
    flow(["原始正文","候选事件","入选决策","正文表述","原文证据","来源链接"]),
    Spacer(1,5*mm),
    P("最终交付的不只是一份 Markdown，而是一套可以复核的决策记录。每个正文 item 都包含 section、title、candidate_id、source_ids 和非空 claims；每个 claim 继续绑定 source_id 与逐字存在于原文中的 evidence。","Callout"),
    table([
        ["审计产物","回答的问题"],
        ["report_inputs.jsonl / summary / index","本期系统实际看到了哪些输入？覆盖是否完整？"],
        ["source_quality_audit.json","哪些来源拿到了全文，哪些只有摘要或存在抓取异常？"],
        ["event_candidates.md","全量输入被拆成了哪些独立事件？"],
        ["selection_decisions.md/json","每个候选为何 include、exclude 或 merge？评分和分区是什么？"],
        ["release_calendar_audit.json","产品事件如何召回、聚类、计数和排序？"],
        ["report_items.json","正式正文的每个事实由哪段原文支持？"],
        ["sources_used.md","读者如何从正式条目进入真实来源链接？"],
    ],[66*mm,104*mm]),
    P("端到端示例（结构示意）","H2"),
    table([
        ["阶段","示例动作"],
        ["采集","三家来源报道某厂商收购工作室，系统保存全文、URL 和发布时间。"],
        ["聚类","确认主体、事件日期与交易事件一致，合并为一个独立候选。"],
        ["评分","资本动作 E=3；对目标市场有明确迁移点 R=2；有新鲜度 M=1，总分 7。"],
        ["决策","达到日报阈值；selection_decisions 记录 include、分数与来源。"],
        ["写作","只写原文支持的交易主体、时间、范围与当前状态；不补交易金额或后续影响。"],
        ["取证","每个公司名、日期和事件状态绑定 source_id 与原文 evidence。"],
        ["发布","同一 Markdown 生成网页、飞书文档和摘要卡，保留来源入口。"],
    ],[26*mm,144*mm]),
    PageBreak(),
]

# 7 Deep handoff
story += [
    P("7. 人机协同：周报深度观察的双窗口交接","H1"),
    P("这是整套系统最明确的人工决策点：AI 负责整理和评分候选，用户决定哪些内容进入周报，以及其中哪一条成为独立飞书卡片。","Callout"),
    table([
        ["时间/窗口","系统动作","人工动作","校验门槛"],
        ["周四候选窗口：上周四至本周三","展示全部合格深度候选，包含 R/I/E/C、观察、分析、URL 和卡片预览。","从正文合格候选中选择进入周报的条目，并唯一指定一条“★卡片”。","selection 文件必须同时声明候选窗口和目标周报窗口。"],
        ["目标周报窗口：上周五至本周四","周五按目标周报 ID 精确消费 selection；补入窗口外但已选择的 deep-only 来源。","不需要再次选择；系统不得自行增删或换卡。","selection 标题、周报第五栏和 deep_card_choice.txt 必须完全闭环。"],
        ["发布阶段","正式周报生成主卡片，并为唯一指定项生成独立深度卡。","仅在异常时处理。","缺失 selection、错用旧窗口、来源 URL 不可用或指定标题不一致，均阻断发布。"],
    ],[33*mm,55*mm,43*mm,39*mm],small=True),
    P("为什么保留人工选择","H2"),
]
story += bullets([
    "深度观察不是单纯的信息排序，而是团队议程设置：本周想讨论什么，本身就是业务决策。",
    "R/I/E/C 可以扩大候选处理能力并暴露判断依据，但不能替代最终主题选择。",
    "唯一指定卡片避免系统按正文顺序自动挑选，也避免为了有卡片而降级。",
])
story += [
    P("日报与周末报的深度规则","H2"),
    P("日报和周末报默认选择 1–2 条；正文采用“观察 / 分析”两层。观察提出变化与核心问题，分析至少两段，展开变化、原有成立前提、前提如何松动以及下游影响。单篇高质量分析可以支撑一个主题，综合主题至少需要两个共同支持结论的原始来源。"),
    P("R/I/E/C 的含义","H2"),
    table([
        ["R 相关性","I 结构性洞察","E 证据强度","C 卡片吸引力"],
        ["国内、移动、优先赛道或明确迁移点。","是否形成“变化—机制—下游影响”的完整链条。","证据是否完整、可核验；综合主题是否有多源共同支撑。","问题是否清晰、可迁移、值得团队继续讨论。"],
    ],[42.5*mm]*4),
    PageBreak(),
]

# 8 Website and Feishu
story += [
    P("8. 一次成稿，多端发布","H1"),
    P("Markdown 是唯一内容真源。网页和飞书负责不同阅读场景，但不再让 AI 进行第二次改写，从而避免多渠道内容漂移。","Callout"),
    flow(["Markdown终稿","互动报告页","历史站点","飞书docx","飞书摘要卡"]),
    Spacer(1,5*mm),
    table([
        ["渠道","适用场景","生成与呈现规则"],
        ["互动报告页","检索、筛选、查看来源和高密度阅读。","确定性解析 Markdown 与 sources_used；提供五分区导航、搜索、密度切换、来源抽屉和最多 3 个派生标签。"],
        ["历史站点","跨期浏览与存档。","扫描 daily / weekend / weekly / monthly 输出并重建 docs/index.html；首页信息流只摄入日报条目，避免摘要报告重复灌入。"],
        ["飞书 docx","团队长文阅读与转发。","同日期默认复用文档；设置链接只读 anyone_readable；严禁 anyone_editable / tenant_editable。"],
        ["飞书主卡片","移动端快速扫描重点。","按板块压缩，每板块默认最多 10 项；玩家舆论日报/周末报最多 2 项、周报最多 3 项。"],
        ["周报深度卡","单独突出一条人工指定的结构性观察。","每周最多 1 张；必须有 doc URL、真实来源 URL 和 deep_card_choice 闭环。"],
    ],[27*mm,45*mm,98*mm]),
    P("飞书卡片的细化规则","H2"),
]
story += bullets([
    "行业新闻每项只占一个 bullet；仅 E×R+M 总分恰好 11 的条目加粗首个短句，评分本身不显示。",
    "AI 新闻与行业新闻保持相同信息密度，每项用“标题 + 一条事实补充”的单行 bullet，全部不加粗；产品日历前 2 项整条加粗，其余不加粗。",
    "玩家舆论保留“加粗标题 + 下一行摘要”的两层结构；日报/周末报最多 2 条，周报最多 3 条。",
    "来源折叠属于视觉优化，失败只告警，不阻断文档发布；权限失败则必须如实报告。",
])
story += [PageBreak()]

# 9 subscription operations
story += [
    P("9. 订阅、反馈、定时任务与容错","H1"),
    flow(["用户发指令","长连接收事件","本地订阅表","生成/复用docx","发送互动卡","反馈回流"]),
    Spacer(1,5*mm),
    table([
        ["环节","规则"],
        ["订阅","飞书长连接接收“订阅日报 / 退订日报”，无需公网回调；订阅状态保存在 data/feishu/。"],
        ["发送","可指定单一 open_id 测试，也可发送给对应报告类型的全部活跃订阅者；dry-run 只预览。"],
        ["文档复用","启用 create-doc 时导入飞书 docx；默认复用同日期已有文档，除非显式 new-doc。"],
        ["发布日志","记录发布时间、文档 URL/token、正文内容哈希、订阅人数和逐用户结果；群发成功后写已推送状态。"],
        ["反馈","主卡提供“很有帮助”和“我有建议”；建议最多 500 字。每天 11:00 将新增反馈同步到飞书 Wiki 表。"],
        ["补发与回放","新订阅者可即时补发当天报告；菜单回放最近一次真正发布成功的报告，而不是磁盘草稿。"],
    ],[35*mm,135*mm]),
    P("定时任务","H2"),
    table([
        ["时间","任务","关键行为"],
        ["每天 08:00","AIGameIndustry_DailyCollectors","采前一日五板块；生成索引；提交并推送 news_data。"],
        ["每天 11:00","FeishuReportFeedbackSync","将新增报告反馈追加到飞书 Wiki 反馈表。"],
        ["每周四","深度候选与人工选择","固定候选窗口，选择周报正文条目并唯一指定卡片。"],
        ["每周五","周报生成与发布","精确消费目标周报 ID selection，完成证据与卡片交接闭环。"],
    ],[28*mm,58*mm,84*mm]),
    P("容错原则","H2"),
]
story += bullets([
    "采集前若 news_data 有本地未提交修改，定时任务拒绝混写。",
    "git pull 最多重试 3 次；网络失败仍继续采集并保留本地提交，待下次同步。",
    "部分采集器失败时仍会构建索引和提交已有数据，并在提交信息中标记 partial。",
    "推送失败不丢弃本地提交；错误必须可见，禁止静默跳过。",
    "scheduled_run.log 当前持续追加且未自动轮转，是明确的运维债务。",
])
story += [PageBreak()]

# 10 Lessons, share takeaways, roadmap
story += [
    P("10. 搭建过程中的经验与下一步","H1"),
    P("很多问题不在模型，而在数据边界、规则表达和长期运维。下面这些经验比具体脚本更适合迁移到其他团队。","Callout"),
    table([
        ["经验","为什么重要","可复用做法"],
        ["“抓到了网页”不等于“拿到了可用正文”","摘要、导航文本或脚本残留会降低证据强度。","记录 fetch_status、fallback 和正文长度；partial 源显式降级。"],
        ["源越多，事件系统越重要","多源会放大重复、跨板块重叠和事件边界问题。","以独立事件为基本单位，严格记录 cluster_basis。"],
        ["规则必须成为机器可校验的契约","仅写在文档里的规则会随时间和不同执行者漂移。","把字段、阈值、文件、标题格式和映射关系写进验证器。"],
        ["人工介入点需要提前设计","全自动系统在需要业务判断时往往会暗中做默认选择。","明确周四选择、边界复核和异常处理入口。"],
        ["同一内容只保留一个真源","多端二次改写会导致事实和结构不一致。","Markdown 单一真源，网页与飞书做确定性变换。"],
        ["运维机制也是产品的一部分","权限、日志、订阅状态和失败恢复直接影响实际可用性。","逐用户日志、内容哈希、任务补跑、权限回读和反馈同步。"],
    ],[45*mm,62*mm,63*mm]),
    P("下一阶段优先级","H2"),
    table([
        ["优先级","方向","具体动作"],
        ["P0","统一编排","明确报告生成与飞书推送的触发关系，避免采集、成稿和发布各自独立。"],
        ["P1","可观测性","建立来源健康度、采集→候选→入选→发布漏斗、耗时和 partial 率仪表盘。"],
        ["P1","日志与告警","为 scheduled_run.log 增加轮转；对持续失败来源和发布失败建立告警。"],
        ["P2","覆盖均衡","行业源占 28/47；持续增强 AI 与社区信号，并用入选质量反向评估来源。"],
        ["P2","规则版本管理","让每份报告可回溯当时使用的规则版本、生成器版本与关键配置。"],
    ],[20*mm,38*mm,112*mm]),
    P("最后的结论","H2"),
    P("这套方法真正可以复制的，不是 47 个网站或某个模型，而是把 AI 放进业务流程的方式：<b>源广但不直接发布，规则严但保留人工入口，一次成稿多端复用，每个结论都能追到原文。</b>","Callout"),
    P("事实口径：本文件依据当前工作区 README、采集器注册表、报告技能规则、定时任务、网站构建脚本、飞书发布与反馈脚本整理；源数量以代码注册表为准，“启用”以生产定时脚本实际调用板块为准。","Small"),
]

OUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                        topMargin=18*mm, bottomMargin=18*mm,
                        title="从47个信息源到一份可审计的游戏行业报告", author="Codex")
doc.build(story, onFirstPage=hf, onLaterPages=hf)
print(OUT)
