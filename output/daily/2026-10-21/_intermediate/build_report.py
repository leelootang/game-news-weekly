import json,re,hashlib,sys,shutil
from pathlib import Path
from collections import Counter

P=Path(__file__).resolve().parent
ROOT=P.parents[3]
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
H=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))['occurrences']
def sid(i):return f'S{i:04d}' if isinstance(i,int) else i
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def proof(i,needle):
    t=S[sid(i)]['text'];assert needle in t,(i,needle)
    return next(l for l in t.splitlines() if needle in l)
def ev(i,n):return dict(source_id=sid(i),evidence=proof(i,n))

# Every record is parsed in full; retain dates and substantive paragraphs as a
# navigable review, including long multilingual mirrors that cannot be treated
# as independent sources merely because their URLs differ.
review=[]
for x in S.values():
    lines=x['text'].splitlines()
    review.append(dict(source_id=x['source_id'],title=x['title'],section=x['section'],url=x['url'],
      sha256=hashlib.sha256(x['text'].encode()).hexdigest(),text_chars=len(x['text']),paragraph_count=len(lines),
      body_status=x['body_status'],date_evidence=[l for l in lines if re.search(r'202[456]|\d{1,2}月\d{1,2}|October|November|2025年',l)],
      signal_evidence=[l for l in lines if re.search(r'首曝|首测|融资|收购|投资|停运|关闭|政策|公测|测试|上线|AI|reveal|launch|acqui|fund|bankrupt|2025|2026',l,re.I)]))
save('full_input_review.json',review)

D=[];DM={}
def base(cid,section,ids,event=None,decision='exclude',reason=''):
    ids=[sid(v) for v in ids]
    d=dict(candidate_id=cid,section=section,source_ids=ids,entities=[S[ids[0]]['title']],event=event or S[ids[0]]['title'],event_date='2026-10-21',decision=decision,reason=reason)
    D.append(d);DM[cid]=d;return d
def industry(i,e=0,r=0,m=0,reason='',subject=None,kind=None,focus=None,subject_quote=None,genre=None,genre_quote=None,ids=None):
    ids=ids or [i];d=base(f'I{i:03}', 'industry_news',ids,reason=reason or 'E0：普通活动/版本/宣传、非游戏或缺少独立实质事件。')
    d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m)
    d['history_check']=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None)
    if e:
        d['subject_assessment']=dict(subject=subject or S[sid(i)]['title'],kind=kind or 'other_or_unknown',focus_companies=focus or [],basis='当前候选来源未证明名单主体、投资/合研/核心人才关系或有声量代表作，不以国产、平台与品类标签抬高R。' if r==0 else reason,evidence=[ev(i,subject_quote)] if subject_quote else [])
        d['genre_assessment']=dict(matched_genres=[genre] if genre else [],basis='事件本身有明确指定品类证据。' if m else '没有明确命中指定细分类别；一般动作、RPG、合作、经营或公司资本事件不加分。',evidence=[ev(i,genre_quote)] if genre_quote else [])
    if len(ids)>1:d['cluster_basis']=dict(subject=subject or d['event'],product=subject or d['event'],event_date='2026-10-21',event=d['event'])
    text='\n'.join(S[sid(v)]['text'] for v in ids)
    if re.search(r'Steam|PS5|Xbox|PC|主机',text,re.I) and re.search(r'发售|试玩|测试|Demo|launch|release|reveal',S[sid(i)]['title'],re.I):
        d['pc_release_scope']=dict(classification='domestic_or_focus' if r==3 else 'multiplayer_or_other' if re.search('合作|多人',text) else 'unknown',basis='平台与产品范围独立记录；R仅按主体，不靠国产或PC/主机标签赋分。',evidence=[dict(source_id=sid(i),evidence=S[sid(i)]['text'].splitlines()[0])])
    return d

