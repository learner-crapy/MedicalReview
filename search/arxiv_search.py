import urllib.request, urllib.parse, time, json, os, re
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
QUERIES=[
 ('Q01','abs:"multi-agent" AND abs:"medical"'),
 ('Q02','abs:"multi-agent" AND abs:"clinical"'),
 ('Q03','abs:"large language model" AND abs:"medical question answering"'),
 ('Q04','all:"MedQA" AND abs:"agent"'),
 ('Q05','abs:"multi-agent" AND abs:"MedQA"'),
 ('Q06','abs:"debate" AND abs:"medical" AND abs:"language model"'),
 ('Q07','abs:"agents" AND abs:"diagnosis" AND abs:"large language model"'),
 ('Q08','abs:"collaboration" AND abs:"large language model" AND abs:"medical"'),
 ('Q09','all:"MedMCQA" AND all:"agent"'),
 ('Q10','abs:"multi-agent" AND abs:"healthcare"'),
 ('Q11','abs:"physician" AND abs:"agents" AND abs:"language model"'),
 ('Q12','abs:"multi-agent" AND abs:"question answering" AND abs:"LLM"'),
 ('Q13','all:"USMLE" AND abs:"agent"'),
 ('Q14','abs:"agent" AND abs:"medical reasoning"'),
]
rows={}
log=[]
for qid,q in QUERIES:
    url='http://export.arxiv.org/api/query?'+urllib.parse.urlencode({
        'search_query':q,'start':0,'max_results':100,
        'sortBy':'submittedDate','sortOrder':'descending'})
    try:
        raw=urllib.request.urlopen(url,timeout=60).read()
    except Exception as e:
        log.append((qid,q,'ERROR',str(e))); time.sleep(3); continue
    root=ET.fromstring(raw)
    n=0
    for e in root.findall('a:entry',NS):
        aid=e.find('a:id',NS).text.strip()
        m=re.search(r'abs/([0-9]+\.[0-9]+)(v\d+)?$',aid)
        if not m: continue
        key=m.group(1)
        title=' '.join(e.find('a:title',NS).text.split())
        summ=' '.join(e.find('a:summary',NS).text.split())
        pub=e.find('a:published',NS).text[:10]
        upd=e.find('a:updated',NS).text[:10]
        authors=[a.find('a:name',NS).text for a in e.findall('a:author',NS)]
        cats=[c.get('term') for c in e.findall('a:category',NS)]
        if key in rows:
            rows[key]['queries'].append(qid)
        else:
            rows[key]={'arxiv_id':key,'title':title,'abstract':summ,'published':pub,
                       'updated':upd,'authors':authors[:12],'n_authors':len(authors),
                       'categories':cats,'queries':[qid],
                       'pdf':'https://arxiv.org/pdf/%s'%key,'abs_url':'https://arxiv.org/abs/%s'%key}
        n+=1
    log.append((qid,q,'OK',n)); time.sleep(3)
os.makedirs('search',exist_ok=True)
json.dump(list(rows.values()),open('search/arxiv_raw.json','w'),ensure_ascii=False,indent=1)
print('unique records:',len(rows))
for l in log: print(l)
