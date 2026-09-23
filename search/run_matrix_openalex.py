import json,urllib.request,urllib.parse,time,sys
sys.path.insert(0,'search'); from matrix import MATRIX
UA={'User-Agent':'systematic-review-tool/1.0'}
def fetch(u,tries=6):
    for t in range(tries):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception as e:
            if '429' in str(e) or 'timed out' in str(e).lower(): time.sleep(10*(t+1)); continue
            return None
    return None
out={}
try: out=json.load(open('search/matrix_openalex.json'))
except Exception: pass
for dim,qs in MATRIX.items():
    for q in qs:
        f='from_publication_date:2022-01-01,type:article|review|preprint'
        u='https://api.openalex.org/works?per_page=50&search=%s&filter=%s'%(urllib.parse.quote(q),urllib.parse.quote(f,safe=':|,-'))
        d=fetch(u)
        if not d: print('FAIL',dim,q[:40],flush=True); continue
        n=0
        for w in d.get('results',[]):
            wid=w['id'].split('/')[-1]
            src=((w.get('primary_location') or {}).get('source') or {}); loc=w.get('best_oa_location') or {}
            ids=w.get('ids') or {}
            if wid in out:
                out[wid].setdefault('dims',[]).append(dim); continue
            out[wid]={'title':w.get('title') or '','year':w.get('publication_year'),
              'venue':src.get('display_name','') or '','venue_type':src.get('type',''),
              'doi':(w.get('doi') or '').replace('https://doi.org/',''),
              'pmid':(ids.get('pmid','') or '').rstrip('/').split('/')[-1],
              'arxiv':(ids.get('arxiv','') or '').split('/')[-1],
              'type':w.get('type',''),'cites':w.get('cited_by_count'),
              'oa_pdf':loc.get('pdf_url') or '','abstract_inv':bool(w.get('abstract_inverted_index')),
              'dims':[dim],'q':q}
            n+=1
        print('%-20s %-48s +%d (total %d)'%(dim,q[:46],n,len(out)),flush=True)
        time.sleep(4)
json.dump(out,open('search/matrix_openalex.json','w'),ensure_ascii=False,indent=1)
pub=[v for v in out.values() if v['venue'] and 'arxiv' not in v['venue'].lower()]
print('\nOpenAlex 矩阵检索：%d 条，其中正式 venue %d 条'%(len(out),len(pub)))
