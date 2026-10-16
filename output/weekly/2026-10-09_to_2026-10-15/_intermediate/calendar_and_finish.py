import copy
from collections import Counter

raw_path=P/'release_calendar_audit_raw.json'
if not raw_path.exists():raw_path.write_text((P/'release_calendar_audit.json').read_text(encoding='utf-8'),encoding='utf-8')
audit=json.loads(raw_path.read_text(encoding='utf-8'))
aliases={'剑侠世界 4：无限':'剑侠世界4：无限','GTA 6':'GTA6','七界梦谭-代号界':'七界梦谭','1999 TOKOYO Building':'1999TOKOYO Building','连城绝':'连城绝：大唐','战锤40K：爆矢枪2（Warhammer 40,000： Boltgun 2）':'战锤40K：爆矢枪2','全面战争：幕府将军2 完全版':'全面战争：幕府将军2','绿梦：时空之声-预下载':'绿梦：时空之声','极限战场-多人战场竞技射击':'极限战场','极限战场-预下载已开启 PC/主机':'极限战场'}
def norm_product(v):
    v=re.sub(r'\s*(?:招募中|已开服|已上线|测试中)$','',v).strip()
    return aliases.get(v,v)
nodes={}
def ingest(product,date,kind,event,score,ids,order,why='',valid=True):
    product=norm_product(product); key=(product,date)
    n=nodes.setdefault(key,{'product':product,'event_date':date,'signal_type':kind,'event':event,'event_type_score':score,'first_seen_order':order,'observed_signal_types':[],'observed_events':[],'source_ids':[],'audit_notes':[],'editorial_valid':False})
    n['source_ids']=list(dict.fromkeys(n['source_ids']+ids));n['first_seen_order']=min(n['first_seen_order'],order)
    if kind not in n['observed_signal_types']:n['observed_signal_types'].append(kind)
    if event not in n['observed_events']:n['observed_events'].append(event)
    if score>n['event_type_score']:n.update(signal_type=kind,event=event,event_type_score=score)
    n['editorial_valid']=n['editorial_valid'] or valid
    if why and why not in n['audit_notes']:n['audit_notes'].append(why)
    return n
for n in audit['nodes']:
    prod=norm_product(n['product']);date=n['event_date'];kind=n['signal_type'];score=n['event_type_score'];valid=True;why=''
    if prod=='极限战场' and '定档' in n['event']:date='2026-10-15'
    if prod=='剑侠世界4：无限' and '10月15日' in n['event']:date='2026-10-15'
    if prod=='极境：垂钓者' and '测试定档' in n['event']:date='2026-10-21'
    if prod=='连城绝：大唐':date='2026-10-15';kind='new_game_test';score=3
    if prod=='BUZZ or DIE' and kind=='new_game_schedule':date='2026-10-28'
    if prod=='GTA6':valid=False;why='发售预告、开发回顾或PC传闻不等于当前正式上线；产品句的日期与事件不绑定'
    if prod=='战锤40K：爆矢枪2' and set(n['source_ids'])&{'S0517','S0518'}:valid=False;why='原记录主体为毁灭战士作曲家，战锤提及是背景；非该作独立定档'
    if prod in ['梦回甄嬛传','扶摇一梦']:valid=False;why='原文为历史8月上线与既有经营背景，不能把月级历史时间回填成10月报道日'
    if prod in ['三角洲行动','王者万象棋','全境封锁2','Disney Solitaire','诡秘之主','向末日开炮','Top Lords','Lordrush','MC','Minecraft','我的世界：地下城2','崩坏：星穹铁道','鬼武者：剑之道','黎明行者之血','影之刃零','Hololive Dreams','Zeus： The God of Arrogance']:
        # 仅对原抽取器误当作当期上线的节点失效；真实首次曝光/定档仍单独召回。
        if kind in ['new_game_launch','new_game_test'] and not any(re.search(r'Event date: '+re.escape(date),S[s]['text']) for s in n['source_ids']):valid=False;why='来源为历史经营/访谈/常规内容/未来节点，未证明本日期新品实际上线或测试'
    if prod in ['雨中冒险2：万象归衡','地牢猎手6','街头霸王6','疯狂出租车：极速环游','全面战争：幕府将军2']:
        kind='old_major_update';score=1
    ingest(prod,date,kind,n['event'],score,n['source_ids'],n['first_seen_order'],why,valid)

