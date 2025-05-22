import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")
    
    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None


# Usage
obj = CustomObject("Alice", 25, True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
if new_obj:
    new_obj.display()