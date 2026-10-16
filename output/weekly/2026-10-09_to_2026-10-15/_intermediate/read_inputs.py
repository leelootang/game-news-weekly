import json,sys,re
from pathlib import Path
p=Path(__file__).parent
rows=[json.loads(x) for x in (p/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
if sys.argv[1]=='read':
    wanted=set(sys.argv[2:])
    for s in rows:
        if s['source_id'] in wanted:
            print('\n###',s['source_id'],s['date'],s['source'],s['title'],s['body_status'],'\n',s['text'])
elif sys.argv[1]=='signals':
    start,end=map(int,sys.argv[2:4])
    for s in rows:
        if start<=int(s['source_id'][1:])<end:
            text=s['text']
            lines=re.split(r'(?<=[。！？])|\n+',text)
            signals=[x.strip() for x in lines if re.search(r'融资|收购|投资|裁员|停运|终止|关闭|首曝|首次|上线|公测|开测|政策|合作|亿|收入|下载|月活|日活|launch|funding|raises|acquir|shut|clos|million|billion|policy|releas',x,re.I)]
            print(s['source_id'],s['title'],'\n'+'\n'.join(signals[:8]))
elif sys.argv[1]=='index':
    start,end=map(int,sys.argv[2:4])
    for s in rows:
        if start<=int(s['source_id'][1:])<end:
            print(s['source_id'],s['date'],s['section'],s['source'],s['title'])
