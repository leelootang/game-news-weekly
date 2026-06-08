#!/usr/bin/env python3
"""Build skill-aligned interactive report pages from report_page_data.json."""

from __future__ import annotations

import argparse
import base64
import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "output" / "assets" / "moonton_logo.png"

SECTION_ORDER = ["rankings", "industry", "ai", "release", "discourse", "deep"]
SECTIONS = [
    {"id": "all", "label": "全部", "desc": "浏览全部日报内容，或从左侧选择单个板块。"},
    {"id": "rankings", "label": "steam当日榜单", "desc": "SteamDB 实时热销榜与近期新品观察。"},
    {"id": "industry", "label": "行业新闻", "desc": "公司、产品、市场与资本动作。"},
    {"id": "ai", "label": "AI 新闻", "desc": "生成式 AI、工作流与安全治理。"},
    {"id": "release", "label": "产品日历", "desc": "上线、测试、新版本与重点节点。"},
    {"id": "discourse", "label": "玩家舆论", "desc": "社区热点、争议与玩家情绪。"},
    {"id": "deep", "label": "深度观察", "desc": "值得内部团队继续跟踪的结构性变化。"},
]


def script_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


def normalize_items(items: list[dict]) -> list[dict]:
    valid = set(SECTION_ORDER)
    normalized = []
    for item in items:
        section = item.get("section") or "industry"
        if section not in valid:
            raise ValueError(f"invalid section: {section}")
        normalized.append(
            {
                "section": section,
                "title": str(item.get("title", "")).strip(),
                "body": str(item.get("body", "")).strip(),
                "body_html": str(item.get("body_html", "") or ""),
                "meta": [str(x) for x in item.get("meta", [])],
                "sources": item.get("sources", []),
            }
        )
    return normalized


def logo_data_uri() -> str:
    if not LOGO.exists():
        return ""
    return f"data:image/png;base64,{base64.b64encode(LOGO.read_bytes()).decode('ascii')}"


def relative_logo(out_path: Path) -> str:
    try:
        return LOGO.relative_to(out_path.parent).as_posix()
    except ValueError:
        return Path("../../assets/moonton_logo.png").as_posix()


