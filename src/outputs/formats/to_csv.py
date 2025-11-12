import csv
from pathlib import Path

def export_csv(data):
    if not data:
        print("⚠️ No data to export.")
        return
    Path("data").mkdir(exist_ok=True)
    with open("data/output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print("💾 CSV exported successfully.")