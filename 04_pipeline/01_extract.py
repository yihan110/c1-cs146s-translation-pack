# -*- coding: utf-8 -*-
"""C1 阶段1: 抽取归档
1) 将 CS146S_offline/pages/*.html 正文抽成干净 Markdown -> 01_sources/html/
2) 将 CS146S_offline/pdfs/*.pdf 文本抽成 .txt -> 01_sources/pdf/
3) 生成 source_map.json (原文slug <-> 来源URL <-> 本地文件)
可复跑：输入不变即可重复生成。
"""
import os, re, json
from html.parser import HTMLParser
from urllib.parse import unquote

# 相对路径：无论脚本放在哪（<交付包根>/04_pipeline/），都能定位到工作根目录
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "materials", "CS146S_offline")
OUT_HTML = os.path.join(BASE, "01_sources", "html")
OUT_PDF = os.path.join(BASE, "01_sources", "pdf")
OUT_MAP = os.path.join(BASE, "01_sources", "source_map.json")

# 噪音文本/元素（导航、页脚、分享按钮等），按小写匹配
NOISE_LO = ["cookie", "privacy policy", "accept all", "sign in", "sign up", "subscribe to",
            "newsletter", "share", "twitter", "linkedin", "facebook", "table of contents",
            "skip to content", "get started free", "request a demo", "all rights reserved"]

class MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.in_pre = 0
        self.skip = 0
        self.title = ""
        self.in_title = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class","") + " " + a.get("id","")).lower()
        if tag in ("script","style","nav","footer","header","form","aside","button"):
            self.skip += 1
        elif tag in ("h1","h2","h3","h4","h5","h6"):
            self.out.append("\n" + "#"*int(tag[1]) + " ")
        elif tag == "pre":
            self.in_pre += 1
            self.out.append("\n```\n")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "br":
            self.out.append("\n")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag == "tr":
            self.out.append("\n| ")
        elif tag == "td" or tag == "th":
            self.out.append(" | ")
        if tag == "title":
            self.in_title += 1
    def handle_endtag(self, tag):
        if tag in ("script","style","nav","footer","header","form","aside","button"):
            self.skip = max(0, self.skip-1)
        elif tag == "pre":
            self.in_pre = max(0, self.in_pre-1)
            self.out.append("\n```\n")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4" or tag == "h5" or tag == "h6":
            self.out.append("\n")
        elif tag == "title":
            self.in_title = max(0, self.in_title-1)
    def handle_data(self, data):
        if self.skip:
            return
        if self.in_title:
            self.title += data
            return
        self.out.append(data)

def clean(text):
    # 折叠多余空白，合并行内碎片
    lines = [ln.strip() for ln in text.split("\n")]
    buf = []
    for ln in lines:
        if not ln:
            if buf and buf[-1] != "":
                buf.append("")
        else:
            buf.append(ln)
    # 去掉首尾空行
    while buf and buf[0] == "":
        buf.pop(0)
    while buf and buf[-1] == "":
        buf.pop()
    return "\n".join(buf)

def html_to_md(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        raw = f.read()
    # 仅取 body 部分
    m = re.search(r"<body[\s>]", raw)
    if m:
        raw = raw[m.start():]
        e = raw.rfind("</body>")
        if e != -1:
            raw = raw[:e]
    p = MD()
    p.feed(raw)
    text = "".join(p.out)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # 噪音行过滤
    lines = text.split("\n")
    keep = []
    for ln in lines:
        low = ln.lower().strip()
        if len(low) < 3:
            keep.append(ln); continue
        if any(n in low for n in NOISE_LO) and len(low) < 80:
            continue
        keep.append(ln)
    return clean("\n".join(keep)), p.title.strip()

def main():
    os.makedirs(OUT_HTML, exist_ok=True)
    os.makedirs(OUT_PDF, exist_ok=True)
    # source_map 基础
    map_url = {}
    pm = os.path.join(SRC, "page_map.json")
    if os.path.exists(pm):
        with open(pm, "r", encoding="utf-8") as f:
            map_url = json.load(f)  # url -> slug.html
    smap = {}
    total_words = 0
    report = []
    for f in sorted(os.listdir(os.path.join(SRC, "pages"))):
        if not f.endswith(".html"):
            continue
        slug = f[:-5]
        md, title = html_to_md(os.path.join(SRC, "pages", f))
        out = os.path.join(OUT_HTML, slug + ".md")
        with open(out, "w", encoding="utf-8") as w:
            w.write(md)
        words = len(md.split())
        total_words += words
        url = next((u for u,s in map_url.items() if s == f), "")
        smap[slug] = {"local_html": f, "md": os.path.join("01_sources","html",slug+".md"), "source_url": url, "words": words}
        report.append((slug, words, bool(url)))
    # PDF
    pdf_report = []
    for f in sorted(os.listdir(os.path.join(SRC, "pdfs"))):
        if not f.endswith(".pdf"):
            continue
        import pymupdf
        doc = pymupdf.open(os.path.join(SRC, "pdfs", f))
        text = "\n\n".join("== page %d ==\n%s" % (i+1, pg.get_text()) for i,pg in enumerate(doc))
        slug = f[:-4]
        out = os.path.join(OUT_PDF, slug + ".txt")
        with open(out, "w", encoding="utf-8") as w:
            w.write(text)
        smap[slug] = {"local_pdf": f, "txt": os.path.join("01_sources","pdf",slug+".txt"), "source_url": "", "words": len(text.split()), "pdf": True}
        pdf_report.append((slug, doc.page_count, len(text.split())))
    with open(OUT_MAP, "w", encoding="utf-8") as w:
        json.dump(smap, w, ensure_ascii=False, indent=2)
    print("HTML files:", len(smap) - len(pdf_report), "| total words:", total_words)
    for r in report:
        print("  ", r)
    print("PDF:")
    for r in pdf_report:
        print("  ", r)

if __name__ == "__main__":
    main()
