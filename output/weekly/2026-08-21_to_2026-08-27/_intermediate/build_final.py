import json, re, sys, hashlib
from pathlib import Path
from collections import Counter, defaultdict

P=Path(__file__).parent; W=Path.cwd(); OUT=P.parent; ID='2026-08-21_to_2026-08-27'
def rd(p): return json.loads(p.read_text(encoding='utf-8'))
def wr(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rows=list(map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()))
S={r['source_id']:r for r in rows}; H=rd(P/'industry_history_14d.json')['occurrences']; CW=rd(P/'current_week_published_history.json')['occurrences']
base=rd(P/'current_week_prior_items.json'); deep=rd(P/'deep_handoff_import.json')['items']; audit=rd(P/'release_calendar_audit.json')
items=[]; decisions=[]; handled={}; counts=Counter()

def exposure(o):
    return f"{o['title']}｜{o['report_kind']} {o['report_window']['start']}_to_{o['report_window']['end']}｜card_exposed={str(o.get('card_exposed')).lower()}｜card_rank={o.get('card_rank')}｜card_limit={o.get('card_limit')}｜card_exposure_source={o.get('card_exposure_source')}"
def history(pattern=None, novelty='new_event', new=None, current_pattern=None):
    matches=[o for o in H if pattern and re.search(pattern,o['title']+' '+o.get('event',''),re.I)]
    if current_pattern: matches += [o for o in CW if re.search(current_pattern,o['title']+' '+o.get('event',''),re.I)]
    return {'history_match':bool(matches),'novelty':novelty if matches else 'new_event','prior_occurrences':[exposure(o) for o in matches],'new_facts':new or [],'prior_card_exposed':any(o.get('card_exposed') for o in matches) if matches else None}
def score(e,r,m): return dict(event=e,relevance=r,hook=m,total=e*r+m)
def evidence(sid, needles=None):
    t=S[sid]['text']
    if not needles:return t
    if isinstance(needles,str):needles=[needles]
    positions=[]
    for n in needles:
        k=t.find(n)
        if k<0: raise ValueError((sid,n))
        a=t.rfind('\n',0,k)+1; b=t.find('\n',k+len(n));positions.append((a,len(t) if b<0 else b))
    return t[min(a for a,b in positions):max(b for a,b in positions)]
def register(cid,section,title,ids,event,decision,reason,sc=None,h=None,entities=None,dt=None,body='',**extra):
    ids=list(dict.fromkeys(ids)); d=dict(candidate_id=cid,section=section,title=title,source_ids=ids,entities=entities or [title],event=event,decision=decision,reason=reason,priority_tracks=[])
    if sc:d['scores']=sc
    if section=='industry':d['history_check']=h or history()
    if len(ids)>1 and section in ['industry','release_calendar']:
        d['cluster_basis']={'subject':(entities or [title])[0],'product':title,'event_date':dt or min(S[x]['date'] for x in ids),'event':event}
    d['facts']=body or next((z.strip() for z in S[ids[0]]['text'].split('\n') if len(z.strip())>30 and not z.startswith(('来源','Title:','Original URL:','http'))),S[ids[0]]['text'])
    d.update(extra);decisions.append(d)
    for sid in ids: handled.setdefault(sid,cid)
    return d
def add(title,ids,parts,e=3,r=3,m=1,entities=None,dt=None,cp=None,novelty='new_event',section='industry',**extra):
    prefix={'industry':'I','ai':'A','community':'C'}[section];counts[prefix]+=1;cid=f'{prefix}{counts[prefix]:03d}'
    body=''.join(p[0] for p in parts)
    claims=[dict(claim=p[0],source_id=p[1],evidence=evidence(p[1],p[2] if len(p)>2 else None)) for p in parts]
    item=dict(candidate_id=cid,section=section,title=title,source_ids=ids,body=body,claims=claims)
    if 'community' in extra:item['community']=extra['community']
    h=history(current_pattern=cp,novelty=novelty,new=[p[0] for p in parts] if novelty=='material_update' else [])
    reason=f'E{e}×R{r}+M{m}={e*r+m}，达到周报8分门槛；主体、事件类型及新鲜度均由当前来源支持。'
    if cp and h['history_match']: reason+=' 本周日报/周末报事件尚未进入已发布周报，本周仅汇总一次。'
    register(cid,section,title,ids,title,'include',reason if section=='industry' else '直接应用案例或持续争议链条证据充分，按分区规则入选。',score(e,r,m) if section=='industry' else None,h,entities,dt,body,**extra)
    items.append(item); return cid

# Industry: independent events, no arbitrary cap. A later article may report a prior-day event;
# the reporting window applies to collected news, while the true event date stays in this audit.
add('郭炜炜宣布离开西山居，8月28日为最后任职日',['S1233','S1235'],[
 ('8月27日，郭炜炜宣布将离开西山居，8月28日是其在公司的最后任职日。','S1235',['明日（8月28日）','西山居']),
 ('他已于2025年12月辞去CEO职务、转任首席制作人，此次进一步结束与公司的长期任职关系。','S1235',['2025年12月1日','首席制作人'])],m=2,entities=['西山居','郭炜炜'],dt='2026-08-27')
add('腾讯签约出售Netmarble约13.4%股权，交易完成后持股降至4.69%',['S0624','S0645'],[
 ('腾讯全资子公司Han River Investment签署协议，拟将Netmarble约13.4%股权以3740.63亿韩元出售给网石董事长房俊爀。','S0624'),
 ('交易完成后，腾讯持股将由18.11%降至4.69%；这是已签约的股权处置安排。','S0624')],m=2,entities=['腾讯','Netmarble'],dt='2026-08-21',cp='Netmarble')
add('腾讯领投W4 Games的1800万美元B轮，双方签署Godot亚洲合作',['S0649','S0675'],[
 ('W4 Games完成1800万美元B轮融资，由腾讯领投；双方同时签署多年战略合作，支持Godot生态及W4技术在亚洲的发展。','S0649'),
 ('合作涵盖本地化、生态支持和市场拓展，W4并计划扩大国际团队。','S0649')],m=2,entities=['腾讯','W4 Games'],dt='2026-08-25',cp='W4 Games')
add('育碧公布《英雄无敌III重制版》，成都与上海团队主导开发',['S0964','S1017'],[
 ('育碧在科隆游戏展公布《魔法门之英雄无敌III重制版》，由育碧成都与育碧上海主导开发。','S0964'),
 ('项目采用Snowdrop引擎，将经典内容转为3D表现，并保留随机地图、地图编辑器和多人玩法。','S0964')],m=2,entities=['育碧成都','育碧上海'],dt='2026-08-26',cp='英雄无敌')
add('钻石猫首曝《伊始之猫》，以知识驱动探索与战斗',['S0629','S0723'],[
 ('广州钻石猫工作室首曝买断制ARPG《伊始之猫》，将动作、探索与解谜结合。','S0629'),
 ('项目以“知识锁”为核心：玩家理解世界规则后，才能发现新的路径和战斗方式。','S0629')],m=2,entities=['钻石猫','伊始之猫'],dt='2026-08-25',cp='伊始之猫')
add('Krafton公布《PUBG: DED.NET》，探索多人射击与肉鸽成长',['S1084','S1325'],[
 ('Krafton公布多人射击新作《PUBG: DED.NET》，以20世纪90年代的卡斯卡迪亚为背景，结合FPS战斗与Roguelite成长。','S1084'),
 ('项目已开放封闭测试报名。','S1084')],m=2,entities=['Krafton','PUBG: DED.NET'],dt='2026-08-26')
