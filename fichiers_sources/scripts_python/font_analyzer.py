#!/usr/bin/env python3
"""
Analyseur de polices avec FontTools
Usage: python font_analyzer.py font.otf

Génère un rapport complet sur les métriques et caractéristiques d'une police
"""

import sys
import json
from fontTools.ttLib import TTFont
from pathlib import Path

def analyze_font(font_path):
    """Analyse complète d'une police"""
    font = TTFont(font_path)

    # Métriques de base
    metrics = {
        'font_name': get_font_name(font),
        'units_per_em': font['head'].unitsPerEm,
        'ascender': font['hhea'].ascent,
        'descender': font['hhea'].descent,
        'line_gap': font['hhea'].lineGap,
        'x_height': get_x_height(font),
        'cap_height': get_cap_height(font),
        'glyph_count': len(font.getGlyphNames()),
        'character_set': get_character_set(font),
        'openType_features': get_opentype_features(font),
        'font_format': Path(font_path).suffix,
        'file_size': Path(font_path).stat().st_size
    }

    return metrics

def get_font_name(font):
    """Extrait le nom de la police"""
    name_table = font['name']
    return name_table.getName(1, 3, 1, 0x409) or name_table.getName(1, 1, 1, 0x0) or "Unknown"

def get_x_height(font):
    """Estime la hauteur d'x"""
    # Cherche le glyphe 'x' minuscule
    if 'x' in font.getGlyphNames():
        glyph = font['gly'][font.getGlyphNames().index('x')]
        return glyph.yMax if hasattr(glyph, 'yMax') else 0
    return 0

def get_cap_height(font):
    """Estime la hauteur des capitales"""
    # Cherche le glyphe 'H' majuscule
    if 'H' in font.getGlyphNames():
        glyph = font['gly'][font.getGlyphNames().index('H')]
        return glyph.yMax if hasattr(glyph, 'yMax') else 0
    return 0

def get_character_set(font):
    """Extrait le jeu de caractères supporté"""
    cmap = font['cmap'].getBestCmap()
    if cmap:
        return {
            'total_chars': len(cmap),
            'ranges': get_unicode_ranges(cmap),
            'scripts': identify_scripts(cmap)
        }
    return {'total_chars': 0}

def get_unicode_ranges(cmap):
    """Identifie les blocs Unicode supportés"""
    ranges = []
    current_start = None
    current_end = None

    for code in sorted(cmap.keys()):
        if current_start is None:
            current_start = code
            current_end = code
        elif code == current_end + 1:
            current_end = code
        else:
            ranges.append({'start': current_start, 'end': current_end})
            current_start = code
            current_end = code

    if current_start is not None:
        ranges.append({'start': current_start, 'end': current_end})

    return ranges

def identify_scripts(cmap):
    """Identifie les scripts supportés"""
    scripts = set()
    for code in cmap.keys():
        if 0x0000 <= code <= 0x007F:
            scripts.add('Latin Basic')
        elif 0x0080 <= code <= 0x00FF:
            scripts.add('Latin Extended')
        elif 0x0100 <= code <= 0x017F:
            scripts.add('Latin Extended-A')
        elif 0x0180 <= code <= 0x024F:
            scripts.add('Latin Extended-B')
        elif 0x1E00 <= code <= 0x1EFF:
            scripts.add('Latin Extended Additional')
        # Ajouter d'autres scripts selon les besoins
    return list(scripts)

def get_opentype_features(font):
    """Extrait les features OpenType"""
    features = []
    if 'GPOS' in font:
        features.append('Kerning')
    if 'GSUB' in font:
        features.append('Ligatures')
        # Analyser les features disponibles
        if font['GSUB'].table.FeatureList:
            for feature in font['GSUB'].table.FeatureList.FeatureRecord:
                features.append(feature.FeatureTag)

    return list(set(features))

def generate_report(metrics, output_format='json'):
    """Génère un rapport formaté"""
    if output_format == 'json':
        return json.dumps(metrics, indent=2, ensure_ascii=False)
    elif output_format == 'markdown':
        return format_markdown_report(metrics)
    else:
        return format_text_report(metrics)

def format_markdown_report(metrics):
    """Format du rapport en Markdown"""
    report = f"""# Analyse de police : {metrics['font_name']}

## Métriques de base
- **Unités par em** : {metrics['units_per_em']}
- **Ascendante** : {metrics['ascender']}
- **Descendante** : {metrics['descender']}
- **Écart de ligne** : {metrics['line_gap']}
- **Hauteur d'x** : {metrics['x_height']}
- **Hauteur des capitales** : {metrics['cap_height']}

## Jeu de caractères
- **Nombre total de glyphes** : {metrics['glyph_count']}
- **Nombre de caractères** : {metrics['character_set']['total_chars']}
- **Scripts supportés** : {', '.join(metrics['character_set']['scripts'])}

## Features OpenType
{', '.join(metrics['openType_features'])}

## Format et taille
- **Format** : {metrics['font_format']}
- **Taille fichier** : {metrics['file_size']} octets

"""
    return report

def format_text_report(metrics):
    """Format du rapport en texte simple"""
    report = f"""
ANALYSE DE POLICE : {metrics['font_name']}
{'=' * 50}

MÉTRIQUES DE BASE:
  Unités par em: {metrics['units_per_em']}
  Ascendante: {metrics['ascender']}
  Descendante: {metrics['descender']}
  Écart de ligne: {metrics['line_gap']}
  Hauteur d'x: {metrics['x_height']}
  Hauteur des capitales: {metrics['cap_height']}

JEU DE CARACTÈRES:
  Glyphes: {metrics['glyph_count']}
  Caractères: {metrics['character_set']['total_chars']}
  Scripts: {', '.join(metrics['character_set']['scripts'])}

FEATURES OPENTYPE:
  {', '.join(metrics['openType_features'])}

FORMAT: {metrics['font_format']} ({metrics['file_size']} octets)
"""
    return report

def main():
    """Point d'entrée principal"""
    if len(sys.argv) != 2:
        print("Usage: python font_analyzer.py <font_file>")
        sys.exit(1)

    font_path = sys.argv[1]

    if not Path(font_path).exists():
        print(f"Erreur: Le fichier {font_path} n'existe pas")
        sys.exit(1)

    try:
        metrics = analyze_font(font_path)

        # Génération du rapport
        json_report = generate_report(metrics, 'json')
        markdown_report = generate_report(metrics, 'markdown')

        # Sauvegarde des rapports
        base_name = Path(font_path).stem

        with open(f"{base_name}_analysis.json", 'w', encoding='utf-8') as f:
            f.write(json_report)

        with open(f"{base_name}_analysis.md", 'w', encoding='utf-8') as f:
            f.write(markdown_report)

        print(f"Analyse terminée ! Rapports générés :")
        print(f"  - {base_name}_analysis.json")
        print(f"  - {base_name}_analysis.md")

    except Exception as e:
        print(f"Erreur lors de l'analyse : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