# Explicit editorial event judgments. Unspecified routine signals retain E0.
events={
 1:(3,0,0,'新品发售信号，但正文仅32字、无已取证重点主体或代表作，R0。'),
 2:(3,0,0,'Demo信号，不能以国产标签证明主体；无主体证据R0。'),
 3:(0,0,0,'两款产品新品节参展宣传，不能证明首次测试。'),
 4:(3,0,0,'试玩实际日期为10月20日；主体证据不足，不能作为本期首测。'),
 7:(2,0,0,'新品定档，主体未证实；日历独立召回。'),
 8:(3,0,0,'试玩节点，来源未证明研运主体层级。'),
 9:(3,0,0,'Demo开放但主体无法确认。'),10:(2,0,0,'定档是日历信号，主体未证实。'),
 13:(0,0,0,'10月20日既有新品节参展，不证明21日首次测试。'),
 14:(3,0,0,'试玩节点，无主体重要性证据。'),16:(3,0,0,'生活向联机试玩信号；网飞不在统一游戏名单，来源未证明代表产品声量，R0。'),
 17:(3,0,0,'Demo节点，无重点主体或代表作声量证据。'),18:(3,0,0,'合作RPG不等于竞技；无研运主体取证，R0、M0。'),
 22:(3,0,0,'新品试玩但来源极短、主体未证实。'),26:(0,0,0,'反作弊普通工具调整；社区反应另建事件。'),
 27:(2,0,0,'定档10月22日，日历独立召回，主体不明。'),30:(2,0,0,'定档12月4日，行业主体不明。'),
 31:(3,0,0,'测试开启，但正文来源49明确为10月14日开始且已有单人测试，不是21日新品首测。'),
 32:(3,0,0,'全新试玩信号，研运主体未取证。'),33:(3,0,0,'两款新作公开，未具名且无主体分层证据。'),34:(2,0,0,'11月6日发售定档，R0。'),35:(2,0,0,'俱乐部解散；短文未证明名单关系或代表作声量，R0。'),
 37:(0,3,0,'仿生机器人公司与AI硬件招聘，没有已落实游戏应用，非游戏事件E0。'),
 38:(1,0,0,'MMO节奏与未来方向访谈；不是21日正式上线或新平台政策，不凭旧活动抬E。'),
 42:(1,3,0,'米哈游《源初之结》设计评论，正文首支PV为8月26日；无本期首曝/测试状态变化。'),
 43:(3,3,0,'Supercell完成Metacore收购，但已在10月19日报卡片曝光；无新状态，重复排除。'),
 45:(2,0,0,'9月17日既有作品10月21日扩展Steam；研运IzanagiGames已证实，但来源没有较大声量量化依据，不凭有作品即给R1。'),
 46:(2,0,0,'公布未来12月4日发售；独立日历召回，R0。'),49:(3,0,0,'10月14日开始的合作测试晚到报道；不把合作当竞技、不把采集日当首测日。'),
 53:(3,3,1,'腾讯生活模拟新作公开稿，算分10；英文镜像与同批2025旧稿混杂，正文没有绝对首曝日期，保留候选但暂不发表以免把旧公开当新公开。'),
 55:(2,3,0,'超自然游戏旧成绩复盘，正文明确2025年；非本期新增状态。'),
 61:(0,3,0,'版号常规审批，且正文11月不在窗口。'),66:(0,3,0,'例行股东回报/分红计划，正文1日晚及2025—2027，非当前窗口异常资本事件。'),
 70:(1,0,0,'创作历程、旧财务困难复盘，不能把过去账户见底写成本期流动性异常。'),
 87:(2,0,0,'旧产品表现与玩法案例，正文11月上线后语境，与21日窗口不一致。'),
 92:(2,3,0,'下周11月24—30日清单，不能把镜像采集日期改成实际测试日期。'),
 98:(1,3,0,'终末地测试与工业设计复盘，非本期首次曝光或测试发生。'),
 102:(0,3,0,'和平精英文旅活动案例，不是新的资本/平台或产品状态。'),
 107:(3,2,0,'鹰角参投团队Demo报道，正文11月10日与10月17日互相冲突，无法核验本期事件日期，来源日期门禁排除。'),
 122:(2,0,0,'X-Clash孵化复盘明确为2025年10月表现，不能当2026本期市场变化。'),
 127:(1,0,0,'制作人讲述既有作品文化、战斗与品质设计，主体层级不明。'),
 132:(3,0,0,'独立游戏孵化空间公开与合作案例，但未证实符合重点主体关系或代表作声量，R0。'),
 142:(1,0,0,'前字节成员独游访谈；半次元创始身份不等于重点游戏项目制作人/主策/主美，不自动R2。'),
 147:(2,0,0,'搜打撤小游戏旧案例，原文2025；背景腾讯网易不能把实际小团队抬为R3。'),
 152:(2,3,1,'腾讯CF手游十周年公开与国际服计划，但正文明确2025年，旧稿不因翻译采集而入选。'),
 159:(0,3,0,'王者荣耀歌曲文旅联动，E0。'),163:(0,3,0,'Unite Shanghai 2025技术分享，旧技术复盘非本期状态新闻。'),
 179:(0,3,0,'网易历史文化联动与公益宣传，非本期高E事件。'),
 189:(1,0,0,'项目失败机制复盘，不是新项目取消公告，主体不能由背景公司推导。'),
 194:(0,0,0,'Steam主题促销节，且正文为22日；非产品新发售。'),200:(2,0,0,'独游成绩与创业历程，正文2025半年榜；没有本期新状态。'),
 208:(2,1,0,'Epic平台与UE6方向来自Unreal Fest Tokyo 2025，旧活动，PC市场R1不因UE名气变R3。'),
 213:(3,3,0,'完美世界本期公告：两支已认购基金完成募资，资本状态从募资转完成；E3R3M0=9。'),
 214:(1,0,0,'工会制度解释稿，非具体资本/组织变更。'),216:(2,1,1,'GTA6分流预测及调查；PC/主机市场整体R1，E2R1M1=3，不因大IP提高主体。'),
 217:(2,1,0,'独游与原创IP市场评论，PC/主机市场整体R1、4?实际E2R1=2，未过线。'),
 218:(2,1,0,'Xbox未来硬件价格/档期传闻，名单外PC/主机市场R1，来源是预测并非正式决策。'),
 221:(2,3,0,'挪威拟将Roblox纳入未成年人社交限制，但仅snippet，缺完整正文不得发表。'),
 222:(2,0,0,'演唱会取消，仅snippet；社区声明范围需另核验。'),223:(2,0,0,'Rotate Rings下载成绩，仅snippet且未取证主体层级。'),
 227:(1,1,0,'Innersloth合同经验访谈，主体代表作有证据但无新资本状态，E1低于线。'),
 228:(1,0,0,'Fuse联合开发模式复盘，不能把流程讲解视作新重大合作；不凭发布商常识补归属。'),
 229:(0,3,0,'发行榜短摘要，E0及snippet。'),230:(0,3,0,'季度授权收入常规财报，snippet且无异常基准。'),231:(3,0,0,'Mika融资短摘要100字；无全文、无名单关系取证。'),
 232:(1,0,0,'创作访谈包含历史旧发售，不能作为本期新品。'),233:(1,0,0,'试玩评论与设计评价，不是当期首次公开或上线。'),234:(1,0,0,'作曲家职业与裁员应对复盘，无具体新公司变更。'),
 237:(0,0,0,'常规Game Pass入库名单。'),240:(2,1,0,'Xbox技术升级，PC/主机平台信息R1。'),
 242:(2,1,0,'下一代Xbox价格与档期传闻，R1未达线。'),243:(2,1,0,'PS5实体与数字销售结构，PC/主机市场R1。'),
 244:(3,1,0,'潜在买方估值报道，不是成交；Xbox市场业务R1。'),245:(2,1,0,'Game Pass服务调整传闻，R1。'),246:(3,1,1,'EA重启Fight Night制作消息，EA名单外，来源有代表系列与15年空窗，E3R1M1=4。'),
 247:(0,0,0,'PS5安全系统更新，非游戏业务新政策。'),248:(1,1,0,'Xbox Labs浏览器试验演示，非新业务发布状态，且旧Labs背景已曝光。'),
 251:(1,0,0,'作品结束更新支持，但名单归属及代表产品声量没有本候选证据。'),
 255:(1,1,1,'使命召唤撤离玩法开发复盘；竞技M1，但E1R1M1=2。'),258:(2,1,0,'Xbox价格传闻重复来源。'),
 261:(2,0,0,'复刻产品预告及未来档期，来源未证实重点主体。'),263:(2,0,0,'复刻作品未来发售预告，未证实主体重要性。'),
 266:(2,0,0,'新品发售日预告，不是现在发售，日历单独召回。'),268:(2,0,0,'既有作品Switch2演示，未证明本期上线。'),
 269:(2,1,0,'Xbox FSR图形技术升级，主机整体信息R1。'),270:(2,1,0,'Game Pass未来调整传闻。'),
 271:(0,0,0,'GTA6啤酒品牌线下营销传闻，不是游戏跨平台上线。'),272:(0,0,0,'真人宣传片拍摄猜测，不是GTA6上线或跨平台。'),
 274:(1,0,0,'试玩前瞻与访谈；无可证主体重要性。'),275:(1,0,1,'竞技战斗试玩前瞻，不证明首次测试/立项；主体重要性未证实。'),276:(1,0,0,'试玩前瞻，不证明本期首测。'),
 277:(0,0,0,'杂志综合旧消息；下述逐条补卡审查，招聘不入选。'),278:(0,0,0,'独游通讯与招募，非当期行业事件；日历信号逐项另审。'),
 279:(0,0,0,'第三方升级器常规版本。'),281:(1,1,1,'守望地图设计访谈；有代表作声量但非本期状态变化。'),282:(0,0,0,'新品节试玩推荐，不证明首测节点。'),
 285:(1,1,0,'鬼武者复刻可能性采访，未正式公布项目。'),286:(3,1,0,'Dont Nod启动保护程序属于异常流动性状态；代表作虽可证，但名单外R1，E3R1M0=3。'),
 287:(0,0,0,'普通既有肉鸽更新，不因借用Diablo概念升级事件。'),289:(2,1,1,'PEGI付费随机物品评级实施，报道以PC/主机EA足球案例为主，未证实移动市场整体范围，E2R1M1=3。'),
 290:(1,0,0,'复刻游戏评论，非当期明确首曝/上线。'),294:(0,0,0,'Deadlock角色内容更新与投票，E0。'),
 298:(2,1,0,'FSR图形兼容技术扩展，PC/主机市场整体信息R1。'),299:(0,0,0,'使命召唤PC启动配置指导，普通技术说明。')}

