# -*- coding: utf-8 -*-
"""Generate inner pages (a-propos, contacts, coffrets-packs, produits, blog)
from a shared head/nav/footer shell. Each page provides its own body content."""

import io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def page_shell(title, desc, active, body_html, extra_head=''):
    nav_links = [
        ('index.html',          'Accueil',           '01'),
        ('produits.html',       'Nos produits',      '02'),
        ('coffrets-packs.html', 'Coffrets & Packs',  '03'),
        ('a-propos.html',       'À propos',          '04'),
        ('blog.html',           'Conseils',          '05'),
        ('contacts.html',       'Contacts',          '06'),
    ]
    def link(h, lbl):
        cls = ' class="active"' if active == h else ''
        return f'    <a href="{h}"{cls}>{lbl}</a>\n'
    nav_top = ''.join(link(h, l) for h, l, _ in nav_links)
    drawer = ''.join(
        f'  <a href="{href}">{label} <small>{num}</small></a>\n'
        for href, label, num in nav_links
    )
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,300;1,9..144,400&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/css/oyayi.css">
{extra_head}
</head>
<body data-da="green" class="loading">

<div class="loader-overlay" id="loader" role="status" aria-label="Chargement">
  <div class="loader-inner">
    <div class="loader-mark"></div>
    <div class="loader-brand">OYAYI <small>NATURE · BÉNIN</small></div>
    <div class="loader-bar"><i></i></div>
  </div>
</div>

<header class="nav">
  <a href="index.html" class="brand"><span class="mark"></span> OYAYI <span style="opacity:.5;font-size:14px;letter-spacing:.3em">NATURE</span></a>
  <nav class="nav-links">
{nav_top}  </nav>
  <div class="nav-right">
    <button class="icon-btn" aria-label="Recherche"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></button>
    <button class="icon-btn" aria-label="Compte"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/></svg></button>
    <a href="panier.html" class="cta">Panier <span class="cart-badge">00</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Menu"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
  </div>
</header>

<div class="nav-drawer" id="navDrawer">
{drawer}  <div class="nav-drawer-foot">+229 0196627168<br/>contact@oyayinature.com<br/>Cotonou · Ganhi</div>
</div>

{body_html}

<section class="section">
  <div class="newsletter">
    <div>
      <h3>Choisissez la <em>nature</em>.<br/>Rejoignez notre newsletter.</h3>
      <p>Recevez de nouveaux articles directement dans votre boîte mail, chaque vendredi matin. Sans spam.</p>
    </div>
    <form class="newsletter-form" autocomplete="off">
      <input type="email" required placeholder="votre@email.com" aria-label="Adresse e-mail" />
      <button type="submit">S’abonner</button>
    </form>
  </div>
</section>

<footer>
  <div class="foot-grid">
    <div>
      <div class="foot-brand">OYAYI <em>Nature</em></div>
      <p class="foot-tag">Cosmétique naturelle béninoise. Huiles essentielles, miels, argiles et soins distillés à Cotonou avec patience, dans le respect du vivant.</p>
      <div style="margin-top:18px;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.18em;color:var(--cream-2);opacity:.7;line-height:1.7">
        +229 0196627168<br/>contact@oyayinature.com<br/>Cotonou · Ganhi
      </div>
    </div>
    <div><h6>// Boutique</h6><ul>
      <li><a href="produits.html">Toutes les huiles</a></li>
      <li><a href="coffrets-packs.html">Coffrets &amp; Packs</a></li>
      <li><a href="produits.html#aromatherapie">Diffuseurs &amp; AVITI</a></li>
      <li><a href="produits.html#apitherapie">Miels aromatisés</a></li>
    </ul></div>
    <div><h6>// Maison</h6><ul>
      <li><a href="a-propos.html">Notre histoire</a></li>
      <li><a href="a-propos.html#vision">Vision &amp; Mission</a></li>
      <li><a href="a-propos.html#distinctions">Distinctions</a></li>
      <li><a href="blog.html">Conseils &amp; Journal</a></li>
    </ul></div>
    <div><h6>// Aide</h6><ul>
      <li><a href="contacts.html">Contacts</a></li>
      <li><a href="index.html#faq">FAQ</a></li>
      <li><a href="https://www.facebook.com/oyayinature/" target="_blank" rel="noopener">Facebook</a></li>
      <li><a href="https://www.instagram.com/oyayicosmetiquenaturellehe/" target="_blank" rel="noopener">Instagram</a></li>
    </ul></div>
  </div>
  <div class="foot-bottom"><span>© 2025 OYAYI NATURE — TOUS DROITS RÉSERVÉS</span><span>COTONOU · BJ // FAIT AVEC PATIENCE</span></div>
</footer>

<button class="theme-fab" id="themeFab" aria-label="Changer la palette de couleurs" title="Basculer entre Vert · Forêt et Brun · Terre">
  <span class="swatch" aria-hidden="true"></span>
  <span id="themeFabLabel">Vert · Forêt</span>
</button>

<script src="assets/js/site.js"></script>
</body>
</html>
"""


# ============================================================
# A PROPOS
# ============================================================
APROPOS_BODY = """
<section class="page-hero">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // À propos</div>
    <h1>Notre <em>histoire</em>,<br/>goutte après goutte.</h1>
    <p class="lead">OYAYI est née d'une passion profonde pour la nature et ses trésors cachés. Une aventure humaine au plus près de la terre béninoise, des productrices et des savoirs ancestraux.</p>
  </div>
</section>

