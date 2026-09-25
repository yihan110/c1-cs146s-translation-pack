# 构建远程 MCP 服务器（Build a Remote MCP Server）

> 来源：Cloudflare 开发者文档（课程 Week 2 阅读）

本指南将展示如何使用 **Streamable HTTP 传输**（当前 MCP 规范标准）在 Cloudflare 上部署你自己的远程 MCP 服务器。你有两种选择：

- **无认证**——任何人都能连接并使用服务器（无需登录）。
- **带认证与授权**——用户在访问工具前需登录，你可以根据用户权限控制智能体能调用哪些工具。

## 选择方案

Agents SDK 提供多种创建 MCP 服务器的方式，选择适合你用例的方案：

| 方案 | 有状态？ | 需要 Durable Objects？ | 最适合 |
|---|---|---|---|
| `createMcpHandler()` | 否 | 否 | 无状态工具，搭建最简单 |
| `McpAgent` | 是 | 是 | 有状态工具、按会话状态、elicitation |
| `Raw WebStandardStreamableHTTPServerTransport` | 否 | 否 | 完全掌控，不依赖 SDK |

- `createMcpHandler()` 是让一个无状态 MCP 服务器最快跑起来的方式，适用于工具不需要按会话状态的场景。
- `McpAgent` 为每个会话提供一个 Durable Object，内置状态管理、elicitation 支持，以及 SSE 和 Streamable HTTP 两种传输。
- Raw transport 让你想直接使用 `@modelcontextprotocol/sdk`、不借助 Agents SDK 辅助时获得完全掌控。

## 部署你的第一个 MCP 服务器

你可以先部署一个**公共 MCP 服务器**（无认证），之后再添加用户认证和范围化授权。如果你已经知道服务器需要认证，可跳到下一节。

### 通过控制台部署

部署示例 MCP 服务器到你的 Cloudflare 账号，部署完成后服务器会运行在你的 workers.dev 子域名（例如 `remote-mcp-server-authless.your-account.workers.dev/mcp`）。你可以立即用 AI Playground（一个远程 MCP 客户端）、MCP inspector 或其他 MCP 客户端连接它。一个新的 git 仓库会在你的 GitHub 或 GitLab 账号中为你的 MCP 服务器建立，配置为每次向主分支推送变更或合并 pull request 时自动部署到 Cloudflare。你可以克隆该仓库、本地开发、开始用你自己的工具定制 MCP 服务器。

### 通过 CLI 部署

可以用 Wrangler CLI 在本地机器创建一个新的 MCP 服务器并部署到 Cloudflare。

打开终端运行以下命令：

```bash
npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
# 或
yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
# 或
pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

安装过程中选择以下选项：对"Do you want to add an AGENTS.md file…"，选 No；对"Do you want to use git for version control?"，选 No；对"Do you want to deploy your application?"，选 No（我们会在部署前先测试服务器）。

现在你有了带依赖的 MCP 服务器项目。进入项目文件夹并启动开发服务器：

```bash
cd remote-mcp-server-authless
npm start
```

检查命令输出的本地端口。本例中 MCP 服务器运行在 8788 端口，MCP 端点 URL 为 `http://localhost:8788/mcp`。

**本地测试**：在新终端运行 MCP inspector（一个交互式 MCP 客户端，让你从浏览器连接 MCP 服务器并调用工具）：

```bash
npx @modelcontextprotocol/inspector@latest
```

MCP Inspector 会在浏览器中启动（也可手动打开 `http://localhost:<PORT>`）。在 inspector 里输入 MCP 服务器 URL（`http://localhost:8788/mcp`），选择 Connect，再选 List Tools 查看服务器暴露的工具。

**部署到 Cloudflare**：从项目目录运行：

```bash
npx wrangler@latest deploy
```

如果你已把 git 仓库连接到包含 MCP 服务器的 Worker，也可通过向主分支推送变更或合并 pull request 来部署。服务器会部署到你的 `*.workers.dev` 子域名，位于 `https://remote-mcp-server-authless.your-account.workers.dev/mcp`。取该 URL 在 MCP inspector（运行在 `http://localhost:5173`）里测试。现在你就有了一个 MCP 客户端可连接的远程 MCP 服务器。

## 通过本地代理从 MCP 客户端连接

远程 MCP 服务器运行后，你可以用 `mcp-remote` 本地代理把 Claude Desktop 或其他 MCP 客户端连接到它——即便你的 MCP 客户端在客户端侧不支持远程传输或授权。这让你能用真实 MCP 客户端测试与远程 MCP 服务器的交互体验。

例如，从 Claude Desktop 连接：更新 Claude Desktop 配置，指向你 MCP 服务器的 URL：

```json
{
  "mcpServers": {
    "math": {
      "command": "npx",
      "args": ["mcp-remote", "https://remote-mcp-server-authless.your-account.workers.dev/mcp"]
    }
  }
}
```

重启 Claude Desktop 加载 MCP 服务器，之后 Claude 就能调用你的远程 MCP 服务器。测试时让 Claude 用你的一个工具，例如："Could you use the math tool to add 23 and 19?" Claude 应调用该工具并显示远程服务器产生的结果。

