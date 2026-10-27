import json,re
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parent
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
raw=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));D=raw['decisions'];DM={d['candidate_id']:d for d in D}
a=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
for merge in a.get('editorial_merged_nodes',[]):
 if merge['candidate_id'] in DM:continue
 n=merge['raw_node'];target=DM[merge['merge_into']]
 d=dict(candidate_id=merge['candidate_id'],section='release_calendar',source_ids=n['source_ids'],entities=[n['product']],event=n['event'],decision='merge',merge_into=merge['merge_into'],reason='同规范化产品、同日期的重复节点合并；原始召回与合并目标全部保留。',industry_overlap_allowed=True,scores=target['scores'],cluster_basis=dict(subject=n['product'],product=n['product'],event_date=n['event_date'],event='同产品同日产品日历节点'))
 D.append(d);DM[d['candidate_id']]=d
# A title mentioning GTA is not verbatim evidence for a priority genre.
DM['I133']['scores'].update(hook=0,total=2)
DM['I133']['genre_assessment']=dict(matched_genres=[],basis='本条经济评论未明确射击或竞技品类，不凭产品名或背景现代战争加M。',evidence=[])
DM['I133']['reason']='GTA6经济损失为假设及评论，非实测损失；主体R1，事件E2，品类无本条逐字证据M0，总分2。'
DM['I212']['scores'].update(hook=0,total=6)
DM['I212']['genre_assessment']=dict(matched_genres=[],basis='来源未明确榜单上的三款产品及各自品类；不借背景KPL赛事抬M，M0。',evidence=[])
for n in a['nodes']:
 if n.get('editorial_exclusion_reason') and DM[n['candidate_id']]['decision']=='exclude':DM[n['candidate_id']]['reason']=n['editorial_exclusion_reason']
def sid(i):return f'S{i:04}' if isinstance(i,int) else i
def claim(t,i,q):
 assert q in S[sid(i)]['text'],(i,q)
 return dict(claim=t,source_id=sid(i),evidence=q)
items=[]
def item(cid,title,triples,body=None,**kw):
 d=DM[cid];assert d['decision']=='include',cid
 x=dict(section=d['section'],title=title,candidate_id=cid,source_ids=d['source_ids'],claims=[claim(*v) for v in triples],body=body or ''.join(v[0] for v in triples));x.update(kw);items.append(x);return x
item('I138','雷霆游戏投资上海火因山风网络，持股约30%',[
 ('据游戏新知10月26日报道，雷霆游戏近日投资上海火因山风网络，持股约30%。',138,'近日，雷霆游戏投资了一家叫做上海火因山风网络的公司，占股约30%。'),
 ('该公司成立于2024年10月，报道援引企查查信息称，其名下已有6款软件著作权。',138,'这家公司成立于2024年10月，企查查显示，火因山风网络旗下软著共有6款软件'),
 ('报道列出的大股东为田佳佳；关于其是否为前阿哇龙COO，报道仍使用“疑似”措辞。',138,'大股东名为田佳佳，疑似为前阿哇龙COO')])
items[-1]['claims'] += [claim('10月26日',138,'2026-10-26 18:02')]
DM['A141']['source_ids']=['S0141','S0002']
item('A141','《全面战争：幕府将军2》完全版下架后，Creative Assembly承认外包审核失守',[
 ('《全面战争：幕府将军2》完全版因生成式AI疑虑及性能问题于上周下架后，《全面战争》系列副总裁Roger Collum进一步说明，该版本由外部团队开发，未经过与内部项目相同的审查和质量保证。',141,'wasn\'t subject to our same internal reviews and quality assurance'),
 ('公司已组织一支资深开发者小组，与Sega及外部开发者商议后续处理。',141,'We\'ve pulled a small team of senior developers together to work with Sega and the external developer on the next steps.'),
 ('Collum表示，公司不使用生成式AI制作游戏资产，并要求外部合作方遵循相同标准，但允许工具辅助分析、调试与快速原型制作。',141,'We do not use generative AI to create game assets')])
