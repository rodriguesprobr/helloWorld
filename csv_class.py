import csv

class csv_class:

    def __init__(self, path):
        self.reader = None
        self.path = path
        self.file = None

    def abrir(self):
        self.file = open(
            self.path,
            "r",
            encoding="utf-8"
        )

    def ver_header(self):
        self.reader = csv.reader(self.file)
        return next(self.reader)

    def pesquisar_estrato(self, estrato):
        self.reader = csv.reader(self.file)
        return_rows = []
        for row in self.reader:
            if row[2] == estrato:
                return_rows.append(row)
        return return_rows

