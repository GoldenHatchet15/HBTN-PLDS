import json

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def reload_from_json(self, json_data):
        for key, value in json_data.items():
            setattr(self, key, value)

# Usage
student = Student("John", "Doe", 23)
json_string = json.dumps(student.to_json())
student.reload_from_json(json.loads(json_string))
print(student.__dict__)

# Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 23}