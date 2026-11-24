# Home Sim Hub

Static UK guide site for home golf simulator bays, brand comparisons and sim racing rigs.

## Rebrand or Go Live (Single Config)
All brand identity, wordmark, domain and preview-noindex settings live in `config.json`:
1. Edit `site_name`, `brand_wordmark`, `tagline`, `base_url`, `custom_domain`, and `noindex` in `config.json`.
2. Regenerate brand SVGs/PNGs (`favicon.svg`, `logo.svg`, `logo.png`, `og.png`):
   ```bash
   python3 build_assets.py
   ```
3. Build `docs/` and run full SEO/link/compliance checks:
   ```bash
   python3 build.py && python3 check_links.py
   ```

When `noindex` is `false` and `custom_domain` is set, `build.py` removes `noindex` tags, switches `docs/robots.txt` to allow crawling with the sitemap URL, and writes `docs/CNAME`.
