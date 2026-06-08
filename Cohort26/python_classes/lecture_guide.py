class ParentClass:
    # Parent class definition
    pass

# ChildClass inherits from ParentClass
class ChildClass(ParentClass):  
    # Child class definition
    pass



# Parent class definition
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        return f"{self.name} is breathing"
    
    def move(self):
        return f"{self.name} is moving"

# Child class inheriting from Animal
class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed      # Add child-specific attribute
    
    def bark(self):             # Add child-specific method
        return f"{self.name} says Woof!"






class Animal:
    def breathe(self):
        return "Breathing..."

class Dog(Animal):
    def bark(self):
        return "Woof! Woof!"

my_dog = Dog()
print(my_dog.breathe())  # Output: Breathing...
print(my_dog.bark())     # Output: Woof! Woof!






class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack! Quack!"

my_duck = Duck()
print(my_duck.fly())    # Output: I can fly!
print(my_duck.swim())   # Output: I can swim!
print(my_duck.quack())  # Output: Quack! Quack!







class Grandparent:
    def wisdom(self):
        return "Share wisdom with family."

class Parent(Grandparent):
    def guidance(self):
        return "Guide the next generation."

class Child(Parent):
    def play(self):
        return "Playing with toys."

kid = Child()
print(kid.wisdom())    # Output: Share wisdom with family.
print(kid.guidance())  # Output: Guide the next generation.
print(kid.play())      # Output: Playing with toys.








class Appliance:
    def plug_in(self):
        return "Appliance is plugged in."

class WashingMachine(Appliance):
    def wash_clothes(self):
        return "Washing clothes..."

class Refrigerator(Appliance):
    def cool_food(self):
        return "Cooling food..."

wm = WashingMachine()
fridge = Refrigerator()

print(wm.plug_in())        # Output: Appliance is plugged in.
print(wm.wash_clothes())   # Output: Washing clothes...
print(fridge.cool_food())  # Output: Cooling food...






# These three class definitions are identical:
class MyClass:          # Implicitly inherits from object
    pass

class MyClass():        # Implicitly inherits from object  
    pass

class MyClass(object):  # Explicitly inherits from object
    pass

# All result in the same thing
print(isinstance(MyClass(), object))  # Output: True
print(issubclass(MyClass, object))    # Output: True





# Example class
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

# Check attributes and methods of the class
print(dir(Person))


# Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
#          '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
#          '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
#          '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
#          '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'greet']





class Student:
    def __init__(self, name):
        self.name = name        # 1. During initialization
    
    def enroll(self, course):
        self.course = course    # 3. In methods

student = Student("Bob")
student.grade = "A"            # 4. From outside the class
student.graduation_year = 2024 # 4. From outside the class

print(student.name)            # "Bob"
print(student.grade)           # "A" 
print(student.graduation_year) # 2024

student.enroll("Computer Science")
print(student.course)          # "Computer Science"







class RestrictedClass:
    __slots__ = ['name', 'age']  # Only these attributes allowed
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = RestrictedClass("Alice", 30)
person.name = "Bob"  # ✓ Allowed
# person.hobby = "reading"  # ✗ AttributeError: no attribute 'hobby'








class Employee:
    def work(self):
        return "Completing assigned tasks."
    
    def get_salary(self):
        return 50000

class Manager(Employee):
    def work(self):  # Overriding the parent method
        return "Overseeing team operations."
    
    def get_salary(self):  # Overriding the parent method
        return 80000

# Comparison
emp = Employee()
mgr = Manager()

print(emp.work())        # Output: Completing assigned tasks.
print(mgr.work())        # Output: Overseeing team operations.
print(emp.get_salary())  # Output: 50000
print(mgr.get_salary())  # Output: 80000






class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        print(f"Vehicle initialized: {brand}")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        # Use super() to initialize parent class attributes
        super().__init__(brand, speed)
        # Add the new attribute specific to Car
        self.fuel_type = fuel_type
        print(f"Car initialized with fuel type: {fuel_type}")

# Create a Car instance
my_car = Car("Toyota", 120, "Gasoline")

# Access all attributes
print(f"Brand: {my_car.brand}")
print(f"Speed: {my_car.speed}")
print(f"Fuel Type: {my_car.fuel_type}")



class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

my_dog = Dog()

# Basic usage
print(isinstance(my_dog, Dog))     # True - exact match
print(isinstance(my_dog, Animal))  # True - inheritance match
print(isinstance(my_dog, Cat))     # False - no relationship




# Check subclass inheritance
print(issubclass(Dog, Animal))    # True
print(issubclass(Animal, Dog))    # False - wrong direction
print(issubclass(Dog, object))    # True - everything inherits from object




# Get type information
print(type(my_dog))                    # <class '__main__.Dog'>
print(type(my_dog).__name__)           # "Dog"

# Exact type checking
print(type(my_dog) is Dog)             # True - exact match
print(type(my_dog) is Animal)          # False - not exact match
print(isinstance(my_dog, Animal))      # True - inheritance-aware





class Shape:
    def area(self):
        return 0  # Placeholder (bad practice!)





from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass  # No implementation, just an obligation


from abc import ABC, abstractmethod


class AbstractClassName(ABC):  # Inherit from ABC
    @abstractmethod
    def method_name(self):
        pass  # No implementation required


class ConcreteClass(AbstractClassName):
    def method_name(self):
        # Must provide implementation
        return "Implementation here"






from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for all payment processors"""
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id):
        pass
    
    def log_transaction(self, message):  # Concrete method
        print(f"Transaction Log: {message}")

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction(f"Processing ${amount} via Credit Card")
        return f"Credit card payment of ${amount} processed successfully"
    
    def refund_payment(self, transaction_id):
        self.log_transaction(f"Refunding transaction {transaction_id}")
        return f"Credit card refund for transaction {transaction_id} completed"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction(f"Processing ${amount} via PayPal")
        return f"PayPal payment of ${amount} processed successfully"
    
    def refund_payment(self, transaction_id):
        self.log_transaction(f"Refunding transaction {transaction_id}")
        return f"PayPal refund for transaction {transaction_id} completed"

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction(f"Processing ${amount} via Bank Transfer")
        return f"Bank transfer of ${amount} processed successfully"
    
    def refund_payment(self, transaction_id):
        self.log_transaction(f"Refunding transaction {transaction_id}")
        return f"Bank transfer refund for transaction {transaction_id} completed"
