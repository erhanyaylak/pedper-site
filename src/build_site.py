#!/usr/bin/env python3
"""Generates the multi-page pedper.com site into ../docs/ (run: python3 src/build_site.py)."""
import os, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

OUT = os.path.join(ROOT, 'docs')
J = 'https://pedagogicalperspective.com/index.php/pub/'
A = 'assets/'

# ---------------------------------------------------------------- CSS
css = open(os.path.join(HERE, 'base.css')).read()
for a, b in [('svg.logo{display:block;height:auto}', 'img.logo{display:block;height:auto}'),
             ('.nav .home svg', '.nav .home img'), ('.hero-mark svg', '.hero-mark img'),
             ('.jcover .hd svg', '.jcover .hd img'), ('.jcover .art svg', '.jcover .art img'),
             ('.foot-main .home svg', '.foot-main .home img')]:
    assert a in css, a
    css = css.replace(a, b)
css += r'''
/* ---------- shared additions ---------- */
.traits{grid-template-columns:repeat(4,1fr)}
.btn-outline{border:1.5px solid var(--lav);color:var(--dark)}
.btn-outline:hover{border-color:var(--dark)}
nav a.active{color:var(--brand);font-weight:600}
nav a.active:not(.btn){box-shadow:inset 0 -2px 0 var(--lav)}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px;padding-top:18px;border-top:1px solid var(--gray)}
.facts dt,.indexed span,.commit span,.eyebrow{display:block;font-size:.7rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--lav)}
.facts dd{font-size:.95rem;font-weight:500;margin-top:2px}
.indexed{margin-top:16px;font-size:.86rem;color:var(--muted);line-height:1.7}
a.pol{color:inherit;display:block}
.commit{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:22px}
.commit div{background:var(--soft);border-radius:12px;padding:18px 22px;font-size:.92rem;font-weight:500;color:var(--dark)}
.c-card dd.addr{font-size:.92rem;line-height:1.5}
.more{margin-top:28px}
.link{font-weight:600;display:inline-flex;gap:8px;align-items:center}
.link:hover{color:var(--dark)}

/* ---------- sub pages ---------- */
.page-hero{position:relative;overflow:hidden;background:var(--night);background-image:var(--iso),radial-gradient(600px 360px at 85% 30%,rgb(110 82 163 / .55),transparent 70%);color:#fff;padding:64px 0 70px}
.page-hero::after{content:"";position:absolute;right:0;top:0;width:200px;height:200px;background:linear-gradient(225deg,rgb(166 140 200 / .35) 0 50%,transparent 50%)}
.page-hero .wrap{position:relative;z-index:1}
.crumbs{font-size:.8rem;color:var(--lav)}
.crumbs a{color:#D9D0F5}
.crumbs a:hover{color:#fff}
.page-hero h1{color:#fff;font-size:clamp(2rem,4.2vw,3rem);font-weight:700;margin-top:14px;letter-spacing:-.01em}
.page-hero p{color:#D9D0F5;font-size:1.1rem;max-width:720px;margin-top:16px}
.page-hero .bar{width:64px;height:4px;background:var(--lav);border-radius:2px;margin-top:24px}
.sub-sec{padding:80px 0}
.sub-sec.alt{background:var(--soft);background-image:var(--iso)}
.sub-sec h2{margin-top:16px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start}
.prose p{color:var(--muted);margin-top:14px}
.prose p:first-child{margin-top:0}
.prose strong{color:var(--ink)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}
.cards.c2{grid-template-columns:repeat(2,1fr)}
.cards.c4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:1px solid var(--gray);border-radius:14px;padding:26px 24px}
.card h3{color:var(--night)}
.card p{color:var(--muted);font-size:.93rem;margin-top:8px}
.card .ic{width:46px;height:46px;border-radius:12px;background:var(--lav-l);display:grid;place-items:center;margin-bottom:16px}
.card svg{width:24px;height:24px;fill:none;stroke:var(--dark);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.checks{list-style:none;margin-top:18px;display:grid;gap:12px}
.checks li{position:relative;padding-left:32px;color:var(--muted)}
.checks li::before{content:"";position:absolute;left:0;top:3px;width:20px;height:20px;border-radius:50%;background:var(--lav-l) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M6 10.5l2.5 2.5L14 7.5' fill='none' stroke='%234A2E83' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/100% no-repeat}
.checks li strong{color:var(--ink)}
.checks.no li::before{background:#FBECEC url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M7 7l6 6M13 7l-6 6' fill='none' stroke='%23B03A3A' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E") center/100% no-repeat}
table.spec{width:100%;border-collapse:collapse;margin-top:28px;background:#fff;border:1px solid var(--gray);border-radius:14px;overflow:hidden;font-size:.95rem}
table.spec th,table.spec td{text-align:left;padding:14px 20px;border-bottom:1px solid var(--gray);vertical-align:top}
table.spec tr:last-child th,table.spec tr:last-child td{border-bottom:0}
table.spec th{width:34%;font-weight:600;color:var(--dark);background:var(--soft)}
table.spec thead th{background:var(--dark);color:#fff;font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;width:auto}
table.spec td{color:var(--ink)}
.timeline{list-style:none;margin-top:36px;position:relative;padding-left:28px}
.timeline::before{content:"";position:absolute;left:7px;top:6px;bottom:6px;width:2px;background:linear-gradient(var(--dark),var(--lav))}
.timeline li{position:relative;padding:0 0 26px}
.timeline li::before{content:"";position:absolute;left:-28px;top:4px;width:16px;height:16px;border-radius:50%;background:#fff;border:3px solid var(--dark)}
.timeline li.now::before{background:var(--dark);box-shadow:0 0 0 5px var(--lav-l)}
.timeline b{display:block;color:var(--night);font-size:1.05rem}
.timeline span{color:var(--muted);font-size:.93rem}
.steps{list-style:none;counter-reset:s;display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:36px}
.steps li{counter-increment:s;background:#fff;border:1px solid var(--gray);border-radius:14px;padding:24px 22px;position:relative}
.steps li::before{content:counter(s);display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--dark);color:#fff;font-weight:700;font-size:.9rem;margin-bottom:14px}
.steps b{display:block;color:var(--night)}
.steps em{display:inline-block;font-style:normal;font-size:.72rem;font-weight:700;letter-spacing:.06em;color:var(--dark);background:var(--lav-l);border-radius:99px;padding:3px 10px;margin-top:8px}
.steps p{color:var(--muted);font-size:.9rem;margin-top:8px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.chips span{font-size:.82rem;font-weight:500;background:#fff;border:1px solid var(--gray);border-radius:99px;padding:7px 14px;color:var(--ink)}
.chips.lav span{background:var(--lav-l);border-color:transparent;color:var(--dark)}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:36px}
.kpi{background:#fff;border:1px solid var(--gray);border-radius:14px;padding:24px;text-align:center}
.kpi b{display:block;font-size:2rem;font-weight:700;color:var(--dark);line-height:1.1}
.kpi span{font-size:.78rem;font-weight:600;color:var(--muted);letter-spacing:.06em}
.issues{list-style:none;margin-top:28px;display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.issues a{display:flex;justify-content:space-between;gap:16px;align-items:center;background:#fff;border:1px solid var(--gray);border-radius:12px;padding:16px 20px;color:var(--ink);transition:border-color .2s}
.issues a:hover{border-color:var(--lav)}
.issues b{color:var(--night);font-weight:600}
.issues small{display:block;color:var(--muted);font-size:.84rem}
.issues .tag{white-space:nowrap}
.pgroup{margin-top:56px}
.pgroup:first-of-type{margin-top:8px}
.pgroup-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;border-bottom:2px solid var(--dark);padding-bottom:12px}
.pgroup-head h2{font-size:1.5rem;margin:0}
.pgroup-head span{font-size:.84rem;color:var(--muted)}
.plist{display:grid;grid-template-columns:repeat(2,1fr);gap:0 40px}
.plist a{display:block;padding:20px 0;border-bottom:1px solid var(--gray);color:inherit}
.plist a:hover h3{color:var(--brand)}
.plist h3{color:var(--night);display:flex;justify-content:space-between;gap:12px}
.plist h3::after{content:"↗";color:var(--lav);font-weight:500}
.plist p{color:var(--muted);font-size:.92rem;margin-top:6px}
.toc{position:sticky;top:100px;background:#fff;border:1px solid var(--gray);border-radius:14px;padding:22px}
.toc a{display:block;padding:7px 0;color:var(--ink);font-size:.92rem;font-weight:500;border-bottom:1px dashed var(--gray)}
.toc a:last-child{border-bottom:0}
.toc a:hover{color:var(--brand)}
.with-toc{display:grid;grid-template-columns:240px 1fr;gap:48px;align-items:start}
.callout{display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;background:var(--night);background-image:var(--iso);color:#fff;border-radius:18px;padding:38px 44px;margin-top:8px}
.callout h3{color:#fff;font-size:1.4rem}
.callout p{color:#D9D0F5;margin-top:6px;max-width:620px}
.people{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}
.person{background:#fff;border:1px solid var(--gray);border-radius:14px;padding:26px}
.person .role{font-size:.7rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--lav)}
.person h3{margin-top:8px;color:var(--night);font-size:1.15rem}
.person p{color:var(--muted);font-size:.92rem;margin-top:6px;line-height:1.6}
.person a{font-weight:600;word-break:break-word}
@media (max-width:960px){
  .traits,.cards,.cards.c2,.cards.c4,.steps,.kpis,.issues,.plist,.people,.two,.with-toc,.facts,.commit{grid-template-columns:1fr}
  .toc{position:static}
  .page-hero{padding:48px 0 54px}
  .sub-sec{padding:60px 0}
  .callout{padding:30px 26px}
  table.spec th{width:40%}
  table.spec th,table.spec td{padding:12px 14px;word-break:break-word;overflow-wrap:anywhere}
  .chips span{white-space:normal}
}
@media (min-width:961px) and (max-width:1180px){.traits,.cards.c4,.steps,.kpis{grid-template-columns:repeat(2,1fr)}}
'''
os.makedirs(OUT + '/assets', exist_ok=True)
import shutil
for _f in ['pedper-logo-yatay-renkli.svg', 'pedper-logo-yatay-beyaz.svg', 'pedper-sembol-beyaz.svg', 'pedper-sembol-renkli.svg']:
    shutil.copy(os.path.join(ROOT, 'brand', 'logo', _f), os.path.join(OUT, 'assets', _f))
