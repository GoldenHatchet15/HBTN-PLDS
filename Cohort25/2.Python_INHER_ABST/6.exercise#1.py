# Defining an abstract class and abstract method

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def run(self):
        print("Running")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
