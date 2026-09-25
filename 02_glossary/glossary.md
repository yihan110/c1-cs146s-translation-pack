# 课程翻译术语表（Glossary）

> 用途：统一全文译法，避免"同一个英文词翻成不同中文"。译文必须全文遵守本表。
> 规则：
> 1. 译法栏为统一译法；「保留英文」表示正文直接保留英文原词（技术规范/产品名）。
> 2. 首次出现可"中英并列"（如：大语言模型（LLM）），后续统一用中文（或表内指定方式）。
> 3. 代码标识符、命令、函数名永不翻译。

## 一、核心译法决策（请你重点确认 ✅）

| # | 英文 | 建议译法 | 理由 / 说明 |
|---|---|---|---|
| D1 | **Vibe Coding** | **保留英文「Vibe Coding」，首次加注「（氛围编程）」** | 领域流行词，直译易失真；官方无统一译法 |
| D2 | **Agent / Coding Agent** | **智能体 / 编码智能体** | 相比"代理/代理式"，"智能体"更贴近当下中文技术社区用法 |
| D3 | **Agentic AI / agentic workflows** | **智能体驱动型 AI / 智能体驱动工作流** | "agentic"统一译"智能体驱动"，避免"代理式/自动式"混用 |
| D4 | **Scaffolding** | **脚手架** | 编程语境标准译法 |
| D5 | **Context Engineering** | **上下文工程（Context Engineering）** | 保留英文括号，属新兴专名 |
| D6 | **Context window / Context rot** | **上下文窗口 / 上下文腐化** | "rot"译"腐化"比"衰减/腐坏"更贴切 |
| D7 | **MCP (Model Context Protocol)** | **模型上下文协议（MCP）** | 保留缩写 MCP（课程高频使用） |
| D8 | **Prompt Engineering** | **提示词工程（Prompt Engineering）** | "提示词"比"提示工程/提示工程学"通用 |

## 二、LLM 与模型（Modeling）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 1 | Large Language Model (LLM) | 大语言模型（LLM） | 保留缩写 |
| 2 | Foundation model | 基础模型 | |
| 3 | Parameter | 参数 | |
| 4 | Token | 词元（token） | 文本单位；技术语境可保留英文 |
| 5 | Fine-tuning | 微调 | |
| 6 | Zero-shot / Few-shot | 零样本 / 少样本 | |
| 7 | Chain-of-thought | 思维链 | |
| 8 | Hallucination | 幻觉 | |
| 9 | Guardrail | 护栏 | |
| 10 | RAG (Retrieval-Augmented Generation) | 检索增强生成（RAG） | 保留缩写 |
| 11 | Embedding | 嵌入（embedding） | |
| 12 | API | 应用程序接口（API） | 保留缩写 |
| 13 | SDK | 软件开发工具包（SDK） | 保留缩写 |

## 三、提示工程（Prompting）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 14 | System prompt | 系统提示词 | |
| 15 | User prompt | 用户提示词 | |
| 16 | Instruction | 指令 | |
| 17 | Output format | 输出格式 | |
| 18 | Structured output | 结构化输出 | |
| 19 | Constraint | 约束条件 | |

## 四、智能体与工具（Agents & Tools）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 20 | Coding agent | 编码智能体 | |
| 21 | Autonomous agent | 自主智能体 | |
| 22 | Multi-agent system | 多智能体系统 | |
| 23 | Tool use / Tool calling | 工具使用 / 工具调用 | |
| 24 | Function calling | 函数调用 | |
| 25 | Tool definition | 工具定义 | |
| 26 | Workflow | 工作流 | |
| 27 | Orchestration | 编排 | |
| 28 | Plan / Plan-and-execute | 计划 / 计划-执行 | |

