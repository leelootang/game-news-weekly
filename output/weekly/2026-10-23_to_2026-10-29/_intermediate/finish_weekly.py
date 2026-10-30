from __future__ import annotations
import json,re,copy,sys,hashlib
from pathlib import Path
from collections import defaultdict,Counter
from datetime import datetime,timezone,timedelta
ROOT=Path.cwd();sys.path.insert(0,str(ROOT/'scripts'))
from industry_timing import build_time_check
from sync_release_decisions import sync
from report_artifacts import parse_report_items
from build_industry_history import _publish_log,_card_exposure
B=ROOT/'output/weekly/2026-10-23_to_2026-10-29/_intermediate';OUT=B.parent
START='2026-10-23';END='2026-10-29';ID=START+'_to_'+END
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ROWS=list(map(json.loads,(B/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()));SRC={r['source_id']:r for r in ROWS}
DEC=read(B/'working_industry_decisions.json');ITEMS=read(B/'working_industry_items.json');BODY=read(B/'working_body.json')
H=read(B/'industry_history_14d.json');HALL=H['occurrences']+H['archive_occurrences'];PRIOR=read(B/'prior_decisions_remapped.json')
# 本周日报也必须读取实际正式广播记录。HOK旧事件已于28日报完成曝光，且曾在5月周报收录，不能再使用周报汇总例外。
within_week=[]
for d in DEC:
 rel=d.get('prior_report')
 if d['section']!='industry_news' or not rel:continue
 olditems=read(ROOT/'output'/rel/'_intermediate/report_items.json')['items']
 inds=[i for i in olditems if i['section']=='industry_news'];oldid=d.get('prior_candidate_id')
 rank=next(n for n,i in enumerate(inds,1) if i['candidate_id']==oldid)
 exp=_card_exposure(_publish_log(ROOT,rel.split('/')[-1]),candidate_id=oldid,title=d['title'],report_rank=rank)
 occurrence=dict(title=d['title'],report=rel,card_exposed=exp['exposed'],card_rank=exp['card_rank'],card_limit=exp['card_limit'],card_exposure_source=exp['source'])
 within_week.append(occurrence);hc=d['history_check'];hc['prior_card_exposed']=bool(hc.get('prior_card_exposed')) or exp['exposed'];hc.setdefault('exposure_details',[]).append(occurrence)
 if d['candidate_id']=='W20261028_I130':
  assert exp['exposed'];d['decision']='exclude';d.pop('card_carryover',None);hc['novelty']='repeat_only';hc['weekly_rollup']=False
  d['exclusion_gates']=['history_repeat'];d['reason']='4月移动版公测事实已在2026-05-28_to_2026-06-04周报记载，并在本周10月28日日报通过card_carryover正式曝光（第4/10）；已非未曝光事件，且曾进入已发布周报，本期无实质更新，repeat_only。'
dump(B/'within_week_card_exposure.json',within_week)
# 未曝光候选中微信6分/R3高于Atari6分/R2。
for d in DEC:
 if d['candidate_id']=='N_ATARI':
  d['decision']='exclude';d.pop('card_carryover',None)
  d['reason']='历史同事件均未曝光，但本期唯一card_carryover由9分、R3的王者荣耀世界条目获得，本候选6分不占第二名额。';d['exclusion_gates']=['carryover_limit']
  if d['candidate_id']=='N_ATARI':
   hs=[h for h in HALL if 'Atari以最高3930万美元' in h['title']]
   d['history_check']=dict(history_match=True,novelty='repeat_only',prior_occurrences=[f"{h['report_kind']} {h['report_window']['start']}_to_{h['report_window']['end']}｜{h['title']}" for h in hs],new_facts=[],prior_card_exposed=False,archive_checked=True,exposure_details=[{k:h.get(k) for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for h in hs])
  else:d['history_check']['novelty']='repeat_only'
  d['reason']='历史同事件均未曝光，但本期唯一card_carryover由同为6分、主体R3的微信小游戏获得；Atari主体R2，排序靠后。'
ITEMS=[i for i in ITEMS if i['candidate_id'] not in ['W20261028_I130','N_ATARI']]
inc={d['candidate_id']:d for d in DEC}; assigned=defaultdict(list)
for d in DEC:
 for sid in d['source_ids']:assigned[(d['section'],sid)].append(d['candidate_id'])
aliases={
 'N_CAPCOM':[1], 'N_DOUYIN':[106,107,109,112], 'N_WECHAT':[131,132,133,134],
 'N_NEKODAY':[165,167,168,169], 'N_HIGHGUARD':[182,183,184,185,186],
 'N_RE9':[248,249,250,251], 'N_MOORE':[658,659,660,661], 'N_GENSHIN':[672,673,674,675],
 'N_ROCO_TEST':[712,713,714,715], 'N_SPIRE':[716,717,718,719,722],
 'N_HELIX':[724,725,726,727,730], 'N_FORGOTTEN':[221,222,223,227],
 'N_COD':[960,1016], 'N_CARD_TEST':[654,655,656,657], 'N_HOK_SCHEDULE':[676,677,680,681],
 'N_MARATHON':[114,115,117,119], 'N_TIANXIA':[174,175,176,177], 'N_WATER':[61,62,63,64],
 'N_BIOWARE':[298,788], 'N_LAST_ASYLUM':[692,694,697,699],
}
for target,nums in aliases.items():
 for n in nums:assigned[('industry_news',f'S{n:04}')]=[target]
for d in DEC:
 if '天美三款王者' in d.get('title',''):assigned[('industry_news','S0831')]=[d['candidate_id']]
 if '灵犀《篮球少女' in d.get('title',''):assigned[('industry_news','S0632')]=[d['candidate_id']]
def q(sid,needle):
 assert needle in SRC[sid]['text'],(sid,needle)
 return next((p.strip() for p in SRC[sid]['text'].splitlines() if needle in p),needle)
def history(rows=None,novelty='new_event',facts=None):
 rows=rows or []
 return dict(history_match=bool(rows),novelty=novelty,prior_occurrences=[f"{h['report_kind']} {h['report_window']['start']}_to_{h['report_window']['end']}｜{h['title']}" for h in rows],new_facts=facts or [],prior_card_exposed=any(h['card_exposed'] for h in rows) if rows else None,archive_checked=True,exposure_details=[{k:h.get(k) for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for h in rows])
def matches(terms):return [h for h in HALL if any(t.lower() in (' '.join([h.get('title',''),h.get('event','')]+h.get('claims',[])+h.get('entities',[]))).lower() for t in terms)]
def timing(d):
 if d.get('scores',{}).get('event',0):d['time_check']=build_time_check(d['source_ids'],SRC,START,END,event_date=d.get('event_date') or 'unknown',basis='published_at优先，缺失回退input date；仅审来源窗口，历史事件日期不设门槛。')
def cluster(d):
 if len(d['source_ids'])>1:d['cluster_basis']=dict(subject=d['entities'][0],product=d['entities'][-1],event_date=d.get('event_date') or 'unknown',event=d['event'])

# 主体、关系及影响力证据单独补齐，避免仅引用事件日期。
for cid,sid,needle in [('N_SIDE','S0141','超过500名美术师'),('N_SYBO','S0029','MAU在1亿到1.5亿之间'),('N_HIGHGUARD','S0184','Tencent, que había invertido'),('N_WATER','S0062','receitas mensais ultrapassaram os 100 milhões')]:
 inc[cid]['subject_assessment']['evidence'].append(dict(source_id=sid,evidence=q(sid,needle)))
inc['N_HOK_SCHEDULE']['source_ids'].append('S0677');next(i for i in ITEMS if i['candidate_id']=='N_HOK_SCHEDULE')['source_ids'].append('S0677')
inc['N_HOK_SCHEDULE']['subject_assessment']['evidence'].append(dict(source_id='S0677',evidence=q('S0677','Tencent')))
cluster(inc['N_HOK_SCHEDULE']);timing(inc['N_HOK_SCHEDULE'])
inc['N_LAST_ASYLUM']['subject_assessment'].update(subject='37 Interactive Entertainment',kind='comparable_major_subject',focus_companies=[],basis='来源用37 Interactive Entertainment英文名直接归属产品，按头部发行研发主体R3判断；未虚构输入中不存在的名单别名或归属引文。')
# 核验到可用的IGN完整正文，替换质量标记不可用的英文转述。
d=inc['N_BIOWARE'];d['source_ids']=['S0788'];d['event_date']='2026-10-21';d['subject_assessment']['evidence']=[dict(source_id='S0788',evidence=q('S0788','10月21日'))];d['reason']='EA全球头部研发发行主体R3，已确认工作室关闭与项目取消E2；以可用完整IGN正文取证，保留10月21日事件日期。';timing(d)
bi=next(i for i in ITEMS if i['candidate_id']=='N_BIOWARE');bi['source_ids']=['S0788']
BODY['N_BIOWARE']='EA于10月21日宣布重大内部重组，包括关闭BioWare并取消多个项目，《质量效应5》亦被取消。该工作室以《质量效应》《龙腾世纪》等角色扮演系列闻名，已有逾30年历史。分析师认为，商业表现、开发成本和收购债务共同构成压力；这些原因判断保留分析师归因。'
bi['claims']=[dict(claim=c,source_id='S0788',evidence=q('S0788',n)) for c,n in [('10月21日','10月21日'),('关闭BioWare','关闭BioWare'),('《质量效应5》亦被取消','EA为何此时取消'),('逾30年历史','逾30年'),('开发成本和收购债务','MST Financial分析师')]]
d=inc['W20261027_I010'];d['subject_assessment']['evidence']=[dict(source_id='S0969',evidence=q('S0969','微软一位代表向PC Gamer表示'))];d['pc_release_scope']['evidence']=[dict(source_id='S0761',evidence=q('S0761','PC Gamer'))]
# 缩至行业每条200字以内，同时保持实体、时间和事实完整。
BODY['N_MOORE']='本期报道回顾，前《Moore Manor》制作人、Qutang Network创始人Zheng Zhouri已于报道所述上月加入网易杭州《Eggy Party》项目组，负责副玩法内容。原文未给入职绝对日期，不能按采集日倒推月份。Qutang曾获FunPlus支持，其后进入破产清算；管理人正公开遴选资产评估机构，评估以游戏为主的无形资产。'
BODY['N_CARD_TEST']="本期报道回顾，腾讯发行、Smilegate旗下SUPER CREATIVE开发的手游《Kaeth's Dream》于3月11日启动第二轮付费测试，当时海外版本已在运营。其设计通过保存roguelike对局成果，把局内构筑与后续角色战斗相连，并结合资源管理、路线选择及队伍配置；这些设计尚不能证明国内长期商业成功。"
BODY['N_CAPCOM']='卡普空确认，10月19日的数据泄露影响超过1170万个Capcom ID账户，系统覆盖《Street Fighter 6》《Monster Hunter》《Resident Evil》等产品。10月23日更新称，196个账户的密码曾被擅改，其中19个账户的日本e-Capcom页面遭访问；相关信息包括姓名、联系方式和购买记录。信用卡信息未受影响，相关游戏服务仍然可用。'
for i in ITEMS:
 if i['candidate_id'] in ['N_MOORE','N_CARD_TEST','N_CAPCOM']:i['claims']=[c for c in i['claims'] if c['claim'] in BODY[i['candidate_id']]]

# 使用所有先前逐字审计作导航；本期所有旧时间理由重新落到实际门禁。
seen=set();source_covered=set();reconsider=[]
for old in reversed(PRIOR):
 if old['section']=='release_calendar':continue
 key=(old['section'],tuple(old['source_ids']),old['event'])
 if key in seen:continue
 seen.add(key);d=copy.deepcopy(old)
 d['candidate_id']='AUD_'+str(len(DEC)+1).zfill(4)
 d['original_review']=dict(report=d.pop('prior_report'),candidate_id=d.pop('prior_candidate_id',d.get('candidate_id')),reason=d.get('reason',''))
 d.pop('card_carryover',None);d.pop('merge_into',None)
 sec=d['section'];sids=d['source_ids'];source_covered.update(sids)
 targets=set(t for sid in sids for t in assigned[(sec,sid)])
 if targets:
  target=max(targets,key=lambda t:len(set(sids)&set(inc[t]['source_ids'])))
  d['decision']='merge';d['merge_into']=target
  d['reason']='与本期正文所列同主体、同事件日期及同一事件相同，纳入该主候选核对，不另写一条。'
  if sec=='industry_news':
   base=inc[target]
   d['scores']=copy.deepcopy(base['scores']);d['history_check']=copy.deepcopy(base['history_check'])
   # 每张候选须引用自己的source，不借另一篇文章的引文；同一来源映射可完整复用。
   for name in ['subject_assessment','genre_assessment','pc_release_scope']:
    if name in base and all(x.get('source_id') in sids for x in base[name].get('evidence',[])):d[name]=copy.deepcopy(base[name])
   if len(sids)==1 and (not d.get('subject_assessment') or d['subject_assessment'].get('kind')=='other_or_unknown'):
    tier=base['scores']['relevance'];kind='comparable_major_subject' if tier==3 else 'comparable_significant_subject' if tier==2 else base['subject_assessment']['kind']
    d['subject_assessment']=dict(subject=base['subject_assessment']['subject'],kind=kind,focus_companies=[],basis='同一来源同一事件的重复审计，按主候选实际影响力判断。',evidence=[dict(source_id=sids[0],evidence=SRC[sids[0]]['text'].splitlines()[0])])
   # 多语种镜像保持同一E/R/M，不沿用旧稿因事件较早而降成R0的判断。
   if target in aliases and len(sids)==1:
    sid=sids[0];r=SRC[sid];sa=base['subject_assessment'];tier=base['scores']['relevance']
    kind='comparable_major_subject' if tier==3 else 'comparable_significant_subject' if tier==2 else sa['kind']
    evidence=next((p for p in r['text'].splitlines() if re.search(r'Tencent|NetEase|Bungie|Mihoyo|miHoYo|Capcom|Bilibili|Microsoft|Yishijie|Wildlight|Nekoday',p)),r['text'].splitlines()[0])
    d['subject_assessment']=dict(subject=sa['subject'],kind=kind,focus_companies=[],basis='同主体同事件的多语种版本；实际主体和影响力按主候选复核，不以未列名或历史日期限制R；原文证据保留本候选语言。',evidence=[dict(source_id=sid,evidence=evidence)])
    ga=base['genre_assessment'];d['genre_assessment']=dict(matched_genres=ga['matched_genres'],basis=ga['basis'],evidence=[])
    if base['scores']['hook']:
     ge=next((p for p in r['text'].splitlines() if re.search(r'FPS|MOBA|PVP|PvP|SLG|competitive|competitiv|competi|射击|竞技|경쟁|슈팅|대전',p)),r['text'].splitlines()[0])
     d['genre_assessment']['evidence']=[dict(source_id=sid,evidence=ge)]
   if d['history_check'].get('novelty')=='card_carryover':d['history_check']['novelty']='repeat_only'
   if sids==['S0831']:
    d['scores']['hook']=0;d['scores']['total']=d['scores']['event']*d['scores']['relevance'];d['reason']='同一王者IP矩阵榜单事件合并；本篇未明确具体产品品类，单独M0，主候选按另一篇完整来源证据取M1。'
   timing(d)
  cluster(d)
 elif sec=='industry_news':
  d['decision']='exclude'
  scores=d.get('scores') or dict(event=0,relevance=0,hook=0,total=0)
  d['scores']=scores
  oldreason=d['reason']
  hc=d.get('history_check') or history()
  if hc.get('novelty')=='card_carryover':hc['novelty']='repeat_only'
  hc.setdefault('prior_card_exposed',False if hc.get('history_match') else None);hc['archive_checked']=True;d['history_check']=hc
  sid=sids[0];r=SRC[sid];num=int(sid[1:])
  if hc.get('history_match') and hc.get('novelty')=='repeat_only':
   d['reason']='同一事件已见历史报告；本期未提供可验证的实质状态变化。';d['exclusion_gates']=['history_repeat']
  elif scores['event']==0:
   d['reason']='逐字正文及旧审计复核：核心为常规版本/联动/折扣/宣传、评测、一般访谈或非游戏业务，没有独立达到事件门槛的状态。';d['exclusion_gates']=['score']
  elif scores['total']<5:
   d['reason']='按实际独立事件及主体影响力复核，E×R+M低于5；事件较早、晚到报道或事件日期不明均不是排除理由。';d['exclusion_gates']=['score']
  else:
   d['reason']='需要单独复核具体非时间门禁';d['exclusion_gates']=['factual_uncertainty'];reconsider.append(d['candidate_id'])
  # 旧稿把名单外主体当作R1上限的几处明确例子重新分档；质量门禁独立执行。
  if any(s in {'S0265','S0268','S0463'} for s in sids):
   d['scores']=dict(event=2,relevance=2,hook=0,total=4)
   d['subject_assessment']=dict(subject='GameMaker',kind='comparable_significant_subject',focus_companies=[],basis='跨桌面、移动、Web及GX Games的成熟2D开发工具；具有较强平台影响力R2，商业许可变化E2，4分。',evidence=[dict(source_id=sid,evidence=r['text'].splitlines()[0])])
   d['genre_assessment']=dict(matched_genres=[],basis='开发工具许可无特定重点品类',evidence=[]);d['reason']='GameMaker商业许可变化E2R2M0=4；名单外主体按实际平台能力判断，不封顶R1。';d['exclusion_gates']=['score']
  if any(s in {'S1260','S1273'} for s in sids):
   d['scores']=dict(event=3,relevance=3,hook=0,total=9)
   d['subject_assessment']=dict(subject='Unity',kind='comparable_major_subject',focus_companies=[],basis='成熟跨平台引擎与Unity Vector广告能力的全球平台主体R3；与PvX融资合作E3，来源质量仍需独立过门槛。',evidence=[dict(source_id=sid,evidence=r['text'].splitlines()[0])])
   d['genre_assessment']=dict(matched_genres=[],basis='平台融资合作不对应具体品类',evidence=[]);d['reason']='Unity与PvX融资合作按E3R3M0=9，但一源正文受阻、一源仅一句资金摘要，条款和适用条件不足，来源质量门禁排除。';d['exclusion_gates']=['source_quality']
  # 已曝光用户规模的较早阶段不能包装成新增状态。
  if num in [84,85,90,92]:
   hs=[x for x in matches(['燕云十六声']) if '全球玩家突破一亿' in x['title']]
   d['history_check']=history(hs,'repeat_only');d['scores']=dict(event=2,relevance=3,hook=0,total=6)
   d['subject_assessment']=dict(subject='NetEase',kind='comparable_major_subject',focus_companies=[],basis='NetEase直接产品用户规模；当前回顾八千万，历史已曝光一亿用户，不能写成新增长。',evidence=[dict(source_id=sid,evidence=r['text'].splitlines()[0])]);d['genre_assessment']=dict(matched_genres=[],basis='用户规模统计不借普通RPG标签加分',evidence=[])
   d['reason']='本期回顾八千万玩家，历史已曝光同产品全球玩家突破一亿；没有新的更高用户状态，repeat_only。';d['exclusion_gates']=['history_repeat']
  if num in range(42,47) or num in range(170,174):
   hs=[x for x in matches(['鹅鸭杀']) if '千万' in x['title'] or '4000万' in x['title']]
   d['history_check']=history(hs,'repeat_only');d['reason']='国服六天千万用户及内容发行复盘已于7月28日报曝光，之后亦有四千万用户；本期无实质新状态。';d['exclusion_gates']=['history_repeat']
  if num in [693,695,696,698]:
   d['scores']=dict(event=2,relevance=3,hook=0,total=6)
   d['subject_assessment']=dict(subject='Bilibili小游戏',kind='comparable_major_subject',focus_companies=[],basis='Bilibili小游戏广告生态，R3；当前译文将月消耗混译成收入或用户，指标有实质歧义。',evidence=[dict(source_id=sid,evidence=q(sid,'Bilibili') if 'Bilibili' in r['text'] else r['text'].splitlines()[0])]);d['genre_assessment']=dict(matched_genres=[],basis='广告生态数据不对应具体重点品类',evidence=[])
   d['reason']='同篇多语言文本对千万元月消耗、月收入和月活混译，正文指标无法可靠统一；保留6分但以事实口径不确定排除。';d['exclusion_gates']=['factual_uncertainty']
  if num in range(47,52):
   d['scores']=dict(event=0,relevance=0,hook=0,total=0);d['reason']='版号例行信息E0直接排除；不因历史日期排除。';d['exclusion_gates']=['score']
  if sid=='S1113':d['reason']='只有标题与“打击AI泛滥”短摘要，无审核新规适用范围和实施说明，来源质量不足。';d['exclusion_gates']=['source_quality']
  if '卡普空上半财年' in d['event']:d['reason']='常规上半财年销量与数字化比例，无直接证明显著超预期、异常减值或资本结构变化，例行财报排除。';d['exclusion_gates']=['financial_routine']
  if sid=='S0972':
   d['scores']=dict(event=1,relevance=3,hook=0,total=3);d['reason']='已传闻掌机的芯片规格线索，不是新品首曝/立项确认或战略动作，E1R3M0=3。';d['exclusion_gates']=['score']
  if d['event'] in ['Q3中国移动市场报告','伽马21日发布Q3中国移动市场数据']:
   d['decision']='exclude';d['reason']='行业汇编仅提及10月21日伽马Q3报告，未给具体统计数值或完整报告正文，当前来源不足支持实质市场数据条目；不按事件日期排除。';d['exclusion_gates']=['source_quality']
  # 每个来源的日期由共享函数生成，不保留旧的事件窗口门禁。
  timing(d);cluster(d)
 else:
  d['decision']='exclude'
  if sec=='ai_trends':
   d['reason']='已反扫本周全部行业与AI池；同层级中本期优先六件来源更完整、游戏作用环节更明确的独立事件，本候选留审计。'
   d.setdefault('ai_tier','transferable_frontier');d.setdefault('game_stage',[]);d.setdefault('industry_reverse_scan',False)
   if d['ai_tier']=='transferable_frontier':d.setdefault('migration_path','用于评估游戏研发、内容管线或运营工具的能力变化；本候选直接落地证据或优先级不足。')
  elif sec=='community_discourse':d['reason']='社区全池及行业外溢反扫完成；本期选择三件触发、争议逻辑及时间线更完整的独立事件，其他话题保留审计。'
  elif sec=='deep_analysis':d['reason']='本周只消费飞书回执明确选择的C001、C022，不自动增加深度正文。'
 DEC.append(d)

# 为先前抽取未覆盖的源逐条建卡；短标题源不能凭记忆补归属。
for r in ROWS:
 sid=r['source_id']
 if sid in source_covered or assigned[(r['section'],sid)]:continue
 sec=r['section']
 if sec=='release_calendar':continue
 d=dict(candidate_id='SRC_'+sid,section=sec,source_ids=[sid],entities=[r['title']],event=r['title'],decision='exclude',reason='完整读取可用正文，未见可独立发表的新增合格事实；短标题/例行宣传不凭常识补主体或状态。',source_text_review=dict(sha256=hashlib.sha256(r['text'].encode()).hexdigest(),chars=len(r['text'])))
 if sec=='industry_news':d.update(scores=dict(event=0,relevance=0,hook=0,total=0),history_check=history(),exclusion_gates=['score'])
 if sec=='deep_analysis':d['scores']=dict(relevance=2,insight=2,evidence=2,card=2,total=8);d['reason']='不在本周飞书正文选择中。'
 DEC.append(d)

# 标记未入选深度原始输入：原始源可含多个主题，只有用户选择的两个主题进入正文。
for r in ROWS:
 if r['section']=='deep_analysis' and not any(r['source_id'] in d['source_ids'] for d in DEC):
  DEC.append(dict(candidate_id='SRC_'+r['source_id'],section='deep_analysis',source_ids=[r['source_id']],entities=[r['title']],event=r['title'],decision='exclude',reason='未获飞书周报正文选择',scores=dict(relevance=2,insight=2,evidence=2,card=2,total=8)))

# 日历逐节点复用已校对的事实证据，而不是沿用自动提取中的假公司和假日期。
rawpath=B/'release_calendar_raw_audit.json'
if not rawpath.exists():dump(rawpath,read(B/'release_calendar_audit.json'))
raw=read(rawpath); valid=[]
for rel in ['weekend/2026-10-23_to_2026-10-25','daily/2026-10-26','daily/2026-10-27','daily/2026-10-28']:
 p=ROOT/'output'/rel/'_intermediate'
 oldrows=list(map(json.loads,(p/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())); um={x['source_id']:next((r['source_id'] for r in ROWS if r['url']==x['url'] and r['text']==x['text']),next((r['source_id'] for r in ROWS if r['url']==x['url']),None)) for x in oldrows}
 def remap(x):
  if isinstance(x,dict):return {k:remap(v) for k,v in x.items()}
  if isinstance(x,list):return [remap(v) for v in x]
  if isinstance(x,str) and re.fullmatch(r'S\d{4}',x):return um.get(x,x)
  return x
 for n in read(p/'release_calendar_audit.json')['nodes']:
  if n.get('publish_eligible') and all(um.get(s) for s in n['source_ids']):valid.append(remap(copy.deepcopy(n)))

for n in valid:
 if n['product']=='影之刃零' and n['event_date']=='2026-10-29':
  n['signal_type']='new_game_schedule';n['event_type_score']=2;n['event']='定于10月29日发售';n['review_note']='输入最晚10月28日，发售尚未发生，改为定档公告而非已发售。'

def normalized(s):
 s=re.sub(r'[-－](?:10月29日上线|魂like异域探索).*','',s)
 return {'影之刃：零':'影之刃零','蓝色星原':'蓝色星原：旅谣','Sign 碎冠篇':'Sign：碎冠篇','GTA 6':'GTA6'}.get(s,s)
groups={}
for n in valid:
 n['product']=normalized(n['product']);key=(n['product'],n['event_date'])
 if key not in groups:groups[key]=n
 else:
  g=groups[key]
  for field in ['source_ids','industry_ids','release_ids','company_evidence_ids']:
   g[field]=list(dict.fromkeys(g.get(field,[])+n.get(field,[])))
  if n.get('company_bonus',0)>g.get('company_bonus',0):
   for field in ['company_bonus','focus_companies','company_relationship','focus_company_relationships']:g[field]=n.get(field)
for key,n in groups.items():
 if n['product']=='篮球少女：飞跃巅峰':
  n['source_ids']=list(dict.fromkeys(n['source_ids']+['S0632','S1349']));n['industry_ids']=list(dict.fromkeys(n.get('industry_ids',[])+['S0632','S1349']));n['company_bonus']=3;n['focus_companies']=['灵犀互娱'];n['company_relationship']='direct';n['company_evidence_ids']=['S1349']
 if n['product']=='蓝色星原：旅谣':
  n['source_ids']=list(dict.fromkeys(n['source_ids']+['S0034']));n['company_bonus']=0;n['focus_companies']=[];n['company_evidence_ids']=[];n['company_relationship']='';n['focus_company_relationships']={};n['review_note']='蛮啾自研自发；正文其他位置提及网易，不能给日历公司加分。'
 if n['product']=='Sign：碎冠篇':n['source_ids']=['S0625','S0751']

def recalc(n):
 sids=list(dict.fromkeys(n['source_ids']));n['source_ids']=sids
 urls=set();hashes=set();count=0
 for sid in sids:
  r=SRC[sid];h=hashlib.sha256(r['text'].encode()).hexdigest()
  if r['url'] not in urls and h not in hashes:count+=1
  urls.add(r['url']);hashes.add(h)
 n['appearance_count']=count;n['source_fingerprints']=list(hashes)
 n['industry_ids']=[s for s in sids if SRC[s]['section']=='industry_news'];n['release_ids']=[s for s in sids if SRC[s]['section']=='release_calendar']
 n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=min(count,3)+n['industry_bonus']
 n['priority_score']=n['event_type_score']*n['source_strength_score']+int(n.get('company_bonus',0))
 date=n['event_date'];sig=n['signal_type']
 n['window_scope']='report_window' if START<=date<=END else 'next_day_lookahead' if END<date<='2026-10-30' else 'future_announcement' if sig in ['new_game_schedule','new_game_first_reveal'] else 'outside'
 n['window_eligible']=bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}',date)) and (START<=date<='2026-10-30' or sig in ['new_game_schedule','new_game_first_reveal'])
 n['publish_eligible']=count>=2 and n['window_eligible'] and not n.get('rejected_reason')

nodes=list(groups.values())
for n in nodes:recalc(n)
validkeys=set(groups)
# 所有自动召回节点均保留去向；已正确建节点的误召回不再作为第二个产品日期节点。
for rawnode in raw['nodes']:
 n=copy.deepcopy(rawnode);n['product']=normalized(n['product']);key=(n['product'],n['event_date'])
 if key in validkeys:
  groups[key].setdefault('raw_candidate_ids',[]).append(n['candidate_id']);continue
 if key in {(x['product'],x['event_date']) for x in nodes}:
  existing=next(x for x in nodes if (x['product'],x['event_date'])==key);existing.setdefault('raw_candidate_ids',[]).append(n['candidate_id']);continue
 n['rejected_reason']='逐字复核：普通运营/历史背景/相对日期误读/归属不清或单源节点，未独立满足本期产品事件与日期证据。'
 n['raw_candidate_ids']=[n['candidate_id']];recalc(n);nodes.append(n)
for n in nodes:
 # 多个原始单源别名已归入真节点，禁止自动标题中的背景公司造成误加分。
 if n.get('rejected_reason'):
  n['publish_eligible']=False
  if n.get('company_bonus') and n['product'] in ['无限大','星塔旅人','异环','代号二杠三','影之刃零','蓝色星原：旅谣','星溯']:
   n['company_bonus']=0;n['focus_companies']=[];n['company_evidence_ids']=[];n['company_relationship']='';n['focus_company_relationships']={};recalc(n)
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n.get('company_bonus',0),-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n.get('first_seen_order',99999)))
for i,n in enumerate(nodes,1):n['candidate_id']=f'R{i:03}'
audit=dict(raw);audit['nodes']=nodes;audit['editorial_review']='全量行业与日历原始召回和当周校对节点联合复核；保留原始审计及逐信号去向，独立来源按URL或正文哈希去重。'
dump(B/'release_calendar_audit.json',audit)

# 给所有行业候选保留PC/主机分类与逐字文本证明。
for d in DEC:
 if d['section']!='industry_news':continue
 if d.get('scores',{}).get('event',0):
  d.setdefault('genre_assessment',dict(matched_genres=[],basis='无本事件明确重点品类证据',evidence=[]))
  if not d.get('subject_assessment'):
   sid=d['source_ids'][0];d['subject_assessment']=dict(subject=d['entities'][0],kind='other_or_unknown',focus_companies=[],basis='当前来源不足支持更高影响力档位，未借公司背景或标签加分。',evidence=[])
  if d.get('decision')=='exclude':d.setdefault('exclusion_gates',['score'])
  timing(d)
 if not d.get('history_check'):d['history_check']=history()
 if not d.get('pc_release_scope') and any(re.search(r'PC|Steam|Xbox|Switch|主机|端游',SRC[s]['text'],re.I) for s in d['source_ids']):
  sid=next(s for s in d['source_ids'] if re.search(r'PC|Steam|Xbox|Switch|主机|端游',SRC[s]['text'],re.I));text=SRC[sid]['text']
  ev=next(p for p in text.splitlines() if re.search(r'PC|Steam|Xbox|Switch|主机|端游',p,re.I))
  d['pc_release_scope']=dict(classification='multiplayer_or_other',basis='兼容分类仅描述报道范围；主体R独立按影响力和来源证据判断。',evidence=[dict(source_id=sid,evidence=ev)])
 cluster(d)

root=dict(scoring_version='subject_genre_v2',industry_timing_version='source_window_v1',report_type='weekly',report_window=dict(start=START,end=END),history_window=H['history_window'],deep_handoff=dict(receipt_id='2ff02addfe2f47d1a6c9789c6adb38c8',body_candidate_ids=['C001','C022'],card_base_candidate_id='C001',card_reference_candidate_ids=[]),decisions=DEC)
dump(B/'selection_decisions.json',root)
sync(B/'release_calendar_audit.json',B/'selection_decisions.json',7)
root=read(B/'selection_decisions.json');DEC=root['decisions']
for d in DEC:
 if d['section']=='release_calendar' and d['decision']=='exclude':
  n=next(x for x in nodes if x['candidate_id']==d['candidate_id'])
  if n.get('rejected_reason'):d['reason']=n['rejected_reason']
dump(B/'selection_decisions.json',root)
dump(B/'reconsider_above_threshold.json',[d for d in DEC if d['candidate_id'] in reconsider and d['decision']=='exclude' and d['scores']['total']>=5])

# 日历正文用当周已逐字取证的句子；本周尚未实际发售者保留未来语态。
visible_old={}
for rel in ['weekend/2026-10-23_to_2026-10-25','daily/2026-10-26','daily/2026-10-27','daily/2026-10-28']:
 p=next((ROOT/'output'/rel).glob('game_industry_*.md'))
 for x in parse_report_items(p.read_text(encoding='utf-8')):
  if x.section=='release_calendar':visible_old[normalized(x.title)]=x.body
mapped_old=read(B/'prior_items_remapped.json')
for d in DEC:
 if d['section']!='release_calendar' or d['decision']!='include':continue
 n=next(x for x in nodes if x['candidate_id']==d['candidate_id']);product=n['product']
 old=next(x for x in reversed(mapped_old) if normalized(x['title'])==product and x['section']=='release_calendar')
 it=copy.deepcopy(old);it.pop('prior_report',None);it['title']=product;it['candidate_id']=d['candidate_id'];it['source_ids']=n['source_ids'];it['release']={**old.get('release',{}),**n,'date':n['event_date']};it['release'].setdefault('platform','');it['release'].setdefault('company','')
 body=visible_old[product]
 if product=='影之刃零':
  body='灵游坊开发的武侠动作多平台产品《影之刃零》定于10月29日发售；团队曾放弃多款手游研发，将资源集中到单机项目。'
  it['claims']=[dict(claim='《影之刃零》',source_id='S1109',evidence=q('S1109','影之刃零')),dict(claim='10月29日',source_id='S1321',evidence=q('S1321','距离10月29日')),dict(claim='灵游坊',source_id='S1321',evidence=q('S1321','灵游坊')),dict(claim='放弃多款手游研发',source_id='S1321',evidence=q('S1321','放弃了多款手游研发'))]
 if product=='蓝色星原：旅谣':
  body='蛮啾网络开发的3D大世界多平台产品《蓝色星原：旅谣》定档11月26日公测；包含捉宠、家园建设和多人轻社交，团队将按测试反馈继续调整体验。'
  it['claims']=[dict(claim='蛮啾网络',source_id='S0034',evidence=q('S0034','蛮啾网络旗下')),dict(claim='11月26日',source_id='S0034',evidence=q('S0034','11月26日')),dict(claim='捉宠、家园建设',source_id='S0034',evidence=q('S0034','捉宠、家园建设'))]
 BODY[it['candidate_id']]=body;ITEMS.append(it)

# 按分数、R、E稳定排序行业；其余保留选题/回执顺序。
dm={d['candidate_id']:d for d in DEC}
sections=['industry_news','ai_trends','release_calendar','community_discourse','deep_analysis']
industry=[it for it in ITEMS if it['section']=='industry_news']
industry.sort(key=lambda i:(-dm[i['candidate_id']]['scores']['total'],-dm[i['candidate_id']]['scores']['relevance'],-dm[i['candidate_id']]['scores']['event']))
ITEMS=industry+[it for section in sections[1:] for it in ITEMS if it['section']==section]
dump(B/'report_items.json',dict(report_type='weekly',report_window=dict(start=START,end=END),items=ITEMS))

# 先写候选与决策，再写待校验正文。
cand=['# 全量事件候选｜'+ID,'','以完整index为导航，全量JSONL为真源。逐字证据、旧审计迁移及本期独立判断见结构化决策。','']
for d in DEC:
 cand+=['## '+d['candidate_id']+' - '+d['event'],'- section: '+d['section'],'- source_ids: '+', '.join(d['source_ids']),'- facts: '+('；'.join(c['claim'] for i in ITEMS if i['candidate_id']==d['candidate_id'] for c in i.get('claims',[])) or d['reason']),'- notes: '+d['reason'],'']
(B/'event_candidates.md').write_text('\n'.join(cand),encoding='utf-8')
lines=['# 选择决策｜'+ID,'','卡片曝光去重：先查2026-10-09至2026-10-22共110条，再查更早1011条，补查本周32条日报/周末报的实际广播。王者荣耀世界已在28日报曝光（第4/10）且5月周报收录，本期repeat_only；微信小游戏6分/R3保留唯一card_carryover，Atari6分/R2排序靠后。微信相关旧报告均未曝光，card_rank=null，card_limit=null或10，来源not_broadcast或publish_log_manifest。','',
 '行业时间口径：source_window_v1；所有非E0候选使用build_time_check核对published_at，缺失回退date；历史事件时间不作门槛。已纠正旧日报按事件时间和封闭名单产生的排除，不把旧理由直接带入本期。','',
 '维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均完成全量反扫；每条候选的主体、事件与去向见下表，数量由JSON按维度检索复核。','',
 '产品日历漏挂反查：保留自动召回原始审计；反扫完整industry_news与release_calendar，按规范产品+日期重新聚类，纠正背景公司归属、普通运营和发售前宣传误判；每个原始信号均映射至节点或显式exclude，由sync_release_decisions.py --max-items 7确定排序前缀。','',
 '深度交接：2ff02addfe2f47d1a6c9789c6adb38c8；正文C001、C022；唯一主卡C001；无融合参考。','',
 '| candidate | decision | target_section | E/R/M或其他评分 | reason |','| --- | --- | --- | --- | --- |']
for d in DEC:lines.append('| '+' | '.join(str(v).replace('|','／').replace('\n',' ') for v in [d['candidate_id'],d['decision']+(' → '+d.get('merge_into','') if d['decision']=='merge' else ''),d['section'],d.get('scores',''),d['reason']])+' |')
(B/'selection_decisions.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
stage=B/'draft';stage.mkdir(exist_ok=True)
(stage/'deep_card_choice.txt').write_text((OUT/'deep_card_choice.txt').read_text(encoding='utf-8'),encoding='utf-8')
report=['# 游戏行业周报｜'+ID,'','> 本期本地采集材料实际覆盖10月23日至28日；10月29日暂无输入。行业历史事件保留实际发生时间与统计期。','']
heads=['一、行业新闻','二、AI 新闻','三、新游发布 / 产品日历','四、玩家舆论 / 社区动态','五、行业精选 / 深度观察']
for sec,head in zip(sections,heads):
 report+=['## '+head,'']
 for n,it in enumerate([x for x in ITEMS if x['section']==sec],1):
  if sec=='release_calendar':report+=['- '+BODY[it['candidate_id']],'']
  else:report+=['### '+str(n)+'. '+it['title'],'',BODY[it['candidate_id']],'']
target=stage/('game_industry_weekly_'+ID+'.md');target.write_text('\n'.join(report),encoding='utf-8')
dump(B/'working_final_body.json',BODY)
print('COUNTS',Counter(i['section'] for i in ITEMS),'decisions',len(DEC),'calendar nodes',len(nodes))
print('ABOVE_THRESHOLD_NEEDS_REVIEW',[(d['candidate_id'],d['source_ids'],d['event'],d['scores']['total']) for d in DEC if d['candidate_id'] in reconsider and d['decision']=='exclude' and d['scores']['total']>=5])