add('Paradox公布《LEGO Skylines》，将乐高积木用于城市建造',['S1089','S1048'],[
 ('Paradox公布由Iceflake Studios开发的城市建造游戏《LEGO Skylines》。','S1089'),
 ('玩家可用乐高积木规划城市、管理居民需求，项目尚未公布具体发售日期。','S1089')],m=2,entities=['Paradox','LEGO Skylines'],dt='2026-08-26')
add('《破坏领主2》正式公布，计划2027年开启抢先体验',['S1210','S1324'],[
 ('暗黑奇幻动作RPG《破坏领主2》正式公布，计划于2027年开启抢先体验。','S1210'),
 ('游戏支持单人或与最多三位好友合作，通过武器、天赋与装备组合构筑战斗方式。','S1324')],m=2,entities=['破坏领主2'],dt='2026-08-27')
add('Paradox正式公布《Afterworld》，科技树依赖探索发现',['S1094','S1051'],[
 ('Paradox正式公布末世大战略游戏《Afterworld》，玩家将经营幸存者部落，从食物、水和聚落生存起步。','S1094'),
 ('科技与观念需要在探索和实践中发现；地图地形固定，但部落、资源与危险会程序化变化。','S1094')],m=2,entities=['Paradox','Afterworld'],dt='2026-08-26',cp='Afterworld')
add('《WARDOGS》开展封闭Beta，开发者披露近50万玩家参与',['S0016','S0735'],[
 ('百人三方战术FPS《WARDOGS》在周末开展封闭Beta，开发者Bulkhead随后披露，近50万名玩家参与了测试。','S0735'),
 ('产品计划于9月10日进入抢先体验。','S0735')],m=2,entities=['Bulkhead','WARDOGS'],dt='2026-08-22',cp='Wardogs|WARDOGS')
add('上海英澈进入破产清算，两款游戏暂时停服',['S1259'],[
 ('上海英澈网络进入破产清算程序，旗下《千年之旅ELF》与《晴空之下》于8月26日公告暂时停服，以处理运营权限交接。','S1259'),
 ('报道同时指出，停服公告随后删除了部分有关资产保全及后续安排的表述。','S1259')],entities=['上海英澈网络'],dt='2026-08-26',cp='英澈')
add('Roblox拟在利雅得设立中东北非总部，并支持当地创作者',['S1269'],[
 ('Roblox计划在沙特阿拉伯利雅得设立中东北非地区总部，并推出面向当地创作者的支持计划。','S1269'),
 ('该计划获得沙特投资部、利雅得创意区及媒体监管机构支持。','S1269')],entities=['Roblox'],dt='2026-08-26')
add('腾讯ACE与腾讯云、Sandbox Interactive合作，支持《Albion Online》安卓安全',['S1255'],[
 ('腾讯游戏安全ACE、腾讯云与Sandbox Interactive达成合作，为《Albion Online》安卓端提供安全支持。','S1255'),
 ('方案结合客户端与服务端验证，使用ACE Standard服务。','S1255')],entities=['腾讯ACE','Sandbox Interactive'],dt='2026-08-27')
add('天津九河游创游戏孵化器成立，为小团队提供场地支持',['S0137'],[
 ('游戏茶馆、罗斯基、天津天创社与坤舆工作室联合成立天津九河游创游戏孵化器，提供约1500平方米空间。','S0137'),
 ('符合条件的8人及以下游戏团队可申请免费工位，并获得研发与发行资源对接。','S0137')],entities=['天津九河游创'],dt='2026-08-21',cp='天津|孵化器')
add('《绝区零》首席美术“阿兔朋友”宣布离职，转向独立种田游戏',['S0040'],[
 ('《绝区零》首席美术“阿兔朋友”于8月20日宣布离开米哈游，接下来将独立开发种田模拟游戏。','S0040')],entities=['米哈游','阿兔朋友'],dt='2026-08-20',cp='阿兔|首席美术')
add('国产单机《只狗：路边一条》首曝，计划年底开展非公开测试',['S0928'],[
 ('红魂制作组首曝国产单机《只狗：路边一条》，以叼剑的流浪狗为主角，采用传送式箱庭关卡设计。','S0928'),
 ('团队已从3人扩充至9人，并计划在2026年底开展非公开Playtest测试。','S0928')],entities=['红魂制作组','只狗：路边一条'],dt='2026-08-20',cp='只狗')
add('育碧公布《Rainbow Six Tactics》，采用单人回合制战术玩法',['S1081'],[
 ('育碧公布《Rainbow Six Tactics》，由《马力欧+疯狂兔子》团队开发，计划于2027年推出。','S1081'),
 ('游戏结合实时侦察、突入与回合制战斗，采用买断制单人体验，不设置游戏内商店。','S1081')],entities=['育碧','Rainbow Six Tactics'],dt='2026-08-26')
add('Atari公布《RollerCoaster Tycoon Wonderworks》，由Springloaded开发',['S1087'],[
 ('Atari公布由Springloaded开发的乐园经营新作《RollerCoaster Tycoon Wonderworks》。','S1087'),
 ('项目计划以抢先体验方式推出，尚未给出具体日期。','S1087')],entities=['Atari','RollerCoaster Tycoon Wonderworks'],dt='2026-08-26')
add('Krafton发行动作RPG《Tarae: The Unbound》，引入五行与轮回构筑',['S1095'],[
 ('Boundary开发、Krafton发行的动作RPG《Tarae: The Unbound》在科隆展亮相，以东方神话为背景。','S1095'),
 ('战斗与成长系统结合五行、阴阳和轮回，项目尚未公布发售日期。','S1095')],entities=['Krafton','Tarae: The Unbound'],dt='2026-08-26')
add('《王国3：开疆拓土》公布，计划2027年登陆PC与主机',['S1357'],[
 ('《王国3：开疆拓土》正式公布，玩家将扮演君主，招募臣民、重建岛屿并防御贪婪生物。','S1357'),
 ('游戏计划于2027年登陆PC、PS5、Xbox Series及Switch 2。','S1357')],entities=['王国3：开疆拓土'],dt='2026-08-27')
add('塔防Roguelite新作《英雄绞碎场》公布，计划2027年发售',['S0614'],[
 ('塔防Roguelite游戏《英雄绞碎场》正式公布，计划于2027年发售。','S0614')],entities=['英雄绞碎场'],dt='2026-08-25')
add('《赫尔铸界》公布，以合成消除结合回合制肉鸽构筑',['S0455'],[
 ('《赫尔铸界》公布，以北欧神话为背景，将合成消除、物理堆叠与回合制肉鸽构筑结合。','S0455'),
 ('游戏计划于2027年第一季度在Steam开启抢先体验。','S0455')],entities=['赫尔铸界'],dt='2026-08-24')
add('《Acornia: Mirror Worlds》公布，结合店铺经营与动作冒险',['S0896'],[
 ('《Acornia: Mirror Worlds》正式公布，玩家将扮演松鼠，在店铺经营与动作冒险之间切换。','S0896')],entities=['Acornia: Mirror Worlds'],dt='2026-08-26')
