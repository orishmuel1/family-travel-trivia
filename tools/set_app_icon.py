#!/usr/bin/env python3
"""
Switch the PWA app icon between saved candidate designs.
Usage:
    python tools/set_app_icon.py 2   # Set to Option 2 (Family Road Trip)
    python tools/set_app_icon.py 3   # Set to Option 3 (Global Academy)
    python tools/set_app_icon.py 1   # Set to Option 1 (Navigator's Compass)
    python tools/set_app_icon.py 4   # Set to Option 4 (Travel Trivia Pin)
"""
import sys
import os
import re
import json
import subprocess
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "icons")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
MANIFEST_PATH = os.path.join(DOCS_DIR, "manifest.json")
INDEX_PATH = os.path.join(DOCS_DIR, "index.html")
SW_PATH = os.path.join(DOCS_DIR, "sw.js")

ICON_OPTIONS = {
    "1": ("option_1_compass.png", "compass", "Option 1: The Navigator's Golden Compass"),
    "2": ("option_2_roadtrip.png", "roadtrip", "Option 2: The Family Road Trip & Trivia Spark"),
    "3": ("option_3_globe_academy.png", "academy", "Option 3: The Global Academy & Trivia Spark"),
    "4": ("option_4_pin_trivia.png", "pin", "Option 4: The Travel Trivia Pin"),
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ICON_OPTIONS:
        print("Usage: python tools/set_app_icon.py <1|2|3|4>")
        for key, (_, _, desc) in ICON_OPTIONS.items():
            print(f"  {key}: {desc}")
        sys.exit(1)

    choice = sys.argv[1]
    filename, tag, desc = ICON_OPTIONS[choice]
    source_path = os.path.join(ASSETS_DIR, filename)

    if not os.path.exists(source_path):
        print(f"Error: Source icon not found at {source_path}")
        sys.exit(1)

    print(f"Switching app icon to {desc}...")
    img = Image.open(source_path)

    # 1. Export standard icons
    for name in [f"icon-{tag}-512.png", "icon-512.png"]:
        p = os.path.join(DOCS_DIR, name)
        img.resize((512, 512), Image.Resampling.LANCZOS).save(p, format="PNG")
        print(f"  ✔ Updated {name}")

    for name in [f"icon-{tag}-192.png", "icon-192.png"]:
        p = os.path.join(DOCS_DIR, name)
        img.resize((192, 192), Image.Resampling.LANCZOS).save(p, format="PNG")
        print(f"  ✔ Updated {name}")

    # 2. Update manifest.json
    manifest_data = {
        "id": f"family-travel-trivia-app-v{choice}",
        "short_name": "TravelTrivia",
        "name": "Family Road Trip Travel Trivia App",
        "icons": [
            {
                "src": f"icon-{tag}-192.png",
                "type": "image/png",
                "sizes": "192x192",
                "purpose": "any"
            },
            {
                "src": f"icon-{tag}-512.png",
                "type": "image/png",
                "sizes": "512x512",
                "purpose": "any"
            },
            {
                "src": f"icon-{tag}-512.png",
                "type": "image/png",
                "sizes": "512x512",
                "purpose": "maskable"
            }
        ],
        "start_url": "./index.html",
        "scope": "./",
        "background_color": "#0f172a",
        "theme_color": "#6366f1",
        "display": "standalone",
        "orientation": "portrait"
    }
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)
    print("  ✔ Updated docs/manifest.json")

    # 3. Update index.html
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()
    html = re.sub(r'<link rel="manifest" href="manifest\.json\?v=\d+">', f'<link rel="manifest" href="manifest.json?v={choice}">', html)
    html = re.sub(r'icon-[a-z]+-192\.png\?v=\d+', f'icon-{tag}-192.png?v={choice}', html)
    html = re.sub(r'icon-[a-z]+-512\.png\?v=\d+', f'icon-{tag}-512.png?v={choice}', html)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✔ Updated docs/index.html")

    # 4. Update sw.js ASSETS_TO_CACHE
    with open(SW_PATH, "r", encoding="utf-8") as f:
        sw = f.read()
    for icon_name in [f"'./icon-{tag}-192.png'", f"'./icon-{tag}-512.png'"]:
        if icon_name not in sw:
            sw = sw.replace("];", f"  {icon_name},\n];")
    with open(SW_PATH, "w", encoding="utf-8") as f:
        f.write(sw)

    # 5. Run compiler to cache-bust sw.js
    compiler_path = os.path.join(BASE_DIR, "compiler.py")
    python_bin = sys.executable
    subprocess.check_call([python_bin, compiler_path])
    print(f"✔ Successfully switched and cache-busted app icon to: {desc}")

if __name__ == "__main__":
    main()
