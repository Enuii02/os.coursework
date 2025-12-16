"""
This file isn't part of the coursework.
It is a script to convert markdown syntax from my note taking app (Obsidian)
to markdown syntax that Github accepts.

To run:
python convert.py input.md output.md
"""

import re
import sys
import os

IMAGE_PREFIX = "./images/"

def sanitize_filename(path = "./images"):
    # Replace spaces with underscores in the filename only
    dirname, filename = os.path.split(path)
    filename = filename.replace(" ", "_")
    return os.path.join(dirname, filename)

# converts the embeds
def convert_image_embeds(text):
    """
    Convert Obsidian-style image embeds to GitHub-style markdown,
    replacing spaces in filenames with underscores.
    """

    sanitize_filename()

    # Case 1: ![[path/to/image.png]]
    text = re.sub(
        r'!\[\[([^|\]]+)\]\]',
        lambda m: f'![{os.path.basename(m.group(1))}]({IMAGE_PREFIX}{sanitize_filename(m.group(1))})',
        text
    )

    # Case 2: ![[path/to/image.png|Alt text]]
    text = re.sub(
        r'!\[\[([^|\]]+)\|([^\]]+)\]\]',
        lambda m: f'![{m.group(2)}]({IMAGE_PREFIX}{sanitize_filename(m.group(1))})',
        text
    )

    return text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.md output.md")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as f:
        md = f.read()

    md = convert_image_embeds(md)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Converted: {output_file}")
