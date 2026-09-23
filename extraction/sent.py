import sys,re
f=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 12
t=open('documents/fulltext_pmc/%s.txt'%f,errors='ignore').read()
sents=re.split(r'(?<=[.!?])\s+',t)
KEY=r'(single[- ]agent|baseline|zero-?shot|multi-?agent|debate|ensemble|collaborat|consensus|our (?:method|framework|system)|accuracy)'
NUM=r'\d{1,2}(?:\.\d+)?\s?%'
hits=[s for s in sents if re.search(NUM,s) and re.search(KEY,s,re.I) and len(s)<420]
for s in hits[:n]: print('•',' '.join(s.split()))
