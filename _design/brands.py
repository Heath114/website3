# Naqsh portfolio: the eight client identities. Rendered to images by render.py.
FONTS = ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Manrope:wght@500;700;800"
         "&family=Space+Grotesk:wght@400;500;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600"
         "&family=DM+Serif+Display&family=Syne:wght@600;700;800&family=Playfair+Display:wght@400;500&family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800"
         "&family=Inter:wght@400;500;600&family=Reem+Kufi:wght@500;700&family=Readex+Pro:wght@400;600&family=IBM+Plex+Sans+Arabic:wght@400;600"
         "&family=Amiri:wght@400;700&family=El+Messiri:wght@500;700&family=Alexandria:wght@500;800&family=Aref+Ruqaa:wght@400;700&family=Lalezar&display=block")

MARKS = {
 # hill + sun: "rabwa" is a hill
 'rabwa': '<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round"><path d="M8 78 Q50 18 92 78"/><path d="M28 78 Q50 48 72 78"/><circle cx="50" cy="26" r="7" fill="currentColor" stroke="none"/></svg>',
 # a plus whose top arm is a leaf: care that grows
 'aafia': '<svg viewBox="0 0 100 100" fill="currentColor"><rect x="40" y="44" width="20" height="46" rx="10"/><rect x="10" y="44" width="80" height="20" rx="10"/><path d="M50 8 C70 18 70 40 50 50 C30 40 30 18 50 8Z"/></svg>',
 # a horizon line running past a frame: "mada" is range, reach
 'mada': '<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="6"><rect x="18" y="22" width="52" height="56"/><path d="M4 60 H96"/></svg>',
 # a serif T drawn as a chair profile
 'tuleen': '<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round"><path d="M22 20 H78"/><path d="M50 20 V62"/><path d="M28 62 H72"/><path d="M34 62 L28 90"/><path d="M66 62 L72 90"/></svg>',
 # an upright olive branch with paired leaves and two olives
 'sahel': '<svg viewBox="0 0 100 100" fill="currentColor"><path d="M34 96 C44 70 58 40 74 8" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/><ellipse cx="31" cy="74" rx="13" ry="4.8" transform="rotate(-35 31 74)"/><ellipse cx="71" cy="66" rx="13" ry="4.8" transform="rotate(40 71 66)"/><ellipse cx="37" cy="52" rx="13" ry="4.8" transform="rotate(-40 37 52)"/><ellipse cx="77" cy="44" rx="13" ry="4.8" transform="rotate(35 77 44)"/><ellipse cx="43" cy="31" rx="13" ry="4.8" transform="rotate(-45 43 31)"/><ellipse cx="83" cy="24" rx="13" ry="4.8" transform="rotate(30 83 24)"/><ellipse cx="26" cy="86" rx="6" ry="7.5"/><ellipse cx="72" cy="58" rx="5.5" ry="7" transform="rotate(20 72 58)"/></svg>',
 # a ring in ten segments, one filled: the savings circle
 'dawra': ''.join(['<svg viewBox="0 0 100 100" fill="none" stroke-width="12" stroke-linecap="butt">'] +
     [f'<circle cx="50" cy="50" r="38" stroke="currentColor" stroke-opacity="{1 if i==0 else .35}" stroke-dasharray="20.9 218" stroke-dashoffset="{-i*23.88:.2f}" transform="rotate(-90 50 50)"/>' for i in range(10)] + ['</svg>']),
 # crescent over three waves
 'layali': '<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"><path d="M58 14 A24 24 0 1 0 74 52 A18 18 0 1 1 58 14Z" fill="currentColor" stroke="none"/><path d="M10 70 Q22 62 34 70 T58 70 T82 70 T96 70"/><path d="M10 82 Q22 74 34 82 T58 82 T82 82 T96 82"/><path d="M10 94 Q22 86 34 94 T58 94 T82 94 T96 94"/></svg>',
 # a thrown vessel
 'fakhar': '<svg viewBox="0 0 100 100" fill="currentColor"><path d="M38 8 H62 V16 C62 22 58 24 58 28 C80 36 86 58 76 78 C70 90 60 94 50 94 C40 94 30 90 24 78 C14 58 20 36 42 28 C42 24 38 22 38 16Z"/><path d="M28 56 H72" stroke="#fff" stroke-opacity=".35" stroke-width="3"/></svg>',
}

