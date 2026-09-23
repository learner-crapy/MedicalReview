# 02 · 清单第 1–15 条详解（标题 / 摘要 / 引言 / 方法）

每条给出四部分：**① 官方要求**（原文关键句 + 中译）→ **② 怎么写**（E&E 的报告要点）→ **③ 合格判据**（自检问题）→ **④ 常见错误**。

原文出处：Page MJ, et al. *BMJ* 2021;372:n71（清单）与 n160（解释与详述），CC BY 4.0。

---

## TITLE

### 条目 1 · 标题
> **Identify the report as a systematic review.**
> 在标题中标明本文是一篇系统综述。

**怎么写**：标题里必须出现 "systematic review" 字样；若做了荟萃分析，写成 "…: a systematic review and meta-analysis"。若用了特定扩展类型，写明（"scoping review"、"network meta-analysis"）。

**合格判据**：读者只看标题，能否判断这是二次研究而非原创实验？数据库检索时能否被 "systematic review" 这个词捞到？

**常见错误**：标题写成 "A review of…" 或 "An overview of…"——既不可检索，也让审稿人一开始就怀疑你的方法学严谨度。

---

## ABSTRACT

### 条目 2 · 摘要
> **See the PRISMA 2020 for Abstracts checklist.**

详见 [`04-abstract-checklist.md`](04-abstract-checklist.md)（12 条）。

---

## INTRODUCTION

### 条目 3 · 理由（Rationale）
> **Describe the rationale for the review in the context of existing knowledge.**
> 在已有知识的背景下描述做这篇综述的理由。

**怎么写**：
- 说明该问题为什么重要、当前证据为什么不确定。
- **必须说明已有综述的情况**：是否已有同题综述？若有，为什么还要再做一篇（已过时 / 范围不同 / 方法有缺陷 / 有新证据出现）。
- 若有理论模型或作用机制假设，在这里交代（这会决定后面的亚组分析）。

**合格判据**：能否用一句话回答"如果不做这篇综述，读者会缺什么"？

**常见错误**：
- 只罗列背景知识、不说明证据缺口 → 变成教科书式介绍。
- 不查已有综述就开工。**在正式检索之前必须先检索是否已有同题系统综述**（PROSPERO、Cochrane Library、Epistemonikos）。

### 条目 4 · 目标（Objectives）
> **Provide an explicit statement of the objective(s) or question(s) the review addresses.**
> 明确陈述本综述的目标或问题。

**怎么写**：用结构化框架表述，最常见的是 PICO：
- **P**opulation 研究对象
- **I**ntervention 干预
- **C**omparator 对照
- **O**utcome 结局
- （+ **S**tudy design / **T**ime frame / **S**etting）

PICO 不适用时改用其他框架，并**说明为什么改**：
- **SPIDER**（Sample, Phenomenon of Interest, Design, Evaluation, Research type）：质性研究
- **PEO**（Population, Exposure, Outcome）：病因学/流行病学
- **PICOTS / PICOS**：加入时间、场景、研究设计
- 方法学/技术类综述：需自定义并显式声明（见 `13`）

**合格判据**：问题里是否有**明确的自变量与因变量**？"What is the effectiveness of X in Y?" 可做；"What is known about X in Y?" 太宽，不可做。

**常见错误**：把目标写成"综述现有文献"——那不是问题，是活动描述。

---

## METHODS

### 条目 5 · 纳排标准（Eligibility criteria）
> **Specify the inclusion and exclusion criteria for the review and how studies were grouped for the syntheses.**
> 说明纳入与排除标准，以及研究如何被分组以进入各项综合。

**怎么写**（E&E 要点）：
- 按 PICO 各要素逐一给出标准，外加研究设计、场景、报告特征（年份、语言、发表状态）。
- **区分"未测量该结局"与"测量了但未报告结果"**——这是两种不同的排除理由，后者关系到报告偏倚。
- 说明**综合分组规则**：哪些干预/人群/结局会被合并到同一个 synthesis 里（这一条是 2020 年新加的重点）。
- 任何限制（年份、语言）必须给出科学理由。

**合格判据**：把标准交给另一个人，他能否独立复现你的纳入决定？

**常见错误**：
- 排除标准写成纳入标准的镜像否定（"纳入成人 / 排除儿童"）——冗余且暴露逻辑混乱。只保留那些**无法嵌入纳入标准的真正例外**。
- 没有科学理由的年份限制（"2015 年以后"）。若技术在某时点前不存在，写明这个理由。
- 检索之后才定标准（事后纳排 = 选择性纳入偏倚）。

### 条目 6 · 信息源（Information sources）
> **Specify all databases, registers, websites, organisations, reference lists and other sources searched or consulted to identify studies. Specify the date when each source was last searched or consulted.**
> 列出所有数据库、注册库、网站、机构、参考文献表及其他检索或查阅过的来源，并说明每个来源最后一次检索的日期。

