# -*- coding: utf-8 -*-
"""生成 documents.md：按发表状态分区登记"""
import json,os,re,glob
ROOT='/Users/dazelu/PycharmProjects/MedicalReview'
import glob as _g
_AX={r['arxiv_id']:r for r in json.load(open(f'{ROOT}/search/arxiv_raw.json'))}
D={}
for _p in _g.glob(f'{ROOT}/documents/arXiv_*.pdf'):
    _a=os.path.basename(_p)[6:-4]
    _r=_AX.get(_a)
    if _r: D['AX'+_a]={'title':_r['title'],'abstract':_r['abstract'],'date':_r['published'],'link':_r['abs_url']}
try:
    for k,v in json.load(open(f'{ROOT}/screening/to_download.json')).items(): D.setdefault(k,v)
except Exception: pass
PM={r['pmid']:r for r in json.load(open(f'{ROOT}/search/pubmed_raw.json'))}
REC={r['rid']:r for r in json.load(open(f'{ROOT}/screening/records.json'))}
PUB=json.load(open(f'{ROOT}/search/pubstatus.json'))
OA=json.load(open(f'{ROOT}/search/openalex_oa.json'))
PMC=json.load(open(f'{ROOT}/search/pmc_map.json'))
DLLOG=json.load(open(f'{ROOT}/search/dl_published_log.json'))

BENCHES=['MedQA','MedMCQA','MMLU','PubMedQA','USMLE','MedBullets','CMExam','MedXpertQA','MedExQA','NBME']
TAGMAP=[(r'multi-?\s?agent|multi-?LLM|multi-?expert','#multi-agent'),(r'debate|argument|adversarial','#debate'),
 (r'role[- ]?play|persona|specialist|expert panel|MDT|multidisciplinary','#role-play'),
 (r'retrieval|RAG|knowledge graph','#rag'),(r'\btool|function call','#tools'),
 (r'ensemble|majority vot|aggregat|mixture of agents','#ensemble'),
 (r'cost|efficien|budget|token|latency|compute|pareto','#cost'),(r'router|routing|adaptive|dynamic','#adaptive'),
 (r'verif|critic|refine|self-correct','#verify'),(r'benchmark|evaluat','#benchmark'),(r'survey|scoping review|systematic review','#survey'),
 (r'diagnos','#diagnosis'),(r'small language model|\bSLM\b|7B|8B|open-?weight','#small-model'),
 (r'hallucinat|safety|risk|bias','#safety'),(r'difficult|complexity','#difficulty')]
def tags(t):
    out=[k for p,k in TAGMAP if re.search(p,t,re.I)]
    out+=['#'+b.lower() for b in BENCHES if re.search(b,t,re.I)]
    return sorted(set(out))
def desc(ab,n=2):
    parts=re.split(r'(?<=[.!?])\s+',(ab or '').strip()); out=[]
    for p in parts[:n]:
        if sum(len(x) for x in out)+len(p)>260 and out: break
        out.append(p)
    t=' '.join(out).strip()
    if t and not t.endswith(('.','!','?')): t=t.rstrip(' ,;:')+'.'
    return t or '(无摘要)'
def is_pub(v):
    if not v or v.get('status')=='not_in_s2': return None
    ven=((v.get('venue') or '')+' '+(v.get('journal') or '')).strip()
    if ven and 'arxiv' not in ven.lower(): return ven
    doi=v.get('doi') or ''
    return 'DOI '+doi if doi and not doi.startswith('10.48550') else None

P1,P2,P3,P4,P5=[],[],[],[],[]   # 已发表+PDF / 已发表+仅全文 / 已发表待手动 / 预印本+PDF / 下载失败
for rid,r in sorted(D.items(),key=lambda kv:kv[1]['date'],reverse=True):
    aid=rid[2:]; fn=f'{ROOT}/documents/arXiv_{aid}.pdf'
    venue=is_pub(PUB.get(aid))
    item={'rid':rid,'title':r['title'],'date':r['date'],'link':r['link'],'venue':venue or 'arXiv 预印本',
          'file':f'documents/arXiv_{aid}.pdf' if os.path.exists(fn) else '',
          'desc':desc(r['abstract']),'tags':tags(r['title']+' '+r['abstract']),
          'cites':(PUB.get(aid) or {}).get('cites')}
    if not item['file']: P5.append(item)
    elif venue: P1.append(item)
    else: P4.append(item)