B = {
 'rabwa': dict(panels=('#efe4cf', '#2a1a12', '#c4553a', '#2a1a12'), name='Rabwa Coffee', ar='ربوة', word='RABWA', tag='Coffee Roasters · Amman', year='2025',
    latin="'Fraunces', serif", lw='700', arabic="'Reem Kufi', sans-serif",
    c=[('Espresso','#2a1a12'),('Clay','#c4553a'),('Cream','#efe4cf'),('Sage','#8a8f6a')],
    fg='#efe4cf', bg='#2a1a12', accent='#c4553a',
    type_note='Fraunces for the wordmark and packaging, Reem Kufi for Arabic. Both share a soft, slightly bookish warmth.'),
 'aafia': dict(panels=('#f7faf8', '#0e4b4a', '#ff7a59', '#0e4b4a'), name='Aafia Health', ar='عافية', word='aafia', tag='Family clinics', year='2025',
    latin="'Manrope', sans-serif", lw='800', arabic="'Readex Pro', sans-serif",
    c=[('Deep teal','#0e4b4a'),('Mint','#cde8da'),('Paper','#f7faf8'),('Coral','#ff7a59')],
    fg='#f7faf8', bg='#0e4b4a', accent='#ff7a59',
    type_note='Manrope for interface and signage, Readex Pro for Arabic. Chosen for legibility at small sizes on phones.'),
 'mada': dict(panels=('#161616', '#dcd8d0', '#9b5a3a', '#f4f2ee'), name='Mada Architects', ar='مدى', word='MADA', tag='Architects', year='2024',
    latin="'Space Grotesk', sans-serif", lw='500', arabic="'IBM Plex Sans Arabic', sans-serif",
    c=[('Concrete','#dcd8d0'),('Ink','#161616'),('Rust','#9b5a3a'),('Stone','#a9a397')],
    fg='#161616', bg='#dcd8d0', accent='#9b5a3a',
    type_note='Space Grotesk set wide and quiet, IBM Plex Sans Arabic alongside. The drawings do the talking.'),
 'tuleen': dict(panels=('#ece3d3', '#5d3f28', '#56613f', '#ece3d3'), name='Tuleen Home', ar='تولين', word='Tuleen', tag='Furniture made in Sahab', year='2024',
    latin="'Cormorant Garamond', serif", lw='600', arabic="'Amiri', serif",
    c=[('Walnut','#5d3f28'),('Linen','#ece3d3'),('Olive','#56613f'),('Charcoal','#2b2926')],
    fg='#ece3d3', bg='#5d3f28', accent='#56613f',
    type_note='Cormorant Garamond with Amiri: two classical faces that feel made by hand, like the furniture.'),
 'sahel': dict(panels=('#f3ead6', '#4f5b2a', '#d49b2f', '#4f5b2a'), name='Sahel Pantry', ar='ساحل', word='Sahel', tag='Pantry from the Jordan Valley', year='2024',
    latin="'DM Serif Display', serif", lw='400', arabic="'El Messiri', sans-serif",
    c=[('Olive','#4f5b2a'),('Harvest','#d49b2f'),('Paper','#f3ead6'),('Sumac','#a44a2a')],
    fg='#f3ead6', bg='#4f5b2a', accent='#d49b2f',
    type_note='DM Serif Display for names, El Messiri for Arabic. Labels read first in Arabic, then in English.'),
 'dawra': dict(panels=('#131316', '#c8f442', '#b9a7ff', '#131316'), name='Dawra', ar='دورة', word='dawra', tag='Save together', year='2023',
    latin="'Syne', sans-serif", lw='800', arabic="'Alexandria', sans-serif",
    c=[('Night','#131316'),('Lime','#c8f442'),('Lilac','#b9a7ff'),('White','#ffffff')],
    fg='#131316', bg='#c8f442', accent='#b9a7ff',
    type_note='Syne for display, Alexandria for Arabic and interface. Loud where it matters, calm inside the app.'),
 'layali': dict(panels=('#c7a268', '#1b2740', '#f4efe6', '#1b2740'), name='Layali Dead Sea Resort', ar='ليالي', word='LAYALI', tag='Dead Sea Resort', year='2023',
    latin="'Playfair Display', serif", lw='400', arabic="'Aref Ruqaa', serif",
    c=[('Dusk','#1b2740'),('Salt','#f4efe6'),('Gold','#c7a268'),('Sea','#5f8a8b')],
    fg='#c7a268', bg='#1b2740', accent='#f4efe6',
    type_note='Playfair Display in spaced capitals, Aref Ruqaa for the Arabic signature. Evening, not beach.'),
 'fakhar': dict(panels=('#2b2623', '#b4532b', '#3f6f86', '#ead6c0'), name='Fakhar Ceramics', ar='فخار', word='fakhar', tag='Handmade in Madaba', year='2022',
    latin="'Bricolage Grotesque', sans-serif", lw='800', arabic="'Lalezar', sans-serif",
    c=[('Terracotta','#b4532b'),('Clay','#ead6c0'),('Charcoal','#2b2623'),('Glaze','#3f6f86')],
    fg='#ead6c0', bg='#b4532b', accent='#3f6f86',
    type_note='Bricolage Grotesque, chunky and a little irregular, with Lalezar for Arabic. Stamped, not printed.'),
}
