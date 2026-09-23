import sys,re
f=sys.argv[1]; want=sys.argv[2] if len(sys.argv)>2 else 'MedQA'
L=open('extraction/text/%s.txt'%f,errors='ignore').read().split('\n')
hits=[i for i,l in enumerate(L) if re.search(want,l,re.I)]
shown=set()
for h in hits:
    lo,hi=max(0,h-3),min(len(L),h+18)
    body='\n'.join(L[lo:hi])
    if len(re.findall(r'\b\d{2}\.\d\b',body))<4: continue   # 只要真有数字表格
    if lo in shown: continue
    shown.add(lo)
    print('===== lines %d-%d ====='%(lo,hi))
    print(body)
    if len(shown)>=3: break
