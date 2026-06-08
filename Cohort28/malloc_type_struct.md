# Memory Allocation Review & Structures with typedef

**Instructor:** Raphael  

---

## Part 1: Memory Allocation Review 

### Quick Recap: The Stack vs The Heap

**Stack Memory** (Automatic Allocation):
- Fast, managed automatically
- Limited size
- Variables disappear when function ends
- Example: `int x = 5;`

**Heap Memory** (Dynamic Allocation):
- Slower, managed by programmer
- Much larger
- Persists until explicitly freed
- Example: `int *ptr = malloc(sizeof(int));`

---

### 1. malloc() - Memory Allocation

**Prototype:**
```c
void *malloc(size_t size);
```

**Purpose:** Allocates a block of memory of specified size in bytes.

**Key Points:**
- Returns a pointer to the allocated memory
- Memory is **uninitialized** (contains garbage values)
- Returns `NULL` if allocation fails
- Must cast the return value in practice

**Basic Example:**
```c
#include <stdlib.h>

int main(void)
{
    int *num;
    char *str;
    
    /* Allocate memory for one integer */
    num = malloc(sizeof(int));
    if (num == NULL)
        return (1);  /* Allocation failed */
    
    *num = 42;
    
    /* Allocate memory for 10 characters */
    str = malloc(sizeof(char) * 10);
    if (str == NULL)
    {
        free(num);
        return (1);
    }
    
    /* Use the memory... */
    
    free(num);
    free(str);
    return (0);
}
```

**Common Pattern:**
```c
type *ptr = malloc(sizeof(type) * number_of_elements);
```

---

### 2. calloc() - Contiguous Allocation

**Prototype:**
```c
void *calloc(size_t nmemb, size_t size);
```

**Purpose:** Allocates memory for an array and **initializes all bytes to zero**.

**Difference from malloc:**
- Takes two arguments: number of elements and size of each
- Initializes memory to zero
- Slightly slower due to initialization

**Example:**
```c
int *arr;

/* Allocate array of 10 integers, all initialized to 0 */
arr = calloc(10, sizeof(int));
if (arr == NULL)
    return (1);

/* arr[0] through arr[9] are all 0 */

free(arr);
```

**malloc vs calloc:**
```c
/* These are functionally similar: */
int *arr1 = malloc(10 * sizeof(int));
int *arr2 = calloc(10, sizeof(int));

/* But arr2's elements are all 0, arr1's are garbage */
```

---

### 3. realloc() - Resize Allocation

**Prototype:**
```c
void *realloc(void *ptr, size_t size);
```

**Purpose:** Changes the size of a previously allocated memory block.

**Key Points:**
- Can grow or shrink the allocation
- May move the memory to a new location
- Preserves the contents (up to the minimum of old and new sizes)
- If `ptr` is `NULL`, behaves like `malloc`
- If `size` is 0, behaves like `free`

**Example:**
```c
int *arr;
int *temp;

/* Start with array of 5 integers */
arr = malloc(5 * sizeof(int));
if (arr == NULL)
    return (1);

/* Initialize values */
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;
arr[3] = 4;
arr[4] = 5;

/* Need more space - resize to 10 integers */
temp = realloc(arr, 10 * sizeof(int));
if (temp == NULL)
{
    free(arr);  /* Original memory still valid */
    return (1);
}
arr = temp;

/* arr[0-4] still have their values, arr[5-9] are uninitialized */

free(arr);
```

**Important Safety Pattern:**
```c
/* WRONG - loses reference if realloc fails */
arr = realloc(arr, new_size);

/* RIGHT - preserves original pointer if realloc fails */
temp = realloc(arr, new_size);
if (temp == NULL)
{
    /* Handle error, arr is still valid */
    free(arr);
    return (1);
}
arr = temp;
```

---

### 4. free() - Deallocate Memory

**Prototype:**
```c
void free(void *ptr);
```