add('4X策略游戏《魔法大战略：穆瑞耶之心》推出免费Demo',['S0052'],[
 ('Matthias Schindler开发、2P Games联合发行的即时制4X策略游戏《魔法大战略：穆瑞耶之心》在Steam推出免费Demo。','S0052'),
 ('玩家从建立聚落起步，结合施法、研究、领土扩张与战术暂停推进征服。','S0052')],entities=['2P Games','魔法大战略：穆瑞耶之心'],dt='2026-08-21')
add('《超自然行动组》DAU突破1200万',['S0371','S0386'],[
 ('巨人网络宣布《超自然行动组》日活跃用户突破1200万，距离今年2月首次公布破千万约半年。','S0371','DAU）突破1200万'),
 ('7月登陆抖音小游戏平台后，产品曾实现单日新增用户突破100万。','S0371','单日新增突破100万')],e=2,m=2,entities=['巨人网络','超自然行动组'],dt='2026-08-24',cp='超自然行动组')
add('《影之刃零》Steam预购首周收入估算约1450万美元',['S0618','S0623','S0942'],[
 ('据Alinea Analytics估算，《影之刃零》开启预购一周内在Steam产生约1450万美元收入，达到《黑神话：悟空》同期数据的73%。','S0942',['1450万美元','73%']),
 ('同篇报道披露其Steam愿望单已超过200万；预购表现与愿望单均不等同于正式发售后的实际销量。','S0942','愿望单人数已突破200万')],e=2,m=2,entities=['影之刃零'],dt='2026-08-25',cp='影之刃零')
add('Thatgamecompany成立发行部门，资金与发行服务面向独立项目',['S0653','S0676'],[
 ('Thatgamecompany成立Thatgamepublisher，并已签下数款尚未公布的游戏，计划把《Sky: Children of the Light》的利润投入情感导向项目。','S0653'),
 ('新部门可提供资金、制作规划、营销、社区及平台策略服务，支持范围从单人作品到AA级预算项目。','S0653')],r=2,m=2,entities=['Thatgamecompany'],dt='2026-08-25',cp='Thatgamecompany|Thatgamepublisher')
add('Riot将于12月结束《2XKO》主动开发，服务器仍将保留',['S0058','S0116','S0147'],[
 ('Riot宣布于12月结束《2XKO》的主动开发，原因是运营成本显著高于收入，较大更新也未持续改变用户参与走势。','S0058'),
 ('游戏仍可免费下载，服务器将保留至2026年之后；团队已启动历史付费退款，并安排剩余更新。','S0058')],e=2,m=2,entities=['Riot Games','2XKO'],dt='2026-08-20',cp='2XKO')
add('Roblox限制儿童入口中的奖励驱动媒体流',['S0973','S1193'],[
 ('Roblox针对Kids和Select新增限制：若体验以连续观看奖励驱动自动播放或无限滚动的媒体流，将不能进入这两类入口。','S0973'),
 ('平台表示，规则不影响由用户主动触发且设有观看次数限制的Rewarded Video Ads。','S0973')],e=2,m=2,entities=['Roblox'],dt='2026-08-26',cp='奖励驱动媒体流|奖励.*媒体')
add('《巫师4》以2028年为目标发行窗口',['S0729','S0613'],[
 ('CD Projekt联合CEO Michał Nowakowski表示，《巫师4》正以2028年为目标发行窗口，目前尚未给出确切日期。','S0729'),
 ('他同时披露，项目已有超过500名开发者参与。','S0729')],e=2,m=2,entities=['CD Projekt','巫师4'],dt='2026-08-24',cp='巫师4|Witcher')
add('Double Fine确认收回游戏IP与发行权，销售收入将支持独立运营',['S0401','S0446'],[
 ('Double Fine确认，在脱离Xbox后已重新获得此前在微软旗下发行的全部游戏IP与发行权。','S0446'),
 ('Tim Schafer表示，玩家购买既有作品的收入将直接支持工作室运营；部分商店权属标注仍待手续更新。','S0446')],r=2,m=2,entities=['Double Fine'],dt='2026-08-21')
add('Compulsion完成管理层收购，重新拥有工作室与原创IP',['S0062','S0337'],[
 ('Compulsion Games完成管理层收购，管理团队取得工作室及员工组织，微软将原创游戏IP转回公司。','S0337'),
 ('这一交易使《South of Midnight》开发团队重新独立，并恢复对自身作品的控制。','S0337')],r=2,m=2,entities=['Compulsion Games'],dt='2026-08-20')
add('Entity获种子融资，计划以浏览器承载本地运行游戏',['S0968','S0677'],[
 ('Entity完成种子轮融资，投资方包括ACT、Delta Partners与Elkstone，并获得Enterprise Ireland支持。','S0968'),
 ('公司计划于2027年初推出游戏平台，通过WebGPU与WebAssembly在用户设备本地运行游戏，玩家可由链接进入，无需安装。','S0968')],r=2,m=2,entities=['Entity'],dt='2026-08-25',cp='Entity',source_conflict='两篇报道美元金额为500万与580万，后一篇同时标明500万欧元；正文仅保留融资及技术路线共同事实，不写金额。')
add('《伊莫》公布双端档期，PC与移动端分别于9月上线',['S1254','S1138'],[
 ('多人在线捉宠RPG《伊莫》公布上线安排：PC端为9月16日，移动端为9月23日。','S1254'),
 ('该作由爪印工作室研发，计划以跨平台方式支持多人探索与生物收集。','S1254')],e=2,m=2,entities=['爪印工作室','伊莫'],dt='2026-08-26')
add('《王者万象棋》定档9月10日，覆盖PC与移动端',['S1305','S1310'],[
 ('腾讯《王者万象棋》定档9月10日，计划在PC与移动端上线。','S1310'),
 ('该作以自走棋玩法为基础，定档时公布全网预约已超过7000万。','S1310')],e=2,m=2,entities=['腾讯','王者万象棋'],dt='2026-08-27')

# AI: all six are direct applications. Other industry AI signals remain auditable below.
add('腾讯披露Motus动画管线，将AI生成资产接入正式制作流程',['S0935'],[
 ('腾讯游戏公共技术线披露，Motus AI已覆盖骨骼、蒙皮、文本或视频生动作、关键帧插帧与动作精修等环节。','S0935','据公共技术线专家'),
 ('分享者称，Agent可先产出模型、蒙皮与绑定结果供动画验证，待正式资产完成后再替换；不同项目仍需逐一适配。','S0935',['Agent用一天','一个个适配融入'])],section='ai',ai_tier='direct_application',game_stage=['development'],industry_reverse_scan=True)
add('Roblox开源三款安全模型，覆盖隐私识别与内容治理',['S0059'],[
 ('Roblox开源PII Classifier、Roblox Sentinel及语音安全相关模型，将已用于平台治理的能力开放给外部开发者。','S0059'),
 ('工具覆盖个人身份信息识别、文本与语音安全，并通过ROOST推动共享使用。','S0059')],section='ai',ai_tier='direct_application',game_stage=['operations'],industry_reverse_scan=True)
add('233工坊披露生成后审核机制，7月逾500款作品通过上线审核',['S0752'],[
 ('233乐园披露，基于自然语言交互的233工坊在7月有超过500款作品通过审核上线。','S0752','7月单月，通过审核上线'),
 ('平台同时审查合规与内容安全，由人工体验游戏性、完整度和亮点，再引入社区反馈支持持续修改。','S0752','审核分为两个层面')],section='ai',ai_tier='direct_application',game_stage=['development','publishing','operations'],industry_reverse_scan=True)
