import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading"), BlockType.HEADING)

        self.assertEqual(
            block_to_block_type("```\ncode block\n```"), BlockType.CODE
        )

        self.assertEqual(
            block_to_block_type("> This is a quote\n> with multiple lines"),
            BlockType.QUOTE,
        )

        self.assertEqual(
            block_to_block_type("- Item 1\n- Item 2\n- Item 3"),
            BlockType.UNORDERED_LIST,
        )

        self.assertEqual(
            block_to_block_type("1. First item\n2. Second item\n3. Third item"),
            BlockType.ORDERED_LIST,
        )
if __name__ == "__main__":
    unittest.main()