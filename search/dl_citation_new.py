import json,os,time,urllib.request,urllib.parse,re
C=json.load(open('search/citation_new_published.json'))
UA={'User-Agent':'systematic-review-tool/1.0'}
BR={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'}
def get(u,h=UA,tries=4):
    for t in range(tries):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=h),timeout=60).read()
        except Exception as e:
            if '429' in str(e): time.sleep(12); continue
            return None
    return None
ok=fail=noa=0; log=[]
for v in C:
    doi=v.get('doi') or ''
    if not doi: noa+=1; log.append((v['title'][:50],'no-doi')); continue
    safe=re.sub(r'[^A-Za-z0-9]','_',doi)[:60]
    fn='documents/DOI_%s.pdf'%safe
    if os.path.exists(fn): continue
    d=get('https://api.openalex.org/works/doi:'+urllib.parse.quote(doi))
    if not d: fail+=1; continue
    w=json.loads(d); loc=w.get('best_oa_location') or {}
    pdf=loc.get('pdf_url') or ''
    v['oa_pdf']=pdf
    if not pdf: noa+=1; log.append((v['title'][:50],'no-oa-pdf')); time.sleep(1); continue
    raw=get(pdf,BR)
    if raw and raw[:4]==b'%PDF':
        open(fn,'wb').write(raw); ok+=1; log.append((v['title'][:50],'OK'))
    else:
        fail+=1; log.append((v['title'][:50],'blocked'))
    time.sleep(1.5)
json.dump(C,open('search/citation_new_published.json','w'),ensure_ascii=False,indent=2)
json.dump(log,open('search/dl_citation_log.json','w'),ensure_ascii=False,indent=1)
print('新下载 %d；无开放 PDF %d；失败 %d'%(ok,noa,fail))
