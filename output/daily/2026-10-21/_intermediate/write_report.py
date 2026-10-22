import json,re,shutil
from pathlib import Path
P=Path(__file__).resolve().parent
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
raw=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));D=raw['decisions'];DM={x['candidate_id']:x for x in D}
def sid(i):return f'S{i:04}' if isinstance(i,int) else i
def evidence(i,needle):
    t=S[sid(i)]['text'];assert needle in t,(i,needle)
    return next(l for l in t.splitlines() if needle in l)
def cl(text,i,needle):return dict(claim=text,source_id=sid(i),evidence=evidence(i,needle))
items=[]
def item(cid,title,triples,body=None,**kwargs):
    d=DM[cid];assert d['decision']=='include',cid
    x=dict(section=d['section'],title=title,candidate_id=cid,source_ids=list(d['source_ids']),claims=[cl(*t) for t in triples],body=body if body is not None else ''.join(t[0] for t in triples));x.update(kwargs);items.append(x);return x

item('I036','腾讯光子正式公布《人间异想计划》，公开22分钟实机并启动长期招募',[
 ('腾讯正式公布光子工作室群宇宙小狗工作室的《人间异想计划》，发布22分钟实机演示并开启长期招募。',36,'腾讯正式公布了旗下光子'),
 ('产品定位为轻怪谈都市异想开放世界RPG，演示展示都市探索、无缝场景切换与多角色轮切战斗。',36,'轻怪谈都市异想开放世界RPG'),
 ('项目此前以Higame等招聘线索出现，本次将正式名称和可观看的实机内容集中公开。',36,'Higame')])
items[-1]['claims'] += [cl('无缝场景切换',36,'场景都会瞬间无缝进行切换'),cl('多角色轮切战斗',36,'三人轮切')]
item('I213','完美世界认购的两支基金完成募资，总规模约112亿元',[
 ('完美世界10月21日公布，先前参与认购的两支投资基金均已完成募资。',213,'今日 （10月21日）'),
 ('天津砺思星深股权投资合伙企业总规模75.2亿元，完美世界认缴5000万元、占0.66%；拾象尚势（天津）创业投资合伙企业总规模36.5亿元，完美世界认缴1亿元、占2.74%。',213,'天津砺思星深股权投资合伙企业'),
 ('这约112亿元为两支基金的合计规模，并非完美世界自身投入；报道将相关基金方向概括为新兴科技，砺思星深主要投向中国大陆AI领域早中期非上市企业。',213,'AI相关领域')])
items[-1]['claims'] += [cl('拾象尚势（天津）创业投资合伙企业总规模36.5亿元，完美世界认缴1亿元、占2.74%',213,'拾象尚势（天津）创业投资合伙企业'),cl('报道将相关基金方向概括为新兴科技',213,'新兴科技领域')]

# Direct game applications precede all transfer-value candidates.
item('A215','Vivrato调查：AI采用广泛，但过半工作室自评流程整合深度不超过3分',[
 ('Vivrato基于2026年4月至9月对欧洲和北美101名工作室负责人的访谈称，97%受访者在研发中使用过某种AI，94%在九个生产环节中的至少一个使用过AI。',215,'101 interviews'),
 ('调查将生成式AI、规则自动化、定制模型、传统机器学习、检索增强与智能体等分别纳入口径；代码与工程采用率为86%。',215,'six types of AI'),
 ('超过半数受访者对AI融入完整生产管线的深度自评不超过3分（满分10分），采用过工具与完成流程整合仍是两个不同指标。',215,'three or lower out of ten')])
