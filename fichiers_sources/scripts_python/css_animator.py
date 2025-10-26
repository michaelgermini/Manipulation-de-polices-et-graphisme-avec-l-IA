#!/usr/bin/env python3
"""
Générateur d'animations CSS à partir de descriptions textuelles
Usage: python css_animator.py --description "fade in with bounce" --element ".logo" --duration 2s

Génère automatiquement du code CSS d'animation basé sur des descriptions en langage naturel
"""

import argparse
import json
import re
from pathlib import Path

class CSSAnimationGenerator:
    def __init__(self):
        self.animation_templates = {
            'fade': self._generate_fade_animation,
            'slide': self._generate_slide_animation,
            'bounce': self._generate_bounce_animation,
            'rotate': self._generate_rotate_animation,
            'scale': self._generate_scale_animation,
            'typewriter': self._generate_typewriter_animation,
            'glow': self._generate_glow_animation,
            'shake': self._generate_shake_animation,
            'pulse': self._generate_pulse_animation,
            'morph': self._generate_morph_animation
        }

        self.easings = {
            'ease': 'ease',
            'linear': 'linear',
            'ease-in': 'ease-in',
            'ease-out': 'ease-out',
            'ease-in-out': 'ease-in-out',
            'bounce': 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
            'elastic': 'cubic-bezier(0.175, 0.885, 0.32, 1.275)'
        }

    def parse_description(self, description):
        """Parse une description textuelle pour extraire les paramètres d'animation"""
        params = {
            'effects': [],
            'direction': None,
            'duration': '1s',
            'easing': 'ease',
            'delay': '0s',
            'repeat': '1',
            'direction': 'normal',
            'fill_mode': 'forwards'
        }

        desc_lower = description.lower()

        # Détection des effets
        for effect in self.animation_templates.keys():
            if effect in desc_lower:
                params['effects'].append(effect)

        # Détection de la direction
        directions = ['up', 'down', 'left', 'right', 'center']
        for direction in directions:
            if direction in desc_lower:
                params['direction'] = direction
                break

        # Détection de la durée
        duration_match = re.search(r'(\d+(?:\.\d+)?)\s*(s|ms)', desc_lower)
        if duration_match:
            params['duration'] = f"{duration_match.group(1)}{duration_match.group(2)}"

        # Détection du timing
        for easing_name, easing_value in self.easings.items():
            if easing_name in desc_lower:
                params['easing'] = easing_value
                break

        # Détection du délai
        delay_match = re.search(r'(\d+(?:\.\d+)?)\s*(s|ms)\s*(?:delay|after)', desc_lower)
        if delay_match:
            params['delay'] = f"{delay_match.group(1)}{delay_match.group(2)}"

        # Détection de la répétition
        if 'infinite' in desc_lower or 'loop' in desc_lower:
            params['repeat'] = 'infinite'

        return params

    def generate_animation_css(self, element_selector, animation_params):
        """Génère le code CSS complet pour une animation"""
        animation_name = f"animation_{len(animation_params['effects'])}_{hash(str(animation_params)) % 1000}"

        css = f"""/* Animation générée: {', '.join(animation_params['effects'])} */
@keyframes {animation_name} {{
"""

        # Génération des keyframes pour chaque effet
        all_keyframes = []
        for effect in animation_params['effects']:
            if effect in self.animation_templates:
                keyframes = self.animation_templates[effect](animation_params)
                all_keyframes.extend(keyframes)

        # Dédoublonnement et tri des keyframes
        unique_keyframes = {}
        for kf in all_keyframes:
            percentage = kf['percentage']
            if percentage not in unique_keyframes:
                unique_keyframes[percentage] = {}
            unique_keyframes[percentage].update(kf['properties'])

        # Tri par pourcentage
        for percentage in sorted(unique_keyframes.keys(), key=lambda x: float(x.rstrip('%'))):
            css += f"  {percentage} {{\n"
            for prop, value in unique_keyframes[percentage].items():
                css += f"    {prop}: {value};\n"
            css += "  }\n"

        css += "}\n\n"

        # Règles CSS pour l'élément
        css += f"{element_selector} {{\n"
        css += f"  animation: {animation_name} {animation_params['duration']} {animation_params['easing']} {animation_params['delay']} {animation_params['repeat']} {animation_params['direction']} {animation_params['fill_mode']};\n"
        css += "}\n"

        return css

    def _generate_fade_animation(self, params):
        """Génère une animation de fondu"""
        keyframes = [
            {'percentage': '0%', 'properties': {'opacity': '0'}},
            {'percentage': '100%', 'properties': {'opacity': '1'}}
        ]

        if params.get('direction') == 'out':
            keyframes.reverse()

        return keyframes

    def _generate_slide_animation(self, params):
        """Génère une animation de glissement"""
        direction = params.get('direction', 'left')

        # Positions de départ selon la direction
        start_positions = {
            'left': {'transform': 'translateX(-100%)'},
            'right': {'transform': 'translateX(100%)'},
            'up': {'transform': 'translateY(-100%)'},
            'down': {'transform': 'translateY(100%)'},
            'center': {'transform': 'translateX(-50%) scale(0.8)'}
        }

        keyframes = [
            {'percentage': '0%', 'properties': start_positions.get(direction, start_positions['left'])},
            {'percentage': '100%', 'properties': {'transform': 'translateX(0) translateY(0) scale(1)'}}
        ]

        return keyframes

    def _generate_bounce_animation(self, params):
        """Génère une animation de rebond"""
        keyframes = [
            {'percentage': '0%', 'properties': {'transform': 'translateY(0)'}},
            {'percentage': '20%', 'properties': {'transform': 'translateY(-30px)'}},
            {'percentage': '40%', 'properties': {'transform': 'translateY(-30px)'}},
            {'percentage': '60%', 'properties': {'transform': 'translateY(-15px)'}},
            {'percentage': '80%', 'properties': {'transform': 'translateY(-15px)'}},
            {'percentage': '100%', 'properties': {'transform': 'translateY(0)'}}
        ]

        if params.get('direction') in ['down', 'right']:
            # Inversion pour les rebonds vers le bas/droite
            for kf in keyframes:
                if 'translateY' in kf['properties']:
                    translate_val = kf['properties']['translateY']
                    if translate_val.startswith('-'):
                        kf['properties']['translateY'] = translate_val[1:]  # Supprimer le -
                    else:
                        kf['properties']['translateY'] = '-' + translate_val

        return keyframes

    def _generate_rotate_animation(self, params):
        """Génère une animation de rotation"""
        rotation_amount = 360  # Rotation complète par défaut

        # Détection d'angles spécifiques
        angle_match = re.search(r'(\d+)(?:deg|degrees?)', params.get('description', '').lower())
        if angle_match:
            rotation_amount = int(angle_match.group(1))

        keyframes = [
            {'percentage': '0%', 'properties': {'transform': 'rotate(0deg)'}},
            {'percentage': '100%', 'properties': {'transform': f'rotate({rotation_amount}deg)'}}
        ]

        return keyframes

    def _generate_scale_animation(self, params):
        """Génère une animation d'échelle"""
        scale_start = '0.1'  # Très petit par défaut
        scale_end = '1'  # Taille normale

        # Détection d'échelles spécifiques
        scale_match = re.search(r'scale\s*(?:from\s*)?(\d+(?:\.\d+)?)', params.get('description', '').lower())
        if scale_match:
            scale_start = scale_match.group(1)

        keyframes = [
            {'percentage': '0%', 'properties': {'transform': f'scale({scale_start})'}},
            {'percentage': '100%', 'properties': {'transform': f'scale({scale_end})'}}
        ]

        return keyframes

    def _generate_typewriter_animation(self, params):
        """Génère une animation d'apparition lettre par lettre"""
        # Cette animation nécessite un élément avec data-text
        keyframes = [
            {'percentage': '0%', 'properties': {'width': '0'}},
            {'percentage': '100%', 'properties': {'width': '100%'}}
        ]

        return keyframes

    def _generate_glow_animation(self, params):
        """Génère une animation de lueur"""
        keyframes = [
            {'percentage': '0%', 'properties': {
                'text-shadow': '0 0 5px currentColor',
                'filter': 'brightness(1)'
            }},
            {'percentage': '50%', 'properties': {
                'text-shadow': '0 0 20px currentColor, 0 0 30px currentColor',
                'filter': 'brightness(1.2)'
            }},
            {'percentage': '100%', 'properties': {
                'text-shadow': '0 0 5px currentColor',
                'filter': 'brightness(1)'
            }}
        ]

        return keyframes

    def _generate_shake_animation(self, params):
        """Génère une animation de tremblement"""
        keyframes = []
        for i in range(11):  # 0% à 100% par pas de 10%
            percentage = f"{i * 10}%"

            if i % 2 == 0:
                properties = {'transform': 'translateX(0)'}
            else:
                offset = 5 if i < 5 else -5
                properties = {'transform': f'translateX({offset}px)'}

            keyframes.append({'percentage': percentage, 'properties': properties})

        return keyframes

    def _generate_pulse_animation(self, params):
        """Génère une animation de pulsation"""
        keyframes = [
            {'percentage': '0%', 'properties': {'transform': 'scale(1)'}},
            {'percentage': '50%', 'properties': {'transform': 'scale(1.1)'}},
            {'percentage': '100%', 'properties': {'transform': 'scale(1)'}}
        ]

        return keyframes

    def _generate_morph_animation(self, params):
        """Génère une animation de transformation de forme"""
        # Animation de base pour morphing
        keyframes = [
            {'percentage': '0%', 'properties': {'border-radius': '50%', 'transform': 'rotate(0deg)'}},
            {'percentage': '50%', 'properties': {'border-radius': '10%', 'transform': 'rotate(180deg)'}},
            {'percentage': '100%', 'properties': {'border-radius': '50%', 'transform': 'rotate(360deg)'}}
        ]

        return keyframes

    def generate_multiple_animations(self, descriptions, element_selector):
        """Génère plusieurs animations à partir d'une liste de descriptions"""
        all_css = []
        animation_sequence = []

        for i, description in enumerate(descriptions):
            params = self.parse_description(description)

            # Ajout d'un délai séquentiel si multiple animations
            if i > 0:
                params['delay'] = f"{i * 0.5}s"

            css = self.generate_animation_css(f"{element_selector}_{i}", params)
            all_css.append(css)

            animation_sequence.append({
                'description': description,
                'params': params,
                'css_selector': f"{element_selector}_{i}"
            })

        return {
            'css': '\n'.join(all_css),
            'sequence': animation_sequence
        }

    def generate_responsive_animations(self, base_css, breakpoints=None):
        """Génère des animations responsive"""
        if not breakpoints:
            breakpoints = {
                'tablet': '768px',
                'mobile': '480px'
            }

        responsive_css = "/* Animations responsive */\n"

        # Animation de base
        responsive_css += base_css + "\n"

        # Adaptations pour différents écrans
        for device, breakpoint in breakpoints.items():
            responsive_css += f"@media (max-width: {breakpoint}) {{\n"

            if device == 'mobile':
                # Animations plus courtes sur mobile
                responsive_css += "  [class*='animation_'] {\n"
                responsive_css += "    animation-duration: calc(var(--animation-duration) * 0.7) !important;\n"
                responsive_css += "  }\n"

            elif device == 'tablet':
                # Animations modérées sur tablette
                responsive_css += "  [class*='animation_'] {\n"
                responsive_css += "    animation-duration: calc(var(--animation-duration) * 0.85) !important;\n"
                responsive_css += "  }\n"

            responsive_css += "}\n\n"

        return responsive_css

    def generate_html_demo(self, css_content, element_selector='.demo-element'):
        """Génère une page HTML de démonstration"""
        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Démonstration d'animation CSS générée</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}

        .demo-container {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 2rem;
            margin: 2rem 0;
            backdrop-filter: blur(10px);
        }}

        {element_selector} {{
            display: inline-block;
            padding: 1rem 2rem;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            font-size: 1.2rem;
            font-weight: bold;
            margin: 1rem;
            cursor: pointer;
            transition: transform 0.3s ease;
        }}

        {element_selector}:hover {{
            transform: scale(1.05);
        }}

        .controls {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 5px;
            padding: 1rem;
            margin: 1rem 0;
        }}

        button {{
            background: #4CAF50;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 3px;
            cursor: pointer;
            margin: 0.25rem;
        }}

        button:hover {{
            background: #45a049;
        }}

        .code-display {{
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 1rem;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
        }}

        {css_content}
    </style>
