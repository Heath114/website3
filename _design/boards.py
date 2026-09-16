from brands import B, MARKS, FONTS

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1600px;font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased}
.board{position:relative;width:1600px;overflow:hidden}
.cover{height:1200px}.wide{height:1000px}
.mark svg{width:100%;height:100%;display:block}
.sh{box-shadow:0 40px 80px -30px rgba(0,0,0,.45),0 12px 24px -12px rgba(0,0,0,.25)}
.phone{width:340px;height:700px;border-radius:52px;background:#0b0b0c;padding:12px;position:absolute}
.phone .scr{width:100%;height:100%;border-radius:42px;overflow:hidden;position:relative}
.phone .notch{position:absolute;top:12px;left:50%;transform:translateX(-50%);width:96px;height:26px;border-radius:14px;background:#0b0b0c;z-index:3}
.sbar{display:flex;justify-content:space-between;padding:18px 30px 0;font:600 14px Inter}
.browser{position:absolute;border-radius:14px;overflow:hidden;background:#fff}
.browser .bar{height:38px;background:#ecebe8;display:flex;align-items:center;gap:8px;padding:0 16px}
.browser .bar i{width:11px;height:11px;border-radius:50%;background:#d0cec9;display:block}
.browser .bar u{margin-left:18px;flex:1;height:22px;border-radius:6px;background:#fff;text-decoration:none;font:500 12px Inter;color:#8a877f;display:flex;align-items:center;padding-left:12px}
.grain:after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.05) 1px,transparent 1px);background-size:4px 4px;pointer-events:none}
"""

def mark(key, size, color, style=''):
    return f'<div class="mark" style="width:{size}px;height:{size}px;color:{color};{style}">{MARKS[key]}</div>'

def word(key, size, color, extra=''):
    b = B[key]
    ls = '.18em' if b['word'].isupper() and key in ('layali', 'mada') else '-.02em'
    return f'<div style="font-family:{b["latin"]};font-weight:{b["lw"]};font-size:{size}px;line-height:1;letter-spacing:{ls};color:{color};{extra}">{b["word"]}</div>'

def arab(key, size, color, extra=''):
    b = B[key]
    return f'<div dir="rtl" style="font-family:{b["arabic"]};font-weight:700;font-size:{size}px;line-height:1.25;color:{color};{extra}">{b["ar"]}</div>'

def lockup(key, size, color, gap=None, arabic_color=None):
    g = gap or size * .35
    return (f'<div style="display:flex;align-items:center;gap:{g}px">{mark(key, size*1.05, color)}'
            f'<div style="display:flex;flex-direction:column;gap:{size*.12}px">{word(key, size*.62, color)}'
            f'{arab(key, size*.42, arabic_color or color, "opacity:.85;text-align:left")}</div></div>')

def page(inner, cls):
    return f'<!doctype html><html><head><meta charset="utf-8"><link href="{FONTS}" rel="stylesheet"><style>{BASE_CSS}</style></head><body><div class="board {cls}">{inner}</div></body></html>'

# ---------------------------------------------------------------- templated
def logo_board(key):
    b = B[key]; bg, fg, ac = b['bg'], b['fg'], b['accent']
    sbg, sfg, abg, afg = b['panels']
    inner = f'''
    <div style="position:absolute;left:0;top:0;width:1000px;height:1000px;background:{bg};display:flex;align-items:center;justify-content:center">
      {lockup(key, 150, fg)}
      <div style="position:absolute;left:56px;bottom:48px;font:500 14px Inter;letter-spacing:.14em;text-transform:uppercase;color:{fg};opacity:.6">{b['name']} · Primary lockup</div>
    </div>
    <div style="position:absolute;left:1000px;top:0;width:600px;height:500px;background:{sbg};display:flex;align-items:center;justify-content:center">
      {mark(key, 190, sfg)}
      <div style="position:absolute;left:40px;bottom:34px;font:500 13px Inter;letter-spacing:.14em;text-transform:uppercase;color:{sfg};opacity:.55">Symbol</div>
    </div>
    <div style="position:absolute;left:1000px;top:500px;width:600px;height:500px;background:{abg};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
      {arab(key, 150, afg)}
      <div style="position:absolute;left:40px;bottom:34px;font:500 13px Inter;letter-spacing:.14em;text-transform:uppercase;color:{afg};opacity:.6">Arabic wordmark</div>
    </div>'''
    return page(inner, 'wide')

def system_board(key):
    b = B[key]
    sw = ''.join(f'''<div style="flex:1;background:{hx};display:flex;flex-direction:column;justify-content:flex-end;padding:26px;color:{'#fff' if i in (0,) or hx in ('#131316','#1b2740','#161616','#2b2623','#2b2926','#0e4b4a','#4f5b2a','#5d3f28','#2a1a12','#b4532b','#9b5a3a','#c4553a','#3f6f86','#56613f','#a44a2a','#5f8a8b') else '#161616'}">
        <div style="font:600 15px Inter">{nm}</div><div style="font:400 14px Inter;opacity:.75;margin-top:4px">{hx.upper()}</div></div>'''
        for i, (nm, hx) in enumerate(b['c']))
    light = b['c'][2][1] if key != 'dawra' else '#f4f4f0'
    ink = '#161616' if key != 'layali' else '#1b2740'
    inner = f'''
    <div style="position:absolute;inset:0;background:{light}"></div>
    <div style="position:absolute;left:0;top:0;width:1600px;height:360px;display:flex">{sw}</div>
    <div style="position:absolute;left:70px;top:430px;width:760px;color:{ink}">
      <div style="font:500 14px Inter;letter-spacing:.14em;text-transform:uppercase;opacity:.55;margin-bottom:22px">Latin</div>
      <div style="font-family:{b['latin']};font-weight:{b['lw']};font-size:150px;line-height:.95">Aa Bb</div>
      <div style="font-family:{b['latin']};font-weight:{b['lw']};font-size:30px;margin-top:26px;line-height:1.25">{b['name']}<br>0123456789 · &amp;?!</div>
    </div>
    <div dir="rtl" style="position:absolute;right:70px;top:430px;width:640px;color:{ink};text-align:right">
      <div dir="ltr" style="font:500 14px Inter;letter-spacing:.14em;text-transform:uppercase;opacity:.55;margin-bottom:22px">Arabic</div>
      <div style="font-family:{b['arabic']};font-weight:700;font-size:130px;line-height:1.35">أ ب ج</div>
      <div style="font-family:{b['arabic']};font-weight:400;font-size:34px;margin-top:34px;line-height:1.5">{b['ar']} · ٠١٢٣٤٥٦٧٨٩</div>
    </div>
    <div style="position:absolute;left:70px;right:70px;bottom:52px;border-top:1px solid {ink}22;padding-top:22px;font:400 17px Inter;color:{ink};opacity:.75;max-width:900px">{b['type_note']}</div>'''
    return page(inner, 'wide')
