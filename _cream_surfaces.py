# -*- coding: utf-8 -*-
"""Append .surface-cream styles to oyayi.css so sections can opt into
the ivoire palette of the OYAYI Sens charter."""

with open('assets/css/oyayi.css', 'r', encoding='utf-8') as f:
    css = f.read()

block = """

  /* ============================================================
     SURFACE-CREAM — ivoire sections per OYAYI Sens charter
     Opt-in via class="section surface-cream". Flips to ivoire bg
     with ink text, green/gold accents preserved. Brings the full
     charter duo (green + ivoire + gold) into the page rhythm.
     ============================================================ */
  .surface-cream{
    background:var(--cream);
    color:var(--ink);
    --line:rgba(26,26,26,.12);
    --hairline:rgba(26,26,26,.06);
    margin-left:0;margin-right:0;
    max-width:none;
    padding-left:max(40px,calc((100vw - 1480px)/2));
    padding-right:max(40px,calc((100vw - 1480px)/2));
  }
  .surface-cream::before{
    content:"";display:block;height:1px;background:linear-gradient(90deg,transparent,color-mix(in oklab,var(--bg-deep) 40%,transparent),transparent);position:absolute;top:0;left:0;right:0;
  }

  /* Headings + tags on cream */
  .surface-cream h1,
  .surface-cream h2,
  .surface-cream h3,
  .surface-cream h4,
  .surface-cream h5,
  .surface-cream h6,
  .surface-cream .sec-title,
  .surface-cream .pname,
  .surface-cream .pcard .name,
  .surface-cream .mini-card .nm,
  .surface-cream .pack h3,
  .surface-cream .blog-card h3,
  .surface-cream .domain h3,
  .surface-cream .ben-card h3,
  .surface-cream .t-card .quote,
  .surface-cream .t-card .nm,
  .surface-cream .quote{
    color:var(--ink);
  }
  .surface-cream .sec-title em,
  .surface-cream em,
  .surface-cream .quote em{
    color:var(--bg-deep);    /* italic emphasis = brand green on cream */
    font-style:italic;
  }
  .surface-cream .sec-tag,
  .surface-cream .latin,
  .surface-cream .desc,
  .surface-cream .meta,
  .surface-cream .lab,
  .surface-cream .role,
  .surface-cream .crumbs,
  .surface-cream .blog-card .meta,
  .surface-cream .blog-card .excerpt,
  .surface-cream .pack p,
  .surface-cream .domain p,
  .surface-cream .ben-card p,
  .surface-cream .article-body p{
    color:#555;
  }
  .surface-cream p{color:#3a3a3a}

  /* Cards on cream — white surfaces with subtle green-tinted borders */
  .surface-cream .pcard,
  .surface-cream .mini-card,
  .surface-cream .pack,
  .surface-cream .domain,
  .surface-cream .ben-card,
  .surface-cream .t-card,
  .surface-cream .blog-card,
  .surface-cream .info-card,
  .surface-cream .product-card,
  .surface-cream .contact-block,
  .surface-cream .diff,
  .surface-cream .distinction,
  .surface-cream .checkout-form-wrap,
  .surface-cream .summary,
  .surface-cream .cart-table{
    background:#FFFFFF !important;
    color:var(--ink);
    border:1px solid rgba(26,26,26,.10);
    box-shadow:0 6px 20px rgba(26,26,26,.06);
  }
  .surface-cream .pcard:hover,
  .surface-cream .mini-card:hover,
  .surface-cream .pack:hover,
  .surface-cream .domain:hover,
  .surface-cream .blog-card:hover,
  .surface-cream .distinction:hover{
    border-color:color-mix(in oklab,var(--accent) 60%,transparent);
    box-shadow:0 18px 40px rgba(26,26,26,.10), 0 0 0 1px color-mix(in oklab,var(--accent) 35%,transparent);
  }

  /* Mini-card image area on cream */
  .surface-cream .pcard .img,
  .surface-cream .mini-card .pimg{
    background:radial-gradient(ellipse at 50% 70%,color-mix(in oklab,var(--accent) 15%,#FFF8E1),#FFFFFF 70%);
    border-bottom-color:rgba(26,26,26,.06);
  }
  .surface-cream .pcard .foot{
    background:transparent !important;
    border-top:1px solid rgba(26,26,26,.08);
  }

  /* Prices in brand green on cream */
  .surface-cream .price,
  .surface-cream .pcard .price,
  .surface-cream .pack .price,
  .surface-cream .product-card .price,
  .surface-cream .mini-card .pr span:first-child,
  .surface-cream .pr,
  .surface-cream .rating-num{
    color:var(--bg-deep);    /* brand green */
    font-weight:500;
  }
  .surface-cream .price small,
  .surface-cream .product-card .price small,
  .surface-cream .pack .price small{color:#777}
  .surface-cream .rating-num span{color:var(--accent)}
  .surface-cream .rating-label{color:#777}

  /* Add buttons */
  .surface-cream .add,
  .surface-cream .pack .add{
    background:var(--bg-deep);
    color:var(--cream);
  }
  .surface-cream .add:hover,
  .surface-cream .pack .add:hover{
    background:var(--accent);
    color:var(--ink);
  }
  .surface-cream .mini-card .pr .add-mini{
    background:var(--bg-deep);
    color:var(--cream);
    box-shadow:0 4px 10px rgba(26,26,26,.15);
  }
  .surface-cream .mini-card .pr .add-mini:hover{
    background:var(--accent);
    color:var(--ink);
  }

  /* Tags / badges on cream */
  .surface-cream .pcard .tag,
  .surface-cream .pack .badge,
  .surface-cream .distinction .badge{
    background:var(--cream-2);
    color:var(--bg-deep);
    border-color:rgba(26,26,26,.12);
    backdrop-filter:none;
  }
  .surface-cream .pcard .tag.hot,
  .surface-cream .pack .badge.coffret{
    color:var(--accent);
    border-color:color-mix(in oklab,var(--accent) 50%,transparent);
  }
  .surface-cream .blog-card .meta .cat{color:var(--accent)}
  .surface-cream .blog-card .read{color:var(--bg-deep);border-top-color:rgba(26,26,26,.08)}
  .surface-cream .blog-card:hover .read{color:var(--accent-2)}
  .surface-cream .blog-card .cover{
    background:linear-gradient(135deg,color-mix(in oklab,var(--accent) 35%,#FFF8E1),#F5F0E0);
  }
  .surface-cream .blog-card .cover svg{color:color-mix(in oklab,var(--bg-deep) 50%,#FFFFFF)}

  /* Section header underline */
  .surface-cream .sec-head{border-bottom:1px solid rgba(26,26,26,.10)}

  /* Chips on cream */
  .surface-cream .chip{
    background:#FFFFFF;
    border-color:rgba(26,26,26,.14);
    color:#555;
  }
  .surface-cream .chip:hover{
    border-color:var(--bg-deep);
    color:var(--bg-deep);
    background:#FFFFFF;
  }
  .surface-cream .chip.active{
    background:var(--bg-deep);
    border-color:var(--bg-deep);
    color:var(--cream);
    box-shadow:0 6px 16px color-mix(in oklab,var(--bg-deep) 30%,transparent);
  }

  /* CTA on cream — invert: dark cta */
  .surface-cream .cta{
    background:var(--bg-deep);
    color:var(--cream);
  }
  .surface-cream .cta:hover{background:var(--accent);color:var(--ink)}
  .surface-cream .cta.ghost{background:transparent;color:var(--ink);border-color:rgba(26,26,26,.20)}
  .surface-cream .cta.ghost:hover{background:#FFF8E1;color:var(--bg-deep);border-color:var(--bg-deep)}

  /* Stars / ratings */
  .surface-cream .stars{color:var(--accent)}

  /* T-card (testimonial) on cream */
  .surface-cream .t-card .av{
    background:linear-gradient(135deg,var(--bg-deep),var(--bg-soft-2));
    color:var(--cream);
  }
  .surface-cream .t-card .who{border-top-color:rgba(26,26,26,.08)}
  .surface-cream .t-card .role{color:#777}

  /* Forms on cream */
  .surface-cream .form-field input,
  .surface-cream .form-field textarea,
  .surface-cream .form-field select,
  .surface-cream .summary .promo input,
  .surface-cream .newsletter input{
    background:#FFFFFF !important;
    border-color:rgba(26,26,26,.14);
    color:var(--ink);
  }
  .surface-cream .form-field input::placeholder,
  .surface-cream .form-field textarea::placeholder{color:#999}
  .surface-cream .form-field input:focus,
  .surface-cream .form-field textarea:focus,
  .surface-cream .form-field select:focus{border-color:var(--bg-deep);background:#FFFFFF !important}
  .surface-cream .form-field label{color:#666}
  .surface-cream .form-submit,
  .surface-cream .summary .pay-btn,
  .surface-cream .newsletter button{
    background:var(--bg-deep);color:var(--cream);
  }
  .surface-cream .form-submit:hover,
  .surface-cream .summary .pay-btn:hover,
  .surface-cream .newsletter button:hover{
    background:var(--accent);color:var(--ink);
  }

  /* Cart table on cream */
  .surface-cream .cart-table .row-h{color:#777;border-bottom-color:rgba(26,26,26,.10)}
  .surface-cream .cart-table .row{border-bottom-color:rgba(26,26,26,.07)}
  .surface-cream .cart-table .row .nm{color:var(--ink)}
  .surface-cream .cart-table .row .nm .sub{color:#888}
  .surface-cream .cart-table .row .qty{border-color:rgba(26,26,26,.16)}
  .surface-cream .cart-table .row .qty button{color:var(--ink)}
  .surface-cream .cart-table .row .total-pr{color:var(--bg-deep)}
  .surface-cream .summary .line{color:#555;border-bottom-color:rgba(26,26,26,.08)}
  .surface-cream .summary .line.total{color:var(--ink);border-top-color:rgba(26,26,26,.16)}
  .surface-cream .summary .line.total span:last-child{color:var(--bg-deep)}

  /* FAQ on cream */
  .surface-cream .faq{border-top-color:rgba(26,26,26,.10)}
  .surface-cream .faq details{border-bottom-color:rgba(26,26,26,.10)}
  .surface-cream .faq summary{color:var(--ink)}
  .surface-cream .faq summary:hover{color:var(--bg-deep)}
  .surface-cream .faq details[open] summary{color:var(--bg-deep)}
  .surface-cream .faq summary .ic{border-color:rgba(26,26,26,.16);color:var(--ink)}
  .surface-cream .faq .a{color:#3a3a3a}
  .surface-cream .faq .a strong{color:var(--ink)}

  /* Article body — long-form reading on cream */
  .surface-cream .article-body{color:#1a1a1a}
  .surface-cream .article-body p{color:#3a3a3a}
  .surface-cream .article-body h2,
  .surface-cream .article-body h3{color:var(--ink)}
  .surface-cream .article-body strong{color:var(--ink)}
  .surface-cream .article-body em{color:var(--bg-deep)}
  .surface-cream .article-body blockquote{
    background:#FFF8E1;
    border-left-color:var(--bg-deep);
    color:var(--ink);
  }
  .surface-cream .article-body a{color:var(--bg-deep)}
  .surface-cream .article-body a:hover{color:var(--accent-2)}

  /* Page hero on cream — softer gradient */
  .surface-cream.page-hero,
  .page-hero.surface-cream{
    background:linear-gradient(180deg,#FAFAF7 0%,#FFF8E1 100%);
    color:var(--ink);
  }
  .surface-cream.page-hero .crumbs{color:#777}
  .surface-cream.page-hero h1{color:var(--ink)}
  .surface-cream.page-hero h1 em{color:var(--bg-deep)}
  .surface-cream.page-hero .lead{color:#555}

  /* Subcat headings on cream */
  .surface-cream .subcat h3{color:var(--ink)}
  .surface-cream .subcat h3 .cover{border-color:rgba(26,26,26,.16)}
  .surface-cream .cat-section{border-bottom-color:rgba(26,26,26,.10)}
  .surface-cream .cat-header h2{color:var(--ink)}
  .surface-cream .cat-header h2 em{color:var(--bg-deep)}
  .surface-cream .cat-header p{color:#555}
  .surface-cream .cat-header .num{color:var(--accent-2)}
"""

if 'SURFACE-CREAM' not in css:
    css += block

with open('assets/css/oyayi.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)

print('Final CSS size:', len(css))