add('Side与Modl.ai签署合作备忘录，将AI引入游戏QA',['S1268'],[
 ('Side与Modl.ai签署为期六个月的合作备忘录，探索以AI执行游戏QA，并保留人工判断。','S1268'),
 ('方案可依据游戏画面操作，不必接入SDK或取得源代码，输出问题记录与视频；现阶段更适合拼图、卡牌等重复测试任务。','S1268')],section='ai',ai_tier='direct_application',game_stage=['development'],industry_reverse_scan=True)
add('Team Liquid与SAP展示语音分析工具，辅助教练复盘沟通',['S0692'],[
 ('Team Liquid与SAP展示AI辅助复盘工具，对队内语音进行说话人区分、转录和情绪分析，并与游戏时间线对齐。','S0692'),
 ('教练可据此定位沟通问题、调整训练重点，工具承担分析辅助角色。','S0692')],section='ai',ai_tier='direct_application',game_stage=['operations'],industry_reverse_scan=True)
add('Meta的AI小游戏应用Pocket扩展至美国测试',['S0078'],[
 ('据Mobilegamer援引TechCrunch报道，Meta的AI小游戏制作与分享应用Pocket已从巴西扩展至美国用户，仍处于早期测试阶段。','S0078',['Pocket (Meta)','previously only available in Brazil']),
 ('应用允许用户通过文字、照片、触摸和声音等输入生成简短互动内容，并以信息流组织分享。','S0078','TikTok-like app')],section='ai',ai_tier='direct_application',game_stage=['product','publishing'],industry_reverse_scan=True)

# Community: paraphrase player claims with explicit attribution, and preserve dated follow-up.
def community(trigger,logic,timeline,ids):return dict(trigger=trigger,claim_scope='玩家帖子与采集到的讨论，不升级为官方已确认事实',complaint_logic=logic,timeline=timeline,follow_up_scan={'source_ids':ids,'result':'按同产品反扫本窗口后续公告转述、回复和纠偏；正文只使用窗口内已有记录。'})
c=community('版本前瞻后的复刻卡池继承争议','玩家关注同角色复刻继承与首次UP不继承的差别，以及未来复刻间隔。',['8月21日前瞻后出现规则解读','8月22日起讨论限定条件','8月24日仍讨论继承范围'],['S0311','S0356','S0595'])
add('《终末地》复刻保底规则引发讨论，玩家关注首次UP与复刻的区别',['S0311','S0356','S0595'],[
 ('围绕版本前瞻，玩家将复刻卡池规则理解为仅同一角色的复刻之间继承，并指出首次UP投入不在同一继承范围。','S0311'),
 ('支持者认为这降低了后续补角色的压力；争议集中在首次投入无法承接、复刻等待时间和规则理解成本。','S0356'),
 ('到8月24日，讨论仍集中在具体继承条件，而非单纯是否增加保底。','S0595')],section='community',community=c)
c=community('角色周边实物与商品描述差异的玩家投诉','先有色纸材质与销毁补发争议，后有立牌高度及修改详情的质疑。',['8月20日原帖更新色纸售后变化','8月25日追加爱弥斯立牌尺寸问题','8月26日新帖讨论商品描述变化与退款'],['S1175','S1178'])
add('《鸣潮》周边争议从色纸补发延伸到立牌尺寸与商品描述',['S1175','S1178'],[
 ('玩家在陆赫斯礼盒色纸争议帖中更新称，原先要求销毁再补发的处理已调整；8月25日又追加爱弥斯立牌实物高度与原商品描述不符的问题。','S1175'),
 ('8月26日，玩家质疑把“高约200mm”改成宽高描述的做法，争议集中在售前承诺与售后责任。','S1178'),
 ('部分玩家接受退货退款，另一些玩家更在意能否按原承诺补发。','S1178')],section='community',community=c)
c=community('更新空窗后的招聘与备案线索讨论','玩家争论招聘和网站备案是否能说明研发恢复及版本日期。',['前期更新延后后持续关注后续版本','8月25日围绕招聘岗位讨论产能','8月27日出现ICP备案截图解读'],['S0874','S0881','S1462'])
add('《尘白禁区》招聘与备案线索接连出现，玩家争论能否转化为实际更新',['S0874','S0881','S1462'],[
 ('在更新空窗的讨论背景下，《尘白禁区》玩家于8月25日围绕招聘信息争论：有人把岗位开放视为积极信号，也有人担心补齐人员和交接仍需要时间。','S0881'),
 ('8月27日，新的备案截图讨论继续升温；部分玩家认为网站ICP备案与游戏运营主体审批不能直接画等号，争议集中在这些线索能否说明游戏将恢复更新。','S1462',['2026-08-27 14:49','运营主体改变','ICP这东西'])],section='community',community=c)

# Calendar prefix; exact source identities and absolute dates remain in the corrected audit.
calendar=[
 ('仙境传说3',['S1412','S1429','S0433'],'bilibili开发发行的多平台MMORPG《仙境传说3》于8月27日开启“重逢测试”，覆盖PC、Android与iOS。','S1412','bilibili','PC / Android / iOS'),
 ('骤影·绯月杀',['S0368','S0644'],'网易投资团队星汉明空研发的多人动作推理端游《骤影·绯月杀》于8月25日开启首次公开测试，将身份推理与ARPG战斗结合。','S0644','星汉明空','PC'),
 ('诡秘之主',['S0036','S0189'],'弹指宇宙研发的多平台MMORPG《诡秘之主》于8月21日正式公测，以蒸汽朋克与神秘学题材构建角色扮演体验。','S0036','弹指宇宙','多端'),
 ('1666：阿姆斯特丹',['S0941','S1059'],'Panache Digital Games剧情动作冒险单机《1666：阿姆斯特丹》于8月25日在PC端开启抢先体验，登陆Steam与Epic。','S0941','Panache Digital Games','PC / Steam / Epic'),
 ('异克斯小队',['S0931','S0965'],'Behaviour Interactive研发、腾讯国内发行的多平台合作PvE射击游戏《异克斯小队》于8月26日首曝，计划2027年登陆PC、PS5与Xbox Series X|S。','S0931','Behaviour Interactive / 腾讯','PC / PS5 / Xbox Series X|S'),
 ('无限大',['S0936','S1142'],'网易Naked Rain多平台都市开放世界游戏《无限大》于8月26日公布上线档期，计划2027年1月15日在PC、PS5与移动端免费推出。','S0936','网易Naked Rain','PC / PS5 / 移动端'),
 ('源初之结',['S0930','S0937','S1147'],'米哈游多平台动作共斗游戏《源初之结》于8月26日正式首曝，采用UE5构建写实奇幻世界，面向PC与主机平台。','S0937','米哈游','PC / 主机'),
]
for n,data in zip(audit['nodes'][:7],calendar):
    name,ids,body,sid,company,platform=data; assert n['product']==name
    claims=[{'claim':body,'source_id':sid,'evidence':S[sid]['text']}]
    # A full-sentence claim can have several complementary evidence records.
    if name=='仙境传说3':claims.append({'claim':'MMORPG','source_id':'S1429','evidence':S['S1429']['text']})
    if name=='无限大':claims.append({'claim':'8月26日','source_id':'S1142','evidence':S['S1142']['text']})
    if name=='源初之结':claims += [{'claim':'PC与主机平台','source_id':'S1147','evidence':S['S1147']['text']},{'claim':'UE5','source_id':'S0930','evidence':S['S0930']['text']}]
    items.append(dict(candidate_id=n['candidate_id'],section='release_calendar',title=name,source_ids=ids,body=body,claims=claims,release=dict(product=name,event=n['event'],date=n['event_date'],platform=platform,company=company)))
    for x in n['source_ids']: handled.setdefault(x,n['candidate_id'])

