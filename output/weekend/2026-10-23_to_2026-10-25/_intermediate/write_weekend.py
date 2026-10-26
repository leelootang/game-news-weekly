import json,re,sys,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
raw=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));D=raw['decisions'];DM={x['candidate_id']:x for x in D}
audit=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
for n in audit['nodes']:
 if n.get('editorial_exclusion_reason') and DM[n['candidate_id']]['decision']=='exclude':DM[n['candidate_id']]['reason']=n['editorial_exclusion_reason']
def sid(i):return f'S{i:04}' if isinstance(i,int) else i
def cl(text,i,q):
 t=S[sid(i)]['text'];assert q in t,(i,q)
 return dict(claim=text,source_id=sid(i),evidence=next(l for l in t.splitlines() if q in l))
items=[]
def item(cid,title,triples,body=None,**kw):
 d=DM[cid];assert d['decision']=='include',cid
 x=dict(section=d['section'],title=title,candidate_id=cid,source_ids=d['source_ids'],claims=[cl(*v) for v in triples],body=body or ''.join(v[0] for v in triples));x.update(kw);items.append(x);return x
item('I039','吉比特披露代号M98已立项并确定制作人',[
 ('吉比特10月23日业绩说明会披露，代号M98已正式立项并确定制作人。',39,'代号M98已正式立项并确定制作人'),
 ('据介绍，制作人从项目初期就有独立想法，并非简单承接管理层构想。',39,'这位制作人从项目初期就有独立想法'),
 ('卢竑岩表示，公司不倾向以内部赛马决定团队淘汰，同一领域可以允许不同制作人并行探索，再各自接受市场检验。',39,'不同制作人有不同生命体验')])
items[-1]['claims'] += [cl('10月23日',39,'今日上午（10月23日）'),cl('卢竑岩',39,'董事长兼总经理卢竑岩')]
item('I529','天美三款王者IP产品同时占据iOS免费榜前三',[
 ('据游戏葡萄10月25日报道，三款王者IP产品在前一日同时占据iOS免费榜前三，形成同一IP产品矩阵集中进入榜单头部的局面。',529,'三款王者 IP 产品'),
 ('在同期周年共创之夜，天美还披露了新英雄、两部衍生番剧，以及《王者荣耀：世界》《王者万象棋》等产品动态。',529,'天美公布了'),
 ('本次变化体现为王者IP多产品同时获得用户关注；周年内容更新与衍生企划共同构成其IP扩展背景。',529,'两部新的衍生番剧')])
# The source does not name all three charting products; do not fill them in.
item('I528','米哈游参投的奥秘游戏首曝多人合作新作《潜梦者》',[
 ('获得米哈游投资的奥秘游戏在本期公开自研新作《潜梦者》的首曝PV，定位为多人合作“搜躲撤”，玩家潜入梦境并探索做梦者的记忆。',528,'他们的自研新品《潜梦者》发布了首曝PV'),
 ('团队在立项中从Unity转向UE5，并围绕“抓取”设计物品组合、伙伴互动与解谜，尽量减少战斗以避开自身短板。',528,'首先是从Unity迁移至UE5引擎'),
 ('创始人徐奥林表示，关卡环节会尽量解耦，以距离、高度差、温度、水位等环境条件容纳不同解法，而不要求玩家完成唯一预设流程。',528,'让关卡中各个环节的逻辑解耦')])
items[-1]['claims'] += [cl('获得米哈游投资的奥秘游戏',528,'不仅获得了米哈游投资'),cl('尽量减少战斗以避开自身短板',528,'决定尽量少做战斗'),cl('围绕“抓取”',528,'核心玩法机制是“抓取”'),cl('创始人徐奥林',528,'奥秘游戏的创始人徐奥林')]
item('A039','吉比特将AI用于玩法原型探索，强调提效不等于整体成本下降',[
 ('吉比特在10月23日业绩说明会上披露，团队已在美术、代码和策划中使用AI，新项目尤其Demo阶段会借此快速实现更多玩法方案。',36,'新项目中，尤其Demo阶段'),
 ('卢竑岩举例称，过去需要先讨论取舍的不同设计，现在可以直接做出原型体验；简单概念草稿也可由AI补全。',36,'原来我们有十个不同的设计思路'),
 ('他同时表示，既有项目使用AI较为慎重，不以缩减团队为目标，且同行普遍提效后，收益可能更多体现为体验和品质提升，而非总成本下降。',36,'不一定就能节省对应的成本')])
