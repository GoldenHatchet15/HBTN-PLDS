#!/usr/bin/env python3

#this is an example of a class that  defines a method to introduce a person.


class Person:
    def __init__(self, name, age):
        self.name = name  # Stores the person's name
        self.age = age  # Stores the person's age
    
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 35)

# Calling the method
person1.introduce()  # Output: Hi, my name is Alice and I am 25 years old.
person2.introduce()  # Output: Hi, my name is Bob and I am 30 years old.
person3.introduce()  # Output: Hi, my name is Charlie and I am 35 years old.

