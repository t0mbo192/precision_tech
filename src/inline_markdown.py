
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            for i, part in enumerate(parts):
                if part:
                    if i % 2 == 0:
                        result.append(TextNode(part, TextType.TEXT))
                    else:
                        result.append(TextNode(part, text_type))    
        else:
            result.append(node)
    return result
        