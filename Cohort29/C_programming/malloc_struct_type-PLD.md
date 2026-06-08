# Memory Allocation Review & Structures with `typedef`

**Instructor:** Raphael

---

# Part 1 — Memory Allocation Review

Before we deeply understand **structures**, we must review **how memory works in C**, because structures frequently interact with **dynamic memory**.

Understanding memory is one of the most important concepts in C programming.

---

# Stack vs Heap Memory

A C program mainly uses two important memory areas:

```
+----------------------+
|        STACK         |
| Local variables      |
| Function calls       |
+----------------------+

+----------------------+
|        HEAP          |
| Dynamic allocation   |
| malloc / calloc      |
+----------------------+
```

---

# Stack Memory (Automatic Memory)

The **stack** is where normal variables live.

Example:

```c
int main(void)
{
    int x = 5;
}
```

When the function runs:

```
STACK
x = 5
```

When the function finishes:

```
STACK
(empty)
```

The variable **automatically disappears**.

### Important Properties of Stack Memory

* Very **fast**
* Managed automatically
* **Limited size**
* Destroyed when the function ends

Example:

```c
void example(void)
{
    int a = 10;
    int b = 20;
}
```

Memory during execution:

```
STACK
a = 10
b = 20
```

After the function ends:

```
STACK
(empty)
```

---

# Heap Memory (Dynamic Memory)

The **heap** is memory that the **programmer controls manually**.

Memory is allocated using:

* `malloc`
* `calloc`
* `realloc`

Example:

```c
int *ptr = malloc(sizeof(int));
```

Memory visualization:

```
STACK

ptr ----->

HEAP
[ int memory ]
```

The memory **remains allocated** until the programmer frees it.

---

# Why Do We Need Heap Memory?

Stack memory disappears when functions end.

Sometimes we need memory that:

* Lives longer
* Changes size
* Stores large data
* Builds dynamic structures

Examples:

* Linked lists
* Dynamic arrays
* File buffers
* Databases

---

# malloc() — Memory Allocation

### Prototype

```c
void *malloc(size_t size);
```

### Purpose

Allocates **size bytes** in memory.

### Important Details

`malloc`:

* Allocates raw memory
* Does **not initialize it**
* Returns pointer to memory
* Returns **NULL if allocation fails**

---

### Example

```c
#include <stdlib.h>

int main(void)
{
    int *ptr;

    ptr = malloc(sizeof(int));

    if (ptr == NULL)
        return (1);

    *ptr = 42;

    free(ptr);

    return (0);
}
```

Memory visualization:

```
STACK

ptr ----->

HEAP
[ 42 ]
```

---

# Common malloc Pattern

Remember this pattern:

```c
type *ptr = malloc(sizeof(type) * number_of_elements);
```

Example:

```c
int *arr = malloc(sizeof(int) * 10);
```

This allocates memory for **10 integers**.

---

# calloc() — Contiguous Allocation

### Prototype

```c
void *calloc(size_t nmemb, size_t size);
```

### Purpose

Allocates memory **and initializes all bytes to zero**.

Example:

```c
int *arr = calloc(10, sizeof(int));
```

Memory comparison:

malloc:

```
[ 2391 ][ -12 ][ ??? ][ ??? ]
```

calloc:

```
[ 0 ][ 0 ][ 0 ][ 0 ]
```

---

# realloc() — Resize Memory

Used when we need to **change the size of allocated memory**.

Example:

```c
int *arr = malloc(5 * sizeof(int));
```

Memory:

```
[1][2][3][4][5]
```

Expanding:

```c
arr = realloc(arr, 10 * sizeof(int));
```

Memory becomes:

```
[1][2][3][4][5][?][?][?][?][?]
```

Old values remain.

New values are **uninitialized**.

---

# Safe realloc Pattern

Incorrect:

```c
arr = realloc(arr, new_size);
```

If realloc fails:

```
arr = NULL
```

Original memory is lost.

Correct pattern:

```c
temp = realloc(arr, new_size);

if (temp == NULL)
{
    free(arr);
    return (1);
}

arr = temp;
```

---

# free() — Releasing Memory

Every `malloc` must eventually have a `free`.

Example:

```c
int *ptr = malloc(sizeof(int));

free(ptr);
```

If you forget:

```
Memory leak occurs
```

---

### Best Practice

```c
free(ptr);
ptr = NULL;
```

This avoids **dangling pointers**.

---

# Detecting Memory Leaks with Valgrind

Command:

```
valgrind --leak-check=full ./program
```

Correct output:

```
All heap blocks were freed -- no leaks are possible
```

---

# Part 2 — Structures

Structures allow us to **group multiple variables together**.

Example: a student record.

Instead of writing:

```c
char *name;
int age;
int id;
float gpa;
```

We group them together.

---

# Structure Definition

```c
struct student
{
    char *name;
    int age;
    int id;
    float gpa;
};
```

