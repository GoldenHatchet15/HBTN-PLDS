# Multiple methods in abstract class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car is starting."
    
    def stop(self):
        return "Car is stopping."

class Bike(Vehicle):
    def start(self):
        return "Bike is starting."
    
    def stop(self):
        return "Bike is stopping."

# Creating objects
car = Car()
bike = Bike()
print(car.start())  # Output: Car is starting.
print(car.stop())   # Output: Car is stopping.
print(bike.start()) # Output: Bike is starting.
print(bike.stop())  # Output: Bike is stopping.
