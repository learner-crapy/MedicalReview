import json,os,time,urllib.request
IDS={'2503.07459':'MedAgentsBench (RQ1+RQ4)','2402.18272':'Rethinking bounds: are MA discussions the key (H4)',
 '2503.13657':'Why do multi-agent LLM systems fail (773 cites)','2403.02419':'Are more LLM calls all you need (RQ2 拐点)',
 '2410.02506':'Cut the crap: economical communication (m_context)','2505.23352':'Communication topologies info propagation (m_topology)',
 '2505.22960':'Revisiting MAD as test-time scaling (RQ3+RQ4+COST)','2203.11171':'Self-consistency (对照臂定义源)',
 '2607.05477':'Decision Protocols in MA LLM Conversations (judge 臂)','2603.19677':'GoAgent topology generation',
 '2602.20229':'HieraMAS intra-node mixtures + topology','2506.08292':'From debate to equilibrium (m_agg 第三类)'}
ok=fail=0
for aid,desc in IDS.items():
    fn='documents/arXiv_%s.pdf'%aid
    if os.path.exists(fn) and os.path.getsize(fn)>40000: print('skip',aid); continue
    try:
        d=urllib.request.urlopen(urllib.request.Request('https://arxiv.org/pdf/%s'%aid,
            headers={'User-Agent':'sysrev/1.0 (academic)'}),timeout=90).read()
        if d[:4]!=b'%PDF': raise ValueError('not pdf')
        open(fn,'wb').write(d); ok+=1; print('OK  %s  %s'%(aid,desc),flush=True)
    except Exception as e:
        fail+=1; print('FAIL %s %s'%(aid,str(e)[:40]),flush=True)
    time.sleep(2.5)
print('downloaded %d fail %d'%(ok,fail))
