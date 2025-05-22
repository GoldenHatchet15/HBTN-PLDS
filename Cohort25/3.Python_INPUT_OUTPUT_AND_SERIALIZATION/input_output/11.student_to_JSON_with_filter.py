class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

# Usage
student = Student("John", "Doe", 23)
print(student.to_json(["first_name", "age"])) 

# Output: {'first_name': 'John', 'age': 23}