<section class="section" id="histoire">
  <div class="split">
    <div class="split-l">
      <div class="sec-tag" style="margin-bottom:20px">// Notre histoire</div>
      <h2 class="sec-title" style="font-size:42px;line-height:1.05">Remettre les bienfaits des plantes au <em>cœur du quotidien</em>.</h2>
      <p style="margin-top:24px;color:var(--cream-2);font-size:15px;line-height:1.7">Nous avons commencé notre aventure avec une seule idée : remettre les bienfaits des plantes au cœur du bien-être quotidien. À travers les huiles essentielles, nous reconnectons l'humain à la terre, avec authenticité, respect et amour des origines.</p>
      <p style="margin-top:18px;color:var(--cream-2);font-size:15px;line-height:1.7">Chaque flacon que nous produisons porte en lui une part d'histoire, de savoir-faire et de pureté. Au fil des années, notre engagement s'est renforcé. Nous avons parcouru les terres, rencontré des producteurs passionnés et redonné de la valeur aux traditions ancestrales de soin par les plantes.</p>
      <p style="margin-top:18px;color:var(--cream-2);font-size:15px;line-height:1.7">Oyayi, c'est aussi une aventure humaine : celle d'hommes et de femmes convaincus que le retour à l'essentiel peut transformer des vies. Aujourd'hui, notre histoire continue de s'écrire, goutte après goutte, avec vous.</p>
    </div>
    <div class="split-r">
      <div class="ring ring1"></div>
      <div class="ring ring2"></div>
      <span class="pin pin1">// 01 — Cueillette</span>
      <span class="pin pin2">// 02 — Distillation</span>
      <span class="pin pin3">// 03 — Mise en flacon</span>
      <img src="assets/products/tchayo.png" alt="Tchayo Basilic Africain" />
    </div>
  </div>
</section>

<section class="section" id="vision">
  <div class="sec-head"><div>
    <div class="sec-tag">// Notre vision</div>
    <h2 class="sec-title">Devenir la référence béninoise et africaine du bien-être <em>100 % naturel</em>.</h2>
  </div></div>
  <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:24px">
    <div style="padding:36px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,color-mix(in oklab,var(--bg-mid) 80%,transparent),color-mix(in oklab,var(--bg-deep) 90%,transparent))">
      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.22em;color:var(--accent);text-transform:uppercase">// Vision</div>
      <p style="margin-top:18px;font-family:'Fraunces',serif;font-weight:300;font-size:24px;line-height:1.35;letter-spacing:-.005em">En valorisant durablement les richesses botaniques locales et les savoirs ancestraux, tout en bâtissant un modèle économique durable qui place les <em style="color:var(--accent)">femmes productrices</em> au cœur de notre succès.</p>
      <p style="margin-top:18px;color:var(--cream-2);font-size:14px;line-height:1.65;font-style:italic">OYAYI est la voie par laquelle ces solutions prennent racine, fleurissent et rayonnent.</p>
    </div>
    <div style="padding:36px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,color-mix(in oklab,var(--bg-mid) 80%,transparent),color-mix(in oklab,var(--bg-deep) 90%,transparent))">
      <div style="font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.22em;color:var(--accent);text-transform:uppercase">// Mission</div>
      <p style="margin-top:18px;font-family:'Fraunces',serif;font-weight:300;font-size:24px;line-height:1.35;letter-spacing:-.005em">Révéler la puissance des <em style="color:var(--accent)">plantes africaines</em> pour le bien-être humain, tout en créant de la valeur durable pour les femmes, les communautés rurales et la planète.</p>
      <p style="margin-top:18px;color:var(--cream-2);font-size:14px;line-height:1.65;font-style:italic">Soigner autrement, produire localement, et impacter durablement.</p>
    </div>
  </div>
</section>

<section class="section" id="valeurs">
  <div class="sec-head"><div>
    <div class="sec-tag">// Nos valeurs</div>
    <h2 class="sec-title">Chaque goutte porte plus qu'un parfum :<br/>une <em>éthique</em>, une <em>terre</em>, un <em>engagement</em>.</h2>
  </div></div>
  <div class="values">
    <div class="value">
      <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2v6m0 0c-3 0-6 2-6 6 0 5 6 8 6 8s6-3 6-8c0-4-3-6-6-6z"/></svg></div>
      <div class="nm">Nature intégrale &amp; transparence</div>
    </div>
    <div class="value">
      <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="5"/><path d="M3 21c0-5 4-9 9-9s9 4 9 9"/></svg></div>
      <div class="nm">Respect des femmes &amp; des savoirs</div>
    </div>
    <div class="value">
      <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 6h18l-2 14H5L3 6zM8 6V4h8v2"/></svg></div>
      <div class="nm">Zéro gaspillage, 100 % de valeurs</div>
    </div>
    <div class="value">
      <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 11h6M12 8v6M5 4h14v16H5z"/></svg></div>
      <div class="nm">Science &amp; tradition, en harmonie</div>
    </div>
    <div class="value">
      <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18"/></svg></div>
      <div class="nm">Impact durable</div>
    </div>
  </div>
</section>

<section class="section" id="differenciateurs">
  <div class="sec-head"><div>
    <div class="sec-tag">// Ce qui nous rend uniques</div>
    <h2 class="sec-title">Qu'est-ce qui rend nos huiles <em>différentes</em> ?</h2>
  </div></div>
  <div class="diffs">
    <div class="diff">
      <div class="num">// 01</div>
      <h3>Le pouvoir des plantes africaines</h3>
      <p>Nous ne copions pas des formules. Nous révélons ce que la nature béninoise et africaine offre de plus pur : citronnelle, niaouli, basilic africain, laurier, clou de girofle, gingembre, etc.</p>
    </div>
    <div class="diff">
      <div class="num">// 02</div>
      <h3>Un modèle porté par des femmes rurales</h3>
      <p>Plusieurs dizaines de femmes productrices, formées, encadrées, rémunérées équitablement. Chez OYAYI, chaque produit est un acte d'autonomisation.</p>
    </div>
    <div class="diff">
      <div class="num">// 03</div>
      <h3>Zéro gaspillage, 100 % valorisation</h3>
      <p>Nous transformons tout. Les plantes deviennent huiles essentielles ou hydrolats ; les déchets deviennent compost. Rien ne se perd. Chaque étape respecte la vie et préserve l'environnement.</p>
    </div>
    <div class="diff">
      <div class="num">// 04</div>
      <h3>Tradition + Science</h3>
      <p>Nos produits sont enracinés dans les savoirs ancestraux africains, mais validés par une démarche scientifique exigeante : certification, traçabilité, qualité pharmaceutique.</p>
    </div>
  </div>
