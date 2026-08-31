import os,sys,json,pathlib,subprocess,hashlib,re,collections,datetime
P=pathlib.Path(__file__).parent; OUT=P.parent; ROOT=P.parents[3]
report=OUT/('game_industry_weekend_'+OUT.name+'.md'); sources=OUT/'sources_used.md'
env=dict(os.environ,PYTHONUTF8='1')
base=['--report',str(report),'--sources',str(sources),'--inputs',str(P/'report_inputs.jsonl')]
commands=[['C:/Users/Admin/.codex/skills/game-industry-report/scripts/report_lint.py']+base,[str(ROOT/'scripts/report_artifacts.py'),'validate']+base+['--items',str(P/'report_items.json'),'--decisions',str(P/'selection_decisions.json'),'--release-audit',str(P/'release_calendar_audit.json'),'--require-artifacts']]
results=[]
for name,args in zip(['report_lint','artifact_contract'],commands):
 r=subprocess.run([sys.executable]+args,capture_output=True,text=True,encoding='utf-8',env=env,cwd=ROOT)
 results.append(dict(check=name,exit_code=r.returncode,output=r.stdout+r.stderr,arguments=args))
 print(name,r.returncode,r.stdout+r.stderr)
if any(x['exit_code'] for x in results):
 report.rename(P/'report_validation_failed_draft.md')
 raise SystemExit('Validation failed; removed deliverable filename.')
I=json.loads((P/'report_items.json').read_text(encoding='utf-8'))['items']
D=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))['decisions'];dm={d['candidate_id']:d for d in D}
S={r['source_id']:r for r in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
used={s for i in I for s in i['source_ids']}
bad=[s for s in used if S[s]['body_status']!='full']; assert not bad
markers=re.findall(r'沐瞳|Moonton|MLBB|决胜巅峰|card_carryover|补位|上期卡片未展示',report.read_text(encoding='utf-8'),re.I);assert not markers
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
counts=dict(collections.Counter(i['section'] for i in I))
hist=[d for d in D if d.get('history_check',{}).get('history_match')]
repeats=[d for d in hist if d['history_check']['novelty']=='repeat_only']; updates=[d for d in hist if d['history_check']['novelty']=='material_update']
review=dict(completed_at=now,kind='weekend',start='2026-08-28',end='2026-08-30',counts=counts,input_records=len(S),source_coverage=json.loads((P/'source_coverage.json').read_text(encoding='utf-8')),history_window=['2026-08-14','2026-08-27'],history_occurrences=135,repeat_only_count=len(repeats),material_updates=updates,carryover=dict(candidate_id='I001',prior_body_rank=13,prior_card_rank=None,prior_card_limit=10,prior_card_exposed=False),checks=results,forbidden_terms=markers,non_full_final_evidence=bad,hashes={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [report,sources,P/'report_items.json',P/'selection_decisions.json',P/'release_calendar_audit.json']})
(P/'final_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# 运行摘要｜'+OUT.name,'',f'完成时间：{now}；周一周末报。终稿：{report}。','',f'分区：{counts}。517条输入全部有审计，终稿来源均为full。','',f'行业双周历史：2026-08-14至2026-08-27，135条；repeat_only排除{len(repeats)}项，material_update入选0项。','ACE为唯一card_carryover，11分；上期正文第13条，卡片rank=null / limit=10，未曝光。','《巫师4》目标平台运行是新增技术进度，但仅4分而排除。','周末深度自动采用GameDiscoverCo的Hearth & Hamlet机制分析，3条card_copy洞察；周五selection及卡片指定文件不适用。','校验：report_lint与artifact validate均0 errors。唯一lint warning是61条short/snippet输入，均未作终稿证据。Steam无本期当日快照。','日历采用多源前4项；《无限大》与上周普通窗口有同档期重复，但非次日前瞻重叠，已按当前日历规则留痕。','git pull --ff-only已同步；未改news_data、未操作飞书/docs/网页、未git add/commit/push。','', '## 行业入选逐条评分','','| 条目 | E×R+M | 判断 |','| --- | --- | --- |']
for i in I:
 if i['section']!='industry_news':continue
 d=dm[i['candidate_id']];s=d['scores'];lines.append(f"| {i['title']} | {s['event']}×{s['relevance']}+{s['hook']}={s['total']} | {d['reason']} |")
lines+=['','## 5–6分边界候选','','| 候选 | E×R+M | 排除理由 |','| --- | --- | --- |']
for d in D:
 s=d.get('scores',{})
 if d['section']=='industry_news' and s.get('total') in [5,6]:lines.append(f"| {d['title']} | {s['event']}×{s['relevance']}+{s['hook']}={s['total']} | {d['reason']} |")
lines+=['','## 重复事件排除','']+[f"- {d['candidate_id']} {d['title']}；此前卡片曝光={d['history_check']['prior_card_exposed']}。" for d in repeats]
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
memory=pathlib.Path('C:/Users/Admin/.codex/automations/daily-generate-game-industry-report/memory.md')
memo=['','',now,'- Monday anchor weekend2026-08-28_to_2026-08-30, Asia/Shanghai. git pull --ff-only Already up to date. Preserved existing edits; no news_data edits, Feishu/Docs/webpage or git add/commit/push.','- Extracted517 records (industry323/AI23/calendar115/community54/deep2);0 failed/empty. All517 audited;61 snippets unused as final evidence.',f'- History2026-08-14..2026-08-27,135 occurrences with exposure fields. Excluded{len(repeats)} repeat_only events. Witcher4 target-platform-running status is material_update but score4/excluded. No material_update include.','- Unique card_carryover ACE/Sandbox partnership scores11: prior weekly body13, card_rank=null/10, card_exposed=false. Other unexposed repeats lose by score. No carryover labels in final report.','- Final sections industry21/AI3/calendar4/community2/deep1. Calendar ranked prefix: Wangzhe Wanxiangqi/Ananta/Sea of Remnants/Fanying. Ananta repeats ordinary prior calendar, not next-day overlap under current rule. Fanying platform unspecified; none guessed.','- Depth GameDiscoverCo Hearth & Hamlet analysis: limited-duration incremental design versus city-building expectations;3 card_copy insights. No Friday handoff or deep_card_choice file.','- report_lint0 errors/1 warning(61 snippets unused); artifact validate0 errors/0 warnings; forbidden terms0. Steam missing current snapshots. Output report/sources/intermediates incl final_review.json and run_summary.md under output/weekend/'+OUT.name+'. Runtime approximately33 minutes.']
with memory.open('a',encoding='utf-8') as f:f.write('\n'.join(memo)+'\n')
print('Saved verification, score tables, and memory',now)
