from textnode import TextNode, TextType, split_nodes_delimiter

def main():
    dummy_text_node_1 = TextNode("Hello, this is **bold** stuff right ere", TextType.TEXT, "https://example.com")
    dummy_text_node_2 = TextNode('Worldly done, this code `print("somethings not right")` is definitely your magnum opus', TextType.TEXT)

    print(split_nodes_delimiter([dummy_text_node_1], "**", TextType.BOLD))
    print(split_nodes_delimiter([dummy_text_node_2], "`", TextType.CODE))


main()