items[-1]['claims'] += [cl('97%受访者在研发中使用过某种AI，94%在九个生产环节中的至少一个使用过AI',215,'97% of studio leaders'),cl('代码与工程采用率为86%',215,'86%')]
item('A039','慧博云通游戏测试访谈：AI加速执行，人工Review与证据回溯需求上升',[
 ('慧博云通游戏业务副总裁岳铠泽在游戏葡萄访谈中表示，AI让代码与内容执行更快，也增加人工Review工作量；团队需要判断数值组合、触控手感及表现是否符合设计意图。',39,'AI加速了执行'),
 ('他举例说，单项数值在合理区间并不保证组合后的发育速度正常，自动跑通关卡也不代表真人操作没有延迟。',39,'数值是离散的，体验是连续的'),
 ('对于要求真人执行的客户，团队会为每条测试提供录屏和截图，把Bug追溯到具体用例与场景。',39,'每完成一条测试')])
items[-1]['claims'] += [cl('慧博云通游戏业务副总裁岳铠泽',39,'就任游戏业务副总裁'),cl('人工Review工作量',39,'Review工作量也增加了10倍')]
item('A304','恺英旗下SoonPlay公测，将视频输入、即时试玩与编辑放入同一平台',[
 ('恺英网络旗下极逸人工智能的SoonPlay于10月20日正式公测，本期介绍称，用户可上传视频生成轻游戏，并在游玩过程中选中元素编辑，或通过对话迭代内容。',304,'2026年10月20日'),
 ('平台不设公开排行榜和公开评论区，作品流量数据仅创作者可见；玩家通过“好玩／无趣”与入库行为提供反馈。',304,'不设公开排行榜'),
 ('文章将SoonPlay定位为面向大众的创作与分发社区，另以SOON承接专业开发需求，覆盖美术资产、代码与数值设计等工作流。',304,'SOON是一站式AI游戏创作平台')])
items[-1]['claims'] += [cl('在游玩过程中选中元素编辑',304,'游玩过程中直接选中要调整的元素'),cl('“好玩／无趣”与入库行为',304,'“好玩/无趣”的评价和入库行为')]
item('A288','ReVamp缩小公开测试后，开发团队披露触达损失与人工准入机制',[
 ('Digital Sun在本期采访中说明，《ReVamp》原Steam公开测试有数万人报名，改为Discord手动授权后，预计最多只能覆盖数百人。',288,'tens of thousands'),
 ('团队称，Discord使其可以要求签署保密协议、查看服务器活动并实时答疑；Steam现有测试控制主要是按国家开放，难以逐个筛选账号。',288,'sign an NDA'),
 ('受访者表示，公开试玩仍会进行，但会靠近发售；提前减少公开构建，意味着同时失去大规模反馈和创作者传播机会。',288,'much closer to launch')])
items[-1]['claims'] += [cl('Digital Sun',288,'Digital Sun Games'),cl('《ReVamp》',288,'ReVamp'),cl('最多只能覆盖数百人',288,'a few hundred people at best')]

rd=next(d for d in D if d['section']=='release_calendar' and d['decision']=='include')
item(rd['candidate_id'],'人间异想计划',[
 ('腾讯光子工作室群宇宙小狗工作室的轻怪谈都市开放世界RPG多平台产品《人间异想计划》于10月21日首次正式发布22分钟实机PV，并开启长期招募；以人类与怪谈体共生的都市为舞台。',36,'腾讯正式公布了旗下光子')],
 release=dict(product='人间异想计划',event='首次正式公开及实机演示',date='2026-10-21',platform='来源未在非虚构表述中明确全部平台',company='腾讯光子'))
items[-1]['claims'] += [cl('10月21日',330,'Event date: 2026-10-21'),cl('轻怪谈都市开放世界RPG',36,'轻怪谈都市异想开放世界RPG'),cl('人类与怪谈体共生',36,'人与怪谈体共生')]
items[-1]['claims'].append(cl('多平台产品',40,'重视PC、主机端品质'))
rd=next(d for d in D if d['section']=='release_calendar' and d['decision']=='include' and d['entities']==['掘地求财：铲友齐上阵'])
item(rd['candidate_id'],'掘地求财：铲友齐上阵',[
 ('Mipumi Games开发、rokaplay select与松竹游戏共同发行的合作挖掘模拟冒险多平台产品《掘地求财：铲友齐上阵》定档12月4日（CEST）在PC、PS5、Xbox Series X|S与Switch 2发售，并加入Xbox Game Pass；支持最多4人跨平台联机。',46,'由Mipumi Games开发')],release=dict(product='掘地求财：铲友齐上阵',event='新品定档',date='2026-12-04',platform='PC / PS5 / Xbox Series X|S / Switch 2',company='Mipumi Games / rokaplay select / 松竹游戏'))
