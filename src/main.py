from splits import split_nodes_image
from textnode import TextNode, TextType

def main():
    # TextNode(This is a text node, bold, https://www.boot.dev)
    # textNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # node = TextNode("This is text with a [link](https://www.boot.dev)", TextType.TEXT)
    # new_nodes = split_nodes_link([node])
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)

if __name__ == "__main__":
    main()