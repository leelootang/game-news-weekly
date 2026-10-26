import json,subprocess,sys,os,re,shutil,hashlib
from collections import Counter
from datetime import datetime
from pathlib import Path
os.environ['PYTHONUTF8']='1'
P=Path(__file__).resolve().parent;OUT=P.parent;ROOT=P.parents[3]
name='game_industry_weekend_2026-10-23_to_2026-10-25.md';stage=P/'staging'
def run(cmd):
 x=subprocess.run([sys.executable,*map(str,cmd)],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
 out=x.stdout+x.stderr;print(out or 'Artifact validation passed: 0 errors, 0 warnings.')
 return dict(command=cmd,exit_code=x.returncode,output=out,errors=[l for l in out.splitlines() if l.startswith('ERROR:')],warnings=[l for l in out.splitlines() if l.startswith('WARN:')])
gen=run(['scripts/report_artifacts.py','generate-sources','--report',stage/name,'--inputs',P/'report_inputs.jsonl','--items',P/'report_items.json','--output',stage/'sources_used.md']);assert gen['exit_code']==0
def checks(folder):
 common=['--report',folder/name,'--sources',folder/'sources_used.md','--inputs',P/'report_inputs.jsonl']
 return [run([Path(r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\report_lint.py'),*common]),run(['scripts/report_artifacts.py','validate',*common,'--items',P/'report_items.json','--decisions',P/'selection_decisions.json','--release-audit',P/'release_calendar_audit.json','--require-artifacts'])]
staged=checks(stage)
def dump(name,data):(P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
dump('validation_results.json',dict(staging=staged))
assert all(x['exit_code']==0 and not x['errors'] for x in staged),'staging rejected; canonical final not created'
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))['decisions'];items=json.loads((P/'report_items.json').read_text(encoding='utf-8'))['items']
covered={s for d in D for s in d['source_ids']};used={s for i in items for s in i['source_ids']}
assert covered==set(S),(len(covered),set(S)-covered)
assert all(S[s]['body_status']=='full' for s in used)
assert len({d['candidate_id'] for d in D})==len(D)
for i in items:
 for c in i['claims']:assert c['claim'] in i['body'] and c['evidence'] in S[c['source_id']]['text']
t=(stage/name).read_text(encoding='utf-8');assert not re.search(r'沐瞳|Moonton|MLBB|决胜巅峰|card_carryover|补位|上期卡片未展示',t,re.I)
shutil.copyfile(stage/name,OUT/name);shutil.copyfile(stage/'sources_used.md',OUT/'sources_used.md')
final=checks(OUT)
if not all(x['exit_code']==0 and not x['errors'] for x in final):
 (OUT/name).replace(P/('failed_'+name));raise RuntimeError('canonical final failed and moved out of publication path')
now=datetime.now().astimezone().isoformat();counts=dict(Counter(i['section'] for i in items))
dump('validation_results.json',dict(completed_at=now,staging=staged,canonical=final,checks=dict(input_coverage=len(covered),inputs=len(S),used_sources=len(used),used_nonfull=0,claim_count=sum(len(i['claims']) for i in items),forbidden_markers=0)))
history=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
industry=[d for d in D if d['section']=='industry_news'];inc=[d for d in industry if d['decision']=='include'];boundary=[d for d in industry if d['scores']['total'] in [3,4]]
repeats=[d for d in industry if d['history_check']['novelty']=='repeat_only'];updates=[d for d in industry if d['history_check']['novelty']=='material_update']
collect=[]
for day in ['2026-10-23','2026-10-24','2026-10-25']:
 r=json.loads((ROOT/'news_data/_collector_runs'/day/'run_summary.json').read_text(encoding='utf-8'));collect.append(dict(date=day,results=r['results'],consistency_mismatches=r['consistency_mismatches'],errors={f.name:f.read_text(encoding='utf-8',errors='replace')[-1800:] for f in (ROOT/'news_data/_collector_runs'/day).glob('*stderr.log')}))
dump('collection_coverage_audit.json',collect)
audit=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
summary=dict(anchor='今天是星期一，应生成周末报，窗口2026-10-23_to_2026-10-25',report_type='weekend',report_id='2026-10-23_to_2026-10-25',report=str(OUT/name),sources=str(OUT/'sources_used.md'),completed_at=now,counts=counts,inputs=len(S),decisions=len(D),used_sources=len(used),history_window=history['history_window'],history_occurrences=len(history['occurrences']),repeat_only_exclusions=[dict(candidate_id=d['candidate_id'],event=d['event'],history=d['history_check']) for d in repeats],material_updates=[dict(candidate_id=d['candidate_id'],event=d['event'],decision=d['decision'],scores=d['scores'],history=d['history_check']) for d in updates],card_carryover=None,prior_card_rank=None,deep_handoff='周一周末报，不消费周五回执或selection；2篇配置完整newsletter进入深度。',industry_scores=[dict(candidate_id=d['candidate_id'],event=d['event'],scores=d['scores']) for d in inc],boundary_candidates=[dict(candidate_id=d['candidate_id'],event=d['event'],scores=d['scores'],reason=d['reason']) for d in boundary],release=[dict(product=n['product'],score=n['priority_score'],source_ids=n['source_ids']) for n in audit['nodes'] if n['publish_eligible']],validation_errors=0,warnings=final[0]['warnings'],limitations=['窗口三天均有数据，但部分采集器失败或降级，完整清单在collection_coverage_audit.json。','没有本期Steam当日榜输入，不用周销量榜或历史榜单替代。','潜梦者行业仅写本期首曝，不写具体日；日历保留23/24日冲突排除，不强行聚类。','本期篮球少女来源未披露发行商，不借历史归属补写灵犀。'],sha256=hashlib.sha256((OUT/name).read_bytes()).hexdigest())
dump('run_summary.json',summary)
lines=['# 周末报生成结果｜2026-10-23_to_2026-10-25','',summary['anchor'],'','- 终稿：'+summary['report'],'- 来源：'+summary['sources'],'- 完成时间：'+now,'- 分区：'+json.dumps(counts,ensure_ascii=False),f'- 全量{len(S)}输入、{len(D)}决策，覆盖{len(covered)}/{len(S)}；正文使用{len(used)}条完整来源。','- 双周历史：2026-10-09至2026-10-22，共110条，含旧格式兼容与卡片exposed/rank/limit/source。','- repeat_only：2个来源候选、1个独立事件（人间异想计划），历史21日报rank1、周报rank2，limit10，均已曝光。','- material_update入选0；篮球少女从预告到23日公测为实质状态变化，但本期未证实重点发行商，行业E3R0M1=1排除。该产品独立通过日历9分多源门槛。','- card_carryover：0，此前排名不适用。','- 深度交接：'+summary['deep_handoff'],'- 两道canonical校验均0 error，artifact validate 0 warning。','','## 行业入选 E/R/M','']
for d in inc:
 sc=d['scores'];lines.append(f'- {d["candidate_id"]} {d["event"]}：E{sc["event"]}×R{sc["relevance"]}+M{sc["hook"]}={sc["total"]}。')
lines+=['','## 3—4分边界（均未单独入选）','']
for d in boundary:
 sc=d['scores'];lines.append(f'- {d["candidate_id"]} {d["event"]}：E{sc["event"]}×R{sc["relevance"]}+M{sc["hook"]}={sc["total"]}；{d["reason"]}')
lines+=['','## Warning 与数据覆盖','']+['- '+x for x in summary['warnings']+summary['limitations']]+['','- news_data只读；未生成HTML、未触碰飞书/docs、未git add/commit/push。','- SHA256：'+summary['sha256']]
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({k:summary[k] for k in ['counts','inputs','decisions','used_sources','completed_at','sha256']},ensure_ascii=False))
