import json

def save_to_json_file(obj, filename):
    with open(filename, "w") as file:
        json.dump(obj, file)

# Usage
data = {"name": "Alice", "age": 25}
save_to_json_file(data, "data.json")