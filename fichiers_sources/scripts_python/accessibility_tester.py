#!/usr/bin/env python3
"""
Testeur d'accessibilité pour designs et couleurs
Usage: python accessibility_tester.py --colors "#2E5B91,#FFFFFF" --fonts "16px,18px"

Analyse l'accessibilité WCAG 2.1 des combinaisons couleurs/polices
"""

import argparse
import json
import re
from pathlib import Path
import colorsys

class AccessibilityTester:
    def __init__(self):
        self.results = {}
        self.wcag_levels = {
            'A': {'small': 3.0, 'large': 3.0},
            'AA': {'small': 4.5, 'large': 3.0},
            'AAA': {'small': 7.0, 'large': 4.5}
        }

    def parse_colors(self, color_string):
        """Parse une chaîne de couleurs hex"""
        colors = []
        for color in color_string.split(','):
            color = color.strip()
            if color.startswith('#'):
                colors.append(color)
            elif color.lower() in ['black', 'white']:
                colors.append('#000000' if color == 'black' else '#FFFFFF')
        return colors

    def parse_font_sizes(self, font_string):
        """Parse une chaîne de tailles de police"""
        sizes = []
        for size in font_string.split(','):
            size = size.strip()
            # Extraction de la valeur numérique
            match = re.match(r'(\d+(?:\.\d+)?)(px|pt|em|rem)', size)
            if match:
                value, unit = match.groups()
                sizes.append({'value': float(value), 'unit': unit})
        return sizes

    def hex_to_rgb(self, hex_color):
        """Convertit hex en RGB (0-1)"""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0
        return (r, g, b)

    def rgb_to_luminance(self, rgb):
        """Calcule la luminance relative d'une couleur RGB"""
        r, g, b = rgb

        # Conversion RGB vers linear RGB
        def linearize(x):
            return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4

        r = linearize(r)
        g = linearize(g)
        b = linearize(b)

        # Calcul de la luminance
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def calculate_contrast_ratio(self, color1, color2):
        """Calcule le ratio de contraste entre deux couleurs"""
        rgb1 = self.hex_to_rgb(color1)
        rgb2 = self.hex_to_rgb(color2)

        l1 = self.rgb_to_luminance(rgb1)
        l2 = self.rgb_to_luminance(rgb2)

        lighter = max(l1, l2)
        darker = min(l1, l2)

        return (lighter + 0.05) / (darker + 0.05)

    def is_large_text(self, font_size):
        """Détermine si le texte est considéré comme 'large' selon WCAG"""
        if font_size['unit'] in ['px', 'pt']:
            # 18pt = 24px, 14pt = 18.67px
            if font_size['unit'] == 'pt':
                px_size = font_size['value'] * 1.333  # 1pt = 1.333px
            else:
                px_size = font_size['value']

            return px_size >= 18  # 18px ou 14pt
        elif font_size['unit'] in ['em', 'rem']:
            # 1.2em = 19.2px si base 16px
            return font_size['value'] >= 1.2

        return False  # Par défaut, considérer comme small text

    def check_color_accessibility(self, colors, font_sizes):
        """Teste l'accessibilité de toutes les combinaisons couleurs/polices"""
        results = {}

        for i, color1 in enumerate(colors):
            for j, color2 in enumerate(colors):
                if i != j:  # Éviter les combinaisons identiques
                    contrast = self.calculate_contrast_ratio(color1, color2)

                    # Test avec chaque taille de police
                    for font_size in font_sizes:
                        is_large = self.is_large_text(font_size)

                        # Test WCAG compliance
                        compliance = {}
                        for level, thresholds in self.wcag_levels.items():
                            threshold = thresholds['large'] if is_large else thresholds['small']
                            compliance[level] = contrast >= threshold

                        result_key = f"{color1}_on_{color2}_{font_size['value']}{font_size['unit']}"

                        results[result_key] = {
                            'foreground': color1,
                            'background': color2,
                            'contrast_ratio': round(contrast, 2),
                            'font_size': font_size,
                            'is_large_text': is_large,
                            'wcag_compliance': compliance,
                            'overall_compliant': all(compliance.values())
                        }

        return results

    def generate_accessibility_report(self, results):
        """Génère un rapport d'accessibilité détaillé"""
        report = {
            'summary': self._generate_summary(results),
            'detailed_results': results,
            'recommendations': self._generate_recommendations(results),
            'wcag_levels': self.wcag_levels
        }

        return report

    def _generate_summary(self, results):
        """Génère un résumé des résultats"""
        total_combinations = len(results)
        compliant_combinations = sum(1 for r in results.values() if r['overall_compliant'])
        aa_compliant = sum(1 for r in results.values() if r['wcag_compliance']['AA'])
        aaa_compliant = sum(1 for r in results.values() if r['wcag_compliance']['AAA'])

        return {
            'total_combinations_tested': total_combinations,
            'fully_compliant_combinations': compliant_combinations,
            'aa_compliant': aa_compliant,
            'aaa_compliant': aaa_compliant,
            'compliance_percentage': round((compliant_combinations / total_combinations) * 100, 1) if total_combinations > 0 else 0
        }

    def _generate_recommendations(self, results):
        """Génère des recommandations d'amélioration"""
        recommendations = []

        # Identifier les problèmes courants
        low_contrast = [r for r in results.values() if r['contrast_ratio'] < 3.0]
        medium_contrast = [r for r in results.values() if 3.0 <= r['contrast_ratio'] < 4.5]

        if low_contrast:
            recommendations.append({
                'type': 'critical',
                'message': f"{len(low_contrast)} combinaisons ont un contraste très faible (< 3.0)",
                'affected_combinations': [k for k, v in results.items() if v['contrast_ratio'] < 3.0],
                'suggestion': "Considérez des couleurs avec plus de contraste ou augmentez la taille de police"
            })

        if medium_contrast:
            recommendations.append({
                'type': 'warning',
                'message': f"{len(medium_contrast)} combinaisons ne respectent pas WCAG AA",
                'affected_combinations': [k for k, v in results.items() if 3.0 <= v['contrast_ratio'] < 4.5],
                'suggestion': "Augmentez le contraste ou utilisez pour du texte de grande taille uniquement"
            })

        # Recommandations spécifiques par couleur
        color_issues = {}
        for result in results.values():
            if not result['wcag_compliance']['AA']:
                fg = result['foreground']
                bg = result['background']
                if fg not in color_issues:
                    color_issues[fg] = []
                color_issues[fg].append(bg)

        for color, backgrounds in color_issues.items():
            recommendations.append({
                'type': 'color_specific',
                'color': color,
                'issue': f"Ne fonctionne pas bien avec {len(backgrounds)} couleurs de fond",
                'backgrounds': backgrounds,
                'suggestion': "Remplacez cette couleur par une alternative plus contrastée"
            })

        return recommendations

    def test_svg_accessibility(self, svg_file):
        """Teste l'accessibilité d'un fichier SVG"""
        try:
            import xml.etree.ElementTree as ET

            tree = ET.parse(svg_file)
            root = tree.getroot()

            # Extraction des couleurs du SVG
            colors = set()
            for element in root.iter():
                for attr in ['fill', 'stroke']:
                    if attr in element.attrib:
                        color = element.get(attr)
                        if color and color.startswith('#'):
                            colors.add(color)

            # Test des contrastes si texte présent
            text_elements = [elem for elem in root.iter() if elem.tag.endswith('text')]

            svg_results = {
                'colors_found': list(colors),
                'text_elements': len(text_elements),
                'has_colors': len(colors) > 0
            }

            return svg_results

        except Exception as e:
            return {'error': str(e)}

    def generate_css_accessibility_guide(self, results, output_file):
        """Génère un guide CSS pour l'accessibilité"""
        css_guide = """/* Guide d'accessibilité CSS généré automatiquement */
/* Basé sur les tests WCAG 2.1 */

:root {
  /* Couleurs validées */
"""

        # Variables CSS pour les combinaisons conformes
        compliant_combinations = [r for r in results.values() if r['wcag_compliance']['AA']]

        for i, combo in enumerate(compliant_combinations[:10]):  # Top 10
            css_guide += f"  --accessible-combo-{i+1}-fg: {combo['foreground']};\n"
            css_guide += f"  --accessible-combo-{i+1}-bg: {combo['background']};\n"

        css_guide += """
}

/* Classes utilitaires pour texte accessible */
.text-accessible-primary {
  color: var(--accessible-combo-1-fg);
  background-color: var(--accessible-combo-1-bg);
}

.text-accessible-secondary {
  color: var(--accessible-combo-2-fg);
  background-color: var(--accessible-combo-2-bg);
}

/* Media queries pour accessibilité */
@media (prefers-contrast: high) {
  :root {
    --contrast-multiplier: 1.2;
  }
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(css_guide)

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(description="Testeur d'accessibilité WCAG 2.1")
    parser.add_argument('--colors', '-c', required=True, help='Couleurs hex séparées par des virgules (ex: "#000,#fff,#2E5B91")')
    parser.add_argument('--fonts', '-f', default='14px,18px,24px', help='Tailles de police (ex: "14px,18px,24px")')
    parser.add_argument('--output', '-o', default='accessibility_report.json', help='Fichier de sortie du rapport')
    parser.add_argument('--css-guide', default='accessibility_guide.css', help='Fichier CSS d\'accessibilité généré')
    parser.add_argument('--svg', help='Fichier SVG à analyser')

    args = parser.parse_args()

    print("🧐 Test d'accessibilité WCAG 2.1")
    print("=" * 50)

    # Parsing des couleurs et polices
    colors = AccessibilityTester().parse_colors(args.colors)
    font_sizes = AccessibilityTester().parse_font_sizes(args.fonts)

    print(f"🎨 Couleurs testées: {', '.join(colors)}")
    print(f"📝 Tailles de police: {', '.join([f['value']{f['unit'] for f in font_sizes])}")
    print()

    # Test d'accessibilité
    tester = AccessibilityTester()
    results = tester.check_color_accessibility(colors, font_sizes)

    # Génération du rapport
    report = tester.generate_accessibility_report(results)

    # Test SVG si fourni
    if args.svg:
        svg_results = tester.test_svg_accessibility(args.svg)
        report['svg_analysis'] = svg_results

    # Sauvegarde du rapport
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Génération du guide CSS
    tester.generate_css_accessibility_guide(results, args.css_guide)

    # Affichage des résultats
    summary = report['summary']

    print("📊 RÉSUMÉ DES RÉSULTATS:")
    print(f"  Combinaisons testées: {summary['total_combinations_tested']}")
    print(f"  Entièrement conformes: {summary['fully_compliant_combinations']}")
    print(f"  WCAG AA compliant: {summary['aa_compliant']}")
    print(f"  WCAG AAA compliant: {summary['aaa_compliant']}")
    print(f"  Taux de conformité: {summary['compliance_percentage']}%")
    print()

    # Recommandations critiques
    critical_recommendations = [r for r in report['recommendations'] if r['type'] == 'critical']
    if critical_recommendations:
        print("🚨 RECOMMANDATIONS CRITIQUES:")
        for rec in critical_recommendations:
            print(f"  ⚠️  {rec['message']}")
            print(f"     Suggestion: {rec['suggestion']}")
        print()

    # Affichage des meilleures combinaisons
    best_combinations = sorted(results.values(), key=lambda x: x['contrast_ratio'], reverse=True)[:5]

    print("✅ MEILLEURES COMBINAISONS (top 5):")
    for combo in best_combinations:
        level = "✅ AA+" if combo['wcag_compliance']['AAA'] else "✅ AA" if combo['wcag_compliance']['AA'] else "⚠️ A"
        large_text = "(grand texte)" if combo['is_large_text'] else "(petit texte)"
        print(f"  {level} {combo['foreground']} sur {combo['background']} - Ratio: {combo['contrast_ratio']} {large_text}")

    print(f"\n📁 Rapports générés:")
    print(f"  - {args.output} (rapport détaillé JSON)")
    print(f"  - {args.css_guide} (guide CSS d'accessibilité)")

    if summary['compliance_percentage'] >= 80:
        print("\n🎉 Excellent! Votre palette est très accessible.")
    elif summary['compliance_percentage'] >= 50:
        print("\n👍 Bonne accessibilité avec quelques améliorations possibles.")
    else:
        print("\n⚠️  Améliorations nécessaires pour une meilleure accessibilité.")

if __name__ == "__main__":
    main()
