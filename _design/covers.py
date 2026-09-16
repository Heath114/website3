# Hand-built application boards for each client: cover (1600x1200) and app (1600x1000).
from boards import page, mark, word, arab, lockup, B
IMG = '../../assets/img/'

def pouch(bg, label_bg, ink, origin, weight, x, y, rot, w=380, h=560):
    return f'''<div class="sh" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);background:{bg};border-radius:18px 18px 26px 26px">
      <div style="height:46px;border-bottom:2px dashed rgba(0,0,0,.18);background:linear-gradient(rgba(255,255,255,.08),transparent)"></div>
      <div style="position:absolute;left:34px;right:34px;top:120px;bottom:70px;background:{label_bg};border-radius:8px;display:flex;flex-direction:column;align-items:center;padding:40px 22px;text-align:center;color:{ink}">
        {mark('rabwa', 84, ink)}
        {word('rabwa', 58, ink, 'margin-top:22px')}
        {arab('rabwa', 34, ink, 'margin-top:6px')}
        <div style="width:60px;height:2px;background:{ink};opacity:.35;margin:24px 0 18px"></div>
        <div style="font:600 15px Inter;letter-spacing:.16em;text-transform:uppercase">{origin}</div>
        <div style="font:400 14px Inter;opacity:.7;margin-top:8px">Washed · Light roast</div>
        <div style="margin-top:auto;font:600 14px Inter;letter-spacing:.1em">{weight}</div>
      </div></div>'''

def cover_rabwa():
    c = B['rabwa']
    return page(f'''<div class="grain" style="position:absolute;inset:0;background:#d8c7a9"></div>
      <div style="position:absolute;right:-120px;top:-60px;width:760px;height:1320px;background:url({IMG}work-1.jpg) center/cover;"></div>
      <div style="position:absolute;right:-120px;top:-60px;width:760px;height:1320px;background:linear-gradient(90deg,#d8c7a9 0%,rgba(216,199,169,0) 40%)"></div>
      {pouch('#2a1a12', '#efe4cf', '#2a1a12', 'Ethiopia · Guji', '250 G', 150, 330, -4)}
      {pouch('#c4553a', '#efe4cf', '#2a1a12', 'Colombia · Huila', '250 G', 500, 290, 3)}
      <div class="sh" style="position:absolute;left:760px;top:760px;width:190px;height:190px;border-radius:50%;background:#efe4cf;color:#2a1a12;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-12deg);text-align:center">
        <div style="font:700 13px Inter;letter-spacing:.2em">ROASTED IN</div><div style="font-family:'Fraunces';font-weight:700;font-size:34px;line-height:1.05;margin-top:6px">Jabal<br>Amman</div>
        <div dir="rtl" style="font-family:'Reem Kufi';font-size:20px;margin-top:6px">جبل عمّان</div></div>
      <div style="position:absolute;left:150px;top:120px">{lockup('rabwa', 70, '#2a1a12')}</div>''', 'cover')

def app_rabwa():
    return page(f'''<div class="grain" style="position:absolute;inset:0;background:#8a8f6a"></div>
      <div class="sh" style="position:absolute;left:170px;top:210px;width:300px;height:420px;background:#efe4cf;clip-path:polygon(0 0,100% 0,88% 100%,12% 100%);border-radius:6px"></div>
      <div style="position:absolute;left:190px;top:330px;width:260px;height:150px;background:#c4553a;clip-path:polygon(0 0,100% 0,96% 100%,4% 100%);display:flex;align-items:center;justify-content:center">{mark('rabwa', 90, '#efe4cf')}</div>
      <div class="sh" style="position:absolute;left:150px;top:180px;width:340px;height:40px;background:#2a1a12;border-radius:8px"></div>
      <div class="sh" style="position:absolute;left:620px;top:220px;width:560px;height:330px;background:#efe4cf;border-radius:14px;padding:40px;color:#2a1a12;transform:rotate(-3deg)">
        <div style="display:flex;justify-content:space-between;align-items:flex-start">{lockup('rabwa', 46, '#2a1a12')}<div style="font:600 13px Inter;letter-spacing:.16em">LOYALTY CARD</div></div>
        <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:18px;margin-top:40px">{''.join(f'<div style="aspect-ratio:1;border-radius:50%;border:2px solid #2a1a12;display:flex;align-items:center;justify-content:center;{"background:#c4553a;border-color:#c4553a" if i<6 else ""}">{mark("rabwa", 40, "#efe4cf") if i<6 else ""}</div>' for i in range(10))}</div>
        <div style="font:400 14px Inter;margin-top:22px;opacity:.75">The tenth cup is on us.</div></div>
      <div class="sh" style="position:absolute;left:720px;top:620px;width:440px;height:250px;background:#2a1a12;border-radius:12px;padding:36px;color:#efe4cf;transform:rotate(4deg)">
        <div style="font-family:'Fraunces';font-weight:700;font-size:30px">Hala Mansour</div><div style="font:400 15px Inter;opacity:.7;margin-top:4px">Head Roaster</div>
        <div style="position:absolute;left:36px;bottom:34px;font:400 14px Inter;line-height:1.6;opacity:.85">Rainbow Street, Jabal Amman<br>hala@rabwa.coffee</div>
        <div style="position:absolute;right:34px;bottom:34px">{mark('rabwa', 60, '#c4553a')}</div></div>
      <div style="position:absolute;left:1240px;top:240px;width:260px;color:#efe4cf;font:400 16px Inter;line-height:1.6">
        <div style="font:600 13px Inter;letter-spacing:.16em;margin-bottom:14px">CAFÉ SYSTEM</div>Cups, loyalty cards and staff stationery across three cafés, all built from the hill symbol and two colours.</div>''', 'wide')

def phone(inner, x, y, rot=0, bg='#fff'):
    return f'<div class="phone sh" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)"><div class="scr" style="background:{bg}"><div class="notch"></div>{inner}</div></div>'

