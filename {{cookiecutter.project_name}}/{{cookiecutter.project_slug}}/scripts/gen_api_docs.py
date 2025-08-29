import os
import pathlib

DOCS_DIR = pathlib.Path("docs")
REF_DIR = DOCS_DIR / "reference"
SRC_DIR = pathlib.Path("src")

def main():
    print("🔧 Generating API reference docs...")

    # Create reference directory if it doesn’t exist
    REF_DIR.mkdir(parents=True, exist_ok=True)

    # Create an index page for reference
    with open(REF_DIR / "index.md", "w") as f:
        f.write("# Reference\n\n")
        f.write("::: src\n")

    print("✅ API reference docs generated at docs/reference/")

if __name__ == "__main__":
    main()
