#!/usr/bin/env python3
"""Static site builder for Home Sim Hub (single-config rebrandable).
To swap brand name, wordmark or go-live domain: edit config.json then run:
  python3 build_assets.py && python3 build.py && python3 check_links.py
"""
import html, importlib.util, json, os, re, shutil
from urllib.parse import urlparse
from xml.sax.saxutils import escape as xesc

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "docs")
CFG = json.load(open(os.path.join(ROOT, "config.json")))
SECTIONS = json.load(open(os.path.join(ROOT, "sections.json")))
PRODUCTS = {p["slug"]: p for p in json.load(open(os.path.join(ROOT, "data", "products.json")))}

spec = importlib.util.spec_from_file_location("pages", os.path.join(ROOT, "content", "pages.py"))
pages_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages_mod)
PAGES = pages_mod.PAGES

BASE_URL = CFG["base_url"].rstrip("/")
BASE_PATH = urlparse(BASE_URL).path.rstrip("/")
TAG = CFG["amazon_tag"]
NAME = CFG["site_name"]
PARTS = CFG.get("brand_wordmark") or [NAME, ""]
P1 = PARTS[0]
P2 = PARTS[1] if len(PARTS) > 1 else ""

BLOCK = re.compile(
    r"(?i)\b(best|perfect|ultimate|unbeatable|unrivall?ed|ideal|revolutionary|world.?class|unmatched|incredible|amazing|top.?notch|must.?have|superior|finest|greatest|guarantee\w*|premium|no.?compromise|precision accuracy|excellent|rock.?solid|spares no expense|complete confidence|elite sim racer|exceptional|top.?tier|top choice|high.?quality|effortless|transformative)\b"
)

def u(path):
    if path.startswith("#"):
        return path
    return BASE_PATH + path

def full(path):
    return BASE_URL + path

def amz(asin):
    return f"https://www.amazon.co.uk/dp/{asin}?tag={TAG}"

def esc(s):
    return html.escape(s, quote=True)

def sub_brand(s):
    return s.replace("[[SITE_NAME]]", NAME)

def price_text(p):
    return f"£{p['price']} when we checked on {CFG['price_checked']}. Prices change often, so check Amazon for the current price."

def product_card(slug):
    p = PRODUCTS[slug]
    bullets = [b for b in p["bullets"] if not BLOCK.search(b)][:3]
    lis = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    facts = "; ".join(f"{esc(k)}: {esc(v)}" for k, v in p["facts"].items() if not BLOCK.search(v))
    notes = "".join(f'<p class="note">{esc(n)}</p>' for n in p["notes"])
    return (
        f'<div class="product" id="{slug}">'
        f'<div class="product-head"><h3>{esc(p["name"])}</h3><span class="price-pill">£{esc(p["price"])}</span></div>'
        f'<p class="small">Amazon UK listing: {esc(p["title"][:140])} (ASIN {p["asin"]})</p>'
        f'<p class="price">{price_text(p)}</p>'
        + (f'<p class="small">What the Amazon listing says:</p><ul>{lis}</ul>' if lis else "")
        + (f'<p class="facts">Listing details: {facts}</p>' if facts else "")
        + notes
        + f'<a class="btn" href="{amz(p["asin"])}" rel="sponsored nofollow noopener" target="_blank">Check price on Amazon &rarr;</a></div>'
    )

