from abc import ABC, abstractmethod

#parent class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def describe(self):
        return "This is a shape."

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(10, 5)
print(rect.area())      # Output: 50
print(rect.describe())  # Output: This is a shape.
