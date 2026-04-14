import unittest

from main import resolve_output_dir


class TestMain(unittest.TestCase):
    def test_resolve_output_dir_defaults_to_docs(self):
        project_root = "/tmp/project"
        self.assertEqual(
            resolve_output_dir(project_root),
            "/tmp/project/docs",
        )

    def test_resolve_output_dir_uses_relative_path_from_project_root(self):
        project_root = "/tmp/project"
        self.assertEqual(
            resolve_output_dir(project_root, ".preview"),
            "/tmp/project/.preview",
        )

    def test_resolve_output_dir_preserves_absolute_path(self):
        project_root = "/tmp/project"
        self.assertEqual(
            resolve_output_dir(project_root, "/tmp/output"),
            "/tmp/output",
        )


if __name__ == "__main__":
    unittest.main()
