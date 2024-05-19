import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
