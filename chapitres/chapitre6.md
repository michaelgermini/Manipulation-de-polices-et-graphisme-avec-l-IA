# Chapitre 6 — Composition typographique et mise en page

L'IA transforme radicalement l'approche de la composition typographique en automatisant la création de mises en page harmonieuses et créatives. Des magazines aux interfaces web, en passant par les affiches publicitaires, les outils d'IA peuvent générer des layouts professionnels en quelques secondes, permettant aux designers de se concentrer sur la direction artistique et la stratégie de contenu.

## Utiliser l'IA pour générer des mises en page

La génération de mises en page assistée par IA combine compréhension du contenu, principes de design, et optimisation technique pour créer des compositions équilibrées et efficaces.

### Types de mises en page générables

#### **Mises en page éditoriales**
- **Magazines** : articles, interviews, portfolios
- **Journaux** : colonnes, hiérarchie informationnelle
- **Livres** : chapitres, sections, index

#### **Mises en page marketing**
- **Affiches** : événementielles, publicitaires, institutionnelles
- **Brochures** : produits, services, présentation d'entreprise
- **Packaging** : étiquettes, boîtes, présentoirs

#### **Mises en page digitales**
- **Sites web** : pages d'accueil, articles, portfolios
- **Applications** : interfaces, tableaux de bord
- **Réseaux sociaux** : posts, stories, couvertures

### Structure d'un prompt de mise en page

#### **Format recommandé**
```
[Type de document] + [Contenu et structure] + [Style visuel] + [Contraintes techniques] + [Format de sortie]
```

#### **Exemple complet**
```
"Design a magazine spread layout for a technology article featuring:
- Main headline (48pt, bold sans-serif)
- Subheading (24pt, light serif)
- Body text (11pt, readable serif)
- Pull quotes (16pt, italic)
- Images (2:3 aspect ratio)
- Modern, clean aesthetic with white space
- 2-page spread, 300DPI, print-ready"
```

### Principes de composition automatisés

#### **Hiérarchie visuelle**
```
"Create a layout with clear visual hierarchy:
- Most important: 40% of space
- Secondary: 30% of space
- Supporting: 20% of space
- Navigation: 10% of space"
```

#### **Équilibre et proportion**
- **Règle des tiers** : division harmonieuse de l'espace
- **Rapport d'or** : proportions mathématiquement agréables
- **Contrepoint typographique** : tension créative entre éléments

---

## Règles de hiérarchie visuelle et grille

Les systèmes de grille et la hiérarchie visuelle sont les fondements de toute composition réussie. L'IA peut appliquer ces principes de manière systématique et créative.

### Systèmes de grille automatisés

#### **Grille de base**
```
"Design a layout using a 12-column grid system with:
- 20px gutters between columns
- 40px margins on all sides
- Consistent vertical rhythm of 8px
- Responsive breakpoints at 768px and 1024px"
```

#### **Grille modulaire**
```
"Create a modular grid layout where:
- Each module is 80x80px with 10px spacing
- Modules can be combined (2x2, 1x3, etc.)
- Typography aligns to module boundaries
- Flexible for different content types"
```

### Hiérarchie typographique

#### **Échelle typographique**
L'IA peut générer des échelles typographiques harmonieuses basées sur des ratios mathématiques :

- **Major Third** (1.25) : 8, 10, 12.5, 15.625, 19.5, 24.375, 30.469
- **Perfect Fourth** (1.333) : 8, 10.5, 14, 18.5, 24.5, 32.5, 43.25
- **Golden Ratio** (1.618) : 8, 13, 21, 34, 55, 89, 144

#### **Application automatique**
```
"Apply typographic scale using golden ratio starting at 12px base size, assign appropriate sizes to:
- Page title (5 steps up)
- Section headers (3 steps up)
- Body text (base)
- Captions (2 steps down)
- Footnotes (3 steps down)"
```

### Espacement et rythme vertical