def cover_aafia():
    t, m, cor = '#0e4b4a', '#cde8da', '#ff7a59'
    s1 = f'''<div class="sbar" style="color:{t}"><span>9:41</span><span>●●●</span></div>
      <div style="padding:26px 24px;font-family:Manrope;color:{t}">
        <div style="display:flex;justify-content:space-between;align-items:center">{mark('aafia', 34, t)}<div style="width:38px;height:38px;border-radius:50%;background:{m};font:700 14px Manrope;display:flex;align-items:center;justify-content:center">HM</div></div>
        <div style="font-size:15px;opacity:.6;margin-top:24px">Good morning,</div><div style="font-size:30px;font-weight:800">Hala</div>
        <div style="background:{t};color:#fff;border-radius:24px;padding:22px;margin-top:22px">
          <div style="font-size:12px;letter-spacing:.12em;opacity:.7">NEXT APPOINTMENT</div>
          <div style="font-size:21px;font-weight:800;margin-top:8px">Dr. Sami Haddad</div><div style="font-size:14px;opacity:.8">Paediatrics · Khalda clinic</div>
          <div style="display:flex;gap:10px;margin-top:18px"><div style="background:rgba(255,255,255,.14);border-radius:12px;padding:8px 12px;font-size:13px;font-weight:700">Tue 14 Oct</div><div style="background:{cor};border-radius:12px;padding:8px 12px;font-size:13px;font-weight:700">10:30</div></div></div>
        <div style="font-size:15px;font-weight:800;margin-top:26px">Book again</div>
        {''.join(f'<div style="display:flex;align-items:center;gap:12px;margin-top:14px;background:#f1f7f3;border-radius:18px;padding:12px"><div style="width:42px;height:42px;border-radius:14px;background:{m};display:flex;align-items:center;justify-content:center;font-weight:800">{i}</div><div><div style="font-size:14px;font-weight:700">{n}</div><div style="font-size:12px;opacity:.6">{s}</div></div></div>' for i,n,s in [('RK','Dr. Rula Khatib','Family medicine'),('OA','Dr. Omar Atallah','Dermatology')])}
      </div>'''
    days = ''.join(f'<div style="border-radius:14px;padding:10px 0;text-align:center;{"background:"+t+";color:#fff" if d=="14" else "background:#f1f7f3"}"><div style="font-size:11px;opacity:.7">{w}</div><div style="font-size:17px;font-weight:800">{d}</div></div>' for w,d in [('Mon','13'),('Tue','14'),('Wed','15'),('Thu','16')])
    slots = ''.join(f'<div style="border-radius:14px;padding:12px 0;text-align:center;font-size:14px;font-weight:700;{"background:"+cor+";color:#fff" if s=="10:30" else "border:1.5px solid #d6e7de"}">{s}</div>' for s in ['09:00','09:30','10:00','10:30','11:00','12:30','13:00','15:30','16:00'])
    s2 = f'''<div class="sbar" style="color:{t}"><span>9:41</span><span>●●●</span></div>
      <div style="padding:26px 24px;font-family:Manrope;color:{t}">
        <div style="font-size:14px;opacity:.6">← Paediatrics</div><div style="font-size:26px;font-weight:800;margin-top:10px;line-height:1.1">Choose a time</div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:22px">{days}</div>
        <div style="font-size:13px;font-weight:700;margin-top:24px;opacity:.6">MORNING</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px">{slots}</div>
        <div style="background:{t};color:#fff;border-radius:18px;padding:18px;text-align:center;font-weight:800;margin-top:40px">Confirm 10:30</div>
        <div dir="rtl" style="font-family:'Readex Pro';text-align:center;font-size:14px;margin-top:14px;opacity:.6">تأكيد الموعد</div></div>'''
    return page(f'''<div style="position:absolute;inset:0;background:{m}"></div>
      <div style="position:absolute;left:-200px;top:520px;width:900px;height:900px;border-radius:50%;background:#bfe0cf"></div>
      <div style="position:absolute;left:110px;top:130px">{lockup('aafia', 86, t)}</div>
      <div style="position:absolute;left:110px;top:330px;width:470px;font:500 22px Manrope;color:{t};line-height:1.45">A patient app for five family clinics. Book, reschedule and see results in Arabic or English.</div>
      <div style="position:absolute;left:110px;bottom:120px;display:flex;gap:40px;color:{t};font-family:Manrope">
        <div><div style="font-size:64px;font-weight:800">58%</div><div style="font-size:15px;opacity:.7">of bookings now in the app</div></div>
        <div><div style="font-size:64px;font-weight:800">4.8</div><div style="font-size:15px;opacity:.7">App Store rating</div></div></div>
      {phone(s1, 700, 240, -4)}{phone(s2, 1110, 190, 4)}''', 'cover')

