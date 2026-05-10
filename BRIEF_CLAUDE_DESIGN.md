# Brief design — Harmonisation chromatique du site OYAYI Nature

> **À transmettre à Claude Design (ou autre agent UI/UX)** pour qu'il propose une harmonisation polie respectant la charte graphique OYAYI Sens, en intégrant intelligemment l'ivoire et le vert sans alternance brutale.

---

## 1. Contexte de la marque

- **Marque** : OYAYI Cosmétique Naturelle — Huiles Essentielles du Bénin
- **Site en production** : https://oyayi-nature.vercel.app
- **Repo GitHub** : https://github.com/Jojohnt29/oyayi-nature
- **Identité** : maison béninoise (Cotonou · Ganhi) d'huiles essentielles 100 % pures, miels aromatisés, beurres végétaux, argiles, tisanes — produits naturels haut de gamme
- **Téléphone** : +229 0196627168 / 0143965339
- **Tagline** : *Soigner autrement, produire localement, et impacter durablement.*
- **Cible** : femmes 25-55 ans, urbaines, sensibles au naturel et au local africain

---

## 2. Charte graphique officielle

> Source : `OYAYI_Sens_Flyer_Commercial_EuniceSoglohoun.html` (flyer commercial Eunice Soglohoun)

### Palette

| Token | Hex | Rôle |
|---|---|---|
| **Vert primaire** | `#1B5E20` | Couleur dominante de la marque |
| **Vert moyen** | `#2E7D32` | Variation un cran plus claire |
| **Vert très clair** | `#E8F5E9` | Fond léger, pour contrastes doux |
| **Or (accent)** | `#C8A84B` | Signature accent — boutons, badges, prix |
| **Or clair** | `#FFF8E1` | Fond ambré subtil, halo |
| **Ivoire** | `#FAFAF7` | Fond clair / texte sur fond foncé |
| **Vert pâle** | `#A5D6A7` | Vert nature secondaire |
| **Noir** | `#1A1A1A` | Texte sur fond clair |
| **Blanc pur** | `#FFFFFF` | Surfaces neutres |
| **Gris** | `#555555` | Texte secondaire |

### Typographie officielle

- **Display (titres)** : `Playfair Display` (serif italique pour les emphases)
- **Body (texte)** : `DM Sans` (sans-serif géométrique propre)
- **Mono (technique)** : `JetBrains Mono` (étiquettes, prix, métadonnées)

### Référence flyer

Le flyer original (recto A5 paysage) utilise :
- **Colonne gauche (280 px)** : fond vert `#1B5E20` plein, marque OYAYI Playfair blanche, badge or
- **Colonne droite (1fr)** : fond ivoire `#FAFAF7`, titres vert, accents or italiques

Le flyer **alterne en colonnes**, pas en bandes horizontales empilées.

---

## 3. État actuel à harmoniser

### V1 — Pure charte (état actuel après revert)

**Branche live** : `main` — déployé sur https://oyayi-nature.vercel.app

- Page bg = `#1B5E20` (vert brand pur)
- Cards = `#164C1A` (vert un cran plus sombre)
- Footer = `#0F3712` (vert très profond)
- Texte = ivoire `#FAFAF7`
- Accents = or `#C8A84B`

**Critique du client** : *« il manque beaucoup de blanc »* — la page est trop monochromatique vert, sature visuellement, manque de respiration.

### V2 — Avec alternance vert/ivoire (rejetée)

**Branche backup** : `backup-with-alternation` — disponible sur GitHub

J'ai introduit une classe `.surface-cream` qui flippe certaines sections en ivoire `#FAFAF7` avec texte noir `#1A1A1A` :

| Page | Sections crémées |
|---|---|
| Accueil | Best-sellers, Témoignages |
| À propos | Galerie distinctions, 16 témoignages |
| Produits | Catalogue complet |
| Coffrets & Packs | Les 7 packs |
| Contacts | Formulaire + Maps |
| Panier / Paiement | Tableau + résumé |
| Blog | Grille articles |
| Articles | Body de lecture |

**Critique du client** : *« je trouve l'alternance de vert et blanc très vilain »* — le rythme zebra-stripes vert/blanc/vert/blanc est trop brutal, peu élégant, donne l'impression d'un site mal cousu.

### Pourquoi V1 et V2 ne marchent ni l'un ni l'autre

- **V1** : conforme à la charte mais trop saturé vert → fatigue oculaire, manque de hiérarchie
- **V2** : apporte du blanc mais l'opposition est trop dure → casse la cohésion, semble bricolé

---

## 4. Demande au designer

Proposer une harmonisation chromatique élégante qui **respecte la charte OYAYI Sens** ET **équilibre visuellement** vert + ivoire + or, sans tomber dans :

- Le vert massif monochrome (V1)
- L'alternance brutale en bandes vert/blanc/vert/blanc (V2)

### Pistes à explorer

