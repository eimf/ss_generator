import textnode as tn

def main():
    # TextNode(This is a text node, bold, https://www.boot.dev)
    textNode = tn.TextNode("This is a text node", tn.TextType.BOLD, "https://www.boot.dev")
    print(textNode)

if __name__ == "__main__":
    main()