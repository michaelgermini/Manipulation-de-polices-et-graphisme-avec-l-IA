#!/usr/bin/env python3
"""
Optimiseur de polices par lots avec FontTools
Usage: python batch_optimizer.py input_dir/ output_dir/

Optimise automatiquement une collection de polices pour le web et l'impression
"""

import os
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, Options

def optimize_font_for_web(font_path, output_path):
    """Optimise une police pour le web"""
    font = TTFont(font_path)

    # Configuration de la sous-ensemble
    options = Options()
    options.desubroutinize = True
    options.ignore_missing_glyphs = True

    # Sous-ensemble pour les caractères latins de base
    subsetter = Subsetter(options)
    subsetter.populate(glyphs=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    subsetter.subset(font)

    # Sauvegarde optimisée
    font.save(output_path)

def optimize_font_for_print(font_path, output_path):
    """Optimise une police pour l'impression"""
    font = TTFont(font_path)

    # Nettoyage des tables inutiles
    if 'DSIG' in font:
        del font['DSIG']  # Signature digitale pas nécessaire pour print

    # Ajout/optimisation du hinting
    if 'cvt ' not in font:
        # Ajout de hinting basique si absent
        add_basic_hinting(font)

    font.save(output_path)

def add_basic_hinting(font):
    """Ajoute un hinting basique à la police"""
    # Implémentation simplifiée du hinting
    # Dans un vrai projet, utiliser ttfautohint
    pass

def convert_to_woff2(font_path, output_path):
    """Convertit une police en WOFF2"""
    try:
        from fontTools.ttLib.woff2 import compress

        with open(font_path, 'rb') as f:
            font_data = f.read()

        compressed_data = compress(font_data)

        with open(output_path, 'wb') as f:
            f.write(compressed_data)

    except ImportError:
        print("Installation requise: pip install brotli")
        return False

    return True

def process_font_collection(input_dir, output_dir):
    """Traite une collection complète de polices"""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not input_path.exists():
        print(f"Erreur: Le dossier {input_dir} n'existe pas")
        return

    output_path.mkdir(parents=True, exist_ok=True)

    font_extensions = {'.otf', '.ttf', '.woff', '.woff2'}

    processed_fonts = []

    for font_file in input_path.rglob('*'):
        if font_file.suffix.lower() in font_extensions:
            print(f"Traitement: {font_file.name}")

            # Création des sous-dossiers
            web_dir = output_path / 'web'
            print_dir = output_path / 'print'
            woff2_dir = output_path / 'woff2'

            for directory in [web_dir, print_dir, woff2_dir]:
                directory.mkdir(exist_ok=True)

            # Optimisation web
            web_output = web_dir / f"{font_file.stem}_web{font_file.suffix}"
            optimize_font_for_web(str(font_file), str(web_output))

            # Optimisation print
            print_output = print_dir / f"{font_file.stem}_print{font_file.suffix}"
            optimize_font_for_print(str(font_file), str(print_output))

            # Conversion WOFF2
            woff2_output = woff2_dir / f"{font_file.stem}.woff2"
            if convert_to_woff2(str(font_file), str(woff2_output)):
                print(f"  ✓ WOFF2 généré: {woff2_output.name}")

            processed_fonts.append({
                'original': str(font_file),
                'web': str(web_output),
                'print': str(print_output),
                'woff2': str(woff2_output)
            })

    return processed_fonts

def generate_css_web_fonts(fonts_data, css_output):
    """Génère un fichier CSS pour les polices web"""
    css_content = """/* Web Fonts générés automatiquement */
@font-face {
    font-family: 'CustomFont';
    src: url('./woff2/font.woff2') format('woff2'),
         url('./web/font_web.woff') format('woff');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'CustomFont';
    src: url('./woff2/font-bold.woff2') format('woff2'),
         url('./web/font-bold_web.woff') format('woff');
    font-weight: bold;
    font-style: normal;
    font-display: swap;
}
"""

    with open(css_output, 'w', encoding='utf-8') as f:
        f.write(css_content)

    print(f"CSS généré: {css_output}")

def generate_html_test_page(fonts_data, html_output):
    """Génère une page HTML de test"""
    html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test des polices optimisées</title>
    <link rel="stylesheet" href="fonts.css">
    <style>
        body {
            font-family: 'CustomFont', Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
        }
        .test-section {
            margin: 2rem 0;
            padding: 1rem;
            border: 1px solid #ccc;
        }
        .font-weight-normal { font-weight: normal; }
        .font-weight-bold { font-weight: bold; }
        .font-size-small { font-size: 14px; }
        .font-size-large { font-size: 48px; }
    </style>
</head>
<body>
    <h1>Test des polices optimisées</h1>

    <div class="test-section">
        <h2>Police normale</h2>
        <p class="font-weight-normal">Le renard brun rapide saute par-dessus le chien paresseux. 0123456789</p>
        <p class="font-weight-bold">Le renard brun rapide saute par-dessus le chien paresseux. 0123456789</p>
    </div>

    <div class="test-section">
        <h2>Tailles de police</h2>
        <p class="font-size-small">Texte petit - Parfait pour les légendes</p>
        <p>Texte normal - Parfait pour le corps du texte</p>
        <p class="font-size-large">Texte large - Parfait pour les titres</p>
    </div>

    <div class="test-section">
        <h2>Jeu de caractères étendu</h2>
        <p>Àáâäçéèêëïîôöùûüÿ</p>
        <p>ABCDEFGHIJKLMNOPQRSTUVWXYZ</p>
        <p>abcdefghijklmnopqrstuvwxyz</p>
    </div>
</body>
</html>"""

    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Page de test générée: {html_output}")

def main():
    """Point d'entrée principal"""
    if len(sys.argv) != 3:
        print("Usage: python batch_optimizer.py <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    print(f"Optimisation des polices depuis {input_dir} vers {output_dir}")
    print("=" * 60)

    # Traitement des polices
    processed_fonts = process_font_collection(input_dir, output_dir)

    if processed_fonts:
        print(f"\nTraitement terminé: {len(processed_fonts)} polices optimisées")

        # Génération des fichiers d'accompagnement
        css_file = Path(output_dir) / 'fonts.css'
        html_file = Path(output_dir) / 'test.html'

        generate_css_web_fonts(processed_fonts, css_file)
        generate_html_test_page(processed_fonts, html_file)

        print("
Fichiers générés:")
        print(f"  - {len(processed_fonts)} polices optimisées")
        print(f"  - {css_file}")
        print(f"  - {html_file}")

        # Rapport de compression
        total_original = sum(Path(f['original']).stat().st_size for f in processed_fonts)
        total_woff2 = sum(Path(f['woff2']).stat().st_size for f in processed_fonts if Path(f['woff2']).exists())

        if total_woff2 > 0:
            compression_ratio = (1 - total_woff2 / total_original) * 100
            print(f"\nCompression WOFF2: {compression_ratio:.1f}% d".1f"pace économisé")
    else:
        print("Aucune police trouvée à traiter")

if __name__ == "__main__":
    main()
