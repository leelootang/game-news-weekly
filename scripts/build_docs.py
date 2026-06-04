"""
Build docs/ for GitHub Pages.

Scans output/daily/*/interactive_report.html (and weekly/monthly when present),
copies them to docs/ with the logo inlined, and generates a portal index page.
"""

import base64
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUTPUT = ROOT / "output"
DOCS = ROOT / "docs"
SHARED_LOGO = OUTPUT / "assets" / "moonton_logo.png"

SECTION_ORDER = ("industry", "ai", "release", "discourse", "deep")

SECTION_LABELS = {
    "industry": "行业新闻",
    "ai": "AI 动态",
    "release": "产品日历",
    "discourse": "玩家舆论",
    "deep":     "深度观察",
}

# Refined, slightly desaturated palette for a premium feel
SECTION_COLORS = {
    "industry": "#4f7cff",
    "ai":       "#00b3d4",
    "release":  "#16b884",
    "discourse":"#f0a02a",
    "deep":     "#8b6df0",
}


# ── helpers ──────────────────────────────────────────────────────────────────

def logo_data_uri() -> str:
    logo = SHARED_LOGO if SHARED_LOGO.exists() else next(OUTPUT.glob("daily/*/moonton_logo.png"), None)
    if not logo:
        return ""
    return f"data:image/png;base64,{base64.b64encode(logo.read_bytes()).decode()}"


LOGO_URI = ""  # set in build_docs()

# Static attribution bar injected into each report page (not sticky there).
ATTRIBUTION_BAR = (
    '<div style="background:#1f2a3d;color:#9fb4d2;font-size:12px;text-align:center;'
    'padding:7px 16px;letter-spacing:.2px;">'
    'Made by 沐瞳科技战略团队 · 有问题请联系 '
    '<a href="mailto:leelootang@moonton.com" '
    'style="color:#56a8ff;text-decoration:none;">leelootang@moonton.com</a>'
    '</div>'
)


