# -*- coding: utf-8 -*-
"""主分析：聚类稳健统计 + 敏感性分析。论文中所有数字由本脚本产生。"""
import csv,random,statistics as st
random.seed(20260923)
R=[r for r in csv.DictReader(open('extraction/data.csv'))]
def f(x):
    try: return float(x)
    except: return None
def sel(tiers=('primary',),clean=True,exclude_study=None,include_map=False):
    out=[]
    for r in R:
        if not r['pub_status'].startswith('published'): continue
        if r['eg_tier'] not in tiers: continue
        if clean and r['attribution_flag']: continue
        if r['baseline_type']!='best-single-agent': continue
        if f(r['delta_acc']) is None: continue
        if exclude_study and r['arxiv_id']==exclude_study: continue
        out.append((r['arxiv_id'],f(r['delta_acc'])))
    return out
def summarise(rows,label):
    v=[d for _,d in rows]
    studies={}
    for a,d in rows: studies.setdefault(a,[]).append(d)
    smed=[st.median(x) for x in studies.values()]
    # 研究聚类 bootstrap（按研究重抽）
    keys=list(studies); boots=[]
    for _ in range(4000):
        samp=[d for k in (random.choice(keys) for _ in keys) for d in studies[k]]
        boots.append(st.median(samp))
    boots.sort()
    lo,hi=boots[int(.025*len(boots))],boots[int(.975*len(boots))]
    return dict(label=label,n=len(v),k=len(studies),med=st.median(v),
        q1=st.quantiles(v,n=4)[0],q3=st.quantiles(v,n=4)[2],
        neg=sum(1 for x in v if x<0),ge2=sum(1 for x in v if x>=2),
        study_med=st.median(smed),study_neg=sum(1 for x in smed if x<0),
        ci_lo=lo,ci_hi=hi)
main=sel()
S=summarise(main,'主分析')
print('=== 主分析（primary × 已发表 × 归因干净 × 最强单代理对照）===')
print('比较行 n=%d，研究 k=%d'%(S['n'],S['k']))
print('行级中位数 %+.2f pp  IQR [%+.2f, %+.2f]  为负 %d (%.0f%%)  ≥2pp %d (%.0f%%)'%(
  S['med'],S['q1'],S['q3'],S['neg'],100*S['neg']/S['n'],S['ge2'],100*S['ge2']/S['n']))
print('**研究级中位数 %+.2f pp（%d/%d 项研究为负）**'%(S['study_med'],S['study_neg'],S['k']))
print('**研究聚类 bootstrap 95%% CI = [%+.2f, %+.2f]**  %s'%(S['ci_lo'],S['ci_hi'],
  '（含 0 → 无可靠增益）' if S['ci_lo']<0<S['ci_hi'] else ''))
from collections import Counter
c=Counter(a for a,_ in main)
print('\n各研究贡献行数（前 5）：',c.most_common(5))
print('\n=== 敏感性分析 ===')
sens=[('留一：剔除 MedAgentsBench',sel(exclude_study='2503.07459')),
      ('主+次级评测组',sel(tiers=('primary','secondary'))),
      ('不剔除归因存疑系统',sel(clean=False))]
for lab,rows in sens:
    s=summarise(rows,lab)
    print('  %-24s n=%3d k=%2d  行级中位 %+5.2f  研究级中位 %+5.2f  为负 %.0f%%  CI [%+.2f, %+.2f]'%(
      lab,s['n'],s['k'],s['med'],s['study_med'],100*s['neg']/s['n'],s['ci_lo'],s['ci_hi']))
print('\n  留一法（逐项剔除，行级中位数范围）：')
studies=sorted(set(a for a,_ in main))
loo=[summarise(sel(exclude_study=a),a) for a in studies]
print('    %.2f ~ %.2f pp；为负比例 %.0f%% ~ %.0f%%'%(min(x['med'] for x in loo),max(x['med'] for x in loo),
  100*min(x['neg']/x['n'] for x in loo),100*max(x['neg']/x['n'] for x in loo)))
print('\n=== 对照梯度（primary × 已发表 × 归因干净）===')
g={}
for r in R:
    if r['eg_tier']!='primary' or not r['pub_status'].startswith('published') or r['attribution_flag']: continue
    if f(r['delta_acc']) is None: continue
    g.setdefault(r['baseline_type'],[]).append(f(r['delta_acc']))
for k,v in sorted(g.items(),key=lambda kv:-st.median(kv[1])):
    if len(v)>=3: print('  %-26s n=%3d  中位 %+6.2f  为负 %.0f%%'%(k,len(v),st.median(v),100*sum(1 for z in v if z<0)/len(v)))
rr=[f(r['R_est']) for r in R if f(r['R_est'])]
print('\n=== 成本 ===\n  有数值 R 的行 %d；中位 R = %.1f×；R_source: %s'%(len(rr),st.median(rr),
  dict(Counter(r['R_source'] for r in R if r['R_source']))))
