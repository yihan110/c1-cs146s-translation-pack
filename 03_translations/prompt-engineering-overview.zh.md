# 提示词工程：总览与指南（Prompt Engineering: Overview and Guide）

> 来源：Google Cloud — Prompt engineering: overview and guide（课程 Week 1 阅读）
> 中文翻译：C1 挑战翻译管线 ｜ 术语表 v1 ｜ 最后更新 2026-01-14（原文）

大语言模型（LLM）的兴起为人机交互带来了令人兴奋的可能性。然而，要充分释放这些强大 AI 模型的能力，需要一项关键技能：**提示词工程**。这个新兴领域专注于设计有效的提示词，以解锁大语言模型的能力，让它们理解意图、遵循指令并生成期望的输出。随着我们在各种应用中越来越多地与 AI 交互，提示词工程在确保准确、相关且安全的交互方面发挥着至关重要的作用。

## 什么是提示词工程？

提示词工程是一门"艺术与科学"：设计和优化提示词，引导 AI 模型（尤其是大语言模型）生成期望的回应。通过精心构造提示词，你为模型提供上下文、指令和示例，帮助它理解你的意图并做出有意义的回应。可以把它想象成给 AI 提供一张路线图，把它引向你心中特定的输出。

想深入了解提示词设计及其应用，可查阅 Google Cloud 的《提示词设计导论》（Introduction to Prompt Design）。想亲手实践大语言模型和提示词工程，可以试试 Vertex AI 免费试用版。

## 什么是 AI 提示词（Prompt）？

在 AI 语境中，提示词是你提供给模型以诱发特定回应的输入。它的形式多种多样，从简单的问题或关键词，到复杂的指令、代码片段，甚至创作样例。提示词的质量直接决定 AI 输出的质量与相关性。

## 提示词工程需要什么？

几个关键要素共同促成有效的提示词工程。掌握它们，你就能与 AI 模型高效沟通，并释放其全部潜力。

### 提示词格式

提示词的结构与风格对引导 AI 的回应有显著影响。不同模型可能对不同格式响应更好，例如自然语言提问、直接指令，或带特定字段的结构化输入。理解模型的能力和它偏好的格式，是写出有效提示词的关键。

### 上下文与示例

在提示词中提供上下文和相关的示例，能帮助 AI 理解期望的任务，生成更准确、更相关的输出。例如，如果你想要一个创作故事，在提示词里写几句描述期望的语气或主题的话，往往能显著改善结果。

### 微调与适配

针对特定任务或领域，用定制提示词微调 AI 模型，可以提升它的表现。此外，根据用户反馈或模型输出适配提示词，也能随着时间推移进一步改进模型回应。

### 多轮对话

为多轮对话设计提示词，让用户能与 AI 模型进行连续、有上下文感知的交互，从而提升整体用户体验。

## 提示词的类型

AI 中使用的提示词有多种类型，各有特定用途：

### 直接提示词（零样本，Zero-shot）

零样本提示：直接给模型一个指令或问题，不带任何额外上下文或示例。例如创意生成——让模型生成创意想法或头脑风暴方案；又如摘要或翻译——让模型对某段内容做概括或翻译。

### 单样本、少样本与多样本提示词

这种方法在给出真正的提示词之前，先给模型提供一个或多个期望的"输入-输出"对示例。这能帮助模型更好地理解任务，生成更准确的回应。

### 思维链提示词（Chain-of-Thought, CoT）

CoT 提示鼓励模型把复杂推理拆解成一系列中间步骤，从而得到更全面、结构更清晰的最终输出。

### 零样本思维链提示词

把思维链提示与零样本提示结合：让模型逐步进行推理，往往能产出更好的结果。

## 提示词工程的应用场景与示例

下面是一些具体示例和应用场景，展示提示词工程如何产出定制化、相关的输出。

### 语言与文本生成

