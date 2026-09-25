# materials/ —— 离线原始资料（**本翻译包内不含**）

本交付包发布的是**翻译成果 + 可复跑管线**，不附带课程原始资料（版权/授权原因，原始资料由作者本人在本地自备）。

## 复跑第 1 步前需要准备什么

把离线资料按下面的结构放好，`04_pipeline/01_extract.py` 才能运行：

```
materials/
├── CS146S_offline/            ← 离线缓存解压后的目录
│   ├── pages/*.html          ← 31 篇 HTML 讲义
│   └── pdfs/*.pdf            ← 3 份 PDF 讲义
└── Vibe_Coding_Playbook.pdf   ← 中文原创学习册（背景资料，本身是中文，无需翻译）
```

- 输入来源与 SHA-256 前缀见根目录 `README.md` 第二节「来源与完整性」。
- 缺了本目录时，第 1 步会因找不到输入而失败——这是**预期行为**，不是包坏了。

## 不依赖原始资料即可复跑的部分

第 2–4 步只依赖包内已发布的 `01_sources/`（原文归档）与 `03_translations/`（译文），可直接运行：

```powershell
python 04_pipeline\02_make_workorders.py
python 04_pipeline\03_check_glossary.py
python 04_pipeline\04_coverage.py
```

预期输出：工作单 34 篇（跳过课程主页 `index`）｜术语闸门「已检查 31 篇、0 疑点、跳过 3 篇（正文 <30 词）」｜覆盖度 31/31 = 100%。
