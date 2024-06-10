from textnode import TextNode
import re


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        elif node.text_type == text_type_text:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                text_type_part = text_type if i % 2 == 1 else text_type_text
                if part.strip():
                    new_nodes.append(TextNode(part, text_type_part))
        else:
            if node.text.strip():
                new_nodes.append(TextNode(node.text, 'text'))
    return new_nodes

def extract_markdown_images(text):
    list_tuple = []
    find_regex = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    for i in find_regex:
        list_tuple.append((i))
    return list_tuple

def extract_markdown_links(text):
    list_tuple = []
    find_regex = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    for i in find_regex:
        list_tuple.append((i))
    return list_tuple

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if  node.text_type == text_type_text:
            parts = node.text.split("![")
            new_nodes.append(TextNode(parts[0], text_type_text))
            for part in parts[1:]:
                image_and_rest = part.split(")", 1)
                alt_text, url = image_and_rest[0].split("](", 1)
                new_nodes.append(TextNode(alt_text, text_type_image, url))
                if len(image_and_rest) == 2 and image_and_rest[1].strip():
                    new_nodes.append(TextNode(image_and_rest[1], text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            parts = node.text.split("[")
            new_nodes.append(TextNode(parts[0], "text"))
            for part in parts[1:]:
                link_and_rest = part.split(")", 1)
                text, url = link_and_rest[0].split("](", 1)
                new_nodes.append(TextNode(text, "link", url))
                if len(link_and_rest) == 2 and link_and_rest[1].strip():
                    new_nodes.append(TextNode(link_and_rest[1], text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes



def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes