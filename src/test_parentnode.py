import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestHTMLNode(unittest.TestCase):
    def test_render_parentnode_1(self):
        html = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()

        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_render_parentnode_2(self):
        html = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                ParentNode("div", [
                    LeafNode("p", "test1"),
                    LeafNode("a", "test2", {"href": "https://www.google.com"}),
                ]),
            ],
        ).to_html()

        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i><div><p>test1</p><a href=\"https://www.google.com\">test2</a></div></p>")


if __name__ == "__main__":
    unittest.main()
