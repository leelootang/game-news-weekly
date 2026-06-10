#!/usr/bin/env python3
"""Deterministically build the interactive report webpage from a report markdown.

Parses a final report markdown (game_industry_<kind>_*.md) plus its sibling
sources_used.md into the self-rendering report template (scripts/report_template.html),
producing game_industry_<kind>_*.html that matches the current site template:
section nav (steam/industry/ai/release/discourse/deep), search, density toggle,
source drawer, and the steam ranking table with week-over-week delta + highlight rows.

Usage:
    python scripts/build_report_html.py <path/to/game_industry_<kind>_*.md>

The HTML is written next to the markdown. No AI/network needed; the markdown is the
single source of truth (including which steam rows are highlighted via **bold** and
the weekly 较上周 column), so the page always matches the report.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "report_template.html"

SECTION_DESCS = {
    "rankings": {"daily": "Steam 全球热销榜 TOP10 与近期新品。",
                 "weekly": "Steam 官方周销量榜 TOP15 与本周新上榜。",
                 "monthly": "Steam 月度热销榜与本月新上榜。"},
    "industry": "公司、产品、市场与资本动作。",
    "ai": "游戏相关的 AI 与开发工具。",
    "release": "上线、测试、新版本与重点节点。",
    "discourse": "社区热点、争议与玩家情绪。",
    "deep": "值得内部团队继续跟踪的结构性变化。",
}
RANK_LABEL = {"daily": "steam当日榜单", "weekly": "steam周榜", "monthly": "steam月榜"}
KIND_CN = {"daily": "日报", "weekly": "周报", "monthly": "月报"}
BRAND_SUB = {"daily": "AI 生成 · 每日更新", "weekly": "AI 生成 · 每周更新", "monthly": "AI 生成 · 每月更新"}


def heading_to_section(text: str) -> str | None:
    if "steam" in text.lower():
        return "rankings"
    if "行业新闻" in text:
        return "industry"
    if "AI" in text:
        return "ai"
    if "新游发布" in text or "产品日历" in text:
        return "release"
    if "玩家舆论" in text or "社区动态" in text:
        return "discourse"
    if "行业精选" in text or "深度观察" in text:
        return "deep"
    return None


def md_inline(text: str) -> str:
    text = (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def parse_meta(md_path: Path):
    name = md_path.name
    m = re.match(r"game_industry_(daily)_(\d{4}-\d{2}-\d{2})\.md$", name)
    if m:
        d = m.group(2)
        return "daily", d, d, f"{d}", f"游戏行业日报 | {d}"
    m = re.match(r"game_industry_(weekly)_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})\.md$", name)
    if m:
        s, e = m.group(2), m.group(3)
        return "weekly", s, e, f"{s} ~ {e}", f"游戏行业周报 | {s} ~ {e}"
    m = re.match(r"game_industry_(monthly)_(\d{4}-\d{2})\.md$", name)
    if m:
        mo = m.group(2)
        return "monthly", mo, mo, mo, f"游戏行业月报 | {mo}"
    raise SystemExit(f"unrecognized report filename: {name}")


def parse_sources(sources_md: str):
    """Return (title->ids, id->(name,url))."""
    title_ids: dict[str, list[str]] = {}
    id_meta: dict[str, tuple[str, str]] = {}
    in_map = False
    in_details = False
    for line in sources_md.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_map = ("Item Source Map" in s or "条目来源映射" in s)
            in_details = ("Source Details" in s or "来源明细" in s)
            continue
        if in_map and s and not s.startswith("#"):
            m = re.match(r"^(?:[-*]\s*|\d+\.\s*)?(?P<title>.+?)\s*(?:——|—|-)\s*(?P<rest>(?:S\d{3,4}|steamdb_rankings)\b.*)$", s)
            if m:
                title = m.group("title").strip().strip("`")
                ids = re.findall(r"S\d{3,4}|steamdb_rankings[\w-]*", m.group("rest"))
                if title and ids:
                    title_ids[title] = ids
        if in_details and s.startswith("- S"):
            parts = [p.strip() for p in s[1:].split("|")]
            if len(parts) >= 2:
                sid = parts[0].strip()
                url = ""
                for p in reversed(parts):
                    if re.match(r"https?://", p):
                        url = p
                        break
                name = parts[-2] if url and len(parts) >= 3 else (parts[1] if len(parts) > 1 else sid)
                id_meta[sid] = (name, url)
    return title_ids, id_meta


def sources_for(title: str, title_ids, id_meta):
    ids = title_ids.get(title)
    if not ids:
        # try a relaxed match (ignore trailing punctuation / quotes)
        for k, v in title_ids.items():
            if k.replace("·", "").replace("：", ":") == title.replace("·", "").replace("：", ":"):
                ids = v
                break
    out = []
    for sid in ids or []:
        name, url = id_meta.get(sid, (sid, ""))
        out.append([sid, name, url])
    return out


def build_rank_body_html(lines: list[str]) -> str:
    """Build the steam body_html (note + bullets + rank-table) from md lines of the section."""
    note_parts, bullets, table_lines = [], [], []
    for ln in lines:
        s = ln.rstrip()
        if s.startswith(">"):
            note_parts.append(md_inline(s.lstrip("> ").strip()))
        elif s.startswith("- "):
            bullets.append(md_inline(s[2:].strip()))
        elif s.startswith("|"):
            table_lines.append(s)
    html = []
    if note_parts:
        html.append('<p style="color:var(--muted);font-size:13px;margin-bottom:10px;">' + " ".join(note_parts) + "</p>")
    if bullets:
        html.append('<ul style="margin:0 0 14px 18px;display:grid;gap:7px;">' + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>")
    if table_lines:
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table_lines]
        header = rows[0]
        body_rows = [r for r in rows[2:]] if len(rows) > 2 else []
        name_idx = next((i for i, h in enumerate(header) if h.lower() == "name"), 2)
        right_cols = {i for i, h in enumerate(header) if h in ("销量", "营收", "Sales", "Revenue")}
        def th(i, h):
            align = "left" if i == name_idx else ("right" if i in right_cols else "center")
            return f'<th style="text-align:{align}">{md_inline(h)}</th>' if align != "center" else f"<th>{md_inline(h)}</th>"
        thead = "<tr>" + "".join(th(i, h) for i, h in enumerate(header)) + "</tr>"
        trs = []
        for r in body_rows:
            hl = any("**" in c for c in r)
            tds = []
            for i, c in enumerate(r):
                cell = c
                strong = "**" in cell
                cell_html = md_inline(cell)
                # marker / delta chips
                if cell.strip() in ("★ 近期新品", "★ 新上榜") or cell.strip() == "新":
                    cell_html = f'<span class="new-tag">{cell.strip()}</span>'
                align = "left" if i == name_idx else ("right" if i in right_cols else "center")
                style = f' style="text-align:{align}"' if align != "center" else ""
                tds.append(f"<td{style}>{cell_html}</td>")
            cls = ' class="hl"' if hl else ""
            trs.append(f"<tr{cls}>" + "".join(tds) + "</tr>")
        html.append('<div style="overflow-x:auto;"><table class="rank-table"><thead>' + thead +
                    "</thead><tbody>" + "".join(trs) + "</tbody></table></div>")
    return "".join(html)


def parse_report(md: str, kind: str, title_ids, id_meta):
    items = []
    # split into sections by '## '
    chunks = re.split(r"(?m)^##\s+", md)
    for chunk in chunks[1:]:
        head, _, rest = chunk.partition("\n")
        sec = heading_to_section(head.strip())
        if not sec:
            continue
        if sec == "rankings":
            lines = rest.splitlines()
            # drop a leading '### N. title' line, keep its text as item title
            title = RANK_LABEL.get(kind, "steam榜单")
            content = []
            for ln in lines:
                m = re.match(r"^###\s+\d+\.\s+(.+)$", ln)
                if m:
                    title = m.group(1).strip()
                    continue
                content.append(ln)
            body_html = build_rank_body_html(content)
            srcs = sources_for(title, title_ids, id_meta)
            if not srcs:
                # fall back: any steam map line
                for k, v in title_ids.items():
                    if "steam" in k.lower():
                        srcs = [[i, *id_meta.get(i, ("Steam 官方榜单", "https://store.steampowered.com/charts/topselling/global"))] for i in v]
                        break
            if not srcs:
                srcs = [["steam", "Steam 官方热销榜（+ Gamalytic 估算）", "https://store.steampowered.com/charts/topselling/global"]]
            items.append({"section": "rankings", "title": title, "body": title, "body_html": body_html,
                          "meta": [], "sources": srcs})
        elif sec == "release":
            for ln in rest.splitlines():
                s = ln.strip()
                if not s.startswith("- "):
                    continue
                body = s[2:].strip()
                gm = re.search(r"《([^》]+)》", body)
                gname = gm.group(1) if gm else body[:24]
                srcs = sources_for(f"产品日历 - {gname}", title_ids, id_meta) or sources_for(gname, title_ids, id_meta)
                items.append({"section": "release", "title": gname, "body": body,
                              "body_html": "<p>" + md_inline(body) + "</p>", "meta": [], "sources": srcs})
        else:
            matches = list(re.finditer(r"(?m)^###\s+\d+\.\s+(.+)$", rest))
            for i, mt in enumerate(matches):
                title = mt.group(1).strip()
                start = mt.end()
                end = matches[i + 1].start() if i + 1 < len(matches) else len(rest)
                body_block = rest[start:end].strip()
                paras = [p.strip() for p in re.split(r"\n\s*\n", body_block) if p.strip()]
                body_plain = " ".join(paras)
                body_html = "".join(f"<p>{md_inline(p)}</p>" for p in paras)
                items.append({"section": sec, "title": title, "body": body_plain,
                              "body_html": body_html, "meta": [], "sources": sources_for(title, title_ids, id_meta)})
    return items


def collected_records(md_path: Path) -> str:
    summ = md_path.parent / "_intermediate" / "report_inputs_summary.md"
    if summ.exists():
        m = re.search(r"Records:\s*(\d+)", summ.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return "—"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    md_path = Path(sys.argv[1]).resolve()
    md = md_path.read_text(encoding="utf-8")
    sources_path = md_path.parent / "sources_used.md"
    title_ids, id_meta = parse_sources(sources_path.read_text(encoding="utf-8")) if sources_path.exists() else ({}, {})

    kind, start, end, date_label, title = parse_meta(md_path)
    items = parse_report(md, kind, title_ids, id_meta)

    sections = [{"id": "all", "label": "全部", "desc": "浏览全部内容，或从左侧选择单个板块。"}]
    order = ["rankings", "industry", "ai", "release", "discourse", "deep"]
    present = {it["section"] for it in items}
    labels = {"industry": "行业新闻", "ai": "AI 新闻", "release": "产品日历", "discourse": "玩家舆论", "deep": "深度观察"}
    for sid in order:
        if sid not in present:
            continue
        if sid == "rankings":
            sections.append({"id": "rankings", "label": RANK_LABEL.get(kind, "steam榜单"),
                             "desc": SECTION_DESCS["rankings"].get(kind, "Steam 榜单。")})
        else:
            sections.append({"id": sid, "label": labels[sid], "desc": SECTION_DESCS[sid]})

    from collections import Counter
    c = Counter(it["section"] for it in items)
    metrics = ('<div class="metrics">'
               f'<div class="metric"><span>行业新闻</span><strong>{c.get("industry",0)}</strong></div>'
               f'<div class="metric"><span>产品日历</span><strong>{c.get("release",0)}</strong></div>'
               f'<div class="metric"><span>玩家舆论</span><strong>{c.get("discourse",0)}</strong></div>'
               f'<div class="metric"><span>采集记录</span><strong>{collected_records(md_path)}</strong></div></div>')

    h1 = f"游戏行业{KIND_CN[kind]}"
    subtitle = f"{date_label} · {RANK_LABEL.get(kind,'steam榜单')}、行业新闻、AI、产品日历、玩家舆论与精选观察"
    stat = f"{date_label} · {len(items)} 条动态"

    tpl = TEMPLATE.read_text(encoding="utf-8")
    out = (tpl
           .replace("__TITLE__", title)
           .replace("__BRAND_SUB__", BRAND_SUB[kind])
           .replace("__H1__", h1)
           .replace("__SUBTITLE__", subtitle)
           .replace("__METRICS__", metrics)
           .replace("__STAT__", stat)
           .replace("__SECTIONS__", json.dumps(sections, ensure_ascii=False))
           .replace("__ITEMS__", json.dumps(items, ensure_ascii=False)))

    out_path = md_path.with_suffix(".html")
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote {out_path}  ({len(items)} items: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())) + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
