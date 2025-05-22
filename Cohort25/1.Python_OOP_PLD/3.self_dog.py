#!/usr/bin/env python3

# Step 1: Define a Dog class (Blueprint)



class Dog:
    # The __init__ method initializes the object with the given name
    def __init__(self, name):
        # `self` refers to the current object being created
        self.name = name  # `self.name` stores the dog's name

    
    # The `bark` method prints the dog's name and a bark message
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says Woof!
