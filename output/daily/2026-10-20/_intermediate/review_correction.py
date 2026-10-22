import json,hashlib
from pathlib import Path
from datetime import datetime,timezone,timedelta
P=Path(__file__).resolve().parent
def read(n):return json.loads((P/n).read_text(encoding='utf-8'))
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
D=read('selection_decisions.json')['decisions'];I=read('report_items.json')['items'];r=read('run_summary.json');v=read('validation_results.json')
changed=[x for x in D if x.get('user_review_basis')]
assert len(changed)==9 and all(x['decision']=='exclude' for x in changed)
assert len(I)==18 and r['sections']['industry_news']==6
assert all(v[k]['exit_code']==0 for k in ['report_lint','artifact_validate'])
used={s for it in I for s in it['source_ids']}
assert not any(x['candidate_id'] in {it['candidate_id'] for it in I} for x in changed)
now=datetime.now(timezone(timedelta(hours=8))).isoformat()
report=P.parent/'game_industry_daily_2026-10-20.md'
r.update(completed_at=now,review_correction={'reason':'用户指出普通Demo/上线节点被机械套用品类标签抬高R；已对同类预约/预下载补查。','removed_candidate_ids':[x['candidate_id'] for x in changed],'removed_industry_items':9,'original_industry_count':15,'corrected_industry_count':6},candidate_decisions=len(D),input_coverage={'covered':230,'total':230},used_source_quality={'full':len(used),'non_full':0},validation={'report_lint_errors':0,'report_lint_warnings':2,'artifact_errors':0,'artifact_warnings':0},report_sha256=hashlib.sha256(report.read_bytes()).hexdigest())
save('run_summary.json',r)
scan=read('full_input_scan.json')
for x in scan['sources']:x['decision_ids']=[d['candidate_id'] for d in D if x['source_id'] in d['source_ids']]
save('full_input_scan.json',scan)
lines=['# 运行摘要｜2026-10-20日报（用户复核后）','',f'- 更正时间：{now}。','- 分区：行业6 / AI6 / 日历2 / 社区2 / 深度2，共18条，引用20条完整来源。','- 行业原15条剔除9条：用户指出的4条Demo/上线，以及同类5条预约/预下载信息。','- 根因：把品类标签当成业务相关性证据；合作误当PVP；“已上线试玩”误当新品首测；普通预下载误套E2。','- 不改变7分阈值，不给日历自动开发布资格；所有候选和原评分保留在审计JSON中。','- 历史窗口2026-10-06_to_2026-10-19；9个repeat_only候选记录排除；ForgeTax为1条material_update；card_carryover=0。','- 周三不涉及周五回执交接。深度仍为2条已选事件综合分析。','- report_lint与artifact validate均0 error；warning2：22条非完整输入未引用、AI6超软目标。','- VGC/DataEye/nadianshi/Cubox/wanjiang失败，PocketGamer降级，无当日Steam排名，不联网补造。','','| 更正候选 | 原E/R/M | 新E/R/M | 新总分 |','| --- | --- | --- | --- |']
for d in changed:
    old=d['user_review_original_scores'];new=d['scores'];lines.append(f"| {d['candidate_id']} {d['event']} | {old['event']}/{old['relevance']}/{old['hook']} | {new['event']}/{new['relevance']}/{new['hook']} | {new['total']} |")
lines += ['','| 保留行业条目 | E/R/M | 总分 |','| --- | --- | --- |']
for x in r['industry_scores']:
    sc=x['scores'];lines.append(f"| {x['title']} | {sc['event']}/{sc['relevance']}/{sc['hook']} | {sc['total']} |")
lines += ['','5–6分边界候选仍全部排除，详见selection_decisions.md/json。']
(P/'run_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
memo=f'''\n\n## {now} 用户纠正行业新闻评分
- 用户指出《龙骨海盗》《流放地牢》《大武林》《英雄请出战》的普通Demo/上线消息达不到行业新闻基准。根因是机械把RPG/卡牌/经营等标签当R3，把合作当PVP，把“已上线试玩”当新品首测；算式和契约校验通过不代表选材判断正确。
- 后续优先遵循用户明确口径：低信息的产品日历节点不能仅靠品类标签取得R3；R需有主体/中国移动业务/实质竞争迁移事实。多人合作不自动等于PVP；“已上线试玩”不足以证明首测。规则中优先品类的宽泛表述不能用于给这些普通节点抬分。没有研发/发行主体信息不得补猜。
- 已从2026-10-20日报行业栏剔除上述4条，并同查剔除《战舰移动2》预约宣传及《守护庄园》《拳皇·命运》《征战王权》《美职篮奇迹梦之队》4条预下载。I020/I195/I198改E3R1M1=4；I191改E0R1M1=1；I190保留国服R3但广告E0=1；4条预下载E0R1M1=1。原评分保存user_review_original_scores，候选保留exclude，不自动塞入日历。
- 更正后行业6/AI6/日历2/社区2/深度2，总18条、20条完整来源。保留行业为南山投资、猩球广州发行、京东公司各10；HITpoint8；社招调查和ForgeTax各7。所有JSON/Markdown审计、来源自动映射、终稿、汇总已更新，canonical双校验均0error（仍2warning）。没有改SKILL/校验脚本、news_data、飞书或docs，没有git add/commit/push。
- 本条覆盖前面09:19记忆里的行业15/总27旧计数；当前SHA256={r['report_sha256']}。当前复核运行记录时间：{now}。\n'''
(P/'memory_review_pending.md').write_text(memo,encoding='utf-8')
print('CORRECTION_READY',now,'industry=6 total=18 full_sources=20',r['report_sha256'])