**Purpose:** Releases dynamically allocated memory back to the system.

**Critical Rules:**
1. Always free what you malloc
2. Never free the same pointer twice
3. Never use memory after freeing it
4. Set pointer to NULL after freeing (good practice)

**Example:**
```c
int *ptr = malloc(sizeof(int));

/* Use ptr... */

free(ptr);
ptr = NULL;  /* Good practice */
```

---

### 5. exit() - Program Termination

**Prototype:**
```c
void exit(int status);
```

**Purpose:** Terminates the program immediately with a status code.

**Key Points:**
- 0 indicates success
- Non-zero indicates failure (typically 1-255)
- Commonly used: 98 for malloc failures in these projects
- Automatically calls cleanup functions

**Example:**
```c
#include <stdlib.h>

void *malloc_checked(unsigned int b)
{
    void *ptr;
    
    ptr = malloc(b);
    if (ptr == NULL)
        exit(98);  /* Terminate with status 98 */
    
    return (ptr);
}
```

---

### Memory Leak Detection with Valgrind

**Command:**
```bash
valgrind --leak-check=full ./program
```

**What to look for:**
```
HEAP SUMMARY:
    in use at exit: 0 bytes in 0 blocks
All heap blocks were freed -- no leaks are possible
```

**Common Issues:**
- Forgetting to free allocated memory
- Losing pointer to allocated memory
- Freeing only part of allocated structures

---

## Part 2: Structures and typedef 

### Introduction to Structures

**What is a Structure?**

A structure is a user-defined data type that groups related variables of different types under a single name. Think of it as creating your own custom data type.

**Why Use Structures?**
- Organize related data together
- Create logical data models
- Pass multiple related values as a single unit
- Make code more readable and maintainable

**Real-World Analogy:**

Think of a structure like a form:
- A student registration form has: name, age, student ID, GPA
- A book record has: title, author, pages, price
- A point in space has: x, y, z coordinates

---

### Defining a Structure

**Basic Syntax:**
```c
struct structure_name
{
    type member1;
    type member2;
    type member3;
    /* ... more members ... */
};
```

**Example 1: Simple Point**
```c
struct point
{
    int x;
    int y;
};
```

**Example 2: Student Record**
```c
struct student
{
    char *name;
    int age;
    int id;
    float gpa;
};
```

**Example 3: Dog (from project)**
```c
struct dog
{
    char *name;
    float age;
    char *owner;
};
```

**Important Notes:**
- The semicolon after the closing brace is required!
- This just defines the structure type; it doesn't create any variables
- Member names follow normal C identifier rules

---

### Declaring Structure Variables

**Method 1: After Definition**
```c
struct point
{
    int x;
    int y;
};

int main(void)
{
    struct point p1;      /* Declare a variable */
    struct point p2, p3;  /* Declare multiple variables */
    
    return (0);
}
```

**Method 2: With Definition**
```c
struct point
{
    int x;
    int y;
} p1, p2, p3;  /* Declare variables immediately */
```

**Method 3: Anonymous Structure (not recommended)**
```c
struct
{
    int x;
    int y;
} p1;  /* Can only use this type for p1 */
```

---

### Accessing Structure Members

**The Dot Operator (.)**

Use the dot operator to access members of a structure variable.

**Syntax:**
```c
structure_variable.member_name
```

**Example:**
```c
struct point
{
    int x;
    int y;
};

int main(void)
{
    struct point p1;
    
    /* Assign values to members */
    p1.x = 10;
    p1.y = 20;
    
    /* Access and use members */
    printf("Point: (%d, %d)\n", p1.x, p1.y);
    
    /* Use in expressions */
    int sum = p1.x + p1.y;
    
    return (0);
}
```