</section>

<section class="section" id="distinctions">
  <div class="sec-head"><div>
    <div class="sec-tag">// Galerie · Nos distinctions</div>
    <h2 class="sec-title">Des moments de <em>reconnaissance</em>.</h2>
  </div></div>
  <div class="distinctions">
""" + ''.join(
        f'    <div class="distinction"><img src="assets/distinctions/{i:02d}.jpg" alt="Distinction OYAYI {i:02d}" loading="lazy"/><span class="lab">Distinction · {i:02d}</span></div>\n'
        for i in range(1, 9)
    ) + """  </div>
  <p style="margin-top:30px;text-align:center;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.22em;color:var(--cream-2);opacity:.6;text-transform:uppercase">// 8 distinctions reçues — Cotonou · Bénin</p>
</section>

<section class="section" id="avis">
  <div class="sec-head"><div>
    <div class="sec-tag">// 16 témoignages clients</div>
    <h2 class="sec-title">Ils ont changé leurs habitudes<br/>avec <em>OYAYI</em>.</h2>
  </div>
    <div class="rating">
      <div class="rating-num">5,0<span aria-hidden="true">★</span></div>
      <div class="rating-label">// Note moyenne sur Google</div>
    </div>
  </div>
  <div class="testi">
""" + ''.join(
        f'''    <article class="t-card"><div><div class="stars">★★★★★</div><p class="quote">« {q} »</p></div><div class="who"><div class="av">{n[0]}</div><div><div class="nm">{n}</div><div class="role">{role}</div></div></div></article>
'''
        for n, role, q in [
            ("Fresnellia SAGBO", "Cliente fidèle",
             "Je suis ravie de partager mon expérience avec OYAYI. La qualité des produits est exceptionnelle, chaque huile est soigneusement sélectionnée. Leur service client est remarquable. Un bien-être waouh !"),
            ("Michèle A.", "Cotonou · cliente régulière",
             "Un lieu magique qui vous fera voyager dans l'univers des huiles essentielles et des hydrolats. Vous ne repartirez pas les mains vides ! J'aime particulièrement leur HE de Laurier."),
            ("Marius Houinsa", "Praticien · Cotonou",
             "Je suis très content des bons retours de mes soins après l'utilisation des huiles essentielles biologiques. Le bon parfum embaume ma cabine et reste longtemps après mes séances de massages."),
            ("Folakè CHOGNIKA", "Maman · Cotonou",
             "L'accueil est très chaleureux. J'ai expérimenté différents miels et tous sont bons. Mes enfants adorent le miel à base d'eucalyptus. C'est notre coup de cœur !"),
            ("Anastasia YVES", "Cliente",
             "Les vendeurs sont très accueillants et donnent des explications claires sur les produits. Les miels sont efficaces et les huiles essentielles ne sont pas diluées donc c'est parfait."),
            ("Marie Medenou", "Cliente engagée",
             "Les meilleurs produits fabriqués avec beaucoup de soin et de rigueur. Très efficaces à tout point de vue. Il faut oser changer ses habitudes de soins avec OYAYI."),
            ("Théophile Aguèmon AVOCEVOU", "Cotonou",
             "Avec OYAYI Cosmétique, nous retrouvons nos sens avec les huiles essentielles. Et notre jeunesse s'en trouve renouvelée. Bon vent OYAYI."),
            ("Sandra Lakoussan", "Maman",
             "L'HV de neem qui a chuté la température de mon enfant la fois dernière est une merveille. Adopter les produits naturels faits au Bénin à base de plantes naturelles."),
            ("Pat34", "Client",
             "C'est la boutique d'huile essentielle de Cotonou. La propriétaire et son savoir-faire ancestral pourra vous conseiller."),
            ("Lewis OGOU", "Client",
             "Je recommande cet endroit. Ils ont de bons produits naturels. Faites un tour là-bas."),
            ("Yolande Dedjinou", "Cliente AVITI",
             "Avec AVITI l'inhalateur des huiles essentielles je n'ai plus de soucis lorsque le rhume attaque un membre de ma famille."),
            ("Alexandre Gandaho", "Client",
             "Très bonne expérience client, des produits efficaces. Le meilleur en termes d'aromathérapie au Bénin tout simplement."),
            ("Emmanuel TAIDJARE", "Client fidèle",
             "J'adore, produits d'excellentes qualités, accueil fantastique toujours avec le sourire dans une atmosphère très chaleureuse. Pleins succès à vous !"),
            ("Candide DOSSOU-YOVO", "Cliente",
             "Un endroit convivial et chaleureux avec des senteurs naturelles. Je le recommande vivement."),
            ("Abikè AGUIDI", "Cliente",
             "Des produits excellents avec beaucoup de professionnalisme pour le service client."),
            ("Sica Christelle Yaovi", "Cliente",
             "Excellents produits. Très satisfaite."),
        ]
    ) + """  </div>
</section>
"""

# ============================================================
# CONTACTS
# ============================================================
CONTACTS_BODY = """
<section class="page-hero">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // Contacts</div>
    <h1><em>Joignez</em>-nous.</h1>
    <p class="lead">Une question, une idée ou juste envie d'échanger ? Écrivez-nous, nous serons ravis de vous répondre rapidement.</p>
  </div>
</section>

