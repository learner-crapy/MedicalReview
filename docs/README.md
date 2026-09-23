# PRISMA 2020 系统综述规则与方法文档

本目录系统整理 **PRISMA 2020**（Preferred Reporting Items for Systematic Reviews and Meta-Analyses）的完整规则、每个条目的实操写法，以及一篇系统综述从选题到发表的全流程方法。

面向对象：本项目（LLM 多代理系统在医学问答中的系统综述）的作者，但内容本身是通用的。

## 阅读顺序

| 文件 | 内容 | 什么时候读 |
|---|---|---|
| [01-overview.md](01-overview.md) | PRISMA 是什么/不是什么、三篇论文套件、2009→2020 的 11 项变化、适用边界 | 开始前 |
| [02-checklist-methods.md](02-checklist-methods.md) | 清单第 1–15 条（标题/摘要/引言/方法）逐条详解 | 写 protocol 时 |
| [03-checklist-results-discussion.md](03-checklist-results-discussion.md) | 清单第 16–27 条（结果/讨论/其他信息）逐条详解 | 写正文时 |
| [04-abstract-checklist.md](04-abstract-checklist.md) | 摘要 12 条清单 | 写摘要时 |
| [05-flow-diagram.md](05-flow-diagram.md) | 流程图四个模板、每个框的计数规则、record/report/study 之别 | 筛选开始前 |
| [06-protocol-prisma-p.md](06-protocol-prisma-p.md) | PRISMA-P 17 条、PROSPERO/OSF 注册、protocol 修订记录 | 检索开始前 |
| [07-search-prisma-s.md](07-search-prisma-s.md) | PRISMA-S 16 条、分面检索式构建、PRESS 同行评议、去重 | 建检索式时 |
| [08-synthesis-certainty.md](08-synthesis-certainty.md) | meta-analysis / SWiM 9 条 / 异质性 / 敏感性分析 / GRADE | 综合阶段 |
| [09-risk-of-bias.md](09-risk-of-bias.md) | 偏倚风险 vs 质量、工具选择、如何把评价结果用进综合 | 提取阶段 |
| [10-extensions.md](10-extensions.md) | 全部 PRISMA 扩展一览 + 何时用哪个 | 确定综述类型时 |
| [11-workflow.md](11-workflow.md) | 端到端 15 步流程，每步产出物与门禁 | 排计划时 |
| [12-pitfalls.md](12-pitfalls.md) | 常见错误清单：症状 → 违反条目 → 正确做法 | 自查时 |
| [13-applying-to-this-project.md](13-applying-to-this-project.md) | 27 条在"多代理 × 医学问答"综述中的改编方式 | 本项目专用 |

## 三条不能忘的前提

1. **PRISMA 是报告规范，不是实施规范。** 它规定"写出来要包含什么"，不规定"怎么做"。实施方法请看 Cochrane Handbook / JBI Manual，本目录的 `08`、`09`、`11` 补上了这部分。
2. **PRISMA 不是质量评价工具。** 不能用"符合 PRISMA 多少条"来判断一篇综述质量高低——那是 AMSTAR 2 和 ROBIS 的工作（见 `09`）。
3. **报告条目要在做之前就决定。** 清单里几乎所有方法学条目（5–15）都必须在检索之前写进 protocol，事后补写即构成选择性报告偏倚。

## 主要依据

- Page MJ, McKenzie JE, Bossuyt PM, et al. **The PRISMA 2020 statement: an updated guideline for reporting systematic reviews.** *BMJ* 2021;372:n71. doi:10.1136/bmj.n71
- Page MJ, Moher D, Bossuyt PM, et al. **PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews.** *BMJ* 2021;372:n160. doi:10.1136/bmj.n160
- Moher D, Shamseer L, Clarke M, et al. **PRISMA-P 2015 statement.** *Syst Rev* 2015;4:1.
- Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. **PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews.** *Syst Rev* 2021;10:39.
- Campbell M, McKenzie JE, Sowden A, et al. **Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline.** *BMJ* 2020;368:l6890.
- PRISMA 官方网站：<https://www.prisma-statement.org/>
- 教材参考：Purssell E, McCrae N. *How to Perform a Systematic Literature Review*（本机蒸馏稿见 `~/.claude/skills/review/distilled/`）

PRISMA 清单与流程图以 CC BY 4.0 发布；本文档中的条目译文与解读为在该许可下的改写，原文引用均标注出处。
