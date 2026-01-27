import argparse
import base64
import os
from datetime import datetime


def data_uri_for_image(filename):
    path = os.path.join(os.getcwd(), "Assets", filename)
    try:
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("ascii")
            return f"data:image/png;base64,{encoded}"
    except Exception:
        return filename


def generate_svg(name, date_str, out_path):
    w = 1600
    h = 1100

    title = "ECHCIC Investment Award 2026"
    subtitle = "Finalist Certificate"

    eton_src = data_uri_for_image("etonlogo.png")
    club_src = data_uri_for_image("ECHCIC.png")
    fm_src = data_uri_for_image("fminstitute_logo.jpeg")
    koyfin_src = data_uri_for_image("koyfin_logo.png")

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{w}" height="{h}" viewBox="0 0 {w} {h}">

<defs>
    <radialGradient id="bgGrad" cx="50%" cy="35%" r="75%">
        <stop offset="0%" stop-color="#f7fffb"/>
        <stop offset="100%" stop-color="#e6f5ec"/>
    </radialGradient>

    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#a7eec9"/>
        <stop offset="100%" stop-color="#2fa76a"/>
    </linearGradient>


    <filter id="softShadow" x="-30%" y="-30%" width="160%" height="160%">
        <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.18"/>
    </filter>


    <pattern id="guilloche" patternUnits="userSpaceOnUse" width="120" height="120">
        <path d="M0 60 H120 M60 0 V120" stroke="#a9d3bd" stroke-opacity="0.10" stroke-width="1"/>
        <circle cx="60" cy="60" r="28" fill="none" stroke="#a9d3bd" stroke-opacity="0.08" stroke-width="1"/>
    </pattern>

</defs>

<rect width="{w}" height="{h}" fill="url(#bgGrad)"/>
<rect x="80" y="80" width="{w - 160}" height="{h - 160}" rx="28" fill="#fffdf6" filter="url(#softShadow)"/>
<rect x="96" y="96" width="{w - 192}" height="{h - 192}" rx="22" fill="none" stroke="url(#goldGrad)" stroke-width="6"/>
<rect x="120" y="120" width="{w - 240}" height="{h - 240}" rx="18" fill="url(#guilloche)" opacity="0.15"/>

<g>
    <!-- Eton Logo (Left) -->
    <image xlink:href="{eton_src}"
           x="200" y="100"
           width="300" height="300"
           preserveAspectRatio="xMidYMid meet"/>

    <!-- Koyfin Logo (Bottom Left) -->
    <image xlink:href="{koyfin_src}"
           x="150" y="{h - 300}"
           width="240" height="240"
           preserveAspectRatio="xMidYMid meet"/>

    <!-- FM Institute Logo (Bottom Right) -->
    <image xlink:href="{fm_src}"
           x="{w - 300}" y="{h - 300}"
           width="180" height="180"
           preserveAspectRatio="xMidYMid meet"/>

    <!-- Club Logo (Right) -->
    <image xlink:href="{club_src}"
           x="{w - 400}" y="190"
           width="180" height="180"
           preserveAspectRatio="xMidYMid meet"/>
</g>

<g>
    <text x="{w/2}" y="420" font-family="Georgia, 'Times New Roman', serif" font-size="48" font-weight="700" text-anchor="middle" fill="#2b2b2b">
        {title}
    </text>
    <text x="{w/2}" y="470" font-family="Georgia, 'Times New Roman', serif" font-size="34" font-weight="500" text-anchor="middle" fill="#2e604d">
        {subtitle}
    </text>
</g>

<g>
    <text x="{w/2}" y="560" font-family="Georgia, 'Times New Roman', serif" font-size="26" text-anchor="middle" fill="#3b5d4f">
        This certifies that
    </text>
    <text x="{w/2}" y="640" font-family="Georgia, 'Times New Roman', serif" font-size="64" font-weight="700" text-anchor="middle" fill="#1f1f1f">
        {name}
    </text>
    <text x="{w/2}" y="700" font-family="Georgia, 'Times New Roman', serif" font-size="26" text-anchor="middle" fill="#3b5d4f">
        was a finalist in the ECHCIC Investment Award 2026
    </text>
</g>


<g>
    <line x1="{w/2 - 180}" y1="{h - 260}" x2="{w/2 + 180}" y2="{h - 260}" stroke="#9fcfb7" stroke-width="2"/>
    <text x="{w/2}" y="{h - 280}" font-family="Georgia, 'Times New Roman', serif" font-size="22" text-anchor="middle" fill="#2e604d">
        Date
    </text>
    <text x="{w/2}" y="{h - 225}" font-family="Georgia, 'Times New Roman', serif" font-size="24" text-anchor="middle" fill="#2b2b2b">
        {date_str}
    </text>
</g>

</svg>
""".strip()

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print(out_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=False, default="Sample Student")
    parser.add_argument("--date", default=None)
    parser.add_argument("--output", default=None)

    args = parser.parse_args()

    date_str = args.date or datetime.today().strftime("%d %B %Y")
    out = args.output or os.path.join(os.getcwd(), "eton_finalist_certificate.svg")

    generate_svg(args.name, date_str, out)


if __name__ == "__main__":
    main()
