# Introduction to Pointers, Arrays, Strings, and Recursion in C

## Welcome!

Hello students! Today we're going to explore some fundamental concepts in C programming that will significantly expand what you can do with code. Don't worry if these topics sound intimidating—we'll break everything down step by step, starting from the basics.

---

## Part 1: Understanding Pointers to Pointers (Double Pointers)

### What is a Pointer? (Quick Review)

Before we talk about pointers to pointers, let's make sure we understand regular pointers:

```c
int number = 42;
int *ptr = &number;
```

- `number` is a variable that holds the value 42
- `ptr` is a pointer that holds the **address** (location in memory) of `number`
- Think of it like this: `number` is a house, and `ptr` is the house's address written on a piece of paper

### So What's a Pointer to a Pointer?

A **pointer to a pointer** (also called a double pointer) is simply a pointer that stores the address of another pointer!

```c
int number = 42;
int *ptr = &number;        // ptr points to number
int **ptr_to_ptr = &ptr;   // ptr_to_ptr points to ptr
```

**Visual representation:**
```
number        ptr           ptr_to_ptr
[  42  ]  <-- [0x100]  <--  [0x200]
(value)       (address      (address
               of number)    of ptr)
```

### Why Would We Need This?

Double pointers are useful when:
1. **Modifying pointers inside functions**: If you want a function to change where a pointer points, you need to pass a pointer to that pointer
2. **Working with 2D arrays**: We'll see this soon!
3. **Dynamic arrays of strings**: Each string is a pointer, so an array of strings is a pointer to pointers

### Practical Example

```c
void make_pointer_point_elsewhere(int **pp) {
    static int new_value = 100;
    *pp = &new_value;  // Change where the original pointer points
}

int main(void) {
    int original = 42;
    int *ptr = &original;
    
    printf("Before: %d\n", *ptr);  // Prints 42
    
    make_pointer_point_elsewhere(&ptr);  // Pass address of ptr
    
    printf("After: %d\n", *ptr);   // Prints 100
    
    return 0;
}
```

---

## Part 2: Multidimensional Arrays (2D Arrays)

### What is a Multidimensional Array?

Think of a regular array as a **row** of boxes:
```
[0] [1] [2] [3] [4]
```

A **2D array** is like a **grid** or **table** with rows and columns:
```
     [0] [1] [2] [3]
[0]   5   3   8   1
[1]   2   7   4   9
[2]   6   0   3   5
```

### Declaring a 2D Array

```c
int grid[3][4];  // 3 rows, 4 columns
```

This creates a grid with 3 rows and 4 columns (12 total elements).

### Initializing a 2D Array

```c
int grid[3][4] = {
    {5, 3, 8, 1},   // Row 0
    {2, 7, 4, 9},   // Row 1
    {6, 0, 3, 5}    // Row 2
};
```

### Accessing Elements

```c
int value = grid[1][2];  // Gets the element at row 1, column 2
                         // This would be 4
```

**Think of it like coordinates:**
- First bracket `[1]` = which row
- Second bracket `[2]` = which column

### Looping Through a 2D Array

```c
int grid[3][4] = {
    {5, 3, 8, 1},
    {2, 7, 4, 9},
    {6, 0, 3, 5}
};

// Print all elements
for (int row = 0; row < 3; row++) {
    for (int col = 0; col < 4; col++) {
        printf("%d ", grid[row][col]);
    }
    printf("\n");  // New line after each row
}
```

### 2D Arrays and Pointers

Here's something important: A 2D array is actually an **array of arrays**.

```c
int grid[3][4];
```

- `grid` is an array of 3 elements
- Each element is itself an array of 4 integers
- `grid[0]` is a pointer to the first row
- `grid[1]` is a pointer to the second row

This is why when you pass a 2D array to a function, you write:
```c
void print_chessboard(char (*board)[8]) {
    // board is a pointer to an array of 8 characters
}
```

The syntax `(*board)[8]` means: "pointer to an array of 8 elements"

---

## Part 3: String Manipulation Functions

### What is a String in C?

In C, a **string** is simply an array of characters that ends with a special character called the **null terminator** (`\0`).

```c
char name[] = "Alice";
```

In memory, this looks like:
```
['A']['l']['i']['c']['e']['\0']
  0    1    2    3    4    5
```

The `\0` tells C "this is where the string ends."

### Common String Operations

Let's look at the functions you'll need to implement:

#### 1. `_memset` - Fill Memory with a Value

**Purpose**: Set all bytes in a memory area to a specific value

```c
char *_memset(char *s, char b, unsigned int n);
```

**Example**:
```c
char buffer[10];
_memset(buffer, 'X', 5);  // First 5 bytes become 'X'
// buffer now: "XXXXX?????" (question marks = uninitialized)
```

