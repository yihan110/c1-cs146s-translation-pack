# -*- coding: utf-8 -*-
"""C1 阶段3-管线: 生成翻译工作单 (workorders)
可复跑: 从 source_map + 术语表 生成每篇的翻译任务清单与状态跟踪。
换源可复用: 换一门课的资料，更新 01_sources/source_map.json 后重跑本脚本即可。
产出: 03_translations/manifest.json (含 原文路径 / 译文路径 / 状态 / 词数 / 批次)
"""
import os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_MAP = os.path.join(BASE, "01_sources", "source_map.json")
GLOSS   = os.path.join(BASE, "02_glossary", "glossary.md")
OUT     = os.path.join(BASE, "03_translations")
MANIFEST= os.path.join(OUT, "manifest.json")

# 批次划分（按课程周/主题），用于分批发翻译
BATCHES = {
    "B1_主页与综述": ["index", "prompt-engineering-overview", "prompt-engineering-guide", "sre-introduction"],
    "B2_Prompt与LLM": [],
    "B3_智能体与工具": ["writing-effective-tools-for-agents", "devin-coding-agents-101", "good-context-good-code"],
    "B4_MCP": ["mcp-introduction", "mcp-server-authentication", "mcp-registry-preview", "mcp-food-for-thought"],
    "B5_上下文工程": ["context-rot", "how-long-contexts-fail", "specs-are-the-new-source-code"],
    "B6_Claude Code与终端": ["claude-code-best-practices", "warp-vs-claude-code", "how-warp-uses-warp", "peeking-under-the-hood-of-claude-code"],
    "B7_代码评审": ["code-reviews-just-do-it", "how-to-review-code-effectively", "code-review-essentials", "ai-code-review-best-practices", "lessons-from-ai-code-reviews"],
    "B8_安全": ["sast-vs-dast", "copilot-prompt-injection-rce", "finding-vulnerabilities-claude-codex", "agentic-ai-threats", "owasp-top-ten"],
    "B9_SRE与可观测": ["observability-basics", "kubernetes-troubleshooting-ai", "benefits-agentic-ai-oncall", "multi-agent-systems-ai-native"],
    "B10_PDF文档": ["how-openai-uses-codex", "how-anthropic-uses-claude-code", "ai-assisted-code-review-assessment"],
}

def main():
    with open(SRC_MAP, "r", encoding="utf-8") as f:
        smap = json.load(f)
    # 反向: 把文件归到批次
    slug_batch = {}
    for b, slugs in BATCHES.items():
        for s in slugs:
            slug_batch[s] = b
    # 未分组的自动归入"未分组"
    manifest = []
    for slug, info in smap.items():
        if slug == "index":
            continue
        src_rel = (info.get("md") or info.get("txt") or "").replace(os.sep, "/")
        is_pdf = "txt" in info
        # 清单里一律写"包内相对路径"，绝不把作者机器的绝对路径写进交付物
        # 统一译文后缀为 .zh.md（HTML 与 PDF 译文一致，便于统一质量闸门扫描）
        zh_name = slug + ".zh.md"
        zh_rel = "03_translations/" + zh_name
        zh_abs = os.path.join(OUT, zh_name)
        batch = slug_batch.get(slug, "未分组")
        status = "done" if os.path.exists(zh_abs) else "pending"
        manifest.append({
            "slug": slug,
            "batch": batch,
            "source": src_rel,
            "source_words": info.get("words", 0),
            "zh": zh_rel,
            "zh_rel": zh_rel,
            "status": status,
            "pdf": is_pdf,
        })
    # 自检：交付清单里不允许出现绝对路径
    leaks = [m["slug"] for m in manifest if os.path.isabs(m["source"]) or os.path.isabs(m["zh"])]
    if leaks:
        raise SystemExit("清单中检出绝对路径，已中止：%s" % leaks[:5])
    manifest.sort(key=lambda x: (list(BATCHES.keys()).index(x["batch"]) if x["batch"] in BATCHES else 999, x["slug"]))
    with open(MANIFEST, "w", encoding="utf-8") as f:
        glossary_rel = os.path.relpath(GLOSS, BASE).replace(os.sep, "/")
        json.dump({"glossary": glossary_rel, "items": manifest}, f, ensure_ascii=False, indent=2)
    done = sum(1 for m in manifest if m["status"]=="done")
    print("工作单已生成。总篇数:", len(manifest), "| 已翻译:", done, "| 待译:", len(manifest)-done)
    from collections import Counter
    for b, c in Counter(m["batch"] for m in manifest).items():
        print("  批次", b, ":", c, "篇")

if __name__ == "__main__":
    main()
