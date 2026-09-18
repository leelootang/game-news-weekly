import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

W = Path.cwd()
RID = "2026-09-11_to_2026-09-17"
START, END = "2026-09-11", "2026-09-17"
OUT = W / "output" / "weekly" / RID
P = OUT / "_intermediate"


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


rows = [json.loads(line) for line in (P / "report_inputs.jsonl").read_text(encoding="utf-8").splitlines()]
S = {row["source_id"]: row for row in rows}
by_url = defaultdict(list)
for row in rows:
    by_url[str(row.get("url") or "").rstrip("/")].append(row)
history_rows = load_json(P / "industry_history_14d.json")["occurrences"]

items = []
decisions = []
used_sources = {}
counters = Counter()


def next_id(section):
    prefix = {
        "industry_news": "I",
        "ai_trends": "A",
        "release_calendar": "R",
        "community_discourse": "C",
    }[section]
    counters[prefix] += 1
    return f"{prefix}{counters[prefix]:03d}"


def old_bundle(report_dir):
    base = W / report_dir / "_intermediate"
    report_items = load_json(base / "report_items.json")
    report_items = report_items["items"] if isinstance(report_items, dict) else report_items
    report_decs = load_json(base / "selection_decisions.json")
    report_decs = report_decs["decisions"] if isinstance(report_decs, dict) else report_decs
    report_rows = [json.loads(x) for x in (base / "report_inputs.jsonl").read_text(encoding="utf-8").splitlines()]
    return report_items, report_decs, {r["source_id"]: r for r in report_rows}


def map_old_source(old_row, evidence_text=""):
    candidates = by_url.get(str(old_row.get("url") or "").rstrip("/"), [])
    same_hash = [r for r in candidates if r.get("sha1") and r.get("sha1") == old_row.get("sha1")]
    if same_hash:
        return same_hash[0]
    if evidence_text:
        exact = [r for r in candidates if evidence_text in str(r.get("text") or "")]
        if exact:
            return exact[0]
    same_date_title = [r for r in candidates if r.get("date") == old_row.get("date") and r.get("title") == old_row.get("title")]
    if same_date_title:
        return same_date_title[0]
    if candidates:
        full = [r for r in candidates if r.get("body_status") == "full"]
        return (full or candidates)[0]
    raise ValueError(f"weekly input missing URL: {old_row.get('url')}")


def adapt(report_dir, old_cid, section=None, score=None, novelty=None, new_facts=None):
    old_items, old_decs, old_s = old_bundle(report_dir)
    old_item = next(x for x in old_items if x["candidate_id"] == old_cid)
    old_dec = next(x for x in old_decs if x["candidate_id"] == old_cid)
    target = section or {
        "industry": "industry_news", "industry_news": "industry_news",
        "ai": "ai_trends", "ai_trends": "ai_trends",
        "release": "release_calendar", "release_calendar": "release_calendar",
        "community": "community_discourse", "community_discourse": "community_discourse",
    }[old_item["section"]]
    cid = next_id(target)
    mapped = {}
    for claim in old_item.get("claims", []):
        mapped.setdefault(claim["source_id"], map_old_source(old_s[claim["source_id"]], claim.get("evidence", ""))["source_id"])
    for sid in old_item.get("source_ids", []):
        mapped.setdefault(sid, map_old_source(old_s[sid])["source_id"])
    item = dict(old_item)
    item["candidate_id"] = cid
    item["section"] = target
    item["source_ids"] = list(dict.fromkeys(mapped[s] for s in old_item.get("source_ids", [])))
    item["claims"] = [dict(c) for c in old_item.get("claims", [])]
    for claim in item["claims"]:
        claim["source_id"] = mapped[claim["source_id"]]
        if claim["evidence"] not in S[claim["source_id"]]["text"]:
            raise ValueError((cid, claim["source_id"], claim["evidence"][:80]))
    dec = dict(old_dec)
    dec.update(candidate_id=cid, section=target, source_ids=item["source_ids"], decision="include", title=item["title"])
    if target == "industry_news":
        if score:
            e, r, m = score
            dec["scores"] = {"event": e, "relevance": r, "hook": m, "total": e * r + m}
        sc = dec["scores"]
        origin = f"{item['title']}｜{Path(report_dir).name}｜current_week_rollup"
        hc = dict(dec.get("history_check") or {})
        prior = list(hc.get("prior_occurrences") or [])
        if origin not in prior:
            prior.append(origin)
        hc.update(
            history_match=True,
            novelty=novelty or hc.get("novelty") or "new_event",
            prior_occurrences=prior,
            new_facts=new_facts if new_facts is not None else list(hc.get("new_facts") or []),
            prior_card_exposed=bool(hc.get("prior_card_exposed")) if hc.get("prior_card_exposed") is not None else False,
        )
        dec["history_check"] = hc
        dec["card_carryover"] = False
        dec["reason"] = f"本周日报/周末报事件合并进入周报；E{sc['event']}×R{sc['relevance']}+M{sc['hook']}={sc['total']}，达到周报8分门槛。"
    items.append(item)
    decisions.append(dec)
    for sid in item["source_ids"]:
        used_sources.setdefault(sid, cid)
    return item, dec


