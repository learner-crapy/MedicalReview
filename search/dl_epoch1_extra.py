import json,urllib.request,urllib.parse,time,re,os
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
T=["Auditing multi-agent llm reasoning trees outperforms majority vote and llm-as-judge",
   "Candidate supply and answer selection shape the value of LLM judging in multi-agent systems",
   "Medbench v4 A robust and scalable benchmark for evaluating chinese medical language models",
   "Benchmarking Chinese Medical LLMs A Medbench-based Analysis of Performance Gaps",
   "ClinicalLab Aligning agents for multi-departmental clinical diagnostics in the real world",
   "Inflated excellence or true performance rethinking medical diagnostic benchmarks with dynamic evaluation",
   "EMR Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse",
   "MedGuards Multi-Agent System for Reliable Medical Error Detection and Correction",
   "Mediator-Guided Multi-Agent Collaboration among Open-Source Models for Medical Decision-Making"]
ok=0
for t in T:
    q='ti:"%s"'%re.sub(r'[^A-Za-z0-9 \-]','',t)[:75]
    aid=''
    try:
        raw=urllib.request.urlopen('http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':3}),timeout=45).read()
        for e in ET.fromstring(raw).findall('a:entry',NS):
            ti=' '.join(e.find('a:title',NS).text.split())
            if ti.lower()[:32]==t.lower()[:32]:
                aid=re.search(r'abs/([0-9]+\.[0-9]+)',e.find('a:id',NS).text).group(1); break
    except Exception as e: pass
    time.sleep(3)
    if not aid: print('--          %s'%t[:64],flush=True); continue
    fn='documents/arXiv_%s.pdf'%aid
    if os.path.exists(fn): print('have %s  %s'%(aid,t[:56]),flush=True); continue
    try:
        d=urllib.request.urlopen(urllib.request.Request('https://arxiv.org/pdf/%s'%aid,headers={'User-Agent':'sysrev/1.0'}),timeout=90).read()
        if d[:4]==b'%PDF': open(fn,'wb').write(d); ok+=1; print('OK   %s  %s'%(aid,t[:56]),flush=True)
    except Exception as e: print('FAIL %s %s'%(aid,str(e)[:30]),flush=True)
    time.sleep(2)
print('downloaded',ok)
