


import json

def from_json_string(json_string):
    return json.loads(json_string)

# Usage
json_data = '{"name": "Alice", "age": 25}'
print(from_json_string(json_data))


















#Usage when returning from a JSON file to a Python object
def from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)
    

# Usage
print(from_json_file("4.example.json"))