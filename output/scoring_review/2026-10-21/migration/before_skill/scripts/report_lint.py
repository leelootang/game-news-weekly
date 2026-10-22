#!/usr/bin/env python3
"""Lint a generated game-industry report for workflow and formatting regressions."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path


ERROR_PATTERNS = [
    ("fixed summary label", re.compile(r"三句话摘要")),
    ("tag metadata", re.compile(r"相关标签")),
    ("importance metadata", re.compile(r"重要性\s*[:：]")),
    ("routine license approval", re.compile(r"(版号发放|喜提版号|网络游戏审批信息公布|过审[:：])")),
    ("moonton or mlbb mention", re.compile(r"(Moonton|沐瞳|Mobile Legends: Bang Bang|决胜巅峰)", re.IGNORECASE)),
    ("generic business advice", re.compile(r"(建议我司|对我司(的)?启发|对我们业务的启发|值得借鉴|可借鉴|建议动作|启示)")),
    (
        "internal card-carryover marker",
        re.compile(r"((?:【|\[)\s*(?:补位|上期卡片未展示)\s*(?:】|\])|上期卡片未展示|card_carryover)", re.IGNORECASE),
    ),
]

WARN_PATTERNS = [
    ("unsupported certainty marker", re.compile(r"(必然|一定会|显然会|毫无疑问会)")),
]

REQUIRED_SECTIONS = [
    "行业新闻",
    "AI 新闻",
    "新游发布",
    "玩家舆论",
    "行业精选",
]

REPORT_FILENAME_PATTERNS = {
    "daily": re.compile(r"^game_industry_daily_\d{4}-\d{2}-\d{2}\.md$"),
    "weekly": re.compile(r"^game_industry_weekly_\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2}\.md$"),
    "monthly": re.compile(r"^game_industry_monthly_\d{4}-\d{2}\.md$"),
}

FORBIDDEN_RELEASE_AGGREGATE_HEADINGS = re.compile(
    r"(国内.*(上线|测试|发布)|海外.*(上线|测试|发布|新品)|重点产品动态|多款产品|一览|MMORPG上线与测试)"
)

FORBIDDEN_RELEASE_PROCESS_LANGUAGE = re.compile(
    r"(本地证据|多源记录|source ids?|本地\s*calendar|JSONL|本地\s*JSONL|本地记录|"
    r"多渠道共同提到|多个日历源记录|多个来源显示|多个\s*calendar\s*source|pipeline)",
    re.IGNORECASE,
)

RELEASE_CONTEXT_ALLOWLIST = re.compile(
    r"(原班工作室|前作|代表作|所属IP|IP新作|系列新作|改编|续作|精神续作|团队|工作室)"
)

# 新游 bullet 的固定句式：分号前的首句须含「型态」与「事件」，卡片只截取这段首句。
RELEASE_FORM_KEYWORDS = re.compile(r"(手游|端游|主机游戏|主机|多平台|页游|网游|单机|PC\s*游戏)")
RELEASE_EVENT_KEYWORDS = re.compile(
    r"(上线|公测|内测|首测|删档测试|不删档|付费测试|测试|抢先体验|EA|发售|发布(?:PV|PV预告|预告片)?|"
    r"PV|首曝|预约|开测|定档|上市|开服|重启|复活|停运|延期|跳票)",
    re.IGNORECASE,
)

COMMUNITY_EMPTY_DISCLAIMER = re.compile(
    r"(最终规则仍需以官方正式说明为准|以官方(正式)?说明为准|影射判断本身仍属于玩家解读|目前可确认的是玩家对.*争议|只是玩家(梳理|解读|说法))"
)

COMMUNITY_GENERIC_HEADING = re.compile(
    r"^《[^》]+》(?:[^，,]{0,8})?(?:引发持续争论|引发争议|持续争议|规则争议|文案修改争议|社区热议|玩家热议)$"
)

COMMUNITY_SPECIFIC_TRIGGER = re.compile(
    r"(被爆|被曝|被指|被质疑|玩家质疑|玩家不满|采用|出现|含|改|删|锁|缩水|独立|保底|副产物|兑换|门槛|文案|模型|贴图|招募|公告|补丁|卡池|联动|下架|道歉|回应)"
)

COMMUNITY_SOURCE_FIRST_SENTENCE = re.compile(
    r"^(?:\d{1,2}月\d{1,2}日，?)?(?:NGA|Reddit|贴吧|论坛|玩家).*?(?:发帖|围绕|讨论)"
)

COMMUNITY_COMPLAINT_LOGIC = re.compile(
    r"(玩家不满的核心在于|争议集中在|玩家讨论集中在|被质疑为|玩家质疑|玩家认为|部分玩家认为)"
)
COMMUNITY_TIMELINE = re.compile(r"\d{1,2}\s*月\s*\d{1,2}\s*日")

# 财报不是日报的常规供给：仅当标题明确标示为异常/超预期事件时，才允许继续由
# 人工在 selection_decisions.md 中核查比较基准和 source_id 证据。
FINANCIAL_REPORT_TITLE = re.compile(
    r"(财报|业绩预告|净利润|扣非|归母|营业收入|预计.*(?:利润|亏损)|(?:利润|亏损).*同比)"
)
FINANCIAL_REPORT_EXCEPTION = re.compile(
    r"(超预期|异常波动|业绩预警|重大减值|流动性危机|暴增|暴跌|断崖)"
)

SECTION_ALIASES = {
    "industry": "一、行业新闻",
    "ai": "二、AI 新闻",
    "release": "三、新游发布",
    "discourse": "四、玩家舆论",
    "selected": "五、行业精选",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def count_input_records(path: Path | None) -> tuple[int, int, int, int]:
    if not path or not path.exists():
        return 0, 0, 0, 0
    total = failed = empty = non_full = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        total += 1
        rec = json.loads(line)
        if rec.get("fetch_status", rec.get("extract_status")) != "ok":
            failed += 1
        elif rec.get("body_status") == "empty" or rec.get("text_chars", 0) == 0:
            empty += 1
        elif rec.get("body_status") in {"short_official", "snippet"}:
            non_full += 1
    return total, failed, empty, non_full


def section_counts_from_jsonl(path: Path | None) -> dict[str, int]:
    """Per-section record counts from the inputs JSONL (ground truth)."""
    counts: dict[str, int] = {}
    if not path or not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        sec = rec.get("section")
        if sec:
            counts[sec] = counts.get(sec, 0) + 1
    return counts


def index_section_stats(path: Path | None) -> dict[str, tuple[int, int]]:
    """Parse report_inputs_index.md → {section: (header_count, listed_bullets)}.

    Header lines look like `## industry_news (580 records)`; bullets are the
    `- ` lines beneath a header until the next `## `.
    """
    stats: dict[str, tuple[int, int]] = {}
    if not path or not path.exists():
        return stats
    header_re = re.compile(r"^##\s+(\S+)\s+\((\d+)\s+records\)\s*$")
    current: str | None = None
    header_n = 0
    listed = 0
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = header_re.match(line)
        if m:
            if current is not None:
                stats[current] = (header_n, listed)
            current = m.group(1)
            header_n = int(m.group(2))
            listed = 0
        elif current is not None and line.lstrip().startswith("- "):
            listed += 1
    if current is not None:
        stats[current] = (header_n, listed)
    return stats


def load_contract_module(report_path: Path):
    """Load the workspace validator without hard-coding one workspace path."""
    for parent in (report_path.parent, *report_path.parents):
        candidate = parent / "scripts" / "report_artifacts.py"
        if candidate.exists():
            spec = importlib.util.spec_from_file_location("report_artifacts", candidate)
            if not spec or not spec.loader:
                return None
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            spec.loader.exec_module(module)
            return module
    return None


def section_text(report: str, section_marker: str) -> str:
    marker = f"## {section_marker}"
    start = report.find(marker)
    if start == -1:
        return ""
    next_start = report.find("\n## ", start + len(marker))
    return report[start:] if next_start == -1 else report[start:next_start]


def item_bodies(section: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^###\s+\d+\.\s+(.+)$", section, flags=re.MULTILINE))
    items: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(section)
        items.append((match.group(1).strip(), section[body_start:body_end].strip()))
    return items


def zh_len(text: str) -> int:
    compact = re.sub(r"\s+", "", text)
    return len(compact)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, help="Generated report markdown")
    parser.add_argument("--sources", help="sources_used.md path")
    parser.add_argument("--inputs", help="report_inputs.jsonl from extract_report_inputs.py")
    parser.add_argument("--items", help="structured report_items.json (defaults beside inputs)")
    parser.add_argument("--decisions", help="structured selection_decisions.json (defaults beside inputs)")
    parser.add_argument("--release-audit", help="structured release_calendar_audit.json (defaults beside inputs)")
    parser.add_argument("--require-artifacts", action="store_true", help="require the structured report audit artifacts")
    parser.add_argument("--report-type", choices=["daily", "weekly", "monthly"], help="Apply count expectations for this report type")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    report_path = Path(args.report)
    date_match = re.search(r"(20\d{2}-\d{2}-\d{2})", report_path.name)
    force_artifacts = args.require_artifacts or bool(date_match and date_match.group(1) >= "2026-07-22")
    report = read(report_path)
    sources_path = Path(args.sources) if args.sources else None
    sources = read(sources_path) if sources_path and sources_path.exists() else ""
    errors: list[str] = []
    warnings: list[str] = []

    if not args.sources:
        errors.append("--sources is required by the current report workflow")
    if not args.inputs:
        errors.append("--inputs is required by the current report workflow")

    if args.report_type:
        expected_name = REPORT_FILENAME_PATTERNS[args.report_type]
        if not expected_name.match(report_path.name):
            errors.append(f"report filename must match {args.report_type} convention; got {report_path.name}")

    for label, pattern in ERROR_PATTERNS:
        if pattern.search(report):
            errors.append(f"Report contains forbidden pattern: {label}")

    for label, pattern in WARN_PATTERNS:
        if pattern.search(report):
            warnings.append(f"Report contains risky pattern: {label}")

    # 周报的「行业精选 / 深度观察」改为人工筛选(周四定、周五消费):没筛选时
    # 整段省略是允许的,所以周报不把它当硬必填;日报/月报仍全五段必填。
    required_sections = [
        s
        for s in REQUIRED_SECTIONS
        if not (args.report_type == "weekly" and s == "行业精选")
    ]
    for section in required_sections:
        if section not in report:
            errors.append(f"Missing required section containing: {section}")

    headings = re.findall(r"^###\s+\d+\.\s+(.+)$", report, flags=re.MULTILINE)
    dupes = sorted({h for h in headings if headings.count(h) > 1})
    if dupes:
        warnings.append(f"Duplicate item headings: {', '.join(dupes)}")

    for title, _ in item_bodies(section_text(report, SECTION_ALIASES["industry"])):
        if FINANCIAL_REPORT_TITLE.search(title) and not FINANCIAL_REPORT_EXCEPTION.search(title):
            errors.append(
                "Routine financial-report item is forbidden in industry news: "
                f"{title}。仅允许标题明确为超预期/异常波动等例外，且须在 "
                "selection_decisions.md 记录财报异常证据、比较基准与 source_id。"
            )

    # --- HARD CHECK: news sections must use `### N. 标题` item headings -------
    # 行业新闻/AI/玩家舆论/行业精选 四节的每个条目必须是 `### N. 标题`。这是
    # report_lint 的 item_bodies() 和 build_report_html.py 的 parse_report()
    # 唯一识别条目的方式。历史回归（2026-06-10）：写报告时用了 `**加粗**` 段落
    # 当标题、没有任何 `### N.`，于是这四节全部解析为 0 条，HTML 网页整段消失、
    # lint 各项逐条检查全部空过。这里强制：section 标题在、且段内有实质正文，
    # 却解析不出任何 `### N.` 条目 → 直接报 error，让生成流程回头重写该节。
    NEWS_SECTION_KEYS = ("industry", "ai", "discourse", "selected")
    EMPTY_SECTION_DISCLAIMER = re.compile(r"本(日|周|月|期)?(暂)?无显著|本(日|周|月)无[^\n]{0,12}|无显著[^\n]{0,12}")
    BOLD_PSEUDO_HEADING = re.compile(r"(?m)^\s*\*\*[^*\n]+\*\*\s*$")
    for key in NEWS_SECTION_KEYS:
        sec = section_text(report, SECTION_ALIASES[key])
        if not sec:
            continue
        # strip the leading "## ..." header line to get the section body
        body = sec.split("\n", 1)[1] if "\n" in sec else ""
        items = item_bodies(sec)
        if items:
            continue
        if EMPTY_SECTION_DISCLAIMER.search(body):
            continue  # legitimately empty section, explicitly declared — allowed
        if zh_len(body) <= 10:
            continue  # essentially empty whitespace — not a format regression
        pseudo = BOLD_PSEUDO_HEADING.findall(sec)
        hint = (f"（发现 {len(pseudo)} 行 `**加粗**` 伪标题，应改为 `### N. 标题`）"
                if pseudo else "（未发现任何 `### N.` 条目标题）")
        errors.append(
            f"{SECTION_ALIASES[key]} 节有正文但解析出 0 个 `### N.` 条目 {hint}；"
            f"新闻类条目必须用 `### N. 标题`（h3+序号），否则 HTML 网页会整段丢失、"
            f"source map 校验会空过——请回头用 `### N.` 格式重写该节后再 lint")

    # --- SOFT CHECK: news sections below the expected floor -------------------
    # Section Targets 的下限不是硬配额（真没料可少写/留空），但若某节只有 1 条
    # 且远低于下限，提示回头确认是不是漏抽或格式问题。
    if args.report_type:
        # 行业新闻不设条数下限：日报/月报 ≥7，周报 ≥8，由 E×R+M 绝对阈值决定。
        floors = {
            "daily": {"ai": 1, "discourse": 1, "selected": 1},
            "weekly": {"ai": 2, "discourse": 2, "selected": 1},
            "monthly": {"ai": 4, "discourse": 3, "selected": 1},
        }.get(args.report_type, {})
        for key, low in floors.items():
            sec = section_text(report, SECTION_ALIASES[key])
            if not sec:
                continue
            body = sec.split("\n", 1)[1] if "\n" in sec else ""
            count = len(item_bodies(sec))
            if 0 < count < low and not EMPTY_SECTION_DISCLAIMER.search(body):
                warnings.append(
                    f"{args.report_type} {SECTION_ALIASES[key]} 节仅 {count} 条（下限 {low}）；"
                    f"确认是当窗口确无更多够分量事件，还是漏抽/格式问题")

    # --- HARD CHECK: source map 必须能被网页脚本(build_report_html.py)解析 -----
    # lint 其它地方用"子串匹配"校验来源覆盖（表格格式也能蒙混过关），但
    # build_report_html.py 的 parse_sources 只认短横线格式：
    #   Item Source Map:  `- 标题 - S0049, S0043`
    #   Source Details :  `## Source Details` + `- S0049 | 域名 | 标题 | URL`
    # 2026-06-10 回归：source map 写成 markdown 表格、且缺 Source Details 段，
    # parse_sources 解析为空 → 每个条目 sources=[] → 网页"查看来源"按钮无内容。
    # 这里用与网页脚本相同的口径校验，避免"lint 绿、网页空"。
    if sources:
        dash_titles = set()
        in_map = False
        for line in sources.splitlines():
            t = line.strip()
            if t.startswith("## "):
                in_map = ("Item Source Map" in t or "条目来源映射" in t)
                continue
            if in_map and t and not t.startswith("#"):
                mm = re.match(r"^(?:[-*]\s*|\d+\.\s*)?(?P<title>.+?)\s*(?:——|—|-)\s*S\d{3,4}\b", t)
                if mm:
                    dash_titles.add(mm.group("title").strip().strip("`"))
        # gather report item titles the webpage will look up
        report_titles = []
        for key in ("industry", "ai", "discourse", "selected"):
            report_titles += [tt for tt, _ in item_bodies(section_text(report, SECTION_ALIASES[key]))]
        rel = section_text(report, SECTION_ALIASES["release"])
        for bullet in re.findall(r"^-\s+(.+)$", rel, flags=re.MULTILINE):
            pm = re.search(r"《([^》]+)》", bullet)
            if pm:
                report_titles.append(f"产品日历 - {pm.group(1)}")
        if report_titles:
            unresolved = [t for t in report_titles if t not in dash_titles]
            if len(unresolved) > len(report_titles) // 2:
                errors.append(
                    f"Item Source Map 不是网页脚本可解析的短横线格式（`- 标题 - Sxxx`）或标题对不上："
                    f"{len(unresolved)}/{len(report_titles)} 个正文条目解析不到来源；"
                    f"网页“查看来源”将为空。请改用短横线列表（勿用 markdown 表格）。首个未解析：{unresolved[0][:40]}")
        if "Source Details" not in sources and "来源明细" not in sources:
            warnings.append(
                "sources 缺少 `## Source Details` 段（`- Sxxx | 域名 | 标题 | URL`）；"
                "没有它网页来源只显示 source id、没有可点链接")

    if sources:
        if "Item Source Map" not in sources and "条目来源映射" not in sources:
            errors.append("sources file has no item-level source map")
    elif args.sources:
        errors.append("sources file is missing or unreadable")

    total, failed, empty, non_full = count_input_records(Path(args.inputs) if args.inputs else None)
    if args.inputs:
        if total == 0:
            errors.append("input JSONL has zero records")
        if failed:
            errors.append(f"input extraction has {failed} failed records")
        if empty:
            warnings.append(f"input extraction has {empty} empty text records")
        if non_full:
            warnings.append(f"input extraction has {non_full} short/snippet records; they are forbidden as final-item evidence")
        intermediate_dir = Path(args.inputs).parent
        required_intermediates = [
            "report_inputs_summary.md",
            "report_inputs_index.md",
            "event_candidates.md",
            "selection_decisions.md",
        ]
        for name in required_intermediates:
            if not (intermediate_dir / name).exists():
                errors.append(f"required intermediate file is missing: {intermediate_dir / name}")

        # --- 召回守卫：report_inputs_index.md 必须完整、无截断 ---
        # 粒粒的小人国被漏召回的根因是 index 被每节截断到 50 条，S0740 在 JSONL 里却
        # 排在截断线外，生成阶段全局扫描时根本没看到。index 是生成阶段下钻前的总览，
        # 一旦截断即等于静默丢候选。这是纯机械的过程/完整性核查（不猜重要性、不用
        # 关键词启发式，遵循「lint 查过程不查启发式」），三方计数必须一致：
        # JSONL 真实分节计数 == index 表头计数 == index 实际列出行数。
        index_path = intermediate_dir / "report_inputs_index.md"
        if index_path.exists():
            jsonl_counts = section_counts_from_jsonl(Path(args.inputs))
            idx_stats = index_section_stats(index_path)
            for sec, real_n in jsonl_counts.items():
                if sec not in idx_stats:
                    errors.append(
                        f"report_inputs_index.md 缺 section『{sec}』（JSONL 有 {real_n} 条）："
                        "index 必须覆盖每个 section 的全部记录"
                    )
                    continue
                header_n, listed = idx_stats[sec]
                if header_n != real_n:
                    errors.append(
                        f"report_inputs_index.md『{sec}』表头计数 {header_n} 与 JSONL 真实计数 "
                        f"{real_n} 不一致：index 已过期或被截断"
                    )
                if listed != header_n:
                    errors.append(
                        f"report_inputs_index.md『{sec}』实际列出 {listed} 行 ≠ 表头计数 {header_n}："
                        "index 被截断，会导致候选被静默漏召回（正是粒粒的小人国被漏的根因）"
                    )

        # New reports are checked as a closed graph: final markdown ↔ structured
        # item claims ↔ candidate decisions ↔ release reverse-scan ↔ sources.
        # Legacy reports keep their old markdown companions and receive a warning
        # until they are intentionally migrated.
        contract = load_contract_module(report_path)
        if not contract:
            errors.append("workspace scripts/report_artifacts.py is missing; cannot run source/audit contract")
        else:
            items_path = Path(args.items) if args.items else intermediate_dir / "report_items.json"
            decisions_path = Path(args.decisions) if args.decisions else intermediate_dir / "selection_decisions.json"
            release_audit_path = Path(args.release_audit) if args.release_audit else intermediate_dir / "release_calendar_audit.json"
            contract_errors, contract_warnings = contract.validate_contract(
                report_path, Path(args.inputs), items_path, decisions_path, release_audit_path,
                sources_path, force_artifacts,
            )
            errors.extend(contract_errors)
            warnings.extend(contract_warnings)

    industry = section_text(report, SECTION_ALIASES["industry"])
    for title, body in item_bodies(industry):
        length = zh_len(body)
        if length > 200:
            errors.append(f"industry item exceeds 200 chars: {title} ({length})")

    # 行业新闻排序不再用关键词启发式检测（旧的「国产优先」窄口径 WARN 已废弃）：
    # 排序完全由四维打分终分决定（终分从高到低、同分国产在前），过程核查见文件末尾
    # selection_decisions.md 四维打分记录校验。

    release = section_text(report, SECTION_ALIASES["release"])
    release_headings = re.findall(r"^###\s+\d+\.\s+(.+)$", release, flags=re.MULTILINE)
    if release_headings:
        errors.append("release_calendar section must use product-level bullets, not ### item headings")
    if FORBIDDEN_RELEASE_AGGREGATE_HEADINGS.search(release):
        errors.append("release_calendar section contains aggregate/category wording; use one bullet per product")
    if FORBIDDEN_RELEASE_PROCESS_LANGUAGE.search(release):
        errors.append("release_calendar section contains internal evidence/process language")
    release_bullets = re.findall(r"^-\s+(.+)$", release, flags=re.MULTILINE)
    for bullet in release_bullets:
        product_mentions = re.findall(r"《[^》]+》", bullet)
        unique_mentions = list(dict.fromkeys(product_mentions))
        if len(unique_mentions) > 1 and not RELEASE_CONTEXT_ALLOWLIST.search(bullet):
            errors.append(f"release_calendar bullet mentions multiple products: {bullet[:80]}")
        lead = re.split(r"[；;]", bullet, maxsplit=1)[0]
        if not re.search(r"《[^》]+》", lead):
            errors.append(f"release_calendar bullet missing 《游戏名》 before '；': {bullet[:80]}")
        if not RELEASE_FORM_KEYWORDS.search(lead):
            errors.append(f"release_calendar bullet lead clause missing 型态(手游/端游/主机游戏/多平台): {bullet[:80]}")
        if not RELEASE_EVENT_KEYWORDS.search(lead):
            errors.append(f"release_calendar bullet lead clause missing 事件(上线/公测/测试/抢先体验/发布PV...): {bullet[:80]}")

    if sources:
        mapped_items: list[str] = []
        for key in ("industry", "ai", "discourse", "selected"):
            for title, _body in item_bodies(section_text(report, SECTION_ALIASES[key])):
                mapped_items.append(title)
        for bullet in release_bullets:
            product_match = re.search(r"《([^》]+)》", bullet)
            mapped_items.append(f"产品日历 - {product_match.group(1)}" if product_match else bullet[:40])
        for item in mapped_items:
            if item not in sources:
                errors.append(f"report item is missing from sources map: {item}")

    discourse = section_text(report, SECTION_ALIASES["discourse"])
    discourse_count = len(item_bodies(discourse))
    report_name = report_path.name
    discourse_cap = (
        3
        if report_name.startswith("game_industry_weekly_")
        else 2
        if report_name.startswith(("game_industry_daily_", "game_industry_weekend_"))
        else None
    )
    report_dates = re.findall(r"\d{4}-\d{2}-\d{2}", report_name)
    discourse_cap_is_enforced = bool(report_dates and max(report_dates) >= "2026-08-11")
    if discourse_cap is not None and discourse_cap_is_enforced and discourse_count > discourse_cap:
        errors.append(
            f"community discourse exceeds report cap {discourse_cap}: {discourse_count}"
        )
    for title, body in item_bodies(discourse):
        if COMMUNITY_GENERIC_HEADING.search(title) and not COMMUNITY_SPECIFIC_TRIGGER.search(title):
            warnings.append(f"community item heading is vague; name the trigger and dispute: {title}")
        if COMMUNITY_EMPTY_DISCLAIMER.search(body):
            errors.append(f"community item contains empty disclaimer language: {title}")
        first_sentence = re.split(r"[。！？\n]", body.strip(), maxsplit=1)[0].strip()
        if COMMUNITY_SOURCE_FIRST_SENTENCE.search(first_sentence):
            warnings.append(f"community item starts from source/post, not event trigger: {title}")
        if not COMMUNITY_COMPLAINT_LOGIC.search(body):
            errors.append(
                f"community item lacks complaint/controversy logic: {title}；"
                "须明确写出玩家为何不满或争议集中点"
            )
        if not COMMUNITY_TIMELINE.search(body):
            errors.append(
                f"community item lacks event timeline: {title}；须写明触发或延续日期"
            )
        if re.search(r"(?:\d+\s*(?:条)?回复|\d+\s*页|浏览(?:量)?\s*\d+|热度\s*\d+)", body):
            errors.append(f"community item contains reply/page/heat count: {title}")

    deep = section_text(report, SECTION_ALIASES["selected"])
    for title, body in item_bodies(deep):
        if "观察：" not in body or "分析：" not in body:
            errors.append(f"deep item lacks required 观察：/分析： structure: {title}")
            continue
        analysis = body.split("分析：", 1)[1]
        if len([part for part in re.split(r"\n\s*\n", analysis) if part.strip()]) < 2:
            errors.append(f"deep item needs at least two analysis paragraphs: {title}")

    # --- HARD CHECK(仅周报)：如存在人工指定的深度卡，校验指定标题及 URL。---
    # 卡片不再由正文第一条隐式决定；周四人工选择由周五生成任务写入
    # deep_card_choice.txt。没有选择文件表示本周不推独立卡，不自动降级。
    if args.report_type == "weekly" and sources:
        deep_items = item_bodies(deep)
        choice_path = report_path.parent / "deep_card_choice.txt"
        chosen_title = choice_path.read_text(encoding="utf-8").strip() if choice_path.exists() else ""
        if chosen_title:
            deep_titles = [title.strip() for title, _body in deep_items]
            if chosen_title not in deep_titles:
                errors.append(
                    f"deep_card_choice.txt 指定标题不在周报深度观察正文中: {chosen_title}"
                )
            map_ids: list[str] = []
            in_map = False
            for line in sources.splitlines():
                t = line.strip()
                if t.startswith("## "):
                    in_map = ("Item Source Map" in t or "条目来源映射" in t)
                    continue
                if in_map and t and not t.startswith("#"):
                    mm = re.match(
                        r"^(?:[-*]\s*|\d+\.\s*)?(?P<title>.+?)\s*(?:——|—|-)\s*(?P<ids>S\d{3,4}\b.*)$",
                        t,
                    )
                    if mm and mm.group("title").strip().strip("`") == chosen_title:
                        map_ids = re.findall(r"S\d{3,4}", mm.group("ids"))
                        break
            detail_has_url: dict[str, bool] = {}
            in_details = False
            for line in sources.splitlines():
                t = line.strip()
                if t.startswith("## "):
                    in_details = ("Source Details" in t or "来源明细" in t)
                    continue
                if in_details and t.startswith("-"):
                    sid_m = re.search(r"S\d{3,4}", t)
                    if sid_m:
                        detail_has_url[sid_m.group(0)] = bool(re.search(r"https?://\S+", t))
            if not map_ids:
                errors.append(
                    f"weekly 深度观察卡片人工指定为: {chosen_title}；"
                    "但它在 Item Source Map 中未映射到任何来源，无法生成带原文链接的卡片。"
                    "请为该指定条目补齐来源映射。"
                )
            elif not any(detail_has_url.get(sid) for sid in map_ids):
                errors.append(
                    f"weekly 深度观察卡片人工指定为: {chosen_title}；"
                    "其映射来源在 Source Details 中都没有可核验 http(s) URL，卡片会被静默跳过。"
                    "请为该指定条目补齐可点原文链接。"
                )

    if args.report_type:
        # 行业新闻不设条数上限：日报/月报 ≥7，周报 ≥8，由 E×R+M 绝对阈值决定。
        expectations = {
            "daily": {"ai": (1, 3), "release": (0, 4), "discourse": (1, 2), "selected": (1, 2)},
            "weekly": {"ai": (2, 6), "release": (0, 7), "discourse": (2, 3), "selected": (0, 99)},
            "monthly": {"ai": (4, 8), "release": (0, 12), "discourse": (3, 6), "selected": (1, 3)},
        }[args.report_type]
        for key, (low, high) in expectations.items():
            section = section_text(report, SECTION_ALIASES[key])
            if key == "release":
                count = len(re.findall(r"^-\s+", section, flags=re.MULTILINE))
            else:
                count = len(item_bodies(section))
            if count > high:
                warnings.append(f"{args.report_type} {key} section has {count} items; expected {low}-{high} unless strong extra news exists")

    # --- process check: 产品日历漏挂反查必须已执行并记录 ---
    # lint 无法判断"重要性"(那是 Value Gate)：靠关键词启发式只会把诺兰电影《奥德赛》、
    # 小众游戏发售和"网易遗忘之海"一起当节点抛出，噪声压过信号。改为过程核查——
    # 强制确认生成阶段真的做了 industry_news→产品日历 的漏挂反查并把结论写进
    # selection_decisions.md（重要性判断留在生成阶段，lint 只查这道自检没被跳过）。
    if args.inputs:
        sd_path = Path(args.inputs).parent / "selection_decisions.md"
        if sd_path.exists():
            sd_text = sd_path.read_text(encoding="utf-8", errors="ignore")
            history_path = Path(args.inputs).parent / "industry_history_14d.json"
            card_exposure_required = False
            if history_path.exists():
                try:
                    history_data = json.loads(history_path.read_text(encoding="utf-8"))
                    card_exposure_required = history_data.get("enforce_card_exposure_check") is True
                except (OSError, json.JSONDecodeError, AttributeError):
                    pass
            if card_exposure_required and "卡片曝光去重" not in sd_text:
                warnings.append(
                    "selection_decisions.md 缺『卡片曝光去重』记录："
                    "须说明历史匹配项是否曾进入订阅卡片、是否存在 card_carryover，"
                    "以及本期至多一条未曝光补位的选择结果"
                )
            if "产品日历漏挂反查" not in sd_text:
                warnings.append(
                    "selection_decisions.md 缺『产品日历漏挂反查』记录："
                    "需扫 industry_news 的上线/定档/测试节点，逐个确认已升产品日历或显式 exclude，"
                    "并落一行结论（参见 SKILL.md 同名自检）"
                )
            # 过程核查：行业新闻改由 E×R+M 打分选材（见 SKILL.md「Industry News 打分选材（E×R+M 模型）」）。
            # lint 不判"重要性"，只查生成阶段真的逐条打了分——要求 selection_decisions.md
            # 出现三项得分记录（形如 `事件3×相关3+钩子2 = 11`）。
            if not re.search(r"事件\s*[0-3]\s*[×xX*]\s*相关\s*[0-3]\s*\+\s*钩子\s*[0-2]", sd_text):
                industry_threshold = 8 if args.report_type == "weekly" else 7
                warnings.append(
                    "selection_decisions.md 缺行业新闻 E×R+M 打分记录："
                    "每条行业新闻候选须逐条记录『事件E×相关R+钩子M = 终分』并标 include/exclude，"
                    f"终分 = E×R+M（E、R 各 0-3，M 0-2）、事件类型 E=0 一票否决、"
                    f"本报告类型终分 ≥{industry_threshold} 才入选、"
                    "按终分从高到低排序（参见 SKILL.md「Industry News 打分选材（E×R+M 模型）」）"
                )

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warnings:
        print(f"WARN: {msg}")
    if not errors and not warnings:
        print("Report lint passed.")
    elif not errors:
        print("Report lint passed with warnings.")

    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
