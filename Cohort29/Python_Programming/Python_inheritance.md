# Python Classes: Inheritance and Abstract

---

## Part 1: Inheritance

---

### What is Inheritance?

**Inheritance** is a fundamental concept in Object-Oriented Programming (OOP) that allows a class to derive properties and behaviors from another class. This enables code reusability, logical organization, and improved maintainability.

#### Why is Inheritance Important?

Imagine a world where every new car model had to be designed from scratch, without using existing designs or features. It would be inefficient! Instead, car manufacturers build upon previous designs, reusing proven features while adding unique elements. This is exactly what inheritance does in programming.

---

### Real-World Analogies

#### 1. Family Inheritance

Think about how we inherit physical traits from our parents. A child may inherit eye color, hair type, and even habits from their parents. However, the child is also unique and can develop their own characteristics over time.

This is similar to how a **child class** in Python inherits from a **parent class** but can also have its own attributes and methods.

#### 2. Electronic Devices

Consider a generic `ElectronicDevice` class. Every electronic device shares common traits such as a power button and a charging port. However, different devices like `Smartphone` and `Laptop` have their unique functionalities. Instead of redefining power-related features for every device, they inherit them from `ElectronicDevice` while implementing their own specific behaviors.

---

### Types of Inheritance in Python

#### 1. Single Inheritance

A child class inherits from a single parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"


my_dog = Dog("Rex")
print(my_dog.speak())  # Rex says: Woof!
```

---

#### 2. Multiple Inheritance

A child class inherits from multiple parent classes.

```python
class Flyable:
    def fly(self):
        return "I can fly!"


class Swimmable:
    def swim(self):
        return "I can swim!"


class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"


donald = Duck()
print(donald.fly())    # I can fly!
print(donald.swim())   # I can swim!
print(donald.quack())  # Quack!
```

---

#### 3. Multilevel Inheritance

A class inherits from another class, which in turn inherits from another class, forming a chain.

```python
class Vehicle:
    def move(self):
        return "The vehicle moves."


class Car(Vehicle):
    def honk(self):
        return "Beep beep!"


class ElectricCar(Car):
    def charge(self):
        return "Charging battery..."


tesla = ElectricCar()
print(tesla.move())    # The vehicle moves.
print(tesla.honk())    # Beep beep!
print(tesla.charge())  # Charging battery...
```

---

#### 4. Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

```python
class Shape:
    def color(self):
        return "I have a color."


class Circle(Shape):
    def area(self, radius):
        return 3.14159 * radius ** 2


class Rectangle(Shape):
    def area(self, width, height):
        return width * height


c = Circle()
r = Rectangle()
print(c.color())        # I have a color.
print(c.area(5))        # 78.53975
print(r.color())        # I have a color.
print(r.area(4, 6))     # 24
```

---

### Method Overriding

**Method overriding** allows a child class to redefine a method inherited from the parent class. The child's version of the method takes priority when called on a child object.

```python
class Animal:
    def speak(self):
        return "Some generic animal sound."


class Cat(Animal):
    def speak(self):  # Overrides Animal.speak()
        return "Meow!"


class Dog(Animal):
    def speak(self):  # Overrides Animal.speak()
        return "Woof!"


animals = [Animal(), Cat(), Dog()]
for animal in animals:
    print(animal.speak())
# Some generic animal sound.
# Meow!
# Woof!
```

---

### Using `super()` to Call Parent Attributes

When a child class needs to extend (not replace) the parent's `__init__`, use `super().__init__()` to properly initialize inherited attributes. This avoids code duplication and maintains a clean inheritance hierarchy.

```python
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} — top speed: {self.speed} km/h"


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)   # Calls Vehicle.__init__()
        self.fuel_type = fuel_type       # Car-specific attribute

    def describe(self):
        base = super().describe()        # Reuse parent method
        return f"{base}, fuel: {self.fuel_type}"


