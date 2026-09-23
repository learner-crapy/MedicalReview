import json,os,time,urllib.request
OA=json.load(open('search/openalex_oa.json'))
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
ok=fail=0; log={}
for pmid,v in OA.items():
    if not v['pdf']: continue
    fn='documents/PMID_%s.pdf'%pmid
    if os.path.exists(fn) and os.path.getsize(fn)>40000: continue
    try:
        d=urllib.request.urlopen(urllib.request.Request(v['pdf'],headers=UA),timeout=75).read()
        if d[:4]!=b'%PDF': raise ValueError('not pdf (%s)'%d[:20])
        open(fn,'wb').write(d); ok+=1; log[pmid]='OK'
    except Exception as e:
        fail+=1; log[pmid]='FAIL '+str(e)[:50]
    time.sleep(1.5)
json.dump(log,open('search/dl_published_log.json','w'),indent=1)
print('已发表文献 PDF：成功 %d  失败 %d'%(ok,fail))
