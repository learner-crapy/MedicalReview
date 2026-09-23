# 文献登记表 documents.md

由 `screening/make_documents_md.py` 自动生成。**按发表状态分区**：优先已发表文献，预印本单列。

| 分区 | 内容 | 数量 |
|---|---|---|
| **Part 1** | **已发表 · 已获取 PDF** | **96** |
| Part 2 | 已发表 · 仅获取全文文本（出版商 PDF 被拦截，可手动下载） | 67 |
| Part 3 | 已发表 · 无开放获取，需手动下载 | 50 |
| Part 4 | 预印本（arXiv，尚无正式发表记录）· 已获取 PDF | 83 |
| Part 5 | 下载失败，可重试 | 6 |

检索去重后记录 2288 条；通过三分面分诊 343 条。
发表状态经 Semantic Scholar 与 OpenAlex 双源核实；**arXiv 上的论文若已被 NeurIPS/ICLR/ACL/EMNLP/AAAI 等同行评审会议接收，计入 Part 1**（该领域会议即正式发表）。

**tag**：`#multi-agent` `#debate` `#role-play` `#rag` `#tools` `#ensemble` `#cost` `#adaptive` `#verify` `#benchmark` `#survey` `#diagnosis` `#small-model` `#safety` `#difficulty` + 基准名。`grep -n "#cost" documents.md` 可定位。

---

## Part 1 · 已发表且已获取 PDF

> 同行评审期刊论文，以及已被同行评审会议接收的论文（arXiv 存档版）。这是主分析的证据来源。

| # | ID | 发表于 | tags | 标题 |
|---|---|---|---|---|
| 1 | `AX2609.01045` | Pacific Rim International Conferen | #benchmark #cost #medqa #rag | AgentFactory: Towards Automated Agentic System Design and Opti |
| 2 | `AX2606.15419` | Journal of the American Medical In | #benchmark #ensemble #medqa #multi-agent #pubmedqa #rag | Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning |
| 3 | `AX2606.10296` | DOI 10.18653/v1/2026.acl-srw.121 | #benchmark #cost #debate #diagnosis #multi-agent #verify | The Confident Liar: Diagnosing Multi-Agent Debate with Log-Pro |
| 4 | `AX2605.17101` | Annual Meeting of the Association  | #adaptive #benchmark #difficulty #multi-agent #rag #role-play | SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Gene |
| 5 | `AX2605.08813` | Annual Meeting of the Association  | #cost #multi-agent #rag | AgentSlimming: Towards Efficient and Cost-Aware Multi-Agent Sy |
| 6 | `AX2605.01566` | DOI 10.18653/v1/2026.acl-srw.1 | #benchmark #cost #debate #ensemble #mmlu #multi-agent | Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Opti |
| 7 | `AX2605.00914` | CAIS Proceedings of the ACM Confer | #adaptive #benchmark #cost #debate #difficulty #mmlu | The Cost of Consensus: Isolated Self-Correction Prevails Over  |
| 8 | `AX2604.17148` | International Conference on Learni | #benchmark #cost #ensemble #medmcqa #mmlu #multi-agent | Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM C |
| 9 | `AX2604.08927` | Annual Meeting of the Association  | #adaptive #cost #diagnosis #difficulty #ensemble #multi-agent | Beyond the Individual: Virtualizing Multi-Disciplinary Reasoni |
| 10 | `AX2607.15280` | DOI 10.18653/v1/2026.findings-acl. | #cost #diagnosis #medqa #multi-agent #rag #verify | GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework |
| 11 | `AX2604.00085` | Annual Meeting of the Association  | #adaptive #benchmark #cost #debate #diagnosis #ensemble | One Panel Does Not Fit All: Case-Adaptive Multi-Agent Delibera |
| 12 | `AX2603.27150` | IEEE International Conference on H | #debate #medqa #multi-agent #pubmedqa #rag | MediHive: A Decentralized Agent Collective for Medical Reasoni |
| 13 | `AX2603.26182` | Proceedings of the 32nd ACM SIGKDD | #adaptive #benchmark #diagnosis #multi-agent #verify | ClinicalAgents: Multi-Agent Orchestration for Clinical Decisio |
| 14 | `AX2602.23864` | Proceedings of the 25th Internatio | #adaptive #benchmark #cost #debate #difficulty #mmlu | RUMAD: Reinforcement-Unifying Multi-Agent Debate |
| 15 | `AX2603.04421` | DOI 10.18653/v1/2026.healing-1.1 | #benchmark #diagnosis #multi-agent #rag #safety #verify | Do Mixed-Vendor Multi-Agent LLMs Improve Clinical Diagnosis? |
| 16 | `AX2602.09379` | Proceedings of the 32nd ACM SIGKDD | #adaptive #benchmark #diagnosis #multi-agent #verify | LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs |
| 17 | `AX2602.10367` | Proceedings of the 32nd ACM SIGKDD | #benchmark #multi-agent #safety #verify | LiveMedBench: A Contamination-Free Medical Benchmark for LLMs  |
| 18 | `AX2601.10581` | European Conference on Information | #benchmark #cost #multi-agent #rag | From Single to Multi-Agent Reasoning: Advancing GeneGPT for Ge |
| 19 | `AX2601.19921` | Annual Meeting of the Association  | #adaptive #benchmark #cost #debate #ensemble #multi-agent | Demystifying Multi-Agent Debate: The Role of Confidence and Di |
| 20 | `AX2512.07132` | Conference of the European Chapter | #benchmark #debate #ensemble #multi-agent #rag #tools | DART: Leveraging Multi-Agent Disagreement for Tool Recruitment |
| 21 | `AX2512.04207` | JAMIA Journal of the American Medi | #adaptive #benchmark #diagnosis #multi-agent #role-play #small-model | Orchestrator Multi-Agent Clinical Decision Support System for  |
| 22 | `AX2511.06727` | AAAI Conference on Artificial Inte | #benchmark #cost #medmcqa #mmlu #multi-agent | S-DAG: A Subject-Based Directed Acyclic Graph for Multi-Agent  |
| 23 | `AX2510.14353` | Big Data and Cognitive Computing B | #adaptive #benchmark #cost #ensemble #medmcqa #medqa | CURE: Confidence-driven Unified Reasoning Ensemble Framework f |
| 24 | `AX2510.10461` | IEEE International Conference on B | #benchmark #diagnosis #multi-agent | MedCoAct: Confidence-Aware Multi-Agent Collaboration for Compl |
| 25 | `AX2509.23725` | AAAI Conference on Artificial Inte | #benchmark #multi-agent #verify | MedLA: A Logic-Driven Multi-Agent Framework for Complex Medica |
| 26 | `AX2509.11079` | The Web Conference Proceedings of  | #adaptive #benchmark #cost #difficulty #multi-agent | Difficulty-Aware Agentic Orchestration for Query-Specific Mult |
| 27 | `AX2508.14063` | PLOS Digital Health PLOS Digital H | #benchmark #difficulty #medqa #multi-agent #rag | A Multi-Agent Approach to Neurological Clinical Reasoning |
| 28 | `AX2508.03038` | ACM Multimedia Proceedings of the  | #diagnosis #multi-agent | Tree-of-Reasoning: Towards Complex Medical Diagnosis via Multi |
| 29 | `AX2506.09513` | Conference on Empirical Methods in | #benchmark #cost #difficulty #medqa #multi-agent #pubmedqa | ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing  |
| 30 | `AX2506.03750` | Neural Information Processing Syst | #benchmark #diagnosis #multi-agent #rag #tools #verify | MoodAngels: A Retrieval-augmented Multi-agent Framework for Ps |
| 31 | `AX2505.18630` | Conference on Empirical Methods in | #diagnosis #multi-agent | DDO: Dual-Decision Optimization for LLM-Based Medical Consulta |
| 32 | `AX2505.16648` | IEEE International Conference on H | #multi-agent | Collaboration among Multiple Large Language Models for Medical |
| 33 | `AX2504.03699` | IEEE Symposium on Computational In | #multi-agent #verify | Enhancing Clinical Decision-Making: Integrating Multi-Agent Sy |
| 34 | `AX2503.07459` | Patterns Patterns | #benchmark #cost #difficulty | MedicalAgentsBench for Complex Medical Reasoning: Comparing In |
| 35 | `AX2502.20689` | npj Digital Medicine NPJ Digital M | #benchmark #diagnosis #multi-agent #rag #safety #verify | WiseMind: a knowledge-guided multi-agent framework for accurat |
| 36 | `AX2502.13010` | Conference on Empirical Methods in | #adaptive #benchmark #medmcqa #medqa #rag #verify | Agentic Medical Knowledge Graphs Enhance Medical Question Answ |
| 37 | `AX2411.14637` | IEEE International Conference on H | #cost #difficulty #multi-agent #rag | Enhancing Clinical Trial Patient Matching through Knowledge Au |
| 38 | `AX2409.14051` | Proceedings of the 25th Internatio | #cost #debate #multi-agent | GroupDebate: Enhancing the Efficiency of Multi-Agent Debate Us |
| 39 | `AX2404.15155` | Neural Information Processing Syst | #adaptive #benchmark #cost #diagnosis #difficulty #multi-agent | MDAgents: An Adaptive Collaboration of LLMs for Medical Decisi |
| 40 | `AX2402.09742` | International Conference on Comput | #adaptive #benchmark #diagnosis #multi-agent | AI Hospital: Benchmarking Large Language Models in a Multi-age |
| 41 | `PM42769415` | Frontiers in artificial intelligen | #diagnosis #difficulty #rag #role-play #safety #tools | AI-assisted multimodal data integration for precision oncology |
| 42 | `PM42750980` | Frontiers in digital health | #benchmark #cost #diagnosis #rag | Multimodal medical diagnosis: a mini review of LLM-vision fusi |
| 43 | `PM42746192` | Frontiers in medicine | #adaptive #multi-agent #safety #survey #verify | Agentic artificial intelligence in radiology workflow: from im |
| 44 | `PM42736348` | NPJ digital medicine | #benchmark #debate #multi-agent #verify | Multi-Agent collaboration as a complementary architecture for  |
| 45 | `PM42527484` | npj health systems | #benchmark #cost #diagnosis #multi-agent | MAP: evaluation and multi-agent enhancement of large language  |
| 46 | `PM42518951` | Frontiers in neurology | #benchmark #multi-agent #safety | A multimodal multi-agent LLM framework for identifying key dri |
| 47 | `PM42487578` | Clinical and molecular hepatology | #benchmark #diagnosis #rag #role-play #safety | Artificial Intelligence and Generative Models in Hepatology: F |
| 48 | `PM42384291` | Current medical science | #multi-agent #rag #role-play #safety #survey | Real-World Analysis of Organ Transplantation-Specific Agent Ba |
| 49 | `PM42369445` | Frontiers in digital health | #benchmark #cost #diagnosis #multi-agent #rag #safety | Medical visual question answering with multimodal: a systemati |
| 50 | `PM42304602` | Journal of Yeungnam medical scienc | #benchmark #rag #safety #tools | Are artificial intelligence (AI) agents ready for medicine and |
| 51 | `PM42284166` | IEEE journal of biomedical and hea | #adaptive #benchmark #cost #difficulty #multi-agent #verify | AutoMedic: An Automated Evaluation Framework for Clinical Conv |
| 52 | `PM42088811` | Cureus | #cost #safety #small-model #survey #tools #verify | Small Language Models for Developing Agentic AI in Healthcare: |
| 53 | `PM41791854` | Archives of disease in childhood | #benchmark #role-play | AI-simulated clinical consultations: Assessing the potential o |
| 54 | `PM41756436` | Research square | #benchmark #diagnosis #rag #safety #survey #verify | Large Language Models in Clinical Neurology: A Systematic Revi |
| 55 | `PM41708802` | NPJ digital medicine | #benchmark #cost #diagnosis #medqa #safety #tools | Benchmarking large language model-based agent systems for clin |
| 56 | `PM41501128` | NPJ digital medicine | #adaptive #benchmark #multi-agent #rag #role-play #safety | EvoMDT: a self-evolving multi-agent system for structured clin |
| 57 | `PM41235147` | Frontiers in digital health | #benchmark #multi-agent #safety | Evaluating the role of ChatGPT in rehabilitation medicine: a n |
| 58 | `PM41066364` | PLOS digital health | #adaptive #benchmark #cost #ensemble #multi-agent #usmle | Collaborative intelligence in AI: Evaluating the performance o |
| 59 | `PM40831649` | Federal practitioner : for the hea | #cost #diagnosis #multi-agent #rag #role-play | Multiagent AI Systems in Health Care: Envisioning Next-Generat |
| 60 | `PM40590109` | Clinical and experimental otorhino | #benchmark #survey | Applications and Future Perspectives of Large Language Models  |
| 61 | `PM41852004` | Archives of Iranian medicine | #benchmark #diagnosis #survey #tools | Performance of ChatGPT and Gemini Compared with Emergency Phys |
| 62 | `PM41339739` | Scientific reports | #benchmark #diagnosis #ensemble #rag #safety #usmle | Benchmarking large language models on the United States medica |
| 63 | `PM41039560` | BMC medical education | #benchmark #debate #tools | Evaluating large language models using national endodontic spe |
| 64 | `PM40336004` | BMC medical education | #benchmark #cost #diagnosis #multi-agent #rag #tools | Performance of single-agent and multi-agent language models in |
| 65 | `PM40026780` | Advances in medical education and  | #cost #multi-agent #rag | Application of Artificial Intelligence Generated Content in Me |
| 66 | `PM39793017` | JMIR medical informatics | #benchmark #ensemble #tools #verify | Qwen-2.5 Outperforms Other Large Language Models in the Chines |
| 67 | `PM39779926` | Nature medicine | #benchmark #debate #ensemble #medmcqa #medqa #mmlu | Toward expert-level medical question answering with large lang |
| 68 | `PM38196648` | medRxiv : the preprint server for  | #adaptive #cost #ensemble #medmcqa #medqa #pubmedqa | One LLM is not Enough: Harnessing the Power of Ensemble Learni |
| 69 | `PM42769038` | Frontiers in cellular and infectio | #debate #ensemble | Evidence-domain translation in the Lyme disease controversy ov |
| 70 | `PM42662474` | Advances in medical education and  | #rag #tools | Large Language Models as Simulated Candidates in Objective Str |
| 71 | `PM42613010` | Psychiatry investigation | #benchmark #cost #difficulty #tools | Determinants of Trust and Reliance on Artificial Intelligence  |
| 72 | `PM42529250` | Frontiers in digital health | #role-play #tools | The potential of LLMs in generating questions and answers with |
| 73 | `PM42521271` | Journal of Korean medical science | #rag #safety #tools | Large Language Models and the Future of Peer-Reviewed Medical  |
| 74 | `PM42494443` | Frontiers in medicine | #benchmark #cost #nbme #tools | Assessing multiple-choice question quality in internal medicin |
| 75 | `PM42359091` | Frontiers in medicine | #cost #diagnosis #survey #tools | Use of large language models for providing automated feedback  |
| 76 | `PM42337008` | NPJ digital medicine | #benchmark #cost #diagnosis #role-play #verify | IVCM-Insight: automated interactive interpretation of in vivo  |
| 77 | `PM42000879` | NPJ digital medicine | #benchmark #diagnosis #role-play | Development and prospective shadow evaluation of a domain-spec |
| 78 | `PM41998244` | Scientific reports | #benchmark #diagnosis #tools #usmle #verify | Input structure-driven instability and convergence in large la |
| 79 | `PM41991937` | Scientific reports | #benchmark | GPT-4o for Automated Determination of Follow-up Examinations B |
| 80 | `PM41743425` | Frontiers in digital health | #benchmark #diagnosis #safety | Tests of large language models' medical competence and applica |
| 81 | `PM41586949` | European radiology experimental | #benchmark #cost #diagnosis | Reliability of Gemini 2.5 Pro, ChatGPT 4.1, DeepSeek V3, and C |
| 82 | `PM41537252` | Swiss dental journal | #benchmark #difficulty | Leading large language models on a periodontology knowledge te |
| 83 | `PM41458620` | Frontiers in oncology | #benchmark #diagnosis #safety | Benchmarking GPT-5 in radiation oncology: measurable gains, bu |
| 84 | `PM41372695` | Obesity surgery | #benchmark #verify | Performance of Large Language Models in Metabolic Bariatric Su |
| 85 | `PM41286823` | BMC medical education | #benchmark #role-play #survey #tools | Comparing AI chatbot simulation and peer role-play for OSCE pr |
| 86 | `PM41122619` | Cureus | #adaptive #benchmark #diagnosis #rag #safety #tools | Large Language Models Perform at Chance Level in the Diagnosis |
| 87 | `PM40892297` | Clinical neuroradiology | #benchmark #diagnosis #rag | Evaluating Retrieval Augmented Generation-enhanced Large Langu |
| 88 | `PM40779162` | European radiology | #benchmark #cost #diagnosis #tools | GPT-4 for automated sequence-level determination of MRI protoc |
| 89 | `PM40517223` | Radiation oncology (London, Englan | #benchmark #debate #diagnosis #tools | Evaluating large language models as an educational tool for me |
| 90 | `PM39819819` | JMIR medical informatics | #benchmark #rag #verify | Evaluating and Enhancing Japanese Large Language Models for Ge |
| 91 | `PM39552958` | Cureus | #tools | Harnessing Artificial Intelligence for Advancing Medical Manus |
| 92 | `PM39355902` | Obstetrics & gynecology science | #debate #rag | Efficacy of large language models and their potential in Obste |
| 93 | `PM39073590` | World journal of urology | #benchmark #difficulty #rag | Using artificial intelligence to generate medical literature f |
| 94 | `PM38381486` | JMIR medical education | #benchmark #rag | Evaluating Large Language Models for the National Premedical E |
| 95 | `PM37131648` | medRxiv : the preprint server for  | #benchmark #safety | Research Letter: Application of GPT-4 to select next-step anti |
| 96 | `PM36868690` | Artificial intelligence in medicin | #benchmark #role-play #safety | Informing clinical assessment by contextualizing post-hoc expl |

### P11. AgentFactory: Towards Automated Agentic System Design and Optimization

- **ID** `AX2609.01045` · **日期** 2026-09-01 · **发表于** Pacific Rim International Conference on Artificial Intelligence · **被引** 0
- **PDF** `documents/arXiv_2609.01045.pdf`
- **链接** https://arxiv.org/abs/2609.01045
- **内容** Large Language Models (LLMs) have demonstrated remarkable capabilities as powerful components in agentic systems, enabling sophisticated reasoning and complex task execution.
- **tags** #benchmark #cost #medqa #rag

### P12. Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering

- **ID** `AX2606.15419` · **日期** 2026-06-13 · **发表于** Journal of the American Medical Informatics Association JAMIA · **被引** 3
- **PDF** `documents/arXiv_2606.15419.pdf`
- **链接** https://arxiv.org/abs/2606.15419
- **内容** Objective: To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA).
- **tags** #benchmark #ensemble #medqa #multi-agent #pubmedqa #rag #small-model #usmle

### P13. The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge

- **ID** `AX2606.10296` · **日期** 2026-06-09 · **发表于** DOI 10.18653/v1/2026.acl-srw.121 · **被引** 1
- **PDF** `documents/arXiv_2606.10296.pdf`
- **链接** https://arxiv.org/abs/2606.10296
- **内容** Multi-agent debate systems are typically evaluated only on whether the final answer is correct, overlooking the quality of the intermediate reasoning that debate is designed to produce.
- **tags** #benchmark #cost #debate #diagnosis #multi-agent #verify

### P14. SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Generation Framework for Medical Reasoning

- **ID** `AX2605.17101` · **日期** 2026-05-16 · **发表于** Annual Meeting of the Association for Computational Linguistics · **被引** 0
- **PDF** `documents/arXiv_2605.17101.pdf`
- **链接** https://arxiv.org/abs/2605.17101
- **内容** Retrieval-Augmented Generation (RAG) is widely employed to mitigate risks such as hallucinations and knowledge obsolescence in medical question answering, yet its predominantly single-round, static retrieval paradigm misaligns with the multi-stage process of clinical reasoning.
- **tags** #adaptive #benchmark #difficulty #multi-agent #rag #role-play #safety

### P15. AgentSlimming: Towards Efficient and Cost-Aware Multi-Agent Systems

- **ID** `AX2605.08813` · **日期** 2026-05-09 · **发表于** Annual Meeting of the Association for Computational Linguistics · **被引** 2
- **PDF** `documents/arXiv_2605.08813.pdf`
- **链接** https://arxiv.org/abs/2605.08813
- **内容** Large Language Model-based Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in complex tasks.
- **tags** #cost #multi-agent #rag

### P16. Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling

- **ID** `AX2605.01566` · **日期** 2026-05-02 · **发表于** DOI 10.18653/v1/2026.acl-srw.1 · **被引** 3
- **PDF** `documents/arXiv_2605.01566.pdf`
- **链接** https://arxiv.org/abs/2605.01566
- **内容** Advances in inference methods have enabled language models to improve their predictions without additional training. These methods often prioritize raw performance over cost-effective compute usage.
- **tags** #benchmark #cost #debate #ensemble #mmlu #multi-agent #verify

### P17. The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate

- **ID** `AX2605.00914` · **日期** 2026-04-29 · **发表于** CAIS Proceedings of the ACM Conference on AI and Agentic Systems · **被引** 0
- **PDF** `documents/arXiv_2605.00914.pdf`
- **链接** https://arxiv.org/abs/2605.00914
- **内容** Multi-agent debate, where teams of LLMs iteratively exchange rationales and vote on answers, is widely deployed under the assumption that peer review filters hallucinations.
- **tags** #adaptive #benchmark #cost #debate #difficulty #mmlu #multi-agent #rag #safety #small-model #verify

### P18. Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration

- **ID** `AX2604.17148` · **日期** 2026-04-18 · **发表于** International Conference on Learning Representations ... International Conference on Learning Representations · **被引** 15
- **PDF** `documents/arXiv_2604.17148.pdf`
- **链接** https://arxiv.org/abs/2604.17148
- **内容** With an ever-growing zoo of LLMs and benchmarks, the need to orchestrate multiple models for improved task performance has never been more pressing.
- **tags** #benchmark #cost #ensemble #medmcqa #mmlu #multi-agent #rag #verify

### P19. Beyond the Individual: Virtualizing Multi-Disciplinary Reasoning for Clinical Intake via Collaborative Agents

- **ID** `AX2604.08927` · **日期** 2026-04-10 · **发表于** Annual Meeting of the Association for Computational Linguistics · **被引** 3
- **PDF** `documents/arXiv_2604.08927.pdf`
- **链接** https://arxiv.org/abs/2604.08927
- **内容** The initial outpatient consultation is critical for clinical decision-making, yet it is often conducted by a single physician under time pressure, making it prone to cognitive biases and incomplete evidence capture.
- **tags** #adaptive #cost #diagnosis #difficulty #ensemble #multi-agent #role-play #safety #verify

### P110. GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis

- **ID** `AX2607.15280` · **日期** 2026-04-08 · **发表于** DOI 10.18653/v1/2026.findings-acl.1092 · **被引** 1
- **PDF** `documents/arXiv_2607.15280.pdf`
- **链接** https://arxiv.org/abs/2607.15280
- **内容** Sequential diagnosis requires balancing diagnostic accuracy against resource costs through iterative information gathering.
- **tags** #cost #diagnosis #medqa #multi-agent #rag #verify

### P111. One Panel Does Not Fit All: Case-Adaptive Multi-Agent Deliberation for Clinical Prediction

- **ID** `AX2604.00085` · **日期** 2026-03-31 · **发表于** Annual Meeting of the Association for Computational Linguistics · **被引** 0
- **PDF** `documents/arXiv_2604.00085.pdf`
- **链接** https://arxiv.org/abs/2604.00085
- **内容** Large language models applied to clinical prediction exhibit case-level heterogeneity: simple cases yield consistent outputs, while complex cases produce divergent predictions under minor prompt changes.
- **tags** #adaptive #benchmark #cost #debate #diagnosis #ensemble #multi-agent #role-play

### P112. MediHive: A Decentralized Agent Collective for Medical Reasoning

- **ID** `AX2603.27150` · **日期** 2026-03-28 · **发表于** IEEE International Conference on Healthcare Informatics Journal of Healthcare Informatics Research · **被引** 0
- **PDF** `documents/arXiv_2603.27150.pdf`
- **链接** https://arxiv.org/abs/2603.27150
- **内容** Large language models (LLMs) have revolutionized medical reasoning tasks, yet single-agent systems often falter on complex, interdisciplinary problems requiring robust handling of uncertainty and conflicting evidence.
- **tags** #debate #medqa #multi-agent #pubmedqa #rag

### P113. ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory

- **ID** `AX2603.26182` · **日期** 2026-03-27 · **发表于** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · **被引** 5
- **PDF** `documents/arXiv_2603.26182.pdf`
- **链接** https://arxiv.org/abs/2603.26182
- **内容** While Large Language Models (LLMs) have demonstrated potential in healthcare, they often struggle with the complex, non-linear reasoning required for accurate clinical diagnosis.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #verify

### P114. RUMAD: Reinforcement-Unifying Multi-Agent Debate

- **ID** `AX2602.23864` · **日期** 2026-02-27 · **发表于** Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems Proc. of the 25th International Conference on Autonomous Agents and Multiagent Systems · **被引** 2
- **PDF** `documents/arXiv_2602.23864.pdf`
- **链接** https://arxiv.org/abs/2602.23864
- **内容** Multi-agent debate (MAD) systems leverage collective intelligence to enhance reasoning capabilities, yet existing approaches struggle to simultaneously optimize accuracy, consensus formation, and computational efficiency.
- **tags** #adaptive #benchmark #cost #debate #difficulty #mmlu #multi-agent #rag #safety

### P115. Do Mixed-Vendor Multi-Agent LLMs Improve Clinical Diagnosis?

- **ID** `AX2603.04421` · **日期** 2026-02-14 · **发表于** DOI 10.18653/v1/2026.healing-1.1 · **被引** 3
- **PDF** `documents/arXiv_2603.04421.pdf`
- **链接** https://arxiv.org/abs/2603.04421
- **内容** Multi-agent large language model (LLM) systems have emerged as a promising approach for clinical diagnosis, leveraging collaboration among agents to refine medical reasoning.
- **tags** #benchmark #diagnosis #multi-agent #rag #safety #verify

### P116. LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis

- **ID** `AX2602.09379` · **日期** 2026-02-10 · **发表于** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · **被引** 7
- **PDF** `documents/arXiv_2602.09379.pdf`
- **链接** https://arxiv.org/abs/2602.09379
- **内容** Mental disorders are highly prevalent worldwide, but the shortage of psychiatrists and the inherent subjectivity of interview-based diagnosis create substantial barriers to timely and consistent mental-health assessment.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #verify

