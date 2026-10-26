from data.csv_reader import read_rows
from data.validate import valid

def import_csv(path):
    return [r for r in read_rows(path) if valid(r)]