def _find_items_block(html: str) -> str | None:
    start = html.find("const items = [")
    if start == -1:
        return None
    idx = html.index("[", start)
    depth = 0
    for i in range(idx, len(html)):
        c = html[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return html[idx: i + 1]
    return None


def extract_items_full(html: str, date_str: str, report_url: str) -> list[dict]:
    block = _find_items_block(html)
    if not block:
        return []
    try:
        items = json.loads(block)
    except json.JSONDecodeError:
        return []
    slim = []
    for item in items:
        slim.append({
            "section": item.get("section", ""),
            "title": item.get("title", ""),
            "body": item.get("body", ""),
            "meta": item.get("meta", []),
            "date": date_str,
            "reportUrl": report_url,
        })
    return slim


def extract_metadata(html: str) -> tuple[int, dict]:
    block = _find_items_block(html)
    if not block:
        return 0, {}
    try:
        items = json.loads(block)
        counts: dict[str, int] = {}
        for item in items:
            s = item.get("section", "")
            counts[s] = counts.get(s, 0) + 1
        return len(items), counts
    except json.JSONDecodeError:
        pass
    counts = {}
    for sec_id in SECTION_LABELS:
        counts[sec_id] = len(re.findall(rf'section:\s*["\']?{sec_id}["\']?', block))
    return sum(counts.values()), {k: v for k, v in counts.items() if v > 0}


def copy_report(html_path: Path, dest_dir: Path) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    content = html_path.read_text(encoding="utf-8")
    if LOGO_URI:
        content = content.replace('src="moonton_logo.png"', f'src="{LOGO_URI}"')
    content = content.replace("<body>", f"<body>{ATTRIBUTION_BAR}", 1)
    (dest_dir / "index.html").write_text(content, encoding="utf-8")


def format_date(date_str: str) -> str:
    parts = date_str.split("-")
    if len(parts) == 3:
        return f"{parts[0]}/{parts[1].lstrip('0')}/{parts[2].lstrip('0')}"
    return date_str


def format_date_long(date_str: str) -> str:
    parts = date_str.split("-")
    if len(parts) == 3:
        return f"{parts[0]} 年 {parts[1].lstrip('0')} 月 {parts[2].lstrip('0')} 日"
    return date_str


def section_pills_html(counts: dict) -> str:
    out = []
    for sid in SECTION_ORDER:
        n = counts.get(sid, 0)
        if not n:
            continue
        c = SECTION_COLORS[sid]
        out.append(
            f'<span style="background:{c}1f;color:{c};padding:2px 9px;border-radius:8px;font-size:11px;">'
            f'{SECTION_LABELS[sid]} {n}</span>'
        )
    return " ".join(out)


def build_index(reports: list[dict], all_items: list[dict]) -> str:
    daily   = [r for r in reports if r["type"] == "daily"]
    weekly  = [r for r in reports if r["type"] == "weekly"]
    monthly = [r for r in reports if r["type"] == "monthly"]

    total_items = len(all_items)
    total_reports = len(reports)

    items_json = json.dumps(all_items, ensure_ascii=False).replace("</", "<\\/")

    def report_card(r: dict) -> str:
        d = r["date"]
        if r["type"] == "weekly":
            parts = d.split("_to_")
            date_label = f"{format_date(parts[0])} — {format_date(parts[1])}" if len(parts) == 2 else d
        elif r["type"] == "monthly":
            date_label = d
        else:
            date_label = format_date_long(d)
        type_labels = {"daily": "日报", "weekly": "周报", "monthly": "月报"}
        type_colors = {"daily": "#4f7cff", "weekly": "#8b6df0", "monthly": "#16b884"}
        bc = type_colors.get(r["type"], "#4f7cff")
        bl = type_labels.get(r["type"], "报告")
        pills = section_pills_html(r["counts"])
        return (
            f'<a href="{r["url"]}" class="rcard">'
            f'<div class="rcard-top">'
            f'<span class="rbadge" style="background:{bc}1f;color:{bc};">{bl}</span>'
            f'<span class="rtotal">{r["total"]} 条</span></div>'
            f'<div class="rdate">{date_label}</div>'
            f'<div class="rpills">{pills}</div>'
            f'<div class="rlink">查看完整报告 →</div></a>'
        )

    all_rcards    = "\n".join(report_card(r) for r in reports) if reports else '<p class="empty-msg">暂无报告</p>'
    daily_rcards  = "\n".join(report_card(r) for r in daily)   if daily   else '<p class="empty-msg">暂无日报</p>'
    weekly_rcards = "\n".join(report_card(r) for r in weekly)  if weekly  else '<p class="empty-msg">暂无周报</p>'
    monthly_rcards= "\n".join(report_card(r) for r in monthly) if monthly else '<p class="empty-msg">暂无月报</p>'

    feed_tabs = '<button class="ftab active" data-sec="all">全部</button>'
    for sid in SECTION_ORDER:
        feed_tabs += f'<button class="ftab" data-sec="{sid}">{SECTION_LABELS[sid]}</button>'

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>游戏行业情报站</title>
  <style>
    :root {{
      --ink:#1a2436; --ink2:#3a4862; --muted:#6b7993; --faint:#9aa6bd;
      --accent:#5b6ef5;
      --glass:rgba(255,255,255,.62); --glass-strong:rgba(255,255,255,.78);
      --glass-border:rgba(255,255,255,.7); --hair:rgba(31,45,75,.10);
      --sh:0 6px 28px rgba(31,45,75,.07); --sh-lg:0 14px 40px rgba(31,45,75,.12);
      --attrib-h:0px; --sw:256px;
    }}
    *{{box-sizing:border-box;margin:0;padding:0;}}
    html,body{{height:100%;}}
    body{{color:var(--ink);font-family:"PingFang SC","Microsoft YaHei","Segoe UI",Arial,sans-serif;
          line-height:1.65;-webkit-font-smoothing:antialiased;}}
    /* decorative gradient field behind the frosted glass */
    body::before{{content:"";position:fixed;inset:0;z-index:-1;
      background:
        radial-gradient(circle at 12% 18%, rgba(91,110,245,.20), transparent 42%),
        radial-gradient(circle at 88% 12%, rgba(0,179,212,.16), transparent 40%),
        radial-gradient(circle at 78% 88%, rgba(139,109,240,.18), transparent 46%),
        radial-gradient(circle at 25% 92%, rgba(22,184,132,.13), transparent 44%),
        linear-gradient(135deg,#eef1fb 0%,#f3effb 48%,#eaf3fc 100%);}}
    a{{color:inherit;text-decoration:none;}}
    button,input{{font:inherit;}}
    ::selection{{background:rgba(91,110,245,.22);}}

    .layout{{display:flex;min-height:100vh;}}

    /* ── sidebar (frosted glass) ── */
    .sb{{width:var(--sw);flex-shrink:0;position:sticky;top:var(--attrib-h);
      height:calc(100vh - var(--attrib-h));overflow-y:auto;display:flex;flex-direction:column;
      background:rgba(255,255,255,.48);backdrop-filter:blur(22px) saturate(170%);
      -webkit-backdrop-filter:blur(22px) saturate(170%);border-right:1px solid rgba(255,255,255,.55);}}
    .sb-brand{{padding:24px 20px 20px;display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--hair);}}
    .sb-logo{{width:40px;height:40px;background:#fff;border-radius:11px;padding:7px;flex-shrink:0;
      display:grid;place-items:center;box-shadow:0 3px 10px rgba(31,45,75,.10);}}
    .sb-logo img{{width:100%;height:100%;object-fit:contain;display:block;}}
    .sb-name{{font-size:15px;font-weight:700;letter-spacing:.2px;color:var(--ink);}}
    .sb-sub{{font-size:11px;color:var(--muted);margin-top:3px;}}
    .sb-section{{padding:20px 22px 8px;}}
    .sb-section-label{{font-size:10px;color:var(--faint);letter-spacing:1.3px;text-transform:uppercase;font-weight:700;}}
    .sb-item{{display:flex;align-items:center;gap:11px;width:calc(100% - 16px);margin:1px 8px;border:0;
      background:transparent;color:var(--ink2);padding:11px 14px;text-align:left;cursor:pointer;
      font-size:14px;font-weight:500;border-radius:11px;position:relative;transition:all .16s;}}
    .sb-item:hover{{background:rgba(255,255,255,.55);color:var(--ink);}}
    .sb-item.active{{background:rgba(91,110,245,.12);color:var(--accent);font-weight:600;box-shadow:inset 0 0 0 1px rgba(91,110,245,.18);}}
    .sb-icon{{font-size:16px;width:20px;text-align:center;}}
    .sb-footer{{margin-top:auto;padding:16px 22px;border-top:1px solid var(--hair);font-size:11.5px;color:var(--muted);line-height:1.65;}}
    .sb-footer .made{{color:var(--ink2);font-weight:600;}}
    .sb-footer a{{color:var(--accent);}}
    .sb-footer .stat{{margin-top:8px;color:var(--faint);}}

    /* ── main ── */
    .main{{flex:1;min-width:0;display:flex;flex-direction:column;}}
    .view{{display:none;flex:1;flex-direction:column;}}
    .view.active{{display:flex;}}

    /* sticky header wrapper (section tabs + date strip move together) */
    .feed-head{{position:sticky;top:0;z-index:8;}}
    /* topbar (frosted) */
    .topbar{{display:flex;align-items:center;gap:0;flex-wrap:wrap;
      background:rgba(255,255,255,.6);backdrop-filter:blur(20px) saturate(160%);
      -webkit-backdrop-filter:blur(20px) saturate(160%);border-bottom:1px solid var(--hair);}}
    .ftabs{{display:flex;flex:1;overflow-x:auto;padding:0 32px;}}
    .ftab{{padding:16px 16px;border:0;background:transparent;color:var(--muted);cursor:pointer;
      font-size:14px;font-weight:500;border-bottom:2px solid transparent;white-space:nowrap;transition:color .14s;}}
    .ftab:hover:not(.active){{color:var(--ink);}}
    .ftab.active{{color:var(--accent);border-bottom-color:var(--accent);font-weight:600;}}
    .search-wrap{{padding:10px 24px;}}
    .search-wrap input{{border:1px solid var(--hair);background:rgba(255,255,255,.7);border-radius:11px;
      padding:9px 15px;font-size:13.5px;color:var(--ink);outline:0;width:300px;transition:all .16s;}}
    .search-wrap input::placeholder{{color:var(--faint);}}
    .search-wrap input:focus{{border-color:var(--accent);box-shadow:0 0 0 3px rgba(91,110,245,.12);background:#fff;}}

    /* date filter strip */
    .date-strip{{display:flex;align-items:center;gap:8px;
      padding:11px 20px;background:rgba(255,255,255,.5);backdrop-filter:blur(18px) saturate(160%);
      -webkit-backdrop-filter:blur(18px) saturate(160%);border-bottom:1px solid var(--hair);}}
    .ds-arrow{{flex-shrink:0;width:30px;height:30px;border-radius:9px;border:1px solid var(--hair);
      background:rgba(255,255,255,.7);color:var(--muted);cursor:pointer;display:grid;place-items:center;
      font-size:14px;transition:all .14s;}}
    .ds-arrow:hover{{color:var(--accent);border-color:var(--accent);}}
    .ds-track{{display:flex;gap:7px;overflow-x:auto;scroll-behavior:smooth;flex:1;
      scrollbar-width:none;}}
    .ds-track::-webkit-scrollbar{{display:none;}}
    .ds-chip{{flex-shrink:0;border:1px solid var(--hair);background:rgba(255,255,255,.6);color:var(--ink2);
      padding:6px 14px;border-radius:20px;font-size:13px;font-weight:500;cursor:pointer;white-space:nowrap;transition:all .14s;}}
    .ds-chip:hover{{border-color:var(--accent);color:var(--accent);}}
    .ds-chip.active{{background:var(--accent);color:#fff;border-color:var(--accent);font-weight:600;box-shadow:0 3px 10px rgba(91,110,245,.28);}}

    /* feed */
    .feed{{padding:30px 48px 64px;width:100%;}}
    /* responsive card grid: auto-fills 1/2/3/4 columns to fill the available width */
    .icard-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;}}
    @media(max-width:900px){{.icard-grid{{grid-template-columns:1fr;}}}}
    /* day group (level 1) */
    .day-block{{margin-bottom:48px;}}
    .day-hd{{display:flex;align-items:center;gap:14px;margin:0 0 8px;}}
    .day-date{{font-size:21px;font-weight:800;letter-spacing:.3px;color:var(--ink);white-space:nowrap;}}
    .day-cnt{{font-size:12.5px;color:var(--muted);font-weight:500;white-space:nowrap;}}
    .day-hd::after{{content:"";flex:1;height:2px;border-radius:2px;
      background:linear-gradient(90deg,var(--hair),transparent);}}
    /* section sub-group (level 2) */
    .subsec-hd{{display:flex;align-items:center;gap:9px;margin:22px 0 12px;}}
    .subsec-bar{{width:4px;height:17px;border-radius:3px;flex-shrink:0;}}
    .subsec-name{{font-size:15px;font-weight:700;letter-spacing:.1px;}}
    .subsec-cnt{{font-size:12px;color:var(--muted);}}

    /* item card (glass) */
    .icard{{background:var(--glass);backdrop-filter:blur(16px) saturate(150%);
      -webkit-backdrop-filter:blur(16px) saturate(150%);border:1px solid var(--glass-border);
      border-radius:18px;padding:22px 26px;margin-bottom:14px;box-shadow:var(--sh);
      transition:transform .18s,box-shadow .18s;}}
    .icard:hover{{transform:translateY(-2px);box-shadow:var(--sh-lg);}}
    .icard-top{{display:flex;align-items:center;gap:9px;margin-bottom:11px;flex-wrap:wrap;}}
    .itag{{font-size:12px;font-weight:700;padding:3px 11px;border-radius:8px;}}
    .idate{{font-size:12px;color:var(--faint);}}
    .ititle{{font-size:17.5px;font-weight:700;line-height:1.45;margin-bottom:10px;color:var(--ink);letter-spacing:.1px;}}
    .ibody{{font-size:14.5px;color:var(--ink2);line-height:1.78;margin-bottom:14px;
      display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;}}
    .imeta{{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:13px;}}
    .imetag{{font-size:12px;background:rgba(31,45,75,.06);color:var(--muted);padding:3px 10px;border-radius:8px;}}
    .imetag.bl{{background:rgba(240,160,42,.14);color:#a8680a;}}
    .ireport{{font-size:13px;color:var(--accent);font-weight:600;}}
    .ireport:hover{{text-decoration:underline;}}
    .no-results{{padding:64px 0;text-align:center;color:var(--muted);font-size:15px;}}

    /* reports view */
    .reports-hd{{padding:30px 48px 0;}}
    .reports-hd h2{{font-size:22px;font-weight:800;letter-spacing:.2px;}}
    .reports-hd p{{font-size:13.5px;color:var(--muted);margin-top:5px;}}
    .rtabs{{display:flex;gap:4px;padding:18px 48px 0;}}
    .rtab{{padding:10px 18px;border:0;background:transparent;color:var(--muted);cursor:pointer;font-size:13.5px;
      font-weight:500;border-radius:10px 10px 0 0;border-bottom:2px solid transparent;transition:color .14s;}}
    .rtab:hover:not(.active){{color:var(--ink);}}
    .rtab.active{{color:var(--accent);border-bottom-color:var(--accent);font-weight:600;}}
    .rgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px;padding:24px 48px 64px;max-width:1200px;}}
    .rcard{{background:var(--glass);backdrop-filter:blur(16px) saturate(150%);
      -webkit-backdrop-filter:blur(16px) saturate(150%);border:1px solid var(--glass-border);
      border-radius:18px;padding:20px 22px;display:flex;flex-direction:column;gap:11px;
      box-shadow:var(--sh);transition:transform .18s,box-shadow .18s;}}
    .rcard:hover{{transform:translateY(-3px);box-shadow:var(--sh-lg);}}
    .rcard-top{{display:flex;align-items:center;justify-content:space-between;}}
    .rbadge{{font-size:11.5px;font-weight:700;padding:3px 11px;border-radius:8px;}}
    .rtotal{{font-size:12px;color:var(--muted);}}
    .rdate{{font-size:17px;font-weight:800;line-height:1.3;}}
    .rpills{{display:flex;flex-wrap:wrap;gap:6px;}}
    .rlink{{font-size:12.5px;color:var(--accent);font-weight:600;}}
    .empty-msg{{color:var(--muted);font-size:14px;padding:48px 0;}}

    /* placeholder / feedback */
    .ph{{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:360px;color:var(--muted);gap:12px;padding:40px;}}
    .ph-icon{{font-size:46px;opacity:.4;}}
    .ph-text{{font-size:16px;font-weight:700;color:var(--ink2);}}
    .ph-sub{{font-size:13.5px;opacity:.85;text-align:center;max-width:380px;line-height:1.7;}}
    .fb-body{{padding:34px 48px;max-width:560px;}}
    .fb-body h2{{font-size:20px;font-weight:800;margin-bottom:12px;}}
    .fb-body p{{font-size:14.5px;color:var(--ink2);line-height:1.8;margin-bottom:22px;}}
    .fb-link{{display:inline-flex;align-items:center;gap:9px;background:var(--glass);
      backdrop-filter:blur(14px);border:1px solid var(--glass-border);border-radius:13px;
      padding:14px 22px;font-size:14.5px;font-weight:600;color:var(--accent);box-shadow:var(--sh);transition:transform .16s;}}
    .fb-link:hover{{transform:translateY(-2px);box-shadow:var(--sh-lg);}}

    @media(max-width:760px){{
      .sb{{display:none;}}
      .feed,.reports-hd,.rgrid,.fb-body{{padding-left:18px;padding-right:18px;}}
      .ftabs{{padding:0 14px;}}
      .search-wrap{{padding:10px 14px;}}
      .search-wrap input{{width:170px;}}
    }}
  </style>
</head>
<body>
<div class="layout">

<aside class="sb">
  <div class="sb-brand">
    <div class="sb-logo"><img src="{LOGO_URI}" alt=""></div>
    <div>
      <div class="sb-name">游戏行业情报站</div>
      <div class="sb-sub">AI 生成 · 每日更新</div>
    </div>
  </div>

  <div class="sb-section"><div class="sb-section-label">内容</div></div>
  <button class="sb-item active" data-view="feed"><span class="sb-icon">📡</span>行业动态</button>
  <button class="sb-item" data-view="reports"><span class="sb-icon">📋</span>日报 · 周报 · 月报</button>

  <div class="sb-section" style="margin-top:6px;"><div class="sb-section-label">其他</div></div>
  <button class="sb-item" data-view="changelog"><span class="sb-icon">📝</span>更新日志</button>
  <button class="sb-item" data-view="feedback"><span class="sb-icon">💬</span>反馈</button>

  <div class="sb-footer">
    <div class="made">Made by 沐瞳科技战略团队</div>
    <div>有问题请联系 <a href="mailto:leelootang@moonton.com">leelootang@moonton.com</a></div>
    <div class="stat">共 {total_reports} 期报告 · {total_items} 条动态</div>
  </div>
</aside>

<div class="main">

  <div class="view active" id="view-feed">
    <div class="feed-head">
      <div class="topbar">
        <div class="ftabs">{feed_tabs}</div>
        <div class="search-wrap">
          <input type="search" id="search" placeholder="搜索产品、公司、动态关键词…" autocomplete="off">
        </div>
      </div>
      <div class="date-strip">
        <button class="ds-arrow" id="ds-prev" aria-label="向前">‹</button>
        <div class="ds-track" id="ds-track"></div>
        <button class="ds-arrow" id="ds-next" aria-label="向后">›</button>
      </div>
    </div>
    <div class="feed" id="feed-content"></div>
  </div>

  <div class="view" id="view-reports">
    <div class="reports-hd">
      <h2>日报 · 周报 · 月报</h2>
      <p>点击卡片查看完整可交互报告</p>
    </div>
    <div class="rtabs">
      <button class="rtab active" data-rtype="all">全部</button>
      <button class="rtab" data-rtype="daily">日报</button>
      <button class="rtab" data-rtype="weekly">周报</button>
      <button class="rtab" data-rtype="monthly">月报</button>
    </div>
    <div class="rgrid" id="reports-grid">{all_rcards}</div>
  </div>

  <div class="view" id="view-changelog">
    <div class="ph">
      <div class="ph-icon">🗒️</div>
      <div class="ph-text">暂无更新日志</div>
      <div class="ph-sub">这里将记录网站功能和数据源的重要更新</div>
    </div>
  </div>

  <div class="view" id="view-feedback">
    <div class="fb-body">
      <h2>反馈与联系</h2>
      <p>如有内容疏漏、数据问题或功能建议，欢迎直接联系我们。</p>
      <a class="fb-link" href="mailto:leelootang@moonton.com">✉ leelootang@moonton.com</a>
    </div>
  </div>

</div>
</div>

<script>
const SECTION_ORDER = {json.dumps(list(SECTION_ORDER))};
const SECTION_LABELS = {json.dumps(SECTION_LABELS, ensure_ascii=False)};
const SECTION_COLORS = {json.dumps(SECTION_COLORS)};
const allItems = {items_json};

document.querySelectorAll('.sb-item').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.sb-item').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('view-' + btn.dataset.view).classList.add('active');
  }});
}});

