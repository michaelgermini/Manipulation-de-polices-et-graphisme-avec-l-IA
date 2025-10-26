#!/usr/bin/env python3
"""
Générateur de systèmes de couleurs pour marques
Usage: python color_generator.py --primary "#2E5B91" --mood "professional"

Génère des palettes complètes avec harmonie et accessibilité
"""

import sys
import json
import argparse
from pathlib import Path

class ColorSystem:
    def __init__(self, primary_color, mood="neutral"):
        self.primary = primary_color
        self.mood = mood
        self.palette = self.generate_palette()

    def generate_palette(self):
        """Génère une palette complète basée sur la couleur primaire"""
        palette = {
            'primary': self._expand_primary(),
            'secondary': self._generate_secondary(),
            'neutrals': self._generate_neutrals(),
            'accents': self._generate_accents(),
            'semantic': self._generate_semantic()
        }
        return palette

    def _expand_primary(self):
        """Développe la couleur primaire en variations"""
        base_hue = self._hex_to_hsl(self.primary)

        variations = {}
        if self.mood in ['vibrant', 'energetic']:
            variations['50'] = self._adjust_lightness(base_hue, 0.95)
            variations['100'] = self._adjust_lightness(base_hue, 0.85)
            variations['200'] = self._adjust_lightness(base_hue, 0.70)
            variations['300'] = self._adjust_lightness(base_hue, 0.55)
            variations['400'] = self._adjust_lightness(base_hue, 0.45)
            variations['500'] = self.primary  # Base
            variations['600'] = self._adjust_lightness(base_hue, 0.35)
            variations['700'] = self._adjust_lightness(base_hue, 0.25)
            variations['800'] = self._adjust_lightness(base_hue, 0.15)
            variations['900'] = self._adjust_lightness(base_hue, 0.05)
        else:
            # Approche plus conservatrice
            variations['50'] = self._adjust_lightness(base_hue, 0.98)
            variations['100'] = self._adjust_lightness(base_hue, 0.90)
            variations['200'] = self._adjust_lightness(base_hue, 0.75)
            variations['300'] = self._adjust_lightness(base_hue, 0.60)
            variations['400'] = self._adjust_lightness(base_hue, 0.50)
            variations['500'] = self.primary
            variations['600'] = self._adjust_lightness(base_hue, 0.40)
            variations['700'] = self._adjust_lightness(base_hue, 0.30)
            variations['800'] = self._adjust_lightness(base_hue, 0.20)
            variations['900'] = self._adjust_lightness(base_hue, 0.10)

        return variations

    def _generate_secondary(self):
        """Génère des couleurs secondaires harmonieuses"""
        base_hsl = self._hex_to_hsl(self.primary)

        # Calcul de couleurs complémentaires/analogues
        secondary_colors = {}

        if self.mood == 'professional':
            # Palette business
            secondary_colors['blue'] = self._adjust_hue(base_hsl, 220)
            secondary_colors['gray'] = self._adjust_hue(base_hsl, 0, saturation=0.1)
        elif self.mood == 'creative':
            # Palette créative
            secondary_colors['purple'] = self._adjust_hue(base_hsl, 270)
            secondary_colors['teal'] = self._adjust_hue(base_hsl, 180)
        elif self.mood == 'energetic':
            # Palette dynamique
            secondary_colors['orange'] = self._adjust_hue(base_hsl, 30)
            secondary_colors['lime'] = self._adjust_hue(base_hsl, 90)

        return secondary_colors

    def _generate_neutrals(self):
        """Génère une échelle de gris harmonieuse"""
        neutrals = {}

        # Grayscale avec teinte subtile basée sur la primaire
        for i in range(50, 1000, 50):
            lightness = 1 - (i - 50) / 950  # 1.0 à 0.05

            if self.mood == 'warm':
                neutral_hsl = (40, 0.05, lightness)  # Teinte chaude
            elif self.mood == 'cool':
                neutral_hsl = (220, 0.05, lightness)  # Teinte froide
            else:
                neutral_hsl = (0, 0, lightness)  # Neutre pur

            neutrals[str(i)] = self._hsl_to_hex(neutral_hsl)

        return neutrals

    def _generate_accents(self):
        """Génère des couleurs d'accent pour les CTAs"""
        base_hsl = self._hex_to_hsl(self.primary)

        accents = {}

        # Couleurs d'accent basées sur la complémentaire
        complement_hue = (base_hsl[0] + 180) % 360

        if self.mood == 'professional':
            accents['success'] = self._hsl_to_hex((120, 0.7, 0.5))  # Vert
            accents['warning'] = self._hsl_to_hex((45, 0.8, 0.6))   # Orange
            accents['error'] = self._hsl_to_hex((0, 0.8, 0.6))     # Rouge
        else:
            accents['success'] = self._adjust_hue(base_hsl, 120, saturation=0.8)
            accents['warning'] = self._adjust_hue(base_hsl, 60, saturation=0.8)
            accents['error'] = self._adjust_hue(base_hsl, 0, saturation=0.8)

        return accents

    def _generate_semantic(self):
        """Génère des couleurs sémantiques pour interfaces"""
        semantic = {}

        semantic['background'] = self.palette['neutrals']['50']
        semantic['surface'] = self.palette['neutrals']['100']
        semantic['text-primary'] = self.palette['neutrals']['900']
        semantic['text-secondary'] = self.palette['neutrals']['600']
        semantic['text-disabled'] = self.palette['neutrals']['400']

        semantic['border'] = self.palette['neutrals']['200']
        semantic['divider'] = self.palette['neutrals']['100']

        return semantic

    def _hex_to_hsl(self, hex_color):
        """Convertit hex en HSL"""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0

        max_val = max(r, g, b)
        min_val = min(r, g, b)
        diff = max_val - min_val

        # Lightness
        l = (max_val + min_val) / 2

        if diff == 0:
            # Achromatic (gray)
            h = s = 0
        else:
            # Saturation
            s = diff / (2 - max_val - min_val) if l > 0.5 else diff / (max_val + min_val)

            # Hue
            if max_val == r:
                h = (60 * ((g - b) / diff) + 360) % 360
            elif max_val == g:
                h = (60 * ((b - r) / diff) + 120) % 360
            else:
                h = (60 * ((r - g) / diff) + 240) % 360

        return (h, s, l)

    def _hsl_to_hex(self, hsl):
        """Convertit HSL en hex"""
        h, s, l = hsl

        if s == 0:
            # Achromatic (gray)
            r = g = b = int(l * 255)
        else:
            def hue_to_rgb(p, q, t):
                if t < 0: t += 1
                if t > 1: t -= 1
                if t < 1/6: return p + (q - p) * 6 * t
                if t < 1/2: return q
                if t < 2/3: return p + (q - p) * (2/3 - t) * 6
                return p

            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q

            r = hue_to_rgb(p, q, h / 360 + 1/3)
            g = hue_to_rgb(p, q, h / 360)
            b = hue_to_rgb(p, q, h / 360 - 1/3)

        return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"

    def _adjust_lightness(self, hsl, target_lightness):
        """Ajuste la luminosité d'une couleur HSL"""
        h, s, l = hsl
        return (h, s, target_lightness)

    def _adjust_hue(self, hsl, new_hue, saturation=None):
        """Ajuste la teinte d'une couleur HSL"""
        h, s, l = hsl
        new_s = saturation if saturation is not None else s
        return (new_hue, new_s, l)

    def check_accessibility(self):
        """Vérifie les ratios de contraste pour l'accessibilité"""
        contrasts = {}

        # Test des combinaisons texte/fond principales
        text_primary = self.palette['semantic']['text-primary']
        background = self.palette['semantic']['background']
        contrasts['primary_text'] = self._contrast_ratio(text_primary, background)

        text_secondary = self.palette['semantic']['text-secondary']
        contrasts['secondary_text'] = self._contrast_ratio(text_secondary, background)

        # Test des couleurs d'accent
        for accent_name, accent_color in self.palette['accents'].items():
            contrasts[f'{accent_name}_on_white'] = self._contrast_ratio(accent_color, '#ffffff')
            contrasts[f'{accent_name}_on_dark'] = self._contrast_ratio(accent_color, '#000000')

        return contrasts

    def _contrast_ratio(self, color1, color2):
        """Calcule le ratio de contraste entre deux couleurs"""
        def luminance(color):
            # Conversion hex vers RGB
            color = color.lstrip('#')
            r = int(color[0:2], 16) / 255.0
            g = int(color[2:4], 16) / 255.0
            b = int(color[4:6], 16) / 255.0

            # Conversion RGB vers linear RGB
            def linearize(x):
                return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4

            r = linearize(r)
            g = linearize(g)
            b = linearize(b)

            # Calcul de la luminance
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        l1 = luminance(color1)
        l2 = luminance(color2)

        lighter = max(l1, l2)
        darker = min(l1, l2)

        return (lighter + 0.05) / (darker + 0.05)

