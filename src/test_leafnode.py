import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999

class TestHTMLNode(unittest.TestCase):
    def test_render_leafnode_1(self):
        html = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(html, "<p>This is a paragraph of text.</p>")

    def test_render_leafnode_2(self):
        html = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(html, "<a href=\"https://www.google.com\">Click me!</a>")

    def test_render_leafnode_3(self):
        html = LeafNode(
            "img",
            props={"src": "path/to/some/image.png", "alt": "The image didn't load =( ..."},
            self_closing=True
        ).to_html()

        self.assertEqual(html, "<img src=\"path/to/some/image.png\" alt=\"The image didn't load =( ...\" />")

if __name__ == "__main__":
    unittest.main()
