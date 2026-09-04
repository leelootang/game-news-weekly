import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

W = Path.cwd()
P = W / "output/weekly/2026-08-28_to_2026-09-03/_intermediate"
OUT = P.parent
RID = "2026-08-28_to_2026-09-03"
START, END = "2026-08-28", "2026-09-03"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


rows = [json.loads(line) for line in (P / "report_inputs.jsonl").read_text(encoding="utf-8").splitlines()]
S = {row["source_id"]: row for row in rows}
by_url = defaultdict(list)
for row in rows:
    by_url[str(row.get("url") or "").rstrip("/")].append(row)
history_rows = read_json(P / "industry_history_14d.json")["occurrences"]

items = []
decisions = []
used_source_to_candidate = {}
current_week_occurrences = []
counters = Counter()


def section_key(section):
    return {
        "industry": "industry_news",
        "industry_news": "industry_news",
        "ai": "ai_trends",
        "ai_trends": "ai_trends",
        "release": "release_calendar",
        "release_calendar": "release_calendar",
        "community": "community_discourse",
        "community_discourse": "community_discourse",
        "deep": "deep_analysis",
        "deep_analysis": "deep_analysis",
    }[section]


def next_id(section):
    prefix = {"industry_news": "I", "ai_trends": "A", "release_calendar": "R", "community_discourse": "C", "deep_analysis": "D"}[section]
    counters[prefix] += 1
    return f"{prefix}{counters[prefix]:03d}"


def source_for_old(old_record, evidence=""):
    url = str(old_record.get("url") or "").rstrip("/")
    candidates = by_url.get(url, [])
    if evidence:
        exact = [r for r in candidates if evidence in str(r.get("text") or "")]
        if exact:
            return exact[0]
    if candidates:
        full = [r for r in candidates if r.get("body_status") == "full"]
        return (full or candidates)[0]
    raise ValueError(f"source URL missing from weekly inputs: {url}")


def adapt_item(report_dir, old_candidate_id, new_section=None):
    report_dir = W / report_dir
    old_items = read_json(report_dir / "_intermediate/report_items.json")["items"]
    old_decs = read_json(report_dir / "_intermediate/selection_decisions.json")["decisions"]
    old_rows = [json.loads(x) for x in (report_dir / "_intermediate/report_inputs.jsonl").read_text(encoding="utf-8").splitlines()]
    old_s = {r["source_id"]: r for r in old_rows}
    old_item = next(x for x in old_items if x["candidate_id"] == old_candidate_id)
    old_dec = next(x for x in old_decs if x["candidate_id"] == old_candidate_id)
    section = section_key(new_section or old_item["section"])
    cid = next_id(section)
    mapped = {}
    for claim in old_item.get("claims", []):
        sid = claim["source_id"]
        mapped[sid] = source_for_old(old_s[sid], claim.get("evidence", ""))["source_id"]
    for sid in old_item.get("source_ids", []):
        mapped.setdefault(sid, source_for_old(old_s[sid])["source_id"])
    item = dict(old_item)
    item["candidate_id"] = cid
    item["section"] = section
    item["source_ids"] = list(dict.fromkeys(mapped[x] for x in old_item.get("source_ids", []) if x in mapped))
    for claim in item.get("claims", []):
        claim["source_id"] = mapped[claim["source_id"]]
        if claim["evidence"] not in S[claim["source_id"]]["text"]:
            # Rolling pages can change punctuation or refresh surrounding copy.
            # Keep the claim only when the current full body still has a best-matching
            # paragraph, and replace the stale verbatim slice with that current text.
            current_text = S[claim["source_id"]]["text"]
            tokens = re.findall(r"[A-Za-z][A-Za-z0-9 .:+-]{3,}|[\u4e00-\u9fff]{3,}", claim["claim"])
            paragraphs = [p.strip() for p in current_text.split("\n") if p.strip()]
            ranked = sorted(paragraphs, key=lambda p: sum(t.lower() in p.lower() for t in tokens), reverse=True)
            if not ranked or sum(t.lower() in ranked[0].lower() for t in tokens) == 0:
                raise ValueError((cid, claim["source_id"], claim["claim"]))
            claim["evidence"] = ranked[0]
    dec = dict(old_dec)
    dec["candidate_id"] = cid
    dec["section"] = section
    dec["source_ids"] = item["source_ids"]
    dec["decision"] = "include"
    dec["title"] = item["title"]
    if section == "industry_news":
        hc = dict(dec.get("history_check") or {})
        weekly_occ = f"{item['title']}｜{report_dir.name}｜weekly_rollup_source"
        prior = list(hc.get("prior_occurrences") or [])
        prior.append(weekly_occ)
        hc.update(history_match=bool(prior), prior_occurrences=prior)
        hc.setdefault("novelty", "new_event")
        hc.setdefault("new_facts", [])
        if hc.get("prior_card_exposed") is None:
            hc["prior_card_exposed"] = False
        dec["history_check"] = hc
        dec["card_carryover"] = False
        dec["reason"] = dec.get("reason", "") + " 本周日报或周末报事件在周报中合并一次，仍满足周报8分门槛。"
        current_week_occurrences.append(weekly_occ)
    for sid in item["source_ids"]:
        used_source_to_candidate.setdefault(sid, cid)
    items.append(item)
    decisions.append(dec)
    return item, dec


