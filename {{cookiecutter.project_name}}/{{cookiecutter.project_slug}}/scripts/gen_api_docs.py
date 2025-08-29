"""Generate API reference docs with mkdocstrings."""
from pathlib import Path
import mkdocs_gen_files

# --- Always resolve relative to project root (where mkdocs.yml is) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC = PROJECT_ROOT / "src"
DOCS = PROJECT_ROOT / "docs"
PACKAGE = "{{cookiecutter.project_slug.replace('-', '_')}}"

nav = mkdocs_gen_files.Nav()

for path in sorted(SRC.rglob("*.py")):
    module_path = path.relative_to(SRC).with_suffix("")
    doc_path = Path("reference", path.relative_to(SRC)).with_suffix(".md")
    full_doc_path = DOCS / doc_path

    parts = tuple(module_path.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    if not parts or parts[-1].startswith("_"):
        continue

    nav[parts] = doc_path.as_posix()

    full_doc_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        fd.write(f"# `{identifier}`\n\n::: {identifier}\n")

# --- Write nav index inside docs/reference ---
(DOCS / "reference").mkdir(parents=True, exist_ok=True)
with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
