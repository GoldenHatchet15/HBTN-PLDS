# PLD: Python Input/Output and Serialization

## Goal of This PLD

By the end of this session, students will understand how Python reads and writes files, how to safely manage files using `with`, what JSON is and why it matters, what serialization and deserialization mean, and how to pass command-line arguments to Python scripts.

---

# Part 1: Python Input/Output

## 1. What does Input/Output mean?

Input/Output is usually abbreviated as **I/O**.

Think of a program as a person sitting at a desk:

- **Input** is anything handed *to* them — a note, a file, something typed.
- **Output** is anything they hand *back* — a printed result, a saved file, a response.

In Python:

```python
name = input("What is your name? ")   # Input: user types something
print(name)                           # Output: program responds
```

But the keyboard and screen are just two examples. **Files are also a form of I/O.**

- Reading from a file → input
- Writing to a file → output

---

## 2. Why do we use files?

Variables only exist while the program is running. The moment the program stops, they disappear.

```python
name = "Raphael"
# When this program ends, "Raphael" is gone forever.
```

Think of it like RAM vs a hard drive. Variables live in RAM — fast, but temporary. Files live on disk — slower, but permanent.

Files let programs:

- Save data between runs (game saves, user settings)
- Share data with other programs (logs, exports)
- Read data that was created elsewhere (config files, datasets)

---

## 3. Opening a file

To work with a file, Python needs to open it first:

```python
open(filename, mode)
```

The `mode` tells Python *what you intend to do* with the file.

| Mode | Meaning | File must exist? |
|------|---------|-----------------|
| `"r"` | Read | Yes |
| `"w"` | Write (overwrites existing content) | No — creates if missing |
| `"a"` | Append (adds to end) | No — creates if missing |
| `"x"` | Create (fails if file already exists) | No |

> **Analogy:** Mode is like telling a librarian what you need. "I want to *read* that book" vs "I need to *write in* a notebook" vs "I want to *add notes* at the back."

---

## 4. Reading an entire file

Given `hello.txt`:

```text
Hello students!
Welcome to Python files.
```

```python
#!/usr/bin/python3
"""Read the full content of a file."""

with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

`file.read()` loads the entire file into a single string.

This is fine for small files. For large files (gigabytes of logs, for example), loading everything at once can crash your program by exhausting memory.

---

## 5. Reading a file line by line

```python
#!/usr/bin/python3
"""Read a file one line at a time."""

with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

> **Analogy:** Reading the whole file at once is like photocopying an entire book and carrying the stack. Reading line by line is like reading one page, putting it down, then picking up the next. The book never fully leaves the shelf — you just visit it piece by piece.

This is memory-efficient because Python only holds one line at a time.

---

## 6. Writing to a file

```python
#!/usr/bin/python3
"""Write text to a file."""

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python!\n")
```

**Warning:** Write mode (`"w"`) is destructive. If the file already exists, all previous content is erased before writing begins.

> **Analogy:** `"w"` is like grabbing a whiteboard eraser before you start writing. The old content is gone the moment you open the file.

---

## 7. Appending to a file

```python
#!/usr/bin/python3
"""Add new content to the end of an existing file."""

with open("output.txt", "a", encoding="utf-8") as file:
    file.write("This line was added later.\n")
```

> **Analogy:** `"a"` is like adding a sticky note to the bottom of a page instead of rewriting the whole thing.

Use append mode when you want to preserve existing content — log files are a classic example.

---

## 8. Why not just `open()` and `close()`?

You *can* do this:

```python
file = open("hello.txt", "r")
content = file.read()
file.close()
```

But it's fragile. If an error occurs on the `file.read()` line, the program crashes before reaching `file.close()`. The file stays open in the operating system until your program exits (or possibly longer).

An open file that never gets closed:
- Locks other programs from accessing it
- Wastes operating system resources
- Can corrupt data in some cases

That is why we use `with`.

---

## 9. The `with` statement

```python
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
# File is guaranteed closed here, even if an error occurred above.
```

The `with` statement uses Python's **context manager** protocol. It guarantees that `file.close()` is called no matter what happens — error or not.

> **Analogy:** `with` is like a library checkout system. The moment you walk out of the "checkout zone" — whether normally or because an alarm went off — the book is automatically returned. You don't have to remember to do it yourself.

