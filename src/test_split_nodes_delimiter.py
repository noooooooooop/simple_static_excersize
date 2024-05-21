import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestMain(unittest.TestCase):
    def test_delimiter_1(self):
        nodes = split_nodes_delimiter(TextNode("# This is a *test emphasizing* something", "text"), "*", "bold")

        self.assertEqual(nodes, [
            TextNode("# This is a ", "text"),
            TextNode("test emphasizing", "bold"),
            TextNode(" something", "text"),
        ])

    def test_delimiter_2(self):
        nodes = split_nodes_delimiter(TextNode("# This is a **test emphasizing** something", "text"), "**", "italic")

        self.assertEqual(nodes, [
            TextNode("# This is a ", "text"),
            TextNode("test emphasizing", "italic"),
            TextNode(" something", "text"),
        ])

    def test_delimiter_3(self):
        nodes = split_nodes_delimiter(TextNode("# This is a `code block` test", "text"), "`", "code")

        self.assertEqual(nodes, [
            TextNode("# This is a ", "text"),
            TextNode("code block", "code"),
            TextNode(" test", "text"),
        ])

    def test_delimiter_4(self):
        nodes = split_nodes_delimiter(TextNode("# This is a `code block` and a *bold term* and an **italic term**", "text"), "`", "code")
        nodes = split_nodes_delimiter(nodes, "**", "italic")
        nodes = split_nodes_delimiter(nodes, "*", "bold")

        self.assertEqual(nodes, [
            TextNode("# This is a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and a ", "text"),
            TextNode("bold term", "bold"),
            TextNode(" and an ", "text"),
            TextNode("italic term", "italic"),
        ])

if __name__ == "__main__":
    unittest.main()
