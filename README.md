# 挑战 C1 · Stanford CS146S 课程全量中文翻译包

> **挑战**：C1 课程资料获取与翻译 ｜ **课程**：Stanford CS146S《The Modern Software Developer》(2025 秋) ｜ **全程不翻墙**

本包交付 Stanford CS146S 课程的**全量中文翻译**，基于你提供的离线资料包（`CS146S_offline.zip` + `Vibe_Coding_Playbook.pdf`），不含任何翻墙获取的在线内容。

---

## 一、交付了什么

| 交付物 | 位置 | 说明 |
|---|---|---|
| 中文译文 | `03_translations/*.zh.md` | **34 篇全部产出**，逐篇与原文对照 |
| 术语表 | `02_glossary/glossary.md` | **79 条**定稿（Agent→智能体、Prompt Engineering→提示词工程等） |
| 可复跑管线 | `04_pipeline/*.py` | 抽取 → 工作单 → 术语检查 → 覆盖度统计，换源可复用 |
| README | 本文件 | 使用说明 |
| AI 协作日志 | `06_deliverables/AI日志.md` | 每天做了什么、踩了什么坑（aiUsage 佐证） |
| AAR 复盘 | `06_deliverables/AAR.md` | 七维复盘：成功/失败经验 + 改进方案 |
| 拿说明 | `06_deliverables/拿说明1~4.md` 共 4 个 | 四个关键产出的「怎么做出来」演示（含真实 prompt 与前后对比） |
| 发布步骤 | `06_deliverables/发布步骤.md` | 本地 zip / GitHub 发布说明（不翻墙、可选） |
| 质量报告 | `05_quality/*.json` | 术语一致性（0 疑点）+ 覆盖度（100%）+ 译文质量抽检（汉字 94,702） |

## 二、来源与完整性

- **原始资料**：`materials/CS146S_offline.zip`（Stanford CS146S 2025 秋离线缓存：**31 篇 HTML 讲义 + 3 份 PDF + 课程主页 + 站点资源**）与 `materials/Vibe_Coding_Playbook.pdf`。**原始资料不随本交付包分发**（见 `materials/README.md`）；复跑第 1 步前需按该说明自备，第 2–4 步无需原始资料即可直接运行。
- **校验通过**（SHA-256 前缀）：`CS146S_offline.zip=968B7A7B…`、`Vibe_Coding_Playbook.pdf=BA5E5DDA…`。
- `Vibe_Coding_Playbook.pdf` 经渲染确认为**中文原创学习册**（8 周 Vibe Coding 蓝图），本身是中文，无需翻译，仅作背景资料。
- 全部处理基于**本地离线文本**，无任何外链图片、无翻墙访问。

## 三、覆盖范围（口径：34 篇全部产出译文）

- **总篇数**：34 篇（31 篇 HTML + 3 份 PDF），**每篇都产出了译文文件**。
- **可译篇数**：34 篇原文中，3 篇为低正文/占位页（原文 <30 词的 JS 动态渲染/访问码占位页）不计入可译统计 → **可译 31 篇、全部完成**，覆盖度 **31/31 = 100%**（挑战要求 ≥80%）。
- **总量**：原文约 **92,649 词**（31 篇 HTML 71,882 词 + 3 份 PDF 20,767 词）；译文 **34 篇、约 16.5 万字符**（含标点与 Markdown 标记；其中汉字约 9.5 万）。

### 已知缺口（已如实标注，不伪造成完整译文）
5 篇原文因离线缓存为 JS 动态渲染 / 访问码 / 被墙占位页而**正文缺失或极短**，译文以「⚠️ 已知缺口」如实标注：

| 缺口篇 | 原文词数 | 是否计入可译篇 |
|---|---|---|
| `lessons-from-ai-code-reviews` | 0 | 否（低正文占位，计入排除） |
| `good-context-good-code` | 13 | 否（低正文占位，计入排除） |
| `how-warp-uses-warp` | 14 | 否（低正文占位，计入排除） |
| `peeking-under-the-hood-of-claude-code` | 37 | 是（低正文，仍产出占位译文并标注） |
| `prompt-engineering-guide` | 208 | 是（低正文，仍产出占位译文并标注） |

> 备注：课程主页 `index` 已抽取但按计划未列入翻译工作单（跳过）。

### 缺口如何手动补齐（评审建议落地）
这 5 篇原文是 JS 动态渲染 / Notion / Medium 被墙页，离线缓存里没有正文。不翻墙前提下已尝试 Wayback Machine（`web.archive.org`）直连超时，无法自动补。未来若有合法可达途径，按此即可补齐：

