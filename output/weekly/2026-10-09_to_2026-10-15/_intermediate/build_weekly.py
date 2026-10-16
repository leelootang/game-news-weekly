import json,re,sys,hashlib,datetime,importlib.util
from pathlib import Path
ROOT=Path.cwd(); P=Path(__file__).parent; OUT=P.parent
ID='2026-10-09_to_2026-10-15'; START='2026-10-09'; END='2026-10-15'
rows=[json.loads(x) for x in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
S={x['source_id']:x for x in rows}; decisions=[]; items=[]; consumed=set()
H=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))['occurrences']
def dump(path,x): path.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def evidence(sid,needle):
    t=S[sid]['text']; pos=t.find(needle)
    if pos<0: raise ValueError(f'Missing evidence {sid}: {needle}')
    a=t.rfind('\n',0,pos)+1; b=t.find('\n',pos+len(needle)); b=len(t) if b<0 else b
    if b-a>1800:
        a=max(t.rfind('。',a,pos)+1,a); q=t.find('。',pos+len(needle)); b=min(b,q+1) if q>=0 else b
    return t[a:b].strip()
def history(terms=(),novelty=None,new=()):
    matches=[h for h in H if any(t.lower() in (h['title']+' '+h['event']+' '+' '.join(h['entities'])).lower() for t in terms)]
    return {'history_match':bool(matches),'novelty':novelty or ('repeat_only' if matches else 'new_event'),
      'prior_occurrences':[f"{h['report_kind']} {h['report_window']['start']}_to_{h['report_window']['end']}｜{h['title']}｜card_exposed={h['card_exposed']};rank={h['card_rank']};limit={h['card_limit']};source={h['card_exposure_source']}" for h in matches],
      'new_facts':list(new),'prior_card_exposed':any(h['card_exposed'] for h in matches) if matches else None}
def add(cid,section,title,ids,facts,score=None,entities=None,event_date=None,reason='',hist=None,**extra):
    body=''.join(f[0] for f in facts)
    claims=[]
    for sentence,sid,needles in facts:
        for needle in ([needles] if isinstance(needles,str) else needles):
            claims.append({'claim':sentence,'source_id':sid,'evidence':evidence(sid,needle)})
    it={'candidate_id':cid,'section':section,'title':title,'source_ids':ids,'claims':claims,'body':body}
    d={'candidate_id':cid,'section':section,'event':title,'event_date':event_date or S[ids[0]]['date'],
       'source_ids':ids,'entities':entities or [title],'decision':'include','reason':reason or '来源正文可核验，达到本分区门槛'}
    if len(ids)>1:
        d['cluster_basis']={'subject':(entities or [title])[0],'product':title,'event_date':event_date or S[ids[0]]['date'],'event':title}
    if score:
        e,r,m=score;d['scores']={'event':e,'relevance':r,'hook':m,'total':e*r+m}
    if section=='industry':d['history_check']=hist or history()
    d.update(extra);items.append(it);decisions.append(d);consumed.update(ids)
    return it,d
def ind(cid,title,ids,facts,score=(3,3,2),entities=None,event_date=None,hist=None,**kw):
    return add(cid,'industry',title,ids,facts,score,entities,event_date,hist=hist,**kw)

ind('I001','网易《极限战场》正式首曝，首轮PC测试定于10月15日',['S0041','S0043','S0271','S0455'],[
 ('10月9日，网易荒野事业部正式公布英雄射击新作《极限战场》，并宣布10月15日开启首次PC测试。','S0041','今日上午10点'),
 ('产品以四人小队战术竞技为基础，通过前期快速复活和局内经济购买武器、战术资源，形成发育、争夺与决战的阶段节奏。','S0041',['4人小队','复活系统','经济系统'])],entities=['网易','极限战场'],event_date='2026-10-09',hist=history(['极限战场'],'material_update',['10月9日正式公布首曝PV','首次PC测试确定于10月15日开启']))
ind('I002','游卡《三国杀·烽烟策》进入首测，将身份博弈引入赛季SLG',['S0042','S0178'],[
 ('游卡旗下《三国杀·烽烟策》于10月8日开启“卧龙出山”首次测试，采用不付费删档形式。','S0042',['昨天（10月8日）','不付费删档测试']),
 ('首测把主公、忠臣、反贼与内奸的身份关系放入州和同盟竞争，并通过奇人系统提供侦察、工程和军阵等战术能力；当前测试尚不代表正式商业化方案。','S0042',['主公','奇人系统','商业化'])],entities=['游卡','三国杀·烽烟策'],event_date='2026-10-08')
ind('I003','腾讯领投Flow Games 4600万美元融资',['S0868','S0873','S0916'],[
 ('据PocketGamer.biz披露并由多家行业媒体转述，土耳其手游开发商Flow Games获得4600万美元融资，腾讯贡献约四分之三资金。','S0916','Tencent has led a $46m'),
 ('其产品《Smash Fest》7月下载量据AppMagic估算达到1020万，同期玩家支出约340万美元；报道指出广告也是其重要收入来源。','S0868',['1020万','340万美元','广告才是'])],entities=['腾讯','Flow Games'],event_date='2026-10-13')
ind('I004','库洛入股言之域15%，创始人刘胜进入董事会',['S0866','S0872','S1103'],[
 ('据工商信息，库洛成为言之域科技（深圳）有限公司新增股东，持股15%，刘胜同时出任董事。','S0866','占股15%'),
 ('言之域的产品包括AI音频平台“Vocu悟声”和3D角色驱动系统“元语TalkiVerse”，覆盖语音、音乐、音效及角色动作生成；报道所述约2亿元是估值口径。','S0866',['Vocu 悟声','元语 TalkiVerse','估值达2亿元'])],entities=['库洛','言之域科技'],event_date='2026-10-14',reason='事件核心为资本与董事席位变化，AI为被投公司业务背景，保留行业栏')
ind('I005','腾讯旗下Funcom重组并更换CEO，资源集中于两款长线产品',['S1121','S1124'],[
 ('Funcom启动重组和裁员，未来集中运营《Conan Exiles》与《Dune: Awakening》。','S1124',['restructuring process','Conan Exiles and Dune: Awakening']),
 ('CEO Rui Casais将在年底离职，由首席产品官Scott Junior接任；公司表示从大规模制作转向长期运营，需要调整组织规模。','S1124',['at the end of the year','different organization']),
 ('该公司于2020年被腾讯全资收购。','S1121','次年完成了对Funcom的全资收购')],entities=['腾讯','Funcom'],event_date='2026-10-14')
ind('I006','西山居《剑侠世界4：无限》开启全平台公测',['S1115','S1120','S1285','S1320'],[
 ('西山居武侠MMO《剑侠世界4：无限》于10月15日10时开启全平台公测，公测稿披露全平台预约超过1000万。','S1115',['全平台公测时间','预约量现已突破1000万']),
 ('产品延续家族群战、门派成长和自由交易，并提供无缝地图与双武器切换。','S1115',['家族群战、门派成长、自由交易','双武器自由切换']),
 ('公布的平台包括PC、Android与iOS。','S1285','Platforms: PC / Android / iOS')],entities=['西山居','剑侠世界4：无限'],event_date='2026-10-15')
