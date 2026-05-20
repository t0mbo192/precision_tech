import argparse
import os
import re
import textwrap


DEFAULT_SUMMARY = (
    "Short summary of what the project is, why it matters, and what changed."
)


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if not slug:
        raise ValueError("Project title must contain at least one letter or number")
    return slug


def project_template(title, summary):
    return textwrap.dedent(
        f"""\
        # {title}

        {summary}

        ## Overview

        Replace this with the project context, problem, and goal.

        ## Work

        - Add the main design, machining, programming, or coding details.
        - Include screenshots or images with Markdown when they are ready.
        - Capture useful setup notes, process choices, or lessons learned.

        ## Result

        Describe the finished outcome, current status, or next step.

        [Back to projects](/projects)
        """
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a new project Markdown page."
    )
    parser.add_argument("title", help="Project title")
    parser.add_argument(
        "--summary",
        default=DEFAULT_SUMMARY,
        help="One-sentence summary shown on the projects page",
    )
    parser.add_argument(
        "--slug",
        help="URL slug. Defaults to a lowercase version of the title.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    slug = slugify(args.slug or args.title)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_dir = os.path.join(project_root, "content", "projects", slug)
    project_path = os.path.join(project_dir, "index.md")

    if os.path.exists(project_path):
        raise FileExistsError(f"Project already exists: {project_path}")

    os.makedirs(project_dir, exist_ok=True)
    with open(project_path, "w", encoding="utf-8") as project_file:
        project_file.write(project_template(args.title, args.summary))

    print(f"Created {project_path}")


if __name__ == "__main__":
    main()
