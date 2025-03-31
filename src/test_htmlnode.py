import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", {"class": "container"})
        node2 = HTMLNode("div", "This is a div", {"class": "container"})
        self.assertEqual(node, node2)
    def test_neq_tag(self):
        node = HTMLNode("div", "This is a div", {"class": "container"})
        node2 = HTMLNode("span", "This is a div", {"class": "container"})
        self.assertNotEqual(node, node2)
    def test_neq_value(self):
        node = HTMLNode("div", "This is a div", {"class": "container"})
        node2 = HTMLNode("div", "This is a different div", {"class": "container"})
        self.assertNotEqual(node, node2)
    def test_neq_props(self):
        node = HTMLNode("div", "This is a div", {"class": "container"})
        node2 = HTMLNode("div", "This is a div", {"class": "different"})
        self.assertNotEqual(node, node2)
    def test_neq_children(self):
        node = HTMLNode("div", "This is a div", {"class": "container"}, [HTMLNode("span")])
        node2 = HTMLNode("div", "This is a div", {"class": "container"})
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()