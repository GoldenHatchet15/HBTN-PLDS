import csv
import json

def convert_csv_to_json(csv_filename, json_filename):
    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open(json_filename, "w") as json_file:
            json.dump(data, json_file)
        return True
    except FileNotFoundError:
        return False

# Usage
convert_csv_to_json("data.csv", "1.data.json")