### P117. LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation

- **ID** `AX2602.10367` · **日期** 2026-02-10 · **发表于** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · **被引** 10
- **PDF** `documents/arXiv_2602.10367.pdf`
- **链接** https://arxiv.org/abs/2602.10367
- **内容** The deployment of Large Language Models (LLMs) in high-stakes clinical settings demands rigorous and reliable evaluation.
- **tags** #benchmark #multi-agent #safety #verify

### P118. From Single to Multi-Agent Reasoning: Advancing GeneGPT for Genomics QA

- **ID** `AX2601.10581` · **日期** 2026-01-15 · **发表于** European Conference on Information Retrieval · **被引** 0
- **PDF** `documents/arXiv_2601.10581.pdf`
- **链接** https://arxiv.org/abs/2601.10581
- **内容** Comprehending genomic information is essential for biomedical research, yet extracting data from complex distributed databases remains challenging.
- **tags** #benchmark #cost #multi-agent #rag

### P119. Demystifying Multi-Agent Debate: The Role of Confidence and Diversity

- **ID** `AX2601.19921` · **日期** 2026-01-09 · **发表于** Annual Meeting of the Association for Computational Linguistics · **被引** 10
- **PDF** `documents/arXiv_2601.19921.pdf`
- **链接** https://arxiv.org/abs/2601.19921
- **内容** Multi-agent debate (MAD) is widely used to improve large language model (LLM) performance through test-time scaling, yet recent work shows that vanilla MAD often underperforms simple majority vote despite higher computational cost.
- **tags** #adaptive #benchmark #cost #debate #ensemble #multi-agent

### P120. DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning

- **ID** `AX2512.07132` · **日期** 2025-12-08 · **发表于** Conference of the European Chapter of the Association for Computational Linguistics · **被引** 4
- **PDF** `documents/arXiv_2512.07132.pdf`
- **链接** https://arxiv.org/abs/2512.07132
- **内容** Specialized visual tools can augment large language models or vision language models with expert knowledge (e.g., grounding, spatial reasoning, medical knowledge, etc.), but knowing which tools to call (and when to call them) can be challenging.
- **tags** #benchmark #debate #ensemble #multi-agent #rag #tools

### P121. Orchestrator Multi-Agent Clinical Decision Support System for Secondary Headache Diagnosis in Primary Care

- **ID** `AX2512.04207` · **日期** 2025-12-03 · **发表于** JAMIA Journal of the American Medical Informatics Association Journal of the American Medical Informatics Association : JAMIA · **被引** 0
- **PDF** `documents/arXiv_2512.04207.pdf`
- **链接** https://arxiv.org/abs/2512.04207
- **内容** Unlike most primary headaches, secondary headaches need specialized care and can have devastating consequences if not treated promptly.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #role-play #small-model

### P122. S-DAG: A Subject-Based Directed Acyclic Graph for Multi-Agent Heterogeneous Reasoning

- **ID** `AX2511.06727` · **日期** 2025-11-10 · **发表于** AAAI Conference on Artificial Intelligence · **被引** 10
- **PDF** `documents/arXiv_2511.06727.pdf`
- **链接** https://arxiv.org/abs/2511.06727
- **内容** Large Language Models (LLMs) have achieved impressive performance in complex reasoning problems. Their effectiveness highly depends on the specific nature of the task, especially the required domain knowledge.
- **tags** #benchmark #cost #medmcqa #mmlu #multi-agent

### P123. CURE: Confidence-driven Unified Reasoning Ensemble Framework for Medical Question Answering

- **ID** `AX2510.14353` · **日期** 2025-10-16 · **发表于** Big Data and Cognitive Computing Big Data Cogn. Comput. · **被引** 0
- **PDF** `documents/arXiv_2510.14353.pdf`
- **链接** https://arxiv.org/abs/2510.14353
- **内容** High-performing medical Large Language Models (LLMs) typically require extensive fine-tuning with substantial computational resources, limiting accessibility for resource-constrained healthcare institutions.
- **tags** #adaptive #benchmark #cost #ensemble #medmcqa #medqa #pubmedqa #rag

### P124. MedCoAct: Confidence-Aware Multi-Agent Collaboration for Complete Clinical Decision

- **ID** `AX2510.10461` · **日期** 2025-10-12 · **发表于** IEEE International Conference on Bioinformatics and Biomedicine 2025 IEEE International Conference on Bioinformatics and Biomedicine (BIBM) · **被引** 6
- **PDF** `documents/arXiv_2510.10461.pdf`
- **链接** https://arxiv.org/abs/2510.10461
- **内容** Autonomous agents utilizing Large Language Models (LLMs) have demonstrated remarkable capabilities in isolated medical tasks like diagnosis and image analysis, but struggle with integrated clinical workflows that connect diagnostic reasoning and medication decisions.
- **tags** #benchmark #diagnosis #multi-agent

### P125. MedLA: A Logic-Driven Multi-Agent Framework for Complex Medical Reasoning with Large Language Models

- **ID** `AX2509.23725` · **日期** 2025-09-28 · **发表于** AAAI Conference on Artificial Intelligence · **被引** 14
- **PDF** `documents/arXiv_2509.23725.pdf`
- **链接** https://arxiv.org/abs/2509.23725
- **内容** Answering complex medical questions requires not only domain expertise and patient-specific information, but also structured and multi-perspective reasoning.
- **tags** #benchmark #multi-agent #verify

### P126. Difficulty-Aware Agentic Orchestration for Query-Specific Multi-Agent Workflows

- **ID** `AX2509.11079` · **日期** 2025-09-14 · **发表于** The Web Conference Proceedings of the ACM Web Conference 2026 · **被引** 23
- **PDF** `documents/arXiv_2509.11079.pdf`
- **链接** https://arxiv.org/abs/2509.11079
- **内容** Large Language Model (LLM)-based agentic systems have shown strong capabilities across various tasks.
- **tags** #adaptive #benchmark #cost #difficulty #multi-agent

### P127. A Multi-Agent Approach to Neurological Clinical Reasoning

- **ID** `AX2508.14063` · **日期** 2025-08-10 · **发表于** PLOS Digital Health PLOS Digital Health · **被引** 3
- **PDF** `documents/arXiv_2508.14063.pdf`
- **链接** https://arxiv.org/abs/2508.14063
- **内容** Large language models (LLMs) have shown promise in medical domains, but their ability to handle specialized neurological reasoning requires systematic evaluation.
- **tags** #benchmark #difficulty #medqa #multi-agent #rag

### P128. Tree-of-Reasoning: Towards Complex Medical Diagnosis via Multi-Agent Reasoning with Evidence Tree

- **ID** `AX2508.03038` · **日期** 2025-08-05 · **发表于** ACM Multimedia Proceedings of the 33rd ACM International Conference on Multimedia · **被引** 15
- **PDF** `documents/arXiv_2508.03038.pdf`
- **链接** https://arxiv.org/abs/2508.03038
- **内容** Large language models (LLMs) have shown great potential in the medical domain. However, existing models still fall short when faced with complex medical diagnosis task in the real world.
- **tags** #diagnosis #multi-agent

### P129. ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning

- **ID** `AX2506.09513` · **日期** 2025-06-11 · **发表于** Conference on Empirical Methods in Natural Language Processing · **被引** 33
- **PDF** `documents/arXiv_2506.09513.pdf`
- **链接** https://arxiv.org/abs/2506.09513
- **内容** Reasoning-based large language models have excelled in mathematics and programming, yet their potential in knowledge-intensive medical question answering remains underexplored and insufficiently validated in clinical contexts.
- **tags** #benchmark #cost #difficulty #medqa #multi-agent #pubmedqa #small-model #verify

### P130. MoodAngels: A Retrieval-augmented Multi-agent Framework for Psychiatry Diagnosis

- **ID** `AX2506.03750` · **日期** 2025-06-04 · **发表于** Neural Information Processing Systems Advances in Neural Information Processing Systems 38 · **被引** 5
- **PDF** `documents/arXiv_2506.03750.pdf`
- **链接** https://arxiv.org/abs/2506.03750
- **内容** The application of AI in psychiatric diagnosis faces significant challenges, including the subjective nature of mental health assessments, symptom overlap across disorders, and privacy constraints limiting data availability.
- **tags** #benchmark #diagnosis #multi-agent #rag #tools #verify

### P131. DDO: Dual-Decision Optimization for LLM-Based Medical Consultation via Multi-Agent Collaboration

- **ID** `AX2505.18630` · **日期** 2025-05-24 · **发表于** Conference on Empirical Methods in Natural Language Processing · **被引** 3
- **PDF** `documents/arXiv_2505.18630.pdf`
- **链接** https://arxiv.org/abs/2505.18630
- **内容** Large Language Models (LLMs) demonstrate strong generalization and reasoning abilities, making them well-suited for complex decision-making tasks such as medical consultation (MC).
- **tags** #diagnosis #multi-agent

### P132. Collaboration among Multiple Large Language Models for Medical Question Answering

- **ID** `AX2505.16648` · **日期** 2025-05-22 · **发表于** IEEE International Conference on Healthcare Informatics 2025 IEEE 13th International Conference on Healthcare Informatics (ICHI) · **被引** 6
- **PDF** `documents/arXiv_2505.16648.pdf`
- **链接** https://arxiv.org/abs/2505.16648
- **内容** Empowered by vast internal knowledge reservoir, the new generation of large language models (LLMs) demonstrate untapped potential to tackle medical tasks.
- **tags** #multi-agent

### P133. Enhancing Clinical Decision-Making: Integrating Multi-Agent Systems with Ethical AI Governance

- **ID** `AX2504.03699` · **日期** 2025-03-25 · **发表于** IEEE Symposium on Computational Intelligence in Bioinformatics and Computational Biology 2025 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology (CIBCB) · **被引** 9
- **PDF** `documents/arXiv_2504.03699.pdf`
- **链接** https://arxiv.org/abs/2504.03699
- **内容** Recent advances in the data-driven medicine approach, which integrates ethically managed and explainable artificial intelligence into clinical decision support systems (CDSS), are critical to ensure reliable and effective patient care.
- **tags** #multi-agent #verify

### P134. MedicalAgentsBench for Complex Medical Reasoning: Comparing Internalized Reasoning Models versus Externalized Agent-based Frameworks

- **ID** `AX2503.07459` · **日期** 2025-03-10 · **发表于** Patterns Patterns · **被引** 43
- **PDF** `documents/arXiv_2503.07459.pdf`
- **链接** https://arxiv.org/abs/2503.07459
- **内容** Complex medical reasoning requires integrating heterogeneous clinical evidence across multiple inference steps.
- **tags** #benchmark #cost #difficulty

### P135. WiseMind: a knowledge-guided multi-agent framework for accurate and empathetic psychiatric diagnosis

- **ID** `AX2502.20689` · **日期** 2025-02-28 · **发表于** npj Digital Medicine NPJ Digital Medicine · **被引** 7
- **PDF** `documents/arXiv_2502.20689.pdf`
- **链接** https://arxiv.org/abs/2502.20689
- **内容** Large Language Models (LLMs) offer promising opportunities to support mental healthcare workflows, yet they often lack the structured clinical reasoning needed for reliable diagnosis and may struggle to provide the emotionally attuned communication essential for patient trust.
- **tags** #benchmark #diagnosis #multi-agent #rag #safety #verify

### P136. Agentic Medical Knowledge Graphs Enhance Medical Question Answering: Bridging the Gap Between LLMs and Evolving Medical Knowledge

- **ID** `AX2502.13010` · **日期** 2025-02-18 · **发表于** Conference on Empirical Methods in Natural Language Processing · **被引** 23
- **PDF** `documents/arXiv_2502.13010.pdf`
- **链接** https://arxiv.org/abs/2502.13010
- **内容** Large Language Models (LLMs) have significantly advanced medical question-answering by leveraging extensive clinical data and medical literature.
- **tags** #adaptive #benchmark #medmcqa #medqa #rag #verify

### P137. Enhancing Clinical Trial Patient Matching through Knowledge Augmentation and Reasoning with Multi-Agent

- **ID** `AX2411.14637` · **日期** 2024-11-22 · **发表于** IEEE International Conference on Healthcare Informatics 2026 IEEE 14th International Conference on Healthcare Informatics (ICHI) · **被引** 1
- **PDF** `documents/arXiv_2411.14637.pdf`
- **链接** https://arxiv.org/abs/2411.14637
- **内容** Matching patients effectively and efficiently for clinical trials is a significant challenge due to the complexity and variability of patient profiles and trial criteria.
- **tags** #cost #difficulty #multi-agent #rag

### P138. GroupDebate: Enhancing the Efficiency of Multi-Agent Debate Using Group Discussion

- **ID** `AX2409.14051` · **日期** 2024-09-21 · **发表于** Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems Proc. of the 25th International Conference on Autonomous Agents and Multiagent Systems · **被引** 72
- **PDF** `documents/arXiv_2409.14051.pdf`
- **链接** https://arxiv.org/abs/2409.14051
- **内容** In recent years, Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse NLP tasks.
- **tags** #cost #debate #multi-agent

### P139. MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making

- **ID** `AX2404.15155` · **日期** 2024-04-22 · **发表于** Neural Information Processing Systems Advances in Neural Information Processing Systems 37 · **被引** 276
- **PDF** `documents/arXiv_2404.15155.pdf`
- **链接** https://arxiv.org/abs/2404.15155
- **内容** Foundation models are becoming valuable tools in medicine. Yet despite their promise, the best way to leverage Large Language Models (LLMs) in complex medical tasks remains an open question.
- **tags** #adaptive #benchmark #cost #diagnosis #difficulty #multi-agent #rag #tools

### P140. AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator

- **ID** `AX2402.09742` · **日期** 2024-02-15 · **发表于** International Conference on Computational Linguistics · **被引** 148
- **PDF** `documents/arXiv_2402.09742.pdf`
- **链接** https://arxiv.org/abs/2402.09742
- **内容** Artificial intelligence has significantly advanced healthcare, particularly through large language models (LLMs) that excel in medical question answering benchmarks.
- **tags** #adaptive #benchmark #diagnosis #multi-agent

### P141. AI-assisted multimodal data integration for precision oncology.

- **ID** `PM42769415` · **日期** 2026 · **发表于** Frontiers in artificial intelligence · **DOI** 10.1016/j.esmoop.2025.105809
- **PDF** `documents/PMID_42769415.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42769415/
- **内容** The complexity of data pertaining to patients diagnosed with cancer requires a shift from fragmented, unimodal diagnostics towards multimodal artificial intelligence (MAI) in order to achieve true precision oncology.
- **tags** #diagnosis #difficulty #rag #role-play #safety #tools #verify

### P142. Multimodal medical diagnosis: a mini review of LLM-vision fusion models in low-resource healthcare settings.

- **ID** `PM42750980` · **日期** 2026 · **发表于** Frontiers in digital health · **DOI** 10.1038/s41591-021-01595-0
- **PDF** `documents/PMID_42750980.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42750980/
- **内容** Recent advances in large language models (LLMs) and vision transformers have enabled multimodal systems that integrate clinical text with medical imaging for diagnostic decision-making.
- **tags** #benchmark #cost #diagnosis #rag

### P143. Agentic artificial intelligence in radiology workflow: from image interpretation to report quality control.

- **ID** `PM42746192` · **日期** 2026 · **发表于** Frontiers in medicine · **DOI** 10.1016/j.acra.2025.05.032
- **PDF** `documents/PMID_42746192.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42746192/
- **内容** Radiology AI has grown past the single-purpose detector.
- **tags** #adaptive #multi-agent #safety #survey #verify

### P144. Multi-Agent collaboration as a complementary architecture for AI-generated medical examination items.

- **ID** `PM42736348` · **日期** 2026 · **发表于** NPJ digital medicine · **DOI** 10.1207/S15324818AME1503_5
- **PDF** `documents/PMID_42736348.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42736348/
- **内容** Qian et al. showed single LLMs can generate acceptable knowledge-based questions but struggle with higher-order reasoning.
- **tags** #benchmark #debate #multi-agent #verify

### P145. MAP: evaluation and multi-agent enhancement of large language models for inpatient pathways.

- **ID** `PM42527484` · **日期** 2026 · **发表于** npj health systems · **DOI** 10.1038/s41586-023-06291-2
- **PDF** `documents/PMID_42527484.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42527484/
- **内容** Inpatient pathways require complex clinical decision-making based on comprehensive patient information, yet research on medical LLMs is limited in this area due to the lack of large-scale datasets.
- **tags** #benchmark #cost #diagnosis #multi-agent

### P146. A multimodal multi-agent LLM framework for identifying key drivers of sleep disorders.

- **ID** `PM42518951` · **日期** 2026 · **发表于** Frontiers in neurology · **DOI** 10.32604/cmc.2023.036779
- **PDF** `documents/PMID_42518951.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42518951/
- **内容** Sleep quality and sleep disorders are influenced by interacting lifestyle, behavioral, physiological, and occupational determinants, but most existing studies examine these factors in isolation.
- **tags** #benchmark #multi-agent #safety

### P147. Artificial Intelligence and Generative Models in Hepatology: From Large Language Models to Digital Pathology in Liver Disease Diagnosis and Treatment.

- **ID** `PM42487578` · **日期** 2026 · **发表于** Clinical and molecular hepatology · **DOI** 10.3350/cmh.2026.0258
- **PDF** `documents/PMID_42487578.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42487578/
- **内容** Artificial intelligence (AI), particularly foundation and generative models, is reshaping the practice of hepatology through enhanced knowledge synthesis, quantitative and reproducible analysis of multimodal data, and personalized clinical decision support.
- **tags** #benchmark #diagnosis #rag #role-play #safety

### P148. Real-World Analysis of Organ Transplantation-Specific Agent Based on Large Language Model in Post-Transplant Self-Management During Off-Hours: A Mixed-Methods Study.

- **ID** `PM42384291` · **日期** 2026 · **发表于** Current medical science · **DOI** 10.7326/ANNALS-25-01738
- **PDF** `documents/PMID_42384291.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42384291/
- **内容** A significant gap exists in medical support for organ transplant patients during out-of-hours (OOH). General large language models (LLMs), affected by AI hallucinations, are unsuitable for complex post-transplant care.
- **tags** #multi-agent #rag #role-play #safety #survey

### P149. Medical visual question answering with multimodal: a systematic mini review (2023-2026).

- **ID** `PM42369445` · **日期** 2026 · **发表于** Frontiers in digital health · **DOI** 10.1016/j.bspc.2025.109908
- **PDF** `documents/PMID_42369445.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42369445/
- **内容** Medical visual question answering (Med-VQA) has emerged as a critical application of artificial intelligence within a short period of time.
- **tags** #benchmark #cost #diagnosis #multi-agent #rag #safety #verify

### P150. Are artificial intelligence (AI) agents ready for medicine and biomedical research? A narrative review.

- **ID** `PM42304602` · **日期** 2026 · **发表于** Journal of Yeungnam medical science · **DOI** 10.48550/arXiv.2604.24658
- **PDF** `documents/PMID_42304602.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42304602/
- **内容** Artificial intelligence (AI) agents extend large language models from single-turn text generation to systems that pursue goals through planning, retrieval, tool use, code execution, memory, feedback, and role coordination.
- **tags** #benchmark #rag #safety #tools

### P151. AutoMedic: An Automated Evaluation Framework for Clinical Conversational Agents with Medical Dataset Grounding.

- **ID** `PM42284166` · **日期** 2026 · **发表于** IEEE journal of biomedical and health informatics · **DOI** 10.1109/JBHI.2026.3703097
- **PDF** `documents/PMID_42284166.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42284166/
- **内容** Evaluating large language models (LLMs) has recently emerged as a critical issue for safe and trustworthy application of LLMs in the medical domain.
- **tags** #adaptive #benchmark #cost #difficulty #multi-agent #verify

### P152. Small Language Models for Developing Agentic AI in Healthcare: A Comprehensive Systematic Review and Critical Analysis.

- **ID** `PM42088811` · **日期** 2026 · **发表于** Cureus · **DOI** 10.7759/cureus.106427
- **PDF** `documents/PMID_42088811.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42088811/
- **内容** Agentic artificial intelligence (AI) systems are emerging as a transformative approach in healthcare, enabling autonomous task execution through integrated reasoning and tool use.
- **tags** #cost #safety #small-model #survey #tools #verify

### P153. AI-simulated clinical consultations: Assessing the potential of ChatGPT to support medical training.

- **ID** `PM41791854` · **日期** 2026 · **发表于** Archives of disease in childhood · **DOI** 10.1016/j.pec.2013.03.022
- **PDF** `documents/PMID_41791854.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41791854/
- **内容** Simulated medical scenarios are useful for evaluating and developing clinical competencies but scheduling them is expensive and time-consuming. Large language models show promise in role-playing tasks.
- **tags** #benchmark #role-play

### P154. Large Language Models in Clinical Neurology: A Systematic Review.

- **ID** `PM41756436` · **日期** 2026 · **发表于** Research square · **DOI** 10.1016/j.amjmed.2025.12.027
- **PDF** `documents/PMID_41756436.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41756436/
- **内容** Large language models (LLMs) are increasingly explored for clinical applications in neurology, yet their real-world utility, safety, and optimal implementation remain uncertain.
- **tags** #benchmark #diagnosis #rag #safety #survey #verify

### P155. Benchmarking large language model-based agent systems for clinical decision tasks.

- **ID** `PM41708802` · **日期** 2026 · **发表于** NPJ digital medicine · **DOI** 10.1038/s41597-022-01899-x
- **PDF** `documents/PMID_41708802.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41708802/
- **内容** Agentic artificial intelligence (AI) systems, designed to autonomously reason, plan, and invoke tools, have shown promise in healthcare, yet systematic benchmarking of their real-world performance remains limited.
- **tags** #benchmark #cost #diagnosis #medqa #safety #tools #verify

### P156. EvoMDT: a self-evolving multi-agent system for structured clinical decision-making in multi-cancer.

- **ID** `PM41501128` · **日期** 2026 · **发表于** NPJ digital medicine · **DOI** 10.1186/s12859-019-3119-4
- **PDF** `documents/PMID_41501128.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41501128/
- **内容** Multidisciplinary tumor boards (MDTs) are central to cancer care but remain constrained by scarce experts and variable decision quality.
- **tags** #adaptive #benchmark #multi-agent #rag #role-play #safety

### P157. Evaluating the role of ChatGPT in rehabilitation medicine: a narrative review.

- **ID** `PM41235147` · **日期** 2025 · **发表于** Frontiers in digital health · **DOI** 10.1097/MD.0000000000041780
- **PDF** `documents/PMID_41235147.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41235147/
- **内容** Chat Generative Pretrained Transformer (ChatGPT) has emerged as a sophisticated artificial intelligence (AI) language model in healthcare.
- **tags** #benchmark #multi-agent #safety

### P158. Collaborative intelligence in AI: Evaluating the performance of a council of AIs on the USMLE.

- **ID** `PM41066364` · **日期** 2025 · **发表于** PLOS digital health · **DOI** 10.1186/s12939-023-01839-0
- **PDF** `documents/PMID_41066364.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41066364/
- **内容** The stochastic nature of next-token generation and resulting response variability in Large Language Models (LLMs) outputs pose challenges in ensuring consistency and accuracy on knowledge assessments.
- **tags** #adaptive #benchmark #cost #ensemble #multi-agent #usmle #verify

### P159. Multiagent AI Systems in Health Care: Envisioning Next-Generation Intelligence.

- **ID** `PM40831649` · **日期** 2025 · **发表于** Federal practitioner : for the health care professionals of the VA, DoD, and PHS · **DOI** 10.1016/S2589-7500
- **PDF** `documents/PMID_40831649.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40831649/
- **内容** Limited staff, rising costs, and regulatory oversight, coupled with the need to achieve clinical endpoints and improve access to care, has made scaling health care operations challenging.
- **tags** #cost #diagnosis #multi-agent #rag #role-play

### P160. Applications and Future Perspectives of Large Language Models in Otolaryngology-Head and Neck Surgery: A Comprehensive Survey.

- **ID** `PM40590109` · **日期** 2025 · **发表于** Clinical and experimental otorhinolaryngology · **DOI** 10.48550/arXiv.2502.11211
- **PDF** `documents/PMID_40590109.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40590109/
- **内容** Since the release of ChatGPT, large language models (LLMs) have rapidly expanded into professional domains, including medicine.
- **tags** #benchmark #survey

### P161. Performance of ChatGPT and Gemini Compared with Emergency Physicians in NSTEMI Cases: A Prospective Cross-sectional Study.

- **ID** `PM41852004` · **日期** 2025 · **发表于** Archives of Iranian medicine · **DOI** 10.7759/cureus.60119
- **PDF** `documents/PMID_41852004.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41852004/
- **内容** Diagnosing non-ST elevation myocardial infarction (NSTEMI) in busy emergency departments is challenging. Artificial intelligence (AI) systems, particularly large language models (LLMs), offer potential as clinical decision support tools.
- **tags** #benchmark #diagnosis #survey #tools

### P162. Benchmarking large language models on the United States medical licensing examination for clinical reasoning and medical licensing scenarios.

- **ID** `PM41339739` · **日期** 2025 · **发表于** Scientific reports · **DOI** 10.1186/s12903-025-06619-6
- **PDF** `documents/PMID_41339739.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41339739/
- **内容** Artificial intelligence (AI) is transforming healthcare by assisting with intricate clinical reasoning and diagnosis.
- **tags** #benchmark #diagnosis #ensemble #rag #safety #usmle

### P163. Evaluating large language models using national endodontic specialty examination questions: are they ready for real-world dentistry?

- **ID** `PM41039560` · **日期** 2025 · **发表于** BMC medical education · **DOI** 10.1038/d41586-023-00288-7
- **PDF** `documents/PMID_41039560.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41039560/
- **内容** Large Language Models (LLMs) are artificial intelligence (AI) systems that simulate human language processing through deep learning techniques and neural networks.
- **tags** #benchmark #debate #tools

### P164. Performance of single-agent and multi-agent language models in Spanish language medical competency exams.

- **ID** `PM40336004` · **日期** 2025 · **发表于** BMC medical education · **DOI** 10.1186/s12982-025-00429-5
- **PDF** `documents/PMID_40336004.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40336004/
- **内容** Large language models (LLMs) like GPT-4o have shown promise in advancing medical decision-making and education. However, their performance in Spanish-language medical contexts remains underexplored.
- **tags** #benchmark #cost #diagnosis #multi-agent #rag #tools

### P165. Application of Artificial Intelligence Generated Content in Medical Examinations.

