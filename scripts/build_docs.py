"""
Build docs/ for GitHub Pages.

Scans output/daily/*/interactive_report.html and output/weekly/*/interactive_report.html,
copies them to docs/ with logos, and generates an index page.
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUTPUT = ROOT / "output"
DOCS = ROOT / "docs"
SHARED_LOGO = OUTPUT / "assets" / "moonton_logo.png"

SECTION_LABELS = {
    "industry": "行业",
    "ai": "AI",
    "release": "产品",
    "discourse": "舆论",
    "deep": "深度",
}

SECTION_COLORS = {
    "industry": "#1769e0",
    "ai": "#00a6c8",
    "release": "#11a36a",
    "discourse": "#d68a00",
    "deep": "#7866d9",
}


def extract_metadata(html_content: str) -> tuple[int, dict]:
    # Find the items array (may be single-line JSON or multi-line JS object literal)
    start = html_content.find("const items = [")
    if start == -1:
        return 0, {}
    block_start = html_content.index("[", start)
    # Walk to find the matching closing bracket
    depth, i, n = 0, block_start, len(html_content)
    while i < n:
        c = html_content[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    block = html_content[block_start : i + 1]

    # Try proper JSON first (new format: quoted keys)
    try:
        items = json.loads(block)
        counts: dict[str, int] = {}
        for item in items:
            sec = item.get("section", "")
            counts[sec] = counts.get(sec, 0) + 1
        return len(items), counts
    except json.JSONDecodeError:
        pass

    # Fallback: count section occurrences for old JS object literal format
    counts = {}
    for sec_id in SECTION_LABELS:
        pattern = rf'section:\s*["\']?{sec_id}["\']?'
        counts[sec_id] = len(re.findall(pattern, block))
    total = sum(counts.values())
    return total, {k: v for k, v in counts.items() if v > 0}


def copy_report(html_path: Path, dest_dir: Path) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    content = html_path.read_text(encoding="utf-8")
    # Repoint logo to the single shared asset (two levels up from docs/daily/DATE/ or docs/weekly/DATE/)
    content = content.replace('src="moonton_logo.png"', 'src="../../assets/moonton_logo.png"')
    (dest_dir / "index.html").write_text(content, encoding="utf-8")


def format_date(date_str: str) -> str:
    parts = date_str.split("-")
    if len(parts) == 3:
        return f"{parts[0]} 年 {parts[1].lstrip('0')} 月 {parts[2].lstrip('0')} 日"
    return date_str


def section_pills(counts: dict) -> str:
    pills = []
    for sec_id in ("industry", "ai", "release", "discourse", "deep"):
        n = counts.get(sec_id, 0)
        if n == 0:
            continue
        color = SECTION_COLORS[sec_id]
        label = SECTION_LABELS[sec_id]
        pills.append(
            f'<span style="background:{color}18;color:{color};border:1px solid {color}40;'
            f'padding:2px 8px;border-radius:10px;font-size:12px;white-space:nowrap;">'
            f"{label} {n}</span>"
        )
    return " ".join(pills)


def build_index(reports: list[dict]) -> str:
    daily = [r for r in reports if r["type"] == "daily"]
    weekly = [r for r in reports if r["type"] == "weekly"]

    def card(r: dict) -> str:
        date_display = format_date(r["date"])
        if r["type"] == "weekly":
            parts = r["date"].split("_to_")
            date_display = f"{format_date(parts[0])} — {format_date(parts[1])}" if len(parts) == 2 else r["date"]
        badge_color = "#1769e0" if r["type"] == "daily" else "#7866d9"
        badge_label = "日报" if r["type"] == "daily" else "周报"
        pills = section_pills(r["counts"])
        return f"""
        <a href="{r['url']}" class="card">
          <div class="card-top">
            <span class="badge" style="background:{badge_color}18;color:{badge_color};border:1px solid {badge_color}40;">{badge_label}</span>
            <span class="total">{r['total']} 条</span>
          </div>
          <div class="card-date">{date_display}</div>
          <div class="pills">{pills}</div>
          <div class="card-link">查看报告 →</div>
        </a>"""

    daily_html = "\n".join(card(r) for r in daily) if daily else '<p class="empty">暂无日报</p>'
    weekly_html = "\n".join(card(r) for r in weekly) if weekly else '<p class="empty">暂无周报</p>'
    total_count = len(reports)

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>游戏行业情报站</title>
  <style>
    :root {{
      --bg:#f4f6fb; --panel:#fff; --ink:#15202e; --muted:#5b6b82;
      --line:#e3e8f1; --shadow:0 4px 16px rgba(24,39,75,.07);
    }}
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ background:var(--bg); color:var(--ink); font-family:"PingFang SC","Microsoft YaHei","Segoe UI",Arial,sans-serif; line-height:1.6; -webkit-font-smoothing:antialiased; }}
    header {{ background:linear-gradient(135deg,#1f2a3d 0%,#283449 100%); color:#eef5ff; padding:40px 48px 36px; }}
    .brand {{ display:flex; align-items:center; gap:14px; margin-bottom:16px; }}
    .brand-logo {{ width:44px; height:44px; background:#fff; border-radius:8px; padding:8px; display:grid; place-items:center; }}
    .brand-logo img {{ width:100%; height:100%; object-fit:contain; }}
    .brand-title {{ font-size:22px; font-weight:700; letter-spacing:.5px; }}
    .brand-sub {{ font-size:13px; color:#9fb4d2; margin-top:3px; }}
    .header-meta {{ font-size:13px; color:#7a93b8; }}
    nav.tabs {{ display:flex; gap:8px; padding:24px 48px 0; border-bottom:1px solid var(--line); background:#fff; position:sticky; top:0; z-index:10; }}
    nav.tabs button {{ padding:10px 20px; border:0; background:transparent; color:var(--muted); cursor:pointer; font-size:14px; font-weight:500; border-bottom:2px solid transparent; margin-bottom:-1px; transition:color .15s; }}
    nav.tabs button.active {{ color:#1769e0; border-bottom-color:#1769e0; }}
    nav.tabs button:hover:not(.active) {{ color:var(--ink); }}
    .container {{ max-width:1100px; margin:0 auto; padding:32px 48px 64px; }}
    .section {{ display:none; }}
    .section.visible {{ display:block; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:16px; margin-top:20px; }}
    .section-title {{ font-size:15px; font-weight:600; color:var(--muted); letter-spacing:.5px; text-transform:uppercase; margin-bottom:4px; }}
    a.card {{ display:flex; flex-direction:column; gap:10px; background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:20px; text-decoration:none; color:inherit; box-shadow:var(--shadow); transition:transform .15s, box-shadow .15s; }}
    a.card:hover {{ transform:translateY(-2px); box-shadow:0 8px 28px rgba(24,39,75,.11); }}
    .card-top {{ display:flex; align-items:center; justify-content:space-between; }}
    .badge {{ padding:3px 10px; border-radius:10px; font-size:12px; font-weight:600; }}
    .total {{ font-size:12px; color:var(--muted); }}
    .card-date {{ font-size:17px; font-weight:600; line-height:1.3; }}
    .pills {{ display:flex; flex-wrap:wrap; gap:6px; }}
    .card-link {{ font-size:13px; color:#1769e0; margin-top:4px; }}
    .empty {{ color:var(--muted); font-size:14px; padding:32px 0; }}
    @media(max-width:640px) {{ header,.container,nav.tabs {{ padding-left:20px; padding-right:20px; }} }}
  </style>
</head>
<body>
<header>
  <div class="brand">
    <div class="brand-logo"><img src="assets/moonton_logo.png" alt=""></div>
    <div>
      <div class="brand-title">游戏行业情报站</div>
      <div class="brand-sub">AI 生成 · 每日更新</div>
    </div>
  </div>
  <div class="header-meta">共 {total_count} 期报告 · 含日报 {len(daily)} 期、周报 {len(weekly)} 期</div>
</header>

<nav class="tabs">
  <button class="active" onclick="showTab('all', this)">全部</button>
  <button onclick="showTab('daily', this)">日报</button>
  <button onclick="showTab('weekly', this)">周报</button>
</nav>

<div class="container">
  <div id="tab-all" class="section visible">
    <div class="section-title">全部报告</div>
    <div class="grid">{"".join(card(r) for r in reports)}</div>
  </div>
  <div id="tab-daily" class="section">
    <div class="section-title">日报</div>
    <div class="grid">{daily_html}</div>
  </div>
  <div id="tab-weekly" class="section">
    <div class="section-title">周报</div>
    <div class="grid">{weekly_html}</div>
  </div>
</div>

<script>
  function showTab(id, btn) {{
    document.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
    document.querySelectorAll('nav.tabs button').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + id).classList.add('visible');
    btn.classList.add('active');
  }}
</script>
</body>
</html>"""


