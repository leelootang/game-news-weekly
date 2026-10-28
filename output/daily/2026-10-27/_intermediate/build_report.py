"""Editorial audit and report assembly for the anchored 2026-10-27 daily only."""
import json, re, sys, hashlib, copy
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'scripts'))
from industry_timing import build_time_check
from sync_release_decisions import sync
P = Path(__file__).resolve().parent
DAY = '2026-10-27'
ROWS = [json.loads(x) for x in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
SRC = {x['source_id']:x for x in ROWS}
H = json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
HMD = (P/'industry_history_14d.md').read_text(encoding='utf-8')
assert len(ROWS)==209 and len(H['occurrences'])==100
def sid(n): return f'S{n:04d}'
def save(name, obj): (P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def quote(n, text):
    assert text in SRC[sid(n)]['text'], (n,text)
    return {'source_id':sid(n),'evidence':text}
def history(refs=(), novelty='new_event', new=()):
    prior=[H[scope][i] for scope,i in refs]
    return {'history_match':bool(prior),'novelty':novelty,
      'prior_occurrences':[f"{x['report_kind']} {x['report_window']['start']}_to_{x['report_window']['end']}｜{x['title']}" for x in prior],
      'new_facts':list(new),'prior_card_exposed':any(x['card_exposed'] for x in prior) if prior else None,
      'exposure_details':[{k:x.get(k) for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for x in prior],
      'archive_checked':True}

decisions=[]; by={}; items=[]
def industry(nums, E,R,M,subject,kind,basis, evidence='', genres=(), genre_quote='',
             event=None, decision=None, reason='', gate=None, focus=(), hist=None, event_date='unknown', scope=None):
    n=nums[0]; ids=[sid(i) for i in nums]; cid=f'I{n:03d}'
    q=quote(n,evidence) if evidence else None
    total=E*R+M; decision=decision or ('include' if E and total>=5 else 'exclude')
    d={'candidate_id':cid,'section':'industry_news','source_ids':ids,'entities':[subject],
       'event':event or SRC[sid(n)]['title'],'decision':decision,
       'reason':reason or (f'E{E}×R{R}+M{M}={total}；'+basis),
       'scores':{'event':E,'relevance':R,'hook':M,'total':total},
       'history_check':hist or history(), 'industry_reverse_scan':True}
    if E:
        d['subject_assessment']={'subject':subject,'kind':kind,'focus_companies':list(focus),'basis':basis,'evidence':[q] if q else []}
        if kind=='representative_subject':d['subject_assessment']['representative_product']=subject
        d['genre_assessment']={'matched_genres':list(genres),'basis':'本事件直接命中重点品类' if M else '本事件没有来源直接证明重点细分类别；不借背景产品加分',
                               'evidence':[quote(n,genre_quote)] if M else []}
        d['time_check']=build_time_check(ids,SRC,DAY,DAY,event_date=event_date,basis='当前报道自身published_at优先；缺失才回退输入date；实际事件日期只用于历史语态，不作门禁。')
        # Keep PC/console scope evidence for all identifiable signals, independent of R.
        if scope or re.search(r'PC|Steam|Switch|主机|端游|PlayStation|Windows|Xbox', '\n'.join(SRC[s]['text'] for s in ids),re.I):
            d['pc_release_scope']={'classification':scope or ('domestic_or_focus' if focus else 'unknown'),
                'basis':'按当前来源识别平台范围；主体重要性独立判断，不因国产或PC平台自动升降R。','evidence':[q or quote(n,SRC[sid(n)]['text'].splitlines()[0])]}
        if decision=='exclude':d['exclusion_gates']=gate or ['score']
    if len(ids)>1:d['cluster_basis']={'subject':subject,'product':subject,'event_date':event_date,'event':d['event']}
    decisions.append(d);by[cid]=d
    # Duplicates retain individual source-level decisions without using snippets as final evidence.
    for other in nums[1:]:
        m=copy.deepcopy(d);m.update(candidate_id=f'I{other:03d}',source_ids=[sid(other)],decision='merge',merge_into=cid,reason=f'同主体、同公告日期、同一事件；合并至{cid}')
        m.pop('exclusion_gates',None)
        m['source_ids']=ids
        if E:
            m['time_check']=build_time_check(ids,SRC,DAY,DAY,event_date=event_date,basis='与主候选同一事件的来源窗口复核；事件日期不作门禁。')
        decisions.append(m);by[m['candidate_id']]=m
    return d

# Substantive industry events: every R judgment is grounded in this run's text.
industry([22],3,3,1,'米哈游','focus_subject','米哈游直接归属的在研生活模拟产品付费测试，不以国产标签赋R。',
 '《星布谷地》三测开放付费后，米哈游也走到了需要回答持续运营的生活模拟游戏如何做商业化的阶段',
 ['life_simulation'],'非买断单机的生活模拟游戏一直是个有点矛盾的品类。',focus=['米哈游'],event='星布谷地三测付费机制公开')
industry([30],3,3,1,'灵犀','comparable_major_subject','来源以灵犀简称直接归属产品，提供畅销榜第4及成熟数值卡牌研发经验，结合重点主体参照判断R3；不为校验补写正文未出现的公司全称或关联。',
 '开服三天后，灵犀的《篮球少女：飞跃巅峰》登上了App Store游戏畅销榜第4。',
 ['competitive'],'一个是异步PVP的竞技场',event='篮球少女实际开服与首轮商业表现',
 hist=history([('occurrences',75)],'material_update',['来源确认已实际开服，开服三天后进入App Store游戏畅销榜第4，而历史仅为10月23日公测安排。']))
industry([25],3,3,0,'NEXON与悠星','comparable_major_subject','开发商收回成熟头部二次元IP日本发行运营权，来源证明约8亿美元全球流水、日本七成以上贡献及长期本地发行生态，具同档行业影响力。',
 '根据第三方数据网站的信息，《蔚蓝档案》全球累计流水可以大致估计在8亿美元左右，约合日元超过千亿，其中日本市场贡献超过七成。',
 event='蔚蓝档案日本发行运营权将移交NEXON',event_date='2026-10-25')
industry([63],3,3,0,'Xbox','comparable_major_subject','微软全球游戏平台业务；首任COO统管端到端盈亏并直接向CEO汇报，核心管理层离职。',
 'Helen Chiang, who assumed the role in July of this year amidst significant layoffs and restructuring at Xbox, became the first-ever Chief Operating Officer for Xbox reporting directly to CEO Asha Sharma.',
 event='Xbox首任COO Helen Chiang离职',
 hist=history([('archive_occurrences',289),('archive_occurrences',386)],'material_update',['此前任命的首任COO已经离职，公司暂未确定继任安排。']))
industry([64],3,3,0,'Xbox','comparable_major_subject','Xbox全IP影视独家许可涉及七年及5亿美元提案，是平台级IP经营的重大商业谈判；保留据报道归因，未称合同成交。',
 "Netflix reportedly sought a $500 million deal with Microsoft's Xbox for seven years of exclusive rights to adapt its full suite of properties for TV and film.",
 event='据报Xbox拒绝Netflix七年IP改编提案')
industry([27,50,80],2,3,1,'腾讯天美','focus_subject','来源明确宝可梦公司与天美共同研发；同一产品10月27日宣布国内外停运安排，按公告事件合并，不把国服和国际服停服日混同。',
 '这款游戏，是由宝可梦公司与天美工作室群共同研发的产品',
 ['competitive'],'MOBA',focus=['腾讯'],event='宝可梦大集结公布国服及国际服停运安排',event_date=DAY)
industry([10,90],2,3,0,'Microsoft游戏业务','comparable_major_subject','微软游戏第一方工作室与重点IP的出售协商期限调整，来源证明工作室217人及微软直接协商安排；不按泛微软业务赋分。',
 '《漫威刀锋战士》开发商Arkane Lyon获得额外时间寻找买家',event='Arkane Lyon寻找买家的协商期延长一个月')
industry([68],2,3,0,'腾讯魔方','focus_subject','来源直接确认Tencent-owned Morefun及其Arena Breakout: Infinite项目；是既有产品进入西方市场的发行规划，不将较早展会亮相伪装为昨日首曝。',
 "Morefun, the Tencent studio behind Arena Breakout: Infinite, debuted Roco Kingdom in the west at Gamescom – and has big plans for the game's launch in 2027.",
 focus=['腾讯'],event='Roco Kingdom面向西方市场亮相并筹划2027年发行')
industry([33,207],2,3,0,'中国出海手游市场','priority_mobile_market','2026年9月中国手游出海完整收入、增长与下载榜的结构性变化；与10月12日单独SLG赛道报告不是同一发布事件，不拆成产品流水快讯。',
 '10月26日，Sensor Tower发布2026年9月中国手游出海收入及下载量排行榜。',event='Sensor Tower发布9月中国手游出海完整榜单',event_date='2026-10-26')
industry([206],2,3,0,'中国移动游戏分发市场','priority_mobile_market','QuestMobile全景生态报告包含中国小程序手机游戏数量结构；只写分类数量比例，不改写成游戏用户或收入份额。',
 '抖音小程序手机游戏和移动视频数量占比分别为60.0%和22.0%。',event='QuestMobile秋季报告披露小程序游戏供给结构')
industry([208],2,3,0,'中国手游发行商全球市场','priority_mobile_market','本期来源发布字段在窗口内，7月统计期本身不是门禁；全量双周及更早归档未找到38家、23亿美元、42.6%的同一7月发行商数据事件，既往7月出海产品榜为另一事件。',
 '2026年7月共38个中国厂商入围全球手游发行商收入榜 TOP 100，合计吸金23亿美元，占本期全球 TOP 100手游发行商收入42.6%。',event='Sensor Tower7月中国手游发行商全球收入回顾')
industry([209],2,3,0,'中国手游发行商全球市场','priority_mobile_market','同一9月发行商收入报告已于10月19日及周报曝光；本次36家/40.4%与旧37家/41.6%不同但来源未解释，不能称为已验证状态更新。',
 '2026年9月共36个中国厂商入围全球手游发行商收入榜 TOP 100',event='Sensor Tower9月中国手游发行商全球收入回顾',
 decision='exclude',gate=['history_repeat','factual_uncertainty'],hist=history([('occurrences',52),('occurrences',67),('occurrences',85)],'repeat_only'),
 reason='已曝光同一9月发行商榜，新增来源没有说明统计家数和占比的差异原因；不把口径冲突自动写成实质更新。')

# Scored exclusions and boundary cases.
industry([8],2,3,0,'Steam','comparable_major_subject','Steam是全球PC分发平台，个人日历提供近期和未来游戏推荐；既有曝光后，本条43字来源未证明功能新增状态。',
 '针对近期发行和即将推出的游戏为玩家进行各种个性化推荐',decision='exclude',gate=['history_repeat'],
 hist=history([('archive_occurrences',275)],'repeat_only'),reason='7月6日已曝光个人日历及推荐入口；本期没有可核验的新状态，不能凭正式发布标题再次计入。')
industry([21],3,1,1,'梧桐宇舟《对峙：交锋时刻》','representative_subject','新发行团队代理海外长线FPS，来源证明基础声量，但未支持其自身达到R2/R3；360投资企业背景不自动抬档。',
 '这款游戏对应的是海外已经运营近十年的《 Standoff 2 》。', ['competitive'],'经典的公平竞技（爆破模式）',event='对峙国服10月16日首测及发行访谈',event_date='2026-10-16')
industry([23,34],3,1,0,'幻萌《战舰少女R》','representative_subject','早期国产二次元代表产品核心主创离世，来源证明代表性但不足以确认头部或R2规模。',
 '据悉，《战舰少女R》主创之一、幻萌网络初创团队成员毛佳栋（“铃兰”）上周在家中不幸离世，终年40岁。',event='战舰少女R核心主创毛佳栋离世')
industry([28],1,3,1,'腾讯《无畏契约》','focus_subject','老产品国服注册用户破亿为重大生命周期里程碑，E1不改成市场报告E2。',
 '2023年5月，腾讯与拳头宣布将瓦定为全球战略级产品', ['competitive'],'瓦的核心体验是高强度竞技。',focus=['腾讯'],event='无畏契约国服注册用户破亿')
industry([29],1,3,0,'完美世界','focus_subject','来源为工程技术分享，有具体优化数据但不是新产品、资本或平台政策事件。',
 '完美世界游戏技术中台发表了名为《<异环>跨平台无缝城市的技术实践》的演讲',focus=['完美世界'],event='异环跨平台无缝城市工程复盘')
industry([31],2,1,1,'Game Spark《Top Lords》','representative_subject','单产品700万美元月流水体现一定声量，但没有真实头部归属、区域发行能力或规模证据支持R2；不将含混渊源写成投资关系。',
 '今年5月，由 Game Spark 推出的中世纪冰雪奇幻题材数字门SLG《Top Lords》', ['casual_slg'],'头部的休闲SLG体系',event='Top Lords9月单月流水突破700万美元',
 hist=history([('archive_occurrences',1018)],'repeat_only'),reason='E2×R1+M1=3；同一9月产品表现已随SLG报告曝光，新稿补充数据和设计背景不证明业务新状态。',gate=['score','history_repeat'])
industry([38],3,1,0,'Funselektor《Over the Hill》','representative_subject','来源证明前作与150万愿望单的独立团队代表性，尚不足头部或R2同档；慢速越野不自动算生活模拟。',
 '2026年10月14日，温哥华独立工作室Funselektor正式发售了这款新作。',event='Over the Hill发售及首轮表现',event_date='2026-10-14')
industry([39],3,1,1,'顽核社与2P Games','representative_subject','新品节玩家第一和60万Demo体现代表性，但本文未证明发行研发生态达到R2；不能凭国产升R。',
 '由顽核社制作、2P Games 发行的《我带过的最差一届》将于 11 月 10 日正式发售！', ['competitive'],'非对称派对游戏',event='我带过的最差一届定档与新品节成绩')
industry([43],2,1,0,'Diversity Game Studio','representative_subject','262万首曝PV支持一定声量；制作人只被证明曾任策划，不是前核心制作人/主策，不能按库洛直属或核心人才创业取R2/R3。',
 '由 Diversity Game Studio负责研发，制作人曾在字节、库洛担任过策划',event='代号二杠三停止研发')
industry([46],1,2,0,'Auroch Digital','comparable_significant_subject','具Warhammer 40,000: Boltgun 2等授权IP和51至200人团队的有影响力开发商；当前事实是纯裁员，E1。',
 'Over the past year our colleagues have delivered amazing games like Warhammer 40,000: Boltgun 2 and Starship Troopers: Ultimate Bug War!',event='Auroch约四分之一岗位进入裁员咨询')
industry([48,86,98,118],1,3,0,'Microsoft游戏业务','comparable_major_subject','Xbox参与自愿离职计划，纯用工调整E1；六万人为微软合资格人数，不是Xbox裁员数。',
 'staff in numerous teams are eligible, including "AI experiences, Copilot, CoreAI, Windows + Devices, Xbox, finance, and human resources."',event='微软自愿离职计划覆盖Xbox')
industry([49,65,78,138],1,3,0,'Sony旗下Sucker Punch','comparable_major_subject','索尼第一方工作室及千万级前作、数百万级新作有头部产品影响力；纯裁员E1，不把成功发售作为新品事件加分。',
 "Yōtei launched last October, selling 3.3 million copies in its first month",event='Sucker Punch裁减24人')
industry([51],1,2,0,'UKIE','comparable_significant_subject','英国游戏行业协会有区域行业代表性，但这里只是税收改革呼吁，不是生效政策。',
 'UKIE, TIGA, and the UK Video Games Council have proposed',event='UKIE呼吁修改英国游戏税收抵免')
industry([52],2,1,0,'PC抢先体验市场','pc_console_market','PC市场整体报道按R1，不能因受访公司名单抬档。',
 "The number of games released through Steam's Early Access program has risen significantly in recent years.",event='抢先体验趋势与开发者案例复盘')
industry([53,134],1,2,0,'Warhorse Studios','comparable_significant_subject','Kingdom Come系列及已公布中土RPG支持较强工作室影响力；本期为安全事故及调查，未证实项目取消、停运或重大资本状态。',
 'Warhorse Studios has experienced a cyberattack resulting in unauthorised access to both company systems and data.',event='Warhorse遭网络攻击')
industry([58],2,2,0,'Nazara Technologies','comparable_significant_subject','印度上市游戏发行平台季度游戏收入具一定规模；本文仅摘要，且是常规季度增长。',
 "The company's core gaming division grew revenue 122% year-over-year to INR 656 crore ($68.9m)",decision='exclude',gate=['financial_routine','source_quality'],reason='季度同比增长没有一致预期/指引异常或资本结构异常证据，且正文被Cloudflare阻断。')
industry([60],1,2,0,'Carry1st','comparable_significant_subject','非洲与中东区域支付发行能力支持R2，但仅有访谈摘要，无法核验完整业务转型细节。',
 'helping other companies sell games and in-game items across Africa and the Middle East',event='Carry1st支付与网店业务重心访谈',decision='exclude',gate=['score','source_quality'])
industry([62],3,1,0,'Azra Games《UnGodly》','representative_subject','标题涉及5000万美元项目和手机适配，但实际正文仅设备参数摘要，未支持项目状态或主体影响力。',
 'The iPhone Duo recently launched on October 23rd',event='UnGodly项目与折叠屏适配访谈信号',decision='exclude',gate=['score','source_quality'])
industry([66],1,2,0,'Nightdive Studios','comparable_significant_subject','来源证明专业复刻发行生态和Atari收购组合，较强垂直行业影响力；本期为管理观点而非新收购。',
 "its business model of remastering and remaking classic games",event='Nightdive负责人谈并购后工作室自主性')
industry([69],2,0,0,'UA融资市场信号','other_or_unknown','正文仅支持教育应用Buddy.ai融资，标题的游戏融资比较缺少可用数据，不据标题替代事实。',event='获客融资与股权融资比较信号',decision='exclude',gate=['source_quality'])
industry([79,129],2,1,1,'Cygnus Cross《Emberville》','representative_subject','新品节有一定代表性，但没有影响力证据支持R2；延期E2，生活与社区建造命中M1。',
 "Emberville's demo was one of the most played during Steam Next Fest last week", ['life_simulation'],'Stardew Valley-like farming and community building',event='Emberville抢先体验推迟至2027年1月7日')
industry([81,137],1,3,1,'Microsoft《Call of Duty》','comparable_major_subject','400亿美元系列收入是头部IP生命周期里程碑E1，不是市场结构数据E2；不改写成新作收入。',
 'The Call of Duty franchise has now exceeded $40 billion in lifetime franchise revenue', ['competitive'],'battle royale genre with Call of Duty: Warzone',event='使命召唤系列累计收入突破400亿美元')
industry([83,110],1,3,0,'BioShock与Netflix改编项目','comparable_major_subject','知名大厂IP电影仍在开发的导演表态，不是新的立项或合作签订。',
 'A BioShock movie at Netflix remains in development, its director has confirmed',event='BioShock电影导演确认仍在推进')
industry([93],3,3,0,'Sony PlayStation','comparable_major_subject','索尼全球游戏平台主体可R3，但所谓下一代架构独占源自专家转述幕后消息，设备本身尚未确认，不能当已发生合作。',
 '索尼可能会为一款尚未确定推出的PlayStation掌机，独家采用AMD的下一代图形架构。',event='传闻索尼掌机采用AMD独占架构',decision='exclude',gate=['factual_uncertainty'],reason='报道明确设备尚未确定推出、仅幕后传闻；未证明拟议独占协议已达成。')
industry([97],1,3,0,'Sony旗下Sucker Punch','comparable_major_subject','同一裁员事件英文正文24人与该中文稿26人不一致，英文较完整源保留审计；纯裁员均不过线。',
 '据Aftermath报道，工作室裁员26人',event='Sucker Punch裁员人数矛盾信号',decision='exclude',gate=['score','factual_uncertainty'])
industry([115],0,3,0,'Valve','comparable_major_subject','外围设备驱动的例行内核补丁，未构成平台政策、重大迁移或新品状态。',
 'Valve developer gaberow said they were looking into it—and patched in kernel support mere minutes later.',
 event='Steam Frame内核新增CD-ROM支持',decision='exclude',reason='E0普通硬件驱动补丁；来源明确不保证终端正式获得支持，不是平台政策或新品跨平台事件。')
industry([116],2,1,0,'Playden for PS5','representative_subject','来源只证明第三方早期alpha兼容项目，不是索尼或Valve官方跨平台发行；尚不足R2。',
 'The program functions as a Steam launcher',event='第三方PS5项目运行Steam游戏')
industry([119],1,1,0,'Jordan Mechner','representative_subject','经典作品创作者回顾访谈，没有新项目立项或公司变更。',
 'Prince of Persia',event='Jordan Mechner2024年访谈于本期刊出')
industry([123],3,0,1,'The Regreening','other_or_unknown','本文提供产品设想，未证明研发发行主体及行业影响力。','', ['life_simulation'],'farm sim',event='The Regreening游戏介绍')
industry([125],0,1,0,'Forbidden Solitaire','representative_subject','既有游戏The Discarded DLC的体验评测，不是新品首曝。',
 'Forbidden Solitaire',event='Forbidden Solitaire的The Discarded DLC评测',decision='exclude',reason='E0：普通DLC内容与评测，不作为新品事件。')
industry([128],3,1,0,'The Mortuary Assistant创作者','representative_subject','代表作创作者推出微型恐怖作品，影响力不足R2。',
 'The Mortuary Assistant',event='微型恐怖新品试玩')
industry([131],2,1,0,'Steam新品节市场','pc_console_market','PC平台活动榜单结构变化R1；不把四款AI声明解读为全部玩家拒绝AI的因果证据。',
 'Valve has revealed the 50 most-played among them',event='10月新品节热门Demo类型结构')
industry([135],1,3,0,'Ubisoft《Dark Messiah》','comparable_major_subject','已有作品社区版内容升级与Steam页面进展，不是本期首次立项或实际新平台发售。',
 'publisher Ubisoft has apparently been a great help',event='Dark Messiah社区版Steam页面与内容介绍')
industry([140],1,1,0,'显卡供应商','representative_subject','外围硬件供应访谈，不是游戏主体业务变化。',
 'RTX 5090',event='RTX5090板卡配件供应信息')
industry([144],3,1,0,'XREAL','representative_subject','有已发布AR产品与显示技术，但本来源缺少游戏业务影响力证据支持R2。',
 'XREAL 1 Pro+',event='XREAL 1 Pro+发布')
industry([147],3,1,0,'BanjihaGames','representative_subject','Seoul2033与FAKEBOOK代表作可核验，但未支持R2同档规模，不因新产品自动入选。',
 'BanjihaGames以独特的前提设定与叙事结构著称，代表作包括文字冒险游戏《Seoul2033》',event='灰烬遗证公布并计划2027年上半年发售')

# Transfer AI/community events before judging generic industry remainder.
for n, target, reason in [(6,'AI','AI NPC试玩信息只有48字，落地细节不足'),(7,'AI','与10月26日已写外包审核说明重复，无新增'),
 (11,'社区','请愿及线下广告诉求写入社区'),(45,'社区','请愿及线下广告诉求写入社区'),(47,'AI','平台AI披露争论转AI候选'),
 (73,'AI','游戏研发AI采用实证转AI候选'),(91,'AI','同一Steam AI披露争论转AI候选'),(92,'AI','主机漏洞AI发现实证转AI候选'),
 (122,'社区','线下广告延续请愿写入社区'),(136,'AI','AI采用预测转AI候选'),(142,'AI','AI制作观点转AI候选')]:
    if f'I{n:03d}' not in by:
        industry([n],1,0,0,target+'候选','other_or_unknown','按事件核心转分区，主体评分不作为转栏资格依据。',event=SRC[sid(n)]['title'],decision='exclude',gate=['section_transfer'],reason=reason)

# Remaining substantive launch signals; other titles are E0 ordinary operations, reviews, awards or non-game items.
for n in [2,4,12,14,17,84,102,103,104,106]:
    if f'I{n:03d}' in by:continue
    text=SRC[sid(n)]['text']; q=text.splitlines()[0]
    industry([n],3 if n in [4,17,102,103,106] else 2,0,0,SRC[sid(n)]['title'],'other_or_unknown',
       '当前来源未证实研发发行主体的行业重要性，R0；新品或档期信号仍完整召回。',q,event=SRC[sid(n)]['title'])
for row in ROWS:
    n=int(row['source_id'][1:])
    if row['section']=='industry_news' and f'I{n:03d}' not in by:
        industry([n],0,0,0,row['title'],'other_or_unknown','例行版本/联动/宣传、评测、聚合推荐、奖项或泛生活内容，没有独立高E状态。',event=row['title'],decision='exclude',reason='E0：'+row['title']+'；普通运营/评测/宣传/非游戏业务，批量留痕；聚合稿中的实际新品另拆候选。')

# Full scans of the two compilation articles; game announcements are independent candidates even at R0.
compilation_games=[]
lines=SRC['S0114']['text'].splitlines()
for i,line in enumerate(lines):
    if line.startswith('发行日期：'):
        product=lines[i-2] if i>=2 else ''; start=max(0,i-2); end=next((j for j in range(i+1,len(lines)) if j+1<len(lines) and lines[j+1].startswith('关键字：')),len(lines))
        block='\n'.join(lines[start:end]); date=re.search(r'2026/(\d\d)/(\d\d)',line)
        if not product or not date:continue
        compilation_games.append((product,f'2026-{date[1]}-{date[2]}',block))
for i,(product,date,block) in enumerate(compilation_games,1):
    d=copy.deepcopy(by['I104']);d.update(candidate_id=f'J114-{i:02d}',source_ids=['S0114'],entities=[product],event=product+'发售清单节点',reason='E3×R0+M0=0；全文分产品反扫，当前输入未证明研发发行主体重要性。',scores={'event':3,'relevance':0,'hook':0,'total':0})
    d['subject_assessment']={'subject':product,'kind':'other_or_unknown','focus_companies':[],'basis':'来源只有产品、玩法与发行清单，无可复核主体影响力证据。','evidence':[]}
    d['genre_assessment']={'matched_genres':[],'basis':'该清单标签不足以确认重点细分类别；不从标题自动加分。','evidence':[]}
    d['pc_release_scope']={'classification':'unknown','basis':'Steam发行清单，未证明重点公司归属。','evidence':[quote(114,block)]}
    d['time_check']=build_time_check(['S0114'],SRC,DAY,DAY,event_date=date,basis='报道在本期，游戏事件日期单独记录，不作行业门禁。')
    decisions.append(d);by[d['candidate_id']]=d
for i,product in enumerate(['无处可藏','归路：新旅途','萌派亚：桌面动物岛','未登记现场','Deep Frost','沙丘：香料与武装','三国：乱世苍生','涌变兽铺','行动与自动','寻常','巡妖','牌与枪','午夜机台','BALLRENA','御龙修仙之踏天证道','见证者'],1):
    d=copy.deepcopy(by['J114-01']);d.update(candidate_id=f'J113-{i:02d}',source_ids=['S0113'],entities=[product],event=product+'开发或试玩信息',reason='E3×R0+M0=0；独立开发项目逐条召回，暂无主体影响力支持。')
    d['subject_assessment']['subject']=product
    d['pc_release_scope']['evidence']=[quote(113,product)]
    d['time_check']=build_time_check(['S0113'],SRC,DAY,DAY,basis='本期独立游戏通讯来源窗口有效，历史开发日期不作行业门禁。')
    decisions.append(d);by[d['candidate_id']]=d

# AI audit: all native AI records plus industry reverse scan and newsletter.
ai_main={73:('direct_application',['development'],'研发全流程采用与项目结果已有可核验自述'),
         92:('direct_application',['development','operations'],'AI已用于PS5漏洞发现并获得赏金，有采访证据'),
         205:('direct_application',['development','publishing','product'],'Meta提示词制作及社交流分发已有具体工具与负责人访谈')}
for n in list(range(148,171))+[6,7,42,44,47,73,87,91,92,113,114,131,136,142,205]:
    cid=f'A{n:03d}'; typ,stages,why=ai_main.get(n,('direct_application',['development'],'来源没有可核验的新增游戏采用机制，或在直接应用三条后不优先采用泛工具/观点。'))
    if n in range(148,170):
        typ='transferable_frontier';why='优先本期三条游戏直接应用；该条为通用模型、研究、融资或企业工具信息，未形成更优先的游戏采用事件。'
    if n==170:why='Mutable是运行时角色定制工具，本文222字未证明AI机制；不能凭原始AI分类入选。'
    if n in [47,91]:why='Sweeney对既有披露政策继续表态，没有新政策或实证采用结果；低于本期实证案例优先级。'
    if n==7:why='与10月26日已写Creative Assembly外包审核说明同一内容，本期短摘无新增。'
    d={'candidate_id':cid,'section':'ai_trends','source_ids':[sid(n)],'entities':[SRC[sid(n)]['title']], 'event':SRC[sid(n)]['title'],
       'decision':'include' if n in ai_main else 'exclude','reason':why,'ai_tier':typ,'game_stage':stages,'industry_reverse_scan':n<148}
    if typ=='transferable_frontier':d['migration_path']='通用能力→游戏研发/运营辅助的潜在迁移；尚未证明游戏使用或优于直接应用案例。'
    decisions.append(d);by[cid]=d

# Community pool scan, with original time blocks inspected to avoid consuming October 28 replies.
for n in range(189,205):
    text=SRC[sid(n)]['text']; dates=re.findall(r'发帖：(\d{4}-\d{2}-\d{2}T[0-9:]+)',text)
    cm={'trigger':SRC[sid(n)]['title'],'claim_scope':'帖子及所引内容，不代表官方事实或全部玩家共识',
        'complaint_logic':'按本帖触发机制核对，不把调侃、推测升级为事实。','timeline':dates,
        'follow_up_scan':{'source_pool_count':209,'community_count':16,'query_terms':[SRC[sid(n)]['title']],
                         'result':'已反扫本期全部行业、AI和16条社区来源；28日回复不纳入27日叙事。'}}
    reason='旧帖仅有延续热度、无本期可核验新状态，或触发信息/争议机制不足；不按回复量选材。'
    if n in [190,197,199,193]:reason='同事件已在行业新闻处理，不重复入选社区。'
    if n==204:reason='本期新触发，有明确宣传内容与角色专属感的冲突机制；仅用玩家归因，不写未证实海外趋势或卡车行动为事实。'
    if n==191:reason='当日讨论存在，但只有剪辑转述及宏观AI立场，缺少游戏层面具体采用；优先完整可归因事件。'
    d={'candidate_id':f'C{n:03d}','section':'community_discourse','source_ids':[sid(n)],'entities':[SRC[sid(n)]['title']],
       'event':SRC[sid(n)]['title'],'decision':'include' if n==204 else 'exclude','reason':reason,'community':cm}
    decisions.append(d);by[d['candidate_id']]=d
cm={'trigger':'EA宣布关闭BioWare并取消下一部Mass Effect后，玩家发起保存系列的请愿并购买时代广场广告',
    'claim_scope':'媒体采访、请愿文本及粉丝组织公开广告信息；不推断EA将出售IP',
    'complaint_logic':'希望持续投入游戏开发，或授权愿意继续制作的工作室；担忧系列只剩影视改编',
    'timeline':['2026-10-21 EA宣布工作室关闭与项目取消','2026-10-26 粉丝公开时代广场广告','2026-10-27 报道追踪请愿与线下行动'],
    'follow_up_scan':{'query_terms':['Mass Effect','BioWare','EA','petition','SaveMassEffect'],'source_ids':['S0011','S0045','S0077','S0122','S0126'],
        'result':'核对同窗行业及16条社区池；作曲家试写配乐是独立侧面，未混入广告事件；无证据证明EA已同意诉求。'}}
decisions.append({'candidate_id':'C045','section':'community_discourse','source_ids':['S0045','S0122'],'entities':['EA','Mass Effect'],
 'event':'Mass Effect玩家请愿并投放时代广场广告','decision':'include','reason':'旧关闭事件在本期出现可核验的请愿及线下传播升级；与行业栏目不重复。','community':cm})
by['C045']=decisions[-1]

# Deep candidates: native newsletter first, then comparable developer evidence, merged at theme level.
deep={'candidate_id':'D205','section':'deep_analysis','source_ids':['S0205','S0073'],'entities':['Meta Horizon','我的奶茶屋'],
 'event':'AI降低制作门槛后，分发和商业验证成为约束','decision':'include',
 'reason':'本期newsletter优先；平台负责人访谈与实际小团队结果共同解释效率、获客、商业化之间的断点；与上期长青MMO服务器减负主题不同。',
 'scores':{'relevance':3,'insight':3,'evidence':3,'card':3,'total':12},'topic_key':'AI制作与分发｜产能不等于商业闭环｜迭代与流量验证'}
decisions.append(deep);by['D205']=deep
for n in [206,207,208,209]:
    decisions.append({'candidate_id':f'D{n:03d}','section':'deep_analysis','source_ids':[sid(n)],'entities':[SRC[sid(n)]['title']],
      'event':SRC[sid(n)]['title'],'decision':'exclude','reason':'数据事实可为新闻，独立深度缺少超过入选AI主题的完整机制链；206仅摘要，208为7月数据，209还与既往9月发行商口径有差异。',
      'scores':{'relevance':3,'insight':1,'evidence':1 if n==206 else 2,'card':1,'total':6 if n==206 else 7}})

# Corrections to extraction audit and full product-level calendar recall. Raw inputs remain untouched.
audit=json.loads((P/('release_calendar_audit_extracted.json' if (P/'release_calendar_audit_extracted.json').exists() else 'release_calendar_audit.json')).read_text(encoding='utf-8'))
save('release_calendar_audit_extracted.json',audit)
nodes=audit['nodes']; corrections=[]
def node(product,date,typ,event,nums,es,reason='',eligible=True):
    ids=[sid(n) for n in nums];ind=[s for s in ids if SRC[s]['section']=='industry_news'];rel=[s for s in ids if SRC[s]['section']=='release_calendar']
    fingerprints=list(dict.fromkeys(hashlib.sha1((SRC[s]['url']+'\n'+SRC[s]['text']).encode()).hexdigest() for s in ids))
    count=len(fingerprints);strength=(3 if count>=3 else count)+int(bool(ind));scope='report_window' if date==DAY else 'next_day_lookahead' if date=='2026-10-28' else 'future_announcement' if typ in ['new_game_schedule','new_game_first_reveal'] else 'outside'
    win=scope!='outside';return {'product':product,'event_date':date,'signal_type':typ,'event':event,'event_type_score':es,'first_seen_order':len(nodes),
      'observed_signal_types':[typ],'observed_events':[event],'industry_ids':ind,'release_ids':rel,'source_ids':ids,'source_fingerprints':fingerprints,
      'appearance_count':count,'appearance_score':min(count,3),'industry_bonus':int(bool(ind)),'source_strength_score':strength,'base_priority_score':es*strength,
      'focus_companies':[],'focus_company_relationships':{},'company_evidence_ids':[],'company_relationship':'none','company_bonus':0,'priority_score':es*strength,
      'multi_source_eligible':count>=2,'window_eligible':win,'window_scope':scope,'publish_eligible':eligible and count>=2 and win,
      'coverage':'industry+release' if ind and rel else 'industry_only' if ind else 'release_only','coverage_rank':3 if ind and rel else 2 if ind else 1,
      'status':'reviewed','editorial_reason':reason}
bad={'GTA6':'周知未来发售日及请假调查，不是本期首次定档/上线；抽取将未来事件错绑当日。',
 '星塔旅人':'2025年10月历史上线，且米哈游只是对比对象，撤销错误公司加分。',
 '王者万象棋':'11月6日是新棋手上线，不是新品定档。',
 '代号二杠三':'本期是停研报道，2024年首曝是背景；研发主体不是库洛。',
 '无畏契约':'国服上线三周年与注册用户里程碑，不是新品上线。',
 'Bus Fever Party':'今年7月上线为历史背景，不是本期新品。',
 '恋与深空':'单张五星思念的普通运营更新，不是新品上线。',
 '挨饿荒野-沙盒生存冒险':'老产品地图更新，不是新品上线。',
 '羊蹄山之魂':'裁员报道提到此前完全版与老发售，不是本期跨平台上线。'}
for x in nodes:
    name=x['product']
    if name in bad:
        x['publish_eligible']=False;x['editorial_reason']=bad[name];x['status']='rejected_false_positive';corrections.append(f"{name}：{bad[name]}")
        if name in ['星塔旅人','代号二杠三']:
            x.update(focus_companies=[],focus_company_relationships={},company_evidence_ids=[],company_relationship='none',company_bonus=0,priority_score=x['base_priority_score'])
    if name=='GTA6':x['source_ids']=['S0092','S0108']
    if name=='泡泡镇餐厅物语':
        x['signal_type']='new_game_launch';x['event']='新品上线';x['editorial_reason']='正文为现已登陆，没有抢先体验依据；仅单源。'
    if name=='奇点灰烬2':
        x['signal_type']='new_game_schedule';x['event_type_score']=2;x['base_priority_score']=2*x['source_strength_score'];x['priority_score']=x['base_priority_score'];x['event']='定档11月10日';x['editorial_reason']='正文未来11月10日发售，修正当日已上线误判。'
    if name=='影之刃零':
        # Merge the normalized 3839 record below; explicit date comes from its Event date field.
        x.update(node('影之刃零',DAY,'new_game_preload','PC版开启预下载',[14,182],2))
    if name.startswith('影之刃零-'):x['publish_eligible']=False;x['editorial_reason']='同产品同日预下载合并至规范产品名节点；不是另一次定档。'
    if name=='魔神英雄传' and x['signal_type']=='new_game_schedule':
        x.update(node('魔神英雄传',DAY,'new_game_preload','预下载，10月28日上线',[183],2,'仅单一来源'))
for product,date,block in compilation_games:
    nodes.append(node(product,date,'new_game_test' if 'EA' in block.splitlines()[2] else 'new_game_launch','Steam清单中的发售/抢先体验',[114],3,'仅单一发行清单来源；不把同媒体无日期推荐计作独立发售证据。'))
for args in [
 ('蕾卡的移动工坊',DAY,'new_game_launch','1.0正式版发售',[17,102],3,'两源确认正式版，但正文未写绝对日期；当前校验要求绝对日期证据，保持审计不发布。',False),
 ('ArcheAge Chronicles',DAY,'new_game_schedule','公布11月3日PC抢先体验',[184],2,'只有Google News标题摘要'),
 ('The Outlast Trials',DAY,'old_cross_platform_launch','Switch 2上线',[185],1,'只有Google News标题摘要'),
 ('Aloft',DAY,'new_game_schedule','宣布PS5版2027年初发行',[186],2,'只有Google News标题摘要'),
 ('Moonlight Peaks',DAY,'old_cross_platform_launch','宣布11月17日PS5版',[187],1,'只有Google News标题摘要'),
 ('BLEACH Mirrors High','2026-10-28','new_game_launch','10月28日发行',[188],3,'单源标题摘要'),
 ('大洋守护者',DAY,'new_game_preload','预下载',[181],2,'单源'),
 ('我带过的最差一届',DAY,'new_game_schedule','宣布11月10日发售',[39],2,'单源，其他新品节排名报道不提供同日定档事实'),
 ('灰烬遗证',DAY,'new_game_first_reveal','公布并计划2027年上半年发行',[147],2,'单源'),
 ('午夜机台','2026-10-21','new_game_test','网页试玩版开放',[113],3,'旧试玩时间，单源'),
 ('牌与枪','2026-10-24','new_game_test','四人试玩招募',[113],3,'仅单源招募'),
 ('BALLRENA',DAY,'new_game_test','Steam Demo开放',[113],3,'单源，日期不够明确')]:
    if not any(x['product']==args[0] and x['event_date']==args[1] for x in nodes):nodes.append(node(*args))
for x in nodes:
    if x.get('status')=='rejected_false_positive':continue
    # Strict calendar cross-report duplicate search, independent of industry selection.
    matches=[]
    for f in (ROOT/'output').glob('**/_intermediate/report_items.json'):
        if DAY in str(f) or not re.search(r'2026-\d\d-\d\d',str(f)):continue
        try:other=json.loads(f.read_text(encoding='utf-8'));other=other.get('items',[]) if isinstance(other,dict) else other
        except (ValueError,OSError):continue
        for it in other:
            rel=it.get('release') or {}
            if rel.get('product')==x['product'] and rel.get('date')==x['event_date']:matches.append(str(f.relative_to(ROOT)))
    x['prior_release_matches']=matches
    if matches:x['publish_eligible']=False;x['editorial_reason']='同产品同日期已在此前报告发布：'+'；'.join(matches)
nodes.sort(key=lambda x:(-int(x['publish_eligible']),-x['priority_score'],-x['company_bonus'],-x['event_type_score'],-x['appearance_count'],-x['industry_bonus'],x['first_seen_order']))
for i,x in enumerate(nodes,1):x['candidate_id']=f'release-candidate-{i:03d}'
audit['nodes']=nodes;audit['editorial_review']={'full_scan_sources':165,'normalization':'同产品+同事件日期','corrections':corrections,'news_data_modified':False}
save('release_calendar_audit.json',audit)

# Editorial source-grounded report text and claims.
def item(cid,title,body,claims,**extra):
    d=by[cid]; assert d['decision']=='include',cid
    cl=[]
    for text,n,ev in claims:
        assert text in body,(cid,text);quote(n,ev)
        cl.append({'claim':text,**quote(n,ev)})
    it={'section':d['section'],'candidate_id':cid,'title':title,'source_ids':d['source_ids'],'body':body,'claims':cl,**extra}
    items.append(it);return it
item('I022','米哈游《星布谷地》三测开放付费，月卡、季卡与外观抽取分层',
 '《星布谷地》三测开放付费后，米哈游展示了生活模拟产品的分层商业化安排。测试中，一期季节活动以90天为周期，68元基础季卡主要交付固定服饰与家具，18元月卡面向长期抽取资源积累。服饰池和家具池承接不同深度的收集需求；这些仍是测试规则，尚不能等同于最终上线方案。',[
 ('《星布谷地》三测开放付费后',22,'《星布谷地》三测开放付费后'),('米哈游',22,'米哈游也走到了'),('生活模拟',22,'生活模拟'),
 ('一期季节活动以90天为周期',22,'一期活动以90天为周期'),('68元基础季卡',22,'68元基础季卡包含120枚抽取货币、6件家具和3件服饰。'),
 ('18元月卡',22,'18元月卡则面向更长期的资源储备。'),('服饰池和家具池',22,'服饰池承接核心单品与套装收集，家具池继续拓展主题解锁和复数配置。')])
item('I030','灵犀《篮球少女：飞跃巅峰》开服三天后进入游戏畅销榜第4',
 '据游戏葡萄报道，灵犀的《篮球少女：飞跃巅峰》开服三天后登上App Store游戏畅销榜第4。产品将篮球题材、少女角色与局内随机养成结合，局外成长又持续影响训练收益，并设置异步PVP竞技场与PVE验证玩法。报道同时指出，单局约20分钟、每日多轮培养的时间负担，仍是长线体验需要面对的问题。',[
 ('灵犀的《篮球少女：飞跃巅峰》开服三天后登上App Store游戏畅销榜第4',30,'开服三天后，灵犀的《篮球少女：飞跃巅峰》登上了App Store游戏畅销榜第4。'),
 ('局外成长又持续影响训练收益',30,'局外对于角色养成的重要程度，与局内几乎一致。'),('异步PVP竞技场与PVE验证玩法',30,'一个是异步PVP的竞技场，另一个则是挑战强敌的PVE玩法「圣山模拟战」。'),('单局约20分钟',30,'单局20分钟在如今这个年代，客观上已经是一个负担')])
item('I025','《蔚蓝档案》日服将于2027年1月转交NEXON运营',
 '悠星日本社长李衡达在10月25日特别视频中宣布，自2027年1月起，《蔚蓝档案》日本地区发行与运营将由悠星移交开发商NEXON。报道指出，调整合作的意向约在一年前由NEXON提出，双方经过长期协商后确定移交。此次变更仅涉及日本地区，国服不受影响。',[
 ('悠星日本社长李衡达',25,'悠星日本社长李衡达'),('10月25日',25,'10月25日晚'),('自2027年1月起',25,'自2027年1月起'),
 ('《蔚蓝档案》日本地区发行与运营将由悠星移交开发商NEXON',25,'《蔚蓝档案》日本地区的发行和运营业务，将由悠星正式移交至开发商NEXON。'),
 ('约在一年前由NEXON提出',25,'大约一年前，NEXON便提出调整运营体制、结束合作的意向。'),('此次变更仅涉及日本地区，国服不受影响',25,'此次变更仅涉及日本地区，国服不会受到影响。')])
item('I063','Xbox首任首席运营官Helen Chiang任职三个月后离职',
 'Game Developer援引内部备忘录报道，Xbox首任首席运营官Helen Chiang已离开微软，距离该职位设立约三个月。她此前在微软工作21年，曾长期负责Minecraft，出任COO后承担端到端盈亏职责并向Asha Sharma汇报。报道指公司当时尚未确定继任安排，离职原因没有得到微软确认。',[
 ('Xbox首任首席运营官Helen Chiang已离开微软',63,'The first-ever Chief Operating Officer at Xbox has left her position'),
 ('约三个月',63,'just three months after it was created'),('在微软工作21年',63,'a 21-year-veteran of Microsoft'),('Minecraft',63,'overseeing Minecraft'),
 ('端到端盈亏职责',63,'end-to-end profit and loss duties'),('Asha Sharma',63,'CEO Asha Sharma'),('尚未确定继任安排',63,'plans are not currently in place for a successor')])
item('I064','据报Xbox拒绝Netflix的5亿美元影视改编提案',
 'Game Developer援引Puck报道，Netflix曾提出以5亿美元取得Xbox旗下IP七年的影视独家改编权。报道指Xbox希望将价格提高到8亿美元，Netflix随后退出谈判；这是一项未达成的提案。双方仍有其他改编项目合作，因此该报道并不意味着两家公司终止全部合作。',[
 ('Netflix曾提出以5亿美元取得Xbox旗下IP七年的影视独家改编权',64,"Netflix reportedly sought a $500 million deal with Microsoft's Xbox for seven years of exclusive rights to adapt its full suite of properties for TV and film."),
 ('Xbox希望将价格提高到8亿美元，Netflix随后退出谈判',64,'Xbox turned that deal down, trying to raise the asking price to $800 million, a number that seemingly caused Netflix to balk and walk away.'),
 ('双方仍有其他改编项目合作',64,'Netflix and Xbox are still working together on some adaptations.')])
item('I027','《宝可梦大集结》公布停运安排，国际服将于2027年3月关闭',
 '由宝可梦公司与天美工作室群共同研发的《宝可梦大集结》公布停运安排：国际服的Switch与手机版将于2027年3月23日停止服务，国服公告则定于2027年1月停运。国际服自10月27日起停止出售亿奥斯宝石，并暂停新会员及自动续订；已有宝石可在停服前使用。停止服务器后，玩家将不能登录或参加对战。',[
 ('由宝可梦公司与天美工作室群共同研发',27,'由宝可梦公司与天美工作室群共同研发的产品'),('《宝可梦大集结》',27,'《宝可梦大集结》'),
 ('2027年3月23日',50,'March 23, 2027'),('Switch与手机版',50,'Nintendo Switch and mobile devices'),('2027年1月停运',27,'2027 年 1 月停运'),
 ('自10月27日起停止出售亿奥斯宝石',50,'As of today (October 27, 2026), players can no longer purchase Aeos gems'),
 ('暂停新会员及自动续订',50,'New Unite Club memberships and automatic renewals have been suspended.'),('已有宝石可在停服前使用',50,'Existing Aeos gems can be used until the shutdown date.'),
 ('不能登录或参加对战',50,'players will no longer be able to log in or participate in battles')])
item('I010','微软将Arkane Lyon寻找买家的协商期延长一个月',
 '据IGN中文报道，微软将Arkane Lyon寻找买家的协商期再延长一个月，并探索由合作方支持工作室完成《漫威刀锋战士》后续开发的方案。报道指原有寻找新东家的期限为11月13日；若无法达成保留方案，工作室217名员工将面临失业风险。微软称延期有明确期限，并会继续向职工委员会通报进展，目前尚未宣布买家或合作已经落定。',[
 ('微软将Arkane Lyon寻找买家的协商期再延长一个月',90,'微软将这一期限延长了一个月。'),('支持工作室完成《漫威刀锋战士》后续开发',90,'支持Arkane Lyon完成《漫威刀锋战士》开发的可能性'),
 ('11月13日',90,'11月13日前找到新东家'),('217名员工',90,'217名员工'),('延期有明确期限',90,'此次延期有明确期限'),('职工委员会',90,'向职工委员会通报进展')])
item('I068','腾讯魔方筹划《Roco Kingdom》2027年西方市场发行',
 'Mobilegamer本期报道提到，腾讯旗下魔方工作室的《Roco Kingdom》此前已在科隆游戏展面向西方市场亮相，团队正筹划2027年发行。报道将其与该工作室的《Arena Breakout: Infinite》并列介绍；当前材料没有给出具体上线日期。',[
 ('腾讯旗下魔方工作室',68,'Morefun, the Tencent studio'),('《Roco Kingdom》此前已在科隆游戏展面向西方市场亮相',68,'debuted Roco Kingdom in the west at Gamescom'),
 ('筹划2027年发行',68,"has big plans for the game's launch in 2027"),('《Arena Breakout: Infinite》',68,'Arena Breakout: Infinite')])
item('I033','9月手游出海榜呈现多产品竞争，点点互动包揽收入榜第2至4名',
 'Sensor Tower的2026年9月中国手游出海榜显示，点点互动三款产品包揽收入榜第2至4名，《Tasty Travels》截至发稿的累计海外收入估算已超过4.5亿美元。增长榜方面，益世界《疯狂水世界》位居首位；《Bus Fever Party!》当月超过1500万次下载，环比增长330%。收入榜按应用商店内购预估，不含广告变现、中国大陆地区及第三方安卓渠道。',[
 ('2026年9月中国手游出海榜',207,'2026年9月中国手游海外市场收入及下载量排行榜'),('点点互动三款产品包揽收入榜第2至4名',207,'点点互动旗下三款产品包揽第2至第4名'),
 ('《Tasty Travels》截至发稿的累计海外收入估算已超过4.5亿美元',207,'该游戏在截止发稿日，累计海外收入已突破4.5亿美元'),('《Tasty Travels》',207,'《Tasty Travels: Merge Game》'),
 ('益世界《疯狂水世界》位居首位',207,'益世界旗下《疯狂水世界》位居榜首'),
 ('《Bus Fever Party!》当月超过1500万次下载，环比增长330%',207,'9月下载量突破1500万次，环比增长330%'),('《Bus Fever Party!》',207,'《Bus Fever Party!》'),
 ('不含广告变现、中国大陆地区及第三方安卓渠道',207,'不包括⼴告变现、中国大陆地区及第三方安卓渠道收入')])
item('I206','QuestMobile：手机游戏占抖音小程序分类数量60%',
 'QuestMobile秋季全景生态报告摘要显示，抖音小程序中手机游戏与移动视频的数量占比分别为60.0%和22.0%。同一摘要称，截至2026年8月，中国移动互联网月活用户规模为12.78亿，同比增长0.9%。前一组衡量小程序供给分类，后一组衡量全移动互联网用户规模，二者不能混算为游戏渗透率。',[
 ('抖音小程序中手机游戏与移动视频的数量占比分别为60.0%和22.0%',206,'抖音小程序手机游戏和移动视频数量占比分别为60.0%和22.0%。'),
 ('截至2026年8月，中国移动互联网月活用户规模为12.78亿，同比增长0.9%',206,'截止到2026年8月，中国移动互联网月活用户规模达到12.78亿，同比微增0.9%。')])
item('I208','7月收入回顾：中国38家手游发行商占全球百强收入42.6%',
 'Sensor Tower的2026年7月发行商收入回顾显示，当月38个中国厂商进入全球手游发行商收入前100，合计收入预估23亿美元，占百强42.6%。该口径覆盖App Store与Google Play，不含第三方安卓商店，中国大陆只计iOS。上述数字对应7月统计期，与9月榜单分别陈述。',[
 ('38个中国厂商进入全球手游发行商收入前100，合计收入预估23亿美元，占百强42.6%',208,'2026年7月共38个中国厂商入围全球手游发行商收入榜 TOP 100，合计吸金23亿美元，占本期全球 TOP 100手游发行商收入42.6%。'),
 ('App Store与Google Play',208,'App Store 与 Google Play'),('不含第三方安卓商店，中国大陆只计iOS',208,'不包含第三方 Android 应用商店数据（中国大陆市场仅统计 iOS 端）'),('7月统计期',208,'2026年7月')])

item('A073','《我的奶茶屋》复盘：AI减少研发人手，获客与商业化仍未达预期',
 '《我的奶茶屋》开发者复盘称，重启项目由原本需要6人的研发缩至2人，策划、美术、SDK、封装和出包等环节均有AI参与。产品后来上线TapTap并产生收益，但新增用户与商业化结果没有达到预期，开发者决定停止继续投入，将经验用于后续项目。这个案例体现的是生产效率改善，不能直接推导出流量、收入或项目成功率同步提高。',[
 ('由原本需要6人的研发缩至2人',73,'原来这个项目研发加起来需要 6 个人，这次重启一共只有 2 个人'),('策划、美术、SDK、封装和出包等环节均有AI参与',73,'策划、美术，到后面的 SDK、封装和出包，各个环节都有 AI 参与。'),
 ('上线TapTap',73,'后来上线 TapTap'),('产生收益',73,'也带来了一定收益'),('新增用户与商业化结果没有达到预期',73,'新增用户和商业化结果没有达到我的预期'),('决定停止继续投入',73,'我决定不再继续投入')])
item('A205','Meta谈提示词游戏商业化：加快迭代，并接入移动端与社交流分发',
 'Meta Horizon负责人Saxs Persson在The Game Business访谈中介绍，Horizon Studio与Horizon Create允许用文本提示制作游戏，并直接发布到移动端以及Instagram、Facebook等社交流。工具在上个月已公布；本次访谈强调的是反复试玩、修改与社区反馈，而非一次生成就完成商业产品。Persson认为这对独立团队存在创业机会，同时明确当前形态并不适合让3A团队直接整体迁入。',[
 ('Meta Horizon负责人Saxs Persson',205,'Meta Horizon VP Saxs Persson'),('Horizon Studio与Horizon Create',205,'Horizon Studio and Horizon Create'),('Instagram、Facebook',205,'Instagram and Facebook'),
 ('文本提示制作游戏',205,'make games using text prompts'),('工具在上个月已公布',205,'Last month, Meta revealed Horizon Studio and Horizon Create.'),
 ('反复试玩、修改与社区反馈',205,'iteration, testing, trying and repeating'),('并不适合让3A团队直接整体迁入',205,'Is it a business opportunity for a triple-A team to switch to this platform right now? No.')])
item('A092','研究者借助AI发现PS5漏洞并领取赏金，主机安全披露节奏受到影响',
 'IGN采访的研究者Jordy称，他借助生成式AI发现PS5虚拟机监控器漏洞，通过HackerOne向索尼报告后获得5万美元赏金。争论集中在披露时间：部分自制软件社区成员希望将漏洞保留到《GTA6》发售后，而Jordy表示另有研究者也在借助模型发现同一漏洞，因此选择先行上报。AI已进入主机安全研究，多名研究者同时发现同一漏洞，也使保留漏洞与提前上报之间的时间选择更紧迫。',[
 ('研究者Jordy称，他借助生成式AI发现PS5虚拟机监控器漏洞',92,'在与IGN交谈时，Jordy承认，他借助生成式AI发现了这个让他获得5万美元赏金的漏洞。'),('虚拟机监控器漏洞',92,'虚拟机监控器漏洞（Hypervisor Bug）'),
 ('通过HackerOne向索尼报告后获得5万美元赏金',92,'他通过HackerOne提交了漏洞报告'),('5万美元赏金',92,'5万美元赏金'),('希望将漏洞保留到《GTA6》发售后',92,'想等《GTA6》发售后再上报'),('另有研究者也在借助模型发现同一漏洞',92,'其他研究者正借助生成式AI陆续发现它')])

# Decisions are written after candidates but before final text, then release sync is mandatory.
meta={'report_type':'daily','report_window':{'start':DAY,'end':DAY},'scoring_version':'subject_genre_v2','industry_timing_version':'source_window_v1',
      'history_window':H['history_window'],'archive_occurrences_checked':len(H['archive_occurrences']),'decisions':decisions}
save('selection_decisions.json',meta)
sync(P/'release_calendar_audit.json',P/'selection_decisions.json',4)
meta=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8')); decisions=meta['decisions']; by={d['candidate_id']:d for d in decisions}
for d in decisions:
    if d['section']=='release_calendar':
        x=next(x for x in nodes if x['candidate_id']==d['candidate_id'])
        if x.get('editorial_reason') and d['decision']=='exclude':d['reason']=x['editorial_reason']+'；'+d['reason']
save('selection_decisions.json',meta)
for x in nodes:
    if by[x['candidate_id']]['decision']=='include':
        assert x['product']=='影之刃零',x
        body='武侠动作端游《影之刃零》于10月27日开启PC版预下载，计划10月29日上线；预下载需预留300GB可用空间。'
        items.append({'section':'release_calendar','candidate_id':x['candidate_id'],'title':'影之刃零','source_ids':x['source_ids'],'body':body,
          'release':{'product':'影之刃零','event':'PC版预下载','date':DAY,'platform':'PC','company':''},
          'claims':[{'claim':'《影之刃零》','source_id':'S0014','evidence':'《影之刃零》PC版现已开启预下载'},
                    {'claim':'武侠动作端游','source_id':'S0072','evidence':'表里武林世界'},
                    {'claim':'10月27日','source_id':'S0182','evidence':'Event date: 2026-10-27 10:00'},
                    {'claim':'10月29日上线','source_id':'S0182','evidence':'10月29日上线'},
                    {'claim':'300GB可用空间','source_id':'S0014','evidence':'需要300GB可用空间'}]})
        # Genre is not inferred from the title: source72's full review directly establishes wuxia/action.
        it=items[-1];it['source_ids'].append('S0072')
        it['claims'][1]['evidence']='表里武林世界'
item('C045','《质量效应》玩家请愿延伸至时代广场广告，要求续作投入或授权',
 'EA于10月21日宣布关闭BioWare并结束下一部《质量效应》的开发后，玩家组织将“拯救系列”的诉求从线上请愿延伸到纽约时代广场广告。PC Gamer追踪了粉丝组织10月26日公开的广告行动；请愿要求EA承诺继续游戏开发、提供资金与人员，或将IP授权给愿意延续系列的工作室。玩家不满的核心在于工作室关闭与项目取消，让系列未来能否继续作为游戏存在失去保障。',[
 ('EA于10月21日宣布关闭BioWare并结束下一部《质量效应》的开发',45,'EA announced on October 21 that it was closing down Mass Effect and Dragon Age developer BioWare after more than 30 years , ending development on the next Mass Effect project.'),
 ('纽约时代广场广告',122,"has rented out digital billboard space in New York's Times Square"),('10月26日',122,'October 26, 2026'),
 ('提供资金与人员',45,'proper funding, adequate staffing, and time allocation'),('将IP授权给愿意延续系列的工作室',45,'licensing the Mass Effect intellectual property (IP) to another studio')],community=by['C045']['community'])
item('C204','玩家质疑《恋与深空》引用《银翼杀手》的宣传削弱角色专属感',
 '《恋与深空》相关宣传被NGA帖内玩家解读为引用《银翼杀手》中乔伊形象出现在商业广告中的场面，10月27日由此引发对角色专属感的讨论。玩家不满的核心在于，原场景把亲密对象呈现为可复制、服务多人的商品，将它用于男主宣传，会让部分玩家感到恋爱幻想被官方主动打破。也有回复质疑，这种不满是否忽略了其他玩家同样与角色互动的产品现实；讨论体现了宣传典故与恋爱产品情感预期之间的冲突。',[
 ('《恋与深空》',204,'《恋与深空》'),('10月27日',204,'发帖：2026-10-27T11:37'),('引用《银翼杀手》中乔伊形象出现在商业广告中的场面',204,'主角在大街上看到乔伊的形象被用在广告上'),
 ('用于男主宣传',204,'此片段被用作恋与深空男主宣传致敬'),('可复制、服务多人的商品',204,'她在服务无数人，只是个资本商品'),('感到恋爱幻想被官方主动打破',204,'打破本该保持的幻想'),('其他玩家同样与角色互动',204,'难道没有共享老公吗，那她们怎么看待其他玩家的呢')],community=by['C204']['community'])
deep_body='''观察：AI正把小团队做出可玩作品的门槛降低，但制作效率与商业闭环之间仍有一段距离。本期Meta关于提示词创作与社交流分发的访谈，以及《我的奶茶屋》开发者的项目复盘，分别从平台和团队两端暴露了这个问题：增加供给，是否也能带来持续的用户与收入？

分析：Meta的Horizon Studio与Horizon Create允许通过文本提示制作游戏，并向移动端、Instagram和Facebook等社交流发布。负责人Saxs Persson强调迭代、测试与社区联系，并明确当前形态尚不适合3A团队整体迁入。这一方案试图同时缩短制作和触达用户的路径：工具让原型修改更便宜，分发入口让试玩更接近已有受众。但平台负责人对创业机会的判断，仍不是创作者普遍获利的实证。

分析：《我的奶茶屋》的重启团队从原先需要6人缩至2人，多个研发环节都有AI参与，产品上线后却因新增用户和商业化结果未达预期而停止继续投入。它提示了生产瓶颈松动后可能出现的下游约束：做得更快没有自动补足获客、曝光和商业验证能力。如果通用工具也让竞争者同步提速，单纯的人天节省就很难长期成为差异。这些材料支持的是将效率与分发分开验证，尚未证明AI制作的整体成败，或社交流入口已经解决了发现问题。'''
it=item('D205','AI降低制作成本后，游戏商业验证仍取决于分发与用户关系',deep_body,[
 ('Horizon Studio与Horizon Create',205,'Horizon Studio and Horizon Create'),('Instagram和Facebook',205,'Instagram and Facebook'),('Saxs Persson',205,'Saxs Persson'),
 ('尚不适合3A团队整体迁入',205,'Is it a business opportunity for a triple-A team to switch to this platform right now? No.'),
 ('从原先需要6人缩至2人',73,'原来这个项目研发加起来需要 6 个人，这次重启一共只有 2 个人'),('新增用户和商业化结果未达预期',73,'新增用户和商业化结果没有达到我的预期'),
 ('停止继续投入',73,'我决定不再继续投入'),('单纯的人天节省就很难长期成为差异',73,'AI 提速是全行业都能拿到的能力。我能用，其他团队也能用。')],
 card_copy={'source_label':'The Game Business访谈与GameRes开发复盘','summary':'AI缩短了制作链路，但游戏能否形成商业闭环，仍取决于迭代、触达用户与商业验证。',
 'insights':[{'title':'产能增加不等于用户增加','detail':'《我的奶茶屋》以两人完成原需六人的研发，新增和商业化仍未达预期。'},
             {'title':'平台尝试连接制作与分发','detail':'Meta把提示词工具接入移动端和社交流，但创业机会仍不等于普遍获利。'},
             {'title':'迭代比一次生成更关键','detail':'Meta访谈强调测试和社区联系，工具降低的是每轮修改成本。'},
             {'title':'通用提速仍需商业验证','detail':'竞争者也能采用同类工具，获客与用户关系不会随研发成本自动改善。'}]})

items.sort(key=lambda it:({'industry_news':0,'ai_trends':1,'release_calendar':2,'community_discourse':3,'deep_analysis':4}[it['section']],
    -by[it['candidate_id']].get('scores',{}).get('total',0) if it['section']=='industry_news' else 0,
    -by[it['candidate_id']].get('scores',{}).get('relevance',0) if it['section']=='industry_news' else 0,
    -by[it['candidate_id']].get('scores',{}).get('event',0) if it['section']=='industry_news' else 0))

# Candidates and decisions are materialized before report_items and the final draft.
head=['# 2026-10-27 候选审计','', '全量读取209条JSONL；完整index五分区计数核对209。行业来源published_at取Asia/Shanghai；source_window_v1不以历史事件日期排除。',
 '双周窗口2026-10-13至2026-10-26，100条；更早归档1025条，JSON与同名Markdown同步读取。','']
for d in decisions:
    qs=[]
    if d.get('subject_assessment'):qs=d['subject_assessment']['evidence']
    if not qs:
        n=d['source_ids'][0]; t=SRC[n]['text'];qs=[{'source_id':n,'evidence':next((line for line in t.splitlines() if line.strip() and not line.startswith('http')),t)}]
    head += [f"## {d['candidate_id']} - {d['event']}",f"- section: {d['section']}",'- status: candidate',f"- source_ids: {', '.join(d['source_ids'])}",
             '- entities: '+', '.join(d['entities']), '- facts: '+'；'.join(q['evidence'] for q in qs),'- notes: '+d['reason'],'']
    if d.get('community'):
        head += [f"- {k}: {json.dumps(v,ensure_ascii=False)}" for k,v in d['community'].items()]+['']
(P/'event_candidates.md').write_text('\n'.join(head),encoding='utf-8')
md=['# 2026-10-27 选择决策','',
 '卡片曝光去重：双周100条与更早1025条均查。Steam个人日历历史第5/10、Top Lords同月SLG报告第5/10、9月发行商榜第3/10及周报第8/10均card_exposed=true，repeat_only排除；篮球少女历史第7/10、Xbox任命历史第2/10已曝光，但本次分别有实际开服与负责人离职的实质更新。card_carryover=0，无此前排名需补位。',
 '行业时间口径：source_window_v1；当前报道自身published_at优先，缺失回退date；旧事件不是门禁。Roco既往展会亮相按历史语态入选，使命召唤里程碑按E1评分而非因事件早排除。',
 '维度覆盖自检：国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均已由全量输入成卡；具体计数见run_summary.json。名单外R按影响力开放分层，不按未列名封顶。',
 '产品日历漏挂反查：无行业↔日历互斥；165条行业与日历输入反扫。保留原抽取审计快照并修正未来发售、旧上线、背景公司误归属；单源、日期与跨期门禁分别执行。',
 '深度交接：星期三日报，无周五selection消费。newsletter优先审查，Meta与小团队AI案例主题级合并一条。', '', '| candidate | decision | target_section | reason |','| --- | --- | --- | --- |']
for d in decisions:md.append(f"| {d['candidate_id']} | {d['decision']} | {d['section']} | {d['reason'].replace('|','/')} |")
(P/'selection_decisions.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
save('report_items.json',{'report_type':'daily','date':DAY,'items':items})
sections={'industry_news':'一、行业新闻','ai_trends':'二、AI 新闻','release_calendar':'三、新游发布 / 产品日历','community_discourse':'四、玩家舆论 / 社区动态','deep_analysis':'五、行业精选 / 深度观察'}
report=['# 游戏行业日报｜2026-10-27','']
for sec,label in sections.items():
    report += ['## '+label,'']
    for i,it in enumerate([it for it in items if it['section']==sec],1):
        report += ['- '+it['body'],''] if sec=='release_calendar' else [f"### {i}. {it['title']}",'',it['body'],'']
draft=P/'draft'/'game_industry_daily_2026-10-27.md';draft.parent.mkdir(exist_ok=True)
draft.write_text('\n'.join(report),encoding='utf-8')
summary={'anchor':'今天是星期三，应生成日报，date=2026-10-27','counts':{sec:sum(it['section']==sec for it in items) for sec in sections},
 'input_records':len(ROWS),'history_window':H['history_window'],'recent_occurrences':100,'archive_occurrences':1025,
 'industry_included':[{'title':it['title'],**by[it['candidate_id']]['scores']} for it in items if it['section']=='industry_news'],
 'boundary_3_4':[{'candidate_id':d['candidate_id'],'event':d['event'],**d['scores']} for d in decisions if d['section']=='industry_news' and d.get('scores',{}).get('total') in [3,4] and d['decision']!='merge'],
 'repeat_only':[d['candidate_id'] for d in decisions if d.get('history_check',{}).get('novelty')=='repeat_only'],
 'material_updates':[{'candidate_id':d['candidate_id'],'new_facts':d['history_check']['new_facts']} for d in decisions if d.get('history_check',{}).get('novelty')=='material_update'],
 'card_carryover':[],'deep_handoff':'日报，无周五选择交接',
 'warnings':['9条PocketGamer为受阻摘要，未用作正文证据。','机核与Mobilegamer多条很短，限于直接支持的事实；本期Roco仅两句规划信息。','未采集到Steam榜单输入，本期未生成榜单。','日历REKA两源但缺绝对日期正文，留审计不发布。','9月发行商榜本期36家/40.4%与历史37家/41.6%差异未解释，不以该差异虚构实质更新。'],
 'run_time':datetime.now().astimezone().isoformat()}
save('run_summary.json',summary)
(P/'release_calendar_corrections.md').write_text('# 产品日历审校\n\n'+'\n'.join('- '+s for s in corrections)+'\n\n蕾卡的移动工坊两源确认，但日期文本缺口未补造；影之刃零按规范名与2026-10-27预下载合并。\n',encoding='utf-8')
print(json.dumps({'draft':str(draft),'counts':summary['counts'],'decisions':len(decisions),'calendar_nodes':len(nodes)},ensure_ascii=False))