# Translation mirrors of the same archive are reviewed as the same concrete
# article/event, not as extra reporting. Two duplicate archives are also marked.
archive_groups={}
for i in range(50,213):
    x=S[sid(i)];key=x['url'].rsplit('/',1)[-1];archive_groups.setdefault(key,[]).append(i)
alias={}
for ids in archive_groups.values():
    for j in ids[1:]:alias[j]=ids[0]
# Explicit reverse-scan destinations, all industry inputs included.
ai_i={39,41,51,52,168,169,171,172,173,174,175,176,177,178,184,185,186,187,188,190,191,197,207,210,215,239,250,254,273,284,288,297,300,304}
for i in range(1,306):
    if i in ai_i:continue
    original=alias.get(i,i);args=events.get(original,(0,0,0,'E0：普通活动/版本/宣传、泛职场或非游戏内容；完整输入信号留在审计。'))
    e,r,m,reason=args
    # Non-focus named subjects use exact evidence rather than borrowed prominence.
    kw={}
    if r==3:
        mapping={37:('叠纸游戏','叠纸'),42:('米哈游','米哈游'),43:('Supercell','Supercell'),53:('腾讯','Tencent'),55:('巨人网络','巨人'),61:('哔哩哔哩','Bilibili'),66:('吉比特','ギガビット'),92:('鹰角网络','イーガン'),98:('鹰角网络','イー'),102:('腾讯','テンセント'),152:('腾讯','Tencent' if original==155 else 'Tencent'),159:('腾讯','テンセント'),163:('叠纸游戏','ディエジ'),179:('网易','NetEase'),213:('完美世界','完美世界'),221:('Roblox','Roblox'),229:('Scopely','Scopely'),230:('Scopely','Monopoly')}
        company,needle=mapping.get(original,('腾讯','Tencent'))
        # Translation mirror takes its own exact line; if this translation lacks
        # an identifiable policy name, evidence cannot establish the tier.
        pats={'腾讯':['Tencent','テンセント','텐센트','腾讯'], '巨人网络':['巨人','Giant','giant','거인'], '米哈游':['米哈游','miHoYo'], '吉比特':['ギガビット','Gigabit','지비트'], '鹰角网络':['イーガン','イーグル','Eagle','이글','鹰角'],'叠纸游戏':['ディエジ','叠纸','Papergames']}
        needles=[needle]+pats.get(company,[company]);found=next((n for n in needles if n in S[sid(i)]['text']),None)
        if e and found:kw=dict(subject=company,kind='focus_subject',focus=[company],subject_quote=found)
        elif e:r=0;reason+=' 当前译文未能逐字证明名单主体，R降0。'
    elif r==2:
        if i==107 or original==107:
            n=next((n for n in ['鷹角','Yingjiao','Eagle','잉자오'] if n in S[sid(i)]['text']),None)
            if n:kw=dict(subject='浣犬游戏',kind='focus_affiliate',focus=['鹰角网络'],subject_quote=n)
            else:r=0
    elif r==1:
        if original in [227,246,281,285,286]:
            n={227:'Among Us',246:'Fight Night',281:'Overwatch',285:'Onimusha',286:'Life is Strange'}[original]
            if n not in S[sid(i)]['text']:r=0
            else:kw=dict(subject={227:'Innersloth',246:'EA',281:'守望先锋开发团队',285:'Capcom',286:"Don't Nod"}[original],kind='representative_subject',subject_quote=n)
        else:kw=dict(subject='PC/主机市场',kind='pc_console_market',subject_quote=S[sid(i)]['text'].splitlines()[0])
    if m:
        if original==53:kw.update(genre='life_simulation',genre_quote='life simulation')
        elif original==152:
            n=next((n for n in ['shooter','Shooter','シューティング','슈팅'] if n in S[sid(i)]['text']),None)
            if n:kw.update(genre='competitive',genre_quote=n)
            else:m=0
        else:
            n=next((n for n in ['shoot','Shoot','FPS','Fight Night','FC 27','七龙珠','使命召唤','Overwatch'] if n in S[sid(i)]['text']),None)
            if n:kw.update(genre='competitive',genre_quote=n)
            else:m=0
    d=industry(i,e,r,m,reason,**kw)
    if kw.get('kind')=='representative_subject':d['subject_assessment']['representative_product']={227:'Among Us',246:'Fight Night',281:'Overwatch',285:'Onimusha',286:'Life is Strange'}[original]
    if i in alias and alias[i] not in ai_i:
        d.update(decision='merge',merge_into=f'I{original:03}',reason=f'同一游戏茶馆archive={S[sid(i)]["url"].rsplit("/",1)[-1]}的翻译镜像；不增加独立来源。'+reason)
    if 50<=i<=212:d['mirror_review']=dict(archive_id=S[sid(i)]['url'].rsplit('/',1)[-1],date_caution='采集日不等于原始事件日，全文逐段检查旧年份、未来档期、历史语境。')

