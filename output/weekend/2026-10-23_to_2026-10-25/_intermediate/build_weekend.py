import json,re,hashlib,sys,copy
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
H=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
def save(name,data): (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sid(i):return f'S{i:04}' if isinstance(i,int) else i
def ev(i,q):
 t=S[sid(i)]['text'];assert q in t,(i,q)
 return dict(source_id=sid(i),evidence=next(l for l in t.splitlines() if q in l))
D=[];DM={}
def decision(cid,section,ids,event,reason,include=False):
 d=dict(candidate_id=cid,section=section,source_ids=[sid(i) for i in ids],entities=[event],event=event,decision='include' if include else 'exclude',reason=reason)
 D.append(d);DM[cid]=d;return d
def ind(i,e=0,r=0,m=0,reason='',subject=None,kind='other_or_unknown',focus=None,q=None,gq=None,ids=None):
 d=decision(f'I{i:03}','industry_news',ids or [i],S[sid(i)]['title'],reason or '普通运营/宣传、评论、硬件或非游戏；没有当期独立状态事件，E0。')
 d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m)
 d['history_check']=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None)
 if e:
  d['subject_assessment']=dict(subject=subject or S[sid(i)]['title'],kind=kind,focus_companies=focus or [],basis=reason or '本候选正文没有证明统一名单或投资/合研/核心人才创业关系，也不凭国产/手游/品类标签加R。',evidence=[ev(i,q)] if q else [])
  d['genre_assessment']=dict(matched_genres=['competitive'] if m else [],basis='本事件有竞技品类原文。' if m else '一般动作、合作、卡牌、经营或公司组织事件均不能证明指定品类，本事件M0。',evidence=[ev(i,gq)] if gq else [])
  if kind=='representative_subject':d['subject_assessment']['representative_product']=subject
 if e and re.search(r'发售|首曝|测试|launch|release|reveal|development',S[sid(i)]['title'],re.I) and re.search(r'PC|PS5|Xbox|Steam|主机',S[sid(i)]['text'],re.I):
  d['pc_release_scope']=dict(classification='domestic_or_focus' if r==3 else 'multiplayer_or_other' if re.search('多人|合作|co-op',S[sid(i)]['text'],re.I) else 'unknown',basis='仅记录平台范围；主体R不受国产、PC/主机或品类自动加分。',evidence=[ev(i,S[sid(i)]['text'].splitlines()[0])])
 return d