## 五、MCP（模型上下文协议）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 29 | MCP server / client | MCP 服务器 / 客户端 | 保留 MCP |
| 30 | Host | 宿主 | |
| 31 | Resource | 资源 | |
| 32 | Prompt template | 提示词模板 | |
| 33 | Registry | 注册表（registry） | 专名可保留英文 |
| 34 | Authentication / Authorization | 认证 / 授权 | |
| 35 | OAuth | OAuth | 保留英文 |
| 36 | Transport | 传输层 | |

## 六、上下文与工程（Context & Dev）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 37 | Context window | 上下文窗口 | |
| 38 | Context rot | 上下文腐化 | |
| 39 | Context engineering | 上下文工程（Context Engineering） | |
| 40 | IDE | 集成开发环境（IDE） | 保留缩写 |
| 41 | CLI / Terminal | 命令行界面 / 终端 | |
| 42 | PRD | 产品需求文档（PRD） | 保留缩写 |
| 43 | Spec / Specs | 规格说明 | |
| 44 | Repository (repo) | 代码仓库（仓库） | |
| 45 | Commit / PR (Pull Request) | 提交 / 合并请求（Pull Request） | PR 保留英文 |

## 七、代码评审（Code Review）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 46 | Code review | 代码评审 | |
| 47 | Reviewer | 评审人 | |
| 48 | Author | 作者（提交者） | |
| 49 | Nit | 小问题（nit） | 口语化，可保留 |
| 50 | LGTM | LGTM（Looks Good To Me 我看没问题） | 保留英文 |
| 51 | Diff / Patch | 变更 / 补丁 | |
| 52 | Static analysis | 静态分析 | |

## 八、安全（Security）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 53 | Prompt injection | 提示注入 | |
| 54 | Remote code execution (RCE) | 远程代码执行（RCE） | |
| 55 | SAST / DAST | 静态应用安全测试 / 动态应用安全测试 | |
| 56 | OWASP Top Ten | OWASP Top 10（OWASP 十大） | 保留英文 |
| 57 | Vulnerability | 漏洞 | |
| 58 | Threat model | 威胁模型 | |
| 59 | Sandbox | 沙箱 | |
| 60 | CVE | CVE（通用漏洞披露编号） | 保留英文 |

## 九、SRE 与可观测性（SRE & Observability）

| # | 英文 | 译法 | 说明 |
|---|---|---|---|
| 61 | Site Reliability Engineering (SRE) | 站点可靠性工程（SRE） | 保留缩写 |
| 62 | Observability | 可观测性 | |
| 63 | Telemetry | 遥测 | |
| 64 | Trace / Span | 追踪 / 跨度 | |
| 65 | Metrics | 指标 | |
| 66 | Logs | 日志 | |
| 67 | On-call | 值班 | |
| 68 | Incident | 事故 | |
| 69 | Service Level Objective (SLO) | 服务等级目标（SLO） | 保留缩写 |
| 70 | Kubernetes | Kubernetes | 保留英文 |
| 71 | Container | 容器 | |

## 十、产品与平台名（保留英文）

| # | 英文 | 处理 | 说明 |
|---|---|---|---|
| 72 | Claude Code | 保留英文 | 产品名 |
| 73 | OpenAI Codex / ChatGPT | 保留英文 | 产品名 |
| 74 | Warp | 保留英文 | 产品名 |
| 75 | GitHub / GitLab | 保留英文 | 平台名 |
| 76 | Cursor / Windsurf | 保留英文 | IDE 产品名 |
| 77 | Anthropic | 保留英文 | 公司名 |
| 78 | Vercel | 保留英文 | 平台名 |
| 79 | Semgrep / Graphite | 保留英文 | 工具名 |

---
**统计**：核心决策 8 条 + 常规术语 63 条 + 产品名 8 条，共 **79 条**（≥50 达标）。
**校对状态**：✅ **已定稿（2026-09-25）** —— 选法标准：术语全文统一 + 准确无硬伤 + 读者可读性。Agent→智能体、Prompt Engineering→提示词工程，专名/产品名保留英文。
