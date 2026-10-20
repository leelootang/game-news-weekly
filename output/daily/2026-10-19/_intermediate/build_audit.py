import json, re, hashlib, sys
from pathlib import Path
sys.dont_write_bytecode = True
P = Path(__file__).resolve().parent
ROOT = P.parents[3]
S = {x['source_id']: x for x in map(json.loads, (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
H = json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))['occurrences']
def save(name, value):
    (P/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def proof(sid, needle):
    text = S[sid]['text']
    assert needle in text, (sid,needle)
    return next(line for line in text.splitlines() if needle in line)
save('full_input_scan.json', {'records':len(S),'scan':'全部 JSONL text 已读取并按段落扫描；译文镜像不作为独立新闻来源；候选逐条判断，正文另作逐事实取证。','sources':[dict(source_id=sid,section=x['section'],chars=len(x['text']),sha256=hashlib.sha256(x['text'].encode()).hexdigest(),paragraph_count=len(x['text'].splitlines()),body_status=x['body_status']) for sid,x in S.items()]})
save('history_read_audit.json',{'window':{'start':'2026-10-05','end':'2026-10-18'},'occurrences':H,'markdown_sha256':hashlib.sha256((P/'industry_history_14d.md').read_bytes()).hexdigest()})
D=[]
def add(cid,ids,entities,event,e=0,r=1,m=1,reason='',section='industry_news',include=False,history=None,**kw):
    d=dict(candidate_id=cid,section=section,source_ids=ids,entities=entities,event=event,event_date='2026-10-19',decision='include' if include else 'exclude',reason=reason)
    if section=='industry_news':
        d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m)
        matches=[x for x in H if any(key in x['title'] or key in x['event'] for key in (history or []))]
        d['history_check']=dict(history_match=bool(matches),novelty='repeat_only' if matches else 'new_event',prior_occurrences=[x['title']+'｜'+x['report_window']['start']+'_to_'+x['report_window']['end'] for x in matches],new_facts=[],prior_card_exposed=any(x['card_exposed'] for x in matches) if matches else None)
        if matches: d['history_occurrence_details']=[{k:x[k] for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for x in matches]
    if len(ids)>1: d['cluster_basis']=dict(subject='/'.join(entities),product='/'.join(entities),event_date=d['event_date'],event=event)
    d.update(kw); D.append(d); return d

# Each source receives its own judgment. Composite sources are additionally split below.
# e/r/m, reason. Domestic products are never hidden inside a generic low-signal batch.
spec={
1:(1,3,1,'现代战争故事收尾为既有产品生命周期表述，4分；同一内容已随新子系列报道曝光。'),
2:(0,3,1,'上古卷轴OL例行第二季地下城，非新品或重大商业状态。'),
3:(0,3,1,'战地皮肤质量回应转社区同事件，不在行业重复。'),
4:(2,3,1,'经典模式收官与历史同事件；短讯27年1月口径与旧报道不一致，不能据24字短讯认定实质新阶段。'),
5:(2,1,1,'海外老作取消VR门槛后的预购，弱迁移3分；不是完整新品发售。'),
6:(2,2,1,'Steam成就整理功能是一般平台能力，5分，非重大分发或收费政策。'),
7:(0,3,1,'国产手柄常规预售宣传，无游戏商业状态变化。'),
8:(1,1,1,'联机试玩版累计下载50万，单产品里程碑E1；未证明国内主体、PVP或结构性赛道份额，2分。'),
9:(0,3,1,'格斗赛事赛果，非资本或电竞组织结构变化。'),
10:(3,1,1,'增量钓鱼PC试玩版；主体相关性未知，不能由模拟标签直接给R3，4分。'),
11:(3,1,1,'海外展会中的PC试玩版，未见移动/中国市场迁移，4分。'),
12:(0,1,1,'试玩版热门榜前十与新英雄，纯榜单/内容更新。'),
13:(0,3,1,'创作者患病信息不等于管理层离任或项目取消；不推测健康及项目后果。'),
14:(2,1,1,'Reshine未来PC档期与试玩，弱迁移3分；日历单独判断。'),
15:(0,3,1,'ACE接入内容检测的客户宣传案例；未披露新合作签署日或重大合作状态，不把既有接入宣传抬为E3。'),
16:(2,2,1,'综合稿拆分幕府重制版下架与RuneScape取消；前者5分，后者另作历史查重。'),
17:(2,3,1,'国产团队太吾授权衍生作的新经营案例数据，7分；不以报道日替代实际EA发售日。'),
18:(2,2,1,'欧盟草案公开征求意见始于10月1日；当前为影响解读，不是本期法律生效。R2、5分。'),
19:(0,2,1,'AI反编译综合评论反扫转AI候选；10月10日DMCA、13日Labs等明确旧日期逐件审计，不包装为19日新事件。'),
20:(0,1,1,'特斯拉汽车与游戏类比，非游戏行业独立新闻。'),
21:(2,2,1,'育碧裁员/工作室关闭5分；天美项目取消另与历史精确匹配。'),
22:(0,3,1,'校招调查转AI新闻；人才培养机制可支撑深度，泛招聘不按核心管理变动计E3。'),
23:(0,3,1,'9月24日上线、国庆后榜单的产品体验分析；没有19日新生命周期节点，日历不得回填上线。'),
24:(0,3,1,'捉宠横向分析，明确9月上线及10月7日结束测试均为前情；普通产品比较不作为本期首曝。'),
25:(2,3,2,'16日发布的Sensor Tower9月发行商收入结构，25/26为同数据事件；全部历史匹配未曝光，可竞争唯一补位。'),
26:(0,3,1,'周报综述按资本、平台、产品等独立事件拆分，不能整篇打包行业卡。'),
27:(0,3,1,'AI NPC记忆工程案例与成本测算转AI，估算不是实际运营账单。'),
28:(0,3,1,'丹青渡叙事版本评论，纯榜单Top3与普通版本不豁免E0；不按采集日重写版本上线。'),
29:(2,3,2,'天美刺客信条命运取消为同一历史事件。'),
30:(0,3,1,'金茶奖历届回顾与征集，非本期公司或产品新增状态。'),
31:(0,1,1,'海外已公开产品参加线下展会，国内首次参展不是新品首次首曝。'),
32:(0,3,1,'大会明确10月15日；合作平台和AI助手披露属窗口外，不作为19日新发布。'),
33:(0,3,1,'S0028英文镜像，同一媒体译文不得作独立来源。'),
34:(0,3,1,'S0030英文镜像，历史回顾。'),
35:(2,3,1,'S0029英文镜像，同项目取消，不独立增加来源数量。'),
36:(3,1,1,'Rain98体验版晚到报道；已进入周末产品日历，同产品同阶段跨期重复；行业纯海外单机R1。'),
37:(0,3,1,'禁止主体的常规赛事宣传，正文排除。'),
38:(0,3,1,'SCS决赛赛果，与S0009同一赛事，不是战略动作。'),
39:(0,3,1,'LAP能力展示明确在10月14日，AI反扫后按窗口外排除，未见本期新的部署里程碑。'),
40:(2,3,1,'国内厂商海外二合游戏最新月收入与社群经营案例，7分；不是把2月上线改成10月。'),
41:(0,3,1,'AI素材与游戏内短剧的直接应用案例，转AI分区，不在行业重复产品数据。'),
42:(0,2,1,'AI法律解读，转AI审计，与UKIE认证服务分属背景/新服务。'),
43:(0,2,1,'UKIE面向游戏工作室的新AI合规认证服务，转AI。'),
44:(3,2,2,'Liquid Swords破产涉及资产出售、27人解雇、网易少数股权投资背景，8分；并非只给裁员E3。'),
45:(0,1,1,'克罗地亚行业会议宣传，非全球竞争格局或游戏新平台。'),
46:(1,2,1,'QA工会罢工授权，尚非实际罢工；一般海外劳资E1，3分。'),
47:(0,1,1,'GDCA参评流程与奖项调整，行业活动例行规则。'),
48:(3,3,1,'Flow融资摘要，历史卡片已曝光，重复排除。'),
49:(2,1,1,'墨西哥社交/流媒体保护法令短摘，没有游戏具体新要求，3分且非完整正文。'),
50:(0,2,1,'Pocket Gamer奖项报名宣传。'),
51:(2,3,1,'EWC新增2027预选路径，7分但仅被阻断页面摘要，无可发布完整正文。'),
52:(0,3,1,'恋与深空联动事件转社区；摘要不足，正文采用完整社区原帖并保留玩家归因。'),
53:(1,3,1,'莉莉丝产品累计流水5000万美元里程碑，E1R3M1=4；完整报道不可读。'),
54:(3,3,2,'Supercell全资收购Metacore完成，与S0060同主体同日同交割事件；正文只引用完整来源。'),
55:(0,2,1,'会议赞助商宣传。'),
56:(0,2,1,'移动变现评论仅有摘要，不能支撑平台规则变化或深度。'),
57:(0,3,1,'每周播客摘要，Squad停运没有新增状态且未获得完整论证。'),
58:(0,2,1,'人事综述拆分Apple渠道核心管理、其他高管和非核心岗位；不全篇打包。'),
59:(1,2,1,'Netflix约60名游戏员工裁员，纯裁员E1R2M1=3，未由本稿证明新增工作室关闭。'),
60:(3,3,2,'Metacore于10月19日宣布交割完成、团队进入Supercell，11分；与此前5月计划属不同实质状态，本双周历史无匹配。'),
61:(3,3,1,'腾讯领投Flow4600万美元旧融资，再次报道不构成新融资。'),
62:(0,3,1,'使命召唤纪念内容短摘，非组织变动新闻。'),
63:(0,1,1,'马里奥铭牌趣闻，非商业或生产变迁。'),
64:(0,1,1,'小岛秀夫动画客串，普通宣传。'),
65:(0,1,1,'Saros新周目更新，非重大新模式证据。'),
66:(0,2,1,'反编译社区关闭转AI候选，但仅171字摘要不能核验完整事件。'),
67:(0,1,1,'星球大战赛车后续内容采访仅短摘。'),
68:(0,3,1,'无畏契约赛事线下活动复盘；英雄公布与营销活动不构成独立行业商业新闻。'),
69:(0,1,1,'GTA6周边档期观察；重复引用既有发售档期、不是本期GTA6正式发售。'),
70:(0,1,1,'触乐澳门见闻，非游戏行业新闻。'),
71:(2,3,1,'本期发表的手工模拟游戏经营案例，7分；明确回本及在线峰值发生在9月21日和10月4日，非本期发行。'),
72:(0,3,1,'开测清单分产品判断；21日垂钓者为已曝光旧定档，23日篮球少女另计。'),
73:(0,2,1,'Game Pass常规游戏轮换，不是订阅定价或渠道政策。'),
74:(2,1,2,'Faraway新档期，普通海外单机R1仅4分；且正文标snippet不采用。'),
75:(0,3,1,'MrBeast营销视频为常规宣传；DMZ预购提前访问单独日历审计，不写完整游戏已上线。'),
76:(0,3,1,'战地皮肤质量争议转社区，与S0091同事件。'),
77:(3,2,2,'Liquid Swords破产关闭同S0044，完整来源覆盖，snippet本身不引用。'),
78:(1,2,1,'Lucasfilm合作对象从大厂延展中小团队的战略访谈，无本期新签合同，3分。'),
79:(0,0,1,'主机帧生成专利转AI审计；专利不等于正式产品规格。'),
80:(0,3,1,'普莱斯演员感谢好评属宣传与口碑，不是新产品状态。'),
81:(3,1,1,'合作恐怖PC试玩版，未证明PVP/国内主体，4分。'),
82:(1,2,1,'FFBE手游改编主机单机的开发采访有移动资产迁移，但当前为前瞻非新立项，3分。'),
83:(3,1,1,'最终幻想单机试玩前瞻；发行类型为海外主机单机，不能仅RPG给R3，4分。'),
84:(1,1,1,'赛博朋克电影原创故事路线表态，非新签影视合作，2分；Hadar旧进展不重复。'),
85:(2,3,2,'天美刺客信条命运取消画面同历史曝光。'),
86:(0,2,1,'NVIDIA App智能体控制转AI；更新日期明确13日，不按19日采集改写为新品。'),
87:(2,1,1,'羊蹄山单款主机续作销量估算，缺少移动或中国市场迁移，3分。'),
88:(0,2,1,'悟空声优抗议AI声音转AI/社区审计，不以当事人愤怒替代确切授权或法律结论。'),
89:(0,0,1,'蝙蝠侠电影旧取消项目剧情，非游戏。'),
90:(0,0,1,'电影票房，非游戏。'),
91:(0,3,1,'战地皮肤官方回应与玩家反应转社区。'),
92:(3,1,1,'Slam Tank未来试玩，海外PC单机相关性未知仅4分；AI为世界观背景非生成式应用。'),
93:(0,1,1,'Brushland已有产品常规玩法预告，不证明首次曝光。'),
94:(0,1,1,'Crop概览预告，2027旧档期，非本期首曝证据。'),
95:(0,1,1,'剑星拍照模式宣传，11月5日旧跨平台安排，不当新定档。'),
96:(2,1,1,'快递员汤姆PC/Switch未来档期，普通海外单机R1，3分。'),
97:(2,1,1,'乐高合集老作Switch2移植，弱迁移3分。'),
98:(3,1,1,'银松镇海外单机已发售宣传，R1、4分。'),
99:(0,3,1,'恶意不息职业系统概览，既有2027年3月档期不证明本期新定档。'),
100:(2,1,1,'生化危机旧作Switch2移植体验，弱迁移3分；多游戏逐项留日历。'),
101:(0,2,1,'AI仿作担忧导致取消试玩，已在上一期AI披露；本期无新状态。'),
102:(0,0,1,'昆汀电影计划，非游戏。'),
103:(2,1,1,'街头霸王电影票房新数据，但纯海外游戏衍生电影与移动业务迁移弱，3分。'),
104:(1,1,1,'Bloober维持实体版战略表态，未公布新项目或渠道政策，2分。'),
105:(0,0,1,'星球大战电影搁置，非游戏项目取消。'),
106:(0,0,1,'演员接戏经历，非游戏。'),
107:(0,1,1,'加菲猫评测，非新商业事实。'),
108:(0,1,1,'GTA6发售预告细节分析，不能把发售预告当正式发售。'),
109:(0,1,1,'Steam即将发行清单逐产品评分；不能全篇按模拟/RPGR3。'),
110:(0,3,1,'ARC2.0体验推荐，13日PVE测试为历史已曝光。'),
111:(0,1,1,'哈迪斯2音乐评论，非新品或公司变化。'),
112:(1,1,1,'Outlast Trials六年开发复盘，无本期产品或组织变化，2分。'),
113:(0,1,1,'Anthropic安全草案泄露转AI审计，与游戏环节无具体迁移链。'),
114:(0,1,1,'黑魂2早期原型考古，无商业状态。'),
115:(3,1,1,'23位开发者免费音量小游戏合集，海外一般小主体，4分。'),
116:(2,2,1,'Steam新品节8011个试玩的供给数据有PC发行迁移，5分；不因提及Roblox背景提高主体R。'),
117:(0,0,1,'婚礼显卡趣闻。'),
118:(0,0,1,'显卡供应传闻与否认，未证明游戏市场竞争迁移。'),
119:(1,1,1,'Outlast历史融资与抵押开发复盘，不是本期新一轮融资，2分。'),
120:(2,1,1,'非官方PS5模拟器运行恶魔之魂的技术演示，弱迁移3分；不是官方PC发售。'),
121:(0,0,1,'显卡机场货物失踪，非游戏行业事件。'),
122:(0,3,1,'手柄产品评测，无产业结构事件。'),
123:(0,2,1,'师父12日移植为历史事件；本期仅品类付费榜第一，不以纯榜单抬E2，未构成实质新状态。'),
124:(3,3,1,'阅文群星漫卡首曝为历史已曝光，晚到同事件解读不再入选。'),
125:(0,0,1,'电源硬件广告。'),
126:(0,0,1,'内存优化硬件广告。'),
127:(0,0,1,'主板硬件广告，AI参数调校宣传不足以单独构成AI游戏新闻。'),
128:(2,3,1,'本期制作人访谈披露帕鲁正式版新增数百万玩家、中国/美洲居前，经营数据与品类结构7分；不声称19日首发。'),
129:(0,3,1,'手柄预售广告同S0007。'),
130:(0,3,1,'国产射击叙事趋势评论，案例均7月、9月等旧节点，不改写为当日新战略。'),
144:(3,3,1,'HUNGER新品封闭测试，原文明确搜打撤/角色扮演与PC，10分。')}
hist={1:['使命召唤'],4:['英雄联盟》经典模式'],25:['9月37家中国手游发行商'],29:['刺客信条：命运'],35:['刺客信条：命运'],48:['Flow Games'],61:['Flow Games'],85:['刺客信条：命运'],110:['ARC Raiders'],123:['苹果独立游戏周'],124:['群星漫卡']}
inc={17,25,40,44,60,71,128,144}
for n,(e,r,m,reason) in spec.items():
    sid=f'S{n:04d}'
    d=add(f'I{n:03d}',[sid],[S[sid]['title'].split('：')[0]],S[sid]['title'],e,r,m,reason,include=n in inc,history=hist.get(n))
    if n in [54,60]:d['entities']=['Supercell','Metacore']
    if n==4:d['entities']=['Riot Games','英雄联盟']
    if n==53:d['entities']=['莉莉丝','Clash of Critters']
    if n==25:
        d['source_ids']=['S0025','S0026'];d['entities']=['Sensor Tower','中国手游发行商'];d['event']='10月16日披露9月中国手游发行商收入结构';d['event_date']='2026-10-16';d['cluster_basis']=dict(subject='中国手游发行商',product='中国手游市场',event_date='2026-10-16',event='Sensor Tower9月发行商收入报告');d['card_carryover']=True;d['history_check']['novelty']='card_carryover'
    if n==44:
        d['source_ids']=['S0044','S0077'];d['entities']=['Liquid Swords','网易'];d['cluster_basis']=dict(subject='Liquid Swords',product='Samson',event_date='2026-10-19',event='破产及关闭，资产出售')
    if n==60:
        d['source_ids']=['S0054','S0060'];d['cluster_basis']=dict(subject='Supercell',product='Metacore',event_date='2026-10-19',event='全资收购交割完成')
    if n in [54,77]:
        d.update(decision='merge',merge_into='I060' if n==54 else 'I044',reason='同一主体、同一10月19日交割/破产事件；由完整正文候选承载。')
    if n in [33,34,35,38,129]:
        d.update(decision='merge',merge_into={33:'I028',34:'I030',35:'I029',38:'I009',129:'I007'}[n])

apple=add('I058_APPLE',['S0058'],['Apple','Carson Oliver'],'Carson Oliver将升任App Store副总裁',3,2,1,'全球移动分发核心管理层变动，报道为将升任，E3R2M1=7；不能写成已完成任命。',include=True)
for cid,ent,event,e,r,m,reason,keys in [
 ('I016_RS',['Jagex','RuneScape Reignited'],'10月15日取消永久分叉服',2,3,1,'历史同事件未曝光，7分；低于本期唯一未曝光候选ST8分，不能再占第二条。',['RuneScape']),
 ('I021_AC',['腾讯','天美'],'刺客信条命运早期取消',2,3,2,'历史卡片已曝光，原型素材与背景补充不构成新取消。',['刺客信条：命运']),
 ('I026_X',['Xbox Labs'],'10月13日Labs成立',3,2,1,'历史任一已曝光，晚到综述排除。',['Labs']),
 ('I026_K',['库洛','言之域科技'],'库洛入股言之域15%',3,3,1,'虽然日报未曝光，周报已第4条曝光，不能再次使用补位。',['库洛']),
 ('I026_F',['腾讯','Flow Games'],'腾讯领投Flow Games4600万美元',3,3,1,'历史已曝光，无新增资金或交割状态。',['Flow Games']),
 ('I026_C',['腾讯','Circle Games'],'腾讯领投Circle Games2500万美元A轮',3,3,1,'融资为半个月前背景且已有历史报道，无新增。',['Circle']),
 ('I026_A',['Aream'],'Q3移动IAP下降7%',2,3,1,'同一期市场报告已在日卡曝光。',['Aream','三季度游戏并购']),
 ('I026_N',['腾讯','火影忍者'],'10月12日宣布国际服',3,3,1,'国际服旧计划已曝光，综述未见新发行日。',['火影忍者']),
 ('I026_D',['腾讯','全境封锁2'],'12月14日国服停运安排',2,3,1,'停运公告已在12日日报卡曝光。',['全境封锁2']),
 ('I026_S',['西山居','剑侠世界4：无限'],'10月15日公测',3,3,1,'公测历史已曝光，重复。',['剑侠世界4']),
 ('I026_G',['绿梦：时空之声'],'10月15日公测',3,3,1,'公测历史已曝光，重复。',['绿梦']),
 ('I026_B',['冰川网络'],'10月13日前三季度预亏公告',2,3,1,'常规业绩预告，无原文一致预期/指引偏离、重大减值或流动性证据；财报例外未过。',[]),
 ('I026_CA',['凉屋','查无此地'],'10月14日Steam抢先体验',3,3,1,'实际日期明确14日，窗口外；此前未入报告也不能把发行日改19日。',[]),
 ('I026_CV',['恶魔城：贝尔蒙特的诅咒'],'10月15日多平台发售',3,1,1,'普通海外单机纯发售R1，4分，日期亦窗口外。',[]),
 ('I026_YY',['网易','燕云十六声'],'11月下旬DLSS5支持计划',0,3,1,'已有产品图像升级预告，普通技术更新，不按新品或平台政策。',[]),
 ('I058_X',['Xbox','Mojang'],'Mojang负责人任命',3,2,1,'任命已随Xbox XP组织调整曝光，无实质变化。',['XP']),
 ('I058_SK',['Skydance','Bobby Kotick'],'Bobby Kotick加入Skydance董事会',1,2,1,'非执行董事加入跨媒体集团，不等于游戏业务CEO或核心团队更换，3分。',[]),
 ('I058_M',['Skydance','Warner Bros. Games'],'派拉蒙与华纳游戏部门合并',3,2,1,'历史10月7日日卡已曝光。',['Paramount与华纳','派拉蒙']),
 ('I058_SC',['Supercell'],'创作者及合作平台非核心岗位入职',0,3,1,'非核心管理层，常规岗位移动；R3不豁免E0。',[]),
 ('I058_SM',['Smadex','Luis de la Camara'],'前Rovio营销副总裁加入Smadex任CMO',3,1,1,'原文未说明新公司的移动广告业务，不能凭记忆补迁移关系，4分。',[]),
 ('I072_F',['紫龙游戏','极境：垂钓者'],'10月21日首次PC测试定档',2,3,1,'同首曝确定档期已在日卡曝光，未发生实际测试。',['极境：垂钓者']),
 ('I072_B',['灵犀互娱','篮球少女：飞跃巅峰'],'10月23日公测安排',2,3,1,'本期清单明确灵犀发行与新公测安排，E2R3M1=7。',[])
]:
    sid=f'S{int(cid[1:4]):04d}'
    d=add(cid,[sid],ent,event,e,r,m,reason,history=keys,include=cid=='I072_B')
    if cid=='I026_CV':d['pc_release_scope']=dict(classification='ordinary_overseas_single_player',basis='科乐美与海外团队2D动作游戏纯发售，无独立国内/移动迁移。',evidence=[dict(source_id=sid,evidence=proof(sid,'10月15日，由科乐美'))])

# Full Steam list: independent product cards, platform scope and date retained.
guide=S['S0109']['text']
for k,mm in enumerate(re.finditer(r'([^\n]+)\n关键字：\s*([^\n]+)\n发行日期：\s*(2026/10/\d+)',guide)):
    name,genre,date=mm.groups();end=guide.find('\n关键字：',mm.end());block=guide[mm.start():end if end>=0 else len(guide)]
    r=3 if name=='FirstPlate' else 1
    d=add(f'I109_{k:02d}',['S0109'],[name],name+'列入Steam发行日程',2,r,1,'即将发行清单不证明已发售；'+('在线合作餐厅经营明确优先赛道，10月20日实际EA尚未发生；日程预排无独立新定档证据，7分仍按时点不明排除。' if r==3 else '普通海外单机/未知主体纯发行R1，不能由中文支持认定国产，3分。'))
    d['event_date']=date.replace('/','-')
    d['pc_release_scope']=dict(classification='multiplayer_or_other' if r==3 else 'unknown',basis='原文明确在线合作餐厅经营，非普通单机。' if r==3 else '只有PC清单及品类，未证明国内/重点主体或实质迁移，R1。',evidence=[dict(source_id='S0109',evidence=mm.group(0))])

# Scope for all identifiable PC launch candidates; source quotes support each exception.
for d in D:
    if d['section']!='industry_news' or 'pc_release_scope' in d:continue
    text='\n'.join(S[s]['text'] for s in d['source_ids'])
    if d['scores']['event']>0 and re.search(r'发售|正式上线|新品上线|首发|\blaunch(?:es|ed)?\b|\breleas(?:e|es|ed)\b',d['event'],re.I) and re.search(r'\bPC\b|Steam|PS5|Xbox|Switch|主机|端游',text,re.I):
        sid=d['source_ids'][0];n=int(sid[1:]);r=d['scores']['relevance']
        cl='ordinary_overseas_single_player' if r==1 else 'domestic_or_focus' if n in [17,26,128] else 'substantive_migration'
        needles={17:'国产独立',26:'凉屋新作',128:'中国市场和美洲市场',83:'家用机',36:'Steam',98:'PS5'}
        needle=needles.get(n)
        quote=proof(sid,needle) if needle and needle in S[sid]['text'] else next(s for s in S[sid]['text'].splitlines() if re.search(r'PC|Steam|PS5|Xbox|Switch|主机',s,re.I))
        d['pc_release_scope']=dict(classification=cl,basis='源文明示国内开发、重点主体或实质跨端迁移；判断依据见逐字证据。' if r>1 else '普通海外PC/主机单机或未能确认国内重点关系的发行消息，取R1，不因品类提高。',evidence=[dict(source_id=sid,evidence=quote)])

# AI reverse scan retains event boundaries and explicit exclusions.
ai_include={22,27,41,43,131}
ai_notes={19:'综合评论含多项明确窗口外事件；无单一本期新进展，不把旧DMCA/Labs/Astrocade改为新发布。',22:'本期校招访谈直接反映AI研发岗位和工作流程，具体采访与岗位统计采用。',26:'Epic/迪士尼AI优先工作流为周报回顾，已在前期AI报道；Character破产为12日旧背景。',27:'NPC长期记忆的游戏直接应用，区分已实现案例与假设模型调用账单。',32:'10月15日大会明确窗口外，助手将上线不可改写已上线。',39:'10月14日峰会既有能力展示，窗口外。',41:'游戏内65集AI短剧/漫剧及广告素材的直接应用，正文不重复行业条目。',42:'法律解读主要提供制度背景；具体新认证服务由A043承担，不将解读拼成另一个新闻。',43:'新服务直接覆盖游戏研发工具、授权、玩家可见内容与融资尽调。',66:'页面被阻断，171字摘要不能核验社区关闭原因或日期。',79:'仅为索尼专利，尚未落地；硬件预测和手柄数据缺乏本期可验证游戏效果。',86:'NVIDIA App11.0.9.565明确13日，窗口外。',88:'声优声音侵权指控，单次争议与拟议立法未形成可核验游戏生产规则变化。',101:'试玩公开改封闭已在周末报AI刊载，本期无新状态。',109:'Hypernet只有AI生成内容标签，没有生产环节或可核验机制。',113:'泛AI安全草案与游戏无直接采用或具体迁移链。',116:'AI仿作/试玩取消主要既有案例，Steam供给数据行业另评5分。',127:'消费主板AI参数宣传，无具体游戏研发/产品经营新机制。',131:'明确速度和任务成本跃迁及价格，迁移至游戏脚本原型、测试和工具自动化，事实与推断分开。',132:'ADK非阻塞语音教程有NPC迁移，但作为既有框架教程，优先于本期已选直接案例之后；未采用。',133:'单榜排名与常规模型小版本，缺少本期实际游戏采用，优先级低于已选明确成本变化。',134:'MIT语音模型有配音原型迁移，但当前未见游戏采用或实测成本；本期优先直接案例与成本突破。',135:'COBOL/Fortran等低资源语言基准，不足以证明游戏主流研发环节变化。',136:'Trainium后端属于基础设施，缺少游戏工作负载迁移证据。',137:'吉瓦级集群训练背景，无具体游戏环节及独立效率变化。',138:'仅572字工作流教程摘要，缺少可审核游戏案例。',139:'网站被智能体入侵，缺少游戏主体或具体游戏安全环节变化。',140:'Disney/Character收购拟议状态与破产后诉讼，未落到具体游戏业务。',141:'健康教练评测方法可类比NPC，但不是本期游戏新应用，优先直接游戏材料。',142:'美国联邦文职采购限制，无游戏具体作用链，不作为游戏行业法律建议。',143:'数据管道编排复盘有开发工具迁移，但本期无游戏落地，优先级低于已选五条。'}
for n,reason in ai_notes.items():
    sid=f'S{n:04d}';direct=n<131 and n not in [113]
    add(f'A{n:03d}',[sid],[S[sid]['title']],S[sid]['title'],section='ai_trends',include=n in ai_include,reason=reason,ai_tier='direct_application' if direct else 'transferable_frontier',game_stage=['development','product','operations'] if direct else ['development'],industry_reverse_scan=n<=130,migration_path='明确能力/成本变化可作用于游戏研发原型、自动化测试或实时NPC；本期按事实完整度和直接作用优先排序，非已落地宣称。' if not direct else '')

# Whole community pool and spillovers, followed by a same-window follow-up scan.
community_reasons={160:'水楼不构成可命名事件。',161:'15日广告量旧帖，19日仅延续商单猜测，无新触发。',162:'16日AIGC激励旧帖，19日为旧立场反讽，缺少新事实；不把截图政策当已证实官方规则。',163:'2日文本修改旧帖，19日仅一句情绪回复。',164:'14日错别字旧帖，19日无新增官方进展。',165:'生物命名讨论缺少具体物种/研究原文，正文无法准确说明对象。',166:'14日EN不同步旧帖，19日仍推测代理/资金，无新增状态。',167:'12日联动旧帖，仅泛论军武受众。',168:'健康信息引发关心，缺少游戏机制争议；不传播玩家医学推测。',169:'签证未过指控没有明确演出者/官方取消信息，事件关键对象不清。',170:'欠薪改单机仅截图标题，游戏主体不明确，不能补猜名称。',171:'16日角色计划旧帖，19日无新机制或官方证据。',172:'18日谋勇兼备联动旧帖，19日为声优旧梗，无新触发。',173:'联动中虚拟伴侣题材与付费情感沉浸的冲突，19日新事件；玩家解释与官方事实区分。'}
for n,reason in community_reasons.items():
    sid=f'S{n:04d}';add(f'C{n:03d}',[sid],[S[sid]['title']],S[sid]['title'],section='community_discourse',include=n==173,reason=reason)
add('C091',['S0003','S0076','S0091'],['战地风云6'],'10月13日皮肤视觉错误与五枪套设计引发争议，窗口内官方回应',section='community_discourse',include=True,reason='行业外溢；官方承认质量不足并明确修复安排，回应构成本期新进展。正文采用完整S0091，不把玩家AI猜测写成官方确认。')
for cid,sids,keywords in [('C173',['S0173'],['恋与深空','银翼杀手','2049']),('C091',['S0091'],['战地','五枪','DICE','Battlefield'])]:
    d=next(x for x in D if x['candidate_id']==cid)
    d['community']=dict(trigger=d['event'],claim_scope='玩家观点归玩家；公告内容按报道归开发团队，不推测因果或AI使用。',complaint_logic='虚拟情感付费与虚拟伴侣商品化叙事的张力' if cid=='C173' else '付费外观质量错误及刻意夸张设计是否符合军事题材',timeline=['10月19日新帖并持续讨论至当晚'] if cid=='C173' else ['10月13日皮肤上线','10月19日采集到官方回应','11月修复为未来安排'],follow_up_scan={'keywords':keywords,'scanned_source_ids':list(S),'same_window_matches':[sid for sid,x in S.items() if any(k.lower() in x['text'].lower() for k in keywords)],'result':'同窗口全文补扫；173仅保留19日回复，不引用20日后续；091以开发团队回应为有效进展，未确认AI生成。'})

for cid,sid,reason,include,scores in [('D174','S0174','已配置newsletter优先检查：付费节目正文缺失，现有内容是采访前言，不足以支持Zelda/GTA机制分析。',False,(1,0,0,1)),('D027','S0027','完整NPC记忆成本分析；来源包含架构、传播边界、假设估算及端云代价，核心来源已选A027；与上一期跨设备调查不撞题。',True,(3,3,3,3)),('D022','S0022','完整多采访校招调查；岗位统计、面试评价、带教实例形成生产门槛与判断门槛分离机制，核心来源已选A022。',True,(3,3,3,3))]:
    d=add(cid,[sid],[S[sid]['title']],S[sid]['title'],section='deep_analysis',reason=reason,include=include)
    d['scores']=dict(zip(['relevance','insight','evidence','card'],scores));d['scores']['total']=sum(scores)

save('selection_decisions.json',{'anchor':{'type':'daily','date':'2026-10-19'},'decisions':D})

# Preserve the extractor's raw calendar. Correct editorial event/date evidence,
# then recompute every score and ranked prefix deterministically.
A=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
if not (P/'release_calendar_audit.raw.json').exists():save('release_calendar_audit.raw.json',A)
else:A=json.loads((P/'release_calendar_audit.raw.json').read_text(encoding='utf-8'))
nodes=A['nodes']
def node(product,date,signal,event,ids,reason='',valid=True):
    nodes.append(dict(candidate_id='R_ADD_'+str(len(nodes)+1),product=product,event_date=date,signal_type=signal,event=event,event_type_score={'new_game_test':3,'new_game_launch':3,'new_game_preload':2,'new_game_schedule':2,'old_major_update':1,'old_cross_platform_launch':1}[signal],source_ids=ids,observed_signal_types=[signal],observed_events=[event],focus_companies=[],focus_company_relationships={},company_evidence_ids=[],company_relationship='none',company_bonus=0,editorial_reason=reason,editorial_valid=valid))
for n in nodes:
    p=n['product'];n['editorial_reason']='全文日期/阶段复核；保留原召回但不以采集日替代历史实际发生日。';n['editorial_valid']=True
    if p=='GTA6':n.update(signal_type='new_game_schedule',event_type_score=2,event_date='2026-11-19',editorial_valid=False,editorial_reason='发售预告/档期分析不是正式上线，也未证明本期新定档。')
    if p=='长夜守卫者':n.update(signal_type='new_game_preload',event_type_score=2,event_date='2026-10-19',event='预下载，20日上线')
    if p=='我不是胖虎：小岛大当家':n.update(signal_type='new_game_preload',event_type_score=2,event_date='2026-10-19',event='20时预下载，22日上线')
    if p in ['全境封锁2','火影忍者','黑神话：悟空','最强蜗牛','伊莫','蓝色星原：旅谣','羊蹄山之魂','幻兽帕鲁','暗区突围','赛博朋克：边缘行者']:
        n.update(editorial_valid=False,editorial_reason='历史回顾/旧计划/非游戏动画；没有本期新增可发布阶段。')
    if p=='无尽冬日':n.update(editorial_valid=False,editorial_reason='历届金茶奖回顾，不是新品上线。')
    if p in ['鹅鸭杀','全面战争：幕府将军2','恶魔城：贝尔蒙特的诅咒','剑侠世界4：无限','绿梦：时空之声','极限战场','交织的乐章']:
        n.update(editorial_valid=False,editorial_reason='正文明确属于1月、9月或10月15日前后的历史上线/测试，无本期新阶段。')
    if p=='Rain98':n.update(editorial_valid=False,editorial_reason='同体验版已通过周末报刊载，日历跨期重复。')
    if p in ['上古卷轴OL','酒鬼女神的酒诡']:n.update(editorial_valid=False,editorial_reason='前者普通第二季内容，后者公开试玩已取消且前期已报道；非本期可发布实际事件。')
    if p=='Hollywood Merge':n.update(event_date='2026-02',editorial_valid=False,editorial_reason='正文仅今年2月上线；日未知，保留月份，不补造具体日期。')
    if p=='Slam Tank':n.update(signal_type='new_game_test',event_type_score=3,event_date='2026-10-20',event='试玩Demo推出')
    if p=='查无此地':n.update(signal_type='new_game_launch',event_type_score=3,event_date='2026-10-14',editorial_valid=False,editorial_reason='原文明确14日首次EA，不是旧品跨平台，且在本期之前。')
node('少女前线2：追放','2026-10-19','old_major_update','危区探遗新版本与全新搜打撤玩法',['S0146','S0148'])
node('仙境传说RO：新启航','2026-10-19','old_major_update','新区翡翠月湾',['S0145'],'普通新区，不属于老品重大玩法更新；保留排除。',False)
node('Super Meat Boy 3D','2026-10-19','old_major_update','MOUSE联动更新',['S0155'],'普通联动，不属于产品日历准入的重大玩法更新。',False)
node('长夜守卫者','2026-10-20','new_game_launch','正式上线',['S0149'])
node('Faraway','2026-11-05','new_game_schedule','公布11月5日多平台发售',['S0074','S0153'],'两来源日期一致，但S0074被标snippet，不能提供第二份完整发布证据。',False)
for p,sid,date in [('PAYDAY: Aces High','S0152','2026-11-05'),('Littlelands','S0156','2026-11-16'),('Cleaner Company','S0157','2027-01-26'),('Dumpster Gang','S0158','2026-12-03')]:node(p,date,'new_game_schedule','公布未来发售日',[sid])
for p,sid,date,sg,ev in [('RPG Maker U2U','S0151','2026-10-19','new_game_test','P2D地图编辑器演示'),('Directive 8020: A Dark Pictures Game','S0154','2026-10-19','old_major_update','在线多人模式'),('Saros','S0159','2026-10-19','old_major_update','Zenith更新'),('极境：垂钓者','S0072','2026-10-21','new_game_test','PC限量删档测试'),('篮球少女：飞跃巅峰','S0072','2026-10-23','new_game_schedule','公测定档')]:
    node(p,date,sg,ev,[sid],valid=p not in ['RPG Maker U2U','Saros'],reason='编辑器工具演示不是新品游戏；Saros普通新周目不按重大新模式。' if p in ['RPG Maker U2U','Saros'] else '')
for p,sid,date in [('最终幻想 Resonance','S0083','2026-10-19'),('诡域深行','S0081','2026-10-19')]:node(p,date,'new_game_test','试玩Demo推出',[sid])
node('使命召唤：现代战争4','2026-10-20','new_game_test','DMZ预购模式提前访问',['S0075','S0080'],'只开放新作单一模式的预购提前访问，非完整新品上线或独立测试；且S0075为snippet。',False)
for k,mm in enumerate(re.finditer(r'([^\n]+)\n关键字：\s*([^\n]+)\n发行日期：\s*(2026/10/\d+)',guide)):
    name,genre,date=mm.groups();node(name,date.replace('/','-'),'new_game_launch','Steam即将发行清单节点',['S0109'],'只有预排清单，未得到独立实际发行确认。')
for name in ['生化危机2重制版','生化危机3重制版','生化危机4重制版']:node(name,'2026-10-19','old_cross_platform_launch','Switch2移植体验',['S0100'],'只有单源，实际发生日未明确；采集日期不证明当日上线。',False)
for name,dt,sid in [('剑星','2026-11-05','S0095'),('恶意不息','2027-03','S0099'),('Crop','2027','S0094')]:node(name,dt,'new_game_schedule','宣传中的既有未来档期',[sid],'普通宣传，仅保留原文月份/年份，不补造日期。',False)
# Re-cluster same product+same date and deduplicate translations/publisher mirrors.
group={}
for n in nodes:
    key=n['product'],n['event_date']
    if key not in group:group[key]=n;continue
    b=group[key];b['source_ids']=list(dict.fromkeys(b['source_ids']+n['source_ids']));b['observed_signal_types']=list(dict.fromkeys(b.get('observed_signal_types',[])+n.get('observed_signal_types',[])));b['observed_events']=list(dict.fromkeys(b.get('observed_events',[])+n.get('observed_events',[])))
nodes=list(group.values())
for n in nodes:
    ids=n['source_ids'];unique={}
    for sid in ids:
        x=S[sid];signature=x['source_key'] if x['source_key']=='youxichaguan' else x['url'];unique.setdefault(signature,x['sha1'])
    n['source_fingerprints']=list(unique.values());n['appearance_count']=len(unique);n['appearance_score']=min(3,len(unique));n['industry_ids']=[s for s in ids if S[s]['section']=='industry_news'];n['release_ids']=[s for s in ids if S[s]['section']=='release_calendar'];n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus']
    if n['product']=='鹅鸭杀':n['company_bonus']=0;n['focus_companies']=[];n['company_evidence_ids']=[];n['company_relationship']='none';n['editorial_reason']+='腾讯ACE为服务供应方，不是鹅鸭杀研运主体，删除公司加分。'
    n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus'];n['first_seen_order']=min(int(s[1:]) for s in ids)
    dt=n['event_date'];sg=n['signal_type'];n['window_scope']='report_window' if dt=='2026-10-19' else 'next_day_lookahead' if dt=='2026-10-20' else 'future_announcement' if sg in ['new_game_schedule','new_game_first_reveal'] else 'outside';n['window_eligible']=n['window_scope']!='outside';n['multi_source_eligible']=len(unique)>=2;n['publish_eligible']=bool(n['multi_source_eligible'] and n['window_eligible'] and n.get('editorial_valid',True));n['coverage']='industry_and_release' if n['industry_ids'] and n['release_ids'] else 'industry_only' if n['industry_ids'] else 'release_only'
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
A['nodes']=nodes;A['editorial_audit']='原始抽取保留raw；已全量反扫industry/release，修正历史日期、普通宣传及不可用证据；行业入选与否不参与日历排序。'
save('release_calendar_audit.json',A)
print('industry',[(d['candidate_id'],d['scores']['total']) for d in D if d['section']=='industry_news' and d['decision']=='include'])
print('calendar publishable',[(n['product'],n['priority_score']) for n in nodes if n['publish_eligible']])
