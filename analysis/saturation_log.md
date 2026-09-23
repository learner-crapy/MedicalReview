# 文献饱和度检查循环日志

**机制**：检查 agent（Opus 5）评估横向（4 个 RQ + 成本维度）与纵向（每维子面）覆盖度 → 主 agent 用 built-in browser（Google Scholar / ACL Anthology / 其他平台）+ API 补检 → 再检查。最多 10 轮。

**停止条件**（满足其一）：
1. 检查 agent 判定 5 个维度全部达到饱和；
2. 单轮新增「已发表且可提取」文献 ≤ 2 篇，连续 2 轮；
3. 达到 10 轮。

| Epoch | 检查结论 | 补检动作 | 新增已发表 | 新增可提取比较 |
|---|---|---|---|---|
| 1 | 检查 agent 运行中（Opus 5，browser+Scholar） | 主 agent 并行执行：引文追溯 1005 篇→筛出 43 篇新的已发表医学 MAS 文献并下载 8 篇；提取 MedAgentBoard(NeurIPS)、MDAgents(NeurIPS)、MedLA(AAAI)、S-DAG(AAAI) 四篇已发表核心研究 | +8 PDF（累计 181） | +39 行（累计 97 行 / 19 项研究） |
| 1（完成） | **未饱和**。指出结构性缺口：整支「MAS vs 强单代理/同预算采样」的通用域方法学文献（ACL/NeurIPS/ICLR 高被引）不在 2288 条记录内；提取欠账（RAG/verify/judge 三个 P0 机制 0 行）；代理数阶梯 Type B=0；RQ4 仅 2 study；δ_base 不可算；纳排口径不一致（通用域行已进主表） | 执行指令 1/2/11/12：补下 12 篇高被引缺口文献 + Auditing reasoning trees + 中文 MedBench 分析；修 row_id 重复；新增 domain/split/sampling_method/n_items 列；裁决通用域归入背景层并记入 plan §12.5；提取 SEMA-RAG 填补 C3.2 | +15 PDF | +16 行（RAG 有/无对照首次落地） |
| 2（完成） | **未饱和，但瓶颈已从检索转为提取**。17 条检索（ACL Anthology×8 / Scholar×7 / PubMed×2）只产出 1 篇能改变结论的新已发表文献（CAMEC）；同时查出 37 篇已发表已下载文献未进数据表，Epoch1 的 5 个缺口有 4 个证据就在 documents/ 里。**并抓到主 agent 一处数据错误**：MDAgents 的 R 用推算值 5，而原文自报 9.3/20.3 calls | 修正 MDAgents 成本口径（reported）；提取 JAMIA 2026（judge 臂 9 行）、CAMEC（中文 EG 3 行）、GoA 代理数阶梯（4 行）；下载 CAMEC/LAMP-MedQA/DynTopology/4 篇 arXiv | +8 PDF（累计 204） | +16 行；**5 个 P0 缺口全部关闭** |
| 3（完成） | **检索侧已饱和，提取侧远未饱和**。重算差集得 105 篇「已发表+已下载+未提取」（Epoch2 报 37 篇为低估），其中 14 篇含数值级证据、可新增 120+ 行。**抓到主 agent 4 处提取错误**：J01–J09 误读 JAMIA 表格区块（前15行=投票/后15行=judge）导致「judge 比 vote 只高 0.71pp」结论错误；R07 误取 9 数据集总平均造成重复计数；P04/P05 漏填原生 API calls 且漏提 4 个 MAS 臂；G01–G16 漏填 token 口径 | 全部修正：J 行按正确区块重算（投票 vs 最强单代理 **中位 −0.71**；judge vs vote **+3.60**）；R07 改为 MMLU 6 科目均值；补 EUNACOM 4 臂（3/4 为负）；批量提取 KAMAC/ClinicalAgents/神经科PLOS/Aegle/AgentFactory/MAM | — | **+51 行**（主分析 158 行 / 23 项研究） |
| 4（完成） | **检索侧饱和正式成立**（连续第 3 轮，本轮新增可提取 = **0**）。提取侧：逐篇打开原文后确认 Epoch3 清单 9 篇中**仅 MedAgentsBench 通过 IN2**，其余 7 篇结局非考试式 MCQ → 证据地图/背景层。**再抓到 12 处错误，10 处集中于 AgentFactory**（漏取 Reflexion 作单代理上界、未识别混合 backbone + 在基准训练集上微调）；另指出 31 行开源模型被误标 S6_closed、J08 取值非区块最大、缺 EG 分层标记导致"诊断 F1 与 MedQA 准确率画进同一张图"的风险 | 落库 MedAgentsBench **108 行**（抽验 3/3 通过）；修 8 类问题；新增 `eg_tier` 与 `attribution_flag` 两列；补 MedAgents 的 few-shot CoT+SC 对照 4 行 | 0（检索已饱和） | **+112 行**（总 293 行） |
| 5（完成） | **整体饱和成立**（检索连续第 4 轮新增 = 0；提取侧 MedAgentsBench 108 行经**全量**核对 108/108 无误）。但判定「数据质量未达可发表标准」，给出 1 CRITICAL + 4 HIGH：**主结论未处理研究内聚类**（102 行仅来自 13 篇、一篇占 47%，行级统计是伪精度）；CAMEC 存在与 AgentFactory 同类的微调混淆却未打 flag；OpenAlex 1129 条从未进入筛选而论文却声称三源；MedAgentsBench 发表年份错（Patterns 2026）；论文摘要与多处正文仍是旧数据 | 全部修复：建 `analysis/main_analysis.py` 做**研究聚类 bootstrap**；CAMEC 打 flag 并补其唯一归因干净的消融行；eg_tier 重分层 50 行；108 行年份改 Patterns 2026 + refs.bib 换已发表条目；摘要/RQ1/讨论/局限全文重写；删除失效表与悬空引用；figs.py 写入完整过滤链重绘 4 图 | 0 | 主分析口径定稿：**n=93 / 13 项研究** |