# Routine and older translated articles remain individually traceable. Event-bearing
# titles receive a separate non-E0 assessment even when source/subject gates exclude.
events={
 1:(2,0,0,'账户泄露事件但32字不能证明主体档位及影响；完整来源263另审。'),
 6:(3,0,0,'新品发售，主体取证不足且48字，R0。'),
 8:(2,0,0,'12月9日离线模式计划，名单关系及代表作声量未在本源证实。'),
 9:(3,0,0,'商城页公开信号，主体重要性未证实。'),
 16:(2,0,0,'10月27日定档，单源且主体未证实；日历独立审查。'),
 19:(2,0,0,'被取消项目素材泄露，不能当作在研新品；短文缺主体证据。'),
 24:(3,0,0,'国产合作丧尸新作发售，国产和合作都不自动抬R/M。'),
 28:(0,3,0,'10月21日退出医疗脑机企业股权，非游戏业务且事件早于本窗口。'),
 30:(0,3,0,'仿生机器人公司10月16日注册；未证实游戏产品落地且不在窗口。'),
 32:(2,0,0,'板块行情评论，不是直接证明相对指引/预期的异常财务事件。'),
 33:(1,0,0,'开发者既有游戏收入分账复盘，非当期融资或流动性变化。'),
 34:(2,1,0,'蛮啾旗下产品定档并有碧蓝航线积累和2500万预约声量，R1；不由平台/背景抬R3。'),
 37:(2,0,0,'多个老品回归复盘：9月众筹/9月2日重启不在窗口，日历分产品审查。'),
 39:(3,3,0,'吉比特业绩说明会披露代号M98已正式立项并确定制作人；单独产品立项E3，常规财报不作为入选依据。'),
 91:(1,3,1,'Supercell产品电竞落地复盘，比赛实际10月17—18日，且E1R3M1=4，不作为本期新赛事。'),
 109:(2,3,0,'抖音小游戏白皮书正文为昨（7）日，绝非本窗口；保留候选并按日期门禁排除。'),
 141:(3,0,0,'Side收购Roboto公告明确10月21日，早于窗口；不由客户提及抬重点关系。'),
 156:(2,1,0,'Steam新品节市场评论，PC市场R1；只有平台/市场信息，不是重点移动主体。'),
 255:(3,0,1,'篮球少女23日公测，本期来源没有发行商灵犀归属，不借历史常识抬R；日历独立可选。'),
 258:(3,0,0,'南棠羽星溯首曝；哔哩哔哩是播放平台而不是发行归属，R0。'),
 261:(1,0,0,'Landfall访谈复盘Peak成绩和工作室流程，不是本期新资本状态。'),
 263:(2,1,0,'Capcom账户安全事件，来源列明代表作及1170万账户规模；名单外主体R1，未达线。'),
 265:(2,0,0,'GameMaker商用许可变化，不在重点名单，本源没有代表作声量证据；R0。'),
 268:(2,0,0,'GameMaker许可变化短摘要，无完整原文，不能发表。'),
 269:(2,1,0,'Dispatch移动移植定档，AdHoc代表作超过500万玩家但只有摘要；R1，不能当期上线。'),
 270:(3,0,0,'Stillfront更换CEO但仅摘要，未证实名单关系或代表作声量，R0。'),
 276:(3,0,0,'Stillfront换CEO的单段短文，未证实主体R1/2/3证据。'),
 280:(1,3,0,'网易率土11周年生命周期节点及运营复盘，E1R3=3。'),
 281:(1,3,0,'网易率土生命周期与周年活动复盘，E1R3=3；与280仅同一运营主题，不拆多条。'),
 284:(2,1,0,'Dispatch移动版12月9日推出，老品跨平台未在本期实际发生，R1未达线。'),
 287:(3,1,0,'EA可能出售BioWare IP为前负责人预测，非已发生资本状态；R1总分3。'),
 288:(2,0,0,'开发成本报道，非相对指引的异常财务状态。'),
 298:(2,1,0,'EA关停BioWare解读；代表作Mass Effect在正文，R1总分2。'),
 299:(3,1,0,'Xbox影视合作报价谈判复盘，没有签约；PC/主机业务R1，3分。'),
 301:(2,0,0,'Arkane可能关停报道，非确认关闭且缺重点主体关系取证。'),
 304:(2,0,0,'质量效应被取消项目预告泄露，不视作新品发布；R0本源。'),
 305:(1,0,0,'EA裁员，纯劳资E1，缺代表产品声量证明。'),
 315:(3,0,0,'发售宣传片不保证当日发售，需日期复核；主体R0。'),
 316:(2,0,0,'Switch2跨平台发售宣传片，仅一个来源，没有绝对发售日。'),
 320:(1,0,0,'Dispatch周年内容，老品节点非新作上线。'),
 322:(2,0,0,'10月8日发售后的成绩消息，未证实主体档位。'),
 334:(1,0,0,'Splash Damage关联团队裁员，未见新收购或工作室关闭状态。'),
 339:(1,0,0,'Valve开发者口误线索，不是正式首曝/立项公开。'),
 360:(3,3,0,'腾讯光子人间异想计划首曝同事件已在21日报及周报曝光；换来源不增加状态。'),
 361:(1,1,0,'卧龙2设计访谈，前作百万销量有证据但不是当期首曝/首测。'),
 464:(2,0,0,'综合新闻逐项拆分：光子旧首曝、21日伽马报告、影刃22日预告均非本窗口新事件；蓝原23日定档独立日历。'),
 475:(0,0,0,'Exodus主角形象常规调整；产品例行宣传。'),
 486:(1,0,0,'Factorio最终大更新，未证实重点主体，E1。'),
 490:(2,1,0,'Steam cozy标签增加的PC市场观察，R1=2；不把标签增长当移动市场。'),
 491:(1,0,0,'日本演员工会AI意见，缺具体游戏落地；不入AI直接作用。'),
 524:(1,1,0,'诗悦望月UE岗位与引擎描述变化；来源有代表作品但未正式确认整体迁移，E1R1=1。'),
 525:(0,3,0,'吉比特常规Q3业绩变化，无显著偏离指引或流动性异常，财报例外不成立。'),
 527:(1,0,0,'法务周综，普通个案诉讼与退款，无重点主体资本或政策变化。'),
 528:(3,2,0,'米哈游投资的奥秘游戏首曝潜梦者；投资关系R2而非R3，多人合作搜躲撤不等于竞技。'),
 529:(2,3,1,'天美王者IP三产品同时包揽iOS免费榜前三，属于同IP产品矩阵结构变化E2，MOBA产品M1；不把常规周年活动抬E。'),
 588:(1,3,1,'荒野乱斗LCQ赛事复盘，17—18日旧事件，E1总分4并日期排除。'),
 589:(1,3,0,'巨人征途21周年生命周期运营复盘，E1R3=3。'),
 596:(3,1,0,'Xbox高管上任3个月离职，名单外互联网游戏业务R1，3分。')}

