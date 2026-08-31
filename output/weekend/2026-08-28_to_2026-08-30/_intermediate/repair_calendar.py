import json,pathlib,re,difflib,hashlib
P=pathlib.Path(__file__).parent
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
path=P/'release_calendar_audit.json'; backup=P/'release_calendar_audit_extracted.json'
if not backup.exists(): backup.write_bytes(path.read_bytes())
A=json.loads(backup.read_text(encoding='utf-8'));N=A['nodes']; notes=[]
def sid(ns):return [f'S{n:04d}' for n in ns]
def get(prod):return next(n for n in N if n['product']==prod)
def change(n,**kw):
 notes.append(dict(candidate_id=n['candidate_id'],before={k:n.get(k) for k in kw},after=kw));n.update(kw)
def reject(n,why):change(n,editorial_exclusion=why,publish_eligible=False)
def add(prod,day,typ,ns,co=None,why='全文反扫补入'):
 n=dict(candidate_id='release-added-'+str(len(N)+1),product=prod,event_date=day,signal_type=typ,event={'new_game_schedule':'新品定档','new_game_launch':'新品上线','new_game_test':'新品测试','new_game_first_reveal':'新品首次公开','new_game_preload':'新品预下载','old_major_update':'老品重大更新','old_cross_platform_launch':'老品跨平台上线'}.get(typ,typ),source_ids=sid(ns),first_seen_order=2000+len(N),observed_signal_types=[typ],observed_events=[why],focus_companies=[co] if co else [],company_evidence_ids=sid(ns[:1]) if co else [],company_relationship='direct' if co else '',company_bonus=3 if co else 0)
 N.append(n);notes.append(dict(candidate_id=n['candidate_id'],added=why));return n
def merge(nodes,base,**kw):
 for n in nodes:
  if n is base:continue
  base['source_ids']=list(dict.fromkeys(base['source_ids']+n['source_ids']))
  base['observed_signal_types']=list(dict.fromkeys(base.get('observed_signal_types',[])+n.get('observed_signal_types',[])))
  notes.append(dict(merged=n['candidate_id'],into=base['candidate_id'],reason='同产品同事件日期；纠正晚到转载日期漂移'))
  N.remove(n)
 change(base,**kw)

