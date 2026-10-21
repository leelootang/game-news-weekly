import json,re,shutil,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
raw=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));D=raw['decisions'];DM={x['candidate_id']:x for x in D}
for d in D:
    if d['candidate_id'].startswith('J_') and d['decision']=='include' and d['candidate_id']!='J_MARKET':
        d['score_revision']='复核：截至8日存量在研线索，原先按首曝E3缺少直接证据，改E1；逐项目候选保留，不合并产品。'
        d.update(decision='exclude',scores=dict(event=1,relevance=3,hook=1,total=4),reason='截至10月8日的岗位/在研方向，原文未证明本期首曝、立项或实际状态变化；E1R3M1=4。')
if 'J_MARKET' not in DM:
    survey=dict(candidate_id='J_MARKET',section='industry_news',source_ids=['S0050'],entities=['中国游戏社招市场'],event='游戏陀螺披露截至10月8日近60家游戏公司社招调查',event_date='2026-10-20',decision='include',reason='本期国内研发人才市场调查，有样本、统计时点、总量和需求结构；E2R3M1=7。单一调查事件，不把在研项目合并为产品首曝。',scores=dict(event=2,relevance=3,hook=1,total=7),history_check=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None),observation_as_of='2026-10-08')
    D.append(survey);DM['J_MARKET']=survey
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sid(i):return f'S{i:04}' if isinstance(i,int) else i
def proof(i,needle):
    text=S[sid(i)]['text'];assert needle in text,(i,needle)
    return next(l for l in text.splitlines() if needle in l)
def cl(t,i,n):return dict(claim=t,source_id=sid(i),evidence=proof(i,n))
items=[]
def item(cid,title,triples,body=None,**kw):
    d=DM[cid];claims=[cl(*v) for v in triples]
    it=dict(section=d['section'],title=title,candidate_id=cid,source_ids=list(dict.fromkeys(d['source_ids']+[c['source_id'] for c in claims])),claims=claims,body=body if body is not None else ''.join(t[0] for t in triples));it.update(kw);items.append(it);return it
