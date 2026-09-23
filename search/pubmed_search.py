import urllib.request, urllib.parse, time, json, re
import xml.etree.ElementTree as ET
E='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
QUERIES=[
 ('P01','("multi-agent"[tiab] OR multiagent[tiab] OR "multi agent"[tiab] OR "agent-based"[tiab] OR agentic[tiab]) AND ("large language model"[tiab] OR "large language models"[tiab] OR LLM[tiab] OR LLMs[tiab] OR ChatGPT[tiab] OR GPT-4[tiab]) AND (medical[tiab] OR clinical[tiab] OR health[tiab])'),
 ('P02','("large language model"[tiab] OR LLM[tiab] OR LLMs[tiab]) AND (MedQA[tiab] OR MedMCQA[tiab] OR USMLE[tiab] OR "multiple-choice question"[tiab] OR "multiple choice questions"[tiab]) AND (agent[tiab] OR agents[tiab] OR debate[tiab] OR collaboration[tiab] OR ensemble[tiab])'),
 ('P03','(debate[tiab] OR "role-play"[tiab] OR roleplay[tiab] OR "expert panel"[tiab] OR consensus[tiab]) AND ("large language model"[tiab] OR LLM[tiab] OR GPT-4[tiab]) AND (medical[tiab] OR clinical[tiab])'),
]
out={}
for qid,q in QUERIES:
    u=E+'esearch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','term':q,'retmax':300,'retmode':'json','datetype':'pdat','mindate':'2022','maxdate':'2026'})
    ids=json.loads(urllib.request.urlopen(u,timeout=60).read())['esearchresult']['idlist']
    print(qid,'ids',len(ids)); time.sleep(1)
    for i in range(0,len(ids),100):
        chunk=ids[i:i+100]
        u2=E+'efetch.fcgi?'+urllib.parse.urlencode({'db':'pubmed','id':','.join(chunk),'retmode':'xml'})
        raw=urllib.request.urlopen(u2,timeout=90).read(); time.sleep(1)
        root=ET.fromstring(raw)
        for art in root.findall('.//PubmedArticle'):
            pmid=art.findtext('.//PMID')
            ti=' '.join((art.findtext('.//ArticleTitle') or '').split())
            ab=' '.join(' '.join(x.text or '' for x in art.findall('.//Abstract/AbstractText')).split())
            jr=art.findtext('.//Journal/Title') or ''
            yr=art.findtext('.//JournalIssue/PubDate/Year') or art.findtext('.//JournalIssue/PubDate/MedlineDate') or ''
            doi=''
            for idn in art.findall('.//ArticleId'):
                if idn.get('IdType')=='doi': doi=idn.text
            if pmid in out: out[pmid]['queries'].append(qid); continue
            out[pmid]={'pmid':pmid,'title':ti,'abstract':ab,'journal':jr,'year':str(yr)[:4],
                       'doi':doi,'queries':[qid],'link':'https://pubmed.ncbi.nlm.nih.gov/%s/'%pmid}
json.dump(list(out.values()),open('search/pubmed_raw.json','w'),ensure_ascii=False,indent=1)
print('pubmed unique:',len(out))