SVGS = {
    "bay-hero": '''<svg viewBox="0 0 420 280" role="img" aria-label="Illustration of an indoor home golf simulator bay with impact screen, ball flight arc and floor mat">
<defs>
  <linearGradient id="bhScreen" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f4c35"/><stop offset="100%" stop-color="#062218"/></linearGradient>
  <linearGradient id="bhArc" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#4ade80"/></linearGradient>
</defs>
<rect width="420" height="280" rx="14" fill="#071e16"/>
<!-- Floor grid -->
<path d="M20 245H400M55 220H365M85 198H335" stroke="rgba(134,239,172,0.18)" stroke-width="1"/>
<path d="M90 198L30 260M155 198L125 260M210 198V260M265 198L295 260M330 198L390 260" stroke="rgba(134,239,172,0.14)" stroke-width="1"/>
<!-- Bay enclosure frame -->
<path d="M72 204V48C72 41 77 36 84 36H336C343 36 348 41 348 48V204" fill="url(#bhScreen)" stroke="#e2e8f0" stroke-width="3.5"/>
<!-- Projected fairway silhouette -->
<path d="M84 196C130 160 190 156 240 165C285 173 320 154 336 144V196H84Z" fill="rgba(34,197,94,0.22)"/>
<circle cx="290" cy="86" r="22" fill="rgba(245,158,11,0.18)"/>
<path d="M254 156V96" stroke="#94a3b8" stroke-width="1.6"/>
<path d="M254 96L274 103L254 110Z" fill="#f59e0b"/>
<!-- Hitting mat -->
<polygon points="148,248 272,248 250,214 170,214" fill="#166534" stroke="#86efac" stroke-width="1.5"/>
<!-- Launch monitor beside ball -->
<rect x="278" y="216" width="22" height="30" rx="4" fill="#1e293b" stroke="#4ade80" stroke-width="1.5"/>
<circle cx="289" cy="226" r="3" fill="#4ade80"/>
<circle cx="289" cy="236" r="3" fill="#f59e0b"/>
<!-- Flight arc -->
<path d="M210 231C214 166 236 126 268 112" fill="none" stroke="url(#bhArc)" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="210" cy="231" r="4.5" fill="#f59e0b"/>
<circle cx="268" cy="112" r="6" fill="#ffffff" stroke="#4ade80" stroke-width="2"/>
<!-- Telemetry pills -->
<rect x="86" y="48" width="112" height="44" rx="8" fill="rgba(6,31,22,0.82)" stroke="rgba(134,239,172,0.3)"/>
<text x="96" y="66" font-family="system-ui,sans-serif" font-size="10" font-weight="700" fill="#86efac">ROOM CLEARANCE</text>
<text x="96" y="83" font-family="system-ui,sans-serif" font-size="13" font-weight="800" fill="#ffffff">2.7m – 3.0m+ H</text>
</svg>''',

    "compare-hero": '''<svg viewBox="0 0 420 260" role="img" aria-label="Illustration of launch monitor brand comparison across radar and camera placement">
<rect width="420" height="260" rx="14" fill="#071e16"/>
<rect x="22" y="24" width="180" height="212" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(147,197,253,0.4)"/>
<text x="38" y="50" font-family="system-ui,sans-serif" font-size="12" font-weight="800" fill="#93c5fd">RADAR (BEHIND)</text>
<text x="38" y="68" font-family="system-ui,sans-serif" font-size="11" fill="#cbd5e1">Garmin R10 · Rapsodo</text>
<text x="38" y="84" font-family="system-ui,sans-serif" font-size="11" fill="#cbd5e1">Shot Scope · FlightScope</text>
<rect x="96" y="196" width="32" height="16" rx="4" fill="#3b82f6"/>
<line x1="112" y1="196" x2="112" y2="124" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4 4"/>
<circle cx="112" cy="122" r="6" fill="#ffffff"/>
<text x="58" y="164" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#bfdbfe">1.5m – 2.7m behind</text>
<rect x="218" y="24" width="180" height="212" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(134,239,172,0.45)"/>
<text x="234" y="50" font-family="system-ui,sans-serif" font-size="12" font-weight="800" fill="#86efac">CAMERA (BESIDE)</text>
<text x="234" y="68" font-family="system-ui,sans-serif" font-size="11" fill="#cbd5e1">Garmin R50 · SkyTrak</text>
<text x="234" y="84" font-family="system-ui,sans-serif" font-size="11" fill="#cbd5e1">Square · Bushnell · Uneekor</text>
<circle cx="290" cy="144" r="6" fill="#ffffff"/>
<rect x="336" y="130" width="24" height="32" rx="4" fill="#22c55e"/>
<line x1="298" y1="144" x2="334" y2="144" stroke="#86efac" stroke-width="2" stroke-dasharray="4 4"/>
<text x="242" y="192" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#bbf7d0">~0.4m – 0.5m beside tee</text>
</svg>''',

    "racing-hero": '''<svg viewBox="0 0 420 260" role="img" aria-label="Illustration of a sim racing cockpit footprint and triple-screen field of view">
<rect width="420" height="260" rx="14" fill="#0f172a"/>
<path d="M24 216H396" stroke="rgba(255,255,255,0.16)" stroke-width="1.5"/>
<!-- Triple screens -->
<path d="M124 64L168 54V116L124 106Z" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<rect x="172" y="54" width="76" height="62" rx="3" fill="#1e293b" stroke="#f8fafc" stroke-width="2.2"/>
<path d="M296 64L252 54V116L296 106Z" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
<!-- Cockpit chassis -->
<path d="M126 196H294L280 156H212L174 128L138 196Z" fill="#334155" stroke="#e2e8f0" stroke-width="2"/>
<!-- Steering wheel + base -->
<rect x="218" y="122" width="28" height="22" rx="4" fill="#dc2626"/>
<circle cx="212" cy="133" r="14" fill="none" stroke="#f8fafc" stroke-width="3.5"/>
<!-- Bucket seat -->
<path d="M134 188L120 112C120 105 128 104 134 110L152 172H186V188H134Z" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
<text x="36" y="42" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#fca5a5">TYPICAL COCKPIT FOOTPRINT</text>
<text x="36" y="60" font-family="system-ui,sans-serif" font-size="13" font-weight="800" fill="#ffffff">~136–170 cm L × 54–60 cm W</text>
</svg>''',

    "radar-vs-camera": '''<figure class="diagram-box"><svg viewBox="0 0 760 240" role="img" aria-label="Top-down room layout comparing radar launch monitor placement behind the tee versus camera launch monitor placement beside the tee">
<rect width="760" height="240" rx="10" fill="#f8fafc"/>
<line x1="380" y1="16" x2="380" y2="224" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 5"/>
<!-- Left: Radar -->
<text x="24" y="34" font-family="system-ui,sans-serif" font-size="14" font-weight="800" fill="#0f172a">Radar unit (sits behind the ball)</text>
<text x="24" y="52" font-family="system-ui,sans-serif" font-size="12" fill="#475569">Needs room behind the tee + ball flight to net</text>
<rect x="24" y="88" width="12" height="106" rx="3" fill="#0f4c35"/>
<text x="42" y="102" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#0f4c35">Net / Screen</text>
<circle cx="170" cy="142" r="7" fill="#15803d"/>
<text x="155" y="168" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#0f172a">Tee</text>
<rect x="284" y="130" width="28" height="24" rx="4" fill="#1d4ed8"/>
<text x="262" y="172" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#1e40af">Radar unit</text>
<line x1="180" y1="142" x2="280" y2="142" stroke="#1d4ed8" stroke-width="2" stroke-dasharray="4 3"/>
<text x="190" y="132" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#1e40af">1.8–2.4 m</text>
<line x1="38" y1="142" x2="160" y2="142" stroke="#15803d" stroke-width="2"/>
<text x="64" y="132" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#15803d">2.4–3.0 m+ flight</text>
<!-- Right: Camera -->
<text x="404" y="34" font-family="system-ui,sans-serif" font-size="14" font-weight="800" fill="#0f172a">Photometric camera (sits beside the ball)</text>
<text x="404" y="52" font-family="system-ui,sans-serif" font-size="12" fill="#475569">Saves depth behind you; sits ~0.4–0.5 m to the side</text>
<rect x="404" y="88" width="12" height="106" rx="3" fill="#0f4c35"/>
<text x="422" y="102" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#0f4c35">Net / Screen</text>
<circle cx="566" cy="142" r="7" fill="#15803d"/>
<text x="556" y="128" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#0f172a">Tee</text>
<rect x="554" y="180" width="24" height="22" rx="4" fill="#15803d"/>
<text x="586" y="195" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#166534">Camera unit (~0.5 m side)</text>
<line x1="566" y1="150" x2="566" y2="178" stroke="#15803d" stroke-width="2" stroke-dasharray="4 3"/>
</svg><figcaption>Placement differences from makers' manuals: radar monitors (Garmin R10, Rapsodo MLM2PRO, Shot Scope LM1, FlightScope Mevo+) sit behind the tee; camera units (Garmin R50, SkyTrak ST MAX, Square Golf, Bushnell, Uneekor) sit beside the tee.</figcaption></figure>''',

    "bay-dimensions": '''<figure class="diagram-box"><svg viewBox="0 0 760 240" role="img" aria-label="Side-view diagram of an indoor golf simulator bay showing ceiling height, net buffer and short-throw projector zone">
<rect width="760" height="240" rx="10" fill="#f8fafc"/>
<!-- Room outline -->
<rect x="30" y="28" width="700" height="184" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
<!-- Wall behind screen buffer -->
<rect x="30" y="28" width="54" height="184" fill="#fef3c7"/>
<text x="36" y="118" font-family="system-ui,sans-serif" font-size="10.5" font-weight="700" fill="#92400e">Buffer</text>
<text x="35" y="133" font-family="system-ui,sans-serif" font-size="10" fill="#92400e">30cm+</text>
<!-- Impact screen -->
<line x1="90" y1="42" x2="90" y2="210" stroke="#0f4c35" stroke-width="5"/>
<text x="98" y="60" font-family="system-ui,sans-serif" font-size="11.5" font-weight="800" fill="#0f4c35">Impact screen &amp; padded enclosure</text>
<!-- Short-throw projector -->
<rect x="278" y="34" width="44" height="18" rx="4" fill="#1e293b"/>
<line x1="278" y1="44" x2="92" y2="54" stroke="rgba(21,128,61,0.3)" stroke-width="1.5" stroke-dasharray="4 3"/>
<line x1="278" y1="46" x2="92" y2="198" stroke="rgba(21,128,61,0.3)" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="234" y="70" font-family="system-ui,sans-serif" font-size="11" font-weight="700" fill="#334155">Short-throw projector</text>
<!-- Hitting mat -->
<rect x="320" y="200" width="130" height="12" rx="2" fill="#16a34a"/>
<text x="342" y="192" font-family="system-ui,sans-serif" font-size="11.5" font-weight="700" fill="#0f172a">Hitting mat</text>
<!-- Height callout -->
<line x1="650" y1="30" x2="650" y2="210" stroke="#d97706" stroke-width="2"/>
<text x="536" y="122" font-family="system-ui,sans-serif" font-size="12" font-weight="800" fill="#92400e">2.7m – 3.0m+ ceiling</text>
<text x="536" y="139" font-family="system-ui,sans-serif" font-size="11" fill="#78350f">(check full driver swing)</text>
</svg><figcaption>Typical indoor bay layout based on SkyTrak, Rapsodo and Garmin room-space guidance. Always check driver swing clearance before buying an enclosure.</figcaption></figure>''',
}

