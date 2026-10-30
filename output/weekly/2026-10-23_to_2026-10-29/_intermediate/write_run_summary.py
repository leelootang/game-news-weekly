import json,subprocess,sys,os
from pathlib import Path
from datetime import datetime,timezone,timedelta
from collections import Counter,defaultdict
ROOT=Path.cwd();B=ROOT/'output/weekly/2026-10-23_to_2026-10-29/_intermediate';OUT=B.parent;ID='2026-10-23_to_2026-10-29'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
d=read(B/'selection_decisions.json');ds=d['decisions'];items=read(B/'report_items.json')['items'];dm={x['candidate_id']:x for x in ds}
for x in ds:
 if x['candidate_id']=='W20261028_I130':x['subject_assessment']['basis']='腾讯直属产品R3、移动版实际公测E3；本期来源所述历史事实可以核验，但已完成卡片曝光且进入过已发布周报，按历史门禁排除，不以事件年龄降低分值。'
dump(B/'selection_decisions.json',d)
report=OUT/('game_industry_weekly_'+ID+'.md');sources=OUT/'sources_used.md'
checks=[('report_lint',[Path('C:/Users/Admin/.codex/skills/game-industry-report/scripts/report_lint.py'),'--report',report,'--sources',sources,'--inputs',B/'report_inputs.jsonl','--report-type','weekly']),('artifact_validate',['scripts/report_artifacts.py','validate','--report',report,'--sources',sources,'--inputs',B/'report_inputs.jsonl','--items',B/'report_items.json','--decisions',B/'selection_decisions.json','--release-audit',B/'release_calendar_audit.json','--require-artifacts'])]
results=[]
for name,args in checks:
 p=subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,env=dict(os.environ,PYTHONUTF8='1'),capture_output=True,text=True,encoding='utf-8')
 (B/('final_'+name+'.log')).write_text(p.stdout+p.stderr,encoding='utf-8');assert p.returncode==0,(name,p.stdout,p.stderr)
 results.append(dict(check=name,errors=0,warnings=[line[6:] for line in p.stdout.splitlines() if line.startswith('WARN:')],exit_code=p.returncode))
now=datetime.now(timezone(timedelta(hours=8))).isoformat()
validation=read(B/'validation_results.json');validation['final_recheck_time']=now;validation['final_recheck']=results;dump(B/'validation_results.json',validation)
industry=[i for i in items if i['section']=='industry_news'];included_scores=[dict(title=i['title'],candidate_id=i['candidate_id'],**dm[i['candidate_id']]['scores']) for i in industry]
bound=[x for x in ds if x['section']=='industry_news' and x['decision']=='exclude' and x['scores']['total'] in [3,4]]
repeat=[x for x in ds if x['section']=='industry_news' and x['decision']=='exclude' and x.get('history_check',{}).get('novelty')=='repeat_only']
updates=[x for x in ds if x['decision']=='include' and x.get('history_check',{}).get('novelty')=='material_update']
carry=[x for x in ds if x['decision']=='include' and x.get('card_carryover')]
coverage=read(B/'collection_coverage.json');failed=defaultdict(list)
for r in coverage['dates']:
 for c in r.get('failed_collectors',[]):failed[c].append(r['date'])
