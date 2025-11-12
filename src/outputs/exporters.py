from src.outputs.formats.to_json import export_json
from src.outputs.formats.to_csv import export_csv
from src.outputs.formats.to_xlsx import export_xlsx

class Exporter:
    def __init__(self, data):
        self.data = data

    def to_all(self):
        export_json(self.data)
        export_csv(self.data)
        export_xlsx(self.data)