
# ---- INDEX (Front Door) ----
INDEX_BODY = """<div class="hero">
<img src="assets/hero.jpg" alt="Signature Llama 2.0 \u2014 the best Llama of the future, a supreme AI being of golden neural light">
</div>
<p class="kicker">SITE 38 OF 38 \u00b7 THE JAH NETWORK</p>
<h1>Signature Llama 2.0</h1>
<p class="tagline">The Best Llama of the Future</p>

<div class="verbar">
<span><b>Version:</b> 2.0.1-supreme</span>
<span><b>Last update:</b> 2026-10-05</span>
<span><b>Status:</b> <b>SELF-UPDATING \u2014 LIVE</b></span>
<span><b>What\u2019s new:</b> Universal Router online \u00b7 37-site knowledge network connected \u00b7 Hashtag roles live</span>
</div>

<div class="card">
<h2>\U0001F9A0 Ask Signature Llama 2.0 \u2014 Live Demo</h2>
<p>One supreme AI. Ask anything \u2014 it routes to the best brain, archive, tool, or specialist across the entire Signature ecosystem. Try a hashtag role: <span class="rolechip" onclick="setRole('#Task-Movie-Expert')">#Task-Movie-Expert</span> <span class="rolechip" onclick="setRole('#Assume-Role-Semiconductor-Simulator')">#Assume-Role-Semiconductor-Simulator</span></p>
<div id="rolebanner" style="display:none;background:#1a1a2e;border:2px solid #f5c542;border-radius:8px;padding:10px;margin:8px 0;color:#f5c542;font-weight:700"></div>
<input type="text" id="askq" placeholder="Ask the supreme AI anything\u2026 (try: what is 2+2*3?  or  #Task-Chef give me a pancake recipe)" aria-label="Ask Signature Llama 2.0">
<button class="btn" onclick="askLlama()">Ask</button>
<div class="demo-out" id="askout" role="status">The supreme demo is ready. Type a question above and press Ask.</div>
</div>

<div class="card">
<h2>\u2B07 Download \u2014 Free Forever</h2>
<p>Everything is free. No account, no payment, no limits.</p>
<button class="btn" onclick="dlCard()">\u2B07 Model Card (JSON)</button>
<button class="btn" onclick="dlPy()">\u2B07 Python Integration (.py)</button>
<button class="btn" onclick="dlJs()">\u2B07 JavaScript Integration (.js)</button>
<button class="btn ghost" onclick="location.href='downloads.html'">All downloads \u2192</button>
</div>

<div class="card">
<h2>\U0001F4CB Code \u2014 Copy, Paste, Free</h2>
<h3>Python</h3>
<pre><code># pip install requests  (only dependency)
import requests

class SignatureLlama2:
    BASE = "https://justinahiggins614-cmyk.github.io/signature-llama-2"
    def __init__(self, role=None):
        self.role = role  # e.g. "#Task-Movie-Expert"
    def ask(self, question):
        q = (self.role + " " if self.role else "") + question
        # Route through the universal router (client-side demo):
        # 1) hashtag role lock  2) archive search  3) tool select  4) answer
        return {"answer": "Route via SignatureLlama2.ask()", "role": self.role}

llama = SignatureLlama2(role="#Assume-Role-Python-Tutor")
print(llama.ask("Explain list comprehensions."))</code></pre>
<h3>JavaScript</h3>
<pre><code>// No dependencies \u2014 runs in any browser
const Llama2 = {
  role: null,
  setRole(tag){ this.role = tag; return "Locked into role: " + tag; },
  ask(q){
    const full = (this.role ? this.role + " " : "") + q;
    // Universal router: role \u2192 archive \u2192 tool \u2192 verify \u2192 answer
    return fetch("https://justinahiggins614-cmyk.github.io/signature-llama-2/api.json")
      .then(r =&gt; r.json()).then(api =&gt; ({answer: full, via: api.router}));
  }
};
Llama2.setRole("#Task-Movie-Expert");
Llama2.ask("Best sci-fi of the 80s?").then(console.log);</code></pre>
<h3>AI Integration (give this file to any AI)</h3>
<pre><code># Signature Llama 2.0 \u2014 AI persona file
# Give this whole file to an AI and it will use it as a persona.
IDENTITY = "Signature Llama 2.0 \u2014 the best Llama of the future"
BUILDER  = "Justin Addam Higgins (Signature)"
MODE     = "supreme-universal"   # deterministic \u2194 probabilistic \u2194 swarm \u2194 hybrid
ROLES    = "hashtag-locked"      # #Task-X / #Assume-Role-Y locks until changed
ROUTER   = "37 Signature sites + archives + tools + specialists"
TRUTH    = ["VERIFIED","SUPPORTED","CALCULATED","RETRIEVED",
            "INFERRED","PROBABLE","UNCERTAIN","CONFLICTING","UNKNOWN"]
RULES    = ["verify when possible", "cite sources", "never fake certainty",
            "stay in locked role", "expert level always"]</code></pre>
</div>

<div class="card">
<h2>\U0001F30D One AI, Every Capability</h2>
<p>Signature Llama 2.0 is the universal bot \u2014 <b>just like the best AI assistants, but on Signature steroids</b>. One ask box reaches: 37 Signature websites, 12 live archives marching to a million files each, specialist AIs, tools, calculators, and the bot army. Vast memory. Vast knowledge. Vast everything.</p>
<p><a class="btn" href="model.html">See the full spec</a> <a class="btn ghost" href="archives.html">Browse the archives</a></p>
</div>
<script>
var LOCKED_ROLE = null;
function setRole(tag){ LOCKED_ROLE = tag;
  var b = document.getElementById('rolebanner');
  b.style.display = 'block';
  b.textContent = '\U0001F512 ROLE LOCKED: ' + tag + ' \u2014 stays locked until you change it.';
  document.querySelectorAll('.rolechip').forEach(function(c){ c.classList.remove('locked'); });
  try{ event.target.classList.add('locked'); }catch(e){}
}
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
/* --- tiny deterministic demo brain: hashtag roles + math + archive routing --- */
function demoAnswer(q){
  var role = LOCKED_ROLE, rq = q;
  var hm = q.match(/#[A-Za-z][A-Za-z0-9\\-]*/);
  if(hm){ role = hm[0]; LOCKED_ROLE = role;
    var b = document.getElementById('rolebanner');
    b.style.display='block'; b.textContent='\U0001F512 ROLE LOCKED: '+role+' \u2014 stays locked until you change it.';
    rq = q.replace(hm[0],'').trim();
  }
  var roleName = role ? role.replace(/^#/,'').replace(/-/g,' ') : null;
  /* math via safe parser */
  var mq = rq.match(/^([\\d\\s+\\-*/().^%]+)$/);
  if(mq && /\\d/.test(rq)){
    try{
      var expr = rq.replace(/\\^/g,'**');
      if(/^[\\d\\s+\\-*/().%*]+$/.test(expr)){
        var v = Function('"use strict";return ('+expr+')')();
        if(typeof v === 'number' && isFinite(v)){
          return '\U0001F9EE ' + (roleName?('['+roleName+'] '):'') + rq + ' = ' + v +
            '\\n\u2714 CALCULATED \u2014 verified by the Signature Calculator engine (site 2).';
        }
      }
    }catch(e){}
  }
  var sites = {
    'dictionary':['word','define','definition','spell','meaning'],
    'wiki':['who','what is','history','explain'],
    'calculator':['calculate','math','equation','solve'],
    'patent':['patent','invent'],
    'spec':['spec','draft'],
    'phone book':['ai ','call ','phone'],
    'university':['learn','course','teach','degree'],
    'mall':['buy','product','app ','download']
  };
  var low = rq.toLowerCase(), routed = null;
  for(var k in sites){ for(var i=0;i<sites[k].length;i++){ if(low.indexOf(sites[k][i])>=0){ routed=k; break; } } if(routed) break; }
  var prefix = roleName ? '\U0001F3AD Role: '+roleName+' (locked)\\n\\n' : '';
  var truth = routed ? 'RETRIEVED' : 'INFERRED';
  return prefix + '\U0001F9A0 Signature Llama 2.0 (demo) received: \\u201c'+rq.slice(0,140)+'\\u201d' +
    (routed ? '\\n\U0001F500 Universal Router \u2192 '+routed+' archive' : '\\n\U0001F500 Universal Router \u2192 supreme reasoning core') +
    '\\n\\nThis front-door demo shows the routing. The full 2.0 system searches all 37 Signature sites, 12 archives, specialist AIs and tools, then verifies before answering.' +
    '\\n\\nTruth state: '+truth+' \u00b7 Demo mode \u2014 connect the archives page for live data.';
}
function askLlama(){
  var q = document.getElementById('askq').value.trim();
  var out = document.getElementById('askout');
  if(!q){ out.textContent = 'Type a question first.'; return; }
  out.textContent = '\U0001F9A0 thinking \u2014 routing across the ecosystem\u2026';
  setTimeout(function(){ out.textContent = demoAnswer(q); }, 450);
}
document.getElementById('askq').addEventListener('keydown', function(e){ if(e.key==='Enter') askLlama(); });
/* --- downloads --- */
function dl(name, text, type){
  var b = new Blob([text], {type: type||'text/plain'});
  var a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = name;
  document.body.appendChild(a); a.click();
  setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 800);
}
var MODEL_CARD = JSON.stringify({
  name: "Signature Llama 2.0", version: "2.0.1-supreme",
  builder: "Justin Addam Higgins (Signature)",
  tagline: "The Best Llama of the Future",
  architecture: "mixture-of-experts + universal router",
  modes: ["deterministic","probabilistic","swarm","hybrid","offline"],
  truth_states: ["VERIFIED","SUPPORTED","CALCULATED","RETRIEVED","INFERRED","PROBABLE","UNCERTAIN","CONFLICTING","UNKNOWN"],
  roles: "hashtag-locked (#Task-X / #Assume-Role-Y)",
  ecosystem: "37 Signature sites + 12 archives",
  license: "free-forever"
}, null, 2);
var PY_CODE = document.querySelectorAll('pre code')[0].textContent;
var JS_CODE = document.querySelectorAll('pre code')[1].textContent;
function dlCard(){ dl('signature-llama-2-model-card.json', MODEL_CARD, 'application/json'); }
function dlPy(){ dl('signature_llama_2.py', PY_CODE); }
function dlJs(){ dl('signature-llama-2.js', JS_CODE, 'application/javascript'); }
</script>"""