open(OUT + '/assets/style.css', 'w').write(css)

# ---------------------------------------------------------------- icons
IC = {
 'book': '<svg viewBox="0 0 32 32"><path d="M16 8c-3.5-2-8-3-13-2v19c5-1 9.5 0 13 2 3.5-2 8-3 13-2V6c-5-1-9.5 0-13 2z"/><path d="M16 8v19"/></svg>',
 'shield': '<svg viewBox="0 0 32 32"><path d="M16 3l11 4v8c0 7-5 12-11 14C10 27 5 22 5 15V7z"/><path d="M11 16l4 4 7-8"/></svg>',
 'scale': '<svg viewBox="0 0 32 32"><path d="M16 5v22M8 27h16M5 11h22M9 11l-4 8a4 4 0 0 0 8 0zM23 11l-4 8a4 4 0 0 0 8 0z"/></svg>',
 'globe': '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="12"/><path d="M4 16h24M16 4c-5 4-5 20 0 24M16 4c5 4 5 20 0 24"/></svg>',
 'lock': '<svg viewBox="0 0 32 32"><rect x="6" y="14" width="20" height="14" rx="2"/><path d="M11 14V9a5 5 0 0 1 9.6-2"/></svg>',
 'eye': '<svg viewBox="0 0 32 32"><path d="M4 16s4-8 12-8 12 8 12 8-4 8-12 8S4 16 4 16z"/><path d="M6 26L26 6"/></svg>',
 'spark': '<svg viewBox="0 0 32 32"><path d="M16 4l2.5 7.5L26 14l-7.5 2.5L16 24l-2.5-7.5L6 14l7.5-2.5z"/><path d="M25 22l1 3 3 1-3 1-1 3-1-3-3-1 3-1z"/></svg>',
 'undo': '<svg viewBox="0 0 32 32"><path d="M6 16a10 10 0 1 0 3-7.1M6 5v6h6"/></svg>',
 'mail': '<svg viewBox="0 0 32 32"><rect x="4" y="7" width="24" height="18" rx="2"/><path d="M4 9l12 9 12-9"/></svg>',
 'server': '<svg viewBox="0 0 32 32"><rect x="5" y="5" width="22" height="9" rx="2"/><rect x="5" y="18" width="22" height="9" rx="2"/><path d="M10 9.5h.01M10 22.5h.01"/></svg>',
 'link': '<svg viewBox="0 0 32 32"><path d="M13 19l6-6M11 14l-3 3a5 5 0 0 0 7 7l3-3M21 18l3-3a5 5 0 0 0-7-7l-3 3"/></svg>',
 'archive': '<svg viewBox="0 0 32 32"><rect x="4" y="6" width="24" height="6" rx="1.5"/><path d="M6 12v13a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1V12M13 17h6"/></svg>',
 'feed': '<svg viewBox="0 0 32 32"><path d="M6 6a20 20 0 0 1 20 20M6 13a13 13 0 0 1 13 13"/><circle cx="7" cy="25" r="1.5"/></svg>',
 'pen': '<svg viewBox="0 0 32 32"><path d="M20 5l7 7L12 27H5v-7z"/><path d="M17 8l7 7"/></svg>',
 'search': '<svg viewBox="0 0 32 32"><circle cx="14" cy="14" r="9"/><path d="M21 21l7 7"/></svg>',
 'child': '<svg viewBox="0 0 32 32"><circle cx="16" cy="8" r="4"/><path d="M9 28v-8l-3-4 4-3h12l4 3-3 4v8"/></svg>',
 'target': '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="12"/><circle cx="16" cy="16" r="7"/><circle cx="16" cy="16" r="2"/></svg>',
 'leaf': '<svg viewBox="0 0 32 32"><path d="M6 26C6 12 14 6 27 5c-1 13-7 21-21 21z"/><path d="M6 26l11-11"/></svg>',
 'free': '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="12"/><path d="M11 21L21 11M12 12h.01M20 20h.01"/></svg>',
 'clock': '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="12"/><path d="M16 9v7l5 3"/></svg>',
 'doc': '<svg viewBox="0 0 32 32"><path d="M8 4h11l6 6v18H8z"/><path d="M19 4v6h6M12 16h9M12 21h9"/></svg>',
}

def favicon():
    return 'data:image/svg+xml,' + urllib.parse.quote(open(OUT + '/assets/pedper-sembol-renkli.svg').read())

NAV = [('index.html', 'Home'), ('about.html', 'About'), ('journals.html', 'Journals'),
       ('authors.html', 'For Authors'), ('policies.html', 'Policies')]