items[-1]['claims'] += [cl('简单概念草稿也可由AI补全',36,'非常简单的概念、草稿'),cl('不以缩减团队为目标',36,'从来不以减少人员为目标使用AI'),cl('10月23日',36,'23日上午召开了财报电话会议')]
item('T494','Kimi K3.1 Pro展示游戏引擎与3D资产创作能力，完整权重计划11月4日前发布',[
 ('月之暗面发布Kimi K3.1 Pro，官方展示其在Unity、Unreal Engine和Godot等游戏引擎中工作，并结合网页搜索和3D生成构建交互体验的能力。',494,'可在 Unity、Unreal Engine 和 Godot'),
 ('发布说明还展示了通过脚本在Blender及CAD软件中构建、编辑模型、材质与场景布局的方式，可作用于游戏原型与资产制作环节。',494,'无需 MCP 连接器'),
 ('模型已在Kimi产品和API中上线，完整模型权重计划于2026年11月4日前发布；这些游戏与3D能力来自发布方展示。',494,'完整模型权重将于 2026 年 11 月 4 日前发布')])
items[-1]['claims'] += [cl('模型已在Kimi产品和API中上线',494,'Kimi API 上使用'),cl('月之暗面',494,'月之暗面发布 Kimi K3.1 Pro')]
item('A488','《Future? No Thanks!》将AI生成语音替换为真人录音',[
 ('开发者Paolo Pedercini在受到玩家反弹后，移除了《Future? No Thanks!》中的若干AI生成语音，替换为此前已录制的真人配音。',488,'removed the offending TTS voice lines'),
 ('他此前解释，文本转语音被用于讽刺语境，另有少量AI代码辅助用于修复着色器和调试；这些用途披露后仍遭到批评。',488,'fixing a shader'),
 ('他向因AI使用而感到受骗的购买者提供邮件申请退款的方式，并表示下一项目将完全手工编写代码。',488,'can request a refund by emailing')])
items[-1]['claims'] += [cl('Paolo Pedercini',488,'Paolo Pedercini'),cl('《Future? No Thanks!》',488,'Future? No Thanks!'),cl('此前已录制的真人配音',488,'recorded earlier this year'),cl('下一项目将完全手工编写代码',488,'will be completely hand-coded')]

item('release-candidate-033','篮球少女：飞跃巅峰',[
 ('篮球策略养成网游《篮球少女：飞跃巅峰》于10月23日公测；玩家以教练身份安排训练，并在多周目循环中培养球员。',255,'10月23日，这款游戏已经公测')],
 release=dict(product='篮球少女：飞跃巅峰',event='公测',date='2026-10-23',platform='来源未明确具体平台',company='本期来源未披露'))
items[-1]['claims'] += [cl('篮球策略养成',255,'主打策略养成'),cl('多周目循环',255,'多周目循环育成体系'),cl('安排训练',255,'安排训练内容')]
item('release-candidate-002','蓝色星原：旅谣',[
 ('蛮啾网络旗下3D大世界多平台产品《蓝色星原：旅谣》于10月23日公布公测定档11月26日；抓宠、家园建设与多人同屏构成其主要体验方向。',34,'蛮啾网络旗下3D大世界新游')],
 release=dict(product='蓝色星原：旅谣',event='公测定档',date='2026-10-23',platform='多平台',company='蛮啾网络'))
