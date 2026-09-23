import json,glob,os,re,time,urllib.request,urllib.parse
ids=[os.path.basename(p)[6:-4] for p in glob.glob('documents/arXiv_*.pdf')]
S2='https://api.semanticscholar.org/graph/v1/paper/arXiv:%s?fields=title,year,venue,publicationVenue,externalIds,publicationTypes,journal,citationCount,openAccessPdf'
out={}
for i,aid in enumerate(ids):
    try:
        r=json.loads(urllib.request.urlopen(urllib.request.Request(S2%aid,
            headers={'User-Agent':'sysrev/1.0'}),timeout=30).read())
    except Exception as e:
        out[aid]={'err':str(e)[:60]}; time.sleep(1.2); continue
    pv=r.get('publicationVenue') or {}
    out[aid]={'title':r.get('title'),'year':r.get('year'),'venue':r.get('venue') or '',
              'venue_type':pv.get('type',''),'venue_name':pv.get('name',''),
              'doi':(r.get('externalIds') or {}).get('DOI',''),
              'pubtypes':r.get('publicationTypes') or [],'cites':r.get('citationCount'),
              'journal':(r.get('journal') or {}).get('name','')}
    time.sleep(1.2)
    if (i+1)%25==0: print('...',i+1,flush=True)
json.dump(out,open('search/pubstatus.json','w'),ensure_ascii=False,indent=1)
pub=[k for k,v in out.items() if v.get('venue') or v.get('doi')]
print('查询',len(out),'篇；有venue或DOI:',len(pub))