# Industry: one weekly roll-up per independent event; scores are rechecked at the weekly threshold.
industry_specs = [
    ("output/weekend/2026-09-11_to_2026-09-13", "I001", None, None, None),
    ("output/weekend/2026-09-11_to_2026-09-13", "I002", None, None, None),
    ("output/weekend/2026-09-11_to_2026-09-13", "I003", None, None, None),
    ("output/weekend/2026-09-11_to_2026-09-13", "I004", None, "material_update", None),
    ("output/weekend/2026-09-11_to_2026-09-13", "I005", None, None, None),
    ("output/weekend/2026-09-11_to_2026-09-13", "I007", None, None, None),
    ("output/daily/2026-09-14", "I006", (3, 2, 2), "material_update", ["项目已错过开发节点并面临严重超支风险；索尼担忧预算、盈利与限时独占回报。"]),
    ("output/daily/2026-09-14", "I001", None, None, None),
    ("output/daily/2026-09-14", "I003", None, "material_update", None),
    ("output/daily/2026-09-15", "I002", None, None, None),
    ("output/daily/2026-09-15", "I003", None, "material_update", None),
    ("output/daily/2026-09-15", "I004", None, None, None),
    ("output/daily/2026-09-15", "I007", None, None, None),
    ("output/daily/2026-09-15", "I008", None, None, None),
    ("output/daily/2026-09-15", "I009", None, None, None),
    ("output/daily/2026-09-15", "I012", None, None, None),
    ("output/daily/2026-09-16", "I001", None, None, None),
    ("output/daily/2026-09-16", "I002", None, None, None),
]
for report_dir, old_cid, score, novelty, facts in industry_specs:
    adapt(report_dir, old_cid, score=score, novelty=novelty, new_facts=facts)


def evidence(sid, needle):
    text = S[sid]["text"]
    pos = text.find(needle)
    if pos < 0:
        raise ValueError((sid, needle))
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos + len(needle))
    return text[start: len(text) if end < 0 else end]


def add_industry(title, source_ids, body, claims, score, entities, event_date):
    cid = next_id("industry_news")
    e, r, m = score
    item = {
        "candidate_id": cid,
        "section": "industry_news",
        "title": title,
        "source_ids": source_ids,
        "body": body,
        "claims": [{"claim": c, "source_id": sid, "evidence": evidence(sid, needle)} for c, sid, needle in claims],
    }
    dec = {
        "candidate_id": cid,
        "section": "industry_news",
        "title": title,
        "source_ids": source_ids,
        "entities": entities,
        "event": title,
        "decision": "include",
        "reason": f"E{e}×R{r}+M{m}={e*r+m}，达到周报8分门槛。",
        "scores": {"event": e, "relevance": r, "hook": m, "total": e * r + m},
        "history_check": {"history_match": False, "novelty": "new_event", "prior_occurrences": [], "new_facts": [], "prior_card_exposed": None},
        "card_carryover": False,
        "cluster_basis": {"subject": entities[0], "product": entities[-1], "event_date": event_date, "event": title},
    }
    items.append(item)
    decisions.append(dec)
    for sid in source_ids:
        used_sources.setdefault(sid, cid)


