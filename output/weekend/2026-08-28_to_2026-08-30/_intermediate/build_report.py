import json, pathlib, re, hashlib, difflib
from datetime import datetime
P=pathlib.Path(__file__).parent
ROOT=P.parents[3]
ID='2026-08-28_to_2026-08-30'
rows=[json.loads(x) for x in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
S={r['source_id']:r for r in rows}
H=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))['occurrences']
def ids(ns): return [f'S{n:04d}' for n in ns]
def dump(name,data): (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
D=[]; ITEMS=[]; used=set()
def history(nums,novelty=None,facts=None):
    old=[dict(H[n-1],history_index=n) for n in nums]
    labels=[o['title']+' | '+o['report_kind']+' '+o['report_window']['start']+'_to_'+o['report_window']['end'] for o in old]
    return dict(history_match=bool(old),novelty=novelty or ('repeat_only' if old else 'new_event'),prior_occurrences=labels,prior_details=old,new_facts=facts or [],prior_card_exposed=any(o['card_exposed'] for o in old) if old else None)
def candidate(cid,title,ns,E=0,R=0,M=0,decision='exclude',reason='',entities=None,hist=None,novelty=None,new_facts=None,section='industry_news',event_date=None,**extra):
    ss=ids(ns); used.update(ss)
    d=dict(candidate_id=cid,title=title,section=section,source_ids=ss,entities=entities or [title],event=title,event_date=event_date or S[ss[0]]['date'],decision=decision,reason=reason)
    if section=='industry_news':
        d['scores']=dict(event=E,relevance=R,hook=M,total=E*R+M)
        d['history_check']=history(hist or [],novelty,new_facts)
        if novelty=='card_carryover': d['card_carryover']=True
    if len(ss)>1: d['cluster_basis']=dict(subject=(entities or [title])[0],product=title,event_date=d['event_date'],event=title)
    d.update(extra);D.append(d);return d
def evidence(sid,needle):
    t=S[sid]['text']; assert needle in t,(sid,needle)
    # Retain the complete paragraph containing the editorially selected evidence.
    return next((p for p in t.split('\n') if needle in p),needle)
def item(d,title,paras,claims,**extra):
    it=dict(candidate_id=d['candidate_id'],section=d['section'],title=title,source_ids=d['source_ids'],body='\n\n'.join(paras),claims=[])
    for claim,n,needle in claims:
        sid=f'S{n:04d}'; assert claim in title+'\n'+it['body'],claim
        it['claims'].append(dict(claim=claim,source_id=sid,evidence=evidence(sid,needle)))
    it.update(extra);ITEMS.append(it);return it

# Independent industry events: E/R/M, history and source text are adjudicated separately.
d=candidate('I001','腾讯ACE与Sandbox Interactive合作',[33,350],3,3,2,'include','同一签约事件；上周正文第13条未进入订阅卡片，本期11分为未曝光合格项最高者。',entities=['腾讯ACE','Sandbox Interactive'],hist=[131],novelty='card_carryover',event_date='2026-08-27')
item(d,'腾讯ACE与Sandbox Interactive合作，为《Albion Online》安卓端提供反作弊支持',[
'腾讯游戏安全ACE、腾讯云与Sandbox Interactive宣布合作，《Albion Online》安卓客户端将接入ACE Standard反作弊方案，计划于2026年第三季度上线。方案结合客户端、服务端验证与代码加固，并向厂商提供反作弊API和对局准入数据。'],[
('腾讯游戏安全ACE、腾讯云与Sandbox Interactive宣布合作',33,'共同宣布达成合作'),('《Albion Online》安卓客户端将接入ACE Standard反作弊方案，计划于2026年第三季度上线',33,'安卓客户端将于2026年第三季度上线'),('客户端、服务端验证与代码加固',33,'从客户端到服务端，再到代码加固'),('反作弊API和对局准入数据',33,'反作弊API、对局准入数据')])
d=candidate('I002','《征服纪：臣民之心》首次公开',[22,59,297],3,3,2,'include','首支预告和商店页面公开；殖民经营与4X为优先赛道。日历低于前四，行业独立收录。',entities=['MicroSimulation','集英社游戏','征服纪：臣民之心'])
item(d,'集英社游戏公布《征服纪：臣民之心》，结合殖民模拟与4X策略',[
'MicroSimulation开发、集英社游戏发行的《征服纪：臣民之心》正式公开，计划于2027年夏季在Steam发售。玩家从聚落建设推进到国家经营，居民的日常活动、愿望与不满可以影响贸易、叛乱和外交；项目同步公开首支预告并上线商店页面。'],[
('MicroSimulation开发、集英社游戏发行',59,'由株式会社MicroSimulation'),('《征服纪：臣民之心》正式公开，计划于2027年夏季在Steam发售',59,'将于2027年夏季在Steam'),('居民的日常活动、愿望与不满可以影响贸易、叛乱和外交',59,'酒馆中市民间的闲谈可能成为叛乱的导火索'),('公开首支预告并上线商店页面',59,'本日同步公开了首支宣传预告片')])
d=candidate('I003','巨人网络与Garena合作推进《超自然行动组》海外发行',[37],3,3,1,'include','独立发行合作事件，与历史DAU里程碑不同；正文不重复DAU和常规财报。',entities=['巨人网络','Garena','超自然行动组'])
item(d,'《超自然行动组》与Garena达成合作，计划进入东南亚和拉美',[
'巨人网络披露，《超自然行动组》已与Garena达成战略合作，计划于2027年第一季度登陆东南亚、拉美市场。该安排属于后续区域发行计划，尚未进入上述市场的正式上线阶段。'],[
('巨人网络',37,'巨人网络'),('《超自然行动组》已与Garena达成战略合作，计划于2027年第一季度登陆东南亚、拉美市场',37,'《超自然行动组》已与知名游戏运营商Garena达成战略合作')])
d=candidate('I004','《燕云十六声》全球玩家突破一亿',[50,111,385],2,3,2,'include','独立玩家规模里程碑；不是常规版本或奖项宣传。',entities=['网易','燕云十六声'])
item(d,'网易《燕云十六声》全球玩家突破一亿',[
'网易《燕云十六声》于8月28日披露，全球玩家已突破一亿。该数字为官方公布的累计玩家规模，体现武侠开放世界产品的覆盖范围，并非日活跃用户口径。'],[
('网易《燕云十六声》于8月28日',111,'8月28日，网易旗下'),('全球玩家已突破一亿',111,'全球游侠现已突破一亿人')])
d=candidate('I005','《赘婿》上线后榜单走势披露',[46],2,3,1,'include','国产模拟经营新品的早期商业反馈，保留最新跌出百名事实，不仅摘录峰值。',entities=['三七互娱','厦门延趣','赘婿'])
item(d,'三七互娱《赘婿》曾进入微信小游戏畅销前15，随后跌至百名外',[
'厦门延趣研发、三七互娱发行的模拟经营游戏《赘婿》于8月12日全平台上线，曾进入微信小游戏畅销榜前15；报道发布时已跌至百名以外。其App端曾达到iOS畅销榜第83名，产品以男频网文IP包装竖屏经营、门客养成与商战玩法。'],[
('厦门延趣研发、三七互娱发行的模拟经营游戏《赘婿》于8月12日全平台上线',46,'由厦门延趣研发、三七互娱发行'),('曾进入微信小游戏畅销榜前15；报道发布时已跌至百名以外',46,'滑落到百名开外'),('iOS畅销榜第83名',46,'iOS畅销榜第83位'),('男频网文IP包装竖屏经营、门客养成与商战玩法',46,'商铺经营、门客系统')])
d=candidate('I006','Rockstar组建洛杉矶NPC制作团队',[77],3,2,1,'include','具体新增制作组织而非普通预告；密集开放世界内容生产有全球研发迁移点。',entities=['Rockstar Games','GTA 6'])
item(d,'Rockstar为《GTA 6》组建洛杉矶团队，逐个设计NPC',[
'Rockstar披露，已在洛杉矶组建由编剧、导演和制作人组成的团队，为《GTA 6》逐个设计更具真实感的NPC。团队不仅处理人物本身，也为房间陈设、照片与生活细节建立相互关联的叙事背景。'],[
('Rockstar披露，已在洛杉矶组建由编剧、导演和制作人组成的团队，为《GTA 6》逐个设计更具真实感的NPC',77,'Los Angeles-based team of writers, directors, and producers'),('房间陈设、照片与生活细节',77,'Every room in the game')])
d=candidate('I007','1047 Games结束两款射击游戏主动开发',[97],2,3,1,'include','PVP产品停止开发且运行模式改为P2P；不能仅按裁员计分。',entities=['1047 Games','Empulse','Splitgate Arena Reloaded'])
item(d,'1047 Games停止两款射击游戏开发，转向点对点托管',[
'1047 Games宣布结束《Empulse》和《Splitgate Arena Reloaded》的开发，两款游戏将改用点对点托管和服务器浏览器，保留玩家继续游玩的入口。工作室同时表示，在专注服务型射击游戏十年后将改变方向，尚未明确下一阶段项目。'],[
('1047 Games宣布结束《Empulse》和《Splitgate Arena Reloaded》的开发',97,'ending development on Splitgate Arena Reloaded and Empulse'),('点对点托管和服务器浏览器',97,'peer-to-peer hosting with a server browser'),('专注服务型射击游戏十年后将改变方向',97,'after ten years of focusing on live service shooters')])
d=candidate('I008','CAA推出Frame1Games独立游戏基金',[97],3,2,1,'include','新增融资与发行支持渠道，有跨市场独立游戏融资迁移点。',entities=['CAA','Frame1Games'])
item(d,'CAA推出Frame1Games，为独立游戏提供资金与市场支持',[
'CAA推出Frame1Games，计划为独立游戏提供资金、加速支持和营销服务，并通过精选市场展示入选作品。从2027年起，该计划还将支持团队参与行业活动，提供导师及合作伙伴资源。'],[
('CAA推出Frame1Games，计划为独立游戏提供资金、加速支持和营销服务',97,'CAA has launched Frame1Games'),('精选市场展示入选作品',97,'curated marketplace'),('从2027年起',97,'Starting in 2027')])
d=candidate('I009','《Corsair Cove》销量与用户地域披露',[79],2,3,1,'include','城市建造优先赛道的新品市场数据；2025年股权出售只作历史背景不报新交易。',entities=['Limbic Entertainment','Corsair Cove'])
item(d,'Limbic《Corsair Cove》发售不足一个月售出20万份',[
'Limbic Entertainment表示，海盗城市建造游戏《Corsair Cove》自7月31日发售后，不足一个月售出20万份，Steam仍有约70万愿望单。团队称产品在中国、日本和美国均获得玩家，发售质量与明确的海盗城建定位是其总结的主要原因。'],[
('Limbic Entertainment',79,'German developer Limbic Entertainment'),('《Corsair Cove》自7月31日发售后，不足一个月售出20万份，Steam仍有约70万愿望单',79,'Corsair Cove recently hit 200,000 sales'),('中国、日本和美国',79,'Japan and the United States'),('发售质量与明确的海盗城建定位',79,'absolutely polished at release')])
d=candidate('I010','《Manor Lords》累计销量突破400万',[179],2,3,1,'include','模拟经营优先赛道的累计销量里程碑；不将普通更新另报为事件。',entities=['Manor Lords'])
item(d,'《Manor Lords》累计销量突破400万份',[
'中世纪经营模拟游戏《Manor Lords》宣布，跨商店累计销量超过400万份。团队同时介绍后续更新中的酿酒、畜牧与河流地图内容，继续扩展聚落经营系统。'],[
('中世纪经营模拟游戏《Manor Lords》宣布，跨商店累计销量超过400万份',179,'over 4 million copies sold across all stores'),('酿酒、畜牧与河流地图',179,'use apples to make cider')])
d=candidate('I011','《Secret Neighbor》遭攻击后临时停服',[344],2,3,1,'include','多人对抗游戏安全事故导致停服，独立生命周期变化。',entities=['Hologryph','tinyBuild','Secret Neighbor'])
item(d,'《Secret Neighbor》后台遭入侵，团队临时关闭游戏并尝试恢复进度',[
'《Secret Neighbor》因攻击者获得后台管理权限并删除玩家档案、进度等数据而临时停服。开发商Hologryph与发行商tinyBuild表示，正与后端服务商PlayFab合作尝试恢复数据，并已向有关部门报案；恢复时间尚未确定。'],[
('《Secret Neighbor》因攻击者获得后台管理权限并删除玩家档案、进度等数据而临时停服',344,'obtained credentials with admin access'),('开发商Hologryph与发行商tinyBuild',344,'developer Hologryph and publisher tinyBuild'),('后端服务商PlayFab合作尝试恢复数据',344,'working with PlayFab'),('已向有关部门报案',344,'alerted the relevant authorities'),('恢复时间尚未确定',344,'no timeframe has been provided')])
d=candidate('I012','《PoE2》公布1.0及转免安排',[384],2,3,1,'include','明确商业模式与正式版档期，不将采访中每项版本改动拆条。',entities=['腾讯','Grinding Gear Games','Path of Exile 2'])
item(d,'《PoE2》1.0定于12月上线并转免，国服安排晚一周',[
'Grinding Gear Games公布，《Path of Exile 2》将于12月11日（太平洋时间）推出1.0正式版并转为免费游玩；腾讯发行的国服《流放之路：降临》定于12月18日同步完成1.0上线与转免。团队表示，正式版将补齐主线与终局内容，但不会一次交付原计划的全部12个职业。'],[
('Grinding Gear Games',384,'Grinding Gear Games'),('《Path of Exile 2》将于12月11日（太平洋时间）推出1.0正式版并转为免费游玩',384,'将于12月11日'),('腾讯发行的国服《流放之路：降临》定于12月18日',384,'腾讯发行的国服《流放之路：降临》将于12月18日'),('不会一次交付原计划的全部12个职业',384,'正式发布时不会有完整的12个职业')])
d=candidate('I013','Garena Free City新增地区下载记录',[388],2,3,1,'include','滚动目录中有明确前后状态：最初仅阿根廷，现新增菲律宾及其他市场下载；其他无增量目录项排除。',entities=['Garena','Garena Free City'])
item(d,'《Garena Free City》区域测试扩展，菲律宾出现下载记录',[
'据AppMagic数据的报道，Garena的开放城市游戏《Garena Free City》最初仅在阿根廷Android端软启动，目前已在菲律宾及部分其他市场出现下载记录。这表明其测试覆盖范围扩大，尚不等于全球正式发行。'],[
('据AppMagic数据的报道，Garena的开放城市游戏《Garena Free City》最初仅在阿根廷Android端软启动，目前已在菲律宾及部分其他市场出现下载记录',388,'It first soft-launched on Android in Argentina only')])
d=candidate('I014','Ratchet & Clank手游扩展至法国',[388],2,3,1,'include','开发者明确确认新增法国可玩状态，多人竞技赛道；未把整个滚动目录当本期首测。',entities=['Oh BiBi','Ratchet & Clank: Ranger Rumble'])
item(d,'《Ratchet & Clank: Ranger Rumble》在法国开放游玩',[
'开发商Oh BiBi确认，多人平台竞技射击手游《Ratchet & Clank: Ranger Rumble》已在法国开放游玩。报道同时指出，产品已在其他部分市场上线并开启预注册，仍处于分区域推广阶段。'],[
('开发商Oh BiBi确认，多人平台竞技射击手游《Ratchet & Clank: Ranger Rumble》已在法国开放游玩',388,'This multiplayer platformer arena shooter is now playable in France'),('其他部分市场上线并开启预注册',388,'pre-registration is now open')])
d=candidate('I015','《猪了个猪》迭代后经营指标披露',[336],2,3,1,'include','国内小游戏开发者披露产品改造与ROI数据，非纯榜单；不推广为全行业实验结论。',entities=['杭州同趣','猪了个猪'])
item(d,'杭州同趣称《猪了个猪》优化关卡与广告后，ROI由64%升至270%',[
'杭州同趣披露，《猪了个猪》在多轮调整难度、失败反馈与广告触发方式后，人均游玩时长由约1800秒增至3000秒，人均广告观看次数由5次增至12次，ROI由64%升至270%。团队称买量侧变化较少，主要调整发生在产品内部，并让激励广告围绕提示、奖励与跳关供玩家主动选择。'],[
('杭州同趣',336,'杭州同趣'),('《猪了个猪》',336,'《猪了个猪》'),('人均游玩时长由约1800秒增至3000秒，人均广告观看次数由5次增至12次，ROI由64%升至270%',336,'游戏人均时长从约1800秒提升到3000秒'),('买量侧变化较少，主要调整发生在产品内部',336,'买量侧几乎没动'),('激励广告围绕提示、奖励与跳关供玩家主动选择',336,'激励视频只在玩家需要提示、奖励或跳关时出现')])
d=candidate('I016','《巫师3》重制版进入Battle.net',[378],3,3,1,'include','平台与开发者新增具体发行合作，RPG优先赛道；与newsletter主分析为独立事件。',entities=['Blizzard','CD Projekt','The Witcher 3'])
item(d,'暴雪与CD Projekt合作，将《巫师3》重制版带到Battle.net',[
'暴雪宣布与CD Projekt合作，将《The Witcher 3: Wild Hunt — Remastered》带到Battle.net。通过该平台购买还可获得《Diablo IV》的杰洛特主题皮肤，合作把第三方RPG销售与平台内既有游戏奖励结合。'],[
('暴雪宣布与CD Projekt合作，将《The Witcher 3: Wild Hunt — Remastered》带到Battle.net',378,'Blizzard just announced a collab with CD Projekt'),('《Diablo IV》的杰洛特主题皮肤',378,'Geralt-themed skin in Diablo IV')])
d=candidate('I017','Discord与Battlefield 6推出Play Quest+',[378],2,3,1,'include','PVP产品获客工具的账户绑定与游戏内目标机制，具体平台能力变化。',entities=['Discord','Battlefield 6','EA'])
item(d,'Discord的《Battlefield 6》任务支持账户绑定与游戏进度同步',[
'Discord与《Battlefield 6》推出Play Quest+合作：玩家接受任务并绑定Discord和EA账户后，可通过完成游戏内目标解锁奖励，进度在游玩时自动同步至Discord。任务入口因此延伸到实际游玩行为，而非仅观看宣传内容。'],[
('Discord与《Battlefield 6》推出Play Quest+合作',378,'Play Quest+ with Battlefield 6'),('玩家接受任务并绑定Discord和EA账户后，可通过完成游戏内目标解锁奖励',378,'players who accept the Quest and link their Discord and EA accounts'),('进度在游玩时自动同步至Discord',378,'progress is automatically updated in Discord as users play')])

# Explicit history gates and independent, scored exclusions.
candidate('I101','郭炜炜离开西山居',[5,54,65],3,3,2,reason='历史卡片已曝光，离职报道与既定最后任职日没有新增状态。',entities=['郭炜炜','西山居'],hist=[134],event_date='2026-08-27')
candidate('I102','Thatgamecompany成立发行品牌',[35],3,2,1,reason='历史日报已曝光；周报未曝光不重置该事件状态。',entities=['Thatgamecompany'],hist=[80,113])
candidate('I103','《超自然行动组》1200万DAU',[37,208],2,3,2,reason='8月24日日报已经曝光，常规财报复述相同里程碑。',entities=['巨人网络','超自然行动组'],hist=[75,124])
candidate('I104','《破坏领主2》正式公布',[20],3,3,1,reason='上周卡片第8条已曝光；本期只有相同首曝简讯。',entities=['破坏领主2'],hist=[121])
candidate('I105','《王者万象棋》定档',[45,47,49,60,63,210,216,302],2,3,2,reason='上周行业正文未曝光，虽达8分但本期唯一补位竞争输给11分ACE；定档事实归产品日历。',entities=['腾讯','王者万象棋'],hist=[120],event_date='2026-08-27')
candidate('I106','《伊莫》双端档期',[99],2,3,1,reason='此前周报正文未曝光，7分低于ACE；没有新的档期状态。',entities=['伊莫'],hist=[116])
candidate('I107','《PUBG Mobile Light》公布',[99],3,3,1,reason='此前日报和周报均已曝光，账号与轻量包背景不构成新状态。',entities=['腾讯','PUBG Mobile Light'],hist=[15,53])
candidate('I108','暴雪Overwatch Rush早期测试',[388],3,3,0,reason='双周已曝光，同一万下载及菲律宾测试回顾。',entities=['Overwatch Rush'],hist=[14,48])
candidate('I109','《源初之结》测试体验与产品介绍',[52,340,414],0,3,1,reason='已知测试后的体验评述，不是新品首测或新档期。',entities=['米哈游','源初之结'])
candidate('I110','《无限大》全球公测定档',[39,50,99,198,213,329],2,3,2,reason='同一事件归产品日历，不跨栏重复。',entities=['网易','无限大'])
candidate('I111','《遗忘之海》封测定档',[50,99,213],2,3,2,reason='同一事件归产品日历，不跨栏重复。',entities=['网易','遗忘之海'])
candidate('I112','《凡应》二轮测试',[57,307],3,3,2,reason='同一测试事件归产品日历，不跨栏重复。',entities=['艺画开天','凡应'],event_date='2026-08-28')
candidate('I113','《Squadron 42》延期',[78,183],2,2,2,reason='E2×R2+M2=6；有发行注意力迁移点但未达7分。',entities=['Cloud Imperium Games','Squadron 42'])
candidate('I114','美国App Store消费下降',[100],2,2,1,reason='E2×R2+M1=5；全球移动支付有迁移点，但不是国内主体或中国手游市场；不因背景提及Roblox抬分。',entities=['Apple','Sensor Tower'])
candidate('I115','育碧巴塞罗那移动工作室罢工',[95],1,2,1,reason='纯劳资罢工E1；重组和腾讯投资为旧背景。',entities=['Ubisoft Mobile Barcelona'])
candidate('I116','《剑网3》50级和2.0长期改造计划',[308,379,381,387],1,3,2,reason='老产品重大生命周期规划E1，不是独立新品立项；5分未达线。',entities=['剑网3'],event_date='2026-08-28')
candidate('I117','钛核招聘并扩充《动物朋克》团队',[304,382],1,3,2,reason='明确项目扩编方向但无核心管理层更换、新融资或新立项，属于实质表态E1，共5分。',entities=['钛核网络','动物朋克'])
candidate('I118','Hinterland推迟Blackfrost并将部分人员转回前作',[413],2,2,1,reason='项目延期和自筹发行结构有迁移点，5分未达线。',entities=['Hinterland','Blackfrost'])
candidate('I119','Xbox实体光盘转数字功能测试',[19,378],2,2,2,reason='跨设备授权机制有迁移点，6分未达线；8月31日测试不是本期已经发生。',entities=['Xbox'])
candidate('I120','EA退出Circana数字销售数据',[378],2,2,1,reason='市场数据可见性变化5分未达线。',entities=['EA','Circana'])
candidate('I121','腾讯育碧以外的一般硬件关税退款',[74,97],2,0,2,reason='海外硬件区域事件，无游戏业务迁移点。',entities=['Panic','Playdate'])
candidate('I122','《渔力全开》首发销量回顾',[334],2,2,0,reason='正文指标止于8月20日发售后第4天，未有本窗口新增销量事实；不将晚到复盘伪装为新纪录。',entities=['Dazed Games','How to Fish'])
candidate('I123','《Mystery Dumpling》下载数据',[407],2,2,0,reason='数据截止8月25日；手游题材获量有迁移点但旧数据4分。',entities=['Mystery Dumpling'])
candidate('I124','《暴走植物园》上线及早期排名回顾',[410],2,3,0,reason='8月4日上线后的排名回顾，无本窗口新增状态，6分不入选。',entities=['海南椰路','暴走植物园'])
candidate('I125','恺英网络常规半年报',[38],2,3,1,reason='常规同比增长，不符合异常财务例外；2月诉讼和解为历史事件。',entities=['恺英网络'])
candidate('I126','游族网络半年报投资收益',[51,73,386],2,3,2,reason='净利润主要由金融资产公允价值带动，属一次性投资收益；不满足非一次性经营异常门槛。AI生产工具独立转AI栏。',entities=['游族网络'])
candidate('I127','巨人网络常规半年报',[37,208],2,3,2,reason='常规同比增长与分红，不因增长幅度直接触发财报例外；独立Garena合作与AI落地分别处理。',entities=['巨人网络'])
candidate('I128','三七互娱常规半年报',[217],2,3,1,reason='常规业绩和储备复述；不符合财报异常例外。',entities=['三七互娱'])
candidate('I129','鹰角新办公楼及租房补贴',[44],0,3,1,reason='泛办公与员工福利，非核心组织或管理层事件。',entities=['鹰角网络'])
candidate('I130','动视向外挂商送达停止侵权函',[420],1,3,1,reason='PVP反作弊执行行动为运营/法律措施，E1总4分；不按新平台规则或资本事件抬分。',entities=['Activision','Call of Duty'])
candidate('I131','《巫师4》在目标平台运行',[93],1,3,1,reason='在研项目技术进度表态4分；并非新档期或首曝。',entities=['CD Projekt Red','The Witcher 4'],hist=[69,117],novelty='material_update',new_facts=['S0093：项目已在全部目标平台运行；当前事件为技术进度，仍未达分数线。'])
candidate('I132','谷歌英国开发者集体诉讼和解',[92],3,2,1,reason='潜在资本/平台事件达7分，但只有snippet，无完整正文，不能作为可核验完整事件入选。',entities=['Google'])
candidate('I133','PeopleFun及Lion Studios CEO变化',[86],3,2,1,reason='组织事件潜在7分但仅snippet，缺完整原文。',entities=['PeopleFun','Lion Studios'])
candidate('I134','Roblox菲律宾儿童安全合作',[87],2,3,1,reason='Roblox固定R3，7分但只有snippet，不据摘要完成正文。',entities=['Roblox','Meta'])
candidate('I135','CookieRun Crumble收入',[81],2,3,1,reason='RPG产品数据潜在7分，但只有snippet。',entities=['CookieRun: Crumble'])
candidate('I136','《Hieronymus》首曝',[422],3,1,1,reason='海外一般单人FPS首曝R1，4分；不是PVP竞技。',entities=['Hurdy-Gurdy Games','Hieronymus'])
candidate('I137','《腐烂国度3》封测计划',[140],2,2,1,reason='合作生存产品档期5分，全球同类产品测试有弱迁移；未命中PVP。',entities=['腐烂国度3'])
candidate('I138','《No More Room in Hell 2》玩家破百万',[97],2,2,1,reason='合作生存市场数据5分；非PVP及重点策略/RPG。',entities=['No More Room in Hell 2'])

# AI direct applications take precedence over transferable general technology news.
d=candidate('A001','腾讯展示GIGA游戏智能体落地',[62,66],section='ai_trends',decision='include',reason='行业候选反扫：独立GIGA智能体应用，正文避开上周已报Motus动画管线。',entities=['腾讯','GIGA'],ai_tier='direct_application',game_stage=['product'],industry_reverse_scan=True)
item(d,'腾讯披露GIGA智能体已用于《和平精英》和《终极角逐》',[
'腾讯在科隆展披露，GIGA通用游戏智能体已陆续用于《和平精英》《终极角逐》等项目。团队将大模型的战术规划与意图理解，同强化学习模型的实时执行结合，探索通过视觉感知和自然语言指令实现战场协作。相关披露属于具体产品应用与持续研发，并未宣称已经解决所有游戏的通用智能问题。'],[
('腾讯',62,'腾讯游戏公共技术线'),('GIGA通用游戏智能体已陆续用于《和平精英》《终极角逐》等项目',62,'GIGA团队的这项能力已经陆续在《和平精英》《终极角逐'),('大模型的战术规划与意图理解，同强化学习模型的实时执行结合',66,'上层用大模型做战术规划和意图识别'),('视觉感知和自然语言指令',66,'纯靠视觉理解画面')])
d=candidate('A002','巨人网络披露游戏研发AI使用比例',[37],section='ai_trends',decision='include',reason='直接作用于代码与策划配置，比例为公司披露，不等同提效幅度。',entities=['巨人网络','超自然行动组'],ai_tier='direct_application',game_stage=['development'],industry_reverse_scan=True)
item(d,'巨人网络称《超自然行动组》代码研发AI生成占比超过80%',[
'巨人网络披露，AI已进入《超自然行动组》的研发流程：代码研发环节AI生成占比超过80%，策划配置环节AI参与率超过60%。公司同时启动智能化集成运营保障平台一期建设，持续完善20余个数字专家；这些使用比例不能直接等同于同等幅度的人力节省或成本下降。'],[
('巨人网络',37,'巨人网络'),('《超自然行动组》',37,'以《超自然行动组》为例'),('代码研发环节AI生成占比超过80%，策划配置环节AI参与率超过60%',37,'代码研发环节AI生成占比超过80%'),('智能化集成运营保障平台一期建设，持续完善20余个数字专家',37,'公司启动建设智能化集成运营保障平台')])
d=candidate('A003','游族部署AI广告与游戏创作平台',[51,386],section='ai_trends',decision='include',reason='已在内部推出具体研发与营销工具；非泛AI投资概念。',entities=['游族网络'],ai_tier='direct_application',game_stage=['development','publishing'],industry_reverse_scan=True)
item(d,'游族推出内部AI创作工具，覆盖广告素材与自然语言游戏制作',[
'游族网络披露，内部已推出AI广告素材创作平台，串联创意构思与视频生成；YOOSpark支持以自然语言对话进行游戏创作，YOOLab则提供图文与视频的可视化创作流程。公司同时推行面向员工的“Token无限额”保障机制，以降低工具使用门槛，尚未披露这些平台各自带来的量化经营收益。'],[
('游族网络',51,'游族网络'),('内部已推出AI广告素材创作平台，串联创意构思与视频生成',51,'AI广告素材创作平台打通从创意构思到视频生成'),('YOOSpark支持以自然语言对话进行游戏创作，YOOLab则提供图文与视频的可视化创作流程',51,'游戏创作平台YOOSpark'),('“Token无限额”保障机制',51,'“Token无限额”保障机制')])

# Community decisions include the follow-up scan and claim boundaries.
comm1=dict(trigger='玩家质疑P3联动赠抽发放方式',claim_scope='社区对公告和直播的解读，彼此存在分歧，不当作官方规则定论',complaint_logic='补偿领取与持续登录及卡池时点绑定',timeline=['2026-08-29：PV后玩家讨论补偿时间','2026-08-30：回复区出现第十天发十连券的反驳与对分批领取的持续不满'],follow_up_scan='扫描本期54条社区记录及行业全文：合并S0369/S0505；没有同事件官方原文，8月30日修正意见必须进入正文。')
d=candidate('C001','《明日方舟》P3赠抽发放争议',[369,505],section='community_discourse',decision='include',reason='新命名社区事件；后续修正直接改变叙述，不能照抄首帖。',entities=['明日方舟'],community=comm1)
item(d,'《明日方舟》P3联动赠抽引发争论，玩家质疑补偿与分日登录绑定',[
'《明日方舟》P3联动赠抽安排在8月29日预告公开后引起讨论：部分玩家将额外赠抽理解为活动开始后逐日领取，认为补偿应让玩家在卡池开启时即可使用，不应继续绑定登录节奏。8月30日，回复中出现不同解释，称额外十连会在第十天以十连券发放，不能与日常单抽混为一谈；也有玩家认为直播已写明活动期间发放，对时间安排并不意外。争议由“到底怎样发”进一步转向“补偿是否应承担维持日活和促销的功能”。'],[
('8月29日预告公开',369,'今天P3联动的PV、预告动态发了'),('部分玩家将额外赠抽理解为活动开始后逐日领取',369,'活动开始后再慢慢发'),('8月30日',505,'2026-08-30'),('额外十连会在第十天以十连券发放，不能与日常单抽混为一谈',505,'多送的那一次十连是直接在第十天发到你邮箱那个十连券'),('也有玩家认为直播已写明活动期间发放',505,'直播截图上也写得明明白白是“活动期间发放”'),('维持日活和促销',369,'把补偿当作促销和保日活的手段')],community=comm1)
comm2=dict(trigger='鸣潮周边瑕疵后的登记补偿方案',claim_scope='玩家对已见方案及未收到补偿实物的争论；不认定补偿没有发出',complaint_logic='色纸能否补偿立牌瑕疵，登记确认的含义，以及角色单人图预期',timeline=['8月25日起色纸/尺寸争议','8月30日新增补货登记和补偿对象争论'],follow_up_scan='按鸣潮/陆赫斯/爱弥斯/色纸/尺寸补扫全窗口社区，合并S0270/S0272/S0362/S0501/S0502/S0513/S0516；仅使用截至8月30日回复，不引用S0516的8月31日回复。')
d=candidate('C002','《鸣潮》周边补偿登记引发二次争论',[270,272,362,501,502,513,516],section='community_discourse',decision='include',reason='上周报道原始瑕疵，本期8月30日新增补货登记与补偿内容争论；有可区分的新阶段。',entities=['鸣潮','库洛'],community=comm2)
item(d,'《鸣潮》周边争议进入补偿阶段，玩家分歧转向补货登记与补偿内容',[
'《鸣潮》角色礼盒的材质、尺寸争议延续到补偿安排：8月30日，玩家称补货登记需要确认接受处理方案，并质疑色纸补偿能否回应立牌本身的瑕疵。另有购买者表示已登记；对补偿是否为角色单人图的猜测，则遭到其他玩家反驳，认为不能在实物尚未到手时就断言没有补偿。讨论因此从商品是否有问题，转向修正原商品、额外赠品与消费者确认之间的关系。'],[
('《鸣潮》角色礼盒的材质、尺寸争议',270,'[鸣潮]'),('8月30日',516,'2026-08-30'),('补货登记需要确认接受处理方案',516,'补货登记还要你确认同意这次处理'),('色纸补偿能否回应立牌本身的瑕疵',516,'发个色纸补偿立牌'),('购买者表示已登记',513,'我有买 我也登记了'),('对补偿是否为角色单人图的猜测',513,'是不是多人图未知'),('不能在实物尚未到手时就断言没有补偿',513,'没给才是瓜')],community=comm2)

# The single high-quality newsletter supports a bounded analysis; chart-only values are omitted.
d=candidate('D001','短流程增量游戏的成长反馈与品类预期',[378],section='deep_analysis',decision='include',reason='高质量newsletter单篇分析，R/I/E/C=3/3/3/3；不重复上期广义Steam新品品类统计。',entities=['GameDiscoverCo','Hearth & Hamlet'],scores=dict(relevance=3,insight=3,evidence=3,card=3,total=12))
item(d,'短流程增量游戏卖的是持续成长，城建外观却可能带来错误预期',[
'观察：GameDiscoverCo对《Hearth & Hamlet》的分析显示，一类低价、流程有限的增量游戏正在用高密度成长反馈吸引玩家。该作售价8美元，完整体验约8至12小时，早期中位游玩时长达到7小时20分钟；但其城市布局预先设定，并非自由建造。问题因此不只是玩家愿不愿意购买短游戏，也在于商店外观会让玩家预期怎样的玩法。',
'分析：这类产品把复杂品类压缩为易理解、持续获得资源与升级的循环。玩家可以主动推进成长，同时避免长篇教程和过高学习负担；有限流程又让一次购买对应较清晰的完成目标。对时间和精力有限的用户而言，吸引力可能来自“低负担地持续变强”，而不是无限挂机或无限内容。该解释来自作者对品类的归纳，不代表所有增量游戏都会获得相同留存。',
'成立前提是展示与实际交互一致。《Hearth & Hamlet》的城建外观吸引了部分期待自由规划的玩家，而开发者明确表示布局是预设的，体验更接近拼装既定微缩景观。发行方认为，一部分负面评价正来自想要更强城建体验的非放置玩家。这意味着，降低学习门槛可以扩大点击与购买，却也可能扩大错误受众；当视觉承诺超过机制提供的选择空间时，转化优势会变成口碑压力。'],[
('GameDiscoverCo',378,'GameDiscoverCo'),('《Hearth & Hamlet》',378,'Hearth & Hamlet'),('售价8美元',378,'Hearth & Hamlet ($8)'),('完整体验约8至12小时',378,'8-12 hours to complete in total'),('中位游玩时长达到7小时20分钟',378,'Median playtime of 7 hours 20 minutes'),('城市布局预先设定',378,'The city layout is completely predetermined'),('主动推进成长',378,'players are actually playing the game'),('避免长篇教程和过高学习负担',378,'Want to play! Don’t want to learn!'),('一部分负面评价正来自想要更强城建体验的非放置玩家',378,'a substantial portion of our negative reviews are specifically non-idle players')],
card_copy=dict(source_label='GameDiscoverCo分析文章',summary='短流程增量游戏以低学习负担和持续成长获得吸引力，但城建式视觉若制造自由建造预期，会把获客优势转化为口碑压力。',insights=[dict(title='成长反馈压缩体验',detail='持续积累与升级把复杂品类提炼为易理解的短流程，不需要无限内容。'),dict(title='主动游玩减少学习负担',detail='玩家仍在推动进展，但不必先掌握完整城建系统。'),dict(title='展示决定受众预期',detail='预设布局与自由建造的差别，会影响被城建外观吸引的用户是否满意。')]))

# Full-source coverage: every record is inspected as text, not only as an index row.
# This scan retains all event-bearing sentences and source hashes for reproducibility.
scan=[]
rx=re.compile(r'首曝|首次|立项|融资|收购|停运|关闭|裁员|离职|CEO|突破|超过|流水|营收|政策|延期|定档|公测|首测|测试|上线|发布|取消|合作|AI|Roblox|Supercell|Riot|Garena|Savvy|launch|million|billion|announce|delay|shut|fund|acquir|releas|invest|revenue|studio',re.I)
for r in rows:
    lines=[x.strip() for x in re.split(r'(?<=[。！？])|\n+',r['text']) if x.strip()]
    scan.append(dict(source_id=r['source_id'],section=r['section'],title=r['title'],text_sha256=hashlib.sha256(r['text'].encode()).hexdigest(),text_chars=len(r['text']),event_sentences=[x for x in lines if rx.search(x)]))
dump('full_source_scan.json',scan)

# Additional explicit original-industry signals; routine previews and non-events remain E0.
spec={2:(2,1,1,'既有产品跨平台商店页面'),3:(3,1,1,'海外动作冒险发售'),7:(2,3,1,'经营新品定档'),9:(2,3,1,'国产推理产品跨平台'),10:(3,1,1,'海外温馨探索新品'),11:(2,3,1,'国产肉鸽全平台档期'),13:(3,1,1,'心理恐怖试玩'),15:(3,3,1,'增量放置新品Demo'),16:(2,1,1,'合作冒险新品档期'),18:(2,3,1,'竞技格斗跨平台计划'),21:(3,1,1,'合作高尔夫平台新品首曝'),23:(3,1,1,'银河城续作首曝'),24:(3,1,1,'警察模拟新品首曝'),28:(3,3,1,'肉鸽构筑新品发售'),29:(2,3,1,'生活经营新品定档'),31:(2,1,1,'海外恐怖新品档期'),56:(3,3,1,'国产剧情探索短篇发布'),69:(3,2,1,'既有合作射击新作展会试玩，不是首曝'),76:(2,2,1,'GTA预告对Netflix流量影响'),85:(1,0,1,'迪拜地方产业展馆宣传'),96:(1,3,1,'Warlock魔法机制采访'),108:(1,3,1,'国产在研产品体验采访'),138:(1,3,1,'老RPG重大更新'),154:(2,1,1,'Blackwood新品档期'),160:(2,3,1,'怪物收集RPG新品档期'),162:(2,1,1,'动作冒险新品档期'),163:(2,3,1,'肉鸽新品档期'),177:(1,3,1,'ARC Raiders未来相机模式'),199:(2,3,1,'神鬼寓言延期回顾'),211:(0,3,1,'UGC榜单及7月旧测试回顾'),324:(2,3,1,'神鬼寓言延期采访'),328:(1,0,1,'Xbox硬件家族表态'),332:(1,1,1,'日本创作者学院参展'),345:(1,2,1,'EA回应已知钢铁侠项目素材泄露'),406:(2,3,0,'海外小语种市场历史案例综述'),421:(2,2,1,'Valve历史开发资料泄露')}
for n,(e,r,m,reason) in spec.items():
    sid=f'S{n:04d}'
    if sid in used:continue
    # Short captions contain no body to substantiate a full publishable event.
    quality=len(S[sid]['text'])<300 or S[sid]['body_status']!='full'
    if e*r+m>=7 and not quality and n not in [69,199,324]:
        # Full standalone new events below are authored after source verification.
        pass
    candidate(f'J{n:04d}',S[sid]['title'],[n],e,r,m,reason=reason+('；仅简讯/短摘录，正文不足以完成产品状态取证。' if quality else '；本期为体验/回顾，未证实新状态，不将文章发布时间当新事件发生日。'))

# Snapshot test-directory entries have no current-window start date unless an explicit change was selected above.
soft=[('Century Games','Frozen Manor: Merge Mystery',3,3),('Fingersoft','Hill Climb Racing 3',3,2),('EA','Plants vs. Zombies 3: Evolved',1,3),('King','Minecraft Blast',2,2),('腾讯','Crownstone Survival',3,3),('Limit Break','Puzzle Panic',3,2),('Miniclip','Hoverboard Party',3,3),('Miniclip','Pure Crime: Gangster Shooting',3,2),('Miniclip','Paint Brawl',1,3),('Miniclip','Rival Nations',3,3),('Moon Active','Royal Splash: Tower Blast',3,2),('Playrix','Aqua Match',3,2),('Playrix','Austin’s Odyssey',3,3),('Playrix','Match Around',3,2),('Playrix','Questbound',3,3),('Playrix','Roomscapes',3,3),('Scopely','WWE Generations: Eras Collide',3,3),('Rovio','Angry Birds Match World',3,2),('Rovio','Angry Birds Rush',3,2),('Rovio','Bloom City Match',3,3),('Supercell','Project Rise',3,3),('NaturalMotion','Borderlands Mobile',2,3),('NaturalMotion','CSR 3',3,2),('Small Giant','Defend the Castle',3,3),('Zynga','Dice Companions',3,3),('Rollic','Farm Rush Fever',2,2),('Nordeus','Top Goal: Soccer Champion',3,3)]
for j,(co,prod,e,r) in enumerate(soft,1):
    candidate(f'T{j:03d}',prod+'滚动测试目录状态',[388],e,r,0,reason='两周更新的存量测试目录，未给出8月28日至30日新发生时间；保留候选但不把现存下载或早期测试自动写成本期首测。'+('Project Rise测试明确8月19日开始。' if co=='Supercell' else ''),entities=[co,prod])

for r in rows:
    sid=r['source_id'];n=int(sid[1:])
    if sid in used or r['section']=='release_calendar': continue
    if r['section']=='ai_trends' or n in [83,84,104,126,131,191,196,325,335,343,377,408,417,517]:
        tier='direct_application' if r['section']!='ai_trends' else 'transferable_frontier'
        candidate('X'+sid,r['title'],[n],section='ai_trends',reason='已反扫；直接应用优先，当前事件为旧披露/争论、观点或证据较弱；通用工具与科技新闻低于三条已入选游戏应用。',ai_tier=tier,game_stage=['development'],industry_reverse_scan=r['section']=='industry_news',migration_path='如用于游戏代码、美术或交互需继续核查实际适用性；本期不采用。')
    elif r['section']=='community_discourse':
        candidate('X'+sid,r['title'],[n],section='community_discourse',reason='补扫留痕：旧讨论、主体推测或证据不完整；在两个更完整的新阶段事件之外排除，不作全体玩家共识。',community=dict(trigger=r['title'],claim_scope='帖内意见',complaint_logic='未完整验证',timeline=[r['date']],follow_up_scan='已按同产品与争议词对本窗口全池补扫，未形成优先于两条入选项的完整事件。'))
    elif r['section']=='deep_analysis':
        candidate('X'+sid,r['title'],[n],section='deep_analysis',reason='创作者生涯采访，独立项目方法论有价值，但本期优先具体产品机制与玩家预期分析。',scores=dict(relevance=2,insight=2,evidence=3,card=2,total=9))
    else:
        candidate('X'+sid,r['title'],[n],0,0,0,reason='完整输入反扫：常规预告、演示、体验、攻略、联动、奖项宣传、泛职场、非游戏或纯榜单；没有可独立采用的本窗口状态变化。')

# A short but complete caption can support a short news item; do not exclude solely on length.
for cid,e,r,m,why in [('J0007',2,1,1,'只提供标题与日期，原文未说明优先赛道；不凭游戏名补玩法。'),('J0011',2,2,1,'肉鸽跨平台有迁移点，原文不写国内主体或RPG，5分。'),('J0056',3,1,1,'原文未写国内研发主体；海外剧情探索一般品类，4分。'),('J0163',2,1,1,'单人第三人称射击，不能以肉鸽标签当PVP/RPG；3分。'),('J0069',0,2,1,'已知项目展会试玩，不是首次立项或新测试。'),('J0199',1,3,1,'已知延期后的解释，实质表态4分。')]:
    d=next(x for x in D if x['candidate_id']==cid);d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m);d['reason']=why