def head(title, desc, canonical):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://pedper.com/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PedPer Publishing">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://pedper.com/{canonical}">
<meta name="theme-color" content="#281A52">
<link rel="icon" type="image/svg+xml" href="assets/pedper-sembol-renkli.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
'''

def header(active):
    items = ''.join(f'<li><a href="{h}"{" class=\"active\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    c = ' active' if active == 'contact.html' else ''
    return f'''</head>
<body>
<header>
  <div class="wrap nav">
    <a href="index.html" class="home" aria-label="PedPer Publishing home"><img class="logo" src="{A}pedper-logo-yatay-renkli.svg" alt="PedPer Publishing" width="170" height="57"></a>
    <nav aria-label="Main">
      <button class="menu-btn" aria-label="Menu" aria-controls="menu" onclick="document.getElementById('menu').classList.toggle('open')">☰</button>
      <ul id="menu">{items}<li><a href="contact.html" class="btn btn-primary{c}">Contact</a></li></ul>
    </nav>
  </div>
</header>
'''

FOOTER = f'''
<footer>
  <div class="wrap">
    <div class="foot-main">
      <div>
        <a href="index.html" class="home" aria-label="PedPer Publishing home"><img class="logo" src="{A}pedper-logo-yatay-beyaz.svg" alt="PedPer Publishing" width="210" height="70"></a>
        <p>Diamond open-access academic publishing in education. Operated by Scitera Information Technologies Ltd., Giresun, Türkiye.</p>
      </div>
      <div>
        <h4>Publisher</h4>
        <ul><li><a href="about.html">About us</a></li><li><a href="journals.html">Journals</a></li><li><a href="authors.html">For authors</a></li><li><a href="policies.html">Policies</a></li><li><a href="contact.html">Contact</a></li></ul>
      </div>
      <div>
        <h4>Pedagogical Perspective</h4>
        <ul><li><a href="https://pedagogicalperspective.com" rel="noopener">Journal website</a></li><li><a href="{J}about/submissions" rel="noopener">Make a submission</a></li><li><a href="{J}about/editorialTeam" rel="noopener">Editorial team</a></li><li><a href="{J}issue/archive" rel="noopener">Archive</a></li><li><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a></li></ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2022 PedPer Publishing. Journal content is published under CC BY 4.0 unless otherwise noted.</span>
      <span class="family">Scitera family: <a href="https://scitera.net/" rel="noopener">Scitera</a> · <span class="cur">PedPer Publishing</span> · <a href="https://misanpaige.com" rel="noopener">MisanpAIge</a> · <a href="https://desk-ly.com" rel="noopener">Deskly</a> · <a href="https://basvurum.net" rel="noopener">Başvurum</a></span>
    </div>
  </div>
</footer>
<script>
document.querySelectorAll('#menu a').forEach(a=>a.addEventListener('click',()=>document.getElementById('menu').classList.remove('open')));
</script>
</body>
</html>
'''

def page_hero(crumb, title, lead):
    return f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
    <h1>{title}</h1>
    <p>{lead}</p>
    <div class="bar"></div>
  </div>
</section>
'''

def label(n, t):
    return f'<div class="label"><i>{n}</i>{t}</div>'

def card(ic, t, p, href=None):
    inner = f'<div class="ic">{IC[ic]}</div><h3>{t}</h3><p>{p}</p>'
    return f'<a class="card pol" href="{href}" rel="noopener">{inner}</a>' if href else f'<div class="card">{inner}</div>'

CTA = f'''<section class="sub-sec" style="padding-top:0">
  <div class="wrap">
    <div class="callout">
      <div><h3>Ready to share your research?</h3><p>Submit to Pedagogical Perspective: diamond open access, double-blind peer review and free language proofreading for accepted manuscripts.</p></div>
      <div class="btns" style="margin-top:0"><a class="btn btn-white" href="{J}about/submissions" rel="noopener">Make a submission →</a><a class="btn btn-ghost" href="authors.html">Author information</a></div>
    </div>
  </div>
</section>
'''

