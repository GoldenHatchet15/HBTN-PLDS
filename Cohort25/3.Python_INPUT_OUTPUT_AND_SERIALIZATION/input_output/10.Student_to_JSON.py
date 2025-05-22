class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        return self.__dict__

# Usage
student = Student("John", "Doe", 23)
print(student.to_json())

# Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 23}