**Complete Dog Example:**
```c
#include <stdio.h>

struct dog
{
    char *name;
    float age;
    char *owner;
};

int main(void)
{
    struct dog my_dog;
    
    my_dog.name = "Buddy";
    my_dog.age = 3.5;
    my_dog.owner = "Alice";
    
    printf("My dog %s is %.1f years old and belongs to %s\n",
           my_dog.name, my_dog.age, my_dog.owner);
    
    return (0);
}
```

---

### Initializing Structures

**Method 1: Member by Member**
```c
struct point p1;
p1.x = 10;
p1.y = 20;
```

**Method 2: Initialization List (C89)**
```c
struct point p1 = {10, 20};  /* x=10, y=20 */
```

**Method 3: Partial Initialization**
```c
struct point p1 = {10};  /* x=10, y=0 */
struct point p2 = {0};   /* x=0, y=0 (zero everything) */
```

**Example with Different Types:**
```c
struct student
{
    char *name;
    int age;
    float gpa;
};

int main(void)
{
    struct student s1 = {"John", 20, 3.5};
    struct student s2 = {"Jane", 21, 3.8};
    
    return (0);
}
```

---

### Pointers to Structures

**Declaration:**
```c
struct dog *ptr;
```

**The Arrow Operator (->)**

When you have a pointer to a structure, use the arrow operator to access members.

**Syntax:**
```c
pointer->member_name
```

**This is equivalent to:**
```c
(*pointer).member_name
```

**Example:**
```c
struct dog
{
    char *name;
    float age;
    char *owner;
};

int main(void)
{
    struct dog my_dog;
    struct dog *ptr;
    
    ptr = &my_dog;
    
    /* Using arrow operator */
    ptr->name = "Max";
    ptr->age = 5.0;
    ptr->owner = "Bob";
    
    /* Equivalent using dot operator with dereference */
    (*ptr).name = "Max";  /* Same as ptr->name */
    
    return (0);
}
```

**Why Use Pointers to Structures?**
1. Pass structures to functions efficiently (avoid copying)
2. Modify structure in functions
3. Dynamic allocation of structures
4. Create linked data structures (lists, trees, etc.)

---

### Structures and Functions

**Passing Structures to Functions**

**Method 1: Pass by Value (copies entire structure)**
```c
void print_point(struct point p)
{
    printf("(%d, %d)\n", p.x, p.y);
}

int main(void)
{
    struct point p1 = {10, 20};
    print_point(p1);  /* Entire structure is copied */
    return (0);
}
```

**Method 2: Pass by Pointer (efficient, can modify)**
```c
void init_point(struct point *p, int x, int y)
{
    p->x = x;
    p->y = y;
}

int main(void)
{
    struct point p1;
    init_point(&p1, 10, 20);  /* Pass address */
    return (0);
}
```

**Complete Function Example:**
```c
#include <stdio.h>

struct dog
{
    char *name;
    float age;
    char *owner;
};

/* Initialize a dog structure */
void init_dog(struct dog *d, char *name, float age, char *owner)
{
    if (d != NULL)  /* Safety check */
    {
        d->name = name;
        d->age = age;
        d->owner = owner;
    }
}

/* Print a dog structure */
void print_dog(struct dog *d)
{
    if (d == NULL)
        return;
    
    if (d->name == NULL)
        printf("Name: (nil)\n");
    else
        printf("Name: %s\n", d->name);
    
    printf("Age: %f\n", d->age);
    
    if (d->owner == NULL)
        printf("Owner: (nil)\n");
    else
        printf("Owner: %s\n", d->owner);
}

int main(void)
{
    struct dog my_dog;
    
    init_dog(&my_dog, "Buddy", 3.5, "Alice");
    print_dog(&my_dog);
    
    return (0);
}
```

---

### Dynamic Allocation of Structures

**Allocating a Single Structure:**
```c
struct dog *ptr;

ptr = malloc(sizeof(struct dog));
if (ptr == NULL)
    return (1);

/* Use the structure */
ptr->name = "Rex";
ptr->age = 4.0;
ptr->owner = "Charlie";

/* Free when done */
free(ptr);
```

