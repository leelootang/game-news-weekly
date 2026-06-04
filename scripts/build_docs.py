"""
Build docs/ for GitHub Pages.

Scans output/daily/*/interactive_report.html and output/weekly/*/interactive_report.html,
copies them to docs/ with logos, and generates a portal index page.
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

SECTION_COLORS = {
    "industry": "#1769e0",
    "ai":       "#00a6c8",
    "release":  "#11a36a",
    "discourse":"#d68a00",
    "deep":     "#7866d9",
}


# ── helpers ──────────────────────────────────────────────────────────────────

def logo_data_uri() -> str:
    logo = SHARED_LOGO if SHARED_LOGO.exists() else next(OUTPUT.glob("daily/*/moonton_logo.png"), None)
    if not logo:
        return ""
    return f"data:image/png;base64,{base64.b64encode(logo.read_bytes()).decode()}"


LOGO_URI = ""  # set in build_docs()

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
    """Return all items from a report HTML (new JSON format only)."""
    block = _find_items_block(html)
    if not block:
        return []
    try:
        items = json.loads(block)
    except json.JSONDecodeError:
        return []
    for item in items:
        item["date"] = date_str
        item["reportUrl"] = report_url
    return items


def extract_metadata(html: str) -> tuple[int, dict]:
    """Return (total_count, {section: count}) for any format."""
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
    total = sum(counts.values())
    return total, {k: v for k, v in counts.items() if v > 0}


# ── per-report page ───────────────────────────────────────────────────────────

def copy_report(html_path: Path, dest_dir: Path) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    content = html_path.read_text(encoding="utf-8")
    if LOGO_URI:
        content = content.replace('src="moonton_logo.png"', f'src="{LOGO_URI}"')
    content = content.replace("<body>", f"<body>{ATTRIBUTION_BAR}", 1)
    (dest_dir / "index.html").write_text(content, encoding="utf-8")


# ── index page ────────────────────────────────────────────────────────────────

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
            f'<span style="background:{c}18;color:{c};border:1px solid {c}33;'
            f'padding:2px 8px;border-radius:8px;font-size:11px;">'
            f'{SECTION_LABELS[sid]} {n}</span>'
        )
    return " ".join(out)


def build_index(reports: list[dict], all_items: list[dict]) -> str:
    daily   = [r for r in reports if r["type"] == "daily"]
    weekly  = [r for r in reports if r["type"] == "weekly"]
    monthly = [r for r in reports if r["type"] == "monthly"]

    total_items = len(all_items)
    total_reports = len(reports)

    # ── embed data as JSON for client-side JS ─────────────────────────────────
    items_json = json.dumps(all_items, ensure_ascii=False)
    reports_json = json.dumps(reports, ensure_ascii=False)

    # ── report cards (日报/周报 tab) ──────────────────────────────────────────
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
        type_colors = {"daily": "#1769e0", "weekly": "#7866d9", "monthly": "#11a36a"}
        bc = type_colors.get(r["type"], "#1769e0")
        bl = type_labels.get(r["type"], "报告")
        pills = section_pills_html(r["counts"])
        return (
            f'<a href="{r["url"]}" class="rcard">'
            f'<div class="rcard-top">'
            f'<span class="rbadge" style="background:{bc}18;color:{bc};border:1px solid {bc}33;">{bl}</span>'
            f'<span class="rtotal">{r["total"]} 条</span>'
            f'</div>'
            f'<div class="rdate">{date_label}</div>'
            f'<div class="rpills">{pills}</div>'
            f'<div class="rlink">查看完整报告 →</div>'
            f'</a>'
        )

    all_rcards   = "\n".join(report_card(r) for r in reports) if reports else '<p class="empty-msg">暂无报告</p>'
    daily_rcards = "\n".join(report_card(r) for r in daily)   if daily   else '<p class="empty-msg">暂无日报</p>'
    weekly_rcards= "\n".join(report_card(r) for r in weekly)  if weekly  else '<p class="empty-msg">暂无周报</p>'
    monthly_rcards="\n".join(report_card(r) for r in monthly) if monthly else '<p class="empty-msg">暂无月报</p>'

    # ── filter tab list for feed ──────────────────────────────────────────────
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
      --bg:#f4f6fb; --panel:#fff; --ink:#15202e; --ink2:#2a3a52; --muted:#5b6b82;
      --line:#e3e8f1; --sh:0 4px 16px rgba(24,39,75,.07); --sh2:0 8px 28px rgba(24,39,75,.11);
      --sw:248px;
    }}
    *{{box-sizing:border-box;margin:0;padding:0;}}
    body{{background:var(--bg);color:var(--ink);font-family:"PingFang SC","Microsoft YaHei","Segoe UI",Arial,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;}}
    a{{color:inherit;text-decoration:none;}}
    button,input{{font:inherit;}}

    /* ── layout ── */
    .layout{{display:flex;min-height:calc(100vh - 34px);}}

    /* ── sidebar ── */
    .sb{{width:var(--sw);flex-shrink:0;background:linear-gradient(180deg,#283449 0%,#1f2a3d 100%);
         color:#eef5ff;position:sticky;top:34px;height:calc(100vh - 34px);overflow-y:auto;
         display:flex;flex-direction:column;border-right:1px solid rgba(255,255,255,.06);}}
    .sb-brand{{padding:22px 18px 18px;border-bottom:1px solid rgba(255,255,255,.08);display:flex;align-items:center;gap:11px;}}
    .sb-logo{{width:36px;height:36px;background:#fff;border-radius:7px;padding:6px;flex-shrink:0;display:grid;place-items:center;}}
    .sb-logo img{{width:100%;height:100%;object-fit:contain;display:block;}}
    .sb-name{{font-size:14.5px;font-weight:700;letter-spacing:.3px;}}
    .sb-sub{{font-size:11px;color:#9fb4d2;margin-top:2px;}}

    .sb-section{{padding:18px 18px 6px;}}
    .sb-section-label{{font-size:10px;color:#4a6480;letter-spacing:1.1px;text-transform:uppercase;font-weight:700;}}
    .sb-item{{display:flex;align-items:center;gap:9px;width:100%;border:0;background:transparent;color:#b8cde6;
              padding:9px 18px;text-align:left;cursor:pointer;font-size:13.5px;position:relative;transition:background .12s,color .12s;}}
    .sb-item:hover{{background:rgba(255,255,255,.05);color:#fff;}}
    .sb-item.active{{background:rgba(255,255,255,.08);color:#fff;}}
    .sb-item.active::before{{content:"";position:absolute;left:0;top:5px;bottom:5px;width:3px;border-radius:0 3px 3px 0;background:#56a8ff;}}
    .sb-icon{{font-size:15px;width:19px;text-align:center;opacity:.8;}}
    .sb-footer{{margin-top:auto;padding:14px 18px;border-top:1px solid rgba(255,255,255,.06);
                font-size:11px;color:#3d5570;line-height:1.5;}}

    /* ── main ── */
    .main{{flex:1;min-width:0;display:flex;flex-direction:column;}}
    .view{{display:none;flex:1;flex-direction:column;}}
    .view.active{{display:flex;}}

    /* topbar (feed) */
    .topbar{{position:sticky;top:34px;z-index:9;background:var(--panel);border-bottom:1px solid var(--line);
             display:flex;align-items:stretch;gap:0;flex-wrap:wrap;}}
    .ftabs{{display:flex;flex:1;overflow-x:auto;padding:0 24px;gap:0;}}
    .ftab{{padding:13px 14px;border:0;background:transparent;color:var(--muted);cursor:pointer;
           font-size:13px;font-weight:500;border-bottom:2px solid transparent;white-space:nowrap;transition:color .12s;}}
    .ftab:hover:not(.active){{color:var(--ink);}}
    .ftab.active{{color:#1769e0;border-bottom-color:#1769e0;}}
    .search-wrap{{display:flex;align-items:center;gap:7px;padding:8px 16px;border-left:1px solid var(--line);}}
    .search-wrap input{{border:1px solid var(--line);background:var(--bg);border-radius:7px;
                        padding:7px 12px;font-size:13px;color:var(--ink);outline:0;width:200px;transition:border-color .15s;}}
    .search-wrap input:focus{{border-color:#1769e0;}}

    /* feed content */
    .feed{{padding:24px 32px 56px;max-width:860px;}}
    .sec-block{{margin-bottom:36px;}}
    .sec-hd{{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid var(--line);}}
    .sec-dot{{width:9px;height:9px;border-radius:50%;flex-shrink:0;}}
    .sec-name{{font-size:15px;font-weight:700;}}
    .sec-cnt{{font-size:12px;color:var(--muted);}}
    .no-results{{padding:48px 0;text-align:center;color:var(--muted);font-size:14px;}}

    /* item card */
    .icard{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:17px 20px;
            margin-bottom:10px;transition:box-shadow .15s;}}
    .icard:hover{{box-shadow:var(--sh);}}
    .icard-top{{display:flex;align-items:center;gap:8px;margin-bottom:9px;flex-wrap:wrap;}}
    .itag{{font-size:11px;font-weight:600;padding:2px 8px;border-radius:6px;}}
    .idate{{font-size:11.5px;color:var(--muted);}}
    .ititle{{font-size:14.5px;font-weight:700;line-height:1.45;margin-bottom:8px;color:var(--ink);}}
    .ibody{{font-size:13px;color:var(--ink2);line-height:1.7;margin-bottom:10px;
            display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;}}
    .imeta{{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px;}}
    .imetag{{font-size:11px;background:#f0f4fa;color:var(--muted);padding:2px 8px;border-radius:6px;}}
    .imetag.bl{{background:#fff3dc;color:#945e00;}}
    .ireport{{font-size:12px;color:#1769e0;}}

    /* report cards */
    .reports-hd{{padding:24px 32px 0;}}
    .reports-hd h2{{font-size:19px;font-weight:700;}}
    .reports-hd p{{font-size:13px;color:var(--muted);margin-top:4px;}}
    .rtabs{{display:flex;gap:4px;padding:16px 32px 0;border-bottom:1px solid var(--line);background:var(--panel);}}
    .rtab{{padding:9px 16px;border:0;background:transparent;color:var(--muted);cursor:pointer;font-size:13px;
           font-weight:500;border-bottom:2px solid transparent;transition:color .12s;}}
    .rtab:hover:not(.active){{color:var(--ink);}}
    .rtab.active{{color:#1769e0;border-bottom-color:#1769e0;}}
    .rgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:13px;padding:22px 32px 56px;}}
    .rcard{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:17px 19px;
            display:flex;flex-direction:column;gap:9px;box-shadow:0 1px 3px rgba(24,39,75,.04);transition:transform .12s,box-shadow .12s;}}
    .rcard:hover{{transform:translateY(-2px);box-shadow:var(--sh2);}}
    .rcard-top{{display:flex;align-items:center;justify-content:space-between;}}
    .rbadge{{font-size:11px;font-weight:700;padding:2px 9px;border-radius:7px;}}
    .rtotal{{font-size:12px;color:var(--muted);}}
    .rdate{{font-size:15.5px;font-weight:700;line-height:1.3;}}
    .rpills{{display:flex;flex-wrap:wrap;gap:5px;}}
    .rlink{{font-size:12px;color:#1769e0;}}
    .empty-msg{{color:var(--muted);font-size:14px;padding:40px 0;}}

    /* placeholder views */
    .ph{{display:flex;flex-direction:column;align-items:center;justify-content:center;
         min-height:320px;color:var(--muted);gap:10px;padding:40px;}}
    .ph-icon{{font-size:42px;opacity:.35;}}
    .ph-text{{font-size:15px;font-weight:600;}}
    .ph-sub{{font-size:13px;opacity:.75;text-align:center;max-width:360px;line-height:1.6;}}

    /* feedback */
    .fb-body{{padding:28px 32px;max-width:520px;}}
    .fb-body h2{{font-size:18px;font-weight:700;margin-bottom:10px;}}
    .fb-body p{{font-size:14px;color:var(--ink2);line-height:1.75;margin-bottom:20px;}}
    .fb-link{{display:inline-flex;align-items:center;gap:8px;background:var(--panel);border:1px solid var(--line);
              border-radius:8px;padding:12px 18px;font-size:14px;font-weight:500;color:#1769e0;transition:background .12s;}}
    .fb-link:hover{{background:#eaf2ff;}}

    @media(max-width:700px){{
      .sb{{display:none;}}
      .feed,.reports-hd,.rgrid,.fb-body{{padding-left:16px;padding-right:16px;}}
      .ftabs{{padding:0 12px;}}
      .search-wrap input{{width:140px;}}
    }}
  </style>
</head>
<body>
{ATTRIBUTION_BAR}
<div class="layout">

<!-- ── sidebar ─────────────────────────────────────────────────────── -->
<aside class="sb">
  <div class="sb-brand">
    <div class="sb-logo"><img src="{LOGO_URI}" alt=""></div>
    <div>
      <div class="sb-name">游戏行业情报站</div>
      <div class="sb-sub">AI 生成 · 每日更新</div>
    </div>
  </div>

  <div class="sb-section"><div class="sb-section-label">内容</div></div>
  <button class="sb-item active" data-view="feed">
    <span class="sb-icon">📡</span>行业动态
  </button>
  <button class="sb-item" data-view="reports">
    <span class="sb-icon">📋</span>日报 · 周报 · 月报
  </button>

  <div class="sb-section" style="margin-top:8px;"><div class="sb-section-label">其他</div></div>
  <button class="sb-item" data-view="changelog">
    <span class="sb-icon">📝</span>更新日志
  </button>
  <button class="sb-item" data-view="feedback">
    <span class="sb-icon">💬</span>反馈
  </button>

  <div class="sb-footer">共 {total_reports} 期报告 · {total_items} 条动态</div>
</aside>

<!-- ── main ─────────────────────────────────────────────────────────── -->
<div class="main">

  <!-- 行业动态 -->
  <div class="view active" id="view-feed">
    <div class="topbar">
      <div class="ftabs">{feed_tabs}</div>
      <div class="search-wrap">
        <input type="search" id="search" placeholder="搜索动态…" autocomplete="off">
      </div>
    </div>
    <div class="feed" id="feed-content"></div>
  </div>

  <!-- 日报 · 周报 · 月报 -->
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

  <!-- 更新日志 -->
  <div class="view" id="view-changelog">
    <div class="ph">
      <div class="ph-icon">🗒️</div>
      <div class="ph-text">暂无更新日志</div>
      <div class="ph-sub">这里将记录网站功能和数据源的重要更新</div>
    </div>
  </div>

  <!-- 反馈 -->
  <div class="view" id="view-feedback">
    <div class="fb-body">
      <h2>反馈与联系</h2>
      <p>如有内容疏漏、数据问题或功能建议，欢迎直接联系我们。</p>
      <a class="fb-link" href="mailto:leelootang@moonton.com">✉ leelootang@moonton.com</a>
    </div>
  </div>

</div><!-- .main -->
</div><!-- .layout -->

<script>
const SECTION_ORDER = {json.dumps(list(SECTION_ORDER))};
const SECTION_LABELS = {json.dumps(SECTION_LABELS, ensure_ascii=False)};
const SECTION_COLORS = {json.dumps(SECTION_COLORS)};
const allItems = {items_json};
const allReports = {reports_json};

// ── sidebar navigation ─────────────────────────────────────────────────
document.querySelectorAll('.sb-item').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.sb-item').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('view-' + btn.dataset.view).classList.add('active');
  }});
}});

// ── feed rendering ─────────────────────────────────────────────────────
let currentSec = 'all';
let searchQuery = '';

function escHtml(s) {{
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}}

function renderFeed() {{
  const q = searchQuery.trim().toLowerCase();
  const feedEl = document.getElementById('feed-content');
  const filtered = allItems.filter(it => {{
    if (currentSec !== 'all' && it.section !== currentSec) return false;
    if (!q) return true;
    const txt = [it.title, it.body, (it.meta||[]).join(' ')].join(' ').toLowerCase();
    return txt.includes(q);
  }});

  if (!filtered.length) {{
    feedEl.innerHTML = '<div class="no-results">没有找到相关内容</div>';
    return;
  }}

  // Group by section (keep SECTION_ORDER), within each section: date desc (already sorted from build)
  const html = [];
  const sections = currentSec === 'all' ? SECTION_ORDER : [currentSec];
  sections.forEach(sid => {{
    const items = filtered.filter(it => it.section === sid);
    if (!items.length) return;
    const color = SECTION_COLORS[sid];
    html.push(`<div class="sec-block">
      <div class="sec-hd">
        <span class="sec-dot" style="background:${{color}}"></span>
        <span class="sec-name">${{SECTION_LABELS[sid]}}</span>
        <span class="sec-cnt">${{items.length}} 条</span>
      </div>`);
    items.forEach(it => {{
      const tagStyle = `background:${{color}}18;color:${{color}};border:1px solid ${{color}}33;`;
      const metaTags = (it.meta||[]).map(m => {{
        const isBl = /borderline/i.test(m);
        return `<span class="imetag${{isBl?' bl':''}}">${{escHtml(m)}}</span>`;
      }}).join('');
      html.push(`<div class="icard">
        <div class="icard-top">
          <span class="itag" style="${{tagStyle}}">${{SECTION_LABELS[it.section]}}</span>
          <span class="idate">${{escHtml(it.date)}}</span>
        </div>
        <div class="ititle">${{escHtml(it.title)}}</div>
        <div class="ibody">${{escHtml(it.body)}}</div>
        ${{metaTags ? `<div class="imeta">${{metaTags}}</div>` : ''}}
        <a class="ireport" href="${{escHtml(it.reportUrl)}}">查看完整报告 →</a>
      </div>`);
    }});
    html.push('</div>');
  }});
  feedEl.innerHTML = html.join('');
}}

// section filter tabs
document.querySelectorAll('.ftab').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.ftab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentSec = btn.dataset.sec;
    renderFeed();
  }});
}});

// search
document.getElementById('search').addEventListener('input', e => {{
  searchQuery = e.target.value;
  renderFeed();
}});

renderFeed();

// ── reports tab filter ─────────────────────────────────────────────────
const dailyCards   = `{daily_rcards}`;
const weeklyCards  = `{weekly_rcards}`;
const monthlyCards = `{monthly_rcards}`;
const allCards     = `{all_rcards}`;

document.querySelectorAll('.rtab').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.rtab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const grid = document.getElementById('reports-grid');
    const t = btn.dataset.rtype;
    if (t === 'all')     grid.innerHTML = allCards;
    else if (t === 'daily')  grid.innerHTML = dailyCards;
    else if (t === 'weekly') grid.innerHTML = weeklyCards;
    else if (t === 'monthly') grid.innerHTML = monthlyCards;
  }});
}});
</script>
</body>
</html>"""


