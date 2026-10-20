import json,re,shutil,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))['decisions'];DM={d['candidate_id']:d for d in D}
nodes={n['candidate_id']:n for n in json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))['nodes']}
for d in D:
    node=nodes.get(d['candidate_id'])
    if node and d['decision']=='exclude' and node.get('editorial_valid') is False:
        d['reason']='正文证据/事件资格复核排除：'+node.get('editorial_reason','无合格本期新节点。')
    if d['candidate_id'] in ['I017','I144']:
        sid=d['source_ids'][0]
        needle='国产独立' if d['candidate_id']=='I017' else 'Features: 搜打撤'
        d['pc_release_scope']=dict(classification='domestic_or_focus' if d['candidate_id']=='I017' else 'multiplayer_or_other',basis='原文明确国产团队及IP授权；当前为产品经营数据披露。' if d['candidate_id']=='I017' else '原文明确PC封闭测试、搜打撤及角色扮演，非海外单机纯发售；以实际赛道判断R3。',evidence=[dict(source_id=sid,evidence=next(line for line in S[sid]['text'].splitlines() if needle in line))])
(P/'selection_decisions.json').write_text(json.dumps({'decisions':D},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def save(name,value): (P/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def proof(sid,needle):
    assert needle in S[sid]['text'],(sid,needle)
    return next(x for x in S[sid]['text'].splitlines() if needle in x)
def claim(text,sid,needle):return dict(claim=text,source_id=sid,evidence=proof(sid,needle))
items=[]
def item(cid,section,title,parts,body=None,**kw):
    claims=[claim(*x) for x in parts]
    item=dict(candidate_id=cid,section=section,title=title,source_ids=list(dict.fromkeys(c['source_id'] for c in claims)),claims=claims,body=body or ''.join(c['claim'] for c in claims));item.update(kw);items.append(item);return item

item('I060','industry_news','Supercell完成Metacore全资收购，《Merge Mansion》并入产品组合',[
 ('Metacore于10月19日宣布，Supercell已完成收购，公司现在由其全资持有。','S0060','Supercell has completed'),
 ('《Merge Mansion》团队已加入Supercell，继续开发该产品；交易财务条款未披露。','S0060','Merge Mansion will become'),
 ('这笔交易在5月公布计划，原预计9月底完成。','S0060','It then announced plans'),
 ('据AppMagic估算，该作自2020年上线以来累计收入约4.9亿美元。','S0060','around $490m')])
# Separate evidence for the closing forecast and undisclosed terms.
items[-1]['claims'] += [claim('交易财务条款未披露。','S0060','Financial terms have not been disclosed'),claim('原预计9月底完成。','S0060','expected to close at the end of September')]
item('I144','industry_news','搜打撤角色扮演新作《HUNGER》开启PC封闭测试',[
 ('GOOD FUN CORPORATION开发、发行的《HUNGER》于10月19日在PC开启封闭内测。','S0144','Game: HUNGER'),
 ('测试资料将产品列为搜打撤、角色扮演类型。','S0144','Features: 搜打撤')])
for text,needle in [('GOOD FUN CORPORATION开发、发行','Publisher: GOOD FUN'),('10月19日在PC开启封闭内测。','Event date: 2026-10-19'),('PC开启封闭内测。','Platforms: PC'),('封闭内测。','Test name: 封闭测试')]:items[-1]['claims'].append(claim(text,'S0144',needle))
item('I025','industry_news','9月中国手游发行商占全球百强收入41.6%，中腰部借新品扩张',[
 ('Sensor Tower于10月16日发布的9月报告显示，37家中国厂商进入全球手游发行商收入百强，合计收入20亿美元，占百强收入41.6%。','S0025','37个中国厂商'),
 ('前七名座次保持不变，哔哩哔哩收入环比增长36%、排名上升7位。','S0025','哔哩哔哩收入环比增长36%'),
 ('《Clash of Critters》当月贡献莉莉丝发行商收入的42%，《疯狂水世界》出海收入占其全球收入的60%。','S0025','42%'),
 ('数据为App Store与Google Play预估，中国大陆仅含iOS。','S0025','报告仅统计发行商收入')])
for text,needle in [('10月16日','10月16日'),('前七名座次保持不变','前七名排名均保持不变'),('《疯狂水世界》出海收入占其全球收入的60%。','全球总收入的60%')]:items[-1]['claims'].append(claim(text,'S0025',needle))
item('I044','industry_news','网易参投的Liquid Swords进入破产程序，27名员工被解雇',[
 ('《Samson》开发商Liquid Swords申请破产，27名员工将全部被解雇。','S0044','All 27 employees'),
 ('据报道，员工此前两个月未获工资，欠薪将由瑞典国家工资保障机制覆盖。','S0044','not receiving pay for two months'),
 ('截至10月14日，《Samson》售出151,900份，收入2,410万瑞典克朗、约240万美元；相关知识产权及开发资产正在出售，竞标截止10月21日。','S0044','151,900 copies'),
 ('网易于2022年收购了该公司的未披露比例少数股权。','S0044','NetEase acquired an undisclosed minority stake')])
for text,needle in [('Liquid Swords申请破产','has filed for bankruptcy'),('相关知识产权及开发资产正在出售','assets for sale'),('竞标截止10月21日。','bidding window will conclude on October 21')]:items[-1]['claims'].append(claim(text,'S0044',needle))
item('I017','industry_news','《太吾异世劫》披露EA首12小时销量1.5万份，授权团队分工明确',[
 ('据GameLook报道，犁浦工作室开发的《太吾异世劫》EA版本发售12小时销量超过1.5万份，Steam好评率为73%。','S0017','销量突破1.5万份'),
 ('螺舟工作室负责IP授权与内容指导，实际开发交由犁浦，4Divinity承担发行、社区及多语言本地化。','S0017','螺舟仅负责授权与内容指导'),
 ('团队坦言当前版本仍需打磨，曾劝玩家暂缓购买、先加入愿望单；现有反馈集中于构筑深度、背包交互、性能及联机稳定性。','S0017','主动劝玩家暂缓购买')])
for text,needle in [('4Divinity承担发行、社区及多语言本地化。','发行交由 4Divinity'),('现有反馈集中于构筑深度、背包交互、性能及联机稳定性。','构筑深度、战斗手感、背包交互和性能表现')]:items[-1]['claims'].append(claim(text,'S0017',needle))
item('I040','industry_news','国内二合游戏《Hollywood Merge》最近一个月收入超过500万美元',[
 ('游戏新知援引AppMagic数据称，国内厂商VoyagerOne的二合游戏《Hollywood Merge》最近一个月收入超过500万美元，折合人民币超过3300万元。','S0040','收入额超过了500万美元'),
 ('产品于今年2月在海外上线，Google Play下载量已超过500万次，玩法除合成外还包括集卡与服装挑战。','S0040','今年2月份上线海外'),
 ('游戏允许等级超过20级的玩家绑定社交账号，并加入官网会员俱乐部获取额外奖励。','S0040','等级超过20级')])
for text,needle in [('Google Play下载量已超过500万次','下载量已经超过了500万次'),('国内厂商VoyagerOne','国内厂商')]:items[-1]['claims'].append(claim(text,'S0040',needle))
item('I072_B','industry_news','灵犀互娱《篮球少女：飞跃巅峰》列入10月23日公测日程',[
 ('GameRes本周开测清单列出，灵犀互娱发行的运动少女养成游戏《篮球少女：飞跃巅峰》将于10月23日公测。','S0072','灵犀互娱发行'),
 ('玩家以教练身份制定训练路线，游戏包含超过300种随机事件，并提供即时球场竞技与临场战术决策。','S0072','超过300种随机事件')])
items[-1]['claims'].append(claim('10月23日公测。','S0072','10月23日'))
item('I071','industry_news','《针影裁梦》复盘上线24小时回本，手工模拟以操作简化扩大受众',[
 ('GameRes本期案例复盘称，手工制衣游戏《针影裁梦》于9月21日登陆Steam，上线24小时收回开发成本，10月4日同时在线达到4.3万。','S0071','仅仅过去24小时'),
 ('产品将测量、打板、选料与缝纫转化为轻量操作，并允许通过辅助功能降低缝线控制难度。','S0071','三围测量、打板、选料'),
 ('文章以《维修物语》作比较，认为熟悉物件、手艺反馈与低学习成本共同支撑了这类小体量模拟游戏的吸引力。','S0071','《维修物语》和《针影裁梦》选择的都是轻量化')])
items[-1]['claims'].append(claim('通过辅助功能降低缝线控制难度。','S0071','辅助功能直接解决'))
item('I128','industry_news','《幻兽帕鲁》制作人称正式版带来数百万新增玩家，仍维持原价',[
 ('溝部拓郎在游戏日报采访中表示，《幻兽帕鲁》正式版上线后新增玩家达到数百万级别，但团队没有统计精准新增数值；中国与美洲长期累计玩家规模交替居前两位。','S0128','正式版上线后新增玩家数量已经达到数百万级别'),
 ('团队曾讨论涨价，最终维持原价，希望降低好友共同游玩的门槛。','S0128','决定了维持原价不变'),
 ('他同时表示，短期内不会有大规模内容更新，未来仍会迭代玩家需求，但目前没有转向3A大作的明确目标。','S0128','短期内不会有大规模的内容更新')])
items[-1]['claims'].append(claim('目前没有转向3A大作的明确目标。','S0128','没有冲击3A大作'))
item('I058_APPLE','industry_news','Carson Oliver据报将升任App Store副总裁',[
 ('据MobileGamer转述彭博社报道，Carson Oliver将升任App Store副总裁，并继续向Eddy Cue汇报。','S0058','Carson Oliver is reportedly being promoted'),
 ('在Phil Schiller退出日常管理后，他此前已负责App Store业务。','S0058','Phil Schiller stepped back')])

item('A041','ai_trends','《疯狂水世界》把AI短剧接入游戏，素材迭代同时服务获客与回流',[
 ('游戏新知的产品观察显示，益世界《疯狂水世界》已把自身IP的AI短剧、AI漫剧放入游戏，总量达到65集。','S0041','总共多达65集'),
 ('广告内容从末日求生、战力竞争转向赛季生态与联盟互助，报道将高频素材迭代归因于AI工具在素材生产中的规模化使用。','S0041','背后是AI工具大规模应用于素材生产过程的结果'),
 ('这一案例中，AI既承担投放素材生产，也成为玩家等待生产资源时可消费的内容。','S0041','如果想在游戏里消磨等待时间')])
for text,needle in [('益世界《疯狂水世界》','益世界的《疯狂水世界》'),('转向赛季生态与联盟互助','9月到现在')]:items[-1]['claims'].append(claim(text,'S0041',needle))
item('A027','ai_trends','AI NPC长期记忆案例显示，成本取决于筛选、检索与信息传播规则',[
 ('游戏陀螺以《星布谷地》等案例分析NPC跨会话记忆：角色使用统一Agent架构与记忆系统，部分事件可在角色间社交传播。','S0027','搭载“超智记忆系统”'),
 ('文章按10万月活、每人每月100轮对话估算，模型推理和记忆处理约需每月6908美元；这是假设用量下的模型调用估算，不含数据库、运维、审核、网络、人工和实时语音。','S0027','每个月产生1000万轮对话'),
 ('近期原文、长期摘要和按需检索可以降低上下文用量，但设计仍需限制哪些角色有权知道某件事。','S0027','近期几轮对话保留原文')])
for text,needle in [('10万月活、每人每月100轮对话','10万月活跃玩家'),('不含数据库、运维、审核、网络、人工和实时语音。','没有包含数据库托管'),('限制哪些角色有权知道某件事。','谁知道这件事')]:items[-1]['claims'].append(claim(text,'S0027',needle))
item('A022','ai_trends','校招调查显示AI岗位类别增加，游戏理解与结果判断仍是面试重点',[
 ('竞核的校招调查援引统计称，截至9月4日，40家游戏公司开放1572类应届全职岗位，其中名称带AI的有116类，春招时为45类。','S0022','40家游戏公司已开启秋招'),
 ('受访候选人称，AI策划面试仍重点追问游戏机制、设计目的与项目经验；会借助工具产出原型，并不直接等于能解释设计。','S0022','真正卡住他的不是AI技术'),
 ('采访还记录了实习生依赖带教、项目文档和既有交付标准来判断AI结果的情况，说明工具能力与验收经验仍需分别培养。','S0022','判断就是要经验')])
item('A043','ai_trends','UKIE与Sheridans推出游戏工作室AI合规及认证服务',[
 ('UKIE与律师事务所Sheridans合作推出AI合规及认证服务，通过四步流程取得UKIE认证标志，可用于向发行商与投资者展示尽职审查。','S0043','four-step process'),
 ('服务检查工作室使用的工具、授权许可、AI生成内容是否到达玩家，以及既有管理流程。','S0043','whether AI-generated material reaches players'),
 ('对UKIE会员，新政策与合规检查通常收费1500至2000英镑，既有政策复核为500至750英镑。','S0043','£1,500 and £2,000')])
items[-1]['claims'].append(claim('既有政策复核为500至750英镑。','S0043','between £500 and £750'))
item('A131','ai_trends','MiniMax发布M3.1 Flash，公布智能体任务降本与推理速度变化',[
 ('MiniMax发布M3.1 Flash，称在线推理速度提升近三倍，智能体任务整体使用成本较上一代降低70%。','S0131','在线推理速度提升近三倍'),
 ('每百万Token输入、输出与缓存输入价格分别为0.15、0.60和0.015美元，模型现已通过API等服务提供，权重将稍后发布。','S0131','每 1M token 统一价格'),
 ('对游戏研发而言，这类成本变化可能降低脚本原型、自动化测试及工具链智能体的试错费用；实际收益仍取决于任务通过率和人工验收。','S0131','支持复杂软件开发工作流')])
items[-1]['claims'].append(claim('权重将稍后发布。','S0131','模型权重将于稍后发布'))

release_d=next(d for d in D if d['section']=='release_calendar' and d['decision']=='include')
item(release_d['candidate_id'],'release_calendar','少女前线2：追放',[
 ('上海散爆网络科技有限公司研发、发行的策略战棋多平台产品《少女前线2：追放》于10月19日上线“危区探遗”新版本，并开放全新搜打撤玩法；版本覆盖PC、Android与iOS。','S0146','Test name: 危区探遗'),
 ('','S0148','全新搜打撤玩法开启')],release=dict(product='少女前线2：追放',event='重大玩法更新',date='2026-10-19',platform='PC / Android / iOS',company='上海散爆网络科技有限公司'))
# The second independent source supports the same single bullet, rather than adding a sentence.
items[-1]['claims'][-1]['claim']='开放全新搜打撤玩法'
items[-1]['body']=items[-1]['claims'][0]['claim']
for text,needle in [('上海散爆网络科技有限公司研发、发行','Publisher: 上海散爆'),('策略战棋','Features: 策略 / 战棋'),('10月19日','Event date: 2026-10-19'),('版本覆盖PC、Android与iOS。','Platforms: PC / Android / iOS')]:items[-1]['claims'].append(claim(text,'S0146',needle))

item('C091','community_discourse','《战地风云6》皮肤拼写错误与五枪套设计遭质疑，团队承诺修复并解释创意',[
 ('《战地风云6》10月13日上线的外观出现臂章拼写错误，另一款Midnight Mirage皮肤配有五个手枪套。玩家不满的核心在于付费外观的质量把关与设计合理性，部分玩家进一步质疑是否使用了生成式AI。','S0091','这两款外观于10月13日正式上线'),
 ('在本期报道收录的Discord回应中，Battlefield Studios承认部分物品未达到玩家及团队自身标准，表示正检查内部流程，并计划在11月修复McNeil皮肤的拼写问题。','S0091','我们正在检查内部流程'),
 ('对于五个手枪套，团队称这是致敬动作电影夸张套路的刻意设计，并表示今后会继续关注社区反馈。','S0091','这是刻意采用的创意构思')],community=DM['C091']['community'])
for text,needle in [('11月修复McNeil皮肤的拼写问题。','于11月上线时修复'),('部分玩家进一步质疑是否使用了生成式AI。','新一轮生成式AI指控'),('今后会继续关注社区反馈。','今后会继续关注社区反馈')]:items[-1]['claims'].append(claim(text,'S0091',needle))
item('C173','community_discourse','《恋与深空》联动《银翼杀手2049》，玩家争论虚拟伴侣叙事是否破坏情感沉浸',[
 ('《恋与深空》与《银翼杀手2049》的联动宣传，使部分玩家把恋爱游戏中的情感承诺，与电影中虚拟伴侣被商品化的叙事联系起来。','S0173','给底层百姓贩卖虚拟对象'),
 ('10月19日出现的讨论里，部分玩家认为这种主题组合会削弱付费恋爱的沉浸感，也有参与者认为电影本就适合讨论虚拟角色的情感问题，分歧在于运营能否处理好题材。','S0173','2049确实挺适合虚拟角色情感这个话题'),
 ('讨论持续到当晚，另有玩家称联动目前主要是小型剧情活动，争议进一步转向是否只是借用IP视觉与热度。','S0173','好像就有个mini活动剧情')],community=DM['C173']['community'])
for text,needle in [('削弱付费恋爱的沉浸感','破坏玩家的美梦和沉浸感'),('10月19日','2026-10-19 01:54'),('讨论持续到当晚','2026-10-19 21:28')]:items[-1]['claims'].append(claim(text,'S0173',needle))

npc_body='''观察：游戏陀螺对《星布谷地》等AI NPC案例的分析说明，长期陪伴感不取决于保存多少聊天记录，而取决于角色能否在恰当情境中提取有效记忆，并让反馈改变后续关系。文章以10万月活、每人每月100轮对话测算出约6908美元的月度模型调用费用，但明确不包含数据库、运维、审核、人工及实时语音；这是一组假设账单，而非相关游戏的实际运营成本。

分析：保存全部历史、每轮重新输入模型，虽然容易实现，却会随着对话积累增加输入成本，也不能保证模型找到关键事实。更可行的组织方式是保留近期原文，将长期交互整理为事件、偏好和关系变化，再按当前情境检索。由此，成本优化与角色塑造指向同一个问题：哪些经历值得记住、何时该忘记、什么时候表达才自然。记忆管理如果只追求召回率，反复提起玩家已不在意的小事，也可能破坏陪伴感。

多角色世界还需要控制信息边界：玩家只告诉一个NPC的秘密，不能无缘无故成为另一个角色的知识。《星布谷地》案例中的事件社交传播，意味着记忆还要记录知情者和传播途径。端侧推理可以减少逐次云调用费用，但《inZOI》的本地小模型案例也提示，部署、适配和性能占用不会消失。商业可行性最终取决于有限算力能否持续带来玩家可感知的关系变化，而不是把更大的数据库当作更深的情感。'''
item('D027','deep_analysis','AI NPC记忆的商业价值，在于把有限调用转化为持续关系',[
 ('《星布谷地》','S0027','《星布谷地》'),('10万月活、每人每月100轮对话','S0027','10万月活跃玩家'),('约6908美元','S0027','6908 美元'),('不包含数据库、运维、审核、人工及实时语音','S0027','没有包含数据库托管'),('保留近期原文，将长期交互整理为事件、偏好和关系变化','S0027','近期几轮对话保留原文'),('记录知情者和传播途径','S0027','谁知道这件事'),('《inZOI》的本地小模型案例','S0027','NVIDIA ACE与KRAFTON')],body=npc_body,card_copy=dict(source_label='游戏陀螺分析文章',summary='AI NPC的长期陪伴感来自有效记忆及恰当反馈，调用费只是成本的一部分，信息边界与工程适配共同决定商业可行性。',insights=[dict(title='记忆需要选择与遗忘',detail='近期原文、长期摘要和按需检索共同减少无效输入，反馈是否自然比保存总量更关键。'),dict(title='多人世界需要知情边界',detail='记录谁知道、如何获知和能否传播，避免一个角色泄露另一个角色才掌握的秘密。'),dict(title='模型账单不是总成本',detail='示例估算排除了运维、审核、人工与实时语音，端侧推理也仍承担部署和性能代价。')]))
campus_body='''观察：竞核本期校招调查呈现出两种同时发生的变化：AI降低了新人制作原型和批量内容的难度，企业却更加重视解释设计、判断结果与进入项目后立即工作的能力。调查援引截至9月4日的数据，40家游戏公司开放1572类应届全职岗位，名称带AI的类别从春招45类增加到116类；岗位名变化并不意味着游戏理解可以被工具熟练度替代。

分析：过去，新人常通过执行性工作积累项目经验，再逐步形成设计与质量判断。AI让一部分内容更容易产出，面试却开始提前要求候选人解释目标、机制和取舍。文章中的候选人能够借工具制作作品，但在被追问设计思路时受阻；另一方面，AI策划实习生仍需要带教、项目文档与历史交付标准来判断“什么是好结果”。生产能力的提升没有自动补齐评价能力，反而使这段差距更容易暴露。

培养通道也存在差异。校企课程、比赛与长期项目实习可以提供连续反馈，帮助学生把参考图和概念变成适合玩法、能够落地的资产；而只要求新人依赖AI自学、却不给评价标准，会把本应在团队内完成的培养成本转给个人。这些访谈不能代表所有公司的招聘实践，但揭示了同一约束：当项目更强调即时交付，能够承担判断与带教的时间可能更稀缺。AI岗位增长最终能否形成稳定人才供给，取决于团队是否保留让新人获得真实反馈的路径。'''
item('D022','deep_analysis','AI让新人更快做出作品，校招却更早要求设计判断',[
 ('40家游戏公司开放1572类应届全职岗位','S0022','40家游戏公司已开启秋招'),('从春招45类增加到116类','S0022','春招时这个数字还只有45类'),('被追问设计思路时受阻','S0022','被问到设计思路和目的时，表达不清'),('带教、项目文档与历史交付标准','S0022','翻项目文档，参考之前交付的标准'),('校企课程、比赛与长期项目实习','S0022','课程共建、比赛选人'),('参考图和概念变成适合玩法、能够落地的资产','S0022','原画要转三维落地')],body=campus_body,card_copy=dict(source_label='竞核校招调查',summary='AI降低了新人制作作品的难度，却没有同步生成设计判断；企业把验收能力前置到招聘阶段，带教与持续反馈因此更加关键。',insights=[dict(title='作品产出不等于设计理解',detail='候选人能用工具完成原型，仍需要解释目标、机制和取舍，AI熟练度不能替代游戏理解。'),dict(title='验收标准仍来自项目经验',detail='带教、文档和历史交付为新人提供判断AI结果的依据，工具不会自动补齐这些经验。'),dict(title='培养路径决定门槛的性质',detail='课程与持续反馈可以加速成长；缺少带教时，即时交付要求可能把培养成本转给个人。')]))

# Candidate cards and decisions are written before the structured publication map.
head='# 选材决策｜日报2026-10-19\n\n卡片曝光去重：历史窗口2026-10-05_to_2026-10-18，共104条；任一历史已曝光的同事件一律去重。I025为唯一card_carryover，历史未曝光、rank=null、limit=10、source=publish_log_manifest；Jagex7分低于I025的8分，其他未曝光旧事件不再入选。无material_update。\n\n维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已逐条成卡；全量174条输入有映射，不设行业条数上限。\n\n产品日历漏挂反查：已反扫全量industry_news/release_calendar正文，按产品+日期聚类并逐个落include/exclude。原始抽取raw保留；历史上线、普通宣传、非完整来源与旧体验版跨期重复均已排除；与行业新闻独立选材。\n\n行业新闻 E×R+M：事件E×相关R+钩子M = 终分；日报阈值≥7，E0一票否决，按总分降序。\n\n'
cards=['# 独立事件候选｜2026-10-19\n\n完整index与JSONL已扫描；行业多源仅按同主体、同事件日、同事件聚类。产品日历按产品+日期独立聚类。\n']
dimensions={'国内移动':r'国内|国产|手游|移动|中国','国产产品与人才':r'腾讯|网易|米哈游|鹰角|莉莉丝|灵犀|犁浦|凉屋|库洛','市场数据':r'销量|收入|下载|付费|数据|榜|million|revenue|sales','并购':r'收购|投资|入股|融资|acqui|funding|raised','平台政策':r'App Store|Steam|条例|法案|政策|渠道|Google','档期变动':r'发售|测试|上线|公测|取消|停运|launch|release|cancel','资本组织':r'破产|裁员|任命|升任|工作室|CEO|bankrupt|staff','海外重大':r'Supercell|Liquid|Apple|Xbox|Ubisoft|Skydance|Jagex'}
head+='维度候选计数（可交叉计数）：'+ ' / '.join(f"{name}{sum(bool(re.search(pattern,d['event']+' '+str(d.get('entities',[])),re.I)) for d in D if d['section']=='industry_news')}张" for name,pattern in dimensions.items())+'。\n\n'
md=[head,'| candidate | decision | target_section | scores | reason |\n| --- | --- | --- | --- | --- |']
for d in D:
    sc=d.get('scores',{});sid=d['source_ids'][0]
    facts='；'.join(c['claim'] for it in items if it['candidate_id']==d['candidate_id'] for c in it['claims']) or d['reason']
    cards.append(f"\n## {d['candidate_id']} - {d['event']}\n- section: {d['section']}\n- source_ids: {', '.join(d['source_ids'])}\n- entities: {', '.join(d['entities'])}\n- event_date: {d.get('event_date','2026-10-19')}\n- facts: {facts}\n- notes: {d['reason']}\n")
    if d.get('history_check'):cards.append('- history_check: '+json.dumps(d['history_check'],ensure_ascii=False)+'\n')
    if d.get('community'):cards.append('- community: '+json.dumps(d['community'],ensure_ascii=False)+'\n')
    if d.get('pc_release_scope'):cards.append('- pc_release_scope: '+json.dumps(d['pc_release_scope'],ensure_ascii=False)+'\n')
    score_text=f"事件{sc['event']}×相关{sc['relevance']}+钩子{sc['hook']} = {sc['total']}" if d['section']=='industry_news' else json.dumps(sc,ensure_ascii=False)
    md.append('| '+' | '.join([d['candidate_id'],d['decision']+(' into '+d['merge_into'] if d.get('merge_into') else ''),d['section'],score_text,d['reason'].replace('|','/').replace('\n',' ')])+' |')
(P/'event_candidates.md').write_text('\n'.join(cards),encoding='utf-8');(P/'selection_decisions.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
save('report_items.json',{'report_type':'daily','date':'2026-10-19','items':items})

report=['# 游戏行业日报｜2026-10-19','']
sections=[('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]
for sec,heading in sections:
    report+=['## '+heading,'']
    group=[x for x in items if x['section']==sec]
    for k,it in enumerate(group,1):
        if sec=='release_calendar':report+=['- '+it['body'],'']
        else:report+=['### '+str(k)+'. '+it['title'],'',it['body'],'']
text='\n'.join(report)
assert not re.search(r'沐瞳|Moonton|MLBB|决胜巅峰|Mobile Legends|card_carryover|补位|对我司|值得借鉴|启示',text,re.I)
for it in items:
    for c in it['claims']:assert c['claim'] in it['body'],(it['candidate_id'],c['claim'])
stage=P/'staging';(stage/'_intermediate').mkdir(parents=True,exist_ok=True)
for name in ['report_inputs.jsonl','report_inputs_summary.md','report_inputs_index.md','industry_history_14d.json','industry_history_14d.md','release_calendar_audit.json','source_quality_audit.json','event_candidates.md','selection_decisions.md','report_items.json','selection_decisions.json']:
    shutil.copy2(P/name,stage/'_intermediate'/name)
(stage/'game_industry_daily_2026-10-19.md').write_text(text,encoding='utf-8')
save('collector_coverage_audit.json',json.loads((P.parents[3]/'news_data/_collector_runs/2026-10-19/run_summary.json').read_text(encoding='utf-8')))
save('run_summary.json',{'report_type':'daily','id':'2026-10-19','sections':{s:sum(x['section']==s for x in items) for s,_ in sections},'history_window':'2026-10-05_to_2026-10-18','repeat_only_excluded':[d['candidate_id'] for d in D if d.get('history_check',{}).get('novelty')=='repeat_only' and d['decision']=='exclude'],'material_updates':[],'card_carryover':['I025'],'sources_used':sorted({s for x in items for s in x['source_ids']}),'industry_scores':[{k:d[k] for k in ['candidate_id','event','scores']} for d in D if d['section']=='industry_news' and d['decision']=='include'],'boundary_5_6':[{k:d[k] for k in ['candidate_id','event','scores','reason']} for d in D if d['section']=='industry_news' and 5<=d['scores']['total']<=6],'deep_handoff':'星期二日报，无周五回执/selection交接；newsletter付费正文不足，已审计排除。','warnings':['22条非完整输入，正文未引用','AI5条超出1–3软目标：4条直接应用/生产流程、1条明确成本迁移','DataEye/nadianshi/Cubox/wanjiang采集失败，PocketGamer/VGC降级','Faraway虽两来源，Gamespot标snippet不可用于发布，保留排除；无当日Steam榜单输入']})
print('items',len(items),'sources',len({s for x in items for s in x['source_ids']}),'staged',stage)