def render(body):
    body = sub_brand(body)
    body = re.sub(r"\[\[p:([\w-]+)\]\]", lambda m: product_card(m.group(1)), body)
    body = re.sub(
        r"\[\[btn:([\w-]+)\|([^\]]+)\]\]",
        lambda m: f'<a class="btn" href="{amz(PRODUCTS[m.group(1)]["asin"])}" rel="sponsored nofollow noopener" target="_blank">{esc(m.group(2))} &rarr;</a>',
        body,
    )
    body = re.sub(
        r"\[\[buy:([\w-]+)\|([^\]]+)\]\]",
        lambda m: f'<a href="{amz(PRODUCTS[m.group(1)]["asin"])}" rel="sponsored nofollow noopener" target="_blank">{esc(m.group(2))}</a>',
        body,
    )
    body = re.sub(r"\[\[price:([\w-]+)\]\]", lambda m: f"£{PRODUCTS[m.group(1)]['price']}", body)
    body = re.sub(r"\[\[link:([^|\]]+)\|([^\]]+)\]\]", lambda m: f'<a href="{u(m.group(1))}">{esc(m.group(2))}</a>', body)
    body = re.sub(r"\[\[svg:([\w-]+)\]\]", lambda m: SVGS[m.group(1)], body)
    body = body.replace("[[checked]]", CFG["price_checked"]).replace("[[BP]]", BASE_PATH)
    body = re.sub(
        r'(?<![">=/])(https?://[^\s<]+[^\s<.,)])',
        lambda m: f'<a href="{m.group(1)}" rel="noopener" target="_blank">{m.group(1)}</a>',
        body,
    )
    body = body.replace("<th>", '<th scope="col">')
    return body

