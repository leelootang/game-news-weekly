import json,re,hashlib,sys,difflib
from pathlib import Path
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
HJ=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8')); H=HJ['occurrences']
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sid(i):return f'S{i:04}'
def proof(i,word):
    t=S[sid(i) if isinstance(i,int) else i]['text'];assert word in t,(i,word)
    return next(l for l in t.splitlines() if word in l)
D=[]
def add(cid,ids,entities,event,e=0,r=1,m=1,reason='',section='industry_news',include=False,history=(),**kw):
    ids=[sid(i) if isinstance(i,int) else i for i in ids]
    d=dict(candidate_id=cid,section=section,source_ids=ids,entities=entities,event=event,event_date='2026-10-20',decision='include' if include else 'exclude',reason=reason)
    if section=='industry_news':
        d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m)
        matches=[x for x in H if any(w in x['title'] or w in x['event'] for w in history)]
        d['history_check']=dict(history_match=bool(matches),novelty='repeat_only' if matches else 'new_event',prior_occurrences=[x['title']+'｜'+x['report_window']['start']+'_to_'+x['report_window']['end'] for x in matches],new_facts=[],prior_card_exposed=any(x['card_exposed'] for x in matches) if matches else None)
        d['history_occurrence_details']=[{k:x[k] for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for x in matches]
    if len(ids)>1:d['cluster_basis']=dict(subject='/'.join(entities),product='/'.join(entities),event_date=d['event_date'],event=event)
    d.update(kw);D.append(d);return d
spec={
1:(2,1,1,'海外单机未来档期与已有试玩，R1；与19日同短讯，无新阶段。'),
2:(0,3,1,'创作者疾病公告不是管理层离任或项目取消；不从健康状况推测商业后果。'),
3:(3,1,1,'普通海外/主体未明PC单机试玩，不能凭钓鱼模拟给R3。'),
4:(3,1,1,'海外发行商参展与PC试玩，弱迁移；两款新PV另拆。'),
5:(0,1,1,'Demo榜单与英雄更新，非首测。'),6:(0,3,1,'赛事赛果。'),7:(0,3,1,'手柄预售广告。'),
8:(1,1,1,'联机Demo下载里程碑，未证国内或PVP赛道，非正式上线。'),9:(0,3,1,'素材争议回应已入19日社区；无本期新回应。'),
10:(2,3,1,'拳头经典模式收官历史同事件；24字短讯不足认定新状态。'),11:(2,1,1,'老作移除VR门槛预购，海外一般消息。'),
12:(2,2,1,'Steam成就管理功能是一般平台能力，5分。'),13:(1,3,1,'现代战争收尾访谈已随新子系列事件曝光，无新商业状态。'),
14:(0,3,1,'老作第二季地下城，普通内容更新。'),15:(3,1,1,'主体与相关性未明的PC试玩，不能猜国内开发。'),
16:(0,3,1,'老作联动。'),17:(0,1,1,'后续剧情PV。'),18:(0,3,1,'足球经理后续功能博客，非首曝/定档变化。'),
19:(0,1,1,'既有Demo更新。'),20:(3,3,1,'首个公开试玩；明确1—6人合作海盗RPG，属多人而非普通海外单机例外。'),
21:(0,1,1,'既有产品参展，非首次曝光。'),22:(0,3,1,'Netflix多人生活新作参展；短讯不证明首次公开试玩或新档期。'),
23:(3,1,2,'工坊经营PC试玩；未证明国内/移动主体，R1；独立竞争日历。'),24:(3,1,1,'PC解谜试玩；相关性未明。'),
25:(2,1,1,'真人恋爱影游未来档期，未证明国内厂商或移动；不凭中文名猜主体。'),26:(0,1,1,'既有产品参展宣传。'),
27:(0,3,1,'已有Demo更新中文，非首次首测；塔防类型不豁免E0。'),28:(0,3,1,'杰仕登自研关系明确，但2.0试玩与PV2为既有产品宣传，不抬首曝。'),
29:(2,1,1,'谍战影游未来档期；未给开发主体，弱迁移。'),30:(3,1,1,'海外单机RPG试玩，R1。'),31:(3,1,1,'海外/主体不明单机试玩，R1。'),
32:(0,3,1,'既有Demo加异步联机与圣器，非新品首测。'),33:(3,1,1,'主体不明PC物理游戏发售，R1。'),
34:(0,3,1,'明确国产，但仅新品节全新Demo，未证首次公开测试，按既有宣传排除。'),35:(0,1,1,'两款作品既有Demo参展；分产品留日历审计。'),
36:(3,1,2,'海外单机RPG试玩，纯PC发布默认R1，5分。'),37:(0,3,2,'国产封神题材但为已有Demo更新，非首曝或首次测试。'),
38:(0,3,1,'恋与深空既有联动的解读；不按重大合作E3。'),39:(2,2,1,'越南发行服务案例含自述规模，明确移动迁移但非中国手游市场，5分。'),
40:(0,2,1,'反扫转AI；反编译综述延续19日相同议题，未新增独立部署事件。'),41:(1,2,1,'明星制作人创业观点与历史案例，不把旧关闭/撤资重写当前。'),
42:(2,3,1,'3750万元与23万人是既有众筹自然延续；免费DLC/资金安排为补背景，未构成新商业阶段。'),
43:(0,3,1,'3D资产/引擎协作直接应用，转AI。'),44:(0,3,1,'酒鬼女神取消试玩为周末已报AI事件，当前是同事件解读。'),
45:(3,3,2,'Metacore交割已进入19日卡片，重复；Flow/Circle等独立资本事件另拆。'),
46:(2,3,1,'针影裁梦24小时回本已入19日卡片；主创谈制作与AI不构成新经营状态。'),47:(0,3,1,'DeepSeek短摘无法核验1元生成具体游戏的流程与条件；转AI审计。'),
48:(1,3,1,'星塔一周年玩法/制作访谈，老品重大生命周期E1，4分；日历独立审计。'),49:(3,3,1,'本期首次召回京东全资游戏服务实体，明确成立日13日，不改写为20日。'),
50:(0,3,1,'招聘综述逐项目拆卡，不能整篇打包。'),51:(3,3,1,'国资与创梦天地共同发起2亿元游戏产业战略投资，10分。'),
52:(0,3,1,'常规半年财报同比下降不满足财报例外；停服/新游/协议另拆。'),53:(0,3,1,'Key公告明确19日；疾病非管理层变更，不推测接任者。'),
54:(3,1,1,'海外PC单机王朝模拟试玩，R1；与158为同稿空白差异，不多算来源。'),55:(3,1,1,'海外PC单机经营试玩，R1；55/159同稿，非两个独立来源。'),
56:(3,1,2,'地渊珠宝匠与23同试玩事件；R1，5分。'),57:(0,3,1,'整机硬件广告。'),58:(0,3,1,'52英文镜像，不能增加独立来源。'),59:(0,3,1,'53英文镜像。'),
60:(1,3,2,'星塔新增常驻自走棋/后宅是老品生命周期E1，5分；日历重大玩法独立准入。'),61:(3,1,2,'36同一余烬试玩；海外单机R1，5分。'),
62:(0,3,1,'硬件广告。'),63:(0,3,2,'37同一Demo更新，非新品首测。'),64:(2,1,1,'乡村模拟新品未来EA与Demo，未证国内/重点主体，R1。'),
65:(1,2,1,'Jeff Kaplan访谈的旧离职与个人感受；新作延期另拆，不把33人团队当新成立。'),
66:(0,3,1,'正文开头明确到访16日，非20日新战略合作；星布谷地旧档期独立审计。'),67:(0,2,1,'AI短剧非游戏直接采用，无具体游戏迁移证据优于本期直接案例，AI审计排除。'),
68:(0,3,1,'SpireBench游戏评测直接应用，转AI，实验为上周研究不伪称20日发表。'),69:(1,3,1,'9日DLC后评测/体验分析，非本期新增状态。'),
70:(0,3,1,'嘉年华定档/售票宣传，非新品或平台政策。'),71:(3,3,1,'国内研发商建立广州发行分部，明确发行组织扩展，10分；产品首月数据为支持事实。'),
72:(2,3,1,'ForgeTax新经营案例，国内复刻产品下载已达30万；与14日原作销量事件匹配，按实质竞争状态变化审计。'),
73:(0,3,1,'海艺AI游戏工作站与Maker内测案例转AI；各不同产品事件另留独立决策。'),
74:(1,1,1,'14日拒绝自愿承认工会，旧海外劳资，2分。'),75:(2,2,2,'付费随机道具评级迁移是全球发行规则，R2；6分边界。'),
76:(0,2,1,'GDC会议日程调整，不是游戏分发规则。'),77:(2,2,2,'美国数字预购结构数据，明确全球大作迁移但非中国/移动，6分；不混作全球销量。'),
78:(0,2,1,'配音AI许可指南转AI；指南不是法律已生效。'),79:(1,3,1,'Mattel/Roblox访谈是8月组织计划复述和战略表态，4分；2月收购不当当前事件。'),
80:(3,2,2,'游戏投资与影视生产组织新合资企业，8分；84/91同主体同一成立事件。'),81:(0,3,1,'会议信息且snippet；Roblox主体仍R3但E0。'),
82:(3,3,1,'Savvy教育MoU符合重点主体重大合作，但仅Cloudflare摘要，不能发布。'),83:(0,3,1,'万圣节活动且snippet。'),
84:(3,2,2,'80同一HITpoint成立，正文用完整80/91。'),85:(1,2,1,'地区会议访谈与市场前景摘要，3分且不可读。'),86:(2,2,2,'75同PEGI规则，非独立新政策。'),
87:(0,3,1,'Supercell停服播客摘要，无新进展且不可读。'),88:(1,2,1,'地铁跑酷累计下载访谈仅摘要，3分。'),
89:(0,3,1,'ReVamp因AI克隆风险缩小公开测试，转AI；与酒鬼女神严格分开。'),90:(2,2,1,'BRUTAL开源是开发框架能力，非游戏首发/资本E3，5分。'),
91:(3,2,2,'80同一HITpoint成立。'),92:(2,2,1,'218字只有审核变慢引语，标题AI归因缺完整正文佐证；5分排除。'),
93:(0,3,1,'恋与深空联动分析，与38同一活动；E0。'),94:(0,1,1,'观影随笔，非游戏行业状态变化。'),95:(0,3,1,'三渲二管线分析，无本期独立发布；留深度审计。'),
96:(0,3,1,'肉鸽设计方法分析，无本期独立新闻事件。'),97:(0,3,1,'重复战斗机制分析，非行业新闻；深度候选留痕。'),
98:(0,1,1,'演员趣闻且snippet。'),99:(1,1,1,'Saros普通BossRush/NG+更新且snippet，不是新品上线。'),
100:(0,1,1,'假想续作点子，并非立项且snippet。'),101:(0,1,1,'云端可玩说明非新品首发，snippet。'),102:(2,3,1,'魔兽用户结构潜在重要，但仅snippet不可核验。'),
103:(0,1,1,'动画内容宣传snippet。'),104:(0,1,1,'动画访谈snippet。'),105:(0,3,1,'老作联动预热snippet，22日未来更新独立日历留痕。'),
106:(2,2,2,'77同一Sensor Tower美国数字预购数据。'),107:(1,1,1,'旧移植收入分成回顾snippet，非新资本变化。'),108:(0,3,1,'堡垒之夜常规联动泄露，snippet。'),
109:(0,1,1,'配乐宣传snippet。'),110:(0,1,1,'订阅内容轮换snippet。'),111:(1,2,1,'Netflix游戏战略评论snippet；无新关停证据。'),
112:(0,1,1,'愚者不灭评测，22日未来发售已知，不是20日上线。'),113:(0,3,1,'游戏片尾致敬；旧逝世不是本期人才变化。'),114:(0,3,1,'Minecraft智能体自主通关转AI。'),
115:(0,3,1,'Riot K/DA音乐单曲，不是名为Firestarter的新游戏。'),116:(0,2,1,'Steam玩家过滤AI诉求转社区候选，尚不是Valve新政策。'),
117:(1,3,1,'现代战争收尾访谈/新子系列历史同事件，无新立项。'),118:(1,1,1,'Saros既有产品更新。'),119:(0,3,1,'已公开MMO射击后续战术视频，不是首曝。'),
120:(2,1,1,'英国9月调查虚拟恋爱态度，海外一般数据3分；争论另审社区。'),121:(2,1,1,'怪物猎人旧作Switch2体验版，R1；未改变全球结构。'),
122:(0,0,1,'非游戏电影。'),123:(0,3,1,'普通免费更新预告。'),124:(0,1,1,'黏土监狱游戏后续视频，未证明首次官宣。'),
125:(2,1,1,'驾驶模拟老品PS5移植，弱迁移3分。'),126:(3,3,1,'多人共斗新Demo；缺明确PVP或RPG/国内主体，仅协作动作不足R3，复核降R1。'),
127:(3,1,1,'PC单机找针试玩，未知主体R1。'),128:(2,1,1,'冰汽时代Switch老品移植，R1。'),129:(0,0,1,'纯海外主机成本传闻，非产业迁移。'),
130:(0,3,1,'GTA6开发回顾，非本期首曝或定档变化。'),131:(0,1,1,'影视积木周边，非游戏。'),132:(0,1,1,'电影开发状态，非游戏立项。'),
133:(0,1,1,'FF共鸣评测，旧手游重做买断的产品型态讨论，不是本期新发售。'),134:(0,3,1,'限时联动PvE模式，不按重大生命周期入行业。'),
135:(0,1,1,'Steam预排清单逐产品审计，不能整篇一张新闻卡。'),136:(0,1,1,'DIY手柄个人项目。'),137:(0,3,1,'既有GTA5模组体验，不是本期商业状态。'),
138:(0,2,1,'Xbox员工AI表态后销号，转AI候选，不能称公司新政策。'),139:(1,2,1,'星战IP对合作伙伴更开放的访谈表态，无本期签约，3分。'),
140:(0,3,1,'战术游戏普通补丁；末尾恢复停薪员工另拆E1，不能整篇抬组织E3。'),141:(0,3,1,'89同一ReVamp测试变更，转AI。'),142:(0,3,1,'攻略选址。'),
143:(0,1,1,'SteamDeck插件个人功能，不是Valve政策。'),144:(2,2,1,'Proton加入XeSS请求，提案非已上线，5分。'),145:(0,0,1,'路由器产地事件非游戏。'),
146:(1,3,1,'Subnautica2 EA内容计划，未给上线日期，老品生命周期4分。'),147:(0,1,1,'键盘轴体音效库，非游戏行业。'),148:(0,1,1,'十余年前销售经验回顾，非当前数据。'),
149:(0,0,1,'VR屏保趣闻，CAD开放为上周背景。'),150:(2,2,1,'非官方实验GamePass兼容项目，非微软/Valve渠道开放政策，5分。'),
151:(3,1,1,'海外单机PC试玩与11月12日未来档期，R1。'),152:(1,3,1,'赛博朋克2.5未来双持玩法，老品节点4分。'),153:(0,0,1,'显卡硬件装饰版。'),
154:(0,2,1,'Deezer13日宣布AI过滤，非本期游戏采用，AI审计排除。'),155:(0,3,1,'欢乐斗地主20周年营销复盘，历史2006/2008上线不能作新品。'),
156:(1,3,1,'19日少前2新模式已入19日日历；本期访谈不重写上线日，行业4分。'),157:(0,3,1,'高校赛事宣传，非资本/组织变化。'),158:(3,1,1,'54同稿英文空白差异，来源去重。'),159:(3,1,1,'55同稿多一个尾标，来源去重。')}
hist={9:['战地风云6'],10:['英雄联盟'],13:['使命召唤'],42:['艾希：续'],45:['Metacore'],46:['针影裁梦'],72:['ForgeTax'],87:['Squad Busters'],117:['使命召唤']}
ai_ids={40,43,44,47,67,68,73,78,89,114,138,141,154}
include_ids={20,49,51,71,72,80}
merges={56:23,61:36,63:37,84:80,86:75,91:80,106:77,158:54,159:55,58:52,59:53,93:38}
for i in range(1,160):
    if i in ai_ids:continue
    e,r,m,why=spec[i]
    if i==126:r=1
    d=add(f'I{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],e,r,m,why,include=i in include_ids,history=hist.get(i,()))
    if i in merges:d.update(decision='merge',merge_into=f'I{merges[i]:03}')
    if i==72:
        d['history_check'].update(novelty='material_update',new_facts=['国内TapTap复刻产品《铸剑大师模拟器》下载已达30万次，显示原作机制已进入国内移动分发；此前历史只有原作VGI销量与玩法。','本期Gamalytic估算原作超过25万份、375万元；与历史VGI估算口径不同，不计算净增幅。'])
        d['new_fact_evidence']=[{'source_id':sid(72),'evidence':proof(72,'已经获得了30万次下载')},{'source_id':sid(72),'evidence':proof(72,'超过25万份')}]
    if i==49:d['event_date']='2026-10-13'
# Individual project cards from the full recruiting investigation: dates are observations, not launch announcements.
projects=[
('RAID','腾讯光子《RAID PROJECT》招聘披露原创战术射击方向',['腾讯','光子','RAID PROJECT'],'光子原创IP',3,'具体命名在研项目及UE5/战术射击定位首次本期召回，E3R3；不声称20日立项。'),
('HIGAME','光子H.STUDIO为《Higame》招募开放世界RPG团队',['腾讯','H.STUDIO','Higame'],'人与怪谈共存',3,'明确独立项目名、研发归属、玩法与岗位，E3R3；招聘线索不是正式发布。'),
('MHY_ACTION','米哈游招聘透露UE5写实奇幻动作预研',['米哈游','UE5动作预研'],'超大型Boss战',3,'未曝光独立动作预研有写实奇幻/多人机制证据，10分；不与其他项目打包。'),
('MHY_MMO','米哈游生活MMO预研强调多剧本角色扮演和社交模拟',['米哈游','生活MMO预研'],'多剧本角色扮演和社交模拟',3,'独立预研题目与核心机制明确，10分。'),
('MHY_SHOOTER','米哈游UE5写实射击预研招聘低延迟战斗岗位',['米哈游','UE5写实射击预研'],'低延迟强实时战斗',3,'独立在研写实射击有服务端生态证据，10分。'),
('MHY_MOBA','米哈游UE5 MOBA预研招聘线索',['米哈游','UE5 MOBA'],'在研UE5 MOBA',1,'只有方向名称，未提供具体产品或新立项状态，E1R3=4。'),
('MHY_SANDBOX','米哈游沙盒预研招聘线索',['米哈游','沙盒预研'],'在研沙盒项目',1,'只有方向名称，不能仅由岗位归纳为正式首曝E3，4分。'),
('LILITH','莉莉丝猫爪拿铁动物都市生活模拟研发',['莉莉丝','猫爪拿铁'],'今年9月',1,'原文明确9月公开招聘，当前是既有线索回顾，不作为20日首曝。'),
('NAMI','库洛《代号NAMI》招聘透露全平台多人共斗ARPG',['库洛','代号NAMI'],'目标覆盖PC、主机、移动端全平台',3,'独立项目代号、UE5、型态、平台均明确，10分；与库洛入股言之域不同事件。'),
('SUN','库洛《代号SUN》招聘指向载具与大规模团队战',['库洛','代号SUN'],'大规模团队战',3,'独立命名在研项目有载具、开放世界动作竞技线索，10分；不包装为正式官宣。'),
('XISHAN','西山居招聘浮现历史国风赛季SLG新游',['西山居','历史国风赛季SLG'],'一款历史国风赛季SLG新游',3,'一个独立产品及商业化/用户运营岗位明确，10分；可能跨端的猜测不写成事实。'),
('EAGLE','鹰角UE项目跨平台技术招聘',['鹰角','UE项目'],'跨平台性能',1,'泛技术职责不能推出未披露的产品类型或正式立项状态，4分。'),
('BYTE','字节多个工作室招聘细分游戏人才',['字节'],'CCG卡牌',1,'职位覆盖不等于一个命名独立新品，4分；各品类只保留观察，不能捏造新项目。'),
('PERFECT','完美世界出海SLG与休闲研发岗位',['完美世界'],'出海SLG',1,'既有招聘方向、没有产品名/首次节点，4分。'),
('PAPER','叠纸AI原生及UE研发岗位',['叠纸'],'AI原生项目',1,'招聘说明计划方向，未证已采用或一个可识别的首曝项目，4分。'),
('FUNPLUS','FunPlus古风仙侠及航海SLG研发岗位',['FunPlus'],'古风仙侠、航海SLG',1,'方向线索无新增立项节点，4分。'),
('GIANT','巨人国风卡牌及SLG研发方向',['巨人网络'],'国风卡牌、SLG+X',1,'泛招聘方向非具体首次公开项目，4分。'),
('CENTURY','世纪华通在研手游与点点休闲管线',['世纪华通','点点互动'],'背包like',1,'既有岗位与储备品类，未给新项目状态变化，4分。'),
('NETEASE','网易雷火国风二次元研发岗位',['网易','雷火'],'2026年9月招聘',1,'明确9月招聘，不能改写当前首曝；商标线索另卡。')]
for key,title,ents,needle,e,why in projects:
    d=add('J_'+key,[50],ents,title,e,3,1,why,include=e==3)
    d['evidence_anchors']=[{'source_id':sid(50),'evidence':proof(50,needle)}];d['observation_as_of']='2026-10-08';d['publication_date']='2026-10-20'
add('J_NETEASE_TM',[50],['网易','ECC:Redline'],'网易注册ECC:Redline商标线索',3,3,1,'有未公布新作商标和MMORPG描述，但未能核实注册发生在本期；保留候选，不将外界对燕云团队的猜测写为事实。',include=False,event_date='unknown')
# Composite stories must not bury unrelated capital/product events.
for key,ids,ents,event,e,r,m,why,h in [
('FLOW',[45],['腾讯','Flow Games'],'腾讯领投Flow4600万美元',3,3,1,'13日融资历史已曝光；16日累计4900万为融资总量重述，没有新融资轮次。',['Flow Games']),
('CIRCLE',[45],['腾讯','Circle Games'],'Circle2500万美元A轮',3,3,1,'明确9月24日的旧投资，仅背景，不当本期融资。',[]),
('FUNDS_TR',[45],['土耳其手游市场'],'2025年土耳其开发商移动内购规模',2,2,1,'2025年数据无本期新报告日期及方法，5分。',[]),
('FISH_CLOSE',[52,58],['飞鱼科技','神仙道3'],'神仙道3宣布12月9日停运',2,3,2,'旧停服事件历史卡片曝光，重复。',['神仙道3']),
('FISH_TENCENT',[52],['飞鱼科技','腾讯'],'2026年4月至2028年腾讯合作框架',3,3,1,'明确始于4月的旧协议；无20日新签署/实质状态，排除。',[]),
('FISH_NEW',[52],['飞鱼科技','下方了'],'9月新游榜单与产品储备',1,3,1,'9月上线及纯榜单，非本期新发售；未来跨端产品未命名，4分。',[]),
('JEFF_DELAY',[65],['Kintsugiyama','加利福尼亚传奇'],'EA推迟到2027年',2,2,1,'延期是独立产品状态，5分；无国内/移动或PVP证据。',[]),
('MATTEL_BUY',[79],['Mattel','网易'],'Mattel163全资收购',3,3,1,'明确2月收购，当前访谈仅背景，窗口外。',[]),
('BIT_REHIRE',[140],['Bit Reactor'],'Zero Company成功后恢复停薪员工',1,2,1,'员工回归不是新收购/核心管理更换，3分。',[]),
('RIMWORLD',[90],['Rimworld'],'上周迁出Unity至Waylith',1,3,1,'上周旧更新与案例，E1R3=4。',[]),
('RUST_YAN',[4],['餍'],'餍新预告片',0,1,1,'后续PV并非首次官宣。',[]),
('RUST_BLOOD',[4],['血墨诡案'],'血墨诡案新预告片',0,1,1,'后续PV并非首次官宣。',[]),
]:add('X_'+key,ids,ents,event,e,r,m,why,history=h)
# PC-only scope quotes for every potentially recognisable launch candidate.
for d in D:
    if d['section']!='industry_news':continue
    i=int(d['source_ids'][0][1:]);text=S[d['source_ids'][0]]['text']
    if any(w in text for w in ['Steam','PC','PS5','Switch','Windows','主机','端游']):
        quote=next((l for l in text.splitlines() if any(w in l for w in ['Steam','PC','PS5','Switch','Windows','主机','端游'])),text.splitlines()[0])
        focus=d['candidate_id'].startswith('J_') or i in [28,34,42,48,49,50,52,60,63,66,71,79,115,156]
        multiplayer=i in [20,119,126]
        classification='domestic_or_focus' if focus else 'multiplayer_or_other' if multiplayer else 'ordinary_overseas_single_player' if i in [1,3,4,15,23,24,30,31,33,36,54,55,56,61,64,99,112,118,121,124,125,127,128,133,151,158,159] else 'multiplayer_or_other'
        d['pc_release_scope']=dict(classification=classification,basis='原文明确国内厂商/产品或重点主体关系；事件类型仍独立审计。' if focus else '原文明示多人合作/射击或不是纯发售消息，按实际事件与迁移点评分。' if classification=='multiplayer_or_other' else '普通海外或主体未明PC/主机单机发布，类型标签不提高相关性R1。',evidence=[dict(source_id=d['source_ids'][0],evidence=quote)])
# AI reverse scan: preserve event boundaries, including excluded direct and frontier cases.
ai_in={43,68,73,78,89,114}
ai_reason={40:'反编译综述延续旧工具/旧案例，无本期独立新部署；不重复19日同议题。',43:'已展示Blender/引擎实际原型制作；按作者演示归因，不能把Demo当量产。',44:'酒鬼女神取消试玩已在周末AI栏报道，本期无新变更。',47:'132字概述无法核验1元生成具体条件，完整本期直接案例优先。',67:'短剧产能分析，没有直接游戏采用且本期直接案例优先。',68:'SpireBench在真实游戏测试长线策略，实验样本与人类对照限制一并保留。',73:'SeaGames资产工作站已上线、Maker内测，明确微信/抖音工程输出，不能写成全面公开发布。',78:'配音生成/翻译的事前许可与报酬指南，直接约束游戏内容制作，非已立法。',89:'ReVamp实际缩减公开测试，AI克隆直接改变游戏研发与发行取证方式。',114:'谷歌智能体在Minecraft完成长任务，明确多智能体协调和实际开销。',138:'员工AI表态后的个人销号，不是Xbox新组织政策；背景Labs已曝光。',141:'89同一ReVamp测试变更，合并原文引语。',154:'Deezer13日AI过滤旧公告，不是游戏新落地。'}
for i in sorted(ai_ids):
    d=add(f'A{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],section='ai_trends',reason=ai_reason[i],include=i in ai_in,ai_tier='direct_application' if i not in [47,67,154] else 'transferable_frontier',game_stage=['development','publishing'] if i in [44,89,141] else ['development','product'],industry_reverse_scan=True)
    if d['ai_tier']=='transferable_frontier':d['migration_path']='生成能力/成本或筛选机制可迁移到游戏资产制作与UGC分发，但当前正文不足或时点旧，直接游戏案例优先。'
    if i==141:d.update(decision='merge',merge_into='A089')
for i in range(160,183):
    why={160:'工程意图验证可迁移游戏代码与测试，但本期已有六个游戏直接作用事件，优先直接采用。',161:'有Curvytron实际托管示例，但核心为通用会话基础设施；可迁移语音NPC连续状态，本期直接AI游戏案例优先。',162:'蛋白质研究非游戏，缺具体迁移链。',163:'TPU推理后端常规平台扩展，未有游戏采用或改变成本的可比证据。',164:'8月风险报告评审、泛AI对齐，非游戏具体治理事件。',165:'通用TPU训练框架与调优，不单独用泛AI更新占位。',166:'模型上线与参数宣传，没有具体游戏采用。',167:'隐藏提示治理可迁移游戏客服，但当前是WhatsApp案例，无游戏落地。',168:'WebDev榜单，非具体游戏应用。',169:'通用模型排名例行更新，不凭开源标签入选。',170:'扩散推理价格与速度有潜在实时NPC迁移，但无实际游戏延迟/质量验证，直接案例优先。',171:'与169同模型但独立榜单事件，保留独立决策不合并；无游戏采用。',172:'窃密法律新闻无游戏直接或清晰迁移。',173:'企业记忆架构可迁移NPC持续记忆，但无游戏部署；19日已有NPC记忆专题，本期优先直接新事件。',174:'反诈应用，无游戏直接案例。',175:'端侧技术仅导读，缺完整部署与质量证据；不将8日前模型开源当20日新发。',176:'自动驾驶非游戏。',177:'公平性基准非游戏、未展示游戏治理环节采用。',178:'一般AI融资，不提供游戏迁移事实。',179:'推理框架只有导读，无完整正文部署取证。',180:'服务基础设施成本案例可迁移游戏NPC与研发代理，但目前为通用工程基准，本期直接事件优先。',181:'军事网络武器非游戏。',182:'视频工作流提示词的转载分析，非游戏采用，内嵌工具指令只是原文资料。'}[i]
    add(f'A{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],section='ai_trends',reason=why,ai_tier='transferable_frontier',game_stage=['development'],industry_reverse_scan=False,migration_path='审计潜在游戏研发/运营迁移；本期未满足具体采用或完整取证，故排除。')
# Raw calendar sources also compete in industry independently.
calendar_industry={183:(0,3,1,'二重螺旋常规版本；事故转社区。'),184:(0,3,1,'元气骑士常规版本。'),185:(0,3,1,'穿越火线常规版本。'),186:(0,3,1,'仙侠世界2普通资料片，无核心机制重构证据。'),187:(0,3,1,'二重螺旋新角色，普通运营。'),188:(0,3,1,'使命召唤老品体验服，不是新品首测。'),189:(0,3,1,'元气骑士普通版本。'),190:(2,3,1,'国服正式首曝是地域/市场扩展节点，海战竞技，7分。'),191:(3,3,1,'放置地牢RPG首次试玩节点，无PC单机限定，优先赛道10分；不补厂商和平台。'),192:(0,1,1,'只有将于海外上线，无日期/主体，不能当正式定档。'),193:(3,1,1,'PC/主机动作RPG试玩，主体未知R1。'),194:(0,3,1,'注册得资格仅测试招募/预下载提示，未证实际首测已开启。'),195:(3,3,1,'放置卡牌角色扮演新品正式上线，10分；不凭武侠名猜开发商。'),196:(2,3,1,'新品预下载，像素RPG，7分；21日上线为明示绝对日期。'),197:(2,3,1,'多人格斗新品预下载，PVP赛道7分。'),198:(3,3,1,'像素JRPG新品正式上线，10分。'),199:(3,1,1,'多人哥特新游上线，但无RPG/PVP/国内主体明确证据，4分。'),200:(3,1,1,'女性向音游首测，未明确生活模拟或国内主体，弱迁移4分。'),201:(2,3,1,'策略卡牌新作预下载，7分；23日上线未发生。'),202:(2,3,1,'篮球经营新品预下载，经营优先赛道7分。')}
for i,(e,r,m,why) in calendar_industry.items():
    add(f'I{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],e,r,m,why,include=e*r+m>=7)
for i in range(203,214):
    add(f'I{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],1 if i==212 else 2,1,1,'单一海外档期/主机移植摘要，无中国移动或固定重点主体依据；纯发售不凭RPG标签取R3。',pc_release_scope={'classification':'ordinary_overseas_single_player','basis':'只有海外PC/主机档期或移植摘要；无例外依据，R1。','evidence':[{'source_id':sid(i),'evidence':S[sid(i)]['text'].splitlines()[0]}]})
# Full release list separately scored for industry, never bundled.
guide=S[sid(135)]['text']
for k,m in enumerate(re.finditer(r'([^\n]+)\n关键字：\s*([^\n]+)\n发行日期：\s*(2026/10/\d+)',guide)):
    name,genre,date=m.groups();d=add(f'G{k:02}',[135],[name],name+' '+date+'发行清单',3,1,1,'预排列表中的普通海外/主体未知PC单机，R1；日历独立判断多源和日期。',pc_release_scope={'classification':'ordinary_overseas_single_player','basis':'清单来自Steam/SteamDB，未给国内/重点主体或实质移动迁移关系。','evidence':[{'source_id':sid(135),'evidence':m.group(0)}]})
# Community: same-window follow-up scan excludes all Oct21 replies from claims.
community_reason={214:'周末已报同一优化问题，20日回复多转向奖励/角色数值，无同一性能事故实质新进展。',215:'20日新周边命名修改争论，有明确触发与玩家逻辑；不使用21日回复。',216:'20日新立绘AI质疑，有事件但与215同产品新周边争论相比证据仅看图推断，受2条上限排除；不当已证AI。',217:'原帖3日、末页摘录截至11日，元数据20日活跃不证明新增可读进展。',218:'9日旧话题，20日仅玩家推测本地服务实现与回坑意愿，不把复活当官方上线。',219:'2日旧文本争议，20日只有追问改了什么，无新事实。',220:'16日旧素材争议周末已报；20日单一回复称好像改了，缺前后图证不作为新官方整改。',221:'19日健康消息及怀念，非可命名游戏商业争议；不转述玩家医学猜测。',222:'19日起演唱会签证取消争论延续，但本期更强国产新事故优先，正文上限2。',223:'未给原始欠薪/版权资料，玩家对辉烬改单机判断不足以当官方状态。',224:'18日联动角色先实装话题，20日主要声优/旧角色比较，无新节点。',225:'泛求推荐，无独立公共事件。',226:'20日1.7开服后进服/掉线、22:30扩容维护，为新事故；21日0点恢复与补偿不写成20日完成。',227:'16日旧本地化争议且帖内质疑缺对比，20日仅旧争论延续。',116:'Steam新品节玩家要求AI过滤，事件合格但未成政策；受2条上限排除。',120:'英国虚拟恋爱民调旧9月；本期国内事故优先。'}
for i,why in community_reason.items():
    comm=dict(trigger=S[sid(i)]['title'],claim_scope='玩家/帖子主张；非官方确认',complaint_logic='具体争议见全文候选，发布条目逐句取证。',timeline='保留原帖与报告日节点，只使用截至2026-10-20 23:59的可读材料。',follow_up_scan={'scope':'全部14条社区 +159条行业正文，按产品名、机制、回应/修改/维护等关键词逐段补扫。','source_ids':[s for s,x in S.items() if x['section'] in ['community_discourse','industry_news'] and any(w in x['text'] for w in (['二重螺旋','1.7','扩容'] if i==226 else ['测量套件','游标','卡尺'] if i==215 else [S[sid(i)]['title'].split(']')[-1]]))],'result':'没有同窗口独立官方原文；正文用帖子称、玩家质疑归因，不追加免责尾注。'})
    add(f'C{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],section='community_discourse',reason=why,include=i in [215,226],community=comm)
# Newsletter intake first, followed by eligible current-event synthesis.
for i,sc,why in [(228,(2,2,2,2),'优先读完整newsletter；复古硬件与手机业务占核心、销量/收入缺统一周期，游戏结构性迁移不足，8分排除。'),(229,(1,1,1,1),'215字摘要，没有完整机制与游戏证据，4分。'),(230,(0,2,2,1),'数字银行报告非游戏，不因Sea主体就作Garena游戏，5分。')]:
    add(f'D{i:03}',[i],[S[sid(i)]['title']],S[sid(i)]['title'],section='deep_analysis',reason=why,scores=dict(zip(['relevance','insight','evidence','card','total'],[*sc,sum(sc)])),source_priority='configured_newsletter')
for cid,ids,title in [('D_PIPELINE',[43,73],'AI游戏工具的交付重点从生成资产转向工程可用性'),('D_DEMO',[72,89,141],'AI复刻风险让公开试玩同时承担获客与泄露成本')]:
    add(cid,ids,[title],title,section='deep_analysis',reason='本期已选事件组成机制分析，多个独立案例支持；与19日NPC/校招深度不撞题。',include=True,scores=dict(relevance=3,insight=3,evidence=3,card=3,total=12),source_priority='current_selected_events')
save('selection_decisions.json',{'anchor':{'type':'daily','date':'2026-10-20'},'decisions':D})
# Calendar: preserve raw extraction, then full-body recall and deterministic ranking.
raw=P/'release_calendar_audit.raw.json'
if not raw.exists():raw.write_bytes((P/'release_calendar_audit.json').read_bytes())
A=json.loads(raw.read_text(encoding='utf-8'));nodes=A['nodes']
def node(product,date,sg,event,ids,why='',valid=True):
    nodes.append(dict(candidate_id='R_ADD_'+str(len(nodes)+1),product=product,event_date=date,signal_type=sg,event=event,event_type_score={'new_game_test':3,'new_game_launch':3,'new_game_preload':2,'new_game_first_reveal':2,'new_game_schedule':2,'old_major_update':1,'old_cross_platform_launch':1,'old_relaunch':1}[sg],source_ids=[sid(i) if isinstance(i,int) else i for i in ids],observed_signal_types=[sg],observed_events=[event],focus_companies=[],focus_company_relationships={},company_evidence_ids=[],company_relationship='none',company_bonus=0,editorial_reason=why,editorial_valid=valid))
for n in nodes:
    p=n['product'];n['editorial_valid']=True;n['editorial_reason']='全文复核日期、产品型态与重复；不以行业是否入选影响日历。'
    if p in ['小小港湾','钓遍海里的鱼','锈都残日','基机受难记']:n.update(signal_type='new_game_test' if p!='基机受难记' else 'new_game_launch',event='试玩版开放' if p!='基机受难记' else '正式发售')
    if p=='小小港湾':n.update(editorial_valid=False,editorial_reason='正文为试玩不是完整发售；55/159正文仅尾标不同，同稿去重后1源，且正文只有今天无绝对月日。')
    if p=='欢乐斗地主':n.update(event_date='2006',editorial_valid=False,editorial_reason='2006年首发与2008年手机上线是历史，不是20日新品。')
    if p=='星布谷地':n.update(event_date='2026-冬季',editorial_valid=False,editorial_reason='明确16日到访中的既有冬季计划，非本期新定档；不造具体日期。')
    if p=='Firestarter':n.update(editorial_valid=False,editorial_reason='K/DA单曲不是游戏。')
    if p=='Smash Fest':n.update(event_date='2026-05',editorial_valid=False,editorial_reason='明确5月上线，当前是融资背景。')
    if p=='神仙道':n.update(event_date='2011-05',editorial_valid=False,editorial_reason='2011年历史首发，3代停服不是新品。')
    if p=='龙之信条2':n.update(event_date='2026-10-09',signal_type='old_major_update',event_type_score=1,editorial_valid=False,editorial_reason='DLC9日上线，窗口外。')
    if p=='弹壳战机':n.update(event_date='2026-09-20',editorial_valid=False,editorial_reason='9月20日上线，首月成绩不是20日新上线。')
    if p=='ForgeTax':n.update(event_date='2026-09-30',editorial_valid=False,editorial_reason='9月30日上线，当前销量/复刻分析不是新品。')
    if p in ['SeaHaze','SeaVerse','SeaGames','No WiFi Mini Games']:n.update(event_date={'SeaHaze':'2026-03','SeaVerse':'2026-01','SeaGames':'2026-08','No WiFi Mini Games':'2026-06'}[p],editorial_valid=False,editorial_reason='原文给出历史上线月份，不造具体日期。')
    if p=='VibeShort':n.update(event_date='2026-上半年',editorial_valid=False,editorial_reason='海外短剧App，非游戏；历史上半年上线。')
    if p=='沙罗周期':n.update(signal_type='old_major_update',event_type_score=1,editorial_valid=False,editorial_reason='BossRush/NG+普通版本功能，未达重大生命周期门槛。')
    if p in ['BeamNG.drive','冰汽时代']:n.update(signal_type='old_cross_platform_launch',event_type_score=1,editorial_valid=False,editorial_reason='旧品移植符合召回但单源、绝对发生日无证。')
    if p=='上古卷轴OL':n.update(editorial_valid=False,editorial_reason='普通赛季地下城不是首次曝光/定档。')
    if p=='酒鬼女神的酒诡':n.update(editorial_valid=False,editorial_reason='公开测试已经取消，且旧期已报道。')
    if p=='艾希：续':n.update(event_date='2027-05-01',editorial_valid=False,editorial_reason='18日Q&A既有计划在20日被分析，非本期首次定档。')
    if p=='余烬之镇':n.update(event_date='2026-10-27',event='EA定档',editorial_valid=True)
    if p=='GTA6':n.update(event_date='2026-11-19',editorial_valid=False,editorial_reason='开发回顾中的既有发售日，非新定档。')
    if p=='使命召唤手游':n.update(editorial_valid=False,editorial_reason='老品体验服资格公布，非新品。')
    if p=='重返地心之下':n.update(editorial_valid=False,editorial_reason='注册得测试资格未证实际首测已开启。')
    if p in ['守护庄园','拳皇·命运','美职篮奇迹梦之队']:n.update(signal_type='new_game_preload',event_type_score=2,event_date='2026-10-20',event='预下载，21日上线')
    if p=='征战王权':n.update(signal_type='new_game_preload',event_type_score=2,event='预下载，23日上线')
    if p=='怪物猎人 荒野':n.update(event='Switch2序章体验版',editorial_valid=True)
# Full-text current-node recall, preserving tests versus later schedules.
node('余烬之镇','2026-10-20','new_game_test','Steam免费试玩',[36,61])
node('地渊珠宝匠','2026-10-20','new_game_test','Steam公开试玩',[23,56],'有两份不同来源，但正文目前/现已缺绝对月日，校验所需日期证据不足，不人工改写source。',False)
node('中世纪崛起','2026-10-19','new_game_test','新品节试玩',[54,158],'同一发布稿空白差异去重1源；19日开始，窗口外。',False)
node('星塔旅人','2026-10-20','old_major_update','新增常驻自走棋与后宅玩法',[48,60],'仅以两个常驻核心玩法扩展入选，不以签到/周年福利填充。')
node('斩月封魔录','2026-10-20','new_game_test','新品节Demo更新',[37,63],'正文明确已有Demo更新，不是首次测试。',False)
node('少女前线2：追放','2026-10-19','old_major_update','危区探遗搜打撤',[156],'19日已进入产品日历，当前为访谈，没有新上线节点。',False)
node('复兴吧温泉镇！','2026-12-07','new_game_schedule','Steam EA定档',[64])
node('复兴吧温泉镇！','2026-10-20','new_game_test','新品节试玩',[64],'仅单源，开放日无绝对月日。',False)
for p,i in [('追逐末日之光',15),('龙骨海盗',20),('HR.SOS',24),('莱露',26),('定海',28),('去月球 传奇RPG 之最终一小时',30),('艾尔塔：逆神',31),('规则怪谈',34),('滑板骑士',35),('地城扫雷Plus',35),('明日英雄：伦敦',126),('Find The Needle',127),('500 Finger Fillet',151)]:
    node(p,'2026-10-20','new_game_test','试玩/新品节节点',[i],'单源；定海/规则怪谈等未证明首次试玩，不能把每次新Demo版本当首测。',p not in ['定海','规则怪谈','莱露','滑板骑士','地城扫雷Plus'])
for i in range(203,214):
    t=S[sid(i)]['text'];title=t.splitlines()[0][7:];match=re.search(r'Parsed release date: ([^\n]+)',t)
    p=title.split(' launches')[0].split(' coming')[0].split(' adds')[0].split(' now available')[0]
    dt=match.group(1) if match else '2026-10-20' if i==205 else '2027' if i in [203,207,209] else 'unknown'
    sg='old_major_update' if i==212 else 'old_cross_platform_launch' if i in [204,205,206,209,213] else 'new_game_schedule'
    node(p,dt,sg,title,[i],'单一Gematsu RSS记录，不补造完整页面或具体日期。',i!=212)
for k,m in enumerate(re.finditer(r'([^\n]+)\n关键字：\s*([^\n]+)\n发行日期：\s*(2026/10/\d+)',guide)):
    name,genre,dt=m.groups();node(name,dt.replace('/','-'),'new_game_launch','Steam预排发售',[135],'只有预排清单，无第二独立来源。')
for p,i in [('二重螺旋',183),('元气骑士',184),('穿越火线',185),('仙侠世界2',186)]:node(p,'2026-10-20','old_major_update','新版本/资料片',[i]+([187] if i==183 else [189] if i==184 else []),'普通版本/新角色/资料片不满足重大玩法生命周期门槛。',False)
for p,dt,i in [('守护庄园','2026-10-21',196),('拳皇·命运','2026-10-21',197),('美职篮奇迹梦之队','2026-10-21',202),('征战王权','2026-10-23',201)]:node(p,dt,'new_game_launch','预下载记录披露未来上线',[i])
group={}
for n in nodes:
    key=n['product'],n['event_date']
    if key not in group:group[key]=n;continue
    b=group[key];b['source_ids']=list(dict.fromkeys(b['source_ids']+n['source_ids']));b['observed_signal_types']=list(dict.fromkeys(b.get('observed_signal_types',[])+n.get('observed_signal_types',[])));b['observed_events']=list(dict.fromkeys(b.get('observed_events',[])+n.get('observed_events',[])))
nodes=list(group.values())
def fingerprint(x):
    # Whitespace/bullet/end-marker-only differences are still the same article.
    t=re.sub(r'[\s#·*]+','',x['text']);return hashlib.sha1(t.encode()).hexdigest()
for n in nodes:
    ids=n['source_ids'];unique={}
    for s in ids:
        x=S[s];signature=fingerprint(x);unique.setdefault(signature,s)
    n['source_fingerprints']=list(unique);n['appearance_count']=len(unique);n['appearance_score']=min(3,len(unique));n['industry_ids']=[s for s in ids if S[s]['section']=='industry_news'];n['release_ids']=[s for s in ids if S[s]['section']=='release_calendar'];n['industry_bonus']=int(bool(n['industry_ids']));n['source_strength_score']=n['appearance_score']+n['industry_bonus']
    n['base_priority_score']=n['event_type_score']*n['source_strength_score'];n['priority_score']=n['base_priority_score']+n['company_bonus'];n['first_seen_order']=min(int(s[1:]) for s in ids)
    dt=n['event_date'];sg=n['signal_type'];n['window_scope']='report_window' if dt=='2026-10-20' else 'next_day_lookahead' if dt=='2026-10-21' else 'future_announcement' if sg in ['new_game_schedule','new_game_first_reveal'] else 'outside';n['window_eligible']=n['window_scope']!='outside';n['multi_source_eligible']=len(unique)>=2;n['publish_eligible']=bool(n['multi_source_eligible'] and n['window_eligible'] and n.get('editorial_valid',True));n['coverage']='industry_and_release' if n['industry_ids'] and n['release_ids'] else 'industry_only' if n['industry_ids'] else 'release_only'
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
A['nodes']=nodes;A['editorial_audit']='全量industry/release逐段扫描；原抽取保留raw；修正试玩/历史日期/音乐误识别，同稿独立来源去重；日历与行业独立。'
save('release_calendar_audit.json',A)
save('full_input_scan.json',{'records':len(S),'sources':[dict(source_id=s,section=x['section'],title=x['title'],body_status=x['body_status'],chars=len(x['text']),sha256=hashlib.sha256(x['text'].encode()).hexdigest(),paragraphs=len(x['text'].splitlines()),decision_ids=[d['candidate_id'] for d in D if s in d['source_ids']]) for s,x in S.items()]})
save('history_read_audit.json',{'history_window':HJ['history_window'],'occurrences':H,'markdown_sha256':hashlib.sha256((P/'industry_history_14d.md').read_bytes()).hexdigest()})
print('industry',[(d['candidate_id'],d['scores']['total']) for d in D if d['section']=='industry_news' and d['decision']=='include'])
print('calendar',[(n['product'],n['event_date'],n['priority_score']) for n in nodes if n['publish_eligible']])