**Always use `with` when working with files.** It is safer, cleaner, and the accepted standard in Python.

---

## 10. The file cursor

When you open a file, Python places an invisible marker called a **cursor** (or pointer) at the beginning. As you read, the cursor moves forward through the file.

```python
#!/usr/bin/python3
"""Demonstrate the file cursor."""

with open("hello.txt", "r", encoding="utf-8") as file:
    print(file.read(5))    # Read first 5 characters
    print(file.tell())     # Tell us where the cursor is now
```

> **Analogy:** The file cursor is like your finger on a page when reading. Once you've read past a word, your finger is already past it. To re-read it, you have to move your finger back.

`file.seek(0)` moves the cursor back to position zero — the beginning of the file.

```python
#!/usr/bin/python3
"""Reset the cursor and read again."""

with open("hello.txt", "r", encoding="utf-8") as file:
    print(file.read(5))   # Read first 5 chars
    file.seek(0)           # Reset to beginning
    print(file.read())     # Read the whole file again
```

---

# Part 2: Command-Line Arguments

## 11. What are command-line arguments?

When you run a script from the terminal, you can pass it values directly:

```bash
python3 greet.py Raphael 25
```

`Raphael` and `25` are **command-line arguments** — input given to the program at launch, before it even starts running.

Python stores them in `sys.argv`, which is a list:

```python
#!/usr/bin/python3
"""Print all command-line arguments."""

import sys

print(sys.argv)
```

Running `python3 script.py hello world` gives:

```python
['script.py', 'hello', 'world']
```

> **Key point:** `sys.argv[0]` is always the script's own name. Your actual arguments start at `sys.argv[1]`.

> **Analogy:** Think of command-line arguments like a food order. When you call a restaurant (`python3 script.py`), you don't just say "give me food" — you say "give me *a burger and a coffee*" (`Raphael 25`). The program receives your specific request the moment it picks up the phone.

### Checking arguments safely

Always verify that the expected arguments were actually passed:

```python
#!/usr/bin/python3
"""Greet a user by name using a command-line argument."""

import sys


if len(sys.argv) < 2:
    print("Usage: ./greet.py <name>")
else:
    print(f"Hello, {sys.argv[1]}!")
```

Without this check, trying to access `sys.argv[1]` when no argument was given raises an `IndexError`.

---

# Part 3: JSON

## 12. What is JSON?

JSON stands for **JavaScript Object Notation**. Despite the name, JSON is language-independent — virtually every programming language works with it. It is the most common format for exchanging data over the internet.

JSON is plain text that follows a strict structure:

```json
{
  "name": "Raphael",
  "age": 25,
  "is_student": true
}
```

It looks very similar to a Python dictionary — but there are important differences:

| Python | JSON |
|--------|------|
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |
| Single or double quotes | Double quotes **only** |

> **Analogy:** JSON is like a universal packing label. It doesn't matter if the sender is Python, JavaScript, or Ruby — as long as the label is in JSON format, the receiver can read it. It's a shared language for data, not tied to any one programming language.

---

# Part 4: Serialization and Deserialization

## 13. What is serialization?

A Python object — a dictionary, a list, a custom class — lives in memory. It can't be directly saved to a file or sent over the network. To do either, it must be converted into a storable format, usually text or bytes.

**Serialization** is that conversion process.

Python dictionary (in memory):
```python
student = {"name": "Ana", "age": 22}
```

JSON string (can be saved or transmitted):
```json
{"name": "Ana", "age": 22}
```

> **Analogy:** Imagine you have a sandcastle on the beach. You can't mail a sandcastle — it'll fall apart in transit. But you can photograph it (serialize it), mail the photo, and the other person can use it to rebuild the castle (deserialize). The photo is the serialized form; it captures all the important information in a transmittable format.

---

## 14. What is deserialization?

**Deserialization** is the reverse: converting stored data back into a live Python object.

JSON string (from a file or network):
```json
{"name": "Ana", "age": 22}
```

Python dictionary (back in memory, ready to use):
```python
{"name": "Ana", "age": 22}
```

> **Analogy:** Continuing the sandcastle photo: when the recipient receives the photo and rebuilds the castle using it, that's deserialization. The castle is alive again — you can add towers to it, change the moat, tear it down. The photo was just the transport.