short_items=[
('J0009','《山河旅探》登陆主机平台','国产本格推理游戏《山河旅探》已登陆主机平台。',9,'国产本格推理游戏《山河旅探》现已登陆主机平台'),
('J0015','增量放置游戏《米粒新世界》开放Demo','增量放置游戏《米粒新世界》已开放Demo，展示围绕一棵树生长的小社会。',15,'增量放置游戏《米粒新世界》Demo现已开放'),
('J0018','《碧蓝幻想Versus -RISING》Switch 2版定于9月17日发售','《碧蓝幻想Versus -RISING》的Switch 2版定于9月17日发售。',18,'NS2版将于9月17日发售'),
('J0028','轮盘赌构筑肉鸽《雪夜枪声》发售','轮盘赌构筑肉鸽游戏《雪夜枪声》已发售。',28,'轮盘赌构筑肉鸽游戏《雪夜枪声》现已发售'),
('J0160','怪物收集RPG《磁带妖怪2002》定档2027年3月','怪物收集RPG《磁带妖怪2002》计划于2027年3月登陆PS5、Xbox Series、Switch 2与PC。游戏支持单人和线上模式，玩家将前往2002年的伦敦，通过录制、战斗与融合应对超过250种怪物。',160,'在《磁带妖怪2002（Cassette Beasts 2002）》这款怪物收集RPG中')]
for cid,title,body,n,needle in short_items:
    d=next(x for x in D if x['candidate_id']==cid);d['decision']='include';d['reason']='短正文直接支持事件状态，达到7分；不因篇幅短而遗漏，不补无证据厂商和日期。'
    if n==15:d['scores']=dict(event=3,relevance=2,hook=1,total=7);d['reason']+='增量游戏有小团队与玩法压缩迁移点，R2。'
    item(d,title,[body],[(body,n,needle)])
