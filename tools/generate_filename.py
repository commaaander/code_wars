#!/usr/bin/env python
import argparse
import os
import re


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("kata_name", type=str, help="The name of the kata.")
    parser.add_argument("--dry-run", action="store_true", help="Run the script without creating files.")
    args = parser.parse_args()

    kata_name: str = re.sub(r"[^\w\s]", "", args.kata_name).lower().replace(" ", "_")

    src_dir: str = os.path.join(os.path.dirname(__file__), "..", "src")
    docs_dir: str = os.path.join(os.path.dirname(__file__), "..", "docs")

    py_file_path: str = os.path.join(src_dir, f"{kata_name}.py")
    md_file_path: str = os.path.join(docs_dir, f"{kata_name}.md")

    if args.dry_run:
        print(f"Would create: {py_file_path}")
        print(f"Would create: {md_file_path}")
        return

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    with open(py_file_path, "w") as py_file:
        py_file.write(f"# {args.kata_name}\n")
        print(f"Created {py_file_path}")

    with open(md_file_path, "w") as md_file:
        md_file.write(f"# {args.kata_name}\n")
        print(f"Created {md_file_path}")


if __name__ == "__main__":
    main()
