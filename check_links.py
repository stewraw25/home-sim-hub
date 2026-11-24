#!/usr/bin/env python3
"""SEO, HTML5 DOM, affiliate-compliance, schema, and link checker for docs/."""
import html, json, os, re
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = "docs"
CFG = json.load(open("config.json"))
BASE_URL = CFG["base_url"].rstrip("/")
BP = urlparse(BASE_URL).path.rstrip("/")
TAG = CFG["amazon_tag"]
VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

class DOMAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.ids, self.dups, self.mismatch = [], set(), [], []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            if d["id"] in self.ids:
                self.dups.append(d["id"])
            self.ids.add(d["id"])
        if tag not in VOID:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.mismatch.append(tag)

errs, ext, pages, titles, descs = [], set(), 0, {}, {}

for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".html"):
            continue
        pages += 1
        p = os.path.join(dp, f)
        s = open(p).read()

        # DOM balance & duplicate IDs
        dom = DOMAudit()
        dom.feed(s)
        if dom.dups or dom.mismatch or dom.stack:
            errs.append(("dom error", p, dom.dups, dom.mismatch, dom.stack))

        # Robots check
        if CFG["noindex"]:
            if 'name="robots" content="noindex, nofollow"' not in s:
                errs.append(("no noindex", p))
        else:
            if 'name="robots" content="index, follow"' not in s:
                errs.append(("no index meta", p))

        if "As an Amazon Associate" not in s:
            errs.append(("no disclosure", p))

        # H1 count & sequential heading order
        if s.count("<h1") != 1:
            errs.append(("h1 count", p, s.count("<h1")))
        hs = [int(x) for x in re.findall(r"<h([1-6])\b", s)]
        prev = 0
        for lvl in hs:
            if prev and lvl > prev + 1:
                errs.append(("heading skip", p, hs))
                break
            prev = lvl

        # Title uniqueness & length
        tm = re.search(r"<title>(.*?)</title>", s)
        if not tm:
            errs.append(("missing title", p))
        else:
            t = html.unescape(tm.group(1))
            if len(t) > 70:
                errs.append(("title > 70", p, len(t), t))
            if t in titles:
                errs.append(("duplicate title", p, titles[t]))
            titles[t] = p

        # Meta description uniqueness & length
        dm = re.search(r'<meta name="description" content="([^"]*)"', s)
        if not dm:
            errs.append(("missing description", p))
        else:
            d = html.unescape(dm.group(1))
            if not (40 <= len(d) <= 170):
                errs.append(("desc length", p, len(d)))
            if d in descs:
                errs.append(("duplicate desc", p, descs[d]))
            descs[d] = p

        # Canonical check
        cm = re.search(r'<link rel="canonical" href="([^"]+)"', s)
        if not cm or not cm.group(1).startswith(BASE_URL):
            errs.append(("bad canonical", p, cm.group(1) if cm else None))

        # Image alt text & th scope
        for im in re.finditer(r"<img\b([^>]*)>", s):
            if not re.search(r'\balt="[^"]+"', im.group(1)):
                errs.append(("missing img alt", p, im.group(0)))
        for th in re.finditer(r"<th\b([^>]*)>", s):
            if 'scope="' not in th.group(1):
                errs.append(("th missing scope", p, th.group(0)))

        # Links & anchors
        for m in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>', s):
            tag, href = m.group(0), m.group(1)
            if 'target="_blank"' in tag and "noopener" not in tag:
                errs.append(("missing noopener", p, href))
            if "amazon.co.uk/dp/" in href:
                if f"tag={TAG}" not in href:
                    errs.append(("bad tag", p, href))
                if 'rel="sponsored nofollow' not in tag:
                    errs.append(("no rel", p, href))
                ext.add(href)
            elif href.startswith("#"):
                aid = href[1:]
                if f'id="{aid}"' not in s:
                    errs.append(("broken local anchor", p, href))
            elif (BP and href.startswith(BP)) or (not BP and href.startswith("/")):
                rel_path = href[len(BP):] if BP else href
                path_part, _, frag = rel_path.partition("#")
                t = os.path.join(ROOT, path_part.lstrip("/"))
                if path_part.endswith("/") or path_part == "":
                    t = os.path.join(t, "index.html")
                if not os.path.exists(t):
                    errs.append(("broken internal", p, href))
                elif frag and f'id="{frag}"' not in open(t).read():
                    errs.append(("broken internal anchor", p, href))
            elif href.startswith("http"):
                ext.add(href)
            else:
                errs.append(("relative/odd", p, href))

        # JSON-LD check
        ld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s)
        if not ld_blocks:
            errs.append(("missing json-ld", p))
        for raw_ld in ld_blocks:
            obj = json.loads(raw_ld)
            if "@context" not in obj or "@type" not in obj:
                errs.append(("bad json-ld keys", p, obj))
        if re.search(r'(?i)"@type": ?"(Review|AggregateRating)"', s):
            errs.append(("review schema", p))

print(f"Checked {pages} HTML pages, {len(ext)} unique external links, {len(titles)} unique titles")
print("\n".join(map(str, errs)) or "NO ERRORS")
raise SystemExit(1 if errs else 0)