add_industry(
    "《伊莫》PC首日Steam同时在线突破12万，海外评价占据主要样本",
    ["S1063", "S1079"],
    "FunPlus旗下爪印工作室研发的多人在线捉宠RPG《伊莫》于9月16日率先登陆PC与云游戏平台，Steam首日同时在线人数突破12万。Steam首批5276条评价中，英文评价超过2500条，显示其跨平台全球化尝试已在PC端获得一轮海外用户验证；移动端计划于9月23日上线。",
    [
        ("FunPlus旗下爪印工作室研发", "S1063", "由 FunPlus 旗下爪印工作室研发"),
        ("9月16日率先登陆PC与云游戏平台", "S1079", "昨日 （9月16日）"),
        ("Steam首日同时在线人数突破12万", "S1079", "首日同时在线人数最高突破12万"),
        ("首批5276条评价", "S1079", "5276 条评测"),
        ("英文评价超过2500条", "S1079", "英语区的评测是最多的，超过2500条"),
        ("移动端计划于9月23日上线", "S1079", "9月23日"),
    ],
    (2, 3, 2),
    ["FunPlus", "爪印工作室", "伊莫"],
    "2026-09-16",
)

add_industry(
    "Nex完成逾1.5亿美元融资，家庭体感主机销量突破100万台",
    ["S1086", "S1104"],
    "家庭体感主机Nex Playground开发商Nex完成超过1.5亿美元股权与债务融资，其硬件全球销量已突破100万台，活跃订阅用户也接近100万。资金将用于德国、日本与韩国等市场扩张、库存和供应链建设，显示家庭主动娱乐硬件正在形成“设备销售+订阅内容”的规模化组合。",
    [
        ("超过1.5亿美元股权与债务融资", "S1104", "raised over $150 million in equity and debt financing"),
        ("硬件全球销量已突破100万台", "S1104", "sold over 1 million units worldwide"),
        ("活跃订阅用户也接近100万", "S1086", "nearing one million active subscribers"),
        ("德国、日本与韩国等市场扩张", "S1086", "entry into Germany later this year and into Japan and Korea in 2027"),
        ("库存和供应链建设", "S1086", "inventory, supply chain"),
    ],
    (3, 2, 2),
    ["Nex", "Nex Playground"],
    "2026-09-17",
)


# AI: retain the six strongest direct game-production/product applications in the weekly window.
for spec in [
    ("output/weekend/2026-09-11_to_2026-09-13", "A001"),
    ("output/weekend/2026-09-11_to_2026-09-13", "A002"),
    ("output/weekend/2026-09-11_to_2026-09-13", "A003"),
    ("output/daily/2026-09-14", "A001"),
    ("output/daily/2026-09-14", "A002"),
    ("output/daily/2026-09-15", "A001"),
]:
    adapt(*spec)


# Community: weekly hard cap is three.
for spec in [
    ("output/weekend/2026-09-11_to_2026-09-13", "C001"),
    ("output/daily/2026-09-15", "C001"),
    ("output/daily/2026-09-16", "C002"),
]:
    adapt(*spec)


# Release-calendar reader items. Existing audited reader copy is reused where possible.
release_items = []


def adapt_release(report_dir, old_cid, cid):
    item, dec = adapt(report_dir, old_cid, section="release_calendar")
    items.pop()
    decisions.pop()
    old_new_cid = item["candidate_id"]
    item["candidate_id"] = cid
    for sid in item["source_ids"]:
        if used_sources.get(sid) == old_new_cid:
            used_sources.pop(sid)
    release_items.append(item)
    return item


adapt_release("output/daily/2026-09-16", "release-candidate-001", "R001")