def generate_css_variables(palette):
    """Génère des variables CSS pour la palette"""
    css = "/* CSS Variables pour le système de couleurs */\n:root {\n"

    # Variables primaires
    for shade, color in palette['primary'].items():
        css += f"  --color-primary-{shade}: {color};\n"

    # Variables secondaires
    for name, color in palette['secondary'].items():
        css += f"  --color-secondary-{name}: {color};\n"

    # Variables neutres
    for shade, color in palette['neutrals'].items():
        css += f"  --color-neutral-{shade}: {color};\n"

    # Variables d'accent
    for name, color in palette['accents'].items():
        css += f"  --color-accent-{name}: {color};\n"

    # Variables sémantiques
    for name, color in palette['semantic'].items():
        css += f"  --color-{name.replace('_', '-')}: {color};\n"

    css += "}\n"
    return css

def generate_scss_mixin(palette):
    """Génère un mixin SCSS"""
    scss = """// SCSS Mixin pour le système de couleurs
@mixin brand-colors {
  // Couleurs primaires"""

    for shade, color in palette['primary'].items():
        scss += f"\n  $primary-{shade}: {color};"

    scss += "\n\n  // Couleurs secondaires"
    for name, color in palette['secondary'].items():
        scss += f"\n  $secondary-{name}: {color};"

    scss += "\n\n  // Variables CSS\n  :root {"
    for shade, color in palette['primary'].items():
        scss += f"\n    --color-primary-{shade}: #{{{color[1:]} }};"
    scss += "\n  }\n}"

    return scss

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(description="Générateur de système de couleurs")
    parser.add_argument('--primary', '-p', required=True, help='Couleur primaire (hex)')
    parser.add_argument('--mood', '-m', default='neutral',
                       choices=['neutral', 'professional', 'creative', 'energetic', 'warm', 'cool'],
                       help='Ambiance de la palette')
    parser.add_argument('--output', '-o', default='color_system',
                       help='Nom de base pour les fichiers de sortie')
    parser.add_argument('--format', '-f', default='all',
                       choices=['json', 'css', 'scss', 'all'],
                       help='Format de sortie')

    args = parser.parse_args()

    # Validation de la couleur hex
    if not (args.primary.startswith('#') and len(args.primary) == 7):
        print("Erreur: La couleur primaire doit être au format hex (#RRGGBB)")
        sys.exit(1)

    # Génération du système
    color_system = ColorSystem(args.primary, args.mood)

    # Vérification accessibilité
    contrasts = color_system.check_accessibility()

    # Génération des fichiers de sortie
    base_name = args.output

    if args.format in ['json', 'all']:
        # Export JSON
        output_data = {
            'primary_color': args.primary,
            'mood': args.mood,
            'palette': color_system.palette,
            'accessibility': {
                'contrast_ratios': contrasts,
                'wcag_compliance': {
                    'AA': all(ratio >= 4.5 for ratio in contrasts.values()),
                    'AAA': all(ratio >= 7.0 for ratio in contrasts.values())
                }
            }
        }

        with open(f'{base_name}.json', 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

    if args.format in ['css', 'all']:
        # Export CSS
        css_content = generate_css_variables(color_system.palette)

        with open(f'{base_name}.css', 'w', encoding='utf-8') as f:
            f.write(css_content)

    if args.format in ['scss', 'all']:
        # Export SCSS
        scss_content = generate_scss_mixin(color_system.palette)

        with open(f'{base_name}.scss', 'w', encoding='utf-8') as f:
            f.write(scss_content)

    # Rapport console
    print(f"\n🎨 Système de couleurs généré pour {args.mood}")
    print(f"📁 Fichiers créés: {base_name}.*")
    print("
Couleur primaire:"    print(f"  {args.primary}")

    print("
Palette générée:")
    for shade, color in color_system.palette['primary'].items():
        print(f"  Primary {shade}: {color}")

    print("
Accessibilité:")
    for test, ratio in contrasts.items():
        status = "✅" if ratio >= 4.5 else "❌"
        print(f"  {status} {test}: {ratio:.2f}")

    if all(ratio >= 4.5 for ratio in contrasts.values()):
        print("\n🎉 WCAG AA compliant!")
    else:
        print("\n⚠️  Amélioration du contraste recommandée")

if __name__ == "__main__":
    main()
