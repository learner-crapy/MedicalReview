import json,urllib.request,urllib.parse,time
UA={'User-Agent':'systematic-review-tool/1.0'}
out=json.load(open('search/openalex_search.json'))
QS=[('O02','LLM agents medical exam MedQA'),('O03','multi-agent debate clinical decision large language model'),
    ('O04','collaborative large language models medical reasoning'),('O05','multi-agent framework medical multiple choice question answering'),
    ('O06','LLM ensemble medical question answering accuracy'),('O07','agent collaboration USMLE large language model'),
    ('O08','multi-agent system medical benchmark MedMCQA'),('O09','physician expert panel large language model agents'),
    ('O10','cost efficiency multi-agent LLM inference')]
def fetch(u,tries=5):
    for t in range(tries):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception as e:
            if '429' in str(e): time.sleep(12*(t+1)); continue
            return None
    return None
new=0
for qid,q in QS:
    f='from_publication_date:2022-01-01,type:article|review|preprint'
    u=('https://api.openalex.org/works?per_page=50&search=%s&filter=%s'%(urllib.parse.quote(q),urllib.parse.quote(f,safe=':|,-')))
    d=fetch(u)
    if not d: print(qid,'FAILED'); continue
    for w in d.get('results',[]):
        wid=w['id'].split('/')[-1]
        src=((w.get('primary_location') or {}).get('source') or {}); loc=w.get('best_oa_location') or {}
        ids=w.get('ids') or {}
        if wid in out: out[wid]['queries'].append(qid); continue
        out[wid]={'title':w.get('title') or '','year':w.get('publication_year'),'venue':src.get('display_name','') or '',
          'venue_type':src.get('type',''),'doi':w.get('doi',''),'pmid':(ids.get('pmid','') or '').rstrip('/').split('/')[-1],
          'type':w.get('type',''),'cites':w.get('cited_by_count'),'oa_pdf':loc.get('pdf_url') or '','queries':[qid]}
        new+=1
    print(qid,'ok'); time.sleep(6)
json.dump(out,open('search/openalex_search.json','w'),ensure_ascii=False,indent=1)
print('新增',new,'总计',len(out))
