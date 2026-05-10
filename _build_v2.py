# -*- coding: utf-8 -*-
"""Build V2 as an exact clone of V1, but locked to the ivory theme.
V2 inherits every page, asset, product, testimonial, FAQ, article from V1.
Only the chromatic theme differs: ivory dominant, deep green as ink, gold accent."""

import os, shutil, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(ROOT, 'v2')

# -------- 1. Wipe and recreate v2/ -----------------------------------
if os.path.exists(V2):
    shutil.rmtree(V2)
os.makedirs(V2)
os.makedirs(os.path.join(V2, 'assets', 'css'))
os.makedirs(os.path.join(V2, 'assets', 'js'))

# -------- 2. Copy all HTML pages -------------------------------------
html_count = 0
for f in sorted(os.listdir(ROOT)):
    if f.endswith('.html'):
        shutil.copy(os.path.join(ROOT, f), os.path.join(V2, f))
        html_count += 1

# -------- 3. Copy all asset folders ----------------------------------
for folder in ['products', 'catalog', 'distinctions']:
    src = os.path.join(ROOT, 'assets', folder)
    if os.path.exists(src):
        shutil.copytree(src, os.path.join(V2, 'assets', folder))

# Copy JS files
for f in os.listdir(os.path.join(ROOT, 'assets', 'js')):
    shutil.copy(os.path.join(ROOT, 'assets', 'js', f),
                os.path.join(V2, 'assets', 'js', f))

# -------- 4. Generate v2 CSS: clone V1 + ivory theme override --------
with open(os.path.join(ROOT, 'assets', 'css', 'oyayi.css'), 'r', encoding='utf-8') as f:
    css = f.read()

