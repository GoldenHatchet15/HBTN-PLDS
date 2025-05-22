#title: Single Inheritance


class Animal:
    def breathe(self):
        return "Breathing..."

class Dog(Animal):
    def bark(self):
        return "Woof! Woof!"

my_dog = Dog()
print(my_dog.breathe())  # Output: Breathing...
print(my_dog.bark())  # Output: Woof! Woof!