- **ID** `PM40026780` · **日期** 2025 · **发表于** Advances in medical education and practice · **DOI** 10.1007/s40670-021-01499-1
- **PDF** `documents/PMID_40026780.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40026780/
- **内容** As the rapid development of large language model, artificial intelligence generated content (AIGC) presents novel opportunities for constructing medical examination questions.
- **tags** #cost #multi-agent #rag

### P166. Qwen-2.5 Outperforms Other Large Language Models in the Chinese National Nursing Licensing Examination: Retrospective Cross-Sectional Comparative Study.

- **ID** `PM39793017` · **日期** 2025 · **发表于** JMIR medical informatics · **DOI** 10.3352/jeehp.2024.21.4
- **PDF** `documents/PMID_39793017.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/39793017/
- **内容** Large language models (LLMs) have been proposed as valuable tools in medical education and practice.
- **tags** #benchmark #ensemble #tools #verify

### P167. Toward expert-level medical question answering with large language models.

- **ID** `PM39779926` · **日期** 2025 · **发表于** Nature medicine · **DOI** 10.1093/biomet/26.4.404
- **PDF** `documents/PMID_39779926.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/39779926/
- **内容** Large language models (LLMs) have shown promise in medical question answering, with Med-PaLM being the first to exceed a 'passing' score in United States Medical Licensing Examination style questions.
- **tags** #benchmark #debate #ensemble #medmcqa #medqa #mmlu #pubmedqa #rag #role-play #verify

### P168. One LLM is not Enough: Harnessing the Power of Ensemble Learning for Medical Question Answering.

- **ID** `PM38196648` · **日期** 2023 · **发表于** medRxiv : the preprint server for health sciences · **DOI** 10.2139/ssrn.4359405
- **PDF** `documents/PMID_38196648.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/38196648/
- **内容** To enhance the accuracy and reliability of diverse medical question-answering (QA) tasks and investigate efficient approaches deploying the Large Language Models (LLM) technologies, We developed a novel ensemble learning pipeline by utilizing state-of-the-art LLMs, focusing on improving performance on diverse medical QA datasets.
- **tags** #adaptive #cost #ensemble #medmcqa #medqa #pubmedqa #rag #usmle #verify

### P169. Evidence-domain translation in the Lyme disease controversy over persistent post-treatment symptoms.

- **ID** `PM42769038` · **日期** 2026 · **发表于** Frontiers in cellular and infection microbiology · **DOI** 10.1016/j.lanepe.2021.100142
- **PDF** `documents/PMID_42769038.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42769038/
- **内容** The debate between post-treatment Lyme disease syndrome (PTLDS) and chronic Lyme disease (CLD) reflects different views about the causes and treatment of persistent symptoms attributed to Lyme disease, including symptoms that continue after recommended antibiotic treatment.
- **tags** #debate #ensemble

### P170. Large Language Models as Simulated Candidates in Objective Structured Clinical Examinations: A Rubric-Mapping Proof-of-Concept Study.

- **ID** `PM42662474` · **日期** 2026 · **发表于** Advances in medical education and practice · **DOI** 10.1046/j.1365-2923.2003.01594.x
- **PDF** `documents/PMID_42662474.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42662474/
- **内容** Large language models (LLMs) perform well on knowledge-based medical examinations, but evidence on their utility for performance-based assessments such as Objective Structured Clinical Examinations (OSCEs) remains limited.
- **tags** #rag #tools

### P171. Determinants of Trust and Reliance on Artificial Intelligence in Clinical Settings: A Study on Physicians' Use of Large Language Model in Psychiatric Symptom Assessment.

- **ID** `PM42613010` · **日期** 2026 · **发表于** Psychiatry investigation · **DOI** 10.1145/3544548.3581025
- **PDF** `documents/PMID_42613010.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42613010/
- **内容** This study investigated physicians' use of large language model (LLM)-generated assessments in psychiatric symptom evaluation and factors influencing their acceptance of artificial intelligence (AI) suggestions.
- **tags** #benchmark #cost #difficulty #tools

### P172. The potential of LLMs in generating questions and answers with EHRs.

- **ID** `PM42529250` · **日期** 2026 · **发表于** Frontiers in digital health · **DOI** 10.9734/BJAST/2015/14975
- **PDF** `documents/PMID_42529250.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42529250/
- **内容** This study aimed to generate medical qualification exam questions and their corresponding answers from real-world electronic health records (EHRs) with large language models (LLMs), and to compare their output to that of human medical experts.
- **tags** #role-play #tools

### P173. Large Language Models and the Future of Peer-Reviewed Medical Publishing: Challenges, Editorial Responses, and a Framework for Responsible Integration.

- **ID** `PM42521271` · **日期** 2026 · **发表于** Journal of Korean medical science · **DOI** 10.3346/jkms.2026.41.e306
- **PDF** `documents/PMID_42521271.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42521271/
- **内容** The public release of large language models (LLMs) in late 2022 has fundamentally altered the landscape of scholarly medical publishing.
- **tags** #rag #safety #tools

### P174. Assessing multiple-choice question quality in internal medicine: a comparative analysis of three large language models against expert consensus.

- **ID** `PM42494443` · **日期** 2026 · **发表于** Frontiers in medicine · **DOI** 10.1016/J.MCPDIG.2024.11.005
- **PDF** `documents/PMID_42494443.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42494443/
- **内容** Large language models (LLMs) are increasingly explored for their potential to support quality assurance in medical education assessment.
- **tags** #benchmark #cost #nbme #tools

### P175. Use of large language models for providing automated feedback in medical imaging education: a systematic review.

- **ID** `PM42359091` · **日期** 2026 · **发表于** Frontiers in medicine · **DOI** 10.1038/s41415-025-8383-2
- **PDF** `documents/PMID_42359091.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42359091/
- **内容** Large language models (LLMs) are an emerging form of generative artificial intelligence (AI) with promising applications in medical education, and their ability to provide automated feedback may enhance medical imaging education for trainees.
- **tags** #cost #diagnosis #survey #tools

### P176. IVCM-Insight: automated interactive interpretation of in vivo confocal microscopy.

- **ID** `PM42337008` · **日期** 2026 · **发表于** NPJ digital medicine · **DOI** 10.1038/s41746-026-02926-6
- **PDF** `documents/PMID_42337008.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42337008/
- **内容** In vivo confocal microscopy (IVCM) is a critical ophthalmic examination that provides in vivo cytological and neurological information essential for diagnosing corneal and certain systemic diseases, but its clinical utility is limited by time-consuming interpretation and the need for subspecialty expertise.
- **tags** #benchmark #cost #diagnosis #role-play #verify

### P177. Development and prospective shadow evaluation of a domain-specific large language model for emergency neurological diagnosis.

- **ID** `PM42000879` · **日期** 2026 · **发表于** NPJ digital medicine · **DOI** 10.1080/15265161.2023.2250319
- **PDF** `documents/PMID_42000879.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/42000879/
- **内容** Large language models (LLMs) show promise in emergency medicine; however, their role in emergency neurology remains unclear. We developed a customized LLM, Xuanwu-NeuroAid, and prospectively enrolled 433 patients.
- **tags** #benchmark #diagnosis #role-play

### P178. Input structure-driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency-level MCQs.

- **ID** `PM41998244` · **日期** 2026 · **发表于** Scientific reports · **DOI** 10.1109/ACCESS.2024.3420709
- **PDF** `documents/PMID_41998244.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41998244/
- **内容** Large language models (LLMs) are increasingly incorporated into medical education and clinical learning environments.
- **tags** #benchmark #diagnosis #tools #usmle #verify

### P179. GPT-4o for Automated Determination of Follow-up Examinations Based on Radiology Reports from Clinical Routine.

- **ID** `PM41991937` · **日期** 2026 · **发表于** Scientific reports · **DOI** 10.6004/jnccn.2021.0022
- **PDF** `documents/PMID_41991937.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41991937/
- **内容** Follow-up imaging recommendations vary across radiologists despite established guidelines. We evaluated whether a large language model (GPT-4o) can standardize follow-up timing and modality selection from routine radiology reports.
- **tags** #benchmark

### P180. Tests of large language models' medical competence and application for clinical decision support of musculoskeletal rehabilitation.

- **ID** `PM41743425` · **日期** 2025 · **发表于** Frontiers in digital health · **DOI** 10.1016/j.ijmedinf.2025.105871
- **PDF** `documents/PMID_41743425.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41743425/
- **内容** Large language models (LLMs) are currently abundant and diverse, yet clinicians lack clarity on top performers, with uncertainty about general LLMs' expertise in musculoskeletal rehabilitation.
- **tags** #benchmark #diagnosis #safety

### P181. Reliability of Gemini 2.5 Pro, ChatGPT 4.1, DeepSeek V3, and Claude Opus 4 in generating standardized CMR protocols.

- **ID** `PM41586949` · **日期** 2026 · **发表于** European radiology experimental · **DOI** 10.3390/jcm12134189
- **PDF** `documents/PMID_41586949.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41586949/
- **内容** Artificial intelligence (AI) and large language models (LLMs) are increasingly integrated into radiology, offering new possibilities for advanced imaging techniques, including cardiovascular magnetic resonance (CMR).
- **tags** #benchmark #cost #diagnosis

### P182. Leading large language models on a periodontology knowledge test.

- **ID** `PM41537252` · **日期** 2026 · **发表于** Swiss dental journal · **DOI** 10.61872/sdj-2025-04-04
- **PDF** `documents/PMID_41537252.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41537252/
- **内容** Large language models (LLMs) are increasingly used in clinical and educational settings. However, there is a paucity of data on LLMs' performance in specialized dental domains.
- **tags** #benchmark #difficulty

### P183. Benchmarking GPT-5 in radiation oncology: measurable gains, but persistent need for expert oversight.

- **ID** `PM41458620` · **日期** 2025 · **发表于** Frontiers in oncology · **DOI** 10.1093/jamia/ocad072
- **PDF** `documents/PMID_41458620.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41458620/
- **内容** Large language models (LLM) have shown great potential in clinical decision support and medical education. GPT-5 is a novel LLM system that has been specifically marketed towards oncology use.
- **tags** #benchmark #diagnosis #safety

### P184. Performance of Large Language Models in Metabolic Bariatric Surgery: a Comparative Study.

- **ID** `PM41372695` · **日期** 2026 · **发表于** Obesity surgery · **DOI** 10.1007/s11695-025-07683-1
- **PDF** `documents/PMID_41372695.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41372695/
- **内容** BACKGROUND: The rapid integration of Large Language Models (LLMs) into healthcare necessitates a rigorous evaluation of their performance in specialized medical fields.
- **tags** #benchmark #verify

### P185. Comparing AI chatbot simulation and peer role-play for OSCE preparation: a pilot randomized controlled trial.

- **ID** `PM41286823` · **日期** 2025 · **发表于** BMC medical education · **DOI** 10.1097/MD.0000000000039058
- **PDF** `documents/PMID_41286823.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41286823/
- **内容** Artificial intelligence (AI) is increasingly applied in medical education, but its role in fostering interactive clinical competencies remains underexplored.
- **tags** #benchmark #role-play #survey #tools

### P186. Large Language Models Perform at Chance Level in the Diagnosis of Pediatric Pneumonia Using Chest Radiographs.

- **ID** `PM41122619` · **日期** 2025 · **发表于** Cureus · **DOI** 10.7759/cureus.92596
- **PDF** `documents/PMID_41122619.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/41122619/
- **内容** Introduction Pneumonia remains a significant cause of morbidity and mortality in children globally.
- **tags** #adaptive #benchmark #diagnosis #rag #safety #tools

### P187. Evaluating Retrieval Augmented Generation-enhanced Large Language Models for Question Answering On German Neurovascular Guidelines.

- **ID** `PM40892297` · **日期** 2026 · **发表于** Clinical neuroradiology · **DOI** 10.1002/2056-4538.70009
- **PDF** `documents/PMID_40892297.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40892297/
- **内容** To investigate the feasibility of Retrieval-augmented Generation (RAG)-enhanced Large Language Models (LLMs) in answering questions about two German neurovascular guidelines.
- **tags** #benchmark #diagnosis #rag

### P188. GPT-4 for automated sequence-level determination of MRI protocols based on radiology request forms from clinical routine.

- **ID** `PM40779162` · **日期** 2026 · **发表于** European radiology · **DOI** 10.3390/diagnostics14020171
- **PDF** `documents/PMID_40779162.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40779162/
- **内容** This study evaluated GPT-4's accuracy in MRI sequence selection based on radiology request forms (RRFs), comparing its performance to radiology residents.
- **tags** #benchmark #cost #diagnosis #tools

### P189. Evaluating large language models as an educational tool for meningioma patients: patient and clinician perspectives.

- **ID** `PM40517223` · **日期** 2025 · **发表于** Radiation oncology (London, England) · **DOI** 10.1136/bmjhci-2023-100775
- **PDF** `documents/PMID_40517223.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/40517223/
- **内容** The study explores the potential of ChatGPT, an advanced large language model (LLM) by OpenAI, in educating patients about meningioma, a common type of brain tumor.
- **tags** #benchmark #debate #diagnosis #tools

### P190. Evaluating and Enhancing Japanese Large Language Models for Genetic Counseling Support: Comparative Study of Domain Adaptation and the Development of an Expert-Evaluated Dataset.

- **ID** `PM39819819` · **日期** 2025 · **发表于** JMIR medical informatics · **DOI** 10.48550/arXiv.2405.05904
- **PDF** `documents/PMID_39819819.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/39819819/
- **内容** Advances in genetics have underscored a strong association between genetic factors and health outcomes, leading to an increased demand for genetic counseling services. However, a shortage of qualified genetic counselors poses a significant challenge.
- **tags** #benchmark #rag #verify

### P191. Harnessing Artificial Intelligence for Advancing Medical Manuscript Composition: Applications and Ethical Considerations.

- **ID** `PM39552958` · **日期** 2024 · **发表于** Cureus · **DOI** 10.7759/cureus.71744
- **PDF** `documents/PMID_39552958.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/39552958/
- **内容** Scientific medical manuscripts are fundamental to advancing research and enhancing patient care. With the emergence of artificial intelligence (AI), the process of composing such manuscripts has witnessed profound transformations.
- **tags** #tools

### P192. Efficacy of large language models and their potential in Obstetrics and Gynecology education.

- **ID** `PM39355902` · **日期** 2024 · **发表于** Obstetrics & gynecology science · **DOI** 10.5468/ogs.24211
- **PDF** `documents/PMID_39355902.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/39355902/
- **内容** The performance of large language models (LLMs) and their potential utility in obstetric and gynecological education are topics of ongoing debate.
- **tags** #debate #rag

### P193. Using artificial intelligence to generate medical literature for urology patients: a comparison of three different large language models.

- **ID** `PM39073590` · **日期** 2024 · **发表于** World journal of urology · **DOI** 10.1007/s10916-024-02056-0
- **PDF** `documents/PMID_39073590.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/39073590/
- **内容** Large language models (LLMs) are a form of artificial intelligence (AI) that uses deep learning techniques to understand, summarize and generate content. The potential benefits of LLMs in healthcare is predicted to be immense.
- **tags** #benchmark #difficulty #rag

### P194. Evaluating Large Language Models for the National Premedical Exam in India: Comparative Analysis of GPT-3.5, GPT-4, and Bard.

- **ID** `PM38381486` · **日期** 2024 · **发表于** JMIR medical education · **DOI** 10.1371/journal.pdig.0000205
- **PDF** `documents/PMID_38381486.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/38381486/
- **内容** Large language models (LLMs) have revolutionized natural language processing with their ability to generate human-like text through extensive training on large data sets.
- **tags** #benchmark #rag

### P195. Research Letter: Application of GPT-4 to select next-step antidepressant treatment in major depression.

- **ID** `PM37131648` · **日期** 2023 · **发表于** medRxiv : the preprint server for health sciences · **DOI** 10.1126/science.aax2342
- **PDF** `documents/PMID_37131648.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/37131648/
- **内容** Large language models perform well on a range of academic tasks including medical examinations. The performance of this class of models in psychopharmacology has not been explored.
- **tags** #benchmark #safety

### P196. Informing clinical assessment by contextualizing post-hoc explanations of risk prediction models in type-2 diabetes.

- **ID** `PM36868690` · **日期** 2023 · **发表于** Artificial intelligence in medicine · **DOI** 10.1016/j.artmed.2023.102498
- **PDF** `documents/PMID_36868690.pdf`
- **链接** https://pubmed.ncbi.nlm.nih.gov/36868690/
- **内容** Medical experts may use Artificial Intelligence (AI) systems with greater trust if these are supported by 'contextual explanations' that let the practitioner connect system inferences to their context of use.
- **tags** #benchmark #role-play #safety

## Part 2 · 已发表 · 仅有全文文本

> 出版商 PDF 拦截了程序化下载，但已通过 PMC 取得全文文本，可用于筛选与数据提取。**如需 PDF 请手动下载，命名 `PMID_<pmid>.pdf` 放入 `documents/`。**

| # | ID | 发表于 | tags | 标题 |
|---|---|---|---|---|
| 1 | `PM42761240` | Frontiers in artificial intelligen | #benchmark #rag | An agentic AI framework connecting language models to electron |
| 2 | `PM42737959` | Biology | #benchmark #cost #difficulty | Biological Foundation Models for Complex Disease Research and  |
| 3 | `PM42686940` | npj health systems | #benchmark #cost #difficulty #multi-agent #safety #survey | Generative large language models in medicine: a scoping review |
| 4 | `PM42666549` | Journal of healthcare informatics  | #debate #medqa #multi-agent #pubmedqa #rag | MediHive: A Decentralized Agent Collective for Medical Reasoni |
| 5 | `PM42631313` | Journal of community hospital inte | #benchmark #tools #verify | Artificial Intelligence in Medicine: A Definition of Terms. |
| 6 | `PM42480539` | Cell genomics | #benchmark #tools | Agentic genomics: From pipeline automation to autonomous valid |
| 7 | `PM42444255` | World journal of surgery | #benchmark #cost #rag #safety #tools #verify | Artificial Intelligence in Medical Writing: A Practical and Et |
| 8 | `PM42241685` | JMIR medical education | #benchmark #safety #survey #tools #verify | AI-Assisted Formative Assessment in Clinical Education: From A |
| 9 | `PM42226236` | BMC medical informatics and decisi | #diagnosis #multi-agent #role-play | Performance comparison of a neuro-symbolic large language mode |
| 10 | `PM42146755` | JAMIA open | #benchmark #cost #multi-agent #rag | OEMA: ontology-enhanced multi-agent collaboration framework fo |
| 11 | `PM42059090` | Journal of Korean Neurosurgical So | #cost #tools | Large Language Model and Pediatric Neurosurgery - A Neurosurge |
| 12 | `PM41982676` | Computational and structural biote | #diagnosis #difficulty #multi-agent #rag | A Systematic Literature Review on Integrated Deep Learning and |
| 13 | `PM41874150` | Methods and protocols | #benchmark #cost #multi-agent #tools #usmle #verify | A Review of Multi-Agent AI Systems for Biological and Clinical |
| 14 | `PM41777589` | Biology methods & protocols | #benchmark #cost #debate #diagnosis #ensemble #multi-agent | Large language model-based multiagent collaboration for abstra |
| 15 | `PM41560983` | Learning health systems | #cost #multi-agent #rag | A Perspective on Software Intelligence for Autonomous Transfor |
| 16 | `PM41502536` | JAMIA open | #benchmark #rag #tools #verify | Leveraging generative AI to enhance Synthea model development. |
| 17 | `PM41348953` | JMIR mental health | #multi-agent #rag #role-play #tools | AI-Facilitated Cognitive Reappraisal via Socrates 2.0: Mixed M |
| 18 | `PM41343478` | PLOS digital health | #benchmark #difficulty #medqa #multi-agent #rag | A multi-agent approach to neurological clinical reasoning. |
| 19 | `PM41037756` | JMIR medical education | #rag #tools | Beyond Chatbots: Moving Toward Multistep Modular AI Agents in  |
| 20 | `PM41016012` | Briefings in bioinformatics | #adaptive #role-play | Streamline automated biomedical discoveries with agentic bioin |
| 21 | `PM40405922` | HSS journal : the musculoskeletal  | #cost #role-play #safety #tools | Artificial Intelligence and Musculoskeletal Surgical Applicati |
| 22 | `PM41494532` | Cell reports. Medicine | #benchmark #debate #diagnosis #ensemble #medqa #mmlu | Model confrontation and collaboration: A debate intelligence f |
| 23 | `PM41031082` | ArXiv | #benchmark #small-model | Language Enhanced Model for Eye (LEME): An Open-Source Ophthal |
| 24 | `PM40658884` | Journal of medical Internet resear | #adaptive #benchmark #cost #ensemble #medmcqa #medqa | Large Language Model Synergy for Ensemble Learning in Medical  |
| 25 | `PM40166749` | ArXiv | #benchmark #difficulty #verify | MicroVQA: A Multimodal Reasoning Benchmark for Microscopy-Base |
| 26 | `PM38960731` | Journal of the American Medical In | #benchmark #ensemble #usmle #verify | Reasoning with large language models for medical question answ |
| 27 | `PM38898116` | Scientific reports | #benchmark #cost #ensemble #medmcqa #medqa #mmlu | OpenMedLM: prompt engineering can out-perform fine-tuning in m |
| 28 | `PM38875575` | JMIR AI | #benchmark #diagnosis #tools #verify | Assessment of ChatGPT-3.5's Knowledge in Oncology: Comparative |
| 29 | `PM42751277` | Cureus | #benchmark #cost #role-play | A Medical Large Language Model-Based System Improves History-T |
| 30 | `PM42690903` | JMIR medical education | #benchmark #cost #difficulty #rag #role-play #safety | What Platform Scores Miss: Multidimensional Evaluation of AI T |
| 31 | `PM42668739` | Digital health | #role-play #safety | When documentation follows the patient: Unprofessional languag |
| 32 | `PM42647856` | Journal of medical Internet resear | #benchmark #cost #safety #survey | Improvement of Clinical Practice Guideline Appraisal by Human  |
| 33 | `PM42566745` | JMIR formative research | #adaptive #benchmark #cost #role-play #safety #verify | Iterative Multidisciplinary Development and Evaluation of a Pa |
| 34 | `PM42561407` | JMIR medical education | #benchmark #cost #safety #verify | Prompt Framing and Evidence Requirement for AI-Generated Educa |
| 35 | `PM42530475` | Early intervention in psychiatry | #benchmark #difficulty #safety #tools | Large Language Models for Individualized Psychoeducational Too |
| 36 | `PM42369998` | Digital health | #benchmark #rag #survey | Performance and usability of retrieval-augmented large languag |
| 37 | `PM42369515` | medRxiv : the preprint server for  | #benchmark #rag #safety | LLM-Driven Extraction of NI-RADS and Imaging Tumor Characteris |
| 38 | `PM42348732` | JMIR formative research | #benchmark #difficulty #rag #usmle | Evaluating Source-Based Large Language Models for Preclinical  |
| 39 | `PM42296682` | Clinics (Sao Paulo, Brazil) | #benchmark #rag #usmle | A comparative benchmark of DeepSeek-R1 on the USMLE: surpassin |
| 40 | `PM42257560` | JMIR AI | #benchmark #safety #tools | AI Chatbot Suicide Risk Detection and Response: Human Validati |
| 41 | `PM42166792` | Journal of medical Internet resear | #benchmark #cost #rag #safety #verify | Benchmarking Large Language Models and Prompt Engineering Stra |
| 42 | `PM42140617` | JMIR medical informatics | #benchmark #ensemble #rag #safety #verify | A Multiassessment and Multiprofessional Agents Approach for Me |
| 43 | `PM42054561` | Journal of medical Internet resear | #benchmark #diagnosis #rag #small-model | Automated Identification of Nursing Diagnoses and Intervention |
| 44 | `PM42030750` | International dental journal | #diagnosis #role-play #tools | Context-Guided Mixture-of-Experts with Multimodal LLMs for Les |
| 45 | `PM41950508` | Journal of medical Internet resear | #benchmark #safety #tools #verify | The Alberta Quality Assessment Tool: Risk of Bias (AQAT:RoB) f |
| 46 | `PM41945643` | Journal of medical Internet resear | #benchmark #cost #rag #safety | Initial Insights Into an Institutional Secure Large Language M |
| 47 | `PM41925792` | Japanese journal of radiology | #benchmark #diagnosis | AI achieves board-level performance on the Japan diagnostic ra |
| 48 | `PM41587455` | JMIR medical informatics | #benchmark #diagnosis #difficulty #rag #safety #tools | Multi-Evidence Clinical Reasoning With Retrieval-Augmented Gen |
| 49 | `PM41525685` | JMIR medical education | #benchmark #difficulty #rag #role-play #safety #verify | GPT-4o and OpenAI o1 Performance on the 2024 Spanish Competiti |
| 50 | `PM41499772` | JMIR AI | #benchmark #diagnosis #difficulty #safety #tools #verify | Assessing the Quality of AI Responses to Patient Concerns Abou |
| 51 | `PM41244561` | iScience | #benchmark #rag #tools | ChatMyopia: An AI agent for myopia-related consultation in pri |
| 52 | `PM41237388` | JMIR medical education | #benchmark #tools | Evaluating the Performance of DeepSeek-R1 and DeepSeek-V3 Vers |
| 53 | `PM41236841` | Journal of dental education | #benchmark #cost #diagnosis #rag | Integrating Clinical and Systemic Knowledge in Periodontal and |
| 54 | `PM40960299` | Liver international : official jou | #benchmark #rag | From Guidelines to Real-Time Conversation: Expert-Validated Re |
| 55 | `PM40550010` | JMIR infodemiology | #debate #safety #verify | Public Versus Academic Discourse on ChatGPT in Health Care: Mi |
| 56 | `PM39832358` | Journal of medical Internet resear | #adaptive #benchmark #multi-agent #rag #role-play #safety | Era of Generalist Conversational Artificial Intelligence to Su |
| 57 | `PM39388255` | JMIR research protocols | #multi-agent #tools | A Novel Cognitive Behavioral Therapy-Based Generative AI Tool  |
| 58 | `PM40001164` | BMC medical education | #benchmark #role-play | Quality assurance and validity of AI-generated single best ans |
| 59 | `PM39946168` | Journal of medical Internet resear | #cost #tools | Large Language Models-Supported Thrombectomy Decision-Making i |
| 60 | `PM39753218` | Journal of medical Internet resear | #benchmark #verify | Slit Lamp Report Generation and Question Answering: Developmen |
| 61 | `PM39466245` | JAMA network open | #benchmark #diagnosis #tools | Large Language Model Influence on Diagnostic Reasoning: A Rand |
| 62 | `PM39001375` | Cancers | #benchmark #rag | Testing and Validation of a Custom Retrained Large Language Mo |
| 63 | `PM38533615` | JMIR mental health | #benchmark #debate | Comparing the Perspectives of Generative AI, Mental Health Exp |
| 64 | `PM38517757` | Clinical orthopaedics and related  | #benchmark #difficulty #ensemble #rag #tools | How Does ChatGPT Use Source Information Compared With Google?  |
| 65 | `PM38349725` | JMIR medical education | #benchmark #diagnosis #ensemble #rag #tools | Learning to Make Rare and Complex Diagnoses With Generative AI |
| 66 | `PM38009003` | Journal of medical Internet resear | #benchmark #cost #rag #tools #verify | Evaluation of the Performance of Generative AI Large Language  |
| 67 | `PM37792871` | Revista da Associacao Medica Brasi | #benchmark #tools | Performance of ChatGPT-4 in answering questions from the Brazi |

### P21. An agentic AI framework connecting language models to electronic health records and a biomedical knowledge graph for real-world evidence.

- **ID** `PM42761240` · **日期** 2026 · **发表于** Frontiers in artificial intelligence · **DOI** 10.1177/20552076261427503
- **全文文本** `documents/fulltext_pmc/PMC13585945.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42761240/
- **内容** Accessing large-scale clinical and biomedical databases remains a significant barrier for clinicians and researchers, requiring substantial computational expertise.
- **tags** #benchmark #rag