items[-1]['claims'] += [cl('合作挖掘模拟冒险',46,'【游戏类型】 模拟 游戏'),cl('12月4日（CEST）',46,'2026年12月4日（CEST）'),cl('最多4人跨平台联机',46,'最多4人，支持跨平台联机')]
rd=next(d for d in D if d['section']=='release_calendar' and d['decision']=='include' and d['entities']==['无光绝境'])
item(rd['candidate_id'],'无光绝境',[
 ('Pokuch开发、META Publishing发行的开放世界生存冒险端游《无光绝境》定档12月2日推出抢先体验版本；支持最多4人合作探索火星地下，围绕资源收集、制作工具与建立据点展开生存。',49,'由 Pokuch 开发')],release=dict(product='无光绝境',event='新品抢先体验定档',date='2026-12-02',platform='Steam',company='Pokuch / META Publishing'))
items[-1]['claims'] += [cl('12月2日推出抢先体验版本',49,'2026年12月2日'),cl('支持最多4人合作探索火星地下',49,'支持最多四人共同游玩'),cl('火星地下',49,'火星地表之下'),cl('资源收集、制作工具与建立据点',49,'收集资源、制作工具、建立生存据点')]

comm1=dict(trigger='帖子转述CQ在停更后宣布周年更新及11月直播说明',claim_scope='官方计划仅由帖主转述，玩家态度局限于被采到的帖子内容',complaint_logic='期待补完旧角色与模式，但担忧衍生作导流、脚本和资源膨胀使长期运营难以恢复',timeline='2023年10月停止更新；2026年10月21日00:25建帖，当日18:29仍有回复',follow_up_scan='扫描同日13条社区与305条行业输入；未见可核验官方全文，正文只采用带主语的转述；不使用22日信息。')
item('C371','《克鲁赛德战记》周年更新计划勾起回流期待，玩家担忧情怀难以恢复运营',[
 ('《克鲁赛德战记》停更后的周年更新计划让老玩家重新讨论回归：10月21日帖子转述，国际服2023年10月停止更新后，团队准备在12周年补充服装、试炼要塞Boss和此前未完成的新角色，并在11月直播说明。',371,'国际服于2023年10月停止更新'),
 ('部分玩家把这视为多年停摆后仍能看到新内容的慰藉；另一些玩家担心，这只是给衍生作导流，脚本刷取和资源膨胀已削弱原作继续商业运营的基础。',371,'也许是为了给新作打广告'),
 ('讨论从21日凌晨延续到当日傍晚，争议集中在新增少量内容能否带来持续运营。',371,'2026-10-21 18:29')],community=comm1)
items[-1]['claims'] += [cl('12周年',371,'12周年'),cl('试炼要塞Boss和此前未完成的新角色',371,'“试炼要塞”更新BOSS'),cl('此前未完成的新角色',371,'停更前没做完的新角色'),cl('资源膨胀',371,'资源已经击穿了盈利体系'),cl('脚本刷取',371,'脚本神游')]
comm2=dict(trigger='21日晚帖子转述Cygames对演唱会取消后的赴美住宿和路费补偿',claim_scope='报销与条件均按玩家转述，未以标题概括为官方全额承诺',complaint_logic='部分玩家赞赏承担费用，另有人提醒只有符合条件项目，临近行程取消仍有损失与挫败',timeline='10月21日20:25发帖，20:45出现符合条件的纠正，22:11仍讨论欧美活动受阻；22日回复不采用',follow_up_scan='同日行业S0222仅Cloudflare短摘要，不能作为官方补偿范围证据；社区13条与行业305条反扫未得官方全文。正文保留转述及范围争论，不写免责尾注。')
item('C373','CY演唱会取消后拟补偿赴美开支，玩家争论“符合条件”的报销范围',[
 ('CY演唱会取消后的赴美开支补偿成为10月21日晚玩家讨论的焦点。帖子称住宿和路费将获报销，但随后有玩家指出表述是“符合条件”的部分，不能理解为全部行程费用都由公司承担。',373,'cy宣布因演唱会取消'),
 ('有玩家认为补偿需要不小成本，也有人对临近行程才取消的体验不满；分歧集中在补偿诚意与实际覆盖范围能否弥补出行损失。',373,'这得花不少钱'),
 ('讨论当晚继续延伸到海外活动受阻，以及取消通知给行程安排带来的挫败。',373,'进军欧美大计受阻')],community=comm2)
