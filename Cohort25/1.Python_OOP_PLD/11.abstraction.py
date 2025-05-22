#Why we need to import ABC and abstractmethod from abc module?
#The ABC (Abstract Base Class) and abstractmethod 
# are used to create abstract classes in Python.
#Abstract classes cannot be instantiated and
# are designed to be subclassed by other classes.
#The abstractmethod decorator is used to define abstract methods,
# which must be implemented by child classes.


from abc import ABC, abstractmethod

# Abstract class (Blueprint)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # This method must be implemented by child classes

# Child classes implementing the abstract method
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with a key."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started with a button."

# Creating objects
car = Car()
bike = Motorcycle()

print(car.start_engine())  # Output: Car engine started with a key.
print(bike.start_engine())  # Output: Motorcycle engine started with a button.



#Why Use Abstraction?
#Hides complex details, exposing only essential functionality.
#Encourages consistency, ensuring all child classes implement the required methods.
#Improves code organization and maintainability.