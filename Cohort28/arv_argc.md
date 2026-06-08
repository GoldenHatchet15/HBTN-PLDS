# C - Pointers, Recursion, and Command Line Arguments

## Table of Contents
1. [Even More Pointers - Function Review](#part-1-even-more-pointers---function-review)
2. [Recursion - Quick Review](#part-2-recursion---quick-review)
3. [argc and argv - Full Lecture](#part-3-argc-and-argv---full-lecture)

---

## Part 1: Even More Pointers - Function Review

### Overview
These are C standard library functions that we'll implement ourselves. Understanding these functions helps you master pointer manipulation and memory operations.

### 1. `_memset` - Memory Set
**Purpose:** Sets a block of memory to a specific value

**Prototype:** `char *_memset(char *s, char b, unsigned int n);`

**How it works:**
- Takes a pointer to memory (`s`)
- Fills the first `n` bytes with the constant byte `b`
- Returns a pointer to the memory area `s`

**Example:**
```c
char buffer[10];
_memset(buffer, 'A', 10);  // Sets all 10 bytes to 'A'
```

**Use cases:** Initializing arrays, clearing buffers, setting default values

---

### 2. `_memcpy` - Memory Copy
**Purpose:** Copies a block of memory from one location to another

**Prototype:** `char *_memcpy(char *dest, char *src, unsigned int n);`

**How it works:**
- Copies `n` bytes from memory area `src` to memory area `dest`
- Returns a pointer to `dest`
- **Important:** Does not handle overlapping memory regions

**Example:**
```c
char src[5] = "Hello";
char dest[5];
_memcpy(dest, src, 5);  // Copies "Hello" to dest
```

**Use cases:** Duplicating data, copying structures, buffer operations

---

### 3. `_strchr` - String Character
**Purpose:** Locates the first occurrence of a character in a string

**Prototype:** `char *_strchr(char *s, char c);`

**How it works:**
- Searches string `s` for character `c`
- Returns a pointer to the first occurrence of `c`
- Returns `NULL` if character is not found

**Example:**
```c
char *str = "hello";
char *result = _strchr(str, 'l');  // Returns pointer to first 'l'
// result points to "llo"
```

**Use cases:** Finding characters, string parsing, validation

---

### 4. `_strspn` - String Span
**Purpose:** Gets the length of a prefix substring consisting only of certain characters

**Prototype:** `unsigned int _strspn(char *s, char *accept);`

**How it works:**
- Counts how many consecutive characters from the beginning of `s` are in `accept`
- Returns the count of matching characters

**Example:**
```c
char *s = "hello, world";
char *accept = "oleh";
unsigned int n = _strspn(s, accept);  // Returns 5
// Because "hello" contains only letters from "oleh"
```

**Use cases:** Input validation, tokenization, parsing

---

### 5. `_strpbrk` - String Pointer Break
**Purpose:** Searches a string for any of a set of bytes

**Prototype:** `char *_strpbrk(char *s, char *accept);`

**How it works:**
- Finds the first occurrence in `s` of any byte in `accept`
- Returns a pointer to the matching byte in `s`
- Returns `NULL` if no match is found

**Example:**
```c
char *s = "hello, world";
char *accept = "world";
char *result = _strpbrk(s, accept);  // Returns pointer to "llo, world"
// First match is 'l' which is in "world"
```

**Use cases:** Finding delimiters, string parsing, pattern matching

---

### 6. `_strstr` - String String
**Purpose:** Locates a substring within a string

**Prototype:** `char *_strstr(char *haystack, char *needle);`

**How it works:**
- Finds the first occurrence of substring `needle` in string `haystack`
- Returns a pointer to the beginning of the located substring
- Returns `NULL` if substring is not found

**Example:**
```c
char *haystack = "hello, world";
char *needle = "world";
char *result = _strstr(haystack, needle);  // Returns pointer to "world"
```

**Use cases:** String searching, pattern matching, text processing

---

### 7. `print_chessboard` - Print Chessboard
**Purpose:** Prints an 8x8 chessboard array

**Prototype:** `void print_chessboard(char (*a)[8]);`

**How it works:**
- Takes a pointer to an array of 8 elements (each element is an array of 8 chars)
- Prints each row of the chessboard
- Uses `_putchar` to print each character

**Key concept:** Pointer to an array - `char (*a)[8]` means pointer to an array of 8 chars

**Example:**
```c
char board[8][8] = {
    {'r', 'k', 'b', 'q', 'k', 'b', 'k', 'r'},
    {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
    // ... more rows
};
print_chessboard(board);
```

---

### 8. `print_diagsums` - Print Diagonal Sums
**Purpose:** Prints the sum of two diagonals of a square matrix

**Prototype:** `void print_diagsums(int *a, int size);`

**How it works:**
- Takes a pointer to a 2D array (cast as 1D) and its size
- Calculates sum of main diagonal (top-left to bottom-right)
- Calculates sum of secondary diagonal (top-right to bottom-left)
- Prints both sums

**Key concept:** Accessing 2D array as 1D: `a[i * size + j]` equals `array[i][j]`

**Example:**
```c
int matrix[3][3] = {
    {0, 1, 5},
    {10, 11, 12},
    {1000, 101, 102}
};
print_diagsums((int *)matrix, 3);
// Main diagonal: 0 + 11 + 102 = 113
// Secondary diagonal: 5 + 11 + 1000 = 1016
```

---

## Part 2: Recursion - Quick Review

### What is Recursion?
Recursion is when a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems.

### Key Components of Recursive Functions
1. **Base case:** The condition that stops the recursion
2. **Recursive case:** The function calling itself with modified parameters

### Quick Function Review

#### 1. `_puts_recursion` - Print String Recursively
```c
void _puts_recursion(char *s);
```
- Prints a string character by character
- Base case: When `*s == '\0'`
- Recursive case: Print current character, call with `s + 1`

#### 2. `_print_rev_recursion` - Print String in Reverse
```c
void _print_rev_recursion(char *s);
```
- Prints string in reverse order
- Base case: When `*s == '\0'`
- Recursive case: Call with `s + 1`, then print current character

#### 3. `_strlen_recursion` - String Length Recursively
```c
int _strlen_recursion(char *s);
```
- Returns length of string
- Base case: Return 0 when `*s == '\0'`
- Recursive case: Return `1 + _strlen_recursion(s + 1)`

#### 4. `factorial` - Calculate Factorial
```c
int factorial(int n);
```
- Returns factorial of n (n!)
- Base case: Return 1 when `n == 0`, return -1 when `n < 0`
- Recursive case: Return `n * factorial(n - 1)`

#### 5. `_pow_recursion` - Power Function
```c
int _pow_recursion(int x, int y);
```
- Returns x raised to power y
- Base case: Return 1 when `y == 0`, return -1 when `y < 0`
- Recursive case: Return `x * _pow_recursion(x, y - 1)`

#### 6. `_sqrt_recursion` - Square Root
```c
int _sqrt_recursion(int n);
```
- Returns natural square root of n
- Base case: Return -1 if no natural square root exists
- Recursive case: Test values until square root is found

#### 7. `is_prime_number` - Prime Number Check
```c
int is_prime_number(int n);
```
- Returns 1 if n is prime, 0 otherwise
- Base case: Numbers less than 2 are not prime
- Recursive case: Check divisibility recursively

### When to Use Recursion
✅ **Good for:**
- Tree/graph traversal
- Mathematical sequences (factorial, fibonacci)
- Divide and conquer problems
- Problems with self-similar structure

❌ **Avoid when:**
- Simple iteration is more efficient
- Stack overflow is a concern (deep recursion)
- Performance is critical

---

## Part 3: argc and argv - Full Lecture

### Introduction
When you run a program from the command line, you can pass information to it. This information is called **command-line arguments**.

```bash
./my_program argument1 argument2 argument3
```

### The Two Parameters of Main

#### Standard main function:
```c
int main(void)
{
    return (0);
}
```

#### Main with command-line arguments:
```c
int main(int argc, char *argv[])
{
    return (0);
}
```

Or equivalently:
```c
int main(int argc, char **argv)
{
    return (0);
}
```

---

### Understanding argc (Argument Count)

**`argc`** - Argument Count
- Type: `int`
- Contains the **number of arguments** passed to the program
- **Always at least 1** (the program name itself counts as an argument)

**Example:**
```bash
./program                    # argc = 1
./program hello              # argc = 2
./program hello world        # argc = 3
./program one two three      # argc = 4
```

---

### Understanding argv (Argument Vector)

**`argv`** - Argument Vector
- Type: `char *argv[]` or `char **argv`
- An **array of strings** (array of pointers to characters)
- Each element contains one argument as a string

**Important:** `argv[0]` is always the program name!

**Example:**
```bash
./myprogram hello world
```

Memory representation:
```
argv[0] → "./myprogram"
argv[1] → "hello"
argv[2] → "world"
argv[3] → NULL (marks the end)
```

---

### Visual Representation

```c
Command: ./calculator 5 + 3

argc = 4

argv:
┌─────┬──────────────┐
│  0  │ "./calculator"│
├─────┼──────────────┤
│  1  │ "5"          │
├─────┼──────────────┤
│  2  │ "+"          │
├─────┼──────────────┤
│  3  │ "3"          │
├─────┼──────────────┤
│  4  │ NULL         │
└─────┴──────────────┘
```

---

### Important Concepts

#### 1. All Arguments are Strings
Even if you pass numbers, they arrive as strings!

```c
./add 5 10
// argv[1] is "5" (string), not 5 (integer)
// argv[2] is "10" (string), not 10 (integer)
```

To use them as numbers, you must convert:
```c
#include <stdlib.h>

int num1 = atoi(argv[1]);  // Converts "5" to 5
int num2 = atoi(argv[2]);  // Converts "10" to 10
```

#### 2. Spaces Separate Arguments
```bash
./program hello world      # 3 arguments: program, hello, world
./program "hello world"    # 2 arguments: program, "hello world"
./program hello,world      # 2 arguments: program, hello,world
```

#### 3. argv Always Ends with NULL
The last element after `argv[argc - 1]` is `NULL`, which helps you know when to stop.

---

### Complete Examples

#### Example 1: Print Program Name
```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("%s\n", argv[0]);
    return (0);
}
```

**Output:**
```bash
$ gcc 0-whatsmyname.c -o mynameis
$ ./mynameis
./mynameis
$ mv mynameis newname
$ ./newname
./newname
```

---

#### Example 2: Count Arguments
```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("%d\n", argc - 1);  // Subtract 1 to exclude program name
    return (0);
}
```

**Output:**
```bash
$ ./nargs
0
$ ./nargs hello
1
$ ./nargs hello world
2
```

---

#### Example 3: Print All Arguments
```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    for (i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
    return (0);
}
```

**Output:**
```bash
$ ./args You can do anything
./args
You
can
do
anything
```

---

#### Example 4: Multiply Two Numbers
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int num1, num2, result;

    if (argc != 3)
    {
        printf("Error\n");
        return (1);
    }

    num1 = atoi(argv[1]);
    num2 = atoi(argv[2]);
    result = num1 * num2;

    printf("%d\n", result);
    return (0);
}
```

**Output:**
```bash
$ ./mul 2 3
6
$ ./mul 2 -3
-6
$ ./mul
Error
```

---

#### Example 5: Add Positive Numbers (Advanced)
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int sum = 0;
    int i, j;

    if (argc == 1)
    {
        printf("0\n");
        return (0);
    }

    for (i = 1; i < argc; i++)
    {
        /* Check if argument contains only digits */
        for (j = 0; argv[i][j] != '\0'; j++)
        {
            if (argv[i][j] < '0' || argv[i][j] > '9')
            {
                printf("Error\n");
                return (1);
            }
        }
        sum += atoi(argv[i]);
    }

    printf("%d\n", sum);
    return (0);
}
```

**Output:**
```bash
$ ./add 1 1
2
$ ./add 1 10 100 1000
1111
$ ./add 1 2 3 e 4 5
Error
$ ./add
0
```

---

### Common Functions for Argument Processing

#### 1. `atoi()` - ASCII to Integer
```c
#include <stdlib.h>
int atoi(const char *str);
```
- Converts a string to an integer
- Returns 0 if conversion fails
- Example: `atoi("123")` returns `123`

#### 2. `isdigit()` - Check if Character is Digit
```c
#include <ctype.h>
int isdigit(int c);
```
- Returns non-zero if c is a digit ('0' to '9')
- Returns 0 otherwise

---

### Using `__attribute__((unused))`

When you have parameters you don't use, the compiler may give warnings. You can suppress these:

```c
int main(int argc __attribute__((unused)), char *argv[])
{
    printf("%s\n", argv[0]);
    return (0);
}
```

Or use `(void)`:
```c
int main(int argc, char *argv[])
{
    (void)argc;
    printf("%s\n", argv[0]);
    return (0);
}
```

---

### Best Practices

1. **Always check argc** before accessing argv elements
   ```c
   if (argc < 2)
   {
       printf("Usage: %s <argument>\n", argv[0]);
       return (1);
   }
   ```

2. **Validate input** before using it
   ```c
   // Check if argument is a valid number
   for (i = 0; argv[1][i]; i++)
   {
       if (!isdigit(argv[1][i]))
       {
           printf("Error: not a number\n");
           return (1);
       }
   }
   ```

3. **Use meaningful error messages**
   ```c
   if (argc != 3)
   {
       printf("Usage: %s <num1> <num2>\n", argv[0]);
       return (1);
   }
   ```

4. **Return appropriate exit codes**
   - `return (0)` for success
   - `return (1)` for errors

---

### Common Pitfalls to Avoid

❌ **Don't access argv without checking argc:**
```c
// BAD - will crash if no arguments
printf("%s\n", argv[1]);
```

✅ **Good - check first:**
```c
if (argc > 1)
    printf("%s\n", argv[1]);
```

❌ **Don't assume arguments are numbers:**
```c
// BAD - what if argv[1] is "hello"?
int num = atoi(argv[1]);
```

✅ **Good - validate first:**
```c
// Check each character is a digit
for (i = 0; argv[1][i]; i++)
{
    if (!isdigit(argv[1][i]))
    {
        printf("Error: not a number\n");
        return (1);
    }
}
int num = atoi(argv[1]);
```

---

### Practice Exercises

1. Write a program that prints "Hello, [name]" where [name] is the first argument
2. Write a program that prints all arguments in reverse order
3. Write a program that counts how many arguments contain the letter 'e'
4. Write a calculator program that handles +, -, *, / operations
5. Write a program that prints the longest argument

---

### Summary

**argc and argv allow you to:**
- Accept input when the program starts
- Make flexible, reusable programs
- Process files, numbers, or options from the command line

**Remember:**
- `argc` = count of arguments (including program name)
- `argv` = array of argument strings
- `argv[0]` = program name
- Always validate input before using it
- Convert strings to numbers when needed (atoi)

---

## Conclusion

You now understand:
1. **Pointers/Arrays/Strings:** Essential string manipulation functions and their purposes
2. **Recursion:** How functions can call themselves to solve problems
3. **argc/argv:** How to accept and process command-line arguments

These concepts form the foundation of C programming and will be used throughout your development journey!

---

## Quick Reference Card

### Function Signatures Quick Reference

```c
/* Pointers, Arrays, Strings */
char *_memset(char *s, char b, unsigned int n);
char *_memcpy(char *dest, char *src, unsigned int n);
char *_strchr(char *s, char c);
unsigned int _strspn(char *s, char *accept);
char *_strpbrk(char *s, char *accept);
char *_strstr(char *haystack, char *needle);
void print_chessboard(char (*a)[8]);
void print_diagsums(int *a, int size);

/* Recursion */
void _puts_recursion(char *s);
void _print_rev_recursion(char *s);
int _strlen_recursion(char *s);
int factorial(int n);
int _pow_recursion(int x, int y);
int _sqrt_recursion(int n);
int is_prime_number(int n);

/* Command Line Arguments */
int main(int argc, char *argv[]);
int main(int argc, char **argv);  // Equivalent
```

Good luck with your studies! 🚀