# OpenAI 如何用 Codex（How OpenAI uses Codex）

> 来源：OpenAI 官方文档（research preview 报告），课程 Week 10 阅读（PDF）

## 引言
Codex 每天被 OpenAI 众多技术团队使用，如安全、产品工程、前端、API、基础设施和性能工程。团队用它加速一系列工程任务——从理解复杂系统、重构大型代码库，到在紧迫期限内发布新特性和解决事件。基于对 OpenAI 工程师的访谈和内部使用数据，我们整理了展示 Codex 如何帮团队提速、提升工作质量、规模化驾驭复杂性的用例和最佳实践。

## 用例 1：代码理解（Code understanding）
Codex 帮团队在入职、调试或调查事件时快速上手不熟悉的代码库区域。他们常用 Codex 定位某个特性的核心逻辑、梳理服务或模块间的关系、追踪数据在系统中的流动。它还能浮现架构模式、或缺失的文档——否则这些需大量人工才能生成。事件响应时，Codex 通过浮现组件间交互、或追踪故障状态如何在系统中传播，帮工程师快速进入新领域。

*团队感言*："修 bug 时，我用 Ask 模式看代码库别处是否也可能出现同一问题。"（检索系统性能工程师）；"值班时，我粘贴堆栈追踪并问 Codex 认证流程在哪。它直接跳到正确的文件，让我快速分流。"（API 平台 SRE）；"Codex 回答我在 Terraform 和 Python 里'这该在哪做？'的仓库问题，比 grep 快多了。"（基础设施服务 DevOps 工程师）

*示例提示词*（保留英文）：Where is the authentication logic implemented in this repo? / Summarize how requests flow through this service from entrypoint to response. / Which modules interact with [module name] and how are failures handled?

## 用例 2：重构与迁移（Refactoring and migrations）
Codex 常用于做出跨多文件或包的变化。例如工程师更新 API、改变某模式的实现方式、或迁移到新依赖时，Codex 让一致地应用变更变得容易。当同一更新需在几十个文件上做、或更新需对"正则或查找替换不易捕获的结构和依赖"有感知时，它尤其有用。团队也用它在重构上：拆分超大模块、用现代模式替换旧模式、或为更好可测试性做准备。

*团队感言*："Codex 把我们每个遗留的 getUserById() 换成了新服务模式并开了 PR。几分钟做完本来要几小时的事。"（ChatGPT Web 后端工程师）；"为清发布阻塞，我让 Codex 扫描旧模式的每个实例、在 Markdown 里总结影响、然后开带修复的 PR。"（ChatGPT Enterprise 产品工程师）

*示例提示词*：Split this file into separate modules by concern and generate tests for each one. / Convert all callback-based database access to async/await.

## 用例 3：性能优化（Performance optimization）
Codex 被用于识别和解决性能瓶颈。调优或可靠性工作期间，工程师提示 Codex 分析慢或内存密集的代码路径（如低效循环、冗余操作、昂贵查询），并建议优化替代方案，常带来效率和可靠性方面的显著提升。Codex 也用于支持代码健康——识别仍在活跃使用但高风险或已废弃的模式。团队依赖它减少长期技术债、主动防止回归。

*团队感言*："我用 Codex 扫描重复的昂贵 DB 调用。它很擅长标记热路径、起草我之后可调优的批量查询。"（API 可靠性基础设施工程师）；"Codex 很擅长快速发现性能问题——花 5 分钟写提示词，省下 30 分钟工作。"（模型服务平台工程师）

*示例提示词*：Optimize this loop for memory efficiency and explain why your version is faster. / Find repeated expensive operations in this request handler and suggest caching opportunities. / Suggest a faster way to batch DB queries in this function.

## 用例 4：提升测试覆盖率（Improving test coverage）
Codex 帮工程师更快写测试——尤其在覆盖率薄弱或完全缺失的地方。做 bug 修复或重构时，工程师常请 Codex 建议覆盖边缘情况或可能失败路径的测试。对新代码，它可根据函数签名和周围逻辑生成单元或集成测试。Codex 特别擅长识别边界条件，如空输入、最大长度、或不寻常但有效的状态——这些常被初始测试遗漏。

*团队感言*："我夜里把 Codex 指向低覆盖模块，醒来就有可运行的单元测试 PR。"（ChatGPT Desktop 前端工程师）；"切换 monorepo 分支很痛苦时，我让 Codex 写测试并启动 CI，我继续在自己的分支上工作。"（支付与计费后端工程师）

*示例提示词*：Write unit tests for this function, including edge cases and failure paths. / Generate a property-based test for this sorting utility. / Extend this test file to cover missing scenarios around null inputs and invalid states.

## 用例 5：提升开发速度（Increasing development velocity）
Codex 通过加速开发周期的起点和终点帮团队更快推进。启动新特性时，工程师用它搭建样板——生成文件夹、模块和 API 桩，快速得到可运行代码而无需手接每部分。项目临近发布时，Codex 通过处理较小但关键的杂务帮团队赶上紧迫期限，如分流 bug、填补最后的实现缺口、生成发布脚本、遥测钩子或配置文件。它也被用来把产品反馈转成起始代码——工程师常粘贴用户请求或规格，让 Codex 生成可回头精炼的草稿。