my_car = Car("Toyota", 180, "Gasoline")
print(my_car.describe())
# Toyota — top speed: 180 km/h, fuel: Gasoline
```

> **Key takeaway:** Without `super().__init__()`, the child class would need to manually re-assign `brand` and `speed`, duplicating code from the parent.

---

### Inheritance Summary

Inheritance is a powerful feature that allows Python classes to:

- **Reuse code efficiently** — child classes get all parent functionality for free.
- **Maintain a clear and logical structure** — related classes live in a hierarchy.
- **Reduce duplication** and **improve maintainability** — change the parent, and all children benefit.

---

## Part 2: Abstraction

---

### What is Abstraction?

**Abstraction** is one of the four fundamental principles of OOP (along with Encapsulation, Inheritance, and Polymorphism).

> **Abstraction means hiding unnecessary details and showing only the essential features.**

For example, when you drive a car:
- You don't need to know how the engine works internally.
- You only need to know how to use the steering wheel, gas, and brake.

Similarly, in programming, abstraction lets us define a **template or blueprint** (an abstract class) without worrying about how each subclass will implement it.

---

### What is an Abstract Base Class (ABC)?

An **Abstract Base Class (ABC)** is a class that **cannot be instantiated on its own**. Instead, it serves as a blueprint for other classes, forcing them to implement certain methods.

Think of it like a workplace contract:
- A company requires all employees to **clock in** and **clock out** every day.
- The company itself doesn't clock in, but all employees must follow the rule.
- Similarly, an abstract class defines methods that **all child classes must implement**.

---

### Why Use Abstract Base Classes?

Imagine building a program to calculate the area of different shapes. You want to guarantee that every shape class has an `area()` method — but each shape calculates area differently.

#### Without abstraction (bad practice):

```python
class Shape:
    def area(self):
        return 0  # Placeholder — subclasses might forget to override this!


class Circle(Shape):
    pass  # Forgot to implement area() — no error raised!


c = Circle()
print(c.area())  # Returns 0 silently — a hidden bug!
```

#### With abstraction (correct approach):

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # No implementation — just an obligation


class Circle(Shape):
    pass  # Missing area() implementation


c = Circle()
# TypeError: Can't instantiate abstract class Circle
# with abstract method area
```

Using `ABC` forces every subclass to implement `area()` or Python raises an error immediately.

---

### Implementing Abstract Classes Properly

```python
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every shape must define how to calculate its area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape must define how to calculate its perimeter."""
        pass

    def describe(self):
        """Concrete method shared by all shapes."""
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.describe())
# Area: 78.54, Perimeter: 31.42
# Area: 24.00, Perimeter: 20.00
```

---

### What Happens When We Import ABC?

```python
from abc import ABC, abstractmethod
```

Two things happen:

1. **It activates the rule of abstraction** — by inheriting from `ABC`, Python knows this class is abstract and should never be instantiated directly.

2. **It enables `@abstractmethod`** — any method decorated with `@abstractmethod` becomes a requirement that all subclasses must fulfill.

```python
from abc import ABC, abstractmethod


class DatabaseConnection(ABC):

    @abstractmethod
    def connect(self):
        """Subclasses must define how to connect."""
        pass

    @abstractmethod
    def disconnect(self):
        """Subclasses must define how to disconnect."""
        pass

    def status(self):
        """A concrete (non-abstract) method."""
        return "Connection object created."


class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to MySQL..."

    def disconnect(self):
        return "Disconnecting from MySQL."


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgreSQL..."

    def disconnect(self):
        return "Disconnecting from PostgreSQL."


# DatabaseConnection()  ← TypeError! Cannot instantiate abstract class.

db = MySQLConnection()
print(db.connect())     # Connecting to MySQL...
print(db.status())      # Connection object created.
print(db.disconnect())  # Disconnecting from MySQL.
```

---

### Abstraction Summary

Abstract Base Classes (ABC) play a crucial role in enforcing structure and consistency in OOP:

- **Abstract classes cannot be instantiated** — they exist only as blueprints.
- **Subclasses must implement all abstract methods** — preventing incomplete or inconsistent implementations.
- **Every derived class adheres to a defined contract** — making the codebase more maintainable, scalable, and predictable.
- **Concrete methods can still exist in ABCs** — shared logic lives in the parent, while unique behavior is delegated to subclasses.

---

## Part 3: Interfaces and Duck Typing

---

### What is an Interface?

An **interface** is a contract that defines *what* methods an object must have, without specifying *how* they work. In Python, there is no `interface` keyword like in Java — instead, interfaces are expressed through **Abstract Base Classes** or simply through convention.

---

### Duck Typing

Python follows the principle of **duck typing**:

> *"If it walks like a duck and quacks like a duck, it's a duck."*

This means Python doesn't care about the *type* of an object — only whether it has the methods or attributes being called. If it does, it works.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep boop."

# Neither inherits from a common base — but both "speak"
for thing in [Dog(), Robot()]:
    print(thing.speak())
