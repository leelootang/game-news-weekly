import json,re,os,sys,subprocess,hashlib,datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
P=Path(__file__).resolve().parent;ROOT=P.parents[3];OUT=P.parent
report=OUT/'game_industry_daily_2026-10-26.md';sources=OUT/'sources_used.md'
env=dict(os.environ,PYTHONUTF8='1')
commands=[
 [sys.executable,r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\report_lint.py','--report',str(report),'--sources',str(sources),'--inputs',str(P/'report_inputs.jsonl'),'--report-type','daily'],
 [sys.executable,str(ROOT/'scripts/report_artifacts.py'),'validate','--report',str(report),'--sources',str(sources),'--inputs',str(P/'report_inputs.jsonl'),'--items',str(P/'report_items.json'),'--decisions',str(P/'selection_decisions.json'),'--release-audit',str(P/'release_calendar_audit.json'),'--require-artifacts'],
]
def check(cmd):
 r=subprocess.run(cmd,cwd=ROOT,env=env,text=True,encoding='utf-8',capture_output=True)
 return dict(command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr,errors=[l for l in (r.stdout+r.stderr).splitlines() if l.startswith('ERROR:')],warnings=[l for l in (r.stdout+r.stderr).splitlines() if l.startswith('WARN:')])
with ThreadPoolExecutor(max_workers=2) as ex:results=list(ex.map(check,commands))
def save(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
save('validation_results.json',dict(checked_at=datetime.datetime.now().astimezone().isoformat(),canonical=True,checks=results))
if any(r['returncode'] for r in results):
 report.replace(P/'failed_canonical_report.md')
 print(json.dumps(results,ensure_ascii=False,indent=2));raise SystemExit('Validation failed; canonical final removed from publication path.')
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
items=json.loads((P/'report_items.json').read_text(encoding='utf-8'))['items'];D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))['decisions']
used={s for x in items for s in x['source_ids']};covered={s for d in D for s in d['source_ids']}
body=report.read_text(encoding='utf-8')
assert not re.search(r'Moonton|沐瞳|MLBB|Mobile Legends|决胜巅峰|card_carryover|补位|上期卡片未展示',body,re.I)
assert not (set(S)-covered)
assert all(S[s]['body_status']=='full' for s in used)
for x in items:
 for c in x['claims']:assert c['claim'] in x['title']+' '+x['body'] and c['evidence'] in S[c['source_id']]['text']
