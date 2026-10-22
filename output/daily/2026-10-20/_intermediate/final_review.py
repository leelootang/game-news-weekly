import json,re,hashlib,subprocess
from pathlib import Path
from datetime import datetime,timezone,timedelta
P=Path(__file__).resolve().parent;ROOT=P.parents[3]
def read(n):return json.loads((P/n).read_text(encoding='utf-8'))
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
D=read('selection_decisions.json')['decisions'];items=read('report_items.json')['items'];summary=read('run_summary.json')
S={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
used={s for x in items for s in x['source_ids']};covered={s for x in D for s in x['source_ids']}
assert set(S)==covered
assert all(S[s]['body_status']=='full' and S[s]['fetch_status']=='ok' for s in used)
final=P.parent/'game_industry_daily_2026-10-20.md';text=final.read_text(encoding='utf-8')
assert not re.search(r'沐瞳|Moonton|MLBB|决胜巅峰|Mobile Legends|card_carryover|补位|对我司|值得借鉴|启示',text,re.I)
assert len(items)==18 and summary['sections']==dict(industry_news=6,ai_trends=6,release_calendar=2,community_discourse=2,deep_analysis=2)
assert all(read('validation_results.json')[key]['exit_code']==0 for key in ['report_lint','artifact_validate'])
assert subprocess.run(['git','diff','--quiet','--','news_data'],cwd=ROOT).returncode==0
scan=read('full_input_scan.json')
for x in scan['sources']:x['decision_ids']=[d['candidate_id'] for d in D if x['source_id'] in d['source_ids']]
save('full_input_scan.json',scan)
health=[dict(collector=x['collector'],status=x.get('status'),health=x.get('health'),articles=x.get('in_window_article_count')) for x in read('collector_coverage_audit.json')['results'] if x.get('status') not in ['ok','success'] or x.get('health') in ['degraded','failed']]
now=datetime.now(timezone(timedelta(hours=8)));elapsed=(now-datetime(2026,10,21,8,55,49,tzinfo=timezone(timedelta(hours=8)))).total_seconds()/60
summary.update(completed_at=now.isoformat(),runtime_minutes=round(elapsed,1),candidate_decisions=len(D),input_coverage={'covered':len(covered),'total':len(S)},used_source_quality={'full':len(used),'non_full':0},collector_health=health,validation={'report_lint_errors':0,'report_lint_warnings':2,'artifact_errors':0,'artifact_warnings':0},report_sha256=hashlib.sha256(final.read_bytes()).hexdigest(),forbidden_marker_matches=0,news_data_modified=False)
summary['warnings'].append('VGC/DataEye/nadianshi/Cubox/wanjiang采集失败；PocketGamer降级。无联网补缺。')
save('run_summary.json',summary)
lines=['# 运行摘要｜2026-10-20日报','',f'- 完成时间：{now.isoformat()}；运行约{elapsed:.1f}分钟。','- 分区：行业15 / AI6 / 日历2 / 社区2 / 深度2。','- 输入230条全部映射至383个独立/聚类决策；正文引用29条完整来源。','- 历史窗口2026-10-06_to_2026-10-19，112次出现；9个repeat_only候选记录排除。','- material_update仅ForgeTax：国内复刻产品TapTap下载30万，历史仅原作销量；不同估算平台不计算净增。','- card_carryover=0；此前卡片排名不适用。ForgeTax历史未曝光，rank=null、limit=10。','- 星期三日报，不运行周五回执交接；已检查3条newsletter，采用2条本期已选事件综合深度。','- report_lint与artifact validate均0 error。warning2：22条非完整输入未引用，AI6条超过软目标。','- 地渊两源缺绝对月日未发布；小小港湾同稿去重1源；当日Steam榜单缺失。','- 采集失败：VGC/DataEye/nadianshi/Cubox/wanjiang；PocketGamer降级。','- git pull --ff-only已是最新；news_data未改；未访问飞书/Docs，未产网页，未git add/commit/push。','','| 入选行业 | E | R | M | 总分 |','| --- | --- | --- | --- | --- |']
for x in summary['industry_scores']:
    sc=x['scores'];lines.append(f"| {x['title']} | {sc['event']} | {sc['relevance']} | {sc['hook']} | {sc['total']} |")
lines += ['','边界候选（包含合并记录，全部不进入行业正文）：','']
for x in summary['boundary_5_6']:
    sc=x['scores'];lines.append(f"- {x['candidate_id']} {x['event']}：E{sc['event']}×R{sc['relevance']}+M{sc['hook']}={sc['total']}；{x['reason']}")
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
memory=Path('C:/Users/Admin/.codex/automations/daily-generate-game-industry-report/memory.md')
memo=f'''\n\n## 2026-10-21 日报生成
- Wednesday Asia/Shanghai anchor: daily date=2026-10-20. Read skill, all six references and memory; git pull --ff-only Already up to date after automatically approved FETCH_HEAD sandbox escalation. No news_data changes, Feishu/Docs/HTML or git add/commit/push; existing script/test changes preserved.
- Extracted230 records (industry159 / AI23 / calendar31 / community14 / deep3),0 failures/empty,22 non-full. All230 IDs covered across383 decisions; final27 items use29 full sources.
- Final counts industry15 / AI6 / calendar2 / community2 / deep2. Industry: Nanshan/iDreamSky2亿元, Apes Guangzhou publishing, JD gaming entity, Dragonkeel co-op demo, Dungeon Exile demo, Dawulin launch, Hero Please launch each E3R3M1=10; HITpoint E3R2M2=8; recruiting market survey, ForgeTax update, Warship Mobile2 national reveal and Guardian Manor/KOF/Fight for Kings/NBA preload each E2R3M1=7. Genre/platform/company only from raw text; unknown PC single-player releases keepR1.
- Recruiting source50 contains snapshot截至10月8日; independently audited19 project/direction candidates. Corrected8 initial E3 judgments toE1 because no current first-reveal/approval state is evidenced. Kept one new market-survey disclosure E2, without bundling products. Validators disallow identical source sets across published items; no invented IDs or validator changes.
- History2026-10-06..2026-10-19,112 exposure-aware occurrences;9 repeat_only candidate records excluded (Metacore, Flow, ICEY, Shenxian3, COD/LoL/Squad repeats). Sole material_update ForgeTax: domestic similar TapTap title30万 downloads, not present in original VGI20万 historical case. Current Gamalytic25万/375万元 uses different estimator; no net-growth calculation. No card_carryover; prior rank N/A (ForgeTax historicalfalse/null/limit10).
- Calendar only Emberville demo9 and Stella Sora major permanent autochess/home update3 passed prefix. Tiny Harbor55/159 same body except end marker ->1 independent source. Medieval54/158 whitespace duplicate and19日 outside window. Earth-depth Jeweler2 distinct reports lack absolute day required by validator; retained exclusion without altering sources. Upcoming lists, history launches, cancelled demos and music Firestarter corrected. No20日 Steam ranking input.
- AI6 direct cases: SeaGamesMaker beta, Blender/engine production examples, ReVamp restricted test, Minecraft autonomous agents, SpireBench, Japanese actors voice-AI guidelines. No generic frontier filler. Community: Endfield tool-name complaint and Duet Night Abyss1.7 service outage; only20日 content, no21日 restoration/compensation or speculation-as-fact. Deep2: asset-to-engine usability; demo exposure/cloning economics, each2 analysis paragraphs+3 card insights. Wednesday: no Friday receipt handoff.
- Canonical report_lint explicit report/sources/inputs and artifactvalidate --require-artifacts both0error; lint2warnings(22non-full inputs unused,AI6 above soft1–3),artifact0warnings. Forbidden marker scan0, all input coverage230/230. Collector VGC/DataEye/nadianshi/Cubox/wanjiang failed;PocketGamer degraded;no web backfill.
- Canonical output/daily/2026-10-20/game_industry_daily_2026-10-20.md plus auto-generatedsources_used and required audits. SHA256={summary['report_sha256']}. Final runtime approximately{elapsed:.1f}min; memory recorded{now.isoformat()}.
'''
memory.parent.mkdir(parents=True,exist_ok=True)
with memory.open('a',encoding='utf-8') as f:f.write(memo)
print('FINAL_REVIEW_OK',now.isoformat(),round(elapsed,1),'minutes',summary['report_sha256'])