# Strong same-event mergers, based on the already-read body rather than title.
d=DM['I036'];d.update(decision='include',entities=['腾讯','光子','宇宙小狗工作室','人间异想计划'],reason='正式公开产品名与22分钟实机，不是旧招聘复述；腾讯直属光子R3；普通开放世界ARPG不等于指定竞技品类，M0。')
d['scores']=dict(event=3,relevance=3,hook=0,total=9)
d['source_ids']=[sid(36),sid(40)]
d['cluster_basis']=dict(subject='腾讯光子宇宙小狗工作室',product='人间异想计划',event_date='2026-10-21',event='正式公开名称及实机演示')
d['subject_assessment']=dict(subject='腾讯',kind='focus_subject',focus_companies=['腾讯'],basis='原文直接说明腾讯旗下光子工作室群宇宙小狗工作室，不凭背景网易给R。',evidence=[ev(36,'腾讯正式公布了旗下光子')])
d['genre_assessment']=dict(matched_genres=[],basis='轻怪谈都市开放世界RPG、轮切战斗不足以证明竞技或数值卡牌RPG。',evidence=[ev(36,'轻怪谈都市异想开放世界RPG')])
d['pc_release_scope']=dict(classification='domestic_or_focus',basis='腾讯直属光子项目；PC/主机方向不降低主体R。',evidence=[ev(40,'重视PC、主机端品质')])
DM['I040'].update(decision='merge',merge_into='I036',reason='同日同产品正式公开事件；文中明确部分对话虚构，不使用员工数、狗主策等戏谑表述作事实。')
DM['I213']['decision']='include'
DM['I045']['pc_release_scope']=dict(classification='ordinary_overseas_single_player',basis='IzanagiGames旧主机单人作品扩展Steam，并非新品首次上线；不凭已有作品列表自动认定主体声量。',evidence=[ev(45,'游玩人数：1人'),ev(45,'发售日期：2026年9月17日')])
# Some automatic translations alter proper names (e.g. Eagle Corner). Do not
# silently resolve them from memory or rewrite source evidence to pass a regex.
for i in [55,92,98,107]:
    d=DM[f'I{i:03}'];d['translation_unverified_original_scores']=dict(d['scores'])
    d['scores'].update(relevance=0,total=d['scores']['hook'])
    d['subject_assessment']=dict(subject='当前翻译稿中的实际工作室/厂商',kind='other_or_unknown',focus_companies=[],basis='原文机器翻译的专名与统一名单缺少可直接核验的拼写对应；不凭记忆补关系。原初步评分保留，当前保守R0；日期门禁已独立排除。',evidence=[])
    d['reason']+=' 当前译名未完成名单专名核验，R保守0，原初评留translation_unverified_original_scores。'