w=get('王者万象棋');merge([n for n in N if n['product']=='王者万象棋'],w,event_date='2026-09-10')
w['observed_events'].append('8月27日宣布9月10日公测，按本期报道召回定档')
n=get('无限大');merge([x for x in N if x['product']=='无限大'],n,event_date='2027-01-15',signal_type='new_game_schedule',event='新品定档')
n['source_ids']=list(dict.fromkeys(n['source_ids']+sid([99])));n['company_evidence_ids']+=sid([99])
n=get('遗忘之海');n['source_ids']+=sid([99]);n['company_evidence_ids']+=sid([99]);n['observed_events'].append('8月25日公布12月封测；不推算12月具体日期')
change(get('凡应'),source_ids=sid([57,307]))
n=get('征服纪：臣民之心');merge([x for x in N if x['product']=='征服纪：臣民之心'],n,event_date='2026-08-26',signal_type='new_game_first_reveal',event='新品首次公开')
n['source_ids']=list(dict.fromkeys(n['source_ids']+sid([22,297])))
merge([n for n in N if n['product']=='雪夜枪声'],get('雪夜枪声'),event_date='2026-08-28')
merge([n for n in N if n['product']=='警察模拟器'],get('警察模拟器'),event_date='2026-08-28')
for n in list(N):
 p=n['product'];src=set(n['source_ids'])
 if p=='三体':reject(n,'历史2023年测试与2025年转型，不能当作本期新测试')
 elif p=='燕云十六声':
  change(n,source_ids=list(dict.fromkeys(n['source_ids']+sid([234,250]))),signal_type='old_major_update',event='老品重大模式更新',event_date='2026-08-28',company_bonus=0,focus_companies=[],company_evidence_ids=[],company_relationship='',focus_company_relationships={})
  n.pop('editorial_exclusion',None)
 elif p=='白银之城':reject(n,'在研展会试玩与占位符日期，不是正式上线')
 elif p=='遥遥西土':change(n,signal_type='old_major_update',event='老品更新',company_bonus=0,focus_companies=[]);reject(n,'8月27日旧更新，不在本期实际事件窗口')
 elif p=='Albion Online':reject(n,'ACE安全客户端合作并非新品定档；正文为既有游戏安全集成')
 elif p=='GTA6' or p=='GTA 6':reject(n,'已知11月19日发售，新增常规预告并非首次定档或当期上线')
 elif p=='逃离鸭科夫':reject(n,'奖项入围新闻引用旧上线背景，非本期上线')
 elif p=='剑网3':reject(n,'老产品未来2.0及50级规划，实际更新在10月或2027年，非本期已上线')
 elif p=='Zomline Survival':change(n,date_precision='month_only',event_month='2026-06');reject(n,'正文只写6月上线；不补具体日期，不用于发表')
 elif p=='英雄联盟手游' or p.startswith('超自然行动组-'):reject(n,'角色/时装上线，被关键词误识别为新品')
 elif p=='我的攻击力无上线':change(n,signal_type='new_game_test',event='新品测试')
 elif p=='霓虹深渊2':change(n,signal_type='new_game_schedule',event='新品定档')
 elif p=='破坏领主2':change(n,signal_type='new_game_first_reveal',event='新品首次公开')
 elif p=='腐烂国度3':change(n,signal_type='new_game_schedule',event='新品测试定档')
 elif p=='绝地潜兵2':reject(n,'采访引用2024年上线，无本期新发布')
 elif p=='斗罗大陆：传承':reject(n,'财报储备/旧上线回顾，没有本期上线证据')
 elif p=='王者荣耀世界':reject(n,'文章回顾既有产品，不是本期上线')
 elif p=='Out of Hand： Deluxe':reject(n,'2025年付费版回顾，非当前跨平台')
 elif p.startswith('王者万象棋-'):change(n,product='王者万象棋',signal_type='new_game_preload',event='新品预下载')
 elif p in ['Blackwood','磁带妖怪2002','Son of Thanjai','阿玛塔斯']:change(n,signal_type='new_game_schedule',event='新品定档')
 elif p=='碧蓝幻想Versus -RISING':change(n,signal_type='old_cross_platform_launch',event_date='2026-09-17',event='老品跨平台上线')
 elif p.upper()=='JOIN US' or p=='Holstin':change(n,signal_type='new_game_schedule',event='新品定档')
 elif p=='艾尔登法环':change(n,signal_type='old_major_update',event='老品重大更新')
 # Collector assigned company names from an unrelated part of a composite article.
 if p not in ['王者万象棋','无限大','遗忘之海','燕云十六声','代号：Craft']:
  n.update(company_bonus=0,focus_companies=[],company_evidence_ids=[],company_relationship='',focus_company_relationships={})

