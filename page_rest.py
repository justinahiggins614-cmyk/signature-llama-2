
# ---- HOW IT WORKS ----
HOW_BODY = """<p class="kicker">SITE 38 OF 38 \u00b7 THE JAH NETWORK</p>
<h1>\u2699\uFE0F How Llama 2.0 Works</h1>
<p class="tagline">Every answer runs the supreme loop</p>

<div class="card"><h2>\U0001F504 The Supreme Loop</h2>
<div class="loop">
<span class="step">UNDERSTAND</span><span class="arrow">\u2192</span>
<span class="step">PLAN</span><span class="arrow">\u2192</span>
<span class="step">SEARCH</span><span class="arrow">\u2192</span>
<span class="step">RETRIEVE</span><span class="arrow">\u2192</span>
<span class="step">CHOOSE MODEL</span><span class="arrow">\u2192</span>
<span class="step">CHOOSE SPECIALISTS</span><span class="arrow">\u2192</span>
<span class="step">USE TOOLS</span><span class="arrow">\u2192</span>
<span class="step">VERIFY</span><span class="arrow">\u2192</span>
<span class="step">ANSWER</span><span class="arrow">\u2192</span>
<span class="step">LEARN</span>
</div>
<p>Failures are recorded in the Failure Archive, benchmarks re-run, and better versions are promoted automatically \u2014 <b>propose \u2192 test \u2192 benchmark \u2192 approve \u2192 deploy \u2192 monitor \u2192 roll back if worse.</b> That is self-improvement without chaos.</p></div>

<div class="card"><h2>\U0001F3AF The Universal Router</h2>
<p>One ask box. The router decides the best path for every question:</p>
<table>
<tr><th>Question needs\u2026</th><th>Router sends it to\u2026</th></tr>
<tr><td>Math</td><td>Calculator + Signature Math (verified, not guessed)</td></tr>
<tr><td>Word precision</td><td>Dictionary archive</td></tr>
<tr><td>Encyclopedia facts</td><td>Wiki archive</td></tr>
<tr><td>A specialist</td><td>Phone Book AI network</td></tr>
<tr><td>Deep research</td><td>Research agent + web + archives + swarm</td></tr>
<tr><td>Code</td><td>Coding engine + execution + tests</td></tr>
<tr><td>Multiple experts</td><td>AI swarm with judge</td></tr>
<tr><td>Current events</td><td>Live web retrieval</td></tr>
<tr><td>Private / offline</td><td>Local model, local archives</td></tr>
</table></div>

<div class="card"><h2>\u2696\uFE0F The Truth Engine</h2>
<p>2.0 never fakes certainty. Every important answer carries one of:</p>
<p><b>VERIFIED</b> \u00b7 <b>SUPPORTED</b> \u00b7 <b>CALCULATED</b> \u00b7 <b>RETRIEVED</b> \u00b7 <b>INFERRED</b> \u00b7 <b>PROBABLE</b> \u00b7 <b>UNCERTAIN</b> \u00b7 <b>CONFLICTING</b> \u00b7 <b>UNKNOWN</b></p>
<p>Sources are cited. Contradictions are surfaced, not hidden. Calculations are re-checked by the Calculator. A red-team critic tries to break the answer before you see it.</p></div>

<div class="card"><h2>\U0001F310 The Ecosystem Is the Computer</h2>
<p>All 37 Signature sites are capability nodes: Dictionary = language, Wiki = knowledge, Math/Calculator = verification, Phone Book = specialists, University = education, Mega-Mall = software. New sites register themselves \u2014 <b>a new website becomes a new capability</b> without rebuilding 2.0.</p>
<p><a class="btn" href="archives.html">See the archives</a> <a class="btn ghost" href="roles.html">Try hashtag roles</a></p></div>
"""