items[-1]['claims'] += [claim('《全面战争：幕府将军2》完全版',2,'《全面战争：幕府将军2》完全版'),claim('上周下架',141,'removed from sale last week amid concerns about the use of generative AI and other performance issues'),claim('《全面战争》系列副总裁Roger Collum',141,'Total War vice president Roger Collum'),claim('要求外部合作方遵循相同标准',141,'We demand the same f any external developers we work with.'),claim('分析、调试与快速原型制作',141,'analysis, debugging, or speedy prototyping')]
item('A140','《新天龙八部》以焦恩俊授权AI形象制作新门派宣传短片',[
 ('畅游在《新天龙八部》新门派昆仑的宣传中，邀请焦恩俊授权AI形象出演TVC短片。',140,'《新天龙》这次邀请了明星焦恩俊授权AI形象出演TVC短片。'),
 ('同期内容还包括由JS组合制作演唱的主题曲《破雪》，共同呈现新门派的角色形象与反差设定。',140,'歌手组合JS，为昆仑制作演唱主题曲《破雪》'),
 ('这一案例中，AI已经进入具体的角色营销素材生产环节，报道描述的是授权形象应用。',140,'授权AI形象出演TVC短片')])
items[-1]['claims'] += [claim('畅游',140,'畅游的《新天龙八部》端游'),claim('新门派昆仑',140,'推出的新门派昆仑')]
item('A191','Naavik梳理AI游戏混搭的三条技术路径，原型传播与成品体验仍有距离',[
 ('本期刊出的Naavik研究编译将AI游戏混搭分为实时联动模组、机制移植，以及完整反编译与重编译三条路径。',191,'游戏行业研究机构Naavik近日发表文章'),
 ('研究举例称，Maurice Heumann借助Claude拆解《现代战争2》历时11周，最多使用17个智能体；并行处理函数可以加速部分工作，却并不意味着完整重建没有成本。',191,'Maurice Heumann借助Claude拆解《现代战争2》，历时11周，最多使用17个智能体'),
 ('编译同时指出，不少传播中的混搭仍是粗糙原型，有的未开放试玩；机制能够拼装，并不保证可以形成完整、好玩的游戏体验。',191,'许多作品只是粗糙原型，有些存在严重问题，还有些根本没有开放试玩。')])
items[-1]['claims'] += [claim('实时联动模组',191,'其一是实时联动模组'),claim('机制移植',191,'其二是机制移植'),claim('完整反编译与重编译',191,'其三是完整反编译与重编译'),claim('并不保证可以形成完整、好玩的游戏体验',191,'来自不同作品的功能可能彼此冲突，无法形成完整体验')]
release=next(d for d in D if d['section']=='release_calendar' and d['decision']=='include')
item(release['candidate_id'],'Sign：碎冠篇',[
 ('猫猫毛工坊Nekonoke开发并发行的都市奇幻视觉小说端游《Sign：碎冠篇》于10月26日登陆Steam，支持Windows与macOS；作品交织校园日常与异世界魔女冒险，并提供全中文配音。',132,'由猫猫毛工坊Nekonoke开发并发行的都市奇幻视觉小说《Sign：碎冠篇》于今日（2026年10月26日）正式登陆 Steam，支持 Windows 与 macOS')],release=dict(product='Sign：碎冠篇',event='正式发售',date='2026-10-26',platform='Steam / Windows / macOS',company='猫猫毛工坊Nekonoke'))