# All selected recruiting claims retain the original snapshot date.
item('I051','创梦天地与南山区国资共同发起2亿元游戏产业战略投资',[
('创梦天地与深圳市南山战略新兴产业投资有限公司达成战略合作，双方将共同发起总规模2亿元的游戏产业战略投资。',51,'总规模2亿元'),
('投资落地于南山区官方游戏产业孵化平台游托邦，重点投向入驻的本地游戏项目，覆盖研发、AI内容生产、发行服务与产业链配套。',51,'覆盖游戏研发'),
('双方还将支持创梦天地发行业务，围绕已储备的海外产品与发行企业拓展进口游戏发行。',51,'加速进口游戏发行业务拓展')])
items[-1]['claims'].append(cl('投资落地于南山区官方游戏产业孵化平台游托邦',51,'南山区官方游戏产业孵化平台'))
item('I071','猩球游戏建立广州发行分部，《弹壳战机》首月内购收入估算超百万美元',[
('《弹壳特攻队》研发商猩球游戏宣布入驻广州天河区狮子文化园，广州团队主要负责发行，已开放买量素材设计师岗位。',71,'广州团队主要负责发行'),
('公司多数产品由Habby发行，9月20日上线的《弹壳战机》则采用自研自发。',71,'今年9月20日上线'),
('据AppMagic估算，该作首月收入超过100万美元，最高到达中国iOS畅销榜第58名；这一收入估算仅含内购。',71,'首月收入超100万美元')])
for t,n in [('猩球游戏宣布入驻广州天河区狮子文化园','猩球游戏宣布入驻广州市天河区'),('仅含内购','该数据仅估算了iap部分')]:items[-1]['claims'].append(cl(t,71,n))
item('I049','京东成立全资公司，经营范围纳入游戏开发与服务',[
('10月13日，北京京玩互娱网络科技有限公司成立，由京东全资持股。',49,'10月13日'),
('公司经营范围同时出现动漫游戏开发、互联网游戏服务等业务。',49,'动漫游戏开发、互联网游戏服务')])
J=[
('J_RAID','光子《RAID PROJECT》招聘披露UE5战术射击方向',[
('游戏陀螺10月20日发布的招聘梳理显示，光子工作室群为《RAID PROJECT》招募UE5引擎、场景、动画与关卡等岗位。','光子工作室群前不久'),
('招聘定位明确写有“现代战争超写实战术射击”和“光子原创IP”。','现代战争超写实战术射击'),
('该篇岗位统计截至10月8日，所呈现的是在研方向与人员需求。','数据截至10月8日')]),
('J_HIGAME','光子H.STUDIO招募《Higame》开放世界RPG团队',[
('游戏陀螺的招聘梳理显示，光子旗下H.STUDIO正为《Higame》密集招聘。','H.STUDIO'),
('项目定位为“人与怪谈共存”的风格化写实开放世界RPG，岗位涉及3A级开放世界玩法、关卡、任务、剧情与3C策划，以及场景、角色和动画制作。','人与怪谈共存'),
('报道的岗位统计截至10月8日。','数据截至10月8日')]),
('J_MHY_ACTION','米哈游UE5动作预研指向写实奇幻与多人战斗',[
('游戏陀螺对截至10月8日招聘信息的梳理，列出米哈游尚未曝光的UE5动作预研。','数据截至10月8日'),
('这款动作冒险项目采用写实奇幻风格，包含超大型Boss战、多人对抗和联机合作玩法。','超大型Boss战'),
('美术招聘同时强调造型、节奏、质感与性能判断。','造型美感、节奏变化、质感、性能')]),
('J_MHY_MMO','米哈游生活MMO预研以多剧本与社交模拟为核心',[
('游戏陀螺在截至10月8日的招聘梳理中，列出米哈游的生活MMO预研项目。','数据截至10月8日'),
('项目以多剧本角色扮演和社交模拟为核心，强调自我养成与社交构筑。','多剧本角色扮演和社交模拟'),
('岗位描述关注多人同屏下的高自由度捏人、换装和角色表现。','多人同屏下的高自由度')]),
('J_MHY_SHOOTER','米哈游写实射击预研招募大规模玩家生态与实时战斗能力',[
('游戏陀螺的招聘梳理列出米哈游一款UE5写实射击预研。','米哈游还有一款UE5写实射击'),
('其服务端岗位描述写有“大规模玩家生态+低延迟强实时战斗”，指向实时对抗和玩家生态。','大规模玩家生态+低延迟强实时战斗'),
('报道的岗位统计截至10月8日。','数据截至10月8日')]),
('J_NAMI','库洛《代号NAMI》招聘透露全平台多人共斗ARPG',[
('游戏陀螺的招聘梳理显示，库洛《代号NAMI》正招募用户研究与共斗玩法人员。','《代号NAMI》招募用户研究'),
('招聘信息将其描述为基于UE5的开放世界多人共斗ARPG，世界观偏向机械与魔法共存，目标覆盖PC、主机和移动端。','目标覆盖PC、主机、移动端全平台'),
('报道的岗位统计截至10月8日。','数据截至10月8日')]),
('J_SUN','库洛《代号SUN》招聘指向载具、大规模团队战与动作竞技',[
('游戏陀螺在招聘梳理中记录了库洛《代号SUN》的在研线索。','《代号SUN》'),
('岗位描述包含现代、西幻与科幻混搭的写实美术，以及载具、大规模团队战、开放世界动作竞技等关键词。','大规模团队战'),
('报道的岗位统计截至10月8日。','数据截至10月8日')]),
('J_XISHAN','西山居招聘透露历史国风赛季SLG新游',[
('游戏陀螺的招聘梳理显示，西山居一款历史国风赛季SLG新游正在招募用户运营、数据运营、内容营销和商业化运营人员。','一款历史国风赛季SLG新游'),
('报道据招聘要求判断，产品强调联盟与国战、大地图联盟对抗。','强调联盟与国战'),
('岗位统计截至10月8日。','数据截至10月8日')])]
for cid,title,facts in J:
    if DM[cid]['decision']=='include':item(cid,title,[(t,50,n) for t,n in facts])
