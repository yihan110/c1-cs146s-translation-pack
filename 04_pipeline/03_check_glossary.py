# -*- coding: utf-8 -*-
"""C1 阶段3-管线: 术语一致性检查 (quality gate 1)
扫描 03_translations 下已翻译文件，检查关键英文原词是否按术语表处理：
  - 需要"中文化"的术语：译文里应出现定稿中文（英文原词可保留/中英并列）
  - 需要"保留英文"的术语：译文里应保留英文原词
产出: 05_quality/glossary_check_report.json + 控制台摘要
"""
import os, json, re, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(BASE, "03_translations", "manifest.json")
OUT_REPORT = os.path.join(BASE, "05_quality", "glossary_check_report.json")

# 关键抽查词条: (英文原词, 期望出现的中文, 模式)  模式: zh(应含中文)/keep(应保留英文)
KEY_TERMS = [
    ("LLM", "大语言模型", "zh"),
    ("prompt", "提示", "zh"),
    ("prompt engineering", "提示词工程", "zh"),
    ("agent", "智能体", "zh"),
    ("coding agent", "编码智能体", "zh"),
    ("agentic", "智能体驱动", "zh"),
    ("scaffolding", "脚手架", "zh"),
    ("context window", "上下文窗口", "zh"),
    ("context rot", "上下文腐化", "zh"),
    ("MCP", "MCP", "keep"),
    ("Model Context Protocol", "模型上下文协议", "zh"),
    ("function calling", "函数调用", "zh"),
    ("code review", "代码评审", "zh"),
    ("prompt injection", "提示注入", "zh"),
    ("remote code execution", "远程代码执行", "zh"),
    ("observability", "可观测性", "zh"),
    ("on-call", "值班", "zh"),
    ("site reliability engineering", "站点可靠性工程", "zh"),
    ("fine-tuning", "微调", "zh"),
    ("hallucination", "幻觉", "zh"),
    ("sandbox", "沙箱", "zh"),
    ("vulnerability", "漏洞", "zh"),
    ("Claude Code", "Claude Code", "keep"),
    ("Warp", "Warp", "keep"),
    ("GitHub", "GitHub", "keep"),
    ("Kubernetes", "Kubernetes", "keep"),
]

def main():
    with open(MANIFEST, "r", encoding="utf-8") as f:
        mf = json.load(f)
    def _abs(p):
        """清单里存的是包内相对路径；统一按工作根解析，换机器/换目录都能跑。"""
        if not p:
            return ""
        return p if os.path.isabs(p) else os.path.join(BASE, p.replace("/", os.sep))

    report = {}
    checked = 0
    skipped_low = skipped_missing = 0
    for item in mf["items"]:
        zh = _abs(item.get("zh", ""))
        # 缺口占位篇（JS渲染/访问码致原文几乎无正文，source_words<30）跳过术语检查
        if item.get("source_words", 0) < 30:
            skipped_low += 1
            continue
        if not zh or not os.path.exists(zh):
            skipped_missing += 1
            continue
        text = open(zh, "r", encoding="utf-8", errors="ignore").read().lower()
        src = _abs(item.get("source", ""))
        src_text = open(src, "r", encoding="utf-8", errors="ignore").read().lower() if src and os.path.exists(src) else ""
        checked += 1
        issues = []
        for en, cn, mode in KEY_TERMS:
            en_in_src = re.search(r"\b" + re.escape(en) + r"\b", src_text) if src_text else True
            if not en_in_src:
                continue  # 原文根本没出现该词，无需要求译文
            if mode == "zh":
                # 原文有该英文词，但译文没出现对应中文 -> 疑似漏译/未统一
                if re.search(r"\b" + re.escape(en) + r"\b", text) and cn.lower() not in text:
                    issues.append({"term": en, "expect": cn, "type": "missing_zh"})
            else:
                if cn.lower() not in text:
                    issues.append({"term": en, "expect": cn, "type": "missing_keep"})
        report[item["slug"]] = issues
    if checked == 0:
        raise SystemExit(
            "术语检查失败：已检查 0 篇（低正文跳过 %d 篇 / 译文缺失跳过 %d 篇）。"
            "换机器或换目录后已检查篇数不应为 0，请先核对 manifest.json 内 zh 路径是否可用。"
            % (skipped_low, skipped_missing)
        )
    if skipped_missing:
        print("警告：有 %d 篇译文文件缺失，未计入检查，请核对 manifest.json 的 zh 路径。" % skipped_missing)
    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    n_clean = sum(1 for v in report.values() if not v)
    print("已检查:", checked, "篇 | 无问题:", n_clean, "篇 | 有疑点:", checked - n_clean, "篇")
    for slug, issues in report.items():
        if issues:
            print("  [%s] %d 处疑点: %s" % (slug, len(issues), "; ".join(i['term'] for i in issues[:6])))

if __name__ == "__main__":
    main()
