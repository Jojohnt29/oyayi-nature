# -*- coding: utf-8 -*-
"""Mark specific sections as .surface-cream across pages so the OYAYI
ivoire palette breaks the green and brings the full charter to life."""

import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def patch_file(path, replacements):
    full = os.path.join(ROOT, path)
    if not os.path.exists(full): return
    with open(full, 'r', encoding='utf-8') as f: c = f.read()
    n = 0
    for old, new in replacements:
        if old in c and new not in c:
            c = c.replace(old, new)
            n += 1
    with open(full, 'w', encoding='utf-8', newline='\n') as f: f.write(c)
    return n

# index.html — Best-sellers + Testimonials get cream
patches_index = [
    ('<section class="section" id="bestsellers">', '<section class="section surface-cream" id="bestsellers">'),
    ('<section class="section" id="avis"', '<section class="section surface-cream" id="avis"'),
]
n = patch_file('index.html', patches_index)
print(f'index.html : {n} sections marked .surface-cream')

# blog.html — entire grid section
patches_blog = [
    ('<section class="section">\n  <div class="sec-head"><div>\n    <div class="sec-tag">// 6 articles', '<section class="section surface-cream">\n  <div class="sec-head"><div>\n    <div class="sec-tag">// 6 articles'),
]
n = patch_file('blog.html', patches_blog)
print(f'blog.html  : {n} sections marked .surface-cream')

# Article pages — wrap article-body in cream
for slug in ['sommeil','melanges','yoga','conservation','erreurs','stress']:
    fname = f'article-{slug}.html'
    full = os.path.join(ROOT, fname)
    if not os.path.exists(full): continue
    with open(full, 'r', encoding='utf-8') as f: c = f.read()
    if 'surface-cream' not in c:
        # Wrap article body + foot + related-articles in a cream container
        c = c.replace(
            '<div class="article-body">',
            '<div class="surface-cream" style="padding-top:60px;padding-bottom:60px"><div class="article-body">'
        )
        c = c.replace(
            '</section>\n\n<section class="section">',
            '</div></section>\n\n<section class="section">'
        )
        # Close the cream wrapper after .related-articles
        c = c.replace(
            '</section>\n\n<section class="section">\n  <div class="newsletter">',
            '</section>\n</div>\n\n<section class="section">\n  <div class="newsletter">'
        )
        with open(full, 'w', encoding='utf-8', newline='\n') as f: f.write(c)
        print(f'article-{slug}.html: cream wrapper added')

# produits.html — entire catalogue area cream
patches_produits = [
    ('<div class="section" style="padding-top:0;padding-bottom:0">', '<div class="section surface-cream" style="padding-top:0;padding-bottom:0">'),
]
n = patch_file('produits.html', patches_produits)
print(f'produits.html: {n} sections marked .surface-cream')

# panier.html — full cart section cream
patches_panier = [
    ('<section class="section" id="cartSection" style="padding-top:30px">', '<section class="section surface-cream" id="cartSection" style="padding-top:30px">'),
]
n = patch_file('panier.html', patches_panier)
print(f'panier.html  : {n} sections marked .surface-cream')

# paiement.html — full checkout section cream
patches_paiement = [
    ('<section class="section" style="padding-top:30px" id="checkoutWrap">', '<section class="section surface-cream" style="padding-top:30px" id="checkoutWrap">'),
]
n = patch_file('paiement.html', patches_paiement)
print(f'paiement.html: {n} sections marked .surface-cream')

# coffrets-packs.html — both coffrets and packs sections cream
patches_coffrets = [
    ('<section class="section" id="coffrets">', '<section class="section surface-cream" id="coffrets">'),
    ('<section class="section" id="packs">', '<section class="section surface-cream" id="packs">'),
]
n = patch_file('coffrets-packs.html', patches_coffrets)
print(f'coffrets-packs.html: {n} sections marked .surface-cream')

# a-propos.html — distinctions + témoignages get cream
patches_apropos = [
    ('<section class="section" id="distinctions">', '<section class="section surface-cream" id="distinctions">'),
    ('<section class="section" id="avis">', '<section class="section surface-cream" id="avis">'),
]
n = patch_file('a-propos.html', patches_apropos)
print(f'a-propos.html: {n} sections marked .surface-cream')

# contacts.html — main grid section cream (formulaire + maps)
patches_contacts = [
    ('<section class="section">\n  <div class="contact-grid">', '<section class="section surface-cream">\n  <div class="contact-grid">'),
]
n = patch_file('contacts.html', patches_contacts)
print(f'contacts.html: {n} sections marked .surface-cream')

print('\nDone.')