def app_aafia():
    t, m, cor = '#0e4b4a', '#cde8da', '#ff7a59'
    return page(f'''<div style="position:absolute;inset:0;background:#e9e7e2"></div>
      <div style="position:absolute;left:0;right:0;bottom:0;height:260px;background:#d7d4cd"></div>
      <div class="sh" style="position:absolute;left:140px;top:120px;width:560px;height:640px;background:{t};border-radius:10px;padding:56px;color:#fff;font-family:Manrope">
        {lockup('aafia', 70, '#fff')}
        {''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.2);padding:22px 0;margin-top:{36 if i==0 else 0}px"><div><div style="font-size:24px;font-weight:800">{e}</div><div dir="rtl" style="font-family:Readex Pro;font-size:20px;opacity:.75;text-align:left">{a}</div></div><div style="width:54px;height:54px;border-radius:50%;background:{cor if i==0 else "rgba(255,255,255,.12)"};display:flex;align-items:center;justify-content:center;font-size:22px">{arr}</div></div>' for i,(e,a,arr) in enumerate([('Reception','الاستقبال','↑'),('Paediatrics','طب الأطفال','→'),('Laboratory','المختبر','←'),('Pharmacy','الصيدلية','↓')]))}
      </div>
      <div class="sh" style="position:absolute;left:800px;top:170px;width:620px;height:330px;background:#fff;border-radius:18px;padding:40px;font-family:Manrope;color:{t};transform:rotate(-2deg)">
        <div style="display:flex;justify-content:space-between">{lockup('aafia', 40, t)}<div style="font-size:13px;letter-spacing:.14em;opacity:.6">APPOINTMENT CARD</div></div>
        <div style="font-size:14px;opacity:.6;margin-top:42px">Your next visit</div><div style="font-size:34px;font-weight:800">Tuesday 14 October, 10:30</div>
        <div style="font-size:16px;margin-top:8px">Dr. Sami Haddad · Khalda clinic</div>
        <div style="position:absolute;right:40px;bottom:36px;width:70px;height:70px;border-radius:16px;background:{cor}"></div></div>
      <div style="position:absolute;left:830px;top:580px;display:flex;gap:28px">
        {''.join(f'<div class="sh" style="width:120px;height:120px;border-radius:28px;background:{bg};display:flex;align-items:center;justify-content:center">{mark("aafia", 64, fg)}</div>' for bg,fg in [(t,'#fff'),(m,t),(cor,'#fff'),('#fff',t)])}
      </div>
      <div style="position:absolute;left:830px;top:740px;font:500 16px Manrope;color:{t};opacity:.75">Wayfinding, patient stationery and app icon set</div>''', 'wide')

def browser(inner, x, y, w, h, url, rot=0):
    return f'<div class="browser sh" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><div class="bar"><i></i><i></i><i></i><u>{url}</u></div><div style="position:relative;height:{h-38}px;overflow:hidden">{inner}</div></div>'

def cover_mada():
    ink, con, rust = '#161616', '#dcd8d0', '#9b5a3a'
    site = f'''<div style="background:#f4f2ee;height:100%;font-family:'Space Grotesk';color:{ink}">
      <div style="display:flex;justify-content:space-between;align-items:center;padding:26px 40px">{lockup('mada', 34, ink)}<div style="display:flex;gap:34px;font-size:15px"><span>Projects</span><span>Practice</span><span>Journal</span><span>Contact</span><span dir="rtl" style="font-family:'IBM Plex Sans Arabic'">عربي</span></div></div>
      <div style="display:grid;grid-template-columns:1fr 1.25fr;gap:40px;padding:30px 40px">
        <div><div style="font-size:14px;letter-spacing:.14em;color:{rust}">SELECTED PROJECT · 2024</div>
          <div style="font-size:62px;line-height:1;margin-top:18px;letter-spacing:-.02em">House on a<br>limestone ridge</div>
          <div style="font-size:17px;line-height:1.55;margin-top:24px;opacity:.75;max-width:30ch">A family home in Dabouq, built into the slope so every room faces west over the valley.</div>
          <div style="display:flex;gap:40px;margin-top:40px;font-size:14px"><div><div style="opacity:.55">Area</div><div style="font-size:24px">412 m²</div></div><div><div style="opacity:.55">Status</div><div style="font-size:24px">Completed</div></div></div></div>
        <div style="height:470px;background:url({IMG}work-3.jpg) center/cover"></div></div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:10px 40px">{''.join(f'<div style="border-top:1px solid {ink};padding-top:12px;font-size:14px"><div style="opacity:.5">0{i+1}</div><div style="font-size:18px;margin-top:4px">{n}</div></div>' for i,n in enumerate(['Ridge House','Weibdeh Studios','Courtyard Villa','Abdoun Terraces']))}</div></div>'''
    return page(f'''<div style="position:absolute;inset:0;background:{rust}"></div>
      <div style="position:absolute;left:0;top:0;width:1600px;height:1200px;background:repeating-linear-gradient(90deg,rgba(255,255,255,.06) 0 1px,transparent 1px 80px),repeating-linear-gradient(0deg,rgba(255,255,255,.06) 0 1px,transparent 1px 80px)"></div>
      {browser(site, 140, 150, 1320, 900, 'mada-architects.jo')}''', 'cover')

def app_mada():
    ink, con, rust = '#161616', '#dcd8d0', '#9b5a3a'
    return page(f'''<div style="position:absolute;inset:0;background:#b9b3a7"></div>
      <div class="sh" style="position:absolute;left:150px;top:90px;width:560px;height:790px;background:#f7f5f1;padding:60px;font-family:'Space Grotesk';color:{ink};transform:rotate(-2deg)">
        {lockup('mada', 44, ink)}
        <div style="margin-top:90px;font-size:15px;line-height:1.7;opacity:.8">14 October 2026<br><br>Dear Mr. Nasser,<br><br>Please find enclosed the revised site plan for the Ridge House, including the retaining wall on the northern boundary and the adjusted terrace levels.</div>
        <div style="position:absolute;left:60px;right:60px;bottom:56px;border-top:1px solid {ink};padding-top:16px;display:flex;justify-content:space-between;font-size:13px"><span>12 Mahmoud Taha St, Jabal Amman</span><span>+962 6 461 2200</span></div></div>
      <div class="sh" style="position:absolute;left:810px;top:150px;width:620px;height:390px;background:{con};padding:40px;font-family:'Space Grotesk';color:{ink}">
        <svg viewBox="0 0 540 310" style="width:100%;height:100%" fill="none" stroke="{ink}" stroke-width="1.5"><rect x="20" y="30" width="300" height="250"/><path d="M20 140 H200 M200 30 V280 M320 170 H510"/><rect x="60" y="180" width="100" height="60"/><path d="M240 60 h50 v50 h-50z"/><path d="M0 200 H540" stroke="{rust}" stroke-width="3"/><text x="340" y="160" font-family="Space Grotesk" font-size="14" fill="{ink}" stroke="none">+842.50 terrace</text><text x="20" y="20" font-family="Space Grotesk" font-size="14" fill="{ink}" stroke="none">RIDGE HOUSE · GROUND FLOOR · 1:200</text></svg></div>
      <div class="sh" style="position:absolute;left:840px;top:620px;width:340px;height:200px;background:{ink};padding:30px;color:{con};font-family:'Space Grotesk'">{mark('mada', 44, con)}<div style="position:absolute;left:30px;bottom:28px;font-size:14px;line-height:1.6">Yara Nasrallah<br><span style="opacity:.6">Partner, Architect</span></div></div>
      <div class="sh" style="position:absolute;left:1210px;top:640px;width:340px;height:200px;background:{rust};padding:30px;display:flex;align-items:center;justify-content:center">{arab('mada', 90, con)}</div>''', 'wide')

