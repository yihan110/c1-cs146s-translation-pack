# -*- coding: utf-8 -*-
"""细查：1) 每篇汉字占比 2) HTML/结构残留 3) 被代码块跳过的段数。"""
import os, re, glob, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(ROOT, "03_translations")

rows = []
for p in sorted(glob.glob(os.path.join(ZH, "*.zh.md"))):
    text = open(p, encoding="utf-8").read()
    cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
    total = len(re.sub(r'\s', '', text))
    ratio = round(cjk / total * 100, 1) if total else 0
    # HTML 残留
    html_tags = re.findall(r'<(div|span|p|img|ul|li|table|br|a|h\d)[\s>]', text)
    # 代码块数量（被跳过的内容）
    code_blocks = len(re.findall(r'```', text)) // 2
    code_chars = sum(len(b) for b in re.findall(r'```[\s\S]*?```', text))
    rows.append({
        "slug": os.path.basename(p).replace(".zh.md",""),
        "cjk_ratio_pct": ratio,
        "cjk": cjk,
        "html_residue": len(html_tags),
        "code_blocks_skipped": code_blocks,
        "code_chars_skipped": code_chars,
    })

low_ratio = sorted([r for r in rows if r["cjk_ratio_pct"] < 50], key=lambda x: x["cjk_ratio_pct"])
html_issues = [r for r in rows if r["html_residue"] > 0]
total_skipped = sum(r["code_chars_skipped"] for r in rows)

print("=== 汉字占比最低的 8 篇 ===")
for r in low_ratio[:8]:
    print(f'  {r["slug"]:42s} 汉字占比 {r["cjk_ratio_pct"]}%  汉字{r["cjk"]}  HTML残留{r["html_residue"]}  代码块{r["code_blocks_skipped"]}段')
print("\n=== 有 HTML 结构残留的篇 ===")
for r in html_issues:
    print(f'  {r["slug"]:42s} HTML标签 {r["html_residue"]} 处')
print(f"\n全包被代码块跳过字符合计: {total_skipped}")
print(f"全包 HTML 残留标签合计: {sum(r['html_residue'] for r in rows)}")