**Complete Example with String Copying:**
```c
#include <stdlib.h>
#include <string.h>

struct dog
{
    char *name;
    float age;
    char *owner;
};

/* Helper function to duplicate a string */
char *_strdup(char *str)
{
    char *dup;
    int i, len;
    
    if (str == NULL)
        return (NULL);
    
    len = 0;
    while (str[len])
        len++;
    
    dup = malloc(sizeof(char) * (len + 1));
    if (dup == NULL)
        return (NULL);
    
    for (i = 0; i <= len; i++)
        dup[i] = str[i];
    
    return (dup);
}

/* Create a new dog with copied strings */
struct dog *new_dog(char *name, float age, char *owner)
{
    struct dog *new;
    
    new = malloc(sizeof(struct dog));
    if (new == NULL)
        return (NULL);
    
    /* Copy name string */
    new->name = _strdup(name);
    if (new->name == NULL)
    {
        free(new);
        return (NULL);
    }
    
    new->age = age;
    
    /* Copy owner string */
    new->owner = _strdup(owner);
    if (new->owner == NULL)
    {
        free(new->name);
        free(new);
        return (NULL);
    }
    
    return (new);
}

/* Free a dog structure */
void free_dog(struct dog *d)
{
    if (d == NULL)
        return;
    
    free(d->name);
    free(d->owner);
    free(d);
}

int main(void)
{
    struct dog *my_dog;
    
    my_dog = new_dog("Buddy", 3.5, "Alice");
    if (my_dog == NULL)
        return (1);
    
    /* Use the dog... */
    
    free_dog(my_dog);
    return (0);
}
```

**Critical Points:**
- Must free all dynamically allocated members before freeing the structure
- Order matters: free members first, then the structure
- Always check for NULL before freeing

---

### The typedef Keyword

**What is typedef?**

`typedef` creates an alias (a new name) for an existing type. It makes code more readable and easier to maintain.

**Basic Syntax:**
```c
typedef existing_type new_name;
```

**Simple Examples:**
```c
/* Create alias for unsigned int */
typedef unsigned int uint;

/* Now these are equivalent: */
unsigned int x;
uint x;

/* Create alias for char pointer */
typedef char *string;

/* Now these are equivalent: */
char *name;
string name;
```

---

### typedef with Structures

**The Problem Without typedef:**
```c
struct dog
{
    char *name;
    float age;
    char *owner;
};

int main(void)
{
    struct dog my_dog;        /* Must use "struct dog" */
    struct dog *ptr;          /* Every time */
    struct dog dogs[10];      /* Gets repetitive */
    
    return (0);
}
```

**Method 1: typedef After Definition**
```c
struct dog
{
    char *name;
    float age;
    char *owner;
};

typedef struct dog dog_t;

int main(void)
{
    dog_t my_dog;      /* Clean and simple! */
    dog_t *ptr;
    dog_t dogs[10];
    
    return (0);
}
```

**Method 2: typedef With Definition (Most Common)**
```c
typedef struct dog
{
    char *name;
    float age;
    char *owner;
} dog_t;

/* Now you can use both:
   struct dog my_dog;  (original name)
   dog_t my_dog;       (typedef name)
*/
```

**Method 3: Anonymous Structure with typedef**
```c
typedef struct
{
    char *name;
    float age;
    char *owner;
} dog_t;

/* Can only use dog_t now, no struct name */
```

**Best Practice for Projects:**
```c
/* In dog.h */
typedef struct dog
{
    char *name;
    float age;
    char *owner;
} dog_t;

/* Provides both options for maximum flexibility */
```

---

### Naming Conventions for typedef

**Common Patterns:**

1. **Append _t suffix:**
   ```c
   typedef struct dog dog_t;
   typedef struct point point_t;
   typedef struct student student_t;
   ```

