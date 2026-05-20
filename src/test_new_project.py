import unittest

from new_project import project_template, slugify


class TestNewProject(unittest.TestCase):
    def test_slugify_title(self):
        self.assertEqual(slugify("Fixture Plate Setup!"), "fixture-plate-setup")

    def test_slugify_removes_path_segments(self):
        self.assertEqual(slugify("../Fixture Plate"), "fixture-plate")

    def test_project_template_uses_title_and_summary(self):
        template = project_template("Fixture Plate", "A repeatable setup project.")

        self.assertIn("# Fixture Plate", template)
        self.assertIn("A repeatable setup project.", template)
        self.assertIn("[Back to projects](/projects)", template)
