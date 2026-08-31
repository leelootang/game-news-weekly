import json, pathlib, sys, re
P=pathlib.Path(__file__).parent
rows=[json.loads(s) for s in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
if sys.argv[1]=='full':
    ids={int(s) for s in sys.argv[2].split(',')}
    for r in rows:
        if int(r['source_id'][1:]) in ids:
            print('\n###',r['source_id'],r['date'],r['title'],r['body_status'],'\n'+r['text'])
elif sys.argv[1]=='scan':
    start,end=map(int,sys.argv[2:4])
    pattern=re.compile(r'宣布|首次|首曝|立项|融资|收购|停运|关闭|裁员|离职|CEO|突破|超过|亿美元|万美元|亿元|流水|营收|政策|延期|定档|公测|首测|测试|上线|发布|取消|合作|AI|Roblox|Supercell|Riot|Garena|Savvy|launch|million|billion|announce|delay|shut|fund|acquir|releas|invest|revenue|studio',re.I)
    for r in rows[start-1:end]:
        lines=re.split(r'(?<=[。！？])|\n+',r['text'])
        hits=[x.strip() for x in lines if pattern.search(x)]
        print('\n',r['source_id'],r['title'],r['body_status'])
        print('\n'.join(hits) if hits else r['text'])