# 全量正文逐句反扫：仅绑定同句单产品、绝对月日与明确产品事件；历史句和推荐区停止。
recall_log=[]
for s in rows:
    if s['section'] not in ['industry_news','release_calendar']:continue
    text=re.split('相关推荐|相关阅读|延伸阅读|猜你喜欢|更多推荐',s['text'])[0]
    for sent in re.split(r'\n+|(?<=[。！？])',text):
        games=re.findall(r'《([^》]+)》',sent)
        if len(games)!=1 or re.search('去年|此前|曾经|早在|过去|上线后|测试后|前作',sent):continue
        dm=re.search(r'(?:2026年)?(\d{1,2})月(\d{1,2})日',sent)
        if not dm:continue
        if re.search('首曝|首次公开|首次曝光|正式公布',sent):kind='new_game_first_reveal';score=2;event='首次曝光'
        elif re.search('预下载',sent):kind='new_game_preload';score=2;event='预下载'
        elif re.search('测试|公测|发售|上线|开服',sent):
            kind='new_game_test' if re.search('测试|公测',sent) else 'new_game_launch';score=3;event='新品测试' if kind=='new_game_test' else '新品上线'
        else:continue
        date=f'2026-{int(dm[1]):02d}-{int(dm[2]):02d}'
        if not START<=date<='2026-10-16':kind='new_game_schedule';score=2;event=f'{date}产品定档'
        if re.search('新赛季|版本|DLC|联动|资料片|皮肤|福利|折扣|更新',sent) and not re.search('新品|新作|首次|新游',sent):continue
        prod=norm_product(games[0]);valid=s['body_status']=='full'
        if prod in ['GTA6','全境封锁2','梦回甄嬛传','扶摇一梦','三角洲行动','王者万象棋','诡秘之主','霓虹深渊2']:valid=False
        n=ingest(prod,date,kind,event,score,[s['source_id']],3000+int(s['source_id'][1:]),'全文同句反扫；完整证据在recall_log',valid)
        recall_log.append({'source_id':s['source_id'],'product':prod,'event_date':date,'evidence':sent.strip(),'editorial_valid':valid})

# 漏掉的别名、正式测试与Gematsu定档来源接回同产品日期节点。
fixes=[
 ('极限战场','2026-10-15','new_game_test','首次PC测试',3,['S0041','S0043','S1293','S1310'],5),
 ('剑侠世界4：无限','2026-10-15','new_game_launch','全平台公测',3,['S1115','S1120','S1285','S1299','S1320'],0),
 ('七界梦谭','2026-10-09','new_game_test','PC端限量删档测试',3,['S0199','S0222','S0268'],9),
 ('绿梦：时空之声','2026-10-15','new_game_launch','三端公测',3,['S1118','S1296','S1313'],3),
 ('太吾异世劫','2026-10-15','new_game_launch','登陆Steam',3,['S0011','S1287'],6),
 ('动物城咖啡店','2026-10-13','new_game_launch','登陆Steam',3,['S0601','S0674'],12),
 ('连城绝：大唐','2026-10-15','new_game_test','首次不删档计费测试',3,['S0777','S0778','S1300'],13),
 ('1999TOKOYO Building','2026-10-14','new_game_test','试玩版发布及11月10日发售定档',3,['S0876','S1010','S1048'],24),
 ('BUZZ or DIE','2026-10-28','new_game_schedule','10月28日发售定档',2,['S0676','S0779','S0820'],23),
 ('极境：垂钓者','2026-10-10','new_game_first_reveal','首次曝光',2,['S0280','S0610','S0370'],22),
 ('绿梦：时空之声','2026-10-13','new_game_preload','预下载',2,['S0814'],1000),
 ('剑侠世界4：无限','2026-10-14','new_game_preload','预下载',2,['S1038'],1001),
]
for args in fixes:ingest(*args)

# URL相同或正文哈希相同只计一源；同站同一新闻稿的轻微排版变体也不增加独立强度。
def independent_groups(ids):
    groups=[]
    for sid in ids:
        s=S[sid];t=re.sub(r'\s+','',s['text']);placed=False
        for g in groups:
            q=S[g[0]];u=re.sub(r'\s+','',q['text'])
            if s['source']==q['source'] or s['url']==q['url'] or s['sha1']==q['sha1'] or (t==u and len(t)>25) or (len(t)>500 and len(u)>500 and __import__('difflib').SequenceMatcher(None,t,u,autojunk=False).quick_ratio()>0.985):
                g.append(sid);placed=True;break
        if not placed:groups.append([sid])
    return groups