focus={39:('吉比特','focus_subject',['吉比特'],'吉比特在业绩会上重点提到四款将上线产品'),91:('Supercell','focus_subject',['Supercell'],'Supercell电竞负责人'),109:('抖音小游戏','major_internet_gaming',[],'抖音发布了'),280:('网易','focus_subject',['网易'],'网易'),281:('网易','focus_subject',['网易'],'网易'),360:('腾讯光子','focus_subject',['腾讯'],'腾讯光子'),528:('奥秘游戏','focus_affiliate',['米哈游'],'不仅获得了米哈游投资'),529:('腾讯天美','focus_subject',['腾讯'],'天美公布了'),588:('Supercell','focus_subject',['Supercell'],'Supercell'),589:('巨人网络','focus_subject',['巨人网络'],'巨人')}
reps={34:('蛮啾/蓝色星原','2500万'),156:('PC/Steam市场','Steam'),263:('Capcom / Street Fighter 6','11.7 million'),269:('AdHoc / Dispatch','five million'),284:('AdHoc / Dispatch','biggest'),287:('EA / BioWare','Mass Effect'),298:('EA / BioWare','Mass Effect'),299:('Xbox游戏业务','Xbox'),361:('光荣特库摩/卧龙','百万份'),490:('PC/Steam市场','Steam'),524:('诗悦/望月','600+'),596:('Xbox游戏业务','Xbox')}
ai_ids={18,27,31,35,36,38,41,53,54,55,56,69,70,71,72,76,77,78,79,98,99,100,101,108,157,158,159,160,244,245,246,247,341,453,461,488,526,532,533,534,535,582,583,584}
for k,x in S.items():
 i=int(k[1:])
 if x['section']!='industry_news':continue
 if i in ai_ids:
  d=decision(f'A{i:03}','ai_trends',[i],x['title'],'反扫AI候选：优先本期具体生产实践和可核验调整；旧稿/复盘、短摘要、日期不明或与本期已选研究重复的候选不选。')
  d.update(ai_tier='direct_application',game_stage=['development'],industry_reverse_scan=True)
  continue
 e,r,m,reason=events.get(i,(0,0,0,''))
 # Older multilingual archives have event-bearing titles; retain their event
 # classification and fail the date/evidence gate rather than pretending E0.
 if i not in events and x['source_key']=='youxichaguan' and re.search(r'financi|Finanzier|투자|融资|acquis|收购|encerr|Einstellung|종료|lança|lanz|veröffent|출시|游戏市场|游戏行业',x['title'],re.I):
  e=3 if re.search(r'financi|Finanzier|투자|融资|acquis|收购|lança|lanz|veröffent|출시',x['title'],re.I) else 2
  reason='多语种归档转载候选；正文历史/跨月语境，没有可核验的10月23—25日新状态；主体关系不借背景公司猜测，R0。'
 kwargs={}
 if i in focus:
  sub,kind,fc,q=focus[i];kwargs=dict(subject=sub,kind=kind,focus=fc,q=q)
  if q not in x['text']:r=0;kwargs={};reason+=' 本源未出现主体归属原文，R降至0，不由产品常识补主体。'
 if i in reps:
  sub,q=reps[i];kwargs=dict(subject=sub,kind='pc_console_market' if i in [156,490] else 'representative_subject',q=q)
 d=ind(i,e,r,m,reason,**kwargs,gq={91:'全球锦标赛',255:'篮球',529:'MOBA',588:'电竞'}.get(i))
 if i in [39,528,529]:d['decision']='include'
 if i in [360]:
  occ=[o for o in H['occurrences'] if '人间异想计划' in o['title']]
  d['history_check']=dict(history_match=True,novelty='repeat_only',prior_occurrences=[o['title']+' | '+o['report_window']['start']+'_to_'+o['report_window']['end'] for o in occ],new_facts=[],prior_card_exposed=any(o['card_exposed'] for o in occ))

