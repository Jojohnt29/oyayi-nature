/* ============================================================
   OYAYI Nature — shared site JS
   Loader, theme toggle, mobile nav drawer, contact form,
   newsletter form, cart badge bump.
   ============================================================ */

/* Apply persisted DA before paint to prevent flash */
document.documentElement.setAttribute('data-da', localStorage.getItem('oyayi-da') || 'green');

/* ---------- LOADER ---------- */
(function(){
  const loader = document.getElementById('loader');
  if (!loader) return;
  const start = performance.now();
  const MIN_DISPLAY = 1100;
  function hide(){
    const wait = Math.max(0, MIN_DISPLAY - (performance.now() - start));
    setTimeout(()=>{
      loader.classList.add('hidden');
      document.body.classList.remove('loading');
      setTimeout(()=>loader.remove(), 800);
    }, wait);
  }
  if (document.readyState === 'complete') hide();
  else window.addEventListener('load', hide, { once:true });
  setTimeout(hide, 4000);
})();

/* ---------- THEME TOGGLE ---------- */
(function(){
  const DA_LABELS = { green: 'Vert · Forêt', brown: 'Brun · Terre' };
  const fab = document.getElementById('themeFab');
  const lab = document.getElementById('themeFabLabel');
  function setDA(da){
    document.documentElement.setAttribute('data-da', da);
    localStorage.setItem('oyayi-da', da);
    if (lab) lab.textContent = DA_LABELS[da] || da;
  }
  if (fab) {
    fab.addEventListener('click', ()=>{
      const cur = document.documentElement.getAttribute('data-da') || 'green';
      setDA(cur === 'green' ? 'brown' : 'green');
    });
  }
  setDA(localStorage.getItem('oyayi-da') || 'green');
})();

/* ---------- MOBILE NAV DRAWER ---------- */
(function(){
  const toggle = document.getElementById('navToggle');
  const drawer = document.getElementById('navDrawer');
  if (!toggle || !drawer) return;
  function close(){ drawer.classList.remove('open'); document.body.style.overflow=''; }
  function open(){ drawer.classList.add('open'); document.body.style.overflow='hidden'; }
  toggle.addEventListener('click', ()=>drawer.classList.contains('open') ? close() : open());
  drawer.querySelectorAll('a').forEach(a=>a.addEventListener('click', close));
  document.addEventListener('keydown', e=>{ if (e.key === 'Escape') close(); });
})();

/* ---------- CART BADGE (demo) ---------- */
window.OYAYI = window.OYAYI || {};
window.OYAYI.cart = JSON.parse(localStorage.getItem('oyayi-cart') || '[]');
window.OYAYI.refreshCartBadge = function(){
  const count = window.OYAYI.cart.length || 0;
  document.querySelectorAll('.cart-badge').forEach(b=>{
    b.textContent = String(count).padStart(2,'0');
  });
};
window.OYAYI.addToCart = function(item){
  window.OYAYI.cart.push(item);
  localStorage.setItem('oyayi-cart', JSON.stringify(window.OYAYI.cart));
  window.OYAYI.refreshCartBadge();
  document.querySelectorAll('.cart-badge').forEach(b=>{
    b.classList.add('bump');
    setTimeout(()=>b.classList.remove('bump'), 250);
  });
};
window.OYAYI.refreshCartBadge();

/* ---------- CONTACT FORM ---------- */
(function(){
  const form = document.getElementById('contactForm');
  if (!form) return;
  const success = document.getElementById('contactSuccess');
  form.addEventListener('submit', e=>{
    e.preventDefault();
    // demo: persist to localStorage; no backend on the static site
    const data = Object.fromEntries(new FormData(form).entries());
    const inbox = JSON.parse(localStorage.getItem('oyayi-contact') || '[]');
    inbox.push({ ...data, ts: Date.now() });
    localStorage.setItem('oyayi-contact', JSON.stringify(inbox));
    if (success) success.classList.add('show');
    form.reset();
    setTimeout(()=>{ if (success) success.classList.remove('show'); }, 6000);
  });
})();

/* ---------- NEWSLETTER FORM ---------- */
(function(){
  document.querySelectorAll('form.newsletter-form').forEach(form=>{
    form.addEventListener('submit', e=>{
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      const original = form.querySelector('button').textContent;
      const btn = form.querySelector('button');
      btn.textContent = 'Merci !';
      btn.style.background = 'var(--accent)';
      btn.style.color = 'var(--cream)';
      input.value = '';
      setTimeout(()=>{
        btn.textContent = original;
        btn.style.background = '';
        btn.style.color = '';
      }, 2400);
    });
  });
})();
