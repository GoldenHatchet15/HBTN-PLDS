# Python Classes and Objects — Full Beginner Lecture

# 🌟 Introduction to Object-Oriented Programming (OOP)

Before learning classes and objects, think about the real world.

Everything around us is made of objects:

* Cars
* Phones
* Students
* Bank accounts
* Books
* Animals

Every object has:

1. **Attributes (data / characteristics)**
2. **Behaviors (actions / things it can do)**

Example:

A car has:

### Attributes

* Color
* Brand
* Speed
* Year

### Behaviors

* Start
* Stop
* Accelerate
* Brake

Object-Oriented Programming lets us model real-world things using code.

---

# 🧠 What is OOP?

OOP stands for:

## Object-Oriented Programming

It is a programming style where we organize code using:

* Classes
* Objects
* Attributes
* Methods

Instead of writing everything in one long script, we group related things together.

---

# 🎯 Why OOP Exists

OOP helps us:

* Organize code
* Reuse code
* Make programs easier to maintain
* Model real-world systems
* Work better in teams

---

# 🧱 "First-Class Everything" in Python

Python treats many things as objects.

This is called:

# “First-class everything”

It means:

Functions, classes, variables, and objects can all:

* Be stored in variables
* Be passed into functions
* Be returned from functions
* Be modified dynamically

Example:

```python
x = 5

print(type(x))
```

Output:

```python
<class 'int'>
```

Even integers are objects in Python.

Another example:

```python
def hello():
    print("Hello")

x = hello
x()
```

Functions themselves are objects.

Classes are also objects.

Everything in Python is built around objects.

---

# 🏗️ What is a Class?

A class is a:

# Blueprint

or

# Template

used to create objects.

Think about:

* House blueprint → used to build houses
* Cookie cutter → used to make cookies
* Car factory design → used to build cars

A class defines:

* What data objects will have
* What actions objects can perform

---

# 🧪 Creating Our First Class

```python
class Student:
    pass
```

---

# 🔍 Understanding This Syntax

```python
class Student:
```

* `class` → keyword to create a class
* `Student` → class name
* `:` → starts the class block

```python
pass
```

`pass` means:

“Do nothing for now.”

The class exists but has no content yet.

---

# 📦 What is an Object?

An object is:

# A real instance created from a class

If the class is the blueprint,
then the object is the real thing.

---

# 🧪 Creating Objects

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

---

# 🧠 What Happened?

```python
student1 = Student()
```

This creates a new object.

`Student()` means:

“Create a Student object.”

Every time we call:

```python
Student()
```

Python creates a completely new object in memory.

---

# 🔥 Object vs Instance

These words usually mean the same thing.

* Object
* Instance

Both refer to a real thing created from a class.

---

# ⚖️ Difference Between a Class and an Object

## Class

Blueprint/template.

Example:

```python
class Student:
    pass
```

---

## Object

Actual thing created from the class.

Example:

```python
student1 = Student()
```

---

# 🧠 Real-World Analogy

| Class         | Object        |
| ------------- | ------------- |
| Car blueprint | Actual car    |
| Cookie cutter | Actual cookie |
| House design  | Actual house  |

---

# 🧾 What is an Attribute?

An attribute is:

# A variable attached to an object

Attributes store data.

---

# 🧪 Example

```python
class Student:
    pass

student1 = Student()

student1.name = "Ana"
student1.age = 20
```

Now the object has attributes.

---

# 🧠 Understanding This

```python
student1.name = "Ana"
```

This dynamically creates an attribute called:

```python
name
```

attached only to:

```python
student1
```

---

# 🔍 Accessing Attributes

```python
print(student1.name)
print(student1.age)
```

Output:

```python
Ana
20
```

---

# 🔥 Dynamic Attribute Creation

Python allows us to create attributes dynamically.

Example:

```python
student1.grade = "A"
```

Even if the class never defined `grade`, Python allows it.

This is possible because Python is highly dynamic.

---

# 🔒 Public, Protected, and Private Attributes

Python has naming conventions for attribute visibility.

---

# 🟢 Public Attributes

Accessible everywhere.

Example:

```python
class Student:
    def __init__(self):
        self.name = "Ana"
```

Access:

```python
student = Student()
print(student.name)
```

Works perfectly.

---

# 🟡 Protected Attributes

Convention only.

Single underscore:

```python
self._name
```

Means:

“Please don’t access this outside the class unless necessary.”

Example:

```python
class Student:
    def __init__(self):
        self._grade = "A"
```

Python still allows access:

```python
print(student._grade)
```

But programmers understand it should be treated carefully.

---

# 🔴 Private Attributes

Double underscore:

```python
self.__password
```

Example:

```python
class Student:
    def __init__(self):
        self.__password = "1234"
```

Trying:

```python
student.__password
```

will fail.

---

# 🧠 Why?

Python uses something called:

# Name Mangling

Internally Python changes:

```python
__password
```

into:

```python
_Student__password
```

This helps hide internal data.

---

# 👤 What is self?

`self` is one of the MOST IMPORTANT concepts in OOP.

`self` refers to:

# The current object using the method

---

# 🧪 Example

```python
class Student:
    def say_hello(self):
        print("Hello")
```

---

# 🧪 Creating an Object

```python
student1 = Student()
student1.say_hello()
```

---

# 🧠 What Python Internally Does

Python internally transforms:

```python
student1.say_hello()
```

into:

```python
Student.say_hello(student1)
```

So:

```python
self
```

becomes:

```python
student1
```

---

# 🧠 Important Rule

Inside class methods:

```python
self
```

must ALWAYS be the first parameter.

---

# ⚙️ What is a Method?

A method is:

# A function inside a class

Methods define behaviors/actions.

---

# 🧪 Example

```python
class Student:
    def study(self):
        print("Studying...")
```

---

# 🧪 Using the Method

```python
student1 = Student()
student1.study()
```

Output:

```python
Studying...
```

---

# 🚀 What is **init**?

`__init__` is a:

# Special method automatically called when creating an object

It is known as:

* Constructor
* Initializer

---

# 🧪 Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 🧪 Creating Objects

```python
student1 = Student("Ana", 20)
student2 = Student("Luis", 25)
```

---

# 🧠 Understanding Step-by-Step

When we do:

```python
student1 = Student("Ana", 20)
```

Python:

1. Creates an empty object
2. Calls `__init__`
3. Passes the object into `self`
4. Stores the values

---

# 🧾 Result

```python
student1.name
```

contains:

```python
Ana
```

and:

```python
student1.age
```

contains:

```python
20
```

---

# 🧠 Data Abstraction

Data Abstraction means:

# Hiding unnecessary complexity

Users only interact with what matters.

Example:

When driving a car:

* You use steering wheel
* Pedals
* Gear shifter

You do NOT manage:

* Fuel injection timing
* Engine combustion
* Electrical signals

The complex details are hidden.

---

# 🧠 Data Encapsulation

Encapsulation means:

# Bundling data and methods together inside a class

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
```

The object contains:

* Data (`__balance`)
* Behavior (`deposit`)

inside one structure.

---

# 🧠 Information Hiding

Information Hiding means:

# Preventing direct access to internal data

Example:

```python
self.__balance
```

The user should not directly modify important internal values.

---

# 🏠 What is a Property?

A property allows us to:

# Control attribute access

while still using attribute syntax.

Properties are the Pythonic way to create:

* Getters
* Setters

---

# ❌ Problem Without Properties

```python
class Student:
    def __init__(self, age):
        self.age = age
```

A user could do:

```python
student.age = -5
```

which makes no sense.

---

# ✅ Solution: Properties

```python
class Student:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self.__age = value
```

---

# 🧠 How This Works

When reading:

```python
student.age
```

Python calls:

```python
@property
```

method.

When assigning:

```python
student.age = 30
```

Python calls:

```python
@age.setter
```

method.

---

# ⚖️ Difference Between an Attribute and a Property

## Attribute

Simple stored variable.

Example:

```python
self.name = "Ana"
```

---

## Property

Controlled access mechanism.

Allows:

* Validation
* Protection
* Custom behavior

while looking like a normal attribute.

---

# 🐍 Pythonic Getters and Setters

In many languages:

```python
getAge()
setAge()
```

are common.

In Python:

We prefer:

```python
@property
```

because it looks cleaner.

---

# ❌ Non-Pythonic Style

```python
student.get_age()
student.set_age(20)
```

---

# ✅ Pythonic Style

```python
student.age
student.age = 20
```

while internally using properties.

---

# 🔥 Dynamically Creating New Attributes

Python allows objects to gain new attributes at runtime.

---

# 🧪 Example

```python
class Student:
    pass