</head>
<body>
    <h1>🎬 Démonstration d'animation CSS</h1>

    <div class="demo-container">
        <h2>Animation générée</h2>
        <div id="demoArea">
            <div class="demo-element">Animation Demo</div>
        </div>

        <div class="controls">
            <button onclick="restartAnimation()">🔄 Redémarrer</button>
            <button onclick="slowMotion()">🐌 Ralenti</button>
            <button onclick="normalSpeed()">⚡ Vitesse normale</button>
        </div>
    </div>

    <div class="demo-container">
        <h2>💻 Code CSS généré</h2>
        <div class="code-display">{self._escape_html(css_content)}</div>
    </div>

    <script>
        function restartAnimation() {{
            const element = document.querySelector('.demo-element');
            element.style.animation = 'none';
            setTimeout(() => {{
                element.style.animation = '';
            }}, 100);
        }}

        function slowMotion() {{
            document.documentElement.style.setProperty('--animation-duration', '3s');
        }}

        function normalSpeed() {{
            document.documentElement.style.setProperty('--animation-duration', '1s');
        }}

        // Rejouer automatiquement l'animation
        setInterval(restartAnimation, 5000);
    </script>
</body>
</html>"""

        return html

    def _escape_html(self, text):
        """Échappe les caractères HTML"""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;')
                   .replace("'", '&#39;'))

def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(description="Générateur d'animations CSS")
    parser.add_argument('--description', '-d', required=True, help='Description de l\'animation (ex: "fade in with bounce from left")')
    parser.add_argument('--element', '-e', default='.animated-element', help='Sélecteur CSS de l\'élément à animer')
    parser.add_argument('--duration', default='1s', help='Durée de l\'animation')
    parser.add_argument('--output', '-o', default='animation.css', help='Fichier CSS de sortie')
    parser.add_argument('--html-demo', default='animation_demo.html', help='Fichier HTML de démonstration')
    parser.add_argument('--responsive', action='store_true', help='Générer des animations responsive')
    parser.add_argument('--multiple', help='Descriptions multiples séparées par des points-virgules')

    args = parser.parse_args()

    print("🎬 Générateur d'animations CSS")
    print("=" * 40)

    generator = CSSAnimationGenerator()

    if args.multiple:
        # Animations multiples
        descriptions = [desc.strip() for desc in args.multiple.split(';')]
        result = generator.generate_multiple_animations(descriptions, args.element)

        css_content = result['css']

        print(f"📝 {len(descriptions)} animations générées:")
        for i, anim in enumerate(result['sequence']):
            print(f"  {i+1}. {anim['description']}")
    else:
        # Animation unique
        params = generator.parse_description(args.description)
        params['duration'] = args.duration

        css_content = generator.generate_animation_css(args.element, params)

        print(f"📝 Animation: {args.description}")
        print(f"⏱️  Durée: {params['duration']}")
        print(f"🎯 Easing: {params['easing']}")
        print(f"📍 Effets: {', '.join(params['effects'])}")

    # Animation responsive si demandée
    if args.responsive:
        css_content = generator.generate_responsive_animations(css_content)

    # Sauvegarde CSS
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(css_content)

    # Génération démo HTML
    html_content = generator.generate_html_demo(css_content, args.element)

    with open(args.html_demo, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("
✅ Fichiers générés:"    print(f"  📄 {args.output}")
    print(f"  🌐 {args.html_demo}")

    print("
💡 Utilisation:"    print(f"  1. Ouvrez {args.html_demo} dans un navigateur")
    print(f"  2. Copiez le CSS de {args.output} dans votre projet")
    print(f"  3. Appliquez la classe à vos éléments HTML")

    print("
🎨 Exemples de descriptions:")
    print("  - 'fade in from left'")
    print("  - 'bounce in with glow effect'")
    print("  - 'slide up and rotate 180 degrees'")
    print("  - 'typewriter effect with pulse'")
    print("  - 'scale up from center with elastic easing'")

if __name__ == "__main__":
    main()
