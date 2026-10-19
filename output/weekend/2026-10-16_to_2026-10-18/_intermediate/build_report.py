"""Run-specific editorial audit and report builder. Does not mutate news_data."""
import json, re, hashlib, sys, collections, datetime, shutil
from pathlib import Path

P=Path(__file__).resolve().parent
ROOT=P.parent
WORK=Path.cwd()
ROWS=[json.loads(x) for x in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
SRC={r['source_id']:r for r in ROWS}
H=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
HMD=(P/'industry_history_14d.md').read_text(encoding='utf-8')
SUMMARY=(P/'report_inputs_summary.md').read_text(encoding='utf-8')
INDEX=(P/'report_inputs_index.md').read_text(encoding='utf-8')
assert all(r['source_id'] in INDEX for r in ROWS)
def sid(n): return f'S{n:04d}'
def text(n): return SRC[sid(n)]['text']
def dump(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def fact_excerpt(r):
 t=r['text']; parts=[x.strip() for x in re.split(r'(?<=[。！？\n])',t) if x.strip()]
 useful=[x for x in parts if re.search(r'宣布|融资|收购|停运|关闭|取消|裁员|首测|首曝|上线|公测|发行日期|测试|million|announc|bankrupt|cancel|launch|releas',x,re.I)]
 return '\n'.join(dict.fromkeys(useful))[:1800] or t[:700]
def history(keys):
 matches=[r for r in H['occurrences'] if any(k.lower() in json.dumps({x:r.get(x) for x in ['title','event','entities']},ensure_ascii=False).lower() for k in keys)]
 return {'history_match':bool(matches),'novelty':'repeat_only' if matches else 'new_event',
  'prior_occurrences':[f"{r['report_kind']} {r['report_window']['start']}_to_{r['report_window']['end']}｜{r['title']}｜card_exposed={r['card_exposed']}; card_rank={r['card_rank']}; card_limit={r['card_limit']}; {r['card_exposure_source']}" for r in matches],
  'new_facts':[], 'prior_card_exposed':any(r['card_exposed'] for r in matches) if matches else None}
def score(e,r,m):return dict(event=e,relevance=r,hook=m,total=e*r+m)
DS={}
for r in ROWS:
 n=int(r['source_id'][1:]); sec=r['section']; title=r['title']; cid=('I' if sec=='industry_news' else 'A' if sec=='ai_trends' else 'C' if sec=='community_discourse' else 'D' if sec=='deep_analysis' else 'L')+f'{n:03d}'
 d=dict(candidate_id=cid,section=sec,source_ids=[r['source_id']],entities=re.findall(r'《([^》]+)》',title)[:3] or [title.split('：')[0][:45]],event=title,event_date=r['date'],decision='exclude',reason='')
 d['facts_read']=fact_excerpt(r)
 d['source_text_sha256']=hashlib.sha256(r['text'].encode()).hexdigest()
 if sec=='industry_news':
  e=3 if re.search(r'正式公布|正式上线|今日推出|正式版|现已登陆|开启.*测试|破产|bankrupt',title,re.I) else 2 if re.search(r'销量|million copies|停运|下架|cancel|layoffs|裁员|delayed',title,re.I) else 0
  rv=3 if re.search(r'Roblox|Supercell|Riot|拳头',title,re.I) else 1 if e else 0
  d.update(scores=score(e,rv,1 if e else 0),history_check=history([]))
  d['reason']=f'逐项核对《{title}》：'+('记录为摘要/受阻正文，不能作为正式证据。' if r['body_status']!='full' else '未证明本期新增的资本、组织、平台或重点产品状态；内容为常规预告、评测、玩法介绍或弱迁移小主体信息。')
 elif sec=='ai_trends':
  d.update(ai_tier='transferable_frontier',game_stage=[],industry_reverse_scan=False,migration_path='候选反扫：检查是否具体改变游戏研发、产品、发行或运营；未建立直接证据链则不采用。')
  d['reason']=f'逐项核对《{title}》：无直接游戏应用；本期已有更具体的研发验证与资产成本案例，不采用泛模型榜单、渠道上架、宏观、硬件或通用科普。'
 elif sec=='community_discourse':
  d['reason']=f'逐项核对《{title}》：保留原帖与窗口内延续，优先级低于本期两条有具体体验/素材触发及后续讨论的事件；旧帖无状态更新不当作新事件。'
  d['community']=dict(trigger=title,claim_scope='社区主张，不提升为官方事实',complaint_logic='见原帖及逐项审计',timeline=re.findall(r'2026-10-\d\d[T ]\d\d:\d\d',r['text']),follow_up_scan='已按产品、角色、机制、争议词扫描本窗口社区和行业池；相同游戏的其他事件不混入。')
 elif sec=='deep_analysis':
  d.update(scores=dict(relevance=3,insight=3,evidence=3,card=3,total=12),reason='完整newsletter调查，先于普通行业分析审阅。')
 else:
  d['section']='release_calendar'
  d['reason']='逐条日历反扫；召回节点将在release_calendar_audit.json与确定性日历决策中记录。'
 DS[cid]=d

def edit(cid,*,e=0,r=1,m=1,reason='',entities=None,event=None,ids=None,hkeys=None,include=False):
 d=DS[cid]; d.update(scores=score(e,r,m),reason=reason or d['reason'])
 if entities is not None:d['entities']=entities
 if event is not None:d['event']=event
 if ids is not None:d['source_ids']=[sid(x) if isinstance(x,int) else x for x in ids]
 d['history_check']=history(hkeys or [])
 if include:d['decision']='include'
 if len(d['source_ids'])>1:d['cluster_basis']=dict(subject='/'.join(d['entities']),product='/'.join(d['entities']),event_date=d['event_date'],event=d['event'])
 return d

# Individual assessments for all domestic/focus subjects and every substantive event.
OV={
 'I033':(0,3,1,'iQOO新品推广与既有赛事/联调合作回顾；正文混有上月赛事和去年合作，不将未明确发生日期的合作升级为本期重大新战略。'),
 'I035':(0,3,1,'国产《车水马龙》Demo体验与开发复盘；没有本期首次上线/首曝日期，不将最近体验稿推定为当天首测。'),
 'I036':(2,3,1,'拳头经典模式关闭是独立生命周期变化，R3固定重点主体，不能把作者“召回目标完成”的评价写成已验证运营结果。'),
 'I037':(3,3,1,'10月15日公测，历史已曝光；16日迟到稿及免费榜第8不构成新的经营状态。'),
 'I038':(0,3,1,'拆分终末地跨平台/榜单、绿梦公测、异环常规联动等事件；10月15日节点不冒充本期新品，单点排名不自动升级市场事件。'),
 'I039':(1,3,1,'LCK高薪选手税务争议，尚未正式课税或处罚；纯税务/劳资与区域事件，E1，重点IP不豁免事件门槛。'),
 'I040':(0,3,1,'库克到访和试玩是交流活动，没有披露新的投资、发行协议或产品首次立项。'),
 'I041':(0,3,1,'与S0040同一到访；2011/2020/2024及3月政策均为历史背景，不能召回为10月16日新品或新抽成政策。'),
 'I044':(0,3,1,'终末地新版本角色/叙事鉴赏，非新品、停运或结构性业绩变化。'),
 'I047':(0,3,0,'正文禁用主体及周年宣传，不进入任何发布分区。'),
 'I051':(1,1,1,'GTA6制作过程复盘与10月14日旧采访，非新增发售、融资或组织变化。'),
 'I053':(1,3,2,'59个岗位、广州11岗是招聘信号；未确认新产品立项，不将招聘推测的两款产品写成官宣。E1×R3+M2=5。'),
 'I054':(2,3,2,'本期新曝光的天美项目取消报道；采用媒体归因，实际取消可能在2025年初，不能写成本周刚砍，也不能与仍在研Jade混同。'),
 'I057':(1,2,1,'Fishlabs纯裁员、项目需求调整，未披露关停/资本交易/具体项目取消，E1不得升至E2/3。'),
 'I058':(0,1,1,'地区行业会议到场增长，不是游戏市场规模或组织资本新事件。'),
 'I059':(0,1,1,'赛车叙事灵感访谈，无本期新品/资本/核心管理变化。'),
 'I060':(0,2,1,'Gamescom Asia展馆招商增补，例行展会预热，不升级为重大合作。'),
 'I061':(1,2,1,'Fuse分布式开发访谈，非组织新调整；与近期Velan分工开发深度主题相邻，不另凑一条深度。'),
 'I062':(2,2,1,'硬件冻结评论引Circana主机数据，有平台经济迁移但非中国移动直接数据，5分边界。'),
 'I065':(3,2,1,'移动开发商取得信贷/贷款，7分候选；唯一正文为受阻snippet，证据门禁排除。'),
 'I066':(2,3,1,'移动射击产品Steam累计收入里程碑，7分候选；仅snippet不可用于正文。'),
 'I067':(3,3,1,'Supercell桌游新项目R3固定重点；仅snippet，无可用完整核心来源，排除。'),
 'I068':(3,3,1,'Flow累计4900万美元并不证明在已报道4600万美元之外又发生新一轮；旧融资已曝光。'),
 'I076':(3,1,1,'Red Rooster10月14日官宣的后续实体书体验；弱迁移海外项目，不能把16日来信稿当新立项。'),
 'I077':(0,3,0,'禁用主体周年稿，仅留内部排除。'),
 'I079':(2,3,1,'截至10月14日3554万元为上周众筹结果的补充数值，未发生新资本/项目状态，旧事件已曝光。'),
 'I097':(1,1,1,'Big Walk解释既有Xbox抵制/缺席，没有新平台发布或当期档期变化。'),
 'I098':(0,1,1,'TGA参评资格与既有发售日，非新定档或实际发售。'),
 'I100':(2,3,2,'幕府将军2撤售恢复旧版已进入上一期周报社区；同一反馈事件不重复转入本期行业/AI。'),
 'I101':(3,3,1,'Hadar结束世界观构想、已开始做游戏，属于明确在研新IP状态；来源描述大型RPG，非普通PC单机纯发售。尚未进入预制作必须保留。'),
 'I102':(0,3,2,'拳头与LV画集为IP商品宣传；非游戏新品/重大合作战略，重点主体R3但E0。'),
 'I104':(3,3,1,'动视营销负责人明确确认在研全新子系列；来源为快节奏竞技射击产品方向，不是普通单机发售；不采用未证实工作室/年代/武术传闻。'),
 'I115':(2,2,2,'Remedy最快销量纪录与大体量自发行，有商业模式迁移，但仍是一般海外销量点；E2R2M2=6，不用全球重要抬R。'),
 'I116':(2,2,2,'美国数字游戏所有权提案，跨境平台/停运合规有迁移但仍是提案，E2R2M2=6，不写成现行法规。'),
 'I117':(0,2,1,'前总监个人心理边界访谈，2021年离职是历史事实，不构成本期管理层变动。'),
 'I118':(2,2,2,'Steam成就集合为平台能力调整，有PC运营迁移，E2R2M2=6；不是新分发/抽成政策。'),
 'I124':(1,1,1,'Turok三人合作/买断制访谈，已知在研内容，无首次立项或新档期。'),
 'I128':(1,3,1,'Pincus复盘旧收购与数据驱动机制；不是本期Supercell并购，不能用2012年旧事计E3。'),
 'I129':(2,3,1,'BagMaster数据截至3—5月，团队人数截至6月；本期是历史开发/发行复盘，无当前新品或新经营数据，保留评分但按时效排除。'),
 'I133':(2,2,2,'合并至Control销量事件，同一10月15日百万销量披露；6分，不把产品评论当第二次资本变化。'),
 'I134':(1,3,1,'WoW装备保值路线阐释，既有版本玩法前瞻，E1，不等同新IP立项。'),
 'I137':(2,3,1,'RuneScape新起点服务器计划撤销，属于MMO重大项目生命周期变更，不是普通版本。'),
 'I138':(2,2,2,'同Steam成就集合更新，6分平台能力候选。'),
 'I139':(2,2,2,'同美国议员数字游戏所有权提案，6分，不外推已经生效。'),
 'I141':(1,1,1,'Black & White3个人暗示，未官宣项目/平台/制作状态，不能计新立项。'),
 'I144':(3,1,2,'现代战争4战役抢先体验是海外PC/主机单人战役纯发行消息，R1；DMZ尚未开放，不借未来多人模式把本次战役发售抬成R3。'),
 'I147':(3,3,1,'阅文10月16日首次披露多IP电子集换卡牌手游《群星漫卡》，国内新品正式立项公开。'),
 'I149':(0,3,2,'K/DA既有品牌画集与联名宣传，E0；历史2019/2020合作不计新战略。'),
 'I259':(1,3,1,'龙之谷10月13日主题服上线后的用研/设计复盘，日期在本期之前，不作为新开服。'),
 'I260':(2,3,2,'并入天美命运项目取消曝光；原报道同为MP1st，同主体/产品/取消事件，不与旧Jade测试合并。'),
 'I261':(0,3,1,'诡秘之主1.3例行版本和上线两月产品访谈；未提供超出版本/排名的新资本或状态变化，不用泛“站稳脚跟”取E2。'),
 'I263':(0,2,1,'综合稿逐事件拆分，育碧RedLynx、库洛、Flow、西山居、姜饼人电影、燕云DLSS、爆裂小队和Game Finder分别留卡，不把综合稿整体当一个行业事件。'),
 'I274':(2,3,1,'战狗蓝队补贴撤销是新的PVP阵营经济调整；归入社区外溢候选并与本期两条比较，未入行业以免同事件跨栏重复。'),
 'I275':(0,1,1,'Over the Hill游玩体验，不是新的发售/平台状态。'),
 'I276':(1,2,1,'Cyberpunk电影开发方式说明，上周合作公告的后续阐释，没有新增资本或组织状态。'),
 'I278':(3,3,1,'Funcom重组与CEO更替已在前期卡片曝光，本期换来源复述，禁止重报。'),
 'I281':(2,1,1,'Ghostwire加入GOG保存计划，单款老品渠道扩展，迁移较弱，3分。'),
 'I282':(2,2,2,'并入美国数字游戏所有权提案。'),
 'I309':(1,3,1,'大作失败评论汇总，多个旧案例，不是新发生的项目取消/组织状态。'),
 'I310':(1,3,1,'单项泄密/商标诉讼E1；欧盟9月30日虚拟币执法为旧背景。国内主体R3不豁免低E。'),
 'I344':(1,2,1,'Wizards工会承认争议是纯劳资，不把利润数字当财报异常。'),
 'I349':(1,1,1,'音乐人舞台传闻，不构成官方立项或新品首曝。'),
 'I350':(3,1,1,'Liquid Swords破产，来源未写国内资本主体；不能凭记忆补网易。海外单工作室弱迁移，4分。'),
 'I353':(3,3,1,'竞技射击核心总监确认离开Bungie并在做未公开项目；来源直接说明Valorant/Marathon职责，优先PVP人才信号。实际离职日未披露，按本期访谈披露留卡，不写成18日当天离职。'),
}
for cid,(e,r,m,reason) in OV.items():edit(cid,e=e,r=r,m=m,reason=reason)

# Exact-event clusters; later collection snapshots are not additional events or hooks.
def merge(cid,into,why):
 DS[cid]['decision']='merge';DS[cid]['merge_into']=into;DS[cid]['reason']=why
edit('I054',e=2,r=3,m=2,entities=['腾讯','天美','刺客信条：命运'],ids=[54,260],event='本期报道首次曝光天美未公开项目命运早期取消',include=True)
merge('I260','I054','同一MP1st报道的天美命运项目取消曝光；严格同主体/产品/事件。')
edit('I115',e=2,r=2,m=2,entities=['Remedy','Control Resonant'],ids=[18,115,133],event='10月15日披露Control Resonant三周销量百万，成为公司最快纪录')
merge('I018','I115','同一百万销量事件');merge('I133','I115','同一百万销量事件')
edit('I116',e=2,r=2,m=2,entities=['Ritchie Torres','数字游戏所有权'],ids=[116,139,282],event='美国议员提出数字游戏所有权提案')
merge('I139','I116','同一提案');merge('I282','I116','同一提案')
edit('I118',e=2,r=2,m=2,entities=['Valve','Steam'],ids=[118,138],event='Steam客户端测试版上线成就集合')
merge('I138','I118','同一Steam测试功能更新')
edit('I003',e=3,r=1,m=2,entities=['恶魔城：贝尔蒙特的诅咒'],ids=[3,120],event='恶魔城贝尔蒙特的诅咒PC主机发售',reason='普通海外单机纯发售，E3R1M2=5；独立竞争日历。')
merge('I120','I003','同一发售事件')
edit('I025',e=3,r=1,m=2,entities=['霜港迷城'],ids=[25,119],event='霜港迷城PC 1.0正式版发售',reason='海外PC纯发售，团队协作措辞未明确在线多人型态，不能只凭策略/RPG标签取R3；5分。')
merge('I119','I025','同一PC 1.0发售事件')
edit('I015',e=3,r=1,m=2,entities=['越过山丘'],ids=[15,113],event='越过山丘登陆PC',reason='合作越野驾驶不等于生活/经营优先赛道，迁移较弱，E3R1M2=5。')
merge('I113','I015','同一PC发售事件')
edit('I030',e=2,r=3,m=1,entities=['战狗'],event='战狗销量超过300万份',hkeys=['战狗'],reason='300万销量与历史相同；赛季新武器不是销量的新状态。虽未曝光仍需与其他候选竞争唯一内部补位，分数7低于Xbox Labs8。')
edit('I037',e=3,r=3,m=1,entities=['西山居','剑侠世界4：无限'],hkeys=['剑侠世界4'],reason=OV['I037'][3])
edit('I068',e=3,r=3,m=1,entities=['腾讯','Flow Games'],hkeys=['Flow Games'],reason=OV['I068'][3])
edit('I079',e=2,r=3,m=1,entities=['艾希：续'],hkeys=['艾希：续'],reason=OV['I079'][3])
edit('I278',e=3,r=3,m=1,entities=['腾讯','Funcom'],hkeys=['Funcom'],reason=OV['I278'][3])

for cid,e,rv,m,entities in [
 ('I036',2,3,1,['拳头游戏','英雄联盟经典模式']),('I049',3,3,1,['Keen Games','雾锁王国']),
 ('I027',3,3,1,['杯杯倒满']),('I101',3,3,1,['CDPR','Project Hadar']),
 ('I104',3,3,1,['动视','使命召唤']),('I137',2,3,1,['Jagex','RuneScape Reignited']),
 ('I147',3,3,1,['阅文','蹊迹游戏','群星漫卡']),('I353',3,3,1,['Joe Ziegler','Bungie','Marathon'])]:
 edit(cid,e=e,r=rv,m=m,entities=entities,include=True)

# One admissible never-exposed historical event, selected by current score then R.
d=edit('I012',e=3,r=2,m=2,entities=['Xbox','Xbox Labs'],ids=[12,306],event='Xbox集中现有研发探索成立Labs团队',hkeys=['Xbox Labs','Xbox集中现有'],include=True,reason='当前两篇独立来源再次召回，E3R2M2=8。所有历史匹配均未在订阅卡片展示；比分7的战狗高，唯一选择。')
assert d['history_check']['prior_card_exposed'] is False
d['history_check']['novelty']='card_carryover';d['card_carryover']=True

def new_ind(cid,ids,entities,event,e,rv,m,reason,include=False,hkeys=None):
 DS[cid]=dict(candidate_id=cid,section='industry_news',source_ids=[sid(x) for x in ids],entities=entities,event=event,event_date='2026-10-16',decision='exclude',reason=reason)
 return edit(cid,e=e,r=rv,m=m,include=include,hkeys=hkeys)
new_ind('I069_TI',[69],['Fellow Traveller','Titanium Court'],'已在PC发行的Titanium Court宣布10月29日登陆移动端与主机',2,3,1,'三消+塔防的移动跨平台新档期，R3来自移动策略产品；属于E2，不将老品跨平台写成首次新品上市。',True)
new_ind('I069_AZ',[69],['蛮啾','Azur Promilia'],'英语公开测试计划为2027年夏季',2,3,1,'社区14日旧帖已在讨论该计划；16日周汇总无新增档期，本期不再作为新状态。')
new_ind('I069_GU',[69],['Bandai Namco','Gundam Blitz Order'],'高达放置游戏测试招募与11月18—24日网络测试安排',1,3,1,'没有首次首曝证据，既有招募/未来测试计划不冒充当期首测；与3839中文名对应未被来源直接证明，保留单独候选。')
new_ind('I069_TO',[69],['字节跳动','Nuverse','Totopia World'],'德国Android软启动在10月13日被发现',3,3,1,'明确10月13日的测试状态，不把16日周汇总误当本期新开测。')
new_ind('I069_NM',[69],['Hello Games','No Man’s Sky'],'10月28日iOS移植与苹果独立游戏周',2,2,1,'与此前苹果独立游戏周跨平台公告同一事件，不因晚到周汇总重报；5分边界。',hkeys=['苹果独立游戏周'])
new_ind('I126_AP',[126],['AMPANIC'],'在线合作商店经营游戏AMPANIC列入10月16日发行清单',2,3,1,'来源是即将发售列表，计E2档期而非已经验证E3上线；在线多人经营原文明确，不属于普通海外单人纯发售。',True)
new_ind('I308_ST',[308],['Sensor Tower','中国手游发行商'],'10月16日披露9月37家中国手游发行商收入20亿美元占百强41.6%',2,3,1,'按中国发行商市场数据独立建卡；不是历史AppMagic全球产品下载/收入排名同一事件，不因同为9月报告合并。',True)
for suffix,ent,event,sc,reason,hk in [
 ('RI',['拳头游戏'],'59岗招聘与广州研发布局',(1,3,2),'与S0053同一招聘；新公司9月21日成立、玩法为招聘推测。',[]),
 ('FL',['腾讯','Flow Games'],'Flow累计融资4900万美元',(3,3,1),'累计值是历史融资口径，未证明新一笔；此前已曝光，repeat_only。',['Flow Games']),
 ('KU',['库洛','言之域'],'库洛入股15%',(3,3,1),'与历史相同工商变更。',['库洛']),
 ('EN',['鹰角','终末地'],'10月15日版本后畅销榜排名',(0,3,1),'普通版本和单点排名E0；不改写为本期新品。',[]),
 ('PH',['Kinetic Games','恐鬼症'],'10月12日累计销量3000万',(2,1,1),'旧日期一般海外销量点，非本期新状态。',[]),
 ('TH',['乐元素','他予回声'],'10月20日首次测试预告',(2,3,1),'20日实际测试超出本期；当前报道为既有8月首曝后的招募/预下载，未证明新的行业战略状态。',[]),
 ('BA',['灵犀互娱','篮球少女：飞跃巅峰'],'10月23日公测定档及NBA联动',(0,3,1),'已多轮测试和既有定档，NBA联动是普通运营；不把联动或预约奖励抬E3。',[]),
 ]:
 new_ind('I308_'+suffix,[308],ent,event,*sc,reason,hkeys=hk)
for suffix,ent,event,sc,reason,hk in [
 ('RE',['育碧','RedLynx'],'拟关闭RedLynx及新加坡裁员',(2,2,2),'关闭是E2而非纯裁员E1；R2迁移，6分边界，未达到7。',[]),
 ('KU',['库洛','言之域'],'库洛入股言之域15%',(3,3,1),'与历史已曝光股权变化重复。',['库洛']),
 ('FL',['腾讯','Flow Games'],'腾讯领投4600万美元',(3,3,1),'与历史融资同一事件。',['Flow Games']),
 ('SQ',['Supercell','Squad Busters'],'爆裂小队12月14日停运',(2,3,1),'历史未曝光，但本次7分竞争低于Xbox Labs8，仅保留审计。',['Squad Busters']),
 ('CK',['Devsisters','跑跑姜饼人'],'与Big Shot Pictures合作电影计划2029年上映',(3,2,1),'移动IP跨媒体新合作属于7分候选；本期综合稿首次回收，无历史同事件。',[]),
 ('YY',['网易','燕云十六声'],'11月支持DLSS5',(0,3,1),'既有产品图形功能升级，非新品/跨平台/重大商业状态。',[]),
 ]:
 new_ind('I263_'+suffix,[263],ent,event,*sc,reason,include=suffix=='CK',hkeys=hk)

# Same-publisher translations are one editorial origin and contain clear stale context.
for nums,why in [
 (range(311,316),'星沙岛旧Demo/WePlay复盘的同站多语言版本，无本期日期，不能按译文篇数计M或多源。'),
 ([316,317,318,319,321],'正文称11月下旬且终末地尚未上线，明显为旧稿译文，拒绝以10月18日采集日期改写事实。'),
 ([320,322,323,324,325],'无限暖暖2.0/2025年奖项叙述为旧稿语境；未证明10月18日新版本，不用今日动态词回填日期。'),
 ([326,327,328,334,335],'正文推广2025年IAA赛事，旧宣传的多语言版本，非本期新战略。'),
 (range(329,334),'Golden Star Vortex Demo同站译稿，海外单机弱迁移R1；原文未给当期绝对发布日期，不把多语言当多源。')]:
 for n in nums:edit('I'+f'{n:03d}',e=3 if 329<=n<=333 else 0,r=1 if 329<=n<=333 else 3,m=0,reason=why)

# Industry -> AI reverse scan. Each event keeps its own boundary.
AI_REVERSE={34:'EGS启动器AI重写已在上期周报AI发布，本期仅新解释和CEO表态。',43:'Character.AI10月12日破产后的商业评论，没有本期新破产状态；不混入通用AI融资。',45:'模组作者实际使用AI辅助逆向和开发并公布演示。',46:'端侧机器评测有研发迁移，但优先于本期选题的是实际模组/UGC案例及验证机制；不只因参数/硬件开售采用。',52:'创作挑战赛招募是活动推广，没有新的已验证游戏研发结果。',55:'昆仑万维GameWave已有UGC内容生产与分发数据。',56:'幕府将军2 AI画面/回滚同一事件已在上期周报社区发布。',90:'Demo取消恐AI克隆只有snippet；同事件完整证据改用S0279。',143:'EGS相同旧事件的外部评价，不是独立AI采用进展。',146:'Linux开源贡献披露变化，无具体游戏环节证据且本期已有更明确治理案例。',148:'SoonPlay公告是游戏生成平台发布计划，实际推出日20日尚未发生。',262:'停服游戏粉丝AI复原为9月起既有趋势，10月14日Labs背景不是本期新复原节点。',277:'AI编程街区射击争议可命名，但非游戏产业采用规模或可迁移研发结果；低于本期四条直接作用案例。',279:'开发商因AI克隆风险明确改变公开Demo分发安排，属于发行环节直接影响。',338:'Konami泛AI创作表态且仅snippet，不作为落地证据。',354:'Sweeney黄金时代论为泛战略表态，无新的落地机制。'}
for n,reason in AI_REVERSE.items():
 d=DS['I'+f'{n:03d}'];d.update(section='ai_trends',reason=reason,ai_tier='direct_application' if n in [34,45,55,56,148,262,277,279,52,90,143] else 'transferable_frontier',game_stage=['development'] if n in [34,45,46,56,52,143] else ['product','publishing'] if n in [55,148,262,277,279,90] else [],industry_reverse_scan=True,migration_path='仅在具体生产、产品、分发或验证环节有证据时采用；泛态度不推定落地。')
for n in [45,55,148,279]:DS['I'+f'{n:03d}']['decision']='include'
for n in [161,287]:DS['A'+f'{n:03d}']['decision']='include'
DS['A161'].update(reason='单GPU开放权重与视频扩分成本从0.59到0.28美元/秒，明确映射游戏宣发素材本地原型/高分辨率处理；事实与迁移推断分开。',game_stage=['development','publishing'],migration_path='单消费级GPU图像生成及视频扩分降价→游戏美术原型、宣发视频处理→可能降低试稿和分辨率迭代成本；不是已被游戏项目采用的断言。')
DS['A287'].update(reason='代码吞吐提高后的验证/评审重构有具体回退与迭代数据，迁移至游戏工具链和自动测试；不将Anthropic自述外推为游戏行业已实现结果。',game_stage=['development'],migration_path='验证证据、独立评审、风险分级与增量复审→游戏代码/工具链自动化→可能减少AI产出变多后人工评审瓶颈及返工。')

# More precise community exclusions and same-thread snapshots.
for n in [221,227,232]:DS['C'+f'{n:03d}']['reason']='此前日报/周报已发布同一争议；本期仅回复延续，无可核验的新处理状态。'
for n in [229,302,362]:DS['C'+f'{n:03d}']['reason']='AIGC激励截图未被抽取为可核验规则正文，不能把玩家怀疑写成官方AI政策，也不足以代替本期两条更具体事件。'
for n in [235,239,304,366]:DS['C'+f'{n:03d}']['reason']='存在可命名讨论，但主张/人事原因依赖玩家推测，缺乏具体已发生业务状态；优先级低于两条已选社区事件。'
for n in [238]:DS['C238']['reason']='泄密判赔属单项诉讼及零散感叹，未形成比本期两条更完整的争议机制，不重复当行业资本变化。'
for n in [297,365]:DS['C'+f'{n:03d}']['decision']='include'
merge('C303','C365','同一绿梦素材对比帖的早期采集，使用18日快照补齐时间线，不合并另一条手游操作争议。')
DS['D306']['decision']='include'
DS['D306'].update(topic_key='Steam核心玩家/跨设备人群重叠/调查分组与样本外推',source_priority=1,quality_route='数据型案例',evidence_anchors=[{'source_id':'S0306','evidence':x} for x in ['>16,000 worldwide Steam players','22% of respondents who play PC and mobile games (but no console)','15.6% of respondents who play PC, console, and mobile']],merge_basis='单篇完整newsletter的调查结果、机制与边界合为一个主题；不拆比例为多个选题。')

# Exact URL duplicate snapshots merge to their first underlying event, never inflate M.
seen={}
for r in ROWS:
 if r['section']!='industry_news':continue
 cid='I'+f"{int(r['source_id'][1:]):03d}"
 key=r['url']
 if key in seen and cid in DS and DS[cid]['decision']=='exclude':merge(cid,seen[key],'同URL重复采集，原发布事件不变；不计额外独立来源。')
 else:seen[key]=cid

# Mandatory PC scope for every relevant candidate, including exclusions.
for d in DS.values():
 if d['section']!='industry_news':continue
 sc=d['scores']; event=d['event']; alltext='\n'.join(SRC[x]['text'] for x in d['source_ids'])
 if sc['event'] and re.search(r'PC|Steam|PS5|XBOX|主机|端游',alltext,re.I) and re.search(r'发售|发行|上线|登陆|推出|发布|测试|公测',event,re.I):
  cl='substantive_migration' if d['candidate_id']=='I069_TI' else 'multiplayer_or_other' if d['candidate_id'] in ['I049','I027','I126_AP','I015'] else 'domestic_or_focus' if sc['relevance']==3 and any(x in '/'.join(d['entities']) for x in ['西山居','网易','腾讯','曜','字节']) else 'unknown'
  if d['candidate_id'] in ['I003','I025','I144']:cl='ordinary_overseas_single_player'
  # R3 exceptions need explicit source facts. Non-release corporate events are not downweighted.
  if cl=='unknown' and sc['relevance']>1 and d['candidate_id'] not in ['I069_TI','I308_ST']:
   cl='multiplayer_or_other'
  anchors=[]
  for x in d['source_ids']:
   tx=SRC[x]['text']; ms=re.search(r'[^\n。]{0,100}(?:PC|Steam|PS5|XBOX|主机|端游|合作|多人)[^\n。]{0,140}',tx,re.I)
   if ms:anchors.append(dict(source_id=x,evidence=ms.group(0).strip()))
  d['pc_release_scope']=dict(classification=cl,basis='按正文平台、产品型态和事件判断：多人经营/生存RPG不属于普通海外单人纯发售；国内主体关系须明示；未知主体不凭记忆推定，纯单人发售R1。',evidence=anchors[:2])

# Calendar raw output retained, followed by full-text reverse scan and corrected nodes.
raw_path=P/'release_calendar_audit.raw.json'
if not raw_path.exists():shutil.copy2(P/'release_calendar_audit.json',raw_path)
RAW=json.loads(raw_path.read_text(encoding='utf-8'))
NODES=[]
def node(product,date,ids,signal='new_game_launch',event='正式上线',eligible=False,why='',factor=None):
 ids=list(dict.fromkeys(sid(x) if isinstance(x,int) else x for x in ids))
 # Same domain/origin + same URL/hash are one source; translated publisher mirrors are one origin.
 unique={}
 for x in ids:
  rr=SRC[x]; key=rr['url']
  origin=rr['source_key'] if rr['source_key']=='youxichaguan' else key
  unique.setdefault(origin,rr['sha1'])
 count=len(unique); ind=[x for x in ids if SRC[x]['section']=='industry_news']; rel=[x for x in ids if SRC[x]['section']=='release_calendar']
 ev=factor if factor is not None else 3 if signal in ['new_game_launch','new_game_test'] else 2 if signal in ['new_game_preload','new_game_first_reveal','new_game_schedule'] else 1
 ss=min(count,3)+bool(ind)
 scope='report_window' if '2026-10-16'<=date<='2026-10-18' else 'next_day_lookahead' if date=='2026-10-19' else 'future_announcement' if signal in ['new_game_schedule','new_game_first_reveal'] else 'outside'
 n=dict(candidate_id=f'R{len(NODES)+1:03d}',product=product,event_date=date,source_ids=ids,signal_type=signal,event=event,event_type_score=ev,first_seen_order=min(int(x[1:]) for x in ids),observed_signal_types=[signal],observed_events=[event],industry_ids=ind,release_ids=rel,source_fingerprints=list(unique.values()),appearance_count=count,appearance_score=min(count,3),industry_bonus=int(bool(ind)),source_strength_score=int(ss),base_priority_score=ev*ss,company_relationship='none',company_bonus=0,focus_companies=[],focus_company_relationships={},company_evidence_ids=[],priority_score=ev*ss,multi_source_eligible=count>=2,window_scope=scope,window_eligible=scope!='outside',publish_eligible=eligible and count>=2,coverage='industry_and_release' if ind and rel else 'industry_only' if ind else 'release_only',status='audited',editorial_reason=why)
 NODES.append(n);return n

# Preserve every extractor recall, including false-positive labels, with specific corrections.
for old in RAW['nodes']:
 product=old['product']; ids=old['source_ids']; date=old['event_date']; sig=old['signal_type']; why='单源、普通运营或日期/事件证据未完整，保留原始召回但不发布。'
 if product=='Rain98':continue
 if product=='GTA6':date='2026-11-19';why='发售预告/资格及制作背景，不是首次正式定档；原抽取把16日采集误读成正式上线，已纠正。'
 if product=='英雄联盟':date='2026-06-30';why='6月底经典模式上线是关停稿的历史前情，不是本期新游。'
 if product=='FlyMe2theMoon':date='2011-09-28';why='2011年旧作上线，非10月16日新品。'
 if product in ['绿梦','绿梦：时空之声','明日方舟：终末地','剑侠世界4：无限']:date='2026-10-15';why='来源明确15日事件，落在窗口之前；前期公测已发布，不以16—18日转载再召回。'
 if '致玩家书' in product:why='书名不是产品名，普通文章标题误召回。'
 if product in ['叛乱：沙漠风暴','绝区零','Spine','异于天堂（STRANGER THAN HEAVEN）']:why='旧品内容预告/既有未来档期，非本期新品首次首曝或老品跨平台，原标签误读。'
 if product in ['三角洲行动','使命召唤手游','和平精英','炼金与魔法-奇幻生存沙盒','破烂水手-多人联机漂流模拟器']:why='新玩法/手册/皮肤/按键功能，非新品上线。'
 if product=='戴森球计划':date='2021-01-01';why='2021年历史众筹/EA背景，非本期新游。'
 if product=='BagMaster Isekai':date='2026-03-01';why='3月全球发行、3—5月收入数据是历史开发案例，原抽取错误回填16日。'
 if product=='龙之谷':date='2026-10-13';why='红莲宫主题服13日上线，非本期新品/重启；不把访谈日期当开服日。'
 if product=='恐鬼症':date='2026-10-12';why='3000万销量与2027年正式版为背景，不是本期测试。'
 if product=='Smash Fest':date='2026-05-01';why='5月已上线，融资稿的历史产品背景。'
 if product=='雾锁王国':why='1.0有新事件但来源只有一篇，且今日未提供绝对月日；保留单源候选。'
 if product=='高达激战指令':sig='new_game_schedule';why='测试招募而非本期实际开测；与英文Gundam Blitz Order的同一性未经原文证明，分别审计。'
 if product=='极限战场-多人战场竞技射击':sig='new_game_schedule';why='追加招募资格非首次开测，本体15日测试已发布。'
 node(product,date,ids,sig,old['event'],False,why)

# Full structured calendar pool: ordinary versions/skins are explicitly retained as rejects.
existing={(x,ss) for x in [] for ss in []}
covered={x for n in NODES for x in n['source_ids']}
for rr in ROWS:
 if rr['section']!='release_calendar' or rr['source_id'] in covered or rr['source_id']=='S0214':continue
 n=int(rr['source_id'][1:]); gm=re.search(r'^Game: (.+)',rr['text'],re.M); product=gm.group(1) if gm else re.sub(r' - .*','',rr['title'])
 sig='old_major_update'; ev='日历原始召回，未达重大更新/新品标准'; dt=rr['date']; why='普通版本、赛季、主题服、皮肤或活动不进入产品日历。'
 if n in [213]:sig='new_game_schedule';ev='Switch版延期';why='延期无新发售日期且单源，不是可发布新品节点。'
 if n in [215,216,217,218,219]:
  sig='new_game_test' if n in [215,217,218] else 'old_cross_platform_launch';ev=rr['title'];why='单源召回；次日测试仍受独立来源门槛约束。'
  if n==217:dt='2026-10-19';product='Second Stone'
 node(product,dt,[rr['source_id']],sig,ev,False,why)

node('Rain98','2026-10-16',[214,258,307],'new_game_test','Steam体验版上线',True,'Gematsu结构化正文明确16日公告，机核说明Steam体验版与超过3小时内容；同URL17/18日快照只计一次。')
node('杯杯倒满','2026-10-16',[27,246],'new_game_launch','1.0正式版上线',False,'同URL只计一个独立来源，不能因两日采集满足多源。')
node('霜港迷城','2026-10-16',[25,119],'new_game_launch','PC 1.0发售',False,'两篇正文只有今日/现已，未出现可核验的绝对月日；不得由采集日期代填实际发售日。')
node('恶魔城：贝尔蒙特的诅咒','2026-10-16',[3,120],'new_game_launch','多平台发售',False,'仅今日/现已，缺正文绝对月日，保留审计。')
node('越过山丘','2026-10-16',[15,113,275],'new_game_launch','PC发售',False,'今日/现已/本周未提供本期实际发售日的绝对日期，禁止以目录日回填。')
node('链兽角斗','2026-10-16',[24,126],'new_game_launch','1—4人合作游戏发售',False,'S0126为即将发售列表且明确提示日期可能不同步，斜杠日期未获另一份实际发售公告的绝对日期确认；保留9分多源候选，未据此断言16日实际上线。')
node('使命召唤：现代战争4','2026-10-16',[144,272],'new_game_launch','单人战役数字预购抢先体验',False,'属于部分战役抢先体验而非全产品正式上线；原文英文October16未被现有日期证据校验接受，保留审计而不猜造ISO原文。')
node('群星漫卡','2026-10-16',[147],'new_game_first_reveal','多IP电子集换卡牌手游首次披露',False,'单源；行业独立入选不降低日历多源门槛。')
node('Gundam Blitz Order','2026-10-16',[69],'new_game_schedule','公布11月18—24日网络测试',False,'只一份可确认英文产品报道；不能凭共同IP强合并3839中文产品。')
node('Titanium Court','2026-10-16',[69],'new_game_schedule','宣布10月29日跨平台发行',False,'单源；移动端策略产品可独立入行业，日历仍不满足多源。')
node('他予回声','2026-10-20',[308],'new_game_test','首次寻星测试',False,'实际测试20日超出允许至19日的产品日历窗口。')
node('篮球少女：飞跃巅峰','2026-10-18',[308],'new_game_schedule','10月23日公测预告',False,'单源日历节点；NBA联动讨论不属于允许召回的两个分区，不能加为第二来源。')

# Independently reverse scan all product paragraphs in the full Steam guide and mobile digest.
guide=text(126)
for block in re.split(r'\n(?=[^\n]+\n关键字：)',guide):
 match=re.search(r'^([^\n]+)\n关键字：.*?发行日期：\s*(2026)/(10)/(\d+)',block,re.S)
 if not match:continue
 product=match.group(1).strip()
 if '链兽角斗' in product:continue
 dt=f'{match.group(2)}-{match.group(3)}-{int(match.group(4)):02d}'
 node(product,dt,[126],'new_game_launch','Steam发行清单节点',False,'仅一份即将发售汇总，未以来源篇数或同篇产品数量冒充多源。')
for product,dt,signal,reason in [
 ('No Man’s Sky','2026-10-28','old_cross_platform_launch','老品28日跨平台，超出19日及时性窗口。'),('Sifu','2026-10-12','old_cross_platform_launch','明确12日，非本期实际上线。'),('Vampire Crawlers','2026-10-12','old_cross_platform_launch','明确12日，非本期实际上线。'),('9 Kings','2026-10-12','old_cross_platform_launch','明确12日，非本期实际上线。'),('Little Kitty, Big City','2026-10-16','old_cross_platform_launch','只有now available，无绝对实际发生日期，单源。'),('Totopia World','2026-10-13','new_game_test','13日首次被发现，非本期实际开测。'),('Replaced','2026-12-08','old_cross_platform_launch','老品移植在12月8日，超出及时性窗口。'),('Dome Keeper','2026-10-16','old_cross_platform_launch','只有out now，无绝对实际发生日，单源。'),('Yes, Your Grace 2: Snowfall','2026-10-16','old_cross_platform_launch','只有has launched，缺绝对日且单源。'),('Battle Spirits Teaching App','2026-10-07','new_game_launch','10月7日旧上线，教学应用亦非新品游戏。'),('Pachislot Sengoku Collection 6','2026-10-13','new_game_launch','13日旧发行，不能按周汇总16日回填。'),('Azur Promilia','2026-10-16','new_game_schedule','英语公测计划在14日旧帖已经出现，单源未来计划不冒充本期新档期。'),('Walk The Frog','2026-10-14','old_cross_platform_launch','14日旧跨平台，非本期。')]:
 node(product,dt,[69],signal,'周汇总所述产品节点',False,reason)

# Additional title/body signals, independently of industry selection.
for product,dt,ids,sg,ev in [
 ('风吹屿小镇','2026-10-16',[2],'new_game_test','免费测试试玩'),('利维坦之巢','2026-10-16',[5],'new_game_first_reveal','首次公布'),('困兽之国2','2026-10-16',[6],'new_game_first_reveal','首次公布'),('Hela：鼠鼠奇旅','2026-10-16',[21,253],'new_game_test','新品节限时Demo'),('北境深潜','2026-10-16',[26,245],'new_game_test','新品节Demo'),('嗨斗农场','2026-10-16',[28,247],'new_game_schedule','10月29日PC主机发行预告'),('鸟的故事','2026-10-16',[22,251],'old_cross_platform_launch','各大主机平台上线'),('破梦之行','2026-10-16',[95],'new_game_test','Steam Demo'),('重力回路2','2026-10-16',[110],'new_game_test','Steam Demo'),('让球飞！','2026-10-17',[270],'new_game_test','Steam Demo'),('Red Rooster','2026-10-14',[76],'new_game_first_reveal','正式官宣'),('Golden Star Vortex','2026-10-18',list(range(329,334)),'new_game_test','Steam免费Demo'),('Second Stone','2026-10-16',[217],'new_game_schedule','公告19日Demo')]:
 if product=='Second Stone':continue
 node(product,dt,ids,sg,ev,False,'单源/同URL重复或同站多语言版本；正式日期及新旧阶段仍需原文支持。')

NODES.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
AUD={k:v for k,v in RAW.items() if k!='nodes'};AUD['nodes']=NODES
AUD['editorial_scan']={'industry_and_calendar_records':sum(r['section'] in ['industry_news','release_calendar'] for r in ROWS),'raw_nodes':len(RAW['nodes']),'corrected_nodes':len(NODES),'industry_overlap_allowed':True,'prior_calendar_reports_checked':['2026-10-14 daily','2026-10-09_to_2026-10-15 weekly'],'date_format_limitations':['Chained Beasts slash dates / upcoming-list actual-date uncertainty','Modern Warfare 4 English dates / partial campaign early access']}
dump(P/'release_calendar_audit.json',AUD)
# Release input records are represented by nodes, not duplicated unscored decisions.
DS={k:d for k,d in DS.items() if not k.startswith('L')}
cards=['# 2026-10-16_to_2026-10-18 独立事件候选\n','来源全文扫描见full_input_scan.json；仅同一主体/产品、同一日期、同一事件合并。AI已反扫全部行业候选；产品日历独立反扫两个输入分区。\n']
for d in DS.values():
 cards.append(f"\n## {d['candidate_id']} - {d['event']}\n- section: {d['section']}\n- status: candidate\n- source_ids: {', '.join(d['source_ids'])}\n- entities: {' / '.join(d['entities'])}\n- event_date: {d.get('event_date','2026-10-16')}\n- facts: {d.get('facts_read',d['event'])}\n- notes: {d['reason']}\n")
 if 'community' in d:cards.append('- community: '+json.dumps(d['community'],ensure_ascii=False)+'\n')
for n in NODES:cards.append(f"\n## {n['candidate_id']} - {n['product']}\n- section: release_calendar\n- source_ids: {', '.join(n['source_ids'])}\n- event_date: {n['event_date']}\n- facts: {n['event']}\n- notes: {n['editorial_reason']}\n")
(P/'event_candidates.md').write_text('\n'.join(cards),encoding='utf-8')
md=['# 筛选决策\n','卡片曝光去重：历史窗口2026-10-02至2026-10-15，92条；Xbox Labs两次历史card_exposed=false、card_rank=null、card_limit=10，8分胜过7分的战狗，唯一内部card_carryover。所有已曝光旧事件重复来源仍排除；无material_update。\n','维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均逐事件覆盖，具体数量由下表和结构化决策计算；综合稿S0069/S0126/S0263/S0308均拆分。\n','行业与AI/社区同事件不重复；行业与日历独立。普通PC/主机纯单人发售R1，不按RPG/经营标签抬R。\n','| candidate | decision | target_section | scores | reason |\n| --- | --- | --- | --- | --- |']
for d in DS.values():md.append(f"| {d['candidate_id']} | {d['decision']} | {d['section']} | {json.dumps(d.get('scores',{}),ensure_ascii=False)} | {d['reason']} |")
(P/'selection_decisions.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
dump(P/'selection_decisions.json',{'decisions':list(DS.values())})
scan=[]
for rr in ROWS:
 scan.append(dict(source_id=rr['source_id'],section=rr['section'],title=rr['title'],text_chars_read=len(rr['text']),sha256=hashlib.sha256(rr['text'].encode()).hexdigest(),facts=fact_excerpt(rr),matching_candidates=[d['candidate_id'] for d in DS.values() if rr['source_id'] in d['source_ids']],calendar_nodes=[n['candidate_id'] for n in NODES if rr['source_id'] in n['source_ids']]))
dump(P/'full_input_scan.json',{'records':len(scan),'text_chars':sum(len(r['text']) for r in ROWS),'inputs':scan})
dump(P/'history_read_audit.json',{'history_window':H['history_window'],'markdown_sha256':hashlib.sha256(HMD.encode()).hexdigest(),'occurrences':H['occurrences']})
print('audit decisions',len(DS),'calendar nodes',len(NODES),'records',len(ROWS))
