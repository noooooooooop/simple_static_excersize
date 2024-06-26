import unittest
from textnode import TextNode
from main import convert_markdown_to_textnodes

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestMain(unittest.TestCase):
    def test_eq_1(self):
        self.maxDiff = None

        md = """# This is a test
for converting *markdown* to **html**.
It converts bold, italics and `code blocks`,
[links](https://www.google.com),
and ![images](path/to/some/image2.jpeg),
and ![more images](path/to/some/image3.png),
[and that's currently about it.](https://www.google.com/images).
"""

        md = convert_markdown_to_textnodes(md)

        self.assertEqual(md, [
            TextNode("# This is a test\nfor converting ", "text"),
            TextNode("markdown", "bold"),
            TextNode(" to ", "text"),
            TextNode("html", "italic"),
            TextNode(".\nIt converts bold, italics and ", "text"),
            TextNode("code blocks", "code"),
            TextNode(",\n", "text"),
            TextNode("links", "link", "https://www.google.com"),
            TextNode(",\nand ", "text"),
            TextNode("images", "image", "path/to/some/image2.jpeg"),
            TextNode(",\nand ", "text"),
            TextNode("more images", "image", "path/to/some/image3.png"),
            TextNode(",\n", "text"),
            TextNode("and that's currently about it.", "link", "https://www.google.com/images"),
            TextNode(".\n", "text"),
        ])

if __name__ == "__main__":
    unittest.main()