# Final editorial review uses direct text support; it does not relax validators.
dm={d['candidate_id']:d for d in D}
for cid in ['I013','I014']:
    dm[cid]['decision']='exclude'
    dm[cid]['reason']='滚动两周测试目录有前后状态，但没有本期新增地区的明确日期；状态变化无法定位在8月28日至30日，不能把目录更新日当事件日。评分保留7分，因时间证据不足排除。'
dm['A002']['decision']='exclude';dm['A002']['reason']='巨人同份披露已采用Garena发行合作；AI栏目优先采用另外两家公司可独立呈现的具体工具应用，避免同一披露跨栏重复。'
ITEMS=[it for it in ITEMS if dm[it['candidate_id']]['decision']=='include']
for cid,n in [('I007',79),('I016',289)]:
    dm[cid]['source_ids'].append(f'S{n:04d}')
    dm[cid]['cluster_basis']=dict(subject=dm[cid]['entities'][0],product=dm[cid]['title'],event_date=dm[cid]['event_date'],event=dm[cid]['event'])
for it in ITEMS:
    if it['candidate_id']=='C002':it['body']=it['body'].replace('并质疑色纸补偿能否回应立牌本身的瑕疵','玩家不满的核心在于，色纸补偿能否回应立牌本身的瑕疵')
    if it['candidate_id']=='I007':it['claims'].append(dict(claim='1047 Games宣布结束',source_id='S0079',evidence=evidence('S0079','1047 Games ends active development')))
    if it['candidate_id']=='I016':it['claims'].append(dict(claim='Battle.net',source_id='S0289',evidence=evidence('S0289','CD Projekt will release a remastered version')))
