# Parent class (Blueprint for all vehicles)
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        print(f"The {self.brand} moves at {self.speed} km/h.")

# Child class (Inheriting from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)  # Calling parent class constructor
        self.fuel_type = fuel_type  # New attribute specific to Car
    
    def refuel(self):
        print(f"The {self.brand} car is refueling with {self.fuel_type}.")

# Creating objects from classes
my_car = Car("Toyota", 120, "Petrol")

# Accessing inherited method
my_car.move()  # Output: The Toyota moves at 120 km/h.

# Accessing method specific to Car
my_car.refuel()  # Output: The Toyota car is refueling with Petrol.



#Why Use Inheritance?
#Reduces code duplication by reusing common functionality.
#Allows easy modifications: Changes in the parent class automatically reflect in child classes.
#Creates hierarchical relationships between objects.
#Improves code organization and readability.