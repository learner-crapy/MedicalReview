# -*- coding: utf-8 -*-
"""论文全部图形。过滤链与 analysis/main_analysis.py 完全一致，可复现。"""
import csv,statistics as st,math,random
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
random.seed(20260923)
R=[r for r in csv.DictReader(open('extraction/data.csv'))]
def f(x):
    try: return float(x)
    except: return None
def base(tiers=('primary',)):
    return [r for r in R if r['pub_status'].startswith('published') and r['eg_tier'] in tiers
            and not r['attribution_flag'] and f(r['delta_acc']) is not None]
FIG='paper/latex/figs/'
P=base()
# Fig1 对照梯度
order=[('zeroshot-CoT-SC','CoT + self-consistency'),('zero-shot','Zero-shot'),
       ('same-backbone-single','Single agent, same backbone'),('same-scale-single','Single model, same scale'),
       ('same-backbone-CoT-noRAG','Same backbone, no retrieval'),('best-single-agent','Strongest single agent')]
data=[[f(x['delta_acc']) for x in P if x['baseline_type']==k] for k,_ in order]
fig,ax=plt.subplots(figsize=(8.0,4.1))
bp=ax.boxplot(data,tick_labels=['%s\n(n=%d)'%(l,len(d)) for (k,l),d in zip(order,data)],
  showfliers=False,widths=.55,patch_artist=True)
for b in bp['boxes']: b.set(facecolor='#dce6f2',edgecolor='#33506e')
for i,d in enumerate(data,1):
    ax.scatter([i+(j-len(d)/2)*0.014 for j in range(len(d))],d,s=10,color='#c0392b',alpha=.5,zorder=3)
ax.axhline(0,color='k',lw=.9); ax.axhline(2,color='#888',ls='--',lw=.9)
ax.set_ylabel(r'$\Delta$Acc (pp)'); ax.set_xlabel('Comparator chosen by the primary study')
ax.set_title('The reported benefit shrinks monotonically as the comparator gets stronger',fontsize=10)
plt.xticks(fontsize=7); plt.tight_layout(); plt.savefig(FIG+'fig1_comparator.pdf'); plt.close()
# Fig4 主结果分布 + 研究级
S=[x for x in P if x['baseline_type']=='best-single-agent']
v=sorted(f(x['delta_acc']) for x in S)
studies={}
for x in S: studies.setdefault(x['arxiv_id'],[]).append(f(x['delta_acc']))
smed=sorted(st.median(d) for d in studies.values())
fig,(a1,a2)=plt.subplots(1,2,figsize=(9.6,4.0),gridspec_kw={'width_ratios':[1.55,1]})
a1.hist(v,bins=26,color='#5b7fa6',edgecolor='white')
a1.axvline(0,color='k',lw=1.1); a1.axvline(2,color='#888',ls=':',lw=1.0)
a1.axvline(st.median(v),color='#c0392b',lw=1.8)
a1.text(st.median(v)-0.5,a1.get_ylim()[1]*0.9,'median %+.2f'%st.median(v),fontsize=8,color='#c0392b',ha='right')
a1.set_xlabel(r'$\Delta$Acc (pp), comparison level'); a1.set_ylabel('comparisons')
a1.set_title('(a) %d comparisons: %d%% negative'%(len(v),round(100*sum(1 for x in v if x<0)/len(v))),fontsize=9.5)
a2.barh(range(len(smed)),smed,color=['#c0392b' if x<0 else '#27ae60' for x in smed],height=.7)
a2.axvline(0,color='k',lw=.9); a2.axvline(2,color='#888',ls=':',lw=.9)
a2.axvline(st.median(smed),color='#2c3e50',lw=1.5)
a2.set_yticks([]); a2.set_xlabel(r'study-level median $\Delta$Acc (pp)')
a2.set_title('(b) %d studies: median %+.2f, %d negative'%(len(smed),st.median(smed),sum(1 for x in smed if x<0)),fontsize=9.5)
plt.tight_layout(); plt.savefig(FIG+'fig4_strongbaseline.pdf'); plt.close()
# Fig2 成本
pts=[x for x in base(('primary','secondary')) if f(x['R_est']) and f(x['R_est'])>=0.5]
fig,ax=plt.subplots(figsize=(6.8,4.2))
for x in pts:
    ax.scatter(f(x['R_est']),f(x['delta_acc']),s=40,alpha=.75,
      color=('#27ae60' if f(x['delta_acc'])>=2 else '#c0392b'),edgecolor='k',linewidth=.3)
ax.set_xscale('log'); ax.axhline(0,color='k',lw=.9); ax.axhline(2,color='#888',ls=':',lw=.9); ax.axvline(1,color='#888',ls='--',lw=.8)
for k in (1,2,4): ax.plot([1.1,25],[k*math.log2(1.1),k*math.log2(25)],color='#ccc',lw=.7,ls=':')
ax.set_xlabel(r'Cost ratio $R$ (MAS calls / baseline calls, log scale)'); ax.set_ylabel(r'$\Delta$Acc (pp)')
ax.set_title('Accuracy gain against inference cost (n=%d, median $R$ = %.1f$\\times$)'%(len(pts),
  st.median([f(x['R_est']) for x in pts])),fontsize=9.5)
plt.tight_layout(); plt.savefig(FIG+'fig2_pareto.pdf'); plt.close()
# Fig3 难度
D=[r for r in R if r['benchmark'].startswith('MedDDx-')]
lv=['Basic','Intermediate','Expert']
import numpy as np
sysn=sorted(set(r['study'] for r in D)); x=np.arange(3); w=0.15
fig,ax=plt.subplots(figsize=(7.2,3.9))
for i,s in enumerate(sysn):
    vals=[f(next(r['delta_acc'] for r in D if r['study']==s and r['benchmark']=='MedDDx-'+l)) for l in lv]
    ax.bar(x+(i-len(sysn)/2)*w+w/2,vals,w,label=s)
med=[st.median([f(r['delta_acc']) for r in D if r['benchmark']=='MedDDx-'+l and r['study']!='MedLA']) for l in lv]
ax.plot(x,med,'k--o',lw=1.6,ms=5,label='median (excl. proposing system)')
ax.axhline(0,color='k',lw=.9); ax.axhline(2,color='#888',ls=':',lw=.9)
ax.set_xticks(x); ax.set_xticklabels(lv); ax.set_ylabel(r'$\Delta$Acc vs same-backbone single agent (pp)')
ax.set_title('Multi-agent gain by item difficulty (MedDDx, LLaMA-3.1-8B)',fontsize=9.5)
ax.legend(fontsize=7,ncol=2,frameon=False); plt.tight_layout(); plt.savefig(FIG+'fig3_difficulty.pdf'); plt.close()
print('4 figs rebuilt with the documented filter chain')
print('  fig1 gradient n per group:',[len(d) for d in data])
print('  fig4 comparisons=%d studies=%d row-median=%.2f study-median=%.2f'%(len(v),len(smed),st.median(v),st.median(smed)))
print('  fig2 n=%d median R=%.1f'%(len(pts),st.median([f(x['R_est']) for x in pts])))
