from textnode import TextNode, TextType

def main():
    dummy_text_node_1 = TextNode("Hello", TextType.TEXT, "https://example.com")
    dummy_text_node_2 = TextNode("World", TextType.BOLD)

    print(dummy_text_node_1.__repr__())
    print(dummy_text_node_2.__repr__())


main()