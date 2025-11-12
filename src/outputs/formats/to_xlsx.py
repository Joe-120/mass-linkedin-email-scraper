from openpyxl import Workbook
from pathlib import Path

def export_xlsx(data):
    if not data:
        print("⚠️ No data to export.")
        return
    wb = Workbook()
    ws = wb.active
    ws.append(list(data[0].keys()))
    for row in data:
        ws.append(list(row.values()))
    Path("data").mkdir(exist_ok=True)
    wb.save("data/output.xlsx")
    print("💾 Excel exported successfully.")