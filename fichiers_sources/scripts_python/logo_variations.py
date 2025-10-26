#!/usr/bin/env python3
"""
Générateur de variations de logos
Usage: python logo_variations.py --input logo.svg --variations 5 --output variations/

Génère automatiquement des variations d'un logo avec différents styles, couleurs et compositions
"""

import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import random
import colorsys

class LogoVariationGenerator:
    def __init__(self, input_svg):
        self.input_svg = input_svg
        self.tree = ET.parse(input_svg)
        self.root = self.tree.getroot()
        self.variations = []

    def generate_color_variations(self, base_colors, variation_count=3):
        """Génère des variations de couleurs harmonieuses"""
        variations = []

        for i in range(variation_count):
            variation = {}

            for color_name, hex_color in base_colors.items():
                # Conversion hex vers HSL pour manipulation
                hsl = self._hex_to_hsl(hex_color)

                # Variations subtiles
                if i == 0:
                    # Version plus claire
                    new_hsl = (hsl[0], hsl[1] * 0.8, min(1.0, hsl[2] * 1.2))
                elif i == 1:
                    # Version plus foncée
                    new_hsl = (hsl[0], hsl[1] * 1.2, hsl[2] * 0.8)
                else:
                    # Version avec teinte modifiée
                    new_hsl = ((hsl[0] + 30) % 360, hsl[1], hsl[2])

                variation[color_name] = self._hsl_to_hex(new_hsl)

            variations.append(variation)

        return variations

    def generate_style_variations(self, base_svg, variation_count=3):
        """Génère des variations de style (minimal, outline, gradient, etc.)"""
        variations = []

        for i in range(variation_count):
            variation_svg = ET.fromstring(ET.tostring(base_svg))

            if i == 0:
                # Version outline
                self._apply_outline_style(variation_svg)
            elif i == 1:
                # Version gradient
                self._apply_gradient_style(variation_svg)
            elif i == 2:
                # Version minimal
                self._apply_minimal_style(variation_svg)

            variations.append(variation_svg)

        return variations

    def _apply_outline_style(self, svg):
        """Applique un style outline au SVG"""
        # Supprimer les remplissages
        for element in svg.iter():
            if 'fill' in element.attrib:
                element.set('fill', 'none')
            if 'stroke' not in element.attrib:
                element.set('stroke', '#000000')
                element.set('stroke-width', '2')

    def _apply_gradient_style(self, svg):
        """Applique des dégradés au SVG"""
        defs = ET.SubElement(svg, 'defs')

        # Dégradé principal
        gradient = ET.SubElement(defs, 'linearGradient')
        gradient.set('id', 'mainGradient')
        gradient.set('x1', '0%')
        gradient.set('y1', '0%')
        gradient.set('x2', '100%')
        gradient.set('y2', '100%')

        ET.SubElement(gradient, 'stop', {'offset': '0%', 'style': 'stop-color:#2E5B91;stop-opacity:1'})
        ET.SubElement(gradient, 'stop', {'offset': '100%', 'style': 'stop-color:#1A3A5C;stop-opacity:1'})

        # Appliquer le dégradé
        for element in svg.iter():
            if 'fill' in element.attrib and element.get('fill') != 'none':
                element.set('fill', 'url(#mainGradient)')

    def _apply_minimal_style(self, svg):
        """Applique un style minimal (suppression des détails)"""
        # Simplification des chemins
        for path in svg.iter('{http://www.w3.org/2000/svg}path'):
            # Simplifier les chemins complexes
            if 'd' in path.attrib:
                d = path.get('d')
                if d.count('M') > 2:  # Si plus de 2 points
                    # Garder seulement le contour principal
                    path.set('d', d.split('M')[0] + 'M' + 'M'.join(d.split('M')[:2]))

    def generate_composition_variations(self, base_svg, variation_count=2):
        """Génère des variations de composition (horizontal, vertical, etc.)"""
        variations = []

        for i in range(variation_count):
            variation_svg = ET.fromstring(ET.tostring(base_svg))

            if i == 0:
                # Version horizontale
                self._apply_horizontal_layout(variation_svg)
            elif i == 1:
                # Version compacte
                self._apply_compact_layout(variation_svg)

            variations.append(variation_svg)

        return variations

    def _apply_horizontal_layout(self, svg):
        """Applique une disposition horizontale"""
        # Ajustement de la vue pour format horizontal
        if 'viewBox' in svg.attrib:
            viewbox = svg.get('viewBox').split()
            if len(viewbox) == 4:
                width = float(viewbox[2])
                height = float(viewbox[3])
                # Format horizontal 16:9
                new_width = max(width, height * 1.78)
                new_height = new_width / 1.78
                svg.set('viewBox', f"0 0 {new_width} {new_height}")
                svg.set('width', str(new_width))
                svg.set('height', str(new_height))

    def _apply_compact_layout(self, svg):
        """Applique une disposition compacte (carrée)"""
        if 'viewBox' in svg.attrib:
            viewbox = svg.get('viewBox').split()
            if len(viewbox) == 4:
                size = max(float(viewbox[2]), float(viewbox[3]))
                svg.set('viewBox', f"0 0 {size} {size}")
                svg.set('width', str(size))
                svg.set('height', str(size))

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
            h = s = 0
        else:
            s = diff / (2 - max_val - min_val) if l > 0.5 else diff / (max_val + min_val)

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

    def save_variation(self, svg_element, filename, colors=None):
        """Sauvegarde une variation SVG"""
        if colors:
            # Appliquer les nouvelles couleurs
            self._apply_colors(svg_element, colors)

        # Conversion en string avec déclaration XML
        svg_string = ET.tostring(svg_element, encoding='unicode')

        # Ajout de la déclaration XML
        svg_with_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg_string

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(svg_with_declaration)

    def _apply_colors(self, svg_element, color_mapping):
        """Applique une mapping de couleurs au SVG"""
        # Recherche des éléments avec des couleurs hex
        for element in svg_element.iter():
            for attr in ['fill', 'stroke']:
                if attr in element.attrib:
                    color = element.get(attr)
                    if color.startswith('#'):
                        # Remplacer par la nouvelle couleur si elle existe dans le mapping
                        if color in color_mapping:
                            element.set(attr, color_mapping[color])

    def generate_all_variations(self, output_dir, variation_counts={'color': 3, 'style': 3, 'composition': 2}):
        """Génère toutes les variations demandées"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Extraction des couleurs de base
        base_colors = self._extract_colors()

        # Génération des variations de couleurs
        color_variations = self.generate_color_variations(base_colors, variation_counts['color'])

        # Génération des variations de style
        style_variations = self.generate_style_variations(self.root, variation_counts['style'])

        # Génération des variations de composition
        composition_variations = self.generate_composition_variations(self.root, variation_counts['composition'])

        variation_index = 1

        # Combinaison de toutes les variations
        for color_var in color_variations:
            for style_var in style_variations:
                for comp_var in composition_variations:
                    filename = output_path / f"variation_{variation_index"03d"}.svg"

                    # Appliquer les couleurs à la variation de style
                    working_svg = ET.fromstring(ET.tostring(style_var))

                    self.save_variation(working_svg, filename, color_var)

                    self.variations.append({
                        'index': variation_index,
                        'filename': filename.name,
                        'colors': color_var,
                        'style': 'outline' if 'stroke' in ET.tostring(style_var) else 'filled'
                    })

                    variation_index += 1

        return self.variations

    def _extract_colors(self):
        """Extrait les couleurs utilisées dans le SVG"""
        colors = {}
        color_id = 1

        for element in self.root.iter():
            for attr in ['fill', 'stroke']:
                if attr in element.attrib:
                    color = element.get(attr)
                    if color.startswith('#') and color not in colors:
                        colors[color] = f'color_{color_id}'
                        color_id += 1

        return colors

    def generate_report(self, output_file):
        """Génère un rapport JSON des variations créées"""
        report = {
            'input_file': str(self.input_svg),
            'total_variations': len(self.variations),
            'variations': self.variations,
            'generated_at': Path.cwd().name
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(description="Générateur de variations de logos")
    parser.add_argument('--input', '-i', required=True, help='Fichier SVG d\'entrée')
    parser.add_argument('--output', '-o', default='logo_variations', help='Dossier de sortie')
    parser.add_argument('--variations', '-v', type=int, default=5, help='Nombre de variations par type')
    parser.add_argument('--color-vars', type=int, default=3, help='Nombre de variations de couleurs')
    parser.add_argument('--style-vars', type=int, default=3, help='Nombre de variations de style')
    parser.add_argument('--comp-vars', type=int, default=2, help='Nombre de variations de composition')

    args = parser.parse_args()

    # Validation du fichier d'entrée
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Erreur: Le fichier {args.input} n'existe pas")
        return

    if not args.input.lower().endswith('.svg'):
        print("Erreur: Le fichier d'entrée doit être au format SVG")
        return

    print(f"Génération de variations pour {args.input}")
    print(f"Dossier de sortie: {args.output}")
    print("-" * 50)

    # Génération des variations
    generator = LogoVariationGenerator(args.input)

    variation_counts = {
        'color': args.color_vars,
        'style': args.style_vars,
        'composition': args.comp_vars
    }

    variations = generator.generate_all_variations(args.output, variation_counts)

    # Génération du rapport
    report_file = Path(args.output) / 'variations_report.json'
    generator.generate_report(report_file)

    print(f"✅ {len(variations)} variations générées avec succès !")
    print(f"📊 Rapport détaillé: {report_file}")

    # Affichage d'un résumé
    print("
Variations créées:"    for var in variations[:5]:  # Afficher les 5 premières
        print(f"  - {var['filename']} ({var['style']})")

    if len(variations) > 5:
        print(f"  ... et {len(variations) - 5} autres")

    print("
💡 Conseils d'utilisation:")
    print(f"  - Utilisez les variations comme base pour vos projets")
    print(f"  - Testez chaque variation dans son contexte d'usage")
    print(f"  - Conservez les variations prometteuses pour itération")
    print(f"  - Le rapport JSON contient tous les détails techniques")

if __name__ == "__main__":
    main()
