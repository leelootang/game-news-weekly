import json,re
from pathlib import Path
P=Path(__file__).resolve().parent
S={r['source_id']:r for r in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))
ds={d['candidate_id']:d for d in D['decisions']}
# The absolute date at the end overrides the article's ambiguous opening 'today'.
ds['I049']['decision']='exclude'
ds['I049']['event_date']='2026-10-15'
ds['I049']['reason']='全文末段明确1.0于10月15日同步登陆PC与PS5；开头今日与采集16日不能覆盖绝对日期。单独保留10分评分，但实际发行在本期之前，不迟报为本期上线。'
ds['I129']['decision']='include'
ds['I129']['entities']=['Doors Studio','BagMaster Isekai','SayGames']
ds['I129']['event']='本期开发案例公开BagMaster Isekai3—5月收入与发行协作数据'
ds['I129']['reason']='E2市场/产品经营数据披露×R3背包构筑手游+M1=7。作为本期发表的开发案例采用，正文明确数据发生在3—5月，不写成10月上线/当月收入，也不按普通版本计分。'
ds['I308_TH']['scores']={'event':0,'relevance':3,'hook':1,'total':1}
ds['I308_TH']['reason']='8月已公开玩法的新作，当前内容为首测前常规预下载/招募，实际测试20日尚未发生；并无新定档变化证据，行业E0。日历另按预下载/测试规则独立审计。'
ds['I308_ST'].pop('pc_release_scope',None)
ds['I144']['pc_release_scope']={'classification':'ordinary_overseas_single_player','basis':'本次仅数字预购的单人战役抢先体验；全产品23日和DMZ20日尚未开放，不能用未来多人模式给本次单人发售抬R。','evidence':[{'source_id':'S0144','evidence':'If you preorder Modern Warfare 4 digitally, you\'ll get early access to the campaign starting October 16 and DMZ on October 20.'}]}
assert ds['I144']['pc_release_scope']['evidence'][0]['evidence'] in S['S0144']['text']
ds['I308_RI'].update(decision='merge',merge_into='I053',reason='同一10月16日59岗招聘事件，广州旧公司成立为背景，不能另拆一张招聘卡。')
ds['I032'].update(decision='include',entities=['隔离区'],event='国产联机丧尸游戏隔离区正式版定档11月6日',scores=dict(event=2,relevance=3,hook=1,total=7),reason='标题直接写国产，必须取R3；当前正式版定档为E2档期节点，不将未来日期写成已经上线。行业7分独立入选，日历同URL仍单源。')
ds['I310'].update(scores=dict(event=0,relevance=3,hook=1,total=1),reason='综合诉讼稿逐案拆分：商标引流、测试泄密、9月30日欧洲虚拟币执法分别留卡；不能整体合并为一个事件。')

def extra(cid,source,ent,event,e,rv,m,reason,proof=None,scope=None):
 if cid in ds:return
 d=dict(candidate_id=cid,section='industry_news',source_ids=source,entities=ent,event=event,event_date='2026-10-16',decision='exclude',reason=reason,scores=dict(event=e,relevance=rv,hook=m,total=e*rv+m),history_check=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None))
 if scope:
  d['pc_release_scope']=dict(classification=scope,basis='发行汇总中的普通PC产品，未证明国内/重点公司或实质移动迁移，不因RPG/策略/模拟品类提高相关性；有多人说明时另按实际赛道。',evidence=[dict(source_id=source[0],evidence=proof)])
 ds[cid]=d

