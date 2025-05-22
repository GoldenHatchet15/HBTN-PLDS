#!/usr/bin/env python3

# Step 1: Define a Car class (Blueprint)

class Car:

    def __init__(self, brand, color):
        self.brand = brand  # Attribute (stores the car's brand)
        self.color = color  # Attribute (stores the car's color)
    
    def start(self):  # Method (an action the car can perform)
        print(f"The {self.color} {self.brand} is starting.")

# Creating an object from the Car class
my_car = Car("Toyota", "Red")

# Accessing attributes
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red

# Calling a method
my_car.start()  # Output: The Red Toyota is starting.




#Car is a class, which is like a blueprint for making cars.
#my_car is an object, which is an actual car with specific details.
#brand and color are attributes, which store information about the car.
#start() is a method, which is an action the car can do.
#We create an object using variable = class().
#We use variable.method() to call an object's function.