items[-1]['claims'] += [cl('“符合条件”的部分',373,'报销“符合条件”的部分'),cl('临近行程才取消',373,'两天前宣布签证官单防')]

deep1='''观察：GameDiscoverCo在10月21日的分析中，把容易借名称搜索的单点玩法，与已有受众、机制复杂的作品分开讨论。它举出“草堆找针”作品在没有公开可玩版本时也出现模仿的案例，提出公开Demo带来的风险不都来自代码反编译；把所有项目一律延后展示，可能付出不同的获客代价。

分析：简单、易描述、可被搜索关键词直接找到的玩法，最脆弱的环节可能是创意与需求一起暴露。GameDiscoverCo认为，这类模仿未必需要取得原始构建，名称与短视频就可能提供实现方向。因此，撤掉Demo并不能自动保护创意，真正发生变化的是模仿所需时间相对原作上市周期缩短。这个判断来自作者的案例分析，不代表所有相似作品都已被证实复制代码。

另一方面，复杂系统、风格与已有用户认同会增加仿制品转化受众的难度。Digital Sun在采访中说，ReVamp原本数万人报名的Steam测试，转到Discord后只能手动覆盖数百人，并失去提前收集大规模反馈和创作者传播的机会。两条材料共同显示：发布构建的风险与长期隐藏的成本同时存在；前者取决于产品可复制性，后者取决于测试反馈和发现渠道的重要性，二者不能用同一个“是否开放Demo”答案替代。'''
item('D_DISCOVERY','AI仿制风险取决于玩法复杂度与搜索名称，撤回Demo的收益因产品而异',[
 ('在没有公开可玩版本时也出现模仿',375,'There was no public playable'),
 ('名称与短视频就可能提供实现方向',375,'It’s the idea'),
 ('已有受众、机制复杂的作品',375,'non-trivially complex'),
 ('数万人报名的Steam测试',288,'tens of thousands'),
 ('手动覆盖数百人',288,'a few hundred people at best')],body=deep1,
 card_copy=dict(source_label='GameDiscoverCo分析与PC Gamer访谈',summary='低复杂度玩法可能仅靠名称与短视频就被模仿；复杂作品撤回Demo则会同时损失反馈与传播，风险取决于产品条件。',insights=[dict(title='创意暴露不依赖构建',detail='作者举出没有公开试玩也出现模仿的单点玩法，撤掉Demo无法消除全部风险。'),dict(title='名称会集中搜索流量',detail='容易描述、容易搜索的机制，使模仿品更容易与原作争夺同一发现入口。'),dict(title='复杂作品承担另一种成本',detail='ReVamp把数万人规模的测试缩为数百人，获得准入控制，也失去广泛反馈与创作者传播。')]))
