# Parent class
class Animal:
    def make_sound(self):
        pass  # This will be overridden by child classes

# Child classes (Overriding the make_sound method)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Using Polymorphism
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())



#Why Use Polymorphism?
#Allows writing general code that works with multiple object 
#types.
#Simplifies the structure and makes code more flexible.
#Supports dynamic method calling, 
#allowing objects to respond differently.