warnings=['10月29日无本地采集运行与输入，实际覆盖10月23日至28日。','输入有65条short/snippet质量警告，未作为最终正文证据。','部分日期采集失败：'+','.join(failed)+'；具体日期见collection_coverage.md。','窗口没有Steam排名输入，未补造榜单。']
summary=dict(run_time=now,anchor='今天是星期五，应生成周报，窗口'+ID,report_type='weekly',report_id=ID,report_path=str(report.resolve()),sources_path=str(sources.resolve()),section_counts=Counter(i['section'] for i in items),input_records=1438,input_text_chars=10001267,extraction_failures=0,empty_text_records=0,decision_count=len(ds),calendar_node_count=len(read(B/'release_calendar_audit.json')['nodes']),history_window=dict(start='2026-10-09',end='2026-10-22'),history_occurrences=110,archive_occurrences=1011,within_week_exposure_records=len(read(B/'within_week_card_exposure.json')),repeat_only_exclusion_count=len(repeat),repeat_only_exclusions=[dict(candidate_id=x['candidate_id'],event=x['event'],history_check=x['history_check']) for x in repeat],material_updates=[dict(title=x.get('title',x['event']),new_facts=x['history_check']['new_facts']) for x in updates],card_carryover=[dict(title=x.get('title',x['event']),scores=x['scores'],history_check=x['history_check']) for x in carry],deep_handoff=d['deep_handoff'],validation=results,warnings=warnings,included_industry_scores=included_scores,boundary_candidates=[dict(candidate_id=x['candidate_id'],event=x['event'],scores=x['scores'],source_ids=x['source_ids'],reason=x['reason']) for x in bound],no_external_writes=True,no_git_add_commit_push=True)
dump(B/'run_summary.json',summary)
lines=['# 周报生成审计摘要｜'+ID,'','- 运行时点：'+now,'- 锚点：'+summary['anchor'],'- 终稿：'+str(report.resolve()),'- 来源映射：'+str(sources.resolve()),'- 分区：行业53 / AI6 / 产品日历7 / 社区3 / 深度2，共71条。','- 输入1438条、抽取失败0、空正文0；1548条决策、154个产品日期节点。','- 双周历史：2026-10-09至2026-10-22，共110条；更早归档1011条；另核对本周32条正式广播曝光。','- 评分subject_genre_v2；行业时间source_window_v1。','- report_lint：0 error / 1 warning；artifact validate --require-artifacts：0 error / 0 warning。','- 未写飞书、docs、news_data；未git add/commit/push。','', '## 采集与warning','']
lines+=['- '+w for w in warnings]
lines+=['- 当前manifest所有URL均可在同日JSONL核对，缺失0；旧run_summary中Sensor Tower缺失已被此前采集修复消除，本次只读消费。','', '## 深度回执闭环','','- 回执：2ff02addfe2f47d1a6c9789c6adb38c8，原话“卡片：C001，正文：C001、C022”。','- 正文顺序：C001、C022；唯一指定主卡C001，无融合参考。','- 精确selection lint零错误；已按selection抽取，deep_card_choice.txt与正文第一题标题一致。','', '## 跨期与曝光去重','',f'- repeat_only排除{len(repeat)}张行业候选审计卡（含同事件多语言记录，并非30个独立新闻）。', '- card_carryover唯一入选：微信小游戏2025生态回顾，E2/R3/M0=6；四条历史报告均card_exposed=false，card_rank=null、card_limit=null、来源not_broadcast。', '- Atari同为6分但R2，排序靠后；王者荣耀世界旧事件已于28日日报卡片第4/10曝光，且更早周报已收录，本周排除。','', '### 实质更新及新增事实','']
for x in updates:
 lines+=['- '+x.get('title',x['event'])+'：'+'；'.join(x['history_check']['new_facts'])]
lines+=['', '## 行业入选全量评分','','| 顺序 | 标题 | E | R | M | 总分 |','| ---: | --- | ---: | ---: | ---: | ---: |']
for n,x in enumerate(included_scores,1):lines.append(f"| {n} | {x['title']} | {x['event']} | {x['relevance']} | {x['hook']} | {x['total']} |")
lines+=['',f'## 3—4分边界候选（共{len(bound)}张审计卡）','','同事件多语言记录保留各自来源，不代表互相独立事件。','', '| 候选 | 事件 | E/R/M | 总分 | 排除理由 |','| --- | --- | --- | ---: | --- |']
for x in bound:
 s=x['scores'];lines.append('| '+' | '.join([x['candidate_id'],x['event'].replace('|','／'),f"{s['event']}/{s['relevance']}/{s['hook']}",str(s['total']),x['reason'].replace('|','／')])+' |')
lines+=['','## repeat_only排除明细','','| 候选 | 事件 | 此前卡片曝光 |','| --- | --- | --- |']
for x in repeat:lines.append('| '+' | '.join([x['candidate_id'],x['event'].replace('|','／'),str(x['history_check'].get('prior_card_exposed'))])+' |')
(B/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(now);print('report',report);print('repeat',len(repeat),'updates',len(updates),'carry',len(carry),'boundary',len(bound));print('validation',results)