<section class="section">
  <div class="contact-grid">
    <div class="contact-info">
      <div class="contact-block">
        <div class="lab"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg> Adresse</div>
        <div class="val">Cotonou / Ganhi</div>
        <div class="sub">République du Bénin</div>
      </div>
      <div class="contact-block">
        <div class="lab"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg> Appelez-nous</div>
        <div class="val"><a href="tel:+2290196627168">+229 0196627168</a></div>
        <div class="sub"><a href="tel:+2290143965339">+229 0143965339</a></div>
      </div>
      <div class="contact-block">
        <div class="lab"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4h16v16H4zM4 4l8 8 8-8"/></svg> E-mail</div>
        <div class="val"><a href="mailto:contact@oyayinature.com">contact@oyayinature.com</a></div>
        <div class="sub">Réponse sous 24-48 h</div>
      </div>
      <div class="contact-block">
        <div class="lab"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg> Réseaux sociaux</div>
        <div class="val">Suivez-nous</div>
        <div class="socials">
          <a href="https://www.facebook.com/oyayinature/" target="_blank" rel="noopener" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.5 9.9v-7H8V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.5 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg></a>
          <a href="https://www.instagram.com/oyayicosmetiquenaturellehe/" target="_blank" rel="noopener" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="1" fill="currentColor"/></svg></a>
        </div>
      </div>
    </div>

    <form class="contact-form" id="contactForm" autocomplete="off">
      <h2>Formulaire de contact</h2>
      <p class="intro">Nous vous répondons sous 48 h ouvrées. Pour toute commande, indiquez la référence du produit.</p>
      <div class="form-row">
        <div class="form-field">
          <label for="cf-name">Nom &amp; Prénoms</label>
          <input id="cf-name" name="name" type="text" required placeholder="Marie KOUASSI" />
        </div>
        <div class="form-field">
          <label for="cf-email">Adresse e-mail</label>
          <input id="cf-email" name="email" type="email" required placeholder="marie@example.com" />
        </div>
      </div>
      <div class="form-field">
        <label for="cf-subject">L'objet du message</label>
        <input id="cf-subject" name="subject" type="text" required placeholder="Conseil sur l'huile essentielle de Tchayo" />
      </div>
      <div class="form-field">
        <label for="cf-msg">Votre message</label>
        <textarea id="cf-msg" name="message" required placeholder="Votre message..."></textarea>
      </div>
      <button type="submit" class="form-submit">Envoyer le message
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>
      </button>
      <div class="form-success" id="contactSuccess">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="m9 12 2 2 4-4"/></svg>
        Merci ! Votre message a bien été envoyé. Nous vous répondons sous 48 h.
      </div>
    </form>
  </div>

  <div class="map-wrap">
    <iframe src="https://www.google.com/maps?q=OYAYI+Cosm%C3%A9tique+Naturelle+Cotonou+Ganhi&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Localisation OYAYI Cotonou Ganhi"></iframe>
  </div>
</section>
"""

# ============================================================
# COFFRETS PACKS
# ============================================================
COFFRETS_BODY = """
<section class="page-hero">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // Coffrets &amp; Packs</div>
    <h1>Coffrets &amp; <em>Packs</em><br/>bien-être.</h1>
    <p class="lead">Des huiles essentielles et soins naturels adaptés à vos besoins, pour une routine bien-être simple et efficace.</p>
  </div>
</section>

<section class="section" id="coffrets">
  <div class="sec-head"><div>
    <div class="sec-tag">// Nos coffrets · 2 références</div>
    <h2 class="sec-title">Nos <em>coffrets</em>.</h2>
  </div></div>
  <div class="packs">
    <article class="pack" data-id="coffret-he">
      <span class="badge coffret">Coffret</span>
      <div class="num">01 / 02</div>
      <h3>Coffret d'huiles essentielles</h3>
      <p>Une sélection de nos meilleures huiles essentielles, présentée dans un écrin élégant. Idéal pour découvrir l'aromathérapie ou pour offrir.</p>
      <div class="pack-foot">
        <div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter au panier" data-name="Coffret d'huiles essentielles" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
    <article class="pack" data-id="coffret-miel">
      <span class="badge coffret">Coffret</span>
      <div class="num">02 / 02</div>
      <h3>Coffret de miel</h3>
      <p>Notre sélection de miels purs et aromatisés (gingembre, citron, eucalyptus, basilic-romarin) pour s'offrir une cure de douceur et de bienfaits.</p>
      <div class="pack-foot">
        <div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter au panier" data-name="Coffret de miel" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
  </div>
</section>

<section class="section" id="packs">
  <div class="sec-head"><div>
    <div class="sec-tag">// Nos packs · 5 routines ciblées</div>
    <h2 class="sec-title">Nos <em>packs</em> bien-être.</h2>
  </div></div>
  <div class="packs">
    <article class="pack" data-id="pack-detente">
      <span class="badge">Pack</span>
      <div class="num">01 / 05</div>
      <h3>Pack détente</h3>
      <p>Lavande, néroli et orange douce pour relâcher les tensions accumulées. Diffusion en fin de journée, massage doux après le bain.</p>
      <div class="pack-foot"><div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter" data-name="Pack détente" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
    <article class="pack" data-id="pack-sommeil">
      <span class="badge">Pack</span>
      <div class="num">02 / 05</div>
      <h3>Pack sommeil</h3>
      <p>Lavande vraie, mandarine, néroli — la trinité apaisante pour retrouver des nuits profondes et réparatrices.</p>
      <div class="pack-foot"><div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter" data-name="Pack sommeil" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
    <article class="pack" data-id="pack-bonnes-vibrations">
      <span class="badge">Pack</span>
      <div class="num">03 / 05</div>
      <h3>Pack bonnes vibrations</h3>
      <p>Citronnelle, agrumes pétillants et tchayo basilic africain pour une ambiance lumineuse et énergisante.</p>
      <div class="pack-foot"><div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter" data-name="Pack bonnes vibrations" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
    <article class="pack" data-id="pack-purification">
      <span class="badge">Pack</span>
      <div class="num">04 / 05</div>
      <h3>Pack purification</h3>
      <p>Niaouli, eucalyptus, laurier — un trio aux notes franches pour assainir l'air et soutenir l'immunité au quotidien.</p>
      <div class="pack-foot"><div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter" data-name="Pack purification" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
    <article class="pack" data-id="pack-antidouleur">
      <span class="badge">Pack</span>
      <div class="num">05 / 05</div>
      <h3>Pack antidouleur</h3>
      <p>Menthe poivrée, baume anti-rhumatisme et HV massage. Soulage tensions musculaires et articulaires.</p>
      <div class="pack-foot"><div class="price">20 000 <small>CFA</small></div>
        <button class="add" aria-label="Ajouter" data-name="Pack antidouleur" data-price="20 000"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>
      </div>
    </article>
  </div>
