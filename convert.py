import re
import sys
import os

IMAGE_PREFIX = "./images/"

def convert_image_embeds(text):

    # Case 2 first: ![[path/to/image.png|Alt text]]
    text = re.sub(
        r'!\[\[([^|\]]+)\|([^\]]+)\]\]',
        lambda m: f'![{m.group(2)}]({IMAGE_PREFIX}{m.group(1).replace(" ", "_")})',
        text
    )

    # Case 1: ![[path/to/image.png]]
    text = re.sub(
        r'!\[\[([^|\]]+)\]\]',
        lambda m: f'![{os.path.basename(m.group(1))}]({IMAGE_PREFIX}{m.group(1).replace(" ", "_")})',
        text
    )

    return text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_obsidian_images.py input.md output.md")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    with open(input_file, "r", encoding="utf-8") as f:
        md = f.read()

    md = convert_image_embeds(md)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Converted: {output_file}")
