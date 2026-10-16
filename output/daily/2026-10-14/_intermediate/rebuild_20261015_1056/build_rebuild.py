"""One-run editorial reconstruction; only writes staged report audit artifacts."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MID = ROOT / '_intermediate'
WORKSPACE = Path(r'C:\Users\Admin\Documents\AI游戏行业周月报')
sys.path.insert(0, str(WORKSPACE / 'scripts'))
from sync_release_decisions import sync

rows = [json.loads(x) for x in (MID/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
inputs = {x['source_id']: x for x in rows}
history = json.loads((MID/'industry_history_14d.json').read_text(encoding='utf-8'))['occurrences']
decisions, items = [], []
consumed = set()

def sid(n): return f'S{n:04d}'
def dump(path, value): path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def evidence(n, needle):
    text = inputs[sid(n)]['text']
    assert needle in text, (n, needle)
    lines = text.splitlines()
    for line in lines:
        if needle in line: return line.strip()
    return needle

def history_check(patterns=()):
    matches = [h for h in history if any(re.search(p, h['title'], re.I) for p in patterns)]
    return {'history_match':bool(matches), 'novelty':'repeat_only' if matches else 'new_event',
            'prior_occurrences':[f"{h['title']} | {h['report_window']['start']}_to_{h['report_window']['end']} | card_exposed={h['card_exposed']}, card_rank={h['card_rank']}, card_limit={h['card_limit']}, card_exposure_source={h['card_exposure_source']}" for h in matches],
            'new_facts':[], 'prior_card_exposed':any(h['card_exposed'] for h in matches) if matches else None}

def industry(cid, title, nums, e, r, m, reason, include=False, entities=None, patterns=(), tracks=()):
    h = history_check(patterns)
    d = {'candidate_id':cid,'section':'industry_news','source_ids':[sid(n) for n in nums],
         'entities':entities or [title], 'event':title,'decision':'include' if include else 'exclude','reason':reason,
         'scores':{'event':e,'relevance':r,'hook':m,'total':e*r+m},'history_check':h,
         'priority_tracks':list(tracks), 'industry_ai_reverse_scan':'AI仅为背景，核心是资本/组织/市场/生命周期变化' if any(n in nums for n in [32,38,81,82,236]) else '已反扫；未发现符合AI采用门槛的独立事件'}
    if len(nums)>1:
        d['cluster_basis']={'subject':(entities or [title])[0],'product':title,'event_date':'2026-10-14报道同一事件','event':title}
    decisions.append(d); consumed.update(nums)
    return d

def ai(cid, title, nums, include, reason, tier='direct_application', stages=('development',), reverse=True, migration=''):
    d={'candidate_id':cid,'section':'ai_trends','source_ids':[sid(n) for n in nums], 'entities':[title], 'event':title,
       'decision':'include' if include else 'exclude','reason':reason,'ai_tier':tier,'game_stage':list(stages),'industry_reverse_scan':reverse}
    if tier=='transferable_frontier': d['migration_path']=migration or '未证明明确游戏业务迁移链条，不采用'
    if len(nums)>1: d['cluster_basis']={'subject':title,'product':title,'event_date':'2026-10-14报道同一事件','event':title}
    decisions.append(d); consumed.update(nums)
    return d

def publish(d, title, triples, extra=None, join=''):
    claims=[{'claim':claim,'source_id':sid(n),'evidence':evidence(n,needle)} for claim,n,needle in triples]
    item={'section':d['section'],'title':title,'candidate_id':d['candidate_id'],'source_ids':d['source_ids'],'claims':claims,
          'body':join.join(x[0] for x in triples)}
    if extra: item.update(extra)
    items.append(item)
    return item

# Capital/platform/product events are individually judged, never a low-signal catch-all.
d=industry('I032','库洛入股言之域并委派董事',[32,38],3,3,2,'国内厂商战略投资及董事席位变化；AI为被投业务背景，不是已接入库洛产品的证明。',True,['库洛','言之域'])
publish(d,'库洛持有言之域15%股权，刘胜进入董事会',[
 ('企查查信息显示，广州库洛科技有限公司成为言之域科技（深圳）有限公司新增股东，持股15%，刘胜进入董事会。',38,'持股15%'),
 ('言之域旗下产品包括AI音频平台“Vocu悟声”和3D角色驱动系统“元语TalkiVerse”，覆盖语音及角色动作生成。',38,'两大核心产品'),
 ('报道提到的约2亿元是本轮融资对应估值，并非库洛投资金额；现有材料没有证明相关模型已经接入库洛游戏。',38,'对应估值约2亿元')])
d=industry('I034','腾讯领投Flow Games融资4600万美元',[34,39,82],3,3,2,'同一Flow Games融资，多家媒体完整报道；昨日仅摘要候选被排除，不是已发布历史事件。',True,['腾讯','Flow Games','Smash Fest'],tracks=('pvp_competitive',))
publish(d,'腾讯领投Flow Games4600万美元融资',[
 ('土耳其游戏工作室Flow Games获得4600万美元融资，腾讯领投，出资约占本轮总额的四分之三。',82,'Tencent represents roughly three quarters'),
 ('据AppMagic估算，其手游《Smash Fest》下载量从6月逾200万增长至7月1020万，玩家支出同期从69.2万美元增至340万美元。',82,'Smash Fest downloads rose'),
 ('其《Smash Fest》累计玩家支出估计接近890万美元，其中约830万美元来自iOS。',82,'lifetime spend is now almost $8.9m')])
d=industry('I125','模拟经营续作动物园之星2发售',[21,125],3,3,2,'新品正式发售、模拟经营优先赛道，两家来源相互支持；正文不猜测未明示的实际发售日。',True,['动物园之星2'],tracks=('life_simulation',))
publish(d,'模拟经营续作《动物园之星2》已发售',[
 ('《动物园之星2》（Planet Zoo 2）现已登陆PS5、Xbox Series及PC平台。',125,'游戏现已登陆'),
 ('游戏允许玩家建造动物园，保育陆生、水生与飞行物种，并将动物放归园区之外的野生动物保护区。',125,'保育陆生')])
d=industry('I126','第一人称魂类新品不朽遗志发售',[16,126],3,3,2,'新品正式发售、魂类RPG优先赛道，两来源支持；非媒体评分事件，未凭报道日期补实际发售日。',True,['不朽遗志'],tracks=('strategy_card_rpg',))
publish(d,'《幽灵行者》创作者新作《不朽遗志》已发售',[
 ('《不朽遗志》（Valor Mortis）现已登陆PS5、Xbox Series及PC平台。',126,'游戏现已登陆'),
 ('这款出自《幽灵行者》创作者之手的第一人称魂类动作游戏，以一名起死回生的拿破仑军队前士兵为主角，围绕超自然力量与怪物战斗展开。',126,'拿破仑军队')])
d=industry('I081','Miniclip推出AdSurge移动广告平台',[81],3,3,1,'腾讯体系移动发行基础设施的新业务上线；只计一个独立全文源，相关摘要与同URL不额外抬高M。',True,['腾讯','Miniclip','AdSurge'])
publish(d,'腾讯旗下Miniclip推出移动广告平台AdSurge',[
 ('Miniclip推出AdSurge，覆盖移动游戏获客与广告变现，初期面向主要依靠应用内广告收入的产品。',81,'The network covers both user acquisition'),
 ('据公司介绍，该平台经过三年研发，以独立公司运营，合作伙伴数据严格隔离；平台借鉴了腾讯广告生态的技术经验，但算法围绕自身全球流量从头构建。',81,'AdSurge operates as an independent'),
 ('AdSurge下一阶段计划扩展至内购及混合变现游戏，并以广告回报、净广告收益、玩家体验和SDK表现衡量效果。',81,'The firm said the next phase')])
d=industry('I082S','Spill Games融资1050万美元',[82],3,2,1,'海外拼图手游融资，移动生产/发行有明确迁移点R2；不因手游标签自动等同中国移动市场或策略RPG优先赛道。融资是核心，AI产线为建设方向。',True,['Spill Games'])
publish(d,'拼图工作室Spill Games获1050万美元融资',[
 ('位于班加罗尔的Spill Games获得1050万美元融资，由Elevation Capital领投。',82,'Spill Games has raised $10.5m'),
 ('工作室由前PlaySimple和Zynga高管Om Misra、Harsh Garg及Tapan Ranjan创立，定位于AI原生拼图游戏。',82,'former PlaySimple and Zynga'),
 ('公司称正在建设AI生产管线，从扫描市场玩法趋势到制作、发行游戏，目标是让一名产品经理同时管理多款产品；这仍是公司描述的产线方向。',82,'The studio says it is building')])
d=industry('I059','Xbox集中研发资源成立Labs团队',[59,135],3,2,2,'新组织整合研发，浏览器分发等具有平台迁移点R2，不因海外大厂自动R3；并非新增大规模招聘或强制AI路线。',True,['Xbox','Xbox Labs'])
publish(d,'Xbox Labs整合研发探索，覆盖浏览器游戏与平台技术',[
 ('Xbox成立Labs团队，整合内部研发探索，由工程师和研究人员构成的小团队尝试新的游戏体验及技术。',59,'Labs'),
 ('报道涉及浏览器技术、WebGPU以及Apple Silicon等方向，重点在于降低实验进入玩家体验的阻力。',59,'WebGPU'),
 ('这次调整不是新增大规模招聘，也没有把使用AI设为项目的统一前提。',59,'AI')])
d=industry('I058','三七梦回甄嬛传两个月产品经营表现',[58],2,3,1,'国内重点厂商R3；当前榜位结合二合循环、女性向IP改编及近期社群运营构成产品经营信号E2，不是孤立纯榜单；历史上线不冒充新上线，用户明确不作深度。',True,['三七互娱','梦回甄嬛传'],tracks=('life_simulation',))
publish(d,'三七互娱《梦回甄嬛传》升至微信小游戏畅销榜第59名',[
 ('游戏新知报道，三七互娱的女性向二合小游戏《梦回甄嬛传》约在8月上线，目前逐渐升至微信小游戏畅销榜第59名。',58,'游戏大约在8月上线'),
 ('产品以合成订单获得货币、消耗货币推进剧情为核心循环，再叠加不同结算周期的奖励活动；玩家扮演穿越到原剧场景中的宫女，以剧情分歧和经典场面推进体验。',58,'每完成一个 二合订单'),
 ('报道还记录了上周加入的配套社群功能，以及近日将“送真花”与番外卡牌、好友互助结合的运营尝试，呈现三七互娱在女性向休闲产品上的持续试水。',58,'就在上周')])
d=industry('I175','王者万象棋上线一月经营表现',[175],2,3,1,'国产自走棋新品一个月成绩与轻量化机制，非纯榜单；未将未披露的留存率量化，不凭记忆添加厂商。',True,['王者万象棋'],tracks=('strategy_card_rpg',))
publish(d,'《王者万象棋》上线一月进入畅销榜前五，轻量化自走棋获得验证',[
 ('据游戏日报报道，《王者万象棋》上线后曾连续11天位居iOS免费榜第一，畅销榜最高达到第五。',175,'连续11天霸榜'),
 ('产品将单局时长压缩至约15分钟，并弱化传统自走棋中的利息、连胜连败等学习负担。',175,'15'),
 ('游戏的皮肤道具不直接增加战斗力，付费动机更多围绕审美、角色认同和稀缺收藏展开。',175,'各类皮肤道具都无法提供直接的战斗力加成')])
d=industry('I084','Squad Busters确定下架与停服日',[84],2,3,1,'Supercell固定R3；停服日期明确，区别于去年已停止研发的旧阶段；同URL摘要不计独立M2。',True,['Supercell','Squad Busters'],tracks=('pvp_competitive',))
publish(d,'Supercell《Squad Busters》将于12月14日停服',[
 ('Supercell确认，《Squad Busters》将于12月1日从App Store和Google Play下架，并于12月14日停止游玩。',84,'December 1 and stop being playable on December 14'),
 ('已安装玩家可继续游玩至停服日，届时所有活动与计时器结束；游戏不会提供离线模式、私人服务器或公开代码。',84,'ruled out offline play'),
 ('这次新增的是具体关闭安排，研发结束则已在去年10月宣布，内购也早已关闭。',84,'announced the end of Squad Busters development last October')])
d=industry('I029','索尔附魔主播营销进入韩国国会质询',[29],2,3,1,'MMORPG优先赛道R3；国会讨论付费主播营销与披露义务是监管信号，不写成已立法或公司已被认定违法。',True,['网石','索尔：附魔'],tracks=('strategy_card_rpg',))
publish(d,'网石《索尔：附魔》主播推广争议进入韩国国会质询',[
 ('GameLook报道，网石MMORPG《索尔：附魔》的付费主播推广争议进入10月12日的韩国国会讨论。',29,'10月12日'),
 ('争议围绕主播接受推广资源后在游戏中充值、竞争，以及普通玩家能否识别这种商业关系展开。',29,'主播'),
 ('报道涉及监管调查与信息披露要求的讨论，主管部门承认尚未开展相关调查；这并非已经生效的新法或对网石违法的最终认定。',29,'没有开展相关调查')])
d=industry('I030','苹果独立游戏周引入PC主机产品到iOS',[30],2,3,1,'事件核心是多款游戏跨平台迁移而不是普通促销；移动分发直接相关R3。',True,['苹果','iOS'])
publish(d,'苹果独立游戏周推动七款PC及主机独游进入iOS',[
 ('据GameLook报道，苹果开启“独立游戏周”，将《师父》《无人深空》《吸血鬼爬行者》《九王》等七款PC及主机独立游戏移植至iOS生态。',30,'七款PC主机平台'),
 ('本次引入的内容以已经在PC及主机平台建立受众的独立产品为主，涵盖格斗、探索与策略等不同体验，扩展了移动端买断制内容供给。',30,'基本全部都是在PC主机平台')])
d=industry('I062','ESA建议将中国安伯尼克列入美国恶名市场名单',[62],2,3,1,'国内主体的游戏内容授权及渠道合规信号R3；名单建议不等于已列入或禁售。',True,['Anbernic','ESA'])
publish(d,'ESA建议将中国掌机厂商Anbernic列入“恶名市场”名单',[
 ('美国娱乐软件协会ESA建议美国贸易代表办公室将中国掌机厂商Anbernic列入“恶名市场”名单。',62,'recommended that retro console maker Anbernic'),
 ('ESA指称相关设备经常搭配装有未经授权游戏的存储卡销售，并要求加强对预装游戏库、销售渠道和重复卖家的处理。',62,'preloaded with hundreds or thousands'),
 ('这是行业协会提交的建议和指控，不是美国政府已经完成列入名单或实施禁售的决定。',62,'recommended')])
d=industry('I097','战狗销量300万与一个月在线变化',[97],2,3,1,'PVP优先赛道R3；当前经营数据与经济系统问题，不将9月22日旧稿125万销量拼成同日多源。',True,['BULKHEAD','战狗'],tracks=('pvp_competitive',))
publish(d,'《战狗》销量超过300万份，在线回落暴露局内经济压力',[
 ('GameRes报道，BULKHEAD的大战场射击新作《战狗》（WARDOGS）日前宣布全球销量超过300万份，仍处抢先体验阶段。',97,'300'),
 ('文章记录其同时在线峰值从开服时40多万回落至16万，并指出战斗、后勤、建造等行为的收益失衡会改变玩家参与前线的动力。',97,'滑落到16万'),
 ('跨局继承金库把团队贡献转换为个人资产，但高额战备损失与后置解锁也放大了新老玩家差距。',97,'跨局继承的金库')])
d=industry('I144','韩国单人铁匠模拟游戏ForgeTax经营成绩',[144],2,3,1,'模拟经营优先赛道R3，当前销量估算及单人开发机制；不是把旧补丁当新品发布。',True,['ForgeTax'],tracks=('life_simulation',))
publish(d,'单人开发的铁匠游戏《ForgeTax》销量估算超过20万份',[
 ('罗斯基介绍，韩国学生独立开发的《ForgeTax》在发售一周多后，据VGI估算销量已超过20万份。',144,'20万'),
 ('产品以第一人称打铁为核心，玩家要在继续强化、上交巨龙贡品和用剑购买遗物之间分配资源，收益与碎剑风险围绕同一件成品展开。',144,'三种用途'),
 ('这一销量属于第三方平台估算；持剑与巨龙战斗的内容仍是开发者以11月为目标的更新计划，并非现有玩法。',144,'目标是在11月更新')])
d=industry('I236S','莉莉丝发行Survival Log当前销量与受众结构',[236],2,3,1,'深度源反扫发现国内重点发行商的产品数据，单列行业候选；不与下文深度的三款不同产品重复。',True,['莉莉丝','Survival Log'],tracks=('life_simulation',))
publish(d,'莉莉丝发行《Survival Log》销量估算约30万份',[
 ('GameDiscoverCo估算，莉莉丝发行的生存模拟游戏《Survival Log》销量约30万份，当前在线峰值约7000，发售后最高曾达1.3万。',236,'hanging out at 7k peak'),
 ('据其数据，约80%的玩家来自中国；产品更偏重资源整理、建造与管理，同时保留抵御僵尸的塔防式环节。',236,'80% of players are Chinese'),
 ('游戏通过手机消息、无人机和支援任务等机制，将幸存者与其他NPC联系起来。',236,'cell phone texts, drones, and support missions')])

# AI: concrete game deployments first; frontier transfer news follows them.
d=ai('A026','游族公开AI红岸研发管线',[26],True,'具体游戏研发场景、模型网关及工具层，不将演示写成量产。')
publish(d,'游族披露“AI红岸”管线，覆盖策划、资产与测试环节',[
 ('游族在10月11日的交流活动中介绍“AI红岸”，围绕游戏研发、运营等六大场景梳理上百个子场景，并通过统一模型网关与Skill Hub组织工具。',26,'六'),
 ('YOOLab围绕世界设定、任务规划、多模态协同、知识库与自动评估构建内容管线；NPC演示将模型决策与引擎执行区分，战斗伤害仍由确定性逻辑结算。',26,'YOOLab'),
 ('YOOSpark沿多智能体协作推进游戏创作平台，“一个想法生成完整可玩世界”仍处探索阶段。',26,'YOOSpark')])
d=ai('A057','不问凡尘AI资产与交互产品成绩',[57],True,'游戏产品直接应用AI资产、音效和对话，且有当前销量披露；不把标价乘销量视为实收。',stages=('development','product'))
publish(d,'朝夕光年《不问凡尘》销量26万份，AI覆盖资产与对话',[
 ('游戏新知报道，朝夕光年旗下《不问凡尘》日前宣布销量达到26万份。',57,'26万'),
 ('产品使用AI制作角色、场景、道具及音效，并提供AI对话功能，技术来自火山引擎。',57,'火山'),
 ('游戏当前处于抢先体验阶段，简体中文区好评率为87%。',57,'好评率为87%')])
d=ai('A166','Epic AI辅助重写启动器推出预览版',[166],True,'AI明确写新代码并参与审查，已公开预览；不重复AI射击项目旧新闻。',stages=('development','publishing'))
publish(d,'Epic以AI辅助重写商店客户端，预览版开始提供下载',[
 ('Epic Games Store推出全新客户端预览版，负责人Martin Keely确认，团队从头更换架构，使用AI编写和审查新功能代码，而不只是分析旧代码。',166,'We started from scratch'),
 ('Epic称启动耗时减半，并宣称冷启动进入商店比Steam快46%；PC Gamer表示尚未自行测试这些性能数字。',166,'We have yet to test the client ourselves'),
 ('预览客户端已提供Windows、macOS和Linux版本，Epic目前按测试方式逐步吸收玩家反馈。',166,'The preview client can be downloaded')])
d=ai('A080','Google Play扩展游戏发现与Gemini能力',[80],True,'推荐和玩家发现直接作用于移动游戏分发；不另将同次发布拆成行业政策条目。',stages=('publishing','operations'))
publish(d,'Google Play推出Game Finder，强化游戏发现与玩家连接',[
 ('Google Play推出Game Finder，按玩家偏好和评论帮助发现游戏，初期面向美国英语用户。',80,'Game Finder'),
 ('公司同时披露，Play in Gemini上线两个月内带来逾600万次应用安装，并将通过Gemini Live提供语音推荐。',80,'over 6m app installs'),
 ('Game Finder还会解释推荐原因，展示相似玩家及所关注用户的游玩情况，将个性化匹配与社区信号结合。',80,'It also explains why a game has been suggested')])
d=ai('A133','NVIDIA展示新版DLSS5模型及游戏接入计划',[46,133,173],True,'聚类的是同一次DLSS5模型更新公告，不是仅因技术相似合并不同事件；具体游戏接入仍为计划。',stages=('development','product'))
publish(d,'新版DLSS 5模型缩减渲染开销，《燕云十六声》等计划接入',[
 ('NVIDIA介绍新版DLSS 5模型，强调减少神经渲染开销，并通过几何与颜色约束保持角色及场景表现。',133,'DLSS'),
 ('据PC Gamer转述，公司称该模型较上一版缩小24%，4K显存占用降低约20%，这些是厂商提供的技术口径。',173,'24%'),
 ('《霍格沃茨之遗》计划11月5日更新；《燕云十六声》也在后续支持名单中，具体日期仍待明确，接入尚属后续安排。',173,'The new update is coming on November 5')])
d=ai('A178','Gemini4Argon全面开放',[178,179,180],True,'全面开放与编码/3D原型能力、成本共同构成迁移价值，区别于例行跑分；第三方比较不当作通用性能承诺。',tier='transferable_frontier',reverse=False,
     migration='代码库重构与可渲染3D原型能力 → 游戏工具/原型研发 → 可能缩短迭代周期；实际工程效率须在各项目验证')
publish(d,'Gemini 4 Argon全面开放，迁移点落在代码维护与3D原型',[
 ('Google宣布Gemini 4 Argon面向开发者及企业开放，入门价格为每百万输入token2美元、输出token10美元。',178,'每百万输入 token 2 美元'),
 ('官方列举了大型代码库重构，以及使用原生代码构建可在浏览器渲染的3D可视化和游戏原型等内部案例。',178,'高保真游戏'),
 ('迁移到游戏研发时，这类能力可能作用于工具维护和交互原型迭代；内部案例并不等于对任意游戏项目的效率保证。',178,'架构重构')])
d=ai('A187','Grok Voice3上线API',[187],True,'API可用、亚秒级延迟与语音打断机制对应明确实时角色交互迁移链，不写成已有游戏采用。',tier='transferable_frontier',stages=('product',),reverse=False,
     migration='低于一秒的语音到语音交互及打断处理 → 实时NPC/陪伴角色 → 可能降低轮流发言等待成本；没有游戏落地证据')
publish(d,'Grok Voice 3.0上线API，亚秒级对话指向实时角色交互',[
 ('xAI发布语音到语音模型Grok Voice 3.0，并在Voice Agent API提供，价格为每分钟0.08美元。',187,'$0.08 / 分钟'),
 ('公司披露延迟低于一秒，并强调对停顿、轮流发言和打断的处理能力。',187,'低于一秒'),
 ('这类低延迟语音能力可迁移到实时NPC或陪伴角色，可能减少对话等待；来源没有显示它已经进入具体游戏。',187,'停顿、轮流发言和打断')])
d=ai('A181','ComfyUI新增NVIDIA视频特效节点',[181],True,'虽正文短但三个明确能力及本地管线均有直接文本证据，迁移到游戏营销视频后期而非凭空说赋能。',tier='transferable_frontier',stages=('publishing',),reverse=False,
     migration='本地视频超分、补帧、SDR转HDR节点 → 游戏宣传视频后期 → 可在节点工作流串联处理，未提供游戏实测效率')
publish(d,'ComfyUI接入NVIDIA视频特效节点，可用于宣传视频后期',[
 ('ComfyUI官方博客介绍，NVIDIA RTX视频特效以自定义节点形式在本地运行，支持视频超分、补帧及SDR转HDR。',181,'支持视频超分'),
 ('官方推荐按超分、补帧、HDR的顺序组织管线。',181,'按超分、补帧、HDR'),
 ('对游戏发行素材而言，这提供了串联处理实录视频的后期路径；现有来源没有给出游戏团队的实测节省时间。',181,'本地运行')])

# Explicit exclusions and repeated events, each with its own score/history record.
industry('I027','出版业十五五规划涉网络游戏',[27],2,3,0,'正文所链接规划为9月21日材料，未证明14日新增发布/生效状态；不将“近日”改成今日政策。',entities=['网络游戏','出版业规划'])
industry('I031','影之刃零试玩与制作访谈',[31,116],1,3,1,'已有档期与后续PV/玩法访谈，不是首次曝光或本日上线。',entities=['影之刃零'])
industry('I035D','三角洲行动5800万DAU复述',[35],2,3,0,'历史已有且曾进入订阅卡片；设计复盘、换媒体和补背景不是实质状态变化。',entities=['腾讯','三角洲行动'],patterns=('三角洲行动.*5800',))
industry('I035S','三角洲行动设计与组织复盘',[35],1,3,1,'专访具有设计解释但未证明本期新的重大组织或生命周期状态；与DAU旧事件分开评分。',entities=['腾讯','三角洲行动'])
industry('I036','多人独游山寨趋势分析',[36],2,3,0,'主要案例和爆发时间早于本窗口，没有可定位的本期市场新增状态；AI仅为推测，不能当成采用事实。',tracks=('pvp_competitive',))
industry('I037','Aream第三季度手游IAP数据',[37,82],2,3,0,'同一Aream报告与同一组数据，历史已订阅曝光；新增媒体数与老产品年龄分布不构成material_update。',patterns=('三季度游戏并购额',))
industry('I040','针影裁梦主创专访与中国市场合作意向',[40],1,3,1,'创作过程、本地化与未来功能意向；没有证明新的商业状态，不能把首次采访当新品首曝。',tracks=('life_simulation',))
industry('I060','Xbox内容IP战略表态',[60],1,2,1,'含实质跨媒介战略但无新增资本/项目/组织决定；不与不同日期的XP部门成立混成新事件。')
industry('I061','育碧关闭RedLynx及工作室调整',[61,83],2,2,2,'确有工作室关闭而非仅裁员；全球多工作室成本调整及移动业务迁移点R2，不因大厂升为R3；总分6未过线。',entities=['育碧','RedLynx'])
industry('I063','Rockstar多年人员规模扩张',[63],1,2,1,'多年人员统计不是本期核心管理层变动或新增组织，平台型研发效率迁移点R2。')
industry('I064','Legacy Games关闭商店及服务',[64],2,2,1,'PC休闲发行服务关闭，数字内容访问/付费所有权有迁移点R2，总分5。')
industry('I066','Galaxies展示会愿望单效应',[66],2,2,1,'展示会与独游发现迁移点，数据取自此前4月活动；未达分数线，不将常规下一场活动抬成E3。')
industry('I071','Roblox与阿尔及利亚重新开放及合作',[71],3,3,1,'重要主体R3、合作信号应成卡；但唯一正文为snippet，证据门禁排除，不能据摘要补写正式事实。',entities=['Roblox'])
industry('I072','Drake Star第三季度融资并购统计',[72],2,2,1,'与Aream不是同一机构同一报告，不机械合并；只有snippet且总分5，无完整证据。')
industry('I075','Anzu扩展游戏外广告',[75],3,2,1,'广告业务跨媒介迁移可评分7，但唯一来源snippet，不满足正文证据门槛。')
industry('I082G','Gardens融资回顾',[82],3,3,0,'同一融资历史已曝光；未有最终关账等新增状态，不因本期再次摘要而入选。',entities=['Gardens'],patterns=('社交RPG开发商Gardens',),tracks=('strategy_card_rpg',))
industry('I082R','9月全球手游收入下载结构复述',[82],2,3,0,'双周历史已发同月全球市场结构；改用另一数据机构和补Roblox数字不是市场实质新阶段。',entities=['Roblox','全球手游市场'],patterns=('9月全球手游下载与收入榜',))
industry('I082A','美国App Store游戏ASO采样',[82],2,2,1,'广告代理对9月29日头部样本的商店页采样，移动分发迁移点R2，总分5；不与同稿融资打包。')
industry('I095','Funcom解释单人模式与主机路线',[95],1,3,1,'来源明确腾讯关系；具体开发方向但未有本期新上线/正式定档，不把假设性商业模式当已变更。',entities=['腾讯','Funcom'])
industry('I096','战狗9月22日旧销量文章',[96],2,3,0,'正文明确写于9月22日，125万/200万份属于旧阶段；不与新300万稿冒充同日多源。',tracks=('pvp_competitive',))
industry('I118','GTA6 PC版Q1传闻',[118,152],2,2,2,'跨平台发行有迁移点R2；非官方匿名消息，总分6，正文不把传言写成已定档。')
industry('I124','全面战争幕府将军2完全版更新',[19,124],1,3,1,'既有策略产品完全版更新，不是新品首发；R3但4分，不能把重打包提到E3。',tracks=('strategy_card_rpg',))
industry('I154','关卡设计师Richard Gray去世',[154],1,2,1,'重大人才讣告应独立评估；未证明现任核心管理职位变动，E1，设计人才迁移点R2。')
industry('I165','ARC Raiders PVE测试体验',[165],2,3,0,'既有PVE测试增加体验描述，没有新增可验证生命周期变化；历史已有订阅曝光。',patterns=('ARC Raiders.*2.0',),tracks=('pvp_competitive',))
d=industry('I167','Epic推进堡垒之夜Linux支持',[167],2,3,1,'PVP产品跨平台开发计划，未上线但已明确开发动作；不与AI商店客户端作为同一事件重复。',True,['Epic','堡垒之夜'],tracks=('pvp_competitive',))
publish(d,'Epic推进《堡垒之夜》Linux支持，重点升级反作弊兼容',[
 ('Epic表示正在升级Easy Anti-Cheat，以推动《堡垒之夜》支持Linux，并帮助其他多人游戏进入该平台。',167,'Linux'),
 ('相关工作涉及Linux发行版与反作弊兼容，并不是当前已经可以在Steam Deck直接游玩的上线公告。',167,'Steam Deck'),
 ('Epic称，在新方案获得足够多Linux发行版维护者支持后，将通过Epic Games Launcher引入《堡垒之夜》；目前也正与Valve沟通Steam Deck兼容。',167,'critical mass of distro maintainers')])
industry('I169','魔兽近百万账号封禁标题',[169],2,3,1,'只保留标题和导航，缺实际正文；即使潜在7分也因证据不足排除，不编造反作弊事实。',tracks=('strategy_card_rpg',))
industry('I170','New Blood谈续作与原创方向',[170],1,2,1,'实质战略表态但没有明确本期新项目正式立项/资本动作，3分。')
industry('I177','Roblox巴西创作者活动',[177],0,3,1,'固定最高关注R3，但年度普通活动不是战略合作；E0排除。',entities=['Roblox'])
industry('I236P','Steam胶囊图文字规则',[236],2,2,1,'平台营销规则有全球分发迁移点R2，5分；与Steam不同UI更新、市场数据分成独立事件。')
industry('I236H','Circana美国8月主机硬件统计',[236],2,0,1,'海外区域主机硬件统计未证明移动/国产/竞争格局迁移点，R0。')
industry('I042','1999TOKOYO Building试玩与发售定档',[42,176],3,1,2,'新品试玩E3、同事件多源M2；一般海外恐怖冒险弱迁移点R1，总分5。产品日历按多源优先级另行采用，不跨栏发布。')

# Every remaining industry input is individually recorded (including E0); no I900 bucket.
special = {
 1:(2,2,1,'PC跨平台传言仅标题导语，未能取证，不写作正式定档'), 6:(3,1,0,'昨日产品日历已出现的上线信息，且仅标题导语；不补实际发售日'),
 8:(3,3,1,'新品测试信号与竞技品类，但正文仅复述标题，缺少测试范围等事实，不据标题扩写'),
 10:(3,1,1,'节奏动作新品上线，弱迁移点R1，4分'), 12:(3,3,1,'定档信号非正式上线E2应修正，且全文只有标题和灵感导语'),
 13:(2,3,1,'已存在产品NS2试玩属跨平台节点，但仅标题与存档导语，证据不足'),
 15:(3,3,1,'模拟类Demo上线信号，但仅标题和未来发售导语，无法区分首次测试范围，不扩写'),
 17:(3,3,1,'模拟类试玩信号，但实际只有标题，具体测试事实无法取证'),
 22:(2,1,1,'预购开启非正式上线、首曝，弱迁移点R1'),
 23:(3,3,1,'PVP新品EA信号，标题式会员推广而无实际正文，证据不足'),
 24:(3,3,1,'多人竞技上线信号，但仅抽奖标题与玩法导语，完整发布事实不足，不写厂商和日期'),
 33:(1,3,0,'国产二游十年回顾与历史周年，没有本期新状态'),
 47:(1,2,0,'开放世界多年趋势回顾，无独立本期新事件'),
 48:(1,3,0,'星铁叙事讨论为旧内容回顾，不把采集日当版本日'),
 49:(3,3,0,'逆水寒海外上线材料提到11月，正文年份/时序与当前窗口不符，旧稿隔离'),
 50:(2,3,0,'明确是2025年第三季度常规财报，旧稿且无异常财报例外'),
 51:(1,3,0,'灵犀RO采访在2025年背景，无本窗口新增阶段'),
 52:(2,3,0,'正文明确为2025年ARC Raiders销量，不与2026年PVE事件混为一谈'),
 53:(1,3,0,'国产团队AI开发长篇旧采访，没有可定位的本窗口AI新采用或产品发布变化'),
 54:(2,0,0,'索尼2025年第二季度旧财报及历史减值，不是本期异常财务事件'),
 55:(2,3,0,'网易旧工作室关闭文章时序不符，无法确认本期新关停'),
 56:(1,2,0,'AA制作长期方法访谈，无本窗口确定性战略动作'),
 67:(2,3,1,'Game Finder为S0080完整正文同事件，当前仅snippet，不重复采用'),
 68:(3,2,1,'MCP游戏发布工具信号有迁移点但只有snippet，不能由标题写已落地能力'),
 73:(3,3,1,'AdSurge同事件的摘要/链接，不作为额外独立全文抬高M'),
 77:(1,3,1,'Wooga设计访谈仅snippet，无法核实AI具体新用法'),
 78:(1,2,1,'D2C访谈会议信息仅snippet，不是本期新平台政策'),
 79:(2,3,1,'与S0084同URL停服摘要，不重复计来源或增加M'),
 85:(3,2,1,'Xbox Labs同事件但snippet，不另计多源或重复正文'),
 86:(2,0,1,'区域主机订阅目录无迁移点，且snippet'),
 87:(2,2,1,'RedLynx关闭同事件的snippet，不额外补写'),
 89:(1,2,1,'Rockstar开发周期言论为战略表态且snippet'),
 90:(2,1,1,'ESRB评级不等于跨平台正式官宣，且snippet'),
 93:(3,2,1,'同一EGS预览客户端仅snippet，由完整S0166进入AI'),
 100:(0,3,1,'付费解锁包是普通运营变化；玩家争议只有snippet无法满足社区证据门槛'),
 102:(1,2,1,'Rockstar制作周期表态，snippet不可扩展成研发新状态'),
 103:(3,2,1,'Xbox Labs同事件snippet，由两个完整来源承接'),
 105:(1,2,1,'洛杉矶工作室旧NPC生产经历，不是本期组织新增'),
 106:(2,1,1,'GTA6规模与费用传闻仅snippet，缺可核验动作'),
 108:(2,2,0,'GTA6既有延期回顾，无本期新延期'),
 110:(1,2,0,'GTA6旧制作规模回顾，snippet不足'),
 111:(2,2,1,'GTA6泄露传闻只有snippet，无可用正文和官方状态'),
 112:(2,2,1,'育碧调整snippet且人数口径不同，依据完整61/83，不借此抬R'),
 127:(2,1,1,'舞力全开NS2未来移植，迁移点弱R1，非当前新上线'),
 136:(0,1,1,'GTA6当地宣传/地标讨论，非本期资本或政策动作'),
 141:(3,3,0,'综合稿按10月5至11日回顾，多款首曝已在旧窗口发生；下列产品另列子候选，不能日期回填14日'),
 142:(1,3,0,'综合推荐稿，本期不证明多产品首次官宣；Demo与定档子事件另列'),
 143:(3,3,0,'再再启程10月9日官宣10月23日EA；非14日新首曝，不回填为本日上线'),
 153:(0,3,1,'魔兽测试玩法体验不是新品首次测试'),
 160:(1,2,1,'HelixSR属于非官方超分工具体验，没有明确本期首次发布，非官方兼容与轻微帧率代价不写成主流AI重大进展'),
 161:(1,3,1,'巧克力游戏设计意向只有导航/标题，无有效正文'),
 164:(1,2,1,'Rockstar旧NPC生产经历不是新设组织'),
 }
non_game={3,5,114,129,155,162,163,174}
for row in rows:
    n=int(row['source_id'][1:])
    if n>177 or n in consumed: continue
    if n in special: e,r,m,reason=special[n]
    elif n in non_game: e,r,m,reason=0,0,0,'非游戏行业事件，人物娱乐/通用科技/影视内容'
    else:
        r=3 if any(w in row['text'] for w in ['腾讯','网易','米哈游','王者','鸣潮','崩坏','原神','Riot','拳头','Supercell','Roblox','MMORPG','RPG','魔兽','格斗']) else 1
        e,m,reason=0,1,'逐篇阅读后判定为普通版本/活动/联动/后续PV、攻略、纯榜单、历史回顾或例行宣传；无本窗口独立商业状态'
    if n==12: e=2
    industry(f'I{n:03d}',row['title'],[n],e,r,m,reason)

# Multi-event digests explicitly split, including disqualified older events.
for suffix,product,date,reason in [
 ('M','Machinarium 2','2026-10-09','Triple-I首次曝光在10月9日旧窗口'),
 ('E','The Escapists 3','2026-10-09','已有10月9日展示会首曝，不能把14日回顾当新立项'),
 ('G','新神纪','2026-10-09','既有RPG首曝旧窗口'),
 ('U','Ultima','2026-10-10','IP权利收回消息在旧窗口，不用回顾稿再造14日动作')]:
    industry('I141'+suffix,product+'旧窗口事件',[141],3,3 if suffix in 'MGU' else 2,0,reason)
for suffix,product,e,r,reason in [
 ('J','江湖一牌',2,3,'公布11月12日EA时间的单源推荐条目，非正式新品上线；无新鲜度钩子总分6，留日历单源审计'),
 ('L','梁山叠义',3,3,'仅描述已存在Demo，未证明14日首次测试；不把当前推荐当首次测试'),
 ('D','My Desktop Dwarf / Taskbar Forge',3,3,'Demo存在信号但未证明本日首次测试，单源不足'),
 ('A','囚偶AI重制',1,3,'只有开发日记推荐摘要，无法提取可验证本期AI发布状态')]:
    industry('I142'+suffix,product,[142],e,r,0,reason)

# Rejected AI candidates retain tier/migration explanation rather than vanishing.
ai('A028','Epic AI优先射击项目旧报道',[28],False,'10月13日报已写同一项目与AI优先开发，14日换源补背景无新状态。')
ai('A188','vLLM自适应验证在线估计器',[188],False,'完整技术证据可迁移高并发NPC推理，但本期无游戏部署证据，较直接游戏应用及前沿交互优先级低，不以技术细节堆满日报。',tier='transferable_frontier',reverse=False,migration='无置信头草稿模型自适应验证→自托管NPC对话推理→可能优化高并发算力；效果依后端与负载而异')
ai('A189','Deep Review公开技术文档审阅',[189],False,'技术文档一致性审阅可迁移，但属于较间接设计文档工具；本期优先游戏直接应用与明确新交互/资产处理变化。',tier='transferable_frontier',reverse=False,migration='跨章节一致性核查→游戏设计/技术文档评审→减少人工核查负担，但没有游戏实际案例')
ai('A192','AI辅助大型代码库维护方法',[192],False,'维护工作流案例可迁移但非新游戏业务落地，优先级低于本期游戏公司管线与公开新能力；不复用通用案例当游戏实绩。',tier='transferable_frontier',reverse=False,migration='证据驱动死代码和实验开关清理→游戏工具及服务代码维护→可能减少构建与CI成本，必须人工复核')
ai('A193','Databricks微调效率教程',[193],False,'优化方法可迁移，但单一Qwen训练配置的6倍结果不是通用游戏效率变化，技术教程不因倍数高自动入选。',tier='transferable_frontier',reverse=False,migration='融合内核及样本打包→游戏角色专用模型微调→可能降低训练时间，收益依GPU/版本/数据分布')
for n,reason in {
 182:'办公室窃听调查，不是游戏采用或可验证迁移能力变化',
 183:'榜单名次与新旧模型比较，未证明游戏环节新能力，不因跑分热度收录',
 184:'通用IDE安全补丁披露，没有本期游戏业务后果；不扩写为游戏事故',
 185:'实测只有摘要式聚合页，且不作与发布同一事件的独立新闻',
 186:'一般基础设施融资，无明确新增游戏迁移能力，融资规模不替代门槛',
 190:'正文只有外链与导读，没有实测全文，不能采用作者结论',
 191:'Chrome漏洞赏金与通用安全研究，没有具体游戏迁移链条',
 194:'增长工具导语截断，缺广告执行边界与游戏案例，不编写投放能力',
 195:'天气预报研究，没有游戏研发或产品的明确迁移路径',
 196:'UEFN培训推广不等于AI采用事件'
}.items():
    ai(f'A{n:03d}',inputs[sid(n)]['title'],[n],False,reason,tier='transferable_frontier',reverse=False)

# Player discourse: two new, attributable triggers, only replies inside October 14.
for n,title,triples,logic in [
 (230,'《终末地》玩家称装Mod被长期封号，争议转向修改边界',[
 ('《终末地》玩家10月14日在NGA声称使用Mod后被封80年，讨论随即围绕模型替换与修改游戏内存的界线展开。',230,'终末地打Mod玩家被封80年'),
  ('一部分玩家认为使用非官方修改就应自行承担封禁风险；另一部分强调普通模型Mod与涉及内存修改的工具不能混称，反对把后者包装成无害外观修改。',230,'普通MOD依然正常使用'),
 ('争议集中在是否应区分普通外观替换和触碰反作弊的修改行为，部分玩家则主张任何非官方修改都应自行承担风险。',230,'改了游戏内存')],
  '风险自担立场与区分模型替换/内存工具立场；禁止将玩家关于付费与处罚关系的说法写成事实'),
 (231,'《异环》宣发图AI水印引发质疑，讨论分歧集中于渠道加工',[
 ('《异环》在TapTap的新版本宣发图被NGA玩家指出带有豆包AI水印，10月14日发帖者随后标注图片已经替换、没有水印。',231,'图片已更新替换'),
  ('有玩家据此质疑素材制作与审核，也有玩家对比B站版本后，推测是渠道运营对画质或色调做了AI处理。',231,'感觉色调光影有点区别'),
 ('玩家讨论集中在同一画面为何在不同平台呈现差异，以及去除UI、调色和画质处理为何还要借助AI，素材加工方式成为争议焦点。',231,'调色也要用豆包吗')],
  '素材审核质疑与渠道修图解释并存；原始图制作方式及责任主体均未获官方证实')]:
    row=inputs[sid(n)]
    c={'trigger':triples[0][0], 'claim_scope':'玩家帖与14日回复的观点，不作官方政策或AI制作事实', 'complaint_logic':logic,
       'timeline':['2026-10-14 首帖触发','2026-10-14 窗口内跟帖形成分歧；10月15日回复不使用'],
       'follow_up_scan':'已检查本期20条社区输入及行业输入；没有同事件官方确认、处罚细则或制作归因的新材料；未拿其他游戏旧帖合并'}
    d={'candidate_id':f'C{n}','section':'community_discourse','source_ids':[sid(n)],'entities':[title], 'event':title,'decision':'include','reason':'本窗口新触发、明确游戏归属、两方解释与跟进可读；按硬上限只选两条','community':c}
    decisions.append(d); publish(d,title,triples,{'community':c})
for n in range(216,236):
    if n in [230,231]: continue
    reasons={216:'2024年日常水楼，非事件',217:'旧明日方舟AI文字争议；14日摘录已漂移到其他游戏，不能混写',218:'9月旧争议延续，未定位本日实质进展',219:'纯网吧榜单讨论，不以热度作为事件',220:'Steam档期旧帖，14日主要阵营争吵，无可取证新官方变化',221:'此前已写歌词争议，窗口内无实质新进展',222:'Mod帖首发12日，主体不明且靠猜公司，不与230硬并',223:'9月代码争议旧帖，14日回复无新官方材料',224:'用户估算日活旧帖，不写成官方420万',225:'诡秘聚会旧争议已写，无本期新进展',226:'AI复活传闻旧帖，缺可核验新产品动作',227:'错别字与删帖猜测，缺清晰新产品/业务触发',228:'库洛投资事实已行业收录，不同栏重复事件',229:'10月4日AI美术旧帖，无14日新动作',232:'艾希众筹旧节点继续争论，无本期新状态',233:'普通联动及日常玩笑，非实质舆论事件',234:'成人二创控制传闻主体和证据不清，且最新回复越窗',235:'暗区少女前线普通联动旧帖，无本期实质进展'}
    decisions.append({'candidate_id':f'C{n}','section':'community_discourse','source_ids':[sid(n)],'entities':[inputs[sid(n)]['title']],'event':inputs[sid(n)]['title'],'decision':'exclude','reason':reasons[n]})

d={'candidate_id':'D236','section':'deep_analysis','source_ids':['S0236'],'entities':['GameDiscoverCo','ReStory','Sandustry','Combolands'],
   'event':'8月Steam新品长尾在线与产品循环机制','decision':'include','reason':'优先配置的GameDiscoverCo原始分析，含数据、多个独立机制与边界；不复述行业已写Survival Log，不将三七普通报道拔高为深度',
   'scores':{'relevance':3,'insight':3,'evidence':3,'card':3,'total':12}}
decisions.append(d)
publish(d,'Steam新品的长尾在线：明确题材、即时反馈与可扩展系统',[
 ('观察：GameDiscoverCo的Simon Carless复盘8月Steam新品在10月中旬的在线表现。其估算，电子维修经营游戏《ReStory》含站外Key销量超过60万份，Steam毛收入超过1000万美元，当前在线约为峰值的15%；工厂自动化游戏《Sandustry》销量约30万份，仍维持较高在线；肉鸽城建游戏《Combolands》销量不足10万份，但当前在线保持在2000多峰值的50%以上。',236,'ReStory ($20)'),
 ('分析：这些产品并非共享同一套内容量或美术规格。《ReStory》把怀旧电子设备的明确题材与“再接一单”的即时完成感连接；《Sandustry》则让采掘、分离和副产物处理不断生成新的生产链问题。前者靠短周期任务反馈，后者靠系统组合持续拓展目标，二者都使玩家在一次游玩结束前看见下一个可完成的动作。',236,'system and physics-based automation'),
 ('《Combolands》把资源选择、商店调整与结果反馈装进更短的肉鸽局次，为传统慢节奏城建提供了另一种时间结构。长尾在线因此更像题材承诺、单次反馈和系统可扩展性共同作用的结果，而不是单纯靠持续堆叠内容；但买断制有限流程游戏可以在低在线下继续产生销售，不能把CCU比例直接等同于商业成功率或用户留存率。',236,'concurrent users a few weeks after launch is the only arbiter')],
 {'card_copy':{'source_label':'GameDiscoverCo / Simon Carless 分析','summary':'长尾在线由清晰题材、短周期反馈和系统可扩展性共同支撑，不能单用CCU衡量买断制成败。',
 'insights':[{'title':'题材与任务闭环','detail':'《ReStory》把怀旧电子维修与“再接一单”的即时完成感结合。'},
 {'title':'系统不断生成目标','detail':'《Sandustry》通过采掘、加工与副产物处理延长生产链探索。'},
 {'title':'复杂类型缩短局次','detail':'《Combolands》用肉鸽局次包装城建决策，当前在线仍超过峰值的一半。'},
 {'title':'在线不是收入替代物','detail':'有限流程买断游戏即使在线下降，仍可能继续积累销量。'}]}},join='\n\n')

# Link duplicate coverage to its event; snippet records stay out of published source sets.
merge_targets={'I001':'I118','I067':'A080','I073':'I081','I079':'I084','I085':'I059','I087':'I061','I093':'A166','I103':'I059','I105':'I164','I112':'I061','A190':'A185'}
for decision in decisions:
    if decision['candidate_id'] in merge_targets:
        decision['decision']='merge';decision['merge_into']=merge_targets[decision['candidate_id']]
        decision['reason']='同一主体/产品、同一日期、同一事件的重复覆盖；'+decision['reason']
        if decision['candidate_id'] in {'I067','I093'}:
            decision.update(section='ai_trends',ai_tier='direct_application',game_stage=['publishing'],industry_reverse_scan=True)

# Calendar audit: preserve extractor recall, correct dates/types, and append missed nodes.
raw_audit_path=MID/'release_calendar_audit_raw.json'
if not raw_audit_path.exists():
    dump(raw_audit_path,json.loads((MID/'release_calendar_audit.json').read_text(encoding='utf-8')))
audit=json.loads(raw_audit_path.read_text(encoding='utf-8'))
nodes=audit['nodes']
bad={3:'Disney Solitaire是融资稿中的历史案例，无本日上线',4:'5800万DAU公告不是上线',5:'正文只写约8月上线，不能回填采集日期',6:'扶摇一梦明确2023年11月上线，历史背景',7:'11月是DLSS技术计划而非新游测试',8:'GTA6 PC版是2027Q1传闻，不是本期上线',9:'疯狂出租车只是地图详情，不是新品上线',18:'影之刃零是后续试玩/PV与既有10月29日档期',19:'山寨案例为历史市场背景',20:'旧产品背景，非本日新游',21:'流放者柯南仅旧业务背景',23:'王者万象棋已经上线一月，14日是表现报道',25:'堡垒之夜在旧项目稿中不是新品定档',26:'一千克拉女王是2020年12月旧背景',27:'那个游戏6是硬件配色文章梗，不是产品定档',28:'绝地潜兵战债为普通运营内容',29:'芭比是影视旧片，不是新游戏',30:'GTA3是旧封面设计回顾，不是当期定档'}
for node in nodes:
    num=int(node['candidate_id'].split('-')[-1])
    node['editorial_review']='逐源核对日期与事件，非机械采用发布时间'
    if num in bad:
        node.update(event_date='',window_eligible=False,window_scope='outside_window',publish_eligible=False,editorial_exclusion_reason=bad[num])
    if num in {1,10,11,12,13,14,15,22,40,41}:
        node.update(event_date='',window_eligible=False,window_scope='outside_window',publish_eligible=False,
                    editorial_exclusion_reason='只有“现已”等状态、缺实际事件日期；不补成14日。行业已采用的新品不跨栏重复' if num in {1,13} else '无法确认实际发生日，或仅标题式导语；不将采集日期当事件日')
    if num==12: node.update(signal_type='new_game_test',event='试玩版上线',event_type_score=3)
    if num==14: node.update(signal_type='new_game_test',event='试玩版上线',event_type_score=3)
    if num in {15,22}: node.update(signal_type='old_major_update',event='完全版重大更新',event_type_score=1)
    if num==2:
        node['source_ids'].append('S0214'); node['release_ids']=['S0214']; node['source_fingerprints'].append(inputs['S0214']['sha1'])
        node['appearance_count']=3; node['coverage']='both'; node['coverage_rank']=3
        node['product']='1999TOKOYO Building'
        node['event']='11月10日发售定档及本日试玩版发布'
        node['observed_signal_types']=['new_game_schedule','new_game_test']; node['observed_events']=['11月10日定档','试玩版今日发布']
        node['event_type_score']=3;node['signal_type']='new_game_test'
        node['editorial_review']='S0214明确Announcement date=2026-10-14，42/176这份14日新闻稿明确“今日”Demo（非3839，按正常发布时间解释）；同产品同日合一节点，取当日新品试玩类型3分，未来正式发售日仍保留11月10日'
    if num in {37,38,39}:
        node['signal_type']='new_game_preload'; node['event']='预下载开启';node['event_type_score']=2
        node['editorial_review']='源正文含14日预下载；不把同文15日测试/上线再拆成14日定档'

def add_calendar(product,n,event,signal,score,date='2026-10-14',eligible=True,note='单源，留审计不发布'):
    sources=[n] if isinstance(n,int) else n
    count=len({(inputs[sid(x)]['url'],inputs[sid(x)]['sha1']) for x in sources})
    industryids=[sid(x) for x in sources if inputs[sid(x)]['section']=='industry_news']
    base={'candidate_id':f'release-manual-{len(nodes)+1:03d}','product':product,'event_date':date,'event':event,'signal_type':signal,'event_type_score':score,
          'first_seen_order':200+len(nodes),'observed_signal_types':[signal],'observed_events':[event], 'industry_ids':industryids,
          'release_ids':[sid(x) for x in sources if inputs[sid(x)]['section']=='release_calendar'], 'source_ids':[sid(x) for x in sources],
          'source_fingerprints':[inputs[sid(x)]['sha1'] for x in sources], 'appearance_count':count,'focus_companies':[], 'focus_company_relationships':{},
          'company_evidence_ids':[],'company_bonus':0,'company_relationship':'none','multi_source_eligible':count>=2,
          'window_eligible':eligible,'window_scope':'report_window' if eligible else 'outside_window','publish_eligible':False,'status':'pending_decision',
          'coverage':'industry_only' if industryids else 'release_only','coverage_rank':2 if industryids else 1,'editorial_exclusion_reason':note}
    nodes.append(base)
    return base

# Merge known aliases, retain original recall nodes and explicit merge audit.
valor=next(x for x in nodes if x['candidate_id']=='release-candidate-013')
valor['source_ids'].append('S0126');valor['industry_ids'].append('S0126');valor['source_fingerprints'].append(inputs['S0126']['sha1']);valor['appearance_count']=2
shogun=next(x for x in nodes if x['candidate_id']=='release-candidate-015')
other=next(x for x in nodes if x['candidate_id']=='release-candidate-022')
shogun['source_ids']+=other['source_ids'];shogun['industry_ids']+=other['industry_ids'];shogun['source_fingerprints']+=other['source_fingerprints'];shogun['appearance_count']=2
other['editorial_exclusion_reason']='同产品别名合并至release-candidate-015；不是新品正式发售'
other['alias_merge_into']='release-candidate-015'
for n in range(206,216):
    if n==214: continue
    row=inputs[sid(n)]; title=row['title']; text=row['text']
    product=title.split(' launches')[0].split(' launch')[0].split(' dated')[0]
    add_calendar(product,n,'首次公开发售定档','new_game_schedule',2)
for product,n,typ,score,note in [
 ('暗喻幻想：ReFantazio NS2',13,'old_cross_platform_launch',1,'单源试玩；不等同新品首发'),
 ('地铁2039',22,'new_game_schedule',2,'预购开启没有首次定档证据，亦单源'),
 ('江湖一牌',142,'new_game_schedule',2,'推荐稿明确11月12日EA但单源'),
 ('梁山叠义',142,'new_game_test',3,'Demo已存在，未证明窗口内首次测试'),
 ('My Desktop Dwarf / Taskbar Forge',142,'new_game_test',3,'只有现已Demo，实际事件日未知'),
 ('米塔移动版',30,'new_game_test',3,'最近招募无具体日，且单源'),
 ('师父iOS',30,'old_cross_platform_launch',1,'单源跨平台业务稿，无明确实际迁移日'),
 ('无人深空iOS',30,'old_cross_platform_launch',1,'单源且原事件已被行业汇总，不跨栏重复'),
 ('吸血鬼爬行者iOS',30,'old_cross_platform_launch',1,'单源，无明确实际迁移日'),
 ('九王iOS',30,'old_cross_platform_launch',1,'单源，无明确实际迁移日'),
 ('Machinarium 2',141,'new_game_reveal',2,'首次曝光在10月9日，旧窗口'),
 ('The Escapists 3',141,'new_game_reveal',2,'旧窗口展示会首曝'),
 ('新神纪',141,'new_game_reveal',2,'旧窗口首曝')]:
    add_calendar(product,n,'召回后人工核对','new_game_schedule' if typ=='new_game_reveal' else typ,score,date='',eligible=False,note=note)
for node in nodes:
    count=node['appearance_count']; node['appearance_score']=min(count,3); node['industry_bonus']=int(bool(node['industry_ids']))
    node['source_strength_score']=node['appearance_score']+node['industry_bonus']
    node['base_priority_score']=node['event_type_score']*node['source_strength_score'];node['priority_score']=node['base_priority_score']+node['company_bonus']
    node['multi_source_eligible']=count>=2
    node['publish_eligible']=count>=2 and node['window_eligible']
    date=node['event_date']
    node['window_scope']=('report_window' if '2026-10-14'<=date<='2026-10-14' else 'next_day_lookahead' if '2026-10-14'<date<='2026-10-15' else 'future_announcement' if node['signal_type'] in {'new_game_schedule','new_game_first_reveal'} else 'outside')
nodes.sort(key=lambda x:(-int(x['publish_eligible']),-x['priority_score'],-x['company_bonus'],-x['event_type_score'],-x['appearance_count'],-x['industry_bonus'],x['first_seen_order']))
audit['nodes']=nodes
dump(MID/'release_calendar_audit.json',audit)

# Write human audit before structured artifacts and report, as required.
def human_audit():
    cards=['# 独立事件候选｜日报2026-10-14','','全量236条：行业177、AI19、日历19、社区20、深度1。逐事件复核，不沿用早报结论。','']
    for d in decisions:
        if d['section']=='release_calendar': continue
        cards += [f"## {d['candidate_id']} — {d['event']}",f"- section: {d['section']}",'- status: candidate',f"- source_ids: {', '.join(d['source_ids'])}",f"- entities: {', '.join(d['entities'])}",'- event_date: 来源正文优先；不以采集日期填补未明事件日',f"- facts: {d['reason']}"]
        if 'cluster_basis' in d: cards.append('- cluster_basis: '+json.dumps(d['cluster_basis'],ensure_ascii=False))
        if 'community' in d:
            cards.extend('- '+k+': '+str(v) for k,v in d['community'].items())
        cards.append('')
    for n in nodes:
        cards += [f"## {n['candidate_id']} — {n['product']} {n['event']}",'- section: release_calendar','- status: candidate',f"- source_ids: {', '.join(n['source_ids'])}",f"- event_date: {n['event_date'] or '未知/历史或非事件，禁止填补'}",f"- facts: {n.get('editorial_exclusion_reason') or n.get('editorial_review','源正文显式档期')}",'']
    (MID/'event_candidates.md').write_text('\n'.join(cards),encoding='utf-8')
    industry_decisions=[d for d in decisions if d['section']=='industry_news']
    dimensions={'国内移动':r'腾讯|网易|三七|库洛|游族|米哈游|莉莉丝|灵犀|王者|国产|中国|朝夕|虎牙|Anbernic',
      '国产产品与人才':r'国产|中国|人才|主创|开发者|制作人|刘胜|库洛|三七|逆水寒|三角洲|明日方舟|影之刃|王者',
      '市场数据':r'数据|销量|收入|IAP|DAU|用户|经营表现|统计|ASO|愿望单',
      '并购':r'融资|入股|收购|投资|并购|资本', '平台政策':r'规则|政策|反作弊|披露|名单|监管|平台|Steam|iOS|Game Finder',
      '档期变动':r'发售|测试|延期|停运|停服|跨平台|上线|定档|取消|关停|关闭|EA',
      '资本组织':r'融资|股权|入股|董事|Labs|工作室|裁员|部门|组织|管理|员工',
      '海外重大':r'Xbox|Epic|育碧|RedLynx|Flow|Spill|Supercell|Roblox|Rockstar|ESA|Steam|GTA|Anzu|Legacy|Gardens'}
    dimension_counts={name:sum(bool(re.search(pattern,d['event']+' '+d['reason'],re.I)) for d in industry_decisions) for name,pattern in dimensions.items()}
    lines=['# 选用决策｜日报2026-10-14','','卡片曝光去重：历史窗口2026-09-30至2026-10-13；71次历史条目，逐条读取card_exposed/card_rank/card_limit/card_exposure_source。已有曝光的重复事件不入选；本期无合格card_carryover，无material_update，未伪造新增事实。',
           '维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已对全量行业177条与综合稿子事件成卡审计；独立事件不放入低信号打包项。具体计数见下表。',
           '维度召回卡计数（可交叉，按事件/原因中的主体与信号标签检索，不是各分区入选数）：'+ '；'.join(f'{k} {v}张' for k,v in dimension_counts.items())+'。',
           '重建说明：未读取早报report_items/decisions作为筛选依据；保留原始抽取日历审计，修正历史月份回填及普通活动误召回。三七互娱产品表现独立评分，不作为深度。',
           '日期门禁：8月上线、2023年上线等不填成10月14日；报道日期只用于已明确的公告，不替代实际发售日。',
           '产品日历漏挂反查：完整扫描行业177条及日历19条；保留44个机器召回节点并增补22个节点，共66个。历史事件、普通内容、实际日期未明、别名合并、单源节点均有显式exclude；唯一合格多源优先前缀为1999TOKOYO Building。',
           '行业新闻 E×R+M 打分：事件E×相关R+钩子M = 终分，E=0排除，日报终分≥7；证据与时效门禁独立，按终分降序，无条数上限。',
           '来源警告：抽取失败0、空正文0；38条snippet或短摘要不作为最终证据。部分full标记记录只有标题导语，另行证据门禁排除。部分翻译长稿含2025年旧事，未视为新事件。',
           '采集覆盖警告：采集审计有4个failed源（dataeye_36kr、nadianshi、cubox、wanjiang_16p_newgame），pocketgamer/vgc为degraded。抽取0失败只描述已落库236条，不等于所有采集源健康；未联网补库。',
           'AI数量说明：5条直接游戏应用（游族管线、不问凡尘、Epic客户端、Google Play发现、DLSS模型）+3条有明确迁移链的新能力（Argon开放、实时语音、ComfyUI后期节点）。8条超过1–3软目标，但不按条数硬截合格信号；不保留一般融资、纯跑分或无正文实测。',
           '深度交接：星期四日报，不执行周五飞书回执流程；只使用当日优先来源分析，不读取用户周报selection。','',
           '| candidate | decision | section | score | reason/history |','| --- | --- | --- | --- | --- |']
    for d in decisions:
        score=d.get('scores',{}); scoretext=(f"事件{score['event']}×相关{score['relevance']}+钩子{score['hook']} = {score['total']}" if 'relevance' in score and 'hook' in score else json.dumps(score,ensure_ascii=False)) if score else d.get('ai_tier','-')
        reason=d['reason']
        if 'history_check' in d: reason+='；'+json.dumps(d['history_check'],ensure_ascii=False)
        lines.append(f"| {d['candidate_id']} | {d['decision']} | {d['section']} | {scoretext} | {reason.replace('|',' / ')} |")
    (MID/'selection_decisions.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
human_audit()
dump(MID/'report_items.json',{'items':[{k:v for k,v in item.items() if k!='body'} for item in items]})
dump(MID/'selection_decisions.json',{'decisions':decisions})
sync(MID/'release_calendar_audit.json',MID/'selection_decisions.json',4)
synced=json.loads((MID/'selection_decisions.json').read_text(encoding='utf-8'))['decisions']
by_node={n['candidate_id']:n for n in nodes}
for d in synced:
    if d['section']=='release_calendar' and by_node[d['candidate_id']].get('editorial_exclusion_reason'):
        d['reason']=by_node[d['candidate_id']]['editorial_exclusion_reason']
    if d['section']=='release_calendar' and len(d['source_ids'])>1 and not d.get('cluster_basis',{}).get('event_date'):
        d['cluster_basis']['event_date']='实际日期未明，原抽取误按2026-10-14归并；仅保留排除审计，不作发布聚类'
dump(MID/'selection_decisions.json',{'decisions':synced})
decisions=synced
human_audit()
cal=next(d for d in decisions if d['section']=='release_calendar' and d['decision']=='include')
publish(cal,'1999TOKOYO Building',[
 ('讲谈社发行、常夜不动产开发的恐怖冒险端游《1999TOKOYO Building》于10月14日宣布定档11月10日在Steam发售，并发布免费试玩版；试玩收录第一章，约两小时，结合房间探索与选项式对话。',42,'确定于2026年11月10日'),
],{'release':{'product':'1999TOKOYO Building','event':'11月10日发售定档及本日试玩版发布','date':'2026-10-14','platform':'Steam','company':'讲谈社 / 常夜不动产'}})
# Explicit date evidence from structured announcement, and developer/genre from complete text.
items[-1]['claims'].extend([
 {'claim':'于10月14日宣布','source_id':'S0214','evidence':evidence(214,'Announcement date: 2026-10-14')},
 {'claim':'常夜不动产开发','source_id':'S0042','evidence':evidence(42,'开发者：常夜不动产')},
 {'claim':'试玩收录第一章，约两小时','source_id':'S0042','evidence':evidence(42,'试玩版完整收录第一章')},
 {'claim':'结合房间探索与选项式对话','source_id':'S0042','evidence':evidence(42,'两种环节交替推进')},
])
dump(MID/'report_items.json',{'items':[{k:v for k,v in item.items() if k!='body'} for item in items]})

# Add separate exact excerpts for multi-clause claims, rather than letting one quote
# stand in for a different paragraph. All fragments below must occur in the body.
extra_support={
 'I032':[('3D角色驱动系统“元语TalkiVerse”',38,'二是3D角色驱动系统')],
 'I034':[('土耳其游戏工作室',34,'土耳其')],
 'I081':[('广告回报、净广告收益、玩家体验和SDK表现',81,'ROAS')],
 'I059':[('不是新增大规模招聘',59,'No new staff')],
 'I058':[('穿越到原剧场景中的宫女',58,'碎玉轩的小宫女'),('“送真花”与番外卡牌、好友互助',58,'送真花')],
 'I084':[('已安装玩家可继续游玩至停服日',84,'players who already have the game installed')],
 'I236S':[('更偏重资源整理、建造与管理',236,'heavy on the building & arranging')],
 'A026':[('10月11日',26,'10月11日'),('Skill Hub',26,'Skill Hub技能商店'),('战斗伤害仍由确定性逻辑结算',26,'数值计算的伤害'),('世界设定',26,'第一层是世界设定层'),('任务规划',26,'第二步要做好任务的规划'),('多模态协同',26,'第三步非常关键'),('知识库与自动评估',26,'第五点，也是最后一个')],
 'A057':[('朝夕光年旗下',57,'朝夕光年江南工作室')],
 'A166':[('Martin Keely',166,'Martin Keely'),('AI编写和审查新功能代码',166,'write and review new features')],
 'A133':[('《燕云十六声》也在后续支持名单',173,'Where Winds Meet')],
 'D236':[('Steam毛收入超过1000万美元',236,'likely >$10m gross'),('当前在线约为峰值的15%',236,'~15% of peak'),('《Sandustry》销量约30万份',236,'~300k sold'),('《Combolands》销量不足10万份',236,'100k sold'),('峰值的50%以上',236,'>50% of its peak'),('“再接一单”的即时完成感',236,'just one more job'),('资源选择、商店调整与结果反馈',236,'go to a shop')],
}
for item in items:
    if item['candidate_id']=='A026': item['title']='游族披露“AI红岸”管线，覆盖策划、资产与质检环节'
    for fragment,n,needle in extra_support.get(item['candidate_id'],[]):
        assert fragment in item['body'], (item['candidate_id'],fragment)
        item['claims'].append({'claim':fragment,'source_id':sid(n),'evidence':evidence(n,needle)})
dump(MID/'report_items.json',{'items':[{k:v for k,v in item.items() if k!='body'} for item in items]})

score_by={d['candidate_id']:d.get('scores',{}).get('total',0) for d in decisions}
headings=[('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]
report=['# 游戏行业日报｜2026-10-14','','覆盖日期：2026年10月14日（Asia/Shanghai）。','']
for sec,heading in headings:
    report.extend(['## '+heading,''])
    group=[item for item in items if item['section']==sec]
    if sec=='industry_news': group.sort(key=lambda x:-score_by[x['candidate_id']])
    for i,item in enumerate(group,1):
        if sec=='release_calendar': report+=['- '+item['body'],'']
        else: report += [f"### {i}. {item['title']}",'',item['body'],'']
(ROOT/'game_industry_daily_2026-10-14.md').write_text('\n'.join(report),encoding='utf-8')
print('sections', {sec:sum(x['section']==sec for x in items) for sec,_ in headings})
print('decisions',len(decisions),'calendar_nodes',len(nodes))