*团队感言*："我整天开会，仍合了 4 个 PR，因为 Codex 在后台工作。"（ChatGPT Enterprise 产品工程师）；"Codex 完美交付了 3-4 个本会烂在积压清单里的低优先级修复，非常有成就感。"（内部工具全栈工程师）

*示例提示词*：Scaffold a new API route for POST /events with basic validation and logging. / Generate a telemetry hook for tracking success/failure of the new onboarding flow, using this template [insert example of your telemetry code]. / Create a stub implementation based on this spec: [insert spec or product feedback].

## 用例 6：保持心流（Staying in flow）
Codex 帮工程师在日程碎片化、充满中断时保持高效。它被用来捕捉未完成工作、把笔记转成可用原型、或衍生出可稍后再看的探索性任务。这让暂停和恢复工作更容易而不丢失上下文，尤其值班或会议多时。

*团队感言*："发现顺手修（drive-by fix）时，我启动一个 Codex 任务而不是切换分支，空闲时审它的 PR。"（ChatGPT API 后端工程师）；"我常把 Slack 线程、Datadog trace、issue 等转发给 Codex，以便专注在高优先级工作上。"（基础设施可观测 API 工程师）

*示例提示词*：Generate a plan to refactor this service and split it into smaller modules. / Stub out the retry logic and add a TODO — I'll fill in the backoff logic later. / Summarize this file so I can pick up where I left off tomorrow.

## 用例 7：探索与构思（Exploration and ideation）
Codex 也适用于开放式工作，如寻找替代方案或验证设计决策。你可以提示不同的解题方式、探索陌生模式、或压力测试假设。这帮助浮现权衡、扩展设计选项、磨锐实现选择。它也被用来识别相关 bug——给定已知问题或废弃方法，Codex 能识别代码别处的相似模式，更易捕获回归或完成清理。

*团队感言*："Codex 帮我解决冷启动问题——粘贴规格和文档，它就搭好代码或告诉我漏了什么。"（ChatGPT Desktop 产品工程师）；"修完一个 bug 后我请 Codex 指出相似 bug 可能潜伏的地方，然后衍生后续任务。"（检索系统性能工程师）

*示例提示词*：How would this work if the system were event-driven instead of request/response? / Find all modules that manually build SQL strings instead of using our query builder. / Rewrite this in a more functional style, avoid mutation and side effects.

## 最佳实践
Codex 在"被给予结构、上下文和迭代空间"时表现最佳。以下是 OpenAI 团队培养的习惯，以在日常工作中获得一致价值：
- **从 Ask 模式开始**：对大的变更，先用 Ask 模式请 Codex 给实现计划，该计划随后成为切到 Code 模式时后续提示词的输入。这种两步流程让 Codex 保持落地，帮助避免输出错误。Codex 最适合范围良好的任务——那些你或队友约一小时能完成、或几百行代码能实现的任务。随模型改进，预计它能承担的任务规模会增大。
- **迭代改进 Codex 的开发环境**：设置启动脚本、环境变量和网络访问能显著降低 Codex 的错误率。运行任务时，寻找可在 Codex 环境配置中纠正的构建错误。这可能要几次迭代，但长期带来显著效率收益。
- **像写 GitHub Issue 一样组织提示词**：当提示词镜像你会在 PR 或 issue 中描述变更的方式时，Codex 响应更好。即包含文件路径、组件名、diff 和文档片段。用"像 [模块 X] 那样实现这个"这类模式能改善结果。
- **把 Codex 任务队列当轻量积压清单**：启动任务来捕捉边缘想法、部分工作或偶然修复。没有一次性生成完整 PR 的压力。Codex 很适合作为聚焦回来时可返回的暂存区。
- **用 AGENTS.md 提供持久上下文**：维护 AGENTS.md 文件，帮 Codex 跨提示词在你的仓库里更有效运作。这些文件通常包含命名约定、业务逻辑、已知怪癖或 Codex 无法仅从代码推断的依赖。
- **善用"Best of N"提升输出**：Best-of-N 特性让你能同时为单个任务生成多个响应，快速探索多种方案并选最佳。对更复杂的任务，可审阅几次迭代并组合不同响应的部分，得到更强结果。

## 展望
Codex 仍处于研究预览，但它已在改变我们的构建方式——帮我们更快、写更好的代码、承担否则永远不会被优先化的活。我们对其潜力感到兴奋——随模型变好、Codex 更深集成进工作流，我们期待用它解锁更强大的软件开发方式。

---

> **翻译说明**：本文为 OpenAI Codex 内部实践报告，示例 prompt 与代码按约定保留英文原文；封面、目录、页眉页脚已省略。术语按表统一（Codex→Codex、Ask/Code Mode→Ask/Code 模式、best practices→最佳实践、on-call→值班、monorepo→monorepo）。