---

## 15. Serializing with `json.dumps()`

```python
#!/usr/bin/python3
"""Convert a Python object to a JSON string."""

import json


student = {
    "name": "Ana",
    "age": 22,
    "courses": ["Python", "C", "SQL"]
}

json_string = json.dumps(student)

print(json_string)
print(type(json_string))   # <class 'str'>
```

`json.dumps()` — "dump to **s**tring". The result is a plain Python string containing valid JSON text.

---

## 16. Deserializing with `json.loads()`

```python
#!/usr/bin/python3
"""Convert a JSON string to a Python object."""

import json


json_string = '{"name": "Ana", "age": 22}'

student = json.loads(json_string)

print(student)
print(type(student))      # <class 'dict'>
print(student["name"])    # Ana
```

`json.loads()` — "load from **s**tring". It parses the JSON text and returns a Python dictionary (or list, depending on the JSON structure).

---

## 17. Saving to a JSON file with `json.dump()`

```python
#!/usr/bin/python3
"""Save a Python object to a JSON file."""

import json


student = {
    "name": "Ana",
    "age": 22
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file)
```

`json.dump()` — no `s` at the end — writes JSON directly into a file object instead of returning a string.

### The four functions, compared

| Function | Direction | Works with |
|----------|-----------|-----------|
| `json.dumps()` | Python → JSON string | String in memory |
| `json.loads()` | JSON string → Python | String in memory |
| `json.dump()` | Python → JSON file | File on disk |
| `json.load()` | JSON file → Python | File on disk |

> **Memory trick:** The `s` stands for "string." If there's an `s`, you're working with a string. No `s` means you're working with a file.

---

## 18. Reading from a JSON file with `json.load()`

```python
#!/usr/bin/python3
"""Read JSON data from a file."""

import json


with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)
print(student["name"])
```

---

# Part 5: Marshaling vs Serialization

## 19. The difference between serialization and marshaling

These terms are often confused. Both involve transforming data to move it somewhere — but the emphasis differs.

**Serialization** focuses on saving the *state* of an object so it can be recreated later. The primary concern is persistence or transmission.

**Marshaling** focuses on preparing data so a *different system, process, or environment* can receive and understand it. The primary concern is interoperability — making sure the receiver can work with it.

```text
Serialization = "I want to save this and bring it back later."
Marshaling    = "I want to send this somewhere else so they can use it."
```

In practice, the two concepts overlap heavily, and in beginner Python work you will mostly hear "serialization." Marshaling tends to appear in lower-level systems programming and distributed computing contexts.

---

# Part 6: Pickle

## 20. What is pickle?

`pickle` is Python's built-in module for serializing Python objects into **binary format** rather than text.

```python
#!/usr/bin/python3
"""Serialize data to a binary file using pickle."""

import pickle


data = {"name": "Ana", "score": 95}

with open("data.pkl", "wb") as file:   # "wb" = write binary
    pickle.dump(data, file)
```

Reading it back:

```python
#!/usr/bin/python3
"""Deserialize a pickle file."""

import pickle


with open("data.pkl", "rb") as file:   # "rb" = read binary
    data = pickle.load(file)

print(data)
```

### When to use pickle vs JSON

| | JSON | Pickle |
|---|------|--------|
| Format | Text | Binary |
| Human-readable | Yes | No |
| Works across languages | Yes | Python only |
| Can serialize most Python types | Partial | Yes (almost everything) |
| Safe to load from untrusted sources | Yes | **No** |

> **Critical warning:** Never unpickle data from a source you don't control. Pickle can execute arbitrary code during loading — it's a known security vulnerability. For any web-facing or shared use case, use JSON.

---

# Part 7: Common Serialization Formats

## 21. Choosing the right format

Different problems call for different formats. Here's a practical overview:

### JSON
Best for: APIs, web apps, config files, data exchange between programs.

Pros: Human-readable, easy to use, universal support.

```json
{"name": "Ana", "age": 22}
```

### CSV
Best for: Tables, spreadsheet exports, datasets.

Pros: Extremely simple, opens in Excel/Sheets, widely supported.

```csv
name,age
Ana,22
Luis,30
```