let currentSec = 'all';
let currentDate = 'all';
let searchQuery = '';

// all available dates (descending)
const allDates = [...new Set(allItems.map(it => it.date))].sort((a, b) => b.localeCompare(a));

function escHtml(s) {{
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}}
function dateLabel(d) {{
  const p = String(d).split('-');
  if (p.length === 3) return `${{p[0]}} 年 ${{parseInt(p[1],10)}} 月 ${{parseInt(p[2],10)}} 日`;
  return d;
}}

function renderFeed() {{
  const q = searchQuery.trim().toLowerCase();
  const feedEl = document.getElementById('feed-content');
  const filtered = allItems.filter(it => {{
    if (currentSec !== 'all' && it.section !== currentSec) return false;
    if (currentDate !== 'all' && it.date !== currentDate) return false;
    if (!q) return true;
    return [it.title, it.body, (it.meta||[]).join(' ')].join(' ').toLowerCase().includes(q);
  }});
  if (!filtered.length) {{
    feedEl.innerHTML = '<div class="no-results">没有找到相关内容</div>';
    return;
  }}
  // Group by date (level 1, descending), then by section (level 2, fixed order).
  const dates = [];
  const byDate = {{}};
  filtered.forEach(it => {{
    if (!byDate[it.date]) {{ byDate[it.date] = []; dates.push(it.date); }}
    byDate[it.date].push(it);
  }});
  dates.sort((a, b) => b.localeCompare(a));

  const singleSection = currentSec !== 'all';
  const html = [];
  dates.forEach(date => {{
    const dayItems = byDate[date];
    html.push(`<div class="day-block">
      <div class="day-hd">
        <span class="day-date">${{dateLabel(date)}}</span>
        <span class="day-cnt">${{dayItems.length}} 条</span>
      </div>`);
    SECTION_ORDER.forEach(sid => {{
      const items = dayItems.filter(it => it.section === sid);
      if (!items.length) return;
      const color = SECTION_COLORS[sid];
      if (!singleSection) {{
        html.push(`<div class="subsec-hd">
          <span class="subsec-bar" style="background:${{color}}"></span>
          <span class="subsec-name">${{SECTION_LABELS[sid]}}</span>
          <span class="subsec-cnt">${{items.length}} 条</span>
        </div>`);
      }}
      html.push('<div class="icard-grid">');
      items.forEach(it => {{
        const tagStyle = `background:${{color}}1f;color:${{color}};`;
        const metaTags = (it.meta||[]).map(m => {{
          const bl = /borderline/i.test(m);
          return `<span class="imetag${{bl?' bl':''}}">${{escHtml(m)}}</span>`;
        }}).join('');
        html.push(`<div class="icard">
          <div class="icard-top">
            <span class="itag" style="${{tagStyle}}">${{SECTION_LABELS[it.section]}}</span>
          </div>
          <div class="ititle">${{escHtml(it.title)}}</div>
          <div class="ibody">${{escHtml(it.body)}}</div>
          ${{metaTags ? `<div class="imeta">${{metaTags}}</div>` : ''}}
          <a class="ireport" href="${{escHtml(it.reportUrl)}}">查看完整报告 →</a>
        </div>`);
      }});
      html.push('</div>');
    }});
  }});
  feedEl.innerHTML = html.join('');
}}

