/* ============================================================
   OYAYI Nature — shared site JS (v2)
   Loader, theme toggle, mobile drawer, cart drawer + persistence,
   contact form, newsletter form.
   ============================================================ */

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

/* ============================================================
   CART SYSTEM — drawer, persistence, qty management
   ============================================================ */
window.OYAYI = window.OYAYI || {};

// load cart from storage
function loadCart(){
  try { return JSON.parse(localStorage.getItem('oyayi-cart') || '[]'); }
  catch(e){ return []; }
}
function saveCart(cart){
  localStorage.setItem('oyayi-cart', JSON.stringify(cart));
}

// Parse "8 500" → 8500
function priceNum(p){
  if (typeof p === 'number') return p;
  return parseInt(String(p).replace(/[^0-9]/g, ''), 10) || 0;
}
function fmtPrice(n){
  return n.toLocaleString('fr-FR').replace(/,/g, ' ');
}

window.OYAYI.cart = loadCart();
window.OYAYI.cartCount = () => window.OYAYI.cart.reduce((s, it) => s + (it.qty || 1), 0);
window.OYAYI.cartTotal = () => window.OYAYI.cart.reduce((s, it) => s + priceNum(it.price) * (it.qty || 1), 0);

window.OYAYI.refreshCartBadge = function(){
  const count = window.OYAYI.cartCount();
  document.querySelectorAll('.cart-badge').forEach(b => {
    b.textContent = String(count).padStart(2, '0');
  });
};

window.OYAYI.addToCart = function(item){
  // item: {id, name, price, image?}
  const cart = window.OYAYI.cart;
  const existing = cart.find(it => it.id === item.id);
  if (existing) {
    existing.qty = (existing.qty || 1) + 1;
  } else {
    cart.push({ id: item.id, name: item.name, price: item.price, image: item.image || '', qty: 1 });
  }
  saveCart(cart);
  window.OYAYI.refreshCartBadge();
  // bump animation
  document.querySelectorAll('.cart-badge').forEach(b => {
    b.classList.add('bump');
    setTimeout(()=>b.classList.remove('bump'), 250);
  });
  // open drawer
  if (window.OYAYI.openCart) window.OYAYI.openCart();
  if (window.OYAYI.renderCart) window.OYAYI.renderCart();
};

window.OYAYI.removeFromCart = function(id){
  window.OYAYI.cart = window.OYAYI.cart.filter(it => it.id !== id);
  saveCart(window.OYAYI.cart);
  window.OYAYI.refreshCartBadge();
  if (window.OYAYI.renderCart) window.OYAYI.renderCart();
};

window.OYAYI.changeQty = function(id, delta){
  const it = window.OYAYI.cart.find(x => x.id === id);
  if (!it) return;
  it.qty = Math.max(0, (it.qty || 1) + delta);
  if (it.qty === 0) {
    window.OYAYI.removeFromCart(id);
    return;
  }
  saveCart(window.OYAYI.cart);
  window.OYAYI.refreshCartBadge();
  if (window.OYAYI.renderCart) window.OYAYI.renderCart();
};

window.OYAYI.clearCart = function(){
  window.OYAYI.cart = [];
  saveCart([]);
  window.OYAYI.refreshCartBadge();
  if (window.OYAYI.renderCart) window.OYAYI.renderCart();
};

