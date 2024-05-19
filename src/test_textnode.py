import unittest

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
        node = TextNode("", "")
        node2 = TextNode("", "")
        self.assertEqual(node, node2)

    def test_eq3_blank(self):
        node = TextNode("", "", "")
        node2 = TextNode("", "", "")
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


if __name__ == "__main__":
    unittest.main()
