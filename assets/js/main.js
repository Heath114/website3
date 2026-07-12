/* Naqsh — interactions */
(function(){
  var burger=document.querySelector('.burger');
  if(burger){ burger.addEventListener('click',function(){ document.body.classList.toggle('mobile-open'); }); }

  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{threshold:.1,rootMargin:'0px 0px -6% 0px'});
  document.querySelectorAll('[data-r]').forEach(function(el,i){ el.style.transitionDelay=(i%2)*0.08+'s'; io.observe(el); });

  // apply buttons -> feedback
  document.addEventListener('click',function(e){
    var a=e.target.closest('[data-apply]');
    if(!a) return; e.preventDefault();
    a.textContent='Application started ✓';
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
