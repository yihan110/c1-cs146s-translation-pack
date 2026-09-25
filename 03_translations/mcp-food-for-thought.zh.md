# API 并不适合直接变成 MCP 工具（APIs Don't Make Good MCP Tools）

> 来源：Reily Wood 博客（mcp-food-for-thought），课程 Week 2 阅读

模型上下文协议（MCP）如今是件大事。它已经成为"把别人写的工具交给 LLM 使用"的事实标准——这当然就把它们变成了智能体。但为新的 MCP 服务器写工具很难，所以人们常提议：把现有 API 自动转换成 MCP 工具，通常用 OpenAPI 元数据来做。

根据我的经验，这**能行，但效果不好**。原因有几条：

## 智能体并不擅长大量工具

众所周知，VS Code 对工具数量有 128 个的硬上限——但许多模型远在达到那个数字之前，就已在准确调用工具上力不从心。而且每个工具及其描述都会占据宝贵的上下文窗口空间。

大多数 Web API 在设计时并没考虑这些约束！当这些 API 由代码调用时，同一个产品域有无数个 API 没问题；但如果把每个 API 都映射成一个 MCP 工具，结果可能不会好。**从零设计的 MCP 工具通常比单个 Web API 灵活得多**——每个工具能完成好几个 API 的工作。

## API 会很快烧穿上下文窗口

设想一个 API 每次返回 100 条记录，而每条记录很"宽"（比如 50 个字段）。把这样的结果原样发给智能体，会消耗大量 token；即便一个查询只需其中几个字段就能满足，所有字段仍都会进到上下文窗口里。

API 通常按记录数分页，但记录的尺寸可能差别很大。一条记录可能含一个占 100,000 token 的大文本字段，另一条可能只占 10 个。把这些 API 结果直接塞进智能体的上下文窗口是场赌博：有时能用，有时就炸了。

数据格式也会是问题。如今大多数 Web API 返回 JSON，但 JSON 是一种很浪费 token 的格式。对比一下：

```json
[
  { "firstName": "Alice", "lastName": "Johnson", "age": 28 },
  { "firstName": "Bob", "lastName": "Smith", "age": 35 }
]
```

同样的数据用 CSV 格式：

```
firstName,lastName,age
Alice,Johnson,28
Bob,Smith,35
```

CSV 数据简洁得多——每条记录只花一半的 token。通常 CSV、TSV 或 YAML（用于嵌套数据）是比 JSON 更好的选择。

这些问题都不是无法克服的。你可以想象：自动添加让智能体投影（project）字段的工具参数、自动截断或摘要大结果、自动把 JSON 结果转成 CSV（嵌套数据转 YAML）。但我见过的服务器，几乎没有哪个做这些事。

## API 没有充分利用智能体的独特能力

API 返回结构化数据供程序化消费。这通常是智能体从工具调用里想要的……但智能体也能处理其他更自由形式的指令。

例如，一个 `ask_question` 工具可以对某些文档做一次 RAG 查询，然后以纯文本返回信息、用于引导下一次工具调用——完全跳过结构化数据。或者，一次对 `search_cities` 工具的调用可以返回结构化城市列表、外加一个"接下来该调用什么"的建议：

```
city_name,population,country,region
Tokyo,37194000,Japan,Asia
Delhi,32941000,India,Asia
Shanghai,28517000,China,Asia

Suggestion: To get more specific information (weather, attractions, demographics),
try calling get_city_details with the city_name parameter.
```

这种分层和工具链式调用在 MCP 服务器里可能非常有效，而如果只是把 API 自动转成工具，你会完全错过它。

## 如果智能体需要调用 API，它本来就能直接做

Claude Code 之类的智能体如今写代码并执行代码的能力相当惊人，包括调用 Web API 的脚本。有些人甚至据此主张：根本不需要 MCP！

我不同意那个结论，但我确实认为我们应该顺势而为。智能体的沙箱化正在快速改善，如果智能体直接调用 API 既容易又安全，那不妨就这么做，砍掉中间人。

## 结论

智能体与 API 的典型消费者有本质不同。从现有 API 自动创建 MCP 工具是可能的，但这样做效果不太可能好。**智能体在拿到"为它们独特的能力与局限而设计"的工具时，表现得最好。**

---

> **翻译说明**：本文为观点随笔，示例代码/数据保留英文原文；文末博客导航已省略。术语按表统一（MCP→模型上下文协议（MCP）、agent→智能体、context window→上下文窗口、token→token、tool chaining→工具链式调用）。