for it in deep:
    items.append(it)
    register(it['candidate_id'],'deep',it['title'],it['source_ids'],it['title'],'include','精确周报selection人工选择，保持C057/C008/C001顺序与指定卡片。',it['scores'],body=it['body'],card_designated=it.get('card_designated',False),handoff_selection=str(W/'output/deep_observation_review'/f'{ID}_selection.md'))

def exclude(cid,title,ids,e,r,m,reason,pattern=None,cp=None,novelty='repeat_only',new=None,entities=None,**extra):
    return register(cid,'industry',title,ids,title,'exclude',reason,score(e,r,m),history(pattern,novelty,new,cp),entities,body='',**extra)
# Deliberate boundary decisions, historical same-event matches and high-priority scans.
exclude('X001','《Gangstar Mirage City》区域上线旧事件',['S0967'],3,3,1,'上一周报已收录且8月26日订阅卡片第4/10位已曝光，禁止再次补位。',pattern='Gangstar',cp='Gangstar',entities=['腾讯','Gangstar Mirage City'])
exclude('X002','Makers Fund第四期基金2.5亿美元',['S0074','S0993'],3,2,1,'本期一条摘要及一条完整综述召回；前周报未曝光，但同事件只有一个可用全文来源、7分低于周报线，不具备补位资格。',pattern='Makers',entities=['Makers Fund'])
exclude('X003','灵犀互娱出售签约与阿里退出',['S0266'],3,3,0,'同一签约状态已进入历史卡片，周回顾与转载不构成状态变化。',pattern='灵犀.*(交易|收购)|(交易|收购).*灵犀',entities=['灵犀互娱'])
exclude('X004','《雾海之下》首测回顾',['S0039'],3,3,0,'首测已在双周历史卡片曝光，当前财报稿再次提及测试而无新测试状态。',pattern='雾海',entities=['网易','雾海之下'])
exclude('X005','《异环》20亿元流水与完美半年报',['S0028'],2,3,0,'流水事实已曝光，常规半年报比较不满足财务例外。',pattern='异环',entities=['完美世界','异环'])
exclude('X006','《梦幻模拟战》续作《剑之海》测试分析',['S0037','S0395'],3,3,0,'8月20日测试已入历史卡片，换媒体及玩法分析无新状态。',pattern='剑之海',entities=['紫龙','剑之海'])
exclude('X007','苹果欧盟抽成与站外支付变化',['S0282'],2,2,0,'同一欧盟平台政策已被历史日报卡片展示，重复阐释排除。',pattern='苹果.*欧盟|Apple.*EU',entities=['Apple'])
exclude('X008','《生存日志》进入Steam中国畅销榜前十',['S0379'],2,3,1,'较此前第15名有可验证排名变化，但单源7分不足周报线。',pattern='生存日志',cp='生存日志',novelty='material_update',new=['当前报道进入Steam中国畅销榜前十，早前历史为前十五。'],entities=['生存日志'])
exclude('X009','《无畏契约手游》畅销榜升至第二',['S0380'],2,3,1,'相对此前注册破亿为新增商业表现，但单源7分不达周报线。',pattern='无畏契约',cp='无畏契约',novelty='material_update',new=['当前报道国区iOS游戏畅销榜第二。'],entities=['腾讯','无畏契约手游'])
exclude('X010','Newzoo发布2026年市场预测',['S0650'],2,3,1,'与2025年结构报告不同：新增2026年预测，但单源该预测总分7。后续主机访谈是另一日期事件，不为提高M强行聚类。',pattern='Newzoo',novelty='material_update',new=['2026年全球市场预测2139亿美元、增长6.1%；移动预测1211亿美元、增长6.8%。'],entities=['Newzoo'])
exclude('X011','中手游不再立项大体量自研项目',['S0939','S0966','S1245'],1,3,2,'主营讨论为业绩会战略表态，未给出本窗口新取消的具体项目；不将表态抬为组织交易。常规亏损收窄不满足财报例外。',cp='中手游',novelty='new_event',entities=['中手游'])
exclude('X012','Xbox宣布实体光盘转数字授权计划',['S1263','S1286','S1328'],2,2,2,'分发与游戏保存的迁移点明确，但E2×R2+M2=6低于周报线。',novelty='new_event',entities=['Xbox'])
exclude('X013','Rovio关闭哥本哈根工作室并取消《Sonic Blitz》',['S0680'],2,3,1,'来源明确项目是跑酷与CCG混合，命中卡牌赛道R3；关闭与取消E2，单源7分。',novelty='new_event',entities=['Rovio','Sonic Blitz'])
exclude('X014','Observer Interactive转自发行并推迟《Rover’s Tale》',['S0061'],2,2,1,'项目发行关系变化与风险承担可观察，但单源E2×R2+M1=5。',novelty='new_event',entities=['Observer Interactive'])
exclude('X015','1047 Games停止两款射击游戏主动开发',['S1265'],2,3,1,'仅一条可用全文，另一篇为snippet不可出版；E2×R3+M1=7。',novelty='new_event',entities=['1047 Games'])
exclude('X016','MBC成立游戏工作室',['S1290'],3,2,1,'新工作室有全球资本迁移点，但不是Savvy主体；E3×R2+M1=7。',novelty='new_event',entities=['MBC'])
exclude('X017','CAA设立Frame1Games独立游戏投资项目',['S0674'],3,2,1,'资本与发行服务变化可观察，单源7分未达周报线。',novelty='new_event',entities=['CAA'])
exclude('X018','《Random Dice 2》此前上线后的商业化分析',['S0399'],2,3,1,'8月13日上线不重算本期E3，当前新鲜钩子是韩国榜单表现与机制分析，E2×R3+M1=7。',cp='Random Dice',novelty='new_event',entities=['111%','Random Dice 2'])
exclude('X019','《云顶之弈》迁移UE5',['S1240'],1,3,1,'老产品重大技术生命周期节点按E1，不以底层升级冒充新品。',novelty='new_event',entities=['Riot Games','云顶之弈'])
exclude('X020','《七界梦谭》定档年内',['S0054'],2,3,1,'已公开项目定档是E2，不是新品首次曝光；单源7分。',novelty='new_event',entities=['上海拾异','七界梦谭'])
exclude('X021','巴西带抽卡游戏年龄分级讨论',['S0033'],2,3,0,'来源写明规则在3月落地，当前未证明本周实质新政策，不能以社区图片再传播作新监管。',novelty='new_event',entities=['Riot Games','巴西游戏市场'])
exclude('X022','Newzoo主机市场对GTA6的依赖判断',['S1271'],2,2,1,'另一日期的分析师访谈单列，E2×R2+M1=5；PC发行年份是机构假设，不写为官方档期。',novelty='new_event',entities=['Newzoo'])
exclude('X023','上海塔耳塔被列为被执行人',['S0398'],1,3,1,'司法执行记录不足以证明已停业、破产或项目取消，按法律组织风险4分。',novelty='new_event',entities=['上海塔耳塔'])
exclude('X024','《沙金工业》抢先体验后的10万份销量披露',['S0483'],2,3,1,'现阶段事件是上市后的销量披露，不重复用此前EA发售计E3；市场数据单源7分。',cp='沙金',novelty='new_event',entities=['沙金工业'])
exclude('X025','《白银之城》公布多人玩法片段',['S0961'],0,3,1,'来源明确为既有项目全新宣传PV片尾15秒多人玩法展示，不是新品首次曝光或正式开测；E0排除。',novelty='new_event',entities=['乐元素','白银之城'])
register('A007','ai','腾讯GIGA跨游戏智能体架构',['S0935'],'GIGA双脑架构和Skill执行机制','exclude','与Motus为同文不同事件，单独召回；本期六条优先展示已有明确采用/合作链的案例，GIGA方向不并入Motus制造一条大事件。',ai_tier='direct_application',game_stage=['development','product'],industry_reverse_scan=True)
register('A008','ai','中手游GPA小游戏AI生产平台',['S0939'],'业绩会回顾GPA平台的生产和分成模式','exclude','属于6月已上线平台的业绩会回顾，不把既有平台上线改写为本周新事件。',ai_tier='direct_application',game_stage=['development','publishing'],industry_reverse_scan=True)
register('A009','ai','Google Cloud介绍《Colony》生成式玩法试验',['S0679'],'Colony实时推理与生成3D内容试验','exclude','直接应用候选已召回；与六个入选案例相比，当前更偏展会试验方向，未公布成熟上线状态。',ai_tier='direct_application',game_stage=['product'],industry_reverse_scan=True)