ORG_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"PedPer Publishing","url":"https://pedper.com/","logo":"https://pedper.com/assets/pedper-logo-yatay-renkli.svg","email":"info@pedagogicalperspective.com","telephone":"+90 454 502 28 29","address":{"@type":"PostalAddress","streetAddress":"Giresun Technology Development Zone, 2nd Organized Industrial Zone, 4th Street, Building No. 5, Office Z12","addressLocality":"Giresun","addressCountry":"TR"},"publishingPrinciples":"https://pedper.com/policies.html","parentOrganization":{"@type":"Organization","name":"Scitera Information Technologies Ltd.","url":"https://scitera.net/"}}
</script>
'''

def write(name, title, desc, body, extra_head=''):
    html = head(title, desc, '' if name == 'index.html' else name) + extra_head + header(name) + '<main>\n' + body + '</main>\n' + FOOTER
    open(f'{OUT}/{name}', 'w').write(html)

# ================================================================ HOME
home = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="kicker">Diamond open-access publishing</div>
      <h1>Open, rigorous scholarship in <span>education.</span></h1>
      <div class="bar"></div>
      <p>PedPer Publishing brings research on pedagogy, teacher education and educational practice to readers worldwide — peer reviewed, free to read and free to publish.</p>
      <div class="btns">
        <a class="btn btn-white" href="journals.html">Explore our journals →</a>
        <a class="btn btn-ghost" href="{J}about/submissions" rel="noopener">Make a submission</a>
      </div>
    </div>
    <div class="hero-mark" aria-hidden="true"><img src="{A}pedper-sembol-beyaz.svg" alt=""></div>
  </div>
</section>

<div class="stats-band">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><b>2022</b><span>Founded</span></div>
      <div class="stat"><b>12</b><span>Issues published</span></div>
      <div class="stat"><b>€0</b><span>APCs &amp; fees</span></div>
      <div class="stat"><b>10</b><span>Indexes &amp; databases</span></div>
    </div>
    <p class="stats-note">Pedagogical Perspective · uninterrupted biannual publication since 2022, including two conference special issues</p>
  </div>
</div>

<section id="about">
  <div class="wrap about">
    <div class="sec-head">
      {label('01', 'About us')}
      <h2>Publishing that serves education research</h2>
      <p class="lead">PedPer Publishing is a Türkiye-based, scholar-led academic publisher dedicated to education, operated by Scitera Information Technologies Ltd. We publish diamond open-access journals that welcome diverse disciplinary, theoretical and methodological perspectives, and we hold every title to transparent editorial and ethical standards guided by COPE.</p>
    </div>
    <div class="traits">
      <div class="trait"><div class="ic">{IC['book']}</div><h3>Diamond open access</h3><p>Free to read and free to publish: no APCs, no submission fees. Content is licensed under CC BY 4.0 and authors retain copyright.</p></div>
      <div class="trait"><div class="ic">{IC['shield']}</div><h3>Rigorous review</h3><p>Double-blind peer review by at least two independent reviewers, with iThenticate similarity screening for every submission.</p></div>
      <div class="trait"><div class="ic">{IC['scale']}</div><h3>Editorial independence</h3><p>Publisher and Editor-in-Chief roles are held by different people. The publisher cannot influence or override editorial decisions.</p></div>
      <div class="trait"><div class="ic">{IC['globe']}</div><h3>International reach</h3><p>An editorial board from more than 25 countries; every article receives a Crossref DOI and is preserved in LOCKSS and CLOCKSS.</p></div>
    </div>
    <div class="more"><a class="link" href="about.html">More about PedPer Publishing →</a></div>
  </div>
</section>

<section id="journals">
  <div class="wrap">
    <div class="sec-head">
      {label('02', 'Our journals')}
      <h2>Journals</h2>
    </div>
    <article class="journal">
      <div class="jcover" aria-hidden="true">
        <div class="hd"><img src="{A}pedper-logo-yatay-renkli.svg" alt=""><small>Vol. 5 · No. 2<br>2026</small></div>
        <h4>Pedagogical<br>Perspective</h4>
        <div class="art"><img src="{A}pedper-sembol-beyaz.svg" alt=""></div>
      </div>
      <div>
        <h3>Pedagogical Perspective</h3>
        <div class="meta">
          <span class="tag">eISSN 2822-4841</span>
          <span class="tag">Biannual · March &amp; October</span>
          <span class="tag">Double-blind review</span>
          <span class="tag">DOI 10.29329</span>
          <span class="tag">CC BY 4.0</span>
          <span class="tag on">Diamond OA · No APC</span>
        </div>
        <p>An international, open-access journal publishing English-language research and review articles in education. Pedagogical Perspective welcomes qualitative, quantitative, mixed-methods, theoretical and methodological studies that advance educational theory and practice and foster interdisciplinary and international dialogue.</p>
        <dl class="facts">
          <div><dt>Editor-in-Chief</dt><dd>Emrah Akman, Ordu University</dd></div>
          <div><dt>Current issue</dt><dd><a href="{J}issue/view/13" rel="noopener">Vol. 5 No. 2 (2026)</a> · 13 articles from 7 countries</dd></div>
        </dl>
        <div class="indexed"><span>Indexed in</span>ERIH PLUS · EBSCO Education Source · H. W. Wilson Education Full Text · Index Copernicus · MIAR · Türk Eğitim İndeksi · Google Scholar · Crossref</div>
        <div class="btns" style="margin-top:26px">
          <a class="btn btn-primary" href="journals.html">Journal details →</a>
          <a class="btn btn-outline" href="https://pedagogicalperspective.com" rel="noopener">Visit the journal</a>
        </div>
      </div>
    </article>
    <div class="soon"><div class="plus">+</div><div><strong>More titles coming.</strong> PedPer Publishing is preparing new journals in education and the social sciences. <a href="contact.html">Propose a journal</a>.</div></div>
  </div>
</section>

<section id="policies">
  <div class="wrap">
    <div class="sec-head">
      {label('03', 'Publishing principles')}
      <h2>Policies</h2>
      <p class="lead">These publisher-level principles apply to every PedPer journal. See all 27 policies, grouped by topic, on our policies page.</p>
    </div>
    <div class="pol-grid">
      <a class="pol" href="policies.html#access"><div class="ic">{IC['lock']}</div><h3>Open access &amp; copyright</h3><p>Immediate diamond open access under CC BY 4.0. Authors retain copyright; no copyright transfer is required.</p></a>
      <a class="pol" href="policies.html#ethics"><div class="ic">{IC['scale']}</div><h3>Publication ethics</h3><p>Our journals follow COPE guidelines in handling misconduct, conflicts of interest and authorship disputes.</p></a>
      <a class="pol" href="policies.html#review"><div class="ic">{IC['eye']}</div><h3>Peer review</h3><p>Double-blind review by at least two independent reviewers, with decisions based solely on scholarly merit.</p></a>
      <a class="pol" href="policies.html#ethics"><div class="ic">{IC['spark']}</div><h3>Generative AI</h3><p>AI tools cannot be listed as authors. Permitted AI use must be disclosed by authors, reviewers and editors.</p></a>
      <a class="pol" href="policies.html#review"><div class="ic">{IC['undo']}</div><h3>Corrections &amp; retractions</h3><p>Errors are corrected openly. Retractions and expressions of concern follow COPE retraction guidelines.</p></a>
      <a class="pol" href="policies.html#review"><div class="ic">{IC['mail']}</div><h3>Complaints &amp; appeals</h3><p>Authors may appeal editorial decisions. Complaints are handled fairly, confidentially and transparently.</p></a>
    </div>
    <div class="commit">
      <div><span>Signatory to</span>Ethical Research Involving Children (ERIC) · DORA · UN SDG Publishers Compact</div>
      <div><span>Preserved in</span>LOCKSS · CLOCKSS · PKP Preservation Network</div>
    </div>
  </div>
</section>

<section id="contact" style="padding:0">
  <div class="wrap">
    <div class="contact">
      <div>
        {label('04', 'Get in touch')}
        <h2>Contact</h2>
        <p class="lead">For publisher enquiries, partnerships or new journal proposals, write to us. For questions about a manuscript, please contact the journal's editorial office.</p>
        <div class="btns"><a class="btn btn-white" href="mailto:info@pedagogicalperspective.com">Email us →</a><a class="btn btn-ghost" href="contact.html">All contacts</a></div>
      </div>
      <dl class="c-card">
        <dt>Publisher enquiries</dt><dd><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a></dd>
        <dt>Editorial office</dt><dd><a href="mailto:editor@pedagogicalperspective.com">editor@pedagogicalperspective.com</a></dd>
        <dt>Phone</dt><dd><a href="tel:+904545022829">+90 454 502 28 29</a></dd>
      </dl>
    </div>
  </div>
</section>
'''
write('index.html', 'PedPer Publishing — Diamond open-access publishing in education',
      'PedPer Publishing is a diamond open-access academic publisher in education. Publisher of Pedagogical Perspective (eISSN 2822-4841).', home, ORG_LD)