def cover_tuleen():
    wal, lin, ol = '#5d3f28', '#ece3d3', '#56613f'
    site = f'''<div style="background:#faf6ef;height:100%;color:#2b2926">
      <div style="display:flex;justify-content:space-between;align-items:center;padding:22px 40px;border-bottom:1px solid #e5dccd">{word('tuleen', 40, wal)}<div style="font:500 14px Inter;display:flex;gap:28px"><span>Dining</span><span>Living</span><span>Outdoor</span><span>Made to order</span><span>Bag (1)</span></div></div>
      <div style="display:grid;grid-template-columns:1.1fr 1fr;gap:50px;padding:40px">
        <div style="height:560px;background:url({IMG}work-4.jpg) center/cover;border-radius:4px"></div>
        <div style="padding-top:20px"><div style="font:500 13px Inter;letter-spacing:.16em;color:{ol}">DINING · SOLID WALNUT</div>
          <div style="font-family:'Cormorant Garamond';font-weight:600;font-size:64px;line-height:1;margin-top:14px">Sahab Dining Chair</div>
          <div dir="rtl" style="font-family:Amiri;font-size:30px;text-align:left;margin-top:8px;color:{wal}">كرسي سحاب</div>
          <div style="font:500 26px Inter;margin-top:26px">145 JD</div>
          <div style="font:400 16px Inter;line-height:1.6;margin-top:18px;opacity:.75;max-width:36ch">Steam-bent back, hand-rubbed oil finish. Made in our Sahab workshop in about three weeks.</div>
          <div style="display:flex;gap:12px;margin-top:26px">{''.join(f'<div style="width:40px;height:40px;border-radius:50%;background:{c};border:3px solid {"#2b2926" if i==0 else "transparent"};box-shadow:0 0 0 2px #faf6ef inset"></div>' for i,c in enumerate([wal,'#b88a5a','#2b2926']))}</div>
          <div style="display:flex;gap:14px;margin-top:34px"><div style="background:{wal};color:#fff;font:600 15px Inter;padding:18px 34px;border-radius:2px">Add to bag</div><div style="border:1px solid #2b2926;font:600 15px Inter;padding:17px 30px;border-radius:2px">Order a sample</div></div>
          <div style="font:400 14px Inter;margin-top:24px;opacity:.6">Free delivery in Amman · Ships to the Gulf in 10 days</div></div></div></div>'''
    return page(f'''<div class="grain" style="position:absolute;inset:0;background:{ol}"></div>
      {browser(site, 120, 170, 1250, 830, 'tuleenhome.com/dining/sahab-chair')}
      <div class="sh" style="position:absolute;left:1260px;top:600px;width:230px;height:380px;background:{lin};border-radius:10px;transform:rotate(8deg);display:flex;flex-direction:column;align-items:center;padding:34px 20px;color:{wal}">
        <div style="width:22px;height:22px;border-radius:50%;background:{ol}"></div>
        {mark('tuleen', 90, wal, 'margin-top:30px')}{word('tuleen', 42, wal, 'margin-top:14px')}{arab('tuleen', 28, wal)}
        <div style="font:500 12px Inter;letter-spacing:.16em;margin-top:auto;text-align:center">HANDMADE IN SAHAB<br>No. 0214</div></div>''', 'cover')