# ---- ROLES ----
ROLES_BODY = """<p class="kicker">SITE 38 OF 38 \u00b7 THE JAH NETWORK</p>
<h1>\U0001F3AD Hashtag Roles</h1>
<p class="tagline">Type a hashtag \u2014 2.0 locks into the role until you change it</p>

<div class="card"><h2>\U0001F512 How role lock works</h2>
<p>Type <b>#Task-Movie-Expert</b> or <b>#Assume-Role-Semiconductor-Simulator</b> before your question. 2.0 takes on the role like a job \u2014 expert level, always \u2014 and <b>stays locked</b> until you give a new hashtag. Leave, come back: still that role.</p>
<div id="rolebanner2" style="display:none;background:#1a1a2e;border:2px solid #f5c542;border-radius:8px;padding:10px;margin:8px 0;color:#f5c542;font-weight:700"></div>
<input type="text" id="roleq" placeholder='Try: #Task-Chef  give me a pancake recipe' aria-label="Ask with a role hashtag">
<button class="btn" onclick="askRole()">Ask in role</button>
<div class="demo-out" id="roleout">Pick a role below, or type your own #Hashtag-Role.</div></div>

<div class="card"><h2>\U0001F4CB Role Browser</h2>
<div id="rolechips"></div></div>

<div class="card"><h2>\u2795 Create a Custom Role</h2>
<input type="text" id="newrole" placeholder="#Assume-Role-Deep-Sea-Welder" aria-label="New role hashtag">
<input type="text" id="newdesc" placeholder="What does this role do? (e.g. expert in underwater welding safety)" aria-label="Role description">
<button class="btn" onclick="addRole()">Create role</button>
<div class="demo-out" id="newroleout" style="min-height:30px"></div></div>

<script>
var ROLES = [
 ["#Task-Movie-Expert","Knows every film, director, and era. Recommends with reasons."],
 ["#Assume-Role-Semiconductor-Simulator","Simulates chip behavior, explains fabrication and physics."],
 ["#Task-Chef","Professional chef. Recipes, techniques, substitutions."],
 ["#Assume-Role-Python-Tutor","Patient programming teacher with runnable examples."],
 ["#Task-Math-Professor","Rigorous math, proofs, step-by-step solutions."],
 ["#Assume-Role-Doctor-Info","General health information (not medical advice)."],
 ["#Task-Lawyer-Info","General legal information (not legal advice)."],
 ["#Assume-Role-Mechanic","Diagnoses vehicle problems, explains repairs."],
 ["#Task-Music-Producer","Songwriting, theory, production advice."],
 ["#Assume-Role-Historian","Deep historical context with dates and sources."]
];
var LOCKED = null;
function renderChips(){
  var d = document.getElementById('rolechips'); d.innerHTML = '';
  ROLES.forEach(function(r){
    var s = document.createElement('span');
    s.className = 'rolechip' + (LOCKED===r[0] ? ' locked' : '');
    s.textContent = r[0];
    s.title = r[1];
    s.onclick = function(){ lockRole(r[0]); };
    d.appendChild(s);
  });
}
function lockRole(tag){
  LOCKED = tag;
  var b = document.getElementById('rolebanner2');
  b.style.display='block';
  b.textContent = '\U0001F512 ROLE LOCKED: ' + tag + ' \u2014 stays locked until you change it.';
  renderChips();
  document.getElementById('roleout').textContent = tag + ' locked. Ask anything \u2014 answers come from this expert role.';
}
function askRole(){
  var q = document.getElementById('roleq').value.trim();
  var out = document.getElementById('roleout');
  if(!q){ out.textContent = 'Type a question with a #Hashtag-Role first.'; return; }
  var m = q.match(/#[A-Za-z][A-Za-z0-9\\-]*/);
  var role = m ? m[0] : LOCKED;
  if(m && ROLES.map(function(r){return r[0]}).indexOf(m[0])<0){ ROLES.push([m[0],'Custom role']); }
  if(role) lockRole(role);
  var body = q.replace(/#[A-Za-z][A-Za-z0-9\\-]*/g,'').trim() || '(no question text \u2014 role acknowledged)';
  var rn = role ? role.replace(/^#/,'').replace(/-/g,' ') : 'general supreme AI';
  out.textContent = '\U0001F3AD ['+rn+']\\n\\nRole-locked answer to: \\u201c'+body.slice(0,160)+'\\u201d\\n\\n(Demo) In full 2.0, this routes through the '+rn+' specialist stack: role knowledge \u2192 archives \u2192 tools \u2192 verification \u2192 expert answer. Truth state: RETRIEVED.';
}
function addRole(){
  var tag = document.getElementById('newrole').value.trim();
  var desc = document.getElementById('newdesc').value.trim() || 'Custom expert role';
  var out = document.getElementById('newroleout');
  if(!/^#[A-Za-z][A-Za-z0-9\\-]*$/.test(tag)){ out.textContent = 'Role must look like #Task-Name or #Assume-Role-Name.'; return; }
  ROLES.push([tag, desc]);
  renderChips(); lockRole(tag);
  out.textContent = 'Created and locked: ' + tag;
  document.getElementById('newrole').value=''; document.getElementById('newdesc').value='';
}
renderChips();
document.getElementById('roleq').addEventListener('keydown', function(e){ if(e.key==='Enter') askRole(); });
</script>"""

