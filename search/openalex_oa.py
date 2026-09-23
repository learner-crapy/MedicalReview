import json,urllib.request,urllib.parse,time
PM={r['pmid']:r for r in json.load(open('search/pubmed_raw.json'))}
REC={r['rid']:r for r in json.load(open('screening/records.json'))}
elig=[p for p in PM if REC.get('PM'+p,{}).get('tier')=='T1_review']
print('候选已发表文献:',len(elig))
out={}
UA={'User-Agent':'systematic-review (mailto:noreply@example.org)'}
for i in range(0,len(elig),40):
    ch=elig[i:i+40]
    f='pmid:'+'|'.join(ch)
    u='https://api.openalex.org/works?per_page=40&filter='+urllib.parse.quote(f,safe=':|')
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
    except Exception as e:
        print('err',str(e)[:60]); time.sleep(3); continue
    for w in d.get('results',[]):
        pm=(w.get('ids') or {}).get('pmid','').rstrip('/').split('/')[-1]
        loc=w.get('best_oa_location') or {}
        out[pm]={'doi':w.get('doi',''),'oa':w.get('open_access',{}).get('is_oa'),
                 'pdf':loc.get('pdf_url') or '','landing':loc.get('landing_page_url') or '',
                 'venue':((w.get('primary_location') or {}).get('source') or {}).get('display_name',''),
                 'type':w.get('type',''),'cites':w.get('cited_by_count'),
                 'title':(w.get('title') or '')[:90]}
    time.sleep(1)
json.dump(out,open('search/openalex_oa.json','w'),ensure_ascii=False,indent=1)
withpdf=[k for k,v in out.items() if v['pdf']]
print('OpenAlex 命中 %d；有直链 PDF 的 %d'%(len(out),len(withpdf)))
