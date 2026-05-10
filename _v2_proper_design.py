# -*- coding: utf-8 -*-
"""V2 = Claude Design's file deployed AS-IS for the homepage, plus the
same body::before/body::after luminous-ivory pattern applied to every
other V2 page so they share the same atmosphere."""

import os, shutil, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(ROOT, 'v2')
INBOX = os.path.join(ROOT, '_v2_inbox_v4')

# --- 1. Wipe v2 and recreate ---
if os.path.exists(V2):
    shutil.rmtree(V2)
os.makedirs(os.path.join(V2, 'assets', 'css'))
os.makedirs(os.path.join(V2, 'assets', 'js'))

# --- 2. Copy all V1 HTML pages to v2/ (for non-home pages) ---
for f in sorted(os.listdir(ROOT)):
    if f.endswith('.html') and not f.startswith('_'):
        shutil.copy(os.path.join(ROOT, f), os.path.join(V2, f))

# --- 3. Copy assets ---
for folder in ['products', 'catalog', 'distinctions']:
    src = os.path.join(ROOT, 'assets', folder)
    if os.path.exists(src):
        shutil.copytree(src, os.path.join(V2, 'assets', folder))
for f in os.listdir(os.path.join(ROOT, 'assets', 'js')):
    shutil.copy(os.path.join(ROOT, 'assets', 'js', f),
                os.path.join(V2, 'assets', 'js', f))

# --- 4. Build v2 CSS = V1 base + ivory-lumiere override with body::before/::after ---
with open(os.path.join(ROOT, 'assets', 'css', 'oyayi.css'), 'r', encoding='utf-8') as f:
    base_css = f.read()

