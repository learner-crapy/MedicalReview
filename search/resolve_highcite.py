import json,urllib.request,urllib.parse,time,re
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
TITLES=["Encouraging divergent thinking in large language models through multi-agent debate",
 "More agents is all you need","Should we be going MAD A look at multi-agent debate strategies for LLMs",
 "Towards a science of scaling agent systems","ColaCare Enhancing Electronic Health Record Modeling",
 "Single-agent or multi-agent systems Why not both","Multi-agent evolve LLM self-improve through co-evolution",
 "A survey on collaborative mechanisms between large and small language models",
 "MediQ Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning",
 "Benchmark data contamination of large language models A survey",
 "Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems",
 "MedAgents Large Language Models as Collaborators for Zero-shot Medical Reasoning",
 "Understanding multi-agent LLM frameworks A unified benchmark and experimental analysis",
 "Beyond the leaderboard Rethinking medical benchmarks for large language models",
 "AgentBalance Backbone-then-topology design for cost-effective multi-agent systems",
 "Token economics for LLM agents A dual-view study","Budgeted Multi-Agent Routing Adaptive Role Assignment",
 "AgentTaxo Dissecting and Benchmarking Token Distribution of LLM Multi-Agent Systems",
 "ConfAgents A Conformal-Guided Multi-Agent Framework for Cost-Efficient Medical Diagnosis",
 "The hidden strength of disagreement Unraveling the consensus-diversity tradeoff"]
res={}
for t in TITLES:
    q='ti:"%s"'%re.sub(r'[^A-Za-z0-9 \-]','',t)[:75]
    try:
        raw=urllib.request.urlopen('http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'max_results':3}),timeout=45).read()
        hit=''
        for e in ET.fromstring(raw).findall('a:entry',NS):
            ti=' '.join(e.find('a:title',NS).text.split())
            if ti.lower()[:35]==t.lower()[:35]:
                hit=re.search(r'abs/([0-9]+\.[0-9]+)',e.find('a:id',NS).text).group(1); break
        res[t]=hit; print('%-11s %s'%(hit or '--',t[:62]),flush=True)
    except Exception as e: res[t]=''; print('ERR',t[:40],str(e)[:30],flush=True)
    time.sleep(3.5)
json.dump(res,open('search/highcite_ids.json','w'),ensure_ascii=False,indent=1)
print('resolved',sum(1 for v in res.values() if v),'/',len(res))
