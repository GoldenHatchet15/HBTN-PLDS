# Python: Lists, Tuples, and Sequences

## 🎓 Introduction

Welcome! This lecture covers foundational data structures in Python: lists and tuples, as well as the concept of sequences. These are essential tools for every Python developer. You'll learn what they are, how they work, how to iterate through them, when to use each, and how to implement real-world use cases like stacks, queues, and matrices.

## 🔍 What is a Sequence?

A sequence in Python is an ordered collection of items that supports:

- **Indexing** (access items by number)
- **Slicing** (getting sub-parts)
- **Iteration** (going through each element one by one)

Examples of sequences:
- Strings
- Lists
- Tuples

## 📂 Lists

### What is a List?

A list is a sequence that is:
- **Ordered** (items have a position)
- **Mutable** (you can change, add, or remove items)
- **Defined with square brackets**: `[]`

### Creating a List

```python
my_list = [1, 2, 3, 4, 5]
```

### Accessing List Elements

```python
print(my_list[0])  # Output: 1
```

### Modifying List Elements

```python
my_list[2] = 9
print(my_list)  # Output: [1, 2, 9, 4, 5]
```

### Iterating Over a List

```python
for num in my_list:
    print(num)
```

### Iterating in Reverse

```python
for i in reversed(my_list):
    print(i)
```

Or using indexing:

```python
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])
```

### List Operations

- `append(x)` → Add x to the end
- `insert(i, x)` → Insert x at index i
- `remove(x)` → Remove first occurrence of x
- `pop(i)` → Remove item at index i
- `len(my_list)` → Length of the list

### Safe Access

```python
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
```

### Replace Element

```python
def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
```

### Replace in a Copy

```python
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list
```

### Deleting Elements

```python
def delete_at(my_list, idx):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
```

## 🔖 Lists as Stacks (LIFO)

A stack follows the Last-In, First-Out (LIFO) principle, meaning the last element added is the first one removed.

### Operations

- `append(x)` → Adds x to the top of the stack
- `pop()` → Removes and returns the top element

```python
stack = []
stack.append(1)   # [1]
stack.append(2)   # [1, 2]
stack.append(3)   # [1, 2, 3]

print(stack.pop())  # Output: 3 (stack is now [1, 2])
print(stack.pop())  # Output: 2 (stack is now [1])
```

## ↗️ Lists as Queues (FIFO)

A queue follows the First-In, First-Out (FIFO) principle, meaning the first element added is the first one removed.

### Preferred Method (Efficient)

Using `collections.deque` (optimized for fast pops from both ends).

### Operations

- `append(x)` → Adds x to the end of the queue
- `popleft()` → Removes and returns the first element

```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)      # deque([1, 2, 3, 4])

print(queue.popleft())  # Output: 1 (queue is now [2, 3, 4])
print(queue.popleft())  # Output: 2 (queue is now [3, 4])
```

## 🛋️ Tuples

### What is a Tuple?

A tuple is:
- An **ordered, immutable** collection
- **Defined with parentheses** `()`
- **Faster and safer** than lists

### Creating a Tuple

```python
tuple_a = (1, 2)
tuple_b = (3,)     # single item needs comma
```

### Accessing Tuple Elements

```python
print(tuple_a[1])  # Output: 2
```

### When to Use Tuples vs Lists

| Feature | List | Tuple |
|---------|------|-------|
| Mutable | Yes | No |
| Syntax | `[]` | `()` |
| Use Case | Changeable data | Fixed structure data |

### Adding Tuples

```python
def add_tuple(a=(), b=()):
    a = a + (0, 0)
    b = b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
```

## 🪡 Tuple Packing & Unpacking

### Packing

Packing means combining multiple values into a single tuple.

**Example: Packing**

```python
my_tuple = 5, "Hello"
```

### Unpacking

Unpacking means extracting values from a tuple into separate variables.

**Example: Unpacking**

```python
num, text = my_tuple
```

### Returning Multiple Values

Tuples are often used to return multiple values from a function.

**Example: Returning Multiple Values**

```python
def get_user():
    name = "Alice"
    age = 25
    return name, age  # Packing into a tuple

user_name, user_age = get_user()  # Unpacking the returned tuple
print(user_name)  # Output: "Alice"
print(user_age)   # Output: 25
```

## 📊 Working with Matrices (Lists of Lists)

A matrix is simply a list of lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print("{:d}".format(col), end=" ")
    print()
```

Empty matrix:
```python
print_matrix_integer([])  # prints nothing
```

## 🔄 Strings vs Lists

| Feature | String | List |
|---------|--------|------|
| Mutable | No | Yes |
| Indexing | Yes | Yes |
| Sliceable | Yes | Yes |

To remove characters from a string without using `.replace()`:

```python
def no_c(my_string):
    new_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
