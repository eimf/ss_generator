import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "paragraph", "id": "123"})
        self.assertEqual(node.props_to_html(), ' class="paragraph" id="123"')

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "paragraph"})
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, [], {'class': 'paragraph'})")

if __name__ == '__main__':
    unittest.main()