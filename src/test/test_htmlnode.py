import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "paragraph", "id": "123"})
        self.assertEqual(node.props_to_html(), ' class="paragraph" id="123"')

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "paragraph"})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, [], {'class': 'paragraph'})")


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", {"class": "paragraph"})
        self.assertEqual(node.to_html(), '<p class="paragraph">This is a paragraph</p>')

    def test_no_value(self):
        node = LeafNode("p", None, {"class": "paragraph"})
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_no_tag(self):
        node = LeafNode(None, "This is a paragraph", {"class": "paragraph"})
        self.assertEqual(node.to_html(), 'This is a paragraph')

if __name__ == '__main__':
    unittest.main()