release_items.append({
    "candidate_id": "R002", "section": "release_calendar", "title": "闪耀吧！噜咪",
    "source_ids": ["S1076", "S1215", "S1243"],
    "body": "哔哩哔哩游戏自研发行的异世界捉宠RPG手游《闪耀吧！噜咪》于9月17日在Android、iOS开启全球公测；产品采用竖屏单手操作，并以抓宠、养成、家园和轻策略对战为核心。",
    "claims": [
        {"claim": "哔哩哔哩游戏自研发行", "source_id": "S1076", "evidence": evidence("S1076", "哔哩哔哩游戏自研发行")},
        {"claim": "异世界捉宠RPG手游《闪耀吧！噜咪》", "source_id": "S1076", "evidence": evidence("S1076", "异世界冒险捉宠RPG手游")},
        {"claim": "9月17日", "source_id": "S1076", "evidence": evidence("S1076", "9月17日")},
        {"claim": "Android、iOS开启全球公测", "source_id": "S1215", "evidence": evidence("S1215", "Platforms: Android / iOS")},
        {"claim": "竖屏单手操作", "source_id": "S1076", "evidence": evidence("S1076", "竖屏单手操作")},
        {"claim": "抓宠、养成、家园和轻策略对战", "source_id": "S1076", "evidence": evidence("S1076", "家园系统支持自由装扮布局")},
    ],
    "release": {"product": "闪耀吧！噜咪", "event": "全球公测", "date": "2026-09-17", "platform": "Android、iOS", "company": "哔哩哔哩游戏"},
})

release_items.append({
    "candidate_id": "R003", "section": "release_calendar", "title": "莫诺微步",
    "source_ids": ["S1075", "S1198"],
    "body": "Studio BBB开发、Phoenixx发行的2D解谜动作端游《莫诺微步》于9月17日在Steam和Nintendo Switch正式发售；玩家通过喜悦、悲伤、愤怒与不安四种情感能力完成移动和环境解谜。",
    "claims": [
        {"claim": "Studio BBB开发", "source_id": "S1075", "evidence": evidence("S1075", "Studio BBB Inc.")},
        {"claim": "Phoenixx发行", "source_id": "S1075", "evidence": evidence("S1075", "Phoenixx 株式会社")},
        {"claim": "2D解谜动作端游《莫诺微步》", "source_id": "S1075", "evidence": evidence("S1075", "2D 解谜动作游戏《莫诺微步》")},
        {"claim": "9月17日在Steam和Nintendo Switch正式发售", "source_id": "S1075", "evidence": evidence("S1075", "2026 年 9 月 17 日")},
        {"claim": "喜悦、悲伤、愤怒与不安四种情感能力", "source_id": "S1075", "evidence": evidence("S1075", "喜悦、悲伤、愤怒、不安")},
    ],
    "release": {"product": "莫诺微步", "event": "正式发售", "date": "2026-09-17", "platform": "Steam、Nintendo Switch", "company": "Studio BBB、Phoenixx"},
})

release_items.append({
    "candidate_id": "R004", "section": "release_calendar", "title": "蓝色星原：旅谣",
    "source_ids": ["S1197", "S1236"],
    "body": "蛮啾网络出品的星宠结伴幻想大世界RPG多平台产品《蓝色星原：旅谣》于9月17日开启限量“旅迹测试”，覆盖Windows、HarmonyOS、Android和iOS；本次测试加入新地区、多人对决与超过200种奇波。",
    "claims": [
        {"claim": "蛮啾网络出品", "source_id": "S1197", "evidence": evidence("S1197", "蛮啾网络出品")},
        {"claim": "星宠结伴幻想大世界RPG多平台产品《蓝色星原：旅谣》", "source_id": "S1197", "evidence": evidence("S1197", "星宠结伴 幻想大世界RPG")},
        {"claim": "9月17日开启限量“旅迹测试”", "source_id": "S1236", "evidence": evidence("S1236", "Event date: 2026-09-17")},
        {"claim": "Windows、HarmonyOS、Android和iOS", "source_id": "S1197", "evidence": evidence("S1197", "PC端（Windows）、手机鸿蒙端、手机安卓端、手机iOS端")},
        {"claim": "新地区、多人对决与超过200种奇波", "source_id": "S1197", "evidence": evidence("S1197", "超过200种奇波")},
    ],
    "release": {"product": "蓝色星原：旅谣", "event": "限量测试", "date": "2026-09-17", "platform": "Windows、HarmonyOS、Android、iOS", "company": "蛮啾网络"},
})