def app_tuleen():
    wal, lin, ol, ch = '#5d3f28', '#ece3d3', '#56613f', '#2b2926'
    tiles = [
      f'<div style="background:url({IMG}work-4.jpg) center/cover"></div>',
      f'<div style="background:{wal};display:flex;align-items:center;justify-content:center;flex-direction:column;color:{lin}">{mark("tuleen", 110, lin)}{word("tuleen", 44, lin, "margin-top:12px")}</div>',
      f'<div style="background:{lin};padding:34px;color:{ch};display:flex;flex-direction:column;justify-content:space-between"><div style="font-family:Cormorant Garamond;font-style:italic;font-size:44px;line-height:1.05">Three weeks,<br>one chair.</div><div style="font:500 13px Inter;letter-spacing:.14em">FROM THE WORKSHOP</div></div>',
      f'<div style="background:{ol};padding:34px;color:{lin};display:flex;flex-direction:column;justify-content:space-between" dir="rtl"><div style="font-family:Amiri;font-size:46px;line-height:1.3">صُنع باليد<br>في سحاب</div><div style="font:500 13px Inter;letter-spacing:.14em" dir="ltr">MADE IN SAHAB</div></div>',
      f'<div style="background:url({IMG}studio-2.jpg) center/cover"></div>',
      f'<div style="background:{ch};padding:34px;color:{lin};display:flex;flex-direction:column;justify-content:space-between"><div style="font:500 13px Inter;letter-spacing:.14em">NEW IN · OCTOBER</div><div style="font-family:Cormorant Garamond;font-weight:600;font-size:48px;line-height:1">Walnut<br>Side Table</div><div style="font:500 18px Inter">210 JD</div></div>',
    ]
    OPEN = '<div style="'
    big = [t.replace(OPEN, OPEN + 'flex:1;', 1) for t in tiles]
    small = [t.replace(OPEN, OPEN + 'flex:none;width:250px;height:250px;transform:scale(.42);transform-origin:top left;', 1) for t in tiles]
    grid = ''.join('<div style="position:relative;width:250px;height:250px;overflow:hidden;display:flex">' + t + '</div>' for t in big)
    feed = ''.join('<div style="aspect-ratio:1;overflow:hidden;position:relative">' + t + '</div>' for t in small)
    profile = (f'<div class="sbar" style="color:{ch}"><span>9:41</span><span>●●●</span></div>'
               f'<div style="display:flex;align-items:center;gap:12px;padding:18px 20px"><div style="width:58px;height:58px;border-radius:50%;background:{wal};display:flex;align-items:center;justify-content:center">{mark("tuleen", 34, lin)}</div>'
               f'<div style="font:600 15px Inter;color:{ch}">tuleen.home<div style="font-weight:400;font-size:12px;opacity:.6">Furniture made in Sahab</div></div></div>'
               f'<div style="padding:0 20px 16px;font:400 13px Inter;color:{ch};line-height:1.5">Solid walnut and oak, made to order.<br><b>tuleenhome.com</b></div>'
               f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">{feed}</div>')
    return page(f'''<div class="grain" style="position:absolute;inset:0;background:{lin}"></div>
      {phone(profile, 170, 150, -3, '#faf6ef')}
      <div style="position:absolute;left:640px;top:110px;display:grid;grid-template-columns:repeat(3,250px);gap:14px">{grid}</div>
      <div style="position:absolute;left:640px;top:680px;width:780px;font:400 17px Inter;color:{ch};line-height:1.6;opacity:.8">Social templates in Arabic and English, built so the Tuleen team can post new pieces from the workshop without a designer.</div>''', 'wide')

def bottle(x, y, h, glass, label_bg, ink, title, ar, sub, rot=0):
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg)">
      <div style="width:70px;height:{h*.22}px;margin:0 auto;background:{glass};border-radius:10px 10px 0 0"></div>
      <div style="width:44px;height:30px;margin:-{h*.22+26}px auto 0;background:#1a1a1a;border-radius:6px;position:relative"></div>
      <div class="sh" style="width:230px;height:{h}px;margin-top:{h*.22-4}px;background:{glass};border-radius:40px 40px 18px 18px;position:relative">
        <div style="position:absolute;left:0;right:0;top:{h*.3}px;height:{h*.5}px;background:{label_bg};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{ink};text-align:center;padding:14px">
          {mark('sahel', 56, ink)}<div dir="rtl" style="font-family:'El Messiri';font-weight:700;font-size:40px;line-height:1.2;margin-top:6px">{ar}</div>
          <div style="font-family:'DM Serif Display';font-size:24px;line-height:1.1">{title}</div><div style="font:500 11px Inter;letter-spacing:.14em;margin-top:8px">{sub}</div></div></div></div>'''

def jar(x, y, lid, body, label_bg, ink, title, ar, sub, rot=0):
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg)">
      <div style="width:260px;height:54px;background:{lid};border-radius:8px;margin:0 auto;position:relative;z-index:2"></div>
      <div class="sh" style="width:290px;height:320px;background:{body};border-radius:26px;margin-top:-6px;position:relative">
        <div style="position:absolute;left:0;right:0;top:60px;height:200px;background:{label_bg};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{ink};text-align:center">
          <div dir="rtl" style="font-family:'El Messiri';font-weight:700;font-size:48px;line-height:1.15">{ar}</div>
          <div style="font-family:'DM Serif Display';font-size:30px;line-height:1">{title}</div><div style="font:500 11px Inter;letter-spacing:.14em;margin-top:10px">{sub}</div></div></div></div>'''

def cover_sahel():
    ol, hv, pa, su = '#4f5b2a', '#d49b2f', '#f3ead6', '#a44a2a'
    pattern = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;opacity:.14;transform:rotate({r}deg)">{mark("sahel", 120, pa)}</div>' for x,y,r in [(40,60,0),(300,-20,40),(1300,80,-20),(1450,420,30),(60,880,-30),(1340,900,10),(680,-40,15)])
    return page(f'''<div style="position:absolute;inset:0;background:{ol}"></div>{pattern}
      <div style="position:absolute;left:0;right:0;top:826px;bottom:0;background:#3f4822"></div>
      {bottle(300, 196, 520, '#2f3a1a', pa, ol, 'Olive Oil', 'زيت زيتون', 'EXTRA VIRGIN · 500 ML')}
      {jar(640, 450, su, '#e9dcc0', pa, su, "Za'atar", 'زعتر بلدي', 'BALADI · 180 G')}
      {jar(1010, 450, hv, '#e9dcc0', pa, ol, 'Freekeh', 'فريكة', 'SMOKED GREEN WHEAT · 400 G')}
      <div style="position:absolute;left:1000px;top:150px;color:{pa}">{lockup('sahel', 84, pa)}</div>
      <div style="position:absolute;left:1000px;top:330px;width:440px;color:{pa};font:400 18px Inter;line-height:1.55;opacity:.85">Labels that read first in Arabic. Now on shelves in Dubai and Riyadh.</div>''', 'cover')

