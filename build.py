#!/usr/bin/env python3
"""Static site builder for Home Sim Hub.
Going live = edit config.json (base_url, noindex) then run: python3 build.py
"""
import json, re, os, shutil, html
from urllib.parse import urlparse
from xml.sax.saxutils import escape as xesc
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
CFG = json.load(open(os.path.join(ROOT, "config.json")))
SECTIONS = json.load(open(os.path.join(ROOT, "sections.json")))
PRODUCTS = {p["slug"]: p for p in json.load(open(os.path.join(ROOT, "data", "products.json")))}
import importlib.util
spec = importlib.util.spec_from_file_location("pages", os.path.join(ROOT, "content", "pages.py"))
pages_mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(pages_mod)
PAGES = pages_mod.PAGES

BASE_URL = CFG["base_url"].rstrip("/")
BASE_PATH = urlparse(BASE_URL).path.rstrip("/")
TAG = CFG["amazon_tag"]
NAME = CFG["site_name"]
BLOCK = re.compile(r"(?i)\b(best|perfect|ultimate|unbeatable|unrivall?ed|ideal|revolutionary|world.?class|unmatched|incredible|amazing|top.?notch|must.?have|superior|finest|greatest|guarantee\w*|premium|no.?compromise|precision accuracy|excellent|rock.?solid|spares no expense|complete confidence|elite sim racer|exceptional|top.?tier|top choice|high.?quality|effortless|transformative)\b")

def u(path):  # internal URL
    return BASE_PATH + path
def full(path):
    return BASE_URL + path
def amz(asin):
    return f"https://www.amazon.co.uk/dp/{asin}?tag={TAG}"
def esc(s): return html.escape(s, quote=True)

def price_text(p):
    return f"£{p['price']} when we checked on {CFG['price_checked']}. Prices change often, so check Amazon for the current price."

def product_card(slug):
    p = PRODUCTS[slug]
    bullets = [b for b in p["bullets"] if not BLOCK.search(b)][:3]
    lis = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    facts = "; ".join(f"{esc(k)}: {esc(v)}" for k, v in p["facts"].items() if not BLOCK.search(v))
    notes = "".join(f'<p class="note">{esc(n)}</p>' for n in p["notes"])
    return (f'<div class="product" id="{slug}"><h3>{esc(p["name"])}</h3>'
            f'<p class="small">Amazon UK listing: {esc(p["title"][:140])} (ASIN {p["asin"]})</p>'
            f'<p class="price">{price_text(p)}</p>'
            + (f'<p class="small">What the Amazon listing says:</p><ul>{lis}</ul>' if lis else "")
            + (f'<p class="facts">Listing details: {facts}</p>' if facts else "") + notes +
            f'<a class="btn" href="{amz(p["asin"])}" rel="sponsored nofollow noopener" target="_blank">Check price on Amazon</a></div>')

def render(body):
    body = re.sub(r"\[\[p:([\w-]+)\]\]", lambda m: product_card(m.group(1)), body)
    body = re.sub(r"\[\[buy:([\w-]+)\|([^\]]+)\]\]", lambda m: f'<a href="{amz(PRODUCTS[m.group(1)]["asin"])}" rel="sponsored nofollow noopener" target="_blank">{m.group(2)}</a>', body)
    body = re.sub(r"\[\[price:([\w-]+)\]\]", lambda m: f"£{PRODUCTS[m.group(1)]['price']}", body)
    body = re.sub(r"\[\[link:([^|\]]+)\|([^\]]+)\]\]", lambda m: f'<a href="{u(m.group(1))}">{m.group(2)}</a>', body)
    body = body.replace("[[checked]]", CFG["price_checked"]).replace("[[BP]]", BASE_PATH)
    body = re.sub(r'(?<![">=/])(https?://[^\s<]+[^\s<.,)])', lambda m: f'<a href="{m.group(1)}" rel="noopener" target="_blank">{m.group(1)}</a>', body)
    body = body.replace("<th>", '<th scope="col">')
    return body

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="7" fill="#1f6b4a"/>'
        '<path d="M7 22h18" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
        '<path d="M9 22V12l7-4 7 4v10" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round"/>'
        '<circle cx="16" cy="17" r="2.4" fill="#fff"/></svg>')

DISC_SHORT = (f'As an Amazon Associate, {NAME} earns from qualifying purchases. Links to Amazon on this page are affiliate links. '
              f'<a href="{{dl}}">How this works</a>.')

