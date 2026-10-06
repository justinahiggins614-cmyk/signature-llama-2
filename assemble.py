#!/usr/bin/env python3
"""Assemble all Signature Llama 2.0 pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import page, write, BASE
from page_index import INDEX_BODY
from page_model import MODEL_BODY
from page_archives import archives_body
from page_rest import HOW_BODY, ROLES_BODY, ARMY_BODY, DL_BODY

PAGES = [
 ("index.html", "Front Door", "index.html", INDEX_BODY,
  "Signature Llama 2.0 \u2014 The Best Llama of the Future. Live demo, free downloads, Python/JS code."),
 ("model.html", "Model Spec", "model.html", MODEL_BODY,
  "Signature Llama 2.0 full model specification \u2014 MoE, reasoning, memory, tools, swarm, safety."),
 ("archives.html", "Archives", "archives.html", archives_body(),
  "All archives powering Signature Llama 2.0 \u2014 live counts from the Signature ecosystem."),
 ("how.html", "How It Works", "how.html", HOW_BODY,
  "How Signature Llama 2.0 works \u2014 the supreme loop, universal router, truth engine."),
 ("roles.html", "Hashtag Roles", "roles.html", ROLES_BODY,
  "Hashtag role lock for Signature Llama 2.0 \u2014 #Task-X and #Assume-Role-Y roles."),
 ("army.html", "Bot Army", "army.html", ARMY_BODY,
  "Deploy Signature AI soldiers \u2014 the 2.0 bot army, expert level always."),
 ("downloads.html", "Downloads", "downloads.html", DL_BODY,
  "Download Signature Llama 2.0 \u2014 model card, code libraries, offline package. Free forever."),
]

for fname, title, active, body, desc in PAGES:
    write(fname, page(title, active, body, desc))

# sitemap + robots
urls = "\n".join(
    f'  <url><loc>{BASE}/signature-llama-2/{f}</loc></url>' for f,_,_,_,_ in PAGES)
write("sitemap.xml",
      f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>')
write("robots.txt",
      f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/signature-llama-2/sitemap.xml\n")
print("ALL PAGES BUILT")
