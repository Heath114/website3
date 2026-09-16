/* Naqsh: interactions */
(function(){
  var burger=document.querySelector('.burger');
  if(burger){ burger.addEventListener('click',function(){ document.body.classList.toggle('mobile-open'); }); }

  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{threshold:.1,rootMargin:'0px 0px -6% 0px'});
  document.querySelectorAll('[data-r]').forEach(function(el,i){ el.style.transitionDelay=(i%2)*0.08+'s'; io.observe(el); });

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