document.querySelectorAll('.ftab').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.ftab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentSec = btn.dataset.sec;
    renderFeed();
  }});
}});
document.getElementById('search').addEventListener('input', e => {{
  searchQuery = e.target.value;
  renderFeed();
}});

function dateChipLabel(d) {{
  const p = String(d).split('-');
  if (p.length === 3) return `${{parseInt(p[1],10)}}/${{parseInt(p[2],10)}}`;
  return d;
}}
function renderDateStrip() {{
  const track = document.getElementById('ds-track');
  const chips = [`<button class="ds-chip${{currentDate==='all'?' active':''}}" data-date="all">全部日期</button>`];
  allDates.forEach(d => {{
    chips.push(`<button class="ds-chip${{currentDate===d?' active':''}}" data-date="${{d}}">${{dateChipLabel(d)}}</button>`);
  }});
  track.innerHTML = chips.join('');
  track.querySelectorAll('.ds-chip').forEach(btn => {{
    btn.addEventListener('click', () => {{
      currentDate = btn.dataset.date;
      track.querySelectorAll('.ds-chip').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderFeed();
    }});
  }});
}}
document.getElementById('ds-prev').addEventListener('click', () => {{
  document.getElementById('ds-track').scrollBy({{ left: -240, behavior: 'smooth' }});
}});
document.getElementById('ds-next').addEventListener('click', () => {{
  document.getElementById('ds-track').scrollBy({{ left: 240, behavior: 'smooth' }});
}});
renderDateStrip();
renderFeed();