# ================================================================ ABOUT
about = page_hero('About', 'About PedPer Publishing',
    'A Türkiye-based, scholar-led academic publisher dedicated to education — committed to transparent, ethical and inclusive scholarly publishing.') + f'''
<section class="sub-sec">
  <div class="wrap two">
    <div>
      {label('01', 'Who we are')}
      <h2>Scholar-led publishing for a global readership</h2>
    </div>
    <div class="prose">
      <p>PedPer Publishing publishes <strong>Pedagogical Perspective</strong> (eISSN 2822-4841), an international, peer-reviewed journal in education founded in 2022. Our aim is to disseminate rigorous educational research to a global readership, free of charge for both readers and authors.</p>
      <p>PedPer Publishing is operated by <strong>Scitera Information Technologies Ltd.</strong>, based in the Giresun Technology Development Zone, Türkiye, and is part of the Scitera family of academic tools and services.</p>
      <p>Our editorial and publishing practices are guided by the <strong>Committee on Publication Ethics (COPE)</strong>, and every policy is publicly documented.</p>
    </div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('02', 'What we stand for')}
    <h2>Our principles</h2>
    <div class="cards c4">
      {card('book', 'Diamond open access', 'All content is immediately and permanently free to read. No APCs, submission, review, page or colour charges.')}
      {card('shield', 'Rigorous review', 'Double-blind peer review by at least two independent reviewers, guided by COPE’s ethical guidelines.')}
      {card('scale', 'Editorial independence', 'A documented separation between publisher and Editor-in-Chief protects editorial decisions.')}
      {card('free', 'Non-commercial', 'Our journals accept no advertising and no commercial sponsorship that could influence editorial decisions.')}
    </div>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap two">
    <div>
      {label('03', 'Governance')}
      <h2>Separation of publisher and editor</h2>
      <p class="lead">To strengthen editorial integrity, accountability and independence, the Publisher and the Editor-in-Chief are different, independent people with distinct responsibilities.</p>
    </div>
    <div>
      <ul class="checks">
        <li><strong>No publisher influence.</strong> The publisher has no authority to influence, override or reverse editorial decisions.</li>
        <li><strong>Full editorial autonomy.</strong> The Editor-in-Chief decides independently on manuscript evaluation, peer review and publication.</li>
        <li><strong>Transparent conflicts of interest.</strong> Any potential conflict involving the publisher or the editor is managed under the journal’s COI policy.</li>
        <li><strong>Publicly documented.</strong> The structure is published openly for authors, reviewers and indexing bodies.</li>
      </ul>
      <div class="people" style="grid-template-columns:1fr 1fr;margin-top:28px">
        <div class="person"><div class="role">Publisher</div><h3>PedPer Publishing</h3><p>Operated by Scitera Information Technologies Ltd.<br>Giresun, Türkiye</p></div>
        <div class="person"><div class="role">Editor-in-Chief</div><h3>Emrah Akman</h3><p>Ordu University, Türkiye<br><a href="mailto:editor@pedagogicalperspective.com">editor@pedagogicalperspective.com</a></p></div>
      </div>
    </div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('04', 'Infrastructure')}
    <h2>Technical infrastructure</h2>
    <p class="lead">Established, community-trusted services support every stage of publishing, discovery and preservation.</p>
    <div class="cards">
      {card('server', 'Open Journal Systems', 'Submission, peer review and publishing platform developed by the Public Knowledge Project (PKP).')}
      {card('link', 'Crossref DOIs', 'Every article receives a persistent DOI under the prefix 10.29329, with interoperable metadata.')}
      {card('archive', 'LOCKSS · CLOCKSS · PKP PN', 'Distributed digital preservation networks secure long-term access to all published content.')}
      {card('feed', 'OAI-PMH &amp; feeds', 'Metadata is freely harvestable by libraries, aggregators and repositories; RSS and Atom feeds are available.')}
      {card('search', 'iThenticate', 'Plagiarism and similarity screening for every submission before peer review.')}
      {card('pen', 'Paperpal by Editage', 'Complimentary language proofreading for all accepted manuscripts.')}
    </div>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap two">
    <div>
      {label('05', 'Track record')}
      <h2>Publication history</h2>
      <p class="lead">Pedagogical Perspective has kept an uninterrupted biannual schedule since its founding. Consistent, timely publication is a key criterion for international indexing bodies.</p>
    </div>
    <ol class="timeline">
      <li><b>2022 · Volume 1</b><span>Founding year — Issues 1 and 2 (June, December)</span></li>
      <li><b>2023 · Volume 2</b><span>Issues 1 and 2 (June, December)</span></li>
      <li><b>2024 · Volume 3</b><span>Issues 1 and 2 (March, October) and a special issue from the TSTT 2023 conference</span></li>
      <li><b>2025 · Volume 4</b><span>Issues 1 and 2 (March, October), indexed in ERIH PLUS, and a special issue from the TSTT 2025 conference</span></li>
      <li class="now"><b>2026 · Volume 5</b><span>Issue 1 (March) and Issue 2 — 13 articles from 7 countries</span></li>
    </ol>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('06', 'Commitments')}
    <h2>Signatory to international initiatives</h2>
    <div class="cards">
      {card('child', 'Ethical Research Involving Children', 'Commitment to protecting the rights, welfare and safety of children in research — central for an education journal.', J + 'ethicalchildren')}
      {card('target', 'DORA', 'The San Francisco Declaration on Research Assessment: fair, content-based evaluation rather than journal-based metrics.', J + 'decresassess')}
      {card('leaf', 'UN SDG Publishers Compact', 'Promoting the Sustainable Development Goals through publishing — especially SDG 4, Quality Education.', J + 'sustainabledevgoals')}
    </div>
  </div>
</section>
''' + CTA
write('about.html', 'About us — PedPer Publishing',
      'PedPer Publishing is a Türkiye-based, scholar-led, diamond open-access publisher in education, operated by Scitera Information Technologies Ltd.', about)

# ================================================================ JOURNALS
issues = [('13', 'Vol. 5 No. 2 (2026)', 'Pedagogical Perspective', 'Current'),
          (None, 'Vol. 5 No. 1 (2026)', 'March 2026', None),
          (None, 'Vol. 4 No. 3 (2025)', 'Special issue · TSTT 2025: Advancing Teacher Training in the Digital Age', 'Special'),
          (None, 'Vol. 4 No. 2 (2025)', 'October 2025', None),
          (None, 'Vol. 4 No. 1 (2025)', 'March 2025', None),
          (None, 'Vol. 3 No. 3 (2024)', 'Special issue · TSTT 2023: Rethinking How We Train Teachers of Tomorrow', 'Special')]
iss_html = ''.join(
    f'<li><a href="{J}issue/view/{i}" rel="noopener"><span><b>{v}</b><small>{d}</small></span>{f"<span class=\"tag on\">{t}</span>" if t else ""}</a></li>' if i else
    f'<li><a href="{J}issue/archive" rel="noopener"><span><b>{v}</b><small>{d}</small></span>{f"<span class=\"tag\">{t}</span>" if t else ""}</a></li>'
    for i, v, d, t in issues)
sections = ['Educational Technology, AI &amp; Digital Learning', 'Teacher Education &amp; Professional Development', 'Language Education &amp; Applied Linguistics',
            'Early Childhood Education', 'Inclusive Education, Special Education &amp; Counseling', 'Social Studies, Citizenship &amp; Comparative Education',
            'STEM, Science &amp; Mathematics Education', 'Assessment, Measurement &amp; Evaluation', 'Learning Sciences', 'Research Methods &amp; Methodology',
            'Curriculum Design', 'Educational Policy', 'Higher Education Pedagogy', 'Multicultural &amp; Intercultural Education',
            'Educational Psychology &amp; Well-being', 'General Education Research']
