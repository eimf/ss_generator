import re

from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, {})
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, {})
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, {})
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, {})
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Invalid TextType")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        delimiter_count = node.text.count(delimiter)
        if delimiter_count < 2 and delimiter_count % 2 != 0: raise Exception("Invalid open and close delimiter count")
        delimiter_indexes = [m.start() for m in re.finditer(re.escape(delimiter), node.text)]
        substrings = []
        for i in range(0, len(delimiter_indexes), 2):
            substrings.append(node.text[delimiter_indexes[i] + 1:delimiter_indexes[i + 1]])
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            parts = list(filter(lambda x: x != "", parts))
            for part in parts:
                if part in substrings:
                    new_nodes.append(TextNode(part, text_type))
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)