/* ============================================================
   OYAYI Nature — home page (carousel + collection grid)
   Uses DOM API (createElement / textContent) — no innerHTML.
   ============================================================ */

const PRODUCTS = [
  {id:'palmarosa', name:'Palmarosa', latin:'Cymbopogon martinii', price:'8 500', cat:'floral', tag:'Vedette',
   desc:'Apaise les peaux fragiles, équilibre l’humeur et rééquilibre les pièces de vie.',
   note:'Floral · Boisé', origin:'Plateau d’Abomey', alt:'Bénin · 100 % naturel',
   notes:['Géraniol','Linalol','Acétate'],
   theme:{c1:'#c97a4a', c2:'#7d8a4a', glow:'#d68f5e', leaf:'#a8b87a'}},
  {id:'lavande', name:'Lavande Vraie', latin:'Lavandula angustifolia', price:'9 500', cat:'floral', tag:'Apaisant',
   desc:'Apaise les tensions, favorise un sommeil profond. Fleur emblématique.',
   note:'Floral · Frais', origin:'Massif de l’Atakora', alt:'Bénin · récolte 2025',
   notes:['Linalol','Camphre','Cinéol'],
   theme:{c1:'#8a76b0', c2:'#5e4d8a', glow:'#a896c8', leaf:'#9b88c5'}},
  {id:'neroli', name:'Néroli', latin:'Citrus aurantium', price:'14 000', cat:'floral', tag:'Rare',
   desc:'Fleur d’oranger amer. Élève l’humeur, signature olfactive précieuse.',
   note:'Floral · Hespéridé', origin:'Vallée du Mono', alt:'Bénin · 100 % pure',
   notes:['Linalol','Limonène','Nérolidol'],
   theme:{c1:'#d6a23c', c2:'#8a5a14', glow:'#e8b850', leaf:'#c79a3c'}},
  {id:'tchayo', name:'Tchayo · Basilic Africain', latin:'Ocimum gratissimum', price:'5 000', cat:'leaf', tag:'Local',
   desc:'Plante symbolique du Bénin. Tonifiante, antibactérienne, aromatique puissante.',
   note:'Herbacé · Épicé', origin:'Plateau béninois', alt:'Récolte coopérative',
   notes:['Eugénol','Thymol','Linalol'],
   theme:{c1:'#5a8a5e', c2:'#1d3a23', glow:'#7ea872', leaf:'#9bbf7e'}},
  {id:'basilic', name:'Basilic', latin:'Ocimum basilicum', price:'6 000', cat:'leaf',
   desc:'Tonique digestif, anti-stress, signature culinaire fine.',
   note:'Herbacé · Anisé', origin:'Plaines de la Mono', alt:'Bénin · récolte locale',
   notes:['Linalol','Methyl-chavicol'],
   theme:{c1:'#3e7042', c2:'#1a3320', glow:'#5e9258', leaf:'#7ea870'}},
  {id:'menthe-poivree', name:'Menthe Poivrée', latin:'Mentha × piperita', price:'6 500', cat:'leaf',
   desc:'Fraîcheur intense, stimule la concentration. Récoltée à l’aube.',
   note:'Vert · Mentholé', origin:'Région d’Abomey', alt:'Bénin · récolte 2025',
   notes:['Menthol','Menthone','Cinéol'],
   theme:{c1:'#3ea872', c2:'#1d4a3a', glow:'#6dd098', leaf:'#7eddae'}},
  {id:'laurier', name:'Laurier Noble', latin:'Laurus nobilis', price:'7 500', cat:'leaf', tag:'Vedette',
   desc:'Anti-infectieux puissant, soutien l’immunité, signature digne.',
   note:'Boisé · Camphré', origin:'Massif de l’Atakora', alt:'Bénin · sélection',
   notes:['Cinéol','Linalol','Eugénol'],
   theme:{c1:'#4a7032', c2:'#1d2e16', glow:'#6e9248', leaf:'#a8c878'}},
  {id:'origan', name:'Origan', latin:'Origanum vulgare', price:'7 000', cat:'leaf',
   desc:'Antibactérien majeur. Force minérale, défense naturelle.',
   note:'Épicé · Phénolé', origin:'Pentes du nord Bénin', alt:'Récolte 2025',
   notes:['Carvacrol','Thymol','γ-Terpinène'],
   theme:{c1:'#6a8a3a', c2:'#2e3e16', glow:'#8eaa56', leaf:'#a8be6c'}},
  {id:'niaouli', name:'Niaouli', latin:'Melaleuca quinquenervia', price:'6 500', cat:'leaf',
   desc:'Décongestionnant respiratoire, antiviral, peau régénérée.',
   note:'Frais · Médicinal', origin:'Côte de Cotonou', alt:'Bénin · 100 % pure',
   notes:['1,8-Cinéol','α-Pinène','Viridiflorol'],
   theme:{c1:'#3a8aa8', c2:'#163d52', glow:'#5ec0d8', leaf:'#7ec8d8'}},
  {id:'mandarine', name:'Mandarine', latin:'Citrus reticulata', price:'5 500', cat:'citrus',
   desc:'Pétillante et solaire, calme l’agitation, parfume avec joie.',
   note:'Hespéridé · Sucré', origin:'Vergers du Mono', alt:'Bénin · récolte 2025',
   notes:['Limonène','γ-Terpinène','Myrcène'],
   theme:{c1:'#e08a3a', c2:'#8a3e10', glow:'#f0a256', leaf:'#dba070'}},
  {id:'orange-douce', name:'Orange Douce', latin:'Citrus sinensis', price:'5 000', cat:'citrus',
   desc:'Joyeuse, réconfortante. La signature lumineuse du Bénin.',
   note:'Hespéridé · Solaire', origin:'Plateaux d’Abomey', alt:'Bénin · 100 % pure',
   notes:['Limonène','Myrcène','Linalol'],
   theme:{c1:'#e89c2a', c2:'#8e4a0e', glow:'#f5b94c', leaf:'#dba040'}},
  {id:'myrrhe', name:'Myrrhe', latin:'Commiphora myrrha', price:'12 000', cat:'resin', tag:'Précieux',
   desc:'Résine sacrée des temps anciens. Cicatrisante profonde, méditative.',
   note:'Résineux · Balsamique', origin:'Sahel · partenaire équitable', alt:'Sélection 2025',
   notes:['Furanodiène','Curzérène','β-Élémène'],
   theme:{c1:'#a85e2e', c2:'#3e1d10', glow:'#c08055', leaf:'#a87e5e'}},
  {id:'muscade', name:'Muscade', latin:'Myristica fragrans', price:'6 500', cat:'spice',
   desc:'Chaude, épicée, réconfortante. Soutient la digestion, réchauffe.',
   note:'Épicé · Boisé', origin:'Marché de Cotonou', alt:'Sélection 2025',
   notes:['Sabinène','α-Pinène','Myristicine'],
   theme:{c1:'#8a5a2e', c2:'#3a2010', glow:'#a87648', leaf:'#a88a5e'}},
];

