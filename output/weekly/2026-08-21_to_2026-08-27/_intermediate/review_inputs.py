import json, sys, hashlib, re
from pathlib import Path
P=Path(__file__).parent
rows=[json.loads(x) for x in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
byid={r['source_id']:r for r in rows}
def dump(v): print(json.dumps(v,ensure_ascii=False,indent=2))
mode=sys.argv[1]
if mode=='index':
    section=sys.argv[2]; start=int(sys.argv[3]); end=int(sys.argv[4])
    selected=[r for r in rows if section=='all' or r['section']==section]
    for r in selected[start:end]: print(r['source_id'],r['date'][5:],r['source'],r['body_status'],len(r['text']),r['title'])
elif mode=='read':
    for sid in sys.argv[2:]:
        r=byid[sid]; print('\n===',sid,r['date'],r['title'],r['url'],'===\n'+r['text'])
elif mode=='history':
    h=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
    for i,o in enumerate(h['occurrences']):
        print(i,json.dumps(o,ensure_ascii=False))
elif mode=='find':
    pat=re.compile(sys.argv[2],re.I)
    for r in rows:
        if pat.search(r['title']): print(r['source_id'],r['date'],r['body_status'],len(r['text']),r['title'])
elif mode=='baseline':
    root=Path.cwd(); found=[]
    for f in sorted((root/'output').glob('**/_intermediate/report_items.json')):
        if f.parent==P: continue
        if any(x in str(f) for x in ['2026-08-21_to_2026-08-23','daily\\2026-08-24','daily\\2026-08-25','daily\\2026-08-26']):
            raw=json.loads(f.read_text(encoding='utf-8')); items=raw if isinstance(raw,list) else raw['items']
            inp={r['source_id']:r for r in map(json.loads,(f.parent/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
            dec=json.loads((f.parent/'selection_decisions.json').read_text(encoding='utf-8')); dec=dec if isinstance(dec,list) else dec['decisions']; ds={d['candidate_id']:d for d in dec}
            for it in items:
                if it['section'] in ['release','deep']: continue
                it=json.loads(json.dumps(it)); d=json.loads(json.dumps(ds[it['candidate_id']])); remap={}
                for sid in it['source_ids']:
                    matches=[r for r in rows if r['url']==inp[sid]['url'] and r['text']==inp[sid]['text']]
                    if matches: remap[sid]=matches[0]['source_id']
                if len(remap)!=len(it['source_ids']): print('MISSING',it['title']); continue
                it['source_ids']=[remap[s] for s in it['source_ids']]
                for c in it['claims']: c['source_id']=remap[c['source_id']]
                d['source_ids']=it['source_ids']; found.append({'item':it,'decision':d,'prior_report':str(f.relative_to(root))})
                print(len(found)-1,it['section'],d.get('scores'),it['title'],','.join(it['source_ids']))
    (P/'current_week_prior_items.json').write_text(json.dumps(found,ensure_ascii=False,indent=2),encoding='utf-8')
elif mode=='inventory':
    # Read every text, retaining complete source-level identity and quality evidence.
    inv=[{'source_id':r['source_id'],'section':r['section'],'date':r['date'],'title':r['title'],'url':r['url'],'body_status':r['body_status'],'text_chars':len(r['text']),'text_sha256':hashlib.sha256(r['text'].encode()).hexdigest()} for r in rows]
    (P/'full_input_inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Read all',len(rows),'records,',sum(len(r['text']) for r in rows),'characters')