2. **Capitalize:**
   ```c
   typedef struct dog Dog;
   typedef struct point Point;
   ```

3. **Same name (rely on struct keyword difference):**
   ```c
   typedef struct dog dog;
   /* struct dog or just dog */
   ```

**For this course, use the _t suffix pattern.**

---

### Complete typedef Example

**Header File (dog.h):**
```c
#ifndef DOG_H
#define DOG_H

/* Define the structure with typedef */
typedef struct dog
{
    char *name;
    float age;
    char *owner;
} dog_t;

/* Function prototypes */
void init_dog(struct dog *d, char *name, float age, char *owner);
void print_dog(struct dog *d);
dog_t *new_dog(char *name, float age, char *owner);
void free_dog(dog_t *d);

#endif /* DOG_H */
```

**Implementation File:**
```c
#include <stdlib.h>
#include <stdio.h>
#include "dog.h"

void init_dog(struct dog *d, char *name, float age, char *owner)
{
    if (d != NULL)
    {
        d->name = name;
        d->age = age;
        d->owner = owner;
    }
}

void print_dog(struct dog *d)
{
    if (d == NULL)
        return;
    
    printf("Name: %s\n", d->name ? d->name : "(nil)");
    printf("Age: %f\n", d->age);
    printf("Owner: %s\n", d->owner ? d->owner : "(nil)");
}

/* ... other functions ... */
```

**Main File:**
```c
#include "dog.h"

int main(void)
{
    dog_t my_dog;           /* Using typedef */
    dog_t *ptr;
    struct dog other_dog;   /* Or original name */
    
    init_dog(&my_dog, "Buddy", 3.5, "Alice");
    print_dog(&my_dog);
    
    ptr = new_dog("Max", 5.0, "Bob");
    print_dog(ptr);
    free_dog(ptr);
    
    return (0);
}
```

---

### Arrays of Structures

**Declaration:**
```c
dog_t dogs[5];  /* Array of 5 dogs */
```

**Initialization:**
```c
dog_t dogs[3] = {
    {"Buddy", 3.5, "Alice"},
    {"Max", 5.0, "Bob"},
    {"Rex", 2.0, "Charlie"}
};
```

**Accessing:**
```c
int i;

for (i = 0; i < 3; i++)
{
    printf("Dog %d: %s\n", i, dogs[i].name);
}
```

**Dynamic Array of Structures:**
```c
dog_t *dogs;
int i, n = 5;

dogs = malloc(sizeof(dog_t) * n);
if (dogs == NULL)
    return (1);

/* Initialize each dog */
for (i = 0; i < n; i++)
{
    dogs[i].name = NULL;
    dogs[i].age = 0.0;
    dogs[i].owner = NULL;
}

/* Use the array... */

free(dogs);
```

---

### Nested Structures

Structures can contain other structures as members.

**Example:**
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
    date_t birthday;  /* Nested structure */
} person_t;

int main(void)
{
    person_t john;
    
    john.name = "John Doe";
    john.age = 25;
    john.birthday.day = 15;
    john.birthday.month = 6;
    john.birthday.year = 1999;
    
    printf("%s was born on %d/%d/%d\n",
           john.name,
           john.birthday.day,
           john.birthday.month,
           john.birthday.year);
    
    return (0);
}
```

---

### Common Mistakes and How to Avoid Them

**1. Forgetting the semicolon after structure definition:**
```c
/* WRONG */
struct dog
{
    char *name;
    float age;
}  /* Missing semicolon! */

/* RIGHT */
struct dog
{
    char *name;
    float age;
};  /* Semicolon required */
```

**2. Confusing . and -> operators:**
```c
struct dog my_dog;
struct dog *ptr = &my_dog;

/* WRONG */
my_dog->name = "Buddy";  /* my_dog is not a pointer */
ptr.name = "Buddy";      /* ptr is a pointer */