items[-1]['claims'] += [claim('校园日常与异世界魔女冒险',132,'将少女的校园日常与异世界魔女的冒险交织在一起'),claim('全中文配音',132,'全中文配音')]
item('C242','《明日方舟：终末地》活动立绘被指两次修改后仍留错误，玩家追问修复质量',[
 ('《明日方舟：终末地》小葱活动立绘被玩家质疑龙尾结构异常并疑似使用AI生成，争议随后延伸到修复是否彻底。',242,'近日小终开了食堂新活动，小葱活动立绘的龙尾疑似用了ai生成'),
 ('原帖始于10月20日；10月26日新增回复称，图片已先后修改尾巴错位及头发从袖子穿出的错误，但头饰仍未修正。',242,'这张图已经更新过两次，第一次修复了尾巴画错的问题，第二次修复了右边头发从袖子里出来的问题。但头饰依然没有修'),
 ('玩家批评的重点由生成方式，转向连续修改后能否完成基本校对；帖内也有人因先前未察觉头发问题而重新检查图片。',242,'才发现第二张头发不对')],community=DM['C242']['community'])
items[-1]['claims'] += [claim('10月20日',242,'发帖：2026-10-20T14:06'),claim('10月26日',242,'2026-10-26 16:18')]
item('C252','《影之刃》手游角色修改被绑定单机发售，回复者指出调整早在9月',[
 ('《影之刃》手游角色被“全部涂黑”的指控在10月26日被冠以“3A单机新作发售前夕”，引起玩家对两款产品是否应被绑定讨论的争论。',252,'[影之刃手游]3A单机新作发售前夕，手游角色全部涂黑和谐'),
 ('当日有回复者称，确有部分角色调整，但发生时间是9月；他们质疑把旧修改重新拼接成发售前的新动作。',252,'这波是有和谐，只是部分'),
 ('另有当晚回复将时间指向9月中旬，批评直到10月末才借单机发售重新传播，争议集中在信息时间线和产品关联是否准确。',252,'皮肤和谐是9月中旬的吧，那时候不冲现在十月末来冲')],community=DM['C252']['community'])
items[-1]['claims'] += [claim('10月26日',252,'发帖：2026-10-26T10:58'),claim('发生时间是9月',252,'另外时间是9月份那波被扫到的'),claim('拼接成发售前的新动作',252,'现在挖出来强调是发售前夕，拼接起来造谣')]
body='观察：本期关于《新天龙八部》的运营报道表明，老玩家继续喜欢一个游戏世界，不等于还能接受原有的时间投入。将服务器按成长速度、日常负担和社交方式细分，是把同一个长青产品重新适配给不同生活阶段玩家的一种办法。\n\n分析：游戏新知的报道介绍，经典轻享服砍掉19项养成、删除部分跨服竞争，并采用阶段性等级上限；制作人称，今年8月上线的经典轻享服有一半活跃用户为回归老玩家。游戏日报的对照分析还援引发布会信息称，怀旧原始服今年累计新开9组服务器、活跃用户增长50%。这些是不同服务器的运营口径，不能相加或直接互相比效果，但共同说明：回归不一定依靠新增内容量，也可能来自重新安排玩家必须付出的时间。\n\n分析：这种细分保留熟悉的世界、关系和成长目标，同时允许部分玩家减少日常投入，另一些玩家继续追求慢成长或完整竞争。它也有边界：如果减负之后缺少持续目标，回归可能只是一轮短暂尝试；若不同规则让朋友难以一起游玩，分服还可能割裂原有社交关系。因此，这些案例支持的是按需求组织体验的机制，尚不能证明服务器越细分，整体留存或收入就随细分数量同步提高。'
item('D140','《新天龙八部》用差异化服务器降低回归门槛，延续熟悉世界的价值',[
 ('经典轻享服砍掉19项养成',140,'经典轻享服砍掉了19项养成'),
 ('阶段性等级上限',140,'首次采取阶段性解锁等级上限'),
 ('今年8月上线的经典轻享服有一半活跃用户为回归老玩家',140,'经典轻享服有一半的活跃用户都是回归的老玩家'),
 ('怀旧原始服今年累计新开9组服务器、活跃用户增长50%',211,'2026年《新天龙八部》怀旧原始服累计新开9组服务器，整体活跃用户数增长50%')],body=body,card_copy=dict(source_label='游戏新知与游戏日报运营分析',summary='长青游戏按成长速度和日常负担细分服务器，可降低老玩家回归门槛，但仍需持续目标与社交关系承接。',insights=[dict(title='时间投入成为门槛',detail='老玩家对熟悉世界仍有感情，但工作生活变化后难以维持旧有投入。'),dict(title='差异规则承接需求',detail='轻享服减少养成负担，原始服保留慢成长，让玩家选择更适合的节奏。'),dict(title='回归仍需长期承接',detail='不同服务器数据口径不可直接比较，细分效果仍取决于后续目标和社交关系。')]))
