import re
import sys

def convert_image_embeds(text):
    # ![[path/to/image.png]]
    text = re.sub(
        r'!\[\[([^|\]]+)\]\]',
        lambda m: f'![{m.group(1).split("/")[-1]}]({m.group(1)})',
        text
    )

    # ![[path/to/image.png|Alt text]]
    text = re.sub(
        r'!\[\[([^|\]]+)\|([^\]]+)\]\]',
        lambda m: f'![{m.group(2)}]({m.group(1)})',
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