| 场景 | 指令 | 示例提示词 |
|---|---|---|
| 创意写作 | 构造提示词，指定题材、语气、风格和情节要点，引导 AI 生成引人入胜的叙事。 | "Write a short story about a young woman who discovers a magical portal in her attic." |
| 摘要 | 给 AI 提供文本，指令它生成抓住关键信息的简洁摘要。 | "Summarize the main points of the following news article on climate change." |
| 翻译 | 指定源语言与目标语言，让 AI 在保留意义和上下文的同时准确翻译。 | "Translate the following text from English to Spanish: 'The quick brown fox jumps over the lazy dog.'" |
| 对话 | 设计模拟对话的提示词，让 AI 生成模仿人类互动并保持上下文的回应。 | "You are a friendly chatbot helping users troubleshoot their computer problems. Respond to the user's query: 'My computer won't turn on.'" |

### 问答

| 场景 | 指令 | 示例提示词 |
|---|---|---|
| 开放式问题 | 构造提示词，鼓励 AI 基于其知识库给出全面、信息量大的回答。 | "Explain the concept of quantum computing and its potential impact on the future of technology." |
| 具体问题 | 设计提示词锁定特定信息，让 AI 从给定上下文或其内部知识库中取回精确答案。 | "What is the capital of France?" 或 "According to the provided text, what are the main causes of deforestation?" |
| 选择题 | 给出带选项的提示，让 AI 分析并选出最恰当的答案。 | "Who wrote the Harry Potter series? A) J.R.R. Tolkien, B) J.K. Rowling, C) Stephen King" |
| 假设性问题 | 构造探索假设情境的提示，让 AI 推理、推测，给出可能的结果或方案。 | "What would happen if humans could travel at the speed of light?" |
| 观点类问题 | 设计提示词引出 AI 对特定话题的看法或观点，鼓励它为自己的立场提供推理和理由。 | "Do you believe that artificial intelligence will eventually surpass human intelligence? Why or why not?" |

### 代码生成

| 场景 | 指令 | 示例提示词 |
|---|---|---|
| 代码补全 | 给 AI 一段不完整的代码片段，提示它基于上下文和编程语言补全剩余代码。 | "Write a Python function to calculate the factorial of a given number." |
| 代码翻译 | 指定源与目标编程语言，让 AI 在保留功能与语法的情况下翻译代码。 | "Translate the following Python code to JavaScript: def greet(name): print('Hello,', name)" |
| 代码优化 | 让 AI 分析现有代码，就效率、可读性或性能提出改进建议。 | "Optimize the following Python code to reduce its execution time." |
| 代码调试 | 给 AI 提供含错误的代码，提示它定位问题并给出解决方案。 | "Debug the following Java code and explain why it is throwing a NullPointerException." |

### 图像生成

| 场景 | 指令 | 示例提示词 |
|---|---|---|
| 逼真图像 | 构造提示词，详细描述期望的图像，包括物体、风景、光线和风格，以生成真实高质量的图像。 | "A photorealistic image of a sunset over the ocean with palm trees silhouetted against the sky." |
| 艺术图像 | 设计提示词，指定艺术风格、技法和主题，引导 AI 生成模仿特定艺术流派或唤起特定情绪的图像。 | "An impressionist painting of a bustling city street with people walking under umbrellas in the rain." |
| 抽象图像 | 构造提示词，鼓励 AI 生成开放解读的图像，利用形状、色彩和质感来唤起感受或概念。 | "An abstract image representing the concept of hope, using bright colors and flowing shapes." |
| 图像编辑 | 给 AI 一张现有图像并指定期望的修改，让它按指令编辑和增强图像。 | "Change the background of this photo to a starry night sky and add a full moon." 或 "Remove the person from this image and replace them with a cat." |

## 写出更好提示词的策略

写出有效提示词需要策略性方法。可参考以下策略提升你的提示词工程能力：

### 1. 设定清晰的目标与目的

| 策略 | 示例提示词 |
|---|---|
| 用动作动词指明期望的动作 | "Write a bulleted list that summarizes the key findings of the attached research paper" |
| 定义输出的期望长度和格式 | "Compose a 500-word essay discussing the impact of climate change on coastal communities." |
| 指明目标受众 | "Write a product description for a new line of organic skincare products, targeting young adults concerned with sustainability." |

### 2. 提供上下文与背景信息

