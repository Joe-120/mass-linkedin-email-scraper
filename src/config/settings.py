import json
from pathlib import Path

def load_settings():
    path = Path("src/config/settings.example.json")
    if not path.exists():
        raise FileNotFoundError("Settings file not found.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)