for n in nodes.values():
    ids=n['source_ids'];groups=independent_groups(ids);n['independent_source_groups']=groups;n['appearance_count']=len(groups)
    n['industry_ids']=[s for s in ids if S[s]['section']=='industry_news'];n['release_ids']=[s for s in ids if S[s]['section']=='release_calendar']
    n['appearance_score']=3 if len(groups)>=3 else 2 if len(groups)==2 else 1;n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus']
    n['company_bonus']=3 if n['product']=='极限战场' else 0;n['focus_companies']=['网易'] if n['company_bonus'] else [];n['company_relationship']='direct' if n['company_bonus'] else 'none';n['focus_company_relationships']={'网易':'direct'} if n['company_bonus'] else {};n['company_evidence_ids']=[next(s for s in ids if '网易' in S[s]['text'])] if n['company_bonus'] else []
    # 其他真实重点关系仅取产品局部句，不沿用跨段或云服务关系误加分。
    for company,pat in [('腾讯','腾讯'),('网易','网易'),('米哈游','米哈游'),('莉莉丝','莉莉丝')]:
        if n['company_bonus'] or not n['signal_type'].startswith('new_game_'):break
        if n['product']=='剑侠世界4：无限':break
        direct=[sid for sid in ids if re.search(re.escape(pat)+r'[^。\n]{0,25}'+re.escape(n['product']),S[sid]['text']) and not re.search(r'云助力|投资|持股',S[sid]['text'][:500])]
        if direct:n['company_bonus']=3;n['focus_companies']=[company];n['company_relationship']='direct';n['focus_company_relationships']={company:'direct'};n['company_evidence_ids']=direct
    n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus']
    n['multi_source_eligible']=len(groups)>=2
    date=n['event_date'];n['window_scope']='report_window' if START<=date<=END else 'next_day_lookahead' if END<date<='2026-10-16' else 'future_announcement' if n['signal_type'] in ['new_game_schedule','new_game_first_reveal'] else 'outside'
    dateforms=[date,f'{int(date[5:7])}月{int(date[8:10])}日',f'{int(date[5:7])} 月 {int(date[8:10])} 日']
    n['date_evidence']=[{'source_id':sid,'evidence':evidence(sid,next(f for f in dateforms if f in S[sid]['text']))} for sid in ids if any(f in S[sid]['text'] for f in dateforms)]
    invalid_context=(n['product'] in ['GTA6','战狗','赛博朋克：边缘行者'] or n['product']=='战锤40K：爆矢枪2' and set(ids).issubset({'S0517','S0518'}) or n['product']=='永恒之塔2' and date<START)
    if invalid_context:n['audit_notes'].append('主体/日期/事件绑定复核失败：宣传、非游戏影集、历史上线或背景提及，不能作为本期新品节点')
    valid=n['editorial_valid'] and bool(n['date_evidence']) and n['window_scope']!='outside' and not invalid_context
    if any(S[s]['body_status']!='full' for s in ids):
        # 只使用完整来源的独立组作为资格，不让摘要抬高多源数。
        full=[s for s in ids if S[s]['body_status']=='full'];valid=valid and len(independent_groups(full))>=2
    n['window_eligible']=valid;n['publish_eligible']=valid and n['multi_source_eligible']
    n['coverage']='industry+release' if n['industry_ids'] and n['release_ids'] else 'industry_only' if n['industry_ids'] else 'release_only'
    n['coverage_rank']=3 if n['industry_ids'] and n['release_ids'] else 2 if n['industry_ids'] else 1
    n['status']='reviewed'
    if not n['date_evidence']:n['audit_notes'].append('无同一产品事件的绝对日期证据；不以采集日/本日指代补造日期')
    # 上一期次日提前刊发的同节点，或已刊周报事件应排除；本周正常日报可汇总。
    prev=[]
    for q in ROOT.glob('output/*/*/_intermediate/report_items.json'):
        if q.parent==P:continue
        try:
            obj=json.loads(q.read_text(encoding='utf-8'));its=obj.get('items',[]) if isinstance(obj,dict) else obj
        except Exception:continue
        reportid=q.parent.parent.name
        for it in its:
            if it.get('section') not in ['release_calendar','release']:continue
            rr=it.get('release',{})
            if norm_product(rr.get('product',''))!=n['product'] or rr.get('date')!=date:continue
            past_dates=re.findall(r'\d{4}-\d{2}-\d{2}',reportid)
            if not past_dates:continue
            # 已刊未来定档不能阻止本期真实上线/测试；只对同一阶段去重。
            past_event=str(rr.get('event',''))
            prior_announcement=bool(re.search('定档|宣布|计划|预告',past_event))
            current_announcement=n['signal_type'] in ['new_game_schedule','new_game_first_reveal']
            previous_end=max(past_dates)
            nextday=(datetime.date.fromisoformat(previous_end)+datetime.timedelta(days=1)).isoformat()==date
            if previous_end<START and (nextday and not prior_announcement or current_announcement and prior_announcement):prev.append(str(q))
    n['prior_occurrences']=prev
    if prev:n['publish_eligible']=False;n['audit_notes'].append('此前已发布报告的同产品同日同事件，排除跨期重复')