def layout(pg, body):
    path = pg["path"]
    title = pg["title"] if path == "/" else f'{pg["title"]} | {NAME}'
    if len(title) > 70: title = pg["title"]
    desc = pg["description"]
    robots = '<meta name="robots" content="noindex, nofollow">' if CFG["noindex"] else '<meta name="robots" content="index, follow">'
    live = [s for s in SECTIONS if s["live"]]
    def cur(p): return ' aria-current="page"' if path.startswith(p) and p != "/" else ""
    nav = "".join(f'<a href="{u(s["path"])}"{cur(s["path"])}>{esc(s["name"])}</a>' for s in live)
    nav += f'<a href="{u("/about/")}"{cur("/about/")}>About</a>'
    crumbs = pg.get("crumbs", [])
    crumb_html = ""
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": full("/"), "logo": full("/logo.png")},
        {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": full("/"), "inLanguage": "en-GB"},
    ]
    if path != "/":
        items = [("Home", "/")] + crumbs + [(pg.get("short", pg["title"]), path)]
        crumb_html = '<p class="crumbs">' + " › ".join(
            (f'<a href="{u(p)}">{esc(n)}</a>' if i < len(items) - 1 else esc(n)) for i, (n, p) in enumerate(items)) + "</p>"
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": full(p)} for i, (n, p) in enumerate(items)]})
    if pg.get("type") == "article":
        ld.append({"@context": "https://schema.org", "@type": "Article", "headline": pg["title"], "description": desc,
                   "datePublished": CFG["published"], "dateModified": CFG["updated"], "inLanguage": "en-GB",
                   "author": {"@type": "Organization", "name": NAME, "url": full("/")},
                   "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": full("/logo.png")}},
                   "mainEntityOfPage": full(path), "image": full("/og.png")})
    ldjson = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    has_links = "amazon.co.uk/dp/" in body or pg.get("disclosure", True)
    disc = f'<div class="disc-bar"><div class="wrap">{DISC_SHORT.format(dl=u("/affiliate-disclosure/"))}</div></div>' if has_links else ""
    dated = f'<p class="meta">Updated {CFG["updated"]}. Researched from makers\' published documents and Amazon UK listings. We have not tested these products.</p>' if pg.get("type") == "article" else ""
    foot_nav = "".join(f'<a href="{u(p)}">{n}</a>' for n, p in [("About", "/about/"), ("Affiliate disclosure", "/affiliate-disclosure/"), ("Privacy", "/privacy/"), ("Contact", "/contact/")])
    return f'''<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">{robots}
<link rel="canonical" href="{full(path)}">
<meta property="og:type" content="{"article" if pg.get("type")=="article" else "website"}"><meta property="og:site_name" content="{esc(NAME)}">
<meta property="og:title" content="{esc(pg["title"])}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{full(path)}"><meta property="og:image" content="{full("/og.png")}"><meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{u("/favicon.svg")}" type="image/svg+xml"><link rel="stylesheet" href="{u("/style.css")}">
{ldjson}</head><body>
<header class="site"><div class="wrap"><a class="logo" href="{u("/")}">{LOGO}<span>{esc(NAME)}</span></a><nav class="main" aria-label="Main">{nav}</nav></div></header>
{disc}
<main><div class="wrap">{crumb_html}<article><h1>{esc(pg["h1"] if "h1" in pg else pg["title"])}</h1>{dated}{body}</article></div></main>
<footer class="site"><div class="wrap"><strong>{esc(NAME)}</strong> · {esc(CFG["tagline"])}<nav aria-label="Footer">{foot_nav}</nav>
<p>As an Amazon Associate, {esc(NAME)} earns from qualifying purchases. Prices and availability were checked on {CFG["price_checked"]} and can change at any time; the price on Amazon at the time of purchase applies. We research products from makers' published documents and Amazon UK listings and have not tested them ourselves.</p>
<p>Amazon and the Amazon logo are trademarks of Amazon.com, Inc. or its affiliates.</p></div></footer>
</body></html>'''

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in os.listdir(os.path.join(ROOT, "static")):
        shutil.copy(os.path.join(ROOT, "static", f), OUT)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    urls = []
    for pg in PAGES:
        body = render(pg["body"])
        m = BLOCK.search(re.sub(r"\[\[[^\]]*\]\]|<[^>]+>", " ", pg["body"]) + " " + pg["title"] + " " + pg["description"])
        assert not m, f"blocked word in {pg['path']}: {m.group(0) if m else ''}"
        doc = layout(pg, body)
        target = os.path.join(OUT, pg["path"].strip("/"), "index.html") if pg["path"] != "/404.html" else os.path.join(OUT, "404.html")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, "w").write(doc)
        if pg["path"] != "/404.html": urls.append(pg["path"])
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls: sm.append(f"<url><loc>{xesc(full(p))}</loc><lastmod>{CFG['updated']}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    if CFG["noindex"]:
        robots = "# Preview build: keep search engines out until the real domain is live.\nUser-agent: *\nDisallow: /\n"
    else:
        robots = f"User-agent: *\nAllow: /\n\nSitemap: {full('/sitemap.xml')}\n"
    open(os.path.join(OUT, "robots.txt"), "w").write(robots)
    if CFG.get("custom_domain") and not CFG["noindex"]:
        open(os.path.join(OUT, "CNAME"), "w").write(CFG["custom_domain"] + "\n")
    print(f"Built {len(urls)} pages into docs/ (noindex={CFG['noindex']}, base={BASE_URL})")

if __name__ == "__main__":
    main()
