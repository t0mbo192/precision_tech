# Tom's Precision Tech

A personal IT, cybersecurity, and technical portfolio for Tom Lett, built with a custom Python static site generator. It collects security tooling, automation, and hands-on engineering projects behind a move into IT and security.

## Adding projects

The easiest way to add a project is to create a Markdown page under
`content/projects/<project-slug>/index.md`. The home page automatically
builds its project sections from those folders when the site is regenerated.

Use the helper command to scaffold a new project:

```bash
python3 src/new_project.py "Home Lab Network Segmentation" \
  --category home-lab \
  --summary "Setting up VLANs and firewall rules on a small home lab to practice network isolation."
```

Then edit the generated Markdown file and rebuild:

```bash
./build.sh
```

## Project categories

Each project opens with a front matter block naming the section it belongs
under on the home page, plus the one-line summary shown there:

```markdown
---
category: home-lab
summary: One dry line describing what it is.
---

# Project title
```

The categories are `cad-cam`, `tool-building`, and `home-lab`. A project with
no category, or one naming a category the home page doesn't list, is built
as a page but left out of the archive — so a typo here hides a project rather
than breaking the build.

To add or rename a category, edit the heading and `{{ ProjectList: <slug> }}`
token in `content/index.md`, then update `CATEGORIES` in
`src/new_project.py` to match. Sections are ordered by where their token sits
on that page, and an empty one prints a short placeholder line instead.

Images go under `static/images/`; reference them from Markdown with an
absolute path such as `/images/projects/<slug>/screenshot.png`.