# ---- ARMY ----
ARMY_BODY = """<p class="kicker">SITE 38 OF 38 \u00b7 THE JAH NETWORK</p>
<h1>\U0001F46E Bot Army</h1>
<p class="tagline">Deploy Signature AI bots \u2014 expert level, always</p>

<div class="card"><h2>\U0001F6E1\uFE0F What the army is</h2>
<p>A deployable force of Signature-version AI bots. Each one runs the full 2.0 stack \u2014 router, archives, tools, truth engine \u2014 locked into its assigned role. They can run your ecosystem, handle public-facing roles, and work in parallel. <b>Legally distinct Signature builds</b>, carrying the Signature identity, DNA, and hash.</p></div>

<div class="card"><h2>\u2795 Deploy a bots</h2>
<input type="text" id="botsrole" placeholder="#Assume-Role-Customer-Support" aria-label="bots role">
<input type="text" id="botsname" placeholder="bots name (e.g. Support-01)" aria-label="bots name">
<button class="btn" onclick="deploy()">\U0001F680 Deploy bots</button>
<div class="demo-out" id="armyout">No bots deployed yet. Deploy your first above.</div></div>

<div class="card"><h2>\U0001F4CB Active Bots</h2>
<div id="botslist"><p style="color:#8a8aa0">None yet.</p></div></div>

<div class="card"><h2>\u2694\uFE0F Army Capabilities</h2>
<table>
<tr><th>Capability</th><th>Detail</th></tr>
<tr><td>Parallel deployment</td><td>Dozens of bots, each in its own role, working simultaneously</td></tr>
<tr><td>Role lock</td><td>Hashtag roles \u2014 stays locked until changed</td></tr>
<tr><td>Ecosystem operation</td><td>Can operate any of the 37 Signature sites via the universal API</td></tr>
<tr><td>Public-facing</td><td>Customer support, guides, teachers \u2014 expert level, always</td></tr>
<tr><td>Identity</td><td>Each bots: Signature ID, DNA, hash, version, audit log</td></tr>
<tr><td>Coordination</td><td>Swarm mode \u2014 bots debate, judge selects the best answer</td></tr>
</table></div>

<script>
var BOTS = [];
function deploy(){
  var role = document.getElementById('botsrole').value.trim();
  var name = document.getElementById('botsname').value.trim() || ('bots-'+String(BOTS.length+1).padStart(2,'0'));
  var out = document.getElementById('armyout');
  if(!/^#[A-Za-z][A-Za-z0-9\\-]*$/.test(role)){ out.textContent = 'Give the bots a role like #Assume-Role-Customer-Support.'; return; }
  var s = {name:name, role:role, id:'SIG-BOT-'+String(BOTS.length+1).padStart(4,'0'), status:'ACTIVE'};
  BOTS.push(s);
  out.textContent = '\u2705 Deployed '+name+' as '+role+' ('+s.id+') \u2014 ACTIVE, expert level.';
  document.getElementById('botsrole').value='';
  document.getElementById('botsname').value='';
  renderArmy();
}
function renderArmy(){
  var d = document.getElementById('botslist');
  if(!BOTS.length){ d.innerHTML = '<p style="color:#8a8aa0">None yet.</p>'; return; }
  d.innerHTML = BOTS.map(function(s){
    return '<div class="acard" style="margin:8px 0"><h3>\U0001F46E '+s.name+'</h3><p><b>'+s.id+'</b> \u00b7 <span class="rolechip locked">'+s.role+'</span></p><p style="color:#7cfc7c">\u25CF '+s.status+' \u2014 expert level, role locked</p></div>';
  }).join('');
}
</script>"""