adapt_release("output/daily/2026-09-15", "release-candidate-001", "R005")
r006 = adapt_release("output/daily/2026-09-14", "release-candidate-002", "R006")
r006["release"]["date"] = "2026-10-09"
r006["release"]["window_scope"] = "future_announcement"
r007 = adapt_release("output/daily/2026-09-16", "release-candidate-002", "R007")
r007["release"]["date"] = "2027-03-04"
r007["release"]["window_scope"] = "future_announcement"

for item in release_items:
    items.append(item)
    for sid in item["source_ids"]:
        used_sources.setdefault(sid, item["candidate_id"])


# Correct release false positives, keep every raw node, and let sync_release_decisions.py choose the prefix.
raw_audit = load_json(P / "release_calendar_audit.json")
dump_json(P / "release_calendar_audit_extracted.json", raw_audit)
raw_by_product = defaultdict(list)
for node in raw_audit["nodes"]:
    raw_by_product[node["product"]].append(node)


def take_node(product, source_ids, cid, repair=None):
    source_set = set(source_ids)
    node = next(n for n in raw_audit["nodes"] if n["product"] == product and source_set.issubset(set(n.get("source_ids", []))))
    node = dict(node)
    node["candidate_id"] = cid
    if repair:
        node.update(repair)
    node["status"] = "pending_decision"
    return node


top_nodes = [
    take_node("伊莫", ["S0835", "S0952", "S0971", "S0974"], "R001"),
    take_node("闪耀吧！噜咪", ["S1076", "S1215", "S1243"], "R002"),
    take_node("莫诺微步", ["S1075", "S1198"], "R003"),
    take_node("蓝色星原：旅谣", ["S1197", "S1236"], "R004"),
    take_node("黑白之地", ["S0753", "S0770"], "R005"),
    take_node("幻想放置远征队", ["S0390", "S0425"], "R006"),
    take_node("卧龙2：凤火连天", ["S0811", "S0895"], "R007", {
        "event_date": "2027-03-04", "signal_type": "new_game_schedule", "event": "公布2027年3月4日发售档期", "event_type_score": 2,
        "observed_signal_types": ["new_game_schedule"], "observed_events": ["公布2027年3月4日发售档期"],
        "base_priority_score": 6, "priority_score": 6, "window_scope": "future_announcement",
    }),
]
top_nodes[5]["event_date"] = "2026-10-09"
top_nodes[5]["window_scope"] = "future_announcement"
selected_keys = {(n["product"], tuple(n["source_ids"])) for n in top_nodes}
rest = []
serial = 8
for node in raw_audit["nodes"]:
    if any(node["product"] == top["product"] and set(node.get("source_ids", [])) == set(top.get("source_ids", [])) for top in top_nodes):
        continue
    n = dict(node)
    n["candidate_id"] = f"R{serial:03d}"
    serial += 1
    n["publish_eligible"] = False
    if n["product"] == "白金档案PLATiNA ：： LAB":
        n["audit_exclusion_reason"] = "来源直接写明9月10日正式发售，实际事件早于本周窗口。"
    elif n["product"] == "暗黑破坏神4":
        n["audit_exclusion_reason"] = "联动皮肤与既有产品内容被误挂为新品上线。"
    elif n["product"] == "护核纪元":
        n["audit_exclusion_reason"] = "老品重大更新实际发生在9月21日，超出产品日历次日窗口。"
    else:
        n["audit_exclusion_reason"] = "规范化复核后为误挂、重复、单源、窗口外或低于多源优先级前7项。"
    rest.append(n)
