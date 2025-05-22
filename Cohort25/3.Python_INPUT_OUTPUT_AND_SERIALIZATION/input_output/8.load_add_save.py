import json

def load_add_save(filename, new_data):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(new_data)
    with open(filename, "w") as file:
        json.dump(data, file)

# Usage
load_add_save("data.json", {"name": "Bob", "age": 30})

#Output: [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]