/* RIGHT */
my_dog.name = "Buddy";   /* Use . for variables */
ptr->name = "Buddy";     /* Use -> for pointers */
```

**3. Not checking for NULL:**
```c
/* WRONG */
void print_dog(struct dog *d)
{
    printf("Name: %s\n", d->name);  /* Crash if d is NULL! */
}

/* RIGHT */
void print_dog(struct dog *d)
{
    if (d == NULL)
        return;
    printf("Name: %s\n", d->name);
}
```

**4. Memory leaks with dynamic structures:**
```c
/* WRONG */
void free_dog(dog_t *d)
{
    free(d);  /* Forgot to free name and owner strings! */
}

/* RIGHT */
void free_dog(dog_t *d)
{
    if (d == NULL)
        return;
    free(d->name);
    free(d->owner);
    free(d);
}
```

**5. Not copying strings:**
```c
/* WRONG */
dog_t *new_dog(char *name, float age, char *owner)
{
    dog_t *d = malloc(sizeof(dog_t));
    d->name = name;  /* Just copying pointer, not string! */
    return (d);
}

/* RIGHT */
dog_t *new_dog(char *name, float age, char *owner)
{
    dog_t *d = malloc(sizeof(dog_t));
    d->name = _strdup(name);  /* Actually copy the string */
    if (d->name == NULL)
    {
        free(d);
        return (NULL);
    }
    return (d);
}
```

---

### Practice Problems

**Problem 1: Create a Book Structure**

Create a structure for a book with title, author, pages, and price. Write functions to:
- Initialize a book
- Print book details
- Create a new book with malloc

**Problem 2: Student Grade System**

Create a structure for a student with name, ID, and an array of 5 grades. Write functions to:
- Calculate average grade
- Print student report
- Find highest grade

**Problem 3: Point Distance**

Create a point structure with x and y coordinates. Write a function to calculate the distance between two points.

**Problem 4: Linked List Node**

Create a structure for a node in a linked list:
```c
typedef struct node
{
    int data;
    struct node *next;
} node_t;
```

Write functions to add a node and print all nodes.

---

### Key Takeaways

**Structures:**
1. Group related data of different types
2. Use `.` for structure variables, `->` for structure pointers
3. Can be passed to functions (by value or pointer)
4. Can be dynamically allocated with malloc
5. Members can be any type, including other structures and pointers

**typedef:**
1. Creates aliases for types
2. Makes code more readable
3. Commonly used with structures
4. Use `_t` suffix for typedef names
5. Can be combined with structure definition

**Memory Management:**
1. Always free dynamically allocated structures
2. Free all dynamically allocated members first
3. Check for NULL before accessing
4. Use valgrind to check for leaks

**Best Practices:**
1. Use typedef for cleaner code
2. Always validate pointer inputs
3. Handle NULL cases explicitly
4. Copy strings when storing in structures
5. Free in reverse order of allocation

---

### Additional Resources

**Man Pages:**
```bash
man 3 malloc
man 3 free
man 3 exit
```

**For More Practice:**
- Implement a student database
- Create a simple address book
- Build a music playlist structure
- Design a game character system

**Next Topics:**
- Function pointers
- Bit manipulation
- File I/O with structures
- Advanced data structures

---

## Summary

Today we reviewed:
- **malloc, calloc, realloc**: Dynamic memory allocation functions
- **free**: Releasing allocated memory
- **exit**: Program termination
- **valgrind**: Memory leak detection

And covered in depth:
- **Structures**: Custom data types grouping related variables
- **typedef**: Creating type aliases for cleaner code
- **Structure pointers**: Efficient structure manipulation
- **Dynamic structures**: Creating structures on the heap
- **Best practices**: Memory management and error handling

**Remember:** 
- Structures organize your data logically
- typedef makes your code more readable
- Always free what you allocate
- Check for NULL everywhere
- Use valgrind to verify no memory leaks

---

**Questions?**