journals = page_hero('Journals', 'Pedagogical Perspective',
    'An international, diamond open-access journal publishing English-language research and review articles in education since 2022.') + f'''
<section class="sub-sec">
  <div class="wrap">
    <article class="journal" style="margin-top:0">
      <div class="jcover" aria-hidden="true">
        <div class="hd"><img src="{A}pedper-logo-yatay-renkli.svg" alt=""><small>Vol. 5 · No. 2<br>2026</small></div>
        <h4>Pedagogical<br>Perspective</h4>
        <div class="art"><img src="{A}pedper-sembol-beyaz.svg" alt=""></div>
      </div>
      <div>
        <div class="eyebrow">Flagship journal</div>
        <h3 style="margin-top:6px">Pedagogical Perspective (PedPer)</h3>
        <div class="meta">
          <span class="tag">eISSN 2822-4841</span><span class="tag">DOI 10.29329</span><span class="tag">Biannual · March &amp; October</span><span class="tag on">Diamond OA · No APC</span>
        </div>
        <p>Pedagogical Perspective welcomes qualitative, quantitative, mixed-methods, theoretical and methodological studies that advance educational theory and practice and foster interdisciplinary and international dialogue.</p>
        <div class="btns" style="margin-top:24px"><a class="btn btn-primary" href="https://pedagogicalperspective.com" rel="noopener">Visit the journal →</a><a class="btn btn-outline" href="{J}about/submissions" rel="noopener">Make a submission</a></div>
      </div>
    </article>
  </div>
</section>

<section class="sub-sec alt" style="padding-top:72px">
  <div class="wrap two">
    <div>
      {label('01', 'At a glance')}
      <h2>Journal facts</h2>
      <p class="lead">Key information for authors, readers, librarians and indexing bodies.</p>
    </div>
    <table class="spec">
      <tr><th>Journal title</th><td>Pedagogical Perspective (PedPer)</td></tr>
      <tr><th>Online ISSN</th><td>2822-4841</td></tr>
      <tr><th>DOI prefix</th><td>10.29329 (Crossref)</td></tr>
      <tr><th>Founded</th><td>2022</td></tr>
      <tr><th>Frequency</th><td>Biannual — March and October, plus thematic issues</td></tr>
      <tr><th>Language</th><td>English only (British or American, used consistently)</td></tr>
      <tr><th>Peer review</th><td>Double-blind, at least two independent reviewers</td></tr>
      <tr><th>Access model</th><td>Diamond open access — no fees for authors or readers</td></tr>
      <tr><th>Licence &amp; copyright</th><td>CC BY 4.0 · authors retain copyright</td></tr>
      <tr><th>Preservation</th><td>LOCKSS, CLOCKSS, PKP Preservation Network</td></tr>
      <tr><th>Platform</th><td>Open Journal Systems (OJS)</td></tr>
      <tr><th>Editor-in-Chief</th><td>Emrah Akman, Ordu University, Türkiye</td></tr>
    </table>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap two">
    <div>
      {label('02', 'Aims &amp; scope')}
      <h2>What we publish</h2>
      <p class="lead">Contemporary scholarship in education — particularly teacher education, curriculum and instruction, learning sciences, social studies education and educational technologies. Submissions with strong methodological grounding, interdisciplinary relevance and international significance are particularly encouraged.</p>
    </div>
    <div>
      <ul class="checks">
        <li>Teacher education and professional development</li>
        <li>Curriculum design, instructional strategies and learning environments</li>
        <li>Educational technologies, AI in education, digital literacy and digital competencies</li>
        <li>Social studies, citizenship education and global competencies</li>
        <li>Learning sciences; cognitive and affective learning processes</li>
        <li>Assessment, measurement and educational evaluation</li>
        <li>Inclusive, equitable and multicultural education</li>
        <li>Interdisciplinary, comparative and international perspectives on education</li>
      </ul>
      <div class="eyebrow" style="margin-top:28px">Outside editorial scope</div>
      <ul class="checks no">
        <li>Manuscripts unrelated to education, pedagogy, teaching and learning, or educational policy and practice</li>
        <li>Purely descriptive reports without a clear research problem, method and scholarly contribution</li>
        <li>Non-scholarly opinion pieces without academic grounding or evidence</li>
      </ul>
    </div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('03', 'Article types')}
    <h2>Sections &amp; word limits</h2>
    <p class="lead">All sections, including Vision Papers, go through double-blind peer review. Editorials are published by invitation for thematic issues. Abstracts are 250–300 words.</p>
    <table class="spec">
      <thead><tr><th>Section</th><th>Scope</th><th>Main text</th></tr></thead>
      <tr><td><b>Research Articles</b></td><td>Original empirical studies — qualitative, quantitative, mixed-methods, experimental, design-based, methodological</td><td>6,000–10,000 words</td></tr>
      <tr><td><b>Review Articles</b></td><td>Systematic reviews, meta-analyses, scoping reviews, critical and integrative reviews</td><td>7,000–12,000 words</td></tr>
      <tr><td><b>Analysis / Case-Based</b></td><td>Case studies, practice-based investigations, policy analyses, context-specific qualitative studies</td><td>5,000–8,000 words</td></tr>
      <tr><td><b>Vision Papers</b></td><td>Forward-looking conceptual, theoretical or reflective contributions</td><td>4,000–7,000 words</td></tr>
    </table>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap">
    {label('04', 'Editorial team')}
    <h2>An international editorial board</h2>
    <p class="lead">Led by Editor-in-Chief Emrah Akman (Ordu University), the editorial board and Scientific Advisory Board bring together more than 60 scholars from over 25 countries, organised in subject sections.</p>
    <div class="kpis">
      <div class="kpi"><b>40+</b><span>Editorial board members</span></div>
      <div class="kpi"><b>25</b><span>Scientific advisors</span></div>
      <div class="kpi"><b>25+</b><span>Countries represented</span></div>
      <div class="kpi"><b>16</b><span>Subject sections</span></div>
    </div>
    <div class="chips lav">{''.join(f'<span>{s}</span>' for s in sections)}</div>
    <div class="more"><a class="link" href="{J}about/editorialTeam" rel="noopener">View the full editorial team →</a></div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('05', 'Abstracting &amp; indexing')}
    <h2>Where PedPer is indexed</h2>
    <div class="cards">
      <div class="card"><div class="eyebrow">Selective databases</div><div class="chips"><span>ERIH PLUS</span><span>EBSCO Education Source</span><span>EBSCO Education Source Ultimate</span><span>H. W. Wilson Education Full Text</span><span>Index Copernicus</span></div></div>
      <div class="card"><div class="eyebrow">Discovery &amp; directories</div><div class="chips"><span>Crossref</span><span>Google Scholar</span><span>Ulrich’s Periodicals Directory</span><span>MIAR</span><span>Türk Eğitim İndeksi</span></div></div>
      <div class="card"><div class="eyebrow">Metadata &amp; archiving</div><div class="chips"><span>OAI-PMH</span><span>LOCKSS</span><span>CLOCKSS</span><span>PKP PN</span><span>RSS / Atom</span></div></div>
    </div>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap">
    <div class="two" style="align-items:end">
      <div>
        {label('06', 'Issues')}
        <h2>Current &amp; recent issues</h2>
      </div>
      <p class="lead" style="margin-top:0">The current issue presents 13 articles from China, Ethiopia, Nepal, Norway, Türkiye, the United States and Zambia, from early childhood to higher education.</p>
    </div>
    <ul class="issues">{iss_html}</ul>
    <div class="more"><a class="link" href="{J}issue/archive" rel="noopener">Browse the full archive →</a></div>
  </div>
</section>

<section class="sub-sec" style="padding-top:0">
  <div class="wrap">
    <div class="soon" style="margin-top:0"><div class="plus">+</div><div><strong>Call for papers.</strong> Special issue “Curriculum Theory and Contemporary Educational Imaginaries: Posthuman Perspectives”. <a href="{J}announcement" rel="noopener">See announcements</a>.</div></div>
    <div class="soon"><div class="plus">+</div><div><strong>More titles coming.</strong> PedPer Publishing is preparing new journals in education and the social sciences. <a href="contact.html">Propose a journal</a>.</div></div>
  </div>
</section>
''' + CTA
write('journals.html', 'Journals — Pedagogical Perspective | PedPer Publishing',
      'Pedagogical Perspective (eISSN 2822-4841): aims and scope, article types, editorial board, indexing and issues.', journals)