| 策略 | 示例提示词 |
|---|---|
| 包含相关事实与数据 | "Given that global temperatures have risen by 1 degree Celsius since the pre-industrial era, discuss the potential consequences for sea level rise." |
| 引用特定来源或文档 | "Based on the attached financial report, analyze the company's profitability over the past five years." |
| 定义关键术语与概念 | "Explain the concept of quantum computing in simple terms, suitable for a non-technical audience." |

### 3. 使用少样本提示（Few-Shot Prompting）

| 策略 | 示例提示词 |
|---|---|
| 提供几个期望的输入-输出对 | Input: "Cat" Output: "A small furry mammal with whiskers." Input: "Dog" Output: "A domesticated canine known for its loyalty." Prompt: "Elephant" |
| 示范期望的风格或语气 | Example 1 (humorous): "The politician's speech was so dull, it could cure insomnia." Example 2 (formal): "The dignitary delivered an address that was both informative and engaging." Prompt: "Write a sentence describing the comedian's stand-up routine." |
| 展示期望的细节程度 | Example 1 (brief): "The movie was about a young boy who befriends an alien." Example 2 (detailed): "The science fiction film follows the story of Elliot, a lonely boy who discovers and forms a unique bond with an extraterrestrial stranded on Earth." Prompt: "Summarize the plot of the novel you just finished reading." |

### 4. 尽量具体

| 策略 | 示例提示词 |
|---|---|
| 使用精确的语言，避免含糊 | 不说 "Write something about climate change," 而用 "Write a persuasive essay arguing for the implementation of stricter carbon emission regulations." |
| 尽可能量化你的请求 | 不说 "Write a long poem," 而用 "Write a sonnet with 14 lines that explores themes of love and loss." |
| 把复杂任务拆解成小步骤 | 不说 "Create a marketing plan," 而用 "1. Identify the target audience. 2. Develop key marketing messages. 3. Choose appropriate marketing channels." |

### 5. 迭代与试验

| 策略 | 操作 |
|---|---|
| 尝试不同的措辞与关键词 | 用同义词或替代句式重写提示词。 |
| 调整细节与具体的程度 | 增删信息以微调输出。 |
| 测试不同的提示词长度 | 分别用更短和更长的提示词试验，找到最优平衡。 |

### 6. 善用思维链提示（Chain of Thought Prompting）

| 策略 | 示例提示词 |
|---|---|
| 鼓励逐步推理 | "Solve this problem step-by-step: John has 5 apples, he eats 2. How many apples does he have left? Step 1: John starts with 5 apples. Step 2: He eats 2 apples, so we need to subtract 2 from 5. Step 3: 5 - 2 = 3. Answer: John has 3 apples left." |
| 让模型解释其推理过程 | "Explain your thought process in determining the sentiment of this movie review: 'The acting was superb, but the plot was predictable.'" |
| 引导模型按逻辑顺序思考 | "To classify this email as spam or not spam, consider the following: 1. Is the sender known? 2. Does the subject line contain suspicious keywords? 3. Is the email offering something too good to be true?" |

更多提示词工程最佳实践，可查阅 Google Cloud《提示词工程五大最佳实践》。

## 提示词工程的益处

有效的提示词工程带来诸多好处，能增强 AI 模型的能力与易用性：

- **提升模型表现**：精心构造的提示词为模型提供清晰的指令和上下文，带来更准确、相关且信息量大的输出。
- **减少偏见与有害回应**：通过仔细控制输入并引导 AI 的关注点，提示词工程有助于缓解偏见、最大限度降低生成不当或冒犯性内容的风险。
- **增强控制与可预测性**：提示词工程让你能够影响 AI 的行为，确保输出一致、可预测，并与你的预期结果对齐。
- **改善用户体验**：清晰简洁的提示词让用户更容易与 AI 模型有效交互，带来更直观、更满意的体验。

---

> **翻译说明**：本篇主体为概念讲解与示例表格，已全量翻译；示例提示词按惯例保留英文原文，便于对照与直接复用。Google Cloud 营销段落（免费额度、产品列表等）与课程教学无关，已省略。