nodes=list(nodes.values());nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
for k,n in enumerate(nodes,1):n['candidate_id']=f'release-candidate-{k:03d}'
audit['nodes']=nodes;audit['editorial_review']={'full_text_records_scanned':len([s for s in rows if s['section'] in ['industry_news','release_calendar']]),'raw_audit_preserved':str(raw_path),'aliases':aliases,'recall_log':recall_log,'cross_section_industry_overlap_allowed':True}
dump(P/'release_calendar_audit.json',audit)
print('CALENDAR PREFIX',[(n['product'],n['event_date'],n['priority_score'],n['appearance_count']) for n in nodes if n['publish_eligible']][:10])

# 日历正文由人工句子映射，顺序来自审计前缀，不手工跳选。
calendar_copy={
 '极限战场':('网易研发的多人战术竞技射击端游《极限战场》于10月15日在PC开启首次测试；围绕英雄技能、复活与局内经济设计小队对抗。','网易','PC','首次测试','S1293','Event date: 2026-10-15'),
 '剑侠世界4：无限':('西山居开发的武侠MMO多平台产品《剑侠世界4：无限》于10月15日开启全平台公测；提供家族群战、门派成长与自由交易。','西山居','PC / Android / iOS','公测','S1115','全平台公测时间'),
 '七界梦谭':('上海拾异信息科技发行、飞光阁工作室开发的国风修仙开放世界角色扮演多平台产品《七界梦谭》于10月9日在PC开启限量删档测试；本轮以PC端体验为主。','上海拾异信息科技 / 飞光阁工作室','PC','限量删档测试','S0199','PC端限量删档测试'),
 '绿梦：时空之声':('二次元横版ACT多平台产品《绿梦：时空之声》于10月15日在Android、iOS与PC开启公测；融合箱庭探索、叙事冒险和小队动作战斗。','','Android / iOS / PC','公测','S1118','今日（2026年10月15日）'),
 '太吾异世劫':('墨境团队打造、太吾IP授权的肉鸽幸存者刷宝端游《太吾异世劫》于10月15日登陆Steam；采用策略与角色扮演要素。','墨境团队','PC / Steam','上线','S0011','10月15日'),
 '动物城咖啡店':('一罐盐工作室开发的直觉系节奏端游《动物城咖啡店》于10月13日登陆Steam；以原创音乐、手绘美术和动物居民故事组织节奏挑战。','一罐盐工作室','PC / Steam','上线','S0674','于10月13日'),
 '连城绝：大唐':('花叮娱乐旗下武侠MMO多平台产品《连城绝：大唐》于10月15日15时开启首次不删档计费测试；包含门派战斗、社交与生活玩法。','花叮娱乐','PC / Web / Android / iOS','首次不删档计费测试','S0778','2026年10月15日（周四）15:00点'),
 '1999TOKOYO Building':('讲谈社发行的怀旧恐怖ADV端游《1999TOKOYO Building》于10月14日发布试玩版，并宣布11月10日发售；采用低多边形画面与文字叙事。','讲谈社','PC / Steam','试玩版发布/发售定档','S1048','Announcement date: 2026-10-14'),
}
eligible=[n for n in nodes if n['publish_eligible']][:7]
for n in eligible:
    if n['product'] not in calendar_copy:raise ValueError('Need calendar body: '+n['product'])
    body,company,platform,event,sid,needle=calendar_copy[n['product']]
    claims=[{'claim':body,'source_id':sid,'evidence':evidence(sid,needle)}]
    # 每条日历保留所有局部主张的原始证据，而非只证明日期。
    for sid2 in n['source_ids']:
        if S[sid2]['body_status']=='full':
            t=S[sid2]['text'];prod=n['product'];variants=[prod,prod.replace('4：',' 4：'),prod.replace('1999','1999 ')]
            key=next((v for v in variants if v in t),None)
            if key:claims.append({'claim':body,'source_id':sid2,'evidence':evidence(sid2,key)})
    items.append({'candidate_id':n['candidate_id'],'section':'release_calendar','title':n['product'],'source_ids':n['source_ids'],'claims':claims,'body':body,'release':{'product':n['product'],'event':event,'date':n['event_date'],'platform':platform,'company':company}})