ivory_override = """

  /* ============================================================
     V2 — IVORY THEME LOCK
     This block overrides the V1 green tokens unconditionally so V2
     stays in the ivory-dominant palette regardless of any toggle.
     Inspired by the OYAYI Sens flyer right-column treatment :
     ivoire as page bg, deep green as ink, gold as signature accent.
     ============================================================ */
  :root,
  :root[data-da="green"],
  :root[data-da="brown"]{
    --bg-deep:#FAFAF7 !important;       /* ivoire — page background */
    --bg-mid:#FFFFFF !important;        /* pure white — cards */
    --bg-soft:#FFF8E1 !important;       /* or clair — warm surfaces */
    --bg-soft-2:#F4F1E8 !important;     /* parchment — footer, marquee */
    --cream:#1B5E20 !important;         /* brand green — text ("ink") */
    --cream-2:#3E5A3F !important;       /* sourd green — secondary text */
    --leaf-light:#2E7D32 !important;
    --accent:#C8A84B !important;        /* gold — accent stays unchanged */
    --accent-2:#A78A2E !important;      /* deeper gold */
    --ink:#FAFAF7 !important;           /* on dark buttons -> ivoire */
    --line:rgba(26,90,32,.18) !important;
    --hairline:rgba(26,90,32,.10) !important;
  }

  /* Body background = ivoire instead of green */
  html, body{background:var(--bg-deep) !important;color:var(--cream) !important}

  /* Hide the theme toggle button (only one theme in V2) */
  .theme-fab{display:none !important}

  /* Loader on ivoire bg */
  .loader-overlay{
    background:radial-gradient(ellipse at 50% 60%, color-mix(in oklab, var(--accent) 22%, var(--bg-soft)), var(--bg-deep) 70%) !important;
  }
  .loader-brand{color:var(--cream)}
  .loader-brand small{color:var(--cream-2)}
  .loader-mark::after{border-color:color-mix(in oklab,var(--cream) 35%,transparent) !important}
  .loader-bar{background:color-mix(in oklab,var(--cream) 14%,transparent) !important}

  /* Nav: white surface with gold hairline + green ink */
  .nav{
    background:linear-gradient(to bottom, rgba(250,250,247,.96) 0%, rgba(250,250,247,.78) 80%, rgba(250,250,247,0) 100%) !important;
    backdrop-filter:saturate(180%) blur(14px);
    border-bottom:1px solid rgba(26,90,32,.08);
  }
  .nav-links a{color:var(--cream)}
  .nav-links a:hover{color:var(--accent-2)}
  .nav-links a.active::after{background:var(--accent);box-shadow:0 0 12px color-mix(in oklab,var(--accent) 60%,transparent)}
  .icon-btn{border-color:rgba(26,90,32,.18);color:var(--cream)}
  .icon-btn:hover{background:color-mix(in oklab,var(--accent) 14%,transparent);border-color:var(--accent)}

  /* CTA on ivoire — dark green pill with ivoire text */
  .cta{background:var(--cream);color:#FAFAF7}
  .cta:hover{background:var(--accent);color:#1A1A1A}
  .cta.ghost{background:transparent;color:var(--cream);border:1px solid rgba(26,90,32,.22)}
  .cta.ghost:hover{background:var(--bg-soft);color:var(--cream);border-color:var(--cream)}
  .cart-badge{background:var(--accent);color:#1A1A1A}

  /* Brand mark dot in nav */
  .brand .mark{background:radial-gradient(circle at 30% 30%, var(--accent-soft, #FFF8E1), var(--accent) 55%, var(--accent-2));box-shadow:0 4px 14px color-mix(in oklab, var(--accent) 40%, transparent)}

  /* Hero — ivory gradient with subtle gold + green vignette */
  .hero .theme-bg{
    background:
      radial-gradient(ellipse 70% 60% at 50% 70%, color-mix(in oklab, var(--accent) 18%, transparent), transparent 70%),
      radial-gradient(circle at 12% 18%, color-mix(in oklab, var(--cream) 12%, transparent), transparent 50%),
      radial-gradient(circle at 88% 10%, color-mix(in oklab, var(--accent) 14%, transparent), transparent 55%),
      linear-gradient(180deg, var(--bg-deep) 0%, var(--bg-soft) 50%, var(--bg-deep) 100%) !important;
  }
  .hero .grain{opacity:.15 !important}
  .hero .sun{background:radial-gradient(circle, color-mix(in oklab, var(--accent) 35%, transparent), transparent 60%)}
  .leaf-deco{color:var(--cream) !important;opacity:.10 !important}
  .hero::after{
    background:radial-gradient(ellipse 90% 60% at 50% 30%, color-mix(in oklab, var(--bg-soft) 70%, transparent), transparent 70%) !important;
  }

  .eyebrow{border-color:rgba(26,90,32,.20);background:rgba(255,255,255,.7);color:var(--cream-2)}
  .hero-title{color:var(--cream)}
  .hero-title .it{color:var(--cream)}

  /* Stage rings on ivoire */
  .stage .ring{border-color:rgba(26,90,32,.20) !important}
  .stage .pedestal{background:radial-gradient(ellipse, color-mix(in oklab, var(--accent) 35%, transparent), transparent 70%)}
  .stage .botanic{color:var(--cream) !important;opacity:.25}

  /* Info cards & product card on ivoire */
  .info-card, .product-card{
    background:#FFFFFF !important;
    border:1px solid rgba(26,90,32,.10);
    box-shadow:0 14px 36px rgba(26,90,32,.06), 0 2px 6px rgba(26,90,32,.04);
    backdrop-filter:none;
  }
  .info-card .lab, .product-card .latin{color:var(--cream-2)}
  .info-card .val, .product-card .pname{color:var(--cream)}
  .info-card .sub, .product-card .desc{color:#555}
  .info-card .bar i{background:var(--accent)}
  .info-card .bar i.off{background:rgba(26,90,32,.18)}
  .product-card .price{color:var(--cream)}
  .product-card .price small{color:#777}
  .product-card .row{border-top-color:rgba(26,90,32,.10)}
  .product-card .add{background:var(--cream);color:#FAFAF7}
  .product-card .add:hover{background:var(--accent);color:#1A1A1A}
  .note{background:var(--bg-soft);color:var(--cream);border-color:rgba(26,90,32,.10)}

  /* Carousel strip */
  .car-strip{border-top-color:rgba(26,90,32,.14)}
  .car-counter{color:var(--cream)}
  .car-counter span{color:var(--cream-2)}
  .thumb{background:#FFFFFF;border-color:rgba(26,90,32,.10)}
  .thumb.active{background:color-mix(in oklab,var(--accent) 18%,#FFFFFF);border-color:var(--accent);box-shadow:0 14px 30px color-mix(in oklab,var(--accent) 25%,transparent)}
  .thumb .tn{color:var(--cream-2)}
  .arr{border-color:rgba(26,90,32,.18);color:var(--cream)}
  .arr:hover{background:var(--cream);color:#FAFAF7;border-color:var(--cream)}

  /* Atouts row */
  .atout{background:#FFFFFF;border-color:rgba(26,90,32,.10)}
  .atout:hover{border-color:var(--accent);background:var(--bg-soft)}
  .atout svg{color:var(--cream)}
  .atout .lab{color:var(--cream-2)}

  /* Marquee strip */
  .marquee{background:var(--bg-soft-2) !important;border-color:rgba(26,90,32,.10) !important}
  .marquee-track{color:var(--cream-2)}
  .marquee-track i{color:var(--accent)}

  /* Sections — headings + tags */
  .sec-tag{color:var(--cream-2)}
  .sec-title{color:var(--cream)}
  .sec-title em{color:var(--accent-2)}
  .sec-head{border-bottom-color:rgba(26,90,32,.12)}

  /* Domains */
  .domain{
    background:#FFFFFF !important;
    border-color:rgba(26,90,32,.10);
    box-shadow:0 12px 30px rgba(26,90,32,.06);
  }
  .domain::before{background:radial-gradient(circle, color-mix(in oklab, var(--accent) 20%, transparent), transparent 70%) !important}
  .domain .num{color:var(--cream-2)}
  .domain h3{color:var(--cream)}
  .domain p{color:#555}
  .domain ul li{color:var(--cream-2)}
  .domain ul li::before{color:var(--accent)}
  .domain ul{border-top-color:rgba(26,90,32,.10)}
  .domain .glyph{background:color-mix(in oklab,var(--accent) 14%, transparent);border-color:color-mix(in oklab,var(--accent) 40%, transparent);color:var(--accent-2)}
  .domain .more{color:var(--accent-2)}
  .domain .more:hover{color:var(--cream)}
  .domain:hover{transform:translateY(-4px);border-color:color-mix(in oklab,var(--accent) 60%,transparent);box-shadow:0 22px 50px rgba(26,90,32,.12)}

  /* Chips */
  .chip{border-color:rgba(26,90,32,.16);color:var(--cream-2);background:#FFFFFF}
  .chip:hover{border-color:var(--cream);color:var(--cream);background:#FFFFFF}
  .chip.active{background:var(--cream);color:#FAFAF7;border-color:var(--cream);box-shadow:0 6px 16px color-mix(in oklab,var(--cream) 30%,transparent)}

  /* Product cards (pcard) on ivoire */
  .pcard{
    background:#FFFFFF !important;
    border-color:rgba(26,90,32,.10);
    box-shadow:0 14px 36px rgba(26,90,32,.06);
  }
  .pcard:hover{border-color:color-mix(in oklab,var(--accent) 60%,transparent);box-shadow:0 22px 50px rgba(26,90,32,.12), 0 0 0 1px color-mix(in oklab,var(--accent) 35%,transparent)}
  .pcard .latin{color:var(--cream-2)}
  .pcard .name{color:var(--cream)}
  .pcard .img{background:radial-gradient(ellipse at 50% 70%, color-mix(in oklab,var(--accent) 18%, var(--bg-soft)), #FFFFFF 75%) !important}
  .pcard .foot{background:transparent !important;border-top-color:rgba(26,90,32,.10)}
  .pcard .price{color:var(--cream)}
  .pcard .price small{color:#777}
  .pcard .add{background:var(--cream);color:#FAFAF7}
  .pcard .add:hover{background:var(--accent);color:#1A1A1A}
  .pcard .tag{background:var(--bg-soft);color:var(--cream-2);border-color:rgba(26,90,32,.12)}
  .pcard .tag.hot{color:var(--accent-2);border-color:color-mix(in oklab,var(--accent) 50%,transparent)}

  /* Mini-cards (catalogue) */
  .mini-card{
    background:#FFFFFF !important;
    border-color:rgba(26,90,32,.10);
    box-shadow:0 8px 22px rgba(26,90,32,.06);
  }
  .mini-card:hover{border-color:color-mix(in oklab,var(--accent) 60%,transparent);box-shadow:0 18px 40px rgba(26,90,32,.10)}
  .mini-card .pimg{background:radial-gradient(ellipse at 50% 65%, color-mix(in oklab,var(--accent) 15%, var(--bg-soft)), #FFFFFF 70%) !important;border-bottom-color:rgba(26,90,32,.06)}
  .mini-card .pimg.placeholder{background:linear-gradient(135deg, var(--bg-soft), #FFFFFF) !important}
  .mini-card .pimg.placeholder svg{color:color-mix(in oklab,var(--cream) 35%,transparent)}
  .mini-card .nm{color:var(--cream)}
  .mini-card .pr{color:var(--accent-2)}
  .mini-card .pr span:first-child{color:var(--cream)}
  .mini-card .pr.tba{color:var(--cream-2);opacity:.7}
  .mini-card .pr .add-mini{background:var(--cream);color:#FAFAF7;box-shadow:0 4px 10px rgba(26,90,32,.18)}
  .mini-card .pr .add-mini:hover{background:var(--accent);color:#1A1A1A}

  /* Subcat */
  .subcat h3{color:var(--cream)}
  .subcat h3::before{background:var(--accent)}
  .subcat h3 .cover{border-color:rgba(26,90,32,.16)}

  /* Cat-section dividers */
  .cat-section{border-bottom-color:rgba(26,90,32,.10)}
  .cat-header .num{color:var(--accent-2)}
  .cat-header h2{color:var(--cream)}
  .cat-header h2 em{color:var(--accent-2)}
  .cat-header p{color:#555}

  /* Story split */
  .split{
    background:linear-gradient(135deg, #FFFFFF, var(--bg-soft)) !important;
    border-color:rgba(26,90,32,.10);
  }
  .split::before{background:radial-gradient(circle at 75% 50%, color-mix(in oklab, var(--accent) 22%, transparent), transparent 60%) !important}
  .split-l .quote{color:var(--cream)}
  .split-l .quote em{color:var(--accent-2)}
  .split-l .meta .v{color:var(--cream)}
  .split-l .meta .l{color:var(--cream-2)}
  .split-r .ring{border-color:rgba(26,90,32,.18) !important}
  .split-r .pin{background:rgba(250,250,247,.9);color:var(--cream);border-color:rgba(26,90,32,.14);backdrop-filter:blur(8px)}

  /* Benefits cards */
  .ben-card{
    background:#FFFFFF !important;
    border-color:rgba(26,90,32,.10);
    box-shadow:0 10px 26px rgba(26,90,32,.06);
  }
  .ben-card:hover{background:var(--bg-soft) !important;border-color:color-mix(in oklab,var(--accent) 50%,transparent)}
  .ben-card .num{color:var(--cream-2)}
  .ben-card h3{color:var(--cream)}
  .ben-card p{color:#555}
  .ben-card .glyph{background:color-mix(in oklab,var(--accent) 14%,transparent);border-color:color-mix(in oklab,var(--accent) 40%,transparent);color:var(--accent-2)}

  /* Testimonials */
  .t-card{
    background:#FFFFFF !important;
    border-color:rgba(26,90,32,.10);
    box-shadow:0 10px 28px rgba(26,90,32,.06);
  }
  .t-card .stars{color:var(--accent)}
  .t-card .quote{color:var(--cream)}
  .t-card .who{border-top-color:rgba(26,90,32,.10)}
  .t-card .av{background:linear-gradient(135deg, var(--cream), color-mix(in oklab, var(--cream) 70%, #000));color:#FAFAF7}
  .t-card .nm{color:var(--cream)}
  .t-card .role{color:var(--cream-2)}
  .rating-num{color:var(--cream)}
  .rating-num span{color:var(--accent)}
  .rating-label{color:var(--cream-2)}

  /* FAQ */
  .faq{border-top-color:rgba(26,90,32,.12)}
  .faq details{border-bottom-color:rgba(26,90,32,.12)}
  .faq summary{color:var(--cream)}
  .faq summary:hover{color:var(--accent-2)}
  .faq summary .ic{border-color:rgba(26,90,32,.16);color:var(--cream)}
  .faq details[open] summary{color:var(--accent-2)}
  .faq details[open] summary .ic{background:var(--accent);border-color:var(--accent);color:#1A1A1A}
  .faq .a{color:#3a3a3a}
  .faq .a strong{color:var(--cream)}

  /* Newsletter */
  .newsletter{
    background:radial-gradient(ellipse at 30% 50%, color-mix(in oklab,var(--accent) 18%, transparent), transparent 60%), linear-gradient(135deg, var(--bg-soft), #FFFFFF) !important;
    border-color:rgba(26,90,32,.14);
  }
  .newsletter h3{color:var(--cream)}
  .newsletter h3 em{color:var(--accent-2)}
  .newsletter p{color:#555}
  .newsletter input{background:#FFFFFF !important;border-color:rgba(26,90,32,.16);color:var(--cream)}
  .newsletter input:focus{border-color:var(--cream)}
  .newsletter button{background:var(--cream);color:#FAFAF7}
  .newsletter button:hover{background:var(--accent);color:#1A1A1A}

  /* Footer */
  footer{
    background:linear-gradient(180deg, var(--bg-soft-2) 0%, color-mix(in oklab, var(--bg-soft-2) 70%, #1B5E20 30%) 100%) !important;
    border-top:2px solid var(--accent) !important;
  }
  .foot-brand{color:var(--cream)}
  .foot-brand em{color:var(--accent-2)}
  .foot-tag{color:var(--cream-2)}
  .foot-grid h6{color:var(--cream-2)}
  .foot-grid a{color:var(--cream)}
  .foot-grid a:hover{color:var(--accent-2)}
  .foot-bottom{border-top-color:rgba(26,90,32,.18);color:var(--cream-2)}

  /* Mobile drawer */
  .nav-drawer{background:rgba(250,250,247,.97) !important;backdrop-filter:blur(24px)}
  .nav-drawer a{color:var(--cream);border-bottom-color:rgba(26,90,32,.12)}
  .nav-drawer a:hover{color:var(--accent-2)}
  .nav-drawer a small{color:var(--cream-2)}
  .nav-drawer-foot{color:var(--cream-2)}
  .nav-toggle{border-color:rgba(26,90,32,.18);color:var(--cream)}

  /* Page hero inner pages */
  .page-hero .theme-bg{
    background:radial-gradient(ellipse 80% 70% at 50% 30%, color-mix(in oklab, var(--accent) 18%, var(--bg-soft)), var(--bg-deep) 75%),
               linear-gradient(180deg, var(--bg-deep) 0%, var(--bg-soft) 50%, var(--bg-deep) 100%) !important;
  }
  .page-hero h1{color:var(--cream)}
  .page-hero h1 em{color:var(--accent-2)}
  .page-hero .lead{color:#555}
  .page-hero .crumbs{color:var(--cream-2)}
  .page-hero .crumbs a:hover{color:var(--accent-2)}

  /* Contact form & info blocks */
  .contact-block{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 10px 26px rgba(26,90,32,.06)}
  .contact-block .lab{color:var(--cream-2)}
  .contact-block .lab svg{color:var(--accent)}
  .contact-block .val{color:var(--cream)}
  .contact-block .val a{color:var(--cream)}
  .contact-block .val a:hover{color:var(--accent-2)}
  .contact-block .sub{color:#555}
  .socials a{border-color:rgba(26,90,32,.18);color:var(--cream-2)}
  .socials a:hover{background:var(--accent);color:#1A1A1A}
  .contact-form{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 14px 40px rgba(26,90,32,.08)}
  .contact-form h2{color:var(--cream)}
  .contact-form .intro{color:#555}
  .form-field label{color:#666}
  .form-field input, .form-field textarea, .form-field select{
    background:#FFFFFF !important;border-color:rgba(26,90,32,.16);color:var(--cream);
  }
  .form-field input:focus, .form-field textarea:focus{border-color:var(--cream);background:#FFFFFF !important}
  .form-field input::placeholder, .form-field textarea::placeholder{color:#999}
  .form-submit{background:var(--cream);color:#FAFAF7}
  .form-submit:hover{background:var(--accent);color:#1A1A1A}
  .form-success{background:color-mix(in oklab,var(--accent) 18%,#FFFFFF);border-color:color-mix(in oklab,var(--accent) 50%,transparent);color:var(--cream)}
  .map-wrap{border-color:rgba(26,90,32,.10);background:var(--bg-soft)}
  .map-wrap iframe{filter:none}

  /* Packs */
  .pack{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 12px 32px rgba(26,90,32,.06)}
  .pack:hover{border-color:color-mix(in oklab,var(--accent) 60%,transparent);box-shadow:0 22px 50px rgba(26,90,32,.12)}
  .pack .num{color:var(--cream-2)}
  .pack h3{color:var(--cream)}
  .pack p{color:#555}
  .pack .badge{background:var(--bg-soft);color:var(--cream-2);border-color:rgba(26,90,32,.12)}
  .pack .badge.coffret{color:var(--accent-2);border-color:color-mix(in oklab,var(--accent) 50%,transparent)}
  .pack .pack-foot{border-top-color:rgba(26,90,32,.10)}
  .pack .price{color:var(--cream)}
  .pack .price small{color:#777}
  .pack .add{background:var(--cream);color:#FAFAF7}
  .pack .add:hover{background:var(--accent);color:#1A1A1A}

  /* Distinctions */
  .distinction{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 10px 26px rgba(26,90,32,.06)}
  .distinction:hover{border-color:color-mix(in oklab,var(--accent) 50%,transparent);box-shadow:0 18px 40px rgba(26,90,32,.12)}
  .distinction .badge{background:rgba(250,250,247,.95);color:var(--cream);border-color:rgba(26,90,32,.12)}
  .distinction .body .year{color:var(--accent-2)}
  .distinction .body h4{color:var(--cream)}
  .distinction .body p{color:#555}
  .distinctions-intro{color:#555}
  .distinctions-intro strong{color:var(--cream)}

  /* Diffs (values) */
  .diff{background:#FFFFFF !important;border-color:rgba(26,90,32,.10)}
  .diff .num{color:var(--accent-2)}
  .diff h3{color:var(--cream)}
  .diff p{color:#555}
  .value{background:#FFFFFF;border-color:rgba(26,90,32,.10)}
  .value .ic{background:color-mix(in oklab,var(--accent) 14%,transparent);color:var(--accent-2)}
  .value .nm{color:var(--cream)}

  /* Blog cards */
  .blog-card{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 12px 32px rgba(26,90,32,.06)}
  .blog-card:hover{border-color:color-mix(in oklab,var(--accent) 60%,transparent);box-shadow:0 22px 50px rgba(26,90,32,.12)}
  .blog-card .cover{background:linear-gradient(135deg, color-mix(in oklab,var(--accent) 30%,var(--bg-soft)), var(--bg-soft)) !important}
  .blog-card .cover svg{color:color-mix(in oklab,var(--cream) 30%,transparent)}
  .blog-card .meta{color:var(--cream-2)}
  .blog-card .meta .cat{color:var(--accent-2)}
  .blog-card h3{color:var(--cream)}
  .blog-card .excerpt{color:#555}
  .blog-card .read{border-top-color:rgba(26,90,32,.10);color:var(--accent-2)}
  .blog-card:hover .read{color:var(--cream)}

  /* Article body */
  .article-body{color:#1a1a1a}
  .article-body p{color:#3a3a3a}
  .article-body h2, .article-body h3{color:var(--cream)}
  .article-body strong{color:var(--cream)}
  .article-body em{color:var(--accent-2)}
  .article-body blockquote{background:var(--bg-soft);border-left-color:var(--cream);color:var(--cream)}
  .article-body a{color:var(--cream)}
  .article-body a:hover{color:var(--accent-2)}
  .article-hero h1{color:var(--cream)}
  .article-hero .lede{color:#555}
  .article-hero .meta-row{color:var(--cream-2)}
  .article-hero .meta-row .cat{color:var(--accent-2)}
  .article-cover{background:linear-gradient(135deg, color-mix(in oklab,var(--accent) 30%,var(--bg-soft)), var(--bg-soft));border-color:rgba(26,90,32,.10)}
  .article-cover svg{color:color-mix(in oklab,var(--cream) 30%,transparent)}
  .article-foot .back{color:var(--cream-2)}
  .article-foot .back:hover{color:var(--accent-2)}
  .article-foot .share a{border-color:rgba(26,90,32,.18);color:var(--cream-2)}
  .article-foot .share a:hover{background:var(--accent);color:#1A1A1A}
  .related-articles{border-top-color:rgba(26,90,32,.12)}
  .related-articles h3{color:var(--cream)}

  /* Cart drawer & cart page */
  .cart-drawer{background:#FFFFFF !important;border-left-color:rgba(26,90,32,.12)}
  .cart-head{border-bottom-color:rgba(26,90,32,.10)}
  .cart-head h3{color:var(--cream)}
  .cart-head h3 small{color:var(--cream-2)}
  .cart-close{border-color:rgba(26,90,32,.16);color:var(--cream)}
  .cart-close:hover{background:var(--accent);border-color:var(--accent);color:#1A1A1A}
  .cart-item{border-bottom-color:rgba(26,90,32,.08)}
  .cart-item .ci-img{background:var(--bg-soft);border-color:rgba(26,90,32,.10)}
  .cart-item .ci-info .nm{color:var(--cream)}
  .cart-item .ci-info .pr{color:var(--accent-2)}
  .cart-item .ci-qty button{border-color:rgba(26,90,32,.16);color:var(--cream)}
  .cart-item .ci-qty button:hover{background:var(--accent);border-color:var(--accent);color:#1A1A1A}
  .cart-item .ci-qty .qv{color:var(--cream)}
  .cart-item .ci-rm{color:var(--cream-2)}
  .cart-item .ci-rm:hover{color:var(--accent-2)}
  .cart-empty{color:var(--cream-2)}
  .cart-empty svg{color:var(--cream-2)}
  .cart-foot{background:var(--bg-soft) !important;border-top-color:rgba(26,90,32,.10)}
  .cart-foot .row{color:#555}
  .cart-foot .row.total{color:var(--cream);border-top-color:rgba(26,90,32,.14)}
  .cart-foot .row.total span:last-child{color:var(--accent-2)}
  .cart-foot .checkout-btn{background:var(--cream);color:#FAFAF7}
  .cart-foot .checkout-btn:hover:not(:disabled){background:var(--accent);color:#1A1A1A}
  .cart-foot .view-cart{color:var(--cream-2)}
  .cart-foot .view-cart:hover{color:var(--accent-2)}

  .cart-table{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 14px 40px rgba(26,90,32,.06)}
  .cart-table .row-h{color:var(--cream-2);border-bottom-color:rgba(26,90,32,.10)}
  .cart-table .row{border-bottom-color:rgba(26,90,32,.07)}
  .cart-table .row .img{background:var(--bg-soft);border-color:rgba(26,90,32,.10)}
  .cart-table .row .nm{color:var(--cream)}
  .cart-table .row .nm .sub{color:var(--cream-2)}
  .cart-table .row .qty{border-color:rgba(26,90,32,.16)}
  .cart-table .row .qty button{color:var(--cream)}
  .cart-table .row .qty button:hover{background:var(--accent);color:#1A1A1A}
  .cart-table .row .qty .qv{color:var(--cream)}
  .cart-table .row .total-pr{color:var(--accent-2)}
  .cart-table .row .rm{color:var(--cream-2)}
  .cart-table .row .rm:hover{color:var(--accent-2)}

  .summary{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 14px 40px rgba(26,90,32,.06)}
  .summary h3{color:var(--cream)}
  .summary .line{color:#555;border-bottom-color:rgba(26,90,32,.08)}
  .summary .line.total{color:var(--cream);border-top-color:rgba(26,90,32,.16)}
  .summary .line.total span:last-child{color:var(--accent-2)}
  .summary .promo input{background:#FFFFFF !important;border-color:rgba(26,90,32,.16);color:var(--cream)}
  .summary .promo button{border-color:rgba(26,90,32,.18);color:var(--cream-2)}
  .summary .promo button:hover{background:var(--accent);border-color:var(--accent);color:#1A1A1A}
  .summary .pay-btn{background:var(--cream);color:#FAFAF7}
  .summary .pay-btn:hover{background:var(--accent);color:#1A1A1A}
  .summary .secure{color:var(--cream-2)}
  .cart-empty-page{color:var(--cream-2)}
  .cart-empty-page svg{color:var(--cream-2)}
  .cart-empty-page h2{color:var(--cream)}

  /* Checkout */
  .checkout-form-wrap{background:#FFFFFF !important;border-color:rgba(26,90,32,.10);box-shadow:0 14px 40px rgba(26,90,32,.06)}
  .checkout-form-wrap h3{color:var(--cream);border-top-color:rgba(26,90,32,.10)}
  .checkout-form-wrap h3 .stp{background:var(--accent);color:#1A1A1A}
  .pay-method{background:#FFFFFF;border-color:rgba(26,90,32,.14)}
  .pay-method:hover{border-color:color-mix(in oklab,var(--accent) 50%,transparent)}
  .pay-method.selected{background:color-mix(in oklab,var(--accent) 18%,#FFFFFF);border-color:var(--accent)}
  .pay-method svg{color:var(--cream)}
  .pay-method.selected svg{color:var(--accent-2)}
  .pay-method .nm{color:var(--cream)}
  .pay-method .sub{color:#777}
  .order-success{background:radial-gradient(ellipse at 50% 30%, color-mix(in oklab,var(--accent) 25%,transparent), transparent 60%), linear-gradient(180deg, var(--bg-soft), #FFFFFF) !important;border-color:color-mix(in oklab,var(--accent) 50%,transparent)}
  .order-success .ic{background:var(--accent);color:#1A1A1A}
  .order-success h2{color:var(--cream)}
  .order-success p{color:#555}
  .order-success .ref{background:color-mix(in oklab,var(--accent) 14%,transparent);color:var(--accent-2)}

  /* Scrollbar */
  ::-webkit-scrollbar-track{background:var(--bg-soft) !important}
  ::-webkit-scrollbar-thumb{background:color-mix(in oklab,var(--accent) 50%,rgba(26,90,32,.20)) !important;border:2px solid var(--bg-soft) !important}
  ::-webkit-scrollbar-thumb:hover{background:var(--accent) !important}
  html{scrollbar-color:color-mix(in oklab,var(--accent) 50%,rgba(26,90,32,.20)) var(--bg-soft) !important}

  /* Focus rings */
  *:focus-visible{outline-color:var(--accent) !important}
  button:focus-visible, a:focus-visible{box-shadow:0 0 0 6px color-mix(in oklab, var(--accent) 30%, transparent) !important}

  /* Selection */
  ::selection{background:var(--accent);color:#1A1A1A}
"""

