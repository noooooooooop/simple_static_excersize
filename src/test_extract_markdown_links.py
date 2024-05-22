import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode
from extract_markdown_links import extract_markdown_links, split_markdown_links

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestMain(unittest.TestCase):
    def test_extract_links_none(self):
        matches = extract_markdown_links(TextNode("# This is an example of something with no link", "text"), is_image=True)

        self.assertEqual(matches, [])

    def test_extract_links_1(self):
        matches = extract_markdown_links(TextNode("# This is a [link](https://www.google.com)", "text"))

        self.assertEqual(matches, [ ("link", "https://www.google.com") ])

    def test_extract_links_2(self):
        matches = extract_markdown_links(TextNode("# This is an ![image](path/to/some.png)", "text"), is_image=True)

        self.assertEqual(matches, [ ("image", "path/to/some.png") ])

    def test_extract_links_3(self):
        matches = extract_markdown_links(TextNode("# This is a [link](https://www.google.com), and this is [another link](https://www.google.com/images), and this ![image](path/to/some.png) should not be extracted", "text"))

        self.assertEqual(matches, [
            ("link", "https://www.google.com"),
            ("another link", "https://www.google.com/images"),
        ])

    def test_extract_links_4(self):
        matches = extract_markdown_links(TextNode("# This is an ![image](path/to/some.png) and this is ![another image](path/to/some/other.png), and this [link](https://www.google.com) should not be extracted", "text"), is_image=True)

        self.assertEqual(matches, [
            ("image", "path/to/some.png"),
            ("another image", "path/to/some/other.png"),
        ])

    def test_split_links_none(self):
        nodes = split_markdown_links(TextNode("# This is an example with no links", "text"))

        self.assertEqual(nodes, [
            TextNode("# This is an example with no links", "text"),
        ])

    def test_split_links_1(self):
        nodes = split_markdown_links(TextNode("# This is a [link](https://www.google.com)", "text"))

        self.assertEqual(nodes, [
            TextNode("# This is a ", "text"),
            TextNode("link", "link", "https://www.google.com"),
        ])

    def test_split_links_2(self):
        nodes = split_markdown_links(TextNode("# This is an ![image](path/to/some.png)", "text"), is_image=True)

        self.assertEqual(nodes, [
            TextNode("# This is an ", "text"),
            TextNode("image", "image", "path/to/some.png"),
        ])

    def test_split_links_3(self):
        nodes = split_markdown_links(TextNode("# This is a [link](https://www.google.com), and this is [another link](https://www.google.com/images), and this ![image](path/to/some.png) should not be extracted", "text"))

        self.assertEqual(nodes, [
            TextNode("# This is a ", "text"),
            TextNode("link", "link", "https://www.google.com"),
            TextNode(", and this is ", "text"),
            TextNode("another link", "link", "https://www.google.com/images"),
            TextNode(", and this ![image](path/to/some.png) should not be extracted", "text"),
        ])

    def test_split_links_4(self):
        nodes = split_markdown_links(TextNode("# This is an ![image](path/to/some.png) and this is ![another image](path/to/some/other.png), and this [link](https://www.google.com) should not be extracted", "text"), is_image=True)

        self.assertEqual(nodes, [
            TextNode("# This is an ", "text"),
            TextNode("image", "image", "path/to/some.png"),
            TextNode(" and this is ", "text"),
            TextNode("another image", "image", "path/to/some/other.png"),
            TextNode(", and this [link](https://www.google.com) should not be extracted", "text"),
        ])

if __name__ == "__main__":
    unittest.main()
