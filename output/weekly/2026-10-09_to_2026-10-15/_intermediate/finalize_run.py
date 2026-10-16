import json,re,datetime,hashlib,subprocess,os
from pathlib import Path
from collections import Counter
P=Path(__file__).parent;OUT=P.parent;ROOT=Path.cwd()
summary=json.loads((P/'run_summary.json').read_text(encoding='utf-8'))
checks=json.loads((P/'validation_results.json').read_text(encoding='utf-8'))
assert len(checks)==3 and all(x['returncode']==0 for x in checks)
items=json.loads((P/'report_items.json').read_text(encoding='utf-8'))['items']
decisions=json.loads((P/'selection_decisions.json').read_text(encoding='utf-8'))['decisions']
inp={x['source_id']:x for x in map(json.loads,(P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
report=OUT/f'game_industry_weekly_{OUT.name}.md';body=report.read_text(encoding='utf-8')
assert not re.search('沐瞳|Moonton|MLBB|决胜巅峰|card_carryover|上期卡片未展示|补位',body,re.I)
assert not any('weekly 2026-10-09_to_2026-10-15' in x for d in decisions if d['section']=='industry' for x in d['history_check']['prior_occurrences'])
assert {sid for d in decisions for sid in d['source_ids'] if inp[sid]['section']=='industry_news'}=={sid for sid,s in inp.items() if s['section']=='industry_news'}
assert all(inp[sid]['body_status']=='full' for it in items for sid in it['source_ids'])
choice=(OUT/'deep_card_choice.txt').read_text(encoding='utf-8').strip()
assert choice==next(it['title'] for it in items if it['candidate_id']=='D001')
assert [d['candidate_id'] for d in decisions if d.get('card_designated')]==['D001']
diff=subprocess.run(['git','diff','--name-only','--','news_data'],capture_output=True,text=True,encoding='utf-8',check=True)
assert not diff.stdout.strip()
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
checkpoint_minutes=round((datetime.datetime.fromisoformat(now)-datetime.datetime.fromisoformat('2026-10-16T08:58:54+08:00')).total_seconds()/60,1)
used={sid for it in items for sid in it['source_ids']}
summary.update(completed_at=now,used_sources=len(used),used_body_status=dict(Counter(inp[x]['body_status'] for x in used)),
 decision_records=len(decisions),calendar_nodes=len(json.loads((P/'release_calendar_audit.json').read_text(encoding='utf-8'))['nodes']),
 weekly_rollups=sum(bool(d.get('weekly_rollup')) for d in decisions),validation_errors=0,
 warnings=[line for check in checks for line in check['stdout'].splitlines() if line.startswith('WARN:')],
 report_sha256=hashlib.sha256(report.read_bytes()).hexdigest())
(P/'run_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
audit=['# 运行结果与复核摘要','',f'- 完成时间：{now}',f'- 锚点：星期五，周报，{OUT.name}',f'- 终稿：{report.resolve()}',f"- 分区数量：{summary['section_counts']}",f'- 输入：1356；实际引用{len(used)}条来源，全部full。',f"- 决策：{len(decisions)}条；产品日历节点：{summary['calendar_nodes']}；全部974条行业来源有明确归属。",'- 双周历史：2026-09-25至2026-10-08，70条，含完整卡片曝光字段。',f"- repeat_only：{len(summary['repeat_only'])}条候选记录排除；不把记录数当作独立事件数。",f"- 周内汇总：{summary['weekly_rollups']}条；不含本期周报自身。",'- card_carryover：0；此前卡片排名N/A。欧盟旧行动虽全部未曝光，但7分未达周报阈值。','- 深度：回执987a7ba088484df3a5e13aee0f3518eb，C001/C002/C003顺序；C001唯一主卡；selection、正文与deep_card_choice闭环。','- git pull --ff-only：Already up to date。news_data差异为空；未触及飞书发布、Docs、HTML或git add/commit/push。','- 双校验：report_lint与report_artifacts validate --require-artifacts均0 error；selection lint为0。','','## 实质更新','']
for x in summary['material_updates']:audit.append('- '+x['title']+'：'+'；'.join(x['new_facts']))
audit+=['','## 入选行业评分','','| 事件 | E | R | M | 总分 |','| --- | --- | --- | --- | --- |']
for x in summary['industry_scores']:audit.append(f"| {x['title']} | {x['event']} | {x['relevance']} | {x['hook']} | {x['total']} |")
audit+=['','## 5–6分边界候选','']
for x in summary['boundary_5_6']:
    s=x['scores'];audit.append(f"- {x['title']}：E{s['event']}×R{s['relevance']}+M{s['hook']}={s['total']}，exclude。")
audit+=['','## Warning与覆盖边界','']+['- '+x for x in summary['warnings']]
audit+=['- 152条非完整输入包含1条空正文；均未作为最终条目证据。', '- AI超出2–6条软目标；本期10条均是直接作用事件，保留研发管线、AI原生产品、游戏平台和发行工具的独立变化。','- Meta Pocket扩区单独留为候选：唯一完整来源与Garena行业事件共用综述；当前校验器禁止行业与AI复用source，即使不同事件，也不允许跨栏通过。本次未改生产脚本或伪造来源拆分。','- 采集窗口7天均有数据，但DataEye/哪点事/Cubox/玩匠/VGC有局部失败，PocketGamer/VGC有降级；详见collection_audit_summary.json。normal_zero/zero_articles不直接等同失败。','- 统计来源是已采集正文，未联网补采；提取0失败不代表采集覆盖完整。']
(P/'run_summary.md').write_text('\n'.join(audit)+'\n',encoding='utf-8')
memory=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'automations/daily-generate-game-industry-report/memory.md'
memory.parent.mkdir(parents=True,exist_ok=True)
entry=f'''\n\n{now}
- Friday anchor: weekly {OUT.name}, Asia/Shanghai. git pull --ff-only returned Already up to date; news_data diff empty; all pre-existing modifications preserved. Elapsed from the first recorded clock checkpoint at 08:58:54+08:00: {checkpoint_minutes} minutes; completion time {now}.
- Read the skill and all six applicable references. Feishu receipt 987a7ba088484df3a5e13aee0f3518eb raw reply selects body C001/C002/C003 and sole card C001. Materialized the exact-ID selection, passed lint-selection, and extracted with --deep-selection. No send or Docs work.
- Extracted 1356 records (industry974 / AI113 / calendar154 / community106 / deep9), 0 extraction failures, 1 empty, 152 non-full. Final evidence: {len(used)} IDs, all full. Every industry source has an individual or clustered audit; no blanket low-signal batch.
- History 2026-09-25..2026-10-08 with 70 exposure-aware occurrences. {len(summary['repeat_only'])} repeat_only candidate records excluded (including Delta DAU, Exit Games, September mobile charts, Grasshopper, Circle, Minecraft Blast, mo.co). Two included material updates: Extreme Combat first reveal/test schedule versus prior trademark; RED LAND >200k visitors, 82% from outside Shanghai, >2.5bn impressions. No card_carryover; prior rank N/A. Within-week rollups exclude the report itself to remain rerun-safe.
- Final sections industry27 / AI10 / calendar7 / community3 / deep3. Ordinary overseas PC single-player launch-only candidates remain R1; Planet Zoo2/Valor Mortis/Boltgun2 each5, Taiwu5 with unknown relevance exception, Steam Next Fest5, RedLynx6. Industry/calendar overlap permitted independently. Astrocade's 10m MAU included; Meta Pocket regional expansion remains an independent excluded AI candidate because the current validator rejects using S0482 in both industry and AI even though events differ. Kept threshold-qualified Garena instead; no script changes or invented split source IDs.
- Calendar preserves raw audit and has {summary['calendar_nodes']} corrected/recall nodes. Corrected GTA trailers, historical month fallback, cloud-provider company bonus, aliases, same-publisher/reprint source dedup and actual launch versus older schedule stages. Prefix: Extreme Combat, Sword World4, Green Dream, Seven Realms, Taiwu, Animal City Cafe, Liancheng. 1999TOKOYO is below weekly cap, not suppressed by industry overlap.
- Deep topics: MMORPG revenue decline, Royal Kingdom mandatory-level friction, Delta shared-prison design reversal. Exact titles/order and sole main-card file agree. Each includes two developed analysis paragraphs and 3–6 card insights.
- Both final canonical validations passed 0 error. Warnings: 152 non-full inputs including1empty (none cited); AI10 exceeds soft2–6, all direct game applications. Collector caveat: some DataEye/nadianshi/Cubox/wanjiang/VGC failures and PocketGamer/VGC degraded; no web backfill. Forbidden/internal marker scan0; no Feishu publishing, Docs, webpage generation or git add/commit/push. Outputs, sources and audits are under output/weekly/{OUT.name}/.
'''
with memory.open('a',encoding='utf-8') as f:f.write(entry)
print(json.dumps({'completed_at':now,'counts':summary['section_counts'],'sources':len(used),'repeat_only':len(summary['repeat_only']),'weekly_rollups':summary['weekly_rollups'],'boundaries':summary['boundary_5_6'],'memory':str(memory),'report':str(report.resolve())},ensure_ascii=False,indent=2))
