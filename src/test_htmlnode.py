import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


class TestLeafNode(unittest.TestCase):
    def test_leafnode_requires_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode(tag="p")
        self.assertEqual(str(context.exception), "LeafNode requires a value")

    def test_leafnode_initialization(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_leafnode_to_html_without_props(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_to_html_with_props(self):
        node = LeafNode(tag="p", value="Hello, world!", props={"class": "text-bold", "id": "greeting"})
        self.assertEqual(node.to_html(), '<p class="text-bold" id="greeting">Hello, world!</p>')

    def test_leafnode_to_html_without_tag(self):
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leafnode_equality(self):
        node1 = LeafNode(tag="p", value="Hello", props={"class": "text-bold"})
        node2 = LeafNode(tag="p", value="Hello", props={"class": "text-bold"})
        self.assertEqual(node1, node2)

    def test_leafnode_inequality_different_value(self):
        node1 = LeafNode(tag="p", value="Hello")
        node2 = LeafNode(tag="p", value="World")
        self.assertNotEqual(node1, node2)

    def test_leafnode_inequality_different_props(self):
        node1 = LeafNode(tag="p", value="Hello", props={"class": "text-bold"})
        node2 = LeafNode(tag="p", value="Hello", props={"id": "greeting"})
        self.assertNotEqual(node1, node2)

    def test_leafnode_repr(self):
        node = LeafNode(tag="p", value="Hello", props={"class": "text-bold"})
        self.assertEqual(repr(node), "LeafNode(tag=p, value=Hello, props={'class': 'text-bold'})")

if __name__ == "__main__":
    unittest.main()