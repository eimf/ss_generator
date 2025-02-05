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
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            parts = list(filter(lambda x: x != "", parts))
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def main():
    # TextNode(This is a text node, bold, https://www.boot.dev)
    textNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(textNode)

if __name__ == "__main__":
    main()