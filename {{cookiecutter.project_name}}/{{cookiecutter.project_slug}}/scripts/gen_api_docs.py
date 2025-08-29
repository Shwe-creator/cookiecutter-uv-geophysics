"""Generate API reference docs with mkdocstrings."""
from pathlib import Path
import mkdocs_gen_files

# point to your source package
SRC = Path("src")
PACKAGE = "{{cookiecutter.project_slug.replace('-', '_')}}"

nav = mkdocs_gen_files.Nav()

for path in sorted(SRC.rglob("*.py")):
    module_path = path.relative_to(SRC).with_suffix("")
    doc_path = Path("reference", path.relative_to(SRC)).with_suffix(".md")
    full_doc_path = Path("docs", doc_path)

    parts = tuple(module_path.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    if parts[-1].startswith("_"):
        continue

    nav[parts] = doc_path.as_posix()

    full_doc_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        fd.write(f"# `{identifier}`\n\n::: {identifier}\n")

# write a nav index
with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
