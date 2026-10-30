from __future__ import annotations
import json, re, sys, copy, hashlib
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime, timezone, timedelta

ROOT=Path.cwd(); sys.path.insert(0,str(ROOT/'scripts'))
from industry_timing import build_time_check
from report_artifacts import parse_report_items
from sync_release_decisions import sync
B=ROOT/'output/weekly/2026-10-23_to_2026-10-29/_intermediate'; OUT=B.parent
START='2026-10-23'; END='2026-10-29'; ID=START+'_to_'+END
ROWS=[json.loads(s) for s in (B/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
SRC={r['source_id']:r for r in ROWS}
PRIOR=json.loads((B/'prior_decisions_remapped.json').read_text(encoding='utf-8'))
OLD_ITEMS=json.loads((B/'prior_items_remapped.json').read_text(encoding='utf-8'))
H=json.loads((B/'industry_history_14d.json').read_text(encoding='utf-8'))
HALL=H['occurrences']+H['archive_occurrences']
DEC=[]; ITEMS=[]; BODY={}; ASSIGNED={}; old_to_new={}

def dump(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def quote(sid,needle):
 t=SRC[sid]['text']; assert needle in t,(sid,needle)
 return next((p.strip() for p in t.splitlines() if needle in p),needle)
def hist(terms):
 return [h for h in HALL if any(t.lower() in (' '.join([h.get('title',''),h.get('event','')]+h.get('claims',[])+h.get('entities',[]))).lower() for t in terms)]
def history(rows=None,novelty='new_event',facts=None):
 rows=rows or []
 return dict(history_match=bool(rows),novelty=novelty,prior_occurrences=[f"{h['report_kind']} {h['report_window']['start']}_to_{h['report_window']['end']}｜{h['title']}" for h in rows],new_facts=facts or [],prior_card_exposed=any(h['card_exposed'] for h in rows) if rows else None,archive_checked=True,exposure_details=[{k:h.get(k) for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source','artifact']} for h in rows])
def cluster(d):
 if len(d['source_ids'])>1:d['cluster_basis']=dict(subject=d['entities'][0],product=d['entities'][-1],event_date=d.get('event_date','unknown'),event=d['event'])
def timing(d):
 if d['section']=='industry_news' and d['scores']['event']:
  d['time_check']=build_time_check(d['source_ids'],SRC,START,END,event_date=d.get('event_date') or 'unknown',basis='逐一使用当前消费来源published_at；缺失时回退输入date。事件时间只供历史叙述，不作准入门槛。')
def add_ind(cid,title,sids,score,subject,kind,focus,basis,paragraphs,evidence,genre=None,event_date='unknown',hc=None):
 sids=sids.split(',') if isinstance(sids,str) else sids
 e,r,m=score
 d=dict(candidate_id=cid,section='industry_news',title=title,source_ids=sids,entities=[subject,title],event=title,event_date=event_date,decision='include',reason=basis,scores=dict(event=e,relevance=r,hook=m,total=e*r+m),subject_assessment=dict(subject=subject,kind=kind,focus_companies=focus,basis=basis,evidence=[dict(source_id=sids[0],evidence=quote(evidence[0][1],evidence[0][2]))]),genre_assessment=dict(matched_genres=[genre[0]] if genre else [],basis='本事件明确涉及对应重点品类' if genre else '本条事件没有明确的重点细分品类证据，不借其他产品或一般标签加分。',evidence=[dict(source_id=genre[1],evidence=quote(genre[1],genre[2]))] if genre else []),history_check=hc or history())
 if d['history_check']['novelty']=='card_carryover':d['card_carryover']=True
 cluster(d);timing(d)
 claims=[]
 for claim,sid,needle in evidence:claims.append(dict(claim=claim,source_id=sid,evidence=quote(sid,needle)))
 body='\n\n'.join(paragraphs)
 for c in claims: assert c['claim'] in title+'\n'+body,(cid,c['claim'])
 it=dict(candidate_id=cid,section='industry_news',title=title,source_ids=sids,claims=claims)
 DEC.append(d);ITEMS.append(it);BODY[cid]=body
 for sid in sids:ASSIGNED.setdefault(sid,cid)
 return d

# 本周既有正文只作为可复用事实草稿；来源ID按URL及正文重新映射，历史与时间重新判定。
for it0 in OLD_ITEMS:
 if it0['section']!='industry_news':continue
 it=copy.deepcopy(it0);rel=it.pop('prior_report')
 d=copy.deepcopy(next(d for d in PRIOR if d['prior_report']==rel and d['candidate_id']==it['candidate_id']))
 old=it['candidate_id'];cid='W'+rel.split('/')[-1].replace('-','').replace('_to_','_')+'_'+old
 old_to_new[(rel,old)]=cid;it['candidate_id']=cid;d['candidate_id']=cid
 report=next(p for p in (ROOT/'output'/rel).glob('game_industry_*.md'))
 visible=next(x for x in parse_report_items(report.read_text(encoding='utf-8')) if x.title==it['title'])
 BODY[cid]=visible.body
 d['title']=it['title'];d['reason']='本周逐字来源及影响力复核后通过；汇总当周日报/周末报的同一事件，仅刊一次。 '+d['reason']
 # 本期周报可汇总当周日报/周末报；同时保留此前跨期曝光记录。
 hc=copy.deepcopy(d.get('history_check') or history())
 hc['history_match']=True
 hc['prior_occurrences']=list(dict.fromkeys(hc.get('prior_occurrences',[])+[rel+'｜'+it['title']]))
 hc['prior_card_exposed']=bool(hc.get('prior_card_exposed'))
 hc['archive_checked']=True;d['history_check']=hc
 if hc.get('novelty')=='new_event':hc['weekly_rollup']=True
 # 更正旧稿把协商原截止日当作延长期终点的歧义。
 if old=='I010' and rel=='daily/2026-10-27':
  BODY[cid]='微软将Arkane Lyon寻找买家的协商期再延长一个月，并探索寻找合作方，支持工作室完成《漫威刀锋战士》的后续开发。此前报道的原截止日为11月13日；微软强调此次延期有明确期限，并承诺持续向职工委员会通报进展。工作室217名员工的去向仍与谈判结果相关。'
  it['source_ids']=['S0761','S0969'];d['source_ids']=it['source_ids']
  it['claims']=[dict(claim=c,source_id='S0969',evidence=quote('S0969',n)) for c,n in [('微软将Arkane Lyon寻找买家的协商期再延长一个月','微软一位代表向PC Gamer表示'),('《漫威刀锋战士》','正探索引入其他公司'),('原截止日为11月13日','此前的报道声称'),('217名员工','217名员工')]]
 # 已确认项目的新发售目标属档期变化，不能再当作新立项首曝。
 if old=='I206' and rel=='daily/2026-10-28':
  d['scores']=dict(event=2,relevance=3,hook=0,total=6);d['reason']='科乐美既有重制项目的新目标档期报道，E2R3M0=6；爆料仍保留归因，未当作官方定档。'
 # 旧判断说明中存在和最终分值不一致的泛化文案，按实际证据改写。
 if old=='I244':d['subject_assessment']['basis']='Blizzard开发及取消大型MMO项目并将团队转向Overwatch，属于全球头部研发主体直接项目变化；来源明确七年研发及六周重新提案。'
 cluster(d);timing(d)
 DEC.append(d);ITEMS.append(it)
 for sid in it['source_ids']:ASSIGNED.setdefault(sid,cid)

add_ind('N_CAPCOM','卡普空确认Capcom ID数据泄露涉及逾1170万账户','S0263',(2,3,0),'Capcom','comparable_major_subject',[],
 '来源证明跨《Street Fighter 6》《Monster Hunter》《Resident Evil》产品组合的统一账户系统及1170万账户覆盖，属于全球头部发行研发主体，R3；账户安全状态E2。',
 ['卡普空确认，10月19日第三方未经授权访问客户信息，事件影响超过1170万个Capcom ID账户。该账户系统用于《Street Fighter 6》《Monster Hunter》《Resident Evil》等产品的在线功能、网页服务与多人游戏。',
  '10月23日更新称，196个账户的密码曾被擅自更改，已全部重置；其中19个账户的日本e-Capcom商店页面遭到访问。受影响信息包括姓名、联系方式及购买记录，信用卡信息未受影响，相关游戏服务仍然可用。'],
 [('超过1170万个Capcom ID账户','S0263','over 11.7 million'),('《Street Fighter 6》《Monster Hunter》《Resident Evil》','S0263','including for titles'),('10月19日','S0263','on October 19'),('196个账户','S0263','196 accounts'),('19个账户','S0263','19 of the 196'),('信用卡信息未受影响','S0263','Credit card information'),('相关游戏服务仍然可用','S0263','remain available')],event_date='2026-10-23')

add_ind('N_SIDE','Side收购成都美术工作室Roboto，并任命全球美术负责人','S0141,S0764',(3,2,0),'Side','comparable_significant_subject',[],
 'Side跨美洲、EMEA和亚洲服务网络、逾500名美术师及多款AAA项目参与证明其具有较强行业影响力；收购及全球负责人任命E3R2。',
 ['Side于10月21日宣布收购成都美术工作室Roboto Entertainment，并据此成立成都工作室。Roboto创始人Andrea Cordella同时出任Side全球美术主管与成都工作室负责人，统筹跨地区美术团队。',
  '成都为Side继上海之后在中国大陆的第二个站点。Roboto专长是环境与世界构建美术，与Side此前偏角色美术的能力互补；这笔交易将中国团队的职责从交付扩展到全球美术管理。'],
 [('10月21日','S0141','10月21日'),('Roboto Entertainment','S0141','Roboto Entertainment'),('Andrea Cordella','S0141','Andrea Cordella'),('全球美术主管与成都工作室负责人','S0141','统管Side遍布'),('第二个站点','S0141','第二个站点'),('此前偏角色美术','S0141','更多集中在角色美术侧')],event_date='2026-10-21')

add_ind('N_SYBO','SYBO称《地铁跑酷》月活仍在1亿至1.5亿之间，长期基本未做买量','S0029',(2,3,0),'SYBO','comparable_major_subject',[],
 '来源证明49亿累计下载、1亿至1.5亿月活及长期全球移动产品经营规模，SYBO为名单外同等影响力手游主体；经营数据E2R3。',
 ['SYBO负责人Mathias Gredal Nørvig在访谈中估计，《地铁跑酷》的月活用户仍在1亿至1.5亿之间，累计下载约49亿次。其称长期基本没有投入买量，偶尔会花1500美元做小测试，产品约90%的收入来自广告。',
  '团队把《地铁跑酷：城市》定位为更适合深入参与的另一种体验，以较短跑酷循环、角色成长与资源选择提供更高难度。上述月活与零买量口径来自经营者自述，不能据此推导其他跑酷游戏的获客成本。'],
 [('Mathias Gredal Nørvig','S0029','Mathias Gredal Nørvig'),('1亿至1.5亿之间','S0029','MAU在1亿到1.5亿之间'),('49亿次','S0029','49亿次的下载量'),('1500美元','S0029','1500美元'),('90%的收入来自广告','S0029','90%收入都来自广告'),('较短跑酷循环','S0029','跑酷时间更短')])

add_ind('N_DOUYIN','抖音小游戏白皮书回顾2025年流水近翻倍，内容渠道用户LTV提高约50%','S0109',(2,3,0),'抖音小游戏','major_internet_gaming',[],
 '头部互联网平台的小游戏业务与中国移动市场数据，R3；2025年统计口径属于当期报道支持的历史数据，E2。',
 ['《2026抖音小游戏行业白皮书》回顾称，2025年抖音小游戏总流水增长近100%，活跃用户规模增长超过120%，在小游戏市场的份额接近30%。这是2025年的平台统计，不能当作10月单月变化。',
  '白皮书称，内容渠道进入的玩家LTV提升约50%，2025年第四季度短视频和直播内容直接转化收入同比增长160%。在小游戏内购与混合变现扩张的同时，平台把内容传播和社交互动作为延长产品经营周期的主要路径。'],
 [('《2026抖音小游戏行业白皮书》','S0109','《2026 抖音小游戏 行业白皮书》'),('总流水增长近100%','S0109','总流水规模增长近100%'),('活跃用户规模增长超过120%','S0109','活跃用户规模增长超120%'),('份额接近30%','S0109','份额占比接近30%'),('玩家LTV提升约50%','S0109','LTV（生命周期总价值）提升约50%'),('同比增长160%','S0109','同比增幅更是达160%')])

add_ind('N_WECHAT','微信小游戏回顾2025年生态：逾300款产品季度流水超过千万元','S0131',(2,3,0),'微信小游戏','major_internet_gaming',[],
 '腾讯旗下移动小游戏平台2025年生态数据E2R3；同事件历史均未曝光，按分数/R/顺序竞争本期唯一内部保留位。',
 ['微信小游戏在2026公开课的生态回顾中披露，平台月活稳定在5亿以上，2025年业务规模增长接近20%。逾300款产品的季度流水超过千万元，数据反映的是2025年生态规模。',
  '回顾同时提到，平台日活同比增长10%，每月活跃至少10天的高黏性用户同比增长27%。这些指标分别描述活跃频次与留存人群，不能直接等同为单款游戏的留存改善。'],
 [('2026公开课','S0131','2026'),('月活稳定在5亿以上','S0131','500'),('增长接近20%','S0131','20%'),('逾300款产品','S0131','300'),('季度流水超过千万元','S0131','10 milhões'),('日活同比增长10%','S0131','10%'),('同比增长27%','S0131','27%')],hc=history([h for h in hist(['微信小游戏']) if h['report_window']['start']<='2026-06-05'],'card_carryover'))

add_ind('N_NEKODAY','网易与哔哩哔哩参投的Nekoday以新作众筹缓解开发资金压力','S0167',(3,2,0),'Nekoday','focus_affiliate',['网易','哔哩哔哩'],
 '来源明确Nekoday获Bilibili和NetEase投资，R2；续作众筹超过60万元是资本筹措E3，并保留春节前发起的历史语态。',
 ['Nekoday在《Bubble Winter Scenery》之后获得哔哩哔哩与网易投资，但其后经历项目取消、亏损与团队缩减。团队与原有伙伴合作开发续作《Poema do Fim do Século》，并在春节前启动众筹。',
  '本期访谈回顾，众筹上线不足一个月获得约1800人支持、筹款超过60万元，超过目标十倍。负责人称资金不再是当前开发的主要障碍，团队计划年内完成作品；这是项目方计划，尚非发售结果。'],
 [('Nekoday','S0167','Nekoday'),('哔哩哔哩与网易投资','S0167','Bilibili e da NetEase'),('《Bubble Winter Scenery》','S0167','Bubble Winter Scenery'),('《Poema do Fim do Século》','S0167','Poema do Fim do Século'),('春节前启动众筹','S0167','Na véspera do Festival da Primavera'),('约1800人支持、筹款超过60万元','S0167','1 800 jogadores'),('计划年内完成作品','S0167','concluir o jogo ainda este ano')])

add_ind('N_HIGHGUARD','《Highguard》停运复盘：3月公告关闭服务器，未达到持续经营所需用户规模','S0184',(2,2,1),'Wildlight','focus_affiliate',['腾讯'],
 '来源证明Wildlight获Tencent投资及Respawn/Apex核心团队背景，按实际工作室R2；停运E2，FPS竞技M1。',
 ['本期报道回顾，《Highguard》在3月4日宣布将于3月12日关闭服务器。Wildlight开发的这款FPS于1月27日上线Steam；官方称累计吸引超过200万玩家，但未能形成支持长期运营的用户基础。',
  '报道援引前员工采访称，团队早期希望避开拥挤的大逃杀市场，后从生存玩法转向更快节奏的竞技射击，部分生存机制被简化。团队对资金、留存与产品方向的判断来自受访者复盘，不能归结为单一玩法导致停运。'],
 [('3月4日','S0184','4 de marzo'),('3月12日','S0184','12 de marzo'),('Wildlight','S0184','Wildlight'),('1月27日上线Steam','S0184','Steam el 27 de enero'),('超过200万玩家','S0184','más de dos millones'),('更快节奏的竞技射击','S0184','más rápida y competitiva')],genre=('competitive','S0184','juego de disparos en primera persona'),event_date='2026-03-04')

add_ind('N_RE9','卡普空3月销量回顾：《Resident Evil 9》五天销量超过500万份','S0249',(2,3,0),'Capcom','comparable_major_subject',[],
 'Capcom全球头部IP与跨作商业规模直接取证，R3；本事件为具体销量数据E2，非例行公司财报。',
 ['本期文章回顾，卡普空在3月4日公告《Resident Evil 9: Requiem》销量超过500万份，达成这一销量用了五天。报道指出，其销售速度超过《Resident Evil 8》和《Resident Evil 4: Remake》。',
  '这是系列三十周年背景下的历史销量节点。正文对双主角、恐怖与动作体验的评价属于作者判断，销量表现本身不能证明所有设计变化均获得玩家认可。'],
 [('3月4日','S0249','4 de março'),('卡普空','S0249','Capcom'),('《Resident Evil 9: Requiem》','S0249','Resident Evil 9: Requiem'),('超过500万份','S0249','5 milhões'),('五天','S0249','5 dias'),('《Resident Evil 8》和《Resident Evil 4: Remake》','S0249','Resident Evil 8'),('三十周年','S0249','trinta anos')],event_date='2026-03-04')

add_ind('N_MOORE','前《Moore Manor》制作人加入网易《Eggy Party》团队，负责副玩法内容','S0658',(3,3,0),'网易','focus_subject',['网易'],
 '实际接收人才的主体为网易直属Eggy团队，R3；前制作人加入产品团队的核心人才变化E3，M0不借派对标签加分。',
 ['本期报道回顾，前《Moore Manor》制作人、Qutang Network创始人Zheng Zhouri已于报道所述的上月加入网易杭州《Eggy Party》项目组，负责副玩法内容。报道未给出入职的绝对日期，不能据10月采集日倒推出具体入职月份。',
  'Qutang Network曾获FunPlus等支持，开发《Mimimaha》，其后进入破产清算流程。报道同时提到，管理人正在公开遴选资产评估机构，评估以游戏为主的无形资产。'],
 [('Zheng Zhouri','S0658','Zheng Zhouri'),('网易杭州《Eggy Party》项目组','S0658','Eggy Party'),('负责副玩法内容','S0658','mecánicas secundarias'),('FunPlus','S0658','FunPlus'),('资产评估机构','S0658','entidad de valoración')])

add_ind('N_GENSHIN','原神UGC开发复盘：截至1月累计游玩超过1.5亿次，吸引逾3万创作者','S0673',(2,3,0),'米哈游','focus_subject',['米哈游'],
 '米哈游直接产品的UGC数据E2R3；1.5亿指累计游玩次数，非收入、独立玩家或本月新增。',
 ['在本期刊载的GDC开发复盘中，米哈游披露，《原神》UGC模块截至1月累计游玩超过1.5亿次，吸引国内外超过3万名创作者。模块于2025年10月推出，相关数字保留原有统计时点。',
  '分享回顾，团队从2022年开始关注UGC，系统经历约两年研发，并准备继续提供内容支持。它反映的是玩家从消费内容转向参与制作的规模，游玩次数不能直接换算为独立用户或商业收入。'],
 [('米哈游','S0673','miHoYo'),('《原神》','S0673','Genshin Impact'),('截至1月累计游玩超过1.5亿次','S0673','hasta enero de este año'),('超过3万名创作者','S0673','más de 30 000'),('2025年10月','S0673','octubre de 2025'),('2022年','S0673','en 2022'),('约两年研发','S0673','dos años de investigación')])

add_ind('N_ROCO_TEST','腾讯魔方3月《Roco Kingdom》试玩回顾：围绕收集、培养与战斗构建开放世界','S0715',(3,3,0),'腾讯魔方','focus_subject',['腾讯'],
 '腾讯Magic Cube直属项目线下新品测试E3R3；不把收集/培养/战斗一般标签自动当作竞技或数值卡牌RPG。与西方发行规划为不同日期的独立事件。',
 ['本期文章回顾，腾讯魔方开发的《Roco Kingdom》于3月12日开启为期三天的线下试玩，当时公布的全平台上线日为3月26日，预约量超过5000万。这里描述的是3月测试阶段，不能当作本周开测。',
  '试玩把精灵收集、培养、战斗与开放世界探索结合，强调精灵作为冒险伙伴的关系。与本期另一篇2027年西方发行规划相比，这条材料对应的是较早的产品验证阶段。'],
 [('腾讯魔方','S0715','Magic Cube de Tencent'),('3月12日','S0715','12 de marzo'),('为期三天','S0715','tres días'),('《Roco Kingdom》','S0715','El Reino de Lock'),('3月26日','S0715','26 de marzo'),('超过5000万','S0715','50 millones'),('精灵收集、培养、战斗','S0715','coleccionar, criar y luchar')],event_date='2026-03-12')

add_ind('N_SPIRE','《Slay the Spire 2》3月EA发售回顾：Steam峰值在线超过28万','S0722',(3,2,0),'Slay the Spire系列开发主体','comparable_significant_subject',[],
 '来源证明定义roguelike卡组构筑细分市场、长期Steam愿望单前五与续作28万峰值，具有较强行业影响力R2；EA实际发售E3；卡组构筑不自动等于数值卡牌RPG，M0。',
 ['《Slay the Spire 2》于3月6日凌晨2点进入Steam抢先体验。报道回顾，发售初期同时在线峰值超过28万，全语言好评率为97%，并曾登上Steam畅销榜首位。',
  '文章记录，发售前后平台出现购买与入库异常，部分玩家重复付款后仍未收到游戏。这些是当时的发售现象，不能据本期转载推断Steam目前仍存在同样故障。'],
 [('《Slay the Spire 2》','S0722','Slay the Spire 2'),('3月6日凌晨2点','S0722','2:00 a.m. today (March 6)'),('超过28万','S0722','over 280,000'),('97%','S0722','97%'),('重复付款后仍未收到游戏','S0722','making a duplicate purchase')],event_date='2026-03-06')

add_ind('N_HELIX','Xbox在3月公开下一代主机代号Project Helix，计划兼容PC游戏','S0727',(3,3,0),'Xbox','major_internet_gaming',[],
 'Microsoft游戏主机平台业务R3；Asha Sharma公开新硬件代号与PC兼容目标属于战略项目公开E3。6月已刊的是硬件成本危机及商业模式表态，不是3月代号公布同一事件。',
 ['本期转载的3月10日报道称，Xbox负责人Asha Sharma公开了下一代主机代号Project Helix，计划同时运行Xbox游戏并原生兼容PC游戏。这个项目当时仍在开发，不能把兼容目标当作已交付能力。',
  '报道中的双系统、模块化硬件等细节属于分析者推测，尚无完整技术披露。相比此前单纯销售主机的边界，该项目提出了连接PC与主机游戏库的方向，但落地规格与商业模式仍待正式确认。'],
 [('3月10日','S0727','10 de marzo de 2026'),('Asha Sharma','S0727','Asha Sharma'),('Project Helix','S0727','Project Helix'),('原生兼容PC游戏','S0727','compatible de forma nativa con juegos de PC'),('尚无完整技术披露','S0727','no se han revelado por completo')],event_date='2026-03-10')

add_ind('N_FORGOTTEN','网易《遗忘之海》2月测试回顾：以海上探索和多种小游戏扩展开放世界','S0222',(3,3,0),'网易Joker','focus_subject',['网易'],
 '来源明确NetEase Games Joker的新作测试E3R3；本条2月测试与历史7月公测为不同事件日期和生命周期阶段，不伪造本周新开服。',
 ['本期转载回顾，网易Joker团队的《遗忘之海》于2月5日开启新一轮测试。文章记录，游戏以风格化木偶角色、海上探索和多种小游戏呈现开放世界，而非只延续单一战斗循环。',
  '测试体验包括海上巨型怪物、区域解谜与多样任务，作者据此讨论玩法组合的方向。这是2月开发验证阶段的记录，不能取代后续正式发行后的运营数据。'],
 [('网易Joker','S0222','divisão Joker da NetEase Games'),('《遗忘之海》','S0222','O Mar Esquecido'),('2月5日','S0222','5 de fevereiro'),('风格化木偶角色','S0222','marionetas animadas'),('海上巨型怪物、区域解谜','S0222','monstros com tentáculos')],event_date='2026-02-05')

add_ind('N_COD','微软确认《Call of Duty》系列累计收入超过400亿美元','S0960',(2,3,1),'Microsoft/Activision','major_internet_gaming',[],
 'Microsoft游戏业务与全球头部Activision系列的经营里程碑，R3；非公司例行财报E2；来源明确射击及battle royale产品形态M1。',
 ['Xbox负责人Asha Sharma确认，《Call of Duty》系列累计收入超过400亿美元。其在10月23日《Modern Warfare 4》发售后披露这一里程碑，但未说明新作销售情况，也未确认是否由新作直接推动跨过该门槛。',
  '该系列于2003年推出，此后扩展到移动端与《Warzone》等产品。系列累计收入不能当作《Modern Warfare 4》的收入，更不能据此计算单款利润。'],
 [('Asha Sharma','S0960','Asha Sharma'),('超过400亿美元','S0960','$40 billion'),('10月23日','S0960','October 23'),('《Modern Warfare 4》','S0960','Modern Warfare 4'),('未说明新作销售情况','S0960','did not, however, share any insights'),('2003年','S0960','in 2003'),('《Warzone》','S0960','Call of Duty: Warzone')],genre=('competitive','S0960','battle royale'))

add_ind('N_BIOWARE','EA确认关闭BioWare并取消开发中的《Mass Effect》新作','S0298',(2,3,0),'Electronic Arts','comparable_major_subject',[],
 'EA为经营全球头部RPG与多IP组合的发行研发主体，来源证明BioWare30年产品积累和多款代表作；不因PC/主机业务降R。关停及项目取消E2R3。',
 ['EA确认关闭BioWare，并取消开发中的《Mass Effect》新作。该项目于2020年公布，此后长期处于早期开发，关闭公告之后流出的预告片并不代表项目重新启动。',
  '报道援引分析师判断，近期作品商业表现与收购债务共同构成成本压力；这些是外部分析，不能代替公司对每一项关停原因的确认。《Mass Effect》真人剧仍在开发，与游戏取消属于不同项目状态。'],
 [('EA确认关闭BioWare','S0298','Electronic Arts just confirmed'),('2020年','S0298','revealed in 2020'),('处于早期开发','S0298','early development'),('外部分析','S0298','Video game analyst'),('真人剧仍在开发','S0298','TV show for Prime Video remains in development')])

add_ind('N_ATARI','Atari任命Hipster Whale联合创始人统筹移动游戏扩展','S1266',(3,2,0),'Atari移动游戏业务','comparable_significant_subject',[],
 '来源证明Atari收购Hipster Whale与Early Morning Studios后建设跨引擎、跨平台移动基础设施，属于具有较强影响力的游戏发行主体R2；核心高管任命E3。标题/正文对人名拼写不一致，正文只采用一致的职务、公司与职责。',
 ['Atari任命Hipster Whale联合创始人担任移动扩展业务执行副总裁。此前公司已收购Hipster Whale和Early Morning Studios，新任负责人的职责包括跨引擎兼容、与移动平台合作，以及建设移动游戏扩展基础设施。',
  '该任命将移动业务的组织职责集中到专门负责人，后续产品扩展仍需分别验证；人事任命本身不等于新移动产品已经上线。'],
 [('Hipster Whale联合创始人','S1266','co-founder of Hipster Whale'),('移动扩展业务执行副总裁','S1266','executive vice-president of Mobile expansion'),('Early Morning Studios','S1266','Early Morning Studios'),('建设移动游戏扩展基础设施','S1266','build out infrastructure')])

add_ind('N_CARD_TEST',"腾讯发行的《Kaeth's Dream》3月二测回顾：把卡组构筑与角色养成结合",'S0657',(3,3,0),'腾讯','focus_subject',['腾讯'],
 '来源直接确认Tencent发行、Smilegate旗下SUPER CREATIVE研发，3月11日付费二测为新品测试E3R3；DBG与CRPG标签不足单独证明数值卡牌RPG，M0。',
 ["本期报道回顾，腾讯发行、Smilegate旗下SUPER CREATIVE开发的手游《Kaeth's Dream》于3月11日启动第二轮付费测试。当时该作已完成国内首测，海外版本亦已进入运营，不能把此次转载当成本周首次公布。",
  '其设计通过保存roguelike对局成果，把局内构筑与后续角色战斗内容相连，并结合资源管理、路线选择与队伍配置。文章讨论的是腾讯二次元发行产品的差异化方向，未证明这些组合已带来国内长期商业成功。'],
 [("《Kaeth's Dream》",'S0657',"Kaeth's Dream"),('腾讯发行、Smilegate旗下SUPER CREATIVE开发','S0657','SUPER CREATIVE de Smilegate'),('3月11日','S0657','11 de marzo'),('第二轮付费测试','S0657','segunda fase de pruebas de pago'),('保存roguelike对局成果','S0657','mecanismo de guardado de datos')],event_date='2026-03-11')

add_ind('N_HOK_SCHEDULE','《王者荣耀：世界》3月定档回顾：PC版4月10日上线，公布两种PVP模式','S0680',(2,3,1),'腾讯','focus_subject',['腾讯'],
 '腾讯头部IP直接项目的档期公布E2R3；来源明确1对1及4对4的PVP模式M1。该3月20日发布会与4月17日移动端上线为不同事件，不把相同事实重复拆条。',
 ['本期转载回顾，《王者荣耀：世界》在3月20日发布会上宣布，PC版定于4月10日上线，移动版随后推出。发布会同时介绍上线英雄、成长系统与商业化方式。',
  '官方当时公布的PVP包括1对1与4对4模式，前者允许组合两种英雄共鸣，后者围绕多人护送与拦截展开。外观销售被确认为主要商业化方式；这些是发布会阶段的产品设计与档期信息。'],
 [('3月20日','S0680','3월 20일'),('《王者荣耀：世界》','S0680','왕자영예 월드'),('4月10日','S0680','4월 10일'),('PVP包括1对1与4对4','S0680','1대1과 4대4'),('主要商业化方式','S0680','주된 수익 모델')],genre=('competitive','S0680','PVP 모드'),event_date='2026-03-20')

add_ind('N_MARATHON','《Marathon》2月压力测试回顾：Steam峰值在线约14万，后续参与度回落','S0119',(3,3,1),'Bungie','comparable_major_subject',[],
 '来源证明Bungie以Halo、Destiny两代产品影响西方FPS，并直接研发Marathon，名单外头部主体R3；新品服务器压力测试E3，FPS竞技M1。',
 ['Bungie新作《Marathon》于2月27日开启免费服务器压力测试。本期文章回顾，Steam测试初期同时在线峰值约14万，预售曾进入Steam畅销榜前三；第二、第三天的同时在线规模随后明显回落。',
  '文章把资源控制与交火作为搜打撤体验的重点，同时记录玩家对界面和单人体验的不同看法。这是早期免费测试表现，不能据此推定正式发售后的销量或留存。'],
 [('Bungie','S0119','novo jogo da Bungie'),('2月27日','S0119','27 de fevereiro'),('免费服务器压力测试','S0119','teste de carga do servidor'),('约14万','S0119','140 mil'),('畅销榜前三','S0119','Top 3'),('明显回落','S0119','caiu rapidamente para metade')],genre=('competitive','S0119','pioneiros dos FPS'),event_date='2026-02-27')

add_ind('N_TIANXIA','网易回顾《天下：万象》跨端上线后表现，PCU达到近十年高点','S0177',(2,3,0),'网易','focus_subject',['网易'],
 'NetEase直属成熟IP跨平台版本上线与明确经营数据，E2R3；属于历史经营数据而非本周更新宣传，不因事件较早降低分值。',
 ['网易《天下》在2025年12月17日升级为《天下：万象》后，推出跨平台版本。本期复盘称，跨端版本上线后PCU达到近十年高点，付费用户数与付费率亦创纪录；2025年端游收入达到近十年最高水平。',
  '团队围绕老玩家回归负担调整产品，并加入满足登录天数条件后返还礼包费用的机制。该案例反映成熟IP试图降低回归投入的不确定性，所列经营表现保留原有年度和阶段口径。'],
 [('网易','S0177','NetEase'),('2025年12月17日','S0177','17 de dezembro do ano passado'),('《天下：万象》','S0177','Tianxia: Wanxiang'),('PCU达到近十年高点','S0177','valor mais elevado dos últimos dez anos'),('付费用户数与付费率亦创纪录','S0177','utilizadores pagantes e a taxa de pagamento'),('返还礼包费用','S0177','reembolso total do valor pago pelo pacote')])

add_ind('N_WATER','益世界《疯狂水世界》1月上线回顾：休闲SLG进入小游戏畅销榜前十','S0062',(2,2,1),'益世界','comparable_significant_subject',[],
 '来源证明Yishijie多款产品月收入过亿及国内外SLG发行能力，按具有较强影响力的主体R2；1月上线后跨渠道数据E2、明确SLGcasual M1。历史9月出海榜中的同名增长属不同统计期，不以产品名相同判作同一数据事件。',
 ['益世界《疯狂水世界》在2025年12月先推出小游戏版本，2026年1月8日推出手游版本。本期复盘记录，其微信小游戏畅销榜曾升至第7、抖音小游戏畅销榜第8。',
  '产品以洪水末日题材和明亮卡通风格切入休闲SLG，把模拟经营与策略成长结合。上述排名对应年初上线阶段，不能当作10月现时榜单表现。'],
 [('益世界','S0062','Yishijie'),('《疯狂水世界》','S0062','Crazy Water World'),('2025年12月','S0062','dezembro de 2025'),('1月8日','S0062','8 de janeiro'),('微信小游戏畅销榜曾升至第7、抖音小游戏畅销榜第8','S0062','7.º lugar'),('休闲SLG','S0062','SLG casual')],genre=('casual_slg','S0062','SLG casual'))

add_ind('N_LAST_ASYLUM','三七互娱《Last Asylum: Plague》首月收入回顾：估算超过2500万元','S0694',(2,3,1),'三七互娱','focus_subject',['三七互娱'],
 '37 Interactive Entertainment直属产品的首月经营数据E2R3，明确休闲SLG加M1；统计期为2月11日上线后的首月，与历史8月海外收入榜为不同统计事件。',
 ['本期文章回顾，三七互娱《Last Asylum: Plague》于2月11日上线，首月收入估算超过2500万元，报道时累计收入接近3000万元，数据来自点点出海。',
  '这款休闲SLG以欧洲黑死病和瘟疫医生为题材，在模拟经营、策略成长的框架内寻求视觉差异。这里保留上线首月的人民币口径，与此前8月榜单的美元收入及环比指标分别理解。'],
 [('三七互娱','S0694','37 Interactive Entertainment'),('《Last Asylum: Plague》','S0694','Last Asylum: Plague'),('2月11日','S0694','11 de fevereiro'),('2500万元','S0694','25 milhões de yuan'),('3000万元','S0694','30 milhões de yuan'),('休闲SLG','S0694','SLG casuais'),('瘟疫医生','S0694','médico da peste')],genre=('casual_slg','S0694','SLG casuais'))

# AI以具体游戏应用优先。本周用六个独立事件，不将同一公司的许可与研发实践合并。
def reuse_item(rel,old,cid,section):
 it=copy.deepcopy(next(x for x in OLD_ITEMS if x['prior_report']==rel and x['candidate_id']==old))
 it.pop('prior_report',None);it['candidate_id']=cid
 d=copy.deepcopy(next(x for x in PRIOR if x['prior_report']==rel and x['candidate_id']==old));d['candidate_id']=cid;d['decision']='include'
 p=next((ROOT/'output'/rel).glob('game_industry_*.md'))
 BODY[cid]=next(x.body for x in parse_report_items(p.read_text(encoding='utf-8')) if x.title==it['title'])
 it['section']=section;d['section']=section;d['title']=it['title'];d['reason']='当周同事件合并一次；'+d['reason']
 old_to_new[(rel,old)]=cid;ITEMS.append(it);DEC.append(d)
 for sid in it['source_ids']:ASSIGNED[sid]=cid
 return it,d

it,d=reuse_item('daily/2026-10-26','A141','A_SHOGUN','ai_trends')
it,d=reuse_item('daily/2026-10-28','A247','A_EPIC_CODE','ai_trends')
it,d=reuse_item('daily/2026-10-28','A176','A_EPIC_EULA','ai_trends')
it,d=reuse_item('daily/2026-10-28','A029','A_AILIAILI','ai_trends')

def add_ai(cid,title,sid,body,facts,tier='direct_application',stages=None,migration=''):
 d=dict(candidate_id=cid,title=title,section='ai_trends',source_ids=[sid],entities=[title],event=title,decision='include',reason='来源完整、游戏应用具体；当周独立事件按优先级采用。',ai_tier=tier,game_stage=stages or ['development'],industry_reverse_scan=SRC[sid]['section']=='industry_news')
 if migration:d['migration_path']=migration
 it=dict(candidate_id=cid,section='ai_trends',title=title,source_ids=[sid],claims=[dict(claim=c,source_id=sid,evidence=quote(sid,n)) for c,n in facts])
 for c in it['claims']:assert c['claim'] in title+'\n'+body
 DEC.append(d);ITEMS.append(it);BODY[cid]=body;ASSIGNED[sid]=cid

add_ai('A_SCALING','米哈游团队相关研究开源游戏操作模型，比较模型规模、数据量与实时表现','S0035',
 '10月22日晚，米哈游崩坏AI研发团队相关研究者与高校作者发布Scaling in Games开源项目，论文仍为arXiv预印本。研究以Qwen3.5视觉语言模型为基础，用游戏画面与键鼠操作记录训练，并以28款未进入训练数据的游戏检验陌生操作预测能力。测试比较不同模型规模、游戏数据量和实时条件，显示更大模型的样本效率优势仍受推理速度约束；这属于研究试验，尚不能视为公司已在商业游戏中部署通用玩家AI。',
 [('10月22日晚','10月22日晚'),('米哈游崩坏AI研发团队相关研究者','崩坏项目 AI 研发团队'),('arXiv预印本','arXiv预印本'),('Qwen3.5','Qwen3.5'),('28款','另外28款'),('实时条件','实时操作测试')])

add_ai('A_GENIE','Genie 4研究预览支持实时场景修改与原生音频，游戏开发者测试交互原型','S1353',
 'Google DeepMind发布Genie 4研究预览，支持通过自然语言实时改变场景，并同步生成环境声音与交互式对话。受信任的游戏开发者和创意技术人员正在测试把初步想法快速变成可探索的原型，在编写引擎代码之前验证视觉风格、材质和交互机制。该模型仍处早期阶段，长时一致性、复杂物理、可读文字与空间准确性存在限制，不能据短时演示认定其已能替代完整游戏引擎。',
 [('Google DeepMind','Google DeepMind'),('Genie 4研究预览','Genie 4 已作为研究预览版'),('交互式对话','交互式对话'),('在编写引擎代码之前','在编写任何一行引擎代码之前'),('长时一致性','长期一致性')],stages=['development','product'])

# 社区池本周三件独立事件，优先采用最新后续，不将玩家怀疑改写为官方事实。
reuse_item('weekend/2026-10-23_to_2026-10-25','C428','C_WUWA','community_discourse')
reuse_item('daily/2026-10-26','C242','C_END','community_discourse')
reuse_item('daily/2026-10-28','C345','C_DELTA','community_discourse')

# 精确消费飞书 C001、C022；其顺序及唯一指定主卡均不得自行变动。
cb=ROOT/'tmp/deep_observation_2026-10-22_to_2026-10-28'
review=json.loads((cb/'candidate_review.json').read_text(encoding='utf-8'))
crsrc={r['source_id']:r for r in map(json.loads,(cb/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
urlmap={r['url']:r['source_id'] for r in ROWS}
for cid in ['C001','C022']:
 c=next(x for x in review['candidates'] if x['candidate_id']==cid)
 mapping={s:urlmap[crsrc[s]['url']] for s in c['source_ids']}
 nid='D_'+cid; paragraphs=[p['detail'] for p in c['analysis_points']]
 body='观察：'+c['observation']+'\n\n分析：\n\n'+' '.join(paragraphs[:2])+'\n\n'+' '.join(paragraphs[2:])
 claims=[dict(claim=p['detail'],source_id=mapping[a['source_id']],evidence=a['evidence']) for p,a in zip(c['analysis_points'],c['evidence_anchors'])]
 it=dict(candidate_id=nid,section='deep_analysis',title=c['title'],source_ids=list(mapping.values()),claims=claims,card_copy=c['card_copy'])
 d=dict(candidate_id=nid,title=c['title'],section='deep_analysis',source_ids=it['source_ids'],entities=c['entities'],event=c['title'],decision='include',reason='飞书周四备选 Bot回执明确选择，按C001、C022顺序写入正文；C001是唯一指定主卡。',scores=c['scores'],card_designated=cid=='C001',human_selected=True,feishu_candidate_id=cid,feishu_receipt_id='2ff02addfe2f47d1a6c9789c6adb38c8')
 ITEMS.append(it);DEC.append(d);BODY[nid]=body
(OUT/'deep_card_choice.txt').write_text(next(it['title'] for it in ITEMS if it['candidate_id']=='D_C001')+'\n',encoding='utf-8')

# 对当期明确消费来源进行逐字证据回读，所有报告事实均须留有真源。
for it in ITEMS:
 for c in it['claims']:
  assert c['evidence'] in SRC[c['source_id']]['text'],(it['candidate_id'],c)

dump(B/'working_industry_items.json',ITEMS)
dump(B/'working_industry_decisions.json',DEC)
dump(B/'working_body.json',BODY)
print('industry drafted',len(ITEMS))
