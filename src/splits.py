import re

from textnode import TextType, TextNode
from utils import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_images(node.text)
            if links:
                for key, value in links:
                    new_nodes.append(TextNode(key, TextType.LINK, value))
                # Regex pattern to match Markdown images
                pattern = r'!\[.*?\]\(.*?\)'

                # Split the text around the links while preserving spaces
                split_text = re.split(pattern, node.text)
                split_text = list(filter(lambda x: x != "", split_text))
                for text in split_text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
        else:
            new_nodes.append(node)
    # print(new_nodes)
    return new_nodes

# build a function that takes a list of TextNodes and returns a list of TextNodes
# node = TextNode("This is text with a [link](https://www.boot.dev)", TextType.TEXT)
# TextNode("This is text with a ", TextType.TEXT), 
# TextNode("link", TextType.LINK, "https://www.boot.dev")
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            if links:
                for key, value in links:
                    new_nodes.append(TextNode(key, TextType.LINK, value))
                # Regex pattern to match Markdown links
                pattern = r'\[.*?\]\(.*?\)'

                # Split the text around the links while preserving spaces
                split_text = re.split(pattern, node.text)
                split_text = list(filter(lambda x: x != "", split_text))
                for text in split_text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes