import json, re, hashlib, copy, sys
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
H=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
def save(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sid(i): return f'S{i:04}' if isinstance(i,int) else i
def ev(i,q):
 t=S[sid(i)]['text']; assert q in t,(i,q)
 return dict(source_id=sid(i),evidence=q)
D=[]; DM={}
def dec(cid,section,ids,event,reason,include=False):
 d=dict(candidate_id=cid,section=section,source_ids=[sid(i) for i in ids],entities=[event],event=event,decision='include' if include else 'exclude',reason=reason)
 D.append(d);DM[cid]=d;return d
def ind(i,e=0,r=0,m=0,reason='',subject=None,kind='other_or_unknown',focus=None,q=None,gq=None,cid=None,ids=None,event=None):
 d=dec(cid or f'I{i:03}', 'industry_news',ids or [i],event or S[sid(i)]['title'],reason or '普通版本、宣传、活动、评论、硬件或非游戏内容；无本期独立状态事件，E0排除。')
 d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m)
 d['history_check']=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None)
 if e:
  d['subject_assessment']=dict(subject=subject or S[sid(i)]['title'],kind=kind,focus_companies=focus or [],basis=reason or '本源未证实统一名单、关联关系或名单外代表作声量；不凭国产、手游、品类抬R。',evidence=[ev(i,q)] if q else [])
  if kind=='representative_subject':d['subject_assessment']['representative_product']=subject
  d['genre_assessment']=dict(matched_genres=['competitive'] if m else [],basis='本条独立事件明确围绕竞技品类。' if m else '本条事件未命中四类二值加分品类；不借集团其他产品加分。',evidence=[ev(i,gq)] if gq else [])
  if re.search(r'PC|PS5|Xbox|Steam|主机',S[sid(i)]['text'],re.I):
   d['pc_release_scope']=dict(classification='domestic_or_focus' if r==3 else 'unknown',basis='平台范围单独记录，主体R由正文关系证据决定；普通动作、单机、国产标签不抬分。',evidence=[ev(i,next(l for l in S[sid(i)]['text'].splitlines() if re.search(r'PC|PS5|Xbox|Steam|主机',l,re.I)))])
 return d
