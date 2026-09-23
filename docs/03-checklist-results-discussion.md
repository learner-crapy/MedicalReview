# 03 · 清单第 16–27 条详解（结果 / 讨论 / 其他信息）

原文出处：Page MJ, et al. *BMJ* 2021;372:n71 与 n160，CC BY 4.0。

结果部分的第一原则：**结果里只写结果**。方法不要重述，解释留给讨论。第二原则：**结果与方法一一对应**——方法里写了 13e（异质性探索），结果里就必须有 20c；写了 15（确信度方法），结果里就必须有 22。

---

## RESULTS

### 条目 16a · 筛选结果
> **Describe the results of the search and selection process, from the number of records identified in the search to the number of studies included in the review, ideally using a flow diagram.**
> 描述检索与筛选结果，从检索到的记录数一直到最终纳入的研究数，最好使用流程图。

**怎么写**：
- 用 PRISMA 流程图（见 [`05-flow-diagram.md`](05-flow-diagram.md)）。
- 正文用一两句话给出关键数字：检索总数 → 去重后 → 全文评估数 → 纳入研究数（及对应报告数）。
- 若用自动化工具排除记录，**单独列出其排除数量**。
- 可报告筛选者一致性（kappa）。

**常见错误**：流程图里的数字与正文/表格对不上；去重数与"其他原因移除"混在一起。

### 条目 16b · 看似合格却被排除的研究
> **Cite studies that might appear to meet the inclusion criteria, but which were excluded, and explain why they were excluded.**
> 引用那些看似符合纳入标准却被排除的研究，并解释排除原因。

**怎么写**：全文阶段排除的研究做成一张表：**文献引用 + 唯一的主要排除理由**。只需列"看起来像是该纳入的"那些，不必列全部。

**为什么重要**：这是 2020 年新增条目，作用是让读者能够检验并挑战你的边界判断。这也是最能体现综述诚实度的地方之一。

### 条目 17 · 研究特征
> **Cite each included study and present its characteristics.**
> 引用每一项纳入研究并呈现其特征。

**怎么写**：一张"纳入研究特征表"，通常包含：
- 研究标识（作者年份）、设计、场景、国家
- 对象人数与特征
- 干预与对照的细节
- 测量的结局与时间点
- 资助来源与利益冲突（E&E 明确要求）

**位置要求**：该表属于**结果**，不属于方法。

### 条目 18 · 各研究的偏倚风险
> **Present assessments of risk of bias for each included study.**
> 呈现每项纳入研究的偏倚风险评价结果。

**怎么写**：逐研究 × 逐领域的表或 traffic-light 图（绿/黄/红），而不是单一总分。可补充各领域低/高/不清楚的比例汇总。

### 条目 19 · 各研究的结果
> **For all outcomes, present, for each study: (a) summary statistics for each group (where appropriate) and (b) an effect estimate and its precision (e.g. confidence/credible interval), ideally using structured tables or plots.**
> 对所有结局，逐研究呈现：(a) 各组的汇总统计量（如适用）；(b) 效应估计值及其精度（如置信区间/可信区间），最好用结构化表格或图。

**怎么写**：
- **所有**分析过的结局都要报告，不论是否显著。
- 给出人数、随访时长等解释所需的上下文。
- 说明一项研究有多个结果时如何处理（呈现全部还是按预设规则选一个）。

### 条目 20a–20d · 综合结果

> **20a** For each synthesis, briefly summarise the characteristics and risk of bias among contributing studies（每项综合中，简述贡献研究的特征与偏倚风险）。
> **20b** Present results of all statistical syntheses conducted. If meta-analysis was done, present for each the summary estimate and its precision (e.g. confidence/credible interval) and measures of statistical heterogeneity. If comparing groups, describe the direction of the effect（呈现所有统计综合的结果；若做荟萃分析，给出合并估计值、精度与异质性指标；若比较组间，说明效应方向）。
> **20c** Present results of all investigations of possible causes of heterogeneity among study results（呈现所有异质性来源探索的结果）。
> **20d** Present results of all sensitivity analyses conducted to assess the robustness of the synthesised results（呈现所有敏感性分析结果）。

**怎么写**：
- 荟萃分析：森林图 + 合并估计 + 95% CI + I²（及 τ²、预测区间）+ 研究数与总样本量。
- 非荟萃综合：按 **SWiM** 报告——研究如何分组、用了什么标准化指标、综合方法是什么、结果的方向与幅度如何汇总。
- 亚组分析要给出**交互作用检验**，不能只比较两个亚组各自是否显著。
- **所有**预设的敏感性分析都要报告结果，包括"结论未改变"这种无聊结果。

**常见错误**：
- 只报告显著的亚组（事后挑选）。
- 用 "results were mixed" 一句话打发异质性——异质性是发现，需要解释，不是噪声。
- 只给 p 值不给效应量和区间。

