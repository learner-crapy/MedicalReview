# 05 · PRISMA 2020 流程图

流程图对应清单条目 **16a**，是系统综述最显眼的方法学证据：它必须让读者一眼看出"从多少条记录，经过哪些筛子，剩下多少项研究，为什么"。

## 5.1 四个官方模板

| 模板 | 适用 |
|---|---|
| 新综述 · 仅数据库与注册库 | 只检索了数据库/注册库 |
| 新综述 · 数据库 + 其他途径 | 另外做了引文追溯、网站、机构、专家联系等 |
| 更新综述 · 仅数据库与注册库 | 在既有综述基础上更新 |
| 更新综述 · 数据库 + 其他途径 | 同上，且有其他检索途径 |

下载：<https://www.prisma-statement.org/prisma-2020-flow-diagram>（CC BY 4.0）。也可用官方 Shiny App 或 R 包 **PRISMA2020** 自动生成。

## 5.2 三个术语必须分清

| 术语 | 含义 | 举例 |
|---|---|---|
| **Record**（记录） | 数据库返回的一条题录 | 同一篇论文在 PubMed 和 Embase 各是一条 record |
| **Report**（报告） | 一份具体文献（全文） | 期刊论文、预印本、会议论文、报告书 |
| **Study**（研究） | 一项研究本身 | 一项研究可能有 3 份 report（会议版、预印本、期刊版） |

**综述的分析单位是 study，不是 report。** 流程图末端要同时给出"纳入研究数"和"这些研究对应的报告数"。计算机领域尤其容易踩坑：arXiv 预印本 + 会议论文 + 期刊扩展版往往是同一项研究。

## 5.3 各框的计数规则（新综述 · 含其他途径）

```
┌─ IDENTIFICATION ────────────────────────────────────────────┐
│ 左栏（数据库/注册库）             右栏（其他途径）          │
│ Records identified from:          Records identified from:  │
│   Database 1 (n=)                   Websites (n=)           │
│   Database 2 (n=)                   Organisations (n=)      │
│   Registers (n=)                    Citation searching (n=) │
│                                                             │
│ Records removed before screening:                           │
│   Duplicate records removed (n=)                            │
│   Records marked ineligible by automation tools (n=)        │
│   Records removed for other reasons (n=)                    │
└─────────────────────────────────────────────────────────────┘
┌─ SCREENING ─────────────────────────────────────────────────┐
│ Records screened (n=)        → Records excluded (n=)        │
│ Reports sought for retrieval → Reports not retrieved (n=)   │
│ Reports assessed for         → Reports excluded (n=)        │
│   eligibility (n=)              **按理由分类计数**          │
└─────────────────────────────────────────────────────────────┘
┌─ INCLUDED ──────────────────────────────────────────────────┐
│ Studies included in review (n=)                             │
│ Reports of included studies (n=)                            │
└─────────────────────────────────────────────────────────────┘
```

逐框说明：

1. **Records identified from…**：按来源分别给数，**不去重**。右栏的其他途径要分类列（网站、机构、引文追溯、作者联系）。
2. **Records removed before screening**：拆成三类——去重、被自动化工具标记为不合格、其他原因移除。自动化工具排除必须单列（2020 新增要求）。
3. **Records screened → Records excluded**：题录筛选阶段。此阶段排除**不要求**列理由。
4. **Reports sought for retrieval → Reports not retrieved**：找全文的阶段。找不到全文的数量必须写出来（这是潜在的选择偏倚来源）。
5. **Reports assessed for eligibility → Reports excluded**：全文筛选阶段。**必须按理由分类给出数量**，如"Reason 1: 非医学问答任务 (n=14)"。这一框与条目 16b 配套。
6. **Studies included / Reports of included studies**：研究数与报告数分开给。

更新综述的模板会在 INCLUDED 区额外加一行：**Studies included in previous version of review (n=)** 与 **Reports of studies included in previous version (n=)**，并把本轮新纳入的研究单列。

## 5.4 数字对不上的常见原因

| 症状 | 原因 |
|---|---|
| 去重前后差值与实际不符 | 自动去重后又做了人工去重，但只记了一次 |
| screened 数 ≠ identified − removed | 中途补检索没有并入图中 |
| 全文排除理由的分项和 ≠ 排除总数 | 一篇文献被记了多个排除理由（**每篇只记一个主要理由**） |
| 纳入研究数 ≠ 特征表行数 | 多报告同一研究未合并，或合并了但表里又分开列 |
| 其他途径找到的研究混进左栏 | 右栏必须独立追踪到底 |

## 5.5 实操建议

- **从第一天就建计数表**，不要等写作时回忆。建议表头：
  `stage | source | n_in | n_out | reason | date | screener | note`
- 用 Zotero/EndNote 做初次去重后，**保留一份未去重的原始导出**，以便核对。
- 全文排除理由建议预设 5–8 个类别并编号，筛选时只填编号，避免自由文本导致无法汇总。
- 流程图生成后，用一次"加减法自检"：每一层的 in − out 必须等于下一层的 in。
- 图中所有数字都要能在补充材料的筛选记录里查到。

## 参考

- PRISMA 2020 流程图模板与说明：<https://www.prisma-statement.org/prisma-2020-flow-diagram>
- Haddaway NR, et al. PRISMA2020: An R package and Shiny app for producing PRISMA 2020-compliant flow diagrams.