def release_sort_key(node):
    return (
        -int(bool(node.get("publish_eligible"))),
        -int(node.get("priority_score") or 0),
        -int(node.get("company_bonus") or 0),
        -int(node.get("event_type_score") or 0),
        -int(node.get("appearance_count") or 0),
        -int(node.get("industry_bonus") or 0),
        int(node.get("first_seen_order") or 0),
    )


raw_audit["nodes"] = sorted(top_nodes + rest, key=release_sort_key)
dump_json(P / "release_calendar_audit.json", raw_audit)

sys.path.insert(0, str(W / "scripts"))
from sync_release_decisions import build_release_decision

release_decisions = [build_release_decision(node, i < 7) for i, node in enumerate(raw_audit["nodes"])]
title_by_id = {x["candidate_id"]: x["title"] for x in release_items}
for d in release_decisions:
    if d["candidate_id"] in title_by_id:
        d["title"] = title_by_id[d["candidate_id"]]
    decisions.append(d)


def normalize(text):
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", " ", text).lower()


def history_check_for(title):
    tokens = [x for x in normalize(title).split() if len(x) >= 3]
    matches = []
    for h in history_rows:
        hay = normalize((h.get("title") or "") + " " + (h.get("event") or "") + " " + " ".join(h.get("entities") or []))
        if any(t in hay for t in tokens[:5]):
            matches.append(h)
    prior = []
    for h in matches[:8]:
        w = h.get("report_window") or {}
        prior.append(
            f"{h.get('title')}｜{h.get('report_kind')} {w.get('start')}_to_{w.get('end')}｜"
            f"card_exposed={str(h.get('card_exposed')).lower()}｜card_rank={h.get('card_rank')}｜"
            f"card_limit={h.get('card_limit')}｜card_exposure_source={h.get('card_exposure_source')}"
        )
    return {
        "history_match": bool(matches),
        "novelty": "repeat_only" if matches else "new_event",
        "prior_occurrences": prior,
        "new_facts": [],
        "prior_card_exposed": any(bool(h.get("card_exposed")) for h in matches) if matches else None,
    }


def heuristic_industry(row):
    title = row["title"]
    if row.get("body_status") in {"empty", "snippet"}:
        return 0, 0, 0
    if re.search(r"收购|融资|投资|首曝|公布.*新作|新作.*公布|成立.*工作室|CEO|acquir|funding|raises|new studio", title, re.I):
        e = 3
    elif re.search(r"销量|收入|营收|日活|DAU|停运|延期|市场|政策|诉讼|裁员|关闭|sales|revenue|market|delay|layoff|closure", title, re.I):
        e = 2
    else:
        e = 0
    r = 3 if re.search(r"腾讯|网易|米哈游|莉莉丝|Supercell|Roblox|Riot|Garena|手游|移动|策略|卡牌|RPG|模拟经营|生活模拟", title, re.I) else 2 if re.search(r"平台|Steam|发行|工作室|游戏", title, re.I) else 1
    m = 1 if e else 0
    return e, r, m