for pmid,r in PM.items():
    if REC.get('PM'+pmid,{}).get('tier')!='T1_review': continue
    oa=OA.get(pmid,{}); pdf=f'{ROOT}/documents/PMID_{pmid}.pdf'
    ft=PMC.get(pmid)
    item={'rid':'PM'+pmid,'title':r['title'],'date':r['year'],'link':r['link'],
          'venue':r['journal'] or oa.get('venue',''),'doi':r.get('doi',''),
          'file':f'documents/PMID_{pmid}.pdf' if os.path.exists(pdf) else '',
          'fulltext':f'documents/fulltext_pmc/{ft}.txt' if ft and os.path.exists(f'{ROOT}/documents/fulltext_pmc/{ft}.txt') else '',
          'desc':desc(r['abstract']),'tags':tags(r['title']+' '+r['abstract'])}
    if item['file']: P1.append(item)
    elif item['fulltext']: P2.append(item)
    else: P3.append(item)

L=['# 文献登记表 documents.md\n',
   '由 `screening/make_documents_md.py` 自动生成。**按发表状态分区**：优先已发表文献，预印本单列。\n',
   '| 分区 | 内容 | 数量 |','|---|---|---|',
   f'| **Part 1** | **已发表 · 已获取 PDF** | **{len(P1)}** |',
   f'| Part 2 | 已发表 · 仅获取全文文本（出版商 PDF 被拦截，可手动下载） | {len(P2)} |',
   f'| Part 3 | 已发表 · 无开放获取，需手动下载 | {len(P3)} |',
   f'| Part 4 | 预印本（arXiv，尚无正式发表记录）· 已获取 PDF | {len(P4)} |',
   f'| Part 5 | 下载失败，可重试 | {len(P5)} |','',
   f'检索去重后记录 {len(REC)} 条；通过三分面分诊 {sum(1 for r in REC.values() if r["tier"]=="T1_review")} 条。',
   '发表状态经 Semantic Scholar 与 OpenAlex 双源核实；**arXiv 上的论文若已被 NeurIPS/ICLR/ACL/EMNLP/AAAI 等同行评审会议接收，计入 Part 1**（该领域会议即正式发表）。\n',
   '**tag**：`#multi-agent` `#debate` `#role-play` `#rag` `#tools` `#ensemble` `#cost` `#adaptive` `#verify` `#benchmark` `#survey` `#diagnosis` `#small-model` `#safety` `#difficulty` + 基准名。`grep -n "#cost" documents.md` 可定位。\n','---\n']

def block(title,items,note='',show_ft=False):
    L.append('## %s\n'%title)
    if note: L.append('> '+note+'\n')
    if not items: L.append('（无）\n'); return
    L.append('| # | ID | 发表于 | tags | 标题 |\n|---|---|---|---|---|')
    for i,r in enumerate(items,1):
        L.append('| %d | `%s` | %s | %s | %s |'%(i,r['rid'],(r.get('venue') or '')[:34],' '.join(r['tags'][:6]),r['title'][:62]))
    L.append('')
    for i,r in enumerate(items,1):
        L.append('### %s%d. %s\n'%(title.split('·')[0].strip().replace('Part ','P'),i,r['title']))
        meta='- **ID** `%s` · **日期** %s · **发表于** %s'%(r['rid'],r['date'],r.get('venue') or '—')
        if r.get('cites') is not None: meta+=' · **被引** %s'%r['cites']
        if r.get('doi'): meta+=' · **DOI** %s'%r['doi']
        L.append(meta)
        if r.get('file'): L.append('- **PDF** `%s`'%r['file'])
        if show_ft and r.get('fulltext'): L.append('- **全文文本** `%s`（PDF 需手动下载）'%r['fulltext'])
        L.append('- **链接** %s'%r['link'])
        L.append('- **内容** %s'%r['desc'])
        L.append('- **tags** %s\n'%' '.join(r['tags']))

block('Part 1 · 已发表且已获取 PDF',P1,'同行评审期刊论文，以及已被同行评审会议接收的论文（arXiv 存档版）。这是主分析的证据来源。')
block('Part 2 · 已发表 · 仅有全文文本',P2,'出版商 PDF 拦截了程序化下载，但已通过 PMC 取得全文文本，可用于筛选与数据提取。**如需 PDF 请手动下载，命名 `PMID_<pmid>.pdf` 放入 `documents/`。**',show_ft=True)
block('Part 3 · 已发表 · 需手动获取',P3,'订阅期刊且无开放获取版本。**请手动下载后命名 `PMID_<pmid>.pdf` 放入 `documents/`。**')
block('Part 4 · 预印本',P4,'尚未检索到正式发表记录。按本综述的发表优先策略，这些文献仅在其内容对研究问题不可替代时进入主分析，否则仅作背景。')
block('Part 5 · 下载失败',P5,'可重试。')
open(f'{ROOT}/documents.md','w').write('\n'.join(L))
print('Part1 %d | Part2 %d | Part3 %d | Part4 %d | Part5 %d'%(len(P1),len(P2),len(P3),len(P4),len(P5)))