# Other original pools are all retained in the decision audit, including rejected
# community speculation and general technology stories with no concrete game use.
for k,x in S.items():
 i=int(k[1:])
 if x['section']=='ai_trends':
  d=decision(f'T{i:03}','ai_trends',[i],x['title'],'泛AI、模型例行参数、医疗/硬件/资本或安全通告；无本条来源直接支持的具体游戏落地/独立迁移链，不以AI标签入选。')
  d.update(ai_tier='transferable_frontier',game_stage=['development'],industry_reverse_scan=False,migration_path='未确立本事件向具体游戏流程的独立迁移证据，因此排除。')
 if x['section']=='community_discourse':
  d=decision(f'C{i:03}','community_discourse',[i],x['title'],'非独立争议、证据薄弱、重复旧帖或相较本期两条事件信息价值较低；不将玩家推测升级为官方事实。')
  d['community']=dict(trigger=x['title'],claim_scope='玩家帖与采集摘录',complaint_logic='仅按原帖归因；未证实的动机不作为事实。',timeline=[x['date']],follow_up_scan='已扫描同窗口行业与44条社区记录，保留日期和归因限制。')
 if x['section']=='deep_analysis':decision(f'D{i:03}','deep_analysis',[i],x['title'],'完整配置newsletter，单一分析可用。',True)
DM['I091']['source_ids'].append('S0588')
DM['I091']['subject_assessment']['evidence']=[ev(588,'Supercell')]
DM['I091']['cluster_basis']=dict(subject='Supercell荒野乱斗',product='荒野乱斗',event_date='2026-10-17',event='同一17—18日LCQ赛事复盘')
DM['I588'].update(decision='merge',merge_into='I091',reason='同一主体、同一17—18日赛事，合并复盘；均非本窗口发生。')
DM['I255']['history_check']=dict(history_match=True,novelty='material_update',prior_occurrences=[o['title']+' | '+o['report_window']['start']+'_to_'+o['report_window']['end'] for o in H['occurrences'] if '篮球少女' in o['title']],new_facts=['本期正文明确10月23日已公测，较历史预告实际进入上线状态。'],prior_card_exposed=True)
DM['I316']['pc_release_scope']=dict(classification='substantive_migration',basis='标题明确Switch2版本跨平台发售信号，当前单源未证明具体实际日；主体分层独立R0。',evidence=[ev(316,'Switch')])
# An omnibus is a container, never one bundled industry event.
DM['I464']['scores']=dict(event=0,relevance=0,hook=0,total=0)
DM['I464']['reason']='综合稿容器不作为独立事件；光子/伽马/影刃/未成年人认定分别建卡，蓝原进独立日历。'
for suffix,title,quote,e,r,kind,focus in [
 ('human','光子人间异想计划21日首曝','10月21日，光子工作室群',3,3,'focus_subject',['腾讯']),
 ('gamma','伽马21日发布Q3中国移动市场数据','中国移动游戏市场实际销售收入为678.20亿元',2,3,'priority_mobile_market',[]),
 ('shadow','影之刃22日最终预告与预载安排','10月22日，灵游坊',0,0,'other_or_unknown',[]),
 ('minor','网信办19日启动未成年人平台认定','10月19日，国家网信办',2,0,'other_or_unknown',[])]:
  # Exact article lines are selected by a stable distinctive substring.
  if quote not in S['S0464']['text']:quote={'human':'腾讯光子工作室群','gamma':'中国移动游戏市场实际销售收入','shadow':'最终预告','minor':'国家网信办'}[suffix]
  d=decision('I464-'+suffix,'industry_news',[464],title,'事件原始日期早于23日，不将本期周综转载当新状态。')
  d['scores']=dict(event=e,relevance=r,hook=0,total=e*r)
  d['history_check']=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None)
  if e:
   d['subject_assessment']=dict(subject='腾讯光子' if suffix=='human' else '中国移动游戏市场' if suffix=='gamma' else title,kind=kind,focus_companies=focus,basis='以原文实际主体和原始事件日审查，日期门禁独立于分数。',evidence=[ev(464,quote)])
   d['genre_assessment']=dict(matched_genres=[],basis='宏观/政策或普通开放世界RPG，不由集团其他产品借品类分。',evidence=[])
  if suffix=='human':d['history_check']=copy.deepcopy(DM['I360']['history_check'])