ind('I007','《绿梦：时空之声》公测，移动端与PC共享进度',['S1118','S1296','S1313'],[
 ('3D二次元横版ACT游戏《绿梦：时空之声》于10月15日在Android、iOS和PC同步公测，支持同服与跨设备进度互通。','S1118','今日（2026年10月15日）'),
 ('产品结合横版箱庭探索和三人小队即时切换战斗，公测新增第三章地图。','S1118',['三人小队即时切换','公测新增第三章地图'])],entities=['绿梦：时空之声'],event_date='2026-10-15')
ind('I008','国产音游《动物城咖啡店》登陆Steam，计划开放关卡编辑器',['S0012','S0601','S0674'],[
 ('国内独立团队一罐盐工作室开发的直觉系音游《动物城咖啡店》于10月13日登陆Steam，原价48元。','S0674','由国内独立游戏团队'),
 ('游戏收录35首原创乐曲，团队计划在正式上线约一个月后推出关卡编辑器，并通过Steam创意工坊分享玩家作品。','S0674',['35首原创乐曲','一个月后推出关卡编辑器'])],entities=['一罐盐工作室','动物城咖啡店'],event_date='2026-10-13')
ind('I009','《七界梦谭》开启PC端限量删档测试',['S0199','S0222','S0268'],[
 ('上海拾异信息科技发行、飞光阁工作室开发的《七界梦谭》于10月9日开启PC端限量删档测试。','S0199',['Event date: 2026-10-09','PC端限量删档测试','Publisher: 上海拾异','Developer: 飞光阁']),
 ('资料将其列为国风修仙开放世界角色扮演产品，平台范围包括PC、Android和iOS。','S0199',['Features:','Platforms:'])],entities=['上海拾异信息科技','七界梦谭'],event_date='2026-10-09')
ind('I010','电魂网络法定代表人将变更为总经理陈芳',['S0457','S0607'],[
 ('电魂网络10月10日临时股东会通过章程修订及法定代表人变更议案，总经理陈芳将成为公司法定代表人。','S0457','10月10日'),
 ('此前股权分割安排使胡建平持股比例由5.78%降至2.78%，陈芳由10.78%升至13.78%；双方签署有效期36个月的一致行动协议。','S0457',['5.78%','36个月'])],entities=['电魂网络','陈芳'],event_date='2026-10-10')
ind('I011','紫龙首曝多人钓鱼新作《极境：垂钓者》，10月21日首测',['S0280','S0610'],[
 ('紫龙旗下BlackJack Studio的子工作室JackWalker Studio研发《极境：垂钓者》，10月10日发布首曝PV和实机演示，并开启招募。','S0280',['今天，一款名为','JackWalker Studio']),
 ('这款多人拟真钓鱼游戏计划于10月21日在PC开启首次限量删档不计费测试，演示展示天气、水温和钓具对鱼获的影响。','S0280',['10月21日','水温'])],entities=['紫龙游戏','极境：垂钓者'],event_date='2026-10-10')
ind('I012','BIGO Ads接入Google AdMob应用内竞价',['S0677','S0781'],[
 ('欢聚集团旗下BIGO Ads宣布SDK接入Google AdMob Mediation，成为应用内竞价合作伙伴。','S0677','BIGO Ads SDK已正式接入'),
 ('合作支持开屏、原生、激励视频、横幅和插屏广告，覆盖休闲游戏、重度游戏与非游戏应用。','S0677',['开屏广告、原生广告','休闲游戏、重度游戏'])],score=(3,3,1),entities=['BIGO Ads','Google AdMob'],event_date='2026-10-13',reason='同稿转载仅记一次信息覆盖，M1；国内广告平台的实质渠道合作')
ind('I013','香港游戏机厂商Nex获超1.5亿美元融资',['S0689'],[
 ('据游戏新知报道，香港游戏机厂商Nex最新一轮融资超过1.5亿美元，估值接近10亿美元。','S0689','来自香港的游戏机厂商Nex'),
 ('其Nex Playground体感设备累计销量超过100万台，采用硬件销售加年费订阅模式，主要面向家庭客厅和儿童。','S0689',['累计卖出超100万台','硬件售卖+年费订阅'])],score=(3,3,1),entities=['Nex'],event_date='2026-10-13')
ind('I014','虎牙启用佛山全球研发总部，承担技术研发与游戏业务孵化',['S0620'],[
 ('10月13日，虎牙全球研发总部在佛山三龙湾揭幕，园区承担技术研发、创新业务孵化与电竞产业生态中枢职能。','S0620',['10月13日','主要承担技术研发']),
 ('虎牙披露园区总投资20亿元、占地18万平方米，后续将持续推进内容营销、游戏发行与AI应用。','S0620',['总投资20亿元','深耕游戏发行'])],score=(3,3,1),entities=['虎牙'],event_date='2026-10-13')
ind('I015','网易武侠SLG《代号：谋略武林》招募保密测试',['S0468','S0558'],[
 ('网易旗下武侠SLG《代号：谋略武林》正在招募小规模保密测试，玩家将经营门派、培养弟子并探索江湖。','S0468',['网易旗下','门派经营、弟子养成']),
 ('开发者说明现阶段美术立绘为AI制作，官网尚未公开实机内容；报道根据测试最低配置推测产品包含移动端与PC端。','S0468',['现阶段美术立绘为AI制作','从官网公布的测试最低配置推测'])],score=(3,3,1),entities=['网易','代号：谋略武林'],event_date='2026-10-12',reason='事件核心为在研新品测试招募，AI只是临时概念图背景；不把配置推测改写为正式平台公告')
ind('I016','Garena Free City软启动范围扩至菲律宾等市场',['S0482'],[
 ('MobileGamer的测试产品更新显示，Garena的GTA式手游《Garena Free City》已从最初仅在阿根廷Android端软启动，扩至菲律宾及部分较小市场。','S0482','it is now registering downloads in the Philippines'),
 ('这是测试区域的扩展，产品仍处于软启动阶段。','S0482','Garena Free City')],score=(3,3,1),entities=['Garena','Garena Free City'],event_date='2026-10-12')
ind('I017','腾讯魔方《火影忍者》手游官宣国际服',['S0611'],[
 ('由万代授权、腾讯魔方研发的《火影忍者》手游宣布推出国际服，相关消息纳入“PROJECT: RASENGAN”全球开发计划。','S0611',['由万代授权、魔方研发','PROJECT: RASENGAN']),
 ('目前公布的是国际服计划与首曝PV，发行安排和上线时间仍待进一步披露。','S0611',['目前尚不清楚','具体情况还有待后续更多信息披露'])],score=(3,3,1),entities=['腾讯','火影忍者'],event_date='2026-10-12')
ind('I018','Miniclip推出独立移动广告平台AdSurge',['S0915'],[
 ('腾讯旗下Miniclip推出AdSurge，作为独立公司同时提供用户获取与广告变现服务，初期重点服务广告收入占比较高的游戏。','S0915',['Tencent-owned Miniclip','independent, standalone company']),
 ('Miniclip称平台筹备约三年，借助自身游戏流量开发算法，未来将扩展至内购及混合变现产品。','S0915',['three years ago','IAPs and hybrid models'])],score=(3,3,1),entities=['腾讯','Miniclip','AdSurge'],event_date='2026-10-14')