# History matches retain every occurrence and all exposure metadata; old hidden
# items do not get an automatic carryover if current R or source gates fail.
history_keywords={43:['Metacore'],152:['火影忍者'],248:['Xbox Labs'],258:[],}
for d in D:
    i=int(d['candidate_id'][1:]);keys=history_keywords.get(alias.get(i,i),[])
    matches=[h for h in H if any(k.lower() in (' '.join([h['title'],h['event']]+h['claims'])).lower() for k in keys)]
    if matches:
        d['history_check']=dict(history_match=True,novelty='repeat_only',prior_occurrences=[h['title']+'｜'+h['report_kind']+' '+h['report_window']['start']+'_to_'+h['report_window']['end'] for h in matches],new_facts=[],prior_card_exposed=any(h['card_exposed'] for h in matches))
        d['history_exposure_details']=[{k:h.get(k) for k in ['title','report_window','card_exposed','card_rank','card_limit','card_exposure_source']} for h in matches]
        if d['decision']!='merge':d.update(decision='exclude',reason=d['reason']+' 14日内同事件已收录且至少一次卡片曝光，无实质新增事实。')

# Fix the CF vs Naruto mismatch: CFM's old 2025 international announcement is
# not the 2026 Naruto event, and must not be false-matched by genre or company.
for i in [152,154,155,156,157,158]:
    d=DM.get(f'I{i:03}')
    if d:
        d['history_check']=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None)
        d.pop('history_exposure_details',None)

# AI reverse scan includes all industry candidates, even the ones below the
# industry threshold. Historical mirrors remain excluded but individually traced.
for i in sorted(ai_i):
    reason='泛AI/硬件或宽泛立场，未形成有足够证据的本期游戏直接应用；优先采用本期直接研发案例。'
    if i in {51,52,168,169,171,172,173,174,175,176,177,178,184,185,186,187,188,190,191,197,207,210}:
        reason='原文2025或已过去/尚未到来的活动、上线语境与本期冲突；保留AI直接应用候选，但不把多语种镜像当2026-10-21新进展。'
    if i==41:reason='Demo风险综合稿，所述酒鬼女神取消试玩已是旧事件；本期优先采用288的新采访细节与375的新分析，不重复普通事件摘要。'
    if i==284:reason='创始人计划下一次创业使用AI原型/重复任务/测试，尚未实际落地；破产旧事实不在AI栏重复。'
    if i in {239,254}:reason='创意与AI一般立场表述，没有已发生的具体使用管线或能力变化，非直接应用新闻。'
    d=base(f'A{i:03}','ai_trends',[i],reason=reason)
    d.update(ai_tier='direct_application' if i not in {273,297,300} else 'transferable_frontier',game_stage=['development'],industry_reverse_scan=True)
    if d['ai_tier']=='transferable_frontier':d['migration_path']='潜在影响本地研发工具/推理成本/陪伴交互，但来源缺少足够游戏采用证据，未入选。'
    if i in {39,215,288,304}:d.update(decision='include',reason={39:'测试服务商披露人工Review、有效执行率与证据回溯的实际业务环节，属直接研发采用。',215:'101次访谈的游戏研发AI采用调查，时间范围、定义与流程深度清楚。',288:'新采访量化ReVamp从数万Steam测试报名缩至Discord数百人，并披露人工准入与保密协议机制，区别于昨日公告。',304:'恺英旗下SoonPlay20日公测，本期披露视频生成、边玩边改与私有反馈机制；报告按来源陈述，不背书全球首个等宣传。'}[i])
for i in range(306,325):
    d=base(f'A{i:03}','ai_trends',[i],reason='未落入具体游戏采用；本期已有更直接的研发、测试、产品案例，不用通用模型、融资、芯片、医学或基础设施新闻凑数。')
    d.update(ai_tier='transferable_frontier',game_stage=['development'],industry_reverse_scan=False,migration_path='可潜在作用于研发工具、资产或运营设施；来源尚不足证明本期具体游戏场景，故不发表。')

# Non-industry input pool: all calendar records get an industry judgment too,
# preserving low-subject first-test/launch candidates without inflating R.
for i in range(325,362):
    t=S[sid(i)]['text'];e=0
    if i in {345,346,347,350,351,355}:e=3
    elif i in {330,344,354,356,357,358,359,360,361}:e=2
    d=industry(i,e,0,1 if i in {347,350} else 0,'单一日历信号不能证明研运主体/重点公司关系；普通版本、预下载、联动不构成高E行业事件。')
    if e and i in {347,350}:d['genre_assessment']=dict(matched_genres=['competitive'],basis='本候选明确格斗/篮球体育竞技标签；仅M1，不抬R。',evidence=[ev(i,'格斗' if i==347 else '篮球')])
    if i==330:d.update(decision='merge',merge_into='I036',reason='同产品同日正式公开事件，行业证据并入I036；日历仍独立评审。')

community_reasons={362:'长期水楼，无可命名独立新事件。',363:'旧AI复活讨论，本期仅一句联机需求延续，缺新进展。',364:'标题称日本游戏普遍维护，正文当日主要是网友推测，不能写成已证实全行业事故。',365:'流水榜单观察及玩家预测，不作为独立社区争议事件。',366:'16日素材相似旧争议，21日两回复未提供新进展，且20日已改说法仅玩家转述。',367:'创作者健康近况，非游戏业务/社区机制焦点；不依据回复补医疗判断。',368:'主播来电营销趣闻，未产生足够独立争议机制，留候选。',369:'19日联动争议已发表，本期仅旧争议延续，排除重复。',370:'正式公开已进产业栏，同一事件不重复进入社区。',371:'停更后周年更新计划触发回流期待与盈利/运营顾虑，完整社区事件。',372:'18日跨作角色落地旧讨论，本期无新阶段。',373:'演唱会取消后补偿范围出现分歧，完整官方公告未采到，帖子只引述符合条件，不能写全部报销。',374:'京东新主体已在20日产业卡片展示，21日只有玩家猜测，未成新事件。'}
for i in range(362,375):
    d=base(f'C{i:03}','community_discourse',[i],reason=community_reasons[i])
    if i==371:d['decision']='include'