1. **Vert dégradé en fond** — du `#1B5E20` au sommet vers un vert très sombre presque noir en bas (ou inversement) → la page n'est plus mat
2. **Cards crémées subtiles** — au lieu de sections ivoire pleine largeur, faire les **cards** légèrement crémées (`rgba(250,250,247,0.04)` à `0.10`) sur fond vert → les cards "respirent" sans casser la couleur dominante
3. **Texture organique** — overlay subtil de feuillage SVG ou bruit végétal sur le vert pour donner de la matière (cosmétique nature ≠ vert plat)
4. **Hero ivoire en colonne, pas en bande** — récupérer le pattern du flyer : colonne gauche verte (visuel) + colonne droite ivoire (texte) sur certains hero ou sections story
5. **Or pour structurer** — bordures or fines `1px` pour délimiter les blocs sans trancher avec du blanc ; les blocs n'ont pas besoin de fond contrastant, juste d'une **frontière dorée**
6. **Verts modulés** — utiliser le vert `#2E7D32` (medium) et le vert `#A5D6A7` (pâle) comme variations au sein du même monochrome → richesse de greens plutôt qu'opposition vert/blanc
7. **Sections "open"** — pour le catalogue et les articles, fond ivoire mais transition graduelle (gradient de bandes 200 px de fade vert → ivoire → vert) plutôt que coupure nette
8. **Inspiration** : Aesop, Tata Harper, La Bouche Rouge, Goop — sites cosmétiques qui assument un fond couleur sans saturation et utilisent le blanc comme "encre" lumineuse

### Contraintes à respecter

- ✅ Garder les polices Playfair Display + DM Sans (commande client confirmée)
- ✅ Garder l'or `#C8A84B` comme accent unique
- ✅ Garder le système de cards déjà conçu (mini-card, pcard, pack, blog-card, etc.)
- ✅ Garder les composants déjà en place (carousel, panier drawer, FAQ, formulaires)
- ✅ Maintenir compatibilité responsive 1280 / 1024 / 768 / 480
- ✅ WCAG AA minimum sur tous les contrastes texte
- ✅ Préserver le toggle thème vert/brun (deux palettes coexistent)
- ❌ Pas de redesign structurel — juste une couche chromatique
- ❌ Pas de nouvelles polices
- ❌ Pas d'images de fond (sauf SVG vectoriels légers)

### Output attendu

1. **Patch CSS chirurgical** à appliquer sur `assets/css/oyayi.css` (ou un fichier additionnel `oyayi-harmonization.css`)
2. **Justification UX** courte de chaque choix (1-2 phrases par règle)
3. **Mockup** ou description verbale détaillée du résultat sur 3 sections clés :
   - Hero accueil
   - Catalogue produits
   - Article de blog
4. **Liste des sections** où la palette ivoire doit pénétrer (et comment)

---

## 5. Ressources disponibles

### Fichiers à consulter dans le repo

| Fichier | Rôle |
|---|---|
| `OYAYI_Sens_Flyer_Commercial_EuniceSoglohoun.html` | **Flyer source** (charte de référence visuelle) |
| `assets/css/oyayi.css` | CSS unique 84 KB — palette, composants, responsive, surface-cream désactivé |
| `index.html` | Accueil — hero carousel, 5 univers, collection 13 huiles, story, témoignages, FAQ |
| `produits.html` | Catalogue 5 univers, ~50 références, mini-cards |
| `coffrets-packs.html` | 2 coffrets + 5 packs |
| `a-propos.html` | Histoire, vision, mission, valeurs, distinctions, 16 témoignages |
| `contacts.html` | Formulaire + Google Maps Cotonou |
| `blog.html` + `article-*.html` | 6 articles long-form |
| `panier.html` + `paiement.html` | Tunnel d'achat (panier + paiement Mobile Money/Carte/Cash) |

### Comment récupérer les deux états

```bash
# État actuel (V1 — pur charte vert)
git clone https://github.com/Jojohnt29/oyayi-nature
cd oyayi-nature

# Pour voir l'alternance V2 (rejetée)
git checkout backup-with-alternation
# revoir le diff: git diff main backup-with-alternation -- "*.html" "assets/css/oyayi.css"
```

### Captures d'écran à fournir

Le client a partagé une capture du rendu actuel sur la page **Nos produits / Diffuseurs** où le vert sature visuellement. Sur mobile Android, la lecture de longues sections vertes est inconfortable.

---

## 6. Questions ouvertes pour le designer

1. **Faut-il une vraie inversion de page** sur certaines pages (catalogue, articles) pour passer en thème clair (ivoire dominant + vert accent), tout en gardant accueil/à propos en vert dominant ? Cela respecte le pattern flyer (vert pour la "vitrine", ivoire pour le "contenu utile").

2. **Faut-il enrichir la palette** avec un vert intermédiaire (`#2E7D32` ou `#A5D6A7`) pour créer 3-4 nuances de vert plutôt qu'une opposition vert/blanc binaire ?

3. **Le toggle thème vert/brun** doit-il rester ou être remplacé par un toggle clair/sombre du thème vert (light = ivoire dominant, dark = vert dominant) ? Le brun n'est pas dans la charte officielle mais avait été demandé en V0.

4. **Densité visuelle** : les pages sont-elles trop denses ? Faut-il aérer (plus de padding vertical entre sections) avant même de toucher aux couleurs ?

---

## 7. Validation finale par le client

Le client (commanditaire OYAYI) attend une proposition qui se sente **luxe accessible, naturel, féminin sans être mièvre, ancré dans la terre béninoise**. Pas trop "pharma", pas trop "spa générique", pas trop "Instagram pastel". Une élégance discrète, professionnelle, avec le caractère du Bénin (chaleur, terre, soleil).

---

*Brief généré le 11 mai 2025 — état du projet : commit `bceb9ee` (avec alternance backupé sur branche `backup-with-alternation`), commit en cours pour le revert charter pur sur `main`.*
