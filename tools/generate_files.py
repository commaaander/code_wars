#!/usr/bin/env python
import argparse
import os
import re

import requests
from bs4 import BeautifulSoup


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Python and Markdown files for a Codewars kata.")

    parser.add_argument("--dry-run", action="store_true", help="Run the script without creating files.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", type=str, help="The URL of the kata.")
    group.add_argument("--name", type=str, help="The name of the kata.")

    args = parser.parse_args()

    if args.url:
        response = requests.get(args.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            og_title = soup.find("meta", property="og:title")
            if og_title and og_title["content"]:
                args.name = og_title["content"]
        else:
            print(f"Failed to fetch the URL: {args.url}")

    kata_slug: str = re.sub(r"[^\w\s]", "", args.name).lower().replace(" ", "_")

    src_dir: str = os.path.join(os.path.dirname(__file__), "..", "src")
    docs_dir: str = os.path.join(os.path.dirname(__file__), "..", "docs")

    py_file_path: str = os.path.join(src_dir, f"{kata_slug}.py")
    md_file_path: str = os.path.join(docs_dir, f"{kata_slug}.md")

    print()
    if args.dry_run:
        print(f"Would create: {py_file_path}")
        print(f"Would create: {md_file_path}")
        return

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    print(f"Create files for kata {args.name}")

    with open(py_file_path, "w") as py_file:
        py_file.write("#!/usr/bin/env python\n")
        print(f"Created {py_file_path}")

    with open(md_file_path, "w") as md_file:
        md_file.write(f"# {args.name}\n\n")
        if args.url:
            md_file.write(f"\n<{args.url}>\n\n")
        print(f"Created {md_file_path}")


if __name__ == "__main__":
    main()