# EAC actual switch is Oct20, but the source is from Oct21; article discussion
# itself uses 'today' for Oct20, so it fails the event window and cannot be new
# community news. Use two demonstrably Oct21 community triggers instead.
d=base('C283','community_discourse',[283,26],reason='正文明确EAC切换及差评发生于October20，虽21日采集也不能改成21日社区新事件；排除日期错位。')
DM['C373'].update(decision='include',reason='21日晚新帖讨论演唱会取消后的住宿/交通报销范围；准确归因帖子和网友，不能把“符合条件”泛化成全额。')

# Newsletter: individual industry signals are not merged as a digest. No memory
# is used to add Marvel Rivals attribution absent from this source text.
newsletter_industry=[('PEGI','PEGI把付费随机物品旧数字游戏评级提高至16','Existing digital-only games',2,1,0),('STEAM_PRICE','Steam区域定价建议10月刷新','regional pricing recommendations',2,1,0),('GDC','GDC2027改为四天','slimming down to four days',2,0,0),('CIRCANA','美国PC/主机玩家购新游戏频次调查','41% of US video game players',2,1,0),('RIOT','Riot财务负责人谈作品成功率及动画收支','CFO of Riot',1,3,0),('ECC','网易射击新作愿望单数据','NetEase',2,3,1)]
for key,title,quote,e,r,m in newsletter_industry:
    cid='N_'+key;d=base(cid,'industry_news',[375],event=title,reason='newsletter单条线索独立评审；普通泛PC/主机市场R1或例行/存量产品成绩不足资格。')
    d['scores']=dict(event=e,relevance=r,hook=m,total=e*r+m)
    d['history_check']=dict(history_match=False,novelty='new_event',prior_occurrences=[],new_facts=[],prior_card_exposed=None)
    kind='pc_console_market' if r==1 else 'focus_subject' if r==3 else 'other_or_unknown'
    d['subject_assessment']=dict(subject='Riot Games' if key=='RIOT' else '网易' if key=='ECC' else title,kind=kind,focus_companies=['Riot Games'] if key=='RIOT' else ['网易'] if key=='ECC' else [],basis='按当前来源实际主体判断；评级范围未证明移动市场，不能凭常识给R3。',evidence=[ev(375,quote)] if r else [])
    d['genre_assessment']=dict(matched_genres=['competitive'] if m else [],basis='正文明确射击产品' if m else '本事件没有指定细分类别，不借背景产品加M。',evidence=[ev(375,'competitive shooter')] if m else [])
    if key=='ECC':d['reason']='仅约10万愿望单的既有测试后成绩快照，不是本期首曝、上线或结构性市场变化，复核E从2改1。';d['scores'].update(event=1,total=4)
    if key=='RIOT':d['subject_assessment']['evidence']=[ev(375,'CFO of Riot')]

# Deep observations depend on selected current events. The first incorporates
# the configured newsletter and adds a distinct conditional mechanism to the
# prior demo-exposure discussion: searchable micro-ideas vs complex products.
for cid,ids,title,reason in [('D_DISCOVERY',[375,288],'AI仿制风险取决于玩法复杂度与搜索名称，统一撤回Demo并非同一收益','本期newsletter完整核心正文可读；新增无公开构建也出现模仿的关键词案例及复杂产品边界，与20日泛Demo曝光成本的观察形成实质新机制。'),('D_QA',[39,215],'AI覆盖研发环节后，质量判断与流程整合成为瓶颈','两条本期已入选AI新闻共同支持：采用广不等于整合深，生成增加Review及体验判断需求；区别于20日资产导入引擎的工具可用性。')]:
    d=base(cid,'deep_analysis',ids,event=title,decision='include',reason=reason);d['scores']=dict(relevance=2,insight=3,evidence=3,card=3,total=11)
    d['topic_key']=title;d['source_priority']='configured_newsletter' if cid=='D_DISCOVERY' else 'selected_current_events'
    d['quality_route']='横向比较' if cid=='D_DISCOVERY' else '数据型案例'

save('selection_decisions.json',dict(scoring_version='subject_genre_v2',report_type='daily',date='2026-10-21',history_window=dict(start='2026-10-07',end='2026-10-20'),decisions=D))

