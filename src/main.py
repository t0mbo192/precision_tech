from inline_markdown import markdown_to_blocks

text = """
This is **bold** text


This is _italic_ text

- This is a list
- with items
"""

text_blocks = markdown_to_blocks(text)
for block in text_blocks:
    print(block)