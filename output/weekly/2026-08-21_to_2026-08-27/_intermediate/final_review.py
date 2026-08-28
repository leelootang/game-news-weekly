import json, hashlib, re, datetime
from pathlib import Path
from collections import Counter
P=Path(__file__).parent.resolve(); OUT=P.parent; ID='2026-08-21_to_2026-08-27'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
items=rd(P/'report_items.json')['items'];ds=rd(P/'selection_decisions.json')['decisions'];D={d['candidate_id']:d for d in ds}
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
report=OUT/f'game_industry_weekly_{ID}.md'; text=report.read_text(encoding='utf-8')
used={sid for i in items for sid in i['source_ids']};covered={sid for d in ds for sid in d['source_ids']}
assert covered==set(S)
assert all(S[x]['body_status']=='full' and S[x].get('fetch_status','ok')=='ok' for x in used)
assert not re.search('沐瞳|Moonton|MLBB|Mobile Legends: Bang Bang|决胜巅峰|card_carryover|补位|上期卡片未展示',text,re.I)
assert [i['title'] for i in items if i['section']=='deep']==[i['title'] for i in rd(P/'deep_handoff_import.json')['items']]
assert sum(d.get('card_designated') is True for d in ds)==1
assert (OUT/'deep_card_choice.txt').read_text(encoding='utf-8').strip()==rd(P/'deep_handoff_import.json')['items'][0]['title']
assert rd(P/'validation_results.json')['passed']
repeat=[d for d in ds if d['section']=='industry' and d['decision']=='exclude' and d['history_check']['novelty']=='repeat_only']
material=[d for d in ds if d['section']=='industry' and d['decision']=='exclude' and d['history_check']['novelty']=='material_update']
border=[d for d in ds if d['section']=='industry' and d['decision']=='exclude' and d['scores']['total'] in [5,6]]
counts=dict(Counter(i['section'] for i in items)); now=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
review=dict(run_at=now,report_id=ID,report_type='weekly',sections=counts,input_records=len(S),used_source_records=len(used),reviewed_source_records=len(covered),decision_records=len(ds),history_window={'start':'2026-08-07','end':'2026-08-20','occurrences':98},repeat_only_excluded=len(repeat),material_update_included=0,material_update_excluded=[{'candidate_id':d['candidate_id'],'title':d['title'],'new_facts':d['history_check']['new_facts']} for d in material],card_carryover_included=0,deep_choice=(OUT/'deep_card_choice.txt').read_text(encoding='utf-8').strip(),reader_facing_forbidden_matches=0,validation=rd(P/'validation_results.json'),file_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [report,OUT/'sources_used.md',P/'report_items.json',P/'selection_decisions.json']})
dump(P/'final_review.json',review)
lines=['# 本期运行与评分复核｜'+ID,'',f'- 完成时间：{now}',f'- 分区：{counts}',f'- 输入：{len(S)}条，审计覆盖{len(covered)}条，出版使用{len(used)}条全文来源。',f'- 双周历史：2026-08-07至2026-08-20，98次出现记录；repeat_only排除{len(repeat)}张候选（包括重复报道）。','- material_update入选0；本周日报新事件按周内合并规则汇总，不伪称跨期新进展。','- card_carryover入选0。Gangstar之前周报未曝光，但8月26日已曝光第4/10位；Makers仅一个可用全文来源、7分不足周报线。','- 深度：C057、C008、C001全部交接；唯一指定卡片为“'+review['deep_choice']+'”。','- report_lint：0 error，1 warning（192条short/snippet输入，未用作终稿证据）。','- report_artifacts validate --require-artifacts：0 error，0 warning。','- git pull --ff-only：Already up to date；news_data只读且tracked diff为空。git status另有全局ignore读取权限警告；未改权限或git配置。','- 无飞书、Docs、网页或git add/commit/push操作。','', '## 行业入选评分','', '| 正文序号 | 新闻 | E | R | M | 总分 |','|---|---|---:|---:|---:|---:|']
for j,i in enumerate([i for i in items if i['section']=='industry'],1):
    s=D[i['candidate_id']]['scores'];lines.append(f"| {j} | {i['title']} | {s['event']} | {s['relevance']} | {s['hook']} | {s['total']} |")
lines+=['','## 5–6分边界候选','', '| 候选 | E | R | M | 总分 | 原因 |','|---|---:|---:|---:|---:|---|']
for d in border:
    s=d['scores'];lines.append(f"| {d['title']} | {s['event']} | {s['relevance']} | {s['hook']} | {s['total']} | {d['reason']} |")
lines+=['','## 有新增事实但未过线','']
for d in material:lines.append('- '+d['title']+'：'+'；'.join(d['history_check']['new_facts'])+'；'+str(d['scores']['total'])+'分。')
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
memory=Path(r'C:\Users\Admin\.codex\automations\daily-generate-game-industry-report\memory.md')
memory.parent.mkdir(parents=True,exist_ok=True)
entry=f"""

{now}
- Friday anchor: weekly {ID}, Asia/Shanghai. git pull --ff-only returned Already up to date. Preserved all pre-existing worktree changes; no news_data edits, Feishu/Docs/webpage work or git add/commit/push.
- Extracted 1465 records (industry981/AI39/release334/community106/deep5), 0 fetch failures/empty texts. Exact --deep-selection used. Imported C057 user-supplied full text into S0671 by exact URL, preserving the original blocked excerpt and provenance; 192 short/snippet records remain, none used in final items.
- Built/read 2026-08-07..2026-08-20 history (98 occurrences, all exposure fields) and supplemental current-week published card history. Excluded {len(repeat)} repeat_only candidate cards. No material_update include; four candidates with material updates (Survival Log Steam China top10; Valorant mobile iOS grossing2; Newzoo 2026 global213.9B/mobile121.1B forecast; Delta Force50M DAU) remain below weekly threshold. Current-week daily events are merged once.
- No card_carryover: Gangstar was already exposed on Aug26 at4/10 despite previous weekly non-exposure; Makers Fund has one usable full-text digest plus a snippet and scores7. Both excluded.
- Final sections industry35 / AI6 / calendar7 / community3 / deep3. Calendar exact ranked prefix: 仙境传说3 / 骤影·绯月杀 / 诡秘之主 / 1666：阿姆斯特丹 / 异克斯小队 / 无限大 / 源初之结. Corrected aliases, event dates, false company bonus and non-first-reveal signals; all1465 sources covered by {len(ds)} decisions.
- Deep handoff C057/C008/C001 preserved in exact order with card_copy; unique card designated: {review['deep_choice']}. Final AI includes Motus,Roblox safety models,233工坊,Side-Modl QA,TeamLiquid-SAP,MetaPocket US test. Entity funding amount omitted because sources disagree on USD conversion.
- Final Markdown: output/weekly/{ID}/game_industry_weekly_{ID}.md; sources_used.md generated automatically. report_lint0 errors/1 warning(192 short/snippet inputs); artifact validation0 errors/0 warnings. Forbidden reader-facing terms0; final hashes and complete score tables in _intermediate/final_review.json and run_summary.md. git status emitted a nonblocking global-ignore permission warning; tracked news_data diff is empty. Runtime approximately 35 minutes; completed {now}.
"""
with memory.open('a',encoding='utf-8') as f:f.write(entry)
print(json.dumps({k:review[k] for k in ['run_at','sections','input_records','used_source_records','decision_records','repeat_only_excluded','material_update_excluded','card_carryover_included']},ensure_ascii=False,indent=2))
print('BORDER',[(d['title'],d['scores']) for d in border])
print('Memory appended:',memory)