# Preserve the extractor's raw audit before editorial corrections.
raw=P/'release_calendar_audit.json';backup=P/'release_calendar_audit_raw.json'
if not backup.exists():shutil.copyfile(raw,backup)
A=json.loads(backup.read_text(encoding='utf-8'))
for n in A['nodes']:
    n['editorial_review']='逐段核对原文事件、实际日期、正文质量、来源独立性与历史；不使用行业评分决定日历资格。'
    prod=n['product'];ids=n['source_ids']
    if prod in {'GTA6','恶魔之魂','黑暗之魂2','赛博朋克2077','克苏鲁：恐怖深渊','沙丘3','魔兽世界'}:
        n.update(publish_eligible=False,window_eligible=False,editorial_exclusion='历史发售/背景讨论/动画电影/营销预告，不是本期新品上线或跨平台。')
    if prod in {'和平精英体验服','地下城与勇士：起源','炉石传说','星球：重启'}:
        n.update(publish_eligible=False,editorial_exclusion='普通老品版本/卡包/体验服，不属重大模式或重启。')
    if prod=='汪洋大盗哥':n.update(signal_type='new_game_test',event='新版Demo公开；未证明首次测试',editorial_exclusion='单源，且不是正式发售。')
    if prod=='无光绝境':n.update(event_date='2026-10-14',window_scope='outside',window_eligible=False,publish_eligible=False,editorial_exclusion='原文明确10月14日开始合作Playtest，不能按21日采集算测试日。')
    if prod.startswith('账单必须支付'):n.update(event_date='2026-07',window_scope='outside',window_eligible=False,publish_eligible=False,date_precision='原文仅7月底，不补造日期，不可发布',editorial_exclusion='历史7月底发售、5月仿品下架，不能当本期发售。')
    if prod in {'掘地求财：铲友齐上阵','皇牌空战8：希孚之翼','怪物史莱克2 复刻版（DreamWorks Shrek 2 Remastered）','The Wolf Among Us 复刻版','最终幻想 RESONANCE','收获日：Aces High'} and n['signal_type']=='old_cross_platform_launch':
        n.update(publish_eligible=False,window_eligible=False,editorial_exclusion='仅未来定档/演示，未在窗口实际跨平台上线。')
    if any(S[v]['body_status']!='full' for v in ids):n.update(publish_eligible=False,editorial_exclusion='来源只有RSS/snippet，不满足正文事实门禁。')

def add_node(product,ids,date,signal,event,eligible=True,reason='',focus=None,bonus=0):
    ids=[sid(v) for v in ids]
    # Fingerprint same full text ignoring whitespace; translated archive mirrors
    # additionally collapse to one original editorial source.
    fps=[]
    for v in ids:
        x=S[v];ar=re.search(r'youxichaguan.com/\w+/archives/(\d+)',x['url'])
        fp='archive-'+ar[1] if ar else hashlib.sha1(re.sub(r'\s+','',x['text']).encode()).hexdigest()
        if fp not in fps:fps.append(fp)
    count=len(fps);industry_ids=[v for v in ids if S[v]['section']=='industry_news'];ib=int(bool(industry_ids))
    factor=3 if signal in {'new_game_launch','new_game_test'} else 2 if signal.startswith('new_game') else 1
    strength=min(count,3)+ib;scope='report_window' if date=='2026-10-21' else 'next_day_lookahead' if date=='2026-10-22' else 'future_announcement' if signal in {'new_game_schedule','new_game_first_reveal'} else 'outside'
    n=dict(product=product,event_date=date,signal_type=signal,event=event,event_type_score=factor,first_seen_order=len(A['nodes'])+500,observed_signal_types=[signal],observed_events=[event],industry_ids=industry_ids,release_ids=[v for v in ids if S[v]['section']=='release_calendar'],source_fingerprints=fps,source_ids=ids,appearance_count=count,appearance_score=min(count,3),industry_bonus=ib,source_strength_score=strength,base_priority_score=factor*strength,company_bonus=bonus,priority_score=factor*strength+bonus,focus_companies=focus or [],focus_company_relationships={c:'direct' for c in focus or []},company_evidence_ids=[sid(36)] if bonus else [],company_relationship='direct' if bonus else 'none',multi_source_eligible=count>=2,window_eligible=eligible,window_scope=scope,publish_eligible=eligible and count>=2 and all(S[v]['body_status']=='full' for v in ids),coverage='industry_and_release' if industry_ids and any(S[v]['section']=='release_calendar' for v in ids) else 'industry_only' if industry_ids else 'release_only',coverage_rank=0,editorial_review=reason)
    if reason and not eligible:n['editorial_exclusion']=reason
    A['nodes'].append(n)

# Replace the single-source reveal node with the full same-product same-date
# cluster, independent of its industry inclusion.
A['nodes']=[n for n in A['nodes'] if n['product']!='人间异想计划-怪诞都市开放世界']
add_node('人间异想计划',[36,40,330],'2026-10-21','new_game_first_reveal','正式公布名称及22分钟实机',focus=['腾讯'],bonus=3)
add_node('AKIBA LOST（秋叶原迷踪）',[45],'2026-10-21','old_cross_platform_launch','已于9月17日发售的作品登陆Steam')
# The original new-launch entry for AKIBA is the same day/product node.
A['nodes']=[n for n in A['nodes'] if not (n['product']=='AKIBA LOST（秋叶原迷踪）' and n['signal_type']=='new_game_launch')]
add_node('无光绝境',[31,49],'2026-10-14','new_game_test','合作Playtest开启',False,'原文10月14日，报告窗口外；不与12月2日EA定档合并。')
A['nodes']=[n for n in A['nodes'] if not(n['product']=='无光绝境' and n.get('first_seen_order',0)<500)]
add_node('Lili’s Miniature World',[53],'2026-10-21','new_game_first_reveal','英文稿称正式公开生活模拟新作',False,'同批镜像大量旧文，首曝绝对日期未能确认；单源且不增补中文正式名。')
add_node('CRITICAL REFLEX两款未具名新作',[33],'2026-10-21','new_game_first_reveal','两款新作首曝',False,'未具名产品不能以两款打包进入最终日历。')
for prod,ids,date,signal,event in [
 ('代号：神灯',[345],'2026-10-21','new_game_test','删档测试'),
 ('炉石传说',[326,339],'2026-10-21','old_major_update','黑暗帝国的统治卡包/版本'),
 ('失落城堡2',[335],'2026-10-21','new_game_preload','预下载'),
 ('星途天城',[337],'2026-10-21','new_game_preload','预下载'),
 ('深空之劫',[348],'2026-10-21','new_game_preload','预下载'),
 ('奥特曼英雄决战',[353],'2026-10-21','new_game_preload','测试预下载'),
 ('篮球少女：飞跃巅峰',[349],'2026-10-21','new_game_preload','预下载'),
 ('Bloody Hell Hotel',[354],'2027','new_game_schedule','定于2027上线'),
 ('CRYMELIGHT',[355],'2026-10-21','new_game_test','Demo公开'),
 ('RV There Yet?',[356,357],'2026-10-29','old_cross_platform_launch','未来跨主机上线'),
 ('Pratfall',[358],'未公布','old_cross_platform_launch','未来跨主机上线'),
 ('Console Archives Raiden Project',[359],'2026-10-22','new_game_launch','发售'),
 ('Arcade Archives Ace Driver Victory Lap',[360],'2026-10-22','new_game_launch','发售'),
 ('The Apothecary Diaries: The False Imperial Brother',[361],'2027-03-18','new_game_schedule','公布未来档期')]:
    A['nodes']=[n for n in A['nodes'] if n['product']!=prod]
    eligible=prod not in {'炉石传说','RV There Yet?','Pratfall'}
    add_node(prod,ids,date,signal,event,eligible,'炉石卡包是普通更新，排除；RSS来源仍需完整正文。' if prod=='炉石传说' else '产品日历独立召回；按实际事件与来源质量，不受行业R影响。')
    if prod=='RV There Yet?':A['nodes'][-1].update(appearance_count=1,appearance_score=1,source_strength_score=1,base_priority_score=1,priority_score=1,source_fingerprints=['Gematsu同一公告的两个RSS标题'],multi_source_eligible=False,editorial_exclusion='同一媒体同一公告的RSS镜像只算一源；实际上线10月29日窗口外。')
