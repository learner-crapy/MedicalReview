import json,urllib.request,urllib.parse,time
UA={'User-Agent':'systematic-review (mailto:noreply@example.org)'}
QS=[('O01','multi-agent large language model medical question answering'),
    ('O02','LLM agents medical exam MedQA'),
    ('O03','multi-agent debate clinical decision large language model'),
    ('O04','collaborative large language models medical reasoning'),
    ('O05','multi-agent framework medical multiple choice question answering'),
    ('O06','LLM ensemble medical question answering accuracy'),
    ('O07','agent collaboration USMLE large language model'),
    ('O08','multi-agent system medical benchmark MedMCQA'),
    ('O09','physician expert panel large language model agents'),
    ('O10','cost efficiency multi-agent LLM inference')]
out={}
for qid,q in QS:
    for page in (1,2):
        f='from_publication_date:2022-01-01,type:article|review|preprint'
        u=('https://api.openalex.org/works?per_page=50&page=%d&search=%s&filter=%s'
           %(page,urllib.parse.quote(q),urllib.parse.quote(f,safe=':|,-')))
        try: d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception as e: print(qid,'err',str(e)[:50]); time.sleep(2); break
        res=d.get('results',[])
        for w in res:
            wid=w['id'].split('/')[-1]
            src=((w.get('primary_location') or {}).get('source') or {})
            venue=src.get('display_name','') or ''
            loc=w.get('best_oa_location') or {}
            ids=w.get('ids') or {}
            rec=out.setdefault(wid,{'title':w.get('title') or '','year':w.get('publication_year'),
              'venue':venue,'venue_type':src.get('type',''),'doi':w.get('doi',''),
              'pmid':(ids.get('pmid','') or '').rstrip('/').split('/')[-1],
              'type':w.get('type',''),'cites':w.get('cited_by_count'),
              'oa_pdf':loc.get('pdf_url') or '','queries':[]})
            rec['queries'].append(qid)
        time.sleep(1)
        if len(res)<50: break
json.dump(out,open('search/openalex_search.json','w'),ensure_ascii=False,indent=1)
pub=[v for v in out.values() if v['venue'] and 'arxiv' not in v['venue'].lower()]
print('OpenAlex 命中 %d，其中有正式 venue 的 %d'%(len(out),len(pub)))
from collections import Counter
print(Counter(v['venue'][:40] for v in pub).most_common(12))
