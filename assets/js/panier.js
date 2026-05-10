/* ============================================================
   OYAYI Nature — full cart page (panier.html)
   Renders cart with quantity controls + summary, links to checkout.
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

function renderCartPage(){
  const root = document.getElementById('cartContent');
  while (root.firstChild) root.removeChild(root.firstChild);
  const cart = window.OYAYI.cart;

  if (cart.length === 0) {
    const empty = el('div', { class: 'cart-empty-page' });
    empty.appendChild(svg('M3 6h2l2.5 12h11l2-9H6', 80, 80, 1.4));
    empty.appendChild(el('h2', null, 'Votre panier est vide'));
    empty.appendChild(el('p', null, 'Découvrez nos huiles essentielles, miels et soins naturels.'));
    const link = el('a', { href: 'produits.html', class: 'cta' }, 'Voir le catalogue ');
    link.appendChild(svg('M5 12h14m-6-6 6 6-6 6', 14, 14, 2));
    empty.appendChild(link);
    root.appendChild(empty);
    return;
  }

  const grid = el('div', { class: 'cart-page' });

  // Cart table
  const table = el('div', { class: 'cart-table' });
  const headerRow = el('div', { class: 'row-h' });
  ['', 'Produit', 'Quantité', 'Total', ''].forEach(t => headerRow.appendChild(el('div', null, t)));
  table.appendChild(headerRow);

  cart.forEach(it => {
    const row = el('div', { class: 'row' });

    const img = el('div', { class: 'img' });
    if (it.image) {
      const i = el('img'); i.src = it.image; i.alt = it.name; img.appendChild(i);
    } else {
      const ph = el('span', { class: 'ph' });
      ph.appendChild(svg('M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12z', 30, 30, 1.4));
      img.appendChild(ph);
    }
    row.appendChild(img);

    const nm = el('div', { class: 'nm' }, it.name);
    const sub = el('span', { class: 'sub' }, fmt(window.OYAYI.priceNum(it.price)) + ' CFA / unité');
    nm.appendChild(sub);
    row.appendChild(nm);

    const qty = el('div', { class: 'qty' });
    const minus = el('button', { 'aria-label': 'Diminuer' }, '−');
    minus.addEventListener('click', () => { window.OYAYI.changeQty(it.id, -1); renderCartPage(); });
    const qv = el('span', { class: 'qv' }, String(it.qty || 1));
    const plus = el('button', { 'aria-label': 'Augmenter' }, '+');
    plus.addEventListener('click', () => { window.OYAYI.changeQty(it.id, +1); renderCartPage(); });
    qty.appendChild(minus); qty.appendChild(qv); qty.appendChild(plus);
    row.appendChild(qty);

    row.appendChild(el('div', { class: 'total-pr' },
      fmt(window.OYAYI.priceNum(it.price) * (it.qty || 1)) + ' CFA'));

    const rm = el('button', { class: 'rm', 'aria-label': 'Supprimer' });
    rm.appendChild(svg('M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14M10 11v6M14 11v6'));
    rm.addEventListener('click', () => { window.OYAYI.removeFromCart(it.id); renderCartPage(); });
    row.appendChild(rm);

    table.appendChild(row);
  });
  grid.appendChild(table);

  // Summary
  const sum = el('aside', { class: 'summary' });
  sum.appendChild(el('h3', null, 'Récapitulatif'));

  const subT = window.OYAYI.cartTotal();
  const ship = subT >= 35000 ? 0 : 2000;

  function line(label, value, cls){
    const l = el('div', { class: 'line' + (cls ? ' ' + cls : '') });
    l.appendChild(el('span', null, label));
    l.appendChild(el('span', null, value));
    return l;
  }
  sum.appendChild(line('Sous-total (' + window.OYAYI.cartCount() + ' articles)', fmt(subT) + ' CFA'));
  sum.appendChild(line('Livraison estimée', ship === 0 ? 'Offerte 🎁' : fmt(ship) + ' CFA'));
  sum.appendChild(line('Total', fmt(subT + ship) + ' CFA', 'total'));

  const promo = el('div', { class: 'promo' });
  const inp = el('input'); inp.type = 'text'; inp.placeholder = 'Code promo';
  const btnP = el('button', null, 'Appliquer');
  btnP.addEventListener('click', () => alert('Code promo bientôt disponible. Merci de votre patience !'));
  promo.appendChild(inp); promo.appendChild(btnP);
  sum.appendChild(promo);

  const pay = el('a', { href: 'paiement.html', class: 'pay-btn' }, 'Passer au paiement ');
  pay.appendChild(svg('M5 12h14m-6-6 6 6-6 6', 14, 14, 2));
  sum.appendChild(pay);

  const sec = el('div', { class: 'secure' });
  sec.appendChild(svg('M5 11h14v10H5zM8 11V7a4 4 0 0 1 8 0v4', 12, 12, 1.8));
  sec.appendChild(document.createTextNode('Paiement 100 % sécurisé'));
  sum.appendChild(sec);

  grid.appendChild(sum);
  root.appendChild(grid);
}

renderCartPage();
// keep drawer + page in sync if user opens drawer from this page
const _origRenderCart = window.OYAYI.renderCart;
window.OYAYI.renderCart = function(){
  if (typeof _origRenderCart === 'function') _origRenderCart();
  renderCartPage();
};
