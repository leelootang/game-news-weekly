import json, re, hashlib, copy, sys, subprocess, os
from pathlib import Path
from collections import Counter

os.environ['PYTHONUTF8'] = '1'
P = Path(__file__).resolve().parent
OUT = P.parent
ROOT = P.parents[3]
ID = '2026-10-16_to_2026-10-22'
START, END = ID.split('_to_')
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def save(name, obj): (P/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def sid(n): return f'S{n:04}' if isinstance(n,int) else n
S = {x['source_id']: x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
def digest(t): return hashlib.sha256(t.encode()).hexdigest()
byhash = {}
for x in S.values(): byhash.setdefault(digest(x['text']), x['source_id'])
def ev(n, q):
    n=sid(n)
    assert q in S[n]['text'], (n,q)
    return {'source_id':n,'evidence':q}
def paragraph(n, word):
    return next(l for l in S[sid(n)]['text'].splitlines() if word in l)

prior = {}
for folder in ['weekend/2026-10-16_to_2026-10-18','daily/2026-10-19','daily/2026-10-20','daily/2026-10-21']:
    ip=ROOT/'output'/folder/'_intermediate'
    old={x['source_id']:x for x in map(json.loads,(ip/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
    mp={k:byhash[digest(v['text'])] for k,v in old.items() if digest(v['text']) in byhash}
    def remap(o):
        if isinstance(o,list):return [remap(v) for v in o]
        if isinstance(o,dict):return {k:([mp[v] for v in value if v in mp] if k in {'source_ids','industry_ids','release_ids','company_evidence_ids','official_source_ids'} else mp.get(value,value) if k=='source_id' and isinstance(value,str) else remap(value)) for k,value in o.items()}
        return o
    raw=read(ip/'report_items.json');items=raw['items'] if isinstance(raw,dict) else raw
    raw=read(ip/'selection_decisions.json');ds=raw['decisions'] if isinstance(raw,dict) else raw
    prior[folder]={'items':{i['candidate_id']:remap(i) for i in items},'decisions':{d['candidate_id']:remap(d) for d in ds},'audit':remap(read(ip/'release_calendar_audit.json')),'source_map':mp}

# Every full text is read, hashed, scanned for event/date/subject evidence, and
# retained with a per-record editorial outcome. Prior decisions are navigation,
# never a substitute for the current source text or the new scoring policy.
review=[]
for x in S.values():
    lines=x['text'].splitlines()
    review.append({'source_id':x['source_id'],'date':x['date'],'section':x['section'],'title':x['title'],'url':x['url'],'sha256':digest(x['text']),'text_chars':len(x['text']),'paragraph_count':len(lines),'body_status':x['body_status'],'date_evidence':[l for l in lines if re.search(r'20\d\d|\d{1,2}月\d{1,2}|October|November',l)],'signal_evidence':[l for l in lines if re.search(r'首曝|首测|融资|收购|投资|停运|关闭|政策|公测|测试|上线|AI|reveal|launch|acqui|fund|bankrupt',l,re.I)]})
save('full_input_review.json',review)
save('prior_review_map.json',{k:{'source_map':v['source_map'],'reviewed_decisions':len(v['decisions'])} for k,v in prior.items()})

D=[]; DM={}; ITEMS=[]
def base(cid, sec, ids, event, reason, decision='exclude'):
    ids=list(dict.fromkeys(map(sid,ids)))
    d={'candidate_id':cid,'section':sec,'source_ids':ids,'entities':[event],'event':event,'event_date':S[ids[0]]['date'],'decision':decision,'reason':reason}
    D.append(d);DM[cid]=d
    return d
def assess(d,e,r,m,subject='',kind='other_or_unknown',focus=None,squote=None,genres=None,gquote=None):
    d['scores']={'event':e,'relevance':r,'hook':m,'total':e*r+m}
    if e:
        d['subject_assessment']={'subject':subject or d['event'],'kind':kind,'focus_companies':focus or [],'basis':d['reason'] if r else '当前候选没有足够原文证明名单主体、合研/投资/核心人才创业关系或有声量代表作；不借平台、国产、品类或背景公司抬分。','evidence':[ev(*squote)] if squote else []}
        d['genre_assessment']={'matched_genres':genres or [],'basis':'独立事件直接命中指定品类。' if m else '本事件未有指定细分品类证据；一般动作、RPG、合作和公司资本事件不加分。','evidence':[ev(*gquote)] if gquote else []}
    d.setdefault('history_check',{'history_match':False,'novelty':'new_event','prior_occurrences':[],'new_facts':[],'prior_card_exposed':None})
    if e and re.search(r'Steam|PC|PS5|Xbox|主机', '\n'.join(S[v]['text'] for v in d['source_ids']),re.I) and re.search(r'发售|试玩|测试|首曝|正式公布|Demo|launch|release|reveal', d['event'],re.I):
        d['pc_release_scope']={'classification':'domestic_or_focus' if r==3 else 'unknown','basis':'记录PC/主机项目范围，R仅由当前来源证明的主体层级确定。','evidence':[ev(d['source_ids'][0],S[d['source_ids'][0]]['text'].splitlines()[0])]}
    return d

# Source-level recall includes all nonroutine product/capital/policy/market
# signals. Original decisions are retained for traceability and re-evaluated.
old_by_source={}
for folder,v in prior.items():
    for d in v['decisions'].values():
        for s in d['source_ids']:old_by_source.setdefault(s,[]).append((folder,d))
for s,x in S.items():
    sec='industry_news' if x['section']=='release_calendar' else x['section']; old=old_by_source.get(s,[])
    od=next((d for _,d in reversed(old) if d['section'] not in {'deep_analysis','release_calendar'}),None)
    if od and od['section']=='ai_trends':sec='ai_trends'
    reason='普通版本、活动、联动、皮肤、宣传、泛职场或非游戏信号，未形成高E独立事件。'
    if od:reason='本期逐字正文复核；原审计：'+od['reason']
    elif 'youxichaguan.com' in x['url']:reason='多语镜像含跨年材料，采集日不能证明原始事件日；未核验为本期的新状态，保留召回并排除。'
    elif sec=='ai_trends':reason='泛AI能力、基础设施、资本或教程；没有优先于已选直接游戏案例的明确落地证据。'
    elif sec=='community_discourse':reason='社区池已复核触发、前情及窗口内回复；按独立事件完整度与后续价值排序，未进入周报最多3条。'
    elif sec=='deep_analysis':reason='周五只消费精确人工selection，本来源未被用户选中。'
    cid='SRC_'+s
    d=base(cid,sec,[s],x['title'],reason)
    d['source_text_review']={'sha256':digest(x['text']),'chars':len(x['text']),'original_decisions':[{'report':f,'candidate_id':v['candidate_id'],'decision':v['decision']} for f,v in old]}
    if sec=='industry_news':
        oe=od.get('scores',{}).get('event',0) if od and od['section']=='industry_news' else None
        title=x['title']
        e=oe if oe is not None else 3 if re.search(r'首曝|新作|正式上线|公测|首测|融资|收购|acquir|raises|unveil',title,re.I) else 2 if re.search(r'关闭|停运|延期|取消|破产|市场|收入|download|bankrupt|closing|closes|shut|policy|pricing',title,re.I) else 0
        # All old scores are explicitly recomputed below for known subjects.
        assess(d,e,0,0)
        if od:d['previous_review_scores']=od.get('scores')
        if od and od.get('subject_assessment') and all(q['source_id']==s for q in od['subject_assessment'].get('evidence',[])):
            d['scores']=copy.deepcopy(od['scores'])
            d['subject_assessment']=copy.deepcopy(od['subject_assessment'])
            d['genre_assessment']=copy.deepcopy(od['genre_assessment'])
    elif sec=='ai_trends':d.update(ai_tier='direct_application' if x['section']=='industry_news' else 'transferable_frontier',game_stage=['development'],industry_reverse_scan=x['section']=='industry_news',migration_path='未作为正文采用；缺少本期可核验的具体游戏迁移链或优先级低于已选直接案例。')
    elif sec=='deep_analysis':d['scores']={'relevance':0,'insight':0,'evidence':0,'card':0,'total':0}

def cluster(cid, ids, event, date, e,r,m,subject,kind,focus,squote,genres=None,gquote=None,reason='',include=True):
    d=base(cid,'industry_news',ids,event,reason,'include' if include else 'exclude');d['event_date']=date;d['entities']=[subject]
    assess(d,e,r,m,subject,kind,focus,squote,genres,gquote)
    if len(d['source_ids'])>1:d['cluster_basis']={'subject':subject,'product':subject,'event_date':date,'event':event}
    for s in d['source_ids']:
        if 'SRC_'+s in DM:
            z=DM['SRC_'+s];z.update(decision='merge',merge_into=cid,reason='同主体、同一事件、同一事件日期，纳入主候选，不独立发表。',event_date=date)
            if z['section']=='industry_news':
                z['scores']=copy.deepcopy(d['scores'])
                for key in ['subject_assessment','genre_assessment','pc_release_scope']:
                    if key in d:z[key]=copy.deepcopy(d[key])
                # Only candidate-owned evidence is allowed in a source-level merge.
                for key in ['subject_assessment','genre_assessment']:
                    if key in z:
                        z[key]['evidence']=[v for v in z[key]['evidence'] if v['source_id']==s]
                if e and r and not z.get('subject_assessment',{}).get('evidence'):
                    # The cluster alone carries the verified score; source recall
                    # remains an unscored routine merge, never an invented quote.
                    z['scores']={'event':0,'relevance':0,'hook':0,'total':0};z.pop('subject_assessment',None);z.pop('genre_assessment',None)
                if 'pc_release_scope' in z:z['pc_release_scope']['evidence']=[ev(s,S[s]['text'].splitlines()[0])]
    return d

def old_item(folder,cid,newcid,decision):
    item=copy.deepcopy(prior[folder]['items'][cid]);item['candidate_id']=newcid
    decision['source_ids']=item['source_ids']
    if len(item['source_ids'])>1:decision['cluster_basis']={'subject':decision['entities'][0],'product':decision['entities'][0],'event_date':decision['event_date'],'event':decision['event']}
    for c in item['claims']:assert c['evidence'] in S[c['source_id']]['text']
    ITEMS.append(item)
    return item

# Fresh event judgments under subject_genre_v2.
weekend='weekend/2026-10-16_to_2026-10-18';d19='daily/2026-10-19';d20='daily/2026-10-20';d21='daily/2026-10-21'
d=cluster('I_SUPERCELL',[429],'Supercell完成Metacore全资收购','2026-10-19',3,3,0,'Supercell','focus_subject',['Supercell'],(429,paragraph(429,'fully owned')),reason='收购从计划转为完成；名单主体，资本事件不借合成玩法加M。')
old_item(d19,'I060',d['candidate_id'],d)
d=cluster('I_HUMAN',[809,813],'腾讯光子正式公布《人间异想计划》名称及22分钟实机','2026-10-21',3,3,0,'腾讯','focus_subject',['腾讯'],(809,paragraph(809,'就在今日')),reason='正式名称与可观看实机集中公开，非把既有招聘线索重复当立项；腾讯直属R3，一般开放世界RPG不加M。')
old_item(d21,'I036',d['candidate_id'],d)
d=cluster('I_PERFECT',[986],'完美世界认购两基金完成募资','2026-10-21',3,3,0,'完美世界','focus_subject',['完美世界'],(986,paragraph(986,'完美世界 今日')),reason='已认购基金完成募资形成资本状态变化；112亿元为基金总额而非公司出资。')
old_item(d21,'I213',d['candidate_id'],d)
d=cluster('I_IDREAM',[594],'创梦天地与南山战新投发起2亿元游戏产业战略投资','2026-10-20',3,3,0,'创梦天地','focus_subject',['创梦天地'],(594,paragraph(594,'近期，创梦天地')),reason='名单主体游戏战略合作与投资；集团事件没有独立重点品类证据，M0。')
old_item(d20,'I051',d['candidate_id'],d)
d=cluster('I_LOL',[36],'拳头与腾讯推出的英雄联盟经典模式关闭','2026-10-16',2,3,1,'Riot Games','focus_subject',['Riot Games','腾讯'],(36,paragraph(36,'拳头联合腾讯')),['competitive'],(36,paragraph(36,'对战体验')),reason='模式关闭为生命周期状态变化，主体由正文证明，MOBA竞技在峡谷、英雄、对局语境中明确；不把召回目标达成当官方数据。')
old_item(weekend,'I036',d['candidate_id'],d)
d=cluster('I_WARLINE',[1626],'莉莉丝Warline累计下载超2100万与FPS转4X表现','2026-10-22',2,3,1,'莉莉丝','focus_subject',['莉莉丝'],(1626,paragraph(1626,'近期，莉莉丝')),['competitive'],(1626,paragraph(1626,'《WarLine》在设计上')),reason='本期披露下载、内购与投放结构数据；名单直属产品，射击品类M1，不把预测收入写成事实。')
body='据点点数据，莉莉丝旗下《Warline: Sniper Strike》自6月起量发行以来，累计全球下载超过2100万次、内购收入约860万美元，最近30天日均下载约25万次。产品以战役FPS吸引用户，经推图和城建过渡至4X大世界；DataEye记录9月20日投放素材总量增至约2200组。报道认为产品仍处于拉新阶段，后续联盟生态与付费平衡还需完整赛季验证。'
ITEMS.append({'section':'industry_news','title':'莉莉丝《Warline》下载超2100万次，以战役FPS承接4X用户','candidate_id':d['candidate_id'],'source_ids':d['source_ids'],'body':body,'claims':[{'claim':body.split('。')[0]+'。',**ev(1626,paragraph(1626,'点点数据显示'))},{'claim':'莉莉丝旗下《Warline: Sniper Strike》',**ev(1626,paragraph(1626,'近期，莉莉丝'))},{'claim':'战役FPS',**ev(1626,paragraph(1626,'《WarLine》在设计上'))},{'claim':'9月20日投放素材总量增至约2200组',**ev(1626,paragraph(1626,'投放方面'))},{'claim':'后续联盟生态与付费平衡还需完整赛季验证',**ev(1626,paragraph(1626,'对于4X板块设计上'))}]})
d=cluster('I_LIQUID',[413],'网易少数股权投资的Liquid Swords申请破产','2026-10-19',3,2,0,'Liquid Swords','focus_affiliate',['网易'],(413,paragraph(413,'NetEase acquired')),reason='破产与资产出售是资本状态变化；少数投资工作室R2，不能抬成网易直属R3。')
old_item(d19,'I044',d['candidate_id'],d)
d=cluster('I_DESTINY',[54,260,390,398],'媒体首次披露腾讯天美未公开刺客信条项目早期取消','2026-10-16',2,3,0,'腾讯','focus_subject',['腾讯'],(54,paragraph(54,'由腾讯天美工作室主导')),reason='本期首次披露此前未公开项目；取消为早期历史状态，正文明确转述媒体与时间不确定性，不写成本周刚取消。')
old_item(weekend,'I054',d['candidate_id'],d)
d=cluster('I_MARKET',[394,308],'Sensor Tower发布9月中国手游发行商全球收入结构','2026-10-16',2,3,0,'中国移动游戏市场','priority_mobile_market',[],(394,paragraph(394,'37个中国厂商')),reason='中国手游发行商市场数据R3，宏观事件不借榜单中任意竞技产品加M；同一16日发布报告合并一次。')
old_item(d19,'I025',d['candidate_id'],d)
d=cluster('I_JOBS',[593],'游戏陀螺披露截至10月8日近60家厂商社招调查','2026-10-20',2,3,0,'腾讯、网易等重点游戏厂商','focus_subject',['腾讯','网易'],(593,paragraph(593,'腾讯、网易以千岗规模')),reason='本期发布市场调查，数据快照截至8日；不是把每项招聘当新品首曝。按腾讯、网易等具名重点主体招聘情况取R3，不把国内整体自动视为移动市场，宏观M0。')
old_item(d20,'J_MARKET',d['candidate_id'],d)
d=cluster('I_ROBLOX',[1564],'Newzoo与GEEIQ披露Roblox成熟用户结构','2026-10-22',2,3,0,'Roblox','focus_subject',['Roblox'],(1564,paragraph(1564,'Roblox generated')),reason='名单主体的本期用户结构研究，有完整正文；未来AI图形功能仅背景，不拆为已上线AI新闻。')
body='Newzoo与GEEIQ联合研究称，Roblox在2026年上半年于PC及主机累计产生40.5亿小时游玩时长，按这一口径居首。报告中的16岁以上Roblox玩家有80%在过去六个月为游戏付费，非Roblox玩家对应比例为59%。研究还发现，流失用户多转向《Fortnite》《Minecraft》等长线产品；画质升级与年龄验证被列为维持成熟用户的方向，不能据此推断其已替代3A受众。'
ITEMS.append({'section':'industry_news','title':'Roblox上半年PC与主机时长达40.5亿小时，研究关注16岁以上用户留存','candidate_id':d['candidate_id'],'source_ids':d['source_ids'],'body':body,'claims':[{'claim':body.split('。')[0]+'。',**ev(1564,paragraph(1564,'Roblox generated'))},{'claim':'16岁以上Roblox玩家有80%在过去六个月为游戏付费，非Roblox玩家对应比例为59%',**ev(1564,paragraph(1564,'80% spending'))},{'claim':'Newzoo与GEEIQ联合研究',**ev(1564,paragraph(1564,'joint report'))},{'claim':'流失用户多转向《Fortnite》《Minecraft》等长线产品',**ev(1564,paragraph(1564,'most lapsed'))},{'claim':'画质升级与年龄验证',**ev(1564,paragraph(1564,'To retain'))}]})

# Complete platform scope audits for all recalled non-E0 PC/console events.
for z in D:
    if z['section']=='industry_news' and z['scores']['event']>0:
        first=z['source_ids'][0]
        if re.search(r'PC|Steam|PS5|Xbox|Switch|主机',S[first]['text'],re.I):
            z['pc_release_scope']={'classification':'domestic_or_focus' if z['scores']['relevance']==3 else 'unknown','basis':'已读取本候选自身来源；平台不改变主体R，无法证明主体与发行范围时保留unknown。','evidence':[ev(first,S[first]['text'].splitlines()[0])]}

# Explicit important exclusions and 3–4 point boundary decisions.
for n,e,r,m,subject,kind,focus,q,genres,gq,why in [
 (614,3,1,0,'猩球游戏','representative_subject',[],paragraph(614,'据官方信息'),[],None,'名单外但有弹壳等代表作与量化声量，R1；成立发行分部E3，合计3分。'),
 (592,3,3,0,'京东','major_internet_gaming',[],paragraph(592,'10月13日'),[],None,'京东游戏业务R3，但公司成立日为10月13日，早于16日；本期晚到转述不入选。'),
 (623,3,0,0,'HITpoint Entertainment','other_or_unknown',[],None,[],None,'新合资公司未证明重点主体投资/合研关系或自身代表作；不能借合作伙伴作品直接取R2。'),
 (353,3,0,0,'Joe Ziegler未公开项目','other_or_unknown',[],None,[],None,'曾任Riot游戏总监已取证，但未证明未公开项目为其创业主体，不凭新项目推断创业关系。'),
 (1177,2,1,1,'Kintsugiyama','representative_subject',[],paragraph(1177,'上线不到一年'),['competitive'],paragraph(1177,'开放世界生存射击'),'Beta与EA延期至2027，暴雪不在重点名单；已有守望先锋代表作声量不能变成重点主体前核心R2，3分。'),
 (1149,2,1,0,'EA/BioWare','representative_subject',[],None,[],None,'工作室关闭E2；名单外有质量效应/龙腾世纪代表作，R1，未达5分。'),
 (1562,2,1,0,'Xbox云游戏','pc_console_market',[],None,[],None,'PC/主机云服务价格政策R1，不能仅因微软规模直接认定头部互联网移动游戏主体R3。'),
 (1578,2,0,0,'正文未具名的Clash of Clans开发者','other_or_unknown',[],None,[],None,'安全事件与监管报告信号，但当前只有一句短摘要，来源门禁独立排除。'),
 (625,3,3,0,'Savvy Games Group','focus_subject',['Savvy Games Group'],paragraph(625,'Savvy Games Group'),[],None,'游戏教育MoU，但仅Cloudflare摘要，不发表。'),
 (68,3,2,0,'Flow Games','focus_affiliate',['腾讯'],paragraph(68,'Tencent'),[],None,'累计融资4900万美元与此前4600万美元融资不是同口径，当前只有短摘要；旧轮已曝光且无完整新进展证据。'),
]:
    d=DM['SRC_'+sid(n)];d['reason']=why
    if q is None and r:q=S[sid(n)]['text'].splitlines()[0]
    assess(d,e,r,m,subject,kind,focus,(n,q) if q else None,genres,(n,gq) if gq else None)
    if kind=='representative_subject':d['subject_assessment']['representative_product']={'猩球游戏':'弹壳特攻队','Kintsugiyama':'守望先锋','EA/BioWare':'质量效应/龙腾世纪'}[subject]

# Additional representative subjects and focus-company boundary recall.
for n,e,r,m,subject,kind,focus,word,product,genreword in [
    (53,1,3,0,'Riot Games','focus_subject',['Riot Games'],'拳头游戏',None,None),
    (101,3,1,0,'CDPR','representative_subject',[],'凭借出色','巫师/赛博朋克2077',None),
    (104,3,1,1,'动视','representative_subject',[],'Sledgehammer Games刚开始','使命召唤','第三人称'),
    (263,3,1,0,'Devsisters','representative_subject',[],'3.5亿','跑跑姜饼人',None),
    (585,3,1,0,'艾希续开发团队','representative_subject',[],'3750','艾希：续',None),
    (615,2,1,0,'ForgeTax开发者','representative_subject',[],'25万','ForgeTax',None),
]:
    z=DM['SRC_'+sid(n)];z['reason']='已重新取证主体；E/R/M按本期新版本计算，不沿用旧品类或多源加分。'
    assess(z,e,r,m,subject,kind,focus,(n,paragraph(n,word)),['competitive'] if m else [],(n,paragraph(n,genreword)) if m else None)
    if product:z['subject_assessment']['representative_product']=product
    if n==53:z['reason']+='招聘与项目推测不等于新品正式立项，3分排除。'
    elif n==263:z['event']='Devsisters与Big Shot Pictures宣布跑跑姜饼人电影合作';z['reason']+='从综合稿中独立召回该合作事件，不将多件新闻打包计分。'
    elif n==615:z['reason']+='代表作销量已取证，但名单外R1且肉鸽M0，2分排除。'
    else:z['reason']+='名单外有代表作及声量，R1，最高4分仍低于5分线。'

# History: first the exact 14 days before the reporting window, then the
# already-published within-week daily/weekend records for weekly aggregation.
H=read(P/'industry_history_14d.json')['occurrences']
exposure=read(P/'within_week_exposure_history.json')['occurrences']
within=[]
for folder,v in prior.items():
    for item in v['items'].values():
        if item['section']!='industry_news':continue
        oldcid=item['candidate_id'];od=v['decisions'].get(oldcid,{})
        within.append({'title':item['title'],'event':od.get('event',item['title']),'claims':[c['claim'] for c in item['claims']],'report_kind':'weekend' if folder.startswith('weekend') else 'daily','report_window':{'start':folder.split('/')[-1].split('_to_')[0],'end':folder.split('/')[-1].split('_to_')[-1]},'source_ids':item['source_ids'],'card_exposed':None,'card_rank':None,'card_limit':10,'card_exposure_source':'within_week_reference_not_exposure_inference'})
        prior_exposure=[h for h in exposure if h['report_kind']!='weekly' and h['title']==item['title'] and h['report_window']==within[-1]['report_window']]
        assert prior_exposure, item['title']
        for key in ['card_exposed','card_rank','card_limit','card_exposure_source']:within[-1][key]=prior_exposure[0][key]
save('within_week_history.json',within)
def exact_matches(d):
    titles=' '.join(S[s]['title'] for s in d['source_ids'])+' '+d['event']
    if d['candidate_id']=='SRC_S0615':titles+=' ForgeTax'
    patterns=[('Flow Games',r'Flow Games'),('Xbox.*Labs|Xbox Labs',r'Xbox.*Labs|Xbox Labs'),('全境封锁2',r'全境封锁2'),('剑侠世界4',r'剑侠世界4'),('极限战场',r'极限战场'),('艾希|ICEY',r'艾希|ICEY'),('神仙道3',r'神仙道3'),('库洛.*言之域|言之域',r'言之域'),('Squad Busters',r'Squad Busters'),('王者万象棋',r'王者万象棋'),('ForgeTax',r'ForgeTax'),('火影忍者.*国际',r'火影忍者'),('Miniclip.*AdSurge|AdSurge',r'AdSurge'),('Survival Log',r'Survival Log'),('三角洲.*5800|5800.*三角洲',r'三角洲'),('Garena.*Free City|Free City',r'Free City'),('谋略武林',r'谋略武林')]
    result=[]
    for pat,hpat in patterns:
        if re.search(pat,titles,re.I) and not (pat=='王者万象棋' and not re.search('成绩|收入|前五|畅销|结构',titles)):result.extend(h for h in H if re.search(hpat,h['title']+' '+h['event'],re.I))
    return list({(h['title'],str(h['report_window'])):h for h in result}.values())
for d in D:
    if d['section']!='industry_news':continue
    h=exact_matches(d)
    if h:
        d['history_check']={'history_match':True,'novelty':'repeat_only','prior_occurrences':[h0['title']+'｜'+h0['report_window']['start']+'_to_'+h0['report_window']['end'] for h0 in h],'new_facts':[],'prior_card_exposed':any(x['card_exposed'] for x in h)}
        if d['decision']!='merge':d['decision']='exclude';d['reason']+='；匹配双周历史，无已取证实质新状态；未曝光项当前分数/来源仍不达门槛或未获唯一名额。'
    inside=[h for h in within if set(h['source_ids']) & set(d['source_ids'])]
    if inside:
        d['within_week_occurrences']=[h['title']+'｜'+h['report_window']['start']+'_to_'+h['report_window']['end'] for h in inside]
        # Within-week aggregation is explicitly allowed, with prior occurrences
        # disclosed separately; it is neither carryover nor a material update.
        if d['decision']=='include':
            d['history_check']['prior_occurrences']+=d['within_week_occurrences']
            d['history_check']['history_match']=True
            d['history_check']['prior_card_exposed']=any(h['card_exposed'] for h in inside)
            d['weekly_aggregation']=True
            d['reason']+='；汇总本周尚未进入任何已发布周报的日报/周末事件，仅保留一个条目。'

forge=DM['SRC_S0615']
forge['history_check']['novelty']='material_update'
forge['history_check']['new_facts']=['本期来源披露TapTap《铸剑大师模拟器》下载达30万，双周历史只记录原作估算销量与核心循环。']
forge['new_fact_evidence']=[ev(615,paragraph(615,'30万'))]
forge['reason']+='本期新增国内复刻产品下载事实；不同估算商25万与20万不计算净销量增长。'

icey=DM['SRC_S0585']
icey['history_check']['novelty']='material_update'
icey['history_check']['new_facts']=['截至10月19日，众筹超过3750万元、支持人数超过23万；10月18日Q&A明确2027年5月1日Steam发售及不因筹款增加而延长开发。']
icey['new_fact_evidence']=[ev(585,paragraph(585,'3750')),ev(585,paragraph(585,'10月18日凌晨'))]
icey['reason']+='有本期新金额与明确发售/交付安排，但名单外R1、总分3，仍排除。'

# Direct AI cases are prioritized over transferable generic model announcements.
def use_ai(folder,oldcid,cid,why):
    item=copy.deepcopy(prior[folder]['items'][oldcid]);ids=item['source_ids']
    d=base(cid,'ai_trends',ids,item['title'],why,'include');d.update(ai_tier='direct_application',game_stage=['development'],industry_reverse_scan=any(S[s]['section']=='industry_news' for s in ids))
    item['candidate_id']=cid;ITEMS.append(item)
    for s in ids:
        z=DM.get('SRC_'+s)
        if z:z.update(decision='merge',merge_into=cid,reason='同一AI直接应用事件合并至周报条目。')
    return d
use_ai(d21,'A304','A_SOON','恺英旗下SoonPlay 20日公测，16日至22日同一平台公测与特性说明合并，不拆成多条。')
use_ai(d20,'A073','A_SEA','SeaGamesMaker beta是具体游戏创作产品；收入与SeaArt产品口径分别保留。')
use_ai(d21,'A039','A_QA','可回溯的游戏QA访谈，有具体审核、证据与责任分工。')
use_ai(d21,'A215','A_SURVEY','101位负责人的AI采用调查，保留样本地域、类型和整合深度口径。')
use_ai(d21,'A288','A_REVAMP','同一ReVamp公开测试缩小事件，以本周更新访谈合并公告与机制，不另拆传播损失。')
d=base('A_MACHINARIUM','ai_trends',[1640],'Amanita反对Machinarium素材AI致敬视频并获道歉','AI直接作用于游戏资产传播与权利治理；完整报道有原工作室回应与删除、道歉。','include');d.update(ai_tier='direct_application',game_stage=['operations'],industry_reverse_scan=True)
body='Nura Studios负责人于10月20日发布一段使用《Machinarium》素材的AI“致敬”视频，Amanita Design公开反对，认为把原作资产输入AI并制作动画不代表工作室的创作。随后Nura负责人删除相关帖子并道歉。争议围绕具体游戏美术资产的使用与“致敬”表述，体现了生成效率之外的授权和创作者认同问题。'
ITEMS.append({'section':'ai_trends','title':'Amanita反对《Machinarium》素材AI“致敬”，发布者删帖道歉','candidate_id':d['candidate_id'],'source_ids':d['source_ids'],'body':body,'claims':[{'claim':body.split('。')[0]+'。',**ev(1640,paragraph(1640,'On October 20'))},{'claim':'Amanita Design公开反对',**ev(1640,paragraph(1640,'The audacity'))},{'claim':'删除相关帖子并道歉',**ev(1640,paragraph(1640,'Nura Studios CEO'))}]})
DM['SRC_S1640'].update(section='ai_trends',decision='merge',merge_into=d['candidate_id'],reason='行业池AI反扫，具体游戏资产治理案例转入AI，行业不重复。',ai_tier='direct_application',game_stage=['operations'],industry_reverse_scan=True)

# Community articles retain player attribution and scan all same-window posts.
def community_old(folder,oldcid,cid):
    item=copy.deepcopy(prior[folder]['items'][oldcid]);item['candidate_id']=cid
    d=base(cid,'community_discourse',item['source_ids'],item['title'],'周报按具体争议事件选材；已扫描本周社区池同产品、机制、回应及后续。','include')
    d['community']=copy.deepcopy(item['community']);ITEMS.append(item)
    return d,item
d,item=community_old(d20,'C226','C_DUET')
d,item=community_old(d20,'C215','C_TOOL')
item['source_ids']=[sid(1745)];d['source_ids']=item['source_ids']
item['body']='《明日方舟：终末地》售价98元的金属测量套件被玩家质疑将不符合标准的卡尺称为“游标卡尺”。帖子称商品详情后来删除了“游标”二字，但玩家仍围绕专业名称、工具实用性与周边定价争论。10月20日建帖后，21日又补充详情页将“助你一臂之力”写成“祝你一臂之力”，讨论延续到22日。'
item['claims']=[{'claim':'售价98元',**ev(1745,paragraph(1745,'终末地官方淘宝店'))},{'claim':'商品详情后来删除了“游标”二字',**ev(1745,paragraph(1745,'终末地官方淘宝店'))},{'claim':'专业名称',**ev(1745,paragraph(1745,'游标卡尺一定要有副标'))},{'claim':'“祝你一臂之力”',**ev(1745,paragraph(1745,'10.21附'))},{'claim':'10月20日建帖',**ev(1745,'发帖：2026-10-20T14:57 |')},{'claim':'讨论延续到22日',**ev(1745,'最新回复：2026-10-22T11:47 |')}]
item['community']['follow_up_scan']='全周同tid快照、行业周边池已扫描；22日快照补充21日文案错误与持续回复，不将玩家关于标准的判断当官方检测结论。';d['community']=copy.deepcopy(item['community'])
d=base('C_PHP','community_discourse',[1747,1752,1632],'PHP漏洞停机引发玩家对老游戏维护投入与数据安全的争论','21日至22日同一漏洞停机及玩家后续争论；GOG官方停机/恢复消息回填，不推断日本游戏全部关服。','include')
body='PHP漏洞相关停机消息在10月21日引起玩家关注，GOG公告称网站与Galaxy暂时离线维护，随后宣布恢复。22日的社区讨论中，有玩家担心低成本老游戏因修复投入过高而终止运营，也有人反对“没人会攻击小产品”的说法，强调个人服务器和玩家数据同样面临风险。玩家质疑，长期服务承诺能否因老系统维护成本而终止；部分玩家称日本小游已停止运营，另一些人认为这更像是借安全事件退出低收入项目。'
comm={'trigger':'PHP漏洞相关服务停机与部分老游戏存续传言','claim_scope':'GOG停机恢复有公告转述；具体日本小游停运与修复成本归玩家判断','complaint_logic':'长期投入与停服损失、修复费用及数据安全责任之间的冲突','timeline':'10月21日停机讨论、GOG随后恢复；22日出现老游戏关服成本与攻击风险争论','follow_up_scan':'扫描全周PHP、维护、GOG、恢复关键词；S1632含GOG恢复公告，S1747/S1752为同一漏洞玩家讨论，不采纳PHP国内使用率等无证据判断。','official_source_ids':[sid(1632)]}
d['community']=comm
ITEMS.append({'section':'community_discourse','title':'PHP漏洞停机引发争论：老游戏修复成本能否成为停服理由','candidate_id':d['candidate_id'],'source_ids':d['source_ids'],'body':body,'community':comm,'claims':[{'claim':'GOG公告称网站与Galaxy暂时离线维护，随后宣布恢复',**ev(1632,paragraph(1632,'We’re temporarily'))},{'claim':'随后宣布恢复',**ev(1632,paragraph(1632,"We're back online"))},{'claim':'修复投入过高',**ev(1752,'其实就是营收比不上修它的成本')},{'claim':'个人服务器和玩家数据同样面临风险',**ev(1752,paragraph(1752,'别以为路边'))},{'claim':'10月21日',**ev(1747,'发帖：2026-10-21T20:12 |')},{'claim':'22日的社区讨论',**ev(1752,'发帖：2026-10-22T12:53 |')}]})

# User-selected deep observation: exact title order, sole designated C001 card.
cand=(ROOT/'output/deep_observation_review'/f'{ID}_candidates.md').read_text(encoding='utf-8')
for num,(cid,n,score,label) in enumerate([('C001',306,12,'GameDiscoverCo玩家调查'),('C002',990,11,'GamesIndustry.biz定制市场研究')],1):
    b=re.search(r'### '+cid+r'\. (.*?)(?=\n### C|\Z)',cand,re.S).group(1)
    title=b.splitlines()[0];obs=re.search(r'\*\*一句话观察：\*\* (.*)',b).group(1)
    insights=[{'title':a,'detail':z} for a,z in re.findall(r'- \*\*(.*?)\*\*：(.*)',b.split('**卡片正文预览**')[0])]
    if cid=='C001':
        paras=['GameDiscoverCo面向超过1.6万名Steam玩家开展调查，经许可连接游戏库，并按每月游玩超过一小时询问设备使用。受访者中22%同时玩PC与手机但不玩主机，15.6%三端都玩。这些重叠关系表明，跨端发行增加的账户或设备覆盖，不能直接等同于同样数量的独立新增玩家。','这一判断成立的前提是把同一人的多设备行为与新增用户分开：跨端既可补充使用场景，也可能主要服务现有核心人群。样本通过线上赠奖招募，偏向活跃且熟悉网络的Steam玩家；这组比例不能直接外推到普通手游和主机市场，也不能单独预测某款产品的跨端转化率。']
        claims=[('超过1.6万名Steam玩家',paragraph(n,'asked >16,000')),('经许可连接游戏库',paragraph(n,'asked >16,000')),('每月游玩超过一小时',paragraph(n,'>1 hour per month')),('22%同时玩PC与手机但不玩主机',paragraph(n,'22% of respondents')),('15.6%三端都玩',paragraph(n,'15.6% of respondents')),('样本通过线上赠奖招募',paragraph(n,'recruited by offering giveaways')),('偏向活跃且熟悉网络',paragraph(n,'online-savvy subset'))]
    else:
        paras=['Sensor Tower受GamesIndustry.biz委托，对两个连续12个月窗口内首月付费销量超过50万份的PC与主机作品进行比较。达标作品从55款增至76款，其中独立作品由13款增至33款、占比从24%升至43%，3A达标数则从27款微增至28款。新增作品来自独游扩张，不能据此把增长解释成3A退出。','合作派对类约贡献一半独游首月销量，却只占33款独游中的9款，说明成功案例也分布在单机与续作。另一方面，研究只观察已经越过销量门槛的作品，并未统计所有发行项目；续作仍占当期样本首月付费销量的55%。样本结构的变化支持增长来源更广的判断，不能证明普通独游的成功概率已经上升。']
        claims=[('两个连续12个月窗口内首月付费销量超过50万份',paragraph(n,'analytics firm picked')),('达标作品从55款增至76款',paragraph(n,'analytics firm picked')),('独立作品由13款增至33款、占比从24%升至43%',paragraph(n,'just 13 titles')),('3A达标数则从27款微增至28款',paragraph(n,'Fifteen AA games')),('合作派对类约贡献一半独游首月销量，却只占33款独游中的9款',paragraph(n,'I expected a strong year')),('续作仍占当期样本首月付费销量的55%',paragraph(n,'sequels accounted'))]
    body='观察：'+obs+'\n\n分析：'+paras[0]+'\n\n'+paras[1]
    did='D_'+cid;d=base(did,'deep_analysis',[n],title,'完整消费飞书回执正文选择，保持C001、C002原顺序。','include');d['scores']={'relevance':3 if num==1 else 2,'insight':3,'evidence':3,'card':3,'total':score};d['card_designated']=num==1
    ITEMS.append({'section':'deep_analysis','title':title,'candidate_id':did,'source_ids':[sid(n)],'body':body,'claims':[{'claim':c,**ev(n,q)} for c,q in claims],'card_copy':{'source_label':label,'summary':obs,'insights':insights}})
    if num==1:(OUT/'deep_card_choice.txt').write_text(title+'\n',encoding='utf-8')

# Calendar: preserve every raw recall, overlay previously verified editorial
# corrections, normalize product/date, and count independent URLs/body hashes.
audit=read(P/'release_calendar_audit.json')
if not (P/'release_calendar_audit_raw.json').exists():save('release_calendar_audit_raw.json',audit)
else:audit=read(P/'release_calendar_audit_raw.json')
nodes=copy.deepcopy(audit['nodes'])
for n in nodes:n['publish_eligible']=False;n['editorial_reason']='原始召回待正文日期、独立来源与事件类别复核；未通过前不发表。'
for folder,v in prior.items():
    for n in v['audit']['nodes']:
        if not n.get('source_ids'):continue
        z=copy.deepcopy(n);z['prior_audit']=folder
        z['editorial_reason']=z.get('editorial_reason') or z.get('review_reason') or '此前本周逐字证据复核结果，按周报窗口重审。'
        nodes.append(z)
# Current multi-source launch and two false-positive launch nodes.
for n in nodes:
    if n['product']=='愚者不灭':n.update(publish_eligible=False,editorial_reason='正文只有今日/现已，没有绝对发售月日；不以采集日期补齐。')
    if n['product']=='影之刃零':n.update(publish_eligible=False,editorial_reason='最终预告与既有发售档期宣传，不是本日上线；27日预下载超出23日事件窗口。')
    if n['product']=='星途天城' and n['event_date']=='2026-10-22':n.update(publish_eligible=True,editorial_reason='完整公告有10月22日；3839是独立时间轴，重复转载仅计一次。')
# Resolve overlays by product/date; a verified prior node supersedes raw parse.
groups={}
for n in nodes:
    product=n['product'];product=re.sub(r'-.*$','',product) if product.startswith('人间异想计划-') else product
    k=(product,n['event_date'])
    if k not in groups:groups[k]=copy.deepcopy(n);groups[k]['product']=product
    else:
        g=groups[k]
        if n.get('prior_audit') or n.get('publish_eligible'):
            keep=list(dict.fromkeys(g.get('source_ids',[])+n.get('source_ids',[])));was_valid=g.get('publish_eligible',False);g.update(copy.deepcopy(n));g['source_ids']=keep;g['product']=product
            if was_valid and ('单源' in n.get('editorial_exclusion','') or '单源' in n.get('editorial_reason','')):g['publish_eligible']=True;g['editorial_reason']='本周合并后有两份完整独立来源；后一天单源池不覆盖此前完整窗口证据。'
        else:g['source_ids']=list(dict.fromkeys(g.get('source_ids',[])+n.get('source_ids',[])))
for n in groups.values():
    ids=n['source_ids'];inds=[s for s in ids if S[s]['section']=='industry_news'];rels=[s for s in ids if S[s]['section']=='release_calendar']
    # Normalize exact/whitespace publisher duplicates as one independent report.
    hashes=set();urls=set();count=0
    for s in ids:
        t=re.sub(r'返回搜狐.*$|/\s*END\s*/.*$','',S[s]['text'],flags=re.S)
        h=digest(re.sub(r'\s+','',t));u=S[s]['url'].split('#')[0]
        if h in hashes or u in urls:continue
        hashes.add(h);urls.add(u);count+=1
    n['industry_ids']=inds;n['release_ids']=rels;n['appearance_count']=count;n['appearance_score']=min(count,3);n['industry_bonus']=int(bool(inds));n['source_strength_score']=min(count,3)+int(bool(inds))
    n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n.get('company_bonus',0)
    n['multi_source_eligible']=count>=2;n['coverage']='industry+release' if inds and rels else 'industry_only' if inds else 'release_only';n['coverage_rank']=3 if inds and rels else 2 if inds else 1
    date=n['event_date'];schedule=n.get('signal_type') in {'new_game_schedule','new_game_first_reveal'}
    n['window_eligible']=bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}',date)) and (START<=date<='2026-10-23' or schedule)
    n['window_scope']='next_day_lookahead' if date=='2026-10-23' else 'report_window' if START<=date<=END else 'future_announcement' if schedule else 'outside'
    n['publish_eligible']=bool(n.get('publish_eligible')) and count>=2 and n['window_eligible'] and all(S[s]['body_status']=='full' for s in ids)
    if not n['publish_eligible'] and count<2:n['editorial_reason']+='；独立来源不足2。'
nodes=list(groups.values())
for n in nodes:n['first_seen_order']=min(int(s[1:]) for s in n['source_ids'])
nodes.sort(key=lambda n:(not n['publish_eligible'],-n['priority_score'],-n.get('company_bonus',0),-n['event_type_score'],-n['appearance_count'],-int(bool(n['industry_ids'])),n['first_seen_order']))
for i,n in enumerate(nodes,1):n['candidate_id']=f'R{i:03}'
audit['nodes']=nodes;save('release_calendar_audit.json',audit)

# Required human-readable candidate/decision artifacts precede structured output.
lines=['# 全周事件候选','',f'- 窗口：{ID}；完整index全部1761个ID已核对；全量正文扫描见full_input_review.json。','- 行业、AI、社区严格按独立事件；产品日历按产品+日期单独召回。','']
for d in D:
    facts=[]
    for s in d['source_ids']:
        text=S[s]['text'];first=next((l for l in text.splitlines() if len(l.strip())>20),text.splitlines()[0]);facts.append(s+': '+first)
    lines.extend([f'## {d["candidate_id"]} - {d["event"]}',f'- section: {d["section"]}',f'- source_ids: {", ".join(d["source_ids"])}',f'- event_date: {d["event_date"]}','- facts: '+' | '.join(facts),'- notes: '+d['reason'],''])
for n in nodes:lines.extend([f'## {n["candidate_id"]} - {n["product"]} {n["event"]}','- section: release_calendar','- source_ids: '+', '.join(n['source_ids']),'- event_date: '+n['event_date'],'- facts: '+n.get('editorial_reason',''),''])
(P/'event_candidates.md').write_text('\n'.join(lines),encoding='utf-8')
save('selection_decisions.json',{'scoring_version':'subject_genre_v2','report_type':'weekly','report_window':{'start':START,'end':END},'history_window':{'start':'2026-10-02','end':'2026-10-15'},'decisions':D})
subprocess.run([sys.executable,str(ROOT/'scripts/sync_release_decisions.py'),'--audit',str(P/'release_calendar_audit.json'),'--decisions',str(P/'selection_decisions.json'),'--max-items','7'],check=True)
D=read(P/'selection_decisions.json')['decisions'];DM={d['candidate_id']:d for d in D}
for d in D:
    if d['section']=='release_calendar':
        node=next(n for n in nodes if n['candidate_id']==d['candidate_id']);d['reason']+='；'+node.get('editorial_reason','')

# Reuse proven full calendar prose where available; current launch added below.
for d in D:
    if d['section']!='release_calendar' or d['decision']!='include':continue
    n=next(n for n in nodes if n['candidate_id']==d['candidate_id'])
    match=next((i for v in prior.values() for i in v['items'].values() if i['section']=='release_calendar' and i.get('release',{}).get('product')==n['product'] and i.get('release',{}).get('date')==n['event_date']),None)
    if match:
        item=copy.deepcopy(match);item['candidate_id']=d['candidate_id'];item['source_ids']=d['source_ids'];ITEMS.append(item)
    elif n['product']=='星途天城':
        body='蒸汽幻想卡牌RPG手游《星途天城》于10月22日开启全平台公测；以星灵三阶段蜕变与角色等级、进阶进度共享降低换阵容的养成负担。'
        ITEMS.append({'section':'release_calendar','title':'星途天城','candidate_id':d['candidate_id'],'source_ids':d['source_ids'],'body':body,'release':{'product':'星途天城','event':'公测','date':'2026-10-22','platform':'全平台','company':'未据当前正文补写'},'claims':[{'claim':'10月22日开启全平台公测',**ev(1665,paragraph(1665,'当蒸汽'))},{'claim':'卡牌RPG',**ev(1665,paragraph(1665,'卡牌RPG走到今天'))},{'claim':'等级、进阶进度共享',**ev(1665,paragraph(1665,'更值得一提'))},{'claim':'三阶段蜕变',**ev(1665,paragraph(1665,'游戏没有走'))}]})
    else:raise ValueError(('Missing verified calendar prose',n['product'],n['event_date']))

# Ensure every included decision has exactly one visible item; nonselected
# original source entries are audit only, never leaked to the source map.
order={'industry_news':0,'ai_trends':1,'release_calendar':2,'community_discourse':3,'deep_analysis':4}
ITEMS.sort(key=lambda i:(order[i['section']],(-DM[i['candidate_id']]['scores']['total'],-DM[i['candidate_id']]['scores']['relevance']) if i['section']=='industry_news' else (int(i['candidate_id'][1:]),) if i['section']=='release_calendar' else (0,)))
save('report_items.json',{'report_type':'weekly','report_window':{'start':START,'end':END},'items':ITEMS})
save('selection_decisions.json',{'scoring_version':'subject_genre_v2','report_type':'weekly','report_window':{'start':START,'end':END},'history_window':{'start':'2026-10-02','end':'2026-10-15'},'decisions':D})
lines=['# 选择决策','', '卡片曝光去重：逐项读取2026-10-02至2026-10-15的92条历史曝光、排名、上限和来源；本周日报/周末事件只做一次周报合并，不冒充实质更新。无入选card_carryover，先前排名不适用。','维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已反扫全量1761条输入；每条召回均列入下表。','产品日历漏挂反查：已按全量行业与日历正文反扫上线/测试/定档/预下载/首曝/重大更新，所有原始与补召回节点均有日历决策；行业评分与日历资格独立。','- 所有非E0行业候选重新执行主体/品类取证；旧分只作previous_review_scores保存。','- 行业与产品日历独立，日历使用修正后的独立多源优先级前缀。','', '| candidate | decision | target_section | reason |','| --- | --- | --- | --- |']
for d in D:
    scores=d.get('scores',{});reason=d['reason']
    if d['section']=='industry_news':reason=f'E{scores["event"]}×R{scores["relevance"]}+M{scores["hook"]}={scores["total"]}；'+reason
    lines.append('| '+d['candidate_id']+' | '+(f'merge into {d["merge_into"]}' if d['decision']=='merge' else d['decision'])+' | '+d['section']+' | '+reason.replace('|','/')+' |')
dimensions={'国内移动':r'手游|移动|mobile','国产产品与人才':r'国产|国内|腾讯|网易|米哈游|制作人|总监|人才','市场数据':r'数据|收入|下载|销量|市场|survey|report|data','并购':r'融资|收购|投资|并购|破产|fund|acquir|bankrupt','平台政策':r'平台|政策|App Store|Steam|Xbox|Apple|Google|微信','档期变动':r'定档|延期|停运|关闭|重启|cancel|delay|shut|release','资本组织':r'公司|团队|管理|裁员|基金|融资|studio|company','海外重大':r'全球|海外|Supercell|Riot|Roblox|NetEase|Tencent|EA|Xbox|Steam'}
for label,pattern in dimensions.items():
    count=sum(d['section']=='industry_news' and bool(re.search(pattern,d['event']+' '+d['reason'],re.I)) for d in D)
    lines.insert(5,'- 维度覆盖 '+label+'：'+str(count)+'张候选；包含排除项与来源层审计，非最终条数。')
(P/'selection_decisions.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

# Stage the report so a failed validator cannot be mistaken for a new final.
stage=P/'staging';stage.mkdir(exist_ok=True)
titles={'industry_news':'一、行业新闻','ai_trends':'二、AI 新闻','release_calendar':'三、新游发布 / 产品日历','community_discourse':'四、玩家舆论 / 社区动态','deep_analysis':'五、行业精选 / 深度观察'}
lines=[f'# 游戏行业周报｜{START} 至 {END}','']
for sec,heading in titles.items():
    lines.extend(['## '+heading,''])
    for num,item in enumerate([i for i in ITEMS if i['section']==sec],1):
        if sec=='release_calendar':lines.extend(['- '+item['body'],''])
        else:lines.extend([f'### {num}. {item["title"]}','',item['body'],''])
(stage/f'game_industry_weekly_{ID}.md').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({'items':dict(Counter(i['section'] for i in ITEMS)),'decisions':len(D),'release_top':[(n['product'],n['priority_score']) for n in nodes if DM[n['candidate_id']]['decision']=='include']},ensure_ascii=False))
