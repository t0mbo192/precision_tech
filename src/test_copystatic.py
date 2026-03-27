import os
import tempfile
import unittest

from copystatic import copy_files_recursive


class TestCopyStatic(unittest.TestCase):
    def test_copy_files_recursive_copies_all_static_images(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            static_dir = os.path.join(tmpdir, "static")
            public_dir = os.path.join(tmpdir, "public")

            nested_image_path = os.path.join(static_dir, "images", "gallery", "hero.png")
            sibling_image_path = os.path.join(static_dir, "images", "cover.png")
            css_path = os.path.join(static_dir, "index.css")

            os.makedirs(os.path.dirname(nested_image_path), exist_ok=True)

            with open(nested_image_path, "wb") as nested_image_file:
                nested_image_file.write(b"nested-image-bytes")

            with open(sibling_image_path, "wb") as sibling_image_file:
                sibling_image_file.write(b"cover-image-bytes")

            with open(css_path, "w", encoding="utf-8") as css_file:
                css_file.write("body { margin: 0; }")

            copy_files_recursive(static_dir, public_dir)

            copied_nested_image_path = os.path.join(
                public_dir, "images", "gallery", "hero.png"
            )
            copied_sibling_image_path = os.path.join(
                public_dir, "images", "cover.png"
            )

            self.assertTrue(os.path.exists(copied_nested_image_path))
            self.assertTrue(os.path.exists(copied_sibling_image_path))

            with open(copied_nested_image_path, "rb") as nested_image_file:
                self.assertEqual(nested_image_file.read(), b"nested-image-bytes")

            with open(copied_sibling_image_path, "rb") as sibling_image_file:
                self.assertEqual(sibling_image_file.read(), b"cover-image-bytes")


if __name__ == "__main__":
    unittest.main()