/* ---- Tiny safe DOM helpers (no innerHTML) ---- */
const SVG_NS = 'http://www.w3.org/2000/svg';
function el(tag, attrs, children){
  const isSvg = tag === 'svg' || tag === 'path';
  const node = isSvg ? document.createElementNS(SVG_NS, tag) : document.createElement(tag);
  if (attrs) for (const k in attrs) {
    if (k === 'class') node.className = attrs[k];
    else if (k === 'text') node.textContent = attrs[k];
    else if (k === 'on' && typeof attrs[k] === 'object') {
      for (const ev in attrs[k]) node.addEventListener(ev, attrs[k][ev]);
    }
    else if (k === 'data' && typeof attrs[k] === 'object') {
      for (const dk in attrs[k]) node.dataset[dk] = attrs[k][dk];
    }
    else if (k === 'style' && typeof attrs[k] === 'object') {
      for (const sk in attrs[k]) node.style.setProperty(sk, attrs[k][sk]);
    }
    else if (isSvg) node.setAttributeNS(null, k, attrs[k]);
    else node.setAttribute(k, attrs[k]);
  }
  if (children) (Array.isArray(children) ? children : [children]).forEach(c => {
    if (c == null) return;
    node.appendChild(c.nodeType ? c : document.createTextNode(String(c)));
  });
  return node;
}
function plusIcon(){
  const svg = el('svg', {width:'16', height:'16', viewBox:'0 0 24 24', fill:'none', stroke:'currentColor', 'stroke-width':'2'});
  svg.appendChild(el('path', {d:'M12 5v14M5 12h14'}));
  return svg;
}