# 周内日报/周末报仅汇总一次：保留完整标题、窗口和曝光字段；不是历史补位。
spec=importlib.util.spec_from_file_location('history_mod',ROOT/'scripts/build_industry_history.py');hm=importlib.util.module_from_spec(spec);spec.loader.exec_module(hm)
current_history=hm.collect_history(ROOT,datetime.date(2026,10,16))
week=[h for h in current_history['occurrences'] if h['report_kind'] in ['daily','weekend'] and h['report_window']['start']>=START and h['report_window']['end']<=END and (ROOT/h['artifact']).resolve().parent!=P.resolve()]
dump(P/'within_week_rollup_history.json',{'report_window':{'start':START,'end':END},'occurrences':week})
for d in decisions:
    if d['section']!='industry':continue
    scope(d)
    if d['decision']!='include':continue
    matches=[]
    for h in week:
        # 根据实体和事件标题找同一条，不因综合稿共享来源误把多个事件合并。
        names=[x for x in d['entities'] if x not in ['腾讯','网易','苹果','Xbox']]
        event_match=any(x.lower() in h['title'].lower() for x in names)
        if d['candidate_id']=='I023' and re.search('Q3|第三季度|三季度',h['title']+' '+h['event']) and re.search('资本|并购|移动|市场',h['title']+' '+h['event']):event_match=True
        if not event_match:continue
        hpath=ROOT/h['artifact'];old_input=hpath.with_name('report_inputs.jsonl')
        if not old_input.exists():continue
        om={v['source_id']:v for v in map(json.loads,old_input.read_text(encoding='utf-8').splitlines())}
        urls={om[x]['url'] for x in h['source_ids'] if x in om}
        if urls & {S[x]['url'] for x in d['source_ids']}:matches.append(h)
    if matches:
        hc=d['history_check'];was_pre=hc['history_match'];hc['history_match']=True
        hc['prior_occurrences'] += [f"{h['report_kind']} {h['report_window']['start']}_to_{h['report_window']['end']}｜{h['title']}｜card_exposed={h['card_exposed']};rank={h['card_rank']};limit={h['card_limit']};source={h['card_exposure_source']}" for h in matches]
        hc['prior_card_exposed']=bool(hc['prior_card_exposed']) or any(h['card_exposed'] for h in matches)
        d['weekly_rollup']=True;d['reason']+='；本周日报/周末报事件尚未进入已发布周报，本期合并一次'

# 同一边界事件的单源召回归入唯一事件根，避免把各转载再算独立候选。
by_cid={d['candidate_id']:d for d in decisions}
merge_roots={'B001':['S0855','S0959','S1076'],'B002':['S0850','S0960','S1078'],'B011':['S0895','S0917','S1144','S1175'],'B012':['S1119','S1199','S1243'],'B014':['S0011']}
for root,sids in merge_roots.items():
    for d in decisions:
        if d['candidate_id'].startswith('X') and d['section']=='industry' and d['source_ids'][0] in sids:
            d.update(decision='merge',merge_into=root,reason=f'同一主体/产品、同一事件日期、同一独立事件的单源召回，统一归入{root}评分与排除')
