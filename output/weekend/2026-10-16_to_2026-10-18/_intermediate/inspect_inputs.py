import json, sys, re
from pathlib import Path
p=Path(__file__).parent
rows=[json.loads(s) for s in (p/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
if sys.argv[1]=='history':
 d=json.loads((p/'industry_history_14d.json').read_text(encoding='utf-8'))
 print(d.keys())
 for r in d.get('items',d.get('occurrences',[])):
  print(json.dumps(r,ensure_ascii=False))
elif sys.argv[1]=='text':
 lo,hi=map(int,sys.argv[2:4])
 for r in rows:
  if lo<=int(r['source_id'][1:])<=hi:
   print('\n###',r['source_id'],r['date'],r['section'],r['body_status'],r['url'],'\n'+r['text'])
elif sys.argv[1]=='index':
 for r in rows:
  print(r['source_id'],r['date'],r['section'],r['body_status'],r['text_chars'],r['title'])
elif sys.argv[1]=='digest':
 lo,hi=map(int,sys.argv[2:4])
 for r in rows:
  if lo<=int(r['source_id'][1:])<=hi:
   t=r['text']
   parts=re.split(r'(?<=[。！？\n])',t)
   signals=[s.strip() for s in parts if re.search(r'宣布|融资|收购|停运|关闭|取消|裁员|辞职|开测|首测|首曝|上线|公测|日发售|万美元|亿元|政策|测试|announc|funding|million|bankrupt|layoff|cancel|launch|shut|releas',s,re.I)]
   print('\n###',r['source_id'],r['date'],r['section'],r['body_status'],r['title'])
   print(t[:350].replace('\n',' ')+'\n信号: '+' '.join(signals)[:1200])