**How it works**:
```c
char *_memset(char *s, char b, unsigned int n) {
    unsigned int i;
    
    for (i = 0; i < n; i++) {
        s[i] = b;  // Set each byte to b
    }
    return s;  // Return the pointer to the beginning
}
```

#### 2. `_memcpy` - Copy Memory

**Purpose**: Copy bytes from one memory location to another

```c
char *_memcpy(char *dest, char *src, unsigned int n);
```

**Example**:
```c
char source[] = "Hello";
char destination[10];
_memcpy(destination, source, 5);
// destination now contains "Hello"
```

**How it works**:
```c
char *_memcpy(char *dest, char *src, unsigned int n) {
    unsigned int i;
    
    for (i = 0; i < n; i++) {
        dest[i] = src[i];  // Copy each byte
    }
    return dest;
}
```

#### 3. `_strchr` - Find Character in String

**Purpose**: Find the first occurrence of a character in a string

```c
char *_strchr(char *s, char c);
```

**Example**:
```c
char *str = "hello";
char *result = _strchr(str, 'l');
// result points to "llo" (first 'l' found)
```

**How it works**:
```c
char *_strchr(char *s, char c) {
    while (*s != '\0') {
        if (*s == c) {
            return s;  // Found it! Return pointer to this position
        }
        s++;  // Move to next character
    }
    
    // Check if looking for null terminator
    if (*s == c) {
        return s;
    }
    
    return NULL;  // Character not found
}
```

#### 4. `_strspn` - Get Prefix Length

**Purpose**: Count how many characters at the start of a string are in an "accept" set

```c
unsigned int _strspn(char *s, char *accept);
```

**Example**:
```c
char *str = "hello, world";
char *accept = "helo";
unsigned int n = _strspn(str, accept);
// n = 5 because "hello" only contains letters from "helo"
// Stops at ',' because comma is not in accept
```

#### 5. `_strpbrk` - Find Any of Multiple Characters

**Purpose**: Find the first occurrence of ANY character from an "accept" set

```c
char *_strpbrk(char *s, char *accept);
```

**Example**:
```c
char *str = "hello, world";
char *accept = "ow";
char *result = _strpbrk(str, accept);
// result points to "o, world" (first 'o' in "hello")
```

#### 6. `_strstr` - Find Substring

**Purpose**: Find the first occurrence of a substring within a string

```c
char *_strstr(char *haystack, char *needle);
```

**Example**:
```c
char *str = "hello, world";
char *sub = "world";
char *result = _strstr(str, sub);
// result points to "world"
```

**How it works** (simplified):
```c
char *_strstr(char *haystack, char *needle) {
    // If needle is empty, return haystack
    if (*needle == '\0') {
        return haystack;
    }
    
    // Try each position in haystack
    while (*haystack != '\0') {
        char *h = haystack;
        char *n = needle;
        
        // Check if needle matches starting here
        while (*h == *n && *n != '\0') {
            h++;
            n++;
        }
        
        // If we reached end of needle, we found it!
        if (*n == '\0') {
            return haystack;
        }
        
        haystack++;  // Try next position
    }
    
    return NULL;  // Not found
}
```

---

## Part 4: Introduction to Recursion

### What is Recursion?

**Recursion** is when a function calls itself. It's like looking into two mirrors facing each other—you see infinite reflections!

### The Key Components of Recursion

Every recursive function needs two things:

1. **Base Case**: The condition that stops the recursion
2. **Recursive Case**: The part where the function calls itself with a simpler problem

### Simple Example: Printing a String

**Non-recursive way** (with a loop):
```c
void print_string(char *s) {
    int i = 0;
    while (s[i] != '\0') {
        _putchar(s[i]);
        i++;
    }
    _putchar('\n');
}
```

**Recursive way**:
```c
void _puts_recursion(char *s) {
    // BASE CASE: if we hit the end, print newline and stop
    if (*s == '\0') {
        _putchar('\n');
        return;
    }
    
    // RECURSIVE CASE: print current character, then recurse on rest
    _putchar(*s);
    _puts_recursion(s + 1);  // Call itself with next character
}
```

**How it works when you call** `_puts_recursion("Hi")`:
```
Call 1: _puts_recursion("Hi")   → prints 'H', calls _puts_recursion("i")
Call 2: _puts_recursion("i")    → prints 'i', calls _puts_recursion("")
Call 3: _puts_recursion("")     → *s is '\0', prints '\n', returns
        ↓ returns to Call 2
        ↓ returns to Call 1
        ↓ done!
```

### Example: String Length

```c
int _strlen_recursion(char *s) {
    // BASE CASE: empty string has length 0
    if (*s == '\0') {
        return 0;
    }
    
    // RECURSIVE CASE: 1 + length of rest of string
    return 1 + _strlen_recursion(s + 1);
}
```

**How it works for** `_strlen_recursion("Cat")`:
```
Call 1: _strlen_recursion("Cat") → return 1 + _strlen_recursion("at")
Call 2: _strlen_recursion("at")  → return 1 + _strlen_recursion("t")
Call 3: _strlen_recursion("t")   → return 1 + _strlen_recursion("")
Call 4: _strlen_recursion("")    → return 0
        ↓
Call 3: return 1 + 0 = 1
        ↓
Call 2: return 1 + 1 = 2
        ↓
Call 1: return 1 + 2 = 3
        ↓
Final answer: 3
```

### Example: Factorial

The factorial of a number n (written as n!) is:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 3! = 3 × 2 × 1 = 6
- 1! = 1
- 0! = 1 (by definition)

```c
int factorial(int n) {
    // BASE CASE: error check
    if (n < 0) {
        return -1;
    }
    
    // BASE CASE: 0! and 1! are both 1
    if (n == 0 || n == 1) {
        return 1;
    }
    
    // RECURSIVE CASE: n! = n × (n-1)!
    return n * factorial(n - 1);
}
```

**How it works for** `factorial(5)`:
```
Call 1: factorial(5) → return 5 * factorial(4)
Call 2: factorial(4) → return 4 * factorial(3)
Call 3: factorial(3) → return 3 * factorial(2)
Call 4: factorial(2) → return 2 * factorial(1)
Call 5: factorial(1) → return 1
        ↓
Call 4: return 2 * 1 = 2
        ↓
Call 3: return 3 * 2 = 6
        ↓
Call 2: return 4 * 6 = 24
        ↓
Call 1: return 5 * 24 = 120
        ↓
Final answer: 120
```

### Example: Power Function

Calculate x raised to the power of y (x^y):

```c
int _pow_recursion(int x, int y) {
    // BASE CASE: negative exponent
    if (y < 0) {
        return -1;
    }
    
    // BASE CASE: anything to power 0 is 1
    if (y == 0) {
        return 1;
    }
    
    // RECURSIVE CASE: x^y = x * x^(y-1)
    return x * _pow_recursion(x, y - 1);
}
```

### When to Use Recursion vs. Loops

**Use Recursion when:**
- The problem naturally breaks into smaller versions of itself
- You're working with tree-like or nested structures
- The recursive solution is clearer and simpler

**Use Loops when:**
- Simple iteration is all you need
- Performance is critical (recursion uses more memory)
- The iterative solution is just as clear

### Important Warning About Recursion

**Stack Overflow**: Each recursive call uses memory. Too many calls = program crash!

```c
// BAD: This will crash!
void infinite_recursion() {
    infinite_recursion();  // Never stops!
}
```

**Always make sure**:
1. You have a base case
2. Each recursive call moves toward the base case
3. The base case will eventually be reached

---

## Practical Tips for Your Projects

### For Pointer Projects:

1. **Draw it out**: Visualize memory with boxes and arrows
2. **Use descriptive variable names**: `ptr_to_ptr` is clearer than `pp`
3. **Check for NULL**: Always verify pointers before dereferencing
4. **Remember the syntax**:
   - `*ptr` = value at address
   - `&var` = address of variable
   - `**ptr_to_ptr` = value pointed to by pointer pointed to

### For Array Projects:

1. **Remember array indices start at 0**
2. **Watch your bounds**: Array of size 5 has indices 0-4
3. **For 2D arrays**: First index = row, second = column
4. **When passing to functions**: Remember the array decays to a pointer

### For String Projects:

1. **Always account for the null terminator** (`\0`)
2. **Test edge cases**: empty strings, single characters
3. **Don't assume input format**: check for NULL pointers
4. **Understand pointer arithmetic**: `s + 1` moves to next character

### For Recursion Projects:

1. **Start with the base case**: What's the simplest version?
2. **Trust the recursion**: Assume the recursive call works
3. **Test with small inputs**: Try n=0, n=1, n=2 first
4. **Draw the call stack**: Visualize what happens
5. **Check that you're moving toward the base case**

---

## Summary

Today we covered:

1. **Pointers to Pointers**: Pointers that store addresses of other pointers
2. **Multidimensional Arrays**: Grids/tables of data accessed with multiple indices
3. **String Functions**: Building blocks for text manipulation
4. **Recursion**: Functions that call themselves to solve problems

Remember: **Practice is key!** These concepts become clearer the more you work with them. Start with simple examples, test frequently, and don't hesitate to draw diagrams to visualize what's happening.

Good luck with your projects, and remember—every expert programmer once struggled with these same concepts. You've got this! 🚀