/* ---------- CART DRAWER (auto-mounted on every page) ---------- */
(function(){
  const SVG_NS = 'http://www.w3.org/2000/svg';
  function svg(d, w, h, sw){
    const s = document.createElementNS(SVG_NS, 'svg');
    s.setAttributeNS(null, 'width', w || 16);
    s.setAttributeNS(null, 'height', h || 16);
    s.setAttributeNS(null, 'viewBox', '0 0 24 24');
    s.setAttributeNS(null, 'fill', 'none');
    s.setAttributeNS(null, 'stroke', 'currentColor');
    s.setAttributeNS(null, 'stroke-width', sw || 1.6);
    const p = document.createElementNS(SVG_NS, 'path');
    p.setAttributeNS(null, 'd', d);
    s.appendChild(p);
    return s;
  }

  // Build drawer DOM
  const backdrop = document.createElement('div');
  backdrop.className = 'cart-backdrop';
  const drawer = document.createElement('aside');
  drawer.className = 'cart-drawer';
  drawer.setAttribute('aria-label', 'Panier');

  // Head
  const head = document.createElement('div');
  head.className = 'cart-head';
  const title = document.createElement('h3');
  title.appendChild(document.createTextNode('Votre panier'));
  const small = document.createElement('small');
  small.id = 'cd-count';
  small.textContent = '0 article';
  title.appendChild(small);
  head.appendChild(title);
  const closeBtn = document.createElement('button');
  closeBtn.className = 'cart-close';
  closeBtn.setAttribute('aria-label', 'Fermer le panier');
  closeBtn.appendChild(svg('M18 6 6 18M6 6l12 12', 14, 14, 2));
  head.appendChild(closeBtn);
  drawer.appendChild(head);

  // List
  const list = document.createElement('div');
  list.className = 'cart-list';
  list.id = 'cd-list';
  drawer.appendChild(list);

  // Foot
  const foot = document.createElement('div');
  foot.className = 'cart-foot';
  foot.id = 'cd-foot';
  drawer.appendChild(foot);

  document.body.appendChild(backdrop);
  document.body.appendChild(drawer);

  function openCart(){
    drawer.classList.add('open');
    backdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
    renderDrawer();
  }
  function closeCart(){
    drawer.classList.remove('open');
    backdrop.classList.remove('open');
    document.body.style.overflow = '';
  }
  closeBtn.addEventListener('click', closeCart);
  backdrop.addEventListener('click', closeCart);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeCart(); });

  // Hook up the navbar cart button
  document.querySelectorAll('a.cta').forEach(a => {
    if (a.querySelector('.cart-badge')) {
      a.addEventListener('click', e => {
        // On the dedicated cart page, do not intercept
        if (location.pathname.endsWith('/panier') || location.pathname.endsWith('/panier.html')) return;
        e.preventDefault();
        openCart();
      });
    }
  });

  function renderDrawer(){
    while (list.firstChild) list.removeChild(list.firstChild);
    const cart = window.OYAYI.cart;
    document.getElementById('cd-count').textContent = `${window.OYAYI.cartCount()} article${window.OYAYI.cartCount() > 1 ? 's' : ''}`;

    if (cart.length === 0) {
      const empty = document.createElement('div');
      empty.className = 'cart-empty';
      empty.appendChild(svg('M3 6h2l2.5 12h11l2-9H6', 50, 50, 1.4));
      const t = document.createElement('div');
      t.style.fontFamily = '"Fraunces", serif';
      t.style.fontSize = '20px';
      t.style.color = 'var(--cream)';
      t.style.marginBottom = '8px';
      t.textContent = 'Votre panier est vide';
      empty.appendChild(t);
      const p = document.createElement('div');
      p.textContent = 'Découvrez nos huiles essentielles, miels et soins naturels.';
      empty.appendChild(p);
      list.appendChild(empty);
    } else {
      cart.forEach(it => {
        const row = document.createElement('div');
        row.className = 'cart-item';
        const img = document.createElement('div');
        img.className = 'ci-img';
        if (it.image) {
          const i = document.createElement('img');
          i.src = it.image;
          i.alt = it.name;
          img.appendChild(i);
        } else {
          const ph = document.createElement('span');
          ph.className = 'ph';
          ph.appendChild(svg('M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12z', 26, 26, 1.4));
          img.appendChild(ph);
        }
        row.appendChild(img);
        const info = document.createElement('div');
        info.className = 'ci-info';
        const nm = document.createElement('div');
        nm.className = 'nm';
        nm.textContent = it.name;
        info.appendChild(nm);
        const pr = document.createElement('div');
        pr.className = 'pr';
        pr.textContent = fmtPrice(priceNum(it.price)) + ' CFA';
        info.appendChild(pr);
        row.appendChild(info);
        const ctrl = document.createElement('div');
        ctrl.style.display = 'flex';
        ctrl.style.flexDirection = 'column';
        ctrl.style.alignItems = 'flex-end';
        ctrl.style.gap = '8px';
        const qty = document.createElement('div');
        qty.className = 'ci-qty';
        const minus = document.createElement('button');
        minus.textContent = '−';
        minus.setAttribute('aria-label', 'Diminuer');
        minus.addEventListener('click', () => window.OYAYI.changeQty(it.id, -1));
        const qv = document.createElement('span');
        qv.className = 'qv';
        qv.textContent = it.qty || 1;
        const plus = document.createElement('button');
        plus.textContent = '+';
        plus.setAttribute('aria-label', 'Augmenter');
        plus.addEventListener('click', () => window.OYAYI.changeQty(it.id, +1));
        qty.appendChild(minus); qty.appendChild(qv); qty.appendChild(plus);
        ctrl.appendChild(qty);
        const rm = document.createElement('button');
        rm.className = 'ci-rm';
        rm.setAttribute('aria-label', 'Supprimer');
        rm.appendChild(svg('M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14M10 11v6M14 11v6', 16, 16, 1.6));
        rm.addEventListener('click', () => window.OYAYI.removeFromCart(it.id));
        ctrl.appendChild(rm);
        row.appendChild(ctrl);
        list.appendChild(row);
      });
    }

    // Foot
    while (foot.firstChild) foot.removeChild(foot.firstChild);
    const subRow = document.createElement('div');
    subRow.className = 'row';
    const sub1 = document.createElement('span'); sub1.textContent = 'Sous-total';
    const sub2 = document.createElement('span'); sub2.textContent = fmtPrice(window.OYAYI.cartTotal()) + ' CFA';
    subRow.appendChild(sub1); subRow.appendChild(sub2);
    foot.appendChild(subRow);
    const ship = document.createElement('div');
    ship.className = 'row';
    const ship1 = document.createElement('span'); ship1.textContent = 'Livraison';
    const ship2 = document.createElement('span'); ship2.textContent = 'Calculée à l’étape suivante';
    ship.appendChild(ship1); ship.appendChild(ship2);
    foot.appendChild(ship);
    const totRow = document.createElement('div');
    totRow.className = 'row total';
    const t1 = document.createElement('span'); t1.textContent = 'Total';
    const t2 = document.createElement('span'); t2.textContent = fmtPrice(window.OYAYI.cartTotal()) + ' CFA';
    totRow.appendChild(t1); totRow.appendChild(t2);
    foot.appendChild(totRow);

    const actions = document.createElement('div');
    actions.className = 'actions';
    const checkout = document.createElement('a');
    checkout.href = 'paiement.html';
    checkout.className = 'checkout-btn';
    checkout.textContent = 'Passer au paiement ';
    if (cart.length === 0) {
      checkout.style.pointerEvents = 'none';
      checkout.style.opacity = '.4';
    }
    const arr = svg('M5 12h14m-6-6 6 6-6 6', 14, 14, 2);
    checkout.appendChild(arr);
    actions.appendChild(checkout);
    const view = document.createElement('a');
    view.href = 'panier.html';
    view.className = 'view-cart';
    view.textContent = 'Voir le panier complet';
    actions.appendChild(view);
    foot.appendChild(actions);
  }

  window.OYAYI.openCart = openCart;
  window.OYAYI.closeCart = closeCart;
  window.OYAYI.renderCart = renderDrawer;
  window.OYAYI.fmtPrice = fmtPrice;
  window.OYAYI.priceNum = priceNum;

  window.OYAYI.refreshCartBadge();
})();

/* ---------- CONTACT FORM ---------- */
(function(){
  const form = document.getElementById('contactForm');
  if (!form) return;
  const success = document.getElementById('contactSuccess');
  form.addEventListener('submit', e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    const inbox = JSON.parse(localStorage.getItem('oyayi-contact') || '[]');
    inbox.push({ ...data, ts: Date.now() });
    localStorage.setItem('oyayi-contact', JSON.stringify(inbox));
    if (success) success.classList.add('show');
    form.reset();
    setTimeout(() => { if (success) success.classList.remove('show'); }, 6000);
  });
})();

/* ---------- NEWSLETTER FORM ---------- */
(function(){
  document.querySelectorAll('form.newsletter-form').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const input = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button');
      const original = btn.textContent;
      btn.textContent = 'Merci !';
      btn.style.background = 'var(--accent)';
      btn.style.color = 'var(--cream)';
      input.value = '';
      setTimeout(() => {
        btn.textContent = original;
        btn.style.background = '';
        btn.style.color = '';
      }, 2400);
    });
  });
})();