# Split digest containers into independent subject/event cards; no multi-company omnibus includes.
exclude('Z001','Century Games《Frozen Manor》出现产品页',['S0078'],1,3,1,'AppMagic产品页尚无Google Play下载，不能将准备测试写成已开测。',novelty='new_event',entities=['Century Games','Frozen Manor'])
exclude('Z002','Aptoide游戏商店重返美国Google Play',['S0078'],2,2,1,'渠道开放有迁移点，但单源E2×R2+M1=5。',novelty='new_event',entities=['Aptoide'])
exclude('Z003','《Lara Croft and the Temple of Osiris》移动版预约',['S0078'],2,2,1,'老作移动移植预注册及9月8日计划，E2×R2+M1=5。',novelty='new_event',entities=['Feral Interactive'])
exclude('Z004','《Fantasy Life i》登陆移动端',['S0078'],2,3,1,'已发布作品跨平台，生活模拟/RPG命中R3，单源7分。',novelty='new_event',entities=['Level-5','Fantasy Life i'])
exclude('Z005','《Hell Clock》登陆Android',['S0078'],2,3,1,'动作RPG老作跨平台而非全新项目，单源7分。',novelty='new_event',entities=['Rogue Snail','Hell Clock'])
exclude('Z006','《The Traitors: Anywhere》WhatsApp玩法预售',['S0078'],2,3,1,'多人推理玩法命中竞技相关性，但为区域预售及后续上线计划，7分。',novelty='new_event',entities=['CityDays'])
exclude('Z007','《Stickmen Hunt》英国iOS上线',['S0078'],3,2,1,'新移动休闲寻物游戏上线，单源7分。',novelty='new_event',entities=['Popcore'])
exclude('Z008','《Ragnarok: Adventures》日本预约与档期',['S0078'],2,3,1,'RPG新品公布10月30日档期，不是已上线，7分。',novelty='new_event',entities=['GungHo'])
exclude('Z009','《Bringer》计划科隆展示首个可玩Demo',['S0078'],2,3,1,'仅预告下一周展会首次可玩体验，尚非测试已开放，7分。',novelty='new_event',entities=['YHKT Entertainment'])
exclude('Z010','Surge Games融资300万美元用于AI辅助解谜生产',['S0993'],3,2,1,'移动解谜生产融资具有迁移点，但单源E3×R2+M1=7；不将AI表述放大为已成熟流水线。',novelty='new_event',entities=['Surge Games'])
exclude('Z011','Miniclip及美国移动广告收入结构',['S0993'],2,2,1,'美国移动休闲广告数据有品类迁移点，但非中国市场、非固定最高主体；单源5分。',novelty='new_event',entities=['Miniclip'])
exclude('Z012','《Smash Fest》带动混合休闲模仿产品增长',['S0993'],2,2,1,'第三方统计复制扩散及收入表现，E2×R2+M1=5。',novelty='new_event',entities=['Flow Games'])
for zid,title,entity in [('Z013','Testronic任命Sonia Kerr为CEO','Testronic'),('Z014','BoomBit任命Gonçalo Alemao Martins为CMO','BoomBit'),('Z015','Tripledot旗下Ludios任命Ilya Buber为总经理','Tripledot')]:
    exclude(zid,title,['S0419'],3,2,1,'逐项拆分人才快讯，核心职务变化有游戏服务/移动发行迁移点，单源7分。',novelty='new_event',entities=[entity])
for i,job in enumerate(['Kimmo Frisk中央QA专家','Vittorio Durin高级技术美术','Yana Brusynska DevOps工程师','Hans Hirth 3D美术与外包管理','Tomás González Saavedra临时产品经理'],16):
    exclude(f'Z{i:03d}','Supercell新增'+job,['S0419'],1,3,1,'逐项拆分人才快讯：专业岗位招聘并非核心公司管理层变动，也不足以证明新项目立项。',novelty='new_event',entities=['Supercell'])
exclude('Z021','腾讯新增Mustafa Yagiz Gulsun休闲游戏产品专家',['S0419'],1,3,1,'国内厂商专业岗位招聘，非核心管理层变动，4分。',novelty='new_event',entities=['腾讯'])

# Remaining prior published events are rechecked, never carried over merely because a daily used them.
for j,b in enumerate(base):
    old=b['decision']; ids=[x for x in b['item']['source_ids'] if x not in handled]
    if not ids:continue
    sec='industry' if old.get('section') in ['industry','industry_news'] else None
    if not sec:continue
    sc=old.get('scores',score(0,3,0)); total=sc.get('total',0)
    if total>=8: reason='已由本期同产品的更完整事件或产品日历条目覆盖，不再跨栏重复。'
    else: reason=f"复核本周既有报道，E{sc.get('event')}×R{sc.get('relevance')}+M{sc.get('hook')}={total}低于周报8分门槛；不因日报曾入选而放宽。"
    title=b['item']['title']; ent=old.get('entities') or [title]
    h=old.get('history_check',history())
    if h.get('novelty')=='card_carryover': h=history('Gangstar','repeat_only',current_pattern='Gangstar')
    h.setdefault('prior_card_exposed',None if not h.get('history_match') else True)
    register(f'B{j:03d}',sec,title,ids,old.get('event',title),'exclude',reason,sc,h,ent,body=b['item'].get('body',''))