def hist(d,pattern,novelty='repeat_only',facts=None):
 matches=[o for o in H['occurrences'] if re.search(pattern,o['title']+' '+o['event'])]
 assert matches,pattern
 d['history_check']=dict(history_match=True,novelty=novelty,prior_occurrences=[o['title']+'｜'+o['report_window']['start']+'_to_'+o['report_window']['end'] for o in matches],new_facts=facts or [],prior_card_exposed=any(o['card_exposed'] for o in matches))
 d['history_evidence']=[{k:o[k] for k in ['title','event','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for o in matches]

# Read and retain every complete text, including multilingual mirrors, before judging.
review=[]
for k,x in S.items():
 t=x['text'];assert t.strip()
 review.append(dict(source_id=k,section=x['section'],title=x['title'],body_status=x['body_status'],text_chars=len(t),sha256=hashlib.sha256(t.encode()).hexdigest(),paragraphs=t.splitlines(),date_evidence=[l for l in t.splitlines() if re.search(r'202[4567]|\d{1,2}月\d{1,2}|March|October|November|Februar|marzo|março',l)],calendar_signal_lines=[l for l in re.split('相关推荐|相关阅读|延伸阅读|猜你喜欢|更多推荐',t)[0].splitlines() if re.search('首曝|正式立项|定档|预下载|测试|上线|发售|发行日期',l)]))
save('full_input_review.json',review)
save('history_exposure_review.json',[{k:o[k] for k in ['title','event','entities','claims','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for o in H['occurrences']])
index=(P/'report_inputs_index.md').read_text(encoding='utf-8'); assert set(re.findall(r'`(S\d{4})`',index))==set(S)

# Nonroutine candidates receive explicit subject and genre assessment, even if excluded.
spec={
3:(2,1,0,'Steam个人日历是PC平台功能，按PC/主机市场R1，未达5分。','Steam','pc_console_market',None,'针对近期发行和即将推出的游戏'),
6:(3,0,0,'Sign新品发售，厂商档位无证据；日历独立竞争。'),
8:(2,0,0,'11月24日定档，互动影游主体档位未证实；单源日历。'),
10:(3,3,0,'代号M98立项已于23—25日周末报披露；常规财报不成立异常例外。','吉比特','focus_subject',['吉比特'],'吉比特召开了财报电话会议'),
11:(1,0,0,'诗悦招聘UE主程及引擎标签变化，未确认全项目换引擎；无本源代表作声量证明，R0。'),
12:(2,1,1,'顽核社Demo30万游玩与2.6万在线提供声量；名单外代表产品R1，统计事件E2，仅3分。','我带过最差的一届','representative_subject',None,'Demo上线七天累计游玩次数突破20万次，10天突破30万', '1v5的非对称派对游戏'),
13:(2,3,1,'灵犀发行产品上线成绩复盘；10月23日公测早于窗口，纯免费/畅销位置不属结构性榜单变化，日期/类型门禁排除。','灵犀互娱','focus_subject',['灵犀互娱'],'灵犀互娱发行的《篮球少女：飞跃巅峰》','体育养成游戏'),
14:(1,3,1,'西山居MMO上线后主创访谈与经营表态E1；大型GVG为竞技M1，总分4。','西山居','focus_subject',['西山居'],'西山居偏偏端出了一款','大型GVG群战'),
15:(2,1,0,'蛮啾碧蓝航线长跑和2500万预约支持名单外代表产品R1；公测定档发生23日且日历已刊，无26日新状态。','碧蓝航线','representative_subject',None,'此前已经突破2500万的全球预约'),
16:(1,1,0,'影之刃零通关评述，来源300万愿望单证明产品声量；无新发售状态。','影之刃零','representative_subject',None,'Steam的300万愿望单'),
17:(1,1,0,'SayGames提供的发行方法访谈；200款游戏80亿下载支持R1，E1未达线。','My Perfect Hotel','representative_subject',None,'全球累计下载量超过 80 亿次'),
19:(2,1,0,'网吧行业数据属PC生态市场而非优先移动市场；E2R1=2，不借背景腾讯网易抬R。','中国网吧市场','pc_console_market',None,'中国上网服务门店'),
22:(3,0,0,'莎拉的黑店正式版10月23日上线，早于窗口；畅游是旧纠纷对象非产品归属。'),
25:(1,0,0,'奇异种子开发复盘，实际发售2025年11月5日，不是新品发布。'),
132:(3,0,0,'Sign发售；猫猫毛工坊未有重点关系或代表作声量证据，R0。'),
133:(2,1,1,'GTA6经济损失是假设及评论，不是实测损失或公司异常财务；R1，总分3。','GTA6','representative_subject',None,'全球两千多亿美元的电子娱乐产业','GTA6'),
134:(1,3,0,'原神UGC创作案例复盘，非新平台发布、政策或资本事件，E1=3。','原神','focus_subject',['米哈游'],'《原神》内置的“小游戏平台”'),
135:(2,1,0,'木木屋98%好评与65万预约案例，名单外R1，口碑/创作复盘不属当期重大状态。','木木屋','representative_subject',None,'65万预约'),
136:(3,0,0,'警目如炬Demo介绍，不能证实当日首测，也无重点关系。'),
138:(3,3,0,'雷霆游戏投资上海火因山风并持股约30%；实际新闻主体为名单内投资方游戏业务，E3R3M0=9。','雷霆游戏','focus_subject',['雷霆游戏'],'近日，雷霆游戏投资了一家叫做上海火因山风网络的公司，占股约30%。'),
139:(1,1,0,'小红书游戏制作人招聘是探索计划，尚无具体产品发布或已落地AI流程，E1R1=1。','小红书游戏业务','representative_subject',None,'为一款女性向休闲独立游戏招募制作人'),
140:(1,3,0,'畅游新天龙老品生命周期运营访谈E1R3=3；AI形象营销另拆独立AI事件。','搜狐畅游','focus_subject',['搜狐畅游'],'畅游的《新天龙八部》端游'),
142:(2,0,0,'Arkane买家协商期延长，关联重点主体未证实，代表产品声量证据不足，R0。'),
143:(3,1,0,'Xbox/Netflix授权报价谈判未签约；微软游戏业务R1，3分且上期已有相同报道。','Xbox游戏业务','representative_subject',None,'Minecraft and Diablo animated series'),
144:(3,0,0,'Undead Labs独立运营融资过程访谈；非名单关联，本源缺代表作量化声量依据。'),
145:(3,0,0,'Side收购Roboto转载，当前原文未证实名单关系或代表作声量；已在上期明确21日公告。'),
150:(3,0,0,'Xbox COO离职但仅snippet，不具正文资格。'),
151:(3,0,0,'Netflix授权报价仅snippet，不具正文资格。'),
152:(3,0,0,'Xbox潜在收购报价仅snippet，非已发生交易。'),
155:(2,3,0,'iPhone Duo游戏阵容概览只给17款中3款等一行摘要，无范围及名单，不能支持移动市场结论。','移动游戏市场','priority_mobile_market',None,'Only three of the 17 non-Arcade games'),
158:(2,0,0,'27款开测标题正文只展示29日影之刃与饼干人，按所见分别召回，不补齐未读25项。'),
160:(3,0,0,'Xbox管理层流动但仅snippet。'),
164:(2,0,0,'Game Pass手机套餐合作仅snippet，无完整条款。'),
165:(2,0,0,'Arkane寻找买家仅snippet。'),
169:(2,1,0,'BioWare21日关闭及分析师解读，非26日新的关停状态；R1，未过线。','BioWare','representative_subject',None,'制作备受喜爱的角色扮演游戏逾30年'),
170:(2,0,0,'Arkane潜在关闭不等于已关闭，代表作存在不等于声量已证，R0。'),
172:(3,1,0,'Xbox COO离职明确，但名单外游戏业务R1，总分3；上期已披露。','Xbox游戏业务','representative_subject',None,'她此前负责《我的世界》系列业务'),
173:(2,0,0,'电影成本报道，非游戏业务重大资本变化。'),
176:(2,0,0,'已取消质量效应项目素材泄露，不冒充新项目首曝。'),
180:(2,0,0,'剑星Switch2宣传片不等于当天跨平台上线，日期不足。'),
182:(2,0,0,'余烬之镇27日EA预告，R0；日历独立审查且反查已刊档期。'),
183:(2,0,0,'4:AM 12月10日定档，厂商关系不明；日历单源。'),
185:(2,0,0,'Pool of Madness11月13日定档，单源且主体R0，恐怖台球不自动体育竞技。'),
186:(2,0,0,'Wall World Strategy11月11日定档，主体R0，一般策略不自动竞技M1。'),
188:(1,3,0,'网易雷火参与魔兽无限线下预热与开发访谈，非当日新产品正式首曝或上线。','网易','focus_subject',['网易'],'网易雷火与暴雪一起'),
189:(1,2,0,'沈黎前腾讯核心岗位创业访谈，采访时间4月2日，旧采访不能冒充当前创业。','铼三实验室','focus_alumni_startup',['腾讯'],'腾讯游戏 IEG Global CTO'),
197:(1,1,0,'质量效应请愿18万签名，名单外代表产品R1；社区另建候选，不作为新关停。','质量效应','representative_subject',None,'180,000 verified signatures'),
198:(2,1,0,'SensorTower PC爆款结构研究，PC整体市场R1，E2=2，非移动市场。','PC游戏市场','pc_console_market',None,'76 breakouts between September 2025 and August 2026'),
204:(2,0,0,'影之刃零26日预下载；当前source未证实重点归属或代表作声量，R0，日历独立单源。'),
207:(2,1,0,'Steam部分账户登录异常属PC平台事件R1，2分；后续扫描无正式修复声明。','Steam市场','pc_console_market',None,'Significant numbers of users are reporting'),
211:(1,0,0,'新天龙分服运营分析，未凭此条跨源补畅游主体；非新服当天上线公告，E1。'),
212:(2,3,1,'王者三产品免费榜前三已于周末报披露；周年庆与新内容普通宣传E0另剔除。','腾讯天美','focus_subject',['腾讯'],'王者IP三款产品还一同占据iOS游戏免费榜前三','KPL王者荣耀职业联赛'),
215:(2,0,0,'29日发售及咪咕云版本宣传，未证明26日首次定档；不是实际上线。'),
}
for i in range(1,216):
 if i in [4,27,28,29,30,113,117,118,119,124,125,126,127,128,141,159,191,200]:continue
 if i in spec:
  v=list(spec[i]);v += [None]*(9-len(v)); ind(i,*v[:4],subject=v[4],kind=v[5] or 'other_or_unknown',focus=v[6],q=v[7],gq=v[8])
 elif 31<=i<=123:
  # Mirrors contain February/March launch dates, retrospective GDC material,
  # or undated recaps. Never reinterpret collection date as an event date.
  eventful=(35<=i<=42 or 47<=i<=58 or i in [61,62] or 73<=i<=80 or 93<=i<=111 or 120<=i<=123)
  d=ind(i,3 if eventful else 0,reason='多语言镜像全文已读取；正文为历史日期/回顾或缺少本期独立时间锚，采集日不能替代事件日。即使标题含重点主体也不跳过时间门禁。')
 else:ind(i)
# R1 representative field for an internet gaming business uses its actual business.
DM['I139']['subject_assessment']['representative_product']='小红书创新游戏孵化业务'
DM['I138']['decision']='include'
for ids,focus,pattern,event_score in [
 ([35,36,37,38],'腾讯',r'Tencent|텐센트',3),
 ([39,40,41,42],'网易',r'NetEase|넷이즈',3),
 ([53,54,55,56],'米哈游',r'miHoYo|Mihoyo|미하|미호',2),
 ([57,58,61,62],'腾讯',r'Tencent|텐센트',3),
 ([74,76,77,79],'三七互娱',r'37 Interactive|삼칠|三七|37',2),
 ([93,94,95,96],'腾讯',r'Tencent|텐센트',3),
 ([101,102,104,109,110],'Supercell',r'Supercell|슈퍼셀',1),
]:
 for i in ids:
  d=DM[f'I{i:03}'];lines=S[sid(i)]['text'].splitlines();proof=next((l for l in lines if re.search(pattern,l,re.I)),None)
  if not proof:continue
  e=event_score;d['scores']=dict(event=e,relevance=3,hook=0,total=e*3)
  d['subject_assessment']=dict(subject=focus,kind='focus_subject',focus_companies=[focus],basis='本源直接描述名单主体或其产品；仍独立执行时间与事件门禁，不因得分过线自动采用。',evidence=[ev(i,proof)])
  d['genre_assessment']=dict(matched_genres=[],basis='未以当前候选逐字证明指定细分品类，不借背景加分。',evidence=[])
  d['reason']='译文回顾或缺本期事件日期：正文保留原时态，不能用26日采集日期确认首次公布。35—38无绝对当期首曝日；39—42明确上月入职；53—56为GDC/1月数据；57等3月公布4月上线；74等无可确认的当期统计窗口；93等3月；101等3月周年。'
  if not d.get('pc_release_scope'):
   d['pc_release_scope']=dict(classification='unknown',basis='未凭译文标题推定平台或发售范围；主体层级与日期单独判断。',evidence=[ev(i,proof)])
# This short teaser proves neither geography nor an independently described market.
DM['I155']['scores']=dict(event=2,relevance=0,hook=0,total=0)
DM['I155']['subject_assessment'].update(kind='other_or_unknown',basis='一行导语没有可确认市场范围，不能取优先移动市场R3。')
for i in [35,42,56,61,94]:
 # These are retrospective collection mirrors, not independent current events.
 d=DM[f'I{i:03}'];d['scores'].update(event=0,total=0);d['reason']='旧产品/旧入职/旧GDC材料的多语言回顾，没有本期独立事件；按普通回顾宣传E0排除。主体原文及日期仍保留在完整审阅。'
for i in [74,76,79]:
 d=DM[f'I{i:03}'];q=next(l for l in S[sid(i)]['text'].splitlines() if 'Bilibili' in l)
 d['subject_assessment']=dict(subject='Bilibili小游戏平台',kind='focus_subject',focus_companies=['哔哩哔哩'],basis='本事件是平台小游戏消费/用户表现复盘，原文Bilibili明确；37 Interactive关系不以未配置别名替代。',evidence=[ev(i,q)])
for cid,i,q in [('I101',101,'Supercell'),('I110',110,'Supercell'),('I134',134,'米哈游的编辑器'),('I212',212,'天美18周年庆主题区')]:
 DM[cid]['subject_assessment']['evidence'].append(ev(i,q))
DM['I140']['scores'].update(event=0,total=0)
DM['I140']['reason']='同产品普通版本与运营回顾为E0；AI形象制作拆入AI栏，分服机制用于独立深度观察；不将周年活动升格新产业事件。'
hist(DM['I010'],'代号M98')
hist(DM['I212'],'王者IP|王者IP产品')
# No prior included Netflix item in exact history.
# No prior included COO item in exact history.

# Split roundup into independent subject/date/event candidates, never a mega item.
for cid,e,r,m,subject,kind,focus,q,event,pattern,reason in [
 ('I020-market',2,3,0,'中国移动游戏市场','priority_mobile_market',[],'移动游戏收入678.20亿元','Q3中国移动市场报告',None,'汇编沿用21日已披露报告，早于本期；不是26日新市场数据。'),
 ('I020-jd',3,3,0,'京东游戏业务','major_internet_gaming',[],'京东近日全资成立北京京玩互娱网络科技','京东成立京玩互娱','京东','历史13日实体成立，转载不改变状态，已曝光。'),
 ('I020-human',3,3,0,'腾讯光子','focus_subject',['腾讯'],'腾讯光子工作室群H.Studio公布开放世界RPG《人间异想计划》22分钟实机','人间异想计划首曝','人间异想','21日首曝已曝光，本期无新实机版本。'),
 ('I020-meta',3,3,0,'Supercell','focus_subject',['Supercell'],'Supercell对其全资收购已完成交割','Supercell收购Metacore交割','Metacore','19日交割已曝光，本期无新交易进展。'),
 ('I020-liquid',3,2,0,'Liquid Swords','focus_affiliate',['网易'],'网易曾于 2022 年购入该公司少数股权','Liquid Swords破产','Liquid Swords','已在周报曝光的破产同事件，无新事实。'),
 ('I020-lisi',2,0,0,'莉丝游戏','other_or_unknown',[],'莉丝游戏《Clashof Critters》','Clashof Critters收入5000万美元',None,'原文写莉丝游戏，不能擅自修成莉莉丝取得R3；发行主体R0。'),
]:
 d=ind(20,e,r,m,reason,subject,kind,focus,q,cid=cid,event=event)
 if pattern:hist(d,pattern)
DM['I020-meta']['subject_assessment']['evidence'].append(ev(20,'Supercell'))

def ai(i,reason,include=False,tier='direct_application',stage=None,reverse=True):
 d=dec(f'A{i:03}','ai_trends',[i],S[sid(i)]['title'],reason,include);d.update(ai_tier=tier,game_stage=stage or ['development'],industry_reverse_scan=reverse)
 if tier=='transferable_frontier':d['migration_path']='能力或流程变化可迁移至游戏工具、内容或运营，但本期缺少足够直接验证或不优于已选直接应用。'
 return d
for i in [4,27,28,29,30,113,117,118,119,124,125,126,127,128,141,159,191,200]:
 reason='行业候选全量AI反扫：旧案例/译文、缺少当期日期或仅方法观点、未验证游戏落地，排除。'
 if i==141:reason='采用本期Creative Assembly最新外包审核说明及处理状态；不把上周下架重写成26日下架。'
 if i==191:reason='采用本期Naavik编译研究，区分实时联动、机制移植及完整反编译；传播量和重建速度来自作者研究，不当作发行产品。'
 if i==200:reason='24—25日Sweeney言论及周综，早于日报窗口；非Steam26日新披露政策。'
 ai(i,reason,i in [141,191])
ai(140,'另拆独立营销应用：焦恩俊授权AI形象用于新天龙TVC，完整访谈和同日对照文共同支持。',True,stage=['publishing'])
for i in range(216,232):
 tier='transferable_frontier' if i in [217,219,222,224,225,226,228,229,230] else 'direct_application'
 ai(i,'原始AI池逐项审查：通用融资/科学/安全或参数信息缺少本期具体游戏验证；有迁移空间者优先级低于已选三条直接游戏应用。' if i!=231 else '引擎来源只有245字导语，非AI案例全文，不当作完整游戏开发复盘。',False,tier,reverse=False)

# Community candidates keep the trigger, contested logic and in-window follow-up separate.
for i in range(241,259):
 d=dec(f'C{i:03}','community_discourse',[i],S[sid(i)]['title'],'同窗口社区池已补扫；缺少明确新事件/可读后续、旧争议无新增、证据薄或相较已选事件优先级较低。',i in [242,252])
 d['community']=dict(trigger=S[sid(i)]['title'],claim_scope='玩家帖及回复者主张，不等同官方事实',complaint_logic='按该帖具体机制审查，不把同游戏其他争议并入。',timeline='仅使用2026-10-26及必要前情；27日回复不用。',follow_up_scan='扫描全部行业与社区输入，以产品名、AI、修复、和谐、公告、回应反查；无同事件官方来源，不在正文追加免责句。')
DM['C242']['community'].update(trigger='小葱活动立绘被指龙尾错位，26日回复称已两次修改',complaint_logic='玩家关注尾巴、头发和头饰错误及修复质量，另有对活动耗时奖励的批评',timeline='20日原帖，26日新增两轮修复与头饰仍未修的说法')
DM['C252']['community'].update(trigger='发售前夕手游角色全涂黑的指控',complaint_logic='回复者称只有部分调整且早在9月，质疑把旧手游修改绑定单机发售',timeline='26日上午建帖，26日晚回复补充9月时间线')
DM['C254']['reason']='周末报已收录同一渡鸦机制，26日回复只是重复表达概率/资源回收看法，未见新官方状态，排除。'
for i in [259,260]:
 d=dec(f'D{i:03}','deep_analysis',[i],S[sid(i)]['title'],'付费节目只有预览可读，不能作为唯一核心深度来源。' if i==259 else '奖项征集广告，不是可分析的机制研究。')
 d['scores']=dict(relevance=2,insight=1,evidence=1,card=1,total=5) if i==259 else dict(relevance=1,insight=0,evidence=0,card=0,total=1)
deep=dec('D140','deep_analysis',[140,211],'新天龙用分服承接用户时间差异','同日完整主创/运营报道与横向分析交叉支持，围绕用户时间预算而非普通周年内容；不同于上期AI研究到设计主题。',True)
deep['scores']=dict(relevance=3,insight=3,evidence=2,card=3,total=11)

# Calendar editorial correction is isolated from read-only news_data.
raw_path=P/'release_calendar_audit_raw.json'
a=json.loads(raw_path.read_text(encoding='utf-8'));nodes=a['nodes']
def recalc(n):
 n['source_ids']=list(dict.fromkeys(n['source_ids'])); n['industry_ids']=[i for i in n['source_ids'] if S[i]['section']=='industry_news'];n['release_ids']=[i for i in n['source_ids'] if S[i]['section']=='release_calendar']
 fingerprints=[];urls=set();hashes=set()
 for i in n['source_ids']:
  url=S[i]['url'];h=hashlib.sha256(S[i]['text'].encode()).hexdigest()
  if url in urls or h in hashes:continue
  urls.add(url);hashes.add(h);fingerprints.append(h)
 n['source_fingerprints']=fingerprints;n['appearance_count']=len(fingerprints);n['appearance_score']=min(3,n['appearance_count']);n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus'];n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus'];n['multi_source_eligible']=n['appearance_count']>=2
 n['window_scope']='report_window' if n['event_date']=='2026-10-26' else 'next_day_lookahead' if n['event_date']=='2026-10-27' else 'future_announcement' if n['signal_type'] in ['new_game_schedule','new_game_first_reveal'] else 'outside'
 n['publish_eligible']=n['multi_source_eligible'] and n.get('window_eligible',True) and not n.get('editorial_exclusion_reason')
 n['coverage']='mixed' if n['industry_ids'] and n['release_ids'] else 'industry_only' if n['industry_ids'] else 'release_only'
def edit(n,reason=None,**kw): n.update(kw);n['editorial_exclusion_reason']=reason or '';recalc(n)
for n in nodes:
 product=n['product']
 if '蓝色星原' in product:
  n.update(focus_companies=[],focus_company_relationships={},company_evidence_ids=[],company_relationship='none',company_bonus=0)
  edit(n,'23日公测定档已进入周末报；并非网易产品，不得把邻句无限大的主体加给蓝原。')
 elif product=='无限大':edit(n,'正文15写已在科隆展公布，非26日首次定档；原文11的此前句不能成为新日期。')
 elif '篮球少女' in product:edit(n,'10月23日公测并已进入上期日历；不是26日新定档。',event_date='2026-10-23')
 elif '王者万象棋' in product:edit(n,'周年活动版本/新内容预告不是新品测试、首次定档或首曝。')
 elif product in ['地心归途','胡闹赶鸭','HollywoodMerge','黑神话：悟空','奥咕和秘密森林','GTA6','原神','新天龙八部','剑侠世界4：无限']:edit(n,'正文为历史上线、普通版本、创作案例或发售背景，不是本期新的日历事件。')
 elif 'Sign' in product:
  edit(n,None,product='Sign：碎冠篇',source_ids=['S0006','S0132'],event_date='2026-10-26',signal_type='new_game_launch',event='正式发售',event_type_score=3)
 elif '余烬' in product:
  edit(n,'同一10月27日抢先体验档期已在9月23日日历公布；本期仍是发售预告，不能伪装成已开始EA。',product='余烬之镇',source_ids=['S0182','S0190'],event_date='2026-10-27',signal_type='new_game_launch',event='将开启抢先体验',event_type_score=3)
 elif '影之刃零' in product:edit(n,'29日发售为重复宣传且晚于次日窗口；预下载只在204单源，另建节点。')
 elif product in ['4：AM','Pool of Madness','Wall World Strategy']:
  edit(n,None,signal_type='new_game_schedule',event_type_score=2,window_eligible=True)
 else:recalc(n)
# Remove duplicate representations but preserve every raw node in a merge audit.
seen={};merged=[];dedup=[]
for n in nodes:
 key=(n['product'],n['event_date'])
 if key in seen: merged.append(dict(candidate_id=n['candidate_id'],merge_into=seen[key]['candidate_id'],raw_node=n));continue
 seen[key]=n;dedup.append(n)
nodes=dedup
def extra(product,ids,date,signal,event,reason=None,focus=None,company=0):
 n=dict(product=product,event_date=date,signal_type=signal,event=event,event_type_score=3 if signal in ['new_game_launch','new_game_test'] else 2 if signal.startswith('new_game_') else 1,first_seen_order=1000+len(nodes),observed_signal_types=[signal],observed_events=[event],source_ids=[sid(i) for i in ids],focus_companies=focus or [],focus_company_relationships={f:'direct' for f in (focus or [])},company_evidence_ids=[sid(ids[0])] if company else [],company_relationship='direct' if company else 'none',company_bonus=company,window_eligible=True,status='pending_decision',candidate_id=f'release-extra-{len(nodes):03}')
 edit(n,reason);nodes.append(n)
extra('影之刃零',[204],'2026-10-26','new_game_preload','预下载开启')
extra('大圣牌：凌霄斗神',[10],'2027-Q1','new_game_schedule','明年一季度计划发布，非精确日期','只有季度计划且10月23日电话会前情，没有精确日期。', ['吉比特'],3)
extra('甄嬛传',[10],'2027-Q1','new_game_schedule','明年一季度计划发布，非精确日期','同电话会季度规划，无精确日期且非26日新公告。',['吉比特'],3)
extra('饼干人联盟',[158],'2026-10-29','new_game_schedule','限量删档计费测试定档')
extra('开派大祖师',[235],'2026-10-26','new_game_preload','开放下载')
extra('警目如炬',[136],'2026-10-26','new_game_test','Demo试玩','只写近期放出Demo，没有26日首次公开证据。')
extra('木木屋',[135],'2026-10-26','new_game_launch','已发售的回顾','未证实26日首次上线，98%好评复盘非新发售。')
extra('Assassin’s Creed Black Flag Resynced',[239],'2026-10-27','old_major_update','New Game+更新','只有RSS摘要，不能核验重大版本机制，普通更新不具本期资格。')
extra('S.T.A.L.K.E.R. 2: Heart of Chornobyl',[240],'2026-10-26','old_major_update','2.1版本更新','只有RSS摘要，不能核验重大版本机制，普通更新不具本期资格。')
# Whole weekly Steam preview is read product by product; each remains single-source.
text=S['S0190']['text'];lines=text.splitlines()
for j,l in enumerate(lines):
 if l.startswith('发行日期：') and '2026/10/27' in l:
  name=next((v.strip() for v in reversed(lines[:j]) if v.strip() and not v.startswith('关键字：')), '')
  if '余烬' in name:continue
  extra(name,[190],'2026-10-27','new_game_launch','次日Steam发售预览')
nodes.sort(key=lambda n:(-int(bool(n['publish_eligible'])),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
a['nodes']=nodes;a['editorial_merged_nodes']=merged;a['editorial_reverse_scan']='全量224条行业/日历正文按产品、事件、日期反扫；周开测稿及Steam逐产品补录；归属、历史日期与跨期重复独立纠正。'
save('release_calendar_audit.json',a)
for x in merged:dec(x['candidate_id'],'release_calendar',x['raw_node']['source_ids'],x['raw_node']['product'],'同产品同日期节点确定性合并；所有原始召回留在raw审计。')['decision']='exclude'
covered={i for d in D for i in d['source_ids']}|{i for n in nodes for i in n['source_ids']}
for k in set(S)-covered:dec('X'+k,'release_calendar' if S[k]['section']=='release_calendar' else S[k]['section'],[k],S[k]['title'],'普通版本/活动或无合格事件；完整输入检查后排除。')
save('selection_decisions.json',dict(scoring_version='subject_genre_v2',report_type='daily',report_window=dict(start='2026-10-26',end='2026-10-26'),decisions=D))
print('inputs',len(S),'decisions',len(D),'calendar nodes',len(nodes),'eligible',[n['product'] for n in nodes if n['publish_eligible']])
