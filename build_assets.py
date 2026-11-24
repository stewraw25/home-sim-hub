#!/usr/bin/env python3
"""Generate brand SVG & PNG assets from config.json.
Swap site_name / brand_wordmark / tagline in config.json and re-run to rebrand all assets.
"""
import html, json, os, subprocess, tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(ROOT, "config.json")))
STATIC = os.path.join(ROOT, "static")
os.makedirs(STATIC, exist_ok=True)

SITE_NAME = CFG["site_name"]
PARTS = CFG.get("brand_wordmark") or [SITE_NAME, ""]
P1 = html.escape(PARTS[0])
P2 = html.escape(PARTS[1]) if len(PARTS) > 1 else ""
TAGLINE = html.escape(CFG["tagline"])

MARK_INNER = '''<defs>
  <linearGradient id="hshBg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#07261a"/>
    <stop offset="55%" stop-color="#0f4c35"/>
    <stop offset="100%" stop-color="#16a34a"/>
  </linearGradient>
  <linearGradient id="hshArc" x1="0" y1="1" x2="1" y2="0">
    <stop offset="0%" stop-color="#f59e0b"/>
    <stop offset="100%" stop-color="#86efac"/>
  </linearGradient>
</defs>
<rect width="48" height="48" rx="12" fill="url(#hshBg)"/>
<rect x="2.5" y="2.5" width="43" height="43" rx="10" fill="none" stroke="rgba(255,255,255,0.16)" stroke-width="1.2"/>
<!-- Simulator bay frame -->
<path d="M10 34V16.5C10 14.6 11.4 13 13.3 13H34.7C36.6 13 38 14.6 38 16.5V34" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
<!-- Bay floor / mat perspective -->
<path d="M7.5 34.5H40.5" stroke="#86efac" stroke-width="2.2" stroke-linecap="round"/>
<path d="M15 34.5L18.5 29H29.5L33 34.5" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.45)" stroke-width="1.2" stroke-linejoin="round"/>
<!-- Launch trajectory arc -->
<path d="M16 31.5C18.5 23.5 23.5 19.5 30.5 18.5" fill="none" stroke="url(#hshArc)" stroke-width="2.4" stroke-linecap="round"/>
<!-- Target ring + golf ball -->
<circle cx="31.5" cy="18.3" r="4.8" fill="none" stroke="#f59e0b" stroke-width="1.3" stroke-opacity="0.85"/>
<circle cx="31.5" cy="18.3" r="2.6" fill="#ffffff"/>
<circle cx="16" cy="31.8" r="1.6" fill="#f59e0b"/>'''

FAVICON_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="{html.escape(SITE_NAME)} icon">{MARK_INNER}</svg>\n'''

# Editable SVG wordmark lockup
WORDMARK_SVG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 60" role="img" aria-label="{html.escape(SITE_NAME)} logo">
  <g transform="translate(4,6)">{MARK_INNER}</g>
  <text x="64" y="34" font-family="system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif" font-size="25" font-weight="800" letter-spacing="-0.6" fill="#0f172a">{P1}<tspan fill="#15803d"> {P2}</tspan></text>
  <text x="65" y="50" font-family="system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif" font-size="10.5" font-weight="600" letter-spacing="1.4" fill="#475569">UK HOME GOLF &amp; SIMULATOR GUIDES</text>
</svg>\n'''

open(os.path.join(STATIC, "favicon.svg"), "w").write(FAVICON_SVG)
open(os.path.join(STATIC, "logo.svg"), "w").write(WORDMARK_SVG)

def chrome_render(html_str, out_path, w, h):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as tf:
        tf.write(html_str)
        tmp_html = tf.name
    try:
        subprocess.run([
            "google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox",
            "--hide-scrollbars", f"--window-size={w},{h}",
            f"--screenshot={out_path}", f"file://{tmp_html}"
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        os.unlink(tmp_html)

logo_html = f'''<!DOCTYPE html><html><body style="margin:0;background:#07261a;display:flex;align-items:center;justify-content:center;width:512px;height:512px;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="440" height="440">{MARK_INNER}</svg>
</body></html>'''
chrome_render(logo_html, os.path.join(STATIC, "logo.png"), 512, 512)

og_html = f'''<!DOCTYPE html><html><body style="margin:0;width:1200px;height:630px;background:radial-gradient(circle at 85% 20%, #15803d 0%, #0b3b2a 42%, #061c14 100%);font-family:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;color:#fff;position:relative;overflow:hidden;display:flex;align-items:center;">
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.04) 1px,transparent 1px);background-size:48px 48px;"></div>
<div style="position:relative;z-index:2;padding:64px 76px;display:flex;align-items:center;justify-content:space-between;width:100%;box-sizing:border-box;gap:48px;">
  <div style="max-width:740px;">
    <div style="display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.16);padding:10px 18px;border-radius:999px;font-size:20px;font-weight:700;letter-spacing:0.4px;color:#86efac;margin-bottom:28px;">
      <span>UK BUYING &amp; ROOM SIZE GUIDES</span>
    </div>
    <div style="font-size:74px;font-weight:800;line-height:1.05;letter-spacing:-1.8px;margin:0 0 22px;">{P1} <span style="color:#4ade80;">{P2}</span></div>
    <div style="font-size:30px;line-height:1.38;color:#d1fae5;font-weight:500;max-width:680px;">{TAGLINE}</div>
    <div style="margin-top:34px;display:flex;gap:14px;font-size:19px;font-weight:600;color:#e2e8f0;">
      <span style="background:rgba(245,158,11,0.18);border:1px solid rgba(245,158,11,0.45);color:#fde68a;padding:8px 16px;border-radius:10px;">Compare Launch Monitor Brands</span>
      <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.18);padding:8px 16px;border-radius:10px;">Makers' Room Specs</span>
    </div>
  </div>
  <div style="flex-shrink:0;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="260" height="260">{MARK_INNER}</svg>
  </div>
</div>
</body></html>'''
chrome_render(og_html, os.path.join(STATIC, "og.png"), 1200, 630)
print("Generated static/favicon.svg, static/logo.svg, static/logo.png, static/og.png")
