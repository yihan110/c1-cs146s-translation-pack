# Claude Code 最佳实践（Claude Code Best Practices）

> 来源：Anthropic 官方文档 — Claude Code best practices（课程 Week 4 阅读）

Claude Code 是一款 AI 驱动的编码助手，帮你开发功能、修复缺陷并自动化开发任务。它理解你的整个代码库，能跨多个文件和工具协作完成任务。

## 开始使用

选择你的环境即可开始。大多数使用界面需要 Claude 订阅或 Anthropic Console 账号。终端 CLI 和 VS Code 还支持第三方模型提供商。

- **终端（Terminal）**：功能完整的 CLI，直接在终端中使用 Claude Code——编辑文件、运行命令、从命令行管理整个项目。
- **VS Code**：提供内联 diff、@-提及、计划评审和会话历史。
- **桌面应用（Desktop app）**：在 IDE 或终端之外独立运行的 App，可可视化评审 diff、并排运行多个会话、安排周期任务、发起云端会话。
- **网页（Web）**：无需本地配置即可在浏览器中运行，可发起长时任务稍后查看结果。
- **JetBrains**：支持 IntelliJ IDEA、PyCharm、WebStorm 等 IDE 的插件。

### 安装

安装 Claude Code 可使用以下任一方式：

```bash
# 原生安装（推荐），macOS/Linux/WSL：
curl -fsSL https://claude.ai/install.sh | bash
# Windows PowerShell：
irm https://claude.ai/install.ps1 | iex
# Windows CMD：
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

# Homebrew（macOS）：
brew install --cask claude-code
# WinGet（Windows）：
winget install Anthropic.ClaudeCode
```

> 提示：若提示 `The token '&&' is not a valid statement separator`，说明你在 PowerShell 而非 CMD，应改用上方的 PowerShell 命令。Windows 需要先安装 Git for Windows。原生安装会在后台自动更新；Homebrew / WinGet 安装不会自动更新，需定期 `brew upgrade claude-code` / `winget upgrade Anthropic.ClaudeCode`。

在任意项目目录启动：

```bash
cd your-project
claude
```

首次使用会提示登录，然后即可开始。

## 你能用它做什么

以下是 Claude Code 的典型用法：

**自动化你一直拖延的琐事**——为无测试代码写测试、修复项目内的 lint 错误、解决合并冲突、更新依赖、编写发布说明：

```bash
claude "write tests for the auth module, run them, and fix any failures"
```

**开发功能与修复缺陷**——用自然语言描述你想要什么，Claude Code 规划方案、跨多文件写代码并验证可用。对缺陷，粘贴错误信息或描述症状，它会沿代码库追踪问题、定位根因并实施修复。

**创建提交与合并请求**——Claude Code 直接与 git 协作：暂存变更、写提交信息、建分支、发起 pull request：

```bash
claude "commit my changes with a descriptive message"
```

在 CI 中，可通过 GitHub Actions 或 GitLab CI/CD 自动化代码评审和问题分诊。

**用 MCP 连接你的工具**——模型上下文协议（MCP）是把 AI 工具接到外部数据源的开放标准。有了 MCP，Claude Code 能读取你 Google Drive 里的设计文档、更新 Jira 工单、从 Slack 拉取数据，或使用你自己的自定义工具。

**用指令、技能和钩子定制**——`CLAUDE.md` 是放在项目根目录的 Markdown 文件，Claude Code 在每次会话开始时读取。用它设定编码规范、架构决策、偏好的库和评审清单。Claude 也会在工作时构建自动记忆，跨会话保存构建命令、调试心得等经验，无需你额外书写。你可以创建自定义命令（如 `/review-pr`、`/deploy-staging`）来封装团队可共享的可复用工作流。钩子（Hooks）让你在 Claude Code 动作前后运行 shell 命令，例如每次编辑后自动格式化，或提交前运行 lint。

**运行智能体团队与构建自定义智能体**——同时派生多个 Claude Code 智能体处理任务的不同部分，由主导智能体协调工作、分配子任务、合并结果。对完全自定义的工作流，Agent SDK 让你构建自己的智能体，复用 Claude Code 的工具与能力，并完全掌控编排、工具访问和权限。

**用 CLI 组合、脚本化与自动化**——Claude Code 可组合，遵循 Unix 哲学：把日志管道给它、在 CI 中运行、或与其他工具串联：

```bash
# 分析最近日志
tail -200 app.log | claude -p "Slack me if you see any anomalies"
# 在 CI 中自动化翻译
claude -p "translate new strings into French and raise a PR for review"
# 跨文件批量操作
git diff main --name-only | claude -p "review these changed files for security issues"
```

**安排周期任务**——让 Claude 按计划运行，自动化重复工作：晨间 PR 评审、夜间 CI 失败分析、每周依赖审计、PR 合并后同步文档等。云端周期任务运行在 Anthropic 托管的基础设施上，即使电脑关机也继续执行；桌面周期任务运行在你的机器上，可直接访问本地文件和工具；`/loop` 在 CLI 会话内重复某提示词，适合快速轮询。

**随处工作**——会话不绑定单一界面，可随上下文变化在不同环境间迁移：离开工位用手机或浏览器继续（Remote Control）；从手机发起任务并打开桌面会话；在网页或 iOS 应用发起长时任务后用 `claude --teleport` 拉回终端；用 `/desktop` 把终端会话交到桌面应用做可视化 diff 评审；在团队聊天中 @Claude 汇报 bug，直接得到一个 pull request。

## 处处使用 Claude Code

所有界面都连接到同一个底层 Claude Code 引擎，因此你的 `CLAUDE.md` 文件、设置和 MCP 服务器在所有界面通用。除终端、VS Code、JetBrains、桌面和网页外，Claude Code 还集成 CI/CD、聊天和浏览器工作流：

| 我想要…… | 最佳方案 |
|---|---|
| 从手机或其他设备继续本地会话 | Remote Control |
| 把 Telegram、Discord、iMessage 或自定义 webhook 事件推入会话 | Channels |
| 本地发起任务、移动端继续 | Web 或 Claude iOS 应用 |
| 按周期运行 Claude | 云端周期任务或桌面周期任务 |
| 自动化 PR 评审和问题分诊 | GitHub Actions 或 GitLab CI/CD |
| 每个 PR 自动代码评审 | GitHub Code Review |
| 把 Slack 中的 bug 报告转成 pull request | Slack |
| 调试在线 Web 应用 | Chrome |
| 为你的工作流构建自定义智能体 | Agent SDK |

## 下一步

安装完 Claude Code 后，这些指南帮你深入：快速上手（从探索代码库到提交修复）、存储指令与记忆（用 CLAUDE.md 和自动记忆给 Claude 持久指令）、常用工作流与最佳实践、设置定制、故障排查，以及 code.claude.com（演示、定价与产品详情）。

---

> **翻译说明**：本文为产品文档，导航/营销条目已省略；安装命令、代码示例按惯例保留英文原文，便于直接执行对照。
