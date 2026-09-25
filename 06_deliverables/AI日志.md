# AI 协作日志（每日）

> 挑战：C1 课程资料获取与翻译 ｜ Stanford CS146S ｜ 全程不翻墙
> 说明：本文件实时记录每一步「用了什么工具 / 什么 prompt / 踩了什么坑 / 产出」。评分维度 aiUsage 的佐证。

---

## 第 1 天（2026-09-25）

### 任务 0：理解挑战与探查资料
- **工具**：PowerShell（Get-ChildItem）、Read
- **做了什么**：读取资料包 CHALLENGE.md / rubric.json / challenge.yaml / README.md，明确交付物（README、AI日志、AAR、拿说明）、评分五维、红线。
- **探查资料**：解压 `CS146S_offline.zip`（31 篇 HTML 讲义 + 3 份 PDF + 课程主页 + 站点资源）；识别出这是 Stanford CS146S「The Modern Software Developer」(2025 秋) 离线缓存。
- **发现**：外部资源（YouTube×3 / Google Slides×14 / Google Drive×5 / GitHub / Medium×1）在无翻墙环境下无法抓取 → 计入"已知缺口"，不翻墙是硬约束。
- **坑**：环境是 Windows，无 Bash，需用 PowerShell 语法（Get-ChildItem 而非 ls）；中文路径在管道传给 `python -` 时被吞输出，改为写 .py 文件再运行。

### 任务 1：资料完整性校验与归档
- **工具**：PowerShell Get-FileHash、自写 Python 脚本 `04_pipeline/01_extract.py`
- **做了什么**：
  - SHA-256 校验通过：`CS146S_offline.zip=968B7A7B…`、`Vibe_Coding_Playbook.pdf=BA5E5DDA…`，与包内记录一致。
  - 用 html.parser 把 31 篇 HTML 抽成干净 Markdown（保留标题/列表/代码块，过滤导航/页脚噪音）→ `01_sources/html/*.md`，共 **71,882 词**。
  - 用 pymupdf 抽取 3 份 PDF 文本 → `01_sources/pdf/*.txt`，约 2 万词。
  - 生成 `01_sources/source_map.json`（原文 ↔ 来源 URL ↔ 本地文件）。
- **关键判断**：`Vibe_Coding_Playbook.pdf` 经渲染后确认是**中文原创学习册**（8 周 Vibe Coding 蓝图），无需翻译。
- **坑**：`good-context-good-code`/`how-warp-uses-warp`/`lessons-from-ai-code-reviews` 是 JS 动态渲染页，静态抽取为 0~14 词；`peeking-under-the-hood` 是 Medium 被墙占位页 → 均如实列入缺口。

### 任务 2：术语表（完成 ✅）
- 起草 79 条术语表（8 条核心决策 + 63 常规 + 8 产品名），按"术语统一 + 无硬伤 + 可读性"标准定稿：Agent→智能体、Prompt Engineering→提示词工程，专名保留英文。
- 用户确认：`哪个得分高用哪个` → 已按上述标准定稿 `02_glossary/glossary.md`。

### 任务 3：可复跑翻译管线（完成 ✅）
- 设计三条脚本（04_pipeline/）：
  - `02_make_workorders.py`：从 source_map 生成 34 篇翻译工作单 + 批次 + 状态（换源可复用）。
  - `03_check_glossary.py`：术语一致性检查（质量闸门 1）。
  - `04_coverage.py`：覆盖度统计（质量闸门 2）。
- **踩坑与迭代**：`03_check_glossary.py` 初版对"保留英文"类术语（Claude Code/Warp 等）在原文未出现该词时报误报。修复：**仅当原文含该英文词时才要求译文处理**。修复后 2 篇样张 0 疑点。
- 产出样张 2 篇：`prompt-engineering-overview.zh.md`（4.4k 词）、`claude-code-best-practices.zh.md`（1.6k 词），通过术语检查。

### 任务 4：分批全量翻译（B1–B10，完成 ✅）
- **工具**：Read（读原文）+ Write/Edit（写译文）
- **做了什么**：按批次 B1–B10 逐篇翻译。约定（已获你确认）：纯中文译文、示例 prompt/代码/命令保留英文原文、专名保留英文、剔除营销噪音、文末加「翻译说明」。
- **进度**：B1 主页综述 → B3 智能体与工具 → B4 MCP → B5 上下文工程 → B6 Claude Code 与终端 → B7 代码评审 → B8 安全 → B9 SRE 与可观测 → B10 3 份 PDF，**共 34 篇全部完成**（译文总字符约 16.5 万）。
- **缺口处理**：5 篇 JS/被墙占位页（prompt-engineering-guide、good-context-good-code、how-warp-uses-warp、peeking-under-the-hood、lessons-from-ai-code-reviews）以「⚠️ 已知缺口」如实标注；其中 3 篇低正文/占位（原文 <30 词）不计入可译统计（可译篇 31/31=100%），其余如实标注、不伪造成完整译文。
- **坑**：Write 工具偶发 timeout，实为瞬时、文件实际已写入，用 Glob 复核确认。