### XML
Best for: Older APIs, enterprise systems, document formats like HTML.

More verbose than JSON, but allows more expressive structure.

```xml
<student>
    <name>Ana</name>
    <age>22</age>
</student>
```

### Binary formats (Pickle, Protocol Buffers, MessagePack)
Best for: Speed-critical applications, large datasets, Python-to-Python communication.

Not human-readable, not cross-language (in the case of pickle), but fast and compact.

**Rule of thumb for most beginner and intermediate projects: use JSON.**

---

# Part 8: Exercises

## Exercise 1: Write to a file

Create `0-write_file.py` that writes the following text to `message.txt`:

```text
Python is awesome!
```

```python
#!/usr/bin/python3
"""Write text to a file."""


with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Python is awesome!\n")
```

```bash
chmod +x 0-write_file.py
./0-write_file.py
cat message.txt
```

---

## Exercise 2: Read a file

Create `1-read_file.py` that reads and prints `message.txt`.

```python
#!/usr/bin/python3
"""Read and print a file."""


with open("message.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")
```

---

## Exercise 3: Read line by line

Create `names.txt`:

```text
Ana
Luis
Maria
Carlos
```

Create `2-read_lines.py`:

```python
#!/usr/bin/python3
"""Read a file one line at a time."""


with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Student: {line}", end="")
```

---

## Exercise 4: Serialize a dictionary to a JSON string

```python
#!/usr/bin/python3
"""Convert a Python dictionary to a JSON string."""

import json


student = {
    "name": "Ana",
    "age": 22,
    "active": True
}

json_text = json.dumps(student)
print(json_text)
print(type(json_text))
```

**Challenge:** What happens to `True` in the output? Why?

---

## Exercise 5: Save a dictionary to a JSON file

```python
#!/usr/bin/python3
"""Save a dictionary to a JSON file."""

import json


student = {
    "name": "Ana",
    "age": 22,
    "active": True
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file)
```

After running it, open `student.json` in a text editor and read what it looks like.

---

## Exercise 6: Load data from a JSON file

```python
#!/usr/bin/python3
"""Load JSON data from a file and use it."""

import json


with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)
print(student["name"])
```

---

## Exercise 7: Command-line file reader

Create `read_cli.py` that accepts a filename as a command-line argument and prints it:

```python
#!/usr/bin/python3
"""Read a file whose name is passed as a command-line argument."""

import sys


if len(sys.argv) != 2:
    print("Usage: ./read_cli.py <filename>")
else:
    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
```

```bash
chmod +x read_cli.py
./read_cli.py message.txt
./read_cli.py names.txt
```

**Challenge:** What happens if you pass a filename that doesn't exist? How would you handle that error?

---

# Part 9: Project Requirements Reminder

Every Python file must:

- Start with `#!/usr/bin/python3`
- End with a new line
- Be executable (`chmod +x filename.py`)
- Follow pycodestyle (`pycodestyle filename.py`)
- Have a module-level docstring

Run doctests with:

```bash
python3 -m doctest ./tests/*
```

---

# Part 10: Summary

## The big picture

| Concept | What it does | Key functions |
|---------|-------------|---------------|
| File I/O | Read/write persistent data | `open()`, `read()`, `write()`, `with` |
| JSON | Human-readable data exchange format | `dumps`, `loads`, `dump`, `load` |
| Serialization | Python object → storable format | `json.dumps()`, `json.dump()`, `pickle.dump()` |
| Deserialization | Stored format → Python object | `json.loads()`, `json.load()`, `pickle.load()` |
| Command-line args | Pass values to scripts at launch | `sys.argv` |

## The final analogy — moving apartments

Imagine you need to move everything from your apartment into a new one.

**Your Python objects** are the furniture — your couch, your desk, your shelves. They live comfortably in your current apartment (memory), but they can't just teleport.

**Serialization** is packing everything into boxes. Your couch becomes "1 couch, brown, 3 cushions" written on a label. The item still exists — it's just been converted into something that can travel.

**The moving truck** is the file or network — it carries the boxes from one place to another.

**Deserialization** is unpacking at the new apartment. You read the label, find the couch, and put it back together where it belongs.

The furniture didn't change. It just traveled in a form that could survive the journey.