# Woof!
# Beep boop.
```

No shared parent class is needed. Python simply calls `speak()` and trusts that the object knows what to do.

---

### Informal Interfaces vs. ABC

| | Informal (Duck Typing) | Formal (ABC) |
|---|---|---|
| Enforced? | No — fails at runtime | Yes — fails at instantiation |
| Requires import? | No | `from abc import ABC, abstractmethod` |
| Best for? | Small, flexible code | Large codebases, team contracts |

Use duck typing for flexibility. Use ABCs when you want Python to catch missing implementations early.

---

### Checking Compatibility with `hasattr`

When using duck typing, you can check if an object supports an operation before calling it:

```python
def make_it_speak(obj):
    if hasattr(obj, "speak"):
        print(obj.speak())
    else:
        print("This object can't speak.")
```

> **Key takeaway:** Duck typing shifts the focus from *"what type is this?"* to *"can this object do what I need?"*

---

## Part 4: Subclassing Standard Base Classes

---

### Why Subclass Built-ins?

Python's built-in types (`list`, `dict`, `int`, etc.) can be extended to create **custom data structures** with specialized behavior, while keeping all the original functionality.

---

### Extending `list`

```python
class VerboseList(list):
    def append(self, item):
        print(f"Adding: {item}")
        super().append(item)

    def remove(self, item):
        print(f"Removing: {item}")
        super().remove(item)


vl = VerboseList()
vl.append(10)   # Adding: 10
vl.append(20)   # Adding: 20
vl.remove(10)   # Removing: 10
print(vl)       # [20]
```

All standard `list` methods (`sort`, `pop`, indexing, etc.) still work — we only changed the behavior of `append` and `remove`.

---

### Extending `dict`

```python
class DefaultDict(dict):
    def __missing__(self, key):
        return "Key not found"


d = DefaultDict({"name": "Alex"})
print(d["name"])   # Alex
print(d["age"])    # Key not found  (no KeyError!)
```

`__missing__` is called automatically by Python when a key doesn't exist, making it a clean hook for custom fallback behavior.

---

### Extending Iterators

You can create custom iterators by implementing `__iter__` and `__next__`:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


for n in Countdown(3):
    print(n)
# 3
# 2
# 1
```

Any class that implements `__iter__` and `__next__` is a valid iterator — no inheritance required (duck typing in action).

---

## Part 5: Mixins

---

### What is a Mixin?

A **Mixin** is a class that provides reusable methods to other classes through multiple inheritance, without being a standalone class itself. Mixins are not meant to be instantiated directly — they are designed to be *mixed in* to other classes.

Think of a mixin like a plugin: you snap it onto any class that needs that feature.

---

### Mixin Example

```python
class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")


class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class User(LogMixin, JsonMixin):
    def __init__(self, name, role):
        self.name = name
        self.role = role


u = User("Ana", "admin")
u.log("User created.")          # [User] User created.
print(u.to_json())              # {"name": "Ana", "role": "admin"}
```

`LogMixin` and `JsonMixin` have no relationship to `User` — they just add capabilities. Any other class can also mix them in.

---

### Mixins vs. Inheritance

| | Regular Inheritance | Mixin |
|---|---|---|
| Purpose | "Is-a" relationship | Adds a capability |
| Instantiated? | Yes | No (by convention) |
| Example | `Dog` is an `Animal` | `User` *has* logging behavior |

> **Naming convention:** Mixins are typically named with the `Mixin` suffix to make their role clear.

---

### MRO — Method Resolution Order

When using multiple inheritance or mixins, Python uses the **MRO** to decide which class's method to call. You can inspect it with `__mro__`:

```python
print(User.__mro__)
# (<class 'User'>, <class 'LogMixin'>, <class 'JsonMixin'>, <class 'object'>)
```

Python searches left to right, so the order you list parent classes matters. This also resolves the **Diamond Problem** — when two parents share a common ancestor, Python ensures each class is only called once.

---

## Full OOP Concepts Summary

| Concept | Purpose | Key Tool |
|---|---|---|
| Inheritance | Reuse and extend behavior | `class Child(Parent)` |
| Method Overriding | Replace parent behavior | Redefine method in child |
| `super()` | Extend (not replace) parent | `super().__init__()` |
| Abstraction | Enforce a contract | `ABC`, `@abstractmethod` |
| Duck Typing | Flexible interfaces | `hasattr`, convention |
| Subclassing Built-ins | Custom data structures | Extend `list`, `dict`, etc. |
| Mixins | Reusable, composable behavior | Multiple inheritance |

---

> *"May your code be clean, your coffee be strong, and your bugs be non-existent!"*
>
> — Holberton