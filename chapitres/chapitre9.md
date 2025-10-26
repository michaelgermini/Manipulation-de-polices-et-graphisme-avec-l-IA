# Chapitre 9 — Automatisation et pipelines créatifs

L'automatisation transforme le design assisté par IA d'une activité artisanale en un processus industriel scalable. Ce chapitre explore comment intégrer l'IA dans des pipelines de production automatisés, permettant de générer des centaines de variations, d'optimiser des assets en continu, et de maintenir la cohérence à travers de gros volumes de contenu.

## Pack d'outils et scripts Python pour automatiser prompts et exports

L'automatisation avec Python permet de traiter des tâches répétitives à grande échelle tout en maintenant la qualité et la cohérence créative.

### Écosystème d'outils Python

#### **Bibliothèques essentielles**
```bash
pip install openai replicate stability-sdk fonttools pillow opencv-python
```

#### **Structure de projet type**
```
creative_ai_pipeline/
├── scripts/
│   ├── generate_fonts.py
│   ├── batch_process.py
│   ├── optimize_assets.py
│   └── export_formats.py
├── configs/
│   ├── prompts.yaml
│   ├── styles.json
│   └── settings.py
├── assets/
│   ├── inputs/
│   ├── outputs/
│   └── templates/
└── utils/
    ├── api_client.py
    ├── image_processor.py
    └── font_generator.py
```

### Script de génération automatisée de polices

#### **Génération par lots**
```python
import yaml
from font_generator import FontGenerator
from pathlib import Path

def batch_generate_fonts(config_path, output_dir):
    """Génère plusieurs polices selon une configuration"""
    with open(config_path) as f:
        configs = yaml.safe_load(f)
    
    generator = FontGenerator()
    
    for font_config in configs['fonts']:
        # Génération des glyphes
        glyphs = generator.generate_glyphs(font_config['prompts'])
        
        # Application des métriques
        font = generator.create_font(glyphs, font_config['metrics'])
        
        # Optimisation et export
        optimized_font = generator.optimize_font(font)
        generator.export_font(optimized_font, output_dir, font_config['formats'])
```

#### **Configuration YAML**
```yaml
fonts:
  - name: "ModernSans"
    style: "modern geometric sans-serif"
    weights: [300, 400, 500, 700]
    prompts:
      uppercase: "Generate uppercase A-Z in modern geometric style..."
      lowercase: "Generate lowercase a-z matching uppercase style..."
      numbers: "Generate numbers 0-9 in consistent style..."
    metrics:
      upm: 1000
      ascender: 800
      descender: -200
      x_height: 500
    formats: ["otf", "woff2", "ttf"]
```

### Automatisation des prompts

#### **Template system**
```python
class PromptTemplate:
    def __init__(self, template_string, variables):
        self.template = template_string
        self.variables = variables
    
    def generate_variations(self, variation_count=5):
        """Génère des variations d'un prompt de base"""
        variations = []
        
        for i in range(variation_count):
            # Modification aléatoire des paramètres
            varied_prompt = self._apply_variations(self.template, i)
            variations.append(varied_prompt)
        
        return variations
    
    def _apply_variations(self, template, iteration):
        # Logique de variation selon l'itération
        return template  # Implémentation personnalisée
```

#### **Exemple d'usage**
```python
template = PromptTemplate(
    "Generate {style} typography for {use_case} in {colors} color scheme",
    {"style": ["modern", "vintage", "futuristic"],
     "use_case": ["logo", "headline", "body text"],
     "colors": ["monochrome", "vibrant", "pastel"]}
)

variations = template.generate_variations(12)
```

---

## Intégration CI (GitHub Actions) pour générer assets automatiquement

L'intégration continue permet de régénérer automatiquement tous les assets graphiques à chaque modification du projet.

### Workflow GitHub Actions de base

#### **Configuration du pipeline**
```yaml
name: Generate Creative Assets
on:
  push:
    paths: ['configs/**', 'scripts/**', 'assets/inputs/**']
  schedule:
    - cron: '0 2 * * 1'  # Lundi 2h du matin

jobs:
  generate-assets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Generate fonts
        run: python scripts/generate_fonts.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          REPLICATE_API_TOKEN: ${{ secrets.REPLICATE_API_TOKEN }}
      
      - name: Optimize assets
        run: python scripts/optimize_assets.py
      
      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: generated-assets
          path: assets/outputs/
```

### Pipeline avancée avec tests

#### **Validation automatique**
```yaml
- name: Test generated assets
  run: |
    python scripts/validate_fonts.py
    python scripts/test_accessibility.py
    python scripts/performance_check.py

- name: Deploy to CDN
  if: success()
  run: |
    aws s3 sync assets/outputs/ s3://cdn.mybrand.com/assets/
    python scripts/invalidate_cache.py

- name: Update design system
  if: success()
  run: python scripts/update_design_tokens.py
```

