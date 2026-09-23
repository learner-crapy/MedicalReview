# -*- coding: utf-8 -*-
"""横向（4 个 RQ + 成本维度）× 纵向（每维多条加深检索式）的查询矩阵"""
MATRIX = {
 'RQ1_baseline_eval': [
   'single-agent baseline medical question answering large language model',
   'MedQA evaluation protocol subset sampling reproducibility',
   'medical benchmark evaluation inconsistency large language model',
   'test set size sampling seed medical LLM benchmark',
   'reproducibility crisis evaluation large language model medicine',
   'MedMCQA MMLU medical subset evaluation baseline accuracy',
 ],
 'RQ2_agents_scale': [
   'number of agents scaling multi-agent large language model',
   'how many agents collaboration LLM performance',
   'small language model multi-agent collaboration',
   'model size scaling multi-agent LLM reasoning',
   'agent count ablation multi-agent system',
   'compute budget inference scaling multi-agent',
   'open-weight small models agent collaboration medical',
 ],
 'RQ3_mechanism': [
   'multi-agent debate medical question answering',
   'role-playing specialist agents clinical decision',
   'retrieval augmented multi-agent medical reasoning',
   'verifier critic agent large language model medical',
   'majority voting aggregation large language models medical',
   'heterogeneous large language model ensemble medical',
   'mixture of agents layered aggregation reasoning',
   'self-consistency versus multi-agent debate comparison',
   'hierarchical coordinator agent medical decision making',
   'moderator agent consensus clinical',
 ],
 'RQ4_difficulty': [
   'question difficulty large language model medical exam',
   'hard questions multi-agent large language model',
   'difficulty aware routing large language model',
   'adaptive collaboration complexity medical decision',
   'item difficulty analysis medical licensing examination AI',
   'easy versus hard items language model accuracy',
 ],
 'COST_balance': [
   'inference cost multi-agent large language model',
   'token cost efficiency LLM agents',
   'cost-effective large language model medical deployment',
   'Pareto optimal test-time scaling language model',
   'efficient multi-agent collaboration reduce cost',
   'API cost accuracy tradeoff large language model',
 ],
}
if __name__=='__main__':
    n=sum(len(v) for v in MATRIX.values())
    print('横向维度 %d 个，纵向检索式 %d 条'%(len(MATRIX),n))
    for k,v in MATRIX.items(): print('  %-20s %d' % (k,len(v)))