| 缺口篇 | 补齐方式 |
|---|---|
| `good-context-good-code` | 原文 blog.stockapp.com 为 JS 渲染；用带 JS 渲染的抓取（`playwright` 打开后取 `document.body.innerText`），或 Wayback Machine `http://web.archive.org/web/*/blog.stockapp.com/good-context-good-code/` |
| `how-warp-uses-warp` | 原文是 Notion 公开页；用 Playwright 等待 `Notion加载完成` 后导出，或 Wayback 存档 |
| `peeking-under-the-hood-of-claude-code` | Medium 被墙；用 Wayback `web.archive.org/web/*/medium.com/@outsightai/peeking-under-the-hood*` 取存档正文 |
| `prompt-engineering-guide` | 仅抓到 208 词目录；`promptingguide.ai/techniques` 整页重抓即可补全 |
| `lessons-from-ai-code-reviews` | 离线包内无此篇正文、无来源 URL；需先在课程大纲里定位原始链接再补抓 |

补齐后把正文放进 `01_sources/html/<slug>.md`，重跑 `02_make_workorders.py` → 翻译 → `03/04/05` 三个闸门即可，管线已支持增量。

### 翻译"跳过规则"说明（针对"跳过是否过宽"的自查）
译文并非全部中文化，以下内容**按规则刻意保留英文/原文**，不是漏译：
1. **代码块与行内代码**：bash/Python/YAML/命令、函数名（`createMcpHandler()` 等）——全包被代码块跳过约 6,132 字符，均为示例，按规则保留；
2. **示例 prompt**：文章里给读者的示例输入（如 "Split this file into separate modules..."），保留原文才可读；
3. **专名与产品名**：Claude Code / Warp / MCP / OWASP / CWE / GitHub 等，按术语表保留；
4. **URL、路径、版本号**：不翻译。
> 经 `06_detail_check.py` 自查：全包译文 **HTML 结构残留 0 处**；汉字占比最低的几篇（mcp-server-authentication 27% 等）低占比均来自上述代码/标识符保留，正文叙述已全部中译，非漏译。

## 四、翻译流程（可复跑）

```
01_extract.py         抽取 31 篇 HTML → 干净 Markdown；3 份 PDF → 文本（01_sources/）
02_make_workorders.py 从 source_map 生成 34 篇翻译工作单 + 批次 + 状态（03_translations/manifest.json）
03_check_glossary.py  术语一致性质量闸门 → 05_quality/glossary_check_report.json（0 疑点）
04_coverage.py        覆盖度统计 → 05_quality/coverage_report.json（100%）
05_qa_sample.py       译文质量抽检（汉字总量 / 疑似占位篇 / 残留英文长句）→ 05_quality/qa_sample_report.json
06_detail_check.py    汉字占比 / HTML 结构残留 / 代码块跳过量自查（命令行输出）
```

**可复跑 / 换源**：4 条脚本均用**基于自身位置（`__file__`）的相对路径**定位工作根目录，不依赖任何写死的绝对路径——任意机器、任意目录下直接运行即可，无需改配置。换新课程时，更新 `01_sources/source_map.json` 后重跑脚本即出新包。

**环境依赖**：Python 3 + 标准库；`01_extract.py` 的 PDF 抽取额外依赖 **PyMuPDF（`pymupdf`）**（`pip install pymupdf`）。

**译文规则**（已获你确认）：纯中文译文；示例 prompt / 代码 / 命令保留英文原文；专名（Claude Code / Warp / MCP / GitHub 等）中文并列首次出现后保留英文；剔除营销噪音；文末加「翻译说明」交代省略内容。

## 五、使用方法

1. **看译文**：打开 `03_translations/`，每篇 `<slug>.zh.md` 对应一篇原文，文末有「翻译说明」交代省略。
2. **查术语**：`02_glossary/glossary.md` 全文统一译法，译文中英文词可对照。
3. **核对质量**：`05_quality/` 两个报告给出术语一致性（0 疑点）与覆盖度（100%）。
4. **重跑管线**（可选，任意位置均可，脚本自动定位工作根）：
   ```powershell
   python 04_pipeline\02_make_workorders.py
   python 04_pipeline\03_check_glossary.py
   python 04_pipeline\04_coverage.py
   python 04_pipeline\05_qa_sample.py
   ```

## 六、发布（不翻墙）

**推荐本地 zip 交付**（`C1-CS146S-中文翻译包.zip`，即本交付包自身；解压即完整交付目录，不再另设 `07_release/`），完全满足"可复用发布"要求；GitHub 发布为可选加分项，仅给手动步骤、不强制、不需要翻墙。详见 `06_deliverables/发布步骤.md`。

## 七、不翻墙说明

本挑战全程**零依赖翻墙**：资料获取使用你提供的离线缓存；校验用本地哈希；翻译、术语、质检、打包全部在本地完成；发布走本地 zip。也正因如此，5 篇无法离线抓取的页面被如实列为「已知缺口」，而非用非法手段抓取。

---
*挑战 C1 交付包 · 2026-09-25*
