import json,urllib.request,urllib.parse,time,re,sys
import xml.etree.ElementTree as ET
sys.path.insert(0,'search'); from matrix import MATRIX
NS={'a':'http://www.w3.org/2005/Atom'}
rows={r['arxiv_id']:r for r in json.load(open('search/arxiv_raw.json'))}
before=len(rows); tagged={}
for dim,qs in MATRIX.items():
    for q in qs:
        terms=[t for t in q.split() if len(t)>3][:6]
        sq=' AND '.join('all:"%s"'%t for t in terms[:4])
        u='http://export.arxiv.org/api/query?'+urllib.parse.urlencode(
            {'search_query':sq,'start':0,'max_results':60,'sortBy':'relevance'})
        try: raw=urllib.request.urlopen(u,timeout=60).read()
        except Exception as e: print('ERR',dim,q[:36],str(e)[:40],flush=True); time.sleep(4); continue
        n=0
        for e in ET.fromstring(raw).findall('a:entry',NS):
            m=re.search(r'abs/([0-9]+\.[0-9]+)',e.find('a:id',NS).text)
            if not m: continue
            k=m.group(1); tagged.setdefault(k,set()).add(dim)
            if k in rows: continue
            rows[k]={'arxiv_id':k,'title':' '.join(e.find('a:title',NS).text.split()),
              'abstract':' '.join(e.find('a:summary',NS).text.split()),
              'published':e.find('a:published',NS).text[:10],'updated':e.find('a:updated',NS).text[:10],
              'authors':[a.find('a:name',NS).text for a in e.findall('a:author',NS)][:12],
              'n_authors':len(e.findall('a:author',NS)),
              'categories':[c.get('term') for c in e.findall('a:category',NS)],
              'queries':['M:'+dim],'pdf':'https://arxiv.org/pdf/%s'%k,'abs_url':'https://arxiv.org/abs/%s'%k}
            n+=1
        print('%-20s %-44s +%d (total %d)'%(dim,q[:42],n,len(rows)),flush=True)
        time.sleep(3.5)
json.dump(list(rows.values()),open('search/arxiv_raw.json','w'),ensure_ascii=False,indent=1)
json.dump({k:sorted(v) for k,v in tagged.items()},open('search/arxiv_dims.json','w'),indent=1)
print('\narXiv：%d -> %d（新增 %d）'%(before,len(rows),len(rows)-before))
