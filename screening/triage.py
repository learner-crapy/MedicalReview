import json,re,csv
ax=json.load(open('search/arxiv_raw.json')); pm=json.load(open('search/pubmed_raw.json'))
recs=[]
for r in ax: recs.append({'rid':'AX'+r['arxiv_id'],'src':'arxiv','title':r['title'],'abstract':r['abstract'],
    'date':r['published'],'link':r['abs_url'],'pdf':r['pdf'],'queries':','.join(r['queries'])})
for r in pm: recs.append({'rid':'PM'+r['pmid'],'src':'pubmed','title':r['title'],'abstract':r['abstract'],
    'date':r['year'],'link':r['link'],'pdf':'','queries':','.join(r['queries'])})
A=r'multi-?\s?agent|agentic|agent-based|debate|collaborat|cooperat|role-?play|expert panel|tumor board|consensus|ensemble|self-consistency|moderator|orchestrat|panel of|multi-?expert|committee'
B=r'large language model|LLMs?\b|GPT|ChatGPT|Claude|Gemini|LLaMA|Qwen|Mistral|DeepSeek|foundation model|language model'
C=r'MedQA|MedMCQA|MMLU|PubMedQA|USMLE|NBME|MedBullets|CMExam|multiple[- ]choice|question answering|\bQA\b|exam|board certif|licens'
M=r'medical|clinical|health|patient|diagnos|physician|biomedic|nurs|disease|doctor'
BENCH=r'MedQA|MedMCQA|MMLU|PubMedQA|USMLE|NBME|MedBullets|CMExam|CMB\b|MedExQA|MedXpertQA'
def has(p,t): return bool(re.search(p,t,re.I))
for r in recs:
    t=r['title']+' '+r['abstract']
    r['fA'],r['fB'],r['fC'],r['fM'],r['fBench']=has(A,t),has(B,t),has(C,t),has(M,t),has(BENCH,t)
    r['score']=sum([r['fA'],r['fB'],r['fC'],r['fM']])+(2 if r['fBench'] else 0)
    if r['fA'] and r['fB'] and r['fM'] and (r['fBench'] or r['fC']): r['tier']='T1_review'
    elif r['fA'] and r['fB'] and r['fM']: r['tier']='T2_maybe'
    else: r['tier']='T3_out'
recs.sort(key=lambda x:(-x['score'],x['date']),reverse=False)
from collections import Counter
print('records total',len(recs),Counter(r['tier'] for r in recs))
print('with explicit benchmark name:',sum(r['fBench'] for r in recs))
json.dump(recs,open('screening/records.json','w'),ensure_ascii=False,indent=1)
with open('screening/triage.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['rid','src','date','tier','score','fBench','title','link','queries'])
    w.writeheader()
    for r in recs: w.writerow({k:r[k] for k in w.fieldnames})
