#!/usr/bin/env python3
"""Build Signature Llama 2.0 site (site 38)."""
import os

BASE = "https://justinahiggins614-cmyk.github.io"
REPO = os.path.dirname(os.path.abspath(__file__))

# (number, label, url) — official live labels, site 6 omitted (self is 38)
NAV = [
 (1,"Signature Math",f"{BASE}/signature-math/"),
 (2,"Signature Universal Paradox Immune Calculator",f"{BASE}/jah-calculator/"),
 (3,"The Signature Dictionary",f"{BASE}/jah-dictionary/"),
 (4,"JAH Wiki",f"{BASE}/jah-wiki/"),
 (5,"JAH-N Wiki Leaks",f"{BASE}/jah-n-wiki-leaks/"),
 (6,"Signature Llama: The Fully Cyber Utilizable AI",f"{BASE}/signature-llama/"),
 (7,"The Signature AI Phone Book",f"{BASE}/jah-ai-models/"),
 (8,"Globally Rejustered Patent Catalog",f"{BASE}/cyber-patent-catalog/"),
 (9,"Signature Spec Catalog Pending Patents",f"{BASE}/signature-one-archive/specs.html"),
 (10,"The Signature PC System Depository",f"{BASE}/jah-computer-systems/"),
 (11,"The Signature Book Depository",f"{BASE}/signature-books/"),
 (12,"The Signature Comic Store",f"{BASE}/signature-comics/"),
 (13,"The Signature Global Newspaper Archive",f"{BASE}/signature-newspapers/"),
 (14,"The Signature AI Mix and Match Generator",f"{BASE}/signature-backend/"),
 (15,"The Signature Boundless Generator Archive",f"{BASE}/signature-boundless-generators/"),
 (16,"The Signature AI Mix Lab",f"{BASE}/signature-ai-mixlab/"),
 (17,"AI Olympics",f"{BASE}/signature-ai-olypics/"),
 (18,"The Signature Computer Chip Maker and Archive",f"{BASE}/signature-chip-maker/"),
 (19,"The Signature App Archive",f"{BASE}/signature-app-archive/"),
 (20,"The Signature AI to Robot Matcher",f"{BASE}/signature-ai-robot-matcher/"),
 (21,"The Signature Experiment Solver",f"{BASE}/signature-experiment-solver/"),
 (22,"Signature AI Pixel",f"{BASE}/signature-ai-image-video-maker/"),
 (23,"Signature Music Studio",f"{BASE}/signature-ai-song-maker/"),
 (24,"The Signature Mr Fix-It",f"{BASE}/signature-fixit/"),
 (25,"The Signature University",f"{BASE}/signature-university/"),
 (26,"Signature Earth",f"{BASE}/signature-earth/"),
 (27,"The Signature Flight School",f"{BASE}/signature-flight-school/"),
 (28,"The Signature Game Store",f"{BASE}/signature-game-store/"),
 (29,"The Signature Website Creator",f"{BASE}/signature-website-creator/"),
 (30,"The Signature Antivirus",f"{BASE}/signature-antivirus/"),
 (31,"The Signature OS Updater",f"{BASE}/signature-os-updater/"),
 (32,"Signature Space Mapping",f"{BASE}/signature-space-mapping/"),
 (33,"The Signature Cookbook",f"{BASE}/signature-cookbook/"),
 (34,"Spell Check",f"{BASE}/signature-spell-check/"),
 (35,"Grid Measure",f"{BASE}/signature-image-grid-measure/"),
 (36,"The Signature Cyber Mega-Mall",f"{BASE}/signature-cyber-mega-mall/"),
 (37,"The Signature 3D Print Mega Mall",f"{BASE}/signature-3d-print/"),
]

TABS = [
 ("index.html","Front Door"),
 ("model.html","Model"),
 ("archives.html","Archives"),
 ("how.html","How It Works"),
 ("roles.html","Roles"),
 ("army.html","Bot Army"),
 ("downloads.html","Downloads"),
]

def nav_html():
    links = "\n".join(f'<a href="{u}">{n} {l}</a>' for n,l,u in NAV)
    return f'''<div class="jahnet"><span class="jahnet-t">THE JAH NETWORK</span>{links}<span class="here">38 Signature Llama 2.0 \u2014 YOU ARE HERE</span></div>'''

def tabbar(active):
    items = []
    for href,label in TABS:
        cls = ' class="on"' if href==active else ''
        items.append(f'<a href="{href}"{cls}>{label}</a>')
    return '<nav class="tabbar" aria-label="Site pages">'+"".join(items)+'</nav>'