</section>

<script>
document.querySelectorAll('.pack .add').forEach(btn => {
  btn.addEventListener('click', e => {
    e.stopPropagation();
    const card = btn.closest('.pack');
    window.OYAYI && window.OYAYI.addToCart({
      id: card.dataset.id,
      name: btn.dataset.name,
      price: btn.dataset.price
    });
  });
});
</script>
"""

# ============================================================
# PRODUITS (catalogue complet)
# ============================================================
def cat_section(num, total, anchor, title_html, desc, subcats):
    cards = ''
    for sub_title, items in subcats:
        # Find a cover image for the subcat (first item with image)
        cover_html = ''
        cover_map = {
            'Diffuseurs':         'assets/catalog/diffuseurs-cover.jpg',
            'Inhalateurs':        'assets/catalog/inhalateurs-cover.jpg',
            'Synergies aromatiques': 'assets/catalog/synergies-cover.jpg',
            'Huiles végétales':   'assets/catalog/hv-cover.jpg',
            'Macérats huileux':   'assets/catalog/macerats-cover.jpg',
            'Huiles de massage':  'assets/catalog/massages-cover.jpg',
            'Beurres végétaux':   'assets/catalog/beurres-cover.jpg',
            'Argiles &amp; sels': 'assets/catalog/argiles-cover.jpg',
            'Tisanes &amp; thés': 'assets/catalog/tisane-cover.png',
            'Poudres':            'assets/catalog/poudres-cover.png',
            'Eaux florales':      'assets/catalog/eaux-florales-cover.jpg',
            'Jus &amp; teintures':'assets/catalog/teintures-cover.jpg',
            'Miel pur':           'assets/catalog/miel-pur-cover.jpg',
            'Miels aromatisés':   'assets/catalog/miels-aromatises-cover.jpg',
            'Crèmes fouettées':   'assets/catalog/cremes-cover.jpg',
            'Bientôt disponible': 'assets/catalog/savons-cover.jpg',
        }
        if sub_title in cover_map:
            cover_html = f'<span class="cover"><img src="{cover_map[sub_title]}" alt=""/></span>'

        cards += f'  <div class="subcat"><h3>{cover_html}{sub_title}</h3><div class="mini-grid">\n'
        for nm, pr in items:
            slug = nm.lower().replace('·', '').replace("'", '').replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('â','a').replace('ô','o').replace('î','i').replace('ï','i').replace('ç','c')
            slug = ''.join(c if c.isalnum() else '-' for c in slug).strip('-')
            slug = '-'.join(filter(None, slug.split('-')))
            img_src = IMG_MAP.get(nm)
            data_attrs = f'data-id="{slug}" data-name="{nm.replace("&amp;","et")}" data-price="{pr or ""}"'
            if img_src:
                data_attrs += f' data-image="{img_src}"'
                bleed = ' class="bleed"' if nm in WHITE_BG_PRODUCTS else ''
                pimg = f'<div class="pimg"><img src="{img_src}" alt="{nm}" loading="lazy"{bleed}/></div>'
            else:
                pimg = f'<div class="pimg placeholder">{PLACEHOLDER_SVG}</div>'
            if pr:
                add_btn = '<button class="add-mini" aria-label="Ajouter au panier"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg></button>'
                pr_html = f'<div class="pr"><span>{pr} CFA</span>{add_btn}</div>'
            else:
                pr_html = '<div class="pr tba">À venir</div>'
            cards += f'    <div class="mini-card" {data_attrs}>{pimg}<div class="body"><div class="nm">{nm}</div>{pr_html}</div></div>\n'
        cards += '  </div></div>\n'
    return f"""
<section class="cat-section" id="{anchor}">
  <div class="cat-header">
    <div>
      <span class="num">{num} / {total}</span>
      <h2>{title_html}</h2>
    </div>
    <p>{desc}</p>
  </div>
{cards}</section>
"""

# Map product names → local image (assets/catalog or assets/products)
IMG_MAP = {
    'HE Tchayo · Basilic Africain':  'assets/products/tchayo.png',
    'HE Basilic':                    'assets/catalog/he-basilic.png',
    'HE Ail':                        'assets/catalog/he-ail.png',
    'HE Bergamote':                  'assets/products/orange-douce.png',  # fallback agrume local
    'HE Laurier Noble':              'assets/products/laurier.png',
    'HE Lavande Vraie':              'assets/products/lavande.png',
    'HE Néroli':                     'assets/products/neroli.png',
    'HE Niaouli':                    'assets/products/niaouli.png',
    'HE Menthe Poivrée':             'assets/products/menthe-poivree.png',
    'HE Origan':                     'assets/products/origan.png',
    'HE Mandarine':                  'assets/products/mandarine.png',
    'HE Orange Douce':               'assets/products/orange-douce.png',
    'HE Palmarosa':                  'assets/products/palmarosa.png',
    'HE Myrrhe':                     'assets/products/myrrhe.png',
    'HE Muscade':                    'assets/products/muscade.png',
    'Pack les 5 indispensables':     'assets/catalog/pack-5-indispensables.jpg',

    'Diffuseur à bâton':             'assets/catalog/diffuseur-baton.png',
    'Diffuseur terre cuite':         'assets/catalog/diffuseur-terre-cuite.jpg',
    'Diffuseur électrique':          'assets/catalog/diffuseur-electrique.png',
    'AVITI · inhalateur':            'assets/catalog/aviti.png',

    'Argile Blanche en poudre':      'assets/catalog/argile-blanche.jpg',

    'Poudre de Cannelle':            'assets/catalog/poudre-cannelle.png',
    'Poudre de Chébé':               'assets/catalog/poudre-chebe.png',
    'Poudre de Clou de Girofle':     'assets/catalog/poudre-girofle.png',

    'Miel Gingembre':                'assets/catalog/miel-gingembre.png',
    'Miel Citron':                   'assets/catalog/miel-citron.png',
    'Miel Citronnelle':              'assets/catalog/miel-citronnelle.png',
    'Miel Eucalyptus':               'assets/catalog/miel-eucalyptus.png',
    'Miel Agrumes':                  'assets/catalog/miel-agrumes.png',
}

PLACEHOLDER_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12z"/></svg>'

# Products with white background that should blend with the dark UI
WHITE_BG_PRODUCTS = {'Diffuseur à bâton'}

PRODUITS_BODY = """
<section class="page-hero">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // Nos produits</div>
    <h1>Catalogue <em>complet</em>.</h1>
    <p class="lead">Cinq univers de soin naturel : aromathérapie, huiles &amp; argiles, phytothérapie, apithérapie, hygiène &amp; cosmétique. Plus de 50 références.</p>
  </div>
