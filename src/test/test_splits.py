import unittest

from textnode import TextNode, TextType
from splits import split_nodes_image, split_nodes_link

# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# # [
# #     TextNode("This is text with a link ", TextType.TEXT),
# #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
# #     TextNode(" and ", TextType.TEXT),
# #     TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
# # ]
# class TestSplitsSplitImageNodes(unittest.TestCase):
#     def test_split_nodes_image(self):
#         node = TextNode(
#             "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#             TextType.TEXT,
#         )
#         new_nodes = split_nodes_image([node])
#         # Define the two possible valid outcomes using the node
#         expected_outcome_1 = [
#             TextNode("This is text with a link ", TextType.TEXT),
#             TextNode(" and ", TextType.TEXT),
#             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#             TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
#         ]
#         expected_outcome_2 = [
#             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#             TextNode("This is text with a link ", TextType.TEXT),
#             TextNode(" and ", TextType.TEXT),
#             TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
#         ]
#         # Check if new_nodes matches either of the expected outcomes
#         self.assertTrue(
#             new_nodes == expected_outcome_1 or new_nodes == expected_outcome_2,
#             f"new_nodes did not match any valid outcome. Got: {new_nodes}"
#         )

class TestSplitsSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://www.boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        # Define the two possible valid outcomes
        expected_outcome_1 = [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("link", TextType.LINK, "https://www.boot.dev")
        ]
        expected_outcome_2 = [
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode("This is text with a ", TextType.TEXT)
        ]
        
        # Check if new_nodes matches either of the expected outcomes
        self.assertTrue(
            new_nodes == expected_outcome_1 or new_nodes == expected_outcome_2,
            f"new_nodes did not match any valid outcome. Got: {new_nodes}"
        )
        # node = TextNode("This is text with a [rick roll](https://www.youtube.com/watch?v=dQw4w9WgXcQ) and [obi wan](https://www.youtube.com/watch?v=3ZlDZPYzfm4)", TextType.TEXT)
        # new_nodes = splits.split_nodes_link([node])
        # self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("[rick roll](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", TextType.LINK, "rick roll"), TextNode(" and ", TextType.TEXT), TextNode("[obi wan](https://www.youtube.com/watch?v=3ZlDZPYzfm4)", TextType.LINK, "obi wan")])

if __name__ == "__main__":
    # import sys
    # unittest.main(argv=sys.argv[:1] + ['TestSplitsSplitImageNodes'])
    unittest.main()