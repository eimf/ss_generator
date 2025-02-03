import unittest

from textnode import TextNode, TextType
import main

class TestMain(unittest.TestCase):
    # text_node_to_html_node
    def test_text_node_to_html_node_TEXT(self):
        text_node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        html_node = main.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), 'This is a text node')
    
    def test_text_node_to_html_node_BOLD(self):
        text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        html_node = main.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b>This is a text node</b>')

    def test_text_node_to_html_node_ITALIC(self):
        text_node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        html_node = main.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<i>This is a text node</i>')

    def test_text_node_to_html_node_CODE(self):
        text_node = TextNode("This is a text node", TextType.CODE, "https://www.boot.dev")
        html_node = main.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<code>This is a text node</code>')
        
    def test_text_node_to_html_node_LINK(self):
        text_node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        html_node = main.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">This is a text node</a>')

    def test_text_node_to_html_node_IMAGE(self):
        text_node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        html_node = main.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.boot.dev" alt="This is a text node"></img>')

if __name__ == "__main__":
    unittest.main()