</section>

<div class="section" style="padding-top:0;padding-bottom:0">
""" + cat_section('01', '05', 'aromatherapie',
    'Aromathérapie<em>.</em>',
    "Soins par les huiles essentielles. Inhalation, diffusion, application cutanée.",
    [
        ('Huiles essentielles', [
            ('HE Tchayo · Basilic Africain', '5 000'),
            ('HE Basilic', '6 000'),
            ('HE Ail', '4 000'),
            ('HE Bergamote', '6 500'),
            ('HE Laurier Noble', '7 500'),
            ('HE Lavande Vraie', '9 500'),
            ('HE Néroli', '14 000'),
            ('HE Niaouli', '6 500'),
            ('HE Menthe Poivrée', '6 500'),
            ('HE Origan', '7 000'),
            ('HE Mandarine', '5 500'),
            ('HE Orange Douce', '5 000'),
            ('HE Palmarosa', '8 500'),
            ('HE Myrrhe', '12 000'),
            ('HE Muscade', '6 500'),
            ('Pack les 5 indispensables', '24 000'),
        ]),
        ('Synergies aromatiques', [
            ('Senteur Ambiance de Noël', '4 500'),
            ('Senteur Concentrate', '4 500'),
            ('Senteur Cozy Cloud', '4 500'),
        ]),
        ('Diffuseurs', [
            ('Diffuseur à bâton', '1 500'),
            ('Diffuseur terre cuite', '7 000'),
            ('Diffuseur électrique', '20 000'),
        ]),
        ('Inhalateurs', [
            ('AVITI · inhalateur', '1 000'),
            ("MEMO'S", None),
        ]),
    ]
) + cat_section('02', '05', 'huiles-argiles',
    'Huiles, beurres &amp; <em>argiles</em>.',
    "Hydratent, nourrissent, réparent et protègent. Argiles purifiantes, beurres végétaux, macérats.",
    [
        ('Huiles végétales', [
            ('HV Amande douce', '3 500'),
            ('HV Argan', '5 000'),
            ('HV Coco', '3 000'),
        ]),
        ('Macérats huileux', [
            ('HV Akpi', '3 500'),
            ('HV Aloe-Vera', '3 500'),
            ('HV anti-moustique', '3 000'),
        ]),
        ('Huiles de massage', [
            ('HV amaigrissant', '4 000'),
            ('HV aphrodisiaque', '4 000'),
            ('HV détente', '4 000'),
        ]),
        ('Beurres végétaux', [
            ('Beurre de karité', '2 500'),
            ('Beurre de cacao', '4 000'),
            ('Baume anti-rhumatisme', '2 000'),
        ]),
        ('Argiles &amp; sels', [
            ('Argile Verte concassée', '2 500'),
            ('Argile Verte en poudre', '3 000'),
            ('Argile Blanche en poudre', '3 000'),
        ]),
    ]
) + cat_section('03', '05', 'phytotherapie',
    'Phytothérapie<em>.</em>',
    "La sagesse des plantes du Bénin : tisanes, poudres, teintures-mères, eaux florales.",
    [
        ('Tisanes &amp; thés', [
            ('Tisane Artemisia', '2 500'),
            ('Tisane Eucalyptus', '2 500'),
            ("Tisane L'autre balai", '2 500'),
        ]),
        ('Poudres', [
            ('Poudre de Cannelle', '3 000'),
            ('Poudre de Chébé', '2 000'),
            ('Poudre de Clou de Girofle', '3 000'),
        ]),
        ('Eaux florales', [
            ('Eau noble Niaouli', '250'),
            ('Eau noble Tchayo', '250'),
        ]),
        ('Jus &amp; teintures', [
            ('Jus de Noni', '3 000'),
            ('Teintures mères', None),
        ]),
    ]
) + cat_section('04', '05', 'apitherapie',
    'Apithérapie<em>.</em>',
    "Soins par les produits de la ruche. Énergie, immunité, vitalité.",
    [
        ('Miel pur', [
            ('Miel pur 100 % naturel', '3 000'),
        ]),
        ('Miels aromatisés', [
            ('Miel Agrumes', '2 000'),
            ('Miel Basilic-Romarin', '2 000'),
            ('Miel Citron', '2 000'),
            ('Miel Citronnelle', '2 000'),
            ('Miel Eucalyptus', '2 000'),
            ('Miel Gingembre', '2 500'),
        ]),
    ]
) + cat_section('05', '05', 'hygiene',
    'Hygiène &amp; <em>cosmétique</em>.',
    "Soins quotidiens 100 % naturels pour le corps, le visage et les cheveux.",
    [
        ('Crèmes fouettées', [
            ('Crème café-vanille', '2 500'),
            ('Crème citronnelle', '2 500'),
            ('Crème eucalyptus', '2 500'),
        ]),
        ('Bientôt disponible', [
            ('Savons artisanaux', None),
            ('Hygiène bucco-dentaire', None),
            ('Produits cheveux', None),
            ('Maquillage', None),
        ]),
    ]
) + """
</div>

