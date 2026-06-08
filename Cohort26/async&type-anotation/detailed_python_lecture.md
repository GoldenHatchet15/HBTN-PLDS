# Python Programming: Async & Type Annotations - Focused Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Asynchronous Programming Basics](#asynchronous-programming-basics)
3. [Async in Practice](#async-in-practice)
4. [Type Annotations](#type-annotations)
5. [Combining Async and Types](#combining-async-and-types)
6. [Best Practices](#best-practices)

---

## Introduction

This guide covers three essential Python concepts:

1. **Async Programming** - Running multiple tasks efficiently
2. **Async Everywhere** - Real-world async applications  
3. **Type Annotations** - Making code clearer and safer

Think of async like a restaurant kitchen where chefs work on multiple dishes simultaneously instead of completing one dish at a time.

---

## Asynchronous Programming Basics

### What is Async?

Async lets your program do multiple things at once without waiting. Instead of:
- Task 1 (5 seconds) → Task 2 (3 seconds) → Task 3 (2 seconds) = 10 seconds total

You get:
- Task 1, 2, and 3 all running together = 5 seconds total (longest task)

### 1. Basic Coroutines

```python
import asyncio

async def fetch_data():
    """A simple async function (coroutine)"""
    print("Starting to fetch data...")
    await asyncio.sleep(2)  # Pretend this is a network request
    print("Data received!")
    return "Sample data"

async def main():
    """Main function that runs our async code"""
    result = await fetch_data()
    print(f"Got: {result}")

# To run: asyncio.run(main())
```

**Key Points:**
- `async def` creates an async function
- `await` pauses the function until something finishes
- Must use `asyncio.run()` to start async code

### 2. Async Generators

```python
async def count_slowly(start: int, end: int):
    """Generate numbers with delays between them"""
    print(f"Counting from {start} to {end}")
    
    for i in range(start, end + 1):
        await asyncio.sleep(0.5)  # Wait half a second
        yield i  # Give back the number

async def use_async_generator():
    """Use the async generator"""
    async for number in count_slowly(1, 5):
        print(f"Got number: {number}")

# asyncio.run(use_async_generator())
```

**Key Points:**
- `async def` + `yield` = async generator
- Use `async for` to get values from async generators
- Can do async work between each `yield`

### 3. Async Comprehensions

```python
async def get_square(x: int):
    """Calculate square with a small delay"""
    await asyncio.sleep(0.1)
    return x * x

async def demo_comprehensions():
    numbers = [1, 2, 3, 4, 5]
    
    # Async list comprehension
    squares = [await get_square(n) for n in numbers]
    print(f"Squares: {squares}")
    
    # Async generator expression  
    square_gen = (await get_square(n) for n in numbers)
    async for square in square_gen:
        print(f"Square: {square}")

# asyncio.run(demo_comprehensions())
```

**Key Points:**
- Add `await` inside comprehensions for async operations
- Works with lists, sets, dictionaries, and generators

### 4. Type-Annotated Generators

```python
from typing import Generator, AsyncGenerator

def simple_generator() -> Generator[int, None, str]:
    """
    Generator[YieldType, SendType, ReturnType]
    - Yields: int numbers
    - Sends: None (doesn't accept input)
    - Returns: str when done
    """
    for i in range(3):
        yield i
    return "Done!"

async def simple_async_generator() -> AsyncGenerator[str, None]:
    """
    AsyncGenerator[YieldType, SendType]  
    - Yields: str values
    - Sends: None (doesn't accept input)
    """
    for i in range(3):
        await asyncio.sleep(0.1)
        yield f"Item {i}"
```

**Key Points:**
- `Generator[YieldType, SendType, ReturnType]` for regular generators
- `AsyncGenerator[YieldType, SendType]` for async generators
- Type annotations help tools understand what your generator produces

---

## Async in Practice

### Running Multiple Tasks

```python
async def download_file(filename: str, delay: float):
    """Simulate downloading a file"""
    print(f"📥 Starting download: {filename}")
    await asyncio.sleep(delay)  # Simulate download time
    print(f"✅ Finished download: {filename}")
    return f"Content of {filename}"

async def download_multiple_files():
    """Download several files at the same time"""
    # This runs all downloads concurrently
    results = await asyncio.gather(
        download_file("photo.jpg", 2.0),
        download_file("document.pdf", 1.5), 
        download_file("video.mp4", 3.0)
    )
    
    print(f"Downloaded {len(results)} files")
    return results

# asyncio.run(download_multiple_files())
```

### Creating and Managing Tasks

```python
async def background_worker(worker_id: int):
    """A worker that does background processing"""
    for step in range(3):
        print(f"Worker {worker_id}: Step {step + 1}")
        await asyncio.sleep(1)
    return f"Worker {worker_id} finished"

async def task_example():
    """Show how to create and manage tasks"""
    # Create tasks (they start running immediately)
    task1 = asyncio.create_task(background_worker(1))
    task2 = asyncio.create_task(background_worker(2))
    
    # Wait for first task to finish
    result1 = await task1
    print(f"First result: {result1}")
    
    # Cancel second task if we don't need it
    if not task2.done():
        task2.cancel()
        try:
            await task2
        except asyncio.CancelledError:
            print("Task 2 was cancelled")

# asyncio.run(task_example())
```

### Using Random with Async

```python
import random

async def random_task(name: str):
    """Task with random delay and outcome"""
    delay = random.uniform(0.5, 2.0)  # Random delay 0.5-2 seconds
    print(f"{name} will take {delay:.1f} seconds")
    
    await asyncio.sleep(delay)
    
    # 80% success rate
    if random.random() < 0.8:
        result = random.randint(100, 999)
        print(f"✅ {name} succeeded: {result}")
        return result
    else:
        print(f"❌ {name} failed")
        raise Exception(f"{name} failed randomly")

async def random_simulation():
    """Run multiple tasks with random outcomes"""
    tasks = [
        asyncio.create_task(random_task(f"Task-{i}"))
        for i in range(5)
    ]
    
    # Collect results, including failures
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Count successes and failures
    successes = [r for r in results if isinstance(r, int)]
    failures = [r for r in results if isinstance(r, Exception)]
    
    print(f"✅ Successes: {len(successes)}")
    print(f"❌ Failures: {len(failures)}")

# asyncio.run(random_simulation())
```

---

## Type Annotations

### Basic Types

```python
# Simple variable types
name: str = "Alice"
age: int = 25
height: float = 5.6
is_student: bool = True

def greet(person: str, age: int) -> str:
    """Function with type hints"""
    return f"Hello {person}, you are {age} years old"

# Call the function
message = greet("Bob", 30)
print(message)
```

### Collection Types

```python
from typing import List, Dict, Optional

def process_scores(scores: List[float]) -> Dict[str, float]:
    """Process a list of scores and return stats"""
    if not scores:
        return {"average": 0.0, "max": 0.0, "min": 0.0}
    
    return {
        "average": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores)
    }

# Example usage
test_scores = [85.5, 92.0, 78.5, 95.0]
stats = process_scores(test_scores)
print(f"Stats: {stats}")

def find_user(user_id: int) -> Optional[str]:
    """Find username by ID, return None if not found"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)  # Returns str or None

# Handle optional return value
username = find_user(1)
if username:
    print(f"Found user: {username}")
else:
    print("User not found")
```

### Union Types

```python
from typing import Union

def format_id(user_id: Union[int, str]) -> str:
    """Accept either integer ID or string username"""
    if isinstance(user_id, int):
        return f"User #{user_id}"
    else:
        return f"User @{user_id}"

# Works with both types
print(format_id(123))        # "User #123"
print(format_id("alice"))    # "User @alice"
```

### Protocols (Duck Typing)

```python
from typing import Protocol

class Drawable(Protocol):
    """Anything that can be drawn"""
    def draw(self) -> None:
        ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> None:
        print(f"Drawing circle with radius {self.radius}")

class Square:
    def __init__(self, size: float):
        self.size = size
    
    def draw(self) -> None:
        print(f"Drawing square with size {self.size}")

def render(shape: Drawable) -> None:
    """Render any drawable shape"""
    shape.draw()

# Both work because they have draw() method
circle = Circle(5.0)
square = Square(3.0)

render(circle)  # Works!
render(square)  # Works!
```

### Using mypy for Type Checking

```python
def calculate_tax(price: float, rate: float) -> float:
    """Calculate tax on a price"""
    return price * rate

# These would be caught by mypy:
# calculate_tax("100", 0.08)    # Error: "100" is str, not float
# calculate_tax(100, "8%")      # Error: "8%" is str, not float

# This is correct:
tax = calculate_tax(100.0, 0.08)  # ✅ Both are floats
```

**To use mypy:**
1. Install: `pip install mypy`
2. Run: `mypy your_file.py`
3. Fix any type errors it finds

---

## Combining Async and Types

### Async Functions with Types

```python
import asyncio
from typing import List, Optional

async def fetch_data(url: str) -> Optional[str]:
    """Fetch data from URL, return None if failed"""
    try:
        print(f"Fetching {url}...")
        await asyncio.sleep(1)  # Simulate network request
        return f"Data from {url}"
    except Exception:
        return None

async def fetch_all(urls: List[str]) -> List[Optional[str]]:
    """Fetch data from multiple URLs concurrently"""
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    urls = ["site1.com", "site2.com", "site3.com"]
    results = await fetch_all(urls)
    
    for url, data in zip(urls, results):
        if data:
            print(f"✅ {url}: Got data")
        else:
            print(f"❌ {url}: Failed")

# asyncio.run(main())
```

### Async Context Managers with Types

```python
from typing import Optional
from types import TracebackType

class AsyncFileProcessor:
    """Process files asynchronously with proper cleanup"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.is_open: bool = False
    
    async def __aenter__(self) -> 'AsyncFileProcessor':
        """Enter async context"""
        print(f"Opening {self.filename}")
        await asyncio.sleep(0.1)  # Simulate file opening
        self.is_open = True
        return self
    
    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException], 
        exc_tb: Optional[TracebackType]
    ) -> None:
        """Exit async context"""
        print(f"Closing {self.filename}")
        await asyncio.sleep(0.1)  # Simulate file closing
        self.is_open = False
    
    async def process(self) -> str:
        """Process the file"""
        if not self.is_open:
            raise RuntimeError("File not open")
        
        await asyncio.sleep(0.5)  # Simulate processing
        return f"Processed {self.filename}"

async def use_async_context():
    """Demonstrate async context manager"""
    async with AsyncFileProcessor("data.txt") as processor:
        result = await processor.process()
        print(result)
    # File automatically closed here

# asyncio.run(use_async_context())
```

---

## Best Practices

### Do's and Don'ts

#### Async Best Practices

```python
# ✅ DO: Always await coroutines
async def good_example():
    result = await fetch_data("example.com")
    return result

# ❌ DON'T: Forget to await
async def bad_example():
    result = fetch_data("example.com")  # This just creates a coroutine!
    return result

# ✅ DO: Use gather for concurrent execution
async def concurrent_downloads():
    results = await asyncio.gather(
        fetch_data("site1.com"),
        fetch_data("site2.com"),
        fetch_data("site3.com")
    )
    return results

# ❌ DON'T: Run sequentially when you could run concurrently
async def sequential_downloads():
    results = []
    results.append(await fetch_data("site1.com"))  # Slow!
    results.append(await fetch_data("site2.com"))  # Slow!
    results.append(await fetch_data("site3.com"))  # Slow!
    return results
```

#### Type Annotation Best Practices

```python
# ✅ DO: Start simple
def add(a: int, b: int) -> int:
    return a + b

# ✅ DO: Use meaningful names
user_scores: Dict[str, float] = {"alice": 95.0, "bob": 87.5}

# ❌ DON'T: Over-complicate
def complex_function(
    data: Dict[str, List[Union[int, float, str, None]]]
) -> Optional[Tuple[Union[int, float], ...]]:
    pass  # Too complex!

# ✅ DO: Use type aliases for complex types
UserData = Dict[str, Union[str, int, float]]

def process_user(data: UserData) -> str:
    return f"Processing {data['name']}"
```

### Common Mistakes

```python
# Mistake 1: Mixing sync and async incorrectly
def bad_sync_function():
    # ❌ Can't await in regular function
    # result = await async_function()  # SyntaxError!
    pass

# Mistake 2: Not handling Optional types
def risky_function(data: Optional[str]) -> int:
    # ❌ What if data is None?
    # return len(data)  # Could crash!
    
    # ✅ Always check for None
    if data is not None:
        return len(data)
    return 0

# Mistake 3: Creating tasks but not awaiting them
async def leaked_task():
    # ❌ Task starts but we never wait for it
    asyncio.create_task(background_worker(1))
    # Task might not finish before program ends!

async def proper_task_handling():
    # ✅ Create and await the task
    task = asyncio.create_task(background_worker(1))
    result = await task
    return result
```

---

## Conclusion

### Key Takeaways

**Async Programming:**
- Use `async def` and `await` for concurrent operations
- `asyncio.gather()` runs multiple tasks at once
- Great for I/O operations (network, files, databases)

**Type Annotations:**
- Make code clearer and catch errors early
- Start with basic types, add complexity gradually
- Use mypy to check your types

**Integration:**
- Async functions can have type annotations
- Use `Optional` for functions that might fail
- Type annotations work great with async context managers

### Next Steps

1. Practice writing simple async functions
2. Add type hints to your existing code
3. Try mypy on your projects
4. Build a small async web scraper or API client
5. Explore more advanced async patterns

Remember: Start simple and build complexity gradually. Both async programming and type annotations make your code better, but they take practice to master!