This defines a **new data type**, but does not create a variable yet.

---

# Declaring a Structure Variable

```c
struct student s1;
```

Memory representation:

```
s1
+----------------------+
| name | age | id | gpa |
+----------------------+
```

---

# Accessing Structure Members

Use the **dot operator (`.`)**.

Example:

```c
s1.age = 20;
s1.gpa = 3.5;
```

Example program:

```c
#include <stdio.h>

struct point
{
    int x;
    int y;
};

int main(void)
{
    struct point p;

    p.x = 10;
    p.y = 20;

    printf("Point: (%d, %d)\n", p.x, p.y);

    return (0);
}
```

---

# Pointers to Structures

Example:

```c
struct point p;
struct point *ptr;

ptr = &p;
```

Memory:

```
ptr ----> p
```

---

# Arrow Operator

When using structure pointers:

```
ptr->x
```

Equivalent to:

```
(*ptr).x
```

Example:

```c
ptr->x = 10;
ptr->y = 20;
```

---

# Why Use Structure Pointers?

### Efficiency

Passing large structures copies all data.

Pointers avoid copying.

### Modify Data

Functions can modify the original structure.

### Dynamic Structures

Used in:

* Linked lists
* Trees
* Graphs

---

# Dynamic Allocation of Structures

Example:

```c
struct dog *d;

d = malloc(sizeof(struct dog));
```

Memory:

```
STACK
d ---->

HEAP
+------------------+
| name | age | owner |
+------------------+
```

Access members:

```c
d->name = "Rex";
d->age = 4.5;
d->owner = "Alice";
```

---

# Important Memory Rule for Structures

If a structure contains pointers:

```c
struct dog
{
    char *name;
    char *owner;
};
```

You must free them individually:

```c
free(d->name);
free(d->owner);
free(d);
```

---

# typedef — Creating Type Aliases

`typedef` creates a **new name for an existing type**.

Example:

```c
typedef unsigned int uint;
```

Now these are equivalent:

```c
unsigned int x;
uint x;
```

---

# typedef with Structures

Without typedef:

```c
struct dog my_dog;
```

With typedef:

```c
dog_t my_dog;
```

---

# Example

```c
typedef struct dog
{
    char *name;
    float age;
    char *owner;
} dog_t;
```

Now we can write:

```c
dog_t d;
```

instead of:

```c
struct dog d;
```

---

# Arrays of Structures

Example:

```c
dog_t dogs[3] =
{
    {"Buddy", 3.5, "Alice"},
    {"Max", 5.0, "Bob"},
    {"Rex", 2.0, "Charlie"}
};
```

Loop through them:

```c
for (int i = 0; i < 3; i++)
{
    printf("%s\n", dogs[i].name);
}
```

---

# Nested Structures

Structures can contain other structures.

Example:

```c
typedef struct date
{
    int day;
    int month;
    int year;
} date_t;

typedef struct person
{
    char *name;
    int age;
    date_t birthday;
} person_t;
```

Example usage:

```c
person_t john;

john.name = "John Doe";
john.age = 25;
john.birthday.day = 15;
john.birthday.month = 6;
john.birthday.year = 1999;
```

---

# Common Mistakes

### Missing Semicolon

Incorrect:

```c
struct dog
{
    char *name;
}
```

Correct:

```c
struct dog
{
    char *name;
};
```

---

### Confusing `.` and `->`

Incorrect:

```c
my_dog->name
```

Correct:

```
my_dog.name
```

Pointer version:

```
ptr->name
```

---

### Not Checking NULL

Always validate pointers before using them.

---

### Memory Leaks

Always free dynamically allocated memory.

---

# Key Takeaways

Structures:

* Group related data
* Improve program organization
* Used heavily in real programs

typedef:

* Creates type aliases
* Improves readability
* Simplifies structure usage

Memory management:

* Always free allocated memory
* Check `malloc` for NULL
* Use Valgrind to detect leaks

---

# Practice Problems

### Problem 1 — Book Structure

Create a structure containing:

* Title
* Author
* Pages
* Price

Functions:

* Print book
* Initialize book
* Dynamically create book

---

### Problem 2 — Student Grade System

Structure containing:

* Name
* ID
* 5 grades

Functions:

* Calculate average
* Find highest grade
* Print report

---

### Problem 3 — Distance Between Points

Create:

```
struct point
{
    int x;
    int y;
};
```

Function:

```
distance(point1, point2)
```

---

# Summary

Today we reviewed:

Memory allocation:

* `malloc`
* `calloc`
* `realloc`
* `free`

Tools:

* `valgrind`

Core concepts:

* Structures
* Structure pointers
* Dynamic structures
* `typedef`

Remember:

* Structures organize data
* typedef simplifies code
* Always free allocated memory
* Check pointers for NULL
* Use valgrind to detect leaks