## 添加认证

前面部署的公共 MCP 服务器允许任何客户端不登录就连接并调用工具。要为你的 MCP 服务器添加用户认证，可以集成 Cloudflare Access 或第三方服务作为 OAuth 提供方。你的 MCP 服务器处理安全的登录流程，并签发 MCP 客户端可用来做已认证工具调用的访问 token。用户用 OAuth 提供方登录，并用**范围化权限**授权他们的 AI 智能体与 MCP 服务器暴露的工具交互。

### Cloudflare Access OAuth

你可以配置 MCP 服务器通过 Cloudflare Access 要求用户认证。Cloudflare Access 充当身份聚合器，验证用户邮箱、来自现有身份提供方（如 GitHub 或 Google）的信号、以及其他属性（如 IP 地址或设备证书）。用户连接 MCP 服务器时会被提示登录所配置的身份提供方，只有通过你的 Access 策略才会被授予访问。

### 第三方 OAuth

你可以把 MCP 服务器连接到任何支持 OAuth 2.0 规范的 OAuth 提供方，包括 GitHub、Google、Slack、Stytch、Auth0、WorkOS 等。下面示例演示如何用 GitHub 作为 OAuth 提供方。

#### 第 1 步——创建新的 MCP 服务器

运行以下命令创建带 GitHub OAuth 的 MCP 服务器：

```bash
npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
# 或
yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
# 或
pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

进入项目文件夹。注意示例 MCP 服务器的 `src/index.ts` 里，主要区别是 `defaultHandler` 被设置为 `GitHubHandler`：

```ts
import GitHubHandler from "./github-handler";
export default new OAuthProvider({
  apiRoute: "/mcp",
  apiHandler: MyMCP.serve("/mcp"),
  defaultHandler: GitHubHandler,
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  clientRegistrationEndpoint: "/register",
});
```

这确保你的用户被重定向到 GitHub 认证。要让这跑通，你需要按下面步骤创建 OAuth 客户端应用。

#### 第 2 步——创建 OAuth 应用

你需要创建两个 GitHub OAuth App——一个用于本地开发，一个用于生产。

**本地开发 OAuth App**：在 `github.com/settings/developers` 创建新 OAuth App，设置：
- Application name: My MCP Server (local)
- Homepage URL: `http://localhost:8788`
- Authorization callback URL: `http://localhost:8788/callback`

把该 OAuth App 的 client ID 作为 `GITHUB_CLIENT_ID`，生成 client secret 作为 `GITHUB_CLIENT_SECRET`，加到项目根目录的 `.env` 文件（用于本地开发的 secrets）：

```bash
touch .env
echo 'GITHUB_CLIENT_ID="your-client-id"' >> .env
echo 'GITHUB_CLIENT_SECRET="your-client-secret"' >> .env
cat .env
```

启动开发服务器（`npm start`），服务器运行在 `http://localhost:8788/mcp`。新终端运行 MCP inspector（`npx @modelcontextprotocol/inspector@latest`），打开 `http://localhost:5173`。在 inspector 里输入 `http://localhost:8788/mcp`，点击右侧 OAuth Settings 按钮，再点 Quick OAuth Flow。你会被重定向到 GitHub 登录/授权页；授权 MCP 客户端（inspector）访问你的 GitHub 账号后，会被重定向回 inspector。点击 Connect，应能看到 List Tools 按钮列出服务器暴露的工具。

**生产 OAuth App**：重复以上步骤创建生产用 OAuth App，设置：
- Application name: My MCP Server (production)
- Homepage URL: 你的 MCP 服务器的 workers.dev URL（如 `worker-name.account-name.workers.dev`）
- Authorization callback URL: 该 URL 的 `/callback` 路径

用 Wrangler CLI 设置 client ID 和 secret：

```bash
npx wrangler secret put GITHUB_CLIENT_ID
npx wrangler secret put GITHUB_CLIENT_SECRET
npx wrangler secret put COOKIE_ENCRYPTION_KEY   # 填任意随机字符串，如 openssl rand -hex 32
```

设置 KV 命名空间：创建命名空间（`npx wrangler kv namespace create "OAUTH_KV"`），把返回的 KV ID 更新进 `wrangler.jsonc`：

```json
{
  "kvNamespaces": [
    { "binding": "OAUTH_KV", "id": "<YOUR_KV_NAMESPACE_ID>" }
  ]
}
```

部署到 Cloudflare workers.dev 域名（`npm run deploy`），然后用 AI Playground、MCP Inspector 或其他 MCP 客户端连接到运行在 `worker-name.account-name.workers.dev/mcp` 的服务器，并用 GitHub 认证。

## 下一步

- **MCP Tools**：给 MCP 服务器添加工具。
- **Authorization**：定制认证与授权。

---

> **翻译说明**：本文为实操部署教程，命令、代码块、配置 JSON 一律保留英文原文便于直接执行；教程配图已省略。术语按表统一（MCP→模型上下文协议（MCP）、authentication→认证、authorization→授权、tool→工具）。