items[-1]['claims'] += [cl('10月23日',464,'10月23日，蛮啾网络官宣'),cl('多平台',409,'编辑推荐 / 多平台'),cl('抓宠、家园建设与多人同屏',34,'捉宠、家园建设')]
item('release-candidate-005','星溯',[
 ('南棠羽网络研发的二次元箱庭动作多平台产品《星溯》于10月23日发布首曝PV及BOSS战实机演示；战斗围绕削韧、轮切、闪避和需要消耗技能点的弹反展开。',258,'今日 （10月23日）')],
 release=dict(product='星溯',event='首次曝光',date='2026-10-23',platform='PC / Android / iOS',company='南棠羽网络'))
items[-1]['claims'] += [cl('南棠羽网络研发',258,'由南棠羽网络研发'),cl('二次元箱庭动作',258,'二次元箱庭动作'),cl('多平台',258,'PC端将于2028年Q1上线，但安卓端和iOS端'),cl('BOSS战实机演示',258,'两段BOSS战的实机演示'),cl('削韧、轮切、闪避',258,'削韧机制'),cl('消耗技能点的弹反',258,'弹反以及释放角色技能均需要消耗一定的 技能点')]

item('C428','《鸣潮》签到奖励被指少发体力药，帖内补发说明改变争议焦点',[
 ('《鸣潮》签到活动被玩家对比前瞻与游戏内截图后质疑少发5个体力药，争议集中在宣传承诺与实际发放是否一致。',428,'好像是少了5个体力药'),
 ('10月23日建帖后，有回复者称回看前瞻确为10个体力剂；另一些玩家指认21日晚已有补发公告，认为发帖忽略了先前说明。',428,'确实是10个体力剂'),
 ('因此，帖内意见也从奖励数量本身，转向是否应在指责前核对补发安排，形成对运营失误与对发帖方式的两种批评。',428,'知道你很急，但你公告都不看就发')],community=DM['C428']['community'])
items[-1]['claims'] += [cl('21日晚已有补发公告',428,'这是21号下午七点的公告'),cl('10月23日建帖',428,'发帖：2026-10-23T20:37')]
item('C616','《三角洲行动》收藏品复制活动被质疑拉大随机收益差距',[
 ('《三角洲行动》“惊喜渡鸦”活动被玩家描述为：在指定地点放置收藏品后，可能得到升级、降级、消失、不变或复制翻倍的结果。',616,'叫做惊喜渡鸦'),
 ('10月25日的帖子称，复制机制可能连续增加稀有收藏品“非洲之心”的数量；玩家不满的核心在于，少数人的随机高收益与长期搜集的投入产生过大差距，担忧原有稀有品价值和经济预期被打乱。',616,'非洲之心可以随着狗运无限增值'),
 ('也有回复将其视为自愿承担风险的抽奖，认为应接受运气差异；另有玩家以自己获得多颗收藏品的经历表达收益落差。',616,'愿赌服输罢了')],community=DM['C616']['community'])
items[-1]['claims'] += [cl('10月25日',616,'发帖：2026-10-25T19:59'),cl('长期搜集的投入',616,'几个月甚至一年'),cl('自己获得多颗收藏品',616,'赌了3颗心')]

