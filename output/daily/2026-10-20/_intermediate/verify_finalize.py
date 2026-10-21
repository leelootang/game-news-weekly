import json, os, subprocess, sys, shutil, hashlib
from pathlib import Path
from datetime import datetime,timezone,timedelta
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
NAME='game_industry_daily_2026-10-20.md'
env=dict(os.environ,PYTHONUTF8='1')
skill=Path('C:/Users/Admin/.codex/skills/game-industry-report/scripts/report_lint.py')
results={}
def run(key,args):
    cp=subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8')
    (P/(key+'.log')).write_text(cp.stdout+cp.stderr,encoding='utf-8')
    results[key]=dict(exit_code=cp.returncode,errors=[s for s in cp.stdout.splitlines() if s.startswith('ERROR:')],warnings=[s for s in cp.stdout.splitlines() if s.startswith('WARN:')])
    print(key,cp.returncode,cp.stdout.strip())
    if cp.returncode:
        (P/'validation_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
        raise RuntimeError(key+' failed; canonical final not accepted')
def checks(folder,suffix):
    common=['--report',folder/NAME,'--sources',folder/'sources_used.md','--inputs',P/'report_inputs.jsonl']
    run('report_lint'+suffix,[skill,*common,'--report-type','daily'])
    run('artifact_validate'+suffix,[ROOT/'scripts/report_artifacts.py','validate',*common,'--items',P/'report_items.json','--decisions',P/'selection_decisions.json','--release-audit',P/'release_calendar_audit.json','--require-artifacts'])
stage=P/'staging'
run('generate_sources',[ROOT/'scripts/report_artifacts.py','generate-sources','--report',stage/NAME,'--inputs',P/'report_inputs.jsonl','--items',P/'report_items.json','--output',stage/'sources_used.md'])
checks(stage,'.staging')
target=P.parent
assert target.resolve().is_relative_to(ROOT.resolve())
shutil.copy2(stage/NAME,target/NAME)
shutil.copy2(stage/'sources_used.md',target/'sources_used.md')
try:checks(target,'')
except Exception:
    # A rejected new report is not left under the completion filename.
    (target/NAME).replace(P/'failed_final.md')
    raise
now=datetime.now(timezone(timedelta(hours=8))).isoformat()
results.update(completed_at=now,canonical_report=str(target/NAME),report_sha256=hashlib.sha256((target/NAME).read_bytes()).hexdigest())
(P/'validation_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('CANONICAL_READY',target/NAME,now)
