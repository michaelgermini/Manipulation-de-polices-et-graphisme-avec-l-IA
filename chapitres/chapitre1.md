# Chapitre 1 — Principes fondamentaux de la typographie

Avant de plonger dans les applications de l'IA pour la typographie, il est essentiel de maîtriser les principes fondamentaux qui guident la création et l'utilisation des polices. Ce chapitre pose les bases théoriques nécessaires pour comprendre comment l'IA peut assister et améliorer le travail typographique traditionnel.

## Anatomie d'une lettre

La compréhension de l'anatomie des caractères est fondamentale pour analyser, créer et modifier des polices de manière efficace.

### Structure générale d'un glyphe

#### **Lignes de référence**
```
  Ascender line ──┐
                   │ Cap height
  Cap line ───────┼─ H, I, M (majuscules)
                   │
  Mean line ──────┼─ x, a, e (hauteur d'x)
                   │ X-height
  Baseline ───────┼─ base des caractères
                   │
                   │ Descender
  Descender line ─┘
```

#### **Éléments dimensionnels**
- **Hauteur d'x (X-height)** : distance entre baseline et mean line
- **Hauteur des capitales** : distance entre baseline et cap line
- **Hauteur des ascendantes** : dépassement des lettres comme b, d, h
- **Profondeur des descendantes** : descente des lettres comme p, q, y

### Classification par empattement

#### **Polices avec serif (empattement)**
- **Old Style** : Garamond, Bembo - empattements obliques, contraste modéré
- **Transitional** : Times New Roman, Baskerville - contraste plus marqué
- **Didone/Modern** : Bodoni, Didot - contraste extrême, empattements fins
- **Slab Serif** : Rockwell, Clarendon - empattements épais, rectangulaires

#### **Polices sans serif**
- **Grotesque** : Helvetica, Arial - apparence neutre, polyvalente
- **Geometric** : Futura, Avenir - formes géométriques pures
- **Humanist** : Gill Sans, Optima - proportions plus naturelles

#### **Polices d'affichage (Display)**
- **Script** : polices imitant l'écriture manuscrite
- **Blackletter** : gothique, inspiration médiévale
- **Decorative** : ornementales, pour usage spécifique

### Contre-formes et espaces négatifs

#### **Importance des contre-formes**
Les espaces vides à l'intérieur et entre les lettres sont aussi importants que les traits :
- **Counter** : espace intérieur (œil du e, boucle du a)
- **Aperture** : ouverture des contre-formes
- **Stress** : axe d'inclinaison des courbes

#### **Impact sur la lisibilité**
- Contre-formes trop fermées : sensation d'étouffement
- Contre-formes trop ouvertes : perte de structure
- Équilibre optimal : reconnaissance rapide des caractères

---

## Paires de polices et harmonies

L'association de plusieurs polices dans un même document est un art subtil qui influence considérablement l'impact visuel et la lisibilité.

### Principes d'harmonie typographique

#### **Contraste vs Similarité**
- **Contraste fort** : serif + sans-serif pour distinction claire
- **Contraste modéré** : deux sans-serif de graisses différentes
- **Similarité** : même famille avec variations de poids

#### **Hiérarchie visuelle**
```
Titre principal : Display serif (ex: Playfair Display)
Sous-titre : Sans-serif géométrique (ex: Montserrat)
Corps de texte : Serif old-style (ex: Crimson Text)
Légende : Sans-serif neutre (ex: Source Sans Pro)
```

### Règles de combinaison éprouvées

#### **Méthode des 3 niveaux**
1. **Police d'affichage** pour les grands titres
2. **Police de texte** pour le contenu principal
3. **Police d'accent** pour les éléments secondaires

#### **Tests de compatibilité**
- **Alignement des x-heights** : harmonie des proportions
- **Contraste de graisse** : distinction claire des rôles
- **Style cohérent** : même période historique ou inspiration

### Exemples d'harmonies réussies

#### **Classique moderne**
- Titre : Bodoni (serif moderne)
- Texte : Helvetica Neue (sans-serif neutre)

#### **Éditorial sophistiqué**
- Titre : Baskerville (transitional serif)
- Texte : Garamond (old-style serif)

#### **Technologique épuré**
- Titre : Futura (geometric sans-serif)
- Texte : Source Sans Pro (humanist sans-serif)

---

## Bonnes pratiques de lisibilité et d'accessibilité

La typographie doit avant tout servir la communication. La lisibilité et l'accessibilité sont des critères non négociables.

### Facteurs de lisibilité

