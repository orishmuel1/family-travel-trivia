#!/usr/bin/env python3
"""
PROJECT: Family Travel Trivia Application
FILE: tools/generate_mock_icons.py
PURPOSE: Programmatically draw and export PWA launcher PNG icons (192x192 and 512x512) 
         without external font dependencies.
"""

import os
import sys
import subprocess

def ensure_pillow():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Try using the venv pip if it exists, otherwise fall back to system pip
    venv_pip = os.path.join(base_dir, ".venv", "bin", "pip")
    
    try:
        from PIL import Image, ImageDraw
        return Image, ImageDraw
    except ImportError:
        print("Pillow library is missing. Attempting to install inside virtual environment...")
        if os.path.exists(venv_pip):
            try:
                subprocess.check_call([venv_pip, "install", "pillow"])
                from PIL import Image, ImageDraw
                print("✔ Pillow installed successfully.")
                return Image, ImageDraw
            except Exception as e:
                print(f"Warning: Failed to install Pillow via venv pip: {e}")
        
        # Fallback to general pip installation instructions
        print("Please install the Pillow package by running:")
        print("  .venv/bin/pip install pillow")
        sys.exit(1)


def generate_icon(Image, ImageDraw, size, output_path):
    # Background color: Indigo #6366f1 (RGB: 99, 102, 241)
    img = Image.new('RGB', (size, size), color=(99, 102, 241))
    draw = ImageDraw.Draw(img)
    
    # Draw a white circular shield in the center
    padding = size // 6
    draw.ellipse(
        [padding, padding, size - padding, size - padding], 
        fill=(255, 255, 255)
    )
    
    # Programmatically draw the letter "T" inside the circle (avoids font-file lookup failures)
    center = size // 2
    bar_thickness = size // 8
    bar_length = size // 3
    
    # Horizontal top bar of "T"
    draw.rectangle(
        [
            center - bar_length // 2, 
            center - bar_length // 2, 
            center + bar_length // 2, 
            center - bar_length // 2 + bar_thickness
        ],
        fill=(99, 102, 241)
    )
    
    # Vertical stem of "T"
    draw.rectangle(
        [
            center - bar_thickness // 2, 
            center - bar_length // 2, 
            center + bar_thickness // 2, 
            center + bar_length // 2
        ],
        fill=(99, 102, 241)
    )
    
    # Save the output file
    img.save(output_path, "PNG")
    print(f"✔ Generated launcher icon: docs/{os.path.basename(output_path)} ({size}x{size})")


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(base_dir, "docs")
    
    if not os.path.exists(docs_dir):
        print(f"Error: Target docs/ folder does not exist. Please run compiler.py first.")
        sys.exit(1)

    Image, ImageDraw = ensure_pillow()
    
    # Generate 192x192 and 512x512 icons required by manifest.json
    generate_icon(Image, ImageDraw, 192, os.path.join(docs_dir, "icon-192.png"))
    generate_icon(Image, ImageDraw, 512, os.path.join(docs_dir, "icon-512.png"))
    
    print("\nPWA icons generated successfully!")

if __name__ == "__main__":
    main()
