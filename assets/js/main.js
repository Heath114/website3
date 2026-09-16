/* Naqsh: interactions */
(function(){
  var burger=document.querySelector('.burger');
  if(burger){ burger.addEventListener('click',function(){ document.body.classList.toggle('mobile-open'); }); }

  // ---------------------------------------------------------------------------
  // motion: each kind of element gets its own entrance instead of one shared
  // fade-up. Kinds are chosen from the element itself, so pages need no markup.
  //   words  headings rise word by word from behind a mask
  //   ink    the big statement darkens word by word as you scroll through it
  //   clip   cards and portraits wipe up; clip-x figures wipe across
  //   row    list rows draw their rule, then slide in
  //   count  stats count up to their value
  //   slide  small labels slide in from the left
  //   fade   everything else fades in quietly
  // ---------------------------------------------------------------------------
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function splitWords(el, cls, wrap){
    var out = [];
    (function walk(node){
      Array.prototype.slice.call(node.childNodes).forEach(function(ch){
        if (ch.nodeType === 3) {
          var frag = document.createDocumentFragment();
          ch.textContent.split(/(\s+)/).forEach(function(part){
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var w = document.createElement('span'); w.className = cls; w.textContent = part; out.push(w);
            if (wrap) { var o = document.createElement('span'); o.className = cls + '-o'; o.appendChild(w); frag.appendChild(o); }
            else frag.appendChild(w);
          });
          node.replaceChild(frag, ch);
        } else if (ch.nodeType === 1 && ch.tagName !== 'BR') walk(ch);
      });
    })(el);
    return out;
  }

  function kindOf(el){
    if (el.matches('.statement h2')) return 'ink';
    if (el.matches('h1, h2, blockquote')) return 'words';
    if (el.matches('.wcard, .member')) return 'clip';
    if (el.matches('img, figure')) return 'clip-x';
    if (el.matches('.srow, .job')) return 'row';
    if (el.matches('.stat')) return 'count';
    if (el.matches('.mono, .eyebrow')) return 'slide';
    return 'fade';
  }

  function countUp(el){
    var n = el.querySelector('.n'); if (!n) return;
    var m = n.textContent.trim().match(/^([^\d]*)([\d,]*\.?\d+)(.*)$/); if (!m) return;
    var target = parseFloat(m[2].replace(/,/g, '')), dec = (m[2].split('.')[1] || '').length, commas = m[2].indexOf(',') > -1;
    var t0 = null, dur = 1400;
    function fmt(v){ var s = v.toFixed(dec); return commas ? s.replace(/\B(?=(\d{3})+(?!\d))/g, ',') : s; }
    n.textContent = m[1] + fmt(0) + m[3];
    (function tick(t){
      if (t0 === null) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
      n.textContent = m[1] + fmt(target * e) + m[3];
      if (k < 1) requestAnimationFrame(tick);
    })(performance.now());
  }

  var inkEls = [];
  function prep(el, baseDelay){
    var kind = kindOf(el);
    el.setAttribute('data-m', kind);
    el.style.setProperty('--d', baseDelay + 's');
    if (kind === 'words') splitWords(el, 'wi', true).forEach(function(w, i){ w.style.transitionDelay = (baseDelay + i * 0.045) + 's'; });
    if (kind === 'ink') inkEls.push({ el: el, words: splitWords(el, 'iw', false) });
    return kind;
  }

  if (reduced) {
    document.querySelectorAll('[data-r]').forEach(function(el){ el.classList.add('in'); });
  } else {
    // IntersectionObserver respects clip-path, so an image clipped to nothing
    // never intersects. Watch its parent instead and reveal the image.
    var watched = new Map();
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (!e.isIntersecting) return;
        (watched.get(e.target) || []).forEach(function(el){
          el.classList.add('in');
          if (el.getAttribute('data-m') === 'count') countUp(el);
        });
        io.unobserve(e.target);
      });
    }, { threshold: .12, rootMargin: '0px 0px -8% 0px' });
    function watch(el){
      var t = el.tagName === 'IMG' ? el.parentNode : el;
      if (!watched.has(t)) { watched.set(t, []); io.observe(t); }
      watched.get(t).push(el);
    }

    document.querySelectorAll('[data-r]').forEach(function(el){
      // stagger among siblings that also animate, not across the whole page
      var sibs = Array.prototype.filter.call(el.parentNode.children, function(c){ return c.hasAttribute('data-r'); });
      var kind = prep(el, Math.min(sibs.indexOf(el), 5) * 0.09);
      if (kind !== 'ink') watch(el); else el.classList.add('in');
    });

    // page titles animate on load rather than on scroll
    document.querySelectorAll('.hero h1, .page-hero h1').forEach(function(h){
      h.setAttribute('data-r', ''); prep(h, 0.1);
      requestAnimationFrame(function(){ requestAnimationFrame(function(){ h.classList.add('in'); }); });
    });

    if (inkEls.length) {
      var ticking = false;
      function ink(){
        ticking = false;
        var vh = window.innerHeight;
        inkEls.forEach(function(o){
          var r = o.el.getBoundingClientRect();
          var p = Math.max(0, Math.min(1, (vh * .85 - r.top) / (r.height + vh * .3)));
          var on = Math.round(p * o.words.length);
          o.words.forEach(function(w, i){ w.classList.toggle('on', i < on); });
        });
      }
      window.addEventListener('scroll', function(){ if (!ticking) { ticking = true; requestAnimationFrame(ink); } }, { passive: true });
      window.addEventListener('resize', ink);
      ink();
    }
  }

  // capability rows expand to show deliverables and related case studies
  function toggleRow(row){ var open=row.classList.toggle('open'); row.setAttribute('aria-expanded',open); }
  document.querySelectorAll('.srow-x').forEach(function(row){
    row.addEventListener('click',function(e){ if(!e.target.closest('a')) toggleRow(row); });
    row.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); toggleRow(row); } });
  });

  // apply buttons -> jump to the application form and preselect the role
  document.addEventListener('click',function(e){
    var a=e.target.closest('[data-apply]');
    if(!a) return; e.preventDefault();

    var role=a.getAttribute('data-apply');
    var form=document.getElementById('apply-form');
    if(!form){ return; }

    var select=form.querySelector('[data-role-select]');
    if(select && role){
      for(var i=0;i<select.options.length;i++){
        if(select.options[i].text===role){ select.selectedIndex=i; break; }
      }
    }

    form.scrollIntoView({behavior:'smooth',block:'center'});
    var firstInput=form.querySelector('input,textarea');
    if(firstInput){ setTimeout(function(){ firstInput.focus({preventScroll:true}); },500); }
  });

  document.querySelectorAll('form[data-form]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      f.querySelectorAll('input,textarea,button,select').forEach(function(el){ el.disabled=true; });
      var note=f.querySelector('[data-note]'); if(note) note.style.display='block';
    });
  });

  var y=document.querySelector('[data-year]'); if(y) y.textContent=new Date().getFullYear();
})();
