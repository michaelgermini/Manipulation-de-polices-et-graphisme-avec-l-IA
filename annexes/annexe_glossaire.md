# Annexe C — Glossaire technique

Ce glossaire définit les termes spécialisés utilisés dans le domaine de la typographie, du graphisme et de l'IA générative. Chaque définition inclut des explications contextuelles et des exemples pratiques.

## A

### **Anatomie typographique (Type anatomy)**
Structure et proportions des caractères typographiques.

**Éléments clés :**
- **Ascendante** : Partie qui dépasse vers le haut (b, d, h)
- **Descendante** : Partie qui descend sous la ligne de base (p, q, y)
- **Hauteur d'x** : Distance entre la ligne de base et la ligne médiane
- **Hauteur des capitales** : Hauteur des majuscules
- **Contre-forme** : Espace vide à l'intérieur des lettres

**Exemple :** La hauteur d'x influence la lisibilité d'une police dans les petits corps.

### **Approche (Letter spacing)**
Espace ajouté entre tous les caractères d'un texte.

**Différence avec le crénage :**
- **Approche** : Espacement global uniforme
- **Crénage** : Ajustements spécifiques entre paires de lettres

**Usage :** L'approche de +50 unités rend le texte plus aéré.

### **Artefact (Artifact)**
Anomalie visuelle indésirable générée par l'IA ou les algorithmes.

**Types courants :**
- Pixels parasites dans les images
- Points de contrôle excessifs dans les courbes
- Transitions abruptes dans les dégradés

**Solution :** Nettoyage automatique ou manuel des outputs.

## B

### **Baseline (Ligne de base)**
Ligne horizontale imaginaire sur laquelle reposent les caractères.

**Importance :**
- Référence pour l'alignement vertical
- Point de départ pour les ascendantes et descendantes
- Base du système de coordonnées typographiques

**Exemple :** Toutes les lettres rondes (o, a, e) reposent sur la baseline.

### **Batch processing (Traitement par lots)**
Traitement automatique de multiples fichiers ou données.

**Applications :**
- Génération de 100 variations d'un logo
- Optimisation de polices complètes
- Conversion de formats en masse

**Avantage :** Gain de temps considérable pour les tâches répétitives.

## C

### **Chasse (Character width)**
Largeur horizontale d'un caractère, de son point d'origine à son point d'échappement.

