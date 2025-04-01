from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise TypeError("text_type must be an instance of TextType Enum")
        
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text)
        
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_to_return = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes_to_return.append(old_node)
            continue

        split_text = old_node.text.split(delimiter)
        new_nodes = []

        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        for index, text in enumerate(split_text):
            if text == "":
                continue

            if index % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))

        nodes_to_return.extend(new_nodes)

    return nodes_to_return