def app_sahel():
    ol, hv, pa, su = '#4f5b2a', '#d49b2f', '#f3ead6', '#a44a2a'
    tile = ''.join(f'<div style="width:200px;height:200px;background:{bg};display:flex;align-items:center;justify-content:center;transform:rotate(0)">{mark("sahel", 120, fg)}</div>' for bg,fg in [(ol,pa),(pa,ol),(hv,ol),(su,pa),(pa,su),(ol,hv)]*2)
    return page(f'''<div style="position:absolute;inset:0;background:{pa}"></div>
      <div style="position:absolute;left:0;top:0;width:800px;height:1000px;display:flex;flex-wrap:wrap;align-content:flex-start;overflow:hidden">{tile}{tile}</div>
      <div class="sh" style="position:absolute;left:900px;top:130px;width:560px;height:340px;background:{pa};border:2px solid {ol};padding:34px;color:{ol}">
        <div style="display:flex;justify-content:space-between;align-items:center">{lockup('sahel', 54, ol)}<div style="text-align:right;font:500 12px Inter;letter-spacing:.14em">BATCH 24-11<br>BEST BEFORE 11/2026</div></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px;font:400 14px Inter;line-height:1.6"><div><b>Ingredients</b><br>Wild thyme, sumac, toasted sesame, salt from the Dead Sea.</div><div dir="rtl" style="font-family:'El Messiri';font-size:17px;line-height:1.6"><b>المكوّنات</b><br>زعتر بري، سماق، سمسم محمّص، ملح من البحر الميت.</div></div></div>
      <div class="sh" style="position:absolute;left:900px;top:540px;width:560px;height:300px;background:{su};padding:34px;color:{pa};display:flex;flex-direction:column;justify-content:space-between">
        <div style="font:500 13px Inter;letter-spacing:.16em">SHIPPING CARTON · 12 × 180 G</div>
        <div style="display:flex;align-items:flex-end;justify-content:space-between">{arab('sahel', 110, pa)}{mark('sahel', 110, pa)}</div></div>''', 'wide')

def cover_dawra():
    n, li, la = '#131316', '#c8f442', '#b9a7ff'
    ring = ''.join(f'<circle cx="120" cy="120" r="96" fill="none" stroke="{li if i<4 else "#2a2a30"}" stroke-width="22" stroke-dasharray="54 549" stroke-dashoffset="{-i*60.3:.1f}" transform="rotate(-90 120 120)"/>' for i in range(10))
    s1 = f'''<div class="sbar" style="color:#fff"><span>9:41</span><span>●●●</span></div>
      <div style="padding:26px 24px;color:#fff;font-family:Alexandria">
        <div style="display:flex;justify-content:space-between;align-items:center"><div style="font-family:Syne;font-weight:800;font-size:26px">Family circle</div><div style="width:36px;height:36px;border-radius:50%;background:{la}"></div></div>
        <div style="font-size:14px;opacity:.6;margin-top:4px">10 members · 100 JD a month</div>
        <div style="position:relative;width:240px;height:240px;margin:30px auto 0"><svg viewBox="0 0 240 240" width="240" height="240">{ring}</svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-family:Syne;font-weight:800;font-size:54px;line-height:1">4<span style="font-size:24px;opacity:.5">/10</span></div><div style="font-size:13px;opacity:.6">months</div></div></div>
        <div style="background:{li};color:{n};border-radius:22px;padding:18px;margin-top:30px"><div style="font-size:12px;letter-spacing:.1em">YOUR PAYOUT</div><div style="font-family:Syne;font-weight:800;font-size:32px">1,000 JD</div><div style="font-size:13px">November · month 7</div></div>
        <div style="display:flex;justify-content:space-between;margin-top:18px;background:#1f1f24;border-radius:18px;padding:16px"><div style="font-size:14px">October payment</div><div style="font-size:14px;color:{li}">Paid ✓</div></div></div>'''
    members = [('LH','Layla','Paid'),('OA','Omar','Paid'),('RK','Rami','Due 3 days'),('SN','Sara','Paid'),('YM','You','Paid'),('HT','Hadi','Paid')]
    s2 = f'''<div class="sbar" style="color:{n}"><span>9:41</span><span>●●●</span></div>
      <div style="padding:26px 24px;color:{n};font-family:Alexandria">
        <div style="font-family:Syne;font-weight:800;font-size:28px">Who gets paid when</div>
        {''.join(f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid #eee"><div style="width:30px;font-family:Syne;font-weight:800;font-size:15px;opacity:.4">{i+1:02d}</div><div style="width:40px;height:40px;border-radius:50%;background:{[la,li,"#ffd3c2","#c9f0ff",n,"#e8e8e8"][i]};color:{"#fff" if i==4 else n};display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800">{a}</div><div style="flex:1;font-size:15px">{nm}<div style="font-size:12px;opacity:.55">{["Jul","Aug","Sep","Oct","Nov","Dec"][i]} payout</div></div><div style="font-size:12px;padding:6px 10px;border-radius:10px;background:{"#fff1ec" if "Due" in st else "#f2f7e0"};color:{"#c2410c" if "Due" in st else "#4d6b00"}">{st}</div></div>' for i,(a,nm,st) in enumerate(members))}
        <div dir="rtl" style="text-align:center;margin-top:24px;font-size:15px;opacity:.6">دورة · وفّروا معاً</div></div>'''
    return page(f'''<div style="position:absolute;inset:0;background:{li}"></div>
      <div style="position:absolute;left:110px;top:120px;color:{n}">{mark('dawra', 120, n)}</div>
      <div style="position:absolute;left:110px;top:290px;font-family:Syne;font-weight:800;font-size:92px;line-height:.92;color:{n};letter-spacing:-.04em">save<br>together.</div>
      <div dir="rtl" style="position:absolute;left:110px;top:500px;font-family:Alexandria;font-weight:800;font-size:56px;color:{n}">وفّروا معاً</div>
      <div style="position:absolute;left:110px;bottom:110px;width:420px;font:500 19px Alexandria;color:{n};line-height:1.5">The family savings circle, finally tracked properly. Everyone sees who has paid and when their turn comes.</div>
      {phone(s1, 810, 200, -5, n)}{phone(s2, 1190, 250, 4, "#fff")}''', 'cover')