ind('I019','育碧《彩虹六号手游》将于2027年1月停运',['S0061','S0081','S0183','S0264','S0283','S0402'],[
 ('育碧宣布《Rainbow Six Mobile》将在2027年1月15日停运，距离2月23日全球上线不到一年。','S0061',['January 15, 2027','February 23, 2026']),
 ('参与研发的团队将转向其他长期战略项目，原定下一周推出的新赛季仍按计划进行。','S0061',['other long-term strategic projects','next season will launch as planned'])],score=(2,3,2),entities=['育碧','Rainbow Six Mobile'],event_date='2026-10-09')
ind('I020','《艾希：续》众筹突破3000万元，制作人强调控制产品预期',['S0040','S0329'],[
 ('国产独立游戏《艾希：续》10月1日开启众筹后，募集金额已超过3000万元，参与人数超过20万人。','S0040','截止完稿时，其众筹金额已经超过3000万元'),
 ('制作人表示，团队只有6人，新增资金主要用于不改变基本框架的CG、音乐与META内容，而非把项目扩成大型游戏。','S0040',['团队只有6个人','“即插即用”的内容'])],score=(2,3,2),entities=['艾希：续'],event_date='2026-10-09')
ind('I021','Xbox成立跨媒体部门XP，由Mojang负责人Kayleen Walters领导',['S0078','S0113','S0150'],[
 ('Xbox成立XP部门，统一管理影视、授权商品、品牌合作及线下体验等游戏IP延伸业务，由Kayleen Walters领导。','S0078',['division named XP','Kayleen Walters']),
 ('原Reddit首席产品官Maria Angelidou-Smith将接任Mojang负责人，两人均直接向Xbox CEO Asha Sharma汇报。','S0078',['Maria Angelidou-Smith','report directly'])],score=(3,2,2),entities=['Xbox','XP'],event_date='2026-10-09')
ind('I022','《全境封锁2》国服将于12月14日停止运营',['S0448','S0467','S0591'],[
 ('腾讯代理发行的《全境封锁2》国服宣布将于12月14日停止运营，结束约三年的国内运营。','S0467',['12月14日','3年'])],score=(2,3,2),entities=['腾讯','全境封锁2'],event_date='2026-10-12')
ind('I023','Aream：Q3游戏并购总额578亿美元，移动内购收入下滑7%',['S0690','S0706','S0916'],[
 ('Aream & Co.第三季度游戏市场报告记录54笔并购、合计578亿美元，其中包括EA的550亿美元杠杆收购。','S0690',['54 transactions','55 billion leveraged buyout']),
 ('同季移动游戏内购收入为196亿美元、同比下降7%；报告口径涵盖iOS与Google Play、中国仅含iOS，并排除网页商店。','S0916',['$19.6bn','iOS only in China','excluding web shops']),
 ('该季私人投资合计28亿美元，种子轮融资降至五年低点，资金进一步向A轮和后期项目集中。','S0690',['$2.8 billion','five-year low'])],score=(2,3,2),entities=['Aream & Co.','移动游戏市场'],event_date='2026-10-13')
ind('I024','苹果中国App Store研究列举网易与米哈游网页支付案例',['S0612','S0688'],[
 ('苹果发布的2025年中国App Store生态研究估算，中国营业额与销售额合计约4万亿元，其中超过95%免于平台抽成。','S0612',['总计约为四万亿元','超95%免于抽成']),
 ('报告列举网易网页商店与米哈游官方支付中心作为开发者通过DTC直接获取收入的案例；这份生态规模研究并不等于中国区已开放应用内第三方支付。','S0612',['网易的网页商店','米哈游的官方网页支付中心','没有接入三方支付'])],score=(2,3,2),entities=['苹果','中国App Store'],event_date='2026-10-08')
ind('I025','Xbox集中现有研发项目成立Labs，探索浏览器分发与模组工具',['S0893','S0969','S1090'],[
 ('Xbox宣布成立Xbox Labs，以小型跨学科团队快速试验工具、产品和功能，并根据玩家与开发者反馈迭代。','S0893',['small group of game makers','rapid development']),
 ('公司向GamesIndustry.biz说明，该团队整合现有研发项目，没有新增招聘，也没有必须使用AI的指令；方向包括Apple芯片移植、WebGPU浏览器分发和模组支持。','S0893',['No new staff','did not have an explicit directive','WebGPU'])],score=(3,2,2),entities=['Xbox','Xbox Labs'],event_date='2026-10-14',reason='组织和研发资源集中为核心，来源明确并非AI专属团队；与10月9日XP为不同事件')
ind('I026','腾讯新生存游戏《Crownstone Survival》出现产品页与测试市场信息',['S0482'],[
 ('据MobileGamer测试产品清单，腾讯新生存游戏《Crownstone Survival》已出现于AppMagic产品页。','S0482','Tencent’s new survival game Crownstone Survival'),
 ('报道判断其可能在菲律宾、法国、印尼、土耳其和美国Google Play软启动，该信息仍属于测试准备信号。','S0482','seemingly slated for a soft launch')],score=(3,3,1),entities=['腾讯','Crownstone Survival'],event_date='2026-10-12')
# 保留高分线索，但原文的seemingly不能证明本期正式立项或已启动测试。
items=[it for it in items if it['candidate_id']!='I026']
next(d for d in decisions if d['candidate_id']=='I026').update(decision='exclude',reason='高分重点新品线索保留；唯一清单只写产品页刚出现并推测软启动市场，没有正式披露或测试发生时间，不将推测写成本期确立的产品阶段')
ind('I027','《连城绝：大唐》开启首次不删档计费测试',['S0777','S0778','S1300'],[
 ('花叮娱乐旗下武侠MMO《连城绝：大唐》定于10月15日15时开启首次不删档、不限量计费测试。','S0778',['首次不删档不限量计费测试','2026年10月15日（周四）15:00点']),
 ('产品公布了五大门派、野外战斗、社交和生活玩法。','S0778',['五大门派','采药炼丹']),
 ('平台范围包括PC、Web、Android与iOS。','S1300','Platforms: PC / Web / Android / iOS')],entities=['花叮娱乐','连城绝：大唐'],event_date='2026-10-15')
ind('I028','RED LAND披露超20万人到场与25亿曝光',['S0462','S0542'],[
 ('RED LAND活动落幕后公布结果：累计超过20万人登岛，82%的游客来自上海以外，全网曝光量超过25亿。','S0542',['累计超20万人','82%的游客','曝光量突破25亿']),
 ('另一篇现场报道也确认到场人数超过20万、较去年翻倍；这些是活动规模扩张之后的实际参与和传播结果。','S0462',['超过 20万用户登岛','人数较去年翻倍'])],score=(2,3,2),entities=['小红书','RED LAND'],event_date='2026-10-12',hist=history(['RED LAND'],'material_update',['累计超过20万人登岛','82%的游客来自上海以外','活动全网曝光量突破25亿']))

# AI独立事件：资本事件保留行业，已落地的工具/产品与管线进入本栏。
def ai(cid,title,ids,facts,stage,**kw):
    return add(cid,'ai',title,ids,facts,ai_tier='direct_application',game_stage=stage,industry_reverse_scan=True,**kw)
ai('A001','字节AI互动游戏《不问凡尘》销量突破26万份',['S0891'],[
 ('朝夕光年江南工作室开发的AI修仙互动游戏《不问凡尘》宣布销量突破26万份，产品已于9月23日进入Steam抢先体验。','S0891',['销量突破26万','9月23日']),
 ('产品大量采用AI生成角色、场景、物品与音效，并支持玩家与AI角色对话。','S0891','大部分内容都使用AI生成'),
 ('Steam页面标注在线生成内容由火山引擎提供，当前仍处于EA阶段。','S0891',['火山引擎','抢先体验'])],['development','product'])
