# Render the Naqsh portfolio boards to assets/img/work/<brand>-<board>.jpg
# usage: node-free: python3 render.py [brand ...] [--only board,board]
import sys, os, json, subprocess, tempfile, io
from PIL import Image
import boards
try:
    import covers
except ImportError:
    covers = None

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'assets', 'img', 'work')
BUILD = os.path.join(HERE, 'build')
os.makedirs(OUT, exist_ok=True); os.makedirs(BUILD, exist_ok=True)

args = [a for a in sys.argv[1:] if not a.startswith('--')]
only = next((a.split('=')[1].split(',') for a in sys.argv[1:] if a.startswith('--only=')), None)
keys = args or list(boards.B)
jobs = []
for k in keys:
    fns = {'logo': boards.logo_board, 'system': boards.system_board}
    if covers:
        fns['cover'] = getattr(covers, 'cover_' + k, None)
        fns['app'] = getattr(covers, 'app_' + k, None)
    for name, fn in fns.items():
        if not fn or (only and name not in only): continue
        path = os.path.join(BUILD, f'{k}-{name}.html')
        open(path, 'w').write(fn(k) if name in ('logo', 'system') else fn())
        jobs.append((path, os.path.join(BUILD, f'{k}-{name}.png')))

pw = os.environ.get('PW_DIR')
script = """
const { chromium } = require('playwright-core');
const jobs = %s;
(async () => {
  const b = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
  const p = await b.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 1 });
  for (const [src, out] of jobs) {
    await p.goto('file://' + src, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(250);
    await p.locator('.board').screenshot({ path: out });
  }
  await b.close();
})();
""" % json.dumps(jobs)
js = os.path.join(pw, 'render-job.js'); open(js, 'w').write(script)
subprocess.run(['node', js], check=True, cwd=pw)
for src, png in jobs:
    name = os.path.basename(png)[:-4]
    Image.open(png).convert('RGB').save(os.path.join(OUT, name + '.jpg'), quality=86, optimize=True, progressive=True)
    print('rendered', name)
