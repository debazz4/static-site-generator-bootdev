import unittest

from textnode import (TextNode, split_nodes_delimiter, extract_markdown_links, 
                      extract_markdown_images, split_nodes_image, split_nodes_link,
                      markdown_to_blocks)

text_type_text = "text"
text_type_image = "image"
text_type_link = "link"
class TestTextNode(unittest.TestCase):
    """def setUp(self):
        self.maxDiff = None
    def test_split_nodes_image(self):
        # Create some sample TextNode objects
        node1 = TextNode(
    "This is text with an ![link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
        node2 = TextNode(
    "This is text with an ![first link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
        old_nodes = [node1, node2]

        # Call the split_nodes_image function
        new_nodes = split_nodes_link(old_nodes)

        # Assert the expected output
        expected_new_nodes = [
    TextNode("This is text with an ", text_type_text),
    TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode(
        "second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),
    TextNode("This is text with an ", text_type_text),
    TextNode("first link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode(
        "link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),
]

        self.assertEqual(new_nodes, expected_new_nodes)"""
    def test_markdown_to_blocks(self):
        markdown = """
        This is **bolded** paragraph.

This is another paragraph with *italic* text and `code` here.
This is the same paragraph on a new line.

* This is a list
* with items

        """

        expected_blocks = [
            "This is **bolded** paragraph.",
            "This is another paragraph with *italic* text and `code` here. This is the same paragraph on a new line.",
            "* This is a list",
            "* with items",
        ]
        
        actual_block = markdown_to_blocks(markdown)
        self.assertEqual(actual_block, expected_blocks)



if __name__ == "__main__":
    unittest.main()

    