from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        if line.strip() == "":
            continue
        block_lines = line.split("\n")
        cleaned_block = "\n".join([l.strip() for l in block_lines])
        final_block = cleaned_block.strip()
        if final_block:
            blocks.append(final_block)
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    # Heading
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    # Code block
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # Quote block
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # Unordered list
    elif block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    # Ordered list
    elif lines[0].startswith("1. "):
        for i in range(len(lines)):
            expected = f"{i+1}. "
            if not lines[i].startswith(expected):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH
    
    