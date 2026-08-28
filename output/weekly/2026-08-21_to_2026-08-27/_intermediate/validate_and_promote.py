import json, os, subprocess, sys, datetime
from pathlib import Path
P=Path(__file__).parent.resolve(); OUT=P.parent; W=Path.cwd().resolve(); ID='2026-08-21_to_2026-08-27'
assert str(OUT).startswith(str(W/'output'/'weekly'))
report=OUT/f'game_industry_weekly_{ID}.md'; sources=OUT/'sources_used.md'
inp=P/'report_inputs.jsonl'; item=P/'report_items.json'; dec=P/'selection_decisions.json'; audit=P/'release_calendar_audit.json'
data=json.loads(dec.read_text(encoding='utf-8')); nodes={x['candidate_id']:x for x in json.loads(audit.read_text(encoding='utf-8'))['nodes']}
supplement=P/'supplementary_calendar_decisions.json'
if supplement.exists():
    present={d['candidate_id'] for d in data['decisions']}
    data['decisions'] += [d for d in json.loads(supplement.read_text(encoding='utf-8')) if d['candidate_id'] not in present]
for d in data['decisions']:
    if d['section']=='release_calendar' and d['candidate_id'] in nodes:
        n=nodes[d['candidate_id']];d.update(title=n['product'],appearance_count=n['appearance_count'],signal_type=n['signal_type'])
        if n.get('audit_exclusion_reason'):d['reason']=n['audit_exclusion_reason']
dec.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report.write_text((P/'report_draft.md').read_text(encoding='utf-8'),encoding='utf-8')
env=dict(os.environ,PYTHONUTF8='1'); results=[]; success=False
try:
    commands=[
        [sys.executable,'scripts/report_artifacts.py','generate-sources','--report',str(report),'--inputs',str(inp),'--items',str(item),'--output',str(sources)],
        [sys.executable,r'C:\Users\Admin\.codex\skills\game-industry-report\scripts\report_lint.py','--report',str(report),'--sources',str(sources),'--inputs',str(inp),'--report-type','weekly'],
        [sys.executable,'scripts/report_artifacts.py','validate','--report',str(report),'--sources',str(sources),'--inputs',str(inp),'--items',str(item),'--decisions',str(dec),'--release-audit',str(audit),'--require-artifacts']
    ]
    for command in commands:
        r=subprocess.run(command,env=env,encoding='utf-8',capture_output=True)
        text=r.stdout+r.stderr; results.append({'command':command,'exit_code':r.returncode,'output':text}); print(text)
    success=all(x['exit_code']==0 for x in results)
finally:
    (P/'validation_results.json').write_text(json.dumps({'run_at':datetime.datetime.now().astimezone().isoformat(),'passed':success,'checks':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if not success:
        # Exact, already resolved report path only; never leave a failed final for publishing.
        if report.exists():report.unlink()
        print('FAILED: final Markdown removed; draft remains under _intermediate.')
sys.exit(0 if success else 1)