```

## 🤷🏼‍♂️ Other Utilities

### Finding the Maximum in a List

This function finds the largest integer in a list.

```python
def max_integer(my_list):
    if not my_list:          # Check if the list is empty
        return None          # Return None if empty
    max_val = my_list[0]     # Assume first element is the max
    for num in my_list[1:]:  # Iterate over remaining elements
        if num > max_val:    # If current number > current max
            max_val = num    # Update max_val
    return max_val           # Return the final max value
```

**Example Usage:**

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
print(max_integer(numbers))  # Output: 9

empty_list = []
print(max_integer(empty_list))  # Output: None
```

### Finding Multiples of 2

This function checks which numbers in a list are divisible by 2 (i.e., even numbers).

```python
def divisible_by_2(my_list):
    return [x % 2 == 0 for x in my_list]
```

- `x % 2 == 0` → True if x is even, False otherwise
- List comprehension → Generates a list of True/False values

### Value Switch

```python
a = 89
b = 10
a, b = b, a
```

## 🎉 Final Notes

- Lists and tuples are fundamental data structures
- Know when to use mutability
- Practice by writing functions and building small tools like:
  - A matrix printer
  - A queue system
  - A tuple calculator


# Python: Sets, Dictionaries, Lambda, Map, Filter, Reduce

## 🎓 Introduction

Welcome! In this lecture, we'll explore more powerful data structures in Python: sets and dictionaries. These allow us to organize data in unique ways and perform efficient lookups. We'll also cover the powerful lambda, map, filter, and reduce functions for functional programming in Python.

## 🔹 Sets in Python

### What is a Set?

A set is:
- An **unordered, unindexed** collection
- That contains only **unique elements**
- **Defined with curly braces**: `{}`

```python
my_set = {1, 2, 3, 2, 1}
print(my_set)  # Output: {1, 2, 3}
```

### Creating a Set

```python
set1 = set([1, 2, 3])
set2 = {"apple", "banana", "cherry"}
```

### Iterating Over a Set

```python
for item in set2:
    print(item)
```

### Common Set Methods

**`add(x)`**: Adds an element to the set.

```python
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}
```

**`remove(x)`**: Removes an element from the set. Raises KeyError if element doesn't exist.

```python
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}
# s.remove(5) would raise KeyError
```

**`discard(x)`**: Removes an element if present (does nothing if element doesn't exist).

```python
s = {1, 2, 3}
s.discard(2)
s.discard(5)  # No error
print(s)  # Output: {1, 3}
```

**`union(set2)`**: Returns a new set with elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
print(set1 | set2)       # Same as above
```

**`intersection(set2)`**: Returns common elements between sets.

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))  # Output: {2, 3}
print(set1 & set2)              # Same as above
```

**`difference(set2)`**: Returns elements in first set but not in second.

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))  # Output: {1}
print(set1 - set2)            # Same as above
```

### Set Use Cases

**Removing duplicates from a list:**

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5] (order may vary)
```

**Membership testing** (`in`) is faster in sets than in lists:

```python
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True (much faster than list for large collections)
```

### Task Examples

**Sum of unique elements:**

```python
def uniq_add(my_list=[]):
    return sum(set(my_list))

print(uniq_add([1, 2, 3, 1, 4, 2, 5]))  # Output: 15 (1+2+3+4+5)
```

**Common elements between sets:**

```python
def common_elements(set_1, set_2):
    return set_1 & set_2  # or set_1.intersection(set_2)

print(common_elements({1, 2, 3}, {2, 3, 4}))  # Output: {2, 3}
```

**Symmetric difference** (elements in either set but not both):

```python
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2  # or set_1.symmetric_difference(set_2)

print(only_diff_elements({1, 2, 3}, {2, 3, 4}))  # Output: {1, 4}
```

## 📖 Dictionaries in Python

### What is a Dictionary?

A dictionary (or "dict") is:
- A collection of **key-value pairs**
- **Unordered** before Python 3.7, but now **preserves order**
- **Defined with** `{ key: value }`

**Example:**

```python
my_dict = {"name": "Rapha", "age": 25}
print(my_dict["name"])  # Output: Rapha
```

### Dictionary Keys

- Keys must be **unique**
- Keys must be **immutable types** (str, int, tuple, etc.)

### Iterating

```python
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### Common Methods

**`keys()`** Returns a view object containing the dictionary's keys.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])
```

**`values()`** Returns a view object containing the dictionary's values.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.values())  # Output: dict_values([1, 2, 3])
```

**`items()`** Returns a view object containing key-value tuples.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
```

**`get(key, default)`** Returns the value for key if it exists, otherwise returns default (None if not specified).