def app_dawra():
    n, li, la = '#131316', '#c8f442', '#b9a7ff'
    return page(f'''<div style="position:absolute;inset:0;background:#2a2a30"></div>
      <div class="sh" style="position:absolute;left:120px;top:110px;width:760px;height:780px;background:{la};padding:60px;color:{n}">
        <div style="font-family:Syne;font-weight:800;font-size:124px;line-height:.85;letter-spacing:-.04em">your<br>turn is<br>month 7.</div>
        <div style="position:absolute;left:60px;bottom:60px;display:flex;align-items:center;gap:22px">{mark('dawra', 90, n)}<div><div style="font-family:Syne;font-weight:800;font-size:44px">dawra</div><div style="font:500 16px Alexandria">App Store · Google Play</div></div></div>
        <div dir="rtl" style="position:absolute;right:60px;bottom:60px;font-family:Alexandria;font-weight:800;font-size:56px">دورك<br>بالشهر ٧</div></div>
      <div style="position:absolute;left:960px;top:110px;display:grid;grid-template-columns:repeat(2,200px);gap:40px">
        {''.join(f'<div class="sh" style="width:200px;height:200px;border-radius:46px;background:{bg};display:flex;align-items:center;justify-content:center">{mark("dawra", 120, fg)}</div>' for bg,fg in [(li,n),(n,li),(la,n),('#fff',n)])}</div>
      <div style="position:absolute;left:960px;top:620px;width:480px;color:#fff;font:400 18px Alexandria;line-height:1.6">Outdoor posters for the launch in Amman and Irbid, and the app icon family. Each ring segment is one member of the circle.</div>''', 'wide')

def cover_layali():
    du, sa, go, se = '#1b2740', '#f4efe6', '#c7a268', '#5f8a8b'
    return page(f'''<div style="position:absolute;inset:0;background:{du}"></div>
      <div style="position:absolute;left:0;top:0;width:760px;height:1200px;background:url({IMG}proj-2.jpg) center/cover"></div>
      <div style="position:absolute;left:0;top:0;width:760px;height:1200px;background:linear-gradient(0deg,rgba(27,39,64,.75),rgba(27,39,64,0) 55%)"></div>
      <div style="position:absolute;left:70px;bottom:90px;color:{sa}">{mark('layali', 110, go)}<div style="font-family:'Playfair Display';font-size:74px;letter-spacing:.2em;margin-top:26px">LAYALI</div><div style="font:500 15px Inter;letter-spacing:.3em;margin-top:6px;opacity:.8">DEAD SEA RESORT</div></div>
      <div class="sh" style="position:absolute;left:880px;top:140px;width:540px;height:340px;border-radius:22px;background:linear-gradient(135deg,#d6b77f,#a9824a);padding:40px;color:{du};transform:rotate(-4deg)">
        <div style="display:flex;justify-content:space-between">{mark('layali', 64, du)}<div style="font:600 13px Inter;letter-spacing:.2em">ROOM KEY</div></div>
        <div style="position:absolute;left:40px;bottom:40px"><div style="font-family:'Playfair Display';font-size:40px;letter-spacing:.16em">LAYALI</div><div dir="rtl" style="font-family:'Aref Ruqaa';font-size:34px;text-align:left">ليالي</div></div>
        <div style="position:absolute;right:40px;bottom:44px;font:500 15px Inter;letter-spacing:.1em">Suite 214</div></div>
      <div class="sh" style="position:absolute;left:940px;top:560px;width:440px;height:560px;background:{sa};padding:46px;color:{du};transform:rotate(3deg);text-align:center">
        {mark('layali', 54, go, 'margin:0 auto')}
        <div style="font-family:'Playfair Display';font-size:34px;letter-spacing:.14em;margin-top:18px">IN-ROOM DINING</div>
        <div dir="rtl" style="font-family:'Aref Ruqaa';font-size:30px;color:{go}">خدمة الغرف</div>
        {''.join(f'<div style="display:flex;justify-content:space-between;border-bottom:1px solid {du}22;padding:14px 0;font:400 16px Inter;text-align:left"><span>{d}</span><span>{p} JD</span></div>' for d,p in [('Mansaf for two','38'),('Grilled Aqaba sea bream','29'),('Fattoush, pomegranate','11'),('Knafeh, warm','9')])}
        <div style="font:400 13px Inter;margin-top:24px;opacity:.6">Served from 12 noon to midnight · Dial 7</div></div>''', 'cover')

def app_layali():
    du, sa, go, se = '#1b2740', '#f4efe6', '#c7a268', '#5f8a8b'
    signs = ''.join(f'<div class="sh" style="width:300px;height:420px;background:{bg};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{fg};text-align:center;gap:10px"><div style="font-family:Playfair Display;font-size:40px;letter-spacing:.16em">{e}</div><div dir="rtl" style="font-family:Aref Ruqaa;font-size:44px;color:{ac}">{a}</div><div style="font-size:54px;margin-top:10px;color:{ac}">{arr}</div></div>' for bg,fg,ac,e,a,arr in [(du,sa,go,'SPA','السبا','→'),(sa,du,go,'POOL','المسبح','↑'),(se,sa,sa,'BEACH','الشاطئ','←')])
    return page(f'''<div style="position:absolute;inset:0;background:#e7e0d3"></div>
      <div style="position:absolute;left:120px;top:120px;display:flex;gap:40px">{signs}</div>
      <div class="sh" style="position:absolute;left:1180px;top:120px;width:300px;height:420px;background:{du};padding:34px;color:{sa}">{mark('layali', 60, go)}<div style="position:absolute;left:34px;bottom:34px;font:400 14px Inter;line-height:1.7">Welcome, Mr. and Mrs. Haddad.<br><br>Sunset from the Salt Terrace is at 6:12 tonight.</div></div>
      <div style="position:absolute;left:120px;top:640px;width:1360px;border-top:1px solid {du}33;padding-top:30px;display:flex;justify-content:space-between;color:{du}">
        <div style="font-family:Playfair Display;font-size:44px;letter-spacing:.14em">Wayfinding &amp; guest stationery</div>
        <div style="font:400 17px Inter;width:520px;line-height:1.6;opacity:.8">Bilingual signs across 120 rooms, two pools and the spa, with the Arabic set in Ruqaa so it feels written, not printed.</div></div>''', 'wide')

