import sys,re
fn=sys.argv[1]; maxblocks=int(sys.argv[2]) if len(sys.argv)>2 else 3
L=open('extraction/text/%s.txt'%fn,errors='ignore').read().split('\n')
num=re.compile(r'\b\d{1,3}\.\d{1,2}\b')
dense=[i for i,l in enumerate(L) if len(num.findall(l))>=3]
# 合并相邻密集行为块
blocks=[];cur=[]
for i in dense:
    if cur and i-cur[-1]<=3: cur.append(i)
    else:
        if cur: blocks.append(cur)
        cur=[i]
if cur: blocks.append(cur)
blocks.sort(key=lambda b:-len(b))
for b in blocks[:maxblocks]:
    lo,hi=max(0,b[0]-6),min(len(L),b[-1]+3)
    print('===== %s lines %d-%d (%d dense rows) ====='%(fn,lo,hi,len(b)))
    print('\n'.join(L[lo:hi])[:3000]); print()
