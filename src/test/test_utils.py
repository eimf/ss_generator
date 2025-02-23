import unittest

from textnode import TextNode, TextType
import utils

class TestUtilsTextNodeToHTML(unittest.TestCase):
    # text_node_to_html_node
    def test_text_node_to_html_node_TEXT(self):
        text_node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        html_node = utils.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), 'This is a text node')
    
    def test_text_node_to_html_node_BOLD(self):
        text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        html_node = utils.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b>This is a text node</b>')

    def test_text_node_to_html_node_ITALIC(self):
        text_node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        html_node = utils.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<i>This is a text node</i>')

    def test_text_node_to_html_node_CODE(self):
        text_node = TextNode("This is a text node", TextType.CODE, "https://www.boot.dev")
        html_node = utils.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<code>This is a text node</code>')
        
    def test_text_node_to_html_node_LINK(self):
        text_node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        html_node = utils.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">This is a text node</a>')

    def test_text_node_to_html_node_IMAGE(self):
        text_node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        html_node = utils.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.boot.dev" alt="This is a text node"></img>')

class TestUtilsSplitNodeDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_mid_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = utils.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])

    def test_split_nodes_delimiter_end_block(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        new_nodes = utils.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE)])

    def test_split_nodes_delimiter_start_block(self):
        node = TextNode("`code block` word", TextType.TEXT)
        new_nodes = utils.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])

class TestUtilsExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(utils.extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

class TestUtilsMisellanious(unittest.TestCase):
    def test_tuple_arr_into_dict(self):
        array_of_tuples = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(utils.tuple_arr_into_dict(array_of_tuples), {"rick roll": "https://i.imgur.com/aKaOqIh.gif", "obi wan": "https://i.imgur.com/fJRm4Vk.jpeg"})

if __name__ == "__main__":
    import sys
    # unittest.main(argv=sys.argv[:1] + ['TestMain.test_split_nodes_delimiter_start_block'])
    # unittest.main(argv=sys.argv[:1] + ['TestUtilsExtractMarkdownImages'])
    unittest.main(argv=sys.argv[:1] + ['TestUtilsMisellanious'])
    unittest.main()