item('J_MARKET','近60家游戏公司社招超8500个岗位，UE5与AI需求进入研发职能',[
('游戏陀螺发布的招聘调查显示，截至10月8日，国内近60家游戏厂商有超过8500个社招岗位，较春季减少、总量趋稳。',50,'国内近60家游戏厂商约有超8500个社招岗位'),
('腾讯IEG国内约1065个岗位，网易互娱与雷火合计超过1500个，需求以成熟产品补充人员和新方向预研并行为主。',50,'网易互娱与雷火共计超1500个岗位'),
('岗位描述中UE5、AIGC、全球化发行与技术美术较常出现；文章将AI策划、AI视觉创意与Agent协作等岗位视为AI进入具体研发职能的迹象。',50,'AI岗位从噱头变职能')])
items[-1]['claims'].append(cl('腾讯IEG国内约1065个岗位',50,'腾讯IEG国内约有1065个社招岗'))
item('I020','合作海盗RPG《龙骨海盗》开放首个公开试玩版',[
('支持简体中文的1—6人合作海盗RPG《龙骨海盗》推出免费试玩版。',20,'1—6人合作海盗RPG'),
('这是游戏首个公开试玩版，也是迄今规模最大的可玩版本，可体验出海与类魂战斗。',20,'首个公开试玩版')])
item('I191','放置地牢RPG《流放地牢》开放试玩',[
('放置、地牢与角色扮演游戏《流放地牢》已上线试玩。',191,'Event: 已上线试玩'),
('该节点列于10月20日产品日程。',191,'Event date: 2026-10-20')])
items[-1]['claims'] += [cl('《流放地牢》',191,'Game: 流放地牢'),cl('放置、地牢与角色扮演',191,'Tags: 放置 / 地牢 / 角色扮演')]
item('I195','放置卡牌新作《大武林》于10月20日正式上线',[
('放置卡牌角色扮演游戏《大武林》于10月20日10:00正式上线。',195,'Event: 10:00 正式上线')])
items[-1]['claims'] += [cl('《大武林》',195,'Game: 大武林'),cl('10月20日10:00',195,'Event date: 2026-10-20 10:00'),cl('放置卡牌角色扮演',195,'Tags: 放置 / 角色扮演 / 卡牌')]
item('I198','像素JRPG《英雄请出战》于10月20日正式上线',[
('像素剧情JRPG《英雄请出战》于10月20日10:00正式上线。',198,'Event: 10:00 正式上线')])
items[-1]['claims'] += [cl('《英雄请出战》',198,'Game: 英雄请出战'),cl('10月20日10:00',198,'Event date: 2026-10-20 10:00'),cl('像素剧情JRPG',198,'Tags: JRPG / 剧情 / 像素')]
DM['I080']['source_ids']=[sid(80),sid(91)];DM['I080']['cluster_basis']=dict(subject='Griffin Gaming Partners/Entertainment 360',product='HITpoint Entertainment',event_date='2026-10-19',event='宣布共同成立游戏影视改编公司')
item('I080','Griffin与Entertainment 360成立HITpoint，拓展游戏影视改编',[
('Griffin Gaming Partners与Entertainment 360共同成立HITpoint Entertainment，专门寻找、开发和制作游戏影视改编项目。',80,'Called HITpoint Entertainment'),
('新公司计划在早期识别有改编潜力的游戏IP，并让游戏创作者从开发到制作保持参与。',80,'keep game creators closely involved'),
('Game Developer报道将成立公告的时间标为前一日。',91,'Yesterday, game industry venture capital')])
item('I072','《ForgeTax》销量估算超25万份，国内复刻产品下载达30万次',[
('据游戏新知援引Gamalytic估算，9月30日上线的铸剑Roguelike《ForgeTax》销量超过25万份，销售额折合人民币超过375万元。',72,'超过25万份'),
('报道同时指出，微信、B站Toy与TapTap已出现高度相似的作品，其中TapTap《铸剑大师模拟器》下载达到30万次。',72,'已经获得了30万次下载'),
('原作由韩国在读大学生独立开发，其强化武器、承担碎剑风险与出售成品的循环，已被带入国内小游戏分发渠道。',72,'仅由一名韩国的在读大学生')])
items[-1]['claims'] += [cl('9月30日上线',72,'9月30日'),cl('微信、B站Toy与TapTap',72,'B站Toy平台的《铸剑大师》'),cl('强化武器、承担碎剑风险与出售成品的循环',72,'博弈→卖钱→再博弈')]
item('I190','《战舰移动2》国服首次曝光，开放预约',[
('海战多人竞技游戏《战舰移动2》国服正式首曝并开放预约，节点列于10月20日产品日程。',190,'Event: 国服正式首曝')])
items[-1]['claims'] += [cl('《战舰移动2》国服',190,'Game: 战舰移动2-国服'),cl('海战多人竞技',190,'Tags: 海战 / 多人联机 / 竞技'),cl('10月20日',190,'Event date: 2026-10-20')]
for cid,title,product,genre,i,launch in [
('I196','像素RPG《守护庄园》开放预下载，10月21日上线','守护庄园','像素冒险角色扮演',196,'10月21日'),
('I197','多人格斗《拳皇·命运》开放预下载，10月21日上线','拳皇·命运','多人格斗动作',197,'10月21日'),
('I201','策略卡牌《征战王权》开放预下载，10月23日上线','征战王权','策略竞技卡牌',201,'10月23日'),
('I202','篮球经营游戏《美职篮奇迹梦之队》开放预下载','美职篮奇迹梦之队','篮球体育经营',202,'10月21日')]:
    item(cid,title,[(f'{genre}游戏《{product}》于10月20日开放预下载，将于{launch}上线。',i,'Event:')])
    items[-1]['claims'] += [cl(f'《{product}》',i,'Game:'),cl('10月20日',i,'Event date: 2026-10-20'),cl(genre,i,'Tags:')]
