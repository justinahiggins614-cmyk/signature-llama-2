
# ---- ARCHIVES ----
ARCHIVES = [
 ("Knowledge Archive", "JAH Wiki", "https://justinahiggins614-cmyk.github.io/jah-wiki/", "1,010,114", "live", "Every spec, patent, and subject article \u2014 the encyclopedia layer 2.0 reasons over."),
 ("Dictionary Archive", "The Signature Dictionary", "https://justinahiggins614-cmyk.github.io/jah-dictionary/", "1,127,335", "live", "Words, definitions, terminology \u2014 the language authority 2.0 queries for precision."),
 ("Spec Archive", "Spec Catalog", "https://justinahiggins614-cmyk.github.io/signature-one-archive/specs.html", "908,995", "live", "Justin Addam Higgins' own draft specifications \u2014 marching to 1,000,000."),
 ("Patent Archive", "Patent Catalog", "https://justinahiggins614-cmyk.github.io/cyber-patent-catalog/", "73,961", "live", "Public patent records, harvested and growing."),
 ("Dossier Archive", "JAH-N Wiki Leaks", "https://justinahiggins614-cmyk.github.io/jah-n-wiki-leaks/", "74,140", "live", "Declassified bizarre-subject dossiers with full analysis."),
 ("Equation Archive", "Calculator", "https://justinahiggins614-cmyk.github.io/jah-calculator/", "132,300", "live", "Solved equation records \u2014 2.0's math verification layer."),
 ("Book Archive", "Book Depository", "https://justinahiggins614-cmyk.github.io/signature-books/", "48,100", "live", "Finished books with Q&A AI \u2014 training-grade text."),
 ("AI Archive", "AI Phone Book", "https://justinahiggins614-cmyk.github.io/jah-ai-models/", "10,000+", "live", "Every Signature AI + word AIs \u2014 2.0's specialist network."),
 ("Code Archive", "App Archive", "https://justinahiggins614-cmyk.github.io/signature-app-archive/", "37,830", "live", "Working apps with runnable code \u2014 software 2.0 can read and learn from."),
 ("Song Archive", "Music Studio", "https://justinahiggins614-cmyk.github.io/signature-ai-song-maker/", "40,000+", "live", "Finished songs \u2014 audio intelligence training data."),
 ("Address Archive", "Signature Earth", "https://justinahiggins614-cmyk.github.io/signature-earth/", "3,500", "live", "Real geocoded addresses \u2014 geographic knowledge."),
 ("Math Archive", "Signature Math", "https://justinahiggins614-cmyk.github.io/signature-math/", "growing", "live", "Formal math grid \u2014 geometric and deterministic reasoning."),
]
PLANNED = [
 ("Model Archive", "Every Llama version, checkpoint, and fine-tune \u2014 v1 \u2192 v2 \u2192 2.0 lineage, never deleted.", "build"),
 ("Training Archive", "Datasets, configs, and cleaning results behind every model version.", "build"),
 ("Experiment Archive", "Every development experiment with results \u2014 the scientific history of 2.0.", "build"),
 ("Failure Archive", "Wrong answers, failed code, hallucinations \u2014 the fuel for self-improvement.", "build"),
 ("Benchmark Archive", "Millions of tests; every model version scored against every previous one.", "build"),
 ("Research Archive", "Research projects, findings, and citations produced by 2.0's research agents.", "plan"),
]

def archives_body():
    cards = []
    for name, site, url, count, st, desc in ARCHIVES:
        cards.append(f"""<div class="acard"><h3>{name}</h3>
<div class="count">{count}</div><div style="font-size:.8em;color:#8a8aa0">records \u00b7 as of 2026-10-05</div>
<p style="font-size:.9em;margin:8px 0">{desc}</p>
<p><a class="btn ghost" style="padding:6px 14px;font-size:.85em" href="{url}">Open {site} \u2192</a></p>
<span class="st {st}">\U0001F7E2 LIVE</span></div>""")
    for name, desc, st in PLANNED:
        label = "\U0001F7E1 BUILDING" if st=="build" else "\u26AA PLANNED"
        cards.append(f"""<div class="acard"><h3>{name}</h3>
<p style="font-size:.9em;margin:8px 0">{desc}</p>
<span class="st {st}">{label}</span></div>""")
    return """<p class="kicker">SITE 38 OF 38 \u00b7 THE JAH NETWORK</p>
<h1>\U0001F5C3\uFE0F Archives Powering Llama 2.0</h1>
<p class="tagline">Live data 2.0 actively searches \u2014 marching to a million files per archive and beyond</p>
<div class="card"><h2>\U0001F4CA How 2.0 uses archives</h2>
<p>2.0 never tries to cram the universe into its weights. It <b>searches</b> these archives, <b>retrieves</b> what matters, <b>reasons</b> over it, and <b>verifies</b> before answering. Every record carries source, date, and provenance \u2014 that\u2019s what makes the answers trustworthy.</p></div>
<div class="grid">""" + "\n".join(cards) + "</div>"