# ================================================================ AUTHORS
authors = page_hero('For Authors', 'For authors',
    'Everything you need to publish with Pedagogical Perspective — from preparing your manuscript to peer review and publication.') + f'''
<section class="sub-sec">
  <div class="wrap">
    {label('01', 'Why publish with us')}
    <h2>Free, fair and visible</h2>
    <div class="cards c4">
      {card('free', 'No fees at any stage', 'No APCs, submission, review, page or colour charges. Readers never pay either.')}
      {card('pen', 'Free language proofreading', 'Accepted manuscripts receive complimentary proofreading via Paperpal by Editage.')}
      {card('link', 'DOI &amp; indexing', 'Crossref DOI for every article and inclusion in ERIH PLUS, EBSCO and more.')}
      {card('lock', 'You keep copyright', 'Published under CC BY 4.0 with no copyright transfer and no embargo on any version.')}
    </div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('02', 'Peer review workflow')}
    <h2>From submission to decision</h2>
    <p class="lead">A transparent, double-blind process with published target times. Author and reviewer identities remain confidential throughout.</p>
    <ol class="steps">
      <li><b>Technical check &amp; initial screening</b><em>≤ 3 business days</em><p>Scope, originality and ethics are assessed; out-of-scope manuscripts may be desk-rejected.</p></li>
      <li><b>Similarity screening</b><em>iThenticate</em><p>All submissions are checked for plagiarism and text recycling before review.</p></li>
      <li><b>External double-blind review</b><em>target ≤ 4 weeks</em><p>A Section Editor invites at least two independent reviewers.</p></li>
      <li><b>Decision, revision &amp; publication</b><em>15 days for revisions</em><p>The Editor-in-Chief decides; authors receive anonymised reports. Extensions are available on request.</p></li>
    </ol>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap two">
    <div>
      {label('03', 'Preparing your manuscript')}
      <h2>Submission essentials</h2>
      <p class="lead">Use the PedPer manuscript template and follow APA 7. Full details are in the Author Guidelines on the journal website.</p>
      <div class="btns"><a class="btn btn-primary" href="{J}authorguidelines" rel="noopener">Author guidelines →</a><a class="btn btn-outline" href="{J}templates" rel="noopener">Templates &amp; forms</a></div>
    </div>
    <div>
      <ul class="checks">
        <li><strong>Title page</strong> (Word) — author names, affiliations, ORCID IDs, corresponding author, declarations and ethics statement.</li>
        <li><strong>Blind manuscript</strong> (Word) — all author names, institutional identifiers and the ethics committee name removed.</li>
        <li><strong>Formatting</strong> — Aptos 11 pt, double-spaced, APA 7 headings and references; abstract of 250–300 words.</li>
        <li><strong>Figures</strong> — embedded in the text and uploaded separately as TIFF, PNG or EPS at 300 DPI or more.</li>
        <li><strong>Declarations</strong> — a Data Availability Statement, conflicts of interest and disclosure of any generative AI use.</li>
        <li><strong>English only</strong> — British or American spelling, applied consistently.</li>
      </ul>
    </div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap">
    {label('04', 'Integrity')}
    <h2>Originality &amp; responsible research</h2>
    <div class="kpis" style="grid-template-columns:repeat(2,1fr);max-width:620px">
      <div class="kpi"><b>≤ 20%</b><span>Overall similarity index<br>(excl. references &amp; quotations)</span></div>
      <div class="kpi"><b>≤ 3%</b><span>Similarity from a single source</span></div>
    </div>
    <div class="cards">
      {card('spark', 'Generative AI', 'AI tools cannot be authors. Any permitted use must be disclosed, and authors remain fully accountable.', J + 'generativeaip')}
      {card('child', 'Research involving children', 'As an ERIC signatory, we require ethical approval, consent and assent for research with participants under 18.', J + 'ethicalchildren')}
      {card('doc', 'Authorship &amp; contributorship', 'Every listed author must meet authorship criteria and take public responsibility for the work.', J + 'AuthorshipContributorship')}
    </div>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap">
    {label('05', 'Templates &amp; forms')}
    <h2>Downloads for authors</h2>
    <div class="cards c4">
      {card('doc', 'Manuscript template', 'Standard formatting template for the anonymised main document.', J + 'templates')}
      {card('doc', 'Title page form', 'Required separate document with author and declaration details.', J + 'templates')}
      {card('doc', 'Revision form', 'Point-by-point response for minor or major revision decisions.', J + 'templates')}
      {card('doc', 'Withdrawal form', 'For authors who need to withdraw a manuscript after submission.', J + 'templates')}
    </div>
  </div>
</section>
''' + CTA
authors = authors.replace('<a class="btn btn-ghost" href="authors.html">Author information</a>', f'<a class="btn btn-ghost" href="{J}authorguidelines" rel="noopener">Author guidelines</a>')
write('authors.html', 'For authors — PedPer Publishing',
      'How to publish in Pedagogical Perspective: no fees, double-blind peer review workflow, manuscript preparation, similarity thresholds and templates.', authors)

# ================================================================ POLICIES
groups = [
 ('access', 'Access &amp; licensing', 'How content is shared, licensed and preserved', [
   ('Open Access Policy', 'openaccesspolicy', 'All content is freely available immediately on publication, with no subscriptions, paywalls or embargoes, in line with the Budapest Open Access Initiative.'),
   ('Copyright &amp; Licensing Policy', 'copyrightpolicy', 'Authors retain copyright; articles are published under CC BY 4.0, covering reuse, self-archiving, text and data mining and third-party material.'),
   ('Article Processing Charges (APCs) / Fees', 'ArticleProcessingCharges', 'No APCs, submission, review, page or colour charges, and no access fees for readers.'),
   ('Repository Policy', 'RepositoryPolicy', 'Authors are encouraged to deposit any version — preprint, accepted or published — with no embargo.'),
   ('Archiving &amp; Preservation Policy', 'ArchivingPolicy', 'Long-term preservation through LOCKSS, CLOCKSS and the PKP Preservation Network, with persistent DOIs.')]),
 ('ethics', 'Ethics &amp; integrity', 'Standards for authors, reviewers, editors and the publisher', [
   ('Publication Ethics &amp; Malpractice', 'publicationethicsmalpractice', 'Responsibilities of all parties in the publication process, aligned with COPE principles and guidelines.'),
   ('Handling Allegations of Misconduct', 'handling', 'A fair, confidential and evidence-based process using COPE flowcharts to protect the scholarly record.'),
   ('Conflicts of Interest (COI) Statement', 'conflicts', 'Editors, reviewers, authors and the publisher must disclose any actual, potential or perceived conflicts.'),
   ('Authorship &amp; Contributorship', 'AuthorshipContributorship', 'Every listed author must meet authorship criteria and take public responsibility for the work.'),
   ('Plagiarism &amp; Similarity Policy', 'plagiarismpolicy', 'All submissions are screened with iThenticate; plagiarism, text recycling and duplicate submission are not tolerated.'),
   ('Generative AI Policy', 'generativeaip', 'AI tools cannot be authors; permitted use must be disclosed, with human accountability for all content.'),
   ('Data Availability Statement Policy', 'dataavailability', 'Every manuscript includes a Data Availability Statement explaining whether and how the data can be accessed.'),
   ('Ethical Research Involving Children', 'ethicalchildren', 'As an ERIC signatory, the journal sets requirements for ethical conduct and reporting of research with children.')]),
 ('review', 'Peer review &amp; editorial process', 'How manuscripts are handled, decided and corrected', [
   ('Peer Review Policy', 'peerreviewpolicy', 'Double-blind review by at least two independent reviewers, with published target times for each stage.'),
   ('Reviewer Guidelines', 'reviewerguidelines', 'Evaluation criteria, confidentiality and ethical responsibilities for reviewers, aligned with COPE.'),
   ('Editorial Board Governance Policy', 'edgovpolicy', 'Composition, roles, selection criteria, terms of service and accountability of the editorial board.'),
   ('Section Policy', 'sectionpolicy', 'Four sections — Research, Review, Analysis / Case-Based and Vision Papers — plus invited editorials.'),
   ('Thematic Issue Policy', 'thematicissuepolicy', 'How thematic issues are proposed, guest-edited and reviewed to the same standard as regular issues.'),
   ('Late &amp; Multiple Submission Policy', 'latesubpol', 'Manuscripts must be original and not under consideration elsewhere; late submissions are handled transparently.'),
   ('Language Policy', 'languagepolicy', 'Manuscripts are accepted in English only, in British or American style used consistently.'),
   ('Corrections, Retractions &amp; Expressions of Concern', 'corrections', 'How the scholarly record is corrected, following COPE retraction guidelines, including withdrawal requests.'),
   ('Complaints &amp; Appeals Policy', 'complaintsappealspolicy', 'Complaints and appeals against editorial decisions are handled fairly, confidentially and transparently.')]),
 ('commitments', 'Commitments', 'International initiatives we have signed', [
   ('Declaration on Research Assessment (DORA)', 'decresassess', 'Fair, transparent and content-based research assessment instead of journal-based metrics.'),
   ('UN SDG Publishers Compact', 'sustainabledevgoals', 'Advancing the 2030 Sustainable Development Goals through publishing, especially SDG 4 — Quality Education.')]),
 ('operations', 'Website &amp; operations', 'Privacy, accessibility and commercial independence', [
   ('Privacy Statement Policy', 'PrivacyStatementPolicy', 'How personal data is processed on the website, the OJS submission system and related services.'),
   ('Advertising &amp; Sponsorship Policy', 'advertisingpolicy', 'The journal is non-profit and accepts no advertising or commercial sponsorship.'),
   ('Accessibility Statement', 'accessibilitystatement', 'Commitment to making the website and published content accessible to all users, including persons with disabilities.')]),
]
total = sum(len(g[3]) for g in groups)
toc = ''.join(f'<a href="#{gid}">{gt} <span style="color:var(--muted);font-weight:400">({len(items)})</span></a>' for gid, gt, _, items in groups)
gh = ''
for gid, gt, gd, items in groups:
    lis = ''.join(f'<a href="{J}{slug}" rel="noopener"><h3>{t}</h3><p>{d}</p></a>' for t, slug, d in items)
    gh += f'<div class="pgroup" id="{gid}"><div class="pgroup-head"><h2>{gt}</h2><span>{gd}</span></div><div class="plist">{lis}</div></div>'