<script>
document.querySelectorAll('.mini-card').forEach(card => {
  if (!card.dataset.price) return;
  card.querySelectorAll('.add-mini').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      window.OYAYI && window.OYAYI.addToCart({
        id: card.dataset.id,
        name: card.dataset.name,
        price: card.dataset.price,
        image: card.dataset.image || ''
      });
    });
  });
  card.addEventListener('click', () => {
    window.OYAYI && window.OYAYI.addToCart({
      id: card.dataset.id,
      name: card.dataset.name,
      price: card.dataset.price,
      image: card.dataset.image || ''
    });
  });
});
</script>
"""

# ============================================================
# BLOG
# ============================================================
ARTICLES = [
    ('comment-les-huiles-essentielles-peuvent-ameliorer-la-qualite-du-sommeil',
     "Comment ces produits peuvent améliorer la qualité du sommeil ?",
     "Conseils", "septembre 2025",
     "Un sommeil de qualité est essentiel pour préserver la santé physique, mentale et émotionnelle. Pourtant, stress, anxiété et écrans perturbent nos nuits. Découvrez comment lavande, néroli et mandarine peuvent transformer vos rituels du soir."),
    ('pourquoi-eviter-de-melanger-trop-tot-ses-huiles-essentielles',
     "Pourquoi éviter de mélanger trop tôt ses huiles essentielles ?",
     "Conseils", "septembre 2025",
     "Les huiles essentielles sont de puissants concentrés de plantes, offrant des parfums envoûtants et des propriétés thérapeutiques variées. Mais comment les associer sans casser leurs équilibres olfactifs et chimiques ?"),
    ('les-huiles-essentielles-dans-la-pratique-du-yoga',
     "Les huiles essentielles dans la pratique du yoga",
     "Conseils", "septembre 2025",
     "Le yoga est bien plus qu'une simple activité physique : c'est un art de vivre qui harmonise le corps, le souffle et l'esprit. Les huiles essentielles peuvent enrichir cette pratique sur tous les plans."),
    ('comment-conserver-et-stocker-correctement-ses-huiles-essentielles',
     "Comment conserver et stocker correctement ses huiles essentielles ?",
     "Conseils", "septembre 2025",
     "Les huiles essentielles sont de véritables trésors de la nature, concentrant les bienfaits et parfums des plantes. Mais leur conservation conditionne directement leur efficacité et leur durée de vie."),
    ('les-erreurs-a-eviter-avec-les-huiles-essentielles',
     "Les erreurs à éviter avec les huiles essentielles",
     "Conseils", "septembre 2025",
     "Les huiles essentielles sont de véritables trésors. Leur parfum envoûtant et leurs multiples bienfaits en font des alliées précieuses, à condition de respecter quelques règles fondamentales."),
    ('bienfaits-des-huiles-essentielles-sur-le-stress-et-lanxiete',
     "Bienfaits des huiles essentielles sur le stress et l'anxiété",
     "Conseils", "septembre 2025",
     "Dans notre quotidien moderne, le stress et l'anxiété sont devenus des compagnons fréquents, parfois invisibles mais toujours présents. Les huiles essentielles offrent une réponse douce et efficace."),
]

ICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 12h6l3-9 6 18 3-9h0"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8 4v16M16 4v16M4 12h16"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="m12 2 3 7h7l-5.5 4.5L18 22l-6-4-6 4 1.5-8.5L2 9h7z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12z"/></svg>',
]

cards_html = '\n'.join(
    f'''    <article class="blog-card" data-href="{slug}">
      <div class="cover">{ICONS[i % len(ICONS)]}</div>
      <div class="meta"><span class="cat">{cat}</span><span>{date}</span></div>
      <h3>{title}</h3>
      <p class="excerpt">{excerpt}</p>
      <div class="read">Lire l'article →</div>
    </article>'''
    for i, (slug, title, cat, date, excerpt) in enumerate(ARTICLES)
)

from _articles_data import ARTICLES as REAL_ARTICLES

cards_html_local = '\n'.join(
    f'''    <a class="blog-card" href="article-{a['slug']}.html" style="text-decoration:none">
      <div class="cover">{ICONS[i % len(ICONS)]}</div>
      <div class="meta"><span class="cat">{a['cat']}</span><span>{a['date']} · {a['read']}</span></div>
      <h3>{a['title']}</h3>
      <p class="excerpt">{a['lede']}</p>
      <div class="read">Lire l'article →</div>
    </a>'''
    for i, a in enumerate(REAL_ARTICLES)
)

BLOG_BODY = f"""
<section class="page-hero">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // Conseils</div>
    <h1>Notre <em>blog</em>,<br/>nos conseils.</h1>
    <p class="lead">Le pouvoir des huiles essentielles au quotidien : comment la nature soigne et équilibre notre bien-être. Six articles pour aller plus loin.</p>
  </div>
</section>

<section class="section">
  <div class="sec-head"><div>
    <div class="sec-tag">// 6 articles · Conseils naturels</div>
    <h2 class="sec-title">Le pouvoir des plantes,<br/>au quotidien.</h2>
  </div></div>
  <div class="blog-grid">
{cards_html_local}
  </div>
</section>
"""

# ============================================================
# CART PAGE — wraps a script tag that uses safe DOM API
# ============================================================
PANIER_BODY = """
<section class="page-hero" style="padding-bottom:40px">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // Panier</div>
    <h1>Votre <em>panier</em>.</h1>
  </div>
</section>

<section class="section" id="cartSection" style="padding-top:30px">
  <div id="cartContent"></div>
</section>

<script src="assets/js/panier.js"></script>
"""

# ============================================================
# CHECKOUT PAGE — wraps the safe paiement.js
# ============================================================
PAIEMENT_BODY = """
<section class="page-hero" style="padding-bottom:40px">
  <div class="theme-bg"></div>
  <div class="grain"></div>
  <div class="page-hero-inner">
    <div class="crumbs"><a href="index.html">Accueil</a> // <a href="panier.html">Panier</a> // Paiement</div>
    <h1><em>Paiement</em> sécurisé.</h1>
  </div>
</section>

<section class="section" style="padding-top:30px" id="checkoutWrap">
  <div id="checkoutContent"></div>
</section>