ai('A002','Epic迪士尼合作射击项目延期，并转向AI优先制作',['S0694','S0762','S0862','S1143'],[
 ('据Bloomberg报道，Epic与迪士尼合作的射击项目延期，尚未公布新的发售时间；团队被要求转向AI优先的制作方式。','S0694',['has delayed','no new release date']),
 ('知情人士称项目将更多采用Claude等工具生成代码和美术，由开发人员监督输出；Epic回应称其采用的是由开发者主导的AI加速研发。','S0694',['Anthropic\'s Claude','AI-accelerated development']),
 ('报道也将延期与人员和工期估算不足联系起来，不能把延期全部归因于AI。','S0694','misjudged the staffing and time')],['development'])
ai('A003','Epic用AI重写商店启动器，发布全新架构预览版',['S1000','S1129','S1179'],[
 ('Epic Games Store新启动器预览版已面向Windows、Mac与Linux提供下载，团队确认AI用于从头编写和审查新功能。','S1000',['preview','We started from scratch','write and review new features']),
 ('Epic宣称冷启动进入商店页的速度比Steam快46%，并表示该结果经过外部供应商验证；这一指标是厂商测试口径。','S1000',['46% faster than Steam','external vendor'])],['development','publishing'])
ai('A004','游族披露AI中台与Agent研发应用，覆盖100多个子场景',['S0860'],[
 ('游族红岸实验室负责人余华松在10月11日的中国元宇宙大会分享AI实践，称公司六大场景、100多个子场景已覆盖AI工具。','S0860',['10月11日','100多个子场景']),
 ('其内部系统通过统一网关接入模型和技能商店，并提供智能BI、内容风控、舆情分析及AIGC平台。','S0860',['Skill Hub','智能BI']),
 ('演讲进一步讨论内容生成、智能NPC和一键游戏创作Agent，相关未来方向与已使用的内部工具应分别理解。','S0860','三大应用方向')],['development','publishing','operations'])
ai('A005','《星布谷地》测试体验展示AI NPC记忆与多人控场',['S1150'],[
 ('触乐的测试体验报道显示，米哈游《星布谷地》已有娜洛等4位AI NPC，咖啡馆角色能在一对多聊天中记住玩家点单和交流内容。','S1150',['目前共有4位AI NPC','一对多的对话场景']),
 ('团队把环境感知、回应优先级和记忆设计接入公共社交空间，并允许玩家选择是否保留测试阶段的娜洛记忆。','S1150',['自主选择是否保留','优先回答什么']),
 ('这些描述对应测试中的产品体验，终测于9月20日开启。','S1150','9月20日')],['product'])
ai('A006','Google Play扩展个性化游戏发现，接入Gemini推荐',['S0914','S1127'],[
 ('Google Play推出Game Finder、48小时Sprints挑战和Sidekick回放等功能，Game Finder根据玩家偏好、行为及社区评价推荐游戏。','S0914',['Game Finder','48-hour','preferences and behaviour']),
 ('Google还把游戏推荐扩展到Gemini Live语音交互；开发者可通过Game Stats与Play Games Rewards接入相关游戏信号和奖励能力。','S0914',['Gemini Live','Game Stats and Play Games Rewards'])],['publishing','operations'])
ai('A007','堀井雄二发布AI制作的文字审讯游戏，称用时约30分钟',['S0693'],[
 ('《勇者斗恶龙》创作者堀井雄二在X发布文字审讯游戏，称使用AI制作过程约30分钟。','S0693',['Yuji Horii','about 30 minutes']),
 ('玩家需要在律师到来前，通过询问和证据拆穿嫌疑人的谎言；该案例展示了个人快速制作可玩原型的路径。','S0693',['lawyer arrives','confront the suspect\'s lies'])],['development','product'])
ai('A008','Meshy创始人披露AI 3D工具ARR突破1亿美元',['S0044'],[
 ('Meshy创始人胡渊鸣披露，公司年度经常性收入ARR突破1亿美元，高于4月接近4000万美元的水平。','S0044',['突破1亿美元','接近4000万美元']),
 ('这家AI 3D工具公司此前展示游戏Demo《黑箱》，表达从制作工具走向AI原生游戏的计划；ARR口径不等同于已实现的全年收入。','S0044',['名为《黑箱》','AI原生游戏公司'])],['development'])
ai('A009','《代号Live》把AI动作生成接入角色互动，团队披露测试数据',['S0459'],[
 ('《代号Live》团队在访谈中介绍，把视频动作提取、动画生成、语音和表情接入AI虚拟偶像的互动内容制作。','S0459',['代号Live','视频','表情']),
 ('团队称9月测试次日留存为72%、五日留存为57%；这些是内部测试结果，产品的长期留存与商业回收仍需验证。','S0459',['72%','57%'])],['development','product'])
ai('A010','AI游戏创作平台Astrocade月活达到1000万',['S0456'],[
 ('AI游戏创作平台Astrocade宣布月活达到1000万，较四个月前的500万翻倍。','S0456','Astrocade官宣达到1000万月活'),
 ('平台把自然语言创作、信息流推荐、游玩和分享连在一起，用户可以生成并继续修改小游戏。','S0456',['自然语言描述','信息流平台']),
 ('据平台规则，达到有效游玩门槛的创作者可按游玩次数获得收益，生成能力正与分发和创作者激励形成同一条产品链。','S0456','累计达到10万次有效游戏')],['development','publishing','product'])
ai('A011','Meta的AI小游戏应用Pocket从巴西测试扩至美国',['S0482'],[
 ('MobileGamer汇总显示，Meta的AI小游戏创作与分享应用Pocket已向美国用户开放，此前仅在巴西测试。','S0482',['Pocket','previously only available in Brazil']),
 ('用户可借助文字、照片、触摸和声音提示生成短互动内容，应用以信息流形式组织这些“gizmos”。','S0482',['text, photos, touch and sound','interactive feed'])],['development','product','publishing'])
items=[it for it in items if it['candidate_id']!='A011']
next(d for d in decisions if d['candidate_id']=='A011').update(decision='exclude',reason='独立AI产品扩区事件已召回；唯一完整来源与Garena行业事件共用同一篇综述，现有校验器禁止行业与AI共用source。保留达到硬分数线的Garena条目，Pocket暂留候选；不把两个产品合并为同一事件',validation_limitation='cross-industry-AI source reuse is rejected even for different events')

# 社区只报道能命名的事件；推测保留归属，不转成官方事实。
it,d=add('C001','community','《明日方舟》活动文案被质疑使用AI，争论聚焦文风与人工审稿',['S0378','S1051','S1338'],[
 ('《明日方舟》“昨日海”活动文案被玩家质疑使用AI，依据包括突兀的数字细节、转折句式和低信息密度。','S1051',['新的活动“昨日海”','大量意义不明的数字']),
 ('10月10日出现的讨论延续至15日；部分玩家把问题归于审核与润色，另一些人认为这些特征也可能来自既有写作风格。','S1338',['2026-10-10T15:30','2026-10-15T09:25','剧情不是一直这样吗']),
 ('15日的后续回复中，也有玩家明确表示可接受AI生成加人工润色，分歧落在最终文本质量和审稿责任，而不只是工具本身。','S1338','我也不反对ai生成+人工润色')],entities=['明日方舟'],event_date='2026-10-10')
