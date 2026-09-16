# Generate project-<key>.html case study pages from cases.py, using work.html's header and footer.
import os, re, html
from cases import CASES
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
work = open(os.path.join(ROOT, 'work.html'), encoding='utf-8').read()
head = work[:work.index('<body>')]
header = re.search(r'<header>.*?</header>', work, re.S).group(0).replace(' class="active"', '')
footer = re.search(r'<footer>.*?</footer>', work, re.S).group(0)
e = html.escape

for i, c in enumerate(CASES):
    nxt = CASES[(i + 1) % len(CASES)]
    k = c['key']
    h = re.sub(r'<title>.*?</title>', f'<title>{e(c["name"])} - Naqsh Studio</title>', head)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{e(c["lede"])}">', h)
    h = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="assets/img/work/{k}-cover.jpg">', h)
    stats = ''.join(f'<div class="stat" data-r><div class="n">{e(n)}</div><div class="l">{e(l)}</div></div>' for n, l in c['stats'])
    body = f'''<body class="case">
{header}

<div class="page-hero case-hero">
  <div class="wrap">
    <a href="work.html" class="mono case-back">&larr; All work</a>
    <div class="case-title">
      <h1 class="display">{e(c["name"])}</h1>
      <span class="case-ar" dir="rtl" lang="ar">{c["ar"]}</span>
    </div>
    <p class="lede">{e(c["lede"])}</p>
    <dl class="case-meta">
      <div><dt>Client</dt><dd>{e(c["client"])}</dd></div>
      <div><dt>Year</dt><dd>{c["year"]}</dd></div>
      <div><dt>Services</dt><dd>{"<br>".join(map(e, c["services"]))}</dd></div>
      <div><dt>Team</dt><dd>{"<br>".join(map(e, c["team"]))}</dd></div>
    </dl>
  </div>
</div>

<section class="case-media first"><div class="wrap"><img src="assets/img/work/{k}-cover.jpg" alt="{e(c["name"])}: key visual" data-r></div></section>

<section class="case-text"><div class="wrap case-cols">
  <div data-r><span class="mono">The brief</span><p>{e(c["brief"])}</p></div>
  <div data-r><span class="mono">What we did</span><p>{e(c["approach"])}</p></div>
</div></section>

<section class="case-media"><div class="wrap"><figure data-r><img src="assets/img/work/{k}-logo.jpg" alt="{e(c["captions"][0])}"><figcaption class="mono">{e(c["captions"][0])}</figcaption></figure></div></section>

<section class="case-stats"><div class="wrap"><div class="stats">{stats}</div></div></section>

<section class="case-media"><div class="wrap"><figure data-r><img src="assets/img/work/{k}-system.jpg" alt="{e(c["captions"][1])}"><figcaption class="mono">{e(c["captions"][1])}</figcaption></figure></div></section>
<section class="case-media"><div class="wrap"><figure data-r><img src="assets/img/work/{k}-app.jpg" alt="{e(c["captions"][2])}"><figcaption class="mono">{e(c["captions"][2])}</figcaption></figure></div></section>

<section class="case-quote"><div class="wrap statement">
  <blockquote data-r>&ldquo;{e(c["quote"][0])}&rdquo;</blockquote>
  <p class="mono" data-r>{e(c["quote"][1])}</p>
</div></section>

<a class="case-next" href="project-{nxt["key"]}.html">
  <div class="wrap">
    <span class="mono">Next project</span>
    <div class="case-next-row"><h2 class="display">{e(nxt["name"])}</h2><img src="assets/img/work/{nxt["key"]}-cover.jpg" alt=""></div>
  </div>
</a>

{footer}
<script src="assets/js/main.js"></script>
</body>
</html>
'''
    open(os.path.join(ROOT, f'project-{k}.html'), 'w', encoding='utf-8').write(h + body)
    print('wrote project-' + k + '.html')