### 任务 5：质量闸门与覆盖度（100% ✅）
- **工具**：PowerShell + 04_pipeline 三脚本
- **做了什么**：重跑 `02_make_workorders.py` / `03_check_glossary.py` / `04_coverage.py`。
- **踩坑与迭代**：
  - PDF 译文我写成 `.zh.md`，但工作单脚本按 `pdf` 标志生成 `.zh.txt` 路径 → 覆盖度假报 90.3%。修复：`02_make_workorders.py` 统一译文后缀为 `.zh.md`，重跑 → **100%**。
  - 术语检查 3 类误报并修复：①"保留英文"词在原文未出现时误报（已在前修复）；②缺口占位篇（原文 0 词）报 keep 误报 → 跳过 `source_words<30`；③`agent` 是产品名（Graphite Agent）组成部分触发"需中文"误报 → 在翻译说明标注产品名不译。
- **终值（最后一次闸门实况）**：`03_check_glossary.py` 输出「已检查 31 篇 | 无问题 31 篇 | 有疑点 0 篇」→ 术语一致性 **0 疑点**；`04_coverage.py` 输出「可译篇数(排除JS/占位) 31 | 已完成 31 | 覆盖度 100.0%」→ 覆盖度 **100%**（口径：34 篇全部产出译文，其中 3 篇低正文/占位不计入可译统计）。
- **复核修正**：`05_quality/glossary_check_report.json` 曾对 `how-anthropic-uses-claude-code` 报 1 条 `agentic→智能体驱动` 疑点（翻译说明误写"智能体式"）——已修正该译文为"智能体驱动"，重跑后 0 疑点；同时把 4 条脚本的写死绝对路径改为基于 `__file__` 的相对路径，任意机器可直接运行。

### 任务 6：交付物撰写与发布
- **工具**：Write
- **做了什么**：撰写 `06_deliverables/` 下 README.md、AAR.md（七维复盘）、拿说明1~3.md；续写本日志；写 `06_deliverables/发布步骤.md` 并打包。
- **产出**：四类交付物齐全；术语表 79 条；覆盖度 100%；管线 4 脚本可复跑。

### 任务 7：交付前终审修正（第三轮）
- **工具**：Bash（Python 脚本）/ Edit
- **做了什么**：
  - 重新生成 `03_translations/manifest.json`：把 `source` / `zh` / `glossary` 三类字段共 69 处**写死的旧绝对路径**（指向已不存在的旧工作目录）全部改为**包内相对路径**（`01_sources/html/…`、`03_translations/…`），并让生成脚本按工作根解析；复检残留绝对路径 = **0 处**。
  - `03_check_glossary.py` 加**非静默防护**：检查篇数为 0 时直接报错退出，并区分 `skipped_low`（正文 <30 词）与 `skipped_missing`（译文缺失）——换机器重跑不会再得到「已检查 0 篇｜0 疑点」的假绿结论。
  - 补 `materials/README.md`（说明原始资料不随包分发、复跑第 1 步的前置条件）；清掉全部 `07_release/` 陈旧引用，统一为「交付 zip 即发布产物」；修正 `分步执行计划.md` 中指向已不存在脚本的陈旧引用与残留旧目录名。
  - 统一覆盖口径：34 篇全部产出译文，其中 3 篇正文 <30 词不计入可译统计 → **可译 31/31 = 100%**。
- **终值**：`03` → 已检查 31 篇｜无问题 31 篇｜有疑点 0 篇；`04` → 可译 31 篇｜已完成 31 篇｜覆盖度 100.0%；全包残留写死绝对路径 **0 处**。

### 任务 8：译文质量抽检（第四轮补证据）
- **工具**：新写 `04_pipeline/05_qa_sample.py` + Read 人工核对
- **做了什么**：覆盖度和术语闸门只回答"有没有文件、术语对不对"，回答不了"有没有漏译/机翻硬伤"。补一道抽检：逐篇数 CJK 汉字、剥代码块后抓 >6 词的英文长句、列出汉字 <200 的疑似占位篇。
- **结果**：全包汉字 **94,702**（≈9.5 万，与 README 自报一致）；疑似低汉字篇仅 3 个（good-context-good-code / how-warp-uses-warp / peeking-under-the-hood，均为已知 JS 空壳/被墙占位）；残留英文长句命中 2 篇（how-openai-uses-codex、prompt-engineering-overview）。
- **人工判定**：把命中的英文长句打开核对，全是文章里的**示例 prompt**（如 "Split this file into separate modules..."），按"示例 prompt/代码/命令保留英文"规则应保留，非漏译。脚本负责报警、人负责判定，不盲信。
- **产出**：`05_quality/qa_sample_report.json` + `拿来说明4-翻译质量抽检闭环.md`。

成 ✅）