LOGO_ICON = '''<svg viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="hdrBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#07261a"/><stop offset="100%" stop-color="#16a34a"/></linearGradient></defs><rect width="48" height="48" rx="12" fill="url(#hdrBg)"/><path d="M10 34V16.5C10 14.6 11.4 13 13.3 13H34.7C36.6 13 38 14.6 38 16.5V34" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M7.5 34.5H40.5" stroke="#86efac" stroke-width="2.4" stroke-linecap="round"/><path d="M16 31.5C18.5 23.5 23.5 19.5 30.5 18.5" fill="none" stroke="#f59e0b" stroke-width="2.6" stroke-linecap="round"/><circle cx="31.5" cy="18.3" r="4.6" fill="none" stroke="#f59e0b" stroke-width="1.4"/><circle cx="31.5" cy="18.3" r="2.6" fill="#fff"/></svg>'''

DISC_SHORT = (
    'As an Amazon Associate, {name} earns from qualifying purchases. '
    'Links to Amazon on this page are affiliate links. <a href="{dl}">How this works</a>.'
)

def build_faq_html(faq):
    if not faq:
        return ""
    items = []
    for q, a in faq:
        items.append(
            f'<details class="faq-item"><summary>{esc(sub_brand(q))}</summary>'
            f'<div class="faq-body"><p>{render(a)}</p></div></details>'
        )
    return '<section class="faq-sec" aria-label="Frequently asked questions"><h2>Frequently asked questions</h2>' + "".join(items) + "</section>"

