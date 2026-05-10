# -*- coding: utf-8 -*-
"""Download all OYAYI product/distinction images in parallel and rename them
into a clean local layout under assets/."""

import os, sys, io, urllib.request, urllib.error, ssl, concurrent.futures, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://oyayinature.com/wp-content/uploads/'

# (url_path, dest_relative_path)
JOBS = [
    # ------- Distinctions (À propos gallery) -------
    ('2025/09/7R508739.jpg',                       'assets/distinctions/01.jpg'),
    ('2025/09/7R508752-e1758818064963.jpg',        'assets/distinctions/02.jpg'),
    ('2025/09/7R508749.jpg',                       'assets/distinctions/03.jpg'),
    ('2025/09/7R508748.jpg',                       'assets/distinctions/04.jpg'),
    ('2025/09/7R508763-1.jpg',                     'assets/distinctions/05.jpg'),
    ('2025/09/7R508756.jpg',                       'assets/distinctions/06.jpg'),
    ('2025/09/7R508746.jpg',                       'assets/distinctions/07.jpg'),
    ('2025/09/7R508741.jpg',                       'assets/distinctions/08.jpg'),

    # ------- Huiles essentielles (vrais produits) -------
    ('2025/09/TCHAYO-BASILIC-100ml-819x1024.png',  'assets/catalog/he-tchayo.png'),
    ('2025/10/AIL-100ml-818x1024.png',             'assets/catalog/he-ail.png'),
    ('2025/10/BASILIC-100ml-819x1024.png',         'assets/catalog/he-basilic.png'),

    # ------- Diffuseurs / Inhalateurs -------
    ('2025/08/7R508541-819x1024.jpg',              'assets/catalog/diffuseur-terre-cuite.jpg'),
    ('2025/10/7R508495__.png',                     'assets/catalog/diffuseur-electrique.png'),
    ('2025/10/OYA_com_soo_2.png',                  'assets/catalog/diffuseur-baton.png'),
    ('2025/10/AVITI_2_.png',                       'assets/catalog/aviti.png'),
    ('2025/08/7R508728_1-1-1-150x150.jpg',         'assets/catalog/inhalateurs-cover.jpg'),
    ('2025/08/7R508495-sqr-scaled.jpg',            'assets/catalog/diffuseurs-cover.jpg'),

    # ------- Miels -------
    ('2025/10/MIEL-GINGEMBRE_-819x1024.png',       'assets/catalog/miel-gingembre.png'),
    ('2025/10/MIEL-CITRON_-818x1024.png',          'assets/catalog/miel-citron.png'),
    ('2025/10/MIEL-CITRONELLE_-819x1024.png',      'assets/catalog/miel-citronnelle.png'),
    ('2025/10/MIEL-EUCALYPTYS1_-819x1024.png',     'assets/catalog/miel-eucalyptus.png'),
    ('2025/10/MIEL-ARGUMES_-818x1024.png',         'assets/catalog/miel-agrumes.png'),
    ('2025/08/2151705786-150x150.jpg',             'assets/catalog/miel-pur-cover.jpg'),
    ('2025/08/7R508705-150x150.jpg',               'assets/catalog/miels-aromatises-cover.jpg'),

    # ------- Poudres / Tisanes -------
    ('2025/10/POUDRE-DE-CANNELLE_-818x1024.png',   'assets/catalog/poudre-cannelle.png'),
    ('2025/10/POUDRE-DE-CHEBE_-819x1024.png',      'assets/catalog/poudre-chebe.png'),
    ('2025/10/Poudre-Clou-de-Girofle_-819x1024.png','assets/catalog/poudre-girofle.png'),
    ('2025/10/Poudre-Clou-de-Girofle_-150x150.png', 'assets/catalog/poudres-cover.png'),
    ('2025/10/LAUTRE-BALAI_-150x150.png',          'assets/catalog/tisane-cover.png'),

    # ------- Argiles / HV / Beurres / Macérats / Massages -------
    ('2025/08/ARGILE-BLANCE-EN-POUDRE_-819x1024.jpg','assets/catalog/argile-blanche.jpg'),
    ('2025/08/ARGILE-BLANCE-EN-POUDRE_-150x150.jpg', 'assets/catalog/argiles-cover.jpg'),
    ('2025/08/ENSEMBLE-HUILE-VEGETAL_sqr-150x150.jpg','assets/catalog/hv-cover.jpg'),
    ('2025/09/7R508572-e1757165048533-150x150.jpg', 'assets/catalog/macerats-cover.jpg'),
    ('2025/08/7R508665-150x150.jpg',               'assets/catalog/massages-cover.jpg'),
    ('2025/08/123103035_whatsubject-sqr-150x150.jpg','assets/catalog/beurres-cover.jpg'),

    # ------- Synergies / Packs / Eaux / Jus -------
    ('2025/09/ENSEMBLE-HUILE-6-150x150.jpg',       'assets/catalog/synergies-cover.jpg'),
    ('2025/09/Pack_les_5_indispensables-150x150.jpg','assets/catalog/pack-5-indispensables.jpg'),
    ('2025/08/eaux_florales-150x150.jpg',          'assets/catalog/eaux-florales-cover.jpg'),
    ('2025/08/teintures_meres-150x150.jpg',        'assets/catalog/teintures-cover.jpg'),
    ('2025/08/noni_sqr-150x150.jpg',               'assets/catalog/jus-noni.jpg'),

    # ------- Hygiène & Cosmétique covers -------
    ('2025/08/2151401433-150x150.jpg',             'assets/catalog/cremes-cover.jpg'),
    ('2025/08/2150533352-150x150.jpg',             'assets/catalog/savons-cover.jpg'),
    ('2025/08/7R508660_1-sqr-scaled.jpg',          'assets/catalog/bucco-dentaire-cover.jpg'),
    ('2025/08/2151382828-150x150.jpg',             'assets/catalog/cheveux-cover.jpg'),
    ('2025/08/2147878880-150x150.jpg',             'assets/catalog/maquillage-cover.jpg'),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Pretend to be a normal browser — Wordfence sometimes blocks Python UA
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Referer':    'https://oyayinature.com/',
    'Accept':     'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
}

def fetch(job):
    url_path, dest_rel = job
    url = BASE + url_path
    dest = os.path.join(ROOT, dest_rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 1024:
        return (dest_rel, 'CACHED', os.path.getsize(dest))
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            data = r.read()
        with open(dest, 'wb') as f:
            f.write(data)
        return (dest_rel, 'OK', len(data))
    except Exception as e:
        return (dest_rel, 'ERR', str(e)[:60])

start = time.time()
ok = err = cached = 0
total_bytes = 0

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    for dest_rel, status, info in pool.map(fetch, JOBS):
        if status == 'OK':
            ok += 1; total_bytes += info
            print(f'  OK     {dest_rel:48s} {info//1024} KB')
        elif status == 'CACHED':
            cached += 1; total_bytes += info
            print(f'  cache  {dest_rel:48s} {info//1024} KB')
        else:
            err += 1
            print(f'  ERR    {dest_rel:48s} {info}')

elapsed = time.time() - start
print(f'\nDone. {ok} downloaded, {cached} cached, {err} errors. {total_bytes//1024} KB total in {elapsed:.1f}s.')
