# Trace 与 Span：你该知道的可观测性基础（Traces & Spans: Observability Basics You Should Know）

> 来源：Last9 博客（Anjali Udasi，2025-04-23），课程 Week 9 阅读

了解 trace 和 span 如何帮你透视分布式系统内部——从而更快排障、构建更可靠的软件。

在现代软件架构中，应用不只是变大——它们变得更分布式。随着微服务、无服务器函数和容器跨多环境运行，理解系统内部发生什么，感觉就像想在暴风雨中追踪一滴雨。这就是 trace 和 span 的用武之地。这些可观测性工具不只是流行词——它们是理解复杂分布式系统的秘密武器。

## 理解 Trace 与 Span：核心概念

**Trace（追踪）**捕获一个请求在分布式系统中穿行的旅程。把 trace 想成请求从头到尾的完整故事——从用户点击按钮，到他们看到结果。

**Span（跨度）**是 trace 的构建块。每个 span 代表那段旅程中的一个工作单元——如一次数据库查询、一次 API 调用或一次函数执行。span 相互嵌套，展示操作间的父子关系。简单来说：一个 trace 包含多个 span；每个 span 代表一个操作；span 带计时数据和元数据；span 可嵌套以显示操作间如何关联。

```
Trace
├── Span (API 网关)
│   ├── Span (认证服务)
│   └── Span (用户服务)
│       └── Span (数据库查询)
└── Span (响应格式化)
```

## 对 DevOps 专业人员的价值

假设你在运行一个有几十个微服务的复杂系统。突然用户报告结账流程变慢。没有追踪，你得逐个检查每个服务，浪费宝贵时间。有了 trace 和 span，你可以：
- **瞬间找到瓶颈**：精确看到哪个服务或函数耗时过长；
- **跨服务边界调试**：跟随请求在服务间跳跃；
- **理解依赖**：可视化服务如何连接和相互依赖；
- **改善性能**：精确识别并修复慢操作；
- **缩短平均恢复时间（MTTR）**：问题出现时更快定位根因。

## Trace 与 Span 的技术实现

### Trace 上下文与传播
要让追踪跨服务边界生效，每个服务需要知道它处理的是同一个请求的一部分。这通过**上下文传播（context propagation）**实现——在服务间传递 trace ID 和 span ID。请求首次命中系统时，被分配一个唯一 trace ID；随请求在服务间移动，该 ID 跟随它（通常作为 HTTP 头）。每个服务随后创建自己的 span，但把它们链到同一 trace。

### Span 属性与事件
span 不只是时间戳——它们富含数据：**名称**（此 span 代表什么操作）、**计时**（开始和结束时间）、**状态**（成功、错误等）、**属性**（自定义键值对，如 user_id 或 cart_size）、**事件**（span 内的显著事件）、**链接**（到其他 span 的连接）。

### 采样策略
追踪一切会生成海量数据，所以多数系统用**采样（sampling）**——只收集一定比例的 trace。明智的采样策略包括：
- **头采样（head-based）**：在请求开始时决定是否采样；
- **尾采样（tail-based）**：在请求完成后决定（更利于捕获错误）；
- **优先级采样**：重要操作始终追踪，常规操作按比例采样。

## 追踪实现指南：工具与框架

### OpenTelemetry：行业标准
OpenTelemetry 已成为实现 trace 和 span 的主流框架。它提供：覆盖所有主流编程语言的库；厂商中立的 API 和 SDK；流行框架的自动插桩；收集和导出数据的一致方式。

### 追踪工具箱
| 工具 | 类型 | 最适合 |
|---|---|---|
| Last9 | 一体化可观测 | 经济高效、高基数可观测，定价可预期 |
| Jaeger | 开源追踪 | 自托管追踪可视化 |
| Zipkin | 开源追踪 | 简单分布式追踪 |
| Grafana Tempo | 追踪后端 | 与 Grafana 仪表盘集成 |
| OpenTelemetry Collector | 数据收集管线 | 处理和路由遥测数据 |

### 在代码中实现追踪
以下是用 OpenTelemetry 在 Node.js 应用中创建 span 的简化示例（代码保留英文原文）：

