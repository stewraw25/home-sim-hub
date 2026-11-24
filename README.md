# Home Sim Hub (working name)

Static Amazon UK affiliate site about home simulators: golf first, then sim racing. More sections (VR, flight sim) can be added in `sections.json` and `content/pages.py`.

## Build
```
python3 build.py        # writes docs/ (GitHub Pages serves main:/docs)
python3 check_links.py  # noindex, disclosure, affiliate tag, rel and internal-link checks
```

## One config file
`config.json` holds the site name, `base_url`, `amazon_tag` and `noindex`. Renaming the site or going live is a change there plus a rebuild.

## Go-live (after the domain is bought)
1. In `config.json`: set `base_url` to `https://<domain>`, `noindex` to `false`, and add `"custom_domain": "<domain>"` (the build then writes `docs/CNAME`).
2. `python3 build.py && python3 check_links.py`, commit, push.
3. DNS at Porkbun: apex A records to GitHub Pages (185.199.108.153, .109.153, .110.153, .111.153) and `www` CNAME to `stewraw25.github.io`.
4. Repo Settings, Pages: set the custom domain and tick Enforce HTTPS.
5. Add the domain to Google Search Console, submit `sitemap.xml`, then ping IndexNow.

## Rules for content
No testing or ownership claims, no star ratings or review schema, no invented specs or superlatives. Specs come from the maker or the Amazon listing. Prices show only as "checked on <date>".