/* ============================================================
   CAROUSEL HERO
   ============================================================ */
let idx = 0;
let auto = true;
let dynBg = true;
let timer = null;

const $bottle = document.getElementById('bottleImg');
const $hero = document.getElementById('hero');
const $thumbs = document.getElementById('thumbs');
const $heroAccent = document.getElementById('heroAccent');
const $ifNote = document.getElementById('ifNote');
const $ifNoteSub = document.getElementById('ifNoteSub');
const $ifOrigin = document.getElementById('ifOrigin');
const $ifAltitude = document.getElementById('ifAltitude');
const $pcLatin = document.getElementById('pcLatin');
const $pcName = document.getElementById('pcName');
const $pcDesc = document.getElementById('pcDesc');
const $pcNotes = document.getElementById('pcNotes');
const $pcPrice = document.getElementById('pcPrice');
const $carIdx = document.getElementById('carIdx');
const $pcAdd = document.getElementById('pcAdd');

function buildThumbs(){
  while ($thumbs.firstChild) $thumbs.removeChild($thumbs.firstChild);
  PRODUCTS.forEach((p, i) => {
    const img = el('img', {src:`assets/products/${p.id}.png`, alt:p.name});
    const tn = el('span', {class:'tn', text:String(i+1).padStart(2,'0')});
    const t = el('button', {
      class: 'thumb' + (i===0?' active':''),
      data: { idx: String(i) },
      on: { click: ()=> go(i, true) }
    }, [img, tn]);
    $thumbs.appendChild(t);
  });
}
buildThumbs();

function applyTheme(p){
  if (!dynBg) {
    $hero.style.removeProperty('--theme-1');
    $hero.style.removeProperty('--theme-2');
    $hero.style.removeProperty('--theme-glow');
    $hero.style.removeProperty('--theme-leaf');
    return;
  }
  $hero.style.setProperty('--theme-1', p.theme.c1);
  $hero.style.setProperty('--theme-2', p.theme.c2);
  $hero.style.setProperty('--theme-glow', p.theme.glow);
  $hero.style.setProperty('--theme-leaf', p.theme.leaf);
}

function go(i, fromClick=false){
  idx = (i + PRODUCTS.length) % PRODUCTS.length;
  const p = PRODUCTS[idx];
  $bottle.classList.add('swap');
  $bottle.style.opacity = 0;
  $bottle.style.transform = 'translateY(10px) scale(.96)';
  setTimeout(()=>{
    $bottle.src = `assets/products/${p.id}.png`;
    $bottle.alt = `Huile essentielle ${p.name}`;
    $bottle.style.opacity = 1;
    $bottle.style.transform = '';
    requestAnimationFrame(()=>$bottle.classList.remove('swap'));
  }, 240);
  applyTheme(p);
  $heroAccent.textContent = p.name.toLowerCase().split(' ')[0];
  $ifNote.textContent = p.note;
  $ifNoteSub.textContent = p.latin;
  $ifOrigin.textContent = p.origin;
  $ifAltitude.textContent = p.alt;
  $pcLatin.textContent = p.latin;
  $pcName.textContent = p.name;
  $pcDesc.textContent = p.desc;
  $pcPrice.textContent = p.price;
  while ($pcNotes.firstChild) $pcNotes.removeChild($pcNotes.firstChild);
  p.notes.forEach(n => $pcNotes.appendChild(el('span', {class:'note', text:n})));
  $carIdx.textContent = String(idx+1).padStart(2,'0');
  document.querySelectorAll('.thumb').forEach(t=>t.classList.toggle('active', +t.dataset.idx===idx));
  const active = $thumbs.querySelector('.thumb.active');
  if (active){
    const target = active.offsetLeft - ($thumbs.clientWidth/2) + (active.clientWidth/2);
    $thumbs.scrollTo({left: Math.max(0,target), behavior:'smooth'});
  }
  if (fromClick) restartAuto();
}

