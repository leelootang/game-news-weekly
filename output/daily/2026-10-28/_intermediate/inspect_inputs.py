import json, sys, re
from pathlib import Path
P=Path(__file__).parent
rows=[json.loads(s) for s in (P/'report_inputs.jsonl').read_text(encoding='utf-8').splitlines()]
if sys.argv[1]=='history':
 h=json.loads((P/'industry_history_14d.json').read_text(encoding='utf-8'))
 md=(P/'industry_history_14d.md').read_text(encoding='utf-8')
 for r in h['occurrences']+h['archive_occurrences']:
  if any(t.lower() in json.dumps(r,ensure_ascii=False).lower() for t in sys.argv[2:]): print(json.dumps(r,ensure_ascii=False))
elif sys.argv[1]=='read':
 for r in rows:
  if r['source_id'] in sys.argv[2:]:print('\n### '+r['source_id']+' '+r['title']+'\n'+r['text'])
elif sys.argv[1]=='scan':
 for r in rows:
  if r['section'] in sys.argv[2:]:
   # Paragraph navigation; the full local JSONL has been parsed above.
   print('\n### '+r['source_id']+' '+r['title'])
   for s in r['text'].splitlines():
    if re.search(r'(?i)launch|release|clos|fund|acquir|partner|appoint|million|billion|revenue|Steam|Nintendo|Tencent|NetEase|[上首公]线|首[曝测]|停[运服]|收购|融资|辞职|离职|亿元|亿美元|下载|发售|定档|[0-9]{1,2}月[0-9]{1,2}日',s):print(s)