# Direct game AI applications precede all possible transferable frontier candidates.
item('A073','海艺SeaGames扩展到游戏美术工作站，Maker正在内测',[
('游戏新知的产品观察显示，海艺科技于8月上线SeaGames，提供角色、场景与音乐等游戏资产生成，并提供Skill接入入口。',73,'《SeaGames》在今年8月份才正式上线'),
('其游戏开发客户端SeaGames Maker正在内测，计划借助Agent覆盖玩法设计、程序、美术与音效，并输出微信、抖音小游戏工程。',73,'正在内测一款AI游戏开发客户端'),
('团队自述，原本开发游戏时受美术进度拖累，因此先制作工具，目标是保持资产一致性并支持后续修改。',73,'团队原本正在制作一款游戏')])
items[-1]['claims'].append(cl('输出微信、抖音小游戏工程',73,'最终输出微信小游戏、抖音小游戏工程'))
item('A043','创作者用AI串联Blender与引擎制作原型，后续适配仍需验证',[
('GameLook整理的创作者案例显示，有人通过Blender MCP让AI搭建医院走廊场景，作者称从首次输入到镜头短片约耗时45分钟。',43,'总共用了约45分钟'),
('另一项GTA风格城市演示由GPT与Codex驱动UE5、处理逻辑，Tripo提供基础3D资产，展示了通用模型与专业工具的协作。',43,'GPT与Codex负责驱动UE5'),
('文章同时指出，演示跑通后仍要检查几何、绑定、碰撞与性能；生成速度并不等于正式游戏资产的可用率。',43,'关节变形、贴图浪费、碰撞错误和性能超标')])
item('A089','Digital Sun因AI复刻风险缩小《ReVamp》公开测试范围',[
('Digital Sun取消了《ReVamp》原计划的大规模公开试玩，改为10月29日起面向Discord社区进行更受控的测试。',89,'starting on October 29'),
('工作室表示，担心作品在正式推出前就被逆向、克隆并抢先发布；该作仍计划于2027年3月推出。',141,'due for release in March 2027'),
('这一决定压缩了提前收集反馈、指标和积累受众的公开渠道，开发团队正将可访问范围纳入测试设计。',89,'solicit player feedback, gather metrics')])
items[-1]['source_ids']=[sid(89),sid(141)]
DM['A089']['source_ids']=[sid(89),sid(141)];DM['A089']['cluster_basis']=dict(subject='Digital Sun',product='ReVamp',event_date='2026-10-20',event='缩小公开试玩范围')
item('A114','谷歌智能体团队自主通关《我的世界》，长任务协调伴随高开销',[
('IGN中国转述谷歌研究称，4个Gemini 4 Argon智能体在随机种子世界中，通过游戏内聊天和共享记忆协作，耗时27个多小时击败末影龙。',114,'4个谷歌Gemini 4 Argon'),
('它们通过Mineflayer控制角色，自行规划、编写与调试程序；研究人员称过程中没有需要人工干预的情况。',114,'每个智能体都通过名为Mineflayer'),
('报道称整个过程运行2783个程序、死亡605次，消耗13.5亿输入token，按普通用户价格约需1620美元，显示完成长任务与经济性仍是不同指标。',114,'运行2783个程序')])
items[-1]['claims'] += [cl('通过游戏内聊天和共享记忆协作',114,'共享记忆与队友协调'),cl('耗时27个多小时击败末影龙',114,'它们花了27个多小时'),cl('消耗13.5亿输入token，按普通用户价格约需1620美元',114,'13.5亿个输入token')]
item('A068','SpireBench用《杀戮尖塔》测试长期规划，模型局部战术强于整局策略',[
('游研社介绍了上周发布的SpireBench研究：20个模型使用铁甲战士，在A20难度挑战相同的10个新种子，200局中仅GPT-5.6 Sol通关心脏一次。',68,'20个大模型统一使用铁甲战士'),
('研究观察到模型更少挑战精英、更常在营火回血，局部战斗能力未能稳定转化为整局构筑优势；跨局记忆还可能强化既有保守倾向。',68,'建议"谨慎行事"的有119条'),
('实验只覆盖一个角色和10个种子，人类对照也未使用同一批种子，结果不能外推为所有游戏的智能体能力排名。',68,'人类玩家也没有在同一批种子上做对照')])
items[-1]['claims'].append(cl('更少挑战精英、更常在营火回血',68,'AI在第一幕平均只打'))
item('A078','日本演员联盟提出AI配音许可指南，复制表演需另付报酬',[
('日本演员联盟发布生成式AI声音使用指南，建议在训练及使用的每个阶段事前取得演员同意；复制表演应被视为新表演，另付报酬或版税。',78,'must be treated as a new performance'),
('对已故演员，指南要求生前许可，以及家属和所属机构的同意与付费。',78,'permission was granted during their lifetime'),
('AI自动翻译还应维持原表演的艺术完整性，跨境使用需取得许可；联盟同时表示将推动声音权利立法。',78,'artistic integrity')])
items[-1]['claims'] += [cl('在训练及使用的每个阶段事前取得演员同意',78,'including before training models'),cl('推动声音权利立法',78,'encourage the government to legislate')]
# Calendar selection is the prefix produced by sync_release_decisions.py.
audit=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
for d in D:
    if d['section']!='release_calendar' or d['decision']!='include':continue
    n=next(n for n in audit['nodes'] if n['candidate_id']==d['candidate_id'])
    if n['product']=='余烬之镇':
        item(d['candidate_id'],'余烬之镇',[
        ('Cygnus Cross开发的像素动作冒险RPG端游《余烬之镇》于10月20日在Steam公开免费试玩；玩家可在序章体验逃离魔法监狱、战斗刷宝与采集锻造。',61,'由独立工作室Cygnus Cross开发')],release=dict(product='余烬之镇',event='公开试玩',date='2026-10-20',platform='Steam',company='Cygnus Cross'))
        items[-1]['claims'] += [cl('10月20日在Steam公开免费试玩',61,'游戏已于10月20日'),cl('《余烬之镇》',36,'《余烬之镇》')]
    elif n['product']=='星塔旅人':
        item(d['candidate_id'],'星塔旅人',[
        ('悠星网络出品的俯视角轻动作手游《星塔旅人》于10月20日上线一周年版本，新增常驻自走棋“尖兵陷阵”和家园玩法“魔王之塔Beta”；前者围绕旅人阵容与站位构筑，后者提供家具布置与角色日常。',60,'由悠星网络出品')],release=dict(product='星塔旅人',event='重大常驻玩法更新',date='2026-10-20',platform='',company='悠星网络'))
        items[-1]['claims'] += [cl('常驻自走棋“尖兵陷阵”',48,'自走棋比较可行'),cl('家园玩法“魔王之塔Beta”',60,'「魔王之塔Beta」系统正式开放'),cl('旅人阵容与站位构筑',60,'合理配置旅人阵容与站位'),cl('手游',48,'作为一个手游')]
