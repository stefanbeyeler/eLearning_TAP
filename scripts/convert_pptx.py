#!/usr/bin/env python3
"""
Script to convert PowerPoint to Markdown with both syntaxes
"""
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx_to_markdown import pptx_to_markdown

if __name__ == "__main__":
    # Get the project root directory (parent of scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    pptx_path = os.path.join(project_root, "source_documents", "Schulung Grundlagenmodul[52].pptx")
    output_dir = os.path.join(project_root, "markdown")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Create version with HTML build syntax
    print("Creating version for build_html.py...")
    markdown_html = pptx_to_markdown(pptx_path, images_dir="pictures", use_html_syntax=True)
    output_path_html = os.path.join(output_dir, "Schulung_Grundlagenmodul.md")
    with open(output_path_html, 'w', encoding='utf-8') as f:
        f.write(markdown_html)
    print(f"✅ Created: {output_path_html} (for build_html.py)")

    # Create version with standard Markdown syntax for viewing
    print("\nCreating version for Markdown viewers...")
    markdown_std = pptx_to_markdown(pptx_path, images_dir="pictures", use_html_syntax=False)
    output_path_preview = os.path.join(output_dir, "Schulung_Grundlagenmodul_preview.md")
    with open(output_path_preview, 'w', encoding='utf-8') as f:
        f.write(markdown_std)
    print(f"✅ Created: {output_path_preview} (for viewing)")

    print(f"\n📊 Images location: {os.path.join(project_root, 'pictures')}/")
    print(f"📁 Markdown files location: {output_dir}/")
    print(f"📄 Total files generated: 2")
