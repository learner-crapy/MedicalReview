import json,urllib.request,urllib.parse,time,re,os
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
gap=json.load(open('search/scholar_gap.json'))
UA={'User-Agent':'systematic-review-tool/1.0'}
out=[]
for g in gap:
    t=g['title'].split('(')[0].strip()
    rec={'title':t,'dim':g['dim'],'cites':g['cites'],'meta':g['meta'],'arxiv':'','doi':'','venue':'','oa_pdf':''}
    # arXiv 标题检索
    q='ti:"%s"'%re.sub(r'[^A-Za-z0-9 :\-]','',t)[:80]
    try:
        raw=urllib.request.urlopen('http://export.arxiv.org/api/query?'+urllib.parse.urlencode(
            {'search_query':q,'max_results':3}),timeout=45).read()
        for e in ET.fromstring(raw).findall('a:entry',NS):
            ti=' '.join(e.find('a:title',NS).text.split())
            if ti.lower()[:40]==t.lower()[:40]:
                rec['arxiv']=re.search(r'abs/([0-9]+\.[0-9]+)',e.find('a:id',NS).text).group(1)
                rec['abstract']=' '.join(e.find('a:summary',NS).text.split()); break
    except Exception as e: pass
    time.sleep(3)
    # OpenAlex 标题检索（拿 venue / DOI / OA PDF）
    try:
        u='https://api.openalex.org/works?per_page=3&search='+urllib.parse.quote(t[:90])
        d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=45).read())
        for w in d.get('results',[])[:1]:
            src=((w.get('primary_location') or {}).get('source') or {}); loc=w.get('best_oa_location') or {}
            rec['venue']=src.get('display_name','') or ''
            rec['doi']=(w.get('doi') or '').replace('https://doi.org/','')
            rec['oa_pdf']=loc.get('pdf_url') or ''
            rec.setdefault('abstract','')
    except Exception: pass
    time.sleep(2)
    out.append(rec); print('%-58s arxiv=%-11s venue=%s'%(t[:56],rec['arxiv'],rec['venue'][:28]),flush=True)
json.dump(out,open('search/scholar_gap_resolved.json','w'),ensure_ascii=False,indent=1)
print('\n解析完成：有 arXiv ID %d / 有 OA PDF %d / 共 %d'%(sum(1 for r in out if r['arxiv']),sum(1 for r in out if r['oa_pdf']),len(out)))
