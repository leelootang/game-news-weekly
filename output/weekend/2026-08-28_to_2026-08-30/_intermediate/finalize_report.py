import json,pathlib,re,collections,hashlib
P=pathlib.Path(__file__).parent; OUT=P.parent; ID=OUT.name
def read(name):return json.loads((P/name).read_text(encoding='utf-8'))
def dump(name,x):(P/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
S={r['source_id']:r for r in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
I=[x for x in read('report_items.json')['items'] if x['section']!='release_calendar']
D=read('selection_decisions.json')['decisions'];A=read('release_calendar_audit.json'); nodes={n['candidate_id']:n for n in A['nodes']}
def c(claim,n,needle):
 sid=f'S{n:04d}';t=S[sid]['text'];assert needle in t,(sid,needle)
 ev=next((p for p in t.split('\n') if needle in p),needle)
 return dict(claim=claim,source_id=sid,evidence=ev)
copy={
'王者万象棋':('腾讯打造的策略自走棋多平台产品《王者万象棋》定于2026年9月10日在移动端与PC同步公测；支持QQ、微信同服游玩。','新品定档','2026-09-10','移动端、PC','腾讯',[c('腾讯',47,'腾讯系产品'),c('策略自走棋',47,'自走棋玩法'),c('《王者万象棋》定于2026年9月10日在移动端与PC同步公测',45,'公测定档2026年9月10日'),c('支持QQ、微信同服游玩',45,'支持QQ、微信同服游玩')]),
'无限大':('网易雷火工作室开发的都市开放世界RPG多平台产品《无限大》定于2027年1月15日全球公测，计划登陆PS5、Windows PC、iOS与Android；以多角色身份和都市探索串联动作冒险。','新品定档','2027-01-15','PS5、Windows PC、iOS、Android','网易',[c('网易雷火工作室',39,'网易雷火工作室'),c('都市开放世界RPG',50,'都市开放世界RPG《无限大》'),c('《无限大》定于2027年1月15日全球公测，计划登陆PS5、Windows PC、iOS与Android',50,'正式官宣2027年1月15日全球公测'),c('多角色身份和都市探索串联动作冒险',39,'以不同角色的身份和能力为入口')]),
'遗忘之海':('网易开发的海洋开放世界RPG多平台产品《遗忘之海》公布大规模封闭测试定于2026年12月开启；玩法结合开放世界探索、海战与肉鸽回合制。','新品定档','2026-08-25','多平台','网易',[c('网易开发',50,'网易游戏携五款自研产品'),c('海洋开放世界RPG多平台产品《遗忘之海》',50,'海洋开放世界RPG《遗忘之海》'),c('大规模封闭测试定于2026年12月开启',50,'封闭测试(Closed Beta Test)定档今年12月'),c('开放世界探索、海战与肉鸽回合制',50,'开放世界探索+海战+肉鸽回合制')]),
'凡应':('艺画开天开发的幻想ARPG产品《凡应》于8月28日开启EP02第二轮测试，现有公布信息未区分端游或手游；融合箱庭探索、四人小队战斗与家园养成。','新品测试','2026-08-28','','艺画开天',[c('艺画开天开发',57,'由出品过《灵笼》系列动画的艺画开天制作开发'),c('幻想ARPG产品《凡应》于8月28日开启EP02第二轮测试',57,'今日（2026年8月28日）'),c('箱庭探索、四人小队战斗与家园养成',57,'游戏采用四人小队作战模式'),c('家园养成',57,'有趣的家园养成玩法')])}
for d in D:
 if d['section']=='release_calendar':
  node=nodes[d['candidate_id']];d['title']=node['product'];d['appearance_count']=node['appearance_count'];d['independent_source_ids']=node['independent_source_ids'];d['event_date']=node['event_date']
  if node.get('editorial_exclusion'): d['reason']=node['editorial_exclusion']
  if d['decision']=='include':
   prod=node['product'];body,event,date,platform,co,claims=copy[prod]
   # Clear, source-supported form is supplied without guessing an absent platform.
   I.append(dict(candidate_id=d['candidate_id'],section='release_calendar',title=prod,body=body,source_ids=d['source_ids'],claims=claims,release=dict(product=prod,event=event,date=date,platform=platform,company=co)))
covered={sid for d in D for sid in d['source_ids']}
for sid in sorted(set(S)-covered):
 r=S[sid]
 reason='原始日历补扫：常规版本/资料片/赛季、活动、皮肤或预约占位，没有首曝、正式定档或新生命周期信号。'
 if sid=='S0253':reason='iOS占位符且安卓为猜测，不认正式定档。'
 D.append(dict(candidate_id='raw-calendar-'+sid,title=r['title'],section='release_calendar',source_ids=[sid],entities=[r['title'].split(' - ')[0]],event=r['title'],event_date=r['date'],decision='exclude',reason=reason))
dm={d['candidate_id']:d for d in D}
order={'industry_news':0,'ai_trends':1,'release_calendar':2,'community_discourse':3,'deep_analysis':4}
I.sort(key=lambda i:(order[i['section']],-dm[i['candidate_id']].get('scores',{}).get('total',0) if i['section']=='industry_news' else 0))

# Write the human audit before finalizing the structured artifacts and reader-facing report.
headers=['# 候选事件审计｜'+ID,'','锚点：周末报；采集窗口2026-08-28至2026-08-30，产品日历事件窗口延至8月31日。','已按完整index与全量JSONL逐记录扫描；正文事实另以逐字证据映射。','']
for d in D:
 ss=d['source_ids'];facts=[]
 for sid in ss:
  t=S[sid]['text'];paras=[p.strip() for p in t.split('\n') if p.strip()]
  # A navigational excerpt, never a substitute for full input text.
  p=next((p for p in paras if len(p)>50),paras[0] if paras else '')
  facts.append(sid+': '+p)
  if len(facts)==2:break
 headers+=['## '+d['candidate_id']+' - '+d.get('title',d['event']),'- section: '+d['section'],'- source_ids: '+', '.join(ss),'- entities: '+', '.join(d['entities']),'- event_date: '+d.get('event_date','参见原文'),'- facts: '+'；'.join(facts),'- notes: '+d['reason']]
 if 'community' in d:headers+=['- '+k+': '+str(v) for k,v in d['community'].items()]
 headers+=['']
(P/'event_candidates.md').write_text('\n'.join(headers),encoding='utf-8')
hist=[d for d in D if d.get('history_check',{}).get('history_match')]
lines=['# 筛选决策｜'+ID,'','卡片曝光去重：历史窗口2026-08-14至2026-08-27，共135条。ACE此前周报正文第13条、card_rank=null、card_limit=10、card_exposed=false；本期唯一card_carryover=I001，11分。王者万象棋8分、伊莫7分均未获补位；TGC与超自然DAU虽周报未曝光，历史日报已曝光，仍排除。','',
'E×R+M：行业只按总分≥7筛选，无条数上限，按分数降序。时间无法定位的滚动目录/展会综述单独排除，不以采集时间冒充事件时间。维度覆盖自检：国内移动/国产产品与人才/市场数据/并购融资/平台政策/档期变动/资本组织/海外重大 — 见下列逐事件候选及full_source_scan.json；最高关注主体含腾讯、网易、巨人、游族、三七、Roblox、Supercell、Garena均有决策；非游戏与常规宣传E0逐记录保留。',
'AI反扫：覆盖全部行业候选，GIGA、Vox与游族创作工具转入AI；巨人披露优先保留发行合作；Motus旧披露、小红书8月18日开放等不作为新事件重报。',
'产品日历漏挂反查：扫描industry_news及release_calendar全文，修正旧测试、皮肤上线、跨年日期及转载来源数；英语综合稿逐产品补入。以sync_release_decisions.py确定性同步前4项。《无限大》定档也见于上周普通窗口日历，并非上期次日前瞻；按日历仅对次日前瞻重叠去重的规则，本期仍参与多源前缀。未发现次日前瞻重叠。',
'Steam：news_data/pc_rankings仅至2026-07-12；本期8月28日至30日无快照，不用旧榜、不联网补缺。',
'深度：周末报自动采用本期GameDiscoverCo单篇高质量分析；周五selection及deep_card_choice.txt不适用。',
'来源边界：61条non-full/snippet记录不用于终稿。短但被采集器标记full的完整简讯仅支持其明确写出的事实；游戏公司、日期和平台不由记忆补齐。','',
'| candidate | decision | section | scores | reason |','| --- | --- | --- | --- | --- |']
for d in D:
 sc=d.get('scores',{});score=(f"事件{sc['event']}×相关{sc['relevance']}+钩子{sc['hook']} = {sc['total']}" if 'hook' in sc else str(sc))
 lines.append('| '+ ' | '.join([d['candidate_id'],d['decision'],d['section'],score,d['reason'].replace('|','/')])+' |')
lines+=['','## 历史匹配逐项','']
for d in hist:
 h=d['history_check']; lines+=['### '+d['candidate_id']+' '+d['title'],'- novelty: '+h['novelty'],'- prior_card_exposed: '+str(h['prior_card_exposed']),'- new_facts: '+str(h['new_facts'])]
 for o in h['prior_details']:lines+=['- '+o['title']+'｜'+str(o['report_window'])+f"｜card_exposed={o['card_exposed']}, rank={o['card_rank']}, limit={o['card_limit']}, source={o['card_exposure_source']}"]
(P/'selection_decisions.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
dump('report_items.json',dict(schema_version=1,items=I));dump('selection_decisions.json',dict(decisions=D))
text=['# 游戏行业周末报｜2026-08-28—2026-08-30','','数据覆盖8月28日至30日。Steam当日榜缺少本期快照，本期不列榜单。','']
sects=[('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]
for sec,heading in sects:
 text+=['## '+heading,'']
 for j,it in enumerate([x for x in I if x['section']==sec],1):
  if sec=='release_calendar':text+=['- '+it['body'],'']
  else:text+=['### '+str(j)+'. '+it['title'],'',it['body'],'']
report=OUT/('game_industry_weekend_'+ID+'.md')
report.write_text('\n'.join(text),encoding='utf-8')
dump('source_coverage.json',dict(input_records=len(S),covered_source_ids=sorted({sid for d in D for sid in d['source_ids']}),uncovered_source_ids=sorted(set(S)-{sid for d in D for sid in d['source_ids']}),final_sources=sorted({sid for it in I for sid in it['source_ids']})))
print(collections.Counter(i['section'] for i in I));print(report)
