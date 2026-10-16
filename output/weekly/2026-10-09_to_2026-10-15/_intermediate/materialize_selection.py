import json
from pathlib import Path

root = Path.cwd()
weekly_id = '2026-10-09_to_2026-10-15'
receipt = json.loads((root/'data/feishu/deep_review/replies/987a7ba088484df3a5e13aee0f3518eb.json').read_text(encoding='utf-8'))
review = json.loads((root/'tmp/deep_observation_2026-10-08_to_2026-10-14/candidate_review.json').read_text(encoding='utf-8'))
old_inputs = [json.loads(x) for x in (root/'tmp/deep_observation_2026-10-08_to_2026-10-14/report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
sources = {x['source_id']:x for x in old_inputs}
out = [f'# 深度观察人工选择｜{weekly_id}', '', '- 候选数据窗口: 2026-10-08_to_2026-10-14', f'- 目标周报窗口: {weekly_id}', '- 选择来源: 飞书周四备选 Bot', f"- 飞书回执ID: {receipt['receipt_id']}", '- 正文候选ID: C001, C002, C003', '- 指定卡片候选ID: C001', '', '原话：正文：C001，C002，C003；卡片：C001。', '', '## 用户选择进入周报的条目', '']
for n, cid in enumerate(receipt['body_candidate_ids'],1):
    c = review['candidates'][int(cid[1:])-1]
    prefix = '★卡片:' if cid == receipt['card_base_candidate_id'] else ''
    points = c['analysis_points']
    out += [f"### {n}. {prefix}{c['title']}", '', '观察：'+c['observation'], '', '分析：'+' '.join(p['detail'] for p in points[:2]), '', ' '.join(p['detail'] for p in points[2:]), '']
    for sid in c['source_ids']:
        s=sources[sid]
        out += [f"- 来源:{s['source']},《{s['title']}》,{s['url']}"]
    out += ['']
path=root/f'output/deep_observation_review/{weekly_id}_selection.md'
if path.exists():
    raise SystemExit('Selection already exists; preserved')
path.write_text('\n'.join(out),encoding='utf-8')
print(path)
