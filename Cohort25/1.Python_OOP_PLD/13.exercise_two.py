class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):  # Method to introduce the person
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Alice", 25)

# Calling the method
person1.introduce()  # Output: Hi, my name is Alice and I am 25 years old.
