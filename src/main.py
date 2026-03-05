from inline_markdown import text_to_textnodes

text = "This is **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://www.google.com)"
text_nodes = text_to_textnodes(text)
for node in text_nodes:
    print(node)