### 条目 21 · 报告偏倚
> **Present assessments of risk of bias due to missing results (arising from reporting biases) for each synthesis assessed.**
> 对每项评估过的综合，呈现因结果缺失（报告偏倚）导致的偏倚风险评价结果。

**怎么写**：漏斗图（研究数足够时）、Egger/Begg 检验结果、protocol 与发表结果的比对结论；并说明若存在偏倚，对结论解释的影响。研究数不足以评估时，明确写出来。

### 条目 22 · 证据确信度
> **Present assessments of certainty (or confidence) in the body of evidence for each outcome assessed.**
> 对每个评估过的结局，呈现证据体确信度的评价结果。

**怎么写**：GRADE 评级 + **每次降级/升级的具体理由**；最好做一张 Summary of Findings 表（结局、研究数/人数、效应估计、CI、确信度等级、备注）。

---

## DISCUSSION

### 条目 23a · 结果解释
> **Provide a general interpretation of the results in the context of other evidence.**

**怎么写**：开头一段总结主要发现（**只一段**，不要重述结果）；然后把发现放回已有证据中：与既往综述一致还是冲突？冲突的可能原因是什么？

### 条目 23b · 证据的局限
> **Discuss any limitations of the evidence included in the review.**

指**纳入研究本身**的局限：偏倚风险、不一致性、间接性、不精确性、报告偏倚——通常与 GRADE 的降级理由一一对应。

### 条目 23c · 综述过程的局限
> **Discuss any limitations of the review processes used.**

指**你自己这项工作**的局限：检索可能不全、语言限制、单人筛选、无法获取原始数据、提取判断的主观性等。诚实陈述，但不必自我贬低。

> 两者不能混为一谈：23b 说的是"证据不够好"，23c 说的是"我的方法有限"。审稿人很在意这个区分。

### 条目 23d · 意义
> **Discuss implications of the results for practice, policy, and future research.**

**怎么写**：
- 对实践/政策的建议必须与证据确信度匹配（GRADE 的措辞约定：强推荐用 "we recommend"，弱推荐用 "we suggest"）。
- 对未来研究的建议要具体：需要什么设计、什么对照、什么结局、什么报告标准——而不是万能句"需要更多高质量研究"。
- 明确区分 **efficacy（理想条件下有效）** 与 **effectiveness（真实场景中有效）**，不要越界推断。

---

## OTHER INFORMATION

### 条目 24a–24c · 注册与 protocol
> **24a** Provide registration information for the review, including register name and registration number, or state that the review was not registered（给出注册信息，含注册库名称与编号；或声明未注册）。
> **24b** Indicate where the review protocol can be accessed, or state that a protocol was not prepared（说明 protocol 在哪里可获取；或声明未撰写 protocol）。
> **24c** Describe and explain any amendments to information provided at registration or in the protocol（描述并解释对注册信息或 protocol 的任何修订）。

**要点**：没注册不是致命伤，**没注册却假装预设**才是。24c 是诚信条目：任何偏离 protocol 的改动都要写出来并说明理由与时点（是在看到结果之前还是之后决定的）。

### 条目 25 · 资助
> **Describe sources of financial or non-financial support for the review, and the role of the funders or sponsors in the review.**

要写明资助方**在综述中的角色**（是否参与设计、分析、决定是否发表），不是只写基金号。

### 条目 26 · 利益冲突
> **Declare any competing interests of review authors.**

包括：作者是否是纳入研究的作者、是否与被评价的方法/产品有关系。若作者的研究被纳入，应说明由谁来做该研究的筛选与偏倚评价（应由未参与该研究的作者承担）。

### 条目 27 · 数据、代码与其他材料的可得性
> **Report which of the following are publicly available and where they can be found: template data collection forms; data extracted from included studies; data used for all analyses; analytic code; any other materials used in the review.**
> 报告以下哪些材料可公开获取及获取地址：提取表模板；从纳入研究提取的数据；所有分析所用数据；分析代码；综述中使用的其他材料。

**怎么写**：给出仓库链接（OSF / Zenodo / GitHub）与 DOI。这是 2020 年新增条目，对计算类、数据密集型综述尤其重要——它让别人可以重跑你的综合，而不只是重读你的结论。

---

## 结果与讨论部分自检

- [ ] 流程图数字与正文、表格完全一致
- [ ] 全文排除的"像是该纳入"的研究有表、有唯一理由
- [ ] 纳入研究特征表在结果而非方法
- [ ] 偏倚风险按领域呈现，没有合成总分
- [ ] 所有分析过的结局都报告了，包括阴性结果
- [ ] 方法里承诺的每一项亚组、敏感性分析，结果里都有对应结果
- [ ] 讨论区分了"证据的局限"与"综述过程的局限"
- [ ] protocol 的每处偏离都在 24c 里写明并解释
- [ ] 数据与代码给出了可访问地址