# Complete source-level recall: explicitly rate non-zero events; E0 routine material is concise.
special_hist=[('灵犀','灵犀.*(交易|收购)|(交易|收购).*灵犀'),('雾海','雾海'),('异环.*20亿','异环'),('林增鸿','尘白'),('剑之海','剑之海'),('Pretty Cool|鹰角.*投资','Pretty Cool|鹰角'),('Makers Fund','Makers'),('Gangstar','Gangstar')]
ai_re=re.compile(r'\bAI\b|人工智能|生成式|智能体|大模型|AIGC|Motus|Modl\.ai',re.I)
routine=re.compile(r'评测|前瞻|攻略|预告|宣传|联动|活动|皮肤|周年|促销|折扣|优惠|财报|半年报|半年净利|Q2|评选|提名|获奖|票务|排行榜|week.*sales|review|trailer|discount|best.*class|tips|how to|DLC',re.I)
event3=re.compile(r'首曝|首测|首次公|正式公|全新.*公布|公布.*新作|新作.*公布|宣布.*成立|收购|融资|股权|破产|incorporat|acquir|funding|buyout|new studio|new game|announc.*studio|raises.*million',re.I)
event2=re.compile(r'定档|延期|延迟|停运|停服|关停|关闭|销量|下载|收入|营收|日活|DAU|市场|用户.*万|政策|抽成|开源|延长|delay|shut|clos.*studio|sales|revenue|market|policy|launch',re.I)
event1=re.compile(r'裁员|工会|劳资|诉讼|解雇|声明|访谈|离职|layoff|laid off|lawsuit|union|interview|CEO|studio',re.I)
high_entities=['Roblox','Supercell','Riot Games','Garena','Savvy','拳头','罗布乐思','超级细胞']
def classify(rec):
    title=rec['title'];t=rec['text']; first=t[:1400];e=3 if event3.search(title) else 2 if event2.search(title) else 1 if event1.search(title) else 0
    if routine.search(title) and not event3.search(title):e=0
    ent=next((x for x in high_entities if x.lower() in title.lower()),None)
    domestic=bool(re.search('腾讯|网易|米哈游|鹰角|叠纸|国产|中国|西山居|巨人|完美|中手游|三七|微信|抖音|莉莉丝|哔哩|快手',title))
    track=bool(re.search(r'策略|卡牌|回合制|MMORPG|ARPG|\bRPG\b|模拟经营|城市建造|生活模拟|自走棋|塔防|PvP|PVP',first))
    r=3 if ent or domestic or track else 2 if re.search('移动|手游|平台|发行|资本|融资|收购|browser|mobile|platform|funding|publish',title,re.I) else 1
    if re.search('显卡|笔记本|显示器|CPU|GPU|耳机|电影|真人剧|动画剧|硬件|Nvidia|AMD|Alienware',title,re.I):r=0;e=0
    m=1 if e else 0
    return e,r,m,ent or title
rescan=[]
calendar_covered={sid for n in audit['nodes'] for sid in n['source_ids']}
for rec in rows:
    sid=rec['source_id']
    if sid in handled:continue
    # Match exact text or exact URL+text, never collapse distinct status changes on a rolling URL.
    equivalent=next((x for x in rows if x['source_id'] in handled and x['text']==rec['text'] and x['section']==rec['section']),None)
    cid='Q'+sid[1:];sec=rec['section']
    if sec=='release_calendar':
        if sid not in calendar_covered:
            txt=rec['text']; title=rec['title']
            reason=('仅有聚合标题与Excerpt，未取得正文；单源未具备出版资格。' if 'Source method: google_news' in txt else '仅测试招募/预约资格信息，尚非实际开测；单源不具备正文资格。' if re.search('预约|招募|抢注',title) else '普通版本、活动、皮肤或后续宣传，不属于新品节点或重大生命周期事件；单源排除。')
            register('T'+sid[1:],'release_calendar',title,[sid],title,'exclude',reason,appearance_count=1,recall_scope='supplementary_source_scan')
        continue
    if sec=='deep_analysis':
        register(cid,'deep',rec['title'],[sid],rec['title'],'exclude','周报仅消费精确人工selection；本条未选。',dict(relevance=1,insight=1,evidence=1,card=1,total=4));continue
    if sec=='community_discourse':
        register(cid,'community',rec['title'],[sid],rec['title'],'exclude','已回扫窗口内触发与后续；相对入选三条缺少新的持续争议链或属于重复话题。');continue
    if sec=='ai_trends' or (sec=='industry_news' and ai_re.search(rec['title'])):
        direct=sec=='industry_news' and bool(re.search('游戏|game|Roblox|Twitch|Unity|Colony',rec['title'],re.I))
        register(cid,'ai',rec['title'],[sid],rec['title'],'merge' if equivalent else 'exclude','同文重复来源并入已审阅候选。' if equivalent else '反扫已成卡；相较六个直接落地案例，属一般观点/争议、摘要或泛工具迁移，未另入正文。',merge_into=handled[equivalent['source_id']] if equivalent else '',ai_tier='direct_application' if direct else 'transferable_frontier',game_stage=['development'] if direct else [],industry_reverse_scan=sec=='industry_news',migration_path='仅能推测用于游戏研发或内容生产；缺少本期可验证的完整采用链条。' if not direct else '');continue
    if sec!='industry_news':continue
    e,r,m,ent=classify(rec);reason='E=0：普通宣传/评测/活动/榜单/非游戏或背景解读，未识别独立的新状态。' if e==0 else f'单独成卡复核；E{e}×R{r}+M{m}={e*r+m}，未达周报8分门槛。'
    hh=history()
    for pat,hpat in special_hist:
        if re.search(pat,rec['title'],re.I):hh=history(hpat,'repeat_only');reason='已核对双周历史与卡片曝光，同事件补背景或转载排除。';break
    target=handled.get(equivalent['source_id']) if equivalent else None
    if target:reason='与已审阅来源全文完全一致，合并同一原始事件；不增加独立媒体计数。'
    if rec.get('body_status') in ['snippet','empty'] or rec.get('fetch_status','ok')!='ok':reason='正文未取得或只有snippet，不能支撑终稿；保留候选及当前评分。'
    elif sid=='S0383':
        e,r,m=0,3,0
        hh=history('雾海|失乐枷锁|异环','repeat_only')
        reason='媒体周汇总拆分反查：雾海首测/失乐枷锁首曝/异环流水均为历史同事件，诡秘由R003承接；招聘推测不等于米哈游新测试，裁员统计单列Q0631，不将汇总标题当一项E3事件。'
    elif e*r+m>=8 and not target and not hh['history_match']:
        rescan.append(dict(source_id=sid,title=rec['title'],scores=score(e,r,m),text=rec['text']))
        reason='待二次语义复核：标题高分信号不能直接确认首次事件/主体归属。'
    register(cid,'industry',rec['title'],[sid],rec['title'],'merge' if target else 'exclude',reason,score(e,r,m),hh,[ent],merge_into=target or '')

# Reconcile same-event syndicated coverage that uses rewritten titles, without changing dates/states.
for d in decisions:
    if d['candidate_id'] in ['Q0691','Q1278']:
        d.update(decision='merge',merge_into='I027',reason='同一Thatgamepublisher成立公告的转载/摘要；只保留I027一个事件，不按另一条平台上线计分。',scores=score(3,2,1))
    if d['candidate_id'] in ['B001','B035','B036','B037','B056']:
        target={'B001':'I009','B035':'I004','B036':'I009','B037':'I011','B056':'I028'}[d['candidate_id']]
        d.update(decision='merge',merge_into=target,reason='本周同一产品事件的先前稿/补充来源并入最新完整条目；不在周报重复成条。')
        d['history_check']=next(x['history_check'] for x in decisions if x['candidate_id']==target)
    if d['candidate_id']=='B005':d['history_check']=history('腾讯Q2','material_update',['本期报道《三角洲行动》日活超过5000万。'])
    if d['candidate_id']=='B026':d['history_check']=history(current_pattern='沙金')
    if d['candidate_id']=='Q1281':d.update(scores=score(3,3,1),reason='三款新品涉及模拟经营，但仅有Cloudflare摘要，不能出版；拆分游戏状态缺全文。')
    if d['candidate_id']=='Q0408':d.update(scores=score(0,3,0),reason='周榜式摘要没有三项事件的完整事实，无法把聚合标题当一个独立事件；原文不可用。')

