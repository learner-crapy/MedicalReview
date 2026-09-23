import json,os,time,urllib.request
todl=json.load(open('search/scholar_todl.json'))
ok=fail=0
for t,aid in todl:
    fn='documents/arXiv_%s.pdf'%aid
    if os.path.exists(fn) and os.path.getsize(fn)>40000: continue
    try:
        req=urllib.request.Request('https://arxiv.org/pdf/%s'%aid,headers={'User-Agent':'sysrev/1.0 (academic)'})
        d=urllib.request.urlopen(req,timeout=90).read()
        if d[:4]!=b'%PDF': raise ValueError('not pdf')
        open(fn,'wb').write(d); ok+=1; print('OK  %s %s'%(aid,t[:50]),flush=True)
    except Exception as e:
        fail+=1; print('FAIL %s %s'%(aid,str(e)[:40]),flush=True)
    time.sleep(2.5)
print('downloaded %d fail %d'%(ok,fail))