deep2='''观察：Vivrato对101名欧洲和北美工作室负责人的访谈显示，97%使用过某种AI，但超过半数对完整管线整合深度的自评不超过3分。慧博云通游戏测试访谈则描述了另一端的压力：执行更快以后，人工Review、体验判断和可回溯证据仍需要投入。两条材料把“用过工具”与“让项目可靠交付”之间的距离具体化了。

分析：工具采用率反映接触面，流程深度才更接近环节之间能否衔接。调查把规则自动化、机器学习与生成式AI等区分开来，本身就限制了把97%直接理解为生成式内容已全面替代人工的解释。若产出增加而审核能力没有同步增长，问题可能在更大的工程量形成后才暴露；岳铠泽对此的描述是，AI加快执行也放大Review负担，后期返工依然消耗人力。

这种压力在游戏中还涉及体验标准，而不仅是程序是否跑通。访谈用单项数值正常但组合后发育异常、关卡能通关却存在触控延迟说明，离散检查与连续体验并不等价。为每条真人测试保留录屏、截图与用例关联，则把“有人判断过”变成可追溯的交付证据。由此可见，流程整合需要同时解决产出衔接、体验判断和责任回溯；单一工具的生成速度不足以证明这三项已经完成。'''
item('D_QA','AI覆盖研发环节后，质量判断与流程整合成为瓶颈',[
 ('101名欧洲和北美工作室负责人',215,'101 interviews'),
 ('97%使用过某种AI',215,'97% of studio leaders'),
 ('完整管线整合深度的自评不超过3分',215,'three or lower out of ten'),
 ('AI加快执行也放大Review负担',39,'Review工作量也增加了10倍'),
 ('单项数值正常但组合后发育异常',39,'数值是离散的，体验是连续的'),
 ('为每条真人测试保留录屏、截图与用例关联',39,'每完成一条测试')],body=deep2,
 card_copy=dict(source_label='Vivrato调查与游戏葡萄访谈',summary='广泛采用AI并不意味着研发流程已深度整合；执行变快后，体验判断、人工Review和证据回溯仍决定交付质量。',insights=[dict(title='采用率不等于整合深度',detail='97%用过AI与过半管线自评不超过3分同时存在，两者衡量不同问题。'),dict(title='执行加速会增加审核负担',detail='测试受访者指出，产出更快可能使底层问题在更大工程量形成后才暴露，返工仍消耗人工。'),dict(title='体验标准需要可追溯证据',detail='数值逐项通过和关卡自动跑通不能替代真人体验；录屏、截图与用例关联让判断可以回溯。')]))

# Keep audit markdown comprehensive, including exclusions and exact score axes.
head=['# 2026-10-21 日报选材决策','', '卡片曝光去重：历史窗口2026-10-07至2026-10-20，114条记录；逐项读取card_exposed/card_rank/card_limit/card_exposure_source。Metacore等已曝光同事件排除；本期无card_carryover，故此前卡片排名不适用。', '', '维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均覆盖全量输入；每个source_id至少一项决策，具体数量见run_summary。', '', '评分版本：subject_genre_v2。行业E×主体R+品类M≥5；日期、来源与曝光去重独立执行。入选I036与I213均E3×R3+M0=9。', '', '产品日历漏挂反查：全文反扫305条industry_news与37条release_calendar，逐句按产品/日期/状态召回；错误新品上线与历史/未来节点修正保留原始审计。57个节点均通过sync生成决策，只有人间异想计划具备完整多源且可发布；与行业同事件不作排除理由。', '', '## 边界与风险复核','', '- I053腾讯生活模拟公开稿10分：本期日期元数据与同批大量2025镜像混杂，原文未提供绝对首曝日；保留候选排除，不能凭推测给中文正式名称。', '- I213：基金募集完成是本期新增资本状态；112亿元是两支基金规模，完美世界认缴额分别5000万元和1亿元。', '- I045：9月主机作品本期登陆Steam，不误写新品首次发售。', '- I286 Dont Nod E3R1M0=3；I246 EA Fight Night E3R1M1=4；I289 PEGI E2R1M1=3；N_ECC E1R3M1=4；N_RIOT E1R3M0=3。', '- C283反作弊变更与差评实际为20日，21日采集不等于21日新事件；本期排除。', '- D_DISCOVERY新增newsletter复杂度、关键词与无公开构建仿制证据，不重复昨日单纯Demo曝光成本观点。', '- 日历与行业不互斥；只要独立通过多源、日期、前缀规则即可分别收录。', '', '| candidate | decision | target_section | reason |','| --- | --- | --- | --- |']
audit=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
for i,line in enumerate(head):
    if line.startswith('产品日历漏挂反查：'):
        head[i]=f'产品日历漏挂反查：全文反扫305条industry_news与37条release_calendar，逐句按产品/日期/状态召回；错误新品上线与历史/未来节点修正保留原始审计。{len(audit["nodes"])}个节点均通过sync生成决策。可发布多源前缀为人间异想计划11分、掘地求财：铲友齐上阵6分、无光绝境6分；后两项为未来定档，不按实际发售/测试日期门禁排除。与行业同事件不作排除理由。'
