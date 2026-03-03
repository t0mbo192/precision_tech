import re
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

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_images(node.text)
            if matches:
                last_index = 0
                for alt_text, url in matches:
                    match_str = f"![{alt_text}]({url})"
                    index = node.text.find(match_str, last_index)
                    if index != -1:
                        if index > last_index:
                            result.append(TextNode(node.text[last_index:index], TextType.TEXT))
                        result.append(TextNode(alt_text, TextType.IMAGE, url))
                        last_index = index + len(match_str)
                if last_index < len(node.text):
                    result.append(TextNode(node.text[last_index:], TextType.TEXT))
            else:
                result.append(node)
        else:
            result.append(node)
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            matches = extract_markdown_links(node.text)
            if matches:
                last_index = 0
                for link_text, url in matches:
                    match_str = f"[{link_text}]({url})"
                    index = node.text.find(match_str, last_index)
                    if index != -1:
                        if index > last_index:
                            result.append(TextNode(node.text[last_index:index], TextType.TEXT))
                        result.append(TextNode(link_text, TextType.LINK, url))
                        last_index = index + len(match_str)
                if last_index < len(node.text):
                    result.append(TextNode(node.text[last_index:], TextType.TEXT))
            else:
                result.append(node)
        else:
            result.append(node)
    return result

def extract_markdown_images(text):
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_pattern, text)
    return matches

def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_pattern, text)
    return matches