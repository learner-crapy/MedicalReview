# -*- coding: utf-8 -*-
import os,re,glob,json,subprocess
ROOT='/Users/dazelu/PycharmProjects/MedicalReview'
BENCH=['MedQA','MedMCQA','MMLU','PubMedQA','MedBullets','CMExam','MedXpertQA','USMLE']
MODEL=r'(GPT-?4o?(?:-mini)?|GPT-?3\.5|GPT-?5|o1|o3|Claude[- ]?[\d.]*\w*|Gemini[- ]?[\d.]*\w*|LLaMA[- ]?[\d.]*\w*|Llama-?\d|Qwen[\d.]*[-\w]*|Mistral[-\w]*|Mixtral[-\w]*|DeepSeek[-\w]*|Meditron[-\w]*|MedPaLM|Med-PaLM|Phi-?\d|Gemma[-\w]*)'
SIZE=r'\b(\d{1,3})\s?[Bb]\b'
rows=[]
for pdf in sorted(glob.glob(f'{ROOT}/documents/*.pdf')):
    base=os.path.basename(pdf)[:-4]
    txt=f'{ROOT}/extraction/text/{base}.txt'
    if not os.path.exists(txt):
        subprocess.run(['pdftotext','-layout',pdf,txt],capture_output=True)
    try: t=open(txt,errors='ignore').read()
    except Exception: continue
    low=t.lower()
    benches=[b for b in BENCH if re.search(b,t,re.I)]
    models=sorted(set(m.group(0) for m in re.finditer(MODEL,t)))[:14]
    sizes=sorted(set(int(m.group(1)) for m in re.finditer(SIZE,t) if 1<=int(m.group(1))<=800))[:12]
    nagents=sorted(set(m.group(1) for m in re.finditer(r'(\d+)\s+agents',t,re.I)))[:8]
    has_cost=bool(re.search(r'\btoken cost|cost of|API cost|inference cost|computational cost|efficienc|\$\s?\d|per query cost|token usage|latency',t,re.I))
    has_base=bool(re.search(r'single[- ]agent|baseline|vanilla|zero[- ]shot|standalone',t,re.I))
    has_abl=bool(re.search(r'ablation',t,re.I))
    has_sc=bool(re.search(r'self[- ]consistency|majority voting',t,re.I))
    has_diff=bool(re.search(r'difficult|hard questions|complexity level',t,re.I))
    rows.append({'file':base,'pages_chars':len(t),'benches':benches,'models':models,'sizes':sizes,
                 'n_agents_mentions':nagents,'cost':has_cost,'baseline':has_base,'ablation':has_abl,
                 'selfcons':has_sc,'difficulty':has_diff})
json.dump(rows,open(f'{ROOT}/extraction/scan.json','w'),ensure_ascii=False,indent=1)
print('scanned',len(rows))
med=[r for r in rows if any(b in r['benches'] for b in ['MedQA','MedMCQA','PubMedQA','MedBullets','CMExam','MedXpertQA'])]
print('含医学基准:',len(med),'| 其中有基线:',sum(r['baseline'] for r in med),'| 有成本讨论:',sum(r['cost'] for r in med),
      '| 有消融:',sum(r['ablation'] for r in med),'| 有难度:',sum(r['difficulty'] for r in med))
