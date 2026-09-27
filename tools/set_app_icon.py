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
import subprocess
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "icons")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

ICON_OPTIONS = {
    "1": ("option_1_compass.png", "Option 1: The Navigator's Golden Compass"),
    "2": ("option_2_roadtrip.png", "Option 2: The Family Road Trip & Trivia Spark"),
    "3": ("option_3_globe_academy.png", "Option 3: The Global Academy & Trivia Spark"),
    "4": ("option_4_pin_trivia.png", "Option 4: The Travel Trivia Pin"),
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ICON_OPTIONS:
        print("Usage: python tools/set_app_icon.py <1|2|3|4>")
        for key, (_, desc) in ICON_OPTIONS.items():
            print(f"  {key}: {desc}")
        sys.exit(1)

    choice = sys.argv[1]
    filename, desc = ICON_OPTIONS[choice]
    source_path = os.path.join(ASSETS_DIR, filename)

    if not os.path.exists(source_path):
        print(f"Error: Source icon not found at {source_path}")
        sys.exit(1)

    print(f"Switching app icon to {desc}...")
    img = Image.open(source_path)

    # Export 512x512
    p512 = os.path.join(DOCS_DIR, "icon-512.png")
    img.resize((512, 512), Image.Resampling.LANCZOS).save(p512, format="PNG")
    print(f"  ✔ Updated {p512}")

    # Export 192x192
    p192 = os.path.join(DOCS_DIR, "icon-192.png")
    img.resize((192, 192), Image.Resampling.LANCZOS).save(p192, format="PNG")
    print(f"  ✔ Updated {p192}")

    # Run compiler to cache-bust sw.js
    compiler_path = os.path.join(BASE_DIR, "compiler.py")
    python_bin = sys.executable
    subprocess.check_call([python_bin, compiler_path])
    print(f"✔ Successfully switched and cache-busted app icon to: {desc}")

if __name__ == "__main__":
    main()
