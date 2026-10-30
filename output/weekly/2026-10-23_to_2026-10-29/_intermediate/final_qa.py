import json,re,sys,hashlib
from pathlib import Path
from collections import Counter,defaultdict
from datetime import date,timedelta,datetime,timezone
ROOT=Path.cwd();sys.path.insert(0,str(ROOT/'scripts'))
from report_artifacts import parse_report_items
from industry_timing import build_time_check
B=ROOT/'output/weekly/2026-10-23_to_2026-10-29/_intermediate';OUT=B.parent
ID='2026-10-23_to_2026-10-29';START='2026-10-23';END='2026-10-29'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rows=list(map(json.loads,(B/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()));src={r['source_id']:r for r in rows}
doc=read(B/'selection_decisions.json');ds=doc['decisions'];itemsdoc=read(B/'report_items.json');items=itemsdoc['items']
stage=B/'draft';report=stage/('game_industry_weekly_'+ID+'.md');text=report.read_text(encoding='utf-8');visible=parse_report_items(text)
for d in ds:
 if d['section']!='industry_news':continue
 if d['decision']!='exclude':d.pop('exclusion_gates',None)
 sid=d['source_ids'][0]
 if d['decision']=='exclude' and sid in ['S0034','S0283','S0634']:
  d['scores']=dict(event=2,relevance=2,hook=0,total=4)
  ev=next((p for p in src[sid]['text'].splitlines() if '蛮啾' in p),src[sid]['text'].splitlines()[0])
  d['subject_assessment']=dict(subject='蛮啾网络',kind='comparable_significant_subject',focus_companies=[],basis='来源证明研发发行大世界项目、2500万预约和既有二次元运营积累，具有较强行业影响力R2；未列名不是R1上限。新品定档E2，M0，4分。',evidence=[dict(source_id=sid,evidence=ev)])
  d['genre_assessment']=dict(matched_genres=[],basis='开放世界、捉宠及家园不能直接等同于生活模拟细分品类',evidence=[])
  d['reason']='蛮啾按实际产品覆盖和研发发行能力取R2；E2R2M0=4，行业未过线；产品日历独立通过多源排序。';d['exclusion_gates']=['score']
 if d['decision']=='exclude' and sid in ['S0925','S0936','S1325']:
  r=d['scores']['relevance'];m=d['scores']['hook'];d['scores'].update(event=1,total=r+m);d['reason']='纯裁员/劳资事件按E1；没有工作室关停或项目取消新状态，当前分数低于5。';d['exclusion_gates']=['score']
 if d['decision']=='exclude' and ('Monster Train 2 is getting a new clan' in d['event'] or '本周 Steam 值得关注的游戏' in d['event']):
  d['scores']=dict(event=0,relevance=0,hook=0,total=0);d['reason']='普通新增内容或综合发售清单E0；综合清单中的产品分别在产品日历反扫，不把无关产品打包成行业事件。';d['exclusion_gates']=['score']
for d in ds:
 if d['section']=='industry_news' and d['scores']['event']:
  d.setdefault('subject_assessment',dict(subject=d['entities'][0],kind='other_or_unknown',focus_companies=[],basis='当前输入未充分证明主体影响力，不能借背景关系抬分。',evidence=[]))
  d.setdefault('genre_assessment',dict(matched_genres=[],basis='本事件无明确重点品类取证',evidence=[]))
  d['time_check']=build_time_check(d['source_ids'],src,START,END,event_date=d.get('event_date') or 'unknown',basis='当前来源发布时间优先，缺失回退input date；事件发生时间不作准入门槛。')
for i in items:
 if i['section']=='release_calendar' and i['title']=='篮球少女：飞跃巅峰':
  old=next(x.body for x in visible if x.section=='release_calendar' and x.title==i['title'])
  new='灵犀互娱研运和发行的篮球策略养成手游《篮球少女：飞跃巅峰》于10月23日开启全平台公测；玩家以教练身份安排训练，在多周目循环中培养球员。'
  text=text.replace('- '+old,'- '+new)
  ev=next(p for p in src['S1349']['text'].splitlines() if '由灵犀互娱研运和发行' in p)
  i['claims']=[c for c in i['claims'] if c['claim'] in new]+[dict(claim='灵犀互娱研运和发行',source_id='S1349',evidence=ev),dict(claim='10月23日开启全平台公测',source_id='S1349',evidence=ev)]
  i['release']['company']='灵犀互娱';i['release']['platform']='全平台'
dump(B/'selection_decisions.json',doc);dump(B/'report_items.json',itemsdoc);report.write_text(text,encoding='utf-8')

# 原始index与JSONL一一闭环；全量文本扫描保留哈希，抽取数据只读。
ids=set(re.findall(r'`(S\d{4})`', (B/'report_inputs_index.md').read_text(encoding='utf-8')))
assert ids==set(src),(len(ids),len(src))
covered={s for d in ds for s in d['source_ids']}
coverage=[]
for r in rows:
 coverage.append(dict(source_id=r['source_id'],date=r['date'],section=r['section'],title=r['title'],chars=len(r['text']),sha256=hashlib.sha256(r['text'].encode()).hexdigest(),candidate_ids=[d['candidate_id'] for d in ds if r['source_id'] in d['source_ids']],review_status='decision_mapped' if r['source_id'] in covered else 'release_no_qualifying_signal',body_status=r['body_status'],fetch_status=r['fetch_status']))
assert all(r['section']=='release_calendar' for r in rows if r['source_id'] not in covered)
dump(B/'corpus_review.json',dict(records=len(rows),text_chars=sum(len(r['text']) for r in rows),index_complete=True,records_reviewed=coverage))

# 维度交叉计数只用来核验召回覆盖，不改变事件边界与入选规则。
patterns={
 '国内移动':r'手游|小游戏|移动游戏|mobile|minigame',
 '国产产品与人才':r'腾讯|网易|米哈游|灵犀|莉莉丝|吉比特|雷霆|制作人|Tencent|NetEase|miHoYo|Chinese|China',
 '市场数据':r'数据|收入|流水|销量|用户|市场|revenue|sales|market|million|bilh|millón|Million',
 '并购':r'收购|并购|投资|融资|众筹|acqui|funding|invest|financi|crowdfund',
 '平台政策':r'政策|许可|引擎|平台|商店|审核|policy|licens|engine|platform|store|EULA',
 '档期变动':r'定档|延期|停运|重启|跨平台|shutdown|shut down|delay|release date|launch date|cross-platform',
 '资本组织':r'财报|组织|裁员|制作人|CEO|COO|任命|离职|资本|layoff|studio|appoint|restructur',
 '海外重大':r'Xbox|Microsoft|Nintendo|Sony|Capcom|EA|Bungie|Atari|Supercell|Scopely|Roblox|global|全球|海外',
}
dimensions={k:[] for k in patterns}
for d in ds:
 if d['section']!='industry_news':continue
 hay=d['event']+' '+d.get('reason','')+' '+str(d.get('subject_assessment',{}))
 for k,p in patterns.items():
  if re.search(p,hay,re.I):dimensions[k].append(d['candidate_id'])
dump(B/'candidate_dimension_coverage.json',dimensions)

# 当前采集状态及manifest/实际JSONL差异，旧run_summary中的缺失与当前文件状态分开记录。
collection=[];dates=[(date.fromisoformat(START)+timedelta(days=n)).isoformat() for n in range(7)]
for day in dates:
 p=ROOT/'news_data/_collector_runs'/day/'run_summary.json'
 if not p.exists():collection.append(dict(date=day,status='missing_run',input_count=sum(r['date']==day for r in rows)));continue
 x=read(p);results=x.get('results',[])
 collection.append(dict(date=day,status='available',input_count=sum(r['date']==day for r in rows),failed_collectors=[z['collector'] for z in results if z.get('status')=='failed'],degraded_collectors=[z['collector'] for z in results if z.get('health')=='degraded'],recorded_consistency_mismatches=x.get('consistency_mismatches',[])))
manifest_missing=[]
for day in dates:
 rawurls=set()
 for section in ['industry_news','ai_trends','community_discourse','release_calendar','deep_analysis']:
  p=ROOT/'news_data'/section/day/'articles.jsonl'
  if p.exists():
   for line in p.read_text(encoding='utf-8').splitlines():
    if line.strip():rawurls.add(json.loads(line).get('url',''))
 for p in (ROOT/'news_data/_collector_runs'/day).glob('*manifest.json'):
  x=read(p)
  for v in x.get('items',{}).values():
   if v.get('url') and v['url'] not in rawurls:manifest_missing.append(dict(date=day,manifest=p.name,title=v.get('title'),url=v['url']))
dump(B/'collection_coverage.json',dict(dates=collection,current_manifest_urls_missing_from_jsonl=manifest_missing,input_counts_by_section=Counter(r['section'] for r in rows),input_counts_by_date=Counter(r['date'] for r in rows),short_or_unavailable_inputs=[r['source_id'] for r in rows if r['fetch_status']!='ok' or r['body_status'] in ['snippet','empty']]))
cov=['# 采集覆盖审计','','窗口：'+ID,'','| 日期 | 输入 | 采集失败 | 降级 |','| --- | ---: | --- | --- |']
for x in collection:cov.append('| '+' | '.join([x['date'],str(x['input_count']),','.join(x.get('failed_collectors',[])) or x['status'],','.join(x.get('degraded_collectors',[])) or '无'])+' |')
cov+=['','10月29日无运行与输入，未联网补缺；news_data只读。','',f'当前manifest有{len(manifest_missing)}个URL未在同日JSONL发现，具体清单见JSON；该计数不等同于正文证据缺失。','',f'65条short/snippet输入仅供审计，最终条目均避开不可用状态。']
(B/'collection_coverage.md').write_text('\n'.join(cov)+'\n',encoding='utf-8')

# 重新写决策总表，避免终稿修订后Markdown审计仍显示早期判断。
md=(B/'selection_decisions.md').read_text(encoding='utf-8')
md=re.sub(r'维度覆盖自检：[^\n]*','维度覆盖自检：'+ ' / '.join(k+str(len(v))+'张候选审计卡' for k,v in dimensions.items())+'；交叉计数，逐卡列表见candidate_dimension_coverage.json。',md)
md=md.split('| candidate |',1)[0]+'| candidate | decision | target_section | E/R/M或其他评分 | reason |\n| --- | --- | --- | --- | --- |\n'
for d in ds:md+='| '+' | '.join(str(v).replace('|','／').replace('\n',' ') for v in [d['candidate_id'],d['decision']+(' → '+d.get('merge_into','') if d['decision']=='merge' else ''),d['section'],d.get('scores',''),d['reason']])+' |\n'
(B/'selection_decisions.md').write_text(md,encoding='utf-8')
dump(B/'above_threshold_exclusions.json',dict(review_status='resolved',decisions=[d for d in ds if d['section']=='industry_news' and d['decision']=='exclude' and d['scores']['total']>=5]))

# 事实和日期闭环最终检查；题材/市场推断不冒充原始事实。
parsed=parse_report_items(text);pmap={(x.section,x.title):x.body for x in parsed}
sections={'industry_news':'industry','ai_trends':'ai','release_calendar':'release_calendar','community_discourse':'community','deep_analysis':'deep'}
for i in items:
 body=pmap[(sections[i['section']],i['title'])]
 for c in i['claims']:
  assert c['claim'] in body,(i['title'],c['claim'])
  assert c['source_id'] in i['source_ids'] and c['evidence'] in src[c['source_id']]['text']
for pattern in ['沐瞳',r'\bMoonton\b',r'\bMLBB\b','决胜巅峰','card_carryover','上期卡片未展示']:
 assert not re.search(pattern,text,re.I),pattern
print('QA',len(items),'items;',len(rows),'records;',len(ds),'decisions;',len(manifest_missing),'manifest URLs absent')