### Gestion des secrets et sécurité

#### **Variables d'environnement**
```bash
# .env file for local development
OPENAI_API_KEY=sk-your-key-here
REPLICATE_API_TOKEN=r_your-token-here
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
```

#### **GitHub Secrets configuration**
```bash
# Repository Settings > Secrets and variables > Actions
OPENAI_API_KEY: sk-...
REPLICATE_API_TOKEN: r_...
CDN_DEPLOY_KEY: your-deployment-key
```

---

## Batch-processing d'images et de glyphes

Le traitement par lots permet de traiter des centaines d'assets simultanément avec des paramètres cohérents.

### Pipeline de traitement d'images

#### **Script de batch processing**
```python
from image_processor import ImageProcessor
from pathlib import Path
import concurrent.futures

def batch_process_images(input_dir, output_dir, operations):
    """Traite un lot d'images avec différentes opérations"""
    processor = ImageProcessor()
    input_paths = list(Path(input_dir).glob("*.png"))
    
    def process_single_image(input_path):
        # Chargement de l'image
        image = processor.load_image(input_path)
        
        # Application des opérations
        for operation in operations:
            image = processor.apply_operation(image, operation)
        
        # Sauvegarde
        output_path = Path(output_dir) / input_path.name
        processor.save_image(image, output_path)
        return str(output_path)
    
    # Traitement parallèle
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_single_image, input_paths))
    
    return results
```

#### **Configuration des opérations**
```python
operations = [
    {'type': 'resize', 'width': 1000, 'height': 1000},
    {'type': 'optimize', 'quality': 85, 'format': 'webp'},
    {'type': 'add_watermark', 'text': '© 2024 MyBrand'},
    {'type': 'color_correction', 'brightness': 1.1, 'contrast': 1.05}
]
```

### Traitement de glyphes en batch

#### **Optimisation de polices complètes**
```python
def optimize_glyph_batch(font_path, output_path, optimizations):
    """Optimise tous les glyphes d'une police"""
    from fontTools.ttLib import TTFont
    
    font = TTFont(font_path)
    glyph_set = font['gly'].glyphs
    
    for glyph_name in glyph_set.keys():
        glyph = glyph_set[glyph_name]
        
        # Application des optimisations
        for optimization in optimizations:
            glyph = apply_glyph_optimization(glyph, optimization)
    
    font.save(output_path)
```

#### **Optimisations courantes**
- **Simplification** : réduction du nombre de points
- **Harmonisation** : uniformisation des épaisseurs
- **Nettoyage** : suppression des points redondants
- **Hinting** : optimisation pour l'affichage écran

---

## Gestion des versions et des métadonnées

Un système de gestion de versions robuste est essentiel pour tracer l'évolution des assets et maintenir la cohérence.

### Système de versioning sémantique

#### **Convention de nommage**
```
brand-primary-font-v2.1.3.otf
├── brand        (nom du projet)
├── primary-font (type d'asset)
├── v2           (version majeure)
├── .1           (version mineure)
└── .3           (patch)
```

#### **Script de versioning**
```python
import re
from datetime import datetime

def update_version(current_version, change_type='patch'):
    """Met à jour la version selon le type de changement"""
    major, minor, patch = map(int, current_version.split('.'))
    
    if change_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif change_type == 'minor':
        minor += 1
        patch = 0
    else:  # patch
        patch += 1
    
    return f"{major}.{minor}.{patch}"

def generate_versioned_filename(base_name, version):
    """Génère un nom de fichier versionné"""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    name, ext = base_name.rsplit('.', 1)
    return f"{name}-v{version}-{timestamp}.{ext}"
```

### Métadonnées et traçabilité

#### **Intégration des métadonnées**
```python
def add_metadata_to_font(font_path, metadata):
    """Ajoute des métadonnées complètes à une police"""
    from fontTools.ttLib import TTFont
    
    font = TTFont(font_path)
    
    # Métadonnées de base
    font['name'].setName(metadata['font_name'], 1, 3, 1, 0x409)
    font['name'].setName(metadata['designer'], 2, 3, 1, 0x409)
    font['name'].setName(metadata['description'], 3, 3, 1, 0x409)
    
    # Métadonnées étendues
    if 'AI' not in font:
        font['AI'] = {}
    
    font['AI']['generation_prompt'] = metadata['prompt']
    font['AI']['timestamp'] = metadata['timestamp']
    font['AI']['model_version'] = metadata['model_version']
    font['AI']['parameters'] = metadata['parameters']
    
    font.save(font_path)
```