collector=json.loads((ROOT/'news_data/_collector_runs/2026-10-26/run_summary.json').read_text(encoding='utf-8'))
coverage=dict(date='2026-10-26',started_at=collector['started_at'],finished_at=collector['finished_at'],consistency_mismatches=collector['consistency_mismatches'],collectors=[{k:r.get(k) for k in ['collector','section','status','health','health_note','returncode','in_window_article_count']} for r in collector['results']])
coverage['failed']=[r for r in coverage['collectors'] if r.get('returncode') not in [0,None] or r.get('status')=='failed']
coverage['degraded']=[r for r in coverage['collectors'] if r.get('health') in ['degraded','partial','zero_articles']]
coverage['stderr_tails']={p.name:p.read_text(encoding='utf-8',errors='replace').splitlines()[-8:] for p in (ROOT/'news_data/_collector_runs/2026-10-26').glob('*stderr.log')}
coverage['steam']='No 2026-10-26 pc_rankings snapshot; do not substitute weekly or older rankings.'
save('collection_coverage_audit.json',coverage)
patterns={
 '国内移动':r'手游|小游戏|移动|iPhone|AppStore|App Store|榜',
 '国产产品与人才':r'制作人|COO|主程|国产|离职|入职|CEO',
 '市场数据':r'收入|营收|用户|万|数据|market|breakout|销量',
 '并购':r'投资|收购|交割|破产|buyout|acqui|投资',
 '平台政策':r'Steam|平台|审核|许可|Game Pass|App Store',
 '档期变动':r'发售|定档|上线|测试|取消|关闭|下架|launch|release',
 '资本组织':r'财报|资本|组织|COO|CEO|关闭|裁员|投资|收购|studio|closure',
 '海外重大':r'Xbox|Netflix|Arkane|Side|Supercell|Liquid|BioWare|EA|Steam|PC',
}
dimension={name:dict(count=len(ids),candidate_ids=ids) for name,pat in patterns.items() for ids in [[d['candidate_id'] for d in D if d['section']=='industry_news' and re.search(pat,d['event'],re.I)]]}
repeat=[d for d in D if d['section']=='industry_news' and d['history_check']['novelty']=='repeat_only']
included=[dict(candidate_id=d['candidate_id'],title=next(x['title'] for x in items if x['candidate_id']==d['candidate_id']),scores=d['scores']) for d in D if d['section']=='industry_news' and d['decision']=='include']
boundary=[{k:d[k] for k in ['candidate_id','event','scores','reason']} for d in D if d['section']=='industry_news' and d['scores']['total'] in [3,4]]
now=datetime.datetime.now().astimezone().isoformat()
summary=dict(report_type='daily',report_id='2026-10-26',anchor='今天是星期二，应生成日报，date=2026-10-26',report=str(report),sources=str(sources),completed_at=now,counts=dict(Counter(x['section'] for x in items)),input_counts=dict(Counter(x['section'] for x in S.values())),input_total=len(S),decisions=len(D),input_coverage=len(covered),used_sources=len(used),dimension_coverage=dimension,scoring_version='subject_genre_v2',industry_included=included,boundary_candidates=boundary,history_window=dict(start='2026-10-12',end='2026-10-25',occurrences=106),repeat_only_excluded=[{k:d[k] for k in ['candidate_id','event','history_check','history_evidence']} for d in repeat],material_update_included=[],card_carryover_included=[],card_carryover_prior_rank=None,deep_handoff='Tuesday daily; no Friday receipt/selection consumption. One original daily deep observation with 3 card insights.',calendar=dict(nodes=71,included=['Sign：碎冠篇'],priority=9,independent_sources=2,lookahead_end='2026-10-27',reverse_scan_inputs=224,corrections='Blue Star ownership/previous schedule; Infinite date; Sign punctuation; old launch false positives; Steam preview whole-body recall; preload single-source; Emberville Oct27 schedule previously published Sep23; quarter dates retained as quarter not fake day.'),checks=results,collector_failed=[r['collector'] for r in coverage['failed']],collector_health=coverage['degraded'],steam=coverage['steam'],warnings=[w for r in results for w in r['warnings']],no_network_backfill=True,report_sha256=hashlib.sha256(report.read_bytes()).hexdigest())
save('run_summary.json',summary)
lines=['# 日报运行摘要｜2026-10-26','',summary['anchor'],'',f'- 完成时间：{now}',f'- 终稿：{report}',f'- 来源：{sources}','- 分区条数：行业1 / AI3 / 产品日历1 / 社区2 / 深度1。','- 输入260条；332项决策覆盖260/260来源；终稿10条来源均为full。','- 行业入选：雷霆游戏投资上海火因山风，E3/R3/M0=9。','- 双周历史：2026-10-12至2026-10-25，106条，逐条读取曝光状态/排名/上限/来源。',f'- repeat_only排除：{len(repeat)}张独立候选；M98、王者IP三产品榜单、京东游戏实体、光子首曝、Metacore交割、Liquid Swords破产。','- material_update入选0，新增事实无；card_carryover入选0，此前卡片排名不适用。匹配历史的实际卡片排名如下：']
for d in repeat:
 lines.append('- '+d['event']+'：'+'；'.join(f"{o['report_window']['start']}_to_{o['report_window']['end']} / rank={o['card_rank']} / limit={o['card_limit']} / exposed={o['card_exposed']} / {o['card_exposure_source']}" for o in d['history_evidence']))
lines+=['','## 3–4分边界候选','']+[f"- {d['candidate_id']} {d['event']}：E{d['scores']['event']}/R{d['scores']['relevance']}/M{d['scores']['hook']}={d['scores']['total']}；{d['reason']}" for d in boundary]
lines+=['','- 产品日历71节点，唯一多源合格前缀Sign，优先级3×3+0=9；无行业跨栏排除。','- 深度交接：周二不消费周五飞书回执；日报原创深度1条，3条卡片洞察。配置newsletter两条分别为付费预览及奖项征集，均留审计排除。','- 两道正式路径校验均0 error；report_lint 1 warning（15条short/snippet输入，正文未使用），artifact validate 0 warning。','- 采集器失败：'+', '.join(summary['collector_failed'])+'。详细健康及空源见collection_coverage_audit.json。','- 缺26日Steam当日快照，未用旧榜替代；仅使用本地采集，不联网补缺。','- 未改news_data、docs；未生成HTML；未执行飞书操作或git add/commit/push。',f"- SHA256：{summary['report_sha256']}"]
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(dict(completed_at=now,counts=summary['counts'],checks=[dict(returncode=r['returncode'],errors=len(r['errors']),warnings=r['warnings']) for r in results],collector_failed=summary['collector_failed'],sha256=summary['report_sha256']),ensure_ascii=False,indent=2))