### P22. Biological Foundation Models for Complex Disease Research and Clinical Translation.

- **ID** `PM42737959` · **日期** 2026 · **发表于** Biology · **DOI** 10.1117/1.JMI.12.6.061412
- **全文文本** `documents/fulltext_pmc/PMC13564972.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42737959/
- **内容** Complex diseases, including cancer, rare genetic disorders, neurodevelopmental and psychiatric conditions, and neurodegenerative diseases, arise from interactions among genetic variation, gene regulation, and cellular states that are difficult to capture using a single data type or biological scale.
- **tags** #benchmark #cost #difficulty

### P23. Generative large language models in medicine: a scoping review of recent methodological advances.

- **ID** `PM42686940` · **日期** 2026 · **发表于** npj health systems · **DOI** 10.52202/075280-1240
- **全文文本** `documents/fulltext_pmc/PMC13538465.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42686940/
- **内容** Generative large language models (LLMs) are rapidly transforming medicine, demonstrating unprecedented capability across a broad spectrum of clinical and biomedical tasks.
- **tags** #benchmark #cost #difficulty #multi-agent #safety #survey #verify

### P24. MediHive: A Decentralized Agent Collective for Medical Reasoning.

- **ID** `PM42666549` · **日期** 2026 · **发表于** Journal of healthcare informatics research · **DOI** 10.3390/app11146421
- **全文文本** `documents/fulltext_pmc/PMC13522319.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42666549/
- **内容** Large language models (LLMs) have revolutionized medical reasoning tasks, yet single-agent systems often falter on complex, interdisciplinary problems requiring robust handling of uncertainty and conflicting evidence.
- **tags** #debate #medqa #multi-agent #pubmedqa #rag

### P25. Artificial Intelligence in Medicine: A Definition of Terms.

- **ID** `PM42631313` · **日期** 2026 · **发表于** Journal of community hospital internal medicine perspectives · **DOI** 10.1001/amajethics.2019.121
- **全文文本** `documents/fulltext_pmc/PMC13496477.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42631313/
- **内容** As artificial intelligence (AI) tools gain traction in clinical, operational, and administrative settings, healthcare professionals must develop a foundational understanding of key AI concepts to engage with these technologies responsibly and effectively.
- **tags** #benchmark #tools #verify

### P26. Agentic genomics: From pipeline automation to autonomous validation.

- **ID** `PM42480539` · **日期** 2026 · **发表于** Cell genomics · **DOI** 10.1038/s41591-018-0300-7
- **全文文本** `documents/fulltext_pmc/PMC13477014.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42480539/
- **内容** Genomics has entered a phase in which AI agents can autonomously discover, configure, execute, and chain bioinformatics operations from natural-language instructions.
- **tags** #benchmark #tools

### P27. Artificial Intelligence in Medical Writing: A Practical and Ethical Framework for Surgical Research and Publication.

- **ID** `PM42444255` · **日期** 2026 · **发表于** World journal of surgery · **DOI** 10.1016/j.lindif.2023.102274
- **全文文本** `documents/fulltext_pmc/PMC13576536.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42444255/
- **内容** Artificial intelligence (AI) is rapidly transforming surgical research and medical publishing by changing how clinicians discover, evaluate, synthesize, and communicate scientific evidence.
- **tags** #benchmark #cost #rag #safety #tools #verify

### P28. AI-Assisted Formative Assessment in Clinical Education: From Algorithms to Agency.

- **ID** `PM42241685` · **日期** 2026 · **发表于** JMIR medical education · **DOI** 10.3389/feduc.2023.1270700
- **全文文本** `documents/fulltext_pmc/PMC13235976.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42241685/
- **内容** Artificial intelligence (AI) is rapidly reshaping clinical education by embedding assessment and feedback into everyday learning activities.
- **tags** #benchmark #safety #survey #tools #verify

### P29. Performance comparison of a neuro-symbolic large language model system versus conventional AI models and human experts in cholangitis management.

- **ID** `PM42226236` · **日期** 2026 · **发表于** BMC medical informatics and decision making · **DOI** 10.1038/s43018-025-00991-6
- **全文文本** `documents/fulltext_pmc/PMC13445689.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42226236/
- **内容** Large language models (LLMs) have shown promising results in medical decision support; Background: Large language models (LLMs) have demonstrated promising outcomes in medical decision support; however, their efficacy in managing complex hepatobiliary conditions remains insufficiently examined.
- **tags** #diagnosis #multi-agent #role-play

### P210. OEMA: ontology-enhanced multi-agent collaboration framework for zero-shot clinical named entity recognition.

- **ID** `PM42146755` · **日期** 2026 · **发表于** JAMIA open · **DOI** 10.1093/jamiaopen/ooag049
- **全文文本** `documents/fulltext_pmc/PMC13175169.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42146755/
- **内容** With the rapid growth of unstructured clinical narratives in electronic health records (EHRs), clinical named entity recognition (NER) has become a crucial technique for extracting structured medical information.
- **tags** #benchmark #cost #multi-agent #rag

### P211. Large Language Model and Pediatric Neurosurgery - A Neurosurgeon's Perspective on the Artificial Nervous System.

- **ID** `PM42059090` · **日期** 2026 · **发表于** Journal of Korean Neurosurgical Society · **DOI** 10.48550/arXiv.2409.1848
- **全文文本** `documents/fulltext_pmc/PMC13341209.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42059090/
- **内容** Large language models (LLMs) are rapidly transforming healthcare, yet their implications for pediatric neurosurgery remain underexplored. This narrative review interprets LLM evolution through a neuroscientific lens familiar to pediatric neurosurgeons.
- **tags** #cost #tools

### P212. A Systematic Literature Review on Integrated Deep Learning and Multiagent Vision-Language Frameworks for Pathology Image Analysis and Report Generation.

- **ID** `PM41982676` · **日期** 2026 · **发表于** Computational and structural biotechnology journal · **DOI** 10.48550/arXiv.2401.16355
- **全文文本** `documents/fulltext_pmc/PMC13073147.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41982676/
- **内容** This systematic literature review investigates the integration of deep learning (DL), vision-language models (VLMs), and multiagent systems in the analysis of pathology images and automated report generation.
- **tags** #diagnosis #difficulty #multi-agent #rag

### P213. A Review of Multi-Agent AI Systems for Biological and Clinical Data Analysis.

- **ID** `PM41874150` · **日期** 2026 · **发表于** Methods and protocols · **DOI** 10.1145/3706598.3713526
- **全文文本** `documents/fulltext_pmc/PMC13010680.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41874150/
- **内容** This review evaluates the emerging paradigm of multi-agent systems (MASs) for biomedical and clinical data analysis, focusing on their ability to overcome the reasoning and reliability limitations of standalone large language models (LLMs).
- **tags** #benchmark #cost #multi-agent #tools #usmle #verify

### P214. Large language model-based multiagent collaboration for abstract screening toward automated systematic reviews.

- **ID** `PM41777589` · **日期** 2026 · **发表于** Biology methods & protocols · **DOI** 10.1109/MCAS.2006.1688199
- **全文文本** `documents/fulltext_pmc/PMC12952526.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41777589/
- **内容** Systematic reviews (SRs) are essential for evidence-based practice but remain labor-intensive, especially during abstract screening.
- **tags** #benchmark #cost #debate #diagnosis #ensemble #multi-agent #rag #survey #verify

### P215. A Perspective on Software Intelligence for Autonomous Transformations in Biomedical Data and Knowledge.

- **ID** `PM41560983` · **日期** 2026 · **发表于** Learning health systems · **DOI** 10.48550/arXiv.2412.15504
- **全文文本** `documents/fulltext_pmc/PMC12813623.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41560983/
- **内容** Persistent knowledge is essential for propagating the learning health system (LHS) cycle. Integral to the cycle are iterative transformations of data into knowledge.
- **tags** #cost #multi-agent #rag

### P216. Leveraging generative AI to enhance Synthea model development.

- **ID** `PM41502536` · **日期** 2026 · **发表于** JAMIA open · **DOI** 10.1001/jama.2023.19052
- **全文文本** `documents/fulltext_pmc/PMC12772637.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41502536/
- **内容** To explore the use of large language models (LLMs) to assist in developing new agent-based disease-specific patient journey models.
- **tags** #benchmark #rag #tools #verify

### P217. AI-Facilitated Cognitive Reappraisal via Socrates 2.0: Mixed Methods Feasibility Study.

- **ID** `PM41348953` · **日期** 2025 · **发表于** JMIR mental health · **DOI** 10.2196/28003
- **全文文本** `documents/fulltext_pmc/PMC12680128.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41348953/
- **内容** Innovative, scalable mental health tools are needed to address systemic provider shortages and accessibility barriers.
- **tags** #multi-agent #rag #role-play #tools

### P218. A multi-agent approach to neurological clinical reasoning.

- **ID** `PM41343478` · **日期** 2025 · **发表于** PLOS digital health · **DOI** 10.1038/s41746-025-01536-y
- **全文文本** `documents/fulltext_pmc/PMC12677565.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41343478/
- **内容** Large language models (LLMs) have demonstrated impressive capabilities in medical domains, yet their ability to handle the specialized reasoning patterns required in clinical neurology warrants systematic evaluation.
- **tags** #benchmark #difficulty #medqa #multi-agent #rag

### P219. Beyond Chatbots: Moving Toward Multistep Modular AI Agents in Medical Education.

- **ID** `PM41037756` · **日期** 2025 · **发表于** JMIR medical education · **DOI** 10.1016/j.amsu.2021.102656
- **全文文本** `documents/fulltext_pmc/PMC12490774.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41037756/
- **内容** The integration of large language models into medical education has significantly increased, providing valuable assistance in single-turn, isolated educational tasks.
- **tags** #rag #tools

### P220. Streamline automated biomedical discoveries with agentic bioinformatics.

- **ID** `PM41016012` · **日期** 2025 · **发表于** Briefings in bioinformatics · **DOI** 10.1007/978-3-030-60447-9_1
- **全文文本** `documents/fulltext_pmc/PMC12476841.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41016012/
- **内容** The emergence of artificial intelligence agents powered by large language models marks a transformative shift in computational biology.
- **tags** #adaptive #role-play

### P221. Artificial Intelligence and Musculoskeletal Surgical Applications.

- **ID** `PM40405922` · **日期** 2025 · **发表于** HSS journal : the musculoskeletal journal of Hospital for Special Surgery · **DOI** 10.1016/j.fas.2024.12.003
- **全文文本** `documents/fulltext_pmc/PMC12092413.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/40405922/
- **内容** Artificial intelligence (AI) has emerged as a transformative force in orthopedic surgery.
- **tags** #cost #role-play #safety #tools

### P222. Model confrontation and collaboration: A debate intelligence framework for enhancing medical reasoning in large language models.

- **ID** `PM41494532` · **日期** 2026 · **发表于** Cell reports. Medicine · **DOI** 10.48550/arXiv.2402.01723
- **全文文本** `documents/fulltext_pmc/PMC12866169.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41494532/
- **内容** Medical reasoning is fundamental to clinical decision-making, underpinning tasks such as patient communication, diagnosis, and treatment planning.
- **tags** #benchmark #debate #diagnosis #ensemble #medqa #mmlu #pubmedqa #verify

### P223. Language Enhanced Model for Eye (LEME): An Open-Source Ophthalmology-Specific Large Language Model.

- **ID** `PM41031082` · **日期** 2024 · **发表于** ArXiv · **DOI** 10.1136/bjo-2023-324438
- **全文文本** `documents/fulltext_pmc/PMC12478424.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41031082/
- **内容** Large Language Models (LLMs) are poised to revolutionize healthcare. Ophthalmology-specific LLMs remain scarce and underexplored.
- **tags** #benchmark #small-model

### P224. Large Language Model Synergy for Ensemble Learning in Medical Question Answering: Design and Evaluation Study.

- **ID** `PM40658884` · **日期** 2025 · **发表于** Journal of medical Internet research · **DOI** 10.1007/BF02289263
- **全文文本** `documents/fulltext_pmc/PMC12337233.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/40658884/
- **内容** Large language models (LLMs) have demonstrated remarkable capabilities in natural language processing tasks, including medical question-answering (QA). However, individual LLMs often exhibit varying performance across different medical QA datasets.
- **tags** #adaptive #benchmark #cost #ensemble #medmcqa #medqa #pubmedqa #rag #usmle

### P225. MicroVQA: A Multimodal Reasoning Benchmark for Microscopy-Based Scientific Research.

- **ID** `PM40166749` · **日期** 2025 · **发表于** ArXiv
- **全文文本** `documents/fulltext_pmc/PMC11957224.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/40166749/
- **内容** Scientific research demands sophisticated reasoning over multimodal data, a challenge especially prevalent in biology.
- **tags** #benchmark #difficulty #verify

### P226. Reasoning with large language models for medical question answering.

- **ID** `PM38960731` · **日期** 2024 · **发表于** Journal of the American Medical Informatics Association : JAMIA · **DOI** 10.1002/hbm.21387
- **全文文本** `documents/fulltext_pmc/PMC11339506.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38960731/
- **内容** To investigate approaches of reasoning with large language models (LLMs) and to propose a new prompting approach, ensemble reasoning, to improve medical question answering performance with refined reasoning and reduced inconsistency.
- **tags** #benchmark #ensemble #usmle #verify

### P227. OpenMedLM: prompt engineering can out-perform fine-tuning in medical question-answering with open-source large language models.

- **ID** `PM38898116` · **日期** 2024 · **发表于** Scientific reports · **DOI** 10.1038/s41586-023-06291-2
- **全文文本** `documents/fulltext_pmc/PMC11187169.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38898116/
- **内容** LLMs can accomplish specialized medical knowledge tasks, however, equitable access is hindered by the extensive fine-tuning, specialized medical data requirement, and limited access to proprietary models.
- **tags** #benchmark #cost #ensemble #medmcqa #medqa #mmlu #pubmedqa #rag #small-model

### P228. Assessment of ChatGPT-3.5's Knowledge in Oncology: Comparative Study with ASCO-SEP Benchmarks.

- **ID** `PM38875575` · **日期** 2024 · **发表于** JMIR AI · **DOI** 10.1111/iej.13985
- **全文文本** `documents/fulltext_pmc/PMC11041475.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38875575/
- **内容** ChatGPT (Open AI) is a state-of-the-art large language model that uses artificial intelligence (AI) to address questions across diverse topics.
- **tags** #benchmark #diagnosis #tools #verify

### P229. A Medical Large Language Model-Based System Improves History-Taking Performance Among Medical Students.

- **ID** `PM42751277` · **日期** 2026 · **发表于** Cureus · **DOI** 10.7759/cureus.114656
- **全文文本** `documents/fulltext_pmc/PMC13580387.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42751277/
- **内容** To develop a history-taking training and assessment system based on a medical large language model (MedLLM), evaluate its effect on medical students' history-taking competence, and examine its feasibility and effectiveness as a supplement to conventional interview teaching.
- **tags** #benchmark #cost #role-play

### P230. What Platform Scores Miss: Multidimensional Evaluation of AI Teaching Agents in Medical Education.

- **ID** `PM42690903` · **日期** 2026 · **发表于** JMIR medical education · **DOI** 10.1097/JPA.0000000000000742
- **全文文本** `documents/fulltext_pmc/PMC13540620.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42690903/
- **内容** Large language model (LLM)-based AI teaching agents are increasingly used in medical education, yet their pedagogical quality is typically judged by platform-generated scores whose scoring criteria are undisclosed and may not reflect the teaching quality of the agent.
- **tags** #benchmark #cost #difficulty #rag #role-play #safety

### P231. When documentation follows the patient: Unprofessional language and behavioral health referrals in substance use disorder - a retrospective cohort study using LLM-augmented natural language processing.

- **ID** `PM42668739` · **日期** 2026 · **发表于** Digital health · **DOI** 10.1016/j.lanepe.2025.101587
- **全文文本** `documents/fulltext_pmc/PMC13525294.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42668739/
- **内容** Substance use disorders (SUDs) are a major public health challenge, and stigma remains a key barrier to care. Unprofessional or stigmatizing language can shape clinician perceptions and affect decision-making.
- **tags** #role-play #safety

### P232. Improvement of Clinical Practice Guideline Appraisal by Human Experts and AI Agents by Using Structured Guidance: Systematic Review, Meta-Analysis, and Validation Study.

- **ID** `PM42647856` · **日期** 2026 · **发表于** Journal of medical Internet research · **DOI** 10.1056/aioa2400196
- **全文文本** `documents/fulltext_pmc/PMC13559151.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42647856/
- **内容** Rehabilitation clinical practice guidelines (CPGs) have increased rapidly, but inconsistent methodological quality limits their implementation.
- **tags** #benchmark #cost #safety #survey

### P233. Iterative Multidisciplinary Development and Evaluation of a Patient-Facing Social Determinants of Health Chatbot Using Synthetic Data Simulation: Mixed Methods Study.

- **ID** `PM42566745` · **日期** 2026 · **发表于** JMIR formative research · **DOI** 10.1001/jama.2025.18490
- **全文文本** `documents/fulltext_pmc/PMC13450882.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42566745/
- **内容** Systematic collection of social determinants of health (SDoH) data remains inconsistent across health care settings, despite its critical impact on patient outcomes.
- **tags** #adaptive #benchmark #cost #role-play #safety #verify

### P234. Prompt Framing and Evidence Requirement for AI-Generated Educational Responses in Dental Education: Experimental Study.

- **ID** `PM42561407` · **日期** 2026 · **发表于** JMIR medical education · **DOI** 10.1016/j.psychres.2023.115334
- **全文文本** `documents/fulltext_pmc/PMC13446791.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42561407/
- **内容** Large language models are increasingly used in health professions education; however, the role of prompt design in shaping their outputs remains poorly understood in clinical training contexts.
- **tags** #benchmark #cost #safety #verify

### P235. Large Language Models for Individualized Psychoeducational Tools for Psychosis: A Cross-Sectional Study.

- **ID** `PM42530475` · **日期** 2026 · **发表于** Early intervention in psychiatry · **DOI** 10.1111/eip.70230
- **全文文本** `documents/fulltext_pmc/PMC13422232.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42530475/
- **内容** This study aimed to evaluate the quality of GPT-4-generated responses to commonly asked psychosis-related psychoeducational questions from patients, caregivers and relatives in a first-episode psychosis programme.
- **tags** #benchmark #difficulty #safety #tools

### P236. Performance and usability of retrieval-augmented large language models for stroke patient and caregiver support.

- **ID** `PM42369998` · **日期** 2026 · **发表于** Digital health · **DOI** 10.1038/s41586-023-05881-4
- **全文文本** `documents/fulltext_pmc/PMC13309650.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42369998/
- **内容** To develop a Retrieval-Augmented Generation (RAG) question-answering system for stroke patients and family caregivers, and evaluate its performance and usability.
- **tags** #benchmark #rag #survey

### P237. LLM-Driven Extraction of NI-RADS and Imaging Tumor Characteristics to Enhance Oropharyngeal Cancer Survivorship Surveillance.

- **ID** `PM42369515` · **日期** 2026 · **发表于** medRxiv : the preprint server for health sciences · **DOI** 10.1002/hed.26991
- **全文文本** `documents/fulltext_pmc/PMC13308436.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42369515/
- **内容** Radiologic surveillance is essential for oropharyngeal cancer (OPC) survivors, guiding recurrence detection and follow-up strategies.
- **tags** #benchmark #rag #safety

### P238. Evaluating Source-Based Large Language Models for Preclinical Dermatology Education: Comparative Study.

- **ID** `PM42348732` · **日期** 2026 · **发表于** JMIR formative research · **DOI** 10.1145/3644815.3644945
- **全文文本** `documents/fulltext_pmc/PMC13298547.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42348732/
- **内容** Large language models (LLMs) have gained increasing popularity in medical education, with evidence supporting their educational value when framed through the lens of cognitive load theory.
- **tags** #benchmark #difficulty #rag #usmle

### P239. A comparative benchmark of DeepSeek-R1 on the USMLE: surpassing human and AI performance averages.

- **ID** `PM42296682` · **日期** 2026 · **发表于** Clinics (Sao Paulo, Brazil) · **DOI** 10.1016/j.clinsp.2026.101021
- **全文文本** `documents/fulltext_pmc/PMC13285263.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42296682/
- **内容** The rapid advancement of Large Language Models (LLMs) has generated interest in their application to medical education, particularly for high-stakes assessments like the USMLE.
- **tags** #benchmark #rag #usmle

### P240. AI Chatbot Suicide Risk Detection and Response: Human Validation Study of the Open-Source VERA-MH Safety Evaluation.

- **ID** `PM42257560` · **日期** 2026 · **发表于** JMIR AI · **DOI** 10.48550/arXiv.2505.06120
- **全文文本** `documents/fulltext_pmc/PMC13365878.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42257560/
- **内容** Millions of people now use leading generative artificial intelligence (AI) tools (chatbots) for psychological support.
- **tags** #benchmark #safety #tools

### P241. Benchmarking Large Language Models and Prompt Engineering Strategies in Microsatellite Instability Cancers: Evaluation Study.

- **ID** `PM42166792` · **日期** 2026 · **发表于** Journal of medical Internet research · **DOI** 10.1038/s41746-025-01536-y
- **全文文本** `documents/fulltext_pmc/PMC13193672.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42166792/
- **内容** The reliability of general-purpose large language models (LLMs) for complex clinical tasks in specialized domains such as microsatellite instability (MSI) cancers remains critically uncharacterized.
- **tags** #benchmark #cost #rag #safety #verify

### P242. A Multiassessment and Multiprofessional Agents Approach for Medical Chatbot Risk Estimation: Development and Evaluation Study.

- **ID** `PM42140617` · **日期** 2026 · **发表于** JMIR medical informatics · **DOI** 10.1007/s10579-023-09704-w
- **全文文本** `documents/fulltext_pmc/PMC13221620.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42140617/
- **内容** Assessing chatbot responses across 3 domains-medical, ethical, and legal-is essential to ensuring the safe use of artificial intelligence in health care.
- **tags** #benchmark #ensemble #rag #safety #verify

### P243. Automated Identification of Nursing Diagnoses and Interventions From Nursing Records Using a Retrieval-Augmented Large Language Model Approach: Quantitative Study.

- **ID** `PM42054561` · **日期** 2026 · **发表于** Journal of medical Internet research · **DOI** 10.1145/3696410.3714782
- **全文文本** `documents/fulltext_pmc/PMC13128066.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42054561/
- **内容** Electronic health records (EHRs) have been widely adopted, but most nursing records remain in unstructured free-text format, which limits the secondary use of nursing data.
- **tags** #benchmark #diagnosis #rag #small-model

### P244. Context-Guided Mixture-of-Experts with Multimodal LLMs for Lesion Detection in Buccal Mucosa Images.

- **ID** `PM42030750` · **日期** 2026 · **发表于** International dental journal · **DOI** 10.1016/j.semarthrit.2010.12.001
- **全文文本** `documents/fulltext_pmc/PMC13127626.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/42030750/
- **内容** Oral lesions are highly prevalent globally, and oral cancer ranks among the most common malignancies, underscoring the need for AI-driven tools to support early detection and triage, especially in resource-scarce settings.
- **tags** #diagnosis #role-play #tools

### P245. The Alberta Quality Assessment Tool: Risk of Bias (AQAT:RoB) for the Evaluation of Medical Large Language Model Question-Answer Studies: Development and Pilot Validation.

- **ID** `PM41950508` · **日期** 2026 · **发表于** Journal of medical Internet research · **DOI** 10.1016/j.jclinepi.2024.111370
- **全文文本** `documents/fulltext_pmc/PMC13061365.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41950508/
- **内容** Despite the transformative potential of large language models (LLMs) in health care, the rapid development of these tools has outpaced their rigorous evaluation.
- **tags** #benchmark #safety #tools #verify

### P246. Initial Insights Into an Institutional Secure Large Language Model for Magnetic Resonance Imaging Examination Requests: Retrospective Study.

- **ID** `PM41945643` · **日期** 2026 · **发表于** Journal of medical Internet research · **DOI** 10.1038/s43856-025-01021-3
- **全文文本** `documents/fulltext_pmc/PMC13055936.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41945643/
- **内容** Incomplete clinical details on magnetic resonance imaging (MRI) examination requests (MERs) can lead to suboptimal protocol selection.
- **tags** #benchmark #cost #rag #safety

### P247. AI achieves board-level performance on the Japan diagnostic radiology board examination through direct image interpretation.

- **ID** `PM41925792` · **日期** 2026 · **发表于** Japanese journal of radiology · **DOI** 10.1038/sdata.2018.251
- **全文文本** `documents/fulltext_pmc/PMC13400479.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41925792/
- **内容** To evaluate text-only versus vision-enabled performance of late-2025 large language models (LLMs) on the Japan Diagnostic Radiology Board Examination (JDRBE) and compare model performance with newly board-certified radiologists.
- **tags** #benchmark #diagnosis

### P248. Multi-Evidence Clinical Reasoning With Retrieval-Augmented Generation for Emergency Triage: Retrospective Evaluation Study.

