from htmlnode import ParentNode
import re
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks

def block_to_block_type(block):
    if re.match(r'^(#+) ', block):
        return block_type_heading
    elif re.match(r'^```.*?```', block):
        return block_type_code
    elif re.match(r'^>', block):
        return block_type_quote
    elif re.match(r'^[\*\-].*', block):
        return block_type_unordered_list
    elif re.match(r'^[1-9]\d*\. .*', block):
        return block_type_ordered_list
    else:
        return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        content = (block[1:])
        if block_type == block_type_quote:
            html_blocks.append(blockquote_to_html_node(content))
        elif block_type == block_type_heading:
            heading_level = count_hashes_at_beginning(block)
            if heading_level > 1:
                word = content[heading_level - 1:]
            html_blocks.append(heading_to_html_node(word, heading_level))
        elif block_type == block_type_code:
            html_blocks.append(code_html_to_node(content))
        elif block_type == block_type_unordered_list:
            lines = block.split("\n")
            html_blocks.append(list_to_html_node(lines))
        elif block_type == block_type_ordered_list:
            lines = block.split("\n")
            html_blocks.append(list_to_html_node(lines, ordered=True))
        else:
            html_blocks.append(paragraph_to_html_node(block))
    return ParentNode("div", html_blocks, None)



def count_hashes_at_beginning(input_string):
    # Use a regular expression to match consecutive '#' characters at the beginning of the string
    match = re.match(r'^#+ ', input_string)
    if match:
        return len(match.group(0))
    else:
        return 0

def list_to_html_node(items, ordered=False):
    list_tag = "ol" if ordered else "ul"
    list_list = []
    for item in items:
        if ordered == True:
            list_list.append(ParentNode("li", text_to_children(item[2:].strip())))
        else:
            list_list.append(ParentNode("li", text_to_children(item[1:].strip())))
    return ParentNode(list_tag, list_list)

def blockquote_to_html_node(blockquote):
    return ParentNode("blockquote", [ParentNode("p", text_to_children(blockquote))])

def code_html_to_node(code):
    return ParentNode("pre", [ParentNode("code", text_to_children(code))])

def heading_to_html_node(heading, level):
    content = text_to_children(heading)
    return ParentNode(f"h{level}", content)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children