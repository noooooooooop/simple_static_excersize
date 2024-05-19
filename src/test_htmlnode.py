import unittest

from htmlnode import HTMLNode, LeafNode

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node = HTMLNode("a", "asdfasfd", HTMLNode("p", "asdfadsf"), {"href": "asdfadsf"})
        node2 = HTMLNode("a", "asdfasfd", HTMLNode("p", "asdfadsf"), {"href": "asdfadsf"})
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = HTMLNode("div", children=[HTMLNode("div"), HTMLNode("a")])
        node2 = HTMLNode("div", children=[HTMLNode("div"), HTMLNode("a")])
        self.assertEqual(node, node2)

    def test_not_eq_1(self):
        node = HTMLNode("div")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = HTMLNode("div", children=[HTMLNode("div"), HTMLNode("a")])
        node2 = HTMLNode("div")
        self.assertNotEqual(node, node2)

    def test_valid_1(self):
        try:
            node = HTMLNode("test", "asdf", HTMLNode("div"))
        except Exception:
            self.fail("Setting HTML Node as a child should not fail")

    def test_invalid_1(self):
        self.assertRaises(ValueError, lambda: HTMLNode("test", "asdf", True))

    def test_render_leafnode_1(self):
        html = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(html, "<p>This is a paragraph of text.</p>")

    def test_render_leafnode_2(self):
        html = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(html, "<a href=\"https://www.google.com\">Click me!</a>")

    def test_render_leafnode_error_1(self):
        self.assertRaises(ValueError, lambda: LeafNode("p"))


if __name__ == "__main__":
    unittest.main()