- **ID** `PM41587455` · **日期** 2026 · **发表于** JMIR medical informatics · **DOI** 10.1161/CIR.0000000000001201
- **全文文本** `documents/fulltext_pmc/PMC12887567.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41587455/
- **内容** Emergency triage accuracy is critical but varies with clinician experience, cognitive load, and case complexity. Mis-triage can delay care for high-risk patients and exacerbate crowding through unnecessary prioritization.
- **tags** #benchmark #diagnosis #difficulty #rag #safety #tools #verify

### P249. GPT-4o and OpenAI o1 Performance on the 2024 Spanish Competitive Medical Specialty Access Examination: Cross-Sectional Quantitative Evaluation Study.

- **ID** `PM41525685` · **日期** 2026 · **发表于** JMIR medical education · **DOI** 10.48550/arXiv.2407.21783
- **全文文本** `documents/fulltext_pmc/PMC12795474.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41525685/
- **内容** In recent years, generative artificial intelligence and large language models (LLMs) have rapidly advanced, offering significant potential to transform medical education.
- **tags** #benchmark #difficulty #rag #role-play #safety #verify

### P250. Assessing the Quality of AI Responses to Patient Concerns About Axial Spondyloarthritis: Delphi-Based Evaluation.

- **ID** `PM41499772` · **日期** 2026 · **发表于** JMIR AI · **DOI** 10.2196/58329
- **全文文本** `documents/fulltext_pmc/PMC12824573.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41499772/
- **内容** Axial spondyloarthritis (axSpA) is a chronic autoinflammatory disease with heterogeneous clinical features, presenting considerable complexity for sustained patient self-management.
- **tags** #benchmark #diagnosis #difficulty #safety #tools #verify

### P251. ChatMyopia: An AI agent for myopia-related consultation in primary eye care settings.

- **ID** `PM41244561` · **日期** 2025 · **发表于** iScience · **DOI** 10.1007/BF00846695
- **全文文本** `documents/fulltext_pmc/PMC12616040.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41244561/
- **内容** Large language models (LLMs) show promise for tailored healthcare communication but face challenges in interpretability and multi-task integration, particularly for domain-specific needs such as myopia, and their real-world effectiveness as patient education tools has yet to be demonstrated.
- **tags** #benchmark #rag #tools

### P252. Evaluating the Performance of DeepSeek-R1 and DeepSeek-V3 Versus OpenAI Models in the Chinese National Medical Licensing Examination: Cross-Sectional Comparative Study.

- **ID** `PM41237388` · **日期** 2025 · **发表于** JMIR medical education · **DOI** 10.1038/s41586-025-09422-z
- **全文文本** `documents/fulltext_pmc/PMC12663704.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41237388/
- **内容** Deepseek-R1, an open-source large language model (LLM), has generated significant global interest in the past months.
- **tags** #benchmark #tools

### P253. Integrating Clinical and Systemic Knowledge in Periodontal and Peri-Implant Disease Education Through a Knowledge Graph.

- **ID** `PM41236841` · **日期** 2026 · **发表于** Journal of dental education · **DOI** 10.1109/TNNLS.2021.3112045
- **全文文本** `documents/fulltext_pmc/PMC13489181.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/41236841/
- **内容** This study aims to construct a knowledge graph in the field of periodontology and develop a knowledge-graph-based intelligent question-answering (QA) system, with the goal of enhancing the structured management and intelligent application of periodontal disease knowledge.
- **tags** #benchmark #cost #diagnosis #rag

### P254. From Guidelines to Real-Time Conversation: Expert-Validated Retrieval-Augmented and Fine-Tuned GPT-4 for Hepatitis C Management.

- **ID** `PM40960299` · **日期** 2025 · **发表于** Liver international : official journal of the International Association for the Study of the Liver · **DOI** 10.1097/HEP.0000000000000992
- **全文文本** `documents/fulltext_pmc/PMC12442523.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/40960299/
- **内容** Advances in artificial intelligence, particularly large language models (LLMs), hold promise for transforming chronic disease management such as Hepatitis C Virus (HCV) infection.
- **tags** #benchmark #rag

### P255. Public Versus Academic Discourse on ChatGPT in Health Care: Mixed Methods Study.

- **ID** `PM40550010` · **日期** 2025 · **发表于** JMIR infodemiology · **DOI** 10.48550/arXiv.2407.09492
- **全文文本** `documents/fulltext_pmc/PMC12208614.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/40550010/
- **内容** The rapid emergence of artificial intelligence-based large language models (LLMs) in 2022 has initiated extensive discussions within the academic community.
- **tags** #debate #safety #verify

### P256. Era of Generalist Conversational Artificial Intelligence to Support Public Health Communications.

- **ID** `PM39832358` · **日期** 2025 · **发表于** Journal of medical Internet research · **DOI** 10.1057/s41599-024-03017-1
- **全文文本** `documents/fulltext_pmc/PMC11791462.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/39832358/
- **内容** The integration of artificial intelligence (AI) into health communication systems has introduced a transformative approach to public health management, particularly during public health emergencies, capable of reaching billions through familiar digital channels.
- **tags** #adaptive #benchmark #multi-agent #rag #role-play #safety #verify

### P257. A Novel Cognitive Behavioral Therapy-Based Generative AI Tool (Socrates 2.0) to Facilitate Socratic Dialogue: Protocol for a Mixed Methods Feasibility Study.

- **ID** `PM39388255` · **日期** 2024 · **发表于** JMIR research protocols · **DOI** 10.1002/cpp.658
- **全文文本** `documents/fulltext_pmc/PMC11502974.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/39388255/
- **内容** Digital mental health tools, designed to augment traditional mental health treatments, are becoming increasingly important due to a wide range of barriers to accessing mental health care, including a growing shortage of clinicians.
- **tags** #multi-agent #tools

### P258. Quality assurance and validity of AI-generated single best answer questions.

- **ID** `PM40001164` · **日期** 2025 · **发表于** BMC medical education · **DOI** 10.1001/jamasurg.2023.5695
- **全文文本** `documents/fulltext_pmc/PMC11854382.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/40001164/
- **内容** Recent advancements in generative artificial intelligence (AI) have opened new avenues in educational methodologies, particularly in medical education.
- **tags** #benchmark #role-play

### P259. Large Language Models-Supported Thrombectomy Decision-Making in Acute Ischemic Stroke Based on Radiology Reports: Feasibility Qualitative Study.

- **ID** `PM39946168` · **日期** 2025 · **发表于** Journal of medical Internet research · **DOI** 10.2196/32690
- **全文文本** `documents/fulltext_pmc/PMC11888093.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/39946168/
- **内容** The latest advancement of artificial intelligence (AI) is generative pretrained transformer large language models (LLMs). They have been trained on massive amounts of text, enabling humanlike and semantical responses to text-based inputs and requests.
- **tags** #cost #tools

### P260. Slit Lamp Report Generation and Question Answering: Development and Validation of a Multimodal Transformer Model with Large Language Model Integration.

- **ID** `PM39753218` · **日期** 2024 · **发表于** Journal of medical Internet research · **DOI** 10.1145/364128
- **全文文本** `documents/fulltext_pmc/PMC11729784.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/39753218/
- **内容** Large language models have shown remarkable efficacy in various medical research and clinical applications. However, their skills in medical image recognition and subsequent report generation or question answering (QA) remain limited.
- **tags** #benchmark #verify

### P261. Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial.

- **ID** `PM39466245` · **日期** 2024 · **发表于** JAMA network open · **DOI** 10.1111/medu.15089
- **全文文本** `documents/fulltext_pmc/PMC11519755.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/39466245/
- **内容** Large language models (LLMs) have shown promise in their performance on both multiple-choice and open-ended medical reasoning examinations, but it remains unknown whether the use of such tools improves physician diagnostic reasoning.
- **tags** #benchmark #diagnosis #tools

### P262. Testing and Validation of a Custom Retrained Large Language Model for the Supportive Care of HN Patients with External Knowledge Base.

- **ID** `PM39001375` · **日期** 2024 · **发表于** Cancers · **DOI** 10.1016/j.eururo.2023.03.037
- **全文文本** `documents/fulltext_pmc/PMC11240646.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/39001375/
- **内容** This study aimed to develop a retrained large language model (LLM) tailored to the needs of HN cancer patients treated with radiotherapy, with emphasis on symptom management and survivorship care.
- **tags** #benchmark #rag

### P263. Comparing the Perspectives of Generative AI, Mental Health Experts, and the General Public on Schizophrenia Recovery: Case Vignette Study.

- **ID** `PM38533615` · **日期** 2024 · **发表于** JMIR mental health · **DOI** 10.2196/preprints.54781
- **全文文本** `documents/fulltext_pmc/PMC11004608.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38533615/
- **内容** The current paradigm in mental health care focuses on clinical recovery and symptom remission. This model's efficacy is influenced by therapist trust in patient recovery potential and the depth of the therapeutic relationship.
- **tags** #benchmark #debate

### P264. How Does ChatGPT Use Source Information Compared With Google? A Text Network Analysis of Online Health Information.

- **ID** `PM38517757` · **日期** 2024 · **发表于** Clinical orthopaedics and related research · **DOI** 10.1097/CORR.0000000000002995
- **全文文本** `documents/fulltext_pmc/PMC10936961.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38517757/
- **内容** The lay public is increasingly using ChatGPT (a large language model) as a source of medical information.
- **tags** #benchmark #difficulty #ensemble #rag #tools

### P265. Learning to Make Rare and Complex Diagnoses With Generative AI Assistance: Qualitative Study of Popular Large Language Models.

- **ID** `PM38349725` · **日期** 2024 · **发表于** JMIR medical education · **DOI** 10.4300/JGME-D-18-00466.1
- **全文文本** `documents/fulltext_pmc/PMC10900078.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38349725/
- **内容** Patients with rare and complex diseases often experience delayed diagnoses and misdiagnoses because comprehensive knowledge about these diseases is limited to only a few medical experts.
- **tags** #benchmark #diagnosis #ensemble #rag #tools

### P266. Evaluation of the Performance of Generative AI Large Language Models ChatGPT, Google Bard, and Microsoft Bing Chat in Supporting Evidence-Based Dentistry: Comparative Mixed Methods Study.

