import json,urllib.request,urllib.parse,time,os,re
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
PM=json.load(open('search/pubmed_raw.json'))
REC={r['rid']:r for r in json.load(open('screening/records.json'))}
elig=[r for r in PM if REC.get('PM'+r['pmid'],{}).get('tier')=='T1_review']
ids=[r['pmid'] for r in elig]
pmc={}
for i in range(0,len(ids),80):
    ch=ids[i:i+80]
    q='&'.join('id=%s'%x for x in ch)
    u=E+'elink.fcgi?dbfrom=pubmed&db=pmc&retmode=json&'+q
    try: d=json.loads(urllib.request.urlopen(u,timeout=90).read())
    except Exception as e: print('err',str(e)[:50]); time.sleep(3); continue
    for ls in d.get('linksets',[]):
        src=str(ls.get('ids',[None])[0])
        for db in ls.get('linksetdbs',[]):
            if db.get('linkname')=='pubmed_pmc' and db.get('links'):
                pmc[src]='PMC'+str(db['links'][0])
    time.sleep(1.2)
json.dump(pmc,open('search/pmc_map.json','w'),indent=1)
print('有 PMC 全文的：%d / %d'%(len(pmc),len(ids)))
