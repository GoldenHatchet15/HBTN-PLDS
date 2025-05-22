import json

def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Usage
sample_data = {"name": "John Doe", "age": 30, "city": "New York"}
serialize_and_save_to_file(sample_data, "data.json")
print(load_and_deserialize("data.json"))