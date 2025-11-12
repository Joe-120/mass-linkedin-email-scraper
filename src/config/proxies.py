import json
from pathlib import Path

def load_proxies():
    path = Path("src/config/proxies.example.json")
    if not path.exists():
        print("⚠️ No proxies config found. Proceeding without proxies.")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)