# Supplement weekly-list events from the full original paragraphs, retaining
# their November dates rather than inventing October launches.
for prod,needle in [('アーキタイプ：終末地','11月28日'),('絶地鴨衛','11月'),('火環','11月')]:
    add_node(prod,[92,94,95,96,97],'11月（年份未证实）','new_game_test','11月24—30日清单中的测试/上线',False,'翻译镜像共享archive212770，实际11月清单；具体产品日期/年份不能确定，不在本期，不补造。')
    A['nodes'][-1]['date_precision']='列表语境，具体日/年份不可用于发布'
for prod,i,event in [('失落城堡2',335,'10月22日上线'),('星途天城',337,'10月22日9点上线'),('深空之劫',348,'10月22日上线'),('奥特曼英雄决战',353,'10月22日开测')]:
    add_node(prod,[i],'2026-10-22','new_game_test' if i==353 else 'new_game_launch',event,True,'次日实际发生节点单独保留，与21日预下载按日期分组；仍单源，不进入正文。')
# A test that started outside this window and a future EA schedule announced in
# current sources are separate signals. Future schedules do not use the actual
# launch/test date gate. Neither low industry R nor a prior test excludes them.
A['nodes']=[n for n in A['nodes'] if n['product']!='掘地求财：铲友齐上阵']
add_node('掘地求财：铲友齐上阵',[30,46],'2026-12-04','new_game_schedule','定档12月4日多平台发售',True,'Gcores与游戏茶馆两源正文明确12月4日；不是旧品跨平台。日历不受行业R0影响。')
A['nodes'][-1]['first_seen_order']=30
add_node('无光绝境',[31,49],'2026-12-02','new_game_schedule','定档12月2日抢先体验',True,'两源正文分别明确预计2026年12月2日EA；与10月14日合作测试分开，未进入先前日历，不因行业排除而漏挂。')
A['nodes'][-1]['first_seen_order']=31
# Recall the remaining short-form demo signals, even though each remains a
# single source. Updates/participation alone are rejected in recall_rejections.
for prod,i,date in [('规则怪谈',2,'2026-10-21'),('余烬之镇',4,'2026-10-20'),('去月球 传奇RPG 之最终一小时',8,'2026-10-21'),('艾尔塔：逆神',9,'2026-10-21'),('HR.SOS',14,'2026-10-21'),('地渊珠宝匠',17,'2026-10-21'),('龙骨海盗',18,'2026-10-21'),('追逐末日之光',22,'2026-10-21'),('脍炙人口',33,'2026-10-21')]:
    add_node(prod,[i],date,'new_game_launch' if i==33 else 'new_game_test','免费上线' if i==33 else 'Demo公开',date=='2026-10-21','单源短稿；实际日期与首次性仍需完整证据，不凭品类强行入选。')
A['recall_rejections']=[dict(source_id=sid(i),decision_candidate_id=f'I{i:03}',reason='参展/试玩既有更新/预告/活动/赛季，不证明首次测试、首次正式公开或重大新模式；不进入新品节点。',evidence=S[sid(i)]['text']) for i in [3,5,6,11,12,13,15,19,20,21,23,24,25,26,28,29]]
for n in A['nodes']:
    # All scope labels derived from the retained event date.
    date=n['event_date'];n['window_scope']='report_window' if date=='2026-10-21' else 'next_day_lookahead' if date=='2026-10-22' else 'future_announcement' if n['signal_type'] in {'new_game_schedule','new_game_first_reveal'} else 'outside'
    if n.get('editorial_exclusion'):n['publish_eligible']=False
A['nodes'].sort(key=lambda n:(-int(bool(n['publish_eligible'])),-n['priority_score'],-n.get('company_bonus',0),-n['event_type_score'],-n['appearance_count'],-n.get('industry_bonus',0),n.get('first_seen_order',0)))
for j,n in enumerate(A['nodes'],1):n['candidate_id']=f'R{j:03}'
save('release_calendar_audit.json',A)
print('decisions',len(D),'release nodes',len(A['nodes']),'eligible',[n['product'] for n in A['nodes'] if n['publish_eligible']])