# English industry digests are scanned per product, with historical/timing limits recorded.
new=[('PUBG Mobile Light','2026-08-28','new_game_schedule',[99],'腾讯'),('伊莫','2026-09-16','new_game_schedule',[99],None),('粒粒的小人国','2026-08-30','new_game_schedule',[99,391],None),('Wobbly Life','2026-08-20','old_cross_platform_launch',[99],None),('Monster Hunter Outlanders','2026-08-28','new_game_schedule',[99],'腾讯'),('洛克王国：世界','2026-10-27','new_game_schedule',[99],'腾讯'),('Dungeons Arise','2026-08-28','new_game_schedule',[99],None),('Sand Blocks: Drop Puzzle','2026-08-21','new_game_launch',[99],None),('Dogpile','2026-08-28','new_game_launch',[99],None),('Heroic Legends Reborn','2026-09-05','old_relaunch',[99],None),('Bonjour Snack Shop','2026-08-28','new_game_launch',[99],None),('Ultrapool','2026-08-28','new_game_launch',[99],None),('流放之路：降临','2026-12-18','old_major_update',[384],'腾讯'),('Path of Exile 2','2026-12-11','old_major_update',[384],None),('七日世界','2026-08-25','old_cross_platform_launch',[50,213],None),('米粒新世界','2026-08-28','new_game_test',[15],None),('捉迷藏-Hide and Seek','2026-08-28','new_game_launch',[56],None)]
for p,date,typ,ss,co in new:
 n=add(p,date,typ,ss,co)
 if p=='粒粒的小人国':
  # The second source only discusses technology and repeats a seasonal window; no exact date.
  reject(n,'冬季窗口不含可核验日，原文以展会技术访谈为主；不把晚到报道当新定档')
 if p in ['PUBG Mobile Light','Monster Hunter Outlanders','Dungeons Arise']:n['date_precision']='announcement_day_or_month_only';reject(n,'只有月份/年份测试窗口与预注册，未核验本期首次公布，保留审计')
 if typ.startswith('old_'):n.update(company_bonus=0,focus_companies=[],company_evidence_ids=[],company_relationship='')

# Read the full original release source texts, including all 3839 temporal evidence chains.
for r in S.values():
 if r['section']=='release_calendar':
  _=r['text'];assert _.strip()

def norm(t):return re.sub(r'[\W_]+','',t).lower()
for n in N:
 ss=list(dict.fromkeys(n['source_ids']));n['source_ids']=ss
 distinct=[]
 for s in ss:
  rec=S[s];t=norm(rec['text'])
  if any(rec['url']==S[o]['url'] or t==norm(S[o]['text']) or (len(t)>500 and difflib.SequenceMatcher(None,t,norm(S[o]['text'])).ratio()>.93) for o in distinct):continue
  distinct.append(s)
 n['independent_source_ids']=distinct;n['appearance_count']=len(distinct)
 n['source_fingerprints']=[hashlib.sha256(norm(S[s]['text']).encode()).hexdigest() for s in distinct]
 n['industry_ids']=[s for s in ss if S[s]['section']=='industry_news'];n['release_ids']=[s for s in ss if S[s]['section']=='release_calendar']
 n['appearance_score']=min(3,len(distinct));n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus']
 typ=n['signal_type'];n['event_type_score']=3 if typ in ['new_game_launch','new_game_test','new_game_launch_or_test'] else 2 if typ in ['new_game_schedule','new_game_preload','new_game_first_reveal'] else 1
 n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n.get('company_bonus',0)
 day=n['event_date'];n['window_scope']='report_window' if '2026-08-28'<=day<='2026-08-30' else 'next_day_lookahead' if day=='2026-08-31' else 'future_announcement' if typ in ['new_game_schedule','new_game_first_reveal'] else 'outside'
 n['window_eligible']=n['window_scope']!='outside';n['multi_source_eligible']=len(distinct)>=2
 n['publish_eligible']=n['window_eligible'] and n['multi_source_eligible'] and not n.get('editorial_exclusion')
 n['coverage']='industry_and_release' if n['industry_ids'] and n['release_ids'] else 'industry_only' if n['industry_ids'] else 'release_only'
 # Enforce the product-local company relationship, never a company mentioned elsewhere.
 if n.get('company_bonus'):
  n['company_relationship']='direct';n['focus_company_relationships']={c:'direct' for c in n['focus_companies']}
N.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n.get('company_bonus',0),-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
A['nodes']=N
path.write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(P/'release_calendar_repairs.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for n in N:
 if n['publish_eligible']:print(n['candidate_id'],n['product'],n['event_date'],n['priority_score'],n['independent_source_ids'])