def build_related_html(rel):
    if not rel:
        return ""
    cards = []
    for path, title, blurb in rel:
        cards.append(
            f'<a class="card tile" href="{u(path)}"><div><h3>{esc(sub_brand(title))}</h3><p>{esc(sub_brand(blurb))}</p></div>'
            f'<span class="tile-cta">Read guide &rarr;</span></a>'
        )
    return '<section class="related-sec"><h2>Related guides &amp; comparisons</h2><div class="cards three">' + "".join(cards) + "</div></section>"

def layout(pg, body):
    path = pg["path"]
    raw_title = sub_brand(pg["title"])
    title = raw_title if (path == "/" or NAME in raw_title) else f"{raw_title} | {NAME}"
    if len(title) > 70:
        title = raw_title
    desc = sub_brand(pg["description"])
    h1_text = sub_brand(pg["h1"] if "h1" in pg else pg["title"])
    robots = '<meta name="robots" content="noindex, nofollow">' if CFG["noindex"] else '<meta name="robots" content="index, follow">'
    live = [s for s in SECTIONS if s["live"]]

    def cur(p):
        return ' aria-current="page"' if path.startswith(p) and p != "/" else ""

    nav_links = []
    for s in live:
        cls = ' class="nav-hi"' if s.get("highlight") else ""
        nav_links.append(f'<a href="{u(s["path"])}"{cls}{cur(s["path"])}>{esc(s["name"])}</a>')
    nav_links.append(f'<a href="{u("/about/")}"{cur("/about/")}>About</a>')
    nav = "".join(nav_links)

    crumbs = pg.get("crumbs", [])
    crumb_html = ""
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": full("/"), "logo": full("/logo.png")},
        {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": full("/"), "inLanguage": "en-GB", "dateModified": CFG["updated"]},
    ]
    if path != "/":
        items = [("Home", "/")] + crumbs + [(sub_brand(pg.get("short", raw_title)), path)]
        crumb_html = (
            '<p class="crumbs">'
            + " &rsaquo; ".join(
                (f'<a href="{u(p)}">{esc(n)}</a>' if i < len(items) - 1 else esc(n))
                for i, (n, p) in enumerate(items)
            )
            + "</p>"
        )
        ld.append(
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": n, "item": full(p)}
                    for i, (n, p) in enumerate(items)
                ],
            }
        )
    if pg.get("type") == "article":
        ld.append(
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": raw_title,
                "description": desc,
                "datePublished": CFG["published"],
                "dateModified": CFG["updated"],
                "inLanguage": "en-GB",
                "author": {"@type": "Organization", "name": NAME, "url": full("/")},
                "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": full("/logo.png")}},
                "mainEntityOfPage": full(path),
                "image": full("/og.png"),
            }
        )
    if pg.get("faq"):
        ld.append(
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": sub_brand(q),
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": re.sub(r"<[^>]+>", "", render(a)),
                        },
                    }
                    for q, a in pg["faq"]
                ],
            }
        )
    if pg.get("itemlist"):
        ld.append(
            {
                "@context": "https://schema.org",
                "@type": "ItemList",
                "name": raw_title,
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "name": sub_brand(n),
                        "url": target if target.startswith("http") else full(target),
                    }
                    for i, (n, target) in enumerate(pg["itemlist"])
                ],
            }
        )

    if pg.get("howto"):
        ht = pg["howto"]
        ld.append(
            {
                "@context": "https://schema.org",
                "@type": "HowTo",
                "name": sub_brand(ht["name"]),
                "description": desc,
                "step": [
                    {"@type": "HowToStep", "position": i + 1, "name": sub_brand(st_name), "text": sub_brand(st_text)}
                    for i, (st_name, st_text) in enumerate(ht["steps"])
                ],
            }
        )
    ldjson = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    has_links = "amazon.co.uk/dp/" in body or pg.get("disclosure", True)
    disc = f'<div class="disc-bar"><div class="wrap">{DISC_SHORT.format(name=esc(NAME), dl=u("/affiliate-disclosure/"))}</div></div>' if has_links else ""
    dated = (
        f'<p class="meta">Last updated <time datetime="{CFG["updated"]}">{CFG["price_checked"]}</time>. Researched from makers\' published documents and Amazon UK listings. We have not tested these products.</p>'
        if path != "/404.html"
        else ""
    )
    da_html = ""
    if pg.get("direct_answer"):
        dq, da_body = pg["direct_answer"]
        da_html = (
            f'<section class="aeo-answer" aria-label="Quick answer">'
            f'<span class="aeo-label">Quick answer</span>'
            f'<h2>{esc(sub_brand(dq))}</h2>'
            f'<p>{render(da_body)}</p></section>'
        )
    hero_html = ""
    h1_block = f"<h1>{esc(h1_text)}</h1>"
    if pg.get("hero"):
        hero = pg["hero"]
        variant = f' {hero["variant"]}' if hero.get("variant") else ""
        ctas = ""
        if hero.get("cta_primary"):
            lbl, href = hero["cta_primary"]
            ctas += f'<a class="btn-hero" href="{u(href)}">{esc(lbl)} &rarr;</a>'
        if hero.get("cta_secondary"):
            lbl, href = hero["cta_secondary"]
            ctas += f'<a class="btn-hero-sec" href="{u(href)}">{esc(lbl)}</a>'
        stats = "".join(f"<span><strong>{esc(v)}</strong> {esc(k)}</span>" for v, k in hero.get("stats", []))
        art = f'<div class="hero-art">{SVGS[hero["svg"]]}</div>' if hero.get("svg") else ""
        hero_html = (
            f'<section class="hero{variant}"><div class="wrap"><div class="hero-grid">'
            f'<div><div class="eyebrow">{esc(sub_brand(hero["eyebrow"]))}</div>'
            f'<h1>{esc(h1_text)}</h1>'
            f'<p class="hero-lede">{esc(sub_brand(hero["lede"]))}</p>'
            + (f'<div class="hero-actions">{ctas}</div>' if ctas else "")
            + (f'<div class="hero-stats">{stats}</div>' if stats else "")
            + f'</div>{art}</div></div></section>'
        )
        h1_block = ""

    faq_html = build_faq_html(pg.get("faq"))
    rel_html = build_related_html(pg.get("related"))
    foot_nav = "".join(
        f'<a href="{u(p)}">{n}</a>'
        for n, p in [
            ("Home golf", "/golf/"),
            ("Compare brands", "/compare/"),
            ("Sim racing", "/racing/"),
            ("About", "/about/"),
            ("Affiliate disclosure", "/affiliate-disclosure/"),
            ("Privacy", "/privacy/"),
            ("Contact", "/contact/"),
        ]
    )
    wordmark_html = f'<span>{esc(P1)}</span> <span class="brand-accent">{esc(P2)}</span>' if P2 else f'<span>{esc(P1)}</span>'
    js_tag = f'<script src="{u("/app.js")}" defer></script>' if pg.get("js") else ""

    return f'''<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">{robots}
<link rel="canonical" href="{full(path)}">
<meta property="og:type" content="{"article" if pg.get("type")=="article" else "website"}"><meta property="og:site_name" content="{esc(NAME)}">
<meta property="og:title" content="{esc(raw_title)}"><meta property="og:description" content="{esc(desc)}">
<meta name="theme-color" content="#07261a">
<meta property="og:url" content="{full(path)}"><meta property="og:image" content="{full("/og.png")}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{u("/favicon.svg")}" type="image/svg+xml"><link rel="apple-touch-icon" href="{u("/logo.png")}"><link rel="stylesheet" href="{u("/style.css")}">
{ldjson}</head><body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="site"><div class="wrap"><a class="logo" href="{u("/")}">{LOGO_ICON}<span>{wordmark_html}</span></a><nav class="main" aria-label="Main">{nav}</nav></div></header>
{disc}{hero_html}
<main id="main-content"><div class="wrap">{crumb_html}<article>{h1_block}{dated}{da_html}{body}{faq_html}{rel_html}</article></div></main>
<footer class="site"><div class="wrap"><strong>{esc(NAME)}</strong> &middot; {esc(sub_brand(CFG["tagline"]))}<nav aria-label="Footer">{foot_nav}</nav>
<p>As an Amazon Associate, {esc(NAME)} earns from qualifying purchases. Prices and availability were checked on {CFG["price_checked"]} and can change at any time; the price on Amazon at the time of purchase applies. We research products from makers' published documents and Amazon UK listings and have not tested them ourselves.</p>
<p>Amazon and the Amazon logo are trademarks of Amazon.com, Inc. or its affiliates.</p></div></footer>
{js_tag}</body></html>'''

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in os.listdir(os.path.join(ROOT, "static")):
        shutil.copy(os.path.join(ROOT, "static", f), OUT)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    urls = []
    for pg in PAGES:
        body = render(pg["body"])
        da = pg.get("direct_answer")
        da_text = (da[0] + " " + da[1]) if da else ""
        faq_text = " ".join(q + " " + a for q, a in pg.get("faq", [])) + " " + da_text
        raw_check = sub_brand(
            re.sub(r"\[\[[^\]]*\]\]|<[^>]+>", " ", pg["body"])
            + " " + pg["title"]
            + " " + pg["description"]
            + " " + faq_text
        )
        m = BLOCK.search(raw_check)
        assert not m, f"blocked word in {pg['path']}: {m.group(0) if m else ''}"
        doc = layout(pg, body)
        target = (
            os.path.join(OUT, pg["path"].strip("/"), "index.html")
            if pg["path"] != "/404.html"
            else os.path.join(OUT, "404.html")
        )
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, "w").write(doc)
        if pg["path"] != "/404.html":
            urls.append(pg["path"])
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append(f"<url><loc>{xesc(full(p))}</loc><lastmod>{CFG['updated']}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    if CFG["noindex"]:
        robots = (
            "# Preview build: keep search and AI crawlers out until the real domain is live.\n"
            "# At go-live (noindex=false), GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended and Bingbot are explicitly allowed.\n"
            "User-agent: *\nDisallow: /\n"
        )
    else:
        ai_bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "ClaudeBot", "Google-Extended", "Bingbot"]
        bot_rules = "\n".join(f"User-agent: {b}\nAllow: /\n" for b in ai_bots)
        robots = f"{bot_rules}\nUser-agent: *\nAllow: /\n\nSitemap: {full('/sitemap.xml')}\n"
    open(os.path.join(OUT, "robots.txt"), "w").write(robots)

    llms_lines = [
        f"# {NAME}",
        f"> {sub_brand(CFG['tagline'])}. Last updated {CFG['updated']}.",
        "",
        f"{NAME} publishes factual UK buying and room-sizing guides for home golf simulator bays and sim racing rigs. "
        f"Every measurement and specification is cited from manufacturers' manuals, official UK product pages, and Amazon UK listings checked on {CFG['price_checked']}. "
        "We do not test products hands-on and do not publish star ratings or review scores.",
        "",
        "## Key Pages",
    ]
    for pg in PAGES:
        if pg["path"] == "/404.html":
            continue
        p_title = sub_brand(pg["title"])
        p_desc = sub_brand(pg["description"])
        llms_lines.append(f"- [{p_title}]({full(pg['path'])}): {p_desc}")
    open(os.path.join(OUT, "llms.txt"), "w").write("\n".join(llms_lines) + "\n")
    if CFG.get("custom_domain") and not CFG["noindex"]:
        open(os.path.join(OUT, "CNAME"), "w").write(CFG["custom_domain"] + "\n")
    print(f"Built {len(urls)} pages into docs/ (noindex={CFG['noindex']}, base={BASE_URL}, name={NAME})")

if __name__ == "__main__":
    main()
