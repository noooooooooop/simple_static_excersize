import unittest

from leafnode import LeafNode
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", "bold", "http://not.a.real.website.adsfasdfasdfsafdasffdassdasfd")
        node2 = TextNode("This is a text node", "bold", "http://not.a.real.website.adsfasdfasdfsafdasffdassdasfd")
        self.assertEqual(node, node2)

    def test_eq2_blank(self):
        node = TextNode("", "text", "")
        node2 = TextNode("", "text", "")
        self.assertEqual(node, node2)

    def test_not_eq_1(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_3(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "adsfasdfafsd")
        self.assertNotEqual(node, node2)

    def test_not_eq_4(self):
        node = TextNode("This is a text node", "bold", "adsfasdfafsd")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_invalid_1(self):
        self.assertRaises(ValueError, lambda: TextNode(None, "bold", "adsfasdfafsd"))

    def test_invalid_2(self):
        self.assertRaises(ValueError, lambda: TextNode("test", None, "adsfasdfafsd"))

    def test_invalid_3(self):
        self.assertRaises(ValueError, lambda: TextNode("test", "asdf", None))

    def test_html_convert_1(self):
        html = TextNode("test", "text").convert_to_html_node()
        self.assertEqual(html, LeafNode(value="test"))

    def test_html_convert_2(self):
        html = TextNode("test", "bold").convert_to_html_node()
        self.assertEqual(html, LeafNode("b", value="test"))

    def test_html_convert_3(self):
        html = TextNode("test", "italic").convert_to_html_node()
        self.assertEqual(html, LeafNode("i", value="test"))

    def test_html_convert_4(self):
        html = TextNode("test", "code").convert_to_html_node()
        self.assertEqual(html, LeafNode("code", value="test"))

    def test_html_convert_5(self):
        html = TextNode("test", "link", "https://www.google.com").convert_to_html_node()
        self.assertEqual(html, LeafNode("a", value="test", props={"href": "https://www.google.com"}))

    def test_html_convert_6(self):
        html = TextNode("the image didn't load =( ...", "image", "path/to/image.png").convert_to_html_node()
        self.assertEqual(
            html,
            LeafNode(
                "img",
                props={"src": "path/to/image.png", "alt": "the image didn't load =( ..."},
                    self_closing=True,
                )
            )

if __name__ == "__main__":
    unittest.main()