- **ID** `PM38009003` · **日期** 2023 · **发表于** Journal of medical Internet research · **DOI** 10.1038/s41415-023-5928-0
- **全文文本** `documents/fulltext_pmc/PMC10784979.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/38009003/
- **内容** The increasing application of generative artificial intelligence large language models (LLMs) in various fields, including dentistry, raises questions about their accuracy.
- **tags** #benchmark #cost #rag #tools #verify

### P267. Performance of ChatGPT-4 in answering questions from the Brazilian National Examination for Medical Degree Revalidation.

- **ID** `PM37792871` · **日期** 2023 · **发表于** Revista da Associacao Medica Brasileira (1992) · **DOI** 10.2196/48002
- **全文文本** `documents/fulltext_pmc/PMC10547492.txt`（PDF 需手动下载）
- **链接** https://pubmed.ncbi.nlm.nih.gov/37792871/
- **内容** The aim of this study was to evaluate the performance of ChatGPT-4.0 in answering the 2022 Brazilian National Examination for Medical Degree Revalidation (Revalida) and as a tool to provide feedback on the quality of the examination.
- **tags** #benchmark #tools

## Part 3 · 已发表 · 需手动获取

> 订阅期刊且无开放获取版本。**请手动下载后命名 `PMID_<pmid>.pdf` 放入 `documents/`。**

| # | ID | 发表于 | tags | 标题 |
|---|---|---|---|---|
| 1 | `PM42771632` | IEEE journal of biomedical and hea | #benchmark #safety | Foundation Models in Ophthalmic Artificial Intelligence: Curre |
| 2 | `PM42740524` | Diagnosis (Berlin, Germany) | #benchmark #diagnosis #multi-agent #tools | Early evidence for a multi-agent AI simulator for clinical rea |
| 3 | `PM42617946` | Drug discovery today | #diagnosis #safety #tools | Artificial intelligence agents and agentic artificial intellig |
| 4 | `PM42582871` | RSC medicinal chemistry | #adaptive #multi-agent #rag #safety #tools #verify | Closed-loop agentic AI in drug discovery. |
| 5 | `PM42508637` | The American journal of pathology | #benchmark #cost #diagnosis #rag #safety | Multimodal Artificial Intelligence in Tissue Diagnostics: Visi |
| 6 | `PM42442213` | Medical image analysis | #diagnosis #verify | PathFound: An agentic multimodal model activating evidence-see |
| 7 | `PM42385839` | Journal of dentistry | #benchmark #cost #rag #safety #tools | DGADS: A graph-based agentic decision support system for preci |
| 8 | `PM42361884` | Journal of dentistry | #benchmark #safety #tools | AI-assisted software development in digital dentistry: A techn |
| 9 | `PM42289818` | Journal of the American Medical In | #benchmark #ensemble #medqa #multi-agent #pubmedqa #rag | Let large language models judge each other: multi-agent peer-r |
| 10 | `PM42178832` | Biopreservation and biobanking | #adaptive #cost #diagnosis #multi-agent #role-play | Biobanking in the Era of Artificial Intelligence: Convergence, |
| 11 | `PM42175320` | Studies in health technology and i | #benchmark #multi-agent #rag | Garbage In, Garbage Out: Context Engineering for Generating Mu |
| 12 | `PM42175303` | Studies in health technology and i | #benchmark #cost #multi-agent #verify | Agent-Based Improvement of Multiple-Choice Question Quality in |
| 13 | `PM42119128` | Studies in health technology and i |  | Designing Agentic Workflows in Healthcare Informatics: Challen |
| 14 | `PM41951492` | The Lancet. Digital health | #multi-agent #rag #role-play | A multiagent large language model-based system to simulate the |
| 15 | `PM41713127` | International journal of medical i | #adaptive #benchmark #cost #diagnosis #rag #tools | Agentic memory-augmented retrieval and evidence grounding for  |
| 16 | `PM41659839` | Health information science and sys | #safety #verify | Big data in healthcare and medicine revisited design and manag |
| 17 | `PM41454792` | Clinical chemistry and laboratory  | #adaptive #cost #difficulty #tools | From automation to agentic artificial intelligence in laborato |
| 18 | `PM41432042` | Diagnostic and interventional imag | #adaptive #multi-agent #safety #tools #verify | Agentic systems in radiology: Principles, opportunities, priva |
| 19 | `PM41360019` | Clinical radiology | #diagnosis | Radiomics in clinical radiology: advances, challenges, and fut |
| 20 | `PM41175385` | Current opinion in ophthalmology | #cost #safety #survey | Toward autonomous discovery: agentic AI and the future of opht |
| 21 | `PM41109093` | International journal of medical i | #adaptive #benchmark #debate #difficulty #ensemble #medqa | MedARC: Adaptive multi-agent refinement and collaboration for  |
| 22 | `PM40669284` | Computers in biology and medicine | #benchmark #cost #ensemble #rag #role-play #verify | Refining LLMs outputs with iterative consensus ensemble (ICE). |
| 23 | `PM42772746` | JMIR research protocols | #benchmark #cost #role-play #safety #tools #verify | Process-Oriented, Behaviorally Anchored Assessment of Clinical |
| 24 | `PM42727622` | Journal of the American College of | #benchmark #diagnosis #rag #small-model #tools #usmle | Human Judgment and the Limits of Artificial Intelligence for A |
| 25 | `PM42647413` | Medical teacher | #benchmark #difficulty | Evaluating hybrid human-LLM coding workflows for qualitative r |
| 26 | `PM42622576` | The Journal of hand surgery | #difficulty #survey | AI Clinical Decision Making Compared with Fellowship-Trained H |
| 27 | `PM42410586` | BMC oral health | #adaptive #cost #debate #diagnosis #safety #tools | Dental image analysis and surgical decision support using modi |
| 28 | `PM42363984` | Graefe's archive for clinical and  | #benchmark #diagnosis #role-play #tools #verify | Automated iridocorneal angle classification using a multimodal |
| 29 | `PM42217017` | International urogynecology journa | #role-play | Shaping AI in Pelvic Floor Physiotherapy: The Impact of Role-P |
| 30 | `PM41998423` | Supportive care in cancer : offici | #benchmark #safety #tools #verify | Artificial intelligence in cancer survivorship: evaluating Cha |
| 31 | `PM41936721` | Rheumatology international | #benchmark #cost #diagnosis #role-play #tools | Comparative evaluation of large language model-based AI platfo |
| 32 | `PM41521528` | Diagnosis (Berlin, Germany) | #benchmark #diagnosis #tools | Rationalisation of a thrombophilia panel using laboratory medi |
| 33 | `PM41379872` | Cornea | #benchmark #cost | To Evaluate the Efficacy of Zero-Shot Prompting Using Large La |
| 34 | `PM41212429` | Journal of medical systems | #benchmark #cost #difficulty #safety #tools #verify | Evaluating the Performance of DeepSeek-R1 as a Patient Educati |
| 35 | `PM40915935` | Academic radiology | #benchmark #diagnosis #tools | Interpreting BI-RADS-Free Breast MRI Reports Using a Large Lan |
| 36 | `PM40627696` | The Journal of bone and joint surg | #benchmark #diagnosis #rag | An Institutional Large Language Model for Musculoskeletal MRI  |
| 37 | `PM40030182` | IEEE transactions on medical imagi | #diagnosis #multi-agent | Integration of Multi-Source Medical Data for Medical Diagnosis |
| 38 | `PM39725770` | Journal of medical systems | #benchmark #diagnosis #multi-agent #safety #survey | Applications and Future Prospects of Medical LLMs: A Survey Ba |
| 39 | `PM39689760` | Modern pathology : an official jou | #cost #debate #diagnosis #multi-agent #safety #tools | Generative Artificial Intelligence in Pathology and Medicine:  |
| 40 | `PM39217985` | Blood purification | #diagnosis #multi-agent #safety #verify | Generative AI in Critical Care Nephrology: Applications and Fu |
| 41 | `PM40439661` | Medical teacher | #benchmark #safety | GPT-4 versus human authors in clinically complex MCQ creation: |
| 42 | `PM40020592` | International journal of law and p | #debate | Large language models and psychiatry. |
| 43 | `PM39287525` | Radiology | #benchmark #diagnosis #difficulty #role-play #safety | Constructing a Large Language Model to Generate Impressions fr |
| 44 | `PM39236407` | Journal of clinical neuroscience : | #cost #debate #role-play #safety #tools | ChatGPT and neurosurgical education: A crossroads of innovatio |
| 45 | `PM39123288` | International journal of dermatolo | #benchmark #role-play #tools | The utility of artificial intelligence platforms for patient-g |
| 46 | `PM38597198` | Journal of pediatric orthopedics | #benchmark #diagnosis #role-play | Are Generative Pretrained Transformer 4 Responses to Developme |
| 47 | `PM38423884` | Journal of cardiothoracic and vasc | #tools | Artificial Intelligence for Anesthesiology Board-Style Examina |
| 48 | `PM38353523` | Neurosurgery | #benchmark #diagnosis #tools | A Quantitative Assessment of ChatGPT as a Neurosurgical Triagi |
| 49 | `PM38315183` | Die Anaesthesiologie | #benchmark #debate | [ChatGPT: aid to medical ethics decision making?]. |
| 50 | `PM37821756` | Innere Medizin (Heidelberg, German | #benchmark #debate | [ChatGPT: aid to medical ethics decision making?]. |

### P31. Foundation Models in Ophthalmic Artificial Intelligence: Current Status and Future Directions.

- **ID** `PM42771632` · **日期** 2026 · **发表于** IEEE journal of biomedical and health informatics · **DOI** 10.1109/JBHI.2026.3736832
- **链接** https://pubmed.ncbi.nlm.nih.gov/42771632/
- **内容** Recent advances in ophthalmic foundation models have accelerated the application of artificial intelligence in ophthalmology, improving disease detection, progression assessment, and treatment evaluation.
- **tags** #benchmark #safety

### P32. Early evidence for a multi-agent AI simulator for clinical reasoning practice: performance, consistency, and challenges.

- **ID** `PM42740524` · **日期** 2026 · **发表于** Diagnosis (Berlin, Germany) · **DOI** 10.1097/ACM.0000000000002768
- **链接** https://pubmed.ncbi.nlm.nih.gov/42740524/
- **内容** Clinical reasoning develops through repeated, deliberate practice, yet clinical and simulation environments are often limited by continuity, feedback, and scalability constraints.
- **tags** #benchmark #diagnosis #multi-agent #tools

### P33. Artificial intelligence agents and agentic artificial intelligence applied to precision medicine.

- **ID** `PM42617946` · **日期** 2026 · **发表于** Drug discovery today · **DOI** 10.1016/j.drudis.2026.104781
- **链接** https://pubmed.ncbi.nlm.nih.gov/42617946/
- **内容** Precision medicine seeks to individualise care by integrating multimodal biomedical data, yet most deployed clinical artificial intelligence (AI) remains assistive, providing predictions without managing workflows or adapting autonomously.
- **tags** #diagnosis #safety #tools

### P34. Closed-loop agentic AI in drug discovery.

- **ID** `PM42582871` · **日期** 2026 · **发表于** RSC medicinal chemistry · **DOI** 10.1038/s41746-025-01992-6
- **链接** https://pubmed.ncbi.nlm.nih.gov/42582871/
- **内容** Drug discovery is undergoing a paradigm shift from isolated artificial intelligence (AI) tools to integrated, closed-loop, agent-driven systems that combine prediction with experimental execution.
- **tags** #adaptive #multi-agent #rag #safety #tools #verify

### P35. Multimodal Artificial Intelligence in Tissue Diagnostics: Vision-Language Models and the Future of Computational Pathology.

- **ID** `PM42508637` · **日期** 2026 · **发表于** The American journal of pathology · **DOI** 10.1016/j.ajpath.2026.07.002
- **链接** https://pubmed.ncbi.nlm.nih.gov/42508637/
- **内容** Vision-language models (VLMs) represent an emerging class of multimodal artificial intelligence systems that integrate visual information with natural-language understanding and generation.
- **tags** #benchmark #cost #diagnosis #rag #safety

### P36. PathFound: An agentic multimodal model activating evidence-seeking pathological diagnosis.

- **ID** `PM42442213` · **日期** 2026 · **发表于** Medical image analysis · **DOI** 10.1016/j.media.2026.104200
- **链接** https://pubmed.ncbi.nlm.nih.gov/42442213/
- **内容** Recent pathological foundation models have substantially advanced visual representation learning and multimodal interaction. However, most models still rely on a static inference paradigm.
- **tags** #diagnosis #verify

### P37. DGADS: A graph-based agentic decision support system for precision dental question answering.

- **ID** `PM42385839` · **日期** 2026 · **发表于** Journal of dentistry · **DOI** 10.1016/j.jdent.2026.106875
- **链接** https://pubmed.ncbi.nlm.nih.gov/42385839/
- **内容** Large language models (LLMs) have significant potential for dental applications, but their inherent tendency to hallucinate remains a major challenge.
- **tags** #benchmark #cost #rag #safety #tools

### P38. AI-assisted software development in digital dentistry: A technical innovation report with three open-source applications.

- **ID** `PM42361884` · **日期** 2026 · **发表于** Journal of dentistry · **DOI** 10.1016/j.jdent.2026.106864
- **链接** https://pubmed.ncbi.nlm.nih.gov/42361884/
- **内容** To present a feasible workflow for artificial intelligence (AI)-assisted software engineering in dentistry as a technical innovation report. The use of this workflow is illustrated through three self-developed open-source dental applications.
- **tags** #benchmark #safety #tools

### P39. Let large language models judge each other: multi-agent peer-reviewed reasoning for medical question answering.

- **ID** `PM42289818` · **日期** 2026 · **发表于** Journal of the American Medical Informatics Association : JAMIA · **DOI** 10.1093/jamia/ocag042
- **链接** https://pubmed.ncbi.nlm.nih.gov/42289818/
- **内容** To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA).
- **tags** #benchmark #ensemble #medqa #multi-agent #pubmedqa #rag #small-model #usmle

### P310. Biobanking in the Era of Artificial Intelligence: Convergence, Challenges, and Opportunities.

- **ID** `PM42178832` · **日期** 2026 · **发表于** Biopreservation and biobanking · **DOI** 10.1177/19475535261445907
- **链接** https://pubmed.ncbi.nlm.nih.gov/42178832/
- **内容** Artificial intelligence (AI) is advancing rapidly, transforming biomedical research and health care through software applications ranging from diagnostics to drug discovery.
- **tags** #adaptive #cost #diagnosis #multi-agent #role-play

### P311. Garbage In, Garbage Out: Context Engineering for Generating Multiple-Choice Questions for Medical Education Using Knowledge Graphs and LLMs.

- **ID** `PM42175320` · **日期** 2026 · **发表于** Studies in health technology and informatics · **DOI** 10.3233/SHTI260652
- **链接** https://pubmed.ncbi.nlm.nih.gov/42175320/
- **内容** Multiple-choice questions (MCQs) are a cornerstone of medical education, but generating high-quality items automatically remains challenging.
- **tags** #benchmark #multi-agent #rag

### P312. Agent-Based Improvement of Multiple-Choice Question Quality in Medical Education.

- **ID** `PM42175303` · **日期** 2026 · **发表于** Studies in health technology and informatics · **DOI** 10.3233/SHTI260635
- **链接** https://pubmed.ncbi.nlm.nih.gov/42175303/
- **内容** High-quality multiple-choice questions (MCQs) are essential for medical education, but costly to design. Large language models (LLMs) can generate MCQs automatically, yet their outputs often fail to meet core quality criteria.
- **tags** #benchmark #cost #multi-agent #verify

### P313. Designing Agentic Workflows in Healthcare Informatics: Challenges and Insights from a Student Perspective.

- **ID** `PM42119128` · **日期** 2026 · **发表于** Studies in health technology and informatics · **DOI** 10.3233/SHTI260092
- **链接** https://pubmed.ncbi.nlm.nih.gov/42119128/
- **内容** Agentic workflows based on large language models (LLMs) are increasingly explored in healthcare, yet their design raises challenges related to control and predictability.
- **tags** 

### P314. A multiagent large language model-based system to simulate the liver transplant selection committee: a retrospective cohort study.

- **ID** `PM41951492` · **日期** 2026 · **发表于** The Lancet. Digital health · **DOI** 10.1016/j.landig.2025.100966
- **链接** https://pubmed.ncbi.nlm.nih.gov/41951492/
- **内容** Transplantation is one of the few areas in medicine in which the definitive treatment is rationed. Subjective decision making poses challenges for the transplantation selection process.
- **tags** #multi-agent #rag #role-play

### P315. Agentic memory-augmented retrieval and evidence grounding for medical question-answering tasks.

- **ID** `PM41713127` · **日期** 2026 · **发表于** International journal of medical informatics · **DOI** 10.1016/j.jbi.2023.104286
- **链接** https://pubmed.ncbi.nlm.nih.gov/41713127/
- **内容** To evaluate whether a tool-using agent-based system built on large language models (LLMs) outperforms standalone LLMs on medical question-answering tasks.
- **tags** #adaptive #benchmark #cost #diagnosis #rag #tools #usmle

### P316. Big data in healthcare and medicine revisited design and managerial challenges in the age of artificial intelligence.

- **ID** `PM41659839` · **日期** 2026 · **发表于** Health information science and systems · **DOI** 10.1038/s41591-021-01312-x
- **链接** https://pubmed.ncbi.nlm.nih.gov/41659839/
- **内容** A decade ago, we characterized big data in healthcare as a nascent field anchored in distributed computing paradigms. The intervening years have witnessed a transformation so profound that revisiting our original framework is essential.
- **tags** #safety #verify

### P317. From automation to agentic artificial intelligence in laboratory medicine: an opinion of the IFCC Division on Emerging Technologies.

- **ID** `PM41454792` · **日期** 2026 · **发表于** Clinical chemistry and laboratory medicine · **DOI** 10.1093/eurheartj/ehaf272
- **链接** https://pubmed.ncbi.nlm.nih.gov/41454792/
- **内容** Agentic artificial intelligence (AI) systems are distinguished by their ability to invoke multiple tools, compose command chains, and combine chain-of-thought reasoning with deep research to execute complex tasks and take actions.
- **tags** #adaptive #cost #difficulty #tools

### P318. Agentic systems in radiology: Principles, opportunities, privacy risks, regulation, and sustainability concerns.

- **ID** `PM41432042` · **日期** 2026 · **发表于** Diagnostic and interventional imaging · **DOI** 10.1016/j.diii.2025.10.002
- **链接** https://pubmed.ncbi.nlm.nih.gov/41432042/
- **内容** The rapid rise of transformer-based large language models (LLMs) has introduced new opportunities for automation and decision support in radiology, particularly in applications such as report generation, protocol optimization, and structured interpretation.
- **tags** #adaptive #multi-agent #safety #tools #verify

### P319. Radiomics in clinical radiology: advances, challenges, and future directions.

- **ID** `PM41360019` · **日期** 2026 · **发表于** Clinical radiology · **DOI** 10.1016/j.crad.2025.107165
- **链接** https://pubmed.ncbi.nlm.nih.gov/41360019/
- **内容** High-throughput extraction of quantitative image features, known as radiomics, has the potential to improve clinical radiology by revealing hidden features in medical images.
- **tags** #diagnosis

### P320. Toward autonomous discovery: agentic AI and the future of ophthalmic research.

- **ID** `PM41175385` · **日期** 2026 · **发表于** Current opinion in ophthalmology · **DOI** 10.1097/ICU.0000000000001179
- **链接** https://pubmed.ncbi.nlm.nih.gov/41175385/
- **内容** Rapid advances in large language models (LLMs) have led to the emergence of agentic artificial intelligence (AI) systems capable of autonomously performing complex scientific tasks.
- **tags** #cost #safety #survey

### P321. MedARC: Adaptive multi-agent refinement and collaboration for enhanced medical reasoning in large language models.

- **ID** `PM41109093` · **日期** 2026 · **发表于** International journal of medical informatics · **DOI** 10.1016/j.ijmedinf.2025.106136
- **链接** https://pubmed.ncbi.nlm.nih.gov/41109093/
- **内容** Large Language Models (LLMs) have shown remarkable potential in medical question answering (QA), yet their deployment in clinical settings remains limited by hallucinations, inconsistent reasoning, and difficulties in handling complex biomedical information.
- **tags** #adaptive #benchmark #debate #difficulty #ensemble #medqa #multi-agent #pubmedqa #safety #verify

### P322. Refining LLMs outputs with iterative consensus ensemble (ICE).

- **ID** `PM40669284` · **日期** 2025 · **发表于** Computers in biology and medicine · **DOI** 10.1016/j.compbiomed.2025.110731
- **链接** https://pubmed.ncbi.nlm.nih.gov/40669284/
- **内容** Large language models (LLMs) show promising accuracy on challenging tasks, including medical question answering. Yet, direct gains from model upgrades can plateau, and reliability issues persist.
- **tags** #benchmark #cost #ensemble #rag #role-play #verify

### P323. Process-Oriented, Behaviorally Anchored Assessment of Clinical Reasoning in Large Language Models and the Effect of Extended Thinking: Protocol for a Prospective, Multigroup, Comparative Study.

- **ID** `PM42772746` · **日期** 2026 · **发表于** JMIR research protocols · **DOI** 10.2196/103220
- **链接** https://pubmed.ncbi.nlm.nih.gov/42772746/
- **内容** Most clinical reasoning evaluations in large language models (LLMs) score only the final answer, usually multiple-choice accuracy, which explains little about model reasoning.
- **tags** #benchmark #cost #role-play #safety #tools #verify

### P324. Human Judgment and the Limits of Artificial Intelligence for Automated Rank Order Lists in Diagnostic Radiology Residency Selection.

- **ID** `PM42727622` · **日期** 2026 · **发表于** Journal of the American College of Radiology : JACR · **DOI** 10.1016/j.jacr.2026.09.006
- **链接** https://pubmed.ncbi.nlm.nih.gov/42727622/
- **内容** To evaluate whether large language models (LLMs) can reliably reproduce a residency program's rank order list (ROL) from pre-interview application data alone versus with human interviews included, and to determine whether automated ranking tools safely mirror human consensus or inadvertently introduce systematic displacements against specific applicant subgroups.
- **tags** #benchmark #diagnosis #rag #small-model #tools #usmle

### P325. Evaluating hybrid human-LLM coding workflows for qualitative research in medical education: A generalizability study.

- **ID** `PM42647413` · **日期** 2026 · **发表于** Medical teacher · **DOI** 10.1080/0142159X.2026.2721362
- **链接** https://pubmed.ncbi.nlm.nih.gov/42647413/
- **内容** Large language models (LLMs) are increasingly proposed as deductive coders in qualitative research, but their measurement properties remain underexplored.
- **tags** #benchmark #difficulty

### P326. AI Clinical Decision Making Compared with Fellowship-Trained Hand Surgeons: A Case-Based Study.

- **ID** `PM42622576` · **日期** 2026 · **发表于** The Journal of hand surgery · **DOI** 10.1016/j.jhsa.2026.06.010
- **链接** https://pubmed.ncbi.nlm.nih.gov/42622576/
- **内容** Large language model-based artificial intelligence (AI) platforms have attracted substantial interest as potential clinical adjuncts within surgical specialties, particularly as patients have begun using AI for clinical advice.
- **tags** #difficulty #survey

### P327. Dental image analysis and surgical decision support using modified generative adversarial networks.

- **ID** `PM42410586` · **日期** 2026 · **发表于** BMC oral health · **DOI** 10.1186/s12903-026-09115-7
- **链接** https://pubmed.ncbi.nlm.nih.gov/42410586/
- **内容** Several clinical issues have remained in dental care and risk estimation because of the insufficient integration of multimodal features, the incapacity to integrate clinical domain literatures and evidence-based principles in their analytical platforms.
- **tags** #adaptive #cost #debate #diagnosis #safety #tools #verify

### P328. Automated iridocorneal angle classification using a multimodal large language model.

- **ID** `PM42363984` · **日期** 2026 · **发表于** Graefe's archive for clinical and experimental ophthalmology = Albrecht von Graefes Archiv fur klinische und experimentelle Ophthalmologie · **DOI** 10.1364/BOE.465286
- **链接** https://pubmed.ncbi.nlm.nih.gov/42363984/
- **内容** To evaluate the diagnostic performance of a general-purpose vision-language model (GPT-4o) in interpreting gonioscopic images of the anterior chamber angle, with a focus on angle configuration classification and Shaffer grading.
- **tags** #benchmark #diagnosis #role-play #tools #verify

### P329. Shaping AI in Pelvic Floor Physiotherapy: The Impact of Role-Play Prompting on ChatGPT Response Quality.

- **ID** `PM42217017` · **日期** 2026 · **发表于** International urogynecology journal · **DOI** 10.3389/fpubh.2024.1364660
- **链接** https://pubmed.ncbi.nlm.nih.gov/42217017/
- **内容** Pelvic floor physiotherapy (PFP) is a highly specialized field requiring complex and multidisiplinary clinical reasoning.
- **tags** #role-play

### P330. Artificial intelligence in cancer survivorship: evaluating ChatGPT's performance in rehabilitation-related queries.

- **ID** `PM41998423` · **日期** 2026 · **发表于** Supportive care in cancer : official journal of the Multinational Association of Supportive Care in Cancer · **DOI** 10.5014/ajot.2017.023572
- **链接** https://pubmed.ncbi.nlm.nih.gov/41998423/
- **内容** This study aimed to evaluate the performance of ChatGPT in responding to patient-centered queries related to cancer rehabilitation.
- **tags** #benchmark #safety #tools #verify

### P331. Comparative evaluation of large language model-based AI platforms for radiographic assessment in rheumatoid arthritis.

- **ID** `PM41936721` · **日期** 2026 · **发表于** Rheumatology international · **DOI** 10.1016/j.jacr.2022.06.019
- **链接** https://pubmed.ncbi.nlm.nih.gov/41936721/
- **内容** Rheumatoid arthritis (RA) is a chronic autoimmune disease characterized by progressive joint damage. Early diagnosis of this disease is crucial to prevent disability.
- **tags** #benchmark #cost #diagnosis #role-play #tools

### P332. Rationalisation of a thrombophilia panel using laboratory medicine Delphi-like consensus evaluation and secondary artificial intelligence-based simulation assessment.

- **ID** `PM41521528` · **日期** 2026 · **发表于** Diagnosis (Berlin, Germany) · **DOI** 10.1371/journal.pone.0298037
- **链接** https://pubmed.ncbi.nlm.nih.gov/41521528/
- **内容** It is important to review laboratory test panels regularly and omit unnecessary tests. This avoids overdiagnosis and makes laboratory work more targeted.
- **tags** #benchmark #diagnosis #tools

### P333. To Evaluate the Efficacy of Zero-Shot Prompting Using Large Language Models in the Extraction of Microbial Keratitis Descriptors.

- **ID** `PM41379872` · **日期** 2025 · **发表于** Cornea · **DOI** 10.1097/ICO.0000000000004049
- **链接** https://pubmed.ncbi.nlm.nih.gov/41379872/
- **内容** To extract microbial keratitis (MK) descriptors from clinician notes in electronic health records using Large Language Models (LLMs) with a zero-shot prompting approach and compare the descriptors with those identified by expert human annotators.
- **tags** #benchmark #cost

### P334. Evaluating the Performance of DeepSeek-R1 as a Patient Education Tool.

- **ID** `PM41212429` · **日期** 2025 · **发表于** Journal of medical systems · **DOI** 10.1016/j.jbi.2025.104812
- **链接** https://pubmed.ncbi.nlm.nih.gov/41212429/
- **内容** The cost-effective open-source artificial intelligence (AI) model DeepSeek-R1 in China holds significant potential for healthcare applications. As a health education tool, it could help patients acquire health science knowledge and improve health literacy.
- **tags** #benchmark #cost #difficulty #safety #tools #verify

### P335. Interpreting BI-RADS-Free Breast MRI Reports Using a Large Language Model: Automated BI-RADS Classification From Narrative Reports Using ChatGPT.

- **ID** `PM40915935` · **日期** 2025 · **发表于** Academic radiology · **DOI** 10.1016/j.acra.2025.08.026
- **链接** https://pubmed.ncbi.nlm.nih.gov/40915935/
- **内容** This study aimed to evaluate the performance of ChatGPT (GPT-4o) in interpreting free-text breast magnetic resonance imaging (MRI) reports by assigning BI-RADS categories and recommending appropriate clinical management steps in the absence of explicitly stated BI-RADS classifications.
- **tags** #benchmark #diagnosis #tools

### P336. An Institutional Large Language Model for Musculoskeletal MRI Improves Protocol Adherence and Accuracy.

- **ID** `PM40627696` · **日期** 2025 · **发表于** The Journal of bone and joint surgery. American volume · **DOI** 10.2106/JBJS.24.01429
- **链接** https://pubmed.ncbi.nlm.nih.gov/40627696/
- **内容** Privacy-preserving large language models (PP-LLMs) hold potential for assisting clinicians with documentation.
- **tags** #benchmark #diagnosis #rag

### P337. Integration of Multi-Source Medical Data for Medical Diagnosis Question Answering.

- **ID** `PM40030182` · **日期** 2025 · **发表于** IEEE transactions on medical imaging · **DOI** 10.1109/TMI.2024.3496862
- **链接** https://pubmed.ncbi.nlm.nih.gov/40030182/
- **内容** Medical question answering aims to enhance diagnostic support, improve patient education, and assist in clinical decision-making by automatically answering medical-related queries, which is an important foundation for realizing intelligent healthcare.
- **tags** #diagnosis #multi-agent

### P338. Applications and Future Prospects of Medical LLMs: A Survey Based on the M-KAT Conceptual Framework.

- **ID** `PM39725770` · **日期** 2024 · **发表于** Journal of medical systems · **DOI** 10.1016/j.psychres.2024.116026
- **链接** https://pubmed.ncbi.nlm.nih.gov/39725770/
- **内容** The success of large language models (LLMs) in general areas have sparked a wave of research into their applications in the medical field. However, enhancing the medical professionalism of these models remains a major challenge.
- **tags** #benchmark #diagnosis #multi-agent #safety #survey

### P339. Generative Artificial Intelligence in Pathology and Medicine: A Deeper Dive.

- **ID** `PM39689760` · **日期** 2025 · **发表于** Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc · **DOI** 10.1016/j.modpat.2024.100687
- **链接** https://pubmed.ncbi.nlm.nih.gov/39689760/
- **内容** This review article builds upon the introductory piece in our 7-part series, delving deeper into the transformative potential of generative artificial intelligence (Gen AI) in pathology and medicine.
- **tags** #cost #debate #diagnosis #multi-agent #safety #tools

### P340. Generative AI in Critical Care Nephrology: Applications and Future Prospects.

- **ID** `PM39217985` · **日期** 2024 · **发表于** Blood purification · **DOI** 10.1159/000541168
- **链接** https://pubmed.ncbi.nlm.nih.gov/39217985/
- **内容** Generative artificial intelligence (AI) is rapidly transforming various aspects of healthcare, including critical care nephrology.
- **tags** #diagnosis #multi-agent #safety #verify

### P341. GPT-4 versus human authors in clinically complex MCQ creation: A blinded analysis of item quality.

- **ID** `PM40439661` · **日期** 2025 · **发表于** Medical teacher · **DOI** 10.1080/0142159X.2025.2505122
- **链接** https://pubmed.ncbi.nlm.nih.gov/40439661/
- **内容** To compare the structural quality of multiple choice questions (MCQs) generated by a large language model, a type of artificial intelligence (AI), GPT-4, against human-authored items at both novice and expert level.
- **tags** #benchmark #safety

### P342. Large language models and psychiatry.

- **ID** `PM40020592` · **日期** 2025 · **发表于** International journal of law and psychiatry · **DOI** 10.1016/j.ijlp.2025.102086
- **链接** https://pubmed.ncbi.nlm.nih.gov/40020592/
- **内容** Integrating Generative Artificial Intelligence and Large Language Models (LLMs) such as GPT-4 is transforming clinical medicine and cognitive psychology.
- **tags** #debate

### P343. Constructing a Large Language Model to Generate Impressions from Findings in Radiology Reports.

- **ID** `PM39287525` · **日期** 2024 · **发表于** Radiology · **DOI** 10.1148/radiol.240885
- **链接** https://pubmed.ncbi.nlm.nih.gov/39287525/
- **内容** Background The specialization and complexity of radiology makes the automatic generation of radiologic impressions (ie, a diagnosis with differential diagnosis and management recommendations) challenging.
- **tags** #benchmark #diagnosis #difficulty #role-play #safety

### P344. ChatGPT and neurosurgical education: A crossroads of innovation and opportunity.

- **ID** `PM39236407` · **日期** 2024 · **发表于** Journal of clinical neuroscience : official journal of the Neurosurgical Society of Australasia · **DOI** 10.1016/j.jocn.2024.110815
- **链接** https://pubmed.ncbi.nlm.nih.gov/39236407/
- **内容** Large language models (LLM) have been promising recently in the medical field, with numerous applications in clinical neuroscience.
- **tags** #cost #debate #role-play #safety #tools

### P345. The utility of artificial intelligence platforms for patient-generated questions in Mohs micrographic surgery: a multi-national, blinded expert panel evaluation.

- **ID** `PM39123288` · **日期** 2024 · **发表于** International journal of dermatology · **DOI** 10.1111/ijd.17382
- **链接** https://pubmed.ncbi.nlm.nih.gov/39123288/
- **内容** Artificial intelligence (AI) and large language models (LLMs) transform how patients inform themselves. LLMs offer potential as educational tools, but their quality depends upon the information generated.
- **tags** #benchmark #role-play #tools

### P346. Are Generative Pretrained Transformer 4 Responses to Developmental Dysplasia of the Hip Clinical Scenarios Universal? An International Review.

- **ID** `PM38597198` · **日期** 2024 · **发表于** Journal of pediatric orthopedics · **DOI** 10.1097/BPO.0000000000002682
- **链接** https://pubmed.ncbi.nlm.nih.gov/38597198/
- **内容** There is increasing interest in applying artificial intelligence chatbots like generative pretrained transformer 4 (GPT-4) in the medical field.
- **tags** #benchmark #diagnosis #role-play

### P347. Artificial Intelligence for Anesthesiology Board-Style Examination Questions: Role of Large Language Models.

- **ID** `PM38423884` · **日期** 2024 · **发表于** Journal of cardiothoracic and vascular anesthesia · **DOI** 10.1053/j.jvca.2024.01.032
- **链接** https://pubmed.ncbi.nlm.nih.gov/38423884/
- **内容** New artificial intelligence tools have been developed that have implications for medical usage. Large language models (LLMs), such as the widely used ChatGPT developed by OpenAI, have not been explored in the context of anesthesiology education.
- **tags** #tools

### P348. A Quantitative Assessment of ChatGPT as a Neurosurgical Triaging Tool.

- **ID** `PM38353523` · **日期** 2024 · **发表于** Neurosurgery · **DOI** 10.21203/rs.3.rs-2566942/v1
- **链接** https://pubmed.ncbi.nlm.nih.gov/38353523/
- **内容** ChatGPT is a natural language processing chatbot with increasing applicability to the medical workflow.
- **tags** #benchmark #diagnosis #tools

### P349. [ChatGPT: aid to medical ethics decision making?].

- **ID** `PM38315183` · **日期** 2024 · **发表于** Die Anaesthesiologie · **DOI** 10.1080/15265161.2022.2075969
- **链接** https://pubmed.ncbi.nlm.nih.gov/38315183/
- **内容** Physicians have to make countless decisions every day. The medical, ethical and legal aspects are often intertwined and subject to change over time.
- **tags** #benchmark #debate

### P350. [ChatGPT: aid to medical ethics decision making?].

- **ID** `PM37821756` · **日期** 2023 · **发表于** Innere Medizin (Heidelberg, Germany) · **DOI** 10.1080/15265161.2022.2075969
- **链接** https://pubmed.ncbi.nlm.nih.gov/37821756/
- **内容** Physicians have to make countless decisions every day. The medical, ethical and legal aspects are often intertwined and subject to change over time.
- **tags** #benchmark #debate

## Part 4 · 预印本

> 尚未检索到正式发表记录。按本综述的发表优先策略，这些文献仅在其内容对研究问题不可替代时进入主分析，否则仅作背景。

| # | ID | 发表于 | tags | 标题 |
|---|---|---|---|---|
| 1 | `AX2609.21527` | arXiv 预印本 | #benchmark #cost #diagnosis #difficulty #multi-agent #role-play | OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi- |
| 2 | `AX2609.05069` | arXiv 预印本 | #benchmark #cost #debate #diagnosis #multi-agent #safety | A Structured Debate-Mixture-of-Agents Framework for Complex Cl |
| 3 | `AX2609.02191` | arXiv 预印本 | #diagnosis #medqa #multi-agent #safety | Examining the Vulnerability of Multi-Agent Medical Systems to  |
| 4 | `AX2608.22566` | arXiv 预印本 | #benchmark #debate #diagnosis #multi-agent | From Diagnosis to Redesign: Using Quantitative Ethnography to  |
| 5 | `AX2608.19029` | arXiv 预印本 | #adaptive #benchmark #difficulty #medmcqa #medqa #multi-agent | Adaptive Memory and Reflection Multi-Agent System for Medical  |
| 6 | `AX2608.06949` | arXiv 预印本 | #benchmark #debate #multi-agent #rag #safety | Does Splitting a Triage Decision Across Agents Hide Bias or He |
| 7 | `AX2608.04893` | arXiv 预印本 | #benchmark #cost #medqa #multi-agent #small-model | When Does Latent Communication Pay? A Causal Audit of Relayed  |
| 8 | `AX2608.03744` | arXiv 预印本 | #benchmark #medmcqa #medqa #multi-agent #usmle #verify | Agents Catching Agents: Shortcut Cascades and Benchmark Gaming |
| 9 | `AX2607.27443` | arXiv 预印本 | #benchmark #cost #diagnosis #difficulty #rag #verify | Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis |
| 10 | `AX2607.22385` | arXiv 预印本 | #adaptive #benchmark #diagnosis #tools #verify | Agentic Root Cause Analysis through Evidence-Grounded Reasonin |
| 11 | `AX2607.10275` | arXiv 预印本 | #benchmark #diagnosis #safety #verify | Information-seeking failures of large language models in agent |
| 12 | `AX2606.25334` | arXiv 预印本 | #adaptive #benchmark #cost #medqa #multi-agent #rag | Bridging the Post-discharge Gap: A Traceable Multi-agent Frame |
| 13 | `AX2606.22955` | arXiv 预印本 | #adaptive #benchmark #cost #diagnosis #rag | Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Ev |
| 14 | `AX2606.22419` | arXiv 预印本 | #benchmark #medqa #rag #tools | Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training  |
| 15 | `AX2606.21123` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #rag #safety #verify | A Multi-Agent Audit Framework for High-Stakes Reasoning: Evalu |
| 16 | `AX2606.18147` | arXiv 预印本 | #adaptive #benchmark #tools | WEQA: Wearable hEalth Question Answering with Query-Adaptive A |
| 17 | `AX2606.15931` | arXiv 预印本 | #multi-agent #rag #safety #tools #verify | DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic  |
| 18 | `AX2606.13945` | arXiv 预印本 | #benchmark #diagnosis #multi-agent | LatentDx: Latent Multi-Agent Communication for Cross-Hospital  |
| 19 | `AX2606.13197` | arXiv 预印本 | #adaptive #benchmark #cost #debate #ensemble #mmlu | ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Deba |
| 20 | `AX2606.08457` | arXiv 预印本 | #benchmark #debate #medqa #multi-agent #safety #usmle | The Consistency Illusion: How Multi-Agent Debate Hides Reasoni |
| 21 | `AX2606.03416` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #verify | MeDxAgent: Multi-Agent Consultation for Interactive Medical Di |
| 22 | `AX2606.01925` | arXiv 预印本 | #benchmark #diagnosis #rag #safety #tools #verify | QoEReasoner: An Agentic Reasoning Framework for Automated and  |
| 23 | `AX2606.01434` | arXiv 预印本 | #benchmark #cost #medqa #multi-agent #pubmedqa #rag | DrugClaw and DrugAudit: A Primary-Source-Grounded Agent and Au |
| 24 | `AX2606.00655` | arXiv 预印本 | #adaptive #cost #debate #multi-agent #verify | Scaling Behavior of Single LLM-Driven Multi-Agent Systems |
| 25 | `AX2606.00820` | arXiv 预印本 | #debate #mmlu #multi-agent #safety | Not All Flips Are Conformity: Decomposing Stance Convergence i |
| 26 | `AX2606.00405` | arXiv 预印本 | #benchmark #cost #ensemble #medmcqa #mmlu #multi-agent | From Talking Words to Sharing Thoughts: Scalable Multi-LLM Agg |
| 27 | `AX2605.27621` | arXiv 预印本 | #benchmark #cost #diagnosis #multi-agent #verify | Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Ba |
| 28 | `AX2605.24699` | arXiv 预印本 | #adaptive #benchmark #diagnosis #multi-agent #safety | MDIA: A Multi-Agent Diagnostic Intelligence Pipeline on Health |
| 29 | `AX2607.22555` | arXiv 预印本 | #benchmark #cost #diagnosis #ensemble #rag #small-model | DeepLens Diagnosis Agent: Agentic Workflow Design Lets a Small |
| 30 | `AX2605.05386` | arXiv 预印本 | #adaptive #benchmark #diagnosis | BALAR : A Bayesian Agentic Loop for Active Reasoning |
| 31 | `AX2604.17186` | arXiv 预印本 | #benchmark #cost #diagnosis #multi-agent #role-play #survey | Persona-Based Requirements Engineering for Explainable Multi-A |
| 32 | `AX2604.15456` | arXiv 预印本 | #benchmark #difficulty #medqa #rag #role-play #safety | DeepER-Med: Advancing Deep Evidence-Based Research in Medicine |
| 33 | `AX2604.08944` | arXiv 预印本 | #benchmark #cost #multi-agent | Multi-Agent Decision-Focused Learning via Value-Aware Sequenti |
| 34 | `AX2604.08203` | arXiv 预印本 | #benchmark #safety #verify | MedVR: Annotation-Free Medical Visual Reasoning via Agentic Re |
| 35 | `AX2604.07667` | arXiv 预印本 | #cost #debate #ensemble #mmlu #multi-agent #rag | From Debate to Decision: Conformal Social Choice for Safe Mult |
| 36 | `AX2603.27820` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #role-play #verify | Improving Clinical Diagnosis with Counterfactual Multi-Agent R |
| 37 | `AX2603.26122` | arXiv 预印本 | #benchmark #diagnosis #multi-agent | SkinGPT-X: A Self-Evolving Collaborative Multi-Agent System fo |
| 38 | `AX2603.24481` | arXiv 预印本 | #benchmark #diagnosis #ensemble #medmcqa #medqa #multi-agent | Multi-Agent Reasoning with Consistency Verification Improves U |
| 39 | `AX2603.21447` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #rag #safety | Deliberative multi-agent large language models improve clinica |
| 40 | `AX2603.13676` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #safety | TheraAgent: Multi-Agent Framework with Self-Evolving Memory an |
| 41 | `AX2603.01607` | arXiv 预印本 | #adaptive #benchmark #rag #safety #tools #verify | CARE: Towards Clinical Accountability in Multi-Modal Medical R |
| 42 | `AX2603.01131` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #role-play #verify | MedCollab: IBIS-Guided Multi-Agent Collaboration with Hierarch |
| 43 | `AX2602.19127` | arXiv 预印本 | #benchmark #diagnosis #rag #verify | AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-S |
| 44 | `AX2602.14160` | arXiv 预印本 | #benchmark #cost #multi-agent #tools #verify | Process-Supervised Multi-Agent Reinforcement Learning for Reli |
| 45 | `AX2602.09341` | arXiv 预印本 | #benchmark #cost #ensemble #multi-agent #safety #verify | Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority  |
| 46 | `AX2603.03292` | arXiv 预印本 | #benchmark #cost #rag #safety #verify | From Conflict to Consensus: Boosting Medical Reasoning via Mul |
| 47 | `AX2602.03794` | arXiv 预印本 | #cost #difficulty #multi-agent #tools | Understanding Agent Scaling in LLM-Based Multi-Agent Systems v |
| 48 | `AX2602.02455` | arXiv 预印本 | #benchmark #diagnosis #rag #role-play #safety | Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents u |
| 49 | `AX2601.20221` | arXiv 预印本 | #adaptive #benchmark #cost #medqa #medxpertqa #rag | Scaling Medical Reasoning Verification via Tool-Integrated Rei |
| 50 | `AX2512.15398` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #rag #tools #verify | Mapis: A Knowledge-Graph Grounded Multi-Agent Framework for Ev |
| 51 | `AX2512.14321` | arXiv 预印本 | #benchmark #cost #medbullets #medqa #multi-agent #pubmedqa | Multi-Agent Medical Decision Consensus Matrix System: An Intel |
| 52 | `AX2512.02485` | arXiv 预印本 | #benchmark #cost #debate #diagnosis #multi-agent #role-play | UCAgents: Unidirectional Convergence for Visual Evidence Ancho |
| 53 | `AX2511.11169` | arXiv 预印本 | #benchmark #debate #diagnosis #ensemble #multi-agent #tools | Refine and Align: Confidence Calibration through Multi-Agent I |
| 54 | `AX2511.05528` | arXiv 预印本 | #adaptive #cost #debate #mmlu #multi-agent | SMAGDi: Socratic Multi Agent Interaction Graph Distillation fo |
| 55 | `AX2510.04969` | arXiv 预印本 | #benchmark #cost #difficulty #multi-agent #rag #verify | Bridging Clinical Narratives and ACR Appropriateness Guideline |
| 56 | `AX2510.01499` | arXiv 预印本 | #benchmark #ensemble #mmlu #multi-agent #rag | Beyond Majority Voting: LLM Aggregation by Leveraging Higher-O |
| 57 | `AX2509.23368` | arXiv 预印本 | #benchmark #cmexam #cost #diagnosis #small-model #verify | MedCritical: Enhancing Medical Reasoning in Small Language Mod |
| 58 | `AX2509.23188` | arXiv 预印本 | #benchmark #cost #diagnosis #medqa #multi-agent #tools | Diagnose, Localize, Align: A Full-Stack Framework for Reliable |
| 59 | `AX2509.20067` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #rag #small-model #verify | MACD: Multi-Agent Clinical Diagnosis with Self-Learned Knowled |
| 60 | `AX2509.14998` | arXiv 预印本 | #adaptive #benchmark #diagnosis #multi-agent #rag #role-play | A Knowledge-driven Adaptive Collaboration of LLMs for Enhancin |
| 61 | `AX2508.15746` | arXiv 预印本 | #benchmark #diagnosis #rag #safety #verify | End-to-End Agentic RAG System Training for Traceable Diagnosti |
| 62 | `AX2508.13754` | arXiv 预印本 | #adaptive #benchmark #debate #diagnosis #difficulty #mmlu | Expertise-aware Multi-LLM Recruitment and Collaboration for Me |
| 63 | `AX2508.08115` | arXiv 预印本 | #benchmark #cost #multi-agent #small-model | TeamMedAgents: Pareto-Efficient Multi-Agent Medical Reasoning  |
| 64 | `AX2508.05996` | arXiv 预印本 | #benchmark #cost #multi-agent | Mediator-Guided Multi-Agent Collaboration among Open-Source Mo |
| 65 | `AX2507.08916` | arXiv 预印本 | #benchmark #medmcqa #medqa #mmlu #pubmedqa #safety | Evaluating LLMs in Medicine: A Call for Rigor, Transparency |
| 66 | `AX2507.03254` | arXiv 预印本 | #benchmark #cost #multi-agent #tools #verify | CodeAgents: A Token-Efficient Framework for Codified Multi-Age |
| 67 | `AX2506.19835` | arXiv 预印本 | #benchmark #cost #diagnosis #multi-agent #rag #role-play | MAM: Modular Multi-Agent Framework for Multi-Modal Medical Dia |
| 68 | `AX2506.01257` | arXiv 预印本 | #benchmark #cost #debate #diagnosis #safety #survey | DeepSeek in Healthcare: A Survey of Capabilities, Risks, and C |
| 69 | `AX2506.00555` | arXiv 预印本 | #adaptive #benchmark #diagnosis #multi-agent #rag #role-play | MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimo |
| 70 | `AX2505.23075` | arXiv 预印本 | #adaptive #benchmark #cost #diagnosis #ensemble #medmcqa | Second Opinion Matters: Towards Adaptive Clinical AI via the C |
| 71 | `AX2505.21503` | arXiv 预印本 | #benchmark #diagnosis #difficulty #multi-agent #rag #safety | Silence is Not Consensus: Disrupting Agreement Bias in Multi-A |
| 72 | `AX2505.20096` | arXiv 预印本 | #benchmark #cost #multi-agent #rag #small-model #verify | MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collabo |
| 73 | `AX2505.14996` | arXiv 预印本 | #adaptive #benchmark #cost #multi-agent #rag #verify | MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision |
| 74 | `AX2505.12371` | arXiv 预印本 | #benchmark #difficulty #multi-agent #verify | MedAgentBoard: Benchmarking Multi-Agent Collaboration with Con |
| 75 | `AX2504.21252` | arXiv 预印本 | #benchmark #medqa #pubmedqa #rag #safety | Talk Before You Retrieve: Agent-Led Discussions for Better RAG |
| 76 | `AX2503.13856` | arXiv 预印本 | #cost #diagnosis #ensemble #medqa #multi-agent #pubmedqa | MDTeamGPT: A Self-Evolving LLM-based Multi-Agent Framework for |
| 77 | `AX2503.07306` | arXiv 预印本 | #benchmark #rag #safety #verify | Benchmarking Chinese Medical LLMs: A Medbench-based Analysis o |
| 78 | `AX2502.11271` | arXiv 预印本 | #medqa #mmlu #multi-agent #rag #tools | OctoTools: An Agentic Framework with Extensible Tools for Comp |
| 79 | `AX2410.12868` | arXiv 预印本 | #adaptive #benchmark #diagnosis #difficulty #medqa #pubmedqa | IMAS: A Comprehensive Agentic Approach to Rural Healthcare Del |
| 80 | `AX2311.10537` | arXiv 预印本 | #medmcqa #medqa #mmlu #pubmedqa #rag #role-play | MedAgents: Large Language Models as Collaborators for Zero-sho |
| 81 | `AX2311.00855` | arXiv 预印本 | #adaptive #cost #diagnosis #ensemble #multi-agent #rag | A Multi-Agent Reinforcement Learning Framework for Public Heal |
| 82 | `AX2305.12031` | arXiv 预印本 | #benchmark #cost #medmcqa #medqa #pubmedqa #rag | Clinical Camel: An Open Expert-Level Medical Language Model wi |
| 83 | `AX2305.09617` | arXiv 预印本 | #benchmark #debate #ensemble #medmcqa #medqa #mmlu | Towards Expert-Level Medical Question Answering with Large Lan |

### P41. OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems

- **ID** `AX2609.21527` · **日期** 2026-09-18 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2609.21527.pdf`
- **链接** https://arxiv.org/abs/2609.21527
- **内容** Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities.
- **tags** #benchmark #cost #diagnosis #difficulty #multi-agent #role-play #verify

