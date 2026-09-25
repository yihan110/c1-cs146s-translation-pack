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
| 拿说明 | `06_deliverables/拿说明1-术语表定稿.md` 等 3 个 | 三个关键产出的「怎么做出来」演示 |
| 发布步骤 | `06_deliverables/发布步骤.md` | 本地 zip / GitHub 发布说明（不翻墙、可选） |
| 质量报告 | `05_quality/*.json` | 术语一致性检查 + 覆盖度统计 |

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

## 四、翻译流程（可复跑）

```
01_extract.py         抽取 31 篇 HTML → 干净 Markdown；3 份 PDF → 文本（01_sources/）
02_make_workorders.py 从 source_map 生成 34 篇翻译工作单 + 批次 + 状态（03_translations/manifest.json）
03_check_glossary.py  术语一致性质量闸门 → 05_quality/glossary_check_report.json（0 疑点）
04_coverage.py        覆盖度统计 → 05_quality/coverage_report.json（100%）
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
   ```

## 六、发布（不翻墙）

**推荐本地 zip 交付**（`C1-CS146S-中文翻译包.zip`，即本交付包自身；解压即完整交付目录，不再另设 `07_release/`），完全满足"可复用发布"要求；GitHub 发布为可选加分项，仅给手动步骤、不强制、不需要翻墙。详见 `06_deliverables/发布步骤.md`。

## 七、不翻墙说明

本挑战全程**零依赖翻墙**：资料获取使用你提供的离线缓存；校验用本地哈希；翻译、术语、质检、打包全部在本地完成；发布走本地 zip。也正因如此，5 篇无法离线抓取的页面被如实列为「已知缺口」，而非用非法手段抓取。

---
*挑战 C1 交付包 · 2026-09-25*
