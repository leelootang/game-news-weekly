import json,collections,re,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[3]
paths=[('本周周一周末报','output/weekend/2026-10-16_to_2026-10-18',7),('本周周二日报','output/daily/2026-10-19',7),('本周周三日报（纠正后）','output/daily/2026-10-20',7),('最近周报，非本周','output/weekly/2026-10-09_to_2026-10-15',8)]
result=[]
for label,path,threshold in paths:
    ip=ROOT/path/'_intermediate'
    data=json.loads((ip/'selection_decisions.json').read_text(encoding='utf-8'))
    decisions=data if isinstance(data,list) else data['decisions']
    sources={x['source_id']:x for x in map(json.loads,(ip/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines())}
    ds=[d for d in decisions if d.get('section') in ['industry_news','industry','行业新闻']]
    dist=collections.Counter((d['decision'],d['scores']['hook']) for d in ds)
    effects=[]
    for d in ds:
        sc=d['scores'];e,r,m=map(int,[sc['event'],sc['relevance'],sc['hook']]);base=e*r
        if d['decision']=='include' and base<threshold:
            effects.append(dict(kind='promoted_by_M',candidate=d,base=base,threshold=threshold))
        elif d['decision']=='exclude' and e>0 and base+m<threshold<=base+2:
            effects.append(dict(kind='potential_M_interception',candidate=d,base=base,threshold=threshold,source_quality=[dict(id=s,status=sources[s].get('body_status'),fetch=sources[s].get('fetch_status'),title=sources[s].get('title')) for s in d['source_ids']]))
    summary=dict(label=label,path=path,threshold=threshold,total_industry_candidates=len(ds),decision_counts=dict(collections.Counter(d['decision'] for d in ds)),hook_distribution=[dict(decision=a,hook=b,count=n) for (a,b),n in sorted(dist.items())],effects=effects,
        included_M0=[d for d in ds if d['decision']=='include' and int(d['scores']['hook'])==0],
        exclusion_M0=[d for d in ds if d['decision']=='exclude' and int(d['scores']['hook'])==0],
        excluded_repeat_only=[d for d in ds if d['decision']=='exclude' and d.get('history_check',{}).get('novelty')=='repeat_only'])
    result.append(summary)
    print('\nREPORT',label,path,'industry',len(ds),'decisions',summary['decision_counts'],'hooks',summary['hook_distribution'])
    print('COUNTS promotion',sum(x['kind']=='promoted_by_M' for x in effects),'potential_M_interception',sum(x['kind']=='potential_M_interception' for x in effects),'repeat_only_exclusions',len(summary['excluded_repeat_only']))
    for x in effects:
        d=x['candidate']
        if x['kind']=='potential_M_interception':
            print('INTERCEPT',json.dumps(x,ensure_ascii=False))
    for d in summary['exclusion_M0']:
        print('EXCLUDE_M0',json.dumps(d,ensure_ascii=False))
(P/'m_value_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