**Unités :**
- Exprimée en unités typographiques (1/1000 d'em généralement)
- Variable selon le style de police
- Influence le rythme de lecture

**Exemple :** Le 'm' a une chasse plus large que le 'i'.

### **Contre-forme (Counter)**
Espace vide à l'intérieur ou entre les lettres.

**Types :**
- **Fermé** : Complètement entouré (o, a, b)
- **Ouvert** : Partiellement ouvert (c, e, s)
- **Semi-fermé** : Partiellement entouré (B, R, P)

**Impact :** Les contre-formes influencent la lisibilité et le style.

### **Crénage (Kerning)**
Ajustement spécifique de l'espacement entre paires de caractères.

**Paires courantes :**
- **VA** : -25 unités (rapprochement)
- **To** : -15 unités (rapprochement)
- **AW** : +10 unités (écartement)

**Méthode :** Analyse optique pour un espacement visuellement harmonieux.

### **CSS (Cascading Style Sheets)**
Langage de style pour la présentation des documents web.

**Propriétés typographiques :**
- `font-family` : Police utilisée
- `font-size` : Taille de la police
- `line-height` : Interlignage
- `letter-spacing` : Approche
- `font-weight` : Graisse

**Responsive :** Utilisation d'unités relatives (em, rem, %).

## D

### **DPI (Dots Per Inch)**
Résolution d'impression mesurée en points par pouce.

**Standards :**
- **Web** : 72-96 DPI
- **Print** : 300 DPI minimum
- **High quality print** : 600-1200 DPI

**Conversion :** 1 pouce = 2.54 cm = 300 points pour l'impression.

### **Descendante (Descender)**
Partie d'un caractère qui s'étend sous la ligne de base.

**Lettres concernées :**
- Minuscules : p, q, y, g, j
- Chiffres : 7, 9
- Ponctuation : virgule, point-virgule

**Profondeur :** Variable selon le style, influence l'interlignage nécessaire.

## E

### **Empattement (Serif)**
Petit trait ornemental aux extrémités des caractères.

**Classification :**
- **Old Style** : Empattements obliques (Garamond)
- **Transitional** : Contraste marqué (Times)
- **Didone** : Contraste extrême (Bodoni)
- **Slab** : Empattements épais (Rockwell)

**Usage :** Facilite la lecture en guidant l'œil le long des lignes.

### **Em (Unité typographique)**
Unité de mesure relative égale à la taille de police spécifiée.

**Applications :**
- **1em** = taille de la police actuelle
- **0.5em** = moitié de la taille
- **2em** = double de la taille

**Responsive :** S'adapte automatiquement aux changements de taille.

### **Escapement (Point d'échappement)**
Point de sortie d'un caractère, définissant sa largeur totale.

**Coordonnées :**
- **Point d'origine** : Début du caractère (généralement à gauche)
- **Point d'échappement** : Fin du caractère (définit la chasse)
- **Largeur** = Échappement - Origine

**Importance :** Détermine l'espacement naturel entre caractères.

## F

### **Famille de polices (Font family)**
Ensemble de polices partageant un design cohérent avec des variations.

**Structure typique :**
- **Regular** : 400 (poids normal)
- **Medium** : 500 (poids moyen)
- **Bold** : 700 (poids gras)
- **Italic** : Inclinaison
- **Bold Italic** : Gras + italique

**OpenType :** Support des features avancées (ligatures, petites capitales).

### **Feature OpenType**
Fonctionnalités avancées intégrées dans les polices OpenType.

**Features courantes :**
- **liga** : Ligatures automatiques (fi, fl, æ)
- **smcp** : Petites capitales
- **onum** : Chiffres elzéviriens
- **kern** : Crénage automatique
- **calt** : Alternates contextuelles

**Activation :** Via CSS `font-feature-settings` ou logiciels de PAO.

## G

### **Glyphe (Glyph)**
Représentation visuelle d'un caractère dans une police.

**Composition :**
- **Contours vectoriels** : Courbes de Bézier
- **Points de contrôle** : Gestion des courbes
- **Métriques** : Position et espacement
- **Unicode** : Point de code associé

**Exemple :** Le glyphe 'A' peut avoir plusieurs variantes (A, Á, Ä).

### **Grille (Grid system)**
Structure invisible divisant la page en sections harmonieuses.

**Types :**
- **Grille de manuscrit** : Colonnes simples
- **Grille modulaire** : Sections répétitives
- **Grille de base** : Lignes de base cohérentes
- **Grille responsive** : Adaptation aux breakpoints

**Règle des tiers :** Division en 3 parties horizontales et verticales.

## H

### **Hauteur d'x (X-height)**
Distance entre la ligne de base et la ligne médiane (hauteur des minuscules).

**Impact sur la lisibilité :**
- **Grande hauteur d'x** : Meilleure lisibilité en petits corps
- **Petite hauteur d'x** : Aspect plus raffiné
- **Ratio idéal** : 0.65-0.75 de la hauteur des capitales

**Exemple :** Helvetica a une hauteur d'x élevée pour la lisibilité.

### **Hinting**
Instructions mathématiques intégrées dans les polices pour optimiser l'affichage à l'écran.

**Fonctionnement :**
- Ajustement des pixels pour les petites tailles
- Amélioration du rendu sur écrans basse résolution
- Maintien de la lisibilité et du caractère

**Outils :**
- **Auto-hinting** : Génération automatique
- **Manual hinting** : Ajustements manuels fins
- **Delta hinting** : Corrections spécifiques par taille

## I

### **Interlignage (Leading)**
Espace vertical entre les lignes de base de texte.

**Mesure :**
- **Métrique** : Distance entre baselines
- **Optique** : Espace visuel perçu
- **Ratio recommandé** : 1.2-1.6 × taille de police

**Exemple :** 12pt/14pt signifie 12pt de police avec 14pt d'interlignage.

### **Interpolation typographique**
Création de styles intermédiaires entre deux masters dans les polices variables.

**Axes standards :**
- **wght** : Weight (100-900)
- **wdth** : Width (50-200%)
- **ital** : Italic (0-1)
- **opsz** : Optical size (8-144pt)

**Avantage :** Fichier unique pour de multiples styles.

## K

### **Keming (Erreur typographique)**
Mauvais espacement entre caractères, particulièrement visible dans les logos.

**Exemples célèbres :**
- **"Th"** avec trop d'espace
- **"rn"** paraissant comme "m"
- **"cl"** avec collision

**Prévention :** Utilisation du crénage automatique et validation manuelle.

## L

### **Ligature (Ligature)**
Caractère unique combinant deux lettres pour un meilleur rendu visuel.

**Ligatures courantes :**
- **fi** : f + i
- **fl** : f + l
- **ffi** : f + f + i
- **æ** : a + e (latin)
- **œ** : o + e (latin)

**Activation :** Feature OpenType `liga` dans les polices modernes.

## M

### **Métriques (Font metrics)**
Données numériques définissant les dimensions et espacement d'une police.

**Métriques principales :**
- **UPM** : Units Per Em (généralement 1000 ou 2048)
- **Ascender** : Hauteur des ascendantes
- **Descender** : Profondeur des descendantes
- **Line gap** : Espace entre lignes
- **Sidebearings** : Marges latérales

**Importance :** Cohérence entre polices lors du mélange.

## O

### **OpenType (Format de police)**
Format de police standard supportant Unicode complet et features avancées.

**Avantages :**
- Support de tous les scripts du monde
- Features typographiques avancées
- Polices variables
- Meilleure compression

**Extensions :**
- **.otf** : OpenType avec PostScript curves
- **.ttf** : OpenType avec TrueType curves

### **Optical size**
Ajustement automatique des proportions selon la taille d'usage.

**Applications :**
- **Petites tailles** : Tracé plus épais pour la lisibilité
- **Grandes tailles** : Détails fins et élégants
- **Display** : Optimisé pour les gros titres
- **Caption** : Optimisé pour les légendes

**Exemple :** Minion Pro avec optical sizing.

## P

### **Point typographique (Point)**
Unité de mesure en typographie.

**Conversions :**
- **1 point** = 1/72 pouce ≈ 0.35 mm
- **1 pica** = 12 points ≈ 4.23 mm
- **1 cm** ≈ 28.35 points
- **1 inch** = 72 points

**Usage :** Mesure des tailles de police et interlignage.

### **Prompt engineering**
Art de formuler des instructions optimales pour les modèles d'IA.

**Composants :**
- **Description précise** : Détails visuels et techniques
- **Contexte d'usage** : Finalité et contraintes
- **Paramètres techniques** : Format, résolution, style
- **Itération** : Raffinement progressif

**Exemple :** "Génère une police sans-serif moderne optimisée pour l'interface utilisateur, avec une excellente lisibilité en 14px, format SVG scalable."

## R

### **RGB (Red Green Blue)**
Modèle de couleur additive utilisé pour les écrans.

**Caractéristiques :**
- **Gamme** : 0-255 par canal
- **Noir** : RGB(0,0,0)
- **Blanc** : RGB(255,255,255)
- **Conversion** : Vers CMYK pour l'impression

**Usage :** Design web, interfaces digitales, écrans.

### **Rendu (Rendering)**
Processus de conversion des données en image visible.

**Types :**
- **Hinted** : Optimisé pour l'écran avec hinting
- **Antialiased** : Lissage des contours
- **Subpixel** : Utilisation des sous-pixels pour la netteté
- **Vectoriel** : Scalable sans perte de qualité

**Qualité :** Dépend de la résolution et de l'optimisation.

## S

### **Sans-serif (Police sans empattement)**
Police de caractères sans ornements aux extrémités.

**Classification :**
- **Grotesque** : Helvetica, Arial (neutre)
- **Geometric** : Futura, Avenir (formes pures)
- **Humanist** : Gill Sans (proportions naturelles)

**Usage :** Interfaces web, signalétique, design moderne.

### **Scalable Vector Graphics (SVG)**
Format d'image vectorielle pour le web.

**Avantages :**
- Infiniement scalable
- Taille de fichier réduite
- Éditable avec du code
- Animation possible avec CSS/SMILE

**Structure :** XML avec éléments path, circle, rect.

### **Script (Style typographique)**
Police imitant l'écriture manuscrite.

**Types :**
- **Formal** : Copperplate, Spencerian
- **Casual** : Handwriting, signatures
- **Brush** : Effet pinceau, dynamique
- **Calligraphic** : Outils traditionnels

**Usage :** Invitations, logos, branding personnel.

## T

### **Tracking (Approche globale)**
Ajustement de l'espacement entre tous les caractères d'une sélection.

**Différence avec le crénage :**
- **Tracking** : Uniforme sur toute la sélection
- **Kerning** : Ajustements par paires spécifiques

**Usage :** Ajustement de la densité visuelle du texte.

### **TrueType (Format de police)**
Format de police développé par Apple et Microsoft.

**Caractéristiques :**
- Courbes quadratiques (plus simples)
- Hinting intégré
- Large compatibilité
- Base des polices système

**Évolution :** Supplanté par OpenType mais encore largement utilisé.

## U

### **Unicode**
Standard international pour la représentation des caractères.

**Points de code :**
- **U+0041** : A majuscule
- **U+0061** : a minuscule
- **U+1F600** : Emoji souriant
- **U+20AC** : € euro

**Support :** OpenType supporte Unicode complet.

### **Unités par em (UPM)**
Résolution interne d'une police pour les calculs.

**Standards :**
- **1000 UPM** : Moderne (FontForge, Glyphs)
- **2048 UPM** : Classique (TrueType)
- **Precision** : Plus d'UPM = plus de précision

**Conversion :** 1 em = 1000 unités (typiquement).

## V

### **Variable fonts (Polices variables)**
Polices avec interpolation continue entre différents styles.

**Axes standards :**
- **wght** : Poids (100-900)
- **wdth** : Largeur (50-200%)
- **ital** : Italique (0-1)
- **opsz** : Taille optique (8-144pt)

**Avantages :**
- Taille de fichier réduite
- Transitions fluides
- Contrôle précis du designer

**Exemple :** Une seule police pour tous les poids d'Helvetica.

### **Vectorisation (Vectorization)**
Conversion d'images bitmap en format vectoriel.

**Processus :**
- Détection des contours
- Création de courbes de Bézier
- Simplification des points
- Optimisation pour l'usage

**Avantages :** Scalabilité infinie, taille réduite, édition possible.

## W

### **Web fonts**
Polices optimisées pour l'affichage web.

**Formats :**
- **WOFF2** : Meilleure compression
- **WOFF** : Large compatibilité
- **TTF** : Fallback universel
- **EOT** : Internet Explorer legacy

**Performance :** Chargement asynchrone, préchargement, fallbacks.

### **Width (Largeur de caractère)**
Dimension horizontale d'un caractère.

**Classification :**
- **Condensed** : Caractères étroits
- **Regular** : Largeur standard
- **Extended** : Caractères larges
- **Variable** : Largeur ajustable (polices variables)

**Usage :** Adaptation à l'espace disponible.

---

## Index des termes par chapitre

### **Chapitre 1 - Fondamentaux**
Anatomie typographique, Empattement, Sans-serif, Baseline, Hauteur d'x, Contre-forme, Chasse, Approche, Interlignage, Famille de polices

### **Chapitre 2 - Génération IA**
Glyphe, Vectorisation, OpenType, Métriques, UPM, Sidebearings, Hinting, Feature OpenType, Ligature, Script

### **Chapitre 3 - Espacement**
Crénage, Approche, Tracking, Sidebearings, Métriques, UPM, Interpolation, Variable fonts, Optical size, Hinting

### **Chapitre 4 - Vectorisation**
SVG, Courbes de Bézier, Points de contrôle, Artefact, Nettoyage, Simplification, Formats d'échange, Batch processing

### **Chapitre 5 - Logotypes**
Monogramme, Wordmark, Combination mark, Scalabilité, Multi-format, Brand guidelines, Visual hierarchy

### **Chapitre 6 - Composition**
Grille, Baseline grid, Typography scale, Responsive, Breakpoints, Visual hierarchy, Golden ratio, Rule of thirds

### **Chapitre 7 - Styles visuels**
Texture, Pattern, Effect, Material, Lighting, Relief, Emboss, Glow, Grain, Halftone, Mockup

### **Chapitre 8 - Animation**
Keyframe, Easing, Transition, Lottie, Morphing, Kinetic typography, Audio sync, Beat mapping, Timeline

### **Chapitre 9 - Automatisation**
Pipeline, Batch processing, CI/CD, API, Webhook, Versioning, Metadata, Script, Automation

### **Chapitre 10 - Prompts**
Prompt engineering, Style, Parameters, Format, Output, Iteration, Template, Brief, Validation

---

**Note :** Ce glossaire est organisé alphabétiquement. Pour les termes spécifiques à l'IA générative, consultez les sections dédiées dans les chapitres correspondants.

**Extensions :** Pour les termes non couverts, consultez les ressources académiques mentionnées dans l'Annexe A.