body='观察：GameDiscoverCo对合作恐怖游戏《Invokyr》的本期访谈与估算显示，清楚可转述的题材卖点，需要通过反复测试成为真实可玩的核心机制，才有机会把传播转为持续购买。\n\n分析：通讯估算，该作10月8日发售后售出约25万份；开发者称中国玩家占比约48%。作者认为，“受诅咒的桌游”容易让观众联想到恐怖版《勇敢者游戏》，即使营销未直接使用这一比较，玩家评论与视频仍会自然复述。这说明传播入口可以由观众熟悉的参照物形成，但销量和收入仍是作者估算，不能视作开发商结算数据。\n\n更关键的是，团队称2025年9月首轮测试就发现玩家没有充分关注桌游部分，之后继续进行小规模测试、试玩和封闭测试。桌游中枢、随机任务与具有正负效果的骰子，逐步把容易理解的题材变成可重复体验的差异。由此可见的机制是：外部类比负责降低理解成本，测试负责确认玩家实际围绕核心系统游玩；只复刻题材外观，未必能够复现相同的传播与留存结果。'
item('D442','《Invokyr》案例：可转述的题材卖点如何通过测试成为核心玩法',[
 ('售出约25万份',442,'~250,000 copies sold'),('10月8日',442,'launched on Oct. 8th'),('中国玩家占比约48%',442,'~48% of players'),('2025年9月首轮测试',442,'first playtest was in September 2025'),('玩家没有充分关注桌游部分',442,'players not focusing on the board aspect'),('随机任务',442,'random quests'),('正负效果的骰子',442,'dice with weird good/bad effects')],body=body,card_copy=dict(source_label='GameDiscoverCo访谈分析',summary='清楚的题材类比能降低观众理解成本，反复测试则让这一卖点真正成为玩家反复使用的核心机制。',insights=[dict(title='类比降低理解成本',detail='受诅咒桌游让观众自然联想到熟悉的电影题材，便于传播。'),dict(title='测试验证玩法重心',detail='首轮测试发现玩家未关注桌游，后续继续迭代其核心地位。'),dict(title='卖点需要系统承接',detail='随机任务与正负骰子把题材转为重复体验，只复制外观不等于复制效果。')]))
# Movie title is author-described analogy, not an official licence claim.
items[-1]['claims'] += [cl('《勇敢者游戏》',442,'Jumanji - the original movie'),cl('小规模测试、试玩和封闭测试',442,'2nd & 3rd [smaller] playtests')]
body='观察：Game Oracle在10月23日发布的v7开发日志中，将市场资料收集、设计文档和任务组织连接起来。其核心变化是让一次研究的理由随设计和执行保留下来，而不只产出一份读完即放下的市场报告。\n\n分析：开发日志介绍，Concept Compass可以把概念研究生成可编辑的GDD草稿、项目愿景、竞品雷达和研究板；Scrapbook允许保存游戏、图片、统计、搜索结果与笔记，并把带来源的材料放到设计段落旁边。这里可能产生的价值，是让“为什么要做这项功能”能够与任务一起流转，后续范围调整或原型验证时仍能找到最初假设，而不是不断重复资料搜索。\n\n这一连接能否改善决策，仍取决于比较组和数据口径。日志中的Powersearch允许审阅SQL后执行查询，再用保存的数据集比较中位数及不确定区间；开发者也明确指出，组间差异不能证明因果。因此，工具展示的是一条可回查的研究到设计流程，并没有证明自动生成文档就会带来更高商业成功率。'
item('D443','Game Oracle v7把市场证据带入设计文档与任务，保留决策理由',[
 ('10月23日',443,'Published: 10/23/2026'),('可编辑的GDD草稿',443,'A Draft GDD you can edit'),('项目愿景、竞品雷达和研究板',443,'A Project Vision whiteboard'),('保存游戏、图片、统计、搜索结果与笔记',443,'games, images, colour palettes'),('审阅SQL后执行查询',443,'inspect the SQL and run'),('中位数及不确定区间',443,'medians and an uncertainty interval'),('组间差异不能证明因果',443,"a difference between groups doesn't establish what caused it")],body=body,card_copy=dict(source_label='Game Oracle开发日志',summary='市场数据与设计文档相连，可以保留功能选择的原始理由；其价值仍取决于比较组、口径和假设的质量。',insights=[dict(title='证据进入设计上下文',detail='研究材料可放在GDD和愿景旁，便于回查最初判断。'),dict(title='任务携带决策理由',detail='工作板链接研究和文档，使执行时仍能追溯功能来源。'),dict(title='比较仍有口径边界',detail='SQL可审阅、数据集可复用，但组间差异不等于因果。')]))
