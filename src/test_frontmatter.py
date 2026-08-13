import unittest

from frontmatter import split_frontmatter


class TestSplitFrontmatter(unittest.TestCase):
    def test_parses_fields_and_returns_body(self):
        metadata, body = split_frontmatter(
            "---\ncategory: tool-building\n---\n\n# Title\n\nBody text."
        )

        self.assertEqual(metadata, {"category": "tool-building"})
        self.assertEqual(body, "# Title\n\nBody text.")

    def test_returns_original_markdown_when_absent(self):
        markdown = "# Title\n\nBody text."
        metadata, body = split_frontmatter(markdown)

        self.assertEqual(metadata, {})
        self.assertEqual(body, markdown)

    def test_unterminated_block_is_left_as_body(self):
        markdown = "---\ncategory: tool-building\n\n# Title"
        metadata, body = split_frontmatter(markdown)

        self.assertEqual(metadata, {})
        self.assertEqual(body, markdown)

    def test_ignores_blank_and_valueless_lines(self):
        metadata, _ = split_frontmatter(
            "---\n\ncategory: cad-cam\nnot a field\nstatus: draft\n---\n\n# Title"
        )

        self.assertEqual(metadata, {"category": "cad-cam", "status": "draft"})

    def test_keys_are_lowercased_and_values_stripped(self):
        metadata, _ = split_frontmatter("---\n  Category :  home-lab  \n---\n\n# Title")

        self.assertEqual(metadata, {"category": "home-lab"})

    def test_value_may_contain_a_colon(self):
        metadata, _ = split_frontmatter("---\nsummary: built: then tested\n---\n\n# Title")

        self.assertEqual(metadata, {"summary": "built: then tested"})


if __name__ == "__main__":
    unittest.main()