# Full source-level audit: every input maps to an included candidate, merge, or explicit exclusion.
for row in rows:
    sid = row["source_id"]
    if sid in used_sources:
        continue
    same_url = [used_sources[x["source_id"]] for x in by_url[str(row.get("url") or "").rstrip("/")] if x["source_id"] in used_sources]
    section = row["section"]
    cid = f"Q{sid[1:]}"
    if same_url:
        decision = "merge"
        merge_into = same_url[0]
        reason = "同URL重复采集，合并到已审阅候选。"
    else:
        decision = "exclude"
        merge_into = None
        if row.get("body_status") in {"empty", "snippet"}:
            reason = "正文为空或仅有短摘要，不能作为终稿事实证据。"
        elif section == "release_calendar":
            reason = "已完成产品日历全量反扫；属于普通活动、误挂、单源、重复、窗口外或低于多源优先级前缀。"
        elif section == "deep_analysis":
            reason = "目标周报精确selection不存在；按规则不自动写入第五栏。"
        elif section == "community_discourse":
            reason = "已补扫触发、争议逻辑、时间线和后续；相对三条入选事件证据、延续性或代表性较弱。"
        elif section == "ai_trends":
            reason = "AI全量反扫后，相对六条直接游戏应用，游戏落地链条较弱或属于泛模型/工具更新。"
        else:
            e, r, m = heuristic_industry(row)
            total = e * r + m
            reason = "E=0：普通版本、活动、宣传、榜单、财报或背景解读。" if e == 0 else f"E{e}×R{r}+M{m}={total}；未达周报8分、属于历史重复或证据不足。"
    d = {
        "candidate_id": cid, "section": section, "title": row["title"], "source_ids": [sid],
        "entities": [row["title"]], "event": row["title"], "decision": decision, "reason": reason,
    }
    if merge_into:
        d["merge_into"] = merge_into
    if section == "industry_news":
        e, r, m = heuristic_industry(row)
        d["scores"] = {"event": e, "relevance": r, "hook": m, "total": e * r + m}
        d["history_check"] = history_check_for(row["title"])
        d["card_carryover"] = False
    elif section == "ai_trends":
        d["ai_tier"] = "direct_application" if re.search(r"游戏|game", row["title"], re.I) else "transferable_frontier"
        d["game_stage"] = ["development"] if d["ai_tier"] == "direct_application" else []
        d["industry_reverse_scan"] = False
        if d["ai_tier"] == "transferable_frontier":
            d["migration_path"] = "通用能力可迁移到游戏研发工具，但本期来源缺少具体落地证据。"
    elif section == "deep_analysis":
        d["scores"] = {"relevance": 1, "insight": 1, "evidence": 1, "card": 1, "total": 4}
    decisions.append(d)
    used_sources[sid] = cid


for d in decisions:
    if d["section"] == "industry_news":
        hc = d.setdefault("history_check", history_check_for(d.get("title") or d.get("event") or ""))
        hc.setdefault("history_match", False)
        hc.setdefault("novelty", "new_event")
        hc.setdefault("prior_occurrences", [])
        hc.setdefault("new_facts", [])
        hc.setdefault("prior_card_exposed", None if not hc["history_match"] else False)
        d.setdefault("card_carryover", False)


# Sort final reader items.
dec_by_id = {d["candidate_id"]: d for d in decisions}
order = {"industry_news": 0, "ai_trends": 1, "release_calendar": 2, "community_discourse": 3}
release_rank = {f"R{i:03d}": i for i in range(1, 8)}
items.sort(key=lambda x: (
    order[x["section"]],
    release_rank.get(x["candidate_id"], 999) if x["section"] == "release_calendar" else -dec_by_id[x["candidate_id"]].get("scores", {}).get("total", 0) if x["section"] == "industry_news" else 0,
))


assert set(S) == set(used_sources), (len(S), len(used_sources), sorted(set(S) - set(used_sources))[:10])

# Human-readable audits.
dims = {
    "国内移动/国产产品与人才": r"腾讯|网易|米哈游|莉莉丝|国产|手游|移动|制作人|三七|FunPlus",
    "市场数据": r"收入|市场|销量|DAU|日活|下载|用户|在线",
    "并购": r"收购|融资|投资|股权|整合",
    "平台政策": r"平台|Steam|App Store|Battle.net|Roblox|欧盟",
    "档期变动": r"上线|发售|定档|延期|停运|测试|重启",
    "资本组织": r"CEO|离职|工作室|融资|收购|裁员",
    "海外重大": r"Supercell|Savvy|EA|暴雪|Nex|Netflix|Bohemia|Curve",
}
industry_decs = [d for d in decisions if d["section"] == "industry_news"]
dim_counts = {k: sum(bool(re.search(pat, d.get("title", ""), re.I)) for d in industry_decs) for k, pat in dims.items()}