#### **Métadonnées d'exemple**
```python
metadata = {
    'font_name': 'ModernSans-Regular',
    'designer': 'AI Assistant',
    'description': 'Modern geometric sans-serif generated with AI',
    'prompt': 'Generate modern geometric sans-serif...',
    'timestamp': '2024-10-26T12:00:00Z',
    'model_version': 'stable-diffusion-xl-1.0',
    'parameters': {
        'steps': 50,
        'cfg_scale': 7,
        'seed': 42
    }
}
```

---

## API et webhooks pour workflows avancés

L'intégration d'API et de webhooks permet de créer des workflows réactifs et interconnectés.

### Intégration API pour génération

#### **Client API unifié**
```python
class CreativeAPIClient:
    def __init__(self, config):
        self.config = config
        self.clients = {
            'openai': OpenAIClient(config['openai']),
            'replicate': ReplicateClient(config['replicate']),
            'stability': StabilityClient(config['stability'])
        }
    
    def generate_asset(self, prompt, asset_type, style_config):
        """Génère un asset via l'API appropriée"""
        if asset_type == 'typography':
            return self.clients['openai'].generate_typography(prompt, style_config)
        elif asset_type == 'image':
            return self.clients['stability'].generate_image(prompt, style_config)
        elif asset_type == 'animation':
            return self.clients['replicate'].generate_animation(prompt, style_config)
```

#### **Configuration multi-API**
```python
api_config = {
    'openai': {
        'api_key': os.getenv('OPENAI_API_KEY'),
        'model': 'gpt-4-vision',
        'max_tokens': 4000
    },
    'replicate': {
        'api_token': os.getenv('REPLICATE_API_TOKEN'),
        'model': 'stability-ai/sdxl'
    },
    'stability': {
        'api_key': os.getenv('STABILITY_API_KEY'),
        'engine': 'stable-diffusion-xl-1024-v1-0'
    }
}
```

### Webhooks pour workflows réactifs

#### **Configuration webhook**
```yaml
# webhooks.yaml
webhooks:
  font_generation:
    url: "https://api.mybrand.com/webhooks/font-generated"
    events: ["font.created", "font.optimized", "font.exported"]
    retry_policy: "exponential_backoff"
  
  asset_validation:
    url: "https://api.mybrand.com/webhooks/asset-validated"
    events: ["validation.passed", "validation.failed"]
    retry_policy: "immediate"
```

#### **Gestionnaire de webhooks**
```python
import flask
from flask import request

app = Flask(__name__)

@app.route('/webhooks/font-generated', methods=['POST'])
def handle_font_generated():
    """Traite les notifications de génération de police"""
    data = request.json
    
    if data['status'] == 'completed':
        # Téléchargement automatique
        download_generated_font(data['font_url'])
        
        # Validation
        validate_font_quality(data['font_path'])
        
        # Déploiement
        deploy_to_cdn(data['font_path'])
    
    return {'status': 'processed'}
```

---

## ⚠️ Considérations pour l'automatisation

**Fiabilité et robustesse :**
- Gestion des erreurs et retry automatique
- Tests unitaires pour tous les scripts
- Logging complet des opérations
- Backup et récupération

**Performance et scalabilité :**
- Traitement parallèle quand possible
- Optimisation mémoire pour gros volumes
- Cache intelligent des résultats
- Monitoring des performances

**Sécurité et conformité :**
- Chiffrement des secrets et API keys
- Validation des entrées et sorties
- Audit trail complet
- Conformité RGPD pour les données

---

## 💡 Optimisations avancées

**Machine Learning adaptatif :**
- Apprentissage des préférences utilisateur
- Optimisation automatique des paramètres
- Prédiction des besoins futurs

**Analyse prédictive :**
- Détection des tendances de design
- Anticipation des besoins en assets
- Optimisation des ressources

**Intégration cloud-native :**
- Serverless pour coûts optimisés
- Auto-scaling selon la demande
- Multi-cloud pour résilience

---

## ✓ Bénéfices de l'automatisation

- **Échelle** : traitement de milliers d'assets
- **Cohérence** : application uniforme des standards
- **Rapidité** : génération en quelques minutes
- **Fiabilité** : réduction des erreurs humaines

---

**Exercice pratique :** Créez un script Python simple qui automatise la génération de 10 variations d'un logo et les exporte dans différents formats. Testez l'intégration avec une API d'IA.

**Prochain chapitre :** Découvrez 100+ prompts prêts à l'emploi, des modèles de briefs clients, et des ateliers pratiques pour maîtriser tous les aspects de la création assistée par IA.
