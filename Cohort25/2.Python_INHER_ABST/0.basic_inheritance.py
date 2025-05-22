# Parent class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        return f"{self.brand} moves at {self.speed} km/h."

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)  # Calling parent class constructor
        self.fuel_type = fuel_type
    
    def refuel(self):
        return f"{self.brand} is refueling with {self.fuel_type}."

# Creating an object
car = Car("Toyota", 120, "Petrol")
print(car.move())  # Output: Toyota moves at 120 km/h.
print(car.refuel())  # Output: Toyota is refueling with Petrol.