CSS = """<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Arial,sans-serif;background:#0a0a14;color:#e8e8f0;line-height:1.6}
.wrap{max-width:960px;margin:0 auto;padding:0 16px}
.tabbar{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;padding:12px;background:#12121f;border-bottom:2px solid #f5c542;position:sticky;top:0;z-index:100}
.tabbar a{color:#f5c542;text-decoration:none;padding:8px 14px;border:1px solid #f5c542;border-radius:20px;font-size:.85em;font-weight:600}
.tabbar a.on,.tabbar a:hover{background:#f5c542;color:#0a0a14}
.hero{position:relative;text-align:center;padding:0 0 24px}
.hero img{width:100%;max-height:340px;object-fit:cover;display:block}
.kicker{text-align:center;color:#f5c542;font-size:.8em;letter-spacing:3px;margin:16px 0 6px}
h1{text-align:center;font-size:2.4em;color:#f5c542;margin:6px 0}
.tagline{text-align:center;font-size:1.2em;color:#b9b9d0;margin-bottom:18px}
.card{background:#14141f;border:1px solid #2a2a3f;border-radius:12px;padding:20px;margin:16px 0}
.card h2{color:#f5c542;margin-bottom:10px}
.card h3{color:#f5c542;margin:14px 0 6px}
.btn{display:inline-block;background:#f5c542;color:#0a0a14;font-weight:700;padding:10px 22px;border:none;border-radius:8px;cursor:pointer;font-size:1em;margin:6px 4px;text-decoration:none}
.btn:hover{background:#ffe08a}
.btn.ghost{background:transparent;color:#f5c542;border:2px solid #f5c542}
input[type=text],textarea,select{width:100%;padding:12px;border:2px solid #2a2a3f;border-radius:8px;background:#0f0f1a;color:#e8e8f0;font-size:1em;margin:8px 0}
.demo-out{background:#0f0f1a;border:1px solid #2a2a3f;border-radius:8px;padding:14px;margin:10px 0;min-height:60px;white-space:pre-wrap}
.verbar{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;background:#101a10;border:1px solid #3a6b3a;border-radius:10px;padding:12px;margin:14px 0;font-size:.9em}
.verbar b{color:#7cfc7c}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin:14px 0}
.acard{background:#14141f;border:1px solid #2a2a3f;border-radius:10px;padding:16px}
.acard h3{color:#f5c542;margin-bottom:6px}
.acard .count{font-size:1.6em;color:#7cfc7c;font-weight:700}
.acard .st{font-size:.8em;padding:3px 10px;border-radius:12px;display:inline-block;margin-top:6px}
.st.live{background:#1a4d1a;color:#7cfc7c}.st.build{background:#4d3d1a;color:#f5c542}.st.plan{background:#3a3a4d;color:#b9b9d0}
pre{background:#0f0f1a;border:1px solid #2a2a3f;border-radius:8px;padding:14px;overflow-x:auto;font-size:.85em;margin:10px 0}
code{color:#7cfc7c}
.loop{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:16px 0}
.step{background:#1a1a2e;border:2px solid #f5c542;color:#f5c542;padding:10px 14px;border-radius:8px;font-weight:700;font-size:.9em}
.arrow{color:#f5c542;font-size:1.4em;align-self:center}
.rolechip{display:inline-block;background:#1a1a2e;border:1px solid #f5c542;color:#f5c542;padding:6px 14px;border-radius:16px;margin:4px;cursor:pointer;font-size:.9em}
.rolechip:hover{background:#f5c542;color:#0a0a14}
.rolechip.locked{background:#f5c542;color:#0a0a14;font-weight:700}
.jahnet{background:#0d0d18;border-top:2px solid #f5c542;padding:20px 16px;margin-top:32px;font-size:.85em;line-height:2}
.jahnet-t{color:#f5c542;font-weight:700;letter-spacing:2px;margin-right:10px}
.jahnet a{color:#8a8aa0;text-decoration:none;margin-right:12px}
.jahnet a:hover{color:#f5c542}
.jahnet .here{display:inline-block;background:#f5c542;color:#0a0a14;font-weight:700;padding:4px 14px;border-radius:16px;margin-top:8px}
footer{text-align:center;padding:20px;color:#5a5a70;font-size:.8em}
table{width:100%;border-collapse:collapse;margin:10px 0;font-size:.9em}
th,td{border:1px solid #2a2a3f;padding:8px;text-align:left}
th{background:#1a1a2e;color:#f5c542}
</style>"""

def page(title, active, body, desc=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} \u2014 Signature Llama 2.0</title>
<meta name="description" content="{desc or title+' \u2014 Signature Llama 2.0, the best Llama of the future.'}">
{CSS}
</head>
<body>
{tabbar(active)}
<div class="wrap">
{body}
</div>
{nav_html()}
<footer>SITE 38 OF 38 \u00b7 THE JAH NETWORK<br>Signature Llama 2.0 \u2014 The Best Llama of the Future \u00b7 Justin Addam Higgins' Signature AI</footer>
</body>
</html>"""

def write(name, html):
    p = os.path.join(REPO, name)
    open(p, "w", encoding="utf-8").write(html)
    print("wrote", name, len(html), "bytes")
