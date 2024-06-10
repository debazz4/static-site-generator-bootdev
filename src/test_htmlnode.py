import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    """def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="p", props={"href": "https://www.google.com"})
        expected_output = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag="img", props={"href": "https://www.google.com", "alt": "Image"})
        expected_output = ' href="https://www.google.com" alt="Image"'
        self.assertEqual(node.props_to_html(), expected_output)
"""
    """def test_leafnode_with_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_output = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_output)

    def test_leafnode_without_tag(self):
        node = LeafNode(None, "This is a text")
        expected_output = "This is a text"
        self.assertEqual(node.to_html(), expected_output)
    
    def test_leafnode_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_output = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_output)
"""
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>",)
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )
        self.assertEqual(node.to_html(),
                        "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
if __name__ == "__main__":
    unittest.main()