with open(os.path.join(V2, 'assets', 'css', 'oyayi.css'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(css + ivory_override)

# -------- 5. Patch v2/index.html ------------------------------------
# Remove the v2-banner from V2 index (it would link to itself)
# Add a "Retour à V1" banner in its place
idx_path = os.path.join(V2, 'index.html')
with open(idx_path, 'r', encoding='utf-8') as f:
    idx = f.read()

# Strip the v2-banner div (if present) and replace with a V1 link
import re
idx = re.sub(
    r'<!-- ============== V2 COMPARISON BANNER ============== -->.*?</div>\s*\n',
    '',
    idx, count=1, flags=re.DOTALL
)
# Insert a "Voir V1" banner instead (links back to parent /)
v1_banner = '''
<!-- ============== V1 RETURN BANNER ============== -->
<div id="v1-banner" style="position:fixed;left:24px;bottom:24px;z-index:99;display:flex;align-items:center;gap:10px;padding:10px 16px;border-radius:999px;background:#1B5E20;color:#FAFAF7;font-family:DM Sans,sans-serif;font-size:12px;font-weight:500;letter-spacing:.06em;box-shadow:0 14px 30px rgba(26,90,32,.35);border:1px solid #C8A84B">
  <span style="width:8px;height:8px;border-radius:50%;background:#C8A84B;box-shadow:0 0 10px #C8A84B"></span>
  <a href="../" style="color:inherit;text-decoration:none">Retour à la <strong style="font-family:Playfair Display,serif;font-style:italic;font-weight:600">V1</strong> (vert charter) →</a>
</div>
'''
# Insert before </body>
idx = idx.replace('</body>', v1_banner + '\n</body>')

with open(idx_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(idx)

# -------- 6. Also force data-da="brown" on all v2 HTML pages --------
# Wait — the V2 ivory tokens use !important so the data-da value is irrelevant.
# But to be safe and to signal intent, set data-da="brown" on body in all v2 pages.
v2_html_files = [f for f in os.listdir(V2) if f.endswith('.html')]
for fname in v2_html_files:
    p = os.path.join(V2, fname)
    with open(p, 'r', encoding='utf-8') as f: c = f.read()
    # In V2 we use the "brown" slot for ivory theme (per Claude Design pattern)
    new = c.replace('<body data-da="green"', '<body data-da="brown"')
    if new != c:
        with open(p, 'w', encoding='utf-8', newline='\n') as f: f.write(new)

print(f'V2 built:')
print(f'  {html_count} HTML pages cloned from V1')
print(f'  v2/assets/products, v2/assets/catalog, v2/assets/distinctions copied')
print(f'  v2/assets/js (site, home, panier, paiement) copied')
print(f'  v2/assets/css/oyayi.css = V1 css + ivory override block ({len(ivory_override)} chars)')
print(f'  v2/index.html: V2 banner removed, V1 return banner added')
print(f'  all {len(v2_html_files)} v2 pages forced to data-da="brown" (=ivory)')