# Community items only use Oct20 content, with player attribution throughout.
body='''《明日方舟：终末地》官方淘宝店的98元金属测量套件，被玩家指出其中标为“游标卡尺”的部件不符合常规游标卡尺特征。10月20日建帖的玩家称，商品详情页已删除“游标”二字；跟帖者质疑，若宣传图就是实物，缺少副标的结构只能称作卡尺。

争议集中在商品功能与宣传名称是否匹配，以及游戏周边借用专业工具名称时的准确性。20日的讨论从定价延伸到专业常识，有玩家表示起初甚至以为宣传图经过恶搞；商品名称修改本身，也成为玩家继续追问产品定位的触发点。'''
item('C215','《终末地》测量套件被指缺少游标，玩家质疑专业名称与实物不符',[
('98元金属测量套件',215,'售价98的金属测量套件'),('10月20日建帖',215,'2026-10-20 14:57'),('商品详情页已删除“游标”二字',215,'已删除《游标》二字'),('缺少副标',215,'游标卡尺一定要有副标'),('起初甚至以为宣传图经过恶搞',215,'黑子P图')],body=body,community=DM['C215']['community'])
body='''《二重螺旋》1.7版本开服当晚出现无法进入游戏与掉线反馈，玩家随之担忧存档和养成进度是否受损。10月20日晚的社区帖称，版本15:00开放，17:23起陆续有人无法进服，21:20后掉线增多，22:30开始维护扩容；同帖还提到外服存在Steam启动器无法启动的问题。

玩家讨论集中在服务稳定性与存档可靠性，争议从“能否登录”进一步转向“是否发生回档”。20日23:12的回复强调，当时社区关于回档主要还是文字描述，尚缺确定性证据；玩家对故障范围与损失的判断并不一致。帖内随后编辑的跨午夜恢复情况属于次日节点，本期时间线截至20日启动扩容维护。'''
item('C226','《二重螺旋》1.7开服后掉线与进服受阻，玩家担忧进度回退',[
('《二重螺旋》1.7版本',226,'《二重螺旋》1.7版本'),('15:00开放，17:23起',226,'今日15:00正式开服'),('21:20后掉线增多，22:30开始维护扩容',226,'21:20起出现更多掉线情况'),('外服存在Steam启动器无法启动的问题',226,'外服出现steam启动器'),('20日23:12',226,'2026-10-20 23:12'),('关于回档主要还是文字描述',226,'回档基本只有文字描述')],body=body,community=DM['C226']['community'])
# No process-language tail in the public community copy.
items[-1]['body']=items[-1]['body'].replace('帖内随后编辑的跨午夜恢复情况属于次日节点，本期时间线截至20日启动扩容维护。','')
pipeline='''观察：AI游戏工具的价值正在从“生成一张图或一个模型”转向“把结果接入可运行、可修改的工程”。海艺SeaGames已提供整套游戏美术资产生成，Maker仍在内测、尝试输出微信与抖音小游戏工程；GameLook整理的Blender与UE5原型案例，则显示通用模型开始组织软件操作，专业工具仍提供基础资产。两类案例共同提出一个问题：产出更多内容之后，谁来保证内容能继续迭代？

分析：单次生成容易用画面效果评价，工程交付却需要一致的人物、可复用的部件和能延续的修改。海艺团队自述，制作游戏时在不同AI工具之间切换、并保持资产一致性，拖慢了进度，因此先做工作站。这意味着付费理由可能落在串联流程和减少返工上；如果每次改动都需要重新整理资产，生成端节省的时间便难以传到项目后端。Maker的内测状态也意味着，这条完整交付链目前仍需实际项目验证。

GameLook案例还呈现了另一种分工：通用模型安排Blender和UE5操作，Tripo负责基础3D资产。但演示能运行，与资产适合正式游戏之间仍隔着几何、绑定、碰撞和性能检查。生成速度越快，未通过规格检查的内容也可能积累得越快。由此推演，游戏工具的竞争会更依赖可用资产比例、修改后的稳定性和整个流程的交付成本，而不是只比较一次生成用了多少时间；现有演示尚不足以证明这些环节已普遍自动化。'''
item('D_PIPELINE','AI游戏工具的交付重点从生成资产转向工程可用性',[
('海艺SeaGames',73,'《SeaGames》'),('Maker仍在内测',73,'正在内测一款AI游戏开发客户端'),('输出微信与抖音小游戏工程',73,'最终输出微信小游戏、抖音小游戏工程'),('在不同AI工具之间切换',73,'在AI工具之间来回切换'),('Tripo负责基础3D资产',43,'Tripo生成3D资产'),('几何、绑定、碰撞和性能检查',43,'关节变形、贴图浪费、碰撞错误和性能超标')],body=pipeline,card_copy=dict(source_label='游戏新知与GameLook案例分析',summary='AI工具开始承担从资产生成到工程交付的衔接，但一致性、修改稳定性与性能验证，仍决定生成能力能否变成项目效率。',insights=[dict(title='付费理由延伸到交付',detail='SeaGames团队因工具切换与资产一致性受阻先做工作站，价值取决于能否减少后续整理和返工。'),dict(title='通用模型与专业工具分工',detail='模型组织Blender和引擎操作，专用工具提供基础资产，流程衔接比孤立生成效果更关键。'),dict(title='演示可运行仍需规格验证',detail='几何、绑定、碰撞和性能问题不会因产量上升消失，完整工程链仍需实际项目验证。')]))
demo='''观察：Digital Sun把《ReVamp》公开测试收缩为Discord社区内的受控测试，理由是担心作品在上线前被AI辅助复刻并抢先发布。与此同时，《ForgeTax》案例已显示，简单规则可以快速进入国内多个小游戏渠道，TapTap上的相似产品下载达到30万次。两者不是同一次侵权事件，却共同改变了提前展示玩法的成本：试玩既能寻找玩家，也可能给后来者提供足够清晰的制作参照。

分析：公开Demo原本依赖一个时间差——小团队先展示核心体验、获得反馈并积累受众，而后来者仍需较长制作与分发周期。Digital Sun明确表示，距离正式推出尚有数月，大规模公开构建版本的风险过高。《ForgeTax》围绕强化概率、碎剑与出售武器建立的短循环，则使核心规则容易被观察和迁移。这里不能据此断言所有相似产品都使用了AI，但制作和渠道进入的速度已经成为宣发决策的一部分。

缩小测试范围可以减少完整构建版本的扩散，却也减少公开反馈、指标和自然获客的机会。受控测试保留了验证环节，但能否接触到目标用户、能否获得足够多样的行为数据，仍是它的成立前提。由此推演，小团队的防御能力会同时取决于可展示内容的范围、正式发布与测试的间隔，以及已有受众能否识别原作；仅仅隐藏所有玩法，也可能让原创项目失去被发现的机会。'''
item('D_DEMO','AI复刻风险让公开试玩同时承担获客与泄露成本',[
('把《ReVamp》公开测试收缩为Discord社区内的受控测试',89,'more contained'),('TapTap上的相似产品下载达到30万次',72,'已经获得了30万次下载'),('距离正式推出尚有数月',89,'With launch still months away'),('获得反馈并积累受众',89,'solicit player feedback, gather metrics'),('强化概率、碎剑与出售武器',72,'破坏 ——武器消失')],body=demo,card_copy=dict(source_label='Game Developer与游戏新知案例分析',summary='公开试玩既帮助原创团队寻找玩家，也可能缩短复刻者的学习与发行时间，受控测试因此成为曝光和验证之间的取舍。',insights=[dict(title='提前展示的时间差缩小',detail='Digital Sun担心测试构建被抢先复刻；ForgeTax相似产品已进入国内多个小游戏渠道。'),dict(title='收紧范围也减少验证机会',detail='Discord受控测试能限制扩散，但仍要验证目标用户覆盖和行为数据的多样性。'),dict(title='隐藏玩法存在获客代价',detail='可展示范围、发布间隔与受众识别共同影响原作的防御能力，全面隐匿也会失去被发现的机会。')]))
# Correct candidate metadata and prepare human-readable audit artifacts BEFORE report_items.
DM['I193']['pc_release_scope']=dict(classification='unknown',basis='明确PC/主机单机试玩，但开发主体未知，R1。',evidence=[dict(source_id=sid(193),evidence=proof(193,'Badges: PC/主机'))])
for d in D:
    if d['candidate_id'].startswith('G') and 'pc_release_scope' in d:
        ev=d['pc_release_scope']['evidence'][0]['evidence']
        if '在线合作' in ev:
            d['pc_release_scope'].update(classification='multiplayer_or_other',basis='来源明确在线合作，不属于单机；但未证明PVP竞技、国内主体或移动迁移，R1。')
    d['source_ids']=list(dict.fromkeys(d['source_ids']))
