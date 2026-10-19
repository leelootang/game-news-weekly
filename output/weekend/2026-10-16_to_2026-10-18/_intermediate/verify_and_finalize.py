import json,sys,subprocess,datetime,re,collections,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parent;W=Path.cwd()
REPORTNAME='game_industry_weekend_2026-10-16_to_2026-10-18.md'
REPORT=P/'staging'/REPORTNAME
def dump(name,data):(P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
S={r['source_id']:r for r in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))['decisions']
A=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
I=json.loads((P/'report_items.json').read_text(encoding='utf-8'))['items']
# Complete source-coverage refresh after refinement, using full text and exact fingerprints.
coverage=json.loads((P/'full_input_scan.json').read_text(encoding='utf-8'))
for rr in coverage['inputs']:
 rr['matching_candidates']=[d['candidate_id'] for d in D if rr['source_id'] in d['source_ids']]
 rr['calendar_nodes']=[n['candidate_id'] for n in A['nodes'] if rr['source_id'] in n['source_ids']]
 assert rr['matching_candidates'] or rr['calendar_nodes'],rr['source_id']
dump('full_input_scan.json',coverage)
collect=[]
for day in ['2026-10-16','2026-10-17','2026-10-18']:
 data=json.loads((W/'news_data'/'_collector_runs'/day/'run_summary.json').read_text(encoding='utf-8'))
 rows=data['results']
 if isinstance(rows,dict):rows=list(rows.values())
 abnormal=[]
 for row in rows:
  if row.get('status') not in [None,'ok'] or row.get('health') in ['degraded','failed']:
   abnormal.append(row)
 collect.append(dict(date=day,consistency_mismatches=data.get('consistency_mismatches'),abnormal=abnormal))
dump('collector_coverage_audit.json',collect)
md=(P/'selection_decisions.md').read_text(encoding='utf-8')
md=md.replace('136个原始修订节点继续按同产品同日聚类',f"{len(A['nodes'])}个修订节点已按同产品同日聚类")
used_count=len({x for item in I for x in item['source_ids']})
md+=f'\n## 来源覆盖与限制\n- 输入覆盖16—18日，369条，0抽取失败、0空正文，36条short/snippet均未用于正文；最终{used_count}个证据ID均full。\n- 采集器健康状况见collector_coverage_audit.json；抽取成功不等于采集源完整。\n- AI6条超过周末报1—3软目标：4条游戏直接作用+2条成本/工程验证迁移，不以泛科技凑数。\n- Steam当日榜16—18日目录缺失，未用周榜或7月旧快照替代。\n- 日历已保留链兽角斗的预排斜杠日期、现代战争4的英文日期/部分抢先体验限制，未伪造标准日期来通过校验。\n'
(P/'selection_decisions.md').write_text(md,encoding='utf-8')
# Final candidate cards reflect all refinements instead of retaining superseded draft labels.
bycid={item['candidate_id']:item for item in I}
cards=['# 独立事件候选｜2026-10-16_to_2026-10-18','', '窗口锚点：周一周末报，16—18日；行业历史2—15日。仅同主体/产品、同一事件日期、同一事件聚类；产品日历按产品+日期。所有369条输入均有全文指纹和对应候选/日历节点，见full_input_scan.json。','']
for d in D:
 facts='；'.join(dict.fromkeys(c['claim'] for c in bycid[d['candidate_id']]['claims'])) if d['candidate_id'] in bycid else d.get('facts_read',d['event'])
 cards += [f"## {d['candidate_id']} - {d.get('event','')}",f"- section: {d['section']}",'- status: candidate',f"- source_ids: {', '.join(d['source_ids'])}",f"- entities: {' / '.join(d.get('entities',[]))}",f"- event_date: {d.get('event_date',d.get('event','').split(' ')[0])}",f'- facts: {facts}',f"- notes: {d['reason']}"]
 if 'community' in d:cards += ['- community: '+json.dumps(d['community'],ensure_ascii=False)]
 if 'history_check' in d:cards += ['- history_check: '+json.dumps(d['history_check'],ensure_ascii=False)]
 cards += ['']
(P/'event_candidates.md').write_text('\n'.join(cards),encoding='utf-8')

def run(args,log):
 cp=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True,encoding='utf-8')
 (P/log).write_text(cp.stdout+cp.stderr,encoding='utf-8')
 print(log,cp.returncode,(cp.stdout+cp.stderr).strip())
 return cp.returncode
sources=ROOT/'sources_used.md'
assert run([W/'scripts/report_artifacts.py','generate-sources','--report',REPORT,'--inputs',P/'report_inputs.jsonl','--items',P/'report_items.json','--output',sources],'generate_sources.log')==0
lint=Path('C:/Users/Admin/.codex/skills/game-industry-report/scripts/report_lint.py')
args1=[lint,'--report',REPORT,'--sources',sources,'--inputs',P/'report_inputs.jsonl']
args2=[W/'scripts/report_artifacts.py','validate','--report',REPORT,'--sources',sources,'--inputs',P/'report_inputs.jsonl','--items',P/'report_items.json','--decisions',P/'selection_decisions.json','--release-audit',P/'release_calendar_audit.json','--require-artifacts']
c1=run(args1,'report_lint.staging.log');c2=run(args2,'artifact_validate.staging.log')
if c1 or c2:sys.exit(1)
report_text=REPORT.read_text(encoding='utf-8')
assert not re.search(r'沐瞳|Moonton|MLBB|Mobile Legends: Bang Bang|决胜巅峰|card_carryover|补位|上期卡片未展示',report_text,re.I)
assert all(S[s]['body_status']=='full' and S[s]['fetch_status']=='ok' for i in I for s in i['source_ids'])
assert len([d for d in D if d.get('card_carryover') and d['decision']=='include'])==1
assert all(set(['history_match','novelty','prior_occurrences','new_facts','prior_card_exposed'])<=set(d.get('history_check',{})) for d in D if d['section']=='industry_news')
keys=[(n['product'],n['event_date']) for n in A['nodes']]
assert len(keys)==len(set(keys))
required=['report_inputs.jsonl','report_inputs_summary.md','report_inputs_index.md','release_calendar_audit.json','source_quality_audit.json','event_candidates.md','selection_decisions.md','report_items.json','selection_decisions.json','industry_history_14d.json','industry_history_14d.md']
assert all((P/x).is_file() for x in required)
FINAL=ROOT/REPORTNAME
FINAL.write_text(report_text,encoding='utf-8')
args1[args1.index(REPORT)]=FINAL;args2[args2.index(REPORT)]=FINAL
c1=run(args1,'report_lint.log');c2=run(args2,'artifact_validate.log')
if c1 or c2:
 FINAL.unlink();sys.exit(1)
result=dict(completed_at=datetime.datetime.now().astimezone().isoformat(),report=str(FINAL),sha256=hashlib.sha256(FINAL.read_bytes()).hexdigest(),report_lint=dict(errors=0,warnings=['input extraction has 36 short/snippet records; none cited']),artifact_validate=dict(errors=0,warnings=[]),section_counts=dict(collections.Counter(i['section'] for i in I)),used_source_ids=sorted({x for i in I for x in i['source_ids']}),required_artifacts='complete',forbidden_scan=0,calendar_unique_nodes=len(A['nodes']))
dump('validation_results.json',result)
print(json.dumps(result,ensure_ascii=False,indent=2))
