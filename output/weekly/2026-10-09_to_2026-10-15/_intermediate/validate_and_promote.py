import os,sys,subprocess,json
from pathlib import Path
P=Path(__file__).parent;OUT=P.parent;ROOT=Path.cwd();ID=OUT.name
env=dict(os.environ,PYTHONUTF8='1')
final=OUT/f'game_industry_weekly_{ID}.md';draft=P/f'game_industry_weekly_{ID}.draft.md'
report=final
source=OUT/'sources_used.md'
final.write_text(draft.read_text(encoding='utf-8'),encoding='utf-8')
common=['--report',str(report),'--sources',str(source),'--inputs',str(P/'report_inputs.jsonl')]
checks=[
 [sys.executable,str(ROOT/'scripts/report_artifacts.py'),'generate-sources','--report',str(report),'--inputs',str(P/'report_inputs.jsonl'),'--items',str(P/'report_items.json'),'--output',str(source)],
 [sys.executable,r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\report_lint.py',*common,'--report-type','weekly'],
 [sys.executable,str(ROOT/'scripts/report_artifacts.py'),'validate',*common,'--items',str(P/'report_items.json'),'--decisions',str(P/'selection_decisions.json'),'--release-audit',str(P/'release_calendar_audit.json'),'--require-artifacts'],
]
logs=[];failed=False
for idx,cmd in enumerate(checks):
    r=subprocess.run(cmd,env=env,encoding='utf-8',capture_output=True)
    logs.append({'command':cmd,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    print(f'CHECK {idx} EXIT {r.returncode}\n{r.stdout}{r.stderr}',flush=True)
    if r.returncode:failed=True
(P/'validation_results.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2),encoding='utf-8')
if failed:
    # 失败时移回中间目录，不给后续发布任务留下终稿路径。
    final.replace(P/f'game_industry_weekly_{ID}.failed_validation.md')
    raise SystemExit(1)
print('Canonical final passed both validators.',flush=True)