#### **Ligne de base cohérente**
```
"Ensure all typography sits on a consistent 4px baseline grid, with line heights that are multiples of 4px, creating perfect vertical alignment throughout the layout"
```

#### **Espacement harmonieux**
```
"Apply spacing system based on 8px grid:
- Small spacing: 8px
- Medium spacing: 16px
- Large spacing: 32px
- Extra large: 64px"
```

---

## Ateliers : générer 10 layouts par brief produit

Les ateliers pratiques permettent de développer une expertise rapide dans la génération de mises en page avec l'IA.

### Workshop 1 : Mise en page magazine

#### **Brief : Article technology**
```
"Generate 10 different magazine layout concepts for a 4-page article about artificial intelligence:

1. Hero layout with large typography and minimal text
2. Traditional column layout with sidebars
3. Full-bleed image with overlay text
4. Modular grid with multiple entry points
5. Timeline layout showing AI evolution
6. Q&A format with pull quotes
7. Data visualization integration
8. Interview layout with portrait photos
9. Future-focused with speculative graphics
10. Academic style with footnotes and references

Each layout should include:
- Consistent brand colors (blue, white, gray)
- Professional typography hierarchy
- Optimal reading flow
- Image placement suggestions"
```

### Workshop 2 : Interface web responsive

#### **Brief : Site e-commerce**
```
"Create 10 responsive web layout variations for a product page:

1. Classic e-commerce with sidebar filters
2. Mobile-first card-based layout
3. Full-width hero with sticky navigation
4. Split-screen with product details
5. Magazine-style with featured products
6. Minimalist single-product focus
7. Comparison layout for similar items
8. Social proof integration (reviews, ratings)
9. Video-first with product demonstration
10. Customizable product builder interface

Include:
- Responsive breakpoints at 768px, 1024px, 1440px
- Touch-friendly interactive elements
- Accessibility compliance (WCAG 2.1 AA)
- Performance optimization considerations"
```

### Workshop 3 : Campagne publicitaire

#### **Brief : Lancement produit**
```
"Design 10 poster concepts for a new smartphone launch:

1. Product hero with dramatic lighting
2. Feature comparison with competitor
3. Lifestyle integration showing usage
4. Technical specifications showcase
5. Brand story and heritage
6. User testimonials visual format
7. Limited-time offer urgency design
8. Color variants presentation
9. Ecosystem integration (apps, accessories)
10. Future-proofing and innovation focus

Requirements:
- A1 poster size (594x841mm)
- 300 DPI resolution
- CMYK color mode
- 10mm safety margins
- Brand consistency"
```

---

## Export print vs web : considérations techniques

Les exigences techniques diffèrent considérablement entre print et web, nécessitant des approches d'optimisation spécifiques.

### Optimisation pour l'impression

#### **Résolution et formats**
- **Résolution** : 300 DPI minimum pour qualité photo
- **Formats** : PDF/X-1a pour magazines, PDF/X-4 pour qualité maximale
- **Couleurs** : CMYK avec profils ICC, tons directs pour marques
- **Polices** : intégrées ou vectorisées pour éviter la substitution

#### **Prompt d'optimisation print**
```
"Prepare this layout for professional printing:
- Convert RGB to CMYK color space
- Embed all fonts or convert to outlines
- Add 3mm bleed on all sides
- Include crop marks and registration
- Optimize for 300 DPI output
- Ensure color accuracy with ICC profile"
```

### Optimisation pour le web

#### **Performance et accessibilité**
- **Formats** : SVG pour graphiques, WebP pour images
- **Compression** : optimisation automatique des assets
- **Polices** : WOFF2 avec fallbacks système
- **Responsive** : adaptation fluide à toutes les tailles

#### **Prompt d'optimisation web**
```
"Optimize this layout for web performance:
- Convert to responsive HTML/CSS
- Compress images to 80% quality
- Implement lazy loading for below-fold content
- Ensure accessibility with proper ARIA labels
- Optimize for Core Web Vitals scores
- Generate critical CSS for above-fold content"
```