DM['A488']['decision']='include';DM['A488']['reason']='开发者已将游戏内AI语音替换为真人录音，有明确动作、原因与退款后续。'
DM['T494'].update(decision='include',ai_tier='direct_application',game_stage=['development'],migration_path='',reason='官方全文展示游戏引擎和3D资产创作能力；只写发布方已展示的应用及权重未发布状态，不泛化为实测生产收益。')
decision('A039','ai_trends',[36],'吉比特在Demo阶段使用AI扩大玩法原型探索','业绩会已披露真实美术、代码、策划使用环节；与M98立项属于不同独立事件。',True).update(ai_tier='direct_application',game_stage=['development'],industry_reverse_scan=True)
for i in [428,616]:DM[f'C{i:03}']['decision']='include';DM[f'C{i:03}']['reason']='触发与争议逻辑清楚，并有窗口内补充或双方态度；严格玩家归因。'
DM['C428']['source_ids'].append('S0609');DM['C609'].update(decision='merge',merge_into='C428',reason='同一10月23日奖励对比帖子续采，合并回复中的补发公告指认。')
DM['C428']['community'].update(trigger='玩家对比鸣潮前瞻与签到发放，称少5个体力药',complaint_logic='承诺落差与发帖是否忽略既有补发说明的争论',timeline=['10月23日建帖','窗口内回复指认21日已有补发公告'],follow_up_scan='扫描428、609及全社区池，补发属于帖内玩家指认；没有冒充官方公告原文。')
DM['C616']['community'].update(trigger='惊喜渡鸦收藏品随机升级/复制活动',complaint_logic='随机收益差距与原有稀有品劳动价值的冲突，亦有愿赌服输意见',timeline=['10月25日建帖，正文只采用25日摘录'],follow_up_scan='同窗口行业及社区池未发现同事件调整来源，正文不写无官方回应尾注。')

# Correct the extractor's event/ownership false positives using read source text.
a=json.loads((P/'release_calendar_audit_raw.json').read_text(encoding='utf-8'))
nodes=a['nodes'];NM={n['candidate_id']:n for n in nodes}
def node(num):return NM[f'release-candidate-{num:03}']
def reject(num,reason):n=node(num);n.update(publish_eligible=False,editorial_exclusion_reason=reason)
def recalc(n):
 ids=n['source_ids'];fp={S[i]['url'] for i in ids};bodies={hashlib.sha1(S[i]['text'].encode()).hexdigest() for i in ids}
 count=min(len(fp),len(bodies));indids=[i for i in ids if S[i]['section']=='industry_news'];relids=[i for i in ids if S[i]['section']=='release_calendar']
 n.update(appearance_count=count,appearance_score=min(count,3),industry_ids=indids,release_ids=relids,industry_bonus=int(bool(indids)),source_strength_score=min(count,3)+int(bool(indids)),source_fingerprints=list(fp),coverage='industry+release' if indids and relids else 'industry_only' if indids else 'release_only',coverage_rank=3 if indids and relids else 2 if indids else 1)
 n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus'];n['multi_source_eligible']=count>=2
 n['publish_eligible']=bool(count>=2 and n.get('window_eligible') and not n.get('editorial_exclusion_reason'))
for num in [1,9,11,12,14,17,19,20,24,27,48,49]:reject(num,'普通更新/宣传片/周年/影视事件被误识别为新品实际上线或跨平台；不是当前有效日历节点。')
for num in [4,13,18,47]:reject(num,'正文明确为此前历史事件，实际日期不在本期产品事件窗口。')
reject(6,'影之刃最终预告为22日，且预下载27日超过26日及时性窗，不重复当成首次曝光。')
reject(7,'蓝原定档发生23日；25日只作背景提及，归并23日节点。')
reject(8,'无限大是背景旧定档，不是25日新增定档。')
reject(22,'产品简称与同日正式名节点002归并，不独立进入正文。')
reject(40,'魂like标签规范化为星溯，证据合并005，不另成产品。')
reject(43,'3839标23日首曝，25日采访说昨天首曝，日差未解；保留两条事实而不强行做同日多源。')
node(2)['source_ids']=['S0034','S0283','S0464','S0409'];node(2)['focus_companies']=[];node(2)['company_bonus']=0;node(2)['company_relationship']='none'
node(5).update(source_ids=['S0258','S0396'],focus_companies=[],focus_company_relationships={},company_evidence_ids=[],company_relationship='none',company_bonus=0)
node(33)['source_ids']=['S0255','S0417']
node(3).update(signal_type='new_game_schedule',event='韩国与东南亚发行定档11月4日',event_type_score=2,editorial_exclusion_reason='单源定档，非10月23日正式上线；不可因大陆旧版上线或财报词句误选。')
node(23).update(editorial_exclusion_reason='11月/12月测试及明年3月发售只有月份，且9月底公布回归；不以本期复盘重置定档日。')
node(46).update(editorial_exclusion_reason='9月众筹旧回归公告，明年春季仍无本期新定档。')
# Additional whole-body recall: every bound product in the business-call pipeline.
def extra(product,ids,event,typ,date='2026-10-23',reason=''):
 n=copy.deepcopy(node(5));n.update(product=product,candidate_id=f'release-extra-{len(nodes)+1:03}',source_ids=[sid(i) for i in ids],event=event,signal_type=typ,event_date=date,event_type_score=2,first_seen_order=1000+len(nodes),focus_companies=[],focus_company_relationships={},company_evidence_ids=[],company_relationship='none',company_bonus=0,observed_signal_types=[typ],observed_events=[event],editorial_exclusion_reason=reason);nodes.append(n);return n