industry_dec={d['candidate_id']:d for d in decisions if d['section']=='industry'}
industry_items=[i for i in items if i['section']=='industry'];industry_items.sort(key=lambda i:(-industry_dec[i['candidate_id']]['scores']['total'],-industry_dec[i['candidate_id']]['scores']['relevance']))
ordered=[]
for section in ['industry','ai','release_calendar','community','deep']:
    ordered += industry_items if section=='industry' else [i for i in items if i['section']==section]
items=ordered

# 先写两份Markdown审计，再保存JSON；最终正文暂存于中间目录。
coverage=['国内移动/国产产品与人才','市场数据','并购','平台政策','档期变动','资本组织','海外重大']
coverage_counts={k:0 for k in coverage}
for d in decisions:
    if d['section']!='industry':continue
    t=d['event'];coverage_counts[coverage[0]]+=int(d['scores']['relevance']==3)
    coverage_counts[coverage[1]]+=int(bool(re.search('数据|收入|流水|市场|下载|日活|月活',t)))
    coverage_counts[coverage[2]]+=int(bool(re.search('融资|并购|收购|投资|入股|股权',t)))
    coverage_counts[coverage[3]]+=int(bool(re.search('平台|政策|Google|苹果|Steam|监管|广告',t,re.I)))
    coverage_counts[coverage[4]]+=int(bool(re.search('发售|测试|上线|首曝|停服|停运|延期',t)))
    coverage_counts[coverage[5]]+=int(bool(re.search('裁员|负责人|管理层|CEO|总经理|部门|融资|重组',t,re.I)))
    coverage_counts[coverage[6]]+=int(d['scores']['relevance']<3 and d['scores']['event']>0)
md=['# 本期事件候选与正文证据', '', f'窗口：{ID}。输入1356条全量JSONL已解析；下列每条保留独立判断。', '']
for d in decisions:
    md += [f"## {d['candidate_id']} - {d['event']}",f"- section: {d['section']}",f"- source_ids: {', '.join(d['source_ids'])}",f"- entities: {' / '.join(d['entities'])}",f"- event_date: {d.get('event_date','按本期来源记录')}",f"- facts/notes: {d['reason']}"]
    for it in items:
        if it['candidate_id']==d['candidate_id']:md += ['- facts: '+it['body'].replace('\n',' ')]
    for e in d.get('source_evidence',[]):md += ['- 原文取证: '+e['evidence'].replace('\n',' ')]
    md += ['']
(P/'event_candidates.md').write_text('\n'.join(md),encoding='utf-8')
md=['# 选材决策', '', '卡片曝光去重：读取9月25日至10月8日全部70条历史记录的card_exposed/card_rank/card_limit/card_exposure_source；历史同事件任一已曝光则不以换源重写。欧盟虚拟货币行动历史均未曝光，但单源7分未达周报8分；本期无card_carryover，排名N/A。', '', '维度覆盖自检：'+'；'.join(f'{k} {v}张候选' for k,v in coverage_counts.items()), '', '产品日历漏挂反查：已反扫974条industry_news及154条release_calendar全文，单产品/日期/事件逐句绑定；保留原始抽取审计，纠正历史月份、预告冒充上线、跨产品背景及主体误加分；全部召回节点均同步决策。', '', '本周日报/周末报事件按within_week_rollup_history.json核对，尚未进入已发布周报者合并一次；不把此类本周汇总误记为card_carryover。', '', '行业与AI/社区同事件不重复；行业与日历允许独立入选。PC单机发售逐条记录scope，不凭RPG/模拟经营标签取R3。', '', '飞书回执987a7ba088484df3a5e13aee0f3518eb：C001/C002/C003为正文顺序；C001是唯一指定卡片。无融合参考；selection lint通过。', '', '| candidate | decision | section | scores / reason |','| --- | --- | --- | --- |']
for d in decisions:
    score=d.get('scores');scoretxt=''
    if score:
        if d['section']=='industry':scoretxt=f"事件{score['event']}×相关{score['relevance']}+钩子{score['hook']} = {score['total']}；"
        else:scoretxt=str(score)+'；'
    md.append(f"| {d['candidate_id']} | {d['decision']} | {d['section']} | {scoretxt}{d['reason'].replace('|','/')} |")