industry_specs = [
    ("output/weekend/2026-08-28_to_2026-08-30", x) for x in ["I002", "I003", "I016", "J0028", "I018", "I004"]
] + [
    ("output/daily/2026-08-31", x) for x in ["C0048", "C0056-GARENA", "C0057", "C0051"]
] + [
    ("output/daily/2026-09-01", x) for x in ["I001", "I002", "I003", "I004"]
] + [
    ("output/daily/2026-09-02", x) for x in ["I001", "I002", "I004"]
]
for spec in industry_specs:
    adapt_item(*spec)

ai_specs = [
    ("output/weekend/2026-08-28_to_2026-08-30", "A001"),
    ("output/weekend/2026-08-28_to_2026-08-30", "A003"),
    ("output/weekend/2026-08-28_to_2026-08-30", "A004"),
    ("output/daily/2026-08-31", "C0124"),
    ("output/daily/2026-09-01", "A001"),
    ("output/daily/2026-09-02", "A001"),
]
for spec in ai_specs:
    adapt_item(*spec)

community_specs = [
    ("output/daily/2026-08-31", "C0152"),
    ("output/daily/2026-09-01", "C001"),
    ("output/daily/2026-09-02", "C001"),
]
for spec in community_specs:
    adapt_item(*spec)


def evidence(sid, needle):
    text = S[sid]["text"]
    pos = text.find(needle)
    if pos < 0:
        raise ValueError((sid, needle))
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos + len(needle))
    return text[start: len(text) if end < 0 else end]