**怎么写**：
- 逐个列出数据库名 **+ 平台/接口**（如 "MEDLINE (Ovid)"、"Embase (Elsevier)"、"CINAHL (EBSCOhost)"），因为同名数据库在不同平台上语法与覆盖不同。
- 给出每个来源的**覆盖年份**与**最后检索日期**（精确到日）。
- 包括：试验注册库、灰色文献、引文追溯（前向/后向）、手工翻查、向作者/机构索取数据。
- 任何日期限制在这里再次说明。

**合格判据**：一年后另一个团队能否用这份清单重跑一遍并得到可比的结果集？

**常见错误**：只写 "PubMed, Google Scholar were searched"。Google Scholar 索引会变、不可复现，可用于查漏补缺（scoping/hand-search），但不能作为主要来源单列。

### 条目 7 · 检索策略（Search strategy）
> **Present the full search strategies for all databases, registers and websites, including any filters and limits used.**
> 给出所有数据库、注册库和网站的完整检索策略，包括使用的过滤器与限制条件。

**怎么写**：
- **逐行复制粘贴实际运行的检索式**（不是概念描述），每个库一份，通常放补充材料。
- 说明每个限制（年份、语言、文献类型）并链接回纳排标准。
- 若使用已发表的检索过滤器（如 Cochrane RCT 高灵敏度过滤器），引用出处并说明是否修改。
- 报告检索式是如何开发的（预检索、MeSH/Emtree 查证、sentinel paper 召回测试）。
- 报告是否经过同行评议（**PRESS** 清单）。

详见 [`07-search-prisma-s.md`](07-search-prisma-s.md)。

**常见错误**：只给出关键词列表而非可执行检索式；同一 facet 内部误用 AND（漏检的首要原因）。

### 条目 8 · 筛选过程（Selection process）
> **Specify the methods used to decide whether a study met the inclusion criteria of the review, including how many reviewers screened each record and each report retrieved, whether they worked independently, and if applicable, details of automation tools used in the process.**
> 说明判定研究是否符合纳入标准的方法，包括每条记录与每份全文由几人筛选、是否独立进行，以及（如适用）所用自动化工具的细节。

**怎么写**：
- 标题/摘要阶段与全文阶段分别报告人数与是否独立。
- 分歧解决机制（讨论 / 第三人仲裁）。
- 一致性指标（如 Cohen's kappa）——非强制但推荐。
- **自动化工具**：软件名与版本、如何集成、训练方式、是否验证过其性能、是否用它直接排除记录。
- 若使用众包或已有的筛选数据集，说明其来源。

**合格判据**：单人筛选不是绝对禁止，但必须如实报告，并在局限性中承认随机误差风险（可通过抽样复核缓解）。

**常见错误**：用 AI/LLM 辅助筛选却不报告；"两位作者筛选"而不说明是否**独立**（两人分工筛一半 ≠ 双人独立筛选）。

### 条目 9 · 数据提取过程（Data collection process）
> **Specify the methods used to collect data from reports, including how many reviewers collected data from each report, whether they worked independently, any processes for obtaining or confirming data from study investigators, and if applicable, details of automation tools used in the process.**
> 说明从报告中提取数据的方法，包括每份报告由几人提取、是否独立、向研究者索取或核实数据的流程，以及（如适用）自动化工具细节。

**怎么写**：
- 提取表是否经过预试（pilot）；在几篇上试过、据此做了哪些修改。
- 是否双人独立提取、如何核对。
- 向原作者索要缺失数据的流程与应答情况。
- 从图中读数所用软件（如 WebPlotDigitizer）；翻译流程。
- **同一研究有多份报告时的取舍规则**（如以期刊版为准、会议版补充）。

**常见错误**：把"提取"当成一次性抄写，不做预试；不记录同一研究多版本的归并规则。

### 条目 10a · 数据条目 — 结局
> **List and define all outcomes for which data were sought. Specify whether all results that were compatible with each outcome domain in each study were sought (e.g. for all measures, time points, analyses), and if not, the methods used to decide which results to collect.**
> 列出并定义所有拟提取的结局。说明是否提取了每个结局领域下所有相容的结果（各种测量方式、时间点、分析方法）；若否，说明取舍方法。

**怎么写**：
- 定义结局**领域**（domain）与**测量方式**（measure）、时间点。
- 区分主要结局与次要结局，并说明优先级理由。
- 明确"一项研究报告了多个相容结果时如何选"：预设层级（如优先选 intention-to-treat、优先选最长随访）。
- 若结局定义在过程中变更，报告变更及其理由。

**为什么重要**：这是防止"挑最显著的那个结果"的核心条目。

### 条目 10b · 数据条目 — 其他变量
> **List and define all other variables for which data were sought (e.g. participant and intervention characteristics, funding sources). Describe any assumptions made about any missing or unclear information.**
> 列出并定义所有其他拟提取变量（如对象与干预特征、资助来源），并描述对缺失或含糊信息所作的假设。

**怎么写**：把提取表的字段全列出来；对"文中未说明时按什么处理"给出明确规则（例：未报告随机化方式一律记为 unclear，不推测）。建议把空白提取表存入公共仓库并在条目 27 中引用。