ivory_lumiere_block = """

  /* ============================================================
     V2 — IVOIRE LUMIÈRE (Claude Design pattern)
     Body itself transparent. body::before draws a fixed 4-stop
     luminous gradient (#FAFAF7 -> #FFF8E1 -> #F4F1E8 -> #F0EDE3).
     body::after layers an SVG fractal-noise overlay at 40 % opacity
     with mix-blend-mode: overlay — gives the page warmth + texture
     instead of a flat white. This is the "ivory light" feel.
     The hero/page-hero contain a GREEN BAND via ::before with
     inset 80px 5% 30px and 32px radius, like the OYAYI Sens flyer.
     ============================================================ */
  :root,
  :root[data-da="green"],
  :root[data-da="brown"]{
    --bg-deep:#FAFAF7 !important;
    --bg-mid:#FFFFFF !important;
    --bg-soft:#FFF8E1 !important;
    --bg-soft-2:#F4F1E8 !important;
    --bg-page-grad-top:#FAFAF7;
    --bg-page-grad-bot:#F0EDE3;
    --cream:#1B5E20 !important;
    --cream-2:#3E5A3F !important;
    --leaf-light:#2E7D32 !important;
    --green-mid:#2E7D32 !important;
    --green-pale:#A5D6A7 !important;
    --green-deep:#0E3A14 !important;
    --accent:#C8A84B !important;
    --accent-2:#A78A2E !important;
    --accent-soft:#FFF8E1 !important;
    --ink:#FAFAF7 !important;
    --line:rgba(27,94,32,.16) !important;
    --hairline:rgba(27,94,32,.08) !important;
    --hero-band:linear-gradient(135deg, #1B5E20 0%, #0E3A14 100%);
  }

  /* THE luminous ivory page surface — body transparent, gradient via ::before */
  html, body{background:transparent !important;color:var(--cream) !important;font-family:"DM Sans",sans-serif !important}
  body::before{
    content:"" !important;position:fixed !important;inset:0 !important;z-index:-3 !important;pointer-events:none !important;
    background:linear-gradient(180deg, #FAFAF7 0%, #FFF8E1 35%, #F4F1E8 70%, #F0EDE3 100%) !important;
    transition:background .8s ease;
  }
  body::after{
    content:"" !important;position:fixed !important;inset:0 !important;z-index:-2 !important;pointer-events:none !important;opacity:.4 !important;mix-blend-mode:overlay !important;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='280' height='280'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.82' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .98 0 0 0 0 .96 0 0 0 0 .85 0 0 0 .10 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>") !important;
  }

  .theme-fab{display:none !important}

  /* LOADER on luminous ivory */
  .loader-overlay{
    background:radial-gradient(ellipse at 50% 60%, color-mix(in oklab, var(--accent) 25%, var(--bg-soft)), #FAFAF7 70%) !important;
  }
  .loader-brand{color:var(--cream)}
  .loader-brand small{color:var(--cream-2)}
  .loader-mark::after{border-color:rgba(27,94,32,.30) !important}
  .loader-bar{background:rgba(27,94,32,.14) !important}

  /* NAV — Claude Design's brand mark style */
  .nav{
    background:linear-gradient(to bottom, color-mix(in oklab, #FAFAF7 88%, transparent) 0%, transparent 100%) !important;
    backdrop-filter:blur(14px) !important;
    border-bottom:1px solid rgba(200,168,75,.18) !important;
  }
  .brand{
    font-family:"Playfair Display",serif !important;font-weight:900 !important;
    font-size:22px !important;letter-spacing:.22em !important;color:#1B5E20 !important;
    display:flex;align-items:center;gap:12px;
  }
  .brand > span:not(.mark){font-family:"DM Sans",sans-serif !important;font-weight:500 !important;font-size:9px !important;letter-spacing:.4em !important;color:#2E7D32 !important;opacity:1 !important}
  .brand .mark{
    background:radial-gradient(circle at 30% 30%, #FFF8E1, var(--accent) 55%, var(--accent-2)) !important;
    box-shadow:inset 0 0 0 1px rgba(255,248,225,.30), 0 4px 14px rgba(200,168,75,.45) !important;
  }
  .nav-links a{color:var(--cream) !important;opacity:.85}
  .nav-links a:hover{opacity:1;color:var(--accent-2) !important}
  .nav-links a.active{opacity:1}
  .nav-links a.active::after{background:var(--accent) !important;height:1px !important}
  .icon-btn{border-color:rgba(27,94,32,.18) !important;color:var(--cream) !important}
  .icon-btn:hover{background:rgba(200,168,75,.14) !important;border-color:var(--accent) !important}
  .nav-toggle{border-color:rgba(27,94,32,.18) !important;color:var(--cream) !important}

  /* CTA — Claude Design : square corners 4px, uppercase, dark green pill */
  .cta{
    padding:12px 20px !important;border-radius:4px !important;
    background:#1B5E20 !important;color:#FAFAF7 !important;font-weight:600 !important;font-size:11px !important;
    letter-spacing:.15em !important;text-transform:uppercase !important;
    display:inline-flex;align-items:center;gap:10px;
    transition:background .2s, transform .2s;
  }
  .cta:hover{transform:translateY(-1px);background:#2E7D32 !important}
  .cta.ghost{background:transparent !important;color:#1B5E20 !important;border:1px solid rgba(27,94,32,.35) !important}
  .cta.ghost:hover{background:rgba(27,94,32,.05) !important}
  .cart-badge{background:var(--accent) !important;color:#1B5E20 !important;font-weight:600}

  /* HERO — green band on ivoire (the signature) */
  .hero{
    background:transparent !important;
    color:#FAFAF7 !important;
    isolation:isolate;
    overflow:visible !important;
    padding:110px 40px 50px !important;
  }
  .hero::before{
    content:"";position:absolute;inset:80px 5% 30px;border-radius:32px;
    background:var(--hero-band);
    box-shadow:0 30px 80px rgba(14,58,20,.25);
    z-index:-2;
  }
  .hero .theme-bg{display:none !important}
  .hero .grain{display:none !important}
  .hero .sun{
    position:absolute;top:5%;right:0;width:35vw;height:35vw;border-radius:50%;
    background:radial-gradient(circle, color-mix(in oklab, var(--accent) 30%, transparent), transparent 60%) !important;
    filter:blur(60px);z-index:-1;pointer-events:none;
  }
  .hero svg.leaf-deco{color:rgba(165,214,167,.4) !important;opacity:.35 !important;z-index:-1}

  .hero .eyebrow{color:#E8F5E9 !important;border-color:rgba(250,250,247,.30) !important;background:rgba(250,250,247,.08) !important;backdrop-filter:blur(8px)}
  .hero-title, .hero-title .it{color:#FAFAF7 !important}

  .hero .info-card, .hero .product-card{
    background:rgba(250,250,247,.10) !important;
    border:1px solid rgba(200,168,75,.40) !important;
    color:#FAFAF7 !important;
    backdrop-filter:blur(14px);
    box-shadow:0 14px 36px rgba(14,58,20,.30);
  }
  .hero .info-card .lab, .hero .product-card .latin,
  .hero .product-card .desc, .hero .info-card .sub{color:#E8F5E9 !important;opacity:.85}
  .hero .info-card .val, .hero .product-card .pname,
  .hero .product-card .price{color:#FAFAF7 !important}
  .hero .product-card .price small{color:#E8F5E9 !important;opacity:.7}
  .hero .info-card .bar i{background:var(--accent) !important}
  .hero .product-card .row{border-top-color:rgba(250,250,247,.18) !important}
  .hero .product-card .add{background:var(--accent) !important;color:#1B5E20 !important}
  .hero .product-card .add:hover{background:#FAFAF7 !important;color:var(--cream) !important}
  .hero .note{background:rgba(250,250,247,.10) !important;color:#E8F5E9 !important;border-color:rgba(250,250,247,.22) !important}
  .hero .stage .ring{border-color:rgba(250,250,247,.30) !important}
  .hero .stage .botanic{color:rgba(165,214,167,.6) !important}

  .hero .atouts .atout{
    background:rgba(250,250,247,.08) !important;
    border:1px solid rgba(200,168,75,.35) !important;
    color:#FAFAF7;backdrop-filter:blur(8px);
  }
  .hero .atouts .atout:hover{background:rgba(250,250,247,.14) !important;border-color:var(--accent) !important}
  .hero .atouts .atout svg{color:var(--accent) !important}
  .hero .atouts .atout .lab{color:#E8F5E9 !important}

  .hero .car-strip{border-top-color:rgba(250,250,247,.20) !important}
  .hero .car-counter{color:#FAFAF7 !important}
  .hero .car-counter span{color:#E8F5E9 !important}
  .hero .thumb{background:rgba(250,250,247,.08) !important;border-color:rgba(200,168,75,.35) !important}
  .hero .thumb.active{background:rgba(200,168,75,.25) !important;border-color:var(--accent) !important;box-shadow:0 14px 30px rgba(200,168,75,.30) !important}
  .hero .thumb .tn{color:#E8F5E9 !important}
  .hero .arr{border-color:rgba(250,250,247,.30) !important;color:#FAFAF7 !important}
  .hero .arr:hover{background:#FAFAF7 !important;color:var(--cream) !important;border-color:#FAFAF7 !important}

  /* Page-hero (inner pages) & article-hero — same band pattern */
  .page-hero, .article-hero{background:transparent !important;color:#FAFAF7 !important;isolation:isolate;overflow:visible !important;padding-top:170px !important;padding-bottom:90px !important}
  .page-hero::before, .article-hero::before{
    content:"";position:absolute;inset:90px 5% 40px;border-radius:32px;
    background:var(--hero-band);
    box-shadow:0 30px 80px rgba(14,58,20,.25);
    z-index:-2;
  }
  .page-hero .theme-bg, .page-hero .grain{display:none !important}
  .page-hero h1{color:#FAFAF7 !important}
  .page-hero h1 em{color:var(--accent) !important}
  .page-hero .lead{color:#E8F5E9 !important}
  .page-hero .crumbs, .page-hero .crumbs a{color:#E8F5E9 !important;opacity:.85}
  .page-hero .crumbs a:hover{color:var(--accent) !important;opacity:1}
  .article-hero h1{color:#FAFAF7 !important}
  .article-hero .lede{color:#E8F5E9 !important}
  .article-hero .meta-row{color:#E8F5E9 !important}
  .article-hero .meta-row .cat{color:var(--accent) !important}
  .article-hero .article-cover{background:rgba(250,250,247,.10) !important;border-color:rgba(200,168,75,.40) !important}
  .article-hero .article-cover svg{color:rgba(250,250,247,.5) !important}

  /* MARQUEE */
  .marquee{background:rgba(232,245,233,.5) !important;border-color:rgba(27,94,32,.10) !important;backdrop-filter:blur(8px)}
  .marquee-track{color:var(--cream-2)}
  .marquee-track i{color:var(--accent)}

  /* Section heads on luminous ivoire */
  .sec-tag{color:var(--cream-2)}
  .sec-title{color:var(--cream)}
  .sec-title em{color:var(--accent-2)}
  .sec-head{border-bottom-color:rgba(27,94,32,.12)}

  /* Cards on ivoire — pure white with green/gold detailing */
  .domain, .ben-card, .pack, .t-card, .blog-card, .pcard, .mini-card,
  .info-card, .product-card, .contact-block, .diff, .distinction,
  .checkout-form-wrap, .summary, .cart-table{
    background:#FFFFFF !important;
    color:var(--cream);
    border:1px solid rgba(27,94,32,.10) !important;
    box-shadow:0 12px 30px rgba(27,94,32,.06) !important;
    backdrop-filter:none !important;
  }
  .domain:hover, .ben-card:hover, .pack:hover, .blog-card:hover,
  .pcard:hover, .mini-card:hover, .distinction:hover{
    border-color:rgba(200,168,75,.60) !important;
    box-shadow:0 22px 50px rgba(27,94,32,.10), 0 0 0 1px rgba(200,168,75,.40) !important;
    transform:translateY(-4px);
  }

  .domain::before{background:radial-gradient(circle, rgba(200,168,75,.22), transparent 70%) !important}
  .domain .num, .pack .num, .ben-card .num{color:var(--cream-2)}
  .domain h3, .pack h3, .ben-card h3{color:var(--cream)}
  .domain p, .pack p, .ben-card p{color:#555}
  .domain ul li{color:var(--cream-2)}
  .domain ul li::before{color:var(--accent)}
  .domain ul{border-top-color:rgba(27,94,32,.10)}
  .domain .glyph, .ben-card .glyph{background:rgba(200,168,75,.14) !important;border-color:rgba(200,168,75,.35) !important;color:var(--accent-2)}
  .domain .more{color:var(--accent-2)}
  .domain .more:hover{color:var(--cream)}

  .chip{background:#FFFFFF !important;border-color:rgba(27,94,32,.16);color:var(--cream-2)}
  .chip:hover{border-color:var(--cream);color:var(--cream)}
  .chip.active{background:var(--cream) !important;color:#FAFAF7 !important;border-color:var(--cream) !important;box-shadow:0 6px 16px rgba(27,94,32,.25) !important}

  .pcard .latin{color:var(--cream-2)}
  .pcard .name{color:var(--cream)}
  .pcard .img{background:radial-gradient(ellipse at 50% 70%, rgba(200,168,75,.18), var(--bg-soft) 75%) !important}
  .pcard .foot{background:transparent !important;border-top-color:rgba(27,94,32,.10)}
  .pcard .price{color:var(--cream)}
  .pcard .price small{color:#777}
  .pcard .add{background:var(--cream) !important;color:#FAFAF7 !important}
  .pcard .add:hover{background:var(--accent) !important;color:#1B5E20 !important}
  .pcard .tag{background:var(--bg-soft);color:var(--cream-2);border-color:rgba(27,94,32,.12);backdrop-filter:none}
  .pcard .tag.hot{color:var(--accent-2);border-color:rgba(200,168,75,.50)}

  .mini-card .pimg{background:radial-gradient(ellipse at 50% 65%, rgba(200,168,75,.15), var(--bg-soft) 70%) !important;border-bottom-color:rgba(27,94,32,.06)}
  .mini-card .pimg.placeholder{background:linear-gradient(135deg, var(--bg-soft), #FFFFFF) !important}
  .mini-card .nm{color:var(--cream)}
  .mini-card .pr span:first-child{color:var(--cream)}
  .mini-card .pr{color:var(--accent-2)}
  .mini-card .pr.tba{color:var(--cream-2);opacity:.7}
  .mini-card .pr .add-mini{background:var(--cream) !important;color:#FAFAF7 !important;box-shadow:0 4px 10px rgba(27,94,32,.18)}
  .mini-card .pr .add-mini:hover{background:var(--accent) !important;color:#1B5E20 !important}

  .subcat h3{color:var(--cream)}
  .subcat h3 .cover{border-color:rgba(27,94,32,.16)}
  .cat-section{border-bottom-color:rgba(27,94,32,.10)}
  .cat-header .num{color:var(--accent-2)}
  .cat-header h2{color:var(--cream)}
  .cat-header h2 em{color:var(--accent-2)}
  .cat-header p{color:#555}

  /* Story split */
  .split{background:linear-gradient(135deg, #FFFFFF, var(--bg-soft)) !important;border:1px solid rgba(27,94,32,.10) !important}
  .split::before{background:radial-gradient(circle at 75% 50%, rgba(200,168,75,.22), transparent 60%) !important}
  .split-l .quote{color:var(--cream)}
  .split-l .quote em{color:var(--accent-2)}
  .split-l .meta .v{color:var(--cream)}
  .split-l .meta .l{color:var(--cream-2)}
  .split-r .ring{border-color:rgba(27,94,32,.18) !important}
  .split-r .pin{background:rgba(250,250,247,.92);color:var(--cream);border-color:rgba(27,94,32,.14)}

  .t-card .stars{color:var(--accent)}
  .t-card .quote{color:var(--cream)}
  .t-card .who{border-top-color:rgba(27,94,32,.10)}
  .t-card .av{background:linear-gradient(135deg, var(--cream), #0E3A14);color:#FAFAF7}
  .t-card .nm{color:var(--cream)}
  .t-card .role{color:var(--cream-2)}
  .rating-num{color:var(--cream)}
  .rating-num span{color:var(--accent)}
  .rating-label{color:var(--cream-2)}

  .faq{border-top-color:rgba(27,94,32,.12)}
  .faq details{border-bottom-color:rgba(27,94,32,.12)}
  .faq summary{color:var(--cream)}
  .faq summary:hover{color:var(--accent-2)}
  .faq summary .ic{border-color:rgba(27,94,32,.18);color:var(--cream)}
  .faq details[open] summary{color:var(--accent-2)}
  .faq details[open] summary .ic{background:var(--accent);border-color:var(--accent);color:#1B5E20}
  .faq .a{color:#3a3a3a}
  .faq .a strong{color:var(--cream)}

  .newsletter{
    background:radial-gradient(ellipse at 30% 50%, rgba(200,168,75,.22), transparent 60%), linear-gradient(135deg, var(--bg-soft), #FFFFFF) !important;
    border:1px solid rgba(27,94,32,.14) !important;
  }
  .newsletter h3{color:var(--cream)}
  .newsletter h3 em{color:var(--accent-2)}
  .newsletter p{color:#555}
  .newsletter input{background:#FFFFFF !important;border:1px solid rgba(27,94,32,.16) !important;color:var(--cream)}
  .newsletter input:focus{border-color:var(--cream)}
  .newsletter button{background:var(--cream) !important;color:#FAFAF7 !important}
  .newsletter button:hover{background:var(--accent) !important;color:#1B5E20 !important}

  footer{
    background:linear-gradient(180deg, var(--bg-soft-2) 0%, color-mix(in oklab, var(--bg-soft-2) 60%, var(--cream) 40%) 100%) !important;
    border-top:2px solid var(--accent) !important;
  }
  .foot-brand{color:var(--cream)}
  .foot-brand em{color:var(--accent-2)}
  .foot-tag{color:var(--cream-2)}
  .foot-grid h6{color:var(--cream-2)}
  .foot-grid a{color:var(--cream)}
  .foot-grid a:hover{color:var(--accent-2)}
  .foot-bottom{border-top-color:rgba(27,94,32,.18);color:var(--cream-2)}

  .nav-drawer{background:rgba(250,250,247,.97) !important;backdrop-filter:blur(24px)}
  .nav-drawer a{color:var(--cream);border-bottom-color:rgba(27,94,32,.12)}
  .nav-drawer a:hover{color:var(--accent-2)}
  .nav-drawer a small{color:var(--cream-2)}
  .nav-drawer-foot{color:var(--cream-2)}

  .contact-block .lab{color:var(--cream-2)}
  .contact-block .lab svg{color:var(--accent)}
  .contact-block .val{color:var(--cream)}
  .contact-block .val a{color:var(--cream)}
  .contact-block .val a:hover{color:var(--accent-2)}
  .contact-block .sub{color:#555}
  .socials a{border-color:rgba(27,94,32,.18);color:var(--cream-2)}
  .socials a:hover{background:var(--accent);color:#1B5E20;border-color:var(--accent)}
  .contact-form h2{color:var(--cream)}
  .contact-form .intro{color:#555}
  .form-field label{color:#666}
  .form-field input, .form-field textarea, .form-field select{
    background:#FFFFFF !important;border:1px solid rgba(27,94,32,.16) !important;color:var(--cream);
  }
  .form-field input:focus, .form-field textarea:focus{border-color:var(--cream);background:#FFFFFF !important}
  .form-field input::placeholder, .form-field textarea::placeholder{color:#999}
  .form-submit{background:var(--cream) !important;color:#FAFAF7 !important}
  .form-submit:hover{background:var(--accent) !important;color:#1B5E20 !important}
  .form-success{background:rgba(200,168,75,.18);border-color:rgba(200,168,75,.50);color:var(--cream)}
  .map-wrap{border-color:rgba(27,94,32,.10);background:var(--bg-soft)}
  .map-wrap iframe{filter:none}

  .pack .badge{background:var(--bg-soft);color:var(--cream-2);border-color:rgba(27,94,32,.12);backdrop-filter:none}
  .pack .badge.coffret{color:var(--accent-2);border-color:rgba(200,168,75,.50)}
  .pack .pack-foot{border-top-color:rgba(27,94,32,.10)}
  .pack .price{color:var(--cream)}
  .pack .price small{color:#777}
  .pack .add{background:var(--cream) !important;color:#FAFAF7 !important}
  .pack .add:hover{background:var(--accent) !important;color:#1B5E20 !important}

  .distinction .badge{background:rgba(250,250,247,.95);color:var(--cream);border-color:rgba(27,94,32,.12)}
  .distinction .body .year{color:var(--accent-2)}
  .distinction .body h4{color:var(--cream)}
  .distinction .body p{color:#555}
  .distinctions-intro{color:#555}
  .distinctions-intro strong{color:var(--cream)}

  .diff .num{color:var(--accent-2)}
  .diff h3{color:var(--cream)}
  .diff p{color:#555}
  .value{background:#FFFFFF !important;border-color:rgba(27,94,32,.10)}
  .value .ic{background:rgba(200,168,75,.14);color:var(--accent-2)}
  .value .nm{color:var(--cream)}

  .blog-card .cover{background:linear-gradient(135deg, color-mix(in oklab, var(--accent) 30%, var(--bg-soft)), var(--bg-soft)) !important}
  .blog-card .cover svg{color:rgba(27,94,32,.30)}
  .blog-card .meta{color:var(--cream-2)}
  .blog-card .meta .cat{color:var(--accent-2)}
  .blog-card h3{color:var(--cream)}
  .blog-card .excerpt{color:#555}
  .blog-card .read{border-top-color:rgba(27,94,32,.10);color:var(--accent-2)}
  .blog-card:hover .read{color:var(--cream)}

  .article-body{color:#1a1a1a}
  .article-body p{color:#3a3a3a}
  .article-body h2, .article-body h3{color:var(--cream)}
  .article-body strong{color:var(--cream)}
  .article-body em{color:var(--accent-2)}
  .article-body blockquote{background:var(--bg-soft);border-left-color:var(--cream);color:var(--cream)}
  .article-body a{color:var(--cream)}
  .article-body a:hover{color:var(--accent-2)}
  .article-foot .back{color:var(--cream-2)}
  .article-foot .back:hover{color:var(--accent-2)}
  .article-foot .share a{border-color:rgba(27,94,32,.18);color:var(--cream-2)}
  .article-foot .share a:hover{background:var(--accent);color:#1B5E20;border-color:var(--accent)}
  .related-articles{border-top-color:rgba(27,94,32,.12)}
  .related-articles h3{color:var(--cream)}

  .cart-drawer{background:#FFFFFF !important;border-left-color:rgba(27,94,32,.12)}
  .cart-head{border-bottom-color:rgba(27,94,32,.10)}
  .cart-head h3{color:var(--cream)}
  .cart-head h3 small{color:var(--cream-2)}
  .cart-close{border-color:rgba(27,94,32,.18);color:var(--cream)}
  .cart-close:hover{background:var(--accent);border-color:var(--accent);color:#1B5E20}
  .cart-item{border-bottom-color:rgba(27,94,32,.08)}
  .cart-item .ci-img{background:var(--bg-soft);border-color:rgba(27,94,32,.10)}
  .cart-item .ci-info .nm{color:var(--cream)}
  .cart-item .ci-info .pr{color:var(--accent-2)}
  .cart-item .ci-qty button{border-color:rgba(27,94,32,.18);color:var(--cream)}
  .cart-item .ci-qty button:hover{background:var(--accent);border-color:var(--accent);color:#1B5E20}
  .cart-item .ci-qty .qv{color:var(--cream)}
  .cart-item .ci-rm{color:var(--cream-2)}
  .cart-item .ci-rm:hover{color:var(--accent-2)}
  .cart-empty{color:var(--cream-2)}
  .cart-foot{background:var(--bg-soft) !important;border-top-color:rgba(27,94,32,.10)}
  .cart-foot .row{color:#555}
  .cart-foot .row.total{color:var(--cream);border-top-color:rgba(27,94,32,.16)}
  .cart-foot .row.total span:last-child{color:var(--accent-2)}
  .cart-foot .checkout-btn{background:var(--cream) !important;color:#FAFAF7 !important}
  .cart-foot .checkout-btn:hover:not(:disabled){background:var(--accent) !important;color:#1B5E20 !important}
  .cart-foot .view-cart{color:var(--cream-2)}
  .cart-foot .view-cart:hover{color:var(--accent-2)}

  .cart-table .row-h{color:var(--cream-2);border-bottom-color:rgba(27,94,32,.10)}
  .cart-table .row{border-bottom-color:rgba(27,94,32,.07)}
  .cart-table .row .img{background:var(--bg-soft);border-color:rgba(27,94,32,.10)}
  .cart-table .row .nm{color:var(--cream)}
  .cart-table .row .nm .sub{color:var(--cream-2)}
  .cart-table .row .qty{border-color:rgba(27,94,32,.18)}
  .cart-table .row .qty button{color:var(--cream)}
  .cart-table .row .qty button:hover{background:var(--accent);color:#1B5E20}
  .cart-table .row .qty .qv{color:var(--cream)}
  .cart-table .row .total-pr{color:var(--accent-2)}
  .cart-table .row .rm{color:var(--cream-2)}
  .cart-table .row .rm:hover{color:var(--accent-2)}

  .summary h3{color:var(--cream)}
  .summary .line{color:#555;border-bottom-color:rgba(27,94,32,.08)}
  .summary .line.total{color:var(--cream);border-top-color:rgba(27,94,32,.16)}
  .summary .line.total span:last-child{color:var(--accent-2)}
  .summary .promo input{background:#FFFFFF !important;border:1px solid rgba(27,94,32,.18) !important;color:var(--cream)}
  .summary .promo button{border:1px solid rgba(27,94,32,.18);color:var(--cream-2);background:transparent}
  .summary .promo button:hover{background:var(--accent);border-color:var(--accent);color:#1B5E20}
  .summary .pay-btn{background:var(--cream) !important;color:#FAFAF7 !important}
  .summary .pay-btn:hover{background:var(--accent) !important;color:#1B5E20 !important}
  .summary .secure{color:var(--cream-2)}
  .cart-empty-page{color:var(--cream-2)}
  .cart-empty-page h2{color:var(--cream)}

  .checkout-form-wrap h3{color:var(--cream);border-top-color:rgba(27,94,32,.10)}
  .checkout-form-wrap h3 .stp{background:var(--accent);color:#1B5E20}
  .pay-method{background:#FFFFFF !important;border:1px solid rgba(27,94,32,.16) !important}
  .pay-method:hover{border-color:rgba(200,168,75,.50) !important}
  .pay-method.selected{background:rgba(200,168,75,.18) !important;border-color:var(--accent) !important}
  .pay-method svg{color:var(--cream)}
  .pay-method.selected svg{color:var(--accent-2)}
  .pay-method .nm{color:var(--cream)}
  .pay-method .sub{color:#777}
  .order-success{background:radial-gradient(ellipse at 50% 30%, rgba(200,168,75,.25), transparent 60%), linear-gradient(180deg, var(--bg-soft), #FFFFFF) !important;border:1px solid rgba(200,168,75,.50) !important}
  .order-success .ic{background:var(--accent);color:#1B5E20}
  .order-success h2{color:var(--cream)}
  .order-success p{color:#555}
  .order-success .ref{background:rgba(200,168,75,.14);color:var(--accent-2)}

  ::-webkit-scrollbar-track{background:var(--bg-soft) !important}
  ::-webkit-scrollbar-thumb{background:color-mix(in oklab, var(--accent) 50%, rgba(27,94,32,.20)) !important;border:2px solid var(--bg-soft) !important}
  ::-webkit-scrollbar-thumb:hover{background:var(--accent) !important}
  html{scrollbar-color:color-mix(in oklab, var(--accent) 50%, rgba(27,94,32,.20)) var(--bg-soft) !important}
  *:focus-visible{outline-color:var(--accent) !important}
  ::selection{background:var(--accent);color:#1B5E20}

  /* Mobile breakpoints for the green band */
  @media (max-width:768px){
    .hero::before{inset:60px 16px 20px;border-radius:24px}
    .page-hero::before, .article-hero::before{inset:70px 16px 30px;border-radius:24px}
  }
  @media (max-width:480px){
    .hero::before{inset:50px 10px 16px;border-radius:20px}
    .page-hero::before, .article-hero::before{inset:60px 10px 24px;border-radius:20px}
  }
"""

