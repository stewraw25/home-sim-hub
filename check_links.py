import re,os,sys,urllib.request,html,json
ROOT="docs"; BP="/home-sim-hub"; errs=[]; ext=set(); pages=0
for dp,_,fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".html"): continue
        pages+=1; p=os.path.join(dp,f); s=open(p).read()
        if 'name="robots" content="noindex' not in s: errs.append(("no noindex",p))
        if "As an Amazon Associate" not in s: errs.append(("no disclosure",p))
        for m in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>',s):
            tag,href=m.group(0),m.group(1)
            if "amazon.co.uk/dp/" in href:
                if "tag=stewraw25-21" not in href: errs.append(("bad tag",p,href))
                if 'rel="sponsored nofollow' not in tag: errs.append(("no rel",p,href))
                ext.add(href)
            elif href.startswith(BP):
                path=href[len(BP):].split("#")[0]
                t=os.path.join(ROOT,path.lstrip("/"))
                if path.endswith("/"): t=os.path.join(t,"index.html")
                if not os.path.exists(t): errs.append(("broken internal",p,href))
            elif href.startswith("http"): ext.add(href)
            else: errs.append(("relative/odd",p,href))
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s): json.loads(m.group(1))
        if re.search(r'(?i)"@type": ?"(Review|AggregateRating)"',s): errs.append(("review schema",p))
        if s.count("<h1")!=1: errs.append(("h1 count",p))
print("pages",pages,"external links",len(ext)); print("\n".join(map(str,errs)) or "NO ERRORS")
