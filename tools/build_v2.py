"""Builds the "Midnight Aurora" design (v2) into /v2/ from the v1 pages.

v1 (site root) is never modified: this script only reads the root *.html files
and writes transformed copies into v2/, adding v4.css / v4.js on top of the
shared stylesheets. v2 pages are noindexed and canonicalised to v1 so the
preview never competes with the live site in search.

Run after tools/build.py (build.py calls it automatically).
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "v2")
os.makedirs(OUT, exist_ok=True)

SWITCH = ('<a href="../index.html" class="v-switch" title="View the current design (v1)">'
          '<span>Design v2</span><b>View v1 ↗</b></a>')

for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    html = open(path, encoding="utf-8").read()
    html = re.sub(r'(href|src)="assets/', r'\1="../assets/', html)
    html = html.replace('<link rel="stylesheet" href="../assets/css/v3.css">',
                        '<link rel="stylesheet" href="../assets/css/v3.css">\n  <link rel="stylesheet" href="../assets/css/v4.css">', 1)
    html = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex, follow">', html, count=1)
    html = re.sub(r'<body([^>]*)class="([^"]*)"', r'<body\1class="v2 \2"', html, count=1)
    if 'class="v2' not in html:
        html = html.replace("<body", '<body class="v2"', 1)
    html = html.replace('<script src="../assets/js/main.js" defer></script>',
                        '<script src="../assets/js/main.js" defer></script>\n<script src="../assets/js/v4.js" defer></script>\n' + SWITCH, 1)
    with open(os.path.join(OUT, os.path.basename(path)), "w", encoding="utf-8") as f:
        f.write(html)
print("v2 built:", len(glob.glob(os.path.join(OUT, "*.html"))), "pages")
