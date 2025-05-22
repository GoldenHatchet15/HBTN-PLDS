#This script converts a Python object to a JSON string.

import json

def to_json_string(obj):
    return json.dumps(obj)



# Usage
data = {"name": "Alice", "age": 25}
#print(to_json_string(data))

















#return output into a json file
def to_json_file(filename, obj):
    with open(filename, "w") as file:
        json.dump(obj, file)

# Usage

to_json_file("4.example.json", data)