it['community']=d['community']={'trigger':'昨日海活动文案被质疑AI生成','claim_scope':'玩家质疑与文风判断，不作官方用AI结论','complaint_logic':'文案质量、信息密度与审核责任；是否能接受AI生成加人工润色','timeline':'10月10日触发，10月15日仍讨论文本质量和润色责任','follow_up_scan':{'source_ids':['S0378','S1051','S1338'],'result':'扫描同窗社区续帖及行业全文；剔除后段针对其他游戏文本的检测对比，不将跨作品检测回填为本次文案证据；未检得可证实的官方制作结论'}}
it,d=add('C002','community','《终末地》玩家称装Mod被长期封号，修改客户端与外挂边界成焦点',['S1064','S1345'],[
 ('《明日方舟：终末地》玩家10月14日称使用Mod后被封80年，引发对模型替换、内存修改和反作弊边界的争论。','S1064',['2026-10-14T13:51','被封80年','改了游戏内存']),
 ('争议集中在普通外观Mod与改变功能、修改内存的工具应否区别处理：部分玩家认为修改客户端本就存在封禁风险，另一些人不接受把不同用途的工具混为一谈。','S1345',['普通MOD依然正常使用','触犯天条']),
 ('讨论到15日继续扩展至自动化脚本与模拟器的检测方式，玩家对技术原理和处罚尺度的说法并不一致。','S1345',['2026-10-15T19:10','模拟器拿头上ace'])],entities=['明日方舟：终末地'],event_date='2026-10-14')
it['community']=d['community']={'trigger':'玩家称Mod导致长期封号','claim_scope':'不将帖内80年、付费警告及反作弊推测写成官方统一政策','complaint_logic':'外观修改、功能改变和客户端注入的边界及处罚一致性','timeline':'10月14日建帖，15日讨论转向脚本和模拟器','follow_up_scan':{'source_ids':['S1064','S1345','S1056'],'result':'按终末地/Mod/ACE检索社区与行业全文；未把另一款游戏的法务事件并入本案'}}
it,d=add('C003','community','《幕府将军2 完全版》差评后，世嘉宣布撤售并恢复原版',['S1239'],[
 ('《全面战争：幕府将军2 完全版》发售后因旧Bug、体验改进不足，以及玩家质疑未披露AI使用而遭遇差评，部分玩家还不满原版先被下架。','S1239',['Thousands of negative user reviews','pulled the original from sale']),
 ('10月15日的报道中，世嘉承认当前体验未达要求，表示正与平台合作撤下完全版并恢复原版销售，同时调查问题。','S1239',['current experience is not where it needs to be','reinstate the original game']),
 ('玩家关注点由“重制增加了什么”升级为能否继续获得旧版；已购买完全版的用户仍可访问该版本。','S1239',['will still have access','putting the original back'])],entities=['世嘉','全面战争：幕府将军2 完全版'],event_date='2026-10-15')
it['community']=d['community']={'trigger':'完全版发售差评与原版下架','claim_scope':'AI仅为玩家指控；撤售恢复原版为媒体引述世嘉声明，未写成已完成','complaint_logic':'升级价值、Bug、旧版可获得性与内容透明度','timeline':'发售后两日积累差评，10月15日媒体引述撤售计划','follow_up_scan':{'source_ids':['S0853','S0958','S1074','S1239'],'result':'合并完全版发售、原版停售与世嘉回应；不从宣传视频推导已修复'}}