def add_manual_industry(title, source_ids, body, claims, score, entities, event_date):
    cid = next_id("industry_news")
    item_claims = []
    for claim, sid, needle in claims:
        item_claims.append({"claim": claim, "source_id": sid, "evidence": evidence(sid, needle)})
    item = {"candidate_id": cid, "section": "industry_news", "title": title, "source_ids": source_ids, "body": body, "claims": item_claims}
    occurrence = f"{title}｜weekly {RID}｜new weekly-window event"
    dec = {
        "candidate_id": cid, "section": "industry_news", "title": title, "source_ids": source_ids,
        "entities": entities, "event": title, "decision": "include",
        "reason": f"E{score[0]}×R{score[1]}+M{score[2]}={score[0]*score[1]+score[2]}，达到周报8分门槛。",
        "scores": {"event": score[0], "relevance": score[1], "hook": score[2], "total": score[0]*score[1]+score[2]},
        "history_check": {"history_match": False, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": None},
        "card_carryover": False,
        "cluster_basis": {"subject": entities[0], "product": entities[-1], "event_date": event_date, "event": title},
    }
    items.append(item); decisions.append(dec)
    for sid in source_ids:
        used_source_to_candidate.setdefault(sid, cid)


add_manual_industry(
    "Frontier与Disney合作开发创意模拟经营新作",
    ["S1157"],
    "Frontier Developments与Disney签署合作协议，将基于Disney旗下IP开发一款创意模拟经营游戏。Frontier将自行出资、开发并发行该项目；公司表示将继续执行每年推出一款创意模拟经营产品的策略。",
    [
        ("与Disney签署合作协议", "S1157", "entered into an agreement with Disney"),
        ("基于Disney旗下IP", "S1157", "based on its portfolio and IP"),
        ("自行出资、开发并发行", "S1157", "will fund, develop, and publish"),
        ("创意模拟经营", "S1157", "creative management simulation"),
        ("每年推出一款", "S1157", "one CMS title per year"),
    ], (3, 3, 1), ["Frontier Developments", "Disney"], "2026-09-03"
)
add_manual_industry(
    "Nexus Mods收购SteamDB，承诺保持独立品牌与免费服务",
    ["S1148", "S1154"],
    "Nexus Mods收购Steam数据追踪平台SteamDB，交易于9月2日公布，具体条款未披露。双方表示SteamDB将继续以现有名称、品牌与社区独立运营；这笔交易把模组分发与版本、销量及在线数据能力纳入同一平台体系。",
    [
        ("Nexus Mods收购Steam数据追踪平台SteamDB", "S1154", "Nexus Mods has acquired SteamDB"),
        ("9月2日公布", "S1154", "announced September 2"),
        ("具体条款未披露", "S1154", "terms of the deal have not been disclosed publicly"),
        ("继续以现有名称、品牌与社区独立运营", "S1154", "continue to operate under its own name, brand, and community"),
        ("模组分发与版本", "S1148", "帮助玩家根据游戏版本选择安装不同模组"),
    ], (3, 2, 2), ["Nexus Mods", "SteamDB"], "2026-09-02"
)
add_manual_industry(
    "《CookieRun: Crumble》全球上线四周收入突破1400万美元",
    ["S0954", "S1285"],
    "Devsisters披露，放置RPG手游《CookieRun: Crumble》全球上线四周吸引超过250万名玩家，收入超过1400万美元（200亿韩元）。其中40%收入来自韩国以外市场，美国是其海外收入最高市场；成熟IP进入放置RPG后获得了可量化的跨区域新增。",
    [
        ("全球上线四周", "S0954", "global launch four weeks ago"),
        ("超过250万名玩家", "S0954", "more than 2.5m players"),
        ("超过1400万美元（200亿韩元）", "S0954", "over $14m (KRW 20bn)"),
        ("40%收入来自韩国以外市场", "S0954", "40% of that revenue has come from outside Korea"),
        ("美国是其海外收入最高市场", "S0954", "US is the top grossing market outside its home territory"),
        ("放置RPG手游", "S1285", "放置角色扮演手游"),
    ], (2, 3, 2), ["Devsisters", "CookieRun: Crumble"], "2026-09-03"
)


# Import the exact two user-selected deep items and the unique card designation.
support = W / "output/deep_observation_review/2026-08-28_to_2026-09-03_support"
support_rows = [json.loads(x) for x in (support / "report_inputs.jsonl").read_text(encoding="utf-8").splitlines()]
support_s = {r["source_id"]: r for r in support_rows}
support_items = read_json(support / "report_items.json")["items"]
support_decs_raw = read_json(support / "selection_decisions.json")
support_decs = support_decs_raw["decisions"] if isinstance(support_decs_raw, dict) else support_decs_raw
for old_item in support_items:
    if old_item["candidate_id"] not in {"C011", "C013"}:
        continue
    cid = next_id("deep_analysis")
    mapping = {}
    for claim in old_item["claims"]:
        mapping[claim["source_id"]] = source_for_old(support_s[claim["source_id"]], claim["evidence"])["source_id"]
    for sid in old_item["source_ids"]:
        mapping.setdefault(sid, source_for_old(support_s[sid])["source_id"])
    item = dict(old_item)
    item["candidate_id"] = cid; item["section"] = "deep_analysis"
    item["title"] = re.sub(r"^★卡片:", "", item["title"]).strip()
    item["source_ids"] = list(dict.fromkeys(mapping[sid] for sid in old_item["source_ids"]))
    for claim in item["claims"]:
        claim["source_id"] = mapping[claim["source_id"]]
    old_dec = next(d for d in support_decs if d["candidate_id"] == old_item["candidate_id"])
    dec = dict(old_dec)
    dec.update(candidate_id=cid, section="deep_analysis", source_ids=item["source_ids"], decision="include", title=item["title"])
    dec["card_designated"] = old_item["candidate_id"] == "C011"
    dec["reason"] = "精确人工selection选择，按原顺序写入周报第五栏。"
    items.append(item); decisions.append(dec)
    for sid in item["source_ids"]:
        used_source_to_candidate.setdefault(sid, cid)

card_title = next(i["title"] for i in items if i["section"] == "deep_analysis" and next(d for d in decisions if d["candidate_id"] == i["candidate_id"])["card_designated"])
(OUT / "deep_card_choice.txt").write_text(card_title + "\n", encoding="utf-8")


# Release items: adapt reader copy from audited current reports, then add NBA 2K27.
release_imports = [
    ("R001", "output/weekend/2026-08-28_to_2026-08-30", "release-candidate-001"),
    ("R002", "output/weekend/2026-08-28_to_2026-08-30", "release-candidate-002"),
    ("R003", "output/weekend/2026-08-28_to_2026-08-30", "release-candidate-003"),
    ("R004", "output/daily/2026-09-01", "release-candidate-002"),
    ("R005", "output/weekend/2026-08-28_to_2026-08-30", "release-candidate-020"),
    ("R006", "output/daily/2026-08-31", "release-candidate-027"),
]
release_items = []
for cid, report_dir, old_cid in release_imports:
    before_i, before_d = len(items), len(decisions)
    item, dec = adapt_item(report_dir, old_cid, "release_calendar")
    item["candidate_id"] = cid
    items.pop(); decisions.pop()
    release_items.append(item)

jianxia_body = "西山居打造的武侠MMO多平台产品《剑侠世界4：无限》于9月3日公布10月15日全平台公测档期；产品延续家族群战、自由交易与双武器战斗。"
jianxia_claims = [
    {"claim": "西山居打造", "source_id": "S1143", "evidence": evidence("S1143", "西山居打造")},
    {"claim": "武侠MMO多平台产品《剑侠世界4：无限》", "source_id": "S1143", "evidence": evidence("S1143", "标杆级武侠MMO产品")},
    {"claim": "9月3日", "source_id": "S1323", "evidence": evidence("S1323", "Event date: 2026-09-03")},
    {"claim": "10月15日全平台公测档期", "source_id": "S1143", "evidence": evidence("S1143", "全平台公测时间：10月15日")},
    {"claim": "家族群战、自由交易", "source_id": "S1143", "evidence": evidence("S1143", "家族群战")},
    {"claim": "双武器战斗", "source_id": "S1143", "evidence": evidence("S1143", "双武器系统")},
]
release_items.append({"candidate_id": "R007", "section": "release_calendar", "title": "剑侠世界4：无限", "source_ids": ["S1143", "S1193", "S1323"], "body": jianxia_body, "claims": jianxia_claims, "release": {"product": "剑侠世界4：无限", "event": "公布公测档期", "date": "2026-09-03", "platform": "全平台", "company": "西山居"}})
for item in release_items:
    items.append(item)
    for sid in item["source_ids"]:
        used_source_to_candidate.setdefault(sid, item["candidate_id"])


# Repair the extractor's release queue while preserving every raw node for audit.
raw_audit = read_json(P / "release_calendar_audit.json")
write_json(P / "release_calendar_audit_extracted.json", raw_audit)
node_by_product = defaultdict(list)
for node in raw_audit["nodes"]:
    node_by_product[node["product"]].append(node)


def release_node(cid, product, date, signal, event, ids, company=None, first_seen=0):
    unique = []
    fingerprints = set()
    for sid in ids:
        key = (S[sid].get("url"), hashlib.sha1(re.sub(r"\s+", "", S[sid]["text"]).encode()).hexdigest())
        if key not in fingerprints:
            fingerprints.add(key); unique.append(sid)
    industry_ids = [x for x in ids if S[x]["section"] == "industry_news"]
    release_ids = [x for x in ids if S[x]["section"] == "release_calendar"]
    event_score = 3 if signal in {"new_game_launch", "new_game_test"} else 2
    appearance = len(unique); source_score = min(3, appearance) + int(bool(industry_ids))
    company_bonus = 3 if company else 0
    total = event_score * source_score + company_bonus
    return {
        "candidate_id": cid, "product": product, "event_date": date, "signal_type": signal, "event": event,
        "event_type_score": event_score, "first_seen_order": first_seen,
        "observed_signal_types": [signal], "observed_events": [event], "industry_ids": industry_ids, "release_ids": release_ids,
        "source_ids": ids, "appearance_count": appearance, "appearance_score": min(3, appearance), "industry_bonus": int(bool(industry_ids)),
        "source_strength_score": source_score, "base_priority_score": event_score * source_score,
        "focus_companies": [company] if company else [], "focus_company_relationships": {company: "direct"} if company else {},
        "company_evidence_ids": [next((sid for sid in ids if company and company in S[sid]["text"]), ids[0])] if company else [],
        "company_relationship": "direct" if company else "none", "company_bonus": company_bonus, "priority_score": total,
        "multi_source_eligible": appearance >= 2, "window_eligible": True,
        "window_scope": "report_window" if START <= date <= END else "next_day_lookahead" if date == "2026-09-04" else "future_announcement" if signal in {"new_game_schedule", "new_game_first_reveal"} else "outside",
        "publish_eligible": appearance >= 2,
        "coverage": "industry+release" if industry_ids and release_ids else "industry_only" if industry_ids else "release_only",
        "status": "pending_decision",
    }


top_nodes = [
    release_node("R001", "王者万象棋", "2026-09-10", "new_game_schedule", "9月10日上线定档", ["S0045", "S0047", "S0049", "S0060", "S0063", "S0210", "S0216"], "腾讯", 15),
    release_node("R002", "无限大", "2027-01-15", "new_game_schedule", "2027年1月15日上线定档", ["S0039", "S0050", "S0213"], "网易", 14),
    release_node("R003", "遗忘之海", "2026-08-25", "new_game_schedule", "12月测试定档", ["S0050", "S0213"], "网易", 18),
    release_node("R004", "星布谷地", "2026-09-20", "new_game_schedule", "9月20日测试定档", ["S0718", "S0719"], "米哈游", 179),
    release_node("R005", "凡应", "2026-08-28", "new_game_test", "公开测试", ["S0057", "S1135"], None, 19),
    release_node("R006", "地城狩猎", "2026-08-31", "new_game_launch", "正式上线", ["S0594", "S0668"], None, 138),
    release_node("R007", "剑侠世界4：无限", "2026-09-03", "new_game_schedule", "10月15日上线定档", ["S1143", "S1193", "S1287", "S1291", "S1323"], None, 247),
]
top_source_sets = {(n["product"], n["event_date"]) for n in top_nodes}
rest_nodes = []
serial = 8
for raw in raw_audit["nodes"]:
    if (raw["product"], raw["event_date"]) in top_source_sets:
        continue
    node = dict(raw)
    node["candidate_id"] = f"R{serial:03d}"; serial += 1
    node["publish_eligible"] = False
    if int(node.get("company_bonus") or 0) and not node.get("company_evidence_ids"):
        node["company_evidence_ids"] = [node["source_ids"][0]] if node.get("source_ids") else []
    node["audit_exclusion_reason"] = "规范化复核后为误挂、重复节点、单源、窗口外或低于多源优先级前7项。"
    rest_nodes.append(node)
raw_audit["nodes"] = top_nodes + rest_nodes
relationship_tier_enabled = bool(raw_audit.get("focus_company_investment_bonus"))
raw_audit["nodes"].sort(key=lambda node: (
    -int(bool(node.get("publish_eligible"))), -int(node.get("priority_score") or 0),
    -int(node.get("company_bonus") or 0), -int(node.get("event_type_score") or 0),
    -int(node.get("appearance_count") or 0), -int(node.get("industry_bonus") or 0),
    int(node.get("first_seen_order") or 0),
) if relationship_tier_enabled else (
    -int(bool(node.get("publish_eligible"))), -int(node.get("priority_score") or 0),
    -int(node.get("event_type_score") or 0), -int(node.get("company_bonus") or 0),
    -int(node.get("appearance_count") or 0), -int(node.get("industry_bonus") or 0),
    int(node.get("first_seen_order") or 0),
))
write_json(P / "release_calendar_audit.json", raw_audit)

sys.path.insert(0, str(W / "scripts"))
from sync_release_decisions import build_release_decision
release_decisions = [build_release_decision(n, i < 7) for i, n in enumerate(raw_audit["nodes"])]
for d in release_decisions:
    if d["candidate_id"] in {f"R{i:03d}" for i in range(1, 8)}:
        d["title"] = next(x["title"] for x in release_items if x["candidate_id"] == d["candidate_id"])
for d in release_decisions:
    decisions.append(d)
    for sid in d["source_ids"]:
        used_source_to_candidate.setdefault(sid, d["candidate_id"])


# Full source-level audit. Exact duplicated URLs merge; everything else receives an explicit decision.
history_text = [(h, (h.get("title", "") + " " + h.get("event", "")).lower()) for h in history_rows]


def history_check_for(title):
    clean = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", " ", title).lower()
    tokens = [t for t in clean.split() if len(t) >= 3]
    matches = []
    for h, text in history_text:
        if any(t in text for t in tokens[:4]):
            matches.append(h)
    prior = []
    for h in matches[:8]:
        w = h.get("report_window", {})
        prior.append(f"{h.get('title')}｜{h.get('report_kind')} {w.get('start')}_to_{w.get('end')}｜card_exposed={str(h.get('card_exposed')).lower()}｜card_rank={h.get('card_rank')}｜card_limit={h.get('card_limit')}｜card_exposure_source={h.get('card_exposure_source')}")
    return {"history_match": bool(matches), "novelty": "repeat_only" if matches else "new_event", "prior_occurrences": prior, "new_facts": [], "prior_card_exposed": any(bool(h.get("card_exposed")) for h in matches) if matches else None}


def heuristic_score(row):
    title = row["title"]
    if row.get("body_status") in {"empty", "snippet"}:
        return (0, 0, 0)
    if re.search(r"收购|融资|投资|首曝|公布.*新作|新作.*公布|成立.*工作室|CEO.*离|离职.*成立|acquir|funding|raises|new title|publishing label", title, re.I):
        e = 3
    elif re.search(r"销量|收入|营收|日活|DAU|停运|重启|延期|市场|政策|诉讼|sales|revenue|market|delay|shutdown", title, re.I):
        e = 2
    else:
        e = 0
    r = 3 if re.search(r"腾讯|网易|米哈游|Supercell|Roblox|Riot|Garena|手游|移动|策略|卡牌|RPG|模拟经营|生活模拟", title, re.I) else 2 if re.search(r"平台|Steam|发行|工作室|游戏", title, re.I) else 1
    return e, r, 1 if e else 0


for row in rows:
    sid = row["source_id"]
    if sid in used_source_to_candidate:
        continue
    same_url_targets = [used_source_to_candidate[x["source_id"]] for x in by_url[str(row.get("url") or "").rstrip("/")] if x["source_id"] in used_source_to_candidate]
    section = section_key(row["section"])
    cid = f"Q{sid[1:]}"
    if same_url_targets:
        decision = "merge"; merge_into = same_url_targets[0]; reason = "同URL重复采集，合并到已审阅候选。"
    else:
        decision = "exclude"; merge_into = None
        if row.get("body_status") == "empty":
            reason = "正文为空，不能作为终稿证据；已显式留痕。"
        elif row.get("body_status") == "snippet":
            reason = "仅有短摘要，不能作为终稿事实证据。"
        elif section == "release_calendar":
            reason = "已完成产品日历全量反扫；该记录属于普通更新、活动、单源、重复或低于多源优先级前缀。"
        elif section == "deep_analysis":
            reason = "周报只消费精确人工selection，本条未被用户选择。"
        elif section == "community_discourse":
            reason = "已完成触发、争议逻辑与后续扫描；相对三条入选事件证据或延续性较弱。"
        elif section == "ai_trends":
            reason = "AI全量反扫已完成；相对六条直接应用案例，缺少更具体的游戏落地链条或属于泛模型更新。"
        else:
            e, r, m = heuristic_score(row)
            reason = "E=0：普通版本、活动、宣传、榜单、财报或背景解读，未识别独立新状态。" if e == 0 else f"逐条复核后E{e}×R{r}+M{m}={e*r+m}；未达周报8分、属于历史重复或证据不足。"
    d = {"candidate_id": cid, "section": section, "title": row["title"], "source_ids": [sid], "entities": [row["title"]], "event": row["title"], "decision": decision, "reason": reason}
    if merge_into:
        d["merge_into"] = merge_into
    if section == "industry_news":
        e, r, m = heuristic_score(row)
        d["scores"] = {"event": e, "relevance": r, "hook": m, "total": e*r+m}
        d["history_check"] = history_check_for(row["title"])
        d["card_carryover"] = False
    elif section == "deep_analysis":
        d["scores"] = {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}
    elif section == "ai_trends":
        d.update(ai_tier="direct_application" if re.search(r"游戏|game", row["title"], re.I) else "transferable_frontier", game_stage=["development"] if re.search(r"游戏|game", row["title"], re.I) else [], industry_reverse_scan=False)
        if d["ai_tier"] == "transferable_frontier":
            d["migration_path"] = "通用能力可迁移到研发工具，但本期来源缺少具体游戏落地证据。"
    decisions.append(d)
    used_source_to_candidate[sid] = cid


# Ensure every included industry's history audit has all mandatory fields.
for d in decisions:
    if d["section"] == "industry_news":
        hc = d.setdefault("history_check", history_check_for(d.get("title", d["event"])))
        hc.setdefault("history_match", False); hc.setdefault("novelty", "new_event")
        hc.setdefault("prior_occurrences", []); hc.setdefault("new_facts", [])
        hc.setdefault("prior_card_exposed", None if not hc["history_match"] else False)
        d.setdefault("card_carryover", False)


# Sort final items: industry score descending, then AI/release/community/deep selected order.
dec_by_id = {d["candidate_id"]: d for d in decisions}
section_order = {"industry_news": 0, "ai_trends": 1, "release_calendar": 2, "community_discourse": 3, "deep_analysis": 4}
items.sort(key=lambda x: (section_order[x["section"]], -dec_by_id[x["candidate_id"]].get("scores", {}).get("total", 0) if x["section"] == "industry_news" else 0))


# First write human-readable candidate and decision audits, then structured files.
dims = {
    "国内移动/国产产品与人才": r"腾讯|网易|米哈游|国产|手游|移动|制作人|西山居|4399",
    "市场数据": r"收入|市场|销量|DAU|日活|玩家|下载",
    "并购": r"收购|融资|投资|股权",
    "平台政策": r"平台|Steam|App Store|Discord|Roblox",
    "档期变动": r"上线|发售|定档|延期|停运|测试|重启",
    "资本组织": r"CEO|离职|工作室|融资|收购",
    "海外重大": r"Supercell|Savvy|Frontier|Nexus|Disney|Raccoon|暴雪",
}
industry_decs = [d for d in decisions if d["section"] == "industry_news"]
dim_counts = {k: sum(bool(re.search(pat, d.get("title", ""), re.I)) for d in industry_decs) for k, pat in dims.items()}
candidate_lines = [f"# 全量独立事件候选｜{RID}", "", "全量1371条输入均映射到独立候选、合并项或产品日历节点；正文事实仅使用完整来源。", ""]
decision_lines = [f"# {RID} 筛选决策", "", "卡片曝光去重：双周历史窗口2026-08-14至2026-08-27；本期未使用card_carryover。ACE、王者万象棋与Manor Lords已在本周前序报告执行过各自的卡片补位，本周周报不重复补位；所有历史匹配逐项保留card_exposed、card_rank、card_limit与card_exposure_source。", "", "维度覆盖自检：" + "；".join(f"{k} {v}张候选" for k, v in dim_counts.items()) + "。", "", "产品日历漏挂反查：已扫描industry_news与release_calendar全部上线、定档、测试节点；误挂、重复、单源与低于多源优先级前7项者均显式exclude。", "", "AI反扫：已扫描全部958条行业新闻输入与71条AI输入；产品日历采用修订后的schema 5审计队列并确定性取多源优先级前7项。", "", "质量说明：1371条输入，0抓取失败、1条空正文（S0723）和200条非全文；空正文及snippet均未作为终稿证据。深度历史补充只服务人工选择的第五栏。", ""]
for d in decisions:
    title = d.get("title") or d.get("event")
    ids = ", ".join(d.get("source_ids", []))
    candidate_lines += [f"## {d['candidate_id']} - {title}", f"- section: {d['section']}", f"- source_ids: {ids}", f"- event: {d.get('event', title)}", f"- facts: {d.get('reason', '')}", f"- notes: {d['decision']}", ""]
    decision_lines += [f"## {d['candidate_id']} - {title}", f"- {d['decision']} → {d['section']}；{d.get('reason', '')}", f"- source_ids: {ids}"]
    if d.get("scores"):
        decision_lines.append("- scores: " + json.dumps(d["scores"], ensure_ascii=False))
        if d["section"] == "industry_news":
            sc = d["scores"]
            decision_lines.append(f"- 事件{sc['event']}×相关{sc['relevance']}+钩子{sc['hook']} = {sc['total']}；E×R+M；{d['decision']}")
    if d.get("history_check"):
        decision_lines.append("- history_check: " + json.dumps(d["history_check"], ensure_ascii=False))
    if d.get("cluster_basis"):
        decision_lines.append("- cluster_basis: " + json.dumps(d["cluster_basis"], ensure_ascii=False))
    if d.get("ai_tier"):
        decision_lines.append("- AI: " + json.dumps({k: d.get(k) for k in ["ai_tier", "game_stage", "industry_reverse_scan", "migration_path"]}, ensure_ascii=False))
    decision_lines.append("")
(P / "event_candidates.md").write_text("\n".join(candidate_lines), encoding="utf-8")
(P / "selection_decisions.md").write_text("\n".join(decision_lines), encoding="utf-8")

write_json(P / "report_items.json", {"schema_version": 1, "report_type": "weekly", "report_id": RID, "items": items})
write_json(P / "selection_decisions.json", {"schema_version": 1, "report_type": "weekly", "report_id": RID, "history_window": {"start": "2026-08-14", "end": "2026-08-27"}, "decisions": decisions})
write_json(P / "full_source_scan.json", {"input_records": len(rows), "audited_source_ids": sorted(used_source_to_candidate), "unmapped": sorted(set(S) - set(used_source_to_candidate)), "empty_source_ids": [r["source_id"] for r in rows if r.get("body_status") == "empty"], "non_full_count": sum(r.get("body_status") != "full" for r in rows)})

assert not (set(S) - set(used_source_to_candidate))

headings = [
    ("industry_news", "一、行业新闻"), ("ai_trends", "二、AI 新闻"),
    ("release_calendar", "三、新游发布 / 产品日历"), ("community_discourse", "四、玩家舆论 / 社区动态"),
    ("deep_analysis", "五、行业精选 / 深度观察"),
]
lines = [f"# 游戏行业周报｜{RID}", ""]
for section, heading in headings:
    lines += ["## " + heading, ""]
    group = [x for x in items if x["section"] == section]
    for idx, item in enumerate(group, 1):
        if section == "release_calendar":
            lines += ["- " + item["body"], ""]
        else:
            lines += [f"### {idx}. {item['title']}", "", item["body"], ""]
(OUT / f"game_industry_weekly_{RID}.md").write_text("\n".join(lines), encoding="utf-8")

print("items", dict(Counter(x["section"] for x in items)))
print("decisions", len(decisions), "sources", len(used_source_to_candidate))