function restartAuto(){
  clearInterval(timer);
  if (auto) timer = setInterval(()=>go(idx+1), 3500);
}

document.getElementById('next').addEventListener('click', ()=>go(idx+1, true));
document.getElementById('prev').addEventListener('click', ()=>go(idx-1, true));
$pcAdd.addEventListener('click', e=>{
  e.stopPropagation();
  const p = PRODUCTS[idx];
  window.OYAYI && window.OYAYI.addToCart({id:p.id, name:p.name, price:p.price, image:`assets/products/${p.id}.png`});
});
go(0);
restartAuto();

/* ============================================================
   COLLECTION GRID
   ============================================================ */
const grid = document.getElementById('pgrid');

function buildPCard(p){
  const card = el('article', {
    class:'pcard',
    style: { '--c-glow': p.theme.glow }
  });
  if (p.tag) {
    const isHot = (p.tag==='Vedette' || p.tag==='Rare' || p.tag==='Précieux');
    card.appendChild(el('span', {class:'tag' + (isHot?' hot':''), text:p.tag}));
  }
  card.appendChild(el('div', {class:'latin', text:p.latin}));
  card.appendChild(el('div', {class:'name', text:p.name}));
  const imgWrap = el('div', {class:'img'}, [el('img', {src:`assets/products/${p.id}.png`, alt:p.name})]);
  card.appendChild(imgWrap);
  const priceWrap = el('div', {class:'price'}, [
    document.createTextNode(p.price + ' '),
    el('small', {text:'CFA · 100 ml'})
  ]);
  const addBtn = el('button', {
    class:'add', 'aria-label':'Ajouter',
    data: { id: p.id },
    on: { click: (e)=> { e.stopPropagation(); window.OYAYI && window.OYAYI.addToCart({id:p.id, name:p.name, price:p.price, image:`assets/products/${p.id}.png`}); } }
  }, [plusIcon()]);
  card.appendChild(el('div', {class:'foot'}, [priceWrap, addBtn]));
  card.addEventListener('click', (e)=>{
    if (e.target.closest('.add')) return;
    const i = PRODUCTS.findIndex(x=>x.id===p.id);
    go(i, true);
    window.scrollTo({top:0, behavior:'smooth'});
  });
  return card;
}

function renderGrid(filter='all'){
  while (grid.firstChild) grid.removeChild(grid.firstChild);
  const list = filter==='all' ? PRODUCTS : PRODUCTS.filter(p=>p.cat===filter);
  list.forEach(p => grid.appendChild(buildPCard(p)));
}
renderGrid();

document.querySelectorAll('#chips .chip').forEach(c=>{
  c.addEventListener('click',()=>{
    document.querySelectorAll('#chips .chip').forEach(x=>x.classList.remove('active'));
    c.classList.add('active');
    renderGrid(c.dataset.cat);
  });
});

/* pause auto on hero hover */
$hero.addEventListener('mouseenter', ()=>{ clearInterval(timer); });
$hero.addEventListener('mouseleave', ()=>{ restartAuto(); });

/* keyboard nav */
window.addEventListener('keydown', e=>{
  if (e.key === 'ArrowRight') go(idx+1, true);
  if (e.key === 'ArrowLeft') go(idx-1, true);
});