```
// Initialize the OpenTelemetry SDK (once in your app)
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { SimpleSpanProcessor } = require('@opentelemetry/sdk-trace-base');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');

const provider = new NodeTracerProvider();
const exporter = new OTLPTraceExporter({
  url: 'http://localhost:4318/v1/traces',
});
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.register();

// Get a tracer
const { trace } = require('@opentelemetry/api');
const tracer = trace.getTracer('my-service');

// Create spans in your code
async function processOrder(orderId) {
  const span = tracer.startSpan('process-order');

  // Add attributes to the span
  span.setAttribute('order.id', orderId);
  span.setAttribute('customer.type', 'premium');

  try {
    // Do work...

    // Create a child span
    const dbSpan = tracer.startSpan('database-query', {
      parent: span,
    });

    try {
      // Run database query...
      dbSpan.end();
    } catch (error) {
      dbSpan.setStatus({ code: SpanStatusCode.ERROR });
      dbSpan.recordException(error);
      dbSpan.end();
      throw error;
    }

    span.end();
  } catch (error) {
    span.setStatus({ code: SpanStatusCode.ERROR });
    span.recordException(error);
    span.end();
    throw error;
  }
}
```

## 高级追踪技术

### 分布式上下文管理
在复杂系统中，你需要管理的不只是 trace ID。W3C Trace Context 规范为以下提供标准：`traceparent`（含 trace ID 和父 span ID）；`tracestate`（允许厂商添加自定义上下文数据）。使用这些头确保追踪跨不同服务和厂商都能工作。

### Trace、指标与日志的关联
可观测性的真正力量来自连接不同信号：**示例 trace（exemplar）**把指标链接到生成它们的 trace；**日志中的 trace ID**——在日志消息中加 trace ID 以便交叉引用；**自定义属性**——在所有遥测类型间使用一致属性。

### 错误处理与异常追踪
异常发生时，span 能提供关键上下文：用错误状态标记 span；记录带堆栈追踪的异常；给 span 添加显示错误演进的事件；创建跨服务边界携带错误上下文的 baggage 项。

## 真实世界的追踪模式与反模式

**有效模式**：有意义的 span 名称（用 `service_name/operation` 之类一致命名约定）；正确的粒度（为重要操作创建 span，而非每次函数调用）；正确的上下文传播（确保 trace 上下文流经所有通信渠道）；有用的属性（添加有助于排障的属性，如用户 ID 或特性开关）；性能意识（注意过多 span 创建的开销）。

**要避免的反模式**：过度插桩（创建太多 span 会导致性能问题）；缺失上下文（未能传播上下文会跨服务边界断开 trace）；命名不一致（不同命名标准让 trace 难解释）；数据过多（把大载荷放进 span 会压垮追踪后端）；忽视第三方服务（缺少外部调用 span 会造成盲区）。

## Trace 与 Span 的业务价值

trace 不只用于排障——也能提供业务洞察：端到端追踪关键用户旅程；衡量关键业务操作的性能；基于 trace 数据设定 SLO（服务级别目标）；以真实用户术语量化性能问题成本；通过向 span 添加相关属性创建业务上下文。当你能展示技术改进如何影响用户体验和业务指标，你就弥合了 DevOps 与业务干系人的鸿沟。

## 结论

Trace 和 span 给你的分布式系统带来 X 光透视。它们揭示服务间的隐藏连接、精确定位性能瓶颈、大幅加速调试。随系统日益复杂，这种可观测性不是奢侈品——而是必需品。

## FAQ
- **追踪和日志有何区别？** 日志捕获离散事件，追踪展示操作在服务间的关系。日志告诉你发生了什么；追踪展示它如何发生。
- **加追踪会拖慢我的应用吗？** 现代追踪库增加的开销极低——配置恰当时通常不到 3% 性能影响。配合采样可进一步降低。
- **我需要修改所有代码才能加追踪吗？** 不一定。许多框架提供自动插桩，几乎不改代码即可加追踪。OpenTelemetry 为多数语言的主流框架提供自动插桩。
- **分布式追踪会生成多少数据？** 因流量、采样率和 span 细节差异很大。繁忙系统要按每天几 GB 到几 TB 规划。因此选对可观测平台对成本控制很重要。
- **trace 能帮上安全和合规吗？** 能。Trace 为请求在系统中的流动创建审计轨迹。配合正确属性，可追踪哪些用户或服务、何时访问了什么数据。
- **trace 和 span 如何与其他可观测性信号配合？** Trace 补充指标和日志。指标高层展示系统健康，日志提供详细事件，trace 连接各点展示服务间的请求流。

---

> **翻译说明**：本文为可观测性（OpenTelemetry/trace/span）技术讲解，示例代码按约定保留英文原文；营销性段落（Last9 产品推广、CTA、社区链接）已精简省略。术语按表统一（trace→trace/追踪、span→span、observability→可观测性、sampling→采样、telemetry→遥测、instrumentation→插桩）。
