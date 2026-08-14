import unittest

from frontmatter import split_frontmatter
from new_project import CATEGORIES, DEFAULT_CATEGORY, project_template, slugify


class TestNewProject(unittest.TestCase):
    def test_slugify_title(self):
        self.assertEqual(slugify("Fixture Plate Setup!"), "fixture-plate-setup")

    def test_slugify_removes_path_segments(self):
        self.assertEqual(slugify("../Fixture Plate"), "fixture-plate")

    def test_project_template_uses_title_and_summary(self):
        template = project_template(
            "Fixture Plate", "A repeatable setup project.", "cad-cam"
        )

        self.assertIn("# Fixture Plate", template)
        self.assertIn("A repeatable setup project.", template)
        self.assertIn("[Back to projects](/projects)", template)

    def test_project_template_writes_parsable_front_matter(self):
        template = project_template("Fixture Plate", "A summary.", "cad-cam")
        metadata, body = split_frontmatter(template)

        self.assertEqual(metadata, {"category": "cad-cam", "summary": "A summary."})
        self.assertTrue(body.startswith("# Fixture Plate"))

    def test_default_category_is_a_known_category(self):
        self.assertIn(DEFAULT_CATEGORY, CATEGORIES)
