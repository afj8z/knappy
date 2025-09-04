import csv
from csv import DictReader
from knappy.definitions import ITEMS_CSV
from knappy.core.models import Items


def append_csv(new_row):
    with open(ITEMS_CSV, "a") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)


def gen_item_dict(csv_file=ITEMS_CSV):
    with open(ITEMS_CSV, "r") as f:
        item_dict = DictReader(f)
        print(item_dict)


def gen_datatable(csv_file=ITEMS_CSV):
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        return [tuple(line) for line in reader]