# 精确回执三题；仅重新映射来源ID，保留人工标题/顺序/主卡。
review_path=ROOT/'tmp/deep_observation_2026-10-08_to_2026-10-14'
review=json.loads((review_path/'candidate_review.json').read_text(encoding='utf-8'))
old={x['source_id']:x for x in map(json.loads,(review_path/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
byurl={x['url']:x for x in rows}
for num,c in enumerate(review['candidates'][:3],1):
    ids=[byurl[old[s]['url']]['source_id'] for s in c['source_ids']]
    points=c['analysis_points']; body='观察：'+c['observation']+'\n\n分析：'+' '.join(x['detail'] for x in points[:2])+'\n\n'+' '.join(x['detail'] for x in points[2:])
    # 全部数据锚点逐字取证；机制和边界再从正文段落匹配，避免只引用标题。
    claims=[]
    for e in c['evidence_anchors']:
        sid=byurl[old[e['source_id']]['url']]['source_id']
        assert e['evidence'] in S[sid]['text']
        # 每个观察/分析段都保留事实证据集合，含推断时明确为分析。
        claims.append({'claim':body.split('\n\n')[1].removeprefix('分析：'),'source_id':sid,'evidence':e['evidence']})
    local_needles={1:['56.3%','日常任务、定时的公会活动','老产品在 2021 至 2025 年间损失了 39 亿美元','数据说明：'],2:['约 15 美元','认知摩擦','可选的 minigame','月收入却已经走平'],3:['监狱只有绝密倍场','我们不会对用户个体去定义和分层','玩家想解锁鱼竿','5800万']}
    for point,needle in zip(points,local_needles[num]):
        claims.append({'claim':point['detail'],'source_id':ids[0],'evidence':evidence(ids[0],needle)})
    claims.append({'claim':c['observation'],'source_id':ids[0],'evidence':evidence(ids[0],local_needles[num][0])})
    if num==1:
        body=body.replace('观察：','观察：Naavik研究显示，2021至2025年MMORPG手游内购收入下降47%。',1)
        claims.append({'claim':'2021至2025年MMORPG手游内购收入下降47%。','source_id':ids[0],'evidence':evidence(ids[0],'降幅为 -47%')})
    expansions={
      1:[('传统MMO以持续投入换取成长、地位与社交归属，这一前提要求玩家仍认可每日时间和重复付费的回报；当相邻RPG提供更轻的替代选择，存量用户减少参与就会同时压低付费。','传统的MMORPG手游提供了一笔极具吸引力的交易'),('因此，新下载不等于补足存量世界的人口与付费，产品还需降低新玩家进入和追赶老友的成本。研究举出《逆水寒手游》调整引导、追赶奖励和年度赛季重置，说明获客与产品结构需要共同作用。','2024 年，网易承认《逆水寒手游》')],
      2:[('普通三消的使用条件是玩家无需持续集中注意力，也能完成熟悉的动作；强制切换规则后，原本适合碎片时间的主线会变成需要专门投入的一段挑战。','认知体验'),('因此，同样用于兑现广告承诺，副玩法能否退出是关键区别：可选关卡没有通过也能回到主线，强制关卡则把不喜欢该玩法的人一起阻塞。评价创新也需要考察它改变了哪一种使用情境。','可选的 minigame')],
      3:[('原先统一难度成长的做法默认用户最终会追求更高强度竞技，但扩盘后玩家的时间和风险偏好发生分化；固定在高压环境中，抱团避险便成为部分玩家的自发选择。','沿着线性跃迁的设计思路'),('把内容放进探索和玩家行为组合中，意味着更新不再只有更高数值与难度一条路径。这里的变化是产品设计目标的调整，不能直接把整体日活增长当作某一项休闲玩法的效果。','真正的沙盒应该是不期而遇')]
    }
    pars=body.split('\n\n')
    for j,(extra_text,needle) in enumerate(expansions[num],1):
        pars[j]+=extra_text
        claims.append({'claim':extra_text,'source_id':ids[0],'evidence':evidence(ids[0],needle)})
    body='\n\n'.join(pars)
    it={'candidate_id':f'D{num:03d}','section':'deep','title':c['title'],'source_ids':ids,'body':body,'claims':claims,'card_copy':c['card_copy']}
    d={'candidate_id':it['candidate_id'],'section':'deep','source_ids':ids,'entities':[c['title']],'event':c['title'],'decision':'include','reason':f'飞书回执指定正文C{num:03d}，保持原顺序','scores':c['scores'],'card_designated':num==1}
    items.append(it);decisions.append(d);consumed.update(ids)
(OUT/'deep_card_choice.txt').write_text(review['candidates'][0]['title']+'\n',encoding='utf-8')

# 其余来源逐条判断；同URL、同事件的已采用材料只做merge，不冒充新增事件。
manual_exclusions={
 'S0477':((3,3,1),'Roblox收编Audioscape团队是必须召回的重点组织/AI工具事件；本地只有snippet，不能用摘要完成正文取证',[],None),
 'S0031':((3,1,1),'首次公布已召回，但中国小镇是故事背景，不能据此猜测国内开发主体；本地仅标题而无可用正文',[],None),
 'S0250':((3,1,1),'同一叫魂首曝的后续采集，未确认国内主体；仅标题不能提供独立正文事实',[],None),
 'S0035':((2,3,1),'欧盟虚拟货币协同行动为9月30日旧事件；本期仅一份完整报道，周报7分；所有历史匹配均未曝光但未达8分，不采用', ['虚拟货币'],None),
 'S0037':((2,3,1),'国际服10月5日上线及近40万在线属于上周节点，本期未提供可辨识的新阶段；7分',[],None),
 'S0058':((2,3,1),'字节广告营销限制有国内业务迁移，E2R3M1=7，未达周报8分',[],None),
 'S0060':((1,3,1),'国内创业者与在研Cycho已个别评估；Demo为6月既有节点，Q4为宽泛计划，非本周首曝/新测试',[],None),
 'S0062':((3,2,1),'海外发行与后台共享合作有全球开发迁移但非国内/移动重点；7分',[],None),
 'S0063':((3,1,1),'VR专利转移非国内移动游戏变化，R1；4分',[],None),
 'S0260':((2,3,1),'国内小游戏产品表现已单独评估，非笼统低信号；结构与榜单结果为E2，单源M1，7分',[],None),
 'S0263':((3,3,1),'网易与草蜢分离旧事件，历史已曝光，无实质新状态',['Grasshopper'],None),
 'S0484':((3,2,1),'Exit Games回购同一股权交易，历史已曝光；晚到转载不构成新增',['Exit Games'],None),
 'S0485':((3,2,1),'Gardens融资具有社交RPG迁移，但本地仅为预告短文，且单源7分；不凭记忆补融资细节',[],None),
 'S0697':((2,3,1),'Q3移动内购属于Aream同一报告，摘要不可作为独立事实源；归并已采用原报告事件',[],None),
 'S0703':((3,3,1),'Flow Games融资标题有信号，但源为snippet；正文改用完整报道',[],None),
 'S0705':((3,2,1),'Rovio在研与资源重新聚焦具有移动迁移，E3R2M1=7；不因移动标签自动赋R3',[],None),
 'S0861':((2,3,1),'国内平台政策已个别评估；出版五年规划为E2，单源7分，未达周报8分',[],None),
 'S0863':((2,3,1),'手游主播补贴进入监管质询为E2R3M1=7；不以争议抬升资本/新品E3',[],None),
 'S0864':((2,3,1),'苹果独立游戏周属渠道供给调整；非首次立项或重大独家合作，7分',[],None),
 'S0892':((2,3,1),'三七互娱《梦回甄嬛传》当前运营表现逐条评估：E2R3M1=7，未达周报8分；8月上线不改成10月',[],None),
 'S0895':((2,2,2),'RedLynx关停与新加坡裁员同一组织事件，E2R2M2=6；已核多源，非纯裁员E1',[],None),
 'S0896':((2,3,1),'中国安伯尼克被建议纳入恶名市场名单；监管建议尚非正式制裁，7分',[],None),
 'S0915':((3,3,1),'AdSurge已独立采用',[],None),
 'S0916':((2,3,1),'Spill融资1050万美元为独立次事件：E3R2M1=7，详见额外候选；Aream/Flow分属各自事件',[],None),
 'S0918':((2,3,1),'Supercell停服日期为新生命周期节点，固定重点R3；仅一份独立完整核心报道，7分；同站播客不增加M',[],None),
 'S0931':((2,3,1),'PVP射击产品战狗成绩为E2R3M1=7，未达周报8分',[],None),
 'S0978':((2,3,1),'铁匠模拟经营产品经营成绩为E2R3M1=7，未达8分',[],None),
 'S1001':((2,3,1),'Fortnite Linux适配计划属跨平台生命周期E2，单源7分',[],None),
 'S1110':((2,3,1),'莉莉丝塔塔冒险队当前四个月表现与9月披露高度重叠，历史已曝光，无可验证新增',['塔塔冒险队'],None),
 'S1111':((2,3,1),'常规业绩预告与买量回收周期解释，无一致预期/指引异常或流动性/资本结构变化，财报门禁排除',[],None),
 'S1112':((3,3,1),'Circle融资为上周已发布且已曝光；Flow部分仅归并本周交易，不把背景投资拆新事件',['Circle Games'],None),
 'S1128':((1,2,1),'德国自愿离职计划为另一起纯裁员事件，E1R2M1=3，不与关停事件混为一条',[],None),
 'S1133':((3,2,1),'开源框架Brutal已用于项目但无重点主体/优先赛道归属；开发工具迁移R2，7分',[],None),
 'S1206':((2,3,1),'诡秘之主首月经营数据为E2R3M1=7，稿中按渠道比例外推不当作官方流水',[],None),
 'S1219':((2,3,1),'Riot Games固定R3；Classic停服为E2，独立单源M1=7，不豁免周报阈值',[],None),
 'S1248':((1,3,1),'SLG赛道讨论/观点未提供独立可验证新事件，E1R3M1=4',[],None),
}
same_events=[
 (['三角洲','5800'],['三角洲行动'], '已发布5800万DAU同一事件，跨期重复；深度选择另按用户指定机制题处理'),
 (['Minecraft Blast'],['Minecraft Blast'],'重回软启动已在历史曝光，无新区域或状态'),
 (['mo.co'],['mo.co'],'回到beta及负责人变更为历史已曝光事件'),
 (['Paramount','Warner'],['Paramount'],'华纳游戏整合为历史已曝光事件；电影项目不是该行业事件的新阶段'),
]
def scope(d):
    joined=' '.join(S[s]['text'] for s in d['source_ids'])
    # 对可识别PC/主机发售候选全部给出范围；非发售可不写。
    if not re.search(r'PC|Steam|PS5|Xbox|XBOX|主机|端游|Switch',joined,re.I) or not re.search(r'发售|正式上线|首发|launch|releas',d['event'],re.I):return
    if d['candidate_id'] in {'I006','I008','I009','I027'}: cls='domestic_or_focus'; basis='来源明确国内开发/发行主体，非普通海外单机品类例外'; needle={'I006':('S1115','西山居'),'I008':('S0674','国内独立游戏团队'),'I009':('S0199','上海拾异'),'I027':('S0777','花叮娱乐')}[d['candidate_id']]
    elif d['candidate_id']=='I007':cls='multiplayer_or_other';basis='Android/iOS/PC三端互通的在线抽卡ACT，不属于海外PC单机纯发售';needle=('S1118','安卓、iOS、PC三端同步')
    elif re.search('多人|联机|multiplayer|co-op',joined,re.I) and re.search('正式发售|首发|新品上线',d['event']):cls='multiplayer_or_other';basis='正文明确多人或联机形态，按实际迁移点评分';needle=None
    else:cls='ordinary_overseas_single_player' if re.search('Planet Zoo|动物园之星|不朽遗志|沉星之序|战锤40K：爆矢枪2',joined,re.I) else 'unknown';basis='纯PC/主机发售或主体相关性无法从正文确认；R按1，不凭RPG/模拟品类升权';needle=None
    if needle: evid=evidence(*needle);sid=needle[0]
    else:
        sid=next(s for s in d['source_ids'] if re.search(r'PC|Steam|PS5|Xbox|XBOX|主机|端游|Switch',S[s]['text'],re.I));t=S[sid]['text'];m=re.search(r'PC|Steam|PS5|Xbox|XBOX|主机|端游|Switch',t,re.I);evid=evidence(sid,m.group())
    d['pc_release_scope']={'classification':cls,'basis':basis,'evidence':[{'source_id':sid,'evidence':evid}]}

for s in rows:
    if s['section']!='industry_news':continue
    sid=s['source_id'];title=s['title'];text=s['text'];cid='X'+sid[1:]
    target=next((d for d in decisions if sid in d['source_ids'] and d['decision']=='include' and d['section']!='release_calendar'),None)
    if target:
        # 已采用主文引用集本身就是该源的审计归属，无需重复一条空merge。
        continue
    if sid=='S0328':
        decisions.append({'candidate_id':cid,'section':'ai','source_ids':[sid],'entities':['朝夕光年','不问凡尘'],'event':title,'decision':'exclude','reason':'AI直接作用候选已独立反扫；本稿为9月23日已上线产品的制作复盘，本期采用10月13日26万销量的新节点，不将两次披露伪合为同日事件','ai_tier':'direct_application','game_stage':['development','product'],'industry_reverse_scan':True})
        continue
    if sid in {'S0617','S0417','S0452','S1101'}:
        reasons={'S0617':'AI陪伴原型为有效直接作用候选，但报道没有给出本期独立测试日期或新产品阶段；本期优先采用已有明确流程、近期成绩或可检验数据的案例，不把玩家哭了作为采用依据','S0417':'AI驾驶Demo运行成本是直接作用候选，产品仍为持续测试；单一开发者成本自述与其他转载口径需核对，本期不以账单标题替代稳定产出结果','S0452':'同一AI驾驶Demo成本故事的中文转载，保留与S0417的口径核对，未作为独立事件再次采用','S1101':'粉丝复刻停服产品属于AI技术应用候选，但不等于官方恢复运营；本期不把工程复刻与正式重启作为同一状态写入正文'}
        decisions.append({'candidate_id':cid,'section':'ai','source_ids':[sid],'entities':[title],'event':title,'decision':'exclude','reason':reasons[sid],'ai_tier':'direct_application','game_stage':['development','product'],'industry_reverse_scan':True})
        continue
    if sid=='S1246':
        decisions.append({'candidate_id':cid,'section':'industry','source_ids':[sid],'entities':['西山居','剑侠世界4：无限'],'event':title,'decision':'merge','merge_into':'I006','reason':'同一10月15日公测新闻稿的转载，归并I006，不新增M','scores':{'event':3,'relevance':3,'hook':1,'total':10},'history_check':history()})
        continue
    # 可精确核验URL/正文的重复采集。
    dup=next((d for d in decisions if d['decision']=='include' and d['section'] in ['industry','ai','deep'] and any(S[q]['url']==s['url'] or (len(text)>100 and S[q]['sha1']==s['sha1']) for q in d['source_ids'])),None)
    if dup:
        d={'candidate_id':cid,'section':dup['section'],'source_ids':[sid],'entities':dup['entities'],'event':title,'decision':'merge','merge_into':dup['candidate_id'],'reason':'同URL/正文哈希的重复采集，不能作为独立新事件或多源加分'}
        if d['section']=='industry':d.update(scores=dup['scores'],history_check=dup['history_check'])
        decisions.append(d);continue
    if sid in manual_exclusions:
        sc,reason,terms,nov=manual_exclusions[sid];e,r,m=sc;hc=history(terms,nov)
    else:
        focus=re.search(r'腾讯|网易|米哈游|莉莉丝|三七|库洛|西山居|灵犀|虎牙|国产|中国|国内|Roblox|Supercell|Riot Games|拳头|Garena|Scopely',title,re.I)
        r=3 if focus else 1;m=1;e=0;terms=[];reason=''
        if re.search(r'融资|收购|入股|成立.*部门|成立.*团队|CEO.*接任',title,re.I):e=3;reason='资本/组织信号已独立成卡；缺少重点主体/移动或全球格局具体迁移证据'
        elif re.search(r'停运|停服|关闭|关停|延期|跳票|重组|裁员|shut|clos|delay|layoff|redundan',title,re.I):e=1 if re.search(r'裁员|layoff|redundan',title,re.I) and not re.search('关闭|关停|clos|取消',title,re.I) else 2;reason='生命周期或组织变化已单独评分，按实际事件而非标题热度判定'
        elif re.search(r'发售|正式上线|公测|首测|首曝|正式公布|新作.*公开|launch|release date',title,re.I) and not re.search('宣传|预告|评测|DLC|联动|新版本|赛季',title,re.I):e=3;reason='新品信号已逐条召回；来源未证明重点主体归属或当前实质移动迁移，R1'
        elif re.search(r'收入|流水|销量|下载|日活|月活|并购|市场|广告|榜单|玩家|数据',title,re.I):e=2;reason='经营/市场信号已逐条判断；单一现象或普通海外产品迁移有限，未达8分'
        elif re.search(r'访谈|谈|采访|开发|设计|AI|人工智能|工具|引擎',title,re.I):e=1;reason='访谈/工具/设计背景逐条检查，未发现能作为独立新品/资本/政策事件的当前状态变化'
        else:reason='原文为常规内容更新、预告/评测/攻略、例行宣传、非游戏或旧作背景，E0'
        if r==3 and e==3:
            # 不能拿来源中顺带提到的公司或旧节点抬高新鲜度；这些均逐条留原文。
            e=1;reason='重点主体已单独检查；正文为既有产品/历史开发复盘/宽泛计划，未提供本期首次状态变化'
        if s['body_status']!='full' or not text.strip():reason='本地正文为snippet/empty，不能验证事实；'+reason
        elif len(text)<120:reason='本地仅标题/极短导语，未能确认更多主体、事件时间或产品型态；'+reason
        if re.search(r'AI|人工智能|Claude|Gemini|prompt|智能体|模型|NPC',title,re.I):reason+='；AI反扫：泛技术、既有背景或没有明确本期游戏作用链，不自动进入AI正文'
        # 显式跨期匹配，原文比标题广，但不能将背景词当成事件相同。
        if re.search('三角洲.*5800|5800.*三角洲',title):terms=['三角洲行动'];reason='5800万DAU同一已曝光事件，非本期新增状态'
        elif re.search('草蜢.*独立|草蜢.*分手|Grasshopper',title,re.I):terms=['Grasshopper'];reason='工作室脱离网易是已曝光同一事件'
        elif re.search('9月全球.*手游.*收入|9月全球.*最赚钱|9月全球手游.*排行',title):terms=['9月全球手游'];reason='9月全球榜单与结构同一月度事件，历史已曝光；不以更换统计机构重写重复结论'
        elif re.search('华纳.*合并|派拉蒙收购华纳|Paramount.*Warner',title,re.I):terms=['Paramount'];reason='同一华纳游戏整合/收购背景已曝光'
        hc=history(terms)
    entities=re.findall(r'Roblox|Supercell|Riot Games|腾讯|网易|米哈游|三七互娱|库洛|Garena',title,re.I) or [re.findall(r'《([^》]+)》',title)[0] if re.findall(r'《([^》]+)》',title) else title]
    if any(x.lower() in ['roblox','supercell','riot games'] for x in entities):r=3
    d={'candidate_id':cid,'section':'industry','source_ids':[sid],'entities':entities,'event':title,'event_date':s['date'],'decision':'exclude','reason':reason,'scores':{'event':e,'relevance':r,'hook':m,'total':e*r+m},'history_check':hc,'source_evidence':[{'source_id':sid,'evidence':text if len(text)<160 else evidence(sid,next((x for x in text.splitlines() if len(x)>30 and '禁止转载' not in x),text[:100]))}] if text else []}
    scope(d)
    if d.get('pc_release_scope',{}).get('classification') in ['ordinary_overseas_single_player','unknown']:
        d['scores']['relevance']=1;d['scores']['total']=d['scores']['event']+d['scores']['hook']
    decisions.append(d)

# 关键边界和未采用主源中的第二事件也分别建卡。
for cid,title,ids,sc,reason,terms in [
 ('B001','普通海外PC单机《动物园之星2》发售',['S0855','S0959'],(3,1,2),'普通海外模拟经营单机纯发售，不能凭品类取得R3；行业5分，日历独立评估',[]),
 ('B002','普通海外PC单机《不朽遗志》发售',['S0850','S0960'],(3,1,2),'普通海外魂类单机纯发售，R1；行业5分，不牵连日历资格',[]),
 ('B003','Spill Games完成1050万美元融资',['S0916'],(3,2,1),'移动益智融资有R2迁移，但非固定重点/优先品类的自动R3；7分',[]),
 ('B004','RED LAND此前扩展场地与IP规模的后续背景报道',['S0681'],(2,3,1),'背景复盘未提供本稿可取证的新增参与结果；本期结果更新另由I028采用',['RED LAND']),
 ('B005','King重新测试Minecraft Blast',['S0482'],(3,3,1),'历史已曝光的同一软启动，未提供实质新状态',['Minecraft Blast']),
 ('B006','Supercell将mo.co转回beta',['S0482'],(2,3,1),'历史已曝光的同一状态',['mo.co']),
 ('B007','腾讯领投Circle Games 2500万美元融资',['S0868','S1112'],(3,3,1),'历史已曝光交易，本期仅背景回顾，不拆成新的融资新闻',['Circle Games']),
 ('B008','Steam新品节预玩产品超过8200款',['S0469'],(2,2,1),'全球PC供给数据有迁移，R2；5分，纯在线纪录不抬E',[]),
 ('B009','Rovio重新聚焦Angry Birds与Sonic',['S0705'],(3,2,1),'明确在研产品单独召回，但海外移动一般主体R2，7分',[]),
 ('B010','网易代理相关常规财报经营背景',['S0884'],(2,3,1),'旧财报翻译与常规同比不是异常财务事件，财报门禁排除',[]),
 ('B011','育碧关闭RedLynx并裁减新加坡岗位',['S0895','S0917','S1144','S1175'],(2,2,2),'工作室关停E2、明确行业组织迁移R2、多源M2，总分6',[]),
 ('B012','海外PC单机《战锤40K：爆矢枪2》发售',['S1119','S1199'],(3,1,2),'海外PC/主机单机纯发售R1，5分；日历另查绝对日期',[]),
 ('B013','网易此前商标与当前极限战场首曝比较',['S0043'],(3,3,1),'历史商标阶段已由I001实质首曝更新覆盖，不拆第二条',['极限战场']),
 ('B014','PC端游《太吾异世劫》发售',['S0011','S1287'],(3,1,2),'发售E3、多源M2；本地记录没有明确国内开发主体例外依据，不凭太吾IP或角色扮演标签猜R3；日历独立采用',[]),
]:
    e,r,m=sc;hc=history(terms)
    d={'candidate_id':cid,'section':'industry','source_ids':ids,'entities':[title],'event':title,'decision':'exclude','reason':reason,'scores':{'event':e,'relevance':r,'hook':m,'total':e*r+m},'history_check':hc}
    if len(ids)>1:d['cluster_basis']={'subject':title,'product':title,'event_date':S[ids[0]]['date'],'event':title}
    scope(d);decisions.append(d)

# 对全部AI/社区/深度原始记录补齐独立审计，不把行业候选判断替代它们。
for s in rows:
    if s['section'] not in ['ai_trends','community_discourse','deep_analysis'] or s['source_id'] in consumed:continue
    sid=s['source_id'];sec={'ai_trends':'ai','community_discourse':'community','deep_analysis':'deep'}[s['section']]
    match=next((d for d in decisions if d['decision']=='include' and d['section']==sec and any(S[q]['url']==s['url'] for q in d['source_ids'])),None)
    d={'candidate_id':'U'+sid[1:],'section':sec,'source_ids':[sid],'entities':[s['title']],'event':s['title'],'decision':'merge' if match else 'exclude','reason':'同一社区事件/同URL连续采集，归并本周事件' if match else f"《{s['title']}》已读取正文反扫；"+('泛科技融资/硬件/例行模型消息或可迁移证据弱于已采用游戏直接作用事件' if sec=='ai' else '旧讨论无实质新增，或可命名事件在本期3条社区上限外' if sec=='community' else '周五只消费精确飞书selection，不自动增加其他深度题')}
    if match:d['merge_into']=match['candidate_id']
    if sec=='ai':d.update(ai_tier='transferable_frontier',game_stage=['development'],industry_reverse_scan=False,migration_path='若有后续实证，可作用于游戏研发、评测或交互；当前证据不足以采用')
    if sid=='S0788':d.update(decision='merge',merge_into='A002',reason='同一Epic迪士尼项目的AI优先与延期报道，归并A002；不用聚合站重复作事实源',ai_tier='direct_application',game_stage=['development'])
    if sid=='S0553':d.update(reason='游戏制作多工具教程为直接应用候选，但属于流程演示，未提供本期独立产品状态或可核验产出结果',ai_tier='direct_application',game_stage=['development'])
    if sid=='S1268':d.update(reason='Matrix-Game 4.0为直接游戏技术候选，但本地虽标full，实际只有AI导读和发布主张；未取到原始技术正文，不用摘要作为唯一核心证据',ai_tier='direct_application',game_stage=['development','product'])
    if sec=='deep':d['scores']={'relevance':2,'insight':2,'evidence':2,'card':2,'total':8}
    decisions.append(d)

# 下阶段补写日历与周内汇总轨迹，再统一输出。
exec((P/'calendar_and_finish.py').read_text(encoding='utf-8'))
