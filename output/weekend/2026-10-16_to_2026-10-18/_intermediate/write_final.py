import json,re,collections
from pathlib import Path
P=Path(__file__).resolve().parent; ROOT=P.parent
R={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
DATA=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8')); DS={d['candidate_id']:d for d in DATA['decisions']}
ITEMS=[]
def sid(n):return f'S{n:04d}'
def add(cid,title,body,proofs,**extra):
 d=DS[cid];assert d['decision']=='include',cid
 claims=[]
 for claim,n,evidence in proofs:
  assert claim in body,(cid,'claim',claim)
  assert evidence in R[sid(n)]['text'],(cid,'evidence',n,evidence)
  assert sid(n) in d['source_ids'],(cid,'source',n)
  claims.append(dict(claim=claim,source_id=sid(n),evidence=evidence))
 item=dict(section=d['section'],title=title,candidate_id=cid,source_ids=d['source_ids'],claims=claims,body=body,**extra)
 ITEMS.append(item)

add('I147','阅文首次披露多IP卡牌手游《群星漫卡》，计划2027年全平台上线',
 '10月16日，阅文在创作大会披露与蹊迹游戏共同开发的电子集换式卡牌手游《群星漫卡》。产品已于9月底完成首轮线上保密测试，预计2027年全平台上线，近期将正式公布并开启首次公开测试。首发内容包括《斗罗大陆》《吞噬星空》《狐妖小红娘》等IP，多IP共存是此次产品公开的主要特征。',[
 ('10月16日，阅文在创作大会披露与蹊迹游戏共同开发的电子集换式卡牌手游《群星漫卡》。',147,'10 月 16 日，2026阅文创作大会正式启幕。'),
 ('阅文在创作大会披露与蹊迹游戏共同开发的电子集换式卡牌手游《群星漫卡》',147,'这款由阅文联合蹊迹游戏共同开发、定位国内首款多IP电子集换式卡牌手游的产品'),
 ('产品已于9月底完成首轮线上保密测试，预计2027年全平台上线',147,'已于 9 月底完成首轮线上保密测试'),
 ('预计2027年全平台上线，近期将正式公布并开启首次公开测试。',147,'《群星漫卡》近期将正式公布，并开启首次公开测试，预计 2027 年全平台上线。'),
 ('首发内容包括《斗罗大陆》《吞噬星空》《狐妖小红娘》等IP',147,'游戏首发集结《斗罗大陆》、《吞噬星空》、《狐妖小红娘》等国民级国漫 IP')])

add('I101','CDPR确认《Project Hadar》已开始开发，尚未进入预制作阶段',
 'CDPR联席首席执行官Michał Nowakowski表示，新IP《Project Hadar》已结束世界观构想，团队开始把概念制作成游戏，但项目尚未进入预制作阶段。公司此前在9月披露团队已有30多人，计划年底增至50人。当前公开的变化是世界构想进入实际制作，发售时间与具体设定仍未公布。',[
 ('CDPR联席首席执行官Michał Nowakowski表示',101,'联席首席执行官Michał Nowakowski表示'),
 ('新IP《Project Hadar》已结束世界观构想，团队开始把概念制作成游戏，但项目尚未进入预制作阶段。',101,'其新IP《Project Hadar》的「世界观构想」阶段现已结束，团队正式开始将这些概念做成游戏。'),
 ('项目尚未进入预制作阶段',101,'不过项目尚未进入预制作阶段。'),
 ('公司此前在9月披露团队已有30多人，计划年底增至50人。',101,'今年9月，CDPR表示正在为《Project Hadar》扩充人手，团队已有30多人，并计划「继续招聘，到今年年底将开发人员增至50人」。'),
 ('发售时间与具体设定仍未公布',101,'我们对《Project Hadar》的世界和设定一无所知')])

add('I104','动视确认正在开发《使命召唤》全新子系列',
 '动视首席营销官Tyler Bahl在采访中确认，旗下工作室正在开发《使命召唤》全新子系列，尚未公布负责团队与发售时间。他同时表示，《现代战争4》将为Infinity Ward自2019年以来讲述的故事收尾，系列后续发展应更多依靠创新。具体背景年代及玩法仍属于外界猜测，此次得到确认的是新子系列已经在研。',[
 ('动视首席营销官Tyler Bahl在采访中确认，旗下工作室正在开发《使命召唤》全新子系列，尚未公布负责团队与发售时间。',104,'动视首席营销官Tyler Bahl近日接受The Game Business采访时确认，旗下一家工作室正在开发《使命召唤》的全新子系列。'),
 ('尚未公布负责团队与发售时间',104,'Bahl没有透露负责开发的工作室，也未公布发售时间'),
 ('《现代战争4》将为Infinity Ward自2019年以来讲述的故事收尾',104,'《现代战争4》将为Infinity Ward自2019年以来讲述的故事画上句号'),
 ('系列后续发展应更多依靠创新',104,'不过，动视认为，《使命召唤》未来的发展应更多依靠创新，而不是倚重既有子系列和熟悉的角色。')])

if DS['I049']['decision']=='include':add('I049','《雾锁王国》推出1.0正式版，补齐生存建造与主线终章',
 'Keen Games的生存动作RPG《雾锁王国》推出1.0正式版，在抢先体验基础上增加浮空岛群落“余烬摇篮”，并补全主线最终章。报道将其长期吸引力归于探索与建造的互相供给：探索产出新建材和工具，建筑投入又为继续远征提供基地支撑。此次正式版继续扩充人物、装备成长与可探索内容。',[
 ('Keen Games的生存动作RPG《雾锁王国》推出1.0正式版',49,'主打生存动作RPG的《雾锁王国》正式迎来了1.0版本'),
 ('Keen Games',49,'开发商Keen Games'),
 ('增加浮空岛群落“余烬摇篮”，并补全主线最终章',49,'前往全新的浮空岛群落“余烬摇篮”，人物和装备的阶级跟着提高了上限，可以刷的东西更多了，外加主线剧情也有了完整的最终章'),
 ('探索产出新建材和工具，建筑投入又为继续远征提供基地支撑',49,'基建狂魔')])

add('I027','多人合作饮品店经营游戏《杯杯倒满》推出1.0正式版',
 '多人合作饮品店经营游戏《杯杯倒满》于10月16日推出1.0正式版，并同步推出新的史低折扣。',[
 ('多人合作饮品店经营游戏《杯杯倒满》于10月16日推出1.0正式版',27,'多人合作饮品店经营游戏《杯杯倒满》于10月16日推出1.0正式版'),
 ('同步推出新的史低折扣',27,'全新史低折扣来了')])

add('I032','国产联机丧尸游戏《隔离区》正式版定档11月6日',
 '国产丧尸游戏《隔离区》宣布正式版定档11月6日，主打联机生存。此次公布的是未来正式版档期，报道同时称产品愿望单达到30万。',[
 ('国产丧尸游戏《隔离区》宣布正式版定档11月6日',32,'国产丧尸游戏《隔离区》正式版定档11月6日'),
 ('主打联机生存',32,'联机生存，末日启程'),
 ('产品愿望单达到30万',32,'30W愿望单')])

add('I353','前《马拉松》总监Joe Ziegler确认已离开Bungie，正制作未公开项目',
 'Joe Ziegler在采访中确认，他在《马拉松》上线后离开Bungie，目前正在制作一个尚未公开的项目。他曾担任《Valorant》游戏总监，并在2024年3月接任《马拉松》项目领导工作。此次访谈没有披露新项目名称、团队或平台；离职发生在产品上线之后，具体日期未公开。',[
 ('Joe Ziegler在采访中确认，他在《马拉松》上线后离开Bungie，目前正在制作一个尚未公开的项目。',353,"Following Marathon's launch, Ziegler left Bungie and is currently working on a new, unrevealed project"),
 ('他曾担任《Valorant》游戏总监，并在2024年3月接任《马拉松》项目领导工作。',353,"game director on Riot's hugely popular arena shooter Valorant"),
 ('在2024年3月接任《马拉松》项目领导工作',353,'which he assumed leadership of in March 2024')])

add('I054','媒体曝光腾讯天美未公开项目《刺客信条：命运》早期取消',
 '据MP1st报道并由游戏新知、竞核转述，腾讯天美曾开发面向PC与主机的《刺客信条：命运》，项目在早期阶段已被取消。公开的原型素材以秦末、楚汉之际为背景，包含女性刺客与项羽相关战斗内容。取消时间尚未明确，报道推测发生在2025年初；这一项目与仍在开发的移动端《刺客信条：Jade》不同，不能据此认定后者也已取消。',[
 ('据MP1st报道并由游戏新知、竞核转述，腾讯天美曾开发面向PC与主机的《刺客信条：命运》，项目在早期阶段已被取消。',54,'两家公司还曾秘密开发另一款《刺客信条》大作，面向当前世代平台 （指PC、主机） ，但该项目在早期阶段便遭到砍掉。'),
 ('腾讯天美',54,'由腾讯天美工作室主导'),
 ('公开的原型素材以秦末、楚汉之际为背景，包含女性刺客与项羽相关战斗内容。',260,'该作设定在公元前206年的秦末/楚汉之际，主角为一名女性刺客，并且可能包含一场与项羽的Boss战斗。'),
 ('报道推测发生在2025年初',260,'据推测，项目被叫停的时间在2025年初。'),
 ('仍在开发的移动端《刺客信条：Jade》',54,'《Jade》只是延期并未取消，项目仍在开发中。')])

add('I012','Xbox成立Labs小团队，探索游戏制作与反编译',
 'Xbox成立Xbox Labs，由游戏开发者、工程师和科学家组成小团队，探索新的技术与制作方式。本期GameDiscoverCo介绍，其探索方向包括游戏反编译；团队以实验方式验证技术如何进入游戏制作与体验。',[
 ('Xbox成立Xbox Labs，由游戏开发者、工程师和科学家组成小团队',306,'the company is launching Xbox Labs , “a small group of game makers, engineers and scientists”'),
 ('探索方向包括游戏反编译',306,'to experiment with decompilation & more'),
 ('探索新的技术与制作方式',12,'Xbox设立全新Xbox Labs团队')])

add('I036','《英雄联盟》经典模式上线三个多月后关闭',
 '据GameLook报道，拳头与腾讯推出的《英雄联盟》经典模式在6月底上线三个多月后关闭。该模式从历代版本提取英雄、装备与机制，由小团队负责，研发资源优先级低于正式服。报道记录了英雄扩充偏慢、菜单及素材问题；将其理解为完成短期召回目标，是报道的分析判断。',[
 ('拳头与腾讯推出的《英雄联盟》经典模式',36,'拳头联合腾讯拿出了一个大胆的回应方案：推出《英雄联盟》经典模式'),
 ('在6月底上线三个多月后关闭',36,'距离今年6月底上线才3个多月，就迎来了关停的结局'),
 ('从历代版本提取英雄、装备与机制',36,'从历代版本里提取经典英雄、装备与机制'),
 ('由小团队负责，研发资源优先级低于正式服',36,'项目由小规模团队负责，人力优先级始终低于正式服主线更新'),
 ('英雄扩充偏慢、菜单及素材问题',36,'英雄扩充速度缓慢、菜单报错、美术素材错位')])

add('I069_TI','《Titanium Court》宣布10月29日登陆移动端与主机',
 'Fellow Traveller宣布，融合三消与塔防的《Titanium Court》将于10月29日登陆iOS、Android、PS5、Switch和Switch 2，全球售价6.99美元。该作由AP Thomson创作，已在4月登陆PC。此次扩展把既有PC作品带到触屏设备与更多主机平台。',[
 ('Fellow Traveller宣布，融合三消与塔防的《Titanium Court》将于10月29日登陆iOS、Android、PS5、Switch和Switch 2',69,'Fellow Traveller’s Titanium Court, a match 3 and tower defence game, comes to iOS, Android, PS5, Switch and Switch 2 on October 29 after debuting on PC in April.'),
 ('全球售价6.99美元',69,'Titanium Court will be available for $6.99 globally.'),
 ('该作由AP Thomson创作，已在4月登陆PC',69,'Created by AP Thomson (Consume Me, Fortune-499)')])

add('I137','Jagex撤销《RuneScape Reignited》计划，避免新服分裂原有社区',
 'Jagex在公布《RuneScape Reignited》不到两周后决定取消该计划。原方案让新玩家和回流玩家在独立服务器重新开始，曾引发社区分裂、角色互动受限和需额外订阅的担忧。团队先道歉并提出修改，随后明确停止推进，表示拉新与召回不能以损害现有社区为代价。',[
 ('Jagex在公布《RuneScape Reignited》不到两周后决定取消该计划。',137,'Less than two weeks after announcing RuneScape Reignited'),
 ('决定取消该计划',137,'the studio has decided to cancel it.'),
 ('新玩家和回流玩家在独立服务器重新开始',137,'a way for new and lapsed players to restart their adventures from fresh on separate, unique servers'),
 ('社区分裂、角色互动受限和需额外订阅的担忧',137,'complaints ranging from a potential community split to restrictions on character interactions and the need to pay for a separate subscription'),
 ('拉新与召回不能以损害现有社区为代价',137,'with returning players coming back and new players joining, but never at the expense of our existing community')])

add('I126_AP','在线合作经营游戏《AMPANIC》列入10月16日Steam发行清单',
 '《AMPANIC》列入10月16日的Steam发行清单，主打在线合作商店经营。玩家以瞄准操作完成收集、加工、调合与接待，顾客流失会触发游戏结束。其玩法将射击操作的甩枪、跟枪与多人店铺分工结合。',[
 ('《AMPANIC》列入10月16日的Steam发行清单，主打在线合作商店经营。',126,'AMPANIC\n关键字： 在线合作、商店管理、动作、制作\n发行日期： 2026/10/16'),
 ('玩家以瞄准操作完成收集、加工、调合与接待，顾客流失会触发游戏结束。',126,'收集、加工、调合、接待顾客，全都靠你的瞄准完成。让顾客跑掉就会 Game Over！'),
 ('甩枪、跟枪与多人店铺分工结合',126,'掌握甩枪与跟枪瞄准，在混乱中维持商店运转。支持在线多人游戏！')])

add('I308_ST','9月37家中国手游发行商合计收入20亿美元，占全球百强41.6%',
 '据竞核汇总的Sensor Tower数据，9月有37家中国手游厂商进入全球手游发行商收入百强，合计收入20亿美元，占百强总收入41.6%。其中哔哩哔哩收入环比增长36%，排名提升7位；《阴阳师》十周年带动收入环比增长超过170%，《原神》六周年版本收入环比增长42%。这组数据反映的是发行商与产品在当月的收入表现。',[
 ('9月有37家中国手游厂商进入全球手游发行商收入百强，合计收入20亿美元，占百强总收入41.6%。',308,'2026年9月共有37家中国手游厂商跻身全球手游发行商收入TOP100，合计收入20亿美元，占百强发行商总收入41.6%。'),
 ('据竞核汇总的Sensor Tower数据',308,'据 Sensor Tower 数据显示'),
 ('哔哩哔哩收入环比增长36%，排名提升7位',308,'哔哩哔哩收入环比增长36%，排名上升 7 位'),
 ('《阴阳师》十周年带动收入环比增长超过170%，《原神》六周年版本收入环比增长42%。',308,'《阴阳师》 十周年收入环比大涨超170%，《原神》六周年版本收入回升，环比增长42%')])

add('I263_CK','Devsisters与Big Shot Pictures合作《跑跑姜饼人》电影，目标2029年上映',
 'Devsisters宣布与Big Shot Pictures合作，将《跑跑姜饼人》系列改编成电影，目标2029年全球上映。该时间点对应系列诞生20周年；按公司披露，这一IP全球累计吸引超过3.5亿名玩家。此次公布的是电影合作计划。',[
 ('Devsisters宣布与Big Shot Pictures合作，将《跑跑姜饼人》系列改编成电影，目标2029年全球上映。',263,'韩国游戏公司Devsisters宣布，将与Big Shot Pictures合作，把《跑跑姜饼人》系列改编成电影，目标是在2029年全球上映'),
 ('对应系列诞生20周年',263,'恰逢系列诞生20周年'),
 ('这一IP全球累计吸引超过3.5亿名玩家',263,'这个 IP 在全球已吸引超过3.5亿名玩家')])

add('I129','《BagMaster Isekai》开发复盘披露收入增长，四人团队借发行服务补齐验证能力',
 '据罗斯基整理的开发案例，Doors Studio的背包构筑手游《BagMaster Isekai》于3月全球发行；AppMagic数据记录，其3月至5月月内购收入由2.6万美元增至25万美元，月下载量由32万增至80万以上。团队最初只有4人，借SayGames的数据工具、对照测试与发行服务反复调整系统，至6月扩大到12人。案例回顾展示了小团队如何连接玩法探索与商业验证。',[
 ('Doors Studio的背包构筑手游《BagMaster Isekai》于3月全球发行',129,'今年3月，一款融合背包管理、肉鸽成长和回合制战斗的手游《BagMaster Isekai》正式面向全球发行。'),
 ('3月至5月月内购收入由2.6万美元增至25万美元，月下载量由32万增至80万以上',129,'根据AppMagic数据，3月至5月，该作上线两个月的时间，月内购收入从2.6万美元增长至25万美元，月下载量也从32万攀升至80万以上。'),
 ('Doors Studio',129,'《BagMaster Isekai》开发商Doors Studio'),
 ('团队最初只有4人',129,'初始团队也只有4个人'),
 ('借SayGames的数据工具、对照测试与发行服务反复调整系统',129,'SayGames为项目提供了分析基础设施。'),
 ('对照测试',129,'利用对照测试比较不同方案，观察用户的实际反应后再作决定'),
 ('至6月扩大到12人',129,'到了2026年6月，工作室已经拥有12名成员')])

add('I055','昆仑万维AI游戏平台GameWave下载突破1000万，日活约50万',
 '据游戏新知援引Sensor Tower数据，昆仑万维旗下GameWave自6月上线、8月起量后，累计下载超过1000万，近期日活约50万。平台让用户上下滑动试玩AI生成的轻量游戏，也可通过对话生成、迭代作品或套用模板二创。印尼与菲律宾分别贡献27%和10%的下载，超过99%的下载来自Android；其商业化方式仍在探索。',[
 ('昆仑万维旗下GameWave自6月上线、8月起量后，累计下载超过1000万，近期日活约50万。',55,'昆仑万维入局是晚了点，但旗下《GameWave》起量很猛'),
 ('自6月上线、8月起量后，累计下载超过1000万，近期日活约50万',55,'该平台于今年6月上线，8月开始发力， 现已拿下1000万下载 ！近期日活涨到50万左右'),
 ('通过对话生成、迭代作品或套用模板二创',55,'用户也可以直接套用他人的游戏模版进行二创 （Remix）'),
 ('印尼与菲律宾分别贡献27%和10%的下载，超过99%的下载来自Android',55,'平台的第一大市场是印尼，贡献了27%的下载，其次是菲律宾，占比10%'),
 ('超过99%的下载来自Android',55,'平台超过99%的下载量来自安卓端。'),
 ('其商业化方式仍在探索',55,'《GameWave》的商业化路径还没有落地')])

add('I045','《星空》模组作者借AI辅助逆向，展示从太空到地表的连续降落',
 '模组开发者Frederik Wessberg公开“Seamless Landings”演示，称独自用约半年、借助AI辅助逆向分析与开发，做出从太空下降至《星空》地表的连续体验。其方法是在后台加载地表资源，再用云层及再入特效遮蔽约130毫秒的场景切换。模组仍在开发，尚未公布上线时间；演示不代表原版引擎已实现完全无切换。',[
 ('模组开发者Frederik Wessberg公开“Seamless Landings”演示',45,'MOD开发者Frederik Wessberg公开了其MOD“Seamless Landings”的演示'),
 ('独自用约半年、借助AI辅助逆向分析与开发',45,'作者明确表示，他一个人花了约半年，借助AI工具的辅助，把MOD制作到了可以公开演示的程度。'),
 ('从太空下降至《星空》地表的连续体验',45,'飞船从太空接近行星，进入大气层，穿过云层，再一路下降到地表，整个过程不再弹出熟悉的加载画面。'),
 ('云层及再入特效遮蔽约130毫秒的场景切换',45,'作者称，这一步约需130毫秒，通过云层或再入特效遮蔽。'),
 ('模组仍在开发，尚未公布上线时间',45,'目前，这款免费MOD仍在开发，尚未公布上线时间。')])

add('I148','极逸人工智能计划10月20日推出SoonPlay，加入视频生成游戏入口',
 '恺英网络旗下极逸人工智能宣布，计划10月20日推出轻游平台SoonPlay，将短视频浏览、游戏体验与创作放在同一应用中。按其公布的方案，用户可上传文字、图片或视频，由AI识别可互动内容并生成作品，原视频与对应游戏可在平台内切换。平台现阶段主打无广告、无内购与不限游玩时长；这些是发布计划与产品方介绍，尚不代表已完成规模化运营验证。',[
 ('恺英网络旗下极逸人工智能宣布，计划10月20日推出轻游平台SoonPlay',148,'恺英 网络（002517.SZ） 旗下 极逸人工智能 将于2026年 10月20日 正式推出首个轻游平台 A PP SoonPlay。'),
 ('短视频浏览、游戏体验与创作放在同一应用中',148,'打通短视频浏览、游戏体验与游戏 开发 三大场景'),
 ('用户可上传文字、图片或视频',148,'用户可通过输入文字，或上传图片、视频等素材，借助AI生成专属游戏作品。'),
 ('原视频与对应游戏可在平台内切换',148,'原视频与由其生成的游戏在平台内同步上线，用户浏览内容时可随时从观看状态切换至游玩状态'),
 ('无广告、无内购与不限游玩时长',148,'产品现阶段主打无广告、无内购、不限时长畅玩')])

add('I279','Alliance Arts因担忧AI克隆取消公开Demo，改为限量封闭试玩',
 'Alliance Arts取消《Drunken Goddess Reflux》原定10月19日推出的Steam公开Demo，改为有限名额的封闭线上试玩。开发商表示，除难以管理视频与直播限制外，也担心试玩中的表现和玩法被AI等工具迅速模仿、抢在正式发售前发布。此次案例体现AI复制风险已经影响具体发行安排，不能据此推断其作品已经遭到克隆。',[
 ('Alliance Arts取消《Drunken Goddess Reflux》原定10月19日推出的Steam公开Demo',279,'developer Alliance Arts planned to release a Steam demo on October 19'),
 ('《Drunken Goddess Reflux》',279,'Drunken Goddess Reflux is a "shot glass Russian roulette" drinking game'),
 ('改为有限名额的封闭线上试玩',279,'the studio will host "closed online play sessions for a limited number of participants."'),
 ('难以管理视频与直播限制',279,'"some restrictions on posting and streaming gameplay videos"'),
 ('担心试玩中的表现和玩法被AI等工具迅速模仿、抢在正式发售前发布',279,"We're concerned that the demo's content could be used to quickly imitate or replicate the game's presentation and gameplay with AI or other tools, and that such works could be released before launch.")])

add('A161','FLUX图像模型支持单消费级GPU，视频扩分价格降至每秒0.28美元',
 '据OpenRouter公告，FLUX 3 Image Klein开放权重，可在单张消费级GPU运行；FLUX Video Upscale进入早期访问，每秒价格由0.59美元降至0.28美元，可把视频提升至4K。FLUX 3 Video同时支持由提示词生成4K视频。对游戏制作而言，单机试稿与视频处理成本变化可作用于美术原型及宣发素材迭代，但公告并未披露具体游戏项目的采用结果。',[
 ('FLUX 3 Image Klein开放权重，可在单张消费级GPU运行',161,'FLUX 3 Image Klein，一款新的开放权重图像模型，可在单张消费级 GPU 上运行'),
 ('FLUX Video Upscale进入早期访问，每秒价格由0.59美元降至0.28美元，可把视频提升至4K',161,'改进版 FLUX Video Upscale 进入早期访问，可将任何视频转为 4K，价格为 $0.28/秒（原为 $0.59/秒）'),
 ('FLUX 3 Video同时支持由提示词生成4K视频',161,'FLUX 3 Video 现在可以根据提示词生成 4K 视频')])

add('A287','Anthropic重构AI代码评审，把验证证据与风险分级接入开发流程',
 '据对Anthropic技术文章的解读，Claude编写了Claude Code约90%的代码，6月至9月合并的代码变更数量翻倍以上，回退比例下降超过40%。团队把自我验证、独立自动评审、安全检查与风险分级串联，并限制重复审查只看新增变化。可迁移到游戏研发的环节是代码与工具链验证：AI提高产出速度后，自动测试、明确责任与回滚机制可能减少人工评审瓶颈；上述结果属于该团队经验。',[
 ('Claude编写了Claude Code约90%的代码，6月至9月合并的代码变更数量翻倍以上，回退比例下降超过40%',287,'Claude 写了约 90% 的代码，2026 年 6 月到 9 月合并 PR 翻倍以上而 revert 率下降超 40%'),
 ('自我验证、独立自动评审、安全检查与风险分级',287,'七层防线：一个变更的一生'),
 ('限制重复审查只看新增变化',287,'后续轮次只看增量 diff')])

ADD_RELEASE=[d for d in DS.values() if d['section']=='release_calendar' and d['decision']=='include']
assert len(ADD_RELEASE)==1,ADD_RELEASE
rcid=ADD_RELEASE[0]['candidate_id']
add(rcid,'Rain98','Lo-Fi风格的心理悬疑冒险端游《Rain98》于10月16日推出Steam体验版；试玩内容时长超过3小时。',[
 ('10月16日',214,'Announcement date: 2026-10-16 16:34'),
 ('Lo-Fi风格的心理悬疑冒险端游《Rain98》',258,'Lo-Fi×心理悬疑冒险游戏《Rain98》'),
 ('推出Steam体验版；试玩内容时长超过3小时',258,'Steam体验版正式上线，游玩时长超过3小时')],release=dict(product='Rain98',event='Steam体验版上线',date='2026-10-16',platform='Steam',company='来源未提供'))

c1=dict(trigger='新版本后PC掉帧、卡死反馈',claim_scope='玩家体验与技术猜测；内存泄漏未经官方确认',complaint_logic='问题跨版本延续、低帧与稳定性恶化，临时清理缓存不能替代根本修复',timeline=['10月17日00:24建帖','10月18日仍有设备负载与帧数补充'],follow_up_scan='已反扫S0037/S0038/S0044/S0222/S0223/S0298/S0308/S0359及全部41条社区；未找到对应优化修复回应，其他角色、封号与AIGC事件不并入。')
DS['C297']['community']=c1
add('C297','《终末地》新版本PC掉帧与卡死被集中反馈，玩家质疑问题跨版本延续',
 '《明日方舟：终末地》PC玩家在新版本后反馈掉帧、卡死及低帧不稳定，部分玩家称早期版本流畅度更好。10月17日出现集中讨论，至18日仍有玩家补充CPU负载与实测帧数。玩家不满的核心在于优化问题被认为持续多个版本、临时清理着色器或切换场景只能缓解体验；将原因归于内存泄漏则是帖内玩家的技术判断。',[
 ('PC玩家在新版本后反馈掉帧、卡死及低帧不稳定',297,'新版本PC优化跳水，多人反馈掉帧卡死'),
 ('部分玩家称早期版本流畅度更好',297,'直到弭弗和卡缪那个版本优化确实好，但是诀那个版本开始优化明显有问题了'),
 ('10月17日出现集中讨论，至18日仍有玩家补充CPU负载与实测帧数',297,'发帖：2026-10-17T00:24'),
 ('CPU负载与实测帧数',297,'个人游玩体验，cpu压力比较大，温度较高'),
 ('临时清理着色器或切换场景只能缓解体验',297,'虽然自己删除着色器文件能治标不治本一会'),
 ('将原因归于内存泄漏则是帖内玩家的技术判断',297,'终末地卡顿大多数是因为内存泄露的原因')],community=c1)

c2=dict(trigger='玩家对比绿梦与崩铁的子弹素材',claim_scope='玩家指认与对比，未认定官方侵权事实',complaint_logic='纹样、长度和口径变化被认为超出同类物品通常相似度，质疑素材采购与美术审核',timeline=['10月16日20:51原帖','17—18日补充对比与素材来源猜测'],follow_up_scan='反扫S0037/S0038/S0303/S0305/S0364/S0365及全部社区池；S0038炸服道歉属于另一事件，不混作素材争议回应；未发现本窗口对应官方处置正文。')
DS['C365']['community']=c2
add('C365','《绿梦》子弹素材被指与《崩铁》高度相似，玩家质疑美术审核',
 '《绿梦》被玩家指出现与《崩铁》高度相似的子弹素材，对比集中在表面纹样、长度与口径变化。10月16日相关对比出现后，17日至18日仍有玩家继续讨论素材来源与采购审核。争议集中在这些细节是否已超出同类物品的通常相似度；有玩家怀疑素材选用出了问题，也有人把矛头转向团队的美术审核与研发投入。',[
 ('《绿梦》被玩家指出现与《崩铁》高度相似的子弹素材',365,'绿梦中出现与崩铁高度相似的游戏素材'),
 ('表面纹样、长度与口径变化',365,'感觉上面那个两发的子弹连花纹都是一样的，但变胖了，长度不变口径变大了'),
 ('10月16日相关对比出现后，17日至18日仍有玩家继续讨论',365,'发帖：2026-10-16T20:51'),
 ('有玩家怀疑素材选用出了问题',365,'这种是素材找的随便，不知道来自崩坏'),
 ('研发投入',365,'游戏做3年钱花哪去了')],community=c2)

deepbody='观察：Steam核心玩家也在跨设备分配游玩时间。跨端发行可能触达同一批用户的新场景，因此平台新增用户不能直接等同为新增人群。\n\n分析：GameDiscoverCo以超过1.6万名Steam玩家的调查为基础，把设备使用与获准关联的游戏库数据结合。样本中，同时玩PC与手机、但不玩主机的受访者占22%，三端都玩的占15.6%。这些重叠意味着“PC用户”“手游用户”并非互斥群体：同一玩家在不同设备上可能寻找不同游玩时段，跨平台新增量需要区分首次接触产品与已有用户换设备。\n\n平台重叠也会改变发行效果的解释。单个平台活跃提升，可能既包含新客，也包含同一用户的时间重分配；若只加总各端账户规模，就容易高估实际覆盖。调查通过线上赠奖招募，覆盖的是更活跃、熟悉网络的Steam玩家，作者明确提醒其不能代表全部PC玩家，更不能直接推算普通手游或主机用户的交叉比例。这份样本更适合检验“用户只属于一个平台”的假设，而非给出全市场跨端转化率。'
add('D306','Steam核心玩家也跨端游玩，平台新增用户不能直接视为新增人群',deepbody,[
 ('GameDiscoverCo以超过1.6万名Steam玩家的调查为基础',306,'GameDiscoverCo asked >16,000 worldwide Steam players'),
 ('把设备使用与获准关联的游戏库数据结合',306,'tied it into their Steam catalog, with their permission'),
 ('同时玩PC与手机、但不玩主机的受访者占22%，三端都玩的占15.6%',306,'22% of respondents who play PC and mobile games (but no console)'),
 ('三端都玩的占15.6%',306,'15.6% of respondents who play PC, console, and mobile'),
 ('调查通过线上赠奖招募',306,'who we recruited by offering giveaways online'),
 ('覆盖的是更活跃、熟悉网络的Steam玩家',306,'We’re surveying a more turned-on, online-savvy subset'),
 ('不能代表全部PC玩家',306,'we’re not saying this is perfectly indicative of all PC or Steam gamers')],card_copy=dict(source_label='GameDiscoverCo调查分析',summary='Steam核心玩家与手机、主机用户存在明显重叠，跨端新增需要区分新客、设备切换和游玩时间重分配。',insights=[dict(title='设备标签不等于独立人群',detail='调查中的PC与手机双端、三端用户说明，同一玩家可能同时属于多个平台群体。'),dict(title='跨端规模需要拆解来源',detail='新平台账户增长可能来自新客，也可能来自既有玩家切换设备，直接加总容易高估覆盖。'),dict(title='核心样本不能代表全市场',detail='线上赠奖招募的Steam玩家更活跃，适合检验平台互斥假设，不能直接推算普通手游用户的转化率。')]))

SEC={'industry_news':'一、行业新闻','ai_trends':'二、AI 新闻','release_calendar':'三、新游发布 / 产品日历','community_discourse':'四、玩家舆论 / 社区动态','deep_analysis':'五、行业精选 / 深度观察'}
out=['# 游戏行业周末报｜2026-10-16 至 2026-10-18','', '覆盖日期：2026年10月16日—18日（北京时间）。','']
ordered=[]
for section,heading in SEC.items():
 arr=[i for i in ITEMS if i['section']==section]
 if section=='industry_news':arr.sort(key=lambda i:(-DS[i['candidate_id']]['scores']['total'],-DS[i['candidate_id']]['scores']['relevance']))
 out+=['## '+heading,'']
 for num,i in enumerate(arr,1):
  out+=['- '+i['body'],''] if section=='release_calendar' else [f"### {num}. {i['title']}",'',i['body'],'']
 ordered.extend(arr)
assert {d['candidate_id'] for d in DS.values() if d['decision']=='include'}=={i['candidate_id'] for i in ordered}
stage=P/'staging';stage.mkdir(exist_ok=True)
REPORT=stage/'game_industry_weekend_2026-10-16_to_2026-10-18.md'
REPORT.write_text('\n'.join(out),encoding='utf-8')
(P/'report_items.json').write_text(json.dumps({'items':ordered},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
AUD=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
for n in AUD['nodes']:
 if DS[n['candidate_id']]['decision']=='exclude':DS[n['candidate_id']]['reason']=n['editorial_reason']
DATA['decisions']=list(DS.values())
(P/'selection_decisions.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

dim={'国内移动/国产产品与人才':r'腾讯|网易|阅文|米哈游|西山居|国产|拳头|Bungie|Joe Ziegler','市场数据':r'Sensor Tower|收入|销量|调查|Circana','并购':r'融资|投资|入股|破产|收购','平台政策':r'Steam|数字游戏所有权|Google Play|App Store','档期变动':r'停运|取消|测试|公测|发售|上线|档期','资本组织':r'Labs|岗位|裁员|总监|工作室|股权','海外重大':r'动视|CDPR|Xbox|Jagex|Liquid Swords|RedLynx'}
counts={k:sum(d['section']=='industry_news' and bool(re.search(p,d['event']+' '+str(d['entities']),re.I)) for d in DS.values()) for k,p in dim.items()}
md=['# 筛选决策｜2026-10-16_to_2026-10-18','', '卡片曝光去重：历史窗口2026-10-02至2026-10-15，共92条。Xbox Labs在2026-10-14日报及2026-10-09_to_2026-10-15周报均card_exposed=false、card_rank=null、card_limit=10，publish_log_manifest；当前8分胜过7分战狗等候选，唯一card_carryover。Flow融资、库洛入股、公测等已曝光旧事件重复排除。无material_update及新增实质状态事实。','', '维度覆盖自检：'+' / '.join(f'{k} {v}张候选' for k,v in counts.items())+'（维度可交叉，非入选配额）。','', 'AI行业反扫：全量行业候选已反扫，4条直接作用及2条迁移价值入选；行业/AI同事件不重复。社区全池按产品、角色与机制补扫，2条入选。产品日历逐条反扫241条行业与44条日历记录，不因行业采用/排除互斥。','', '周一无周五飞书回执/selection交接；深度优先阅读本期唯一newsletter，成一完整主题。Steam10月16—18日当日榜目录缺失，未使用旧榜或周榜替代。','', '日历：保留原抽取release_calendar_audit.raw.json，纠正历史月份、晚到转载、普通运营和同URL/同站多语言计数。Rain98独立来源前缀入选1条。链兽角斗的斜杠日期来自预排列表且缺绝对实际发行确认；现代战争4为部分战役抢先体验且英文日期未被现有证据校验接受，两者保留审计、不伪造ISO证据。行业和产品日历不做跨栏互斥。','', '| candidate | decision | target_section | scores | reason |','| --- | --- | --- | --- | --- |']
for d in DS.values():
 label='merge into '+d['merge_into'] if d['decision']=='merge' else d['decision']
 sc=d.get('scores',{})
 scoretext=f"事件{sc['event']}×相关{sc['relevance']}+钩子{sc['hook']} = {sc['total']}" if d['section']=='industry_news' else json.dumps(sc,ensure_ascii=False)
 md.append(f"| {d['candidate_id']} | {label} | {d['section']} | {scoretext} | {d['reason'].replace('|','/')} |")
md.insert(10,'产品日历漏挂反查：已全文反扫industry_news与release_calendar，共285条；136个原始修订节点继续按同产品同日聚类，每个召回均有include/exclude。行业日历允许独立同选，普通版本和旧月份不召回为新品；绝对日期与独立来源门槛单独复核。')
(P/'selection_decisions.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
stats={'counts':dict(collections.Counter(i['section'] for i in ordered)),'sources':len({x for i in ordered for x in i['source_ids']}),'industry_scores':[{**{k:i[k] for k in ['candidate_id','title']},**DS[i['candidate_id']]['scores']} for i in ordered if i['section']=='industry_news'],'boundaries':[{k:d.get(k) for k in ['candidate_id','event','scores','reason']} for d in DS.values() if d['section']=='industry_news' and d.get('scores',{}).get('total') in [5,6] and d['decision']!='merge'],'repeat_only_excluded':[d['candidate_id'] for d in DS.values() if d['section']=='industry_news' and d['decision']=='exclude' and d.get('history_check',{}).get('novelty')=='repeat_only'],'history_window':json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))['history_window']}
(P/'run_summary.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False,indent=2))
