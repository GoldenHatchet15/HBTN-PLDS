class Dog:
    def __init__(self, name):
        self.name = name  # Adding a name attribute

    def bark(self):  # Method that makes the dog "bark"
        print(f"{self.name} says Woof!")

# Creating an object (dog instance)
my_dog = Dog("Buddy")

# Calling the method
my_dog.bark()  # Output: Buddy says Woof!