extra('I306_BR',['S0306'],['Dean Hall','BRUTAL'],'Dean Hall公开免费的底层引擎框架BRUTAL',2,2,1,'游戏引擎能力公开是平台技术事件E2，存在工作室工具迁移R2，5分；不把免费框架披露当融资或大规模游戏新品。')
extra('I306_SC',['S0306'],['Steam'],'Steam首页提高个人日历入口并引入视频编解码能力',2,2,1,'一般平台功能更新，5分，不把常规客户端功能当重大渠道政策。')
extra('I306_WS',['S0306'],['Steam','HowToMarketAGame'],'愿望单通胀与销售预测能力研究',2,2,1,'PC发行数据具有迁移，5分；来源中是研究结论的短引，不拆成单独深度主题。')
extra('I306_VR',['S0306'],['Meta Quest'],'Quest畅销结构由免费社交沙盒产品占据',2,2,1,'VR用户结构对UGC具有迁移，但非中国移动市场直接数据，5分，不凭平台用户低龄化取R3。')
extra('I306_FAN',['S0306'],['GameDiscoverCo','Steam'],'Steam核心玩家跨设备调查',2,2,1,'PC优先样本跨端研究有明确移动迁移但不是中国移动大盘，行业5分；完整分析在深度分区成为一个主题。')
extra('I308_SM',['S0308'],['Flow Games','Smash Fest'],'10月16日累计下载突破2300万',1,3,1,'单款既有游戏累计下载里程碑为E1；6—7月收入为旧数据，没有实质新收入/市场份额变化，4分，不借融资热度取E3。')
extra('I310_TM',['S0310'],['恋与深空'],'电商商标引流侵权单案判赔',1,3,1,'具体商标侵权诉讼，非重大平台规则或资本结构变化，E1R3M1=4。')
extra('I310_GS',['S0310'],['米哈游','原神'],'线下测试泄密二审维持赔偿50万元',1,3,1,'单项商业秘密诉讼终审，国内主体R3但E1；不能用诉讼主体关注度取E3。')
extra('I310_EU',['S0310'],['Supercell','欧盟CPC'],'9月30日九款游戏虚拟货币销售执法行动',2,3,1,'Supercell固定重点R3，但原文明示9月30日，非本期新执法；保留7分候选并按旧日期排除。')
ds['I310_EU']['event_date']='2026-09-30'
# Every genuine Steam release in the composite gets its own assessment.
guide=S['S0126']['text']
blocks=re.split(r'\n(?=[^\n]+\n关键字：)',guide)
for k,block in enumerate(blocks):
 mm=re.search(r'(?:^|\n)([^\n]+)\n关键字：\s*([^\n]+)\n发行日期：\s*(2026/10/\d+)',block)
 if not mm:continue
 product,genre,dt=mm.groups()
 if product=='AMPANIC':continue
 proof=mm.group(0).strip()
 extra(f'I126_{k:02d}',['S0126'],[product],product+'列入Steam发行列表',3,1,1,'原清单为PC产品预排日期，未证明国内或重点主体；单人产品纯发售默认R1，其他合作/恐怖/动作产品未命中PVP、经营等直接优先赛道，4分。不得把中文支持当国产证据。',proof,'unknown')
for suffix,product,e,rv,m,reason in [
 ('SI','Sifu',2,2,1,'12日移动移植，5分且在本期之前。'),
 ('VC','Vampire Crawlers',2,3,1,'卡牌手游的12日老品跨平台，本期周汇总没有新事件，不重复为16日上线。'),
 ('9K','9 Kings',2,3,1,'策略手游的12日跨平台，7分但实际事件在本期之前。'),
 ('LC','Little Kitty, Big City',2,1,1,'单款海外冒险移植，弱迁移，3分。'),
 ('RE','Replaced',2,2,1,'12月8日未来Android老品移植；5分。'),
 ('DK','Dome Keeper',2,2,1,'单款生存采矿移动移植有迁移但无重点主体，5分。'),
 ('YG','Yes, Your Grace 2: Snowfall',2,3,1,'经营手游移植7分；汇总只有has launched，无绝对实际发生日，无法证明属于本期，候选保留，不按文章日代填。'),
 ('BS','Battle Spirits Teaching App',0,3,1,'10月7日教学应用，非本期新品游戏。'),
 ('PA','Pachislot Sengoku Collection 6',3,1,1,'13日海外地域性老虎机模拟器，4分且旧日期。'),
 ('WF','Walk The Frog',2,1,1,'14日旧作跨平台，弱迁移3分。')]:extra('I069_'+suffix,['S0069'],[product],product+'移动端/跨平台节点',e,rv,m,reason)

# Normalize product aliases and repeated collection days before node clustering.
A=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
nodes=A['nodes']
if not any(n['product']=='EarthX 2' for n in nodes):
 first=dict(next(n for n in nodes if n['source_ids']==['S0126']))
 first.update(candidate_id='R_EARTHX2',product='EarthX 2',event_date='2026-10-16',signal_type='new_game_launch',event='Steam抢先体验发行清单节点',event_type_score=3,source_ids=['S0126'],observed_signal_types=['new_game_launch'],observed_events=['2026/10/16 Steam EA清单'],publish_eligible=False,editorial_reason='全清单首个产品补召回；单份即将发行汇总，仍不满足独立多源。')
 nodes.append(first)
