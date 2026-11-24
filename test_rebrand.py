#!/usr/bin/env python3
"""Non-destructive test verifying config.json rebrand & go-live switch."""
import json, os, shutil, subprocess, tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
with tempfile.TemporaryDirectory() as tmp:
    dst = os.path.join(tmp, "site")
    shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    cfg_path = os.path.join(dst, "config.json")
    cfg = json.load(open(cfg_path))
    old_name = cfg["site_name"]
    cfg["site_name"] = "Test Golf Guide"
    cfg["brand_wordmark"] = ["Test Golf", "Guide"]
    cfg["base_url"] = "https://example.co.uk"
    cfg["custom_domain"] = "example.co.uk"
    cfg["noindex"] = False
    json.dump(cfg, open(cfg_path, "w"), indent=2)

    subprocess.run(["python3", "build_assets.py"], cwd=dst, check=True)
    subprocess.run(["python3", "build.py"], cwd=dst, check=True)
    subprocess.run(["python3", "check_links.py"], cwd=dst, check=True)

    for rel in ("docs/index.html", "docs/compare/index.html", "docs/about/index.html", "docs/logo.svg"):
        txt = open(os.path.join(dst, rel)).read()
        assert old_name not in txt, f"Found old brand {old_name!r} in {rel}"
        assert "Test Golf" in txt, f"Missing new brand in {rel}"
    assert "Allow: /" in open(os.path.join(dst, "docs/robots.txt")).read()
    assert open(os.path.join(dst, "docs/CNAME")).read().strip() == "example.co.uk"
print("REBRAND & GO-LIVE TEST PASSED")
