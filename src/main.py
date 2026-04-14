import os
import sys

from copystatic import copy_files_recursive
from markdown_to_html import generate_pages_recursive, normalize_basepath


def resolve_output_dir(project_root, output_arg=None):
    if output_arg is None:
        return os.path.join(project_root, "docs")

    if os.path.isabs(output_arg):
        return output_arg

    return os.path.join(project_root, output_arg)


def main():
    basepath = normalize_basepath(sys.argv[1] if len(sys.argv) > 1 else "/")
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(project_root, "static")
    content_dir = os.path.join(project_root, "content")
    output_dir = resolve_output_dir(
        project_root,
        sys.argv[2] if len(sys.argv) > 2 else None,
    )
    template_path = os.path.join(project_root, "template.html")

    copy_files_recursive(static_dir, output_dir)
    generate_pages_recursive(content_dir, template_path, output_dir, basepath)


if __name__ == "__main__":
    main()