for n in nodes:
 p=n['product']
 if p=='越过山丘 over the hill':n['product']='越过山丘'
 if p in ['007 初露锋芒','叫魂','哈克小天地','隔离区']:n['event_date']='2026-10-16'
 if p=='雾锁王国':n.update(event_date='2026-10-15',window_eligible=False,publish_eligible=False,editorial_reason='正文末段明确10月15日，实际事件在报告窗口之前；覆盖开头今日的歧义。')
 if n['product']=='他予回声':
  n['candidate_id']='R_TH_PRE';n['event_date']='2026-10-18';n['signal_type']='new_game_preload';n['event']='已开放首次测试预下载，20日测试';n['event_type_score']=2;n['window_eligible']=True;n['observed_signal_types']=['new_game_preload'];n['observed_events']=['首次测试预下载'];n['editorial_reason']='当前预下载为允许召回的独立阶段，20日实际测试另超出窗口；来源仅一份，不满足多源。'
# Keep the current preload distinct from the future test stage by preserving another node.
for n in list(nodes):
 if n['product']=='他予回声' and n['signal_type']=='new_game_preload':
  future=dict(n);future.update(candidate_id='R_TH_TEST',event_date='2026-10-20',signal_type='new_game_test',event='首次寻星测试',event_type_score=3,window_eligible=False,editorial_reason='20日实际测试超过允许至19日的及时性窗口。');nodes.append(future);break
grouped={}
for n in nodes:
 key=(n['product'],n['event_date'])
 if key not in grouped:grouped[key]=dict(n);continue
 b=grouped[key]
 b['source_ids']=list(dict.fromkeys(b['source_ids']+n['source_ids']))
 b['observed_signal_types']=list(dict.fromkeys(b['observed_signal_types']+n['observed_signal_types']))
 b['observed_events']=list(dict.fromkeys(b['observed_events']+n['observed_events']))
 if n['publish_eligible']:b['publish_eligible']=True
 b['editorial_reason']+=' / '+n['editorial_reason']
 if n['event_type_score']>b['event_type_score']:b['event_type_score']=n['event_type_score'];b['signal_type']=n['signal_type'];b['event']=n['event']
nodes=list(grouped.values())
for n in nodes:
 ids=n['source_ids'];uni={}
 for x in ids:
  rr=S[x];uni.setdefault(rr['source_key'] if rr['source_key']=='youxichaguan' else rr['url'],rr['sha1'])
 n['industry_ids']=[x for x in ids if S[x]['section']=='industry_news'];n['release_ids']=[x for x in ids if S[x]['section']=='release_calendar']
 n['appearance_count']=len(uni);n['appearance_score']=min(len(uni),3);n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus'];n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus'];n['source_fingerprints']=list(uni.values());n['multi_source_eligible']=len(uni)>=2
 dt=n['event_date'];sg=n['signal_type'];n['window_scope']='report_window' if '2026-10-16'<=dt<='2026-10-18' else 'next_day_lookahead' if dt=='2026-10-19' else 'future_announcement' if sg in ['new_game_schedule','new_game_first_reveal'] else 'outside'
 n['first_seen_order']=min(int(x[1:]) for x in ids)
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
A['nodes']=nodes;A['editorial_scan']['corrected_nodes']=len(nodes)
(P/'release_calendar_audit.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Remove old synced release decisions; the canonical sync is run next.
D['decisions']=[d for d in ds.values() if d['section']!='release_calendar']
(P/'selection_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
candidate_text=(P/'event_candidates.md').read_text(encoding='utf-8')
for d in D['decisions']:
 if f"## {d['candidate_id']} -" not in candidate_text:
  candidate_text+=f"\n## {d['candidate_id']} - {d['event']}\n- section: {d['section']}\n- source_ids: {', '.join(d['source_ids'])}\n- entities: {' / '.join(d['entities'])}\n- event_date: {d['event_date']}\n- facts: {d['event']}\n- notes: {d['reason']}\n"
candidate_text+='\n## 全文复核修正\n- S0049末段10月15日优先于开头今日；行业排除、日历日期更正。\n- S0129为本期开发案例披露，保留3—5月数据期间，非10月新上线。\n- 全部产品日历规范化节点以release_calendar_audit.json为准，重复采集与同产品同日已聚类。\n'
(P/'event_candidates.md').write_text(candidate_text,encoding='utf-8')
print('refined industry candidates',sum(d['section']=='industry_news' for d in D['decisions']),'calendar',len(nodes))