def render_html(data: dict, logo_src: str) -> str:
    items = normalize_items(data.get("items", []))
    counts = {sid: sum(1 for item in items if item["section"] == sid) for sid in SECTION_ORDER}
    title = data.get("title") or "游戏行业日报"
    date = data.get("date") or ""
    subtitle = data.get("subtitle") or "行业新闻、AI、产品日历、玩家舆论与精选观察"
    collected_records = data.get("collected_records", len(items))

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(str(title))} | {escape(str(date))}</title>
  <style>
    :root {{
      --ink:#1a2436; --ink-soft:#3a4862; --muted:#6b7993; --faint:#9aa6bd;
      --accent:#5b6ef5; --glass:rgba(255,255,255,.62); --glass-border:rgba(255,255,255,.7);
      --line:rgba(31,45,75,.10); --line-strong:rgba(31,45,75,.16);
      --shadow-sm:0 3px 12px rgba(31,45,75,.05); --shadow-lg:0 14px 40px rgba(31,45,75,.12);
      --rankings:#d05f3f; --rankings-soft:rgba(208,95,63,.12); --rankings-ink:#9d3f25;
      --industry:#4f7cff; --industry-soft:rgba(79,124,255,.12); --industry-ink:#2b53c4;
      --ai:#00b3d4; --ai-soft:rgba(0,179,212,.12); --ai-ink:#06748a;
      --release:#16b884; --release-soft:rgba(22,184,132,.13); --release-ink:#0b7a57;
      --discourse:#f0a02a; --discourse-soft:rgba(240,160,42,.15); --discourse-ink:#9a6206;
      --deep:#8b6df0; --deep-soft:rgba(139,109,240,.13); --deep-ink:#5a3fc0;
    }}
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    html,body {{ min-height:100%; }}
    body {{ color:var(--ink); font-family:"PingFang SC","Microsoft YaHei","Segoe UI",Arial,sans-serif; line-height:1.65; -webkit-font-smoothing:antialiased; overflow-x:hidden; }}
    body::before {{ content:""; position:fixed; inset:0; z-index:-1;
      background:
        radial-gradient(circle at 12% 18%, rgba(91,110,245,.20), transparent 42%),
        radial-gradient(circle at 88% 12%, rgba(0,179,212,.16), transparent 40%),
        radial-gradient(circle at 78% 88%, rgba(139,109,240,.18), transparent 46%),
        radial-gradient(circle at 25% 92%, rgba(22,184,132,.13), transparent 44%),
        linear-gradient(135deg,#eef1fb 0%,#f3effb 48%,#eaf3fc 100%); }}
    a {{ color:inherit; text-decoration:none; }}
    button,input {{ font:inherit; }}
    .app {{ min-height:100vh; display:grid; grid-template-columns:264px minmax(0,1fr); transition:grid-template-columns .25s cubic-bezier(.4,0,.2,1); }}
    .app.collapsed {{ grid-template-columns:0 minmax(0,1fr); }}
    aside.sidebar {{ position:sticky; top:0; height:100vh; padding:24px 18px; color:var(--ink); display:flex; flex-direction:column;
      background:rgba(255,255,255,.48); backdrop-filter:blur(22px) saturate(170%); -webkit-backdrop-filter:blur(22px) saturate(170%);
      border-right:1px solid rgba(255,255,255,.55); overflow-y:auto; overflow-x:hidden; transition:transform .25s cubic-bezier(.4,0,.2,1), opacity .2s; }}
    .app.collapsed aside.sidebar {{ transform:translateX(-100%); opacity:0; pointer-events:none; }}
    .brand {{ display:flex; align-items:center; gap:12px; padding-bottom:20px; border-bottom:1px solid var(--line); }}
    .brand-mark {{ width:42px; height:42px; display:grid; place-items:center; border-radius:12px; background:#fff; padding:7px; box-shadow:0 3px 10px rgba(31,45,75,.10); }}
    .brand-mark img {{ width:100%; height:100%; display:block; object-fit:contain; }}
    .brand strong {{ display:block; font-size:16px; line-height:1.1; letter-spacing:.3px; color:var(--ink); }}
    .brand span {{ display:block; font-size:11.5px; color:var(--muted); margin-top:3px; }}
    .nav-title {{ margin:22px 0 10px; color:var(--faint); font-size:10px; letter-spacing:1.3px; text-transform:uppercase; font-weight:700; }}
    .nav {{ display:grid; gap:3px; }}
    .nav button {{ width:100%; display:flex; justify-content:space-between; align-items:center; gap:8px; border:0; background:transparent; color:var(--ink-soft); padding:11px 14px; text-align:left; cursor:pointer; border-radius:11px; position:relative; font-size:14px; font-weight:500; transition:all .14s; }}
    .nav button:hover {{ background:rgba(255,255,255,.55); color:var(--ink); }}
    .nav button.active {{ background:rgba(91,110,245,.12); color:var(--accent); font-weight:600; box-shadow:inset 0 0 0 1px rgba(91,110,245,.18); }}
    .nav button.active::before {{ content:""; position:absolute; left:0; top:9px; bottom:9px; width:3px; border-radius:0 3px 3px 0; background:var(--accent2,var(--accent)); }}
    .nav button[data-section="rankings"] {{ --accent2:var(--rankings); }}
    .nav button[data-section="industry"] {{ --accent2:var(--industry); }}
    .nav button[data-section="ai"] {{ --accent2:var(--ai); }}
    .nav button[data-section="release"] {{ --accent2:var(--release); }}
    .nav button[data-section="discourse"] {{ --accent2:var(--discourse); }}
    .nav button[data-section="deep"] {{ --accent2:var(--deep); }}
    .count {{ min-width:24px; padding:1px 9px; color:var(--muted); background:rgba(31,45,75,.07); text-align:center; border-radius:11px; font-size:12px; font-weight:600; }}
    .nav button.active .count {{ background:var(--accent2,var(--accent)); color:#fff; }}
    .aside-note {{ margin-top:22px; padding:14px; background:rgba(255,255,255,.5); border:1px solid var(--glass-border); border-left:3px solid var(--ai); color:var(--ink-soft); font-size:12.5px; line-height:1.6; border-radius:12px; }}
    .sidebar-footer {{ margin-top:auto; padding:16px 4px 0; border-top:1px solid var(--line); color:var(--muted); font-size:11.5px; line-height:1.7; }}
    .sidebar-footer strong {{ display:block; color:var(--ink-soft); font-weight:700; }}
    .sidebar-footer a {{ color:var(--accent); font-weight:600; overflow-wrap:anywhere; }}
    main {{ padding:30px 40px 64px; min-width:0; }}
    .topbar {{ display:flex; align-items:flex-start; justify-content:space-between; gap:18px; margin-bottom:26px; padding-bottom:22px; border-bottom:1px solid var(--line); }}
    h1 {{ margin:0; font-size:28px; line-height:1.25; font-weight:800; color:var(--ink); }}
    .subtitle {{ margin-top:8px; color:var(--muted); font-size:13.5px; }}
    .actions {{ display:flex; gap:10px; align-items:center; }}
    .sidebar-toggle,.icon-btn {{ border:1px solid var(--glass-border); background:var(--glass); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); color:var(--ink-soft); cursor:pointer; width:40px; height:40px; border-radius:12px; transition:all .14s; }}
    .sidebar-toggle:hover,.icon-btn:hover {{ color:var(--accent); border-color:var(--accent); }}
    .sidebar-toggle .icon-open {{ display:inline; }}
    .sidebar-toggle .icon-close {{ display:none; }}
    .app.collapsed .sidebar-toggle .icon-open {{ display:none; }}
    .app.collapsed .sidebar-toggle .icon-close {{ display:inline; }}
    .search {{ width:320px; display:flex; align-items:center; gap:8px; background:var(--glass); backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); border:1px solid var(--glass-border); padding:9px 14px; border-radius:12px; transition:border-color .15s, box-shadow .15s; }}
    .search:focus-within {{ border-color:var(--accent); box-shadow:0 0 0 3px rgba(91,110,245,.12); background:#fff; }}
    .search input {{ width:100%; border:0; outline:0; background:transparent; color:var(--ink); font-size:13.5px; }}
    .search input::placeholder {{ color:var(--faint); }}
    .metrics {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; margin-bottom:30px; }}
    .metric {{ background:var(--glass); backdrop-filter:blur(16px) saturate(150%); -webkit-backdrop-filter:blur(16px) saturate(150%); border:1px solid var(--glass-border); padding:18px 20px; border-radius:18px; box-shadow:var(--shadow-sm); position:relative; overflow:hidden; }}
    .metric::before {{ content:""; position:absolute; left:0; top:0; bottom:0; width:3px; background:var(--accent2,var(--industry)); }}
    .metric:nth-child(1) {{ --accent2:var(--industry); }}
    .metric:nth-child(2) {{ --accent2:var(--release); }}
    .metric:nth-child(3) {{ --accent2:var(--discourse); }}
    .metric:nth-child(4) {{ --accent2:var(--deep); }}
    .metric span {{ color:var(--muted); font-size:12.5px; letter-spacing:.3px; }}
    .metric strong {{ display:block; font-size:26px; line-height:1.1; margin-top:6px; font-weight:800; color:var(--ink); }}
    .section-head {{ display:flex; justify-content:space-between; gap:16px; align-items:flex-end; margin:6px 0 20px; padding:16px 20px; background:var(--glass); backdrop-filter:blur(16px); -webkit-backdrop-filter:blur(16px); border:1px solid var(--glass-border); border-left:4px solid var(--accent2,var(--industry)); border-radius:18px; box-shadow:var(--shadow-sm); }}
    .section-head[data-section="rankings"] {{ --accent2:var(--rankings); }}
    .section-head[data-section="industry"] {{ --accent2:var(--industry); }}
    .section-head[data-section="ai"] {{ --accent2:var(--ai); }}
    .section-head[data-section="release"] {{ --accent2:var(--release); }}
    .section-head[data-section="discourse"] {{ --accent2:var(--discourse); }}
    .section-head[data-section="deep"] {{ --accent2:var(--deep); }}
    h2 {{ margin:0; font-size:20px; font-weight:700; }}
    .section-head p {{ margin:4px 0 0; color:var(--muted); font-size:13px; }}
    .toggle {{ display:flex; border:1px solid var(--glass-border); background:var(--glass); border-radius:11px; overflow:hidden; }}
    .toggle button {{ padding:8px 15px; border:0; background:transparent; color:var(--ink-soft); cursor:pointer; font-size:13px; transition:all .14s; }}
    .toggle button.active {{ background:var(--accent); color:#fff; font-weight:600; }}
    .section-block {{ margin-top:38px; }}
    .section-block:first-child {{ margin-top:0; }}
    .section-banner {{ display:flex; align-items:baseline; gap:14px; padding:13px 18px; margin-bottom:16px; background:var(--accent-soft,var(--industry-soft)); border-left:4px solid var(--accent2,var(--industry)); border-radius:14px; }}
    .section-banner[data-section="rankings"] {{ --accent2:var(--rankings); --accent-soft:var(--rankings-soft); --accent-ink:var(--rankings-ink); }}
    .section-banner[data-section="industry"] {{ --accent2:var(--industry); --accent-soft:var(--industry-soft); --accent-ink:var(--industry-ink); }}
    .section-banner[data-section="ai"] {{ --accent2:var(--ai); --accent-soft:var(--ai-soft); --accent-ink:var(--ai-ink); }}
    .section-banner[data-section="release"] {{ --accent2:var(--release); --accent-soft:var(--release-soft); --accent-ink:var(--release-ink); }}
    .section-banner[data-section="discourse"] {{ --accent2:var(--discourse); --accent-soft:var(--discourse-soft); --accent-ink:var(--discourse-ink); }}
    .section-banner[data-section="deep"] {{ --accent2:var(--deep); --accent-soft:var(--deep-soft); --accent-ink:var(--deep-ink); }}
    .section-banner h2 {{ color:var(--accent-ink); font-size:17px; margin:0; font-weight:700; }}
    .section-banner .banner-count {{ color:var(--accent2); font-weight:700; font-size:13px; }}
    .section-banner .banner-desc {{ color:var(--accent-ink); opacity:.7; font-size:13px; margin-left:auto; }}
    .grid {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; }}
    .grid.compact {{ grid-template-columns:1fr; }}
    .section-block[data-section="rankings"] .grid {{ grid-template-columns:1fr; }}
    .item {{ background:var(--glass); backdrop-filter:blur(16px) saturate(150%); -webkit-backdrop-filter:blur(16px) saturate(150%); border:1px solid var(--glass-border); border-left:3px solid var(--accent2,var(--industry)); padding:20px 24px; border-radius:18px; box-shadow:var(--shadow-sm); transition:transform .18s, box-shadow .18s; display:flex; flex-direction:column; min-width:0; }}
    .item:hover {{ box-shadow:var(--shadow-lg); transform:translateY(-2px); }}
    .item[data-section="rankings"] {{ --accent2:var(--rankings); --accent-soft:var(--rankings-soft); --accent-ink:var(--rankings-ink); }}
    .item[data-section="industry"] {{ --accent2:var(--industry); --accent-soft:var(--industry-soft); --accent-ink:var(--industry-ink); }}
    .item[data-section="ai"] {{ --accent2:var(--ai); --accent-soft:var(--ai-soft); --accent-ink:var(--ai-ink); }}
    .item[data-section="release"] {{ --accent2:var(--release); --accent-soft:var(--release-soft); --accent-ink:var(--release-ink); }}
    .item[data-section="discourse"] {{ --accent2:var(--discourse); --accent-soft:var(--discourse-soft); --accent-ink:var(--discourse-ink); }}
    .item[data-section="deep"] {{ --accent2:var(--deep); --accent-soft:var(--deep-soft); --accent-ink:var(--deep-ink); }}
    .item-top {{ display:flex; justify-content:space-between; gap:12px; align-items:center; margin-bottom:11px; }}
    .tag {{ padding:3px 11px; font-size:12px; color:var(--accent-ink); background:var(--accent-soft); border-radius:8px; font-weight:700; letter-spacing:.2px; }}
    h3 {{ margin:2px 0 10px; font-size:17.5px; line-height:1.45; font-weight:700; color:var(--ink); letter-spacing:.1px; }}
    .body {{ margin:0 0 14px; color:var(--ink-soft); font-size:14.5px; line-height:1.78; }}
    .body p {{ margin:0 0 14px; }}
    .body ul {{ margin:0 0 12px; padding-left:20px; }}
    .body li {{ margin:0 0 8px; }}
    .ranking-table-wrap {{ width:100%; overflow-x:auto; border:1px solid var(--line); border-radius:10px; background:rgba(255,255,255,.54); }}
    .ranking-table {{ width:100%; min-width:680px; border-collapse:collapse; font-size:12.5px; }}
    .ranking-table th,.ranking-table td {{ padding:6px 10px; border-bottom:1px solid var(--line); text-align:left; white-space:nowrap; }}
    .ranking-table th {{ color:var(--ink); background:rgba(208,95,63,.08); font-weight:700; }}
    .ranking-table td:first-child,.ranking-table th:first-child {{ text-align:right; }}
    .ranking-table td:nth-child(2):not(:empty) {{ color:var(--rankings); font-weight:700; }}
    .ranking-table tbody tr:last-child td {{ border-bottom:0; }}
    .meta-row {{ display:flex; flex-wrap:wrap; gap:7px; color:var(--muted); font-size:12px; margin-bottom:4px; }}
    .meta-row span {{ padding:3px 10px; background:rgba(31,45,75,.06); border-radius:8px; }}
    .item .meta-row span.borderline {{ background:rgba(240,160,42,.14); color:#a8680a; }}
    .source-btn {{ margin-top:14px; padding:8px 14px; border:1px solid var(--glass-border); background:rgba(255,255,255,.5); color:var(--accent); cursor:pointer; border-radius:11px; font-size:13px; font-weight:600; align-self:flex-start; transition:all .14s; }}
    .source-btn:hover {{ background:var(--accent-soft); border-color:var(--accent2); }}
    .empty {{ display:none; padding:48px; border:1px dashed var(--line-strong); color:var(--muted); text-align:center; background:var(--glass); border-radius:18px; }}
    .empty.visible {{ display:block; }}
    .overlay {{ position:fixed; inset:0; display:none; background:rgba(26,36,54,.3); backdrop-filter:blur(3px); z-index:10; }}
    .overlay.open {{ display:block; }}
    .drawer {{ position:fixed; top:0; right:0; width:min(440px,100vw); height:100vh; transform:translateX(100%); transition:.22s cubic-bezier(.4,0,.2,1); background:rgba(255,255,255,.85); backdrop-filter:blur(24px) saturate(160%); -webkit-backdrop-filter:blur(24px) saturate(160%); border-left:1px solid var(--glass-border); box-shadow:-18px 0 44px rgba(31,45,75,.16); padding:24px; overflow:auto; z-index:11; }}
    .drawer.open {{ transform:translateX(0); }}
    .drawer-head {{ display:flex; justify-content:space-between; gap:12px; align-items:flex-start; margin-bottom:8px; }}
    .drawer h2 {{ font-size:17px; line-height:1.4; }}
    #drawerNote {{ color:var(--muted); font-size:13px; line-height:1.7; margin:0 0 18px; padding-bottom:16px; border-bottom:1px solid var(--line); }}
    .source-card {{ border:1px solid var(--glass-border); padding:13px 15px; margin-top:10px; border-radius:12px; background:rgba(255,255,255,.55); }}
    .source-card strong {{ font-size:13px; color:var(--ink); }}
    .source-url {{ display:block; margin-top:6px; color:var(--accent); overflow-wrap:anywhere; user-select:text; font-size:12.5px; text-decoration:none; }}
    a.source-url:hover {{ text-decoration:underline; }}
    @media (max-width:900px) {{
      .app {{ grid-template-columns:1fr; }}
      aside.sidebar {{ position:relative; height:auto; }}
      .nav {{ grid-template-columns:repeat(2,minmax(0,1fr)); }}
      main {{ padding:22px 18px 36px; }}
      .topbar,.section-head {{ align-items:stretch; flex-direction:column; }}
      .actions {{ flex-wrap:wrap; }}
      .search {{ width:100%; order:2; }}
      .metrics,.grid {{ grid-template-columns:1fr; }}
      .section-banner {{ flex-wrap:wrap; }}
      .section-banner .banner-desc {{ margin-left:0; width:100%; }}
    }}
    @media print {{
      body::before {{ display:none; }}
      aside.sidebar,.actions,.toggle,.source-btn,.drawer,.overlay {{ display:none!important; }}
      .app {{ display:block; }}
      main {{ padding:0; }}
      .item {{ break-inside:avoid; box-shadow:none; border-color:#bbb; backdrop-filter:none; background:#fff; }}
      .section-banner {{ break-after:avoid; }}
    }}
  </style>
</head>
<body>
  <div class="app" id="app">
    <aside class="sidebar">
      <div class="brand" aria-label="沐瞳科技">
        <div class="brand-mark" aria-hidden="true"><img src="{escape(logo_src)}" alt=""></div>
        <div><strong>MOONTON</strong><span>沐瞳科技 · Strategy Brief</span></div>
      </div>
      <div class="nav-title">Sections</div>
      <nav class="nav" id="nav"></nav>
      <div class="aside-note">面向内部团队的报告视图。内容按业务事件、产品节点和玩家反馈拆分，来源映射可在每条内容内查看。</div>
      <div class="sidebar-footer"><strong>Made by 沐瞳科技战略团队</strong><span>有问题请联系 <a href="mailto:leelootang@moonton.com">leelootang@moonton.com</a></span></div>
    </aside>
    <main>
      <div class="topbar">
        <div><h1>{escape(str(title))}</h1><div class="subtitle">{escape(str(date))} · {escape(str(subtitle))}</div></div>
        <div class="actions">
          <button class="sidebar-toggle" id="sidebarToggle" type="button" title="折叠 / 展开侧栏" aria-label="切换侧栏"><span class="icon-open">«</span><span class="icon-close">»</span></button>
          <label class="search">⌕<input id="search" type="search" placeholder="搜索条目、公司、产品"></label>
          <button class="icon-btn" id="printBtn" type="button" title="打印">⎙</button>
        </div>
      </div>
      <div class="metrics">
        <div class="metric"><span>行业新闻</span><strong>{counts.get("industry", 0)}</strong></div>
        <div class="metric"><span>产品日历</span><strong>{counts.get("release", 0)}</strong></div>
        <div class="metric"><span>玩家舆论</span><strong>{counts.get("discourse", 0)}</strong></div>
        <div class="metric"><span>采集记录</span><strong>{escape(str(collected_records))}</strong></div>
      </div>
      <div class="section-head" id="sectionHead"><div><h2 id="sectionTitle"></h2><p id="sectionDesc"></p></div><div class="toggle"><button id="viewGrid" class="active" type="button">双列</button><button id="viewList" type="button">列表</button></div></div>
      <div id="content"></div>
      <div class="empty" id="empty">没有匹配的条目。</div>
    </main>
  </div>
  <div class="overlay" id="overlay"></div>
  <aside class="drawer" id="drawer" aria-label="来源详情">
    <div class="drawer-head"><h2 id="drawerTitle"></h2><button class="icon-btn" id="closeDrawer" type="button">×</button></div>
    <p id="drawerNote"></p>
    <div id="sourceList"></div>
  </aside>
  <script>
    const sections = {script_json(SECTIONS)};
    const items = {script_json(items)};
    const sectionLabels = Object.fromEntries(sections.map(s => [s.id, s.label]));
    const sectionDescs = Object.fromEntries(sections.map(s => [s.id, s.desc]));
    const orderedSectionIds = sections.filter(s => s.id !== "all").map(s => s.id);
    let currentSection = "all";
    let compact = false;
    const nav = document.getElementById("nav");
    const content = document.getElementById("content");
    const sectionHead = document.getElementById("sectionHead");
    const search = document.getElementById("search");
    const empty = document.getElementById("empty");
    const drawer = document.getElementById("drawer");
    const overlay = document.getElementById("overlay");
    function escHtml(value) {{
      return String(value == null ? "" : value).replace(/[&<>"']/g, ch => ({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}}[ch]));
    }}
    function matches(item, query) {{
      if (!query) return true;
      const text = [item.title, item.body, (item.meta||[]).join(" "), (item.sources||[]).map(s => s.join(" ")).join(" ")].join(" ").toLowerCase();
      return text.includes(query.toLowerCase());
    }}
    function isBorderline(m) {{ return /borderline/i.test(m); }}
    function renderNav() {{
      nav.innerHTML = "";
      sections.forEach(section => {{
        const count = section.id === "all" ? items.length : items.filter(item => item.section === section.id).length;
        const button = document.createElement("button");
        button.dataset.section = section.id;
        if (section.id === currentSection) button.classList.add("active");
        button.innerHTML = `<span>${{escHtml(section.label)}}</span><span class="count">${{count}}</span>`;
        button.addEventListener("click", () => {{ currentSection = section.id; render(); }});
        nav.appendChild(button);
      }});
    }}
    function renderItem(item) {{
      const node = document.createElement("article");
      node.className = "item";
      node.dataset.section = item.section;
      const metaTags = (item.meta || []).map(m => `<span class="${{isBorderline(m) ? "borderline" : ""}}">${{escHtml(m)}}</span>`).join("");
      const bodyMarkup = item.body_html && item.body_html.trim() ? item.body_html : `<p>${{escHtml(item.body)}}</p>`;
      node.innerHTML = `<div class="item-top"><span class="tag">${{escHtml(sectionLabels[item.section])}}</span></div><h3>${{escHtml(item.title)}}</h3><div class="body">${{bodyMarkup}}</div><div class="meta-row">${{metaTags}}</div><button class="source-btn" type="button">查看来源 →</button>`;
      node.querySelector(".source-btn").addEventListener("click", () => openDrawer(item));
      return node;
    }}
    function buildGrid(itemList) {{
      const grid = document.createElement("section");
      grid.className = compact ? "grid compact" : "grid";
      itemList.forEach(item => grid.appendChild(renderItem(item)));
      return grid;
    }}
    function buildSectionBlock(sectionId, itemList) {{
      const block = document.createElement("div");
      block.className = "section-block";
      block.dataset.section = sectionId;
      const banner = document.createElement("div");
      banner.className = "section-banner";
      banner.dataset.section = sectionId;
      banner.innerHTML = `<h2>${{escHtml(sectionLabels[sectionId])}}</h2><span class="banner-count">${{itemList.length}} 条</span><span class="banner-desc">${{escHtml(sectionDescs[sectionId])}}</span>`;
      block.appendChild(banner);
      block.appendChild(buildGrid(itemList));
      return block;
    }}
    function render() {{
      renderNav();
      const query = search.value.trim();
      const filtered = items.filter(item => (currentSection === "all" || item.section === currentSection) && matches(item, query));
      content.innerHTML = "";
      if (currentSection === "all") {{
        sectionHead.style.display = "none";
        orderedSectionIds.forEach(sid => {{
          const sectionItems = filtered.filter(it => it.section === sid);
          if (sectionItems.length > 0) content.appendChild(buildSectionBlock(sid, sectionItems));
        }});
      }} else {{
        sectionHead.style.display = "flex";
        sectionHead.dataset.section = currentSection;
        document.getElementById("sectionTitle").textContent = sectionLabels[currentSection];
        document.getElementById("sectionDesc").textContent = sectionDescs[currentSection];
        content.appendChild(buildGrid(filtered));
      }}
      empty.classList.toggle("visible", filtered.length === 0);
    }}
    function openDrawer(item) {{
      document.getElementById("drawerTitle").textContent = item.title;
      document.getElementById("drawerNote").textContent = item.body;
      document.getElementById("sourceList").innerHTML = (item.sources || []).map(([id,name,url]) => {{
        const safeUrl = String(url || "");
        const isHttp = /^https?:\\/\\//i.test(safeUrl);
        const urlEl = isHttp ? `<a class="source-url" href="${{escHtml(safeUrl)}}" target="_blank" rel="noopener noreferrer">${{escHtml(safeUrl)}} ↗</a>` : `<span class="source-url">${{escHtml(safeUrl)}}</span>`;
        return `<div class="source-card"><strong>${{escHtml(id)}} · ${{escHtml(name)}}</strong>${{urlEl}}</div>`;
      }}).join("");
      drawer.classList.add("open");
      overlay.classList.add("open");
    }}
    function closeDrawer() {{ drawer.classList.remove("open"); overlay.classList.remove("open"); }}
    search.addEventListener("input", render);
    document.getElementById("printBtn").addEventListener("click", () => window.print());
    const app = document.getElementById("app");
    const SIDEBAR_KEY = "report-sidebar-collapsed";
    try {{ if (localStorage.getItem(SIDEBAR_KEY) === "1") app.classList.add("collapsed"); }} catch (e) {{}}
    document.getElementById("sidebarToggle").addEventListener("click", () => {{
      app.classList.toggle("collapsed");
      try {{ localStorage.setItem(SIDEBAR_KEY, app.classList.contains("collapsed") ? "1" : "0"); }} catch (e) {{}}
    }});
    document.getElementById("closeDrawer").addEventListener("click", closeDrawer);
    overlay.addEventListener("click", closeDrawer);
    document.getElementById("viewGrid").addEventListener("click", () => {{ compact = false; document.getElementById("viewGrid").classList.add("active"); document.getElementById("viewList").classList.remove("active"); render(); }});
    document.getElementById("viewList").addEventListener("click", () => {{ compact = true; document.getElementById("viewList").classList.add("active"); document.getElementById("viewGrid").classList.remove("active"); render(); }});
    render();
  </script>
</body>
</html>
"""


def build_one(date: str) -> None:
    report_dir = ROOT / "output" / "daily" / date
    data_path = report_dir / "report_page_data.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    out_path = report_dir / "interactive_report.html"
    out_path.write_text(render_html(data, relative_logo(out_path)), encoding="utf-8")

    docs_path = ROOT / "docs" / "daily" / date / "index.html"
    docs_path.parent.mkdir(parents=True, exist_ok=True)
    docs_path.write_text(render_html(data, logo_data_uri()), encoding="utf-8")
    print(f"Built {date}: {out_path} -> {docs_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dates", nargs="+")
    args = parser.parse_args()
    for date in args.dates:
        build_one(date)


if __name__ == "__main__":
    main()