# ── main ──────────────────────────────────────────────────────────────────────

def build_docs() -> None:
    global LOGO_URI
    LOGO_URI = logo_data_uri()

    DOCS.mkdir(exist_ok=True)
    reports: list[dict] = []
    all_items: list[dict] = []

    for html_path in sorted((OUTPUT / "daily").glob("*/interactive_report.html"), reverse=True):
        date_str = html_path.parent.name
        report_url = f"daily/{date_str}/"
        dest_dir = DOCS / "daily" / date_str
        copy_report(html_path, dest_dir)
        content = html_path.read_text(encoding="utf-8")
        total, counts = extract_metadata(content)
        items = extract_items_full(content, date_str, report_url)
        all_items.extend(items)
        reports.append({"type": "daily", "date": date_str, "url": report_url, "total": total, "counts": counts})
        print(f"  daily/{date_str}  ({total} items, {len(items)} in feed)")

    for html_path in sorted((OUTPUT / "weekly").glob("*/interactive_report.html"), reverse=True):
        folder = html_path.parent.name
        report_url = f"weekly/{folder}/"
        dest_dir = DOCS / "weekly" / folder
        copy_report(html_path, dest_dir)
        content = html_path.read_text(encoding="utf-8")
        total, counts = extract_metadata(content)
        items = extract_items_full(content, folder, report_url)
        all_items.extend(items)
        reports.append({"type": "weekly", "date": folder, "url": report_url, "total": total, "counts": counts})
        print(f"  weekly/{folder}  ({total} items)")

    for html_path in sorted((OUTPUT / "monthly").glob("*/interactive_report.html"), reverse=True):
        folder = html_path.parent.name
        report_url = f"monthly/{folder}/"
        dest_dir = DOCS / "monthly" / folder
        copy_report(html_path, dest_dir)
        content = html_path.read_text(encoding="utf-8")
        total, counts = extract_metadata(content)
        items = extract_items_full(content, folder, report_url)
        all_items.extend(items)
        reports.append({"type": "monthly", "date": folder, "url": report_url, "total": total, "counts": counts})
        print(f"  monthly/{folder}  ({total} items)")

    index_html = build_index(reports, all_items)
    (DOCS / "index.html").write_text(index_html, encoding="utf-8")
    print(f"\nDone — {len(reports)} reports, {len(all_items)} feed items → docs/index.html")


if __name__ == "__main__":
    build_docs()