### Scripts d'automatisation d'export

#### **Pipeline de production**
```python
def layout_export_pipeline(layout_design, targets):
    """Pipeline complet d'export pour différents supports"""
    exports = {}
    
    for target in targets:
        if target['format'] == 'print':
            # Optimisation print
            processed_layout = optimize_for_print(layout_design, target['specs'])
            export_pdf = generate_print_pdf(processed_layout)
            exports['print'] = export_pdf
            
        elif target['format'] == 'web':
            # Optimisation web
            processed_layout = optimize_for_web(layout_design, target['specs'])
            html_css = generate_responsive_html(processed_layout)
            assets = optimize_web_assets(processed_layout)
            exports['web'] = {'html': html_css, 'assets': assets}
            
        elif target['format'] == 'social':
            # Optimisation réseaux sociaux
            processed_layout = optimize_for_social(layout_design, target['specs'])
            exports['social'] = generate_social_formats(processed_layout)
    
    return exports
```

---

## Responsive typography et adaptation mobile

La typographie responsive s'adapte dynamiquement aux caractéristiques de l'appareil et aux préférences de l'utilisateur.

### Principes de la typographie responsive

#### **Fluidité typographique**
```
"Create a responsive typography system where:
- Base size scales from 16px on mobile to 18px on desktop
- Line height adjusts from 1.4 on mobile to 1.6 on desktop
- Letter spacing optimizes for different screen densities
- Font loading prioritizes critical text"
```

#### **Breakpoints typographiques**
- **Mobile first** : 320px - 768px
- **Tablet** : 768px - 1024px
- **Desktop** : 1024px - 1440px
- **Large screens** : 1440px+

### Adaptation contextuelle

#### **Conditions de lecture**
```
"Adapt typography based on:
- Screen brightness (high contrast in sunlight)
- User preferences (larger text for accessibility)
- Content type (shorter lines for scanning)
- Reading distance (larger text for TV/mobile)"
```

#### **Performance adaptive**
```
"Implement adaptive loading where:
- Critical typography loads first
- Enhanced features load progressively
- Fallback fonts display immediately
- Variable fonts optimize based on connection speed"
```

---

## ⚠️ Considérations pour la production

**Cohérence de marque :**
- Respect des guidelines existants
- Adaptation des systèmes de design
- Validation par les parties prenantes

**Tests utilisateurs :**
- Validation de la lisibilité sur différents appareils
- Tests de navigation et de compréhension
- Évaluation de la performance perçue

**Maintenance :**
- Documentation des systèmes de grille
- Guide d'utilisation pour les équipes
- Processus de mise à jour et évolution

---

## 💡 Optimisations avancées

**Génération contextuelle :**
- Adaptation automatique au contenu
- Personnalisation selon les données utilisateur
- Optimisation basée sur l'analyse comportementale

**Intégration de données :**
- Layouts générés à partir de bases de données
- Adaptation temps réel aux métriques de performance
- Personnalisation automatisée du contenu

**Automatisation complète :**
- Génération de variants A/B pour tests
- Optimisation automatique basée sur les conversions
- Adaptation continue aux tendances du design

---

## ✓ Bénéfices de l'approche IA

- **Rapidité** : 10 layouts en 30 minutes au lieu de 2 semaines
- **Cohérence** : application systématique des principes de design
- **Innovation** : exploration de solutions non conventionnelles
- **Évolutivité** : adaptation facile à différents formats et supports

---

**Exercice pratique :** Créez 5 variations de mise en page pour un article de blog fictif. Testez différentes grilles et hiérarchies typographiques, puis évaluez leur efficacité.

**Prochain chapitre :** Explorez comment l'IA peut générer des palettes cohérentes, des textures procédurales et des effets spéciaux pour enrichir vos compositions typographiques.