#### **Facteurs visuels**
- **Taille de police** : minimum 16px pour le web, 9pt pour l'impression
- **Longueur de ligne** : 45-75 caractères par ligne (règle des 45-75)
- **Interlignage** : 120-145% de la taille de police
- **Contraste** : rapport minimum 4.5:1 pour le texte normal

#### **Facteurs cognitifs**
- **Complexité des formes** : polices simples pour le long texte
- **Largeur des caractères** : proportions équilibrées
- **Espacement** : crénage et approche optimisés

### Accessibilité typographique

#### **Standards WCAG**
- **AA** : contraste 4.5:1, texte redimensionnable à 200%
- **AAA** : contraste 7:1, support des technologies d'assistance
- **Police de fallback** : spécifier des alternatives sûres

#### **Support des langues**
- **Jeux de caractères** : Latin, Cyrillic, Greek, Arabic, CJK
- **Features OpenType** : ligatures, petites capitales, fractions
- **Localisation** : adaptation des métriques par langue

### Considérations multisupport

#### **Print vs Digital**
- **Impression** : résolution 300 DPI, vectorisation parfaite
- **Web** : hinting pour l'affichage écran, formats WOFF2
- **Mobile** : lisibilité en petite taille, touch-friendly

#### **Conditions de lecture**
- **Éclairage variable** : contraste suffisant
- **Distance de lecture** : adaptation de la taille
- **Temps de lecture** : confort pour lecture prolongée

---

## Outils classiques de création typographique

Les outils traditionnels restent essentiels pour comprendre les contraintes techniques et artistiques de la typographie.

### FontForge (open-source)

**FontForge** est l'outil de référence pour la création de polices open-source.

#### **Fonctionnalités principales**
- **Édition vectorielle** : courbes de Bézier, points d'ancrage
- **Métriques** : définition précise des espacements
- **Features OpenType** : programmation des fonctionnalités avancées
- **Import/Export** : support de tous les formats standards

#### **Workflow typique**
1. Import d'un modèle de police existante
2. Modification des glyphes avec l'outil de courbes
3. Ajustement des métriques et du crénage
4. Génération des features OpenType
5. Test et validation

### Glyphs (professionnel)

**Glyphs** est l'outil standard des typographes professionnels.

#### **Interface intuitive**
- **Multi-master** : création de polices variables
- **Smart components** : réutilisation de composants
- **Plugins** : extension des fonctionnalités
- **Prévisualisation** : test en temps réel

#### **Avantages pour les professionnels**
- **Productivité** : workflow optimisé pour la production
- **Qualité** : standards professionnels élevés
- **Communauté** : support et ressources étendus

### Robofont (développement)

**Robofont** combine création typographique et programmation Python.

#### **Scripting intégré**
- **Python API** : automatisation des tâches répétitives
- **Extensions** : écosystème de plugins
- **Interpolation** : création de styles intermédiaires
- **Test automatisé** : validation technique

#### **Applications avancées**
- **Batch processing** : traitement de plusieurs polices
- **Analyse comparative** : métriques et caractéristiques
- **Génération procédurale** : création algorithmique

### Outils d'analyse et de test

#### **Validation technique**
- **FontVal** : validation des standards OpenType
- **WOFF tools** : optimisation pour le web
- **Metrics Machine** : analyse comparative des métriques

#### **Tests de lisibilité**
- **Reading tests** : évaluation de la vitesse de lecture
- **Screen rendering** : test sur différents systèmes
- **Print proofing** : validation d'impression

---

## 💡 Conseils pratiques

**Pour l'apprentissage :**
- Commencez par analyser des polices que vous aimez
- Reproduisez des caractères simples avant de créer des alphabets complets
- Étudiez l'histoire de la typographie pour comprendre les choix stylistiques

**Pour la pratique professionnelle :**
- Testez toujours vos polices dans leur contexte d'usage final
- Considérez l'accessibilité dès la phase de conception
- Documentez vos choix typographiques pour les clients

---

## ✓ Points clés à retenir

- **L'anatomie** des caractères influence directement la lisibilité
- **L'harmonie typographique** se construit sur le contraste et la complémentarité
- **L'accessibilité** doit être intégrée dès la conception
- **Les outils traditionnels** restent essentiels pour comprendre les contraintes techniques

---

**Exercice pratique :** Analysez une page de magazine ou un site web. Identifiez les polices utilisées, leur rôle dans la hiérarchie, et évaluez leur lisibilité selon les critères abordés dans ce chapitre.

**Prochain chapitre :** Découvrez comment l'IA peut générer et modifier des polices de manière automatisée, en s'appuyant sur ces principes fondamentaux.