### P42. A Structured Debate-Mixture-of-Agents Framework for Complex Clinical Diagnostic Decision Support

- **ID** `AX2609.05069` · **日期** 2026-09-04 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2609.05069.pdf`
- **链接** https://arxiv.org/abs/2609.05069
- **内容** Large language models (LLMs) show potential for medical tasks, but their single-turn question-answer format does not reflect how clinical diagnosis is performed in practice. As a result, they remain limited in complex diagnostic settings.
- **tags** #benchmark #cost #debate #diagnosis #multi-agent #safety

### P43. Examining the Vulnerability of Multi-Agent Medical Systems to Human Interventions for Clinical Reasoning

- **ID** `AX2609.02191` · **日期** 2026-09-02 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2609.02191.pdf`
- **链接** https://arxiv.org/abs/2609.02191
- **内容** Human interventions at fault points can alter the diagnostic accuracy of multi-agent medical systems. We defined fault points as moments in AI agent conversations, in which an agent's reasoning became most vulnerable to external influence.
- **tags** #diagnosis #medqa #multi-agent #safety

### P44. From Diagnosis to Redesign: Using Quantitative Ethnography to Improve Multi-Agent LLM Reasoning

- **ID** `AX2608.22566` · **日期** 2026-08-23 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2608.22566.pdf`
- **链接** https://arxiv.org/abs/2608.22566
- **内容** Multi-agent large language model (LLM) systems are designed to improve reasoning by decomposing tasks across multiple agents with specialized functions, but the presence of multiple agents does not inherently guarantee coherent reasoning or outputs that align with task objectives.
- **tags** #benchmark #debate #diagnosis #multi-agent

### P45. Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering

- **ID** `AX2608.19029` · **日期** 2026-08-19 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2608.19029.pdf`
- **链接** https://arxiv.org/abs/2608.19029
- **内容** Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning.
- **tags** #adaptive #benchmark #difficulty #medmcqa #medqa #multi-agent #rag

### P46. Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints

- **ID** `AX2608.06949` · **日期** 2026-08-07 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2608.06949.pdf`
- **链接** https://arxiv.org/abs/2608.06949
- **内容** Prior benchmarking work has shown that a single large language model (LLM), forced to make life-or-death resource-allocation decisions, exhibits measurable demographic bias.
- **tags** #benchmark #debate #multi-agent #rag #safety

### P47. When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs

- **ID** `AX2608.04893` · **日期** 2026-08-05 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2608.04893.pdf`
- **链接** https://arxiv.org/abs/2608.04893
- **内容** Multi-agent LLM systems relay key-value caches instead of text and credit their gains to exchanged "latent thoughts". That credit is a claim about which example's cache is relayed, not merely that one is.
- **tags** #benchmark #cost #medqa #multi-agent #small-model

### P48. Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi-Agent Systems

- **ID** `AX2608.03744` · **日期** 2026-08-04 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2608.03744.pdf`
- **链接** https://arxiv.org/abs/2608.03744
- **内容** Clinical decision support is moving toward committees of language-model agents deliberating on a shared workspace. We ask whether such committees can be gamed by shortcuts, cues a benchmark rewards but a clinician would ignore.
- **tags** #benchmark #medmcqa #medqa #multi-agent #usmle #verify

### P49. Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems

- **ID** `AX2607.27443` · **日期** 2026-07-29 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2607.27443.pdf`
- **链接** https://arxiv.org/abs/2607.27443
- **内容** Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks. However, they often struggle with long-horizon interactive tasks common in domains, such as embodied AI.
- **tags** #benchmark #cost #diagnosis #difficulty #rag #verify

### P410. Agentic Root Cause Analysis through Evidence-Grounded Reasoning

- **ID** `AX2607.22385` · **日期** 2026-07-24 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2607.22385.pdf`
- **链接** https://arxiv.org/abs/2607.22385
- **内容** Diagnosing the root cause of anomalies is essential for safe industrial operation. Despite extensive sensor instrumentation, formulating hypotheses and gathering evidence remains a manual process, creating a major operational bottleneck.
- **tags** #adaptive #benchmark #diagnosis #tools #verify

### P411. Information-seeking failures of large language models in agentic clinical reasoning

- **ID** `AX2607.10275` · **日期** 2026-07-11 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2607.10275.pdf`
- **链接** https://arxiv.org/abs/2607.10275
- **内容** Large language models achieve high scores on medical knowledge assessments, yet clinical reasoning requires actively deciding what to investigate under uncertainty.
- **tags** #benchmark #diagnosis #safety #verify

### P412. Bridging the Post-discharge Gap: A Traceable Multi-agent Framework for Safe and Continuous Care

- **ID** `AX2606.25334` · **日期** 2026-06-24 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.25334.pdf`
- **链接** https://arxiv.org/abs/2606.25334
- **内容** Post-discharge clinical follow-up is critical for maintaining continuity of care and mitigating long-term health risks.
- **tags** #adaptive #benchmark #cost #medqa #multi-agent #rag #safety #verify

### P413. Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval

- **ID** `AX2606.22955` · **日期** 2026-06-22 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.22955.pdf`
- **链接** https://arxiv.org/abs/2606.22955
- **内容** Large-scale pretrained foundation models have revolutionized general medical screening, but often falter on rare diseases because such conditions are underrepresented in real-world clinical datasets.
- **tags** #adaptive #benchmark #cost #diagnosis #rag

### P414. Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training Knowledge: A Controlled Study on Clinical Question Answering

- **ID** `AX2606.22419` · **日期** 2026-06-21 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2606.22419.pdf`
- **链接** https://arxiv.org/abs/2606.22419
- **内容** A recent Nature Medicine study reports that general-purpose frontier LLMs outperform specialized retrieval-augmented clinical tools on medical benchmarks, and that retrieval can hurt strong models.
- **tags** #benchmark #medqa #rag #tools

### P415. A Multi-Agent Audit Framework for High-Stakes Reasoning: Evaluation and Interpretability in Clinical Mental Health Screening

- **ID** `AX2606.21123` · **日期** 2026-06-19 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.21123.pdf`
- **链接** https://arxiv.org/abs/2606.21123
- **内容** High-stakes reasoning tasks necessitate transparent and verifiable workflows, yet conventional single-model large language models (LLMs) often struggle with hallucination and low interpretability under zero-shot paradigms.
- **tags** #benchmark #diagnosis #multi-agent #rag #safety #verify

### P416. WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning

- **ID** `AX2606.18147` · **日期** 2026-06-16 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2606.18147.pdf`
- **链接** https://arxiv.org/abs/2606.18147
- **内容** Language models are remarkably capable at medical question answering, in some cases surpassing the accuracy of general physicians.
- **tags** #adaptive #benchmark #tools

### P417. DeepRoot: A KG-Coordinated Multi-Agent System for Therapeutic Reasoning over Historical Medical Texts

- **ID** `AX2606.15931` · **日期** 2026-06-14 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.15931.pdf`
- **链接** https://arxiv.org/abs/2606.15931
- **内容** Historical medical archives and traditional medicines hold immense potential for drug discovery and remain a primary source for current drug development.
- **tags** #multi-agent #rag #safety #tools #verify

### P418. LatentDx: Latent Multi-Agent Communication for Cross-Hospital Rare-Disease Diagnosis

- **ID** `AX2606.13945` · **日期** 2026-06-11 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2606.13945.pdf`
- **链接** https://arxiv.org/abs/2606.13945
- **内容** Rare diseases affect over $300$ million patients across more than $7{,}000$ conditions, yet no single hospital encounters enough cases of any one condition for reliable diagnosis.
- **tags** #benchmark #diagnosis #multi-agent

### P419. ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning

- **ID** `AX2606.13197` · **日期** 2026-06-11 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.13197.pdf`
- **链接** https://arxiv.org/abs/2606.13197
- **内容** Multi-agent debate (MAD) can improve large language model reasoning, but fixed debate pipelines often waste computation and can amplify correlated errors among similar agents.
- **tags** #adaptive #benchmark #cost #debate #ensemble #mmlu #multi-agent

### P420. The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment

- **ID** `AX2606.08457` · **日期** 2026-06-07 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.08457.pdf`
- **链接** https://arxiv.org/abs/2606.08457
- **内容** Multi-agent LLM systems for medical question answering often treat consensus as a reliability signal: if multiple agents agree on an answer, it is presumed trustworthy. However, answer-level consensus does not entail reasoning-level alignment.
- **tags** #benchmark #debate #medqa #multi-agent #safety #usmle #verify

### P421. MeDxAgent: Multi-Agent Consultation for Interactive Medical Diagnosis

- **ID** `AX2606.03416` · **日期** 2026-06-02 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2606.03416.pdf`
- **链接** https://arxiv.org/abs/2606.03416
- **内容** Large language models (LLMs) are increasingly used for health-related decision support. Yet most evaluations treat diagnosis as a single-shot task with complete information provided upfront, often as a multiple-choice selection.
- **tags** #benchmark #diagnosis #multi-agent #verify

### P422. QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs

- **ID** `AX2606.01925` · **日期** 2026-06-01 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.01925.pdf`
- **链接** https://arxiv.org/abs/2606.01925
- **内容** Diagnosing Quality-of-Experience (QoE) degradations in operational Radio Access Networks (RANs) is a critical but notoriously complex task, traditionally requiring labor-intensive expert analysis over high-dimensional, cross-layer telemetry.
- **tags** #benchmark #diagnosis #rag #safety #tools #verify

### P423. DrugClaw and DrugAudit: A Primary-Source-Grounded Agent and Authority-Aware Benchmark for Drug-Information Question Answering

- **ID** `AX2606.01434` · **日期** 2026-05-31 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.01434.pdf`
- **链接** https://arxiv.org/abs/2606.01434
- **内容** Drug-information question answering is a high-stakes setting where hallucinated facts can mislead clinical decision-making and the provenance of each cited fact matters as much as the fact itself.
- **tags** #benchmark #cost #medqa #multi-agent #pubmedqa #rag #safety

### P424. Scaling Behavior of Single LLM-Driven Multi-Agent Systems

- **ID** `AX2606.00655` · **日期** 2026-05-30 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.00655.pdf`
- **链接** https://arxiv.org/abs/2606.00655
- **内容** The burgeoning field of LLM-based Multi-Agent Systems (MAS) promises to tackle complex tasks through collaborative intelligence, yet fundamental questions regarding their scaling behavior and intrinsic collective dynamics remain underexplored.
- **tags** #adaptive #cost #debate #multi-agent #verify

### P425. Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate

- **ID** `AX2606.00820` · **日期** 2026-05-30 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2606.00820.pdf`
- **链接** https://arxiv.org/abs/2606.00820
- **内容** Multi-agent debate (MAD) is a promising strategy for improving LLM reasoning, but when agents converge on a shared answer, it is unclear whether that convergence reflects genuine deliberation or social compliance.
- **tags** #debate #mmlu #multi-agent #safety

### P426. From Talking Words to Sharing Thoughts: Scalable Multi-LLM Aggregation via Structured Message Passing

- **ID** `AX2606.00405` · **日期** 2026-05-29 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2606.00405.pdf`
- **链接** https://arxiv.org/abs/2606.00405
- **内容** The emergence of specialized, domain-tuned Large Language Models (LLMs) has demonstrated that smaller models can achieve expert-level performance in specific tasks, while struggling in out-of-domain settings.
- **tags** #benchmark #cost #ensemble #medmcqa #mmlu #multi-agent #verify

### P427. Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution

- **ID** `AX2605.27621` · **日期** 2026-05-26 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2605.27621.pdf`
- **链接** https://arxiv.org/abs/2605.27621
- **内容** As multi-agent systems (MAS) become increasingly complex, identifying the contributions of individual agents is critical for system optimization. However, existing approaches lack a rigorous, unified framework for credit assignment.
- **tags** #benchmark #cost #diagnosis #multi-agent #verify

### P428. MDIA: A Multi-Agent Diagnostic Intelligence Pipeline on HealthBench Professional

- **ID** `AX2605.24699` · **日期** 2026-05-23 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2605.24699.pdf`
- **链接** https://arxiv.org/abs/2605.24699
- **内容** Most reported gains on agentic-LLM clinical benchmarks are often attributed to prompt engineering, yet our results suggest that larger improvements can come from architectural and engine-level design.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #safety

### P429. DeepLens Diagnosis Agent: Agentic Workflow Design Lets a Small Reasoning Model Compete with Frontier LLMs

- **ID** `AX2607.22555` · **日期** 2026-05-19 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2607.22555.pdf`
- **链接** https://arxiv.org/abs/2607.22555
- **内容** Medical diagnosis is a multi-stage process: extract facts, consult knowledge, generate a differential analysis, and select the best diagnosis with explanations.
- **tags** #benchmark #cost #diagnosis #ensemble #rag #small-model

### P430. BALAR : A Bayesian Agentic Loop for Active Reasoning

- **ID** `AX2605.05386` · **日期** 2026-05-06 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2605.05386.pdf`
- **链接** https://arxiv.org/abs/2605.05386
- **内容** Large language models increasingly operate in interactive settings where solving a task requires multiple rounds of information exchange with a user.
- **tags** #adaptive #benchmark #diagnosis

### P431. Persona-Based Requirements Engineering for Explainable Multi-Agent Educational Systems: A Scenario Simulator for Clinical Reasoning Training

- **ID** `AX2604.17186` · **日期** 2026-04-19 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2604.17186.pdf`
- **链接** https://arxiv.org/abs/2604.17186
- **内容** As Artificial Intelligence (AI) and Agentic AI become increasingly integrated across sectors such as education and healthcare, it is critical to ensure that Multi-Agent Education System (MAES) is explainable from the early stages of requirements engineering (RE) within the AI software development lifecycle.
- **tags** #benchmark #cost #diagnosis #multi-agent #role-play #survey #verify

### P432. DeepER-Med: Advancing Deep Evidence-Based Research in Medicine Through Agentic AI

- **ID** `AX2604.15456` · **日期** 2026-04-16 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2604.15456.pdf`
- **链接** https://arxiv.org/abs/2604.15456
- **内容** Trustworthiness and transparency are essential for the clinical adoption of artificial intelligence (AI) in healthcare and biomedical research.
- **tags** #benchmark #difficulty #medqa #rag #role-play #safety

### P433. Multi-Agent Decision-Focused Learning via Value-Aware Sequential Communication

- **ID** `AX2604.08944` · **日期** 2026-04-10 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2604.08944.pdf`
- **链接** https://arxiv.org/abs/2604.08944
- **内容** Multi-agent coordination under partial observability requires agents to share complementary private information.
- **tags** #benchmark #cost #multi-agent

### P434. MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning

- **ID** `AX2604.08203` · **日期** 2026-04-09 · **发表于** arXiv 预印本 · **被引** 7
- **PDF** `documents/arXiv_2604.08203.pdf`
- **链接** https://arxiv.org/abs/2604.08203
- **内容** Medical Vision-Language Models (VLMs) hold immense promise for complex clinical tasks, but their reasoning capabilities are often constrained by text-only paradigms that fail to ground inferences in visual evidence.
- **tags** #benchmark #safety #verify

### P435. From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation

- **ID** `AX2604.07667` · **日期** 2026-04-09 · **发表于** arXiv 预印本 · **被引** 5
- **PDF** `documents/arXiv_2604.07667.pdf`
- **链接** https://arxiv.org/abs/2604.07667
- **内容** Multi-agent debate improves LLM reasoning, yet agreement among agents is not evidence of correctness. When agents converge on a wrong answer through social reinforcement, consensus-based stopping commits that error to an automated action with no recourse.
- **tags** #cost #debate #ensemble #mmlu #multi-agent #rag #safety

### P436. Improving Clinical Diagnosis with Counterfactual Multi-Agent Reasoning

- **ID** `AX2603.27820` · **日期** 2026-03-29 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2603.27820.pdf`
- **链接** https://arxiv.org/abs/2603.27820
- **内容** Clinical diagnosis is a complex reasoning process in which clinicians gather evidence, form hypotheses, and test them against alternative explanations.
- **tags** #benchmark #diagnosis #multi-agent #role-play #verify

### P437. SkinGPT-X: A Self-Evolving Collaborative Multi-Agent System for Transparent and Trustworthy Dermatological Diagnosis

- **ID** `AX2603.26122` · **日期** 2026-03-27 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2603.26122.pdf`
- **链接** https://arxiv.org/abs/2603.26122
- **内容** While recent advancements in Large Language Models have significantly advanced dermatological diagnosis, monolithic LLMs frequently struggle with fine-grained, large-scale multi-class diagnostic tasks and rare skin disease diagnosis owing to training data sparsity, while also lacking the interpretability and traceability essential for clinical reasoning.
- **tags** #benchmark #diagnosis #multi-agent

### P438. Multi-Agent Reasoning with Consistency Verification Improves Uncertainty Calibration in Medical MCQA

- **ID** `AX2603.24481` · **日期** 2026-03-25 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2603.24481.pdf`
- **链接** https://arxiv.org/abs/2603.24481
- **内容** Miscalibrated confidence scores are a practical obstacle to deploying AI in clinical settings. A model that is always overconfident offers no useful signal for deferral.
- **tags** #benchmark #diagnosis #ensemble #medmcqa #medqa #multi-agent #role-play #small-model #usmle #verify

### P439. Deliberative multi-agent large language models improve clinical reasoning in ophthalmology

- **ID** `AX2603.21447` · **日期** 2026-03-22 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2603.21447.pdf`
- **链接** https://arxiv.org/abs/2603.21447
- **内容** Large language models (LLMs) show potential for ophthalmic clinical reasoning, yet individual models risk introducing harm. We evaluated whether multi-agent LLM deliberative councils improve diagnostic performance and mitigate harm compared to individual LLMs.
- **tags** #benchmark #diagnosis #multi-agent #rag #safety

### P440. TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics

- **ID** `AX2603.13676` · **日期** 2026-03-14 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2603.13676.pdf`
- **链接** https://arxiv.org/abs/2603.13676
- **内容** PET theranostics is transforming precision oncology, yet treatment response varies substantially; many patients receiving 177Lu-PSMA radioligand therapy (RLT) for metastatic castration-resistant prostate cancer (mCRPC) fail to respond, demanding reliable pre-therapy prediction.
- **tags** #benchmark #diagnosis #multi-agent #safety

### P441. CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework

- **ID** `AX2603.01607` · **日期** 2026-03-02 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2603.01607.pdf`
- **链接** https://arxiv.org/abs/2603.01607
- **内容** Large visual language models (VLMs) have shown strong multi-modal medical reasoning ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability.
- **tags** #adaptive #benchmark #rag #safety #tools #verify

### P442. MedCollab: IBIS-Guided Multi-Agent Collaboration with Hierarchical Disease Relation Chains for Clinical Diagnosis

