import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown.split("\n")
    for block in blocks:
        block = block.strip()
        if block.startswith('# '):
            content = block[2:]
            if content:
                return content
    #raise Exception("No h1 tag in markdown")
    return None

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}.')
    with open(from_path, 'r') as file:
        markdown_content = file.read()
        
    with open(template_path, 'r') as files:
        template = files.read()
    content_node = markdown_to_html_node(markdown_content)
    content = content_node.to_html()
    title = extract_title(markdown_content)

    with open(dest_path, "w") as f:
        f.write(template.replace("{{ Title }}", title).replace("{{ Content }}", content ))

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isfile(from_path):
            if Path(from_path).suffix == ".md":
                dest_path = os.path.join(dest_dir_path, f"{Path(from_path).stem}.html")
                generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            new_dest_dir_path = os.path.join(dest_dir_path, filename)
            generate_pages_recursive(from_path, template_path, new_dest_dir_path)