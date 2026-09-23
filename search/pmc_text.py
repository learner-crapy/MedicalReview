import json,os,time,urllib.request,re
import xml.etree.ElementTree as ET
pmc=json.load(open('search/pmc_map.json'))
os.makedirs('documents/fulltext_pmc',exist_ok=True)
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&retmode=xml&id='
ok=0;fail=0
items=[(p,c) for p,c in pmc.items() if not os.path.exists('documents/fulltext_pmc/%s.txt'%c)]
for i in range(0,len(items),8):
    ch=items[i:i+8]
    try:
        raw=urllib.request.urlopen(E+','.join(c[3:] for _,c in ch),timeout=90).read()
    except Exception as e:
        fail+=len(ch); time.sleep(2); continue
    try: root=ET.fromstring(raw)
    except Exception: fail+=len(ch); continue
    arts=root.findall('.//article')
    for art in arts:
        pid=None
        for aid in art.iter('article-id'):
            if aid.get('pub-id-type')=='pmcid': pid=(aid.text or '').strip()
        if not pid: continue
        txt=' '.join(''.join(x.itertext()) for x in art.iter('body')) or ''.join(art.itertext())
        txt=re.sub(r'\s+',' ',txt)
        if len(txt)<800: fail+=1; continue
        open('documents/fulltext_pmc/%s.txt'%pid,'w').write(txt); ok+=1
    time.sleep(1.2)
print('PMC 全文抓取：成功 %d，失败/无正文 %d'%(ok,fail))