for prod,event in [('问剑长生','计划2026年第四季度进入欧美'),('甄嬛传','计划2027年第一季度前于大陆上线'),('大圣牌：凌霄斗神','计划2027年第一季度前于大陆上线'),('代号M98','正式立项并确定制作人')]:extra(prod,[39],event,'new_game_first_reveal' if prod=='代号M98' else 'new_game_schedule',reason='单源，且产品细节/具体发行日不足；留审计不入正文。')
extra('潜梦者',[528],'采访报道新作首曝','new_game_first_reveal','2026-10-24','采访昨日指24日、3839标23日，不能强行合并同日多源。')
extra('Dispatch',[269,284],'12月9日移动跨平台上线','old_cross_platform_launch','2026-12-09','老品跨平台实际发生日在12月，不能按新品定档特例越过产品事件窗口。')
for n in nodes:
 recalc(n)
 n['window_scope']='report_window' if '2026-10-23'<=n['event_date']<='2026-10-25' else 'next_day_lookahead' if n['event_date']=='2026-10-26' else 'outside'
 if n['window_scope']=='outside' and n['signal_type'] in ['new_game_schedule','new_game_first_reveal']:n['window_scope']='future_announcement'
 # Every calendar use must have full source text; unavailable details do not count.
 if any(S[i]['body_status']!='full' for i in n['source_ids']):n['publish_eligible']=False;n['editorial_exclusion_reason']='包含不可读取完整正文来源，证据质量不达本期发布门槛。'
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-int(bool(n['industry_ids'])),n['first_seen_order']))
a['nodes']=nodes;a['editorial_reverse_scan']='全量industry_news与release_calendar按句反扫，历史语境、相关阅读和无主语绑定语句不得冒充当前新事件；补录业绩会4项管线与跨平台/首曝日期分歧。'
covered={si for d in D for si in d['source_ids']}|{si for n in nodes for si in n['source_ids']}
for si in S.keys()-covered:
 i=int(si[1:]);ind(i,reason='全量原始日历反查：普通活动、版本、重复宣传或没有可明确绑定的新产品事件；E0排除，来源仍留审计。')
save('release_calendar_audit.json',a)
save('selection_decisions.json',dict(scoring_version='subject_genre_v2',report_type='weekend',report_window=dict(start='2026-10-23',end='2026-10-25'),decisions=D))

# Whole-file machine review keeps paragraph date signals and hashes for every ID.
review=[]
for k,x in S.items():
 t=x['text'];assert t.strip();review.append(dict(source_id=k,section=x['section'],title=x['title'],text_chars=len(t),sha256=hashlib.sha256(t.encode()).hexdigest(),body_status=x['body_status'],paragraphs=len(t.splitlines()),date_evidence=[l for l in t.splitlines() if re.search(r'202[4567]|\d{1,2}月\d{1,2}|October|November|March|January',l)],decisions=[d['candidate_id'] for d in D if k in d['source_ids']],calendar_signal_lines=[l for l in re.split('相关推荐|相关阅读|延伸阅读|猜你喜欢|更多推荐',t)[0].splitlines() if re.search('首曝|正式立项|定档|预下载|开启.{0,8}测试|将于.{0,30}上线',l)]))
save('full_input_review.json',review)
save('history_exposure_review.json',[{k:o[k] for k in ['title','event','entities','claims','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for o in H['occurrences']])
print('decisions',len(D),'calendar',len(nodes),'input',len(S))
