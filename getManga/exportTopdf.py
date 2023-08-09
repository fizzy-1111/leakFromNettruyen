import os
from PIL import Image

# Step 1: List the images in the folder
image_folder = "chapter1"
image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Step 2: Generate a Markdown file with image references
markdown_content = ""
for image_file in image_files:
    markdown_content += f"![{image_file}]({os.path.join(image_folder, image_file)})\n"

markdown_file = "chapter_1_images.md"
with open(markdown_file, "w", encoding="utf-8") as file:
    file.write(markdown_content)

print(f"Markdown file '{markdown_file}' generated.")

# Step 3: Convert Markdown to PDF using Pandoc
output_pdf = "chapter_1_images.pdf"
os.system(f"pandoc {markdown_file} -o {output_pdf}")

print(f"PDF file '{output_pdf}' generated.")
