# -*- coding: utf-8 -*-
"""Apply post-charter UI/UX harmonization patches to oyayi.css."""

with open('assets/css/oyayi.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1) Cards in hero info-card / pcard / pack / domain etc.
old_card_bg = "linear-gradient(180deg,color-mix(in oklab, var(--bg-mid) 90%, transparent),color-mix(in oklab, var(--bg-deep) 90%, transparent))"
new_card_bg = "linear-gradient(180deg,color-mix(in oklab, var(--bg-soft-2) 75%, var(--bg-mid)),color-mix(in oklab, var(--bg-soft-2) 90%, var(--bg-mid)))"
n1 = css.count(old_card_bg)
css = css.replace(old_card_bg, new_card_bg)

# 2) Cream-tinted card bg
old_card_bg_v2 = "linear-gradient(180deg,color-mix(in oklab, var(--cream) 2%, transparent),transparent)"
new_card_bg_v2 = "linear-gradient(180deg,color-mix(in oklab, var(--bg-soft-2) 60%, var(--bg-mid)),color-mix(in oklab, var(--bg-soft-2) 80%, var(--bg-mid)))"
n2 = css.count(old_card_bg_v2)
css = css.replace(old_card_bg_v2, new_card_bg_v2)

old_card_bg_v3 = "linear-gradient(180deg,color-mix(in oklab, var(--cream) 3%, transparent),transparent)"
n3 = css.count(old_card_bg_v3)
css = css.replace(old_card_bg_v3, new_card_bg_v2)

# 3) Marquee / footer base
old_strip = "color-mix(in oklab, var(--bg-deep) 70%, #000)"
new_strip = "var(--bg-soft-2)"
n4 = css.count(old_strip)
css = css.replace(old_strip, new_strip)

# 4) Loader background
old_loader = "radial-gradient(ellipse at 50% 60%, color-mix(in oklab, var(--accent) 12%, var(--bg-deep)), var(--bg-deep) 70%)"
new_loader = "radial-gradient(ellipse at 50% 60%, color-mix(in oklab, var(--accent) 18%, var(--bg-soft-2)), var(--bg-soft-2) 70%)"
n5 = css.count(old_loader)
css = css.replace(old_loader, new_loader)

# 5) Form input bg
old_input = "background:color-mix(in oklab,var(--bg-deep) 60%,transparent);"
new_input = "background:color-mix(in oklab,var(--bg-soft-2) 70%,var(--bg-mid));"
n6 = css.count(old_input)
css = css.replace(old_input, new_input)

# 6) Drop shadows
n7 = css.count("rgba(0,0,0,.4)")
css = css.replace("rgba(0,0,0,.4)", "rgba(0,0,0,.55)")
n8 = css.count("rgba(0,0,0,.5)")
css = css.replace("rgba(0,0,0,.5)", "rgba(0,0,0,.6)")

polish = """

  /* ============================================================
     UI/UX HARMONIZATION (post-charter)
     Accessibility: keyboard focus, prefers-reduced-motion, scrollbars
     ============================================================ */
  *:focus-visible{
    outline:2px solid var(--accent);
    outline-offset:3px;
    border-radius:4px;
  }
  button:focus-visible, a:focus-visible{
    outline:2px solid var(--accent);
    outline-offset:3px;
    box-shadow:0 0 0 6px color-mix(in oklab, var(--accent) 25%, transparent);
  }
  @media (prefers-reduced-motion: reduce){
    *,*::before,*::after{
      animation-duration:.01ms !important;
      animation-iteration-count:1 !important;
      transition-duration:.05ms !important;
      scroll-behavior:auto !important;
    }
  }
  ::-webkit-scrollbar{width:10px;height:10px}
  ::-webkit-scrollbar-track{background:var(--bg-soft-2)}
  ::-webkit-scrollbar-thumb{background:color-mix(in oklab,var(--accent) 40%,var(--bg-mid));border-radius:6px;border:2px solid var(--bg-soft-2)}
  ::-webkit-scrollbar-thumb:hover{background:var(--accent)}
  html{scrollbar-color:color-mix(in oklab,var(--accent) 40%,var(--bg-mid)) var(--bg-soft-2);scrollbar-width:thin}

  .pcard, .pack, .domain, .ben-card, .t-card, .blog-card, .mini-card, .info-card, .product-card, .contact-block, .diff, .distinction, .article-cover{
    box-shadow:inset 0 1px 0 rgba(255,255,255,.04), 0 12px 30px rgba(0,0,0,.35);
  }
  .pcard:hover, .pack:hover, .domain:hover, .blog-card:hover, .mini-card:hover, .distinction:hover{
    box-shadow:inset 0 1px 0 rgba(255,255,255,.08), 0 22px 50px rgba(0,0,0,.55), 0 0 0 1px color-mix(in oklab,var(--accent) 30%,transparent);
  }

  footer{background:linear-gradient(180deg, var(--bg-soft-2) 0%, color-mix(in oklab, var(--bg-soft-2) 60%, #000) 100%) !important;}

  .section, .cat-section{position:relative}
  .car-strip{border-top-color:color-mix(in oklab,var(--cream) 22%,transparent)}

  .nav{background:linear-gradient(to bottom, color-mix(in oklab, var(--bg-soft-2) 88%, transparent) 0%, color-mix(in oklab, var(--bg-soft-2) 50%, transparent) 70%, transparent 100%) !important;}

  .pcard .price small, .pack .price small, .product-card .price small{color:var(--cream-2)}

  .cta:hover{background:#fff;box-shadow:0 12px 28px rgba(0,0,0,.45)}
  .cta.ghost:hover{background:color-mix(in oklab,var(--cream) 12%,transparent);border-color:var(--cream)}

  .chip.active{background:var(--accent);color:var(--ink);border-color:var(--accent);box-shadow:0 6px 16px color-mix(in oklab,var(--accent) 45%,transparent)}

  .faq summary{transition:background .25s, color .25s, padding-left .25s}
  .faq summary:hover{padding-left:8px}
  .faq details[open] summary{color:var(--accent)}

  .distinction .badge{background:color-mix(in oklab, var(--bg-soft-2) 85%, transparent)}

  .nav-links a.active::after{height:2px;background:var(--accent);box-shadow:0 0 12px color-mix(in oklab,var(--accent) 60%,transparent)}
  .nav-links a:hover{color:var(--accent);opacity:1}

  .mini-card .pr .add-mini{box-shadow:0 4px 10px rgba(0,0,0,.3)}

  body{text-rendering:optimizeLegibility;font-feature-settings:"kern" 1, "liga" 1, "ss01" 1}

  ::selection{background:var(--accent);color:var(--ink)}
"""

if 'UI/UX HARMONIZATION (post-charter)' not in css:
    css += polish

with open('assets/css/oyayi.css', 'w', encoding='utf-8', newline='\n') as f:
    f.write(css)

print('Patches applied:')
print(f'  card-bg v1 main:   {n1} replacements')
print(f'  card-bg v2 cream2: {n2} replacements')
print(f'  card-bg v3 cream3: {n3} replacements')
print(f'  marquee/footer:    {n4} replacements')
print(f'  loader bg:         {n5} replacements')
print(f'  form inputs:       {n6} replacements')
print(f'  shadow .4 -> .55:  {n7} replacements')
print(f'  shadow .5 -> .6:   {n8} replacements')
print(f'Final CSS size: {len(css)} chars')
