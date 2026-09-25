# -*- coding: utf-8 -*-
"""翻译质量抽检：逐篇计算 中文字符数 / 英文残留句 / 可疑漏译。
只读，产出 05_quality/qa_sample_report.json。"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "01_sources", "html")
PDFSRC = os.path.join(ROOT, "01_sources", "pdf")
ZH = os.path.join(ROOT, "03_translations")
MANIFEST = os.path.join(ZH, "manifest.json")

def cjk_count(text):
    return len(re.findall(r'[\u4e00-\u9fff]', text))

def english_sentences(text):
    # 去掉代码块/行内代码
    t = re.sub(r'```[\s\S]*?```', ' ', text)
    t = re.sub(r'`[^`]*`', ' ', t)
    # 找连续英文单词组成的句子（>6个词）
    sents = re.findall(r'([A-Z][a-z]+(?:\s+[A-Za-z][a-z]+){6,}[.!?])', t)
    return sents

rows = []
for zh_path in sorted(glob.glob(os.path.join(ZH, "*.zh.md"))):
    slug = os.path.basename(zh_path).replace(".zh.md", "")
    text = open(zh_path, encoding="utf-8").read()
    cjk = cjk_count(text)
    en_long = english_sentences(text)
    rows.append({
        "slug": slug,
        "zh_chars": len(text),
        "cjk_chars": cjk,
        "long_en_sentences_in_zh": en_long,
    })

# 找 CJK 极少但文件不小的（可能是占位/漏译）
low = [r for r in rows if r["cjk_chars"] < 200 and r["zh_chars"] > 200]
# 找译文中残留长英文句（疑似漏译）
leak = [{"slug": r["slug"], "samples": r["long_en_sentences_in_zh"][:5]} for r in rows if len(r["long_en_sentences_in_zh"]) > 3]

report = {
    "n_files": len(rows),
    "total_cjk": sum(r["cjk_chars"] for r in rows),
    "low_cjk_files": low,
    "files_with_residual_english_sentences": leak,
}
out = os.path.join(ROOT, "05_quality", "qa_sample_report.json")
json.dump(report, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps(report, ensure_ascii=False, indent=2))