const cardSets = {{
  all: `{all_rcards}`,
  daily: `{daily_rcards}`,
  weekly: `{weekly_rcards}`,
  monthly: `{monthly_rcards}`
}};
document.querySelectorAll('.rtab').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.rtab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('reports-grid').innerHTML = cardSets[btn.dataset.rtype] || '';
  }});
}});
</script>
</body>
</html>"""


def build_docs() -> None:
    global LOGO_URI
    LOGO_URI = logo_data_uri()

    DOCS.mkdir(exist_ok=True)
    reports: list[dict] = []
    all_items: list[dict] = []

    # Daily reports feed the 行业动态 stream (weekly/monthly are digests; excluded to avoid duplication)
    for html_path in sorted((OUTPUT / "daily").glob("*/interactive_report.html"), reverse=True):
        date_str = html_path.parent.name
        report_url = f"daily/{date_str}/"
        copy_report(html_path, DOCS / "daily" / date_str)
        content = html_path.read_text(encoding="utf-8")
        total, counts = extract_metadata(content)
        items = extract_items_full(content, date_str, report_url)
        all_items.extend(items)
        reports.append({"type": "daily", "date": date_str, "url": report_url, "total": total, "counts": counts})
        print(f"  daily/{date_str}  ({total} items, {len(items)} in feed)")

    for html_path in sorted((OUTPUT / "weekly").glob("*/interactive_report.html"), reverse=True):
        folder = html_path.parent.name
        report_url = f"weekly/{folder}/"
        copy_report(html_path, DOCS / "weekly" / folder)
        total, counts = extract_metadata(html_path.read_text(encoding="utf-8"))
        reports.append({"type": "weekly", "date": folder, "url": report_url, "total": total, "counts": counts})
        print(f"  weekly/{folder}  ({total} items)")

    for html_path in sorted((OUTPUT / "monthly").glob("*/interactive_report.html"), reverse=True):
        folder = html_path.parent.name
        report_url = f"monthly/{folder}/"
        copy_report(html_path, DOCS / "monthly" / folder)
        total, counts = extract_metadata(html_path.read_text(encoding="utf-8"))
        reports.append({"type": "monthly", "date": folder, "url": report_url, "total": total, "counts": counts})
        print(f"  monthly/{folder}  ({total} items)")

    (DOCS / "index.html").write_text(build_index(reports, all_items), encoding="utf-8")
    print(f"\nDone — {len(reports)} reports, {len(all_items)} feed items → docs/index.html")


if __name__ == "__main__":
    build_docs()