reverse=[]
for rec in rows:
    if rec['section']!='industry_news':continue
    matches=[p.strip() for p in rec['text'].split('\n') if ai_re.search(p)]
    reverse.append({'source_id':rec['source_id'],'ai_signal':bool(matches),'candidate_ids':[d['candidate_id'] for d in decisions if rec['source_id'] in d['source_ids']],'matched_paragraphs':matches,'review_result':'直接采用案例进入AI；已阅但未选信号作为泛观点、旧状态、非游戏或较弱案例排除。' if matches else '未发现AI采用信号。'})
wr(P/'ai_reverse_scan.json',reverse)

wr(P/'priority_rescan_unresolved.json',rescan)
sys.path.insert(0,str(W/'scripts'))
from sync_release_decisions import build_release_decision
for i,n in enumerate(audit['nodes']):
    d=build_release_decision(n,i<7);d['title']=n['product'];d['appearance_count']=n['appearance_count'];d['signal_type']=n['signal_type'];d['facts']=n['event'];d['priority_tracks']=[]
    if n.get('audit_exclusion_reason'):d['reason']=n['audit_exclusion_reason']
    decisions.append(d)
    for sid in n['source_ids']:handled.setdefault(sid,n['candidate_id'])

def write_audits():
    dims={'国内移动/国产产品与人才':r'腾讯|网易|米哈游|国产|手游|微信|人才|制作人','市场数据':r'市场|收入|DAU|日活|销量|Newzoo|愿望单','并购':r'融资|收购|股权|基金|投资|funding|acqui|buyout','平台政策':r'Roblox|Steam|微信|苹果|Google|平台|政策|Xbox','档期变动':r'定档|上线|发售|延期|停服|测试|Beta|launch','资本组织':r'管理|离职|破产|裁员|工作室|studio|融资','海外重大':r'Riot|Roblox|Xbox|Krafton|Paradox|Atari|Newzoo|Entity|Sony|Ubisoft'}
    dc={k:sum(bool(re.search(p,d['title'],re.I)) for d in decisions if d['section']=='industry') for k,p in dims.items()}
    header=['# 2026-08-21_to_2026-08-27 筛选决策','', '卡片曝光去重：历史窗口2026-08-07至2026-08-20，共98条历史出现记录；另查本周已发布日报/周末报曝光。Gangstar曾未进入上周卡片，但8月26日已在第4/10位曝光，本期排除；Makers Fund未曝光，本期一条全文综述加一条snippet召回仍仅7分，本期无card_carryover。历史匹配及曝光来源逐条列在下方。','', '维度覆盖自检：'+'；'.join(f'{k} {v}张候选' for k,v in dc.items())+'。','', 'AI反扫：全量981条行业输入已程序遍历并按标题/正文线索复核；直接采用案例优先。产品日历漏挂反查：完整输入与行业节点反扫，规范化修订记录见release_audit_repairs.json，取多源优先级前7项。','', '周内汇总：本周日报事件可合并一次；本周日报先披露的泄露与后续正式公告仅保留一个最新状态。消息采集日期与实际事件日期分列，不将早一天发生的事件改写为本周发生。','', '质量说明：1465条输入，192条非全文；未将snippet作为出版来源。S0671按精确URL导入用户提供全文并保留补证记录。Entity美元金额不一致，仅保留融资与技术路线共同事实。','']
    c=['# 全量独立事件候选｜'+ID,'','所有记录先召回再决策；同文重复单列merge，E=0记录简写，产品按产品+事件日期合并。','']
    for d in decisions:
        sc=d.get('scores',{});h=d.get('history_check'); ids=', '.join(d['source_ids'])
        c += [f"## {d['candidate_id']} - {d['title']}",f"- section: {d['section']}",f'- source_ids: {ids}',f"- event: {d['event']}",f"- facts: {str(d.get('facts',''))[:1100].replace(chr(10),' ')}",f"- notes: {d['reason']}",'']
        if 'community' in d:c += ['- community: '+json.dumps(d['community'],ensure_ascii=False),'']
        header += [f"## {d['candidate_id']} - {d['title']}",f"- {d['decision']} → {d['section']}；{d['reason']}",f'- source_ids: {ids}']
        if sc:
            header.append('- scores: '+json.dumps(sc,ensure_ascii=False))
            if d['section']=='industry':header.append(f"- 事件{sc['event']}×相关{sc['relevance']}+钩子{sc['hook']} = {sc['total']}；E×R+M；{d['decision']}")
        if h:header.append('- history_check: '+json.dumps(h,ensure_ascii=False))
        if d.get('cluster_basis'):header.append('- cluster_basis: '+json.dumps(d['cluster_basis'],ensure_ascii=False))
        if d.get('ai_tier'):header.append('- AI: '+json.dumps({k:d.get(k) for k in ['ai_tier','game_stage','industry_reverse_scan','migration_path']},ensure_ascii=False))
        header.append('')
    (P/'event_candidates.md').write_text('\n'.join(c),encoding='utf-8')
    (P/'selection_decisions.md').write_text('\n'.join(header),encoding='utf-8')

write_audits()  # Human-readable decisions precede structured decisions and the report.
sections=['industry','ai','release_calendar','community','deep']; sm={d['candidate_id']:d for d in decisions}
items.sort(key=lambda i:(sections.index(i['section']),-sm[i['candidate_id']].get('scores',{}).get('total',0) if i['section']=='industry' else 0,-sm[i['candidate_id']].get('scores',{}).get('relevance',0) if i['section']=='industry' else 0))
wr(P/'report_items.json',dict(schema_version=1,report_type='weekly',report_id=ID,items=items))
wr(P/'selection_decisions.json',dict(schema_version=1,report_type='weekly',report_id=ID,history_window={'start':'2026-08-07','end':'2026-08-20'},decisions=decisions))
wr(P/'supplementary_calendar_decisions.json',[d for d in decisions if d['candidate_id'].startswith('T')])
covered={sid for d in decisions for sid in d['source_ids']}
assert set(S)==covered, ('unreviewed sources', sorted(set(S)-covered))
wr(P/'coverage_check.json',dict(input_records=len(S),reviewed_source_records=len(covered),unmapped_source_ids=[],industry_ai_reverse_scanned=len(reverse),independent_decisions=len(decisions),high_score_unresolved=len(rescan)))
(OUT/'deep_card_choice.txt').write_text(deep[0]['title']+'\n',encoding='utf-8')
headings=['一、行业新闻','二、AI 新闻','三、新游发布 / 产品日历','四、玩家舆论 / 社区动态','五、行业精选 / 深度观察']
lines=['# 游戏行业周报｜'+ID,'']
for section,heading in zip(sections,headings):
    lines += ['## '+heading,'']; group=[it for it in items if it['section']==section]
    for j,it in enumerate(group,1):
        if section=='release_calendar':lines += ['- '+it['body'],'']
        else:lines += [f"### {j}. {it['title']}",'',it['body'],'']
(P/'report_draft.md').write_text('\n'.join(lines),encoding='utf-8')
print('section counts',dict(Counter(it['section'] for it in items)))
print('decisions',len(decisions),'unresolved high-score',len(rescan))
for d in rescan: print(d['source_id'],d['scores'],d['title'])