<script src="assets/js/paiement.js"></script>
"""

# ============================================================
# ARTICLE PAGE (one per article)
# ============================================================
def article_body(a, prev_a, next_a):
    related = ''
    for other in [prev_a, next_a]:
        if other:
            related += f'''      <a class="blog-card" href="article-{other['slug']}.html" style="text-decoration:none">
        <div class="cover">{ICONS[0]}</div>
        <div class="meta"><span class="cat">{other['cat']}</span><span>{other['read']}</span></div>
        <h3>{other['title']}</h3>
        <p class="excerpt">{other['lede']}</p>
        <div class="read">Lire l'article →</div>
      </a>'''
    return f"""
<article>
  <div class="article-hero">
    <div class="theme-bg" style="position:absolute;inset:0;z-index:-2;background:radial-gradient(ellipse 80% 70% at 50% 30%,color-mix(in oklab,var(--accent) 18%,transparent),transparent 65%),linear-gradient(180deg,var(--bg-deep) 0%,color-mix(in oklab,var(--bg-deep) 60%,var(--accent-2)) 50%,var(--bg-deep) 100%)"></div>
    <div class="meta-row"><span class="cat">{a['cat']}</span><span>{a['date']}</span><span>· {a['read']} de lecture</span></div>
    <h1>{a['title']}</h1>
    <p class="lede">{a['lede']}</p>
    <div class="article-cover"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12z"/></svg></div>
  </div>

  <div class="article-body">
{a['body']}
  </div>

  <div class="article-foot">
    <a href="blog.html" class="back">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5m6 6-6-6 6-6"/></svg>
      Retour aux articles
    </a>
    <div class="share">
      <a href="#" aria-label="Partager Facebook" onclick="window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(location.href),'_blank','noopener,width=600,height=500');return false;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.5 9.9v-7H8V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.5 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg></a>
      <a href="#" aria-label="Partager X" onclick="window.open('https://twitter.com/intent/tweet?url='+encodeURIComponent(location.href)+'&amp;text='+encodeURIComponent(document.title),'_blank','noopener,width=600,height=500');return false;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18 3h3l-7.5 8.6L22 21h-6.8l-5-6.5L4 21H1l8-9.2L1.5 3H8.5l4.5 6 5-6z"/></svg></a>
      <a href="#" aria-label="Partager WhatsApp" onclick="window.open('https://wa.me/?text='+encodeURIComponent(document.title+' '+location.href),'_blank','noopener');return false;"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5-1.4A10 10 0 1 0 12 2zm5 14c-.2.7-1.4 1.4-2 1.4-1 .1-2.2.5-7-1.6-2.5-1-4.6-3.7-4.7-3.9-.2-.2-1.1-1.5-1.1-2.9 0-1.4.7-2 1-2.3.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.4.2.5.7 1.7.7 1.8.1.2.1.3 0 .5l-.3.5-.3.4-.4.4c-.1.2-.3.3-.1.6 0 .3.7 1.5 1.7 2.4 1.3 1.1 2.4 1.5 2.7 1.7.3.1.5.1.7-.1l.7-.8c.2-.3.5-.2.7-.1.3.1 1.7.8 2 1l.4.2c.1.2.1.5 0 1z"/></svg></a>
    </div>
  </div>
</article>

<section class="related-articles">
  <h3>Continuer la lecture</h3>
  <div class="blog-grid">
{related}
  </div>
</section>
"""

# ============================================================
# WRITE PAGES
# ============================================================
PAGES = [
    ('a-propos.html',       "OYAYI Nature — À propos · Notre histoire, vision, mission",                      "L'histoire d'OYAYI Nature, maison béninoise d'huiles essentielles. Vision, mission, valeurs et distinctions.", 'a-propos.html',       APROPOS_BODY),
    ('contacts.html',       "OYAYI Nature — Contacts · Cotonou Ganhi · +229 0196627168",                       "Contactez OYAYI Nature à Cotonou (Ganhi). Téléphone, email, formulaire et localisation Google Maps.",            'contacts.html',       CONTACTS_BODY),
    ('coffrets-packs.html', "OYAYI Nature — Coffrets &amp; Packs bien-être",                                   "Coffrets d'huiles essentielles, coffret de miel et 5 packs thématiques (détente, sommeil, antidouleur…).",      'coffrets-packs.html', COFFRETS_BODY),
    ('produits.html',       "OYAYI Nature — Catalogue complet · 5 univers de soin naturel",                    "Catalogue OYAYI Nature : huiles essentielles, miels, argiles, tisanes, beurres, crèmes. 100 % Bénin.",          'produits.html',       PRODUITS_BODY),
    ('blog.html',           "OYAYI Nature — Conseils &amp; Journal · Les huiles essentielles au quotidien",    "Six articles pour mieux comprendre les huiles essentielles : sommeil, stress, yoga, conservation, erreurs.",     'blog.html',           BLOG_BODY),
    ('panier.html',         "OYAYI Nature — Votre panier",                                                     "Votre panier OYAYI Nature. Modifier, supprimer, passer au paiement.",                                            'panier.html',         PANIER_BODY),
    ('paiement.html',       "OYAYI Nature — Paiement sécurisé",                                                "Paiement sécurisé OYAYI Nature : Mobile Money, paiement à la livraison ou carte bancaire.",                      'paiement.html',       PAIEMENT_BODY),
]

# Add one page per blog article
for i, a in enumerate(REAL_ARTICLES):
    prev_a = REAL_ARTICLES[(i-1) % len(REAL_ARTICLES)]
    next_a = REAL_ARTICLES[(i+1) % len(REAL_ARTICLES)]
    fname = f"article-{a['slug']}.html"
    title = f"OYAYI Nature — {a['title']}"
    desc = a['lede'][:160]
    PAGES.append((fname, title, desc, 'blog.html', article_body(a, prev_a, next_a)))

for fname, title, desc, active, body in PAGES:
    out = page_shell(title, desc, active, body)
    with open(os.path.join(OUT_DIR, fname), 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
    print(f'  wrote {fname:30s}  {len(out):>6} chars')
print(f'Done. {len(PAGES)} pages generated.')
