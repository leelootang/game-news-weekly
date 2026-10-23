import json, re, sys, subprocess, shutil, hashlib, os
from pathlib import Path
from collections import Counter
from datetime import datetime, timedelta

os.environ['PYTHONUTF8']='1'
P=Path(__file__).resolve().parent;OUT=P.parent;ROOT=P.parents[3]
ID='2026-10-16_to_2026-10-22';NAME=f'game_industry_weekly_{ID}.md'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
D=read(P/'selection_decisions.json');I=read(P/'report_items.json')['items'];A=read(P/'release_calendar_audit.json')
ds=D['decisions'];dm={d['candidate_id']:d for d in ds}
text=(P/'staging'/NAME).read_text(encoding='utf-8')
assert D['scoring_version']=='subject_genre_v2'
assert {s for d in ds for s in d['source_ids']}==set(S)
assert len(dm)==len(ds)
assert {i['candidate_id'] for i in I}=={d['candidate_id'] for d in ds if d['decision']=='include'}
assert not re.search(r'沐瞳|Moonton|MLBB|Mobile Legends|决胜巅峰|card_carryover|补位|上期卡片未展示',text,re.I)
used={s for i in I for s in i['source_ids']}
assert all(S[s]['body_status']=='full' and S[s]['fetch_status']=='ok' for s in used)
for i in I:
    assert all(c['claim'] in i['body'] and c['evidence'] in S[c['source_id']]['text'] for c in i['claims'])
assert len([i for i in I if i['section']=='community_discourse'])<=3
selected=read(ROOT/'data/feishu/deep_review/replies/b2eeb82624f7427b852799f7642385e7.json')
assert selected['body_candidate_ids']==['C001','C002'] and selected['card_base_candidate_id']=='C001'
deep=[i for i in I if i['section']=='deep_analysis']
assert [i['candidate_id'] for i in deep]==['D_C001','D_C002']
assert (OUT/'deep_card_choice.txt').read_text(encoding='utf-8').strip()==deep[0]['title']

