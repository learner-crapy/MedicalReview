# 10 · PRISMA 扩展与相关规范

## 10.1 官方 PRISMA 扩展一览

来源：<https://www.prisma-statement.org/extensions>

| 扩展 | 用途 |
|---|---|
| **PRISMA-Abstracts** | 系统综述摘要的报告（已并入 PRISMA 2020 主声明，见 `04`） |
| **PRISMA-P**（Protocols） | 系统综述 **protocol** 的报告，17 条（见 `06`） |
| **PRISMA-S**（Search） | 文献检索的报告，16 条（见 `07`） |
| **PRISMA-ScR**（Scoping Reviews） | 范围综述 |
| **PRISMA-NMA**（Network Meta-Analyses） | 网状荟萃分析 |
| **PRISMA-IPD**（Individual Participant Data） | 个体参与者数据综述 |
| **PRISMA-DTA**（Diagnostic Test Accuracy） | 诊断准确性研究综述 |
| **PRISMA-Harms** | 以不良反应/危害为结局的综述 |
| **PRISMA-Equity** | 关注健康公平性的综述 |
| **PRISMA-CI**（Complex Interventions） | 复杂干预综述 |
| **PRISMA-COSMIN** | 结局测量工具的综述 |
| **PRISMA-Children and Adolescents** | 儿童与青少年人群 |
| **PRISMA-Living Systematic Reviews** | 持续更新的"活综述" |
| **PRISMA-EcoEvo** | 生态与进化科学领域 |
| **PRISMA-Acupuncture** | 针灸干预 |
| **PRISMA-Chinese Herbal Medicines** | 中草药干预 |
| **PRISMA-Moxibustion** | 艾灸干预 |

## 10.2 怎么选

```
你的综述是……
├─ 评价干预效果、有明确 PICO
│   └─ PRISMA 2020（主清单）
├─ 只想摸清"这个领域有哪些研究、用了什么方法"
│   └─ PRISMA-ScR（范围综述）——不做效应合并、通常不做偏倚评价
├─ 同时比较 3 个以上干预
│   └─ PRISMA 2020 + PRISMA-NMA
├─ 关注诊断准确性（敏感度/特异度）
│   └─ PRISMA-DTA + QUADAS-2
├─ 拿到了各研究的个体数据
│   └─ PRISMA-IPD
├─ 计划持续更新
│   └─ PRISMA 2020 + PRISMA-Living SR
└─ 方法学/技术类综述（无对应扩展）
    └─ PRISMA 2020 主清单 + 显式声明改编方式（见 `13`）
```

**系统综述 vs 范围综述的分界**：能否提出一个带明确比较的、可回答的问题。能 → 系统综述；只能描述"有什么" → 范围综述。两者都可以严谨，但不要用系统综述的外壳装范围综述的内容（或反之）。

## 10.3 与 PRISMA 配套的其他规范

| 规范 | 管什么 | 何时用 |
|---|---|---|
| **SWiM** | 不做荟萃分析时的综合报告，9 条 | 无法合并效应量时（见 `08`） |
| **GRADE / CERQual** | 证据体确信度 | 条目 15、22 |
| **PRESS** | 电子检索策略的同行评议 | 检索式定稿前（见 `07`） |
| **AMSTAR 2 / ROBIS** | 评价已发表综述的质量/偏倚风险 | 自查、或综述之综述 |
| **MECIR** | Cochrane 综述的实施与报告标准 | 做 Cochrane 综述时 |
| **ENTREQ** | 质性研究综合的报告，21 条 | metasynthesis |
| **EQUATOR Network** | 所有报告规范的总目录 | 找不到对应规范时先查这里 |

## 10.4 实施手册（PRISMA 不覆盖的部分）

- **Cochrane Handbook for Systematic Reviews of Interventions**（在线免费）：干预类综述的权威实施手册。
- **JBI Manual for Evidence Synthesis**（在线免费）：覆盖面更广，含质性、混合方法、文本与意见类证据。
- **CRD Guidance**（约克大学 Centre for Reviews and Dissemination）：讨论部分结构的经典来源。

## 10.5 注册与报告的对照速查

| 阶段 | 用什么规范 | 产出 |
|---|---|---|
| 写 protocol | PRISMA-P 17 条 | protocol 文档 |
| 注册 | PROSPERO / OSF | 注册号 / DOI |
| 建检索式 | PRISMA-S + PRESS | 逐库检索式 + 同行评议记录 |
| 筛选 | PRISMA 2020 条目 8、16a | 筛选记录 + 流程图计数表 |
| 提取 | 条目 9、10a、10b | 提取表 + 数据文件 |
| 偏倚评价 | 条目 11、18 | 逐领域判断表 |
| 综合 | 条目 13a–f、20a–d / SWiM | 森林图或综合表 |
| 确信度 | GRADE | SoF 表 |
| 报告 | PRISMA 2020 27 条 + 摘要 12 条 | 正文 + 已填写的清单 |
| 开放材料 | 条目 27 | OSF/Zenodo 仓库 |
