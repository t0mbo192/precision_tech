"""Optional front matter at the top of a Markdown file.

A page can open with a fenced block of `key: value` lines:

    ---
    category: tool-building
    ---

    # Project title

Only flat string fields are supported, which is enough to tag a project
with a category without taking on a YAML dependency.
"""

DELIMITER = "---"


def split_frontmatter(markdown):
    """Split ``markdown`` into a ``(metadata, body)`` pair.

    Returns an empty dict alongside the untouched text when the file has
    no front matter, or when an opening delimiter is never closed.
    """
    lines = markdown.split("\n")
    if not lines or lines[0].strip() != DELIMITER:
        return {}, markdown

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == DELIMITER:
            metadata = _parse_fields(lines[1:index])
            body = "\n".join(lines[index + 1 :]).lstrip("\n")
            return metadata, body

    return {}, markdown


def _parse_fields(lines):
    fields = {}
    for line in lines:
        key, separator, value = line.partition(":")
        if not separator:
            continue
        fields[key.strip().lower()] = value.strip()
    return fields