- **ID** `AX2603.01131` · **日期** 2026-03-01 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2603.01131.pdf`
- **链接** https://arxiv.org/abs/2603.01131
- **内容** Clinical diagnosis is a gradual process of evidence integration, in which physicians move from symptoms and medical history to examinations, competing hypotheses, disease relations, and treatment decisions.
- **tags** #benchmark #diagnosis #multi-agent #role-play #verify

### P443. AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG

- **ID** `AX2602.19127` · **日期** 2026-02-22 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2602.19127.pdf`
- **链接** https://arxiv.org/abs/2602.19127
- **内容** With the rapid advancement of agent-based methods in recent years, Agentic RAG has undoubtedly become an important research direction.
- **tags** #benchmark #diagnosis #rag #verify

### P444. Process-Supervised Multi-Agent Reinforcement Learning for Reliable Clinical Reasoning

- **ID** `AX2602.14160` · **日期** 2026-02-15 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2602.14160.pdf`
- **链接** https://arxiv.org/abs/2602.14160
- **内容** Clinical decision-making requires nuanced reasoning over heterogeneous evidence and traceable justifications.
- **tags** #benchmark #cost #multi-agent #tools #verify

### P445. Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge

- **ID** `AX2602.09341` · **日期** 2026-02-10 · **发表于** arXiv 预印本 · **被引** 13
- **PDF** `documents/arXiv_2602.09341.pdf`
- **链接** https://arxiv.org/abs/2602.09341
- **内容** Multi-agent systems (MAS) can substantially extend the reasoning capacity of large language models (LLMs). Most MAS frameworks aggregate agent outputs via simple majority voting, discarding the evidential structure of reasoning traces.
- **tags** #benchmark #cost #ensemble #multi-agent #safety #verify

### P446. From Conflict to Consensus: Boosting Medical Reasoning via Multi-Round Agentic RAG

- **ID** `AX2603.03292` · **日期** 2026-02-06 · **发表于** arXiv 预印本 · **被引** 3
- **PDF** `documents/arXiv_2603.03292.pdf`
- **链接** https://arxiv.org/abs/2603.03292
- **内容** Large Language Models (LLMs) exhibit high reasoning capacity in medical question-answering, but their tendency to produce hallucinations and outdated knowledge poses critical risks in healthcare fields.
- **tags** #benchmark #cost #rag #safety #verify

### P447. Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

- **ID** `AX2602.03794` · **日期** 2026-02-03 · **发表于** arXiv 预印本 · **被引** 27
- **PDF** `documents/arXiv_2602.03794.pdf`
- **链接** https://arxiv.org/abs/2602.03794
- **内容** LLM-based multi-agent systems (MAS) have emerged as a promising approach to tackle complex tasks that are difficult for individual LLMs.
- **tags** #cost #difficulty #multi-agent #tools

### P448. Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction

- **ID** `AX2602.02455` · **日期** 2026-02-02 · **发表于** arXiv 预印本 · **被引** 8
- **PDF** `documents/arXiv_2602.02455.pdf`
- **链接** https://arxiv.org/abs/2602.02455
- **内容** As Large Language Models transition to autonomous agents, user inputs frequently violate cooperative assumptions (e.g., implicit intent, missing parameters, false presuppositions, or ambiguous expressions), creating execution risks that text-only evaluations do not capture.
- **tags** #benchmark #diagnosis #rag #role-play #safety

### P449. Scaling Medical Reasoning Verification via Tool-Integrated Reinforcement Learning

- **ID** `AX2601.20221` · **日期** 2026-01-28 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2601.20221.pdf`
- **链接** https://arxiv.org/abs/2601.20221
- **内容** Large language models have achieved strong performance on medical reasoning benchmarks, yet their deployment in clinical settings demands rigorous verification to ensure factual accuracy.
- **tags** #adaptive #benchmark #cost #medqa #medxpertqa #rag #tools #verify

### P450. Mapis: A Knowledge-Graph Grounded Multi-Agent Framework for Evidence-Based PCOS Diagnosis

- **ID** `AX2512.15398` · **日期** 2025-12-17 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2512.15398.pdf`
- **链接** https://arxiv.org/abs/2512.15398
- **内容** Polycystic Ovary Syndrome (PCOS) constitutes a significant public health issue affecting 10% of reproductive-aged women, highlighting the critical importance of developing effective diagnostic tools.
- **tags** #benchmark #diagnosis #multi-agent #rag #tools #verify

### P451. Multi-Agent Medical Decision Consensus Matrix System: An Intelligent Collaborative Framework for Oncology MDT Consultations

- **ID** `AX2512.14321` · **日期** 2025-12-16 · **发表于** arXiv 预印本 · **被引** 15
- **PDF** `documents/arXiv_2512.14321.pdf`
- **链接** https://arxiv.org/abs/2512.14321
- **内容** Multidisciplinary team (MDT) consultations are the gold standard for cancer care decision-making, yet current practice lacks structured mechanisms for quantifying consensus and ensuring decision traceability.
- **tags** #benchmark #cost #medbullets #medqa #multi-agent #pubmedqa #rag #role-play

### P452. UCAgents: Unidirectional Convergence for Visual Evidence Anchored Multi-Agent Medical Decision-Making

- **ID** `AX2512.02485` · **日期** 2025-12-02 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2512.02485.pdf`
- **链接** https://arxiv.org/abs/2512.02485
- **内容** Vision-Language Models (VLMs) show promise in medical diagnosis, yet suffer from reasoning detachment, where linguistically fluent explanations drift from verifiable image evidence, undermining clinical trust.
- **tags** #benchmark #cost #debate #diagnosis #multi-agent #role-play #safety #verify

### P453. Refine and Align: Confidence Calibration through Multi-Agent Interaction in VQA

- **ID** `AX2511.11169` · **日期** 2025-11-14 · **发表于** arXiv 预印本 · **被引** 5
- **PDF** `documents/arXiv_2511.11169.pdf`
- **链接** https://arxiv.org/abs/2511.11169
- **内容** In the context of Visual Question Answering (VQA) and Agentic AI, calibration refers to how closely an AI system's confidence in its answers reflects their actual correctness.
- **tags** #benchmark #debate #diagnosis #ensemble #multi-agent #tools #verify

### P454. SMAGDi: Socratic Multi Agent Interaction Graph Distillation for Efficient High Accuracy Reasoning

- **ID** `AX2511.05528` · **日期** 2025-10-29 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2511.05528.pdf`
- **链接** https://arxiv.org/abs/2511.05528
- **内容** Multi-agent systems (MAS) often achieve higher reasoning accuracy than single models, but their reliance on repeated debates across agents makes them computationally expensive.
- **tags** #adaptive #cost #debate #mmlu #multi-agent

### P455. Bridging Clinical Narratives and ACR Appropriateness Guidelines: A Multi-Agent RAG System for Medical Imaging Decisions

- **ID** `AX2510.04969` · **日期** 2025-10-06 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2510.04969.pdf`
- **链接** https://arxiv.org/abs/2510.04969
- **内容** The selection of appropriate medical imaging procedures is a critical and complex clinical decision, guided by extensive evidence-based standards such as the ACR Appropriateness Criteria (ACR-AC).
- **tags** #benchmark #cost #difficulty #multi-agent #rag #verify

### P456. Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information

- **ID** `AX2510.01499` · **日期** 2025-10-01 · **发表于** arXiv 预印本 · **被引** 23
- **PDF** `documents/arXiv_2510.01499.pdf`
- **链接** https://arxiv.org/abs/2510.01499
- **内容** With the rapid progress of multi-agent large language model (LLM) reasoning, how to effectively aggregate answers from multiple LLMs has emerged as a fundamental challenge.
- **tags** #benchmark #ensemble #mmlu #multi-agent #rag

### P457. MedCritical: Enhancing Medical Reasoning in Small Language Models via Self-Collaborative Correction

- **ID** `AX2509.23368` · **日期** 2025-09-27 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2509.23368.pdf`
- **链接** https://arxiv.org/abs/2509.23368
- **内容** In the field of medicine, complex reasoning tasks such as clinical diagnosis, treatment planning, and medical knowledge integration pose significant challenges, where small language models often underperform compared to large language models like GPT-4 and Deepseek.
- **tags** #benchmark #cmexam #cost #diagnosis #small-model #verify

### P458. Diagnose, Localize, Align: A Full-Stack Framework for Reliable LLM Multi-Agent Systems under Instruction Conflicts

- **ID** `AX2509.23188` · **日期** 2025-09-27 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2509.23188.pdf`
- **链接** https://arxiv.org/abs/2509.23188
- **内容** Large Language Model (LLM)-powered multi-agent systems (MAS) have rapidly advanced collaborative reasoning, tool use, and role-specialized coordination in complex tasks.
- **tags** #benchmark #cost #diagnosis #medqa #multi-agent #tools #verify

### P459. MACD: Multi-Agent Clinical Diagnosis with Self-Learned Knowledge for LLM

- **ID** `AX2509.20067` · **日期** 2025-09-24 · **发表于** arXiv 预印本 · **被引** 9
- **PDF** `documents/arXiv_2509.20067.pdf`
- **链接** https://arxiv.org/abs/2509.20067
- **内容** Large language models (LLMs) have shown promise in supporting medical diagnosis, with prompting-based methods offering a flexible and deployable means of capability enhancement.
- **tags** #benchmark #diagnosis #multi-agent #rag #small-model #verify

### P460. A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making

- **ID** `AX2509.14998` · **日期** 2025-09-18 · **发表于** arXiv 预印本 · **被引** 6
- **PDF** `documents/arXiv_2509.14998.pdf`
- **链接** https://arxiv.org/abs/2509.14998
- **内容** Medical decision-making often involves integrating knowledge from multiple clinical specialties, typically achieved through multidisciplinary teams.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #rag #role-play

### P461. End-to-End Agentic RAG System Training for Traceable Diagnostic Reasoning

- **ID** `AX2508.15746` · **日期** 2025-08-21 · **发表于** arXiv 预印本 · **被引** 13
- **PDF** `documents/arXiv_2508.15746.pdf`
- **链接** https://arxiv.org/abs/2508.15746
- **内容** The integration of Large Language Models (LLMs) into healthcare is constrained by knowledge limitations, hallucinations, and a disconnect from Evidence-Based Medicine (EBM).
- **tags** #benchmark #diagnosis #rag #safety #verify

### P462. Expertise-aware Multi-LLM Recruitment and Collaboration for Medical Decision-Making

- **ID** `AX2508.13754` · **日期** 2025-08-19 · **发表于** arXiv 预印本 · **被引** 1
- **PDF** `documents/arXiv_2508.13754.pdf`
- **链接** https://arxiv.org/abs/2508.13754
- **内容** Medical Decision-Making (MDM) is a complex process requiring substantial domain-specific expertise to effectively synthesize heterogeneous and complicated clinical information.
- **tags** #adaptive #benchmark #debate #diagnosis #difficulty #mmlu #multi-agent #rag

### P463. TeamMedAgents: Pareto-Efficient Multi-Agent Medical Reasoning Through Teamwork Theory

- **ID** `AX2508.08115` · **日期** 2025-08-11 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2508.08115.pdf`
- **链接** https://arxiv.org/abs/2508.08115
- **内容** Complex medical reasoning has historically required frontier language models to achieve clinically-acceptable accuracy, creating computational barriers that limit deployment in resource-constrained clinical settings.
- **tags** #benchmark #cost #multi-agent #small-model

### P464. Mediator-Guided Multi-Agent Collaboration among Open-Source Models for Medical Decision-Making

- **ID** `AX2508.05996` · **日期** 2025-08-08 · **发表于** arXiv 预印本 · **被引** 4
- **PDF** `documents/arXiv_2508.05996.pdf`
- **链接** https://arxiv.org/abs/2508.05996
- **内容** Complex medical decision-making involves cooperative workflows operated by different clinicians. Designing AI multi-agent systems can expedite and augment human-level clinical decision-making.
- **tags** #benchmark #cost #multi-agent

### P465. Evaluating LLMs in Medicine: A Call for Rigor, Transparency

- **ID** `AX2507.08916` · **日期** 2025-07-11 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2507.08916.pdf`
- **链接** https://arxiv.org/abs/2507.08916
- **内容** Objectives: To evaluate the current limitations of large language models (LLMs) in medical question answering, focusing on the quality of datasets used for their evaluation.
- **tags** #benchmark #medmcqa #medqa #mmlu #pubmedqa #safety #tools #verify

### P466. CodeAgents: A Token-Efficient Framework for Codified Multi-Agent Reasoning in LLMs

- **ID** `AX2507.03254` · **日期** 2025-07-04 · **发表于** arXiv 预印本 · **被引** 8
- **PDF** `documents/arXiv_2507.03254.pdf`
- **链接** https://arxiv.org/abs/2507.03254
- **内容** Effective prompt design is essential for improving the planning capabilities of large language model (LLM)-driven agents.
- **tags** #benchmark #cost #multi-agent #tools #verify

### P467. MAM: Modular Multi-Agent Framework for Multi-Modal Medical Diagnosis via Role-Specialized Collaboration

- **ID** `AX2506.19835` · **日期** 2025-06-24 · **发表于** arXiv 预印本 · **被引** 66
- **PDF** `documents/arXiv_2506.19835.pdf`
- **链接** https://arxiv.org/abs/2506.19835
- **内容** Recent advancements in medical Large Language Models (LLMs) have showcased their powerful reasoning and diagnostic capabilities.
- **tags** #benchmark #cost #diagnosis #multi-agent #rag #role-play

### P468. DeepSeek in Healthcare: A Survey of Capabilities, Risks, and Clinical Applications of Open-Source Large Language Models

- **ID** `AX2506.01257` · **日期** 2025-06-02 · **发表于** arXiv 预印本 · **被引** 14
- **PDF** `documents/arXiv_2506.01257.pdf`
- **链接** https://arxiv.org/abs/2506.01257
- **内容** DeepSeek-R1 is a cutting-edge open-source large language model (LLM) developed by DeepSeek, showcasing advanced reasoning capabilities through a hybrid architecture that integrates mixture of experts (MoE), chain of thought (CoT) reasoning, and reinforcement learning.
- **tags** #benchmark #cost #debate #diagnosis #safety #survey #usmle

### P469. MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning

- **ID** `AX2506.00555` · **日期** 2025-05-31 · **发表于** arXiv 预印本 · **被引** 45
- **PDF** `documents/arXiv_2506.00555.pdf`
- **链接** https://arxiv.org/abs/2506.00555
- **内容** Medical Large Vision-Language Models (Med-LVLMs) have shown strong potential in multimodal diagnostic tasks. However, existing single-agent models struggle to generalize across diverse medical specialties, limiting their performance.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #rag #role-play

### P470. Second Opinion Matters: Towards Adaptive Clinical AI via the Consensus of Expert Model Ensemble

- **ID** `AX2505.23075` · **日期** 2025-05-29 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2505.23075.pdf`
- **链接** https://arxiv.org/abs/2505.23075
- **内容** Despite the growing clinical adoption of large language models (LLMs), current approaches heavily rely on single model architectures.
- **tags** #adaptive #benchmark #cost #diagnosis #ensemble #medmcqa #medqa #medxpertqa #role-play #safety

### P471. Silence is Not Consensus: Disrupting Agreement Bias in Multi-Agent LLMs via Catfish Agent for Clinical Decision Making

- **ID** `AX2505.21503` · **日期** 2025-05-27 · **发表于** arXiv 预印本 · **被引** 2
- **PDF** `documents/arXiv_2505.21503.pdf`
- **链接** https://arxiv.org/abs/2505.21503
- **内容** Large language models (LLMs) have demonstrated strong potential in clinical question answering, with recent multi-agent frameworks further improving diagnostic accuracy via collaborative reasoning.
- **tags** #benchmark #diagnosis #difficulty #multi-agent #rag #safety #verify

### P472. MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning

- **ID** `AX2505.20096` · **日期** 2025-05-26 · **发表于** arXiv 预印本 · **被引** 43
- **PDF** `documents/arXiv_2505.20096.pdf`
- **链接** https://arxiv.org/abs/2505.20096
- **内容** We present MA-RAG, a Multi-Agent framework for Retrieval-Augmented Generation (RAG) that addresses the inherent ambiguities and reasoning challenges in complex information-seeking tasks.
- **tags** #benchmark #cost #multi-agent #rag #small-model #verify

### P473. MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision

- **ID** `AX2505.14996` · **日期** 2025-05-21 · **发表于** arXiv 预印本 · **被引** 27
- **PDF** `documents/arXiv_2505.14996.pdf`
- **链接** https://arxiv.org/abs/2505.14996
- **内容** Multi-agent systems (MAS) leveraging the impressive capabilities of Large Language Models (LLMs) hold significant potential for tackling complex tasks. However, most current MAS depend on manually designed agent roles and communication protocols.
- **tags** #adaptive #benchmark #cost #multi-agent #rag #verify

### P474. MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks

- **ID** `AX2505.12371` · **日期** 2025-05-18 · **发表于** arXiv 预印本 · **被引** 38
- **PDF** `documents/arXiv_2505.12371.pdf`
- **链接** https://arxiv.org/abs/2505.12371
- **内容** The rapid advancement of Large Language Models (LLMs) has stimulated interest in multi-agent collaboration for addressing complex medical tasks. However, the practical advantages of multi-agent collaboration approaches remain insufficiently understood.
- **tags** #benchmark #difficulty #multi-agent #verify

### P475. Talk Before You Retrieve: Agent-Led Discussions for Better RAG in Medical QA

- **ID** `AX2504.21252` · **日期** 2025-04-30 · **发表于** arXiv 预印本 · **被引** 11
- **PDF** `documents/arXiv_2504.21252.pdf`
- **链接** https://arxiv.org/abs/2504.21252
- **内容** Medical question answering (QA) is a reasoning-intensive task that remains challenging for large language models (LLMs) due to hallucinations and outdated domain knowledge.
- **tags** #benchmark #medqa #pubmedqa #rag #safety

### P476. MDTeamGPT: A Self-Evolving LLM-based Multi-Agent Framework for Multi-Disciplinary Team Medical Consultation

- **ID** `AX2503.13856` · **日期** 2025-03-18 · **发表于** arXiv 预印本 · **被引** 35
- **PDF** `documents/arXiv_2503.13856.pdf`
- **链接** https://arxiv.org/abs/2503.13856
- **内容** Large Language Models (LLMs) have made significant progress in various fields. However, challenges remain in Multi-Disciplinary Team (MDT) medical consultations.
- **tags** #cost #diagnosis #ensemble #medqa #multi-agent #pubmedqa #role-play

### P477. Benchmarking Chinese Medical LLMs: A Medbench-based Analysis of Performance Gaps and Hierarchical Optimization Strategies

- **ID** `AX2503.07306` · **日期** 2025-03-10 · **发表于** arXiv 预印本 · **被引** 3
- **PDF** `documents/arXiv_2503.07306.pdf`
- **链接** https://arxiv.org/abs/2503.07306
- **内容** The evaluation and improvement of medical large language models (LLMs) are critical for their real-world deployment, particularly in ensuring accuracy, safety, and ethical alignment.
- **tags** #benchmark #rag #safety #verify

### P478. OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning

- **ID** `AX2502.11271` · **日期** 2025-02-16 · **发表于** arXiv 预印本 · **被引** 75
- **PDF** `documents/arXiv_2502.11271.pdf`
- **链接** https://arxiv.org/abs/2502.11271
- **内容** Solving complex reasoning tasks may involve visual understanding, domain knowledge retrieval, numerical calculation, and multi-step reasoning.
- **tags** #medqa #mmlu #multi-agent #rag #tools

### P479. IMAS: A Comprehensive Agentic Approach to Rural Healthcare Delivery

- **ID** `AX2410.12868` · **日期** 2024-10-13 · **发表于** arXiv 预印本 · **被引** 6
- **PDF** `documents/arXiv_2410.12868.pdf`
- **链接** https://arxiv.org/abs/2410.12868
- **内容** Since the onset of COVID-19, rural communities worldwide have faced significant challenges in accessing healthcare due to the migration of experienced medical professionals to urban centers.
- **tags** #adaptive #benchmark #diagnosis #difficulty #medqa #pubmedqa #role-play

### P480. MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning

- **ID** `AX2311.10537` · **日期** 2023-11-16 · **发表于** arXiv 预印本 · **被引** 529
- **PDF** `documents/arXiv_2311.10537.pdf`
- **链接** https://arxiv.org/abs/2311.10537
- **内容** Large language models (LLMs), despite their remarkable progress across various general domains, encounter significant barriers in medicine and healthcare.
- **tags** #medmcqa #medqa #mmlu #pubmedqa #rag #role-play #verify

### P481. A Multi-Agent Reinforcement Learning Framework for Public Health Decision Analysis

- **ID** `AX2311.00855` · **日期** 2023-11-01 · **发表于** arXiv 预印本 · **被引** 0
- **PDF** `documents/arXiv_2311.00855.pdf`
- **链接** https://arxiv.org/abs/2311.00855
- **内容** Human immunodeficiency virus (HIV) is a major public health concern in the United States (U.S.), with about 1.2 million people living with it and about 35,000 newly infected each year.
- **tags** #adaptive #cost #diagnosis #ensemble #multi-agent #rag #verify

### P482. Clinical Camel: An Open Expert-Level Medical Language Model with Dialogue-Based Knowledge Encoding

- **ID** `AX2305.12031` · **日期** 2023-05-19 · **发表于** arXiv 预印本 · **被引** 91
- **PDF** `documents/arXiv_2305.12031.pdf`
- **链接** https://arxiv.org/abs/2305.12031
- **内容** We present Clinical Camel, an open large language model (LLM) explicitly tailored for clinical research. Fine-tuned from LLaMA-2 using QLoRA, Clinical Camel achieves state-of-the-art performance across medical benchmarks among openly available medical LLMs.
- **tags** #benchmark #cost #medmcqa #medqa #pubmedqa #rag #safety #usmle

### P483. Towards Expert-Level Medical Question Answering with Large Language Models

- **ID** `AX2305.09617` · **日期** 2023-05-16 · **发表于** arXiv 预印本 · **被引** 818
- **PDF** `documents/arXiv_2305.09617.pdf`
- **链接** https://arxiv.org/abs/2305.09617
- **内容** Recent artificial intelligence (AI) systems have reached milestones in "grand challenges" ranging from Go to protein-folding.
- **tags** #benchmark #debate #ensemble #medmcqa #medqa #mmlu #pubmedqa #rag #usmle #verify

## Part 5 · 下载失败

> 可重试。

| # | ID | 发表于 | tags | 标题 |
|---|---|---|---|---|
| 1 | `AX2511.15974` | arXiv 预印本 | #adaptive #benchmark #cost #diagnosis #difficulty #medqa | KRAL: Knowledge and Reasoning Augmented Learning for LLM-assis |
| 2 | `AX2509.11656` | arXiv 预印本 | #benchmark #cost #debate #mmlu #multi-agent #rag | MALLM: Multi-Agent Large Language Models Framework |
| 3 | `AX2506.20430` | arXiv 预印本 | #benchmark #diagnosis #multi-agent #rag #tools #verify | An Agentic System for Rare Disease Diagnosis with Traceable Re |
| 4 | `AX2503.16547` | arXiv 预印本 | #adaptive #benchmark #diagnosis #multi-agent | Empowering Medical Multi-Agents with Clinical Consultation Flo |
| 5 | `AX2501.05464` | arXiv 预印本 | #benchmark #cost #medqa #multi-agent #rag #verify | LLM-MedQA: Enhancing Medical Question Answering through Case S |
| 6 | `AX2401.14589` | arXiv 预印本 | #adaptive #benchmark #diagnosis #multi-agent #rag #safety | Enhancing Diagnostic Accuracy through Multi-Agent Conversation |

### P51. KRAL: Knowledge and Reasoning Augmented Learning for LLM-assisted Clinical Antimicrobial Therapy

- **ID** `AX2511.15974` · **日期** 2025-11-20 · **发表于** arXiv 预印本
- **链接** https://arxiv.org/abs/2511.15974
- **内容** Clinical antimicrobial therapy requires the dynamic integration of pathogen profiles,host factors, pharmacological properties of antimicrobials,and the severity of infection.
- **tags** #adaptive #benchmark #cost #diagnosis #difficulty #medqa #rag #safety

### P52. MALLM: Multi-Agent Large Language Models Framework

- **ID** `AX2509.11656` · **日期** 2025-09-15 · **发表于** arXiv 预印本
- **链接** https://arxiv.org/abs/2509.11656
- **内容** Multi-agent debate (MAD) has demonstrated the ability to augment collective intelligence by scaling test-time compute and leveraging expertise.
- **tags** #benchmark #cost #debate #mmlu #multi-agent #rag #role-play #tools #verify

### P53. An Agentic System for Rare Disease Diagnosis with Traceable Reasoning

- **ID** `AX2506.20430` · **日期** 2025-06-25 · **发表于** arXiv 预印本
- **链接** https://arxiv.org/abs/2506.20430
- **内容** Rare diseases affect over 300 million individuals worldwide, yet timely and accurate diagnosis remains an urgent challenge.
- **tags** #benchmark #diagnosis #multi-agent #rag #tools #verify

### P54. Empowering Medical Multi-Agents with Clinical Consultation Flow for Dynamic Diagnosis

- **ID** `AX2503.16547` · **日期** 2025-03-19 · **发表于** arXiv 预印本
- **链接** https://arxiv.org/abs/2503.16547
- **内容** Traditional AI-based healthcare systems often rely on single-modal data, limiting diagnostic accuracy due to incomplete information.
- **tags** #adaptive #benchmark #diagnosis #multi-agent

### P55. LLM-MedQA: Enhancing Medical Question Answering through Case Studies in Large Language Models

- **ID** `AX2501.05464` · **日期** 2024-12-31 · **发表于** arXiv 预印本
- **链接** https://arxiv.org/abs/2501.05464
- **内容** Accurate and efficient question-answering systems are essential for delivering high-quality patient care in the medical field.
- **tags** #benchmark #cost #medqa #multi-agent #rag #verify

### P56. Enhancing Diagnostic Accuracy through Multi-Agent Conversations: Using Large Language Models to Mitigate Cognitive Bias

- **ID** `AX2401.14589` · **日期** 2024-01-26 · **发表于** arXiv 预印本
- **链接** https://arxiv.org/abs/2401.14589
- **内容** Background: Cognitive biases in clinical decision-making significantly contribute to errors in diagnosis and suboptimal patient outcomes. Addressing these biases presents a formidable challenge in the medical field.
- **tags** #adaptive #benchmark #diagnosis #multi-agent #rag #safety
