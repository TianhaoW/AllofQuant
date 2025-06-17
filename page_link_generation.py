import os
import re
import yaml

# Configuration
TOPIC_FOLDERS = ["Probability", "Statistics", "Brainteaser", "Finance", "MachineLearning", "Coding"]
OUTPUT_FILE = "_data/leftnav.yml"

NAME_DICT = {
    "Probability": "Probability",
    "Statistics": "Statistics",
    "Brainteaser": "Brainteaser",
    "Finance": "Math Finance",
    "MachineLearning": "Machine Learning",
    "Coding": "Coding",
}

def parse_index_md(index_path):
    """Parse the markdown links in index.md."""
    items = []
    with open(index_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r"- \[(.+?)\]\((.+?)\)", line.strip())
            if match:
                name, link = match.groups()
                link = link[2:-3]
                items.append({"name": name, "link": f"/{os.path.dirname(index_path)}/{link}"})
    return items

def generate_leftnav():
    nav = []

    for folder in TOPIC_FOLDERS:
        index_md = os.path.join(folder, "index.md")
        if os.path.exists(index_md):
            section = {
                "label": NAME_DICT[folder],
                "link": f"/{folder}",
                "items": parse_index_md(index_md)
            }
            nav.append(section)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(nav, f, sort_keys=False, allow_unicode=True)

    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_leftnav()