```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))      # Output: 1
print(my_dict.get('c'))      # Output: None
print(my_dict.get('c', 0))   # Output: 0
```

**`pop(key)`** Removes the key and returns its value. Raises KeyError if key doesn't exist.

```python
my_dict = {'a': 1, 'b': 2}
val = my_dict.pop('a')
print(val)      # Output: 1
print(my_dict)  # Output: {'b': 2}
```

### Task Examples

**1. Count dictionary keys:**

```python
def number_keys(a_dictionary):
    return len(a_dictionary)

print(number_keys({'a': 1, 'b': 2}))  # Output: 2
```

**2. Print sorted dictionary:**

```python
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")

print_sorted_dictionary({'b': 2, 'a': 1, 'c': 3})
# Output:
# a: 1
# b: 2
# c: 3
```

**3. Update dictionary:**

```python
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

my_dict = {'a': 1}
print(update_dictionary(my_dict, 'b', 2))  # Output: {'a': 1, 'b': 2}
```

**4. Delete key from dictionary:**

```python
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

my_dict = {'a': 1, 'b': 2}
print(simple_delete(my_dict, 'a'))  # Output: {'b': 2}
print(simple_delete(my_dict, 'c'))  # Output: {'b': 2} (no error)
```

**5. Multiply all values by 2:**

```python
def multiply_by_2(a_dictionary):
    return {k: v * 2 for k, v in a_dictionary.items()}

print(multiply_by_2({'a': 1, 'b': 2}))  # Output: {'a': 2, 'b': 4}
```

**6. Find key with maximum value:**

```python
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)

print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16}))
# Output: 'Molly'
print(best_score({}))  # Output: None
```

## 🤖 Lambda Functions

Lambda functions are small, anonymous functions in Python that can have any number of arguments but only one expression. They're useful for creating quick, throwaway functions without formally defining them with `def`.

```python
lambda arguments: expression
```

### Key Characteristics

- **Anonymous**: They don't have a name (unless assigned to a variable)
- **Single expression**: Can only contain one expression (no statements or multiple lines)
- **First-class objects**: Can be passed as arguments to other functions

### Usage Example

```python
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

## 🔄 Functional Programming Tools

### `map()`

Applies a function to every item:

```python
my_list = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, my_list))  # [2, 4, 6, 8]
```

**Project example:**

```python
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
```

### `filter()`

Filters items based on a function:

```python
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
```

### `reduce()`

Applies a rolling computation to a list:

```python
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # Output: 24
```

## 🧰 2D Lists and Matrix Operations

```python
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]
```

Ensures original matrix is untouched while computing square values.

## 📌 Use Case: Search and Replace

```python
def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
```

Creates a new list without altering the original.

## ⚖️ Summary: When to Use

| Structure | Use When... |
|-----------|------------|
| **List** | You need ordered, changeable data with duplicates |
| **Set** | You need uniqueness and fast membership tests |
| **Dict** | You need key-value access, fast lookup by keys |

## 🥇 Wrap-Up

- **Sets** help eliminate duplicates and do math-like operations on data
- **Dictionaries** allow fast key-based data retrieval
- **Lambdas** make functions quick and anonymous
- **map, filter, reduce** = powerful data transformation tools






# Python Exceptions:

## 📅 Introduction

In this lesson, we will explore the Exceptions system in Python. Exceptions are how Python handles errors in a program without immediately crashing. Instead of letting errors break your code, you can manage them and continue running your program smoothly.

## 🚫 Errors vs Exceptions

### Errors

Errors are serious problems that stop a program from running. For example:

```python
print(unknown_variable)  # NameError: name 'unknown_variable' is not defined
```

### Exceptions

Exceptions are runtime events that indicate something went wrong, but they can be caught and handled:

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

## ✅ try / except: Catching Errors Gracefully

Python allows us to try something and except if it fails:

```python
try:
    risky_code()
except SomeError:
    handle_it()
```

**Example:**

```python
try:
    value = int(input("Enter a number: "))
    print("You entered:", value)
except ValueError:
    print("That's not a valid number!")
```

## ✅ Multiple except Blocks

You can catch different exceptions separately:

```python
try:
    a = int("5a")
except ValueError:
    print("This is a value error.")
except TypeError:
    print("This is a type error.")
```

## 🛠️ finally: Code That Always Runs

The `finally` block will always execute, even if there is an exception:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Divide by zero error")
finally:
    print("This code always runs")
```

**Useful for:**
- Closing files
- Releasing network connections
- Cleaning up temporary resources

## 🚨 raise: Triggering Your Own Exceptions

You can manually raise exceptions using `raise`:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

## 🔍 Task-Specific Detailed Examples

### Task 0 – Safe List Printing