items[-1]['claims'] += [claim('今年8月上线',140,'今年8月上线'),claim('删除部分跨服竞争',140,'删除了天外和跨服竞争')]

# Keep story audit readable before creating any canonical final Markdown.
candidates=['# 日报事件候选｜2026-10-26','']
decisions=['# 逐项采用决策｜2026-10-26','','卡片曝光去重：读取2026-10-12至2026-10-25全部106条历史及card_exposed/card_rank/card_limit/card_exposure_source。M98、王者IP三产品榜单、京东实体、光子首曝、Metacore、Liquid Swords同事件均已有曝光并排除；无material_update入选，无card_carryover，之前排名详见history_evidence。未把完整报告收录直接当作卡片曝光。','','产品日历漏挂反查：224条行业与日历全文已扫描，71个规范节点均有决策；开测周历、Steam周预览、财报管线逐产品补录，普通版本和旧宣传显式排除。','','维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均有候选；精确计数及ID见run_summary.json的dimension_coverage。全量260/260输入留有决策，反扫包含英文与多语言镜像。','','| candidate | decision | target_section | reason |','| --- | --- | --- | --- |']
for d in D:
 sc=d.get('scores',{});score=f'E{sc["event"]}×R{sc["relevance"]}+M{sc["hook"]}={sc["total"]}；' if d['section']=='industry_news' else ''
 decisions.append(f'| {d["candidate_id"]} | {d["decision"]}'+(' into '+d['merge_into'] if d['decision']=='merge' else '')+f' | {d["section"]} | {(score+d["reason"]).replace("|","/")} |')
 candidates += [f'## {d["candidate_id"]} - {d["event"]}',f'- section: {d["section"]}',f'- status: candidate',f'- source_ids: {", ".join(d["source_ids"])}',f'- event_date: 2026-10-26（采集窗口；旧事件或未来事件按决策理由分别核验）',f'- facts: {d["reason"]}',f'- evidence: {json.dumps(d.get("subject_assessment",{}).get("evidence",[]),ensure_ascii=False)}']
 if d.get('community'):candidates.append('- community: '+json.dumps(d['community'],ensure_ascii=False))
 if d.get('history_check'):candidates.append('- history_check: '+json.dumps(d['history_check'],ensure_ascii=False))
 candidates.append('')
(P/'event_candidates.md').write_text('\n'.join(candidates)+'\n',encoding='utf-8')
(P/'selection_decisions.md').write_text('\n'.join(decisions)+'\n',encoding='utf-8')
(P/'report_items.json').write_text(json.dumps(dict(items=items),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(P/'selection_decisions.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sections=[('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]
out=['# 游戏行业日报｜2026-10-26','']
for sec,label in sections:
 out += ['## '+label,'']
 for rank,x in enumerate([x for x in items if x['section']==sec],1):
  if sec=='release_calendar':out+=['- '+x['body'],'']
  else:out += [f'### {rank}. {x["title"]}','',x['body'],'']
stage=P/'staging';stage.mkdir(exist_ok=True)
(stage/'game_industry_daily_2026-10-26.md').write_text('\n'.join(out),encoding='utf-8')
covered={s for d in D for s in d['source_ids']};assert set(S)<=covered, sorted(set(S)-covered)
for x in items:
 for c in x['claims']:assert c['claim'] in x['title']+' '+x['body'],(x['candidate_id'],c['claim'])
print('items',Counter(x['section'] for x in items),'decisions',len(D),'coverage',len(covered),'sources',len({s for x in items for s in x['source_ids']}))