student1 = Student()

student1.city = "Arecibo"
student1.country = "Puerto Rico"
```

These attributes did not exist before.

Python created them dynamically.

---

# 🔗 Binding Attributes to Objects and Classes

Attributes can belong to:

* Objects (instance attributes)
* Classes (class attributes)

---

# 🧪 Instance Attributes

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Every object gets its own value.

---

# 🧪 Example

```python
student1 = Student("Ana")
student2 = Student("Luis")
```

Each object stores different data.

---

# 🧪 Class Attributes

```python
class Student:
    school = "Holberton"
```

This attribute belongs to the CLASS itself.

---

# 🧪 Accessing Class Attributes

```python
print(Student.school)
```

or:

```python
student1 = Student()
print(student1.school)
```

Both work.

---

# 🧠 What is **dict**?

`__dict__` is a dictionary storing object/class attributes.

---

# 🧪 Instance **dict**

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Ana")

print(student1.__dict__)
```

Output:

```python
{'name': 'Ana'}
```

---

# 🧪 Class **dict**

```python
print(Student.__dict__)
```

Shows:

* Methods
* Class attributes
* Internal Python information

---

# 🔍 How Python Finds Attributes

When Python sees:

```python
student1.name
```

it searches in this order:

1. Inside the object itself
2. Inside the class
3. Parent classes (inheritance)

---

# 🧪 Example

```python
class Student:
    school = "Holberton"

student1 = Student()

print(student1.school)
```

Python:

1. Looks inside `student1`
2. Does not find `school`
3. Looks inside `Student`
4. Finds it there

---

# 🧠 What is getattr()?

`getattr()` dynamically accesses attributes.

---

# 🧪 Syntax

```python
getattr(object, attribute_name)
```

---

# 🧪 Example

```python
class Student:
    def __init__(self):
        self.name = "Ana"

student1 = Student()

print(getattr(student1, "name"))
```

Output:

```python
Ana
```

---

# 🧠 Why Use getattr()?

Useful when attribute names are stored as strings.

---

# 🧪 Example

```python
attribute = "name"

print(getattr(student1, attribute))
```

---

# 🚀 Final Full Example

```python
class Student:
    school = "Holberton"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self.__age = value

    def study(self):
        print(f"{self.name} is studying")

student1 = Student("Ana", 20)

student1.study()

print(student1.name)
print(student1.age)
print(Student.school)
print(student1.__dict__)
print(getattr(student1, "name"))
```

---

# 🎯 Key Concepts Summary

| Concept            | Meaning                          |
| ------------------ | -------------------------------- |
| Class              | Blueprint/template               |
| Object             | Real instance created from class |
| Attribute          | Variable attached to object      |
| Method             | Function inside class            |
| self               | Current object                   |
| **init**           | Constructor method               |
| Property           | Controlled attribute access      |
| Encapsulation      | Bundling data + methods          |
| Information Hiding | Protecting internal data         |
| **dict**           | Dictionary storing attributes    |
| getattr()          | Dynamically access attributes    |

---

# 🧪 Practice Exercises

## Exercise 1

Create a `Car` class with:

* brand
* color
* year

---

## Exercise 2

Add a method:

```python
start_engine()
```

---

## Exercise 3

Make `year` private.

---

## Exercise 4

Create a property for `year` with validation.

---

## Exercise 5

Print the object’s `__dict__`.

---

# 🎓 Final Important Idea

OOP is NOT just syntax.

OOP is a way of organizing programs.

The goal is to:

* Group related data together
* Group related behaviors together
* Create reusable and organized code

Classes describe what objects should look like.

Objects are the real things created from those classes.

That is the foundation of Object-Oriented Programming.
