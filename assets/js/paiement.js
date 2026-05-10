/* ============================================================
   OYAYI Nature — checkout page (paiement.html)
   Form for shipping + payment method (Mobile Money / Cash / Card),
   confirms order with localStorage persistence and a success panel.
   ============================================================ */

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
function el(tag, attrs, text){
  const n = document.createElement(tag);
  if (attrs) for (const k in attrs) {
    if (k === 'class') n.className = attrs[k];
    else if (k === 'style' && typeof attrs[k] === 'object') for (const s in attrs[k]) n.style[s] = attrs[k][s];
    else n.setAttribute(k, attrs[k]);
  }
  if (text != null) n.textContent = text;
  return n;
}
function fmt(n){ return n.toLocaleString('fr-FR').replace(/,/g, ' '); }

function field(id, label, type, placeholder, required){
  const fld = el('div', { class: 'form-field' });
  const lbl = el('label', null, label); lbl.htmlFor = id;
  const inp = el('input'); inp.id = id; inp.name = id; inp.type = type || 'text'; inp.placeholder = placeholder || '';
  if (required) inp.required = true;
  fld.appendChild(lbl); fld.appendChild(inp);
  return fld;
}

let selectedMethod = 'mobile';

function renderCheckout(){
  const root = document.getElementById('checkoutContent');
  while (root.firstChild) root.removeChild(root.firstChild);
  const cart = window.OYAYI.cart;

  if (cart.length === 0) {
    const empty = el('div', { class: 'cart-empty-page' });
    empty.appendChild(svg('M3 6h2l2.5 12h11l2-9H6', 80, 80, 1.4));
    empty.appendChild(el('h2', null, 'Votre panier est vide'));
    empty.appendChild(el('p', null, 'Ajoutez des produits avant de passer commande.'));
    const a = el('a', { href: 'produits.html', class: 'cta' }, 'Voir le catalogue');
    empty.appendChild(a);
    root.appendChild(empty);
    return;
  }

  const grid = el('div', { class: 'checkout-grid' });

  // FORM
  const form = el('form', { class: 'checkout-form-wrap', id: 'orderForm' });

  function step(num, title){
    const h = el('h3');
    const stp = el('span', { class: 'stp' }, String(num));
    h.appendChild(stp);
    h.appendChild(document.createTextNode(' ' + title));
    return h;
  }

  // Step 1
  form.appendChild(step(1, 'Vos coordonnées'));
  const r1 = el('div', { class: 'form-row' });
  r1.appendChild(field('name', 'Nom complet', 'text', 'Marie KOUASSI', true));
  r1.appendChild(field('phone', 'Téléphone', 'tel', '+229 01 96 62 71 68', true));
  form.appendChild(r1);
  const r2 = el('div', { class: 'form-row' });
  r2.appendChild(field('email', 'E-mail', 'email', 'vous@example.com', true));
  r2.appendChild(field('city', 'Ville', 'text', 'Cotonou', true));
  form.appendChild(r2);
  form.appendChild(field('address', 'Adresse de livraison', 'text', 'Quartier · rue · indication', true));

  // Step 2 — payment methods
  form.appendChild(step(2, 'Mode de paiement'));
  const methods = el('div', { class: 'pay-methods' });
  const PAY = [
    { id: 'mobile', nm: 'Mobile Money', sub: 'MTN · Moov · Celtiis', icon: 'M5 4h14v16H5zM5 8h14M9 16h6' },
    { id: 'cash',   nm: 'À la livraison', sub: 'Espèces sur Cotonou', icon: 'M3 6h18v12H3zM3 12h18M16 9v6' },
    { id: 'card',   nm: 'Carte bancaire', sub: 'VISA · Mastercard',  icon: 'M3 6h18v12H3zM3 11h18M7 16h4' },
  ];

  PAY.forEach(m => {
    const card = el('div', { class: 'pay-method' + (m.id === selectedMethod ? ' selected' : '') });
    card.dataset.id = m.id;
    card.appendChild(svg(m.icon, 30, 30, 1.6));
    card.appendChild(el('div', { class: 'nm' }, m.nm));
    card.appendChild(el('div', { class: 'sub' }, m.sub));
    card.addEventListener('click', () => {
      selectedMethod = m.id;
      methods.querySelectorAll('.pay-method').forEach(x => x.classList.toggle('selected', x.dataset.id === selectedMethod));
      form.querySelectorAll('.pay-fields').forEach(x => x.classList.toggle('active', x.dataset.id === selectedMethod));
    });
    methods.appendChild(card);
  });
  form.appendChild(methods);

  // Mobile Money fields
  const mob = el('div', { class: 'pay-fields' + (selectedMethod === 'mobile' ? ' active' : '') });
  mob.dataset.id = 'mobile';
  mob.appendChild(field('momo', 'Numéro Mobile Money', 'tel', '+229 01 …'));
  mob.appendChild(field('momoOp', 'Opérateur', 'text', 'MTN, Moov ou Celtiis'));
  form.appendChild(mob);

  // Cash fields
  const cash = el('div', { class: 'pay-fields' + (selectedMethod === 'cash' ? ' active' : '') });
  cash.dataset.id = 'cash';
  const cashInfo = el('p', null, 'Paiement en espèces à la livraison à Cotonou et grande banlieue. Notre livreur vous contactera 30 minutes avant son passage.');
  cashInfo.style.color = 'var(--cream-2)';
  cashInfo.style.fontSize = '13px';
  cashInfo.style.lineHeight = '1.6';
  cashInfo.style.padding = '14px 18px';
  cashInfo.style.background = 'color-mix(in oklab,var(--cream) 4%,transparent)';
  cashInfo.style.borderRadius = '12px';
  cash.appendChild(cashInfo);
  form.appendChild(cash);

  // Card fields
  const card2 = el('div', { class: 'pay-fields' + (selectedMethod === 'card' ? ' active' : '') });
  card2.dataset.id = 'card';
  card2.appendChild(field('cardNum', 'Numéro de carte', 'text', '1234 5678 9012 3456'));
  const r3 = el('div', { class: 'form-row' });
  r3.appendChild(field('cardExp', 'Date d’expiration (MM / AA)', 'text', '12 / 28'));
  r3.appendChild(field('cardCvc', 'CVC', 'text', '123'));
  card2.appendChild(r3);
  form.appendChild(card2);

  // Submit
  const submit = el('button', { type: 'submit', class: 'form-submit' }, 'Confirmer la commande ');
  submit.style.marginTop = '24px';
  submit.appendChild(svg('M5 12h14m-6-6 6 6-6 6', 14, 14, 2));
  form.appendChild(submit);

  grid.appendChild(form);

  // SUMMARY
  const sum = el('aside', { class: 'summary' });
  sum.appendChild(el('h3', null, 'Votre commande'));
  cart.forEach(it => {
    const l = el('div', { class: 'line' });
    const a = el('span', null, (it.qty > 1 ? it.qty + '× ' : '') + it.name);
    a.style.maxWidth = '60%';
    const b = el('span', null, fmt(window.OYAYI.priceNum(it.price) * (it.qty || 1)) + ' CFA');
    l.appendChild(a); l.appendChild(b);
    sum.appendChild(l);
  });
  const subT = window.OYAYI.cartTotal();
  const ship = subT >= 35000 ? 0 : 2000;
  function lin(label, value, cls){
    const l = el('div', { class: 'line' + (cls ? ' ' + cls : '') });
    l.appendChild(el('span', null, label));
    l.appendChild(el('span', null, value));
    return l;
  }
  sum.appendChild(lin('Sous-total', fmt(subT) + ' CFA'));
  sum.appendChild(lin('Livraison', ship === 0 ? 'Offerte 🎁' : fmt(ship) + ' CFA'));
  sum.appendChild(lin('Total à payer', fmt(subT + ship) + ' CFA', 'total'));
  grid.appendChild(sum);

  // SUCCESS panel (hidden until submit)
  const success = el('div', { class: 'order-success', id: 'orderSuccess' });
  const ic = el('div', { class: 'ic' });
  ic.appendChild(svg('M5 12l5 5L20 7', 40, 40, 2));
  success.appendChild(ic);
  success.appendChild(el('h2', null, 'Commande confirmée !'));
  success.appendChild(el('p', null, 'Merci pour votre confiance. Notre équipe vous contactera sous 24 h pour finaliser la livraison.'));
  const ref = el('div', { class: 'ref', id: 'orderRef' });
  success.appendChild(ref);
  const cont = el('div');
  cont.style.marginTop = '20px';
  cont.style.display = 'flex';
  cont.style.gap = '14px';
  cont.style.justifyContent = 'center';
  cont.style.flexWrap = 'wrap';
  cont.appendChild(el('a', { href: 'index.html', class: 'cta' }, 'Retour à l’accueil'));
  cont.appendChild(el('a', { href: 'produits.html', class: 'cta ghost' }, 'Continuer mes achats'));
  success.appendChild(cont);

  root.appendChild(grid);
  root.appendChild(success);

  form.addEventListener('submit', e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    const orderRef = 'OYY-' + String(Date.now()).slice(-8);
    const orders = JSON.parse(localStorage.getItem('oyayi-orders') || '[]');
    orders.push({
      ref: orderRef,
      method: selectedMethod,
      total: subT + ship,
      shipping: ship,
      cart: window.OYAYI.cart.slice(),
      customer: data,
      date: new Date().toISOString(),
    });
    localStorage.setItem('oyayi-orders', JSON.stringify(orders));
    document.getElementById('orderRef').textContent = 'Référence : ' + orderRef;
    grid.style.display = 'none';
    success.classList.add('show');
    window.OYAYI.clearCart();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

renderCheckout();
