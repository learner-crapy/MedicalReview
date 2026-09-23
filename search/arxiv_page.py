import urllib.request, urllib.parse, time, json, re
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
CAPPED=[('Q01','abs:"multi-agent" AND abs:"medical"'),
        ('Q02','abs:"multi-agent" AND abs:"clinical"'),
        ('Q03','abs:"large language model" AND abs:"medical question answering"'),
        ('Q07','abs:"agents" AND abs:"diagnosis" AND abs:"large language model"'),
        ('Q08','abs:"collaboration" AND abs:"large language model" AND abs:"medical"'),
        ('Q10','abs:"multi-agent" AND abs:"healthcare"'),
        ('Q12','abs:"multi-agent" AND abs:"question answering" AND abs:"LLM"')]
rows={r['arxiv_id']:r for r in json.load(open('search/arxiv_raw.json'))}
added=0
for qid,q in CAPPED:
    for start in (100,200,300):
        url='http://export.arxiv.org/api/query?'+urllib.parse.urlencode({
            'search_query':q,'start':start,'max_results':100,
            'sortBy':'submittedDate','sortOrder':'descending'})
        try: raw=urllib.request.urlopen(url,timeout=60).read()
        except Exception as e: print(qid,start,'ERR',e); time.sleep(3); continue
        root=ET.fromstring(raw); n=0
        for e in root.findall('a:entry',NS):
            aid=e.find('a:id',NS).text.strip()
            m=re.search(r'abs/([0-9]+\.[0-9]+)(v\d+)?$',aid)
            if not m: continue
            k=m.group(1); n+=1
            if k in rows:
                if qid not in rows[k]['queries']: rows[k]['queries'].append(qid)
                continue
            rows[k]={'arxiv_id':k,'title':' '.join(e.find('a:title',NS).text.split()),
                'abstract':' '.join(e.find('a:summary',NS).text.split()),
                'published':e.find('a:published',NS).text[:10],
                'updated':e.find('a:updated',NS).text[:10],
                'authors':[a.find('a:name',NS).text for a in e.findall('a:author',NS)][:12],
                'n_authors':len(e.findall('a:author',NS)),
                'categories':[c.get('term') for c in e.findall('a:category',NS)],
                'queries':[qid],'pdf':'https://arxiv.org/pdf/%s'%k,'abs_url':'https://arxiv.org/abs/%s'%k}
            added+=1
        print(qid,start,'got',n); time.sleep(3)
        if n<100: break
json.dump(list(rows.values()),open('search/arxiv_raw.json','w'),ensure_ascii=False,indent=1)
print('total unique:',len(rows),'newly added:',added)