(P/'selection_decisions.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
dump(P/'report_items.json',{'schema_version':1,'report_window':{'start':START,'end':END},'items':items})
dump(P/'selection_decisions.json',{'decisions':decisions})

# 固定脚本同步日历决策，其输出是排序与include/exclude唯一依据。
import subprocess,os
env=dict(os.environ,PYTHONUTF8='1')
subprocess.run([sys.executable,str(ROOT/'scripts/sync_release_decisions.py'),'--audit',str(P/'release_calendar_audit.json'),'--decisions',str(P/'selection_decisions.json'),'--max-items','7'],check=True,env=env)
dd=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))
for d in dd['decisions']:
    if d['section']=='release_calendar':
        n=next(n for n in nodes if n['candidate_id']==d['candidate_id'])
        if d['decision']=='exclude' and n['audit_notes']:d['reason']='；'.join(n['audit_notes'])+'；'+d['reason']
dump(P/'selection_decisions.json',dd)
# 日历审计也补入两份Markdown。
with (P/'selection_decisions.md').open('a',encoding='utf-8') as f:
    for d in dd['decisions']:
        if d['section']=='release_calendar':f.write(f"| {d['candidate_id']} | {d['decision']} | release_calendar | {d['scores']}；{d['reason']} |\n")
with (P/'event_candidates.md').open('a',encoding='utf-8') as f:
    for n in nodes:f.write(f"\n## {n['candidate_id']} - {n['product']} {n['event_date']}\n- section: release_calendar\n- source_ids: {', '.join(n['source_ids'])}\n- facts: {n['event']}\n- notes: {'；'.join(n['audit_notes']) or '同产品同日聚类，独立来源计数与排序详见审计JSON'}\n")

headings={'industry':'一、行业新闻','ai':'二、AI 新闻','release_calendar':'三、新游发布 / 产品日历','community':'四、玩家舆论 / 社区动态','deep':'五、行业精选 / 深度观察'}
md=[f'# 游戏行业周报｜{START}—{END}', '', f'覆盖窗口：{START}—{END}（Asia/Shanghai）。', '']
for sec in headings:
    md += ['## '+headings[sec],'']
    for j,it in enumerate([x for x in items if x['section']==sec],1):
        if sec=='release_calendar':md+=['- '+it['body'],'']
        else:md += [f"### {j}. {it['title']}",'',it['body'],'']
(P/f'game_industry_weekly_{ID}.draft.md').write_text('\n'.join(md),encoding='utf-8')
summary={'report_type':'weekly','id':ID,'input_records':len(rows),'section_counts':dict(Counter(x['section'] for x in items)),
 'industry_scores':[{'title':x['title'],**industry_dec[x['candidate_id']]['scores']} for x in industry_items],
 'history_window':{'start':'2026-09-25','end':'2026-10-08'},'history_occurrences':len(H),'carryover':[],
 'material_updates':[{'title':d['event'],'decision':d['decision'],'new_facts':d['history_check']['new_facts']} for d in dd['decisions'] if d['section']=='industry' and d.get('history_check',{}).get('novelty')=='material_update'],
 'repeat_only':[d['candidate_id'] for d in dd['decisions'] if d['section']=='industry' and d.get('history_check',{}).get('novelty')=='repeat_only'],
 'boundary_5_6':[{'candidate_id':d['candidate_id'],'title':d['event'],'scores':d['scores']} for d in dd['decisions'] if d['section']=='industry' and d['decision']=='exclude' and d['scores']['total'] in [5,6]],'coverage_counts':coverage_counts,'deep_handoff':{'receipt_id':'987a7ba088484df3a5e13aee0f3518eb','body':['C001','C002','C003'],'card':'C001'}}
dump(P/'run_summary.json',summary)
collection=[]
for day in ['2026-10-09','2026-10-10','2026-10-11','2026-10-12','2026-10-13','2026-10-14','2026-10-15']:
    cp=ROOT/'news_data/_collector_runs'/day/'run_summary.json'
    if cp.exists():
        co=json.loads(cp.read_text(encoding='utf-8'));collection.append({'date':day,'started_at':co.get('started_at'),'finished_at':co.get('finished_at'),'problems':[{k:r.get(k) for k in ['collector','status','health','health_note','returncode']} for r in co.get('results',[]) if r.get('status') not in ['ok',None] or r.get('health') not in ['healthy','empty_window','no_update',None]]})
dump(P/'collection_audit_summary.json',collection)
print('WROTE',summary['section_counts'],len(decisions),'decisions +',len(nodes),'calendar nodes')
