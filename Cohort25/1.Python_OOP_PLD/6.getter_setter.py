#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute (cannot be accessed directly)

    # Getter method (to retrieve private attribute)
    def get_age(self):
        return self.__age

    # Setter method (to update private attribute with validation)
    def set_age(self, new_age):
        if new_age > 0:  # Ensuring the age is positive
            self.__age = new_age
        else:
            print("Age must be positive!")

# Creating an object
person1 = Person("Alice", 25)

# Accessing private attribute using the getter
print(person1.get_age())  # Output: 25

# Updating private attribute using the setter
person1.set_age(30)
print(person1.get_age())  # Output: 30

# Attempting to set an invalid age
person1.set_age(-5)  # Output: Age must be positive!