policies = page_hero('Policies', 'Publishing policies',
    f'{total} publicly documented policies guide every stage of publishing at PedPer, in line with COPE guidelines and international best practice.') + f'''
<section class="sub-sec">
  <div class="wrap with-toc">
    <aside class="toc" aria-label="Policy groups"><div class="eyebrow" style="margin-bottom:8px">On this page</div>{toc}</aside>
    <div>
      <p class="lead" style="margin-top:0;margin-bottom:12px">Each summary links to the full policy text on the Pedagogical Perspective website.</p>
      {gh}
    </div>
  </div>
</section>
''' + CTA
write('policies.html', 'Policies — PedPer Publishing',
      'Open access, ethics, peer review and editorial policies of PedPer Publishing and Pedagogical Perspective, aligned with COPE.', policies)

# ================================================================ CONTACT
contact = page_hero('Contact', 'Contact us',
    'Reach the right team quickly: publisher enquiries, the editorial office or submission support.') + f'''
<section class="sub-sec">
  <div class="wrap">
    <div class="people">
      <div class="person"><div class="role">Publisher enquiries</div><h3>PedPer Publishing</h3><p>Partnerships, new journal proposals, indexing and general questions about the publisher.</p><p><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a><br><a href="tel:+904545022829">+90 454 502 28 29</a></p></div>
      <div class="person"><div class="role">Editorial office</div><h3>Emrah Akman</h3><p>Editor-in-Chief, Ordu University. Editorial policy, peer review and publication decisions.</p><p><a href="mailto:editor@pedagogicalperspective.com">editor@pedagogicalperspective.com</a><br><a href="tel:+904522265200">+90 452 226 52 00</a> (ext. 5591)</p></div>
      <div class="person"><div class="role">Submission support</div><h3>Ceren Hatipoğlu</h3><p>Help with the submission system, templates, forms and the status of your manuscript.</p><p><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a><br><a href="tel:+904522265200">+90 452 226 52 00</a> (ext. 5542)</p></div>
    </div>
  </div>
</section>

<section class="sub-sec alt">
  <div class="wrap two">
    <div>
      {label('01', 'Addresses')}
      <h2>Where to find us</h2>
      <p class="lead">Postal correspondence for the publisher and the editorial office.</p>
    </div>
    <div class="cards c2" style="margin-top:0">
      <div class="card"><div class="ic">{IC['server']}</div><h3>Publisher’s executive office</h3><p>PedPer Publishing<br>Operated by Scitera Information Technologies Ltd.<br>Pazarsuyu Village, 2nd Organized Industrial Zone<br>4th Street, Building No. 5<br>Giresun Technology Development Zone<br>Ground Floor, Office Z12<br>Giresun, Türkiye</p></div>
      <div class="card"><div class="ic">{IC['book']}</div><h3>Editorial office</h3><p>Pedagogical Perspective<br>Ordu University, Faculty of Education<br>Department of Educational Sciences<br>1st Floor, Cumhuriyet Campus<br>Altınordu, Ordu, Türkiye</p></div>
    </div>
  </div>
</section>

<section class="sub-sec">
  <div class="wrap">
    {label('02', 'Who to contact')}
    <h2>Find the right channel</h2>
    <table class="spec">
      <thead><tr><th>Topic</th><th>Contact</th></tr></thead>
      <tr><td>Partnerships, new journal proposals, publisher questions</td><td><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a></td></tr>
      <tr><td>Editorial decisions, peer review, ethics concerns</td><td><a href="mailto:editor@pedagogicalperspective.com">editor@pedagogicalperspective.com</a></td></tr>
      <tr><td>Appeals against editorial decisions</td><td><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a> — see the <a href="{J}complaintsappealspolicy" rel="noopener">Complaints &amp; Appeals Policy</a></td></tr>
      <tr><td>Submission system, templates and forms</td><td><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a></td></tr>
      <tr><td>Indexing enquiries</td><td><a href="mailto:info@pedagogicalperspective.com">info@pedagogicalperspective.com</a></td></tr>
    </table>
  </div>
</section>
''' + CTA
write('contact.html', 'Contact — PedPer Publishing',
      'Contact PedPer Publishing and the Pedagogical Perspective editorial office: emails, phone numbers and postal addresses.', contact, ORG_LD)

print('built', sorted(os.listdir(OUT)))

# ---------------------------------------------------------------- make every page self-contained
import base64, re
css_txt = open(OUT + '/assets/style.css').read()
def data_uri(fname):
    return 'data:image/svg+xml;base64,' + base64.b64encode(open(OUT + '/assets/' + fname, 'rb').read()).decode()
for name in ['index.html', 'about.html', 'journals.html', 'authors.html', 'policies.html', 'contact.html']:
    p = f'{OUT}/{name}'
    h = open(p).read()
    h = h.replace('<link rel="stylesheet" href="assets/style.css">', '<style>' + css_txt + '</style>')
    h = re.sub(r'(src|href)="assets/([\w.-]+\.svg)"', lambda m: f'{m.group(1)}="{data_uri(m.group(2))}"', h)
    assert 'assets/' not in h.replace('https://pedper.com/assets/', ''), name
    open(p, 'w').write(h)
print('inlined')