with open(os.path.join(V2, 'assets', 'css', 'oyayi.css'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(base_css + ivory_lumiere_block)

# --- 5. Patch all V2 HTML pages: data-da="brown", remove banners ---
v2_html_files = [f for f in os.listdir(V2) if f.endswith('.html')]
for fname in v2_html_files:
    p = os.path.join(V2, fname)
    with open(p, 'r', encoding='utf-8') as f: c = f.read()
    c = re.sub(r'<!-- ============== V[12][^>]*?============== -->.*?</div>\s*\n', '', c, flags=re.DOTALL)
    c = re.sub(r'<div id="v[12]-banner"[^>]*>.*?</div>\s*', '', c, flags=re.DOTALL)
    c = c.replace('<body data-da="green"', '<body data-da="brown"')
    with open(p, 'w', encoding='utf-8', newline='\n') as f: f.write(c)

# --- 6. Strip v2-banner from V1 root index.html ---
v1_idx = os.path.join(ROOT, 'index.html')
with open(v1_idx, 'r', encoding='utf-8') as f: c = f.read()
c = re.sub(r'<!-- ============== V2 COMPARISON BANNER ============== -->.*?</div>\s*\n', '', c, flags=re.DOTALL)
c = re.sub(r'<div id="v2-banner"[^>]*>.*?</div>\s*', '', c, flags=re.DOTALL)
with open(v1_idx, 'w', encoding='utf-8', newline='\n') as f: f.write(c)

print('V2 rebuilt with "ivoire lumière":')
print(f'  V2 HTML pages : {len(v2_html_files)}')
print(f'  Body bg pattern: body::before fixed 4-stop gradient + body::after noise overlay')
print(f'  Hero band     : inset 80px 5% 30px, radius 32px, dark green shadow')
print(f'  Brand CTA     : square 4px radius, uppercase 11px tracking .15em')
print(f'  CSS override  : +{len(ivory_lumiere_block)} chars')