def cover_fakhar():
    tc, cl, ch, gl = '#b4532b', '#ead6c0', '#2b2623', '#3f6f86'
    stamp = f'<div style="width:190px;height:190px;border-radius:50%;border:5px solid {tc};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{tc};transform:rotate(-14deg)">{mark("fakhar", 70, tc)}<div style="font-family:Bricolage Grotesque;font-weight:800;font-size:26px;line-height:1">fakhar</div><div dir="rtl" style="font-family:Lalezar;font-size:24px;line-height:1">فخار</div></div>'
    shop = f'''<div style="background:#f6efe6;height:100%;color:{ch}">
      <div style="display:flex;justify-content:space-between;align-items:center;padding:20px 30px">{word('fakhar', 38, tc)}<div style="font:500 14px Inter;display:flex;gap:24px"><span>Shop</span><span>Workshops</span><span>Visit Madaba</span><span>Bag (2)</span></div></div>
      <div style="height:300px;margin:0 30px;background:linear-gradient(0deg,rgba(43,38,35,.72),rgba(43,38,35,0) 70%),url({IMG}proj-3.jpg) center/cover;border-radius:6px;position:relative"><div style="position:absolute;left:30px;bottom:26px;color:#fff;font-family:Bricolage Grotesque;font-weight:800;font-size:54px;line-height:.95;text-shadow:0 2px 20px rgba(0,0,0,.3)">Thrown by hand,<br>fired in Madaba.</div></div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding:22px 30px">{''.join(f'<div><div style="height:140px;border-radius:6px;background:{bg};display:flex;align-items:center;justify-content:center">{mark("fakhar", 80, fg)}</div><div style="font:600 15px Inter;margin-top:10px">{nm}</div><div style="font:400 14px Inter;opacity:.6">{pr} JD</div></div>' for bg,fg,nm,pr in [(cl,tc,'Everyday bowl','14'),(gl,cl,'Glazed jug','32'),(ch,cl,'Espresso cup, set of 2','18')])}</div></div>'''
    return page(f'''<div class="grain" style="position:absolute;inset:0;background:{cl}"></div>
      <div class="sh" style="position:absolute;left:110px;top:430px;width:520px;height:520px;background:#c89b6d;transform:rotate(-6deg)">
        <div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,rgba(0,0,0,.03) 0 2px,transparent 2px 7px)"></div>
        <div style="position:absolute;left:0;right:0;top:40px;height:54px;background:{tc};opacity:.92"></div>
        <div style="position:absolute;left:170px;top:160px">{stamp}</div></div>
      <div class="sh" style="position:absolute;left:470px;top:180px;width:210px;height:300px;background:#f6efe6;border-radius:6px;transform:rotate(7deg);padding:24px;color:{ch}">
        <div style="width:16px;height:16px;border-radius:50%;background:{cl};margin:0 auto"></div>
        <div style="font-family:Bricolage Grotesque;font-weight:800;font-size:28px;margin-top:30px;line-height:1">Glazed jug</div><div style="font:400 13px Inter;margin-top:8px;opacity:.7">Stoneware, reactive blue glaze. Food safe.</div>
        <div style="position:absolute;left:24px;bottom:24px;font:600 12px Inter;letter-spacing:.12em">MADE BY NOUR · 06/24</div></div>
      {browser(shop, 760, 160, 740, 820, 'fakharceramics.jo')}
      <div style="position:absolute;left:110px;top:110px">{lockup('fakhar', 80, tc)}</div>''', 'cover')

def app_fakhar():
    tc, cl, ch, gl = '#b4532b', '#ead6c0', '#2b2623', '#3f6f86'
    tiles = ''.join(f'<div style="width:160px;height:160px;background:{bg};display:flex;align-items:center;justify-content:center;border-radius:{r}">{mark("fakhar", 90, fg)}</div>' for bg,fg,r in [(tc,cl,'0'),(cl,gl,'50%'),(gl,cl,'0'),(ch,tc,'50%'),(cl,tc,'50%'),(tc,ch,'0'),(gl,cl,'50%'),(cl,ch,'0'),(ch,cl,'0'),(tc,cl,'50%'),(cl,gl,'0'),(gl,tc,'50%')])
    return page(f'''<div style="position:absolute;inset:0;background:{ch}"></div>
      <div style="position:absolute;left:110px;top:110px;display:grid;grid-template-columns:repeat(4,160px);gap:20px">{tiles}</div>
      <div class="sh" style="position:absolute;left:940px;top:120px;width:520px;height:300px;background:{cl};border-radius:8px;padding:36px;color:{ch}">
        {lockup('fakhar', 58, tc)}<div style="position:absolute;left:36px;bottom:32px;font:400 15px Inter;line-height:1.6">Nour Haddadin, potter<br>King Talal St, Madaba · +962 77 204 1180</div></div>
      <div class="sh" style="position:absolute;left:940px;top:480px;width:520px;height:220px;background:{tc};border-radius:8px;display:flex;align-items:center;justify-content:space-around;color:{cl}">
        {arab('fakhar', 120, cl)}<div style="font-family:Bricolage Grotesque;font-weight:800;font-size:96px">fakhar</div></div>
      <div style="position:absolute;left:940px;top:760px;width:520px;color:{cl};font:400 17px Inter;line-height:1.6;opacity:.85">A pattern system drawn from the vessel symbol, used on tissue paper, tape and workshop aprons.</div>''', 'wide')