DM['I080']['event_date']='2026-10-19'
for i in [54,55,158,159]:
    d=DM[f'I{i:03}'];d['pc_release_scope']['classification']='unknown';d['pc_release_scope']['basis']='没有本地正文依据确认国内/重点主体；按未知相关性R1。'
for i in [75,77]:
    d=DM[f'I{i:03}'];d['cluster_basis']=dict(subject='PEGI/GRA' if i==75 else 'Sensor Tower',product='数字游戏付费随机道具评级' if i==75 else 'GTA6美国数字预购',event_date='2026-10-20',event=d['event'])
    d['source_ids'] = list(dict.fromkeys(d['source_ids']+([sid(86)] if i==75 else [sid(106)])))
save('selection_decisions.json',raw)
items.sort(key=lambda x:(['industry_news','ai_trends','release_calendar','community_discourse','deep_analysis'].index(x['section']),-DM[x['candidate_id']].get('scores',{}).get('total',0) if x['section']=='industry_news' else 0))
cards=['# 全量事件候选｜2026-10-20','\n输入230条；候选按独立事件建卡；行业与日历独立选材。\n']
md=['# 选材决策｜2026-10-20','','卡片曝光去重：历史窗口2026-10-06_to_2026-10-19，112次行业曝光记录已逐项读取card_exposed/card_rank/card_limit/card_exposure_source。Metacore、Flow、艾希、神仙道3等存在已曝光匹配；本期不选card_carryover。ForgeTax历史rank=null、limit=10、card_exposed=false，本期采用新增国内复刻下载状态为material_update，不冒充原作净增销量。','','维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均有独立候选；19个招聘项目/方向逐条审计；普通宣传E0逐条保留。全部230个输入ID有决策映射，产品日历另反扫industry+release。','','AI反扫：159条行业原始记录及招聘/综合稿拆项全部检查，直接采用转AI并保持独立事件边界。','','社区补扫：14条社区与159条行业按游戏名/卡尺/游标/1.7/回档/维护等全文扫描，公开正文只使用截至20日节点；21日回复不倒灌。','','产品日历：两源前缀为余烬之镇(9)、星塔旅人(3)；小小港湾/中世纪同稿去重；地渊两源缺可逐字核验的绝对日，不伪造日期。','','| candidate | decision | section | score | reason |','| --- | --- | --- | --- | --- |']
for d in D:
    evidence=[c['evidence'] for x in items if x['candidate_id']==d['candidate_id'] for c in x['claims']]
    if not evidence:
        # Paragraph scan keeps factual lines; procedural boilerplate stays out of candidate facts.
        for s in d['source_ids']:
            lines=[l for l in S[s]['text'].splitlines() if re.search(r'上线|测试|发布|宣布|开发|收入|融资|收购|million|launch|release|develop|announce|Event:|Tags:|延期|停运|招聘|流水|卡尺|回档',l,re.I)]
            evidence += lines[:2]
    facts='；'.join(dict.fromkeys(evidence)) or '原文为'+S[d['source_ids'][0]]['text'].splitlines()[0]+'；判断：'+d['reason']
    cards += [f"## {d['candidate_id']} - {d['event']}",f"- section: {d['section']}",'- status: candidate',f"- source_ids: {', '.join(d['source_ids'])}",f"- entities: {', '.join(d['entities'])}",f"- event_date: {d.get('event_date','2026-10-20')}",'- facts: '+facts.replace('\n',' '),'- notes: '+d['reason'],'']
    for field in ['history_check','history_occurrence_details','pc_release_scope','community','cluster_basis']:
        if field in d:cards += ['- '+field+': '+json.dumps(d[field],ensure_ascii=False),'']
    sc=d.get('scores',{});score=f"事件{sc['event']}×相关{sc['relevance']}+钩子{sc['hook']} = {sc['total']}" if d['section']=='industry_news' else json.dumps(sc,ensure_ascii=False)
    md += ['| '+' | '.join([d['candidate_id'],d['decision']+(' into '+d['merge_into'] if d.get('merge_into') else ''),d['section'],score,d['reason'].replace('|','/')])+' |']
