import csv

def read_rows(path):
    with open(path) as f:
        return list(csv.DictReader(f))