d=candidate('A004','腾讯展示面向游戏的Vox语音引擎',[62],section='ai_trends',decision='include',reason='具体游戏TTS引擎技术展示，与GIGA决策智能体为不同产品；只写披露性能，不推断已规模化部署。',entities=['腾讯','Tencent Games Vox'],ai_tier='direct_application',game_stage=['development','product'],industry_reverse_scan=True)
item(d,'腾讯展示Vox游戏语音引擎，披露140毫秒首包延迟',[
'腾讯展示面向游戏场景的原生TTS引擎Tencent Games Vox，可生成具有角色特征和情绪表现力的44kHz语音。团队披露其流式合成首包延迟低至140毫秒，生成10秒语音约需0.8秒，并将智能NPC、AI教练与实时解说列为适用方向；这些数据属于技术展示，未给出各项目的部署规模。'],[
('面向游戏场景的原生TTS引擎Tencent Games Vox',62,'Tencent Games Vox 是腾讯游戏面向游戏场景打造的原生TTS引擎'),('44kHz语音',62,'44kHz原生音质'),('首包延迟低至140毫秒',62,'首包延迟低至140毫秒'),('生成10秒语音约需0.8秒',62,'生成10秒语音仅需0.8秒'),('智能NPC、AI教练与实时解说',62,'智能NPC、AI教练、数字人和实时解说')])
d=candidate('I018','Raccoon Logic公布4对4冰球新作',[289],3,3,1,'include','本期原始采访明确刚公布的新游戏，4对4竞技为PVP优先赛道；不是综合稿尾部旧消息汇总。',entities=['Raccoon Logic','Breakaway Hockey League'])
item(d,'Raccoon Logic公布4对4冰球新作，计划通过抢先体验迭代',[
'Raccoon Logic公布快节奏4对4冰球游戏《Breakaway Hockey League》，计划采用抢先体验模式。团队表示，希望缩短传统三四年的封闭开发周期，更早与玩家共同迭代；这一选择也与其前作虽通过订阅获得大量玩家、附加内容购买却未同步增长的经验有关。'],[
('Raccoon Logic',289,'Canadian game developer Raccoon Logic'),('快节奏4对4冰球游戏《Breakaway Hockey League》，计划采用抢先体验模式',289,'That new game is Breakaway Hockey League'),('缩短传统三四年的封闭开发周期',289,'Instead of spending three or four years'),('附加内容购买却未同步增长',289,'many of them didn’t go on to buy any of the add-on content')])
roundup=[('Worms: Galactic Tactics首曝',3,3,1,[]),('Focus接手Maverick Clutch发行',3,2,1,[]),('Exodus未来定档',2,3,1,[]),('Sega关闭Rovio Copenhagen',2,2,1,[]),('Ubisoft Player Council反馈平台',2,2,1,[]),('Stage Tour未来档期',2,1,1,[]),('Makers Fund融资',3,2,1,[38]),('Rainbow Six Tactics公布',3,3,1,[129]),('2XKO停止开发',2,3,1,[65,110]),('thatgamepublisher',3,2,1,[80,113]),('007 First Light销量',2,1,1,[])]
for j,(title,e,r,m,hn) in enumerate(roundup,1):
    if j==10:
        prior=next(x for x in D if x['candidate_id']=='I102');prior['source_ids'].append('S0289')
        prior['cluster_basis']=dict(subject='Thatgamecompany',product='Thatgamepublisher',event_date=prior['event_date'],event=prior['event'])
        continue
    candidate('N'+str(j).zfill(3),title,[289],e,r,m,reason=('历史同事件，已曝光者排除；未曝光者按本期总分排序低于ACE11分，未获唯一补位。' if hn else '深度newsletter末尾科隆消息汇总未给出独立消息日期，无法确认属于本期；保留事实候选及原始分数，不把周末采集日当首次公告日。'),hist=hn)
dump('report_items.json',dict(schema_version=1,items=ITEMS))
dump('selection_decisions.json',dict(decisions=D))
print('authored',len(ITEMS),'items;',len(D),'decisions')