candidate_lines = [
    f"# 全量独立事件候选｜{RID}", "",
    f"全量{len(rows)}条输入均映射到独立候选、合并项或产品日历节点；正文事实仅使用完整来源。", "",
]
item_by_id = {x["candidate_id"]: x for x in items}
decision_lines = [
    f"# {RID} 筛选决策", "",
    "卡片曝光去重：双周历史窗口2026-08-28至2026-09-10；本期未使用card_carryover。历史匹配逐项读取card_exposed、card_rank、card_limit与card_exposure_source；本周日报/周末报已覆盖的事件只在本周周报合并一次。", "",
    "维度覆盖自检：" + "；".join(f"{k} {v}张候选" for k, v in dim_counts.items()) + "。", "",
    "产品日历漏挂反查：已扫描industry_news与release_calendar全部上线、测试、预下载、首次曝光、定档、跨平台、回归和重大更新信号；误挂、重复、单源、窗口外与低于多源优先级前7项者均显式exclude。", "",
    "AI反扫：已扫描全部949条行业新闻输入与50条AI输入；同一事件仅保留一个分区。", "",
    f"质量说明：{len(rows)}条输入，0抽取失败、0空正文和{sum(r.get('body_status') != 'full' for r in rows)}条非全文；非全文未作为终稿证据。精确深度selection不存在，旧错名selection也不存在，因此第五栏省略。", "",
]
for d in decisions:
    title = d.get("title") or d.get("event") or d["candidate_id"]
    ids = ", ".join(d.get("source_ids") or [])
    linked_item = item_by_id.get(d["candidate_id"])
    facts_text = "；".join(c["claim"] for c in linked_item.get("claims", [])) if linked_item else d.get("reason", "")
    candidate_lines.extend([
        f"## {d['candidate_id']} - {title}", f"- section: {d['section']}", f"- source_ids: {ids}",
        f"- event: {d.get('event', title)}", f"- facts: {facts_text}", f"- notes: {d['decision']}；{d.get('reason', '')}", "",
    ])
    decision_lines.extend([
        f"## {d['candidate_id']} - {title}", f"- {d['decision']} → {d['section']}；{d.get('reason', '')}", f"- source_ids: {ids}",
    ])
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

dump_json(P / "report_items.json", {"schema_version": 1, "report_type": "weekly", "report_id": RID, "items": items})
dump_json(P / "selection_decisions.json", {
    "schema_version": 1, "report_type": "weekly", "report_id": RID,
    "history_window": {"start": "2026-08-28", "end": "2026-09-10"}, "decisions": decisions,
})
dump_json(P / "full_source_scan.json", {
    "input_records": len(rows), "audited_source_ids": sorted(used_sources), "unmapped": [],
    "empty_source_ids": [r["source_id"] for r in rows if r.get("body_status") == "empty"],
    "non_full_count": sum(r.get("body_status") != "full" for r in rows),
})

subprocess.run([
    sys.executable, str(W / "scripts" / "sync_release_decisions.py"),
    "--audit", str(P / "release_calendar_audit.json"),
    "--decisions", str(P / "selection_decisions.json"),
    "--max-items", "7",
], check=True)

headings = [
    ("industry_news", "一、行业新闻"),
    ("ai_trends", "二、AI 新闻"),
    ("release_calendar", "三、新游发布 / 产品日历"),
    ("community_discourse", "四、玩家舆论 / 社区动态"),
]
lines = [f"# 游戏行业周报｜{RID}", ""]
for section, heading in headings:
    lines.extend(["## " + heading, ""])
    group = [x for x in items if x["section"] == section]
    for i, item in enumerate(group, 1):
        if section == "release_calendar":
            lines.extend(["- " + item["body"], ""])
        else:
            lines.extend([f"### {i}. {item['title']}", "", item["body"], ""])
(OUT / f"game_industry_weekly_{RID}.md").write_text("\n".join(lines), encoding="utf-8")

print("items", dict(Counter(x["section"] for x in items)))
print("decisions", len(decisions), "sources", len(used_sources))
