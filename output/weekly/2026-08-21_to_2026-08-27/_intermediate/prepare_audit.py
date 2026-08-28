import json, sys, importlib.util, hashlib, re
from pathlib import Path
from datetime import date
P=Path(__file__).parent; W=Path.cwd(); START='2026-08-21'; END='2026-08-27'
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rows=[json.loads(x) for x in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
S={r['source_id']:r for r in rows}
support=W/'output/deep_observation_review/2026-08-21_to_2026-08-27_support'
hand={r['source_id']:r for r in map(json.loads,(support/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
deep=read(support/'report_items.json')['items']; imported=[]
for it in deep:
    mapping={sid:next(r['source_id'] for r in rows if r['url']==hand[sid]['url']) for sid in it['source_ids']}
    if it['candidate_id']=='C057':
        target=S[mapping[it['source_ids'][0]]]; original=dict(target)
        target.update(text=hand['S1010']['text'],body_status='full',extract_status='ok',text_chars=len(hand['S1010']['text']))
        target['text_sha256']=hashlib.sha256(target['text'].encode()).hexdigest()
        target['evidence_provenance']={'kind':'user_supplied_fulltext','provided_at':'2026-08-27','handoff_path':str(support/'C057_user_fulltext.md'),'original_body_status':original['body_status'],'original_text':original['text'],'original_sha1':original['sha1']}
        target['sha1']=hashlib.sha1(target['text'].encode()).hexdigest()
        imported.append({'source_id':target['source_id'],'url':target['url'],'original_chars':original['text_chars'],'imported_chars':target['text_chars'],'method':'Exact URL match; user-supplied body, not a successful network refetch.'})
    it['source_ids']=[mapping[x] for x in it['source_ids']]
    for c in it['claims']: c['source_id']=mapping[c['source_id']]
    it['candidate_id']='D'+it['candidate_id'][1:]; it['section']='deep'
write(P/'deep_handoff_import.json',{'selection':str(W/'output/deep_observation_review/2026-08-21_to_2026-08-27_selection.md'),'imports':imported,'items':deep})
(P/'report_inputs.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
spec=importlib.util.spec_from_file_location('extractor',r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\extract_report_inputs.py'); mod=importlib.util.module_from_spec(spec); sys.modules['extractor']=mod;spec.loader.exec_module(mod)
mod.write_index(P/'report_inputs.jsonl',rows)
quality=read(P/'source_quality_audit.json')
for r in quality['records']:
    src=S[r['source_id']];r.update(body_status=src['body_status'],text_chars=len(src['text']))
write(P/'source_quality_audit.json',quality)
summary=(P/'report_inputs_summary.md').read_text(encoding='utf-8').replace('Non-full body records: 193','Non-full body records: 192')
(P/'report_inputs_summary.md').write_text(summary+'\n## 人工证据补足与日历审计修订\n\n- S0671按精确URL导入用户提供全文，保留原414字摘要与来源记录；非联网补采。\n- 原抽取日历队列保留在上述摘要；最终规范化、日期修正和排序以release_calendar_audit.json及release_audit_repairs.json为准。\n',encoding='utf-8')
sys.path.insert(0,str(W/'scripts'))
from build_industry_history import collect_history
h=collect_history(W,date(2026,8,28));h['occurrences']=[o for o in h['occurrences'] if o['report_window']['start']>=START and o['report_window']['end']<=END]
write(P/'current_week_published_history.json',h)
rawpath=P/'release_calendar_audit_raw.json'
if not rawpath.exists(): write(rawpath,read(P/'release_calendar_audit.json'))
a=read(rawpath); nodes=a['nodes']; repairs=[]
def replace(product,ids,dt,signal,event,company=None):
    global nodes
    old=[n for n in nodes if n['product']==product or set(n['source_ids'])&set(ids)]
    # Replace only product aliases sharing evidence; record original nodes for audit.
    ids=list(dict.fromkeys(ids)); order=min([n.get('first_seen_order',9999) for n in old] or [int(ids[0][1:])])
    nodes=[n for n in nodes if n not in old]
    n={'product':product,'event_date':dt,'signal_type':signal,'event':event,'first_seen_order':order,'source_ids':ids,'focus_companies':[company[0]] if company else [],'company_evidence_ids':[company[1]] if company else [],'observed_signal_types':list(dict.fromkeys([x for o in old for x in o.get('observed_signal_types',[])] +[signal])),'observed_events':list(dict.fromkeys([x for o in old for x in o.get('observed_events',[])] +[event]))}
    nodes.append(n); repairs.append({'product':product,'source_ids':ids,'event_date':dt,'correct_signal':signal,'old_nodes':[o['candidate_id'] for o in old],'basis':'逐条读取source text，按真实产品及发生日聚类；定档不是上线，删除相关推荐造成的主体加分。'})
replace('诡秘之主',['S0034','S0036','S0056','S0374','S0189','S0211','S0261','S0326','S0636'],'2026-08-21','new_game_launch','正式公测')
replace('骤影·绯月杀',['S0368','S0606','S0644'],'2026-08-25','new_game_test','首次公开测试',('网易','S0644'))
replace('仙境传说3',['S0433','S1412','S1429'],'2026-08-27','new_game_test','重逢测试',('哔哩哔哩','S1412'))
replace('1666：阿姆斯特丹',['S0910','S0941','S1059','S1086','S1119','S1206'],'2026-08-25','new_game_launch','抢先体验上线')
replace('无限大',['S0929','S0936','S1018','S1023','S1053','S1142','S1246','S0867'],'2026-08-26','new_game_schedule','公布2027年1月15日上线档期',('网易','S0936'))
replace('源初之结',['S0892','S0930','S0933','S0937','S1016','S1082','S1114','S1147'],'2026-08-26','new_game_first_reveal','首次正式曝光',('米哈游','S0930'))
replace('异克斯小队',['S0931','S0940','S0965','S1019','S1021','S1140','S1229','S1238','S1404'],'2026-08-26','new_game_first_reveal','首次正式曝光',('腾讯','S0965'))
replace('王者万象棋',['S1305','S1310','S1422'],'2026-08-27','new_game_schedule','公布9月10日上线档期',('腾讯','S1310'))
replace('伊始之猫',['S0629','S0723','S0724','S0753','S0766'],'2026-08-25','new_game_first_reveal','首次曝光')
replace('魔法门之英雄无敌III重制版',['S0964','S1017','S1040','S1070','S1244','S1307','S1378'],'2026-08-26','new_game_first_reveal','首次公开重制项目')
replace('白金档案 PLATiNA ：： LAB',['S0017','S0047','S0253'],'2026-09-10','new_game_launch','中文正式版发售')
replace('伊莫',['S0870','S1138','S1254'],'2026-08-26','new_game_schedule','PC端9月16日、移动端9月23日上线定档')
replace('闪耀吧！噜咪',['S1249','S1426'],'2026-08-27','new_game_schedule','9月17日公测定档')
replace('公路英雄',['S0895','S0914','S1201'],'2026-08-26','new_game_schedule','2027年3月11日发售定档')
replace('坦克狂途',['S0915','S1067','S1202','S0869'],'2026-08-26','new_game_schedule','2027年1月15日发售定档')
replace('狂热运输3',['S0911','S1049','S1116','S1204'],'2026-08-26','new_game_schedule','9月29日发售定档')
replace('破坏领主2',['S1210','S1324'],'2026-08-27','new_game_first_reveal','首次公布；2027年抢先体验')
replace('LEGO Skylines',['S0909','S1048','S1089','S1205'],'2026-08-26','new_game_first_reveal','首次公布')
replace('Rainbow Six Tactics',['S0995','S1081'],'2026-08-26','new_game_first_reveal','首次公布')
replace('PUBG: DED.NET',['S1084','S1325'],'2026-08-26','new_game_first_reveal','首次公布')
replace('RollerCoaster Tycoon Wonderworks',['S1087'],'2026-08-26','new_game_first_reveal','首次公布')
replace('Tarae: The Unbound',['S1095'],'2026-08-26','new_game_first_reveal','首次公布')
replace('王国3：开疆拓土',['S1357'],'2026-08-27','new_game_first_reveal','首次公布')
replace('英雄绞碎场',['S0614','S0905'],'2026-08-25','new_game_first_reveal','首次公布')
replace('只狗：路边一条',['S0928'],'2026-08-26','new_game_first_reveal','首次公布')
replace('西游奇妙冒险',['S0774','S0850'],'2026-08-25','new_game_test','限量测试')
replace('新月大陆',['S1154','S1414'],'2026-08-27','new_game_launch','公测')
# Collapse exact product/date aliases left by the extractor; do not discard signals.
group={}
for n in nodes:
    key=(n['product'],n['event_date'])
    if key in group:
        other=group[key];other['source_ids']=list(dict.fromkeys(other['source_ids']+n['source_ids']))
    else:group[key]=n
nodes=list(group.values())
invalid={'赛博朋克：边缘行者2':'动画非游戏','异环':'既有流水财报并非新品定档','GTA6':'泄露及机制披露不是首次曝光或上线','影之刃零':'愿望单和预售数据不是上线','超自然行动组':'日活数据非新品上线','三角洲行动':'品类分析误挂产品','九阴真经：武侠':'后续实机PV非首次曝光','元梦之星':'常规祈愿','范式：起源':'新专辑非新品上线','王者荣耀体验服-新英雄王维':'体验服新英雄非新品','第五人格(官服)-1v4对抗':'时装活动','修仙时代':'招募不是已开测','一梦江湖':'正文主体是另一款新品','鬼武者 剑之道':'角色预告非跨平台上线','最终幻想 RESONANCE':'角色预告非跨平台上线','漫威金刚狼':'豪华版预告非跨平台','黎明行者之血':'性能模式预告','恶魔城：贝尔蒙特的诅咒':'配音预告','白银之城':'既有产品多人玩法PV非新品首曝','和平精英':'相关文章旧主体误召回','三国志·战略版':'历史灵犀新闻而非预下载'}
factors={'new_game_launch':3,'new_game_test':3,'new_game_launch_or_test':3,'new_game_preload':2,'new_game_first_reveal':2,'new_game_schedule':2,'old_cross_platform_launch':1,'old_relaunch':1,'old_major_update':1}
for n in nodes:
    ids=list(dict.fromkeys(n['source_ids']));n['source_ids']=ids
    # One independent source per identical URL OR identical full source text.
    urls=set();hashes=set();uniq=[]
    for sid in ids:
        r=S[sid]; text_hash=hashlib.sha1(re.sub(r'\s+','',r['text']).encode()).hexdigest()
        if r['url'] not in urls and text_hash not in hashes:uniq.append(sid)
        urls.add(r['url']);hashes.add(text_hash)
    n['independent_source_ids']=uniq;n['appearance_count']=len(uniq);n['appearance_score']=min(3,len(uniq))
    n['industry_ids']=[s for s in ids if S[s]['section']=='industry_news'];n['release_ids']=[s for s in ids if S[s]['section']=='release_calendar']
    n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus']
    n['event_type_score']=factors[n['signal_type']];n['company_bonus']=3 if n.get('focus_companies') and n['signal_type'].startswith('new_game_') else 0
    n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus']
    dt=n['event_date'];n['window_scope']='report_window' if START<=dt<=END else 'next_day_lookahead' if dt=='2026-08-28' else 'future_announcement' if n['signal_type'] in ['new_game_schedule','new_game_first_reveal'] else 'outside'
    n['window_eligible']=n['window_scope']!='outside';n['multi_source_eligible']=len(uniq)>=2
    n['publish_eligible']=n['window_eligible'] and n['multi_source_eligible'] and n['product'] not in invalid
    if n['product'] in invalid:n['audit_exclusion_reason']=invalid[n['product']]
    n['coverage']='industry+release' if n['industry_ids'] and n['release_ids'] else 'industry_only' if n['industry_ids'] else 'release_only'
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['event_type_score'],-n['company_bonus'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
for i,n in enumerate(nodes,1):n['candidate_id']=f'R{i:03d}'
a['nodes']=nodes;write(P/'release_calendar_audit.json',a);write(P/'release_audit_repairs.json',repairs)
for n in nodes[:18]: print(n['candidate_id'],n['product'],n['event_date'],n['signal_type'],n['priority_score'],n['appearance_count'],n['source_ids'])
