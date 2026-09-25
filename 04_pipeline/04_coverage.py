# -*- coding: utf-8 -*-
"""C1 阶段3-管线: 覆盖度统计 (quality gate 2)
统计已翻译中文篇幅 vs 原文篇幅，判断覆盖是否 >=80%。
产出: 05_quality/coverage_report.json + 控制台摘要
"""
import os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(BASE, "03_translations", "manifest.json")
OUT_REPORT = os.path.join(BASE, "05_quality", "coverage_report.json")

def main():
    with open(MANIFEST, "r", encoding="utf-8") as f:
        mf = json.load(f)
    rows = []
    total_src = total_zh = 0
    covered = pending = 0
    for item in mf["items"]:
        # 清单里存的是包内相对路径，统一按工作根解析（换机器/换目录都能跑）
        zh = item.get("zh", "")
        if zh and not os.path.isabs(zh):
            zh = os.path.join(BASE, zh.replace("/", os.sep))
        src_w = item.get("source_words", 0)
        if zh and os.path.exists(zh):
            zh_w = len(open(zh, "r", encoding="utf-8", errors="ignore").read())
            total_zh += zh_w
            covered += 1
        else:
            zh_w = 0
            pending += 1
        total_src += src_w
        # 无正文可译(JS渲染/占位)的单独计数
        skip = src_w < 30
        rows.append({"slug": item["slug"], "src_words": src_w, "zh_chars": zh_w, "translated": zh_w > 0, "skip_low_text": skip})
    n_translatable = sum(1 for r in rows if not r["skip_low_text"])
    n_done = sum(1 for r in rows if r["translated"] and not r["skip_low_text"])
    coverage = (n_done / n_translatable * 100) if n_translatable else 0
    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        json.dump({"rows": rows, "n_translatable": n_translatable, "n_done": n_done,
                   "coverage_percent": round(coverage, 1)}, f, ensure_ascii=False, indent=2)
    print("可译篇数(排除JS/占位):", n_translatable, "| 已完成:", n_done, "| 覆盖度: %.1f%%" % coverage)

if __name__ == "__main__":
    main()
