import csv
import os


def read_csv(filename):
    """
    Reads a CSV from the data/ folder and returns a list of dicts,
    one dict per row, keyed by the CSV header.
    Used to feed @pytest.mark.parametrize with real test data.
    """
    path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