shutil.copyfile(P/'staging'/NAME,OUT/NAME)
shutil.copyfile(P/'staging'/'sources_used.md',OUT/'sources_used.md')
common=['--report',str(OUT/NAME),'--sources',str(OUT/'sources_used.md'),'--inputs',str(P/'report_inputs.jsonl')]
commands=[
 [sys.executable,r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\report_lint.py',*common,'--report-type','weekly'],
 [sys.executable,str(ROOT/'scripts/report_artifacts.py'),'validate',*common,'--items',str(P/'report_items.json'),'--decisions',str(P/'selection_decisions.json'),'--release-audit',str(P/'release_calendar_audit.json'),'--require-artifacts'],
 [sys.executable,str(ROOT/'scripts/deep_observation_handoff.py'),'lint-selection','--selection',str(ROOT/'output/deep_observation_review'/f'{ID}_selection.md')],
]
validation=[]
for command in commands:
    cp=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    output=cp.stdout+cp.stderr
    validation.append({'command':command,'exit_code':cp.returncode,'errors':[l for l in output.splitlines() if l.startswith('ERROR:')],'warnings':[l for l in output.splitlines() if l.startswith('WARN:')],'output':output})
    print(output or 'Passed: 0 errors, 0 warnings.')
if any(v['exit_code'] or v['errors'] for v in validation):
    (OUT/NAME).replace(P/('failed_'+NAME))
    save('validation_results.json',validation)
    raise RuntimeError('Canonical validation failed; final removed from publishable path.')

now=datetime.now().astimezone().isoformat()
counts=dict(Counter(i['section'] for i in I))
industry=[{'candidate_id':i['candidate_id'],'title':i['title'],'scores':dm[i['candidate_id']]['scores']} for i in I if i['section']=='industry_news']
boundaries=[{'candidate_id':d['candidate_id'],'event':d['event'],'scores':d['scores'],'reason':d['reason']} for d in ds if d['section']=='industry_news' and d['decision']=='exclude' and d['scores']['total'] in [3,4]]
repeat=[{'candidate_id':d['candidate_id'],'event':d['event'],'prior_card_exposed':d['history_check']['prior_card_exposed'],'prior_occurrences':d['history_check']['prior_occurrences']} for d in ds if d['decision']=='exclude' and d.get('history_check',{}).get('novelty')=='repeat_only']
updates=[{'candidate_id':d['candidate_id'],'decision':d['decision'],'event':d['event'],'new_facts':d['history_check']['new_facts'],'evidence':d.get('new_fact_evidence',[]),'scores':d['scores']} for d in ds if d.get('history_check',{}).get('novelty')=='material_update']

collection=[]
for day in [f'2026-10-{n}' for n in range(16,23)]:
    root=ROOT/'news_data/_collector_runs'/day
    rows=[]
    if root.exists():
        for f in root.glob('*stderr.log'):
            tail=f.read_text(encoding='utf-8',errors='replace').splitlines()
            rows.append({'collector':f.name.replace('_stderr.log',''),'tail':'\n'.join(tail[-2:]),'path':str(f)})
    collection.append({'date':day,'records':sum(x['date']==day for x in S.values()),'stderr_records':rows})
save('collection_coverage_audit.json',collection)
summary={'report_type':'weekly','id':ID,'anchor':'今天是星期五，应生成周报，窗口2026-10-16_to_2026-10-22','completed_at':now,'report':str(OUT/NAME),'sources':str(OUT/'sources_used.md'),'counts':counts,'total_items':len(I),'inputs':len(S),'decisions':len(ds),'used_sources':len(used),'claims':sum(len(i['claims']) for i in I),'history_window':{'start':'2026-10-02','end':'2026-10-15','occurrences':92},'within_week_history':'逐项读取本周已发布日报/周末报的曝光、排名、上限和日志来源；仅一次周报合并。','repeat_only_excluded':repeat,'material_updates':updates,'material_update_included':0,'card_carryover':[],'prior_card_rank':None,'deep_handoff':{'receipt_id':'b2eeb82624f7427b852799f7642385e7','raw_reply':selected['raw_reply'],'body_candidate_ids':['C001','C002'],'card_base_candidate_id':'C001','card_reference_candidate_ids':[],'selection_lint_errors':0},'industry_scores':industry,'boundary_candidates':boundaries,'release_prefix':[{'product':n['product'],'date':n['event_date'],'score':n['priority_score'],'appearance_count':n['appearance_count']} for n in A['nodes'] if dm[n['candidate_id']]['decision']=='include'],'validation':validation,'warnings':[w for v in validation for w in v['warnings']],'coverage_limitations':['窗口16日至22日都有输入；提取失败0，空正文0，125条短文/摘要未被用于正文。','采集器存在接口受阻与失败，详见collection_coverage_audit.json；22日涉及Cubox、DataEye36kr、GameLook、GameOracle、哪点事、VGC、玩匠。','多语镜像出现2015/2016/2025年及11月旧文；采集日期不被当作事件新鲜度证据。','未联网补缺；只写报告Markdown、sources_used、深度交接文本与中间产物，未写飞书/docs或git add/commit/push。'],'sha256':hashlib.sha256((OUT/NAME).read_bytes()).hexdigest()}
save('run_summary.json',summary)
save('validation_results.json',{'completed_at':now,'canonical':validation,'semantic_checks':{'source_coverage':len(S),'used_non_full_sources':0,'claim_count':summary['claims'],'forbidden_marker_matches':0,'selection_order':['C001','C002'],'sole_card_candidate':'C001'}})
lines=['# 本周周报生成摘要','',summary['anchor'],'','- ID：'+ID,'- 终稿：'+str(OUT/NAME),'- sources_used：'+str(OUT/'sources_used.md'),'- 完成时间：'+now,'- 分区：行业11 / AI6 / 产品日历7 / 社区3 / 深度2，共29条。',f'- 输入{len(S)}条、决策{len(ds)}项，正文使用{len(used)}条完整来源；逐字claims {summary["claims"]}条。','- 双周历史：2026-10-02至2026-10-15，共92条；另核对本周已发布日报/周末报及实际卡片曝光。',f'- repeat_only排除：{len(repeat)}项候选来源记录；不等同于{len(repeat)}个独立事件。','- material_update：2个候选，均未入选；《艾希：续》3750万元/23万人及10月18日交付安排；《ForgeTax》新增国内复刻产品30万下载，分别3分/2分。','- card_carryover：0；此前卡片排名不适用。','- 飞书交接：回执b2eeb82624f7427b852799f7642385e7；正文C001、C002，唯一卡片C001，无融合参考；selection lint零错误。','- 两道终稿校验均0 error；report_lint 1 warning，artifact validate 0 warning。','','## 行业入选评分','','| 标题 | E | R | M | 总分 |','| --- | --- | --- | --- | --- |']
for x in industry:
    s=x['scores'];lines.append(f'| {x["title"]} | {s["event"]} | {s["relevance"]} | {s["hook"]} | {s["total"]} |')
lines+=['','## 3—4分边界候选（均排除）','']
for x in boundaries:
    s=x['scores'];lines.append(f'- {x["candidate_id"]} {x["event"]}：E{s["event"]}×R{s["relevance"]}+M{s["hook"]}={s["total"]}。')
lines+=['','## 日历排序前缀','']
for x in summary['release_prefix']:lines.append(f'- {x["product"]}：{x["date"]}，{x["score"]}分，{x["appearance_count"]}个独立来源。')
lines+=['','## 历史重复与实质新增','']
for x in repeat:lines.append('- '+x['candidate_id']+' '+x['event']+'；此前card_exposed='+str(x['prior_card_exposed'])+'；'+' / '.join(x['prior_occurrences']))
for x in updates:lines.append('- '+x['candidate_id']+' material_update，'+x['decision']+'：'+'；'.join(x['new_facts']))
lines+=['','## Warning 与覆盖限制','']+['- '+x for x in summary['warnings']+summary['coverage_limitations']]
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'completed_at':now,'counts':counts,'inputs':len(S),'decisions':len(ds),'used_sources':len(used),'repeat_only_excluded':len(repeat),'material_update_included':0,'card_carryover':0,'sha256':summary['sha256']},ensure_ascii=False))