def build_docs() -> None:
    DOCS.mkdir(exist_ok=True)
    assets_dir = DOCS / "assets"
    assets_dir.mkdir(exist_ok=True)
    logo_src = SHARED_LOGO if SHARED_LOGO.exists() else next(OUTPUT.glob("daily/*/moonton_logo.png"), None)
    if logo_src:
        shutil.copy2(logo_src, assets_dir / "moonton_logo.png")

    reports: list[dict] = []

    for html_path in sorted((OUTPUT / "daily").glob("*/interactive_report.html"), reverse=True):
        date_str = html_path.parent.name
        dest_dir = DOCS / "daily" / date_str
        copy_report(html_path, dest_dir)
        content = html_path.read_text(encoding="utf-8")
        total, counts = extract_metadata(content)
        reports.append({"type": "daily", "date": date_str, "url": f"daily/{date_str}/", "total": total, "counts": counts})
        print(f"  daily/{date_str}  ({total} items)")

    for html_path in sorted((OUTPUT / "weekly").glob("*/interactive_report.html"), reverse=True):
        folder = html_path.parent.name
        dest_dir = DOCS / "weekly" / folder
        copy_report(html_path, dest_dir)
        content = html_path.read_text(encoding="utf-8")
        total, counts = extract_metadata(content)
        reports.append({"type": "weekly", "date": folder, "url": f"weekly/{folder}/", "total": total, "counts": counts})
        print(f"  weekly/{folder}  ({total} items)")

    index_html = build_index(reports)
    (DOCS / "index.html").write_text(index_html, encoding="utf-8")
    print(f"\nDone — {len(reports)} reports → docs/index.html")


if __name__ == "__main__":
    build_docs()