items[-1]['claims'] += [cl('Game Oracle',443,'v7 of Game Oracle')]
for cid in ['D442','D443']:DM[cid]['scores']=dict(relevance=2,insight=3,evidence=3 if cid=='D442' else 2,card=3,total=11 if cid=='D442' else 10)
(P/'report_items.json').write_text(json.dumps(dict(items=items),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(P/'selection_decisions.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Required narrative artifacts precede the publishable final file.
candidates=['# 周末报事件候选｜2026-10-23_to_2026-10-25','']
decisions=['# 逐项采用决策','', '卡片曝光去重：双周窗口2026-10-09至2026-10-22，110条历史均读取card_exposed、rank、limit与source。《人间异想计划》历史曝光为true（21日报rank1、周报rank2，limit10），本期换源排除。无符合资格的card_carryover；不将已进入完整报告等同已上卡。','', '维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均保留候选，计数与来源完整检查见full_input_review.json；PC候选主体独立判定，不凭平台或品类给R3。','', '| candidate | decision | target_section | reason |','| --- | --- | --- | --- |']
for d in D:
 sc=d.get('scores',{});score=f'E{sc["event"]}×R{sc["relevance"]}+M{sc["hook"]}={sc["total"]}；' if d['section']=='industry_news' else ''
 reason=score+d['reason'];decisions.append(f'| {d["candidate_id"]} | {d["decision"]}'+(' into '+d['merge_into'] if d['decision']=='merge' else '')+f' | {d["section"]} | {reason.replace("|","/")} |')
 facts=[]
 for si in d['source_ids']:
  tx=S[si]['text'];facts.append(si+'：'+next((l[:220] for l in tx.splitlines() if l.strip()),''))
 candidates += [f'## {d["candidate_id"]} - {d["event"]}',f'- section: {d["section"]}','- status: candidate','- source_ids: '+', '.join(d['source_ids']),'- facts: '+' / '.join(facts),'- notes: '+d['reason'],'']
dim={label:sum(bool(re.search(pat,d['event'],re.I)) for d in D if d['section']=='industry_news') for label,pat in [('国内移动','手游|移动|mobile|吉比特|王者|网易|米哈游|腾讯|叠纸|巨人'),('国产产品与人才','国产|制作人|团队|工作室|人才|星溯|潜梦者|M98'),('市场数据','市场|收入|销量|用户|百万|million|millionen|MAU|榜|销售'),('并购','收购|投资|融资|financi|acquis|Finanzier'),('平台政策','平台|政策|许可|Steam|GameMaker|App Store'),('档期变动','上线|发售|公测|首曝|定档|停服|停运|launch|release'),('资本组织','CEO|高管|裁员|股|裁|关闭|shutdown|boss'),('海外重大','Capcom|Xbox|BioWare|EA|Supercell|Stillfront|GameMaker') ]}
decisions[4]='维度覆盖自检（可重叠）：'+' / '.join(k+' '+str(v)+'张候选' for k,v in dim.items())+'。全部619条来源与逐段日期信号见full_input_review.json；主体与品类单独取证。'
decisions.insert(6,'产品日历漏挂反查：全量industry_news与release_calendar已按句反扫，pipeline管线、星溯简称、蓝原简称、篮球公测、潜梦者日期分歧及Dispatch跨平台均进入审计；普通版本/历史/无主语绑定不冒充新品，全部节点确定性sync。')
(P/'event_candidates.md').write_text('\n'.join(candidates)+'\n',encoding='utf-8');(P/'selection_decisions.md').write_text('\n'.join(decisions)+'\n',encoding='utf-8')
stage=P/'staging';stage.mkdir(exist_ok=True)
lines=['# 游戏行业周末报｜2026-10-23—2026-10-25','']
for section,label in [('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]:
 lines += ['## '+label,''];n=0
 for it in items:
  if it['section']!=section:continue
  n+=1
  lines += ['- '+it['body'],''] if section=='release_calendar' else [f'### {n}. {it["title"]}','',it['body'],'']
name='game_industry_weekend_2026-10-23_to_2026-10-25.md'
(stage/name).write_text('\n'.join(lines),encoding='utf-8')
print('items',len(items),'staged',stage/name)