md.insert(3,'产品日历漏挂反查：完整industry/release逐段召回新品首曝、定档、预下载、试玩与重大老品节点；全部节点均有include/exclude，行业是否收录不参与日历排序。')
(P/'event_candidates.md').write_text('\n'.join(cards)+'\n',encoding='utf-8');(P/'selection_decisions.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
save('report_items.json',{'report_type':'daily','date':'2026-10-20','items':items})
report=['# 游戏行业日报｜2026-10-20','']
sections=[('industry_news','一、行业新闻'),('ai_trends','二、AI 新闻'),('release_calendar','三、新游发布 / 产品日历'),('community_discourse','四、玩家舆论 / 社区动态'),('deep_analysis','五、行业精选 / 深度观察')]
for sec,h in sections:
    report += ['## '+h,'']
    for k,it in enumerate([x for x in items if x['section']==sec],1):
        report += ['- '+it['body'],''] if sec=='release_calendar' else [f'### {k}. '+it['title'],'',it['body'],'']
text='\n'.join(report)
assert not re.search(r'沐瞳|Moonton|MLBB|决胜巅峰|Mobile Legends|card_carryover|补位|对我司|值得借鉴|启示',text,re.I)
for it in items:
    for c in it['claims']:assert c['claim'] in it['body'],(it['candidate_id'],c['claim'])
stage=P/'staging';(stage/'_intermediate').mkdir(parents=True,exist_ok=True)
for name in ['report_inputs.jsonl','report_inputs_summary.md','report_inputs_index.md','industry_history_14d.json','industry_history_14d.md','release_calendar_audit.json','source_quality_audit.json','event_candidates.md','selection_decisions.md','report_items.json','selection_decisions.json']:shutil.copy2(P/name,stage/'_intermediate'/name)
(stage/'game_industry_daily_2026-10-20.md').write_text(text,encoding='utf-8')
collector=P.parents[3]/'news_data/_collector_runs/2026-10-20/run_summary.json'
if collector.exists():save('collector_coverage_audit.json',json.loads(collector.read_text(encoding='utf-8')))
save('run_summary.json',{'report_type':'daily','id':'2026-10-20','sections':{s:sum(x['section']==s for x in items) for s,_ in sections},'history_window':'2026-10-06_to_2026-10-19','repeat_only_excluded':[d['candidate_id'] for d in D if d.get('history_check',{}).get('novelty')=='repeat_only' and d['decision']=='exclude'],'material_updates':['I072'],'card_carryover':[],'sources_used':sorted({s for x in items for s in x['source_ids']}),'industry_scores':[dict(candidate_id=x['candidate_id'],title=x['title'],scores=DM[x['candidate_id']]['scores']) for x in items if x['section']=='industry_news'],'boundary_5_6':[{k:d[k] for k in ['candidate_id','event','scores','reason']} for d in D if d['section']=='industry_news' and 5<=d['scores']['total']<=6],'deep_handoff':'星期三日报，无周五飞书回执交接；3条newsletter已审计；2条本期已选事件综合深度。','warnings':['22条非完整输入，正文未引用','AI6条均为游戏直接作用案例，超出1–3软目标','地渊珠宝匠两源但正文缺绝对发生日，未伪造日期；小小港湾同稿不算多源','无10月20日Steam榜单输入，不补旧榜']})
print('staged',len(items),'items;',len({s for x in items for s in x['source_ids']}),'sources')
