import json,urllib.request,time
SEEDS={'MedAgents':'2311.10537','MDAgents':'2404.15155','MedAgentBoard':'2505.12371',
       'MoreAgents':'2402.05120','DivergentDebate':'2305.19118','MedPrompt':'2311.16452'}
UA={'User-Agent':'systematic-review-tool/1.0'}
def get(u,tries=6):
    for t in range(tries):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        except Exception as e:
            if '429' in str(e): time.sleep(15*(t+1)); continue
            return None
    return None
out={}
for name,aid in SEEDS.items():
    got=0
    for off in (0,100,200):
        u=('https://api.semanticscholar.org/graph/v1/paper/arXiv:%s/citations?limit=100&offset=%d'
           '&fields=title,year,venue,publicationVenue,externalIds,citationCount,publicationTypes'%(aid,off))
        d=get(u)
        if not d or not d.get('data'): break
        for c in d['data']:
            p=c.get('citingPaper') or {}
            ex=p.get('externalIds') or {}
            key=ex.get('ArXiv') or ex.get('DOI') or p.get('paperId')
            if not key: continue
            r=out.setdefault(key,{'title':p.get('title') or '','year':p.get('year'),
               'venue':p.get('venue') or '','cites':p.get('citationCount'),
               'arxiv':ex.get('ArXiv',''),'doi':ex.get('DOI',''),'seeds':[]})
            r['seeds'].append(name)
        got+=len(d['data']); time.sleep(4)
        if len(d['data'])<100: break
    print('%-16s citations harvested: %d (running total %d)'%(name,got,len(out)),flush=True)
    time.sleep(5)
json.dump(out,open('search/citations.json','w'),ensure_ascii=False,indent=1)
pub=[v for v in out.values() if v['venue'] and 'arxiv' not in v['venue'].lower()]
print('\n引文追溯：%d 篇施引文献，其中有正式 venue 的 %d 篇'%(len(out),len(pub)))