### 条目 11 · 纳入研究的偏倚风险评价
> **Specify the methods used to assess risk of bias in the included studies, including details of the tool(s) used, how many reviewers assessed each study and whether they worked independently, and if applicable, details of automation tools used in the process.**
> 说明评价纳入研究偏倚风险的方法，包括所用工具及其版本、每项研究由几人评价、是否独立，以及（如适用）自动化工具细节。

**怎么写**：
- 工具名 + 版本 + 所评领域清单（RoB 2 / ROBINS-I / QUADAS-2 / Newcastle-Ottawa…）。
- 是否做总体判断，以及总体判断的合成规则。
- 任何对工具的改编或自建工具必须说明。
- **关键概念区分**：评价的是"设计、实施、分析中可能使结果产生系统偏倚的特征"，不是笼统的"质量"。

详见 [`09-risk-of-bias.md`](09-risk-of-bias.md)。

**常见错误**：把偏倚风险评价做成打分总表；用报告规范（CONSORT/PRISMA）当评价工具。

### 条目 12 · 效应量（Effect measures）
> **Specify for each outcome the effect measure(s) (e.g. risk ratio, mean difference) used in the synthesis or presentation of results.**
> 说明每个结局在综合或呈现结果时所使用的效应量。

**怎么写**：
- 二分类结局 → RR / OR / RD；连续结局 → MD / SMD；时间事件 → HR。
- 说明选择理由（例：量表不同故用 SMD）。
- 给出**解释阈值**（最小重要差值 MID、效应量大小分级）。
- 若做过换算（如 OR→RR、SMD→原量表单位），说明方法。

### 条目 13a–13f · 综合方法（Synthesis methods）

> **13a** Describe the processes used to decide which studies were eligible for each synthesis（如何决定哪些研究进入每一项综合，例如把研究特征制表后与条目 5 的预设分组比对）。
> **13b** Describe any methods required to prepare the data for presentation or synthesis（数据准备：缺失统计量的处理、单位换算等）。
> **13c** Describe any methods used to tabulate or visually display results（制表与可视化方法）。
> **13d** Describe any methods used to synthesise results and provide a rationale for the choice(s). If meta-analysis was performed, describe the model(s), method(s) to identify the presence and extent of statistical heterogeneity, and software package(s) used（综合方法及理由；若做荟萃分析，说明模型、异质性识别方法、软件包）。
> **13e** Describe any methods used to explore possible causes of heterogeneity among study results（探索异质性来源的方法，如亚组分析、meta 回归）。
> **13f** Describe any sensitivity analyses conducted to assess robustness of the synthesised results（评估稳健性的敏感性分析）。

**怎么写**：见 [`08-synthesis-certainty.md`](08-synthesis-certainty.md)。要点：
- 固定效应 vs 随机效应的选择是**理论判断**，不能看异质性检验结果再定。
- 亚组分析必须**预先设定**并限制数量，说明每个亚组的假设机制。
- 不做荟萃分析时，13d 要写明替代综合方法，并按 **SWiM** 九条报告——不能只写 "narrative synthesis" 四个字。
- **vote counting（数有多少篇阳性）不是合格的综合方法**，除非明确用于回答"是否存在任何效应"这一极宽问题，且说明其不加权的局限。

### 条目 14 · 报告偏倚评价方法
> **Describe any methods used to assess risk of bias due to missing results in a synthesis (arising from reporting biases).**
> 说明评价"因结果缺失（报告偏倚）导致的偏倚风险"的方法。

**怎么写**：
- 漏斗图 + 非对称性检验（Egger / Begg），**通常要求 ≥10 项研究**才有意义。
- 选择性结局报告：比对 protocol/注册记录与发表结果（ORBIT 方法）。
- 可用 ROB-ME 等工具做系统判断。

### 条目 15 · 证据确信度评价方法
> **Describe any methods used to assess certainty (or confidence) in the body of evidence for an outcome.**
> 说明评价某一结局的证据体确信度的方法。

**怎么写**：通常用 **GRADE**：RCT 证据起始为 High，可因偏倚风险、不一致性、间接性、不精确性、发表偏倚降级；观察性证据起始为 Low，可因效应量大、剂量反应、残余混杂方向相反升级。质性证据用 **GRADE-CERQual**。说明由谁评、如何解决分歧、降级/升级决策如何记录。

详见 [`08-synthesis-certainty.md`](08-synthesis-certainty.md)。

---

## 方法部分自检（写完 5–15 条后过一遍）

- [ ] 5–15 条的每一条都在 protocol 里就写好了，不是事后补的
- [ ] 每个限制条件都有科学理由，不是习惯或方便
- [ ] 检索式是可执行的原文，不是概念描述
- [ ] 筛选/提取/偏倚评价三处都写清了"几人、是否独立、有无自动化工具"
- [ ] 结局定义里写明了"同一结局多个结果怎么选"
- [ ] 综合方法写明了模型选择理由，而不只是方法名
- [ ] 亚组与敏感性分析是预设的，且列出了具体清单
- [ ] 报告偏倚与确信度评价都有明确方法（哪怕结论是"研究数太少无法评估"）
