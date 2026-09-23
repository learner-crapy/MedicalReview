import json,glob,os,urllib.request,time
ids=[os.path.basename(p)[6:-4] for p in glob.glob('documents/arXiv_*.pdf')]
out=json.load(open('search/pubstatus.json'))
todo=[i for i in ids if i not in out]
print('need status for',len(todo))
url='https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,year,venue,publicationVenue,externalIds,publicationTypes,journal,citationCount'
for i in range(0,len(todo),60):
    ch=todo[i:i+60]
    body=json.dumps({'ids':['ARXIV:'+a for a in ch]}).encode()
    req=urllib.request.Request(url,data=body,headers={'Content-Type':'application/json','User-Agent':'sysrev/1.0'})
    res=None
    for a in range(5):
        try: res=json.loads(urllib.request.urlopen(req,timeout=60).read()); break
        except Exception as e: time.sleep(10)
    if not res: continue
    for aid,r in zip(ch,res):
        if not r: out[aid]={'status':'not_in_s2'}; continue
        pv=r.get('publicationVenue') or {}
        out[aid]={'title':r.get('title'),'year':r.get('year'),'venue':r.get('venue') or '',
          'vtype':pv.get('type',''),'doi':(r.get('externalIds') or {}).get('DOI',''),
          'pubtypes':r.get('publicationTypes') or [],'cites':r.get('citationCount'),
          'journal':(r.get('journal') or {}).get('name','')}
    time.sleep(3)
json.dump(out,open('search/pubstatus.json','w'),ensure_ascii=False,indent=1)
def pub(v):
    ven=((v.get('venue') or '')+' '+(v.get('journal') or '')).strip()
    return bool(ven and 'arxiv' not in ven.lower())
print('总状态记录 %d，其中已发表 %d'%(len(out),sum(1 for v in out.values() if pub(v))))
