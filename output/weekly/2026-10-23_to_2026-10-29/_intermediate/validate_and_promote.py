import json,os,sys,subprocess,shutil
from pathlib import Path
from datetime import datetime,timezone,timedelta
ROOT=Path.cwd();B=ROOT/'output/weekly/2026-10-23_to_2026-10-29/_intermediate';OUT=B.parent
NAME='game_industry_weekly_2026-10-23_to_2026-10-29.md';stage=B/'draft'
env=dict(os.environ,PYTHONUTF8='1');results=[]
def run(label,args):
 p=subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8')
 (B/(label+'.log')).write_text(p.stdout+p.stderr,encoding='utf-8')
 r=dict(check=label,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr,command=[str(x) for x in args]);results.append(r)
 if p.returncode:raise RuntimeError(label+' failed; final not promoted')
def validate(where,label):
 report=where/NAME;sources=where/'sources_used.md'
 run(label+'_sources',['scripts/report_artifacts.py','generate-sources','--report',report,'--inputs',B/'report_inputs.jsonl','--items',B/'report_items.json','--output',sources])
 run(label+'_report_lint',[Path('C:/Users/Admin/.codex/skills/game-industry-report/scripts/report_lint.py'),'--report',report,'--sources',sources,'--inputs',B/'report_inputs.jsonl','--report-type','weekly'])
 run(label+'_artifact_validate',['scripts/report_artifacts.py','validate','--report',report,'--sources',sources,'--inputs',B/'report_inputs.jsonl','--items',B/'report_items.json','--decisions',B/'selection_decisions.json','--release-audit',B/'release_calendar_audit.json','--require-artifacts'])
validate(stage,'staged')
target=OUT/NAME;assert target.resolve().is_relative_to(ROOT.resolve());assert not target.exists()
shutil.copy2(stage/NAME,target)
try:validate(OUT,'final')
except Exception:
 target.unlink(missing_ok=True)
 raise
finally:
 (B/'validation_results.json').write_text(json.dumps(dict(run_time=datetime.now(timezone(timedelta(hours=8))).isoformat(),results=results),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# 不保留第二份固定命名的报告，防止后续扫描把草稿重复视为终稿。
(stage/NAME).unlink();(stage/'sources_used.md').unlink(missing_ok=True)
print('PROMOTED',target)
for r in results:
 if 'sources' not in r['check']:print(r['check'],r['exit_code'],r['stdout'].strip())
