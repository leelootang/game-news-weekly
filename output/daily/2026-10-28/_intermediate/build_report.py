"""Editorial decisions for the fixed 2026-10-28 daily window; local inputs only."""
import json, re, sys, hashlib, copy
from pathlib import Path
P=Path(__file__).parent
ROOT=P.parents[3]
sys.path.insert(0,str(ROOT/'scripts'))
from industry_timing import build_time_check
from sync_release_decisions import sync
DATE='2026-10-28'
rows=[json.loads(s) for s in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
inputs={r['source_id']:r for r in rows}
hist=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
history_md=(P/'industry_history_14d.md').read_text(encoding='utf-8')
history=hist['occurrences']+hist['archive_occurrences']
decisions=[]; items=[]; covered=set()
def sid(n): return f'S{n:04d}' if isinstance(n,int) else n
def txt(n): return inputs[sid(n)]['text']
def quote(n,needle):
 t=txt(n)
 assert needle in t,(n,needle)
 return next((s for s in t.splitlines() if needle in s),needle)
def ev(n,needle):return {'source_id':sid(n),'evidence':quote(n,needle)}
def dump(name,data): (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def prior(*terms):return [r for r in history if any(t.casefold() in (r['title']+' '+r['event']).casefold() for t in terms)]
def hcheck(matches=(),novelty='new_event',facts=()):
 return {'history_match':bool(matches),'novelty':novelty,'prior_occurrences':[r['report_kind']+' '+r['report_window']['start']+'_to_'+r['report_window']['end']+'｜'+r['title'] for r in matches], 'new_facts':list(facts),'prior_card_exposed':any(r['card_exposed'] for r in matches) if matches else None,'exposure_details':[{k:r.get(k) for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source','artifact']} for r in matches],'archive_checked':True}
def industry(cid,ns,event,E,R=1,M=0,subject='',kind=None,focus=(),basis='',evidence=None,genre=None,decision=None,gates=None,matches=(),novelty='new_event',facts=(),date='unknown',pc=None):
 ids=[sid(n) for n in ns];covered.update(ids)
 if decision is None:decision='include' if E and E*R+M>=5 else 'exclude'
 d={'candidate_id':cid,'section':'industry_news','source_ids':ids,'entities':[subject or event],'event':event,'decision':decision,'reason':basis or ('E0：常规运营、宣传、非游戏或没有独立业务变化。' if E==0 else '事件和主体逐项判断，低于统一5分线。'),'scores':{'event':E,'relevance':R,'hook':M,'total':E*R+M},'history_check':hcheck(matches,novelty,facts),'industry_reverse_scan':True}
 if len(ids)>1:d['cluster_basis']={'subject':subject or event,'product':subject or event,'event_date':date,'event':event}
 if E:
  kind=kind or {0:'other_or_unknown',1:'representative_subject',2:'comparable_significant_subject',3:'comparable_major_subject'}[R]
  q=evidence or [ev(ns[0],txt(ns[0]).splitlines()[0])]
  d['subject_assessment']={'subject':subject or event,'kind':kind,'focus_companies':list(focus),'basis':basis or '原文可识别产品/发行或平台主体，当前证据不足支持更高影响力档位。','evidence':q if R else []}
  if R==1:d['subject_assessment']['representative_product']=subject or event
  d['genre_assessment']={'matched_genres':[genre] if M else [],'basis':'本事件有明确竞技/重点品类证据，标签不叠加。' if M else '本事件未明确命中竞技、休闲SLG、生活模拟或数值卡牌RPG；不借集团其他产品加分。','evidence':[]}
  if M:d['genre_assessment']['evidence']=[ev(ns[0],genre_needle[cid])]
  d['time_check']=build_time_check(ids,inputs,DATE,DATE,event_date=date,basis='当前报道自身published_at优先，缺失回退输入date；事件日期不作准入门禁；核查近14天及更早已发布报告和卡片曝光。')
  if decision=='exclude': d['exclusion_gates']=gates or (['history_repeat'] if novelty=='repeat_only' else ['score'])
 if pc:
  d['pc_release_scope']={'classification':pc,'basis':'仅记录PC/主机范围；R依实际主体影响力判定，国产和平台本身均不抬分。','evidence':evidence or [ev(ns[0],txt(ns[0]).splitlines()[0])]}
 if novelty=='card_carryover' and decision=='include': d['card_carryover']=True
 decisions.append(d);return d
def item(d,title,body,claims,extra=None):
 it={'section':d['section'],'candidate_id':d['candidate_id'],'title':title,'source_ids':d['source_ids'],'body':body,'claims':[]}
 for c,n,needle in claims:
  assert c in body,(title,c)
  it['claims'].append({'claim':c,**ev(n,needle)})
 if extra:it.update(extra)
 items.append(it);return it
genre_needle={'I059':'During PvP matches','I036':'爆破模式公平竞技','I124':'MMO eスポーツ','I201':'life sim'}

# Main industry decisions, independently clustered by subject, event and actual date.
d=industry('I160',[160],'宝可梦大集结制作人杨思勤已转岗腾讯魔方',3,3,subject='腾讯天美/魔方',kind='focus_subject',focus=['腾讯'],basis='核心制作人转岗为组织变化E3；来源明确腾讯天美与腾讯魔方，主体R3；公司人事不借MOBA背景加M。',evidence=[ev(160,'制作人 杨思勤')])
item(d,'《宝可梦大集结》制作人杨思勤已转岗腾讯魔方','游戏新知报道，《宝可梦大集结》制作人杨思勤已转岗至腾讯魔方工作室群。他曾参与《元梦之星》大世界捉宠模式与《合金弹头：觉醒》开发，并在《魂斗罗：归来》担任助理制作人。本条关注制作人去向。', [('游戏新知报道',160,'游戏新知了解到'),('《宝可梦大集结》制作人杨思勤已转岗至腾讯魔方工作室群',160,'制作人 杨思勤'),('《元梦之星》大世界捉宠模式与《合金弹头：觉醒》开发',160,'《元梦之星》'),('《魂斗罗：归来》担任助理制作人',160,'助理制作人')])
# The already-reported shutdown is a separate event; no repackaging it as new personnel news.
industry('I160_STOP',[160],'宝可梦大集结国服与国际服停运安排',2,3,subject='腾讯',kind='focus_subject',focus=['腾讯'],basis='停运安排已于10月27日曝光；国服补全具体日不改变同一停运决定，不再次刊载。',evidence=[ev(160,'腾讯天美工作室群')],decision='exclude',matches=prior('公布停运安排'),novelty='repeat_only',gates=['history_repeat'])
d=industry('I239',[239],'Dan Ayoub升任Wizards of the Coast及Hasbro Digital Games负责人',3,3,subject='Wizards of the Coast/Hasbro Digital Games',basis='统辖Magic、D&D、Duel Masters及数字游戏的头部IP与发行主体，任命为E3，影响力可比头部主体取R3；AI仅背景不加M。',evidence=[ev(239,'head up Magic: The Gathering')])
item(d,'Dan Ayoub升任威世智与孩之宝数字游戏负责人','Dan Ayoub从数字游戏高级副总裁升任Wizards of the Coast与Hasbro Digital Games负责人，接替7月离职的John Hight，职责覆盖《万智牌》《龙与地下城》《Duel Masters》及数字游戏。他将统筹在研科幻RPG《Exodus》和动作冒险游戏《Warlock: Dungeons and Dragons》。孩之宝表示，他是经过内部与外部候选人遴选后，首位从内部晋升至该职位的人选。', [('Dan Ayoub',239,'Dan Ayoub'),('数字游戏高级副总裁',239,'senior vice president of digital games'),('Wizards of the Coast与Hasbro Digital Games负责人',239,'head up Magic: The Gathering'),('7月离职的John Hight',239,'John Hight, who left the position in July'),('《万智牌》《龙与地下城》《Duel Masters》',239,'Magic: The Gathering, Dungeons and Dragons, Duel Masters'),('《Exodus》',239,'Exodus'),('《Warlock: Dungeons and Dragons》',239,'Warlock: Dungeons and Dragons'),('首位从内部晋升至该职位',239,'first internal candidate')])
d=industry('I206',[206],'寂静岭初代重制项目及据报2027年目标档期',3,3,subject='科乐美/Bloober Team',basis='来源确认双方去年已宣布初代重制，属于既有新品立项E3，当前报道可消费；科乐美多作系列与600万份重制作品证明头部产品矩阵，R3；不因项目较早降E。报道目标档期须保留爆料归因。',evidence=[ev(206,'Bloober Team和科乐美'),ev(206,'双方将重制初代')],pc='ordinary_overseas_single_player')
item(d,'据报《寂静岭》初代重制版以2027年发售为目标','科乐美与Bloober Team去年已确认重制初代《寂静岭》。据IGN中文转述MP1ST爆料，该项目自2022年起开发，以2027年发售为目标，选角代号为“Project Noise”。这些开发时间和目标档期来自报道，尚不能写成官方正式定档。', [('科乐美与Bloober Team去年已确认重制初代《寂静岭》',206,'双方将重制初代'),('IGN中文转述MP1ST爆料',206,'据MP1ST最新爆料'),('自2022年起开发',206,'自2022年起便已展开'),('2027年发售为目标',206,'目标于2027年发售'),('Project Noise',206,'Project Noise')])
world_matches=prior('《王者荣耀：世界》执行制作人李新平')
d=industry('I130',list(range(130,135)),'王者荣耀世界4月17日移动端上线复盘',3,3,subject='腾讯',kind='focus_subject',focus=['腾讯'],basis='当前多语言报道回顾4月移动版正式上线，E3不因历史日期下降；腾讯直属R3；旧报告已记载4月公测但从未卡片曝光，竞争唯一card_carryover，9分高于Atari6分。',evidence=[ev(134,'テンセントが5年間')],matches=world_matches,novelty='card_carryover',date='2026-04-17',pc='domestic_or_focus')
item(d,'腾讯《王者荣耀：世界》4月移动版上线复盘：熟悉的英雄进入开放世界','游戏茶馆当期刊载的复盘回顾，《王者荣耀：世界》移动版于4月17日正式上线，补齐腾讯这一项目的移动端布局。文章认为，熟悉的英雄技能与角色故事被放入开放世界后，既降低了既有IP用户的理解成本，也让较长的叙事铺垫成为初期体验门槛。这是对当时产品结构的回看。', [('《王者荣耀：世界》移动版于4月17日正式上线',134,'4月17日'),('腾讯',134,'テンセントが5年間'),('熟悉的英雄技能与角色故事被放入开放世界',134,'馴染み深いスキルロジックが3D'),('较长的叙事铺垫成为初期体验门槛',134,'メインストーリーの伏線が長すぎ')])
d=industry('I059',list(range(59,65)),'Shiyue Network新品Dream Guardians的3月上线及早期表现复盘',3,2,1,subject='Shiyue Network',basis='来源显示前作iOS累计收入超4亿元，新作半月iOS下载360万、收入逾1300万元，构成细分市场较强发行与研运影响力R2；新品上线E3；明确PvP竞技M1，不借背景点点互动取R3。',evidence=[ev(59,'Shiyue Network’s *Eternal Blue Planet*'),ev(59,'revenue exceeding 13 million yuan')],genre='competitive',date='2026-03-17')
item(d,'Shiyue Network复盘《Dream Guardians》3月上线，强化阵容与局内构筑','游戏茶馆当期译稿回顾，Shiyue Network的《Dream Guardians》于3月17日上线；据文中引用的点点数据，截至3月29日，iOS累计下载约360万次、收入超过1300万元。产品削减前作的随机召唤与融合设计，转向固定英雄阵容和技能模块搭配，并提供PvP对战。上述数据属于3月的早期表现。', [('Shiyue Network的《Dream Guardians》',59,'Shiyue Network is capitalizing'),('3月17日上线',59,'on March 17—the day the game launched'),('截至3月29日，iOS累计下载约360万次、收入超过1300万元',59,'through March 29'),('固定英雄阵容和技能模块搭配',59,'fixed hero roster'),('PvP对战',59,'During PvP matches')])
d=industry('I030',[30],'世佳朗新AlipayHK战略合作及LumiGames出海品牌',3,2,subject='世佳网络/AlipayHK小游戏业务',basis='围绕小游戏平台开放、发行与支付进行正式战略合作E3；来源载明500万年活平台与过往100亿流水生态实战，具区域分发能力取R2；不凭蚂蚁背景自动当阿里R3。',evidence=[ev(30,'三方将围绕'),ev(30,'AlipayHK年活跃用户约500万')])
item(d,'世佳、朗新与AlipayHK合作，LumiGames承接海外钱包小游戏业务','世佳网络、朗新科技集团与AlipayHK在香港启动合作，联合品牌LumiGames成为内容与运营载体。AlipayHK提供流量入口、用户场景及支付能力，世佳负责游戏引入、发行运营与本地化，朗新提供钱包客户基础及平台商业化协同。项目计划先验证香港市场的内容需求与商业化，再扩大供给和用户规模。', [('世佳网络、朗新科技集团与AlipayHK在香港启动合作',30,'合作启动仪式在中国香港举行'),('LumiGames',30,'LumiGames'),('AlipayHK提供流量入口、用户场景及支付能力',30,'提供流量入口、用户场景和支付能力'),('世佳负责游戏引入、发行运营与本地化',30,'负责游戏引入、发行运营及本地化适配'),('先验证香港市场的内容需求与商业化',30,'先完成游戏中心搭建与内容引入')])
d=industry('I164',[164],'Charu Desodt接任BAFTA游戏委员会主席',3,2,subject='BAFTA Games Committee',basis='游戏行业奖项与专业组织的委员会核心负责人任命E3；跨工作室与行业委员会的组织影响力R2，不借其曾任Microsoft/Sony职位抬R3。',evidence=[ev(164,'appointed chair of the BAFTA Games Committee'),ev(164,'member of the UK Video Games Council')])
item(d,'Charu Desodt出任BAFTA游戏委员会主席','Interior Night工作室负责人Charu Desodt获任BAFTA游戏委员会主席，接替已加入Lego Digital Play的Tara Saunders。她拥有超过25年行业经验，曾在微软、索尼欧洲及Preloaded担任高级制作职务，也是英国电子游戏委员会成员。', [('Interior Night工作室负责人Charu Desodt获任BAFTA游戏委员会主席',164,'Interior Night studio head Charu Desodt'),('Tara Saunders',164,'Desodt succeeds'),('超过25年行业经验',164,'over 25 years'),('微软、索尼欧洲及Preloaded',164,'Microsoft, Sony Computer Entertainment Europe, and Preloaded'),('英国电子游戏委员会成员',164,'UK Video Games Council')])
d=industry('I251',[251],'GOG与Retrovibe启动Retrovibe by GOG发行业务',3,2,subject='GOG/Retrovibe',basis='DRM-free商店与独立发行商正式联合发行E3；全球PC店面、营销与跨平台发行能力构成R2，名单外不封顶R1。',evidence=[ev(251,'DRM-free storefront'),ev(251,'platform expertise, marketing capabilities')])
item(d,'GOG与Retrovibe联合发行，提供资金、营销与跨平台认证支持','GOG与独立发行商Retrovibe启动“Retrovibe by GOG”，面向PC商店和主机平台支持独立开发者。服务包括资金、营销、内容创作者与媒体沟通，以及发行认证；已列入阵容的作品有《Cop Bastard》和《Project Warlock: Lost Chapters》。两款游戏也有Steam页面，并非GOG独占。', [('GOG与独立发行商Retrovibe启动“Retrovibe by GOG”',251,'Retrovibe by GOG'),('PC商店和主机平台',251,'PC storefronts and consoles'),('资金、营销',251,'Funding, marketing'),('发行认证',251,'getting games certified'),('《Cop Bastard》',251,'Cop Bastard'),('《Project Warlock: Lost Chapters》',251,'Project Warlock: Lost Chapters'),('并非GOG独占',251,'not GOG-sclusives')])
d=industry('I241',[241],'Discord可发现服务器消息将纳入网页搜索',2,3,subject='Discord游戏社区平台',basis='游戏工作室论坛和wiki迁入Discord造成知识封闭，来源直接说明其游戏社区基础设施作用；平台级公开内容可发现性规则E2，头部社区分发平台R3。',evidence=[ev(241,'message boards were common'),ev(241,'biggest public servers searchable')])
item(d,'Discord拟于12月中旬开放部分公共服务器消息的网页搜索','Discord计划从12月中旬起，让指定“Discoverable Servers”频道中的问答出现在网页搜索中，涉及至少1000名用户的部分大型公共服务器。管理员可退出或限定可搜索频道，用户也可在隐私设置中退出；用户名与头像不会随消息显示。邀请制服务器和私信不在此次调整范围内，相关控制设置已开放。', [('12月中旬',241,'starting in mid-December'),('至少1000名用户',241,'1,000 or more users'),('管理员可退出或限定可搜索频道',241,'opt their server out, or limit web searches'),('用户也可在隐私设置中退出',241,'Users can opt out'),('用户名与头像不会随消息显示',241,'Usernames and avatars will not be shown'),('邀请制服务器和私信不在此次调整范围内',241,'does not affect any invite-only servers or DMs'),('相关控制设置已开放',241,'settings for server admins and users are now available')])
d=industry('I157',list(range(135,140))+[157],'Zero Creation Games复盘Ai Hong发售首日回本',3,2,subject='Zero Creation Games',basis='前作销量超过百万、历史AVG细分市场影响力支持R2；新品正式发售E3，首日约4万销量回本有制作者自述；不因清明历史日期降分，不把文化争议当官方事实。',evidence=[ev(157,'sold over a million copies'),ev(157,'sold approximately 40,000 copies')],pc='domestic_or_focus')
item(d,'Zero Creation Games回顾《Ai Hong》首日回本，AVG投入上限仍受市场约束','游戏茶馆当期译稿刊载了一场清明假期后的访谈：Zero Creation Games制作人Ji Ling称，《Ai Hong》首日约售出4万份并收回成本，采访时累计销量已超过8万份；前作销量则已超过百万。尽管新作同期销售领先前作，他仍预计未来两年的销售总量会稍低，并认为高投入AVG可能只会尝试这一次。这里记录的是该次访谈时点的数据与判断。', [('清明假期后的访谈',157,'On the first day after the Qingming Festival holiday'),('Zero Creation Games制作人Ji Ling',157,'Ji Ling at Zero Creation Games'),('《Ai Hong》首日约售出4万份并收回成本',157,'sold approximately 40,000 copies'),('累计销量已超过8万份',157,'exceeded 80,000 copies'),('前作销量则已超过百万',157,'sold over a million copies'),('未来两年的销售总量会稍低',157,'sales over the next two years'),('高投入AVG可能只会尝试这一次',157,'one-time thing')])
d=industry('I145',list(range(140,146)),'Raccoon Coin Pusher首日十万销量及Playstack中国合作',3,2,subject='Playstack发行的Raccoon Coin Pusher',basis='实际新闻主体包含发行商Playstack，来源证明其发行TGA最佳独立游戏及首次中国团队合作，国际独立发行能力R2；新品发售E3，非单纯榜位；肉鸽推币不自动命中竞技/数值卡牌。',evidence=[ev(145,'publisher of *Raccoon Coin Pusher*'),ev(145,'first collaboration with a Chinese developer')],pc='domestic_or_focus')
item(d,'《Raccoon Coin Pusher》发售复盘：三人团队首日销量10万份','游戏茶馆当期译稿回顾，《Raccoon Coin Pusher》由三名2024届毕业生组成的团队开发，发售首日销量10万份、同时在线峰值11500人。发行商Playstack此前发行过获得TGA最佳独立游戏奖的作品，此次是其首次与中国开发者合作。制作人表示，发售前约40万份愿望单中，美国地区占比最高；这些是稿件所记录的发售初期数据。', [('《Raccoon Coin Pusher》',145,'Raccoon Coin Pusher'),('三名2024届毕业生',145,'three people—all of whom are 2024 graduates'),('发售首日销量10万份、同时在线峰值11500人',145,'100,000 copies on its first day'),('Playstack',145,'Playstack'),('TGA最佳独立游戏奖',145,'2025 TGA Award for Best Indie Game'),('首次与中国开发者合作',145,'first collaboration with a Chinese developer'),('约40万份愿望单中，美国地区占比最高',145,'400,000 wishlist entries')])
d=industry('I229_BRUTAL',[229],'RocketWerkz开源C#游戏开发框架BRUTAL',3,2,subject='RocketWerkz/Ahwoo',basis='推出开放游戏开发基础设施为战略动作E3；DayZ资深开发者创立、已有商业产品并获边缘世界引擎迁移采用，实际研发影响力R2。',evidence=[ev(229,'均由资深《DayZ》开发者'),ev(229,'从 Unity 引擎迁移')],date='2026-10-20')
item(d,'RocketWerkz开源BRUTAL框架，商业游戏可免版税使用','据indienova汇编，RocketWerkz与Ahwoo于10月20日宣布开源C#游戏开发框架BRUTAL，将C#、.NET、C++库和底层图形访问结合，供团队构建和维护自己的开发工具。框架可免费用于商业游戏、不收版税或分成，但需遵守开源许可并展示版权声明与标志。报道还以《边缘世界》迁移至基于BRUTAL的自研引擎为采用案例。', [('RocketWerkz与Ahwoo于10月20日宣布开源',229,'10 月 20 日'),('C#游戏开发框架BRUTAL',229,'游戏开发框架“BRUTAL”'),('C#、.NET、C++库和底层图形访问',229,'将 C# 和 .NET 与 C++ 库'),('免费用于商业游戏、不收版税或分成',229,'商业游戏中免费使用'),('版权声明与标志',229,'BRUTAL 版权声明'),('《边缘世界》',229,'《边缘世界》')])
d=industry('I211',[211],"Don't Nod保障程序与工会披露年内清算风险",3,2,subject="Don't Nod",basis='非例行财报：保障程序、无力偿债风险及最坏年内清算情形构成流动性异常E3；奇异人生开发主体R2；不同于仅工会裁员表态E1。对照9月现金可撑至2027年1月底警告，本期新增保障程序与11月裁定/解雇节点，保留工会归因。',evidence=[ev(211,"早期《奇异人生》"),ev(211,'正处于保障程序')],matches=prior("Don't Nod警告现金"),novelty='material_update',facts=['本期报道公司已处于保障程序，工会披露最坏情形为2026年内清算。','政府机构拟11月3日裁定，获批后员工可能11月25日收到解雇通知。'])
item(d,"Don't Nod工会警告年内清算风险，重组方案进入11月裁定节点","《奇异人生》早期作品开发商Don't Nod的工会员工于10月27日声明，公司处于避免无力偿债的保障程序中，管理层讨论的最坏财务情形包括2026年内清算。工会称，拟裁撤岗位覆盖多个研发职能，并质疑以外包承接工作是否可行。报道列出的下一节点是11月3日有关机构裁定；若方案获批，员工可能于11月25日收到解雇通知。", [('《奇异人生》早期作品开发商',211,'早期《奇异人生》'),('10月27日声明',211,'10月27日发表声明'),('保障程序',211,'正处于保障程序'),('2026年内清算',211,'公司在2026年内清算'),('工会称',211,'工会认为'),('以外包承接工作',211,'通过外包来承接'),('11月3日',211,'11月3日作出裁定'),('11月25日收到解雇通知',211,'11月25日收到解雇通知')])
d=industry('I346_IOS',[346],'澳大利亚法院要求Fortnite重返iOS App Store',2,3,subject='Fortnite移动分发',basis='头部全球游戏的移动平台准入裁定E2R3；本期newsletter明确记录澳洲法院要求重新上架。较早全球iOS回归报道仍明确澳洲不可用，本期为可核验地区状态变化。',evidence=[ev(346,'an Australian court ordered Fortnite')],matches=prior('全球重返 iOS','Fortnite全球iOS回归'),novelty='material_update',facts=['本期来源记载澳大利亚法院要求Fortnite重返当地iOS App Store；历史记录明确该地区尚不可用。'])
item(d,'据报澳大利亚法院要求《堡垒之夜》重返当地iOS商店','GameDiscoverCo当期简报记载，澳大利亚法院已要求《堡垒之夜》重新进入当地iOS App Store。该信息描述的是法院要求，不能等同于游戏已完成重新上架。', [('澳大利亚法院已要求《堡垒之夜》重新进入当地iOS App Store',346,'an Australian court ordered Fortnite')])

# Above-line repeats, financial gate, and explicit boundary candidates.
for cid,ns,event,E,R,subject,terms,evidence in [
 ('I012',[12],'Arkane Lyon寻找买家协商延期',2,3,'Microsoft游戏业务',['微软将Arkane Lyon'],[ev(12,'Arkane Lyon')]),
 ('I165',[165],'Xbox首任COO离职',3,3,'Xbox',['Xbox首任首席运营官Helen'],[ev(165,"Xbox's first COO")]),
 ('I260',[260],'篮球少女实际开服和畅销第4',3,3,'灵犀互娱',['开服三天后进入游戏畅销榜'],[ev(260,'灵犀互娱')]),
 ('I053',list(range(53,58)),'异环4月公测回顾',3,3,'苏州幻塔工作室',['《异环》日本版登顶','5月全球手游市场','异环》Q2','异环》流水超'],[ev(53,'蘇州幻塔スタジオ')]),
]:
 industry(cid,ns,event,E,R,subject=subject,basis='当前来源在窗口内；历史报告已收录并曝光同一已上线/任职变化状态，本期没有实质变化，仅复述或翻译，不因事件较早排除。',evidence=evidence,decision='exclude',matches=prior(*terms),novelty='repeat_only',gates=['history_repeat'],pc='domestic_or_focus' if cid=='I053' else None)
# A lower-scoring unexposed repeat loses the sole carryover slot.
industry('I177',[177],'Atari移动业务由Crossy Road创作者统筹',3,2,subject='Atari/Hipster Whale',basis='收购后统筹移动开发的安排在5月28日至6月4日周报已记载，全部未曝光；E3R2=6，低于王者世界9分，唯一card_carryover名额不选择本条。正文与标题姓名不一致另记录，不消费摘要源补齐姓名。',evidence=[ev(177,'Atari has named'),ev(177,'co-founder of Hipster Whale')],decision='exclude',matches=prior('Atari以最高3930万美元'),novelty='repeat_only',gates=['carryover_limit'])
industry('I209',[3,209],'卡普空上半财年销量与数字版占比',2,3,subject='Capcom',basis='常规财报及历史销量纪录，未证明相对指引/预期异常、重大减值或流动性变化；且源文销量增量与累计数据互相冲突，不引用矛盾数字。',evidence=[ev(209,'卡普空迎来了')],decision='exclude',gates=['financial_routine','factual_uncertainty'])
industry('I036',[36],'无畏契约端游国服注册用户破亿',1,3,1,subject='腾讯',kind='focus_subject',focus=['腾讯'],basis='长线既有产品用户里程碑E1；腾讯R3，爆破竞技M1，总分4。源文区分端游与已曝光的手游过亿，不将二者误并。',evidence=[ev(36,'腾讯在今年8月')],genre='competitive')
industry('I124',list(range(124,130)),'梦幻西游手游巅峰联赛六年运营复盘',1,3,1,subject='网易',kind='focus_subject',focus=['网易'],basis='既有产品赛事生态与六年生命周期回顾E1，网易R3、明确电竞机制M1，总分4，不因4月赛事日期降分。',evidence=[ev(124,'NetEase')],genre='competitive')
industry('I166',[166],'Newzoo9月PC和主机收入结构',2,1,subject='PC/主机市场',kind='pc_console_market',basis='市场数据E2，PC/主机市场整体基准R1，M0，2分；其中Remedy项目成绩另建独立候选，不借其他榜内大公司抬整篇R3。',evidence=[ev(166,"September PC revenue charts")])
industry('I166_REMEDY',[166],'Control Resonant首月百万与Remedy首次自发行',2,2,subject='Remedy',basis='首次自发行作品首月百万、成为自家最快销售作品，属于产品销售状态数据E2；成熟跨平台研发与发行能力R2，动作冒险无重点品类M，4分边界。',evidence=[ev(166,"Remedy's first self-published title")])
industry('I201',[201],'Witchbrook正式定档2027年1月28日',2,2,1,subject='Witchbrook',basis='既有新品正式定档E2；八年开发、全平台计划及成熟生活模拟细分竞争具有较强产品声量R2，明确life sim M1，5分；正常定档在日历呈现，行业不将未发生的正式上线评E3。',evidence=[ev(201,'Eight years after its reveal')],genre='life_simulation',decision='exclude',gates=['section_transfer'],pc='multiplayer_or_other')
# The same event belongs in the product calendar; keep the industry decision explicit.

# Remaining translated groups: scores follow actual events, not translation language.
groups=[(40,[40],3,1,'Cat Society/Sarah’s Dungeon Inn','新品1.0正式发售，独立工作室代表作可核验，当前影响力R1，3分。'),(41,[41],1,1,'All Geeks','零售店损失及拟联合诉讼E1，实际主体为独立零售商R1。'),(44,[44,45,46,106,107],1,1,'Bit Egg/Lost & Found','外包工作室转原创开发经验访谈，属于既有战略与开发复盘E1，代表产品R1。'),(47,list(range(47,53)),1,1,'PC独立游戏市场','小众开发与获客经验讨论E1，PC市场整体R1。'),(65,list(range(65,71)),3,1,'Mingkun Technology/Fantasy Mech Fighter','2025年VR产品上线回顾E3，当前代表作品及创作者影响力R1，不能因历史日期改E0。'),(71,list(range(71,77)),3,1,'MyACG/Land of Ashes','新品抢先体验及十万销量E3，代表独立作品R1，非竞技动作肉鸽M0。'),(77,list(range(77,83)),3,1,'Shangguan/Cervical Spondylosis','4月2日新品发售回顾E3，代表独立视觉小说团队R1。'),(89,list(range(89,95)),1,2,'Yandex Ads','俄语区营销会议与既有能力宣传E1，区域广告平台能力R2，2分。'),(95,list(range(95,100)),3,1,'Sad Cat Studios/Replaced','已发售新品及八年开发复盘E3，当前团队有代表作但R1，3分；剧情AI角色不是实际生成式AI应用。'),(108,list(range(108,113)),3,1,'Explosive Guard','小游戏发布及PvP养成结构，E3，当前实际主体有代表作品R1，竞技品类M1后4分。'),(113,list(range(113,119)),3,1,'Shenzhen Mixaoyou','3月小游戏新上线回顾E3，系列作品与榜位支持代表主体R1；塔防/跑道不自动竞技，M0。'),(151,list(range(151,157)),0,3,'暗区突围','既有手游赛季模式与内容运营E0，不以新模式当新品。')]
for n,ns,E,R,sub,basis in groups:
 M=1 if n==108 else 0
 if M: genre_needle['I108']='PvP'
 industry(f'I{n:03d}',ns,inputs[sid(n)]['title'],E,R,M,subject=sub,basis=basis,evidence=[ev(n,txt(n).splitlines()[0])],genre='competitive' if M else None,decision='exclude',gates=['score'] if E else None,pc='ordinary_overseas_single_player' if n in [40,71,77,95] else None)

# AI reverse scan: all industry inputs, not only industry includes.
def ai(cid,ns,event,reason,include=False,tier='direct_application',stages=('development',),reverse=True,migration=''):
 ids=[sid(n) for n in ns];covered.update(ids)
 d={'candidate_id':cid,'section':'ai_trends','source_ids':ids,'entities':[event],'event':event,'decision':'include' if include else 'exclude','reason':reason,'ai_tier':tier,'game_stage':list(stages),'industry_reverse_scan':reverse}
 if tier=='transferable_frontier':d['migration_path']=migration or '通用模型能力可以迁移到研发原型或内容工具，但本条没有足够明确且非例行的游戏变化。'
 if len(ids)>1:d['cluster_basis']={'subject':event,'event_date':DATE,'event':event}
 decisions.append(d);return d
d=ai('A029',[29],'爱哩爱哩AI居民与自动研发管线','直接游戏产品与制作流程落地，完整开发者访谈提供交互、记忆、成本与边界。',True,stages=('product','development'))
item(d,'《爱哩爱哩》以自主AI居民替代直接控制，付费对应内容生成频率','制作人Sea团队曝光AI新品《爱哩爱哩》：角色自行生活、发布图文或视频，玩家通过投喂道具与MOD间接影响行为，产品不提供直接打字聊天。团队用分层日志组织角色记忆，并称已建立多Agent循环审核的资产生产管线。Sea表示，视频生成成本使产品选择F2P，付费主要增加生活内容的产出频率；这些仍需通过早期测试验证。', [('Sea',29,'Sea：'),('《爱哩爱哩》',29,'《爱哩爱哩》'),('不提供直接打字聊天',29,'把打字聊天全部干掉'),('分层日志组织角色记忆',29,'30 个碎片聚成一页日记'),('多Agent循环审核的资产生产管线',29,'不同的 Agent 循环迭代三四遍'),('视频生成成本使产品选择F2P',29,'商业模式必须是 F2P'),('付费主要增加生活内容的产出频率',29,'付费增加产出频率')])
d=ai('A161',[161],'Lumio AI游戏创作平台早期运营','一人核心研发及创作平台已有可量化产出，直接产品与研发应用；自述规模不外推行业效率。',True,stages=('development','product'))
item(d,'Lumio AI游戏创作平台已有122款作品，开发者强调需求与验收仍需人掌握','游戏新知采访的程序员大崔离职后开发了AI游戏创作平台Lumio，平台已有122款创作者游戏，总游玩时长超过47小时。按其介绍，开发经历包括独自借助AI工作三个月，再与三名伙伴协作半个月。他同时认为，AI缩短编码时间后，需求并行扩张会增加程序员的心智负担，技术方案与需求理解不能只靠转达给模型。', [('大崔',161,'大崔'),('AI游戏创作平台Lumio',161,'AI游戏创作平台「Lumio」'),('122款创作者游戏，总游玩时长超过47小时',161,'122款游戏，总游玩时长超过47小时'),('三个月',161,'一个人加上AI做了三个月'),('三名伙伴协作半个月',161,'三个小伙伴一起做了半个月'),('需求并行扩张会增加程序员的心智负担',161,'心智负担会高非常多'),('技术方案与需求理解',161,'一定要深入地读策划案')])
d=ai('A247',[247],'Epic披露AI编码进入UE6与Fortnite研发','引擎与游戏开发直接应用，提供人工架构控制和具体任务时长结果；厂商自述归因。',True)
item(d,'Epic称已用AI开发UE6与《堡垒之夜》，工程师保留架构与性能控制','Epic开发负责人Marcus Wassmer表示，工程师已不再编写大部分代码，而是指导AI工具并持续迭代，确保引擎满足内存、性能与扩展性约束。当前相关开发流连接《堡垒之夜》、UEFN和UE6，使用工具包括Claude Code与Codex。他举例称，原估单名工程师需三至六周的D3D12渲染层部分重写，实际约一周完成；这是厂商披露的具体任务结果。', [('Marcus Wassmer',247,'Marcus Wassmer'),('工程师已不再编写大部分代码',247,'engineers are no longer writing the bulk of the code'),('内存、性能与扩展性约束',247,'memory, performance, and scalability'),('《堡垒之夜》、UEFN和UE6',247,'attached to Fortnite'),('Claude Code与Codex',247,'Claude Code and Codex'),('三至六周',247,'three to six weeks'),('D3D12',247,'D3D12'),('约一周完成',247,'about one week')])
d=ai('A176',[25,176],'Epic拟修改UE和MetaHuman输出的AI训练限制','直接作用于游戏工具的训练授权，区分计划修改与现行禁止，不与编码应用合并。',True,stages=('development','product'))
item(d,'Epic拟解除UE与MetaHuman输出的AI训练限制，具体游戏授权仍由开发者决定','Tim Sweeney表示，Epic正在推进修改许可条款，移除使用虚幻引擎与MetaHuman输出训练AI的限制，现行条款目前仍有限制。他同时强调，采用这些工具制作的每款游戏，仍可由开发者自行选择允许或禁止AI训练。工具许可的调整计划因此不等于所有游戏资产都已开放训练。', [('Tim Sweeney',176,'Tim Sweeney'),('Epic正在推进修改许可条款',176,'working to remove this restriction'),('虚幻引擎与MetaHuman输出训练AI的限制',176,'outputs of Unreal Engine and MetaHuman'),('现行条款目前仍有限制',176,'Yes currently'),('开发者自行选择允许或禁止AI训练',176,'developers’ choosing which can allow or restrict AI training')])
d=ai('A181',[181],'Roblox确认关闭误抓成人资产的AI代理','直接游戏生成工具训练数据治理，站方指控和公司确认分别归因，属于完整且有处置结果的独立事件。',True,stages=('development','product'))
item(d,'Roblox关闭误抓成人资产的AI代理，称数据未用于训练','Roblox向Game Developer确认，一名研究人员建立的3D资产采集代理未按预期运行，抓取了Open3DLab及关联站点的内容。公司表示已停用该代理，数据没有用于任何用途，包括模型训练，并正在强化代理构建与审查的防护。站方管理员则指控该抓取忽略robots.txt、服务条款及部分作者的非商业许可；两方陈述须分别理解。', [('Roblox',181,'Roblox Corporation has confirmed'),('Open3DLab',181,'Open3DLab'),('未按预期运行',181,'failing to operate as intended'),('已停用该代理',181,'The agent was decommissioned'),('数据没有用于任何用途，包括模型训练',181,'data was not used for any purpose'),('强化代理构建与审查',181,'strengthening safeguards'),('站方管理员则指控',181,'According to Salaryman'),('robots.txt',181,'robots.txt'),('非商业许可',181,'non-commercial licenses')])
# Soft target is exceeded deliberately: these five are separate, substantiated direct applications.
ai('A180',[180,194],'Valve回应AI快速克隆游戏','直接发行治理候选，来源有问题确认但没有新执行方案；在五条可核验产品/流程/授权/处置进展之后不另刊同类争论。',stages=('publishing',))
ai('A026',[26,264,272],'Genie4世界模型实时交互与原生音频','迁移价值类；当期有发布，但直接游戏应用优先，本期已有五条证据完整的直接应用，不用未规模落地的引擎替代叙事扩写。',tier='transferable_frontier',migration='实时可控世界与同步音频→前期原型、互动影游或UGC→可能缩短场景验证/生成流程，尚受连续稳定性限制。')
ai('A027',[27],'80亿分之一人生模拟器','直接产品应用，但核心开发于10月5日；与本期更完整的AI原生产品和管线案例相比，统计偏差/幻觉边界较多，未另刊。',stages=('product',))
ai('A032',[32,214],'宫本茂与樱井政博AI创作观点','不同受访者不聚合为一条新闻；本记录仅审计观点型池，未产生已部署游戏变化。',tier='transferable_frontier')
decisions[-1]['event']='AI创作观点池审计（各来源独立排除）'; decisions[-1]['cluster_basis']='非正文合并；逐源排除：S0032宫本茂，S0214樱井政博。'
ai('A058',[58]+list(range(146,151)),'Feeling AI与NieTa创始人访谈','世界模型与AI创作社区长访谈，现有证据主要是较早经营指标与方法论；低于本期直接游戏落地优先级。',tier='transferable_frontier')
ai('A100',list(range(100,106)),'VAST Tripo资产可用性访谈','直接3D研发工具候选，含3月发布的模型与生产拓扑机制；本期优先具体游戏团队实际管线与新处置，不把厂商自述引擎可用性写成量产事实。')
ai('A119',list(range(119,124)),'腾讯游戏创作大赛AI学习与创作支持','直接人才培养/创作支持候选，主要赛事方法与历史案例，不挤占本期更具体的产品/授权/研发变化。')
for r in rows:
 if r['section']=='ai_trends' and r['source_id'] not in covered:
  ai('A'+r['source_id'][1:],[r['source_id']],r['title'],'通用工具教程、融资/治理/财务/硬件或非游戏课程；未证明独立且明确的游戏迁移变化。',tier='transferable_frontier',reverse=False)

# Daily community: fresh, named event plus one substantive economic mechanism; only window replies.
def community(cid,n,include,reason,trigger,logic,timeline,follow):
 d={'candidate_id':cid,'section':'community_discourse','source_ids':[sid(n)],'entities':[inputs[sid(n)]['title']],'event':trigger,'decision':'include' if include else 'exclude','reason':reason,'community':{'trigger':trigger,'claim_scope':'玩家帖子与回复的主张；不等于官方规则或技术结论','complaint_logic':logic,'timeline':timeline,'follow_up_scan':follow}}
 covered.add(sid(n));decisions.append(d);return d
d=community('C334',334,True,'报告日新建、可命名的评测口径争论；只使用28日首页摘录，剔除29日回复。','米哈游游戏AI评测被玩家质疑高低分取样不对称','最高分/最低分对比会影响读者对相对模型能力和稳定性的判断；另有用户指出不同参数规模结果不一。','10月28日16:26发帖，28日16:33至17:17已有质疑与复核线索。','按米哈游、Qwen、gamescaling、模型、评测补扫20条社区及262条行业输入，仅S0334对应；无同事件官方公告或可核验代码正文。')
item(d,'玩家质疑米哈游游戏AI评测取样不对称，争论集中于可比性','米哈游游戏AI的评测展示被玩家质疑采用不对称取样：10月28日新帖称，自家模型取十轮最高分，其他模型取十轮最低分，并给出项目页面和代码位置作为复核线索。玩家担忧这种比较会放大性能优势，另有回复指出，暂停与实时模式、不同参数规模的结果并不一致。帖子也有用户表示自己尚未确认高低分取样，争议仍围绕比较口径与结论是否相称展开。', [('米哈游游戏AI',334,'[米哈游]'),('10月28日',334,'2026-10-28 16:26'),('自家模型取十轮最高分，其他模型取十轮最低分',334,'本模型取10轮最高分'),('项目页面和代码位置',334,'选择data.js，160行'),('暂停与实时模式、不同参数规模的结果并不一致',334,'暂停模式在0.8b下'),('尚未确认高低分取样',334,'有没有取高低分倒是没看')],{'community':d['community']})
d=community('C345',345,True,'旧帖在28日出现围绕收益方差和资产价值的新反驳，保留前情与对立意见；不把玩家估算写成概率或官方事实。','三角洲惊喜渡鸦收藏品随机复制活动','稀有收藏品复制可能拉大收益差距，支持者认为本身经济可积累、随机收益不代表整体失衡。','10月25日建帖，26日讨论机会限制和损失，28日仍有关于资产消耗的新反驳。','以惊喜渡鸦、非洲之心、收藏品、复制补扫社区与行业池，只有S0345；当前没有同事件可用官方调整材料。')
item(d,'《三角洲行动》“惊喜渡鸦”随机复制收藏品，玩家争论收益差距','《三角洲行动》“惊喜渡鸦”活动被玩家描述为可使当局收藏品升级、降级、消失、不变或复制，稀有收藏品也可能进入这一循环。10月25日开启的讨论中，质疑者担心随机收益放大玩家资产差距；支持者则认为触发机会和可用物资本就受限，不能用少数高收益视频代表常态。到10月28日，仍有玩家以资产消耗速度反驳“经济失衡”的判断。', [('《三角洲行动》',345,'三角洲'),('“惊喜渡鸦”',345,'惊喜渡鸦'),('升级、降级、消失、不变或复制',345,'品质提升，下降，消失'),('10月25日',345,'2026-10-25 19:59'),('触发机会和可用物资本就受限',345,'其实能赌的机会不多'),('10月28日',345,'2026-10-28 12:39'),('以资产消耗速度反驳',345,'一个亿亏完只需要')],{'community':d['community']})
for r in rows:
 if r['section']=='community_discourse' and r['source_id'] not in covered:
  n=int(r['source_id'][1:]);reason='旧帖延续但缺少报告日实质进展、关键对象/触发事实不足，或在两条上限之外；按原帖主张保留审计，不视为官方事实。'
  if n in [337,341]:reason='与已发布的行业事件相同，当前只增加旧热度/意见，没有窗口内新进展。'
  if n in [336,340]:reason='文本或立绘调整旧争议，28日回复仍未明确关键改动或新增处置；不以旧热度凑数。'
  community('C'+r['source_id'][1:],n,False,reason,r['title'],'详见逐字原帖，未形成优于入选事件的完整可核验报道链。',next((s for s in r['text'].splitlines() if '发帖：' in s),'报告窗口内收录'), '全量同窗口社区/行业反扫完成；没有可补齐关键事实的新材料。')

# Deep newsletter first, with its own R/I/E/C.
d={'candidate_id':'D346','section':'deep_analysis','source_ids':['S0346'],'entities':['Steam Next Fest','GameDiscoverCo'],'event':'10月新品节供给扩张与愿望单转化机制','decision':'include','reason':'配置newsletter全文优先；同一统计口径比较6月/10月，具完整机制与边界；单篇高质量分析支撑独立主题。','scores':{'relevance':2,'insight':3,'evidence':3,'card':3,'total':11},'topic_key':'Steam新品节+供给拥挤+既有兴趣放大','quality_route':'横向比较/深度分析','source_priority':'configured_newsletter','evidence_anchors':[ev(346,'>7,300'),ev(346,'top 10%'),ev(346,'hype amplifier')],'merge_basis':'同一期newsletter的数据、机制与边界构成一个选题，不按游戏/指标拆题。'}
decisions.append(d);covered.add('S0346')
item(d,'Steam新品节参展激增，已有热度比现场曝光更能决定结果','观察：GameDiscoverCo对10月Steam新品节的复盘显示，参展供给的增长快于可分配注意力，活动更像放大已有兴趣，而非普遍创造兴趣。其跟踪的Demo超过7300款，较6月约4400款明显增加。\n\n分析：原先开发者可以把集中试玩活动当作一段较强的发现窗口，前提是平台曝光足以让中腰部作品获得可观的新关注。该机构用更可跨期比较的Steam关注者增量观察发现，10月排名前10%的门槛仅为新增63名关注者，6月为121名、去年10月为173名；这不是愿望单的精确换算，而是同类排名位置上的关注收益在下降。供给扩张后，同一百分位的可见度被摊薄，单凭“参加了活动”更难支撑发行预期。\n\n多个靠前Demo在活动前就已积累玩家兴趣，新增愿望单前十的中位数也由6月约14.3万降至10月约8万。由此可以理解作者提出的“热度放大器”：场外传播、既有试玩与产品受众的积累，先形成进入活动的基础，再由活动集中转化。与此同时，文章强调不同细分品类的微趋势并存，不能把供给拥挤简单归因为某一种题材或把所有参展作品视为AI产物。', [('GameDiscoverCo',346,'GameDiscoverCo'),('Demo超过7300款',346,'>7,300'),('6月约4400款',346,'~4,400'),('新增63名关注者',346,'+63 followers'),('6月为121名、去年10月为173名',346,'+121 followers'),('Steam关注者增量',346,'Steam follower increase'),('前十的中位数也由6月约14.3万降至10月约8万',346,'+143k, vs. +80k'),('多个靠前Demo在活动前就已积累玩家兴趣',346,'strong demo momentum pre-NF'),('热度放大器',346,'hype amplifier'),('不同细分品类的微趋势并存',346,'existing microtrends')],{'card_copy':{'source_label':'GameDiscoverCo分析','summary':'试玩供给扩张摊薄了同一排名位置的关注收益，Steam新品节正更多地放大开发者在场外已积累的兴趣。','insights':[{'title':'供给先于注意力增长','detail':'超过7300款Demo竞争同一活动窗口，参加活动本身更难保证可见度。'},{'title':'同一百分位收益下降','detail':'以关注者增量比较，前10%门槛从6月121名降至10月63名，不能直接当作愿望单数量。'},{'title':'活动放大既有兴趣','detail':'多个头部试玩在活动前已有热度，发行转化依赖先前积累与集中曝光衔接。'},{'title':'拥挤并非单一品类趋势','detail':'多种细分体验同时发展，不能用一种题材或AI标签解释全部变化。'}]}})
for n in [347,348]:
 decisions.append({'candidate_id':f'D{n}','section':'deep_analysis','source_ids':[sid(n)],'entities':[inputs[sid(n)]['title']],'event':inputs[sid(n)]['title'],'decision':'exclude','reason':'汽车或电商市场，不具本期游戏深度观察证据链。','scores':{'relevance':0,'insight':1,'evidence':1,'card':0,'total':2}});covered.add(sid(n))

# Individual remainder audit. Ordinary marketing/updates E0; other real events retain E1-3.
E3={5,13,17,22,23,42,193,199,202,203,218,222,223,226,230}
E2={11,18,24,159,163,171,172,178,184,187,195,196,197,204,207,208,213,229,232,236,240,243,244,246,248,255,258,259,262}
E1={1,2,4,6,7,9,10,19,20,21,28,31,34,35,37,43,167,168,173,174,175,179,185,188,189,190,191,192,198,200,205,210,212,215,216,225,227,231,233,237,238,242,245,252,253,256,257,260,261}
head={1:('Nintendo',3),10:('EA',3),19:('Pocketpair',2),24:('Valve',3),159:('Paradox',2),163:('Gamescom Asia',2),171:('Unity/PvX',3),172:('Dimensions Games',1),178:('Warhorse',2),184:('Unity/PvX',3),187:('网易',3),193:('Blizzard',3),197:('Nintendo',3),199:('Undead Labs/Xbox',3),204:('Sony',3),207:('Warhorse',2),208:('Sony',3),213:('Capcom',3),216:('Blizzard',3),231:('莉莉丝',3),232:('灵游坊',2),236:('Auroch Digital',2),243:('灵游坊',2),244:('Blizzard',3),248:('Shiny Shoe',2),255:('Epic',3),258:('网易',3),259:('PWN Games',2),261:('灵游坊',2),262:('Vanillaware/Marvelous',2)}
for r in rows:
 if r['section']!='industry_news' or r['source_id'] in covered:continue
 n=int(r['source_id'][1:]); E=3 if n in E3 else 2 if n in E2 else 1 if n in E1 else 0
 sub,R=head.get(n,(r['title'],1))
 reason='E0：常规运营/促销/评测或非游戏资讯，没有本模型认可的独立行业状态变化。' if E==0 else '独立候选逐项评估：E×R+M低于5；日期较早不构成门禁。'
 gates=['score'];decision='exclude'
 if E*R>=5:
  if n in [171,184]:reason='合作本可E3，但现有正文仅受阻摘要/99字引流，未获完整合作条款与事实链，不用残缺材料进入正文。';E=3;gates=['source_quality']
  elif n==24:reason='平台审核要求E2R3达线，但仅31字标题式源文，无审核适用范围与生效条件；转AI反扫后不把它当已验证新政策。';gates=['source_quality']
  elif n==199:reason='项目研发多年原因回顾，未发生新品立项/上线或取消；实际为在研项目复盘E1，不能用“开发多年”当新立项。';E=1;gates=['score']
  elif n==197:reason='既有独立游戏节目发布汇编E0；各产品具体测试/定档已拆入日历，不给节目借所有参展作品累计E3。';E=0
  elif n in [204,258]:reason='普通订阅阵容公布/显示技术接入属于既有产品运营与宣传E0。';E=0
  elif n in [213,255]:reason='已有系列规划与既有战略访谈表态E1，未单独确认新的立项/合作/政策生效。';E=1;gates=['score']
  else:
   # Source-only headlines and previews do not establish an implemented release/strategy.
   reason='标题式短源或在研/发售前说明不足证明已发生高E状态；保留候选，不补造公司归属、正式上线或战略动作。';gates=['source_quality']
 if n==231:
  E=2;reason='本期截至发稿累计收入与下载显著高于历史9月数据，作为独立material_update候选补入下方，不在此重复。';gates=['section_transfer']
 pc='unknown' if n in E3 or n in [11,18,159,193,199,207,232,243,246,262] else None
 industry(f'I{n:03d}',[n],r['title'],E,R,subject=sub,basis=reason,decision=decision,gates=gates,pc=pc)

# Substantive new revenue snapshot, separately from the old release date in calendar.
decisions[:]=[d for d in decisions if d['candidate_id']!='I231']
d=industry('I231',[231],'塔塔冒险队截至本期累计下载和收入新状态',2,3,subject='莉莉丝',kind='focus_subject',focus=['莉莉丝'],basis='E2产品经营数据，来源直接归属莉莉丝R3；随机奖励/塔防/营地经营不足证明本事件数值卡牌RPG或竞技，M0。相对9月28日四个月4560万美元，当前双平台9500万美元、下载1800万为有口径说明的新数据，不以媒体数量作更新。',evidence=[ev(231,'莉莉丝旗下《塔塔冒险队》'),ev(231,'累计下载超1800万次')],matches=prior('《塔塔冒险队》'),novelty='material_update',facts=['本期点点数据口径为海外iOS/安卓及国内iOS合计收入超过9500万美元、下载超过1800万次；9月28日报告四个月累计流水4560万美元。','1.1亿美元含国内安卓推估，须与9500万美元观测口径区分。'])
item(d,'莉莉丝《塔塔冒险队》累计下载超1800万次，双平台收入估算超9500万美元','据罗斯基引用点点数据，莉莉丝《塔塔冒险队》自5月21日起量至本期发稿，累计下载超过1800万次，海外iOS、海外安卓及国内iOS合计收入超过9500万美元。文中另将国内安卓收入作推估后给出APP总收入约1.1亿美元，不能把这一推估与前述口径混用。产品以弹珠抽宠、塔防战斗和营地经营组成循环，近期投放仍在迭代素材。', [('莉莉丝《塔塔冒险队》',231,'莉莉丝旗下《塔塔冒险队》'),('5月21日',231,'5月21日'),('累计下载超过1800万次',231,'累计下载超1800万次'),('海外iOS、海外安卓及国内iOS合计收入超过9500万美元',231,'双平台累计收入超9500万美元'),('约1.1亿美元',231,'1.1亿美元'),('国内安卓收入作推估',231,'据此预估国内安卓'),('弹珠抽宠、塔防战斗和营地经营',231,'弹珠抽宠 + 塔防战斗 + 营地经营'),('近期投放仍在迭代素材',231,'近期也同样新增了投放素材')])

# Product-calendar repair and whole-input reverse scan are deterministic after editorial evidence fixes.
raw_audit=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
if not (P/'release_calendar_audit_extracted.json').exists():dump('release_calendar_audit_extracted.json',raw_audit)
else:raw_audit=json.loads((P/'release_calendar_audit_extracted.json').read_text(encoding='utf-8'))
nodes=[];release_scan=[]
def node(product,date,typ,ns,reason='',company=None,bonus=0,relationship='none',eligible=True,order=None):
 ids=list(dict.fromkeys(sid(n) for n in ns));ind=[s for s in ids if inputs[s]['section']=='industry_news'];rel=[s for s in ids if inputs[s]['section']=='release_calendar']
 fps=list(dict.fromkeys(inputs[s]['url']+'|'+inputs[s]['sha1'] for s in ids));count=len(fps)
 E={'new_game_test':3,'new_game_launch':3,'new_game_preload':2,'new_game_schedule':2,'new_game_first_reveal':2,'old_cross_platform_launch':1,'old_relaunch':1,'old_major_update':1}[typ]
 strength=min(count,3)+int(bool(ind)); scope='report_window' if date==DATE else 'next_day_lookahead' if date=='2026-10-29' else 'future_announcement' if typ in ['new_game_schedule','new_game_first_reveal'] else 'outside'
 win=scope!='outside';publish=eligible and win and count>=2
 nd={'product':product,'event_date':date,'signal_type':typ,'event':{'new_game_test':'新品试玩/测试','new_game_launch':'新品上线','new_game_preload':'新品预下载','new_game_schedule':'新品定档','new_game_first_reveal':'新品首次曝光','old_cross_platform_launch':'跨平台上线','old_major_update':'重大更新','old_relaunch':'重启回归'}[typ],'event_type_score':E,'first_seen_order':order if order is not None else min(int(s[1:]) for s in ids)*100+len(nodes),'observed_signal_types':[typ],'observed_events':[typ],'industry_ids':ind,'release_ids':rel,'source_ids':ids,'source_fingerprints':fps,'appearance_count':count,'appearance_score':min(count,3),'industry_bonus':int(bool(ind)),'source_strength_score':strength,'base_priority_score':E*strength,'company_bonus':bonus,'company_relationship':relationship,'focus_companies':[company] if company else [],'focus_company_relationships':{company:relationship} if company else {},'company_evidence_ids':[s for s in ids if company and (company in txt(s) or (company=='腾讯' and '腾讯' in txt(s)))],'priority_score':E*strength+bonus,'multi_source_eligible':count>=2,'window_eligible':win,'window_scope':scope,'publish_eligible':publish,'coverage':'both' if ind and rel else 'industry_only' if ind else 'release_only','coverage_rank':3 if ind and rel else 2 if ind else 1,'editorial_note':reason,'status':'reviewed'}
 nodes.append(nd);return nd
node('影之刃零','2026-10-29','new_game_launch',[20,28,35,232,243,261,230],'正式发售为29日；28日预下载另记，不能混成28日上线。腾讯仅投资+2。','腾讯',2,'investment')
node('Raccoin: Chaos Max Edition',DATE,'new_game_test',[197,203],'两篇不同URL、不同正文的独立新闻均明确当期Demo；不把11月10日正式发售当28日已上线。')
node('Witchbrook','2027-01-28','new_game_schedule',[197,201,320],'多平台生活模拟新品正式定档，无名单公司加分。')
node('Petal Runner','2027-03-08','new_game_schedule',[197,203,308],'当前公告未来定档；S0203另有单源Demo。')
node('奇迹：新纪元',DATE,'new_game_test',[280,289],'17173与3839两源一致的实际测试。')
node('Bao Bao’s Cozy Cleaning Services',DATE,'old_cross_platform_launch',[197,203,303],'Switch版当日可用；PC次日日期不与该Switch节点混并。')
node('影之刃零',DATE,'new_game_preload',[9,243],'上一期已发布同一PC预下载，不能因今日来源再次召回重复。',eligible=False)
# Retain all extracted candidates, applying only supported correction, with false positives explicitly excluded.
used_products={'影之刃零','奇迹：新纪元'}
for old in raw_audit['nodes']:
 if old['product'] in used_products:continue
 product=old['product'];date=old['event_date'];typ=old['signal_type'];ns=old['source_ids'];eligible=True;note='复核原始节点；多源和事件日期门禁独立执行。'
 if product=='花开时见你':typ='new_game_schedule';date='unknown';eligible=False;note='只有开启预约、上线时间待定，不足确认实际上线或新定档。'
 if product=='塔塔冒险队':date='2026-05-21';eligible=False;note='历史起量与成绩复盘，不是当期新品上线。'
 if product=='异环':date='2026-04';eligible=False;note='文章回顾4月上线，非当期新开服；版本前瞻不算新品。'
 if product=='篮球少女：飞跃巅峰':date='2026-10-23';eligible=False;note='开服后畅销成绩不等于当日再次上线。'
 if product in ['都市：天际线','都市：天际线 扩展版']:typ='old_cross_platform_launch';note='老品Switch2移植；不按新品上线E3计日历。'
 if product=='胧村正怪奇谭':typ='new_game_schedule';date='2027-02-05';note='强化重置新品已于6月定档，只有本次单源回顾，非当前跨平台实际上线。'
 if product in ['天国：拯救','恶灵骑士','沙丘3','寂静岭','王者荣耀','我的世界','模拟农场25']:
  eligible=False;note='网络攻击/影视/旧背景/运营宣传或未核实发售事件的误召回，不得当新品日历。'
 if product=='武道风云':typ='new_game_preload';date=DATE;note='28日预下载与29日上线分别审计，当前仅一独立来源。'
 if not any(n['product']==product and n['event_date']==date for n in nodes):node(product,date,typ,ns,note,eligible=eligible)
# Complete release-only section, including Google News announcement records missed by the extractor.
for r in rows:
 if r['section']!='release_calendar':continue
 n=int(r['source_id'][1:]);t=r['text'];title=r['title'];release_scan.append({'source_id':r['source_id'],'title':title,'text_sha256':hashlib.sha256(t.encode()).hexdigest(),'scanned':True})
 if any(r['source_id'] in nd['source_ids'] for nd in nodes):continue
 if n in [283,284,286,296,325]:
  release_scan[-1]['exclude_reason']='普通剧情/联动/自制关卡/前瞻/预约，不是合格的独立日历事件。';continue
 m=re.search(r'^Game: (.+)',t,re.M)
 product=m.group(1) if m else re.split(r' adds | coming | launches | now available| delayed | pre-registration',title)[0]
 if n>=297:
  m=re.search(r'Parsed release date: (\S+)',t);date=m.group(1) if m else DATE if 'now available' in title else '2027' if '2027' in title else '2026-12' if 'in December' in title else 'unknown'
  typ='old_cross_platform_launch' if 'now available' in title else 'new_game_schedule'
  node(product,date,typ,[n],'未来实际跨平台/DLC未发生或单源，保留公告候选；季/月精度不擅自补日。')
 else:node(product,DATE,'new_game_schedule',[n],'原始信号保留，但单源或不具正式定档事实。',eligible=False)
# Whole industry prose and structured lists: every named dated release is recalled.
for r in rows:
 if r['section']!='industry_news':continue
 release_scan.append({'source_id':r['source_id'],'title':r['title'],'text_sha256':hashlib.sha256(r['text'].encode()).hexdigest(),'scanned':True,'scope':'全正文；剔除历史背景、相关阅读与不明回指。'})
 if r['source_id']=='S0230':
  blocks=re.split(r'\n(?=[^\n]+\n关键字：)',r['text'])
  for block in blocks:
   m=re.search(r'^([^\n]+)\n关键字：[^\n]+\n发行日期：\s*(2026/10/29)',block)
   if not m:continue
   product=m.group(1);date='2026-10-29'
   if '影之刃零' in product:continue
   node(product,date,'new_game_launch',[230],'新品发行结构化清单；单源，次日窗口不豁免多源门槛。')
# Showcase product blocks, preserving their actual future date/precision; no company inference.
show=[('Winds of Viridia','2027-early',[197]),('City of None','2027',[197]),('Sword of the Sea','2026-10-29',[197]),('Threads of Time','2027-summer',[197,317]),('Tenjutsu','2027',[197,318]),('Dumpster Gang','2027-03',[197,316]),('Super Battle Golf','2027-03-25',[197,315]),('REPO','2027',[197]),('Haunted Paws','2027-05',[197,314]),('Kitsune: The Journey of Adashino','2027-spring',[197]),('Slime Rancher 2','2027-01',[197,298]),('Spirit Crossing','2026-11-16',[197,310]),('My Arms Are Longer Now','2027-03-11',[197,309]),('Raccoin: Chaos Max Edition','2026-11-10',[197,203,307]),('Tanuki Pon’s Summer','2026-11-10',[197,306]),('Finding Polka','2027-spring',[197,305]),('Floor Plan: Slap Out of It!','2027-spring',[197,304]),('Lost and Found Co.','2027-early',[197]),('Everything is Crab','2027-01-26',[197]),('HyperYuki: Snowboard Syndicate','2027-early',[197,302])]
for product,date,ns in show:
 # Replace weaker single-source auto node only when clearly the same product.
 aliases=[nd for nd in nodes if nd['product'].casefold()==product.casefold()]
 for nd in aliases:
  if nd['event_date']==date or (len(nd['source_ids'])==1 and nd['window_scope']=='future_announcement'):nodes.remove(nd)
 if not any(nd['product']==product and nd['event_date']==date for nd in nodes):node(product,date,'new_game_schedule',ns,'同一次发布会独立报道的未来定档；明确季度/月，不能按实际当期上线。')
node('Petal Runner',DATE,'new_game_test',[203],'单源现已开放Demo；其未来定档为另一个日期节点。')
node('Haunted Paws',DATE,'new_game_test',[203],'单源Demo不因未来定档多源而提升当日测试资格。')
# Single-source prose signals missing from extraction.
for product,date,typ,ns,note in [('Dream Guardians','2026-03-17','new_game_launch',[59],'历史3月上线，日历事件超窗；行业来源窗口独立可入选。'),('Sarah’s Dungeon Inn','2026-10-23','new_game_launch',[40],'历史1.0上线，日历事件超窗。'),('Land of Ashes','2026-03-30','new_game_launch',[71],'历史EA上线，日历事件超窗。'),('Cervical Spondylosis','2026-04-02','new_game_launch',[77],'历史发售，日历事件超窗。'),('爱哩爱哩',DATE,'new_game_first_reveal',[29],'新品首曝，仅单源。'),('Cop Bastard','2026-10-29','new_game_launch',[251],'明确次日发售，仅单源。'),('宝可梦大集结','2027-01-28','old_relaunch',[160],'停运非回归：保留误召回审计，禁止刊载。')]:
 if not any(nd['product']==product and nd['event_date']==date for nd in nodes):node(product,date,typ,ns,note,eligible=False if product=='宝可梦大集结' else True)
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
for i,nd in enumerate(nodes,1):nd['candidate_id']=f'release-candidate-{i:03d}'
audit={**{k:v for k,v in raw_audit.items() if k!='nodes'},'nodes':nodes,'editorial_review':'逐源反扫并修正日期、历史背景与首曝/预下载/上线分类；不按行业include排除日历。'}
dump('release_calendar_audit.json',audit);dump('release_reverse_scan.json',release_scan)
doc={'report_type':'daily','report_window':{'start':DATE,'end':DATE},'scoring_version':'subject_genre_v2','industry_timing_version':'source_window_v1','history_window':hist['history_window'],'archive_occurrences_checked':len(hist['archive_occurrences']),'decisions':decisions}
dump('selection_decisions.json',doc)
sync(P/'release_calendar_audit.json',P/'selection_decisions.json',4)
doc=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));decisions=doc['decisions']
for d in decisions:
 if d['candidate_id']=='I193':
  d['scores']={'event':1,'relevance':3,'hook':0,'total':3};d['reason']='开放角色预创建与名字预留属于发售前运营节点E1，尚非新品正式上线或首次测试；Blizzard主体R3，3分。';d['exclusion_gates']=['score']
 if d['candidate_id']=='I208':
  d['event']='索尼2028年实体光盘政策旧争议';d['reason']='新书预订引发新一轮玩家反应，未改变此前已曝光的2028年实体光盘政策，行业不重复旧政策；社区外溢候选另记录。';d['history_check']=hcheck(prior('索尼确认 2028','索尼宣布 2028','索尼 Bungie'),'repeat_only');d['exclusion_gates']=['history_repeat']
 if d['candidate_id']=='I244':
  d['decision']='include';d.pop('exclusion_gates',None);d['reason']='Project Titan取消为E2，暴雪R3，6分；本期来源回顾既有项目取消，完整文本可核验，未检索到历史同事件，不因取消发生较早而降低E或排除。'
  item(d,'暴雪回顾《Project Titan》取消：七年研发后以六周重提新方案','暴雪回顾《守望先锋》的起点：MMO项目《Project Titan》在研发七年后被取消，团队随后只有六周提出新方案。Keller认为，这段经历从一开始就让团队形成谦逊与韧性，并延续到《守望先锋》十年的运营中。这是对历史项目取舍与组织经验的复盘。',[('暴雪',244,'cancelled by Blizzard'),('《守望先锋》',244,'Overwatch'),('《Project Titan》在研发七年后被取消',244,'Project Titan, an MMO'),('六周提出新方案',244,'six weeks to come up with a new pitch'),('Keller',244,'Keller'),('十年的运营',244,'a decade of Overwatch')])
 if d['section']=='release_calendar' and d['decision']=='exclude':
  nd=next(n for n in nodes if n['candidate_id']==d['candidate_id']);d['reason']=nd['editorial_note']+'；'+d['reason']
dump('selection_decisions.json',doc)
release_texts={
 '影之刃零':('灵游坊自主研发及发行的武侠动作多平台游戏《影之刃零》定于10月29日正式发售；玩家将在六十六天生命倒计时中展开战斗与探索。', [('灵游坊自主研发及发行',230,'由灵游坊自主研发及发行'),('武侠动作多平台游戏《影之刃零》',230,'影之刃零（Phantom Blade Zero）'),('10月29日',230,'发行日期： 2026/10/29'),('六十六天生命倒计时',230,'仅余六十六天的生命')]),
 'Raccoin: Chaos Max Edition':('肉鸽牌组构筑主机游戏《Raccoin: Chaos Max Edition》于10月28日开放Switch 2试玩版，正式版定于11月10日推出；玩法围绕推币机、特殊硬币与得分修正展开。',[('肉鸽牌组构筑',203,'deckbuilder roguelike'),('《Raccoin: Chaos Max Edition》',203,'Raccoin: Chaos Max Edition'),('10月28日开放Switch 2试玩版',197,'A demo is also available right now'),('11月10日',203,'November 10'),('推币机、特殊硬币与得分修正',203,'special coins and other modifiers')]),
 'Witchbrook':('生活模拟多平台游戏《Witchbrook》定于2027年1月28日登陆PS5、Xbox Series X|S、PC、Switch与Switch 2；玩家将在魔法学校学习、经营生活，并可邀请三名朋友进入同一世界。',[('生活模拟',201,'life sim'),('《Witchbrook》',201,'Witchbrook'),('2027年1月28日',201,'January 28, 2027'),('PS5、Xbox Series X|S、PC、Switch与Switch 2',201,'PS5, Xbox Series X|S, PC, Nintendo Switch, and Nintendo Switch 2'),('邀请三名朋友进入同一世界',201,'invite three of your friends')]),
 'Petal Runner':('像素风冒险主机游戏《Petal Runner》定于2027年3月8日登陆Switch 2；玩家扮演配送数字宠物的摩托车信使，探索太阳朋克世界。',[('像素风',203,'pixel art'),('《Petal Runner》',203,'Petal Runner'),('2027年3月8日',203,'March 8, 2027'),('Switch 2',203,'Switch 2'),('配送数字宠物的摩托车信使',203,'motorcycle courier who delivers digital pets')])}
for nd in nodes:
 d=next(d for d in decisions if d['candidate_id']==nd['candidate_id'])
 if d['decision']!='include':continue
 assert nd['product'] in release_texts,nd['product']
 body,claims=release_texts[nd['product']]
 item(d,nd['product'],body,claims,{'release':{'product':nd['product'],'event':nd['event'],'date':nd['event_date'],'platform':'详见正文与来源','company':'灵游坊' if nd['product']=='影之刃零' else ''}})

# Final editorial corrections, before writing reviewable artifacts.
royal=next(d for d in decisions if d['candidate_id']=='I130')
royal['subject_assessment']['evidence']=[ev(130,'von Tencent')]
for d in decisions:
 if d['candidate_id']=='I242':d['pc_release_scope']={'classification':'multiplayer_or_other','basis':'Rockstar工会投票报道包含GTA6发售背景；非新品上线条目，保留PC/主机范围审计。','evidence':[ev(242,txt(242).splitlines()[0])]}
 if d['candidate_id']=='I187':
  d['scores']={'event':1,'relevance':3,'hook':0,'total':3};d['reason']='逆水寒制作人对MMO的既有战略与运营访谈E1，网易R3；没有新的立项、资本或平台状态，不按E2数据新闻计分。';d['exclusion_gates']=['score']
 if d['candidate_id']=='I201':
  d['decision']='include';d.pop('exclusion_gates',None);d['reason']='E2正式定档×R2有较强声量的长期开发生活模拟产品+M1=5；行业与产品日历独立，两栏均可入选。'
  item(d,'《Witchbrook》定档2027年1月28日，生活模拟扩展到全平台','首次曝光八年后，生活模拟游戏《Witchbrook》确定于2027年1月28日登陆PS5、Xbox Series X|S、PC、Switch与Switch 2。玩家在魔法学校学习，与镇民建立关系，也可邀请三名朋友共同经营、布置房屋或参加扫帚竞速。此次发布明确了正式发售日与平台范围。',[('首次曝光八年后',201,'Eight years after its reveal'),('生活模拟游戏《Witchbrook》',201,'life sim'),('2027年1月28日',201,'January 28, 2027'),('PS5、Xbox Series X|S、PC、Switch与Switch 2',201,'PS5, Xbox Series X|S, PC, Nintendo Switch, and Nintendo Switch 2'),('邀请三名朋友',201,'invite three of your friends'),('扫帚竞速',201,'broomstick race')])
 if d['candidate_id']=='A032':
  d['source_ids']=['S0032'];d['event']='宫本茂对AI创作的观点';d.pop('cluster_basis',None)
decisions.append({**copy.deepcopy(next(d for d in decisions if d['candidate_id']=='A032')),'candidate_id':'A214','source_ids':['S0214'],'event':'樱井政博对AI游戏同质化的观点'})
for it in items:
 if it['candidate_id']=='I160':it['body']=it['body'].replace('本条关注制作人去向。','')
 if it['candidate_id']=='I239':
  it['body']=it['body'].replace('孩之宝表示，他是经过内部与外部候选人遴选后，首位从内部晋升至该职位的人选。','孩之宝称，他是首位内部晋升至该职位的人选。')
  for c in it['claims']:c['claim']=c['claim'].replace('首位从内部晋升至该职位','首位内部晋升至该职位')
 if it['candidate_id']=='C345':it['body']=it['body'].replace('质疑者担心随机收益放大玩家资产差距','争议集中在随机收益是否放大玩家资产差距')
# “Demo available now” proves availability, not that a new test began on this date.
for nd in nodes:
 if nd['product']=='Raccoin: Chaos Max Edition' and nd['signal_type']=='new_game_test':
  nd['publish_eligible']=False;nd['editorial_note']='现已可玩不等于10月28日首次开放测试，缺确切启用日；保留其11月10日多源正式定档节点。'
nodes.sort(key=lambda n:(-int(n['publish_eligible']),-n['priority_score'],-n['company_bonus'],-n['event_type_score'],-n['appearance_count'],-n['industry_bonus'],n['first_seen_order']))
audit['nodes']=nodes;dump('release_calendar_audit.json',audit)
# Re-sync the ranked prefix after the test-date correction; preserve all root metadata.
dump('selection_decisions.json',doc)
sync(P/'release_calendar_audit.json',P/'selection_decisions.json',4)
doc=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));decisions=doc['decisions']
for d in decisions:
 if d['section']=='release_calendar' and d['decision']=='exclude':
  nd=next(n for n in nodes if n['candidate_id']==d['candidate_id']);d['reason']=nd['editorial_note']+'；'+d['reason']
dump('selection_decisions.json',doc)
items[:]=[it for it in items if it['section']!='release_calendar']
release_texts['Raccoin: Chaos Max Edition']=('牌组构筑肉鸽主机游戏《Raccoin: Chaos Max Edition》定于11月10日在Switch 2正式发售；该版本提供专属机台外观与鼠标操作支持。',[('牌组构筑肉鸽',203,'deckbuilder roguelike'),('《Raccoin: Chaos Max Edition》',203,'Raccoin: Chaos Max Edition'),('11月10日',203,'November 10'),('Switch 2正式发售',203,'releases on November 10'),('专属机台外观与鼠标操作支持',203,'exclusive in-game cabinet skin and mouse-control support')])
for nd in nodes:
 d=next(d for d in decisions if d['candidate_id']==nd['candidate_id'])
 if d['decision']!='include':continue
 body,claims=release_texts[nd['product']]
 body=body.replace('登陆PS5、Xbox Series X|S、PC、Switch与Switch 2；','在PS5、Xbox Series X|S、PC、Switch与Switch 2正式发售；').replace('登陆Switch 2；','在Switch 2正式发售；')
 # Claims track the final phrasing, with identical source facts.
 item(d,nd['product'],body,claims,{'release':{'product':nd['product'],'event':nd['event'],'date':nd['event_date'],'platform':'详见正文与来源','company':'灵游坊' if nd['product']=='影之刃零' else ''}})

# Write the mandatory audits before the final report staging file.
item_by={it['candidate_id']:it for it in items}
industry_in=[d for d in decisions if d['section']=='industry_news' and d['decision']=='include']
industry_in.sort(key=lambda d:(-d['scores']['total'],-d['scores']['relevance'],-d['scores']['event'],decisions.index(d)))
order={d['candidate_id']:i for i,d in enumerate(industry_in)}
items.sort(key=lambda it:({'industry_news':0,'ai_trends':1,'release_calendar':2,'community_discourse':3,'deep_analysis':4}[it['section']],order.get(it['candidate_id'],0)))
dump('report_items.json',{'report_type':'daily','date':DATE,'items':items})
lines=['# 卡片曝光去重','近14天与更早archive均检索；历史曝光字段含rank/limit/source。唯一card_carryover为I130：9分、此前未卡片曝光；Atari6分未获名额。','', '# 行业时间口径','source_window_v1：published_at优先，缺失回退input date；事件历史日期不作门禁。较早新品/数据保留真实日期，来源窗外不得用采集日期覆盖。','', '# 维度覆盖自检','国内移动/国产产品与人才/市场数据/并购/平台政策/档期变动/资本组织/海外重大均完成全量262条反扫；新闻与AI严格按事件聚类，日历独立反扫308条，详情见release_reverse_scan.json。','产品日历漏挂反查：逐源全文及结构化清单已扫，单产品+日期建节点，误召回保留排除记录；行业与日历不跨栏互斥。','行业评分记录：事件E×主体R+品类M，E/R为0–3、M为0/1，统一≥5。','', '| candidate | decision | section | score | reason |','| --- | --- | --- | --- | --- |']
candidates=['# 2026-10-28独立事件候选审计','全量348条JSONL已解析；完整index为导航，source text为事实真源；同源广告/正文尾链不补写事实。']
for d in decisions:
 score=d.get('scores',{});lines.append('| '+d['candidate_id']+' | '+d['decision']+' | '+d['section']+' | '+str(score.get('total','—'))+' | '+d['reason'].replace('|','/')+' |')
 candidates+=['','## '+d['candidate_id']+' - '+d['event'],'- section: '+d['section'],'- status: '+d['decision'],'- source_ids: '+', '.join(d['source_ids']),'- entities: '+', '.join(d['entities']),'- event_date: '+str(d.get('time_check',{}).get('event_date','见来源和产品节点')),'- facts: '+ ' / '.join(c['evidence'] for c in item_by.get(d['candidate_id'],{}).get('claims',[])[:3]) if d['candidate_id'] in item_by else '- facts: '+quote(d['source_ids'][0],txt(d['source_ids'][0]).splitlines()[0]),'- notes: '+d['reason']]
 if 'history_check' in d:lines.append('<!-- '+d['candidate_id']+' '+json.dumps(d['history_check'],ensure_ascii=False)+' -->')
 if 'community' in d:candidates.append('- community: '+json.dumps(d['community'],ensure_ascii=False))
(P/'selection_decisions.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(P/'event_candidates.md').write_text('\n'.join(candidates)+'\n',encoding='utf-8')
dump('input_read_audit.json',{'records':len(rows),'text_chars':sum(len(r['text']) for r in rows),'index_records':sum(1 for l in (P/'report_inputs_index.md').read_text(encoding='utf-8').splitlines() if l.startswith('- `S')),'history_json_records':len(history),'history_markdown_chars_read':len(history_md),'full_sources':[{'source_id':r['source_id'],'text_sha256':hashlib.sha256(r['text'].encode()).hexdigest(),'chars':len(r['text'])} for r in rows],'uncovered_noncalendar_sources':[r['source_id'] for r in rows if r['section']!='release_calendar' and r['source_id'] not in covered]})
heads={'industry_news':'一、行业新闻','ai_trends':'二、AI 新闻','release_calendar':'三、新游发布 / 产品日历','community_discourse':'四、玩家舆论 / 社区动态','deep_analysis':'五、行业精选 / 深度观察'}
out=['# 游戏行业日报｜2026-10-28','']
for section,heading in heads.items():
 out+=['## '+heading,'']
 for i,it in enumerate([it for it in items if it['section']==section],1):
  out+=['- '+it['body'],''] if section=='release_calendar' else ['### '+str(i)+'. '+it['title'],'',it['body'],'']
(P/'game_industry_daily_2026-10-28.md').write_text('\n'.join(out),encoding='utf-8')
print('counts', {s:sum(it['section']==s for it in items) for s in heads})
print('calendar',[(n['product'],n['priority_score']) for n in nodes if n['publish_eligible']][:10])
print('uncovered',[r['source_id'] for r in rows if r['section']!='release_calendar' and r['source_id'] not in covered])
