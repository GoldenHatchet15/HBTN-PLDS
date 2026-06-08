# Peer Learning Day: C Functions & Nested Loops

## Introduction
Hey everyone! Today we're diving into two fundamental concepts in C programming: **functions** and **nested loops**. These are building blocks you'll use constantly, so let's make sure we really understand them.

---

## Part 1: Functions in C

### What is a Function?
A function is a reusable block of code that performs a specific task. Think of it like a recipe - you write it once and can use it many times.

**Basic anatomy:**
```c
return_type function_name(parameters)
{
    /* code here */
    return value;
}
```

### Key Concepts

**1. Declaration vs Definition**
- **Declaration (Prototype)**: Tells the compiler a function exists
  ```c
  int add(int a, int b);  /* Just the signature */
  ```
- **Definition**: The actual implementation
  ```c
  int add(int a, int b)
  {
      return a + b;
  }
  ```

**2. Why Use Prototypes?**
Prototypes go in header files (like `main.h`) and tell the compiler what functions are available before you use them. This allows you to call functions before they're defined in your code.

**3. Return Types**
- `void`: Returns nothing (like `print_alphabet`)
- `int`: Returns an integer (like `add`, `_islower`)
- Must match what your function actually returns!

**4. Practical Example**
```c
/* Prototype */
int _islower(int c);

/* Definition */
int _islower(int c)
{
    if (c >= 'a' && c <= 'z')
        return (1);
    return (0);
}
```

---

## Part 2: Nested Loops

### What Are Nested Loops?
A nested loop is simply a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

**Basic structure:**
```c
for (outer conditions)
{
    for (inner conditions)
    {
        /* code executes here */
    }
}
```

### How They Work
Think of it like a clock:
- **Outer loop** = hours (moves slowly)
- **Inner loop** = minutes (completes 60 times per hour)

### Practical Example: Times Table
```c
void times_table(void)
{
    int i, j, result;

    for (i = 0; i <= 9; i++)        /* Outer: rows */
    {
        for (j = 0; j <= 9; j++)    /* Inner: columns */
        {
            result = i * j;
            /* Print result with proper formatting */
        }
        _putchar('\n');
    }
}
```

**How it executes:**
- When i=0: j goes 0→9 (prints first row)
- When i=1: j goes 0→9 again (prints second row)
- Continues until i=9

---

## Part 3: Variable Scope

**Scope** = where a variable can be accessed

- **Local variables**: Declared inside functions, only accessible there
- **Parameters**: Variables passed to functions, act like local variables
- **Global variables**: ❌ Not allowed in this project!

```c
void example(int param)    /* param is local to this function */
{
    int local = 5;         /* local is only accessible here */
}
```

---

## Part 4: Header Files & Compilation

### Header Files (`main.h`)
Contains:
- Function prototypes
- Macro definitions
- Included with `#include "main.h"`

**Example main.h:**
```c
#ifndef MAIN_H
#define MAIN_H

int _putchar(char c);
void print_alphabet(void);
int _islower(int c);
int add(int a, int b);

#endif
```

### Understanding Header Guards

**What are they?**
The `#ifndef`, `#define`, and `#endif` directives are called **include guards** or **header guards**.

**Why do we need them?**
They prevent a header file from being included multiple times in the same compilation, which would cause errors.

**How they work:**
```c
#ifndef MAIN_H        /* If MAIN_H is NOT defined */
#define MAIN_H        /* Define MAIN_H now */

/* Your prototypes here */

#endif                /* End of the guard */
```

**Real-world scenario without guards:**
```c
/* file1.c includes main.h */
/* file2.c includes main.h */
/* file1.c also includes file2.c */
/* Now main.h would be included twice! ❌ */
```

With guards, the second time `main.h` is included, `MAIN_H` is already defined, so the compiler skips the contents. Problem solved! ✅

**Naming convention:** Use `FILENAME_H` in all caps (e.g., `MAIN_H`, `HELPER_H`)

---

### GCC Flags Explained (In Detail)

```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 file.c
```

#### `-Wall` (Warnings All)
- Enables most common warning messages
- Catches issues like: unused variables, implicit function declarations, missing return statements
- **Example:** Warns if you declare `int x;` but never use it

#### `-Werror` (Warnings as Errors)
- Treats ALL warnings as compilation errors
- Your code won't compile until you fix every warning
- **Why?** Forces you to write clean code with no "maybe problems"

#### `-Wextra` (Extra Warnings)
- Enables additional warnings not covered by `-Wall`
- Catches subtle issues like: comparing signed/unsigned integers, unused parameters
- **Example:** Warns about `if (x = 5)` when you meant `if (x == 5)`

#### `-pedantic` (Pedantic ISO C)
- Enforces strict ISO C standard compliance
- Rejects any code that uses compiler-specific extensions
- **Why?** Ensures your code is portable and follows the official C standard
- **Example:** Rejects `//` comments in C89 (only `/* */` allowed)

#### `-std=gnu89` (Standard GNU C89)
**What is C89?**
- C89 (also called ANSI C or C90) is a version of the C programming language standardized in 1989
- It's an older, more restrictive standard compared to modern C (C99, C11, C17)

**Key C89 restrictions:**
- Variables must be declared at the beginning of a block
  ```c
  /* C89 - CORRECT */
  int i;
  i = 0;
  
  /* C99 - WRONG in C89 */
  for (int i = 0; i < 10; i++)  /* Can't declare here! */
  ```
- No `//` comments (only `/* */`)
- No inline variable declarations
- Different rules for function declarations

**Why GNU89 instead of pure C89?**
- `gnu89` = C89 + some helpful GNU extensions
- Allows some compiler-specific features while staying mostly standard
- Balance between strictness and practicality

**Why learn C89 in 2025?**
- Teaches disciplined programming habits
- Many embedded systems and legacy codebases still use C89
- Understanding older standards helps you appreciate modern C features
- Forces you to think about code organization

---

### Full Compilation Example
```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 _putchar.c 1-main.c 1-alphabet.c -o 1-alphabet
```

**Breaking it down:**
1. `gcc` - The GNU C Compiler
2. Flags enforce strict, clean code
3. List all `.c` files to compile
4. `-o 1-alphabet` - Output executable named "1-alphabet"
5. Result: A compiled program ready to run with `./1-alphabet`

---

## Quick Tips for Success

1. **Always prototype** your functions in `main.h`
2. **Use meaningful names** for functions and variables
3. **Test nested loops** with small numbers first
4. **Remember `_putchar`** is your only printing tool (no `printf`!)
5. **Check your formatting** - spacing matters in output
6. **One task per function** - keep them focused

---

## Common Pitfalls

- Forgetting to include `main.h`
- Missing newline at end of file
- Off-by-one errors in loops
- Wrong return type
- Not handling negative numbers properly

---

## Practice Challenge
Try writing a function that uses nested loops to print a simple pattern:
```
*
**
***
****
```

This combines everything: function definition, nested loops, and `_putchar`!

---

## Summary

- **Functions** make code reusable and organized
- **Prototypes** declare functions before use
- **Nested loops** allow you to work with grid-like patterns
- **Scope** determines where variables are accessible
- **Header files** organize your prototypes
- **Compiler flags** help catch errors early

**Questions?** Remember: functions make code reusable, loops make code repeat, and nested loops let you work with grid-like patterns. Master these and you're well on your way to becoming a solid C programmer!

---

## Additional Resources

- Man pages: `man 3 printf`, `man gcc`
- Betty style guide for code formatting
- Practice with the project tasks 0-11
- Experiment with different loop combinations

Good luck with your project!