import json
from pathlib import Path

def export_json(data):
    Path("data").mkdir(exist_ok=True)
    with open("data/output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("💾 JSON exported successfully.")