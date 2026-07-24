# Tom's Precision Tech

A personal IT, cybersecurity, and technical portfolio for Tom Lett, built with a custom Python static site generator. It collects systems, scripting, and hands-on engineering projects behind a move into IT and security.

## Adding projects

The easiest way to add a project is to create a Markdown page under
`content/projects/<project-slug>/index.md`. The projects page automatically
builds its archive from those folders when the site is regenerated.

Use the helper command to scaffold a new project:

```bash
python3 src/new_project.py "Home Lab Network Segmentation" --summary "Setting up VLANs and firewall rules on a small home lab to practice network isolation."
```

Then edit the generated Markdown file and rebuild:

```bash
./build.sh
```

Images go under `static/images/`; reference them from Markdown with an
absolute path such as `/images/projects/<slug>/screenshot.png`.
