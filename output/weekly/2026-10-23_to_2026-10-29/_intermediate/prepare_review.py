import json, re, hashlib, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT=Path.cwd()
B=ROOT/'output/weekly/2026-10-23_to_2026-10-29/_intermediate'
rows=[json.loads(s) for s in (B/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
byid={r['source_id']:r for r in rows}
byurl=defaultdict(list)
for r in rows: byurl[r['url']].append(r)
prior=[]; olditems=[]
for rel in ['weekend/2026-10-23_to_2026-10-25','daily/2026-10-26','daily/2026-10-27','daily/2026-10-28']:
 p=ROOT/'output'/rel/'_intermediate'
 old={r['source_id']:r for r in map(json.loads,(p/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
 mapping={sid: next((r['source_id'] for r in byurl[x['url']] if r['text']==x['text']), next((r['source_id'] for r in byurl[x['url']]),None)) for sid,x in old.items()}
 def remap(x):
  if isinstance(x,dict): return {k:remap(v) for k,v in x.items()}
  if isinstance(x,list): return [remap(v) for v in x]
  if isinstance(x,str): return mapping.get(x,x) if re.fullmatch('S[0-9]{4}',x) else x
  return x
 ds=json.loads((p/'selection_decisions.json').read_text(encoding='utf-8'))['decisions']
 for d in ds:
  if all(mapping.get(s) for s in d.get('source_ids',[])):
   z=remap(d);z['prior_report']=rel;z['prior_candidate_id']=d['candidate_id'];prior.append(z)
 items=json.loads((p/'report_items.json').read_text(encoding='utf-8'))['items']
 for it in items:
  if all(mapping.get(s) for s in it.get('source_ids',[])):
   z=remap(it);z['prior_report']=rel;olditems.append(z)
(B/'prior_decisions_remapped.json').write_text(json.dumps(prior,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'prior_items_remapped.json').write_text(json.dumps(olditems,ensure_ascii=False,indent=2),encoding='utf-8')
per=defaultdict(list)
for d in prior:
 for sid in d['source_ids']: per[sid].append(d)
review=[]
for r in rows:
 text=r['text']
 review.append(dict(source_id=r['source_id'],date=r['date'],section=r['section'],title=r['title'],url=r['url'],published_at=r['published_at'],chars=len(text),sha256=hashlib.sha256(text.encode()).hexdigest(),prior_reviews=[dict(report=d['prior_report'],candidate_id=d['candidate_id'],decision=d['decision'],reason=d['reason'],scores=d.get('scores')) for d in per[r['source_id']]],lines=len(text.splitlines())))
(B/'source_review_coverage.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
print('records',len(rows),'prior decisions',len(prior),'prior items',len(olditems),'source reviewed previously',sum(bool(per[r['source_id']]) for r in rows))
print('UNREVIEWED')
for r in rows:
 if not per[r['source_id']]:print(r['source_id'],r['section'],r['title'])