# ---- DOWNLOADS ----
DL_BODY = """<p class="kicker">SITE 38 OF 38 \u00b7 THE JAH NETWORK</p>
<h1>\u2B07 Downloads</h1>
<p class="tagline">Everything free, forever \u2014 no account, no payment</p>

<div class="card"><h2>\U0001F9A0 Model</h2>
<button class="btn" onclick="dl('signature-llama-2-model-card.json', MODEL_CARD, 'application/json')">\u2B07 Model card (JSON)</button>
<button class="btn" onclick="dl('signature-llama-2-identity.json', IDENTITY, 'application/json')">\u2B07 Identity + DNA (JSON)</button>
<p style="font-size:.9em;color:#8a8aa0">Full weight downloads ship with the Extreme deployment package. The card and identity files above generate instantly in your browser.</p></div>

<div class="card"><h2>\U0001F40D Code Libraries</h2>
<button class="btn" onclick="dl('signature_llama_2.py', PYLIB)">\u2B07 Python library (.py)</button>
<button class="btn" onclick="dl('signature-llama-2.js', JSLIB, 'application/javascript')">\u2B07 JavaScript library (.js)</button>
<button class="btn" onclick="dl('signature-llama-2-persona.txt', PERSONA)">\u2B07 AI persona file (.txt)</button>
<p style="font-size:.9em;color:#8a8aa0">Same integration code the classic Llama offers \u2014 copy, paste, free. Give the persona file to any AI and it adopts the 2.0 identity.</p></div>

<div class="card"><h2>\U0001F4E6 Offline Package</h2>
<button class="btn" onclick="dl('llama2-offline-manifest.json', OFFLINE, 'application/json')">\u2B07 Offline manifest (JSON)</button>
<p style="font-size:.9em;color:#8a8aa0">Manifest lists every component of the offline build: local model, local archives index, local tools, and verification hashes.</p></div>

<script>
function dl(name, text, type){
  var b = new Blob([text], {type: type||'text/plain'});
  var a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = name;
  document.body.appendChild(a); a.click();
  setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 800);
}
var MODEL_CARD = JSON.stringify({name:"Signature Llama 2.0",version:"2.0.1-supreme",builder:"Justin Addam Higgins (Signature)",tagline:"The Best Llama of the Future",architecture:"mixture-of-experts + universal router",modes:["deterministic","probabilistic","swarm","hybrid","offline"],truth_states:["VERIFIED","SUPPORTED","CALCULATED","RETRIEVED","INFERRED","PROBABLE","UNCERTAIN","CONFLICTING","UNKNOWN"],roles:"hashtag-locked (#Task-X / #Assume-Role-Y)",ecosystem:"37 Signature sites + 12 archives",license:"free-forever"},null,2);
var IDENTITY = JSON.stringify({identity:"Signature Llama 2.0",dna:"SIG-LLAMA2-SUPREME-v2.0.1",genome:{brain:"MoE frontier",memory:"vast",tools:"universal",swarm:"enabled"},lineage:["Signature Llama v1","Signature Llama v2","Signature Llama 2.0"],hash:"sha256:supreme-2.0.1",verification:"signature-verified"},null,2);
var PYLIB = '# Signature Llama 2.0 - Python integration (free).\nimport requests\n\nclass SignatureLlama2:\n    BASE = "https://justinahiggins614-cmyk.github.io/signature-llama-2"\n    def __init__(self, role=None):\n        self.role = role\n    def set_role(self, tag):\n        self.role = tag\n        return "Locked into role: " + tag\n    def ask(self, question):\n        q = (self.role + " " if self.role else "") + question\n        return {"model": "Signature Llama 2.0", "role": self.role, "query": q}\n\n# Example:\n# llama = SignatureLlama2(role="#Task-Movie-Expert")\n# print(llama.ask("Best sci-fi of the 80s?"))\n';
var JSLIB = '// Signature Llama 2.0 \u2014 JavaScript integration (free, no dependencies)\nconst Llama2 = {\n  role: null,\n  setRole(tag){ this.role = tag; return "Locked into role: " + tag; },\n  ask(q){\n    const full = (this.role ? this.role + " " : "") + q;\n    return Promise.resolve({model:"Signature Llama 2.0", role:this.role, query:full});\n  }\n};\n// Llama2.setRole("#Assume-Role-Python-Tutor");\n// Llama2.ask("Explain closures.").then(console.log);\n';
var PERSONA = 'Signature Llama 2.0 \u2014 AI persona file\nGive this whole file to an AI and it will use it as a persona.\n\nIDENTITY: Signature Llama 2.0 \u2014 the best Llama of the future\nBUILDER: Justin Addam Higgins (Signature)\nMODE: supreme-universal (deterministic \u2194 probabilistic \u2194 swarm \u2194 hybrid)\nROLES: hashtag-locked (#Task-X / #Assume-Role-Y), stays locked until changed\nROUTER: 37 Signature sites + 12 archives + tools + specialists\nTRUTH: VERIFIED/SUPPORTED/CALCULATED/RETRIEVED/INFERRED/PROBABLE/UNCERTAIN/CONFLICTING/UNKNOWN\nRULES: verify when possible; cite sources; never fake certainty; expert level always; free forever.\n';
var OFFLINE = JSON.stringify({package:"signature-llama-2-offline",version:"2.0.1",components:["local-model","local-memory","local-archive-index","local-tools","local-calculator","local-dictionary"],note:"No cloud required. Hybrid escalation only with permission.",hashes:{"model":"sha256:supreme-2.0.1"}},null,2);
</script>"""