head += ['', '## 日历跨期重复检查', '', '读取此前日报/周末报/周报release_calendar条目，未发现本期三个规范化产品+日期+事件已发表。RV There Yet?两条Gematsu RSS属于同一公告，只算一源；炉石两源仍为普通卡包更新；10月14日无光绝境Playtest与12月2日EA定档分别留痕。']
candidates=['# 2026-10-21 全量事件候选','', '以375条完整输入为真源，所有分区反扫；不按预期分数删掉召回信号。','']
for d in D:
    sc=d.get('scores');score=('；'+json.dumps(sc,ensure_ascii=False)) if sc else ''
    head.append('| '+d['candidate_id']+' | '+(d['decision']+' into '+d['merge_into'] if d['decision']=='merge' else d['decision'])+' | '+d['section']+' | '+d['reason'].replace('|','／')+score+' |')
    quotes=[]
    for v in d['source_ids']:
        lines=[l for l in S[v]['text'].splitlines() if l.strip()]
        # Source bodies are not truncated to an arbitrary character length.
        useful=next((l for l in lines if re.search('首曝|上线|测试|AI|2025|2026|launch|reveal|Game:|Norway|募资',l,re.I)),lines[0])
        quotes.append(v+'：'+useful)
    candidates += ['## '+d['candidate_id']+' - '+d['event'],'- section: '+d['section'],'- status: candidate','- source_ids: '+', '.join(d['source_ids']),'- event_date: '+str(d.get('event_date','见日历节点')),'- facts: '+'；'.join(quotes),'- notes: '+d['reason']]
    if d.get('history_check'):candidates.append('- history_check: '+json.dumps(d['history_check'],ensure_ascii=False))
    if d.get('subject_assessment'):candidates.append('- subject_assessment: '+json.dumps(d['subject_assessment'],ensure_ascii=False))
    if d.get('genre_assessment'):candidates.append('- genre_assessment: '+json.dumps(d['genre_assessment'],ensure_ascii=False))
    candidates.append('')
(P/'event_candidates.md').write_text('\n'.join(candidates)+'\n',encoding='utf-8')
(P/'selection_decisions.md').write_text('\n'.join(head)+'\n',encoding='utf-8')
(P/'report_items.json').write_text(json.dumps(dict(report_type='daily',date='2026-10-21',items=items),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

stage=P/'staging';stage.mkdir(exist_ok=True);si=stage/'_intermediate';si.mkdir(exist_ok=True)
for name in ['report_inputs.jsonl','report_inputs_summary.md','report_inputs_index.md','release_calendar_audit.json','source_quality_audit.json','industry_history_14d.json','industry_history_14d.md','event_candidates.md','selection_decisions.md','report_items.json','selection_decisions.json']:shutil.copyfile(P/name,si/name)
labels=[('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]
md=['# 游戏行业日报｜2026-10-21','']
for sec,label in labels:
    md += ['## '+label,'']
    for j,x in enumerate([x for x in items if x['section']==sec],1):
        md += ['- '+x['body'],''] if sec=='release_calendar' else ['### '+str(j)+'. '+x['title'],'',x['body'],'']
report=stage/'game_industry_daily_2026-10-21.md';report.write_text('\n'.join(md),encoding='utf-8')
print(report);print('items',len(items),{sec:sum(x['section']==sec for x in items) for sec,_ in labels})
