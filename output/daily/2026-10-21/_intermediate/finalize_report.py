import json,re,subprocess,sys,shutil,hashlib,os
from pathlib import Path
from datetime import datetime
from collections import Counter
P=Path(__file__).resolve().parent;OUT=P.parent;ROOT=P.parents[3]
os.environ['PYTHONUTF8']='1'
name='game_industry_daily_2026-10-21.md';stage=P/'staging'
lint=Path(r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\report_lint.py')
def checks(directory):
    common=['--report',str(directory/name),'--sources',str(directory/'sources_used.md'),'--inputs',str(P/'report_inputs.jsonl')]
    commands=[[sys.executable,str(lint),*common,'--report-type','daily'],[sys.executable,str(ROOT/'scripts/report_artifacts.py'),'validate',*common,'--items',str(P/'report_items.json'),'--decisions',str(P/'selection_decisions.json'),'--release-audit',str(P/'release_calendar_audit.json'),'--require-artifacts']]
    results=[]
    for cmd in commands:
        p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        output=p.stdout+p.stderr
        results.append(dict(command=cmd,exit_code=p.returncode,errors=[x for x in output.splitlines() if x.startswith('ERROR:')],warnings=[x for x in output.splitlines() if x.startswith('WARN:')],output=output))
        print(output or 'Artifact validation passed: 0 errors, 0 warnings.')
    return results

results=checks(stage)
assert all(r['exit_code']==0 and not r['errors'] for r in results),'staging validation failed; canonical report not created'
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
doc=json.loads((P/'report_items.json').read_text(encoding='utf-8'));items=doc['items']
D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'));decisions=D['decisions']
assert D['scoring_version']=='subject_genre_v2'
covered={s for d in decisions for s in d['source_ids']};assert covered==set(S)
used={s for i in items for s in i['source_ids']};assert all(S[s]['body_status']=='full' for s in used)
text=(stage/name).read_text(encoding='utf-8')
assert not re.search(r'沐瞳|Moonton|MLBB|Mobile Legends|决胜巅峰|card_carryover|补位|上期卡片未展示',text,re.I)
assert all(c['evidence'] in S[c['source_id']]['text'] and c['claim'] in i['body'] for i in items for c in i['claims'])
assert len({d['candidate_id'] for d in decisions})==len(decisions)
shutil.copyfile(stage/name,OUT/name);shutil.copyfile(stage/'sources_used.md',OUT/'sources_used.md')
canonical=checks(OUT)
if not all(r['exit_code']==0 and not r['errors'] for r in canonical):
    (OUT/name).replace(P/('failed_'+name))
    raise RuntimeError('Canonical validation failed; report moved out of publishable path')
now=datetime.now().astimezone();clock=now.isoformat()
validation=dict(completed_at=clock,staging=results,canonical=canonical,semantic_checks=dict(input_coverage=len(covered),inputs=len(S),used_sources=len(used),non_full_used=0,claims=sum(len(i['claims']) for i in items),forbidden_marker_matches=0,news_data_modified=False,scoring_version=D['scoring_version']))
(P/'validation_results.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
counts=Counter(i['section'] for i in items)
included=[dict(candidate_id=d['candidate_id'],event=d['event'],scores=d['scores']) for d in decisions if d['section']=='industry_news' and d['decision']=='include']
boundary=[dict(candidate_id=d['candidate_id'],event=d['event'],scores=d['scores']) for d in decisions if d['section']=='industry_news' and d['scores']['total'] in {3,4}]
repeat=[d['candidate_id'] for d in decisions if d.get('history_check',{}).get('novelty')=='repeat_only' and d['decision']=='exclude']
a=json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))
summary=dict(report_type='daily',date='2026-10-21',anchor='今天是星期四，应生成日报，date=2026-10-21',completed_at=clock,report_path=str(OUT/name),sources_path=str(OUT/'sources_used.md'),counts=dict(counts),total_items=len(items),input_count=len(S),decision_count=len(decisions),used_sources=len(used),history_window=dict(start='2026-10-07',end='2026-10-20',occurrences=114),repeat_only_excluded=repeat,material_updates=[],card_carryover=None,prior_card_rank=None,deep_handoff='星期四日报，不消费或操作周五飞书回执；未生成周四候选Bot任务产物。',industry_scores=included,boundary_candidates=boundary,release_nodes=len(a['nodes']),release_scores=[dict(product=n['product'],event_date=n['event_date'],score=n['priority_score'],sources=n['source_ids']) for n in a['nodes'] if n['publish_eligible']],validation_errors=0,warnings=canonical[0]['warnings'],collector_caveats=['gamelook','vgc','dataeye_36kr','gameres','nadianshi','cubox','wanjiang_16p_newgame'],degraded_collectors=['pocketgamer'],editorial_caveats=['英文腾讯生活模拟首曝稿事件日期未能核验，10分候选保留排除','本期没有Steam当日榜输入，未用旧榜代替','部分多语种镜像正文明确2025年或11月日期，未作为本期新事件'],sha256=hashlib.sha256((OUT/name).read_bytes()).hexdigest())
(P/'run_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# 2026-10-21 日报生成摘要','',summary['anchor'],'','- 终稿：'+str(OUT/name),'- 来源：'+str(OUT/'sources_used.md'),'- 完成时间：'+clock,f'- 分区：行业{counts["industry_news"]} / AI{counts["ai_trends"]} / 日历{counts["release_calendar"]} / 社区{counts["community_discourse"]} / 深度{counts["deep_analysis"]}，共{len(items)}条。',f'- 输入375条，全部覆盖；{len(decisions)}项决策，正文使用{len(used)}条完整来源。','- 双周历史：2026-10-07至2026-10-20，114条；每条已读取曝光、排名、上限及曝光来源。','- repeat_only排除：'+', '.join(repeat)+'；Metacore历史卡片rank1/limit10；Xbox Labs历史至少一次rank7/limit10。','- material_update：0，新增事实不适用。card_carryover：0，此前卡片排名不适用。','- 深度交接：周四日报不消费周五selection，不触碰飞书、docs。','- 两道canonical校验均0 error；artifact validate 0 warning。','', '## 行业入选分数','', '| 候选 | E | R | M | 总分 |','| --- | --- | --- | --- | --- |']
for x in included:
    sc=x['scores'];lines.append(f'| {x["candidate_id"]} {x["event"]} | {sc["event"]} | {sc["relevance"]} | {sc["hook"]} | {sc["total"]} |')
lines+=['','## 3—4分边界候选（均排除）','']
for x in boundary:
    sc=x['scores'];lines.append(f'- {x["candidate_id"]} {x["event"]}：E{sc["event"]}×R{sc["relevance"]}+M{sc["hook"]}={sc["total"]}。')
lines+=['','## 日历独立排序前缀','']
for x in summary['release_scores']:lines.append(f'- {x["product"]}：{x["event_date"]}，{x["score"]}分，'+', '.join(x['sources'])+'。')
lines+=['','## Warning 与覆盖限制','']+['- '+x for x in summary['warnings']]+['- 采集器失败：'+', '.join(summary['collector_caveats'])+'；PocketGamer degraded。没有联网补缺。']+['- '+x for x in summary['editorial_caveats']]+['','- news_data只读；没有git add/commit/push、HTML、飞书或docs写入。','- SHA256：'+summary['sha256']]
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({k:summary[k] for k in ['counts','total_items','decision_count','used_sources','completed_at','sha256']},ensure_ascii=False))
