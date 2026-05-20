# site_generator

## Adding projects

The easiest way to add a project is to create a Markdown page under
`content/projects/<project-slug>/index.md`. The projects page automatically
builds its archive from those folders when the site is regenerated.

Use the helper command to scaffold a new project:

```bash
python3 src/new_project.py "Fixture Plate Setup" --summary "A setup and CAM planning project for repeatable fixture work."
```

Then edit the generated Markdown file and rebuild:

```bash
./build.sh
```
