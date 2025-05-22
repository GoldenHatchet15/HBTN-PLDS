def class_to_json(obj):
    return obj.__dict__

# Example Usage
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(class_to_json(person)) 

# Output: {'name': 'Alice', 'age': 25}