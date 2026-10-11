#!/usr/bin/env python3
"""
Script to update README.md table with semiconductor fab data from the latest year's JSON file in data/.
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
README_PATH = PROJECT_ROOT / "README.md"


def get_latest_data_file():
    json_files = sorted(DATA_DIR.glob("fabs_*.json"))
    if not json_files:
        raise FileNotFoundError("No fabs_*.json data files found in data/ directory.")
    return json_files[-1]


def format_status(status_str):
    # Format inline italics or bold for status text if needed
    if "(" in status_str and ")" in status_str:
        main_part, extra = status_str.split("(", 1)
        extra = extra.rstrip(")")
        return f"**{main_part.strip()}** *({extra})*"
    return f"**{status_str.strip()}**"


def generate_markdown_table(data):
    header = "| 🌍 Country / Region | 🏭 Operating Fabs Count | 🔬 ASML Lithography Equipment Status | 🏢 Major Domestic Fabs & Specialties |\n"
    divider = "| :--- | :---: | :--- | :--- |\n"
    
    rows = []
    for item in data:
        country = f"**{item['country']}**"
        count = item['operating_fabs_count']
        status = format_status(item['asml_lithography_status'])
        specialties = item['major_domestic_fabs_specialties']
        rows.append(f"| {country} | {count} | {status} | {specialties} |")
    
    return header + divider + "\n".join(rows)


def update_readme():
    latest_file = get_latest_data_file()
    print(f"Loading data from: {latest_file.name}")
    
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_table_md = generate_markdown_table(data)
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Pattern to replace content under '## 📊 Global Semiconductor Fab Statistics' up to the next '---'
    pattern = r"(## 📊 Global Semiconductor Fab Statistics\n\n)(.*?)(?=\n\n---)"
    
    if not re.search(pattern, readme_content, flags=re.DOTALL):
        raise ValueError("Could not find Global Semiconductor Fab Statistics table section in README.md")

    updated_content = re.sub(pattern, rf"\1{new_table_md}", readme_content, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Successfully updated README.md with data from {latest_file.name}")


if __name__ == "__main__":
    update_readme()