```python
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Just skip the error
    print()
    return count
```

✅ Safely prints x items even if the list is shorter.

### Task 1 – Safe Integer Printing

```python
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
```

✅ Returns True if value is an integer, False otherwise.

### Task 2 – Print and Count Integers

```python
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
```

✅ Prints only integers, silently skips other types.

### Task 3 – Division with Debug

```python
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
```

✅ Prints result inside the finally block whether it succeeded or failed.

### Task 4 – List Division with Full Checks

```python
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
```

✅ Handles all errors and returns a list with safe division results.

### Task 5 – Raising a TypeError

```python
def raise_exception():
    raise TypeError("Intentional TypeError")
```

✅ This will raise a TypeError when called.

### Task 6 – Raising with a Message

```python
def raise_exception_msg(message=""):
    raise NameError(message)
```

✅ You can control the error message shown to the user.

## 🧼 Common Use Case: File Handling

```python
try:
    f = open("my_file.txt")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    f.close()
```

✅ Always closes the file no matter what.

## 💡 Best Practices

- **Catch specific exceptions**, not just `except:`
- **Use `finally`** to clean up external resources
- **Use `raise`** to enforce constraints in functions
- **Avoid catching exceptions** unless you plan to handle them properly

## 🧠 Summary

| Concept | Usage |
|---------|-------|
| `try/except` | Catch errors that may happen |
| `finally` | Always runs (cleanup code) |
| `raise` | Manually trigger exceptions |
| `except TypeError` | Catch specific exception types |



# Test-Driven Development in Python

## 📚 What is Test-Driven Development (TDD)?

Test-Driven Development (TDD) is a method where you write tests first, then write the actual code that passes the tests.

### The TDD cycle:

1. **Write a test** (which will initially fail)
2. **Write the minimum code** to make the test pass
3. **Run the test** to ensure it passes
4. **Refactor the code** while keeping tests green (passing)

This ensures you focus on correctness and reliability from the start.

## 🎨 Why is TDD Important?

- **Forces you to think** before coding
- **Catches bugs early**
- **Helps create clean, modular code**
- **Makes collaboration easier**
- **Builds confidence** in your code

## ✍️ Writing Tests Before Code

In Python, tests can be written using:
- **`doctest`** (in separate .txt files for this project)
- **`unittest`** (for larger, structured tests)

We'll begin with `doctest` in separate text files.

## 🔢 Example: add_integer(a, b=98)

### Function Implementation:

```python
def add_integer(a, b=98):
    """Adds two integers with type checking."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
```

### Corresponding Test File (tests/0-add_integer.txt):

```python
>>> from 0-add_integer import add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100)
198
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
TypeError: b must be an integer
>>> add_integer(None)
Traceback (most recent call last):
TypeError: a must be an integer
```

**Run the tests with:**

```bash
python3 -m doctest -v tests/0-add_integer.txt
```

## 📃 Task 1: matrix_divided(matrix, div)

```python
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
```

### Test File (tests/2-matrix_divided.txt):

```python
>>> from 2-matrix_divided import matrix_divided
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix_divided([[1, 2], [3, "a"]], 2)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats
```

## 🤖 Task 2: say_my_name(first_name, last_name="")

```python
def say_my_name(first_name, last_name=""):
    """Prints full name using first and last name."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
```

### Test File (tests/3-say_my_name.txt):

```python
>>> from 3-say_my_name import say_my_name
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Bob")
My name is Bob 
>>> say_my_name(3, "Smith")
Traceback (most recent call last):
TypeError: first_name must be a string
```

## #️⃣ Task 3: print_square(size)

```python
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
```

### Test File (tests/4-print_square.txt):

```python
>>> from 4-print_square import print_square
>>> print_square(2)
##
##
>>> print_square(0)

>>> print_square(-1)
Traceback (most recent call last):
ValueError: size must be >= 0
```

## 📄 Task 4: text_indentation(text)

```python
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in ".?:":
        text = text.replace(c, c + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))
```

### Test File (tests/5-text_indentation.txt):

```python
>>> from 5-text_indentation import text_indentation
>>> text_indentation("Hello. How are you? Fine: okay.")
Hello.

How are you?

Fine:

okay.
```

## 🔢 BONUS: unittest Example (Task 5)

```python
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_negative(self):
        self.assertEqual(max_integer([-5, -2, -3]), -2)

if __name__ == '__main__':
    unittest.main()
```

**Run with:**

```bash
python3 -m unittest tests/6-max_integer_test.py
```

## 📈 Final Advice

- **Write test files** in `tests/`
- **Always test before** writing the actual function logic
- **Use `doctest`** for small cases and documentation
- **Use `unittest`** for structured, complex testing
- **The more you test, the more confident you are** ✅





