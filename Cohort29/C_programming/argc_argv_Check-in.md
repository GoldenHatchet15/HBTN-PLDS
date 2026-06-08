# Command-Line Arguments in C

## A Complete Beginner-Friendly Lecture on `argc` and `argv`

---

# 1. Introduction

When we run a program in the terminal, we can send extra information to it.

Example:

```bash
./myprogram Hello World
```

The words `Hello` and `World` are called **command-line arguments**.

They allow a program to behave differently **without modifying the source code**.

---

# 2. The `main` Function Prototypes

There are two common versions of `main`.

## 2.1 No Arguments Version

```c
int main(void)
```

Use this when the program does not need command-line input.

---

## 2.2 With Command-Line Arguments

```c
int main(int argc, char *argv[])
```

This version allows the program to receive arguments from the terminal.

---

# 3. Understanding `argc`

`argc` stands for **Argument Count**.

It represents the total number of arguments passed to the program, including the program name.

Important rule:

* `argc` is always at least **1**.

Why?

Because the program name itself counts as the first argument.

---

## Example

If you run:

```bash
./myprogram Hello World
```

Then internally:

```
argc = 3
```

Because:

1. `./myprogram`
2. `Hello`
3. `World`

---

# 4. Understanding `argv`

`argv` stands for **Argument Vector**.

It is an array of strings:

```c
char *argv[]
```

Each element is a pointer to a string.

| Index   | Value         |
| ------- | ------------- |
| argv[0] | "./myprogram" |
| argv[1] | "Hello"       |
| argv[2] | "World"       |

Important:

* `argv[0]` is always the program name.
* Actual user input starts at `argv[1]`.

---

# 5. Why Arrays Start at 0

C arrays are zero-indexed.

If:

```
argc = 3
```

Valid indexes are:

```
0, 1, 2
```

That is why loops must use:

```c
for (i = 0; i < argc; i++)
```

Never:

```c
for (i = 0; i <= argc; i++)
```

Because that would access memory out of bounds.

---

# 6. Memory Model

When you run:

```bash
./myprogram Hello
```

Memory conceptually looks like this:

```
argv
 |
 |--> argv[0] --> "./myprogram\0"
 |--> argv[1] --> "Hello\0"
```

This explains why:

* `argv[i]` is a string
* `argv[i][j]` is a character inside that string

---

# 7. Exercise 1 — Print Program Name

## Code

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Program name: %s\n", argv[0]);
    return 0;
}
```

## Explanation

* `argv[0]` always stores the program name.
* `%s` prints a string.

If you rename the program, `argv[0]` changes automatically.

---

# 8. Exercise 2 — Count Arguments

## Code

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("Number of arguments: %d\n", argc - 1);
    return 0;
}
```

## Explanation

* `argc` includes the program name.
* We subtract 1 to count only user-provided arguments.

Example:

```bash
./countargs Hello World
```

```
argc = 3
argc - 1 = 2
```

---

# 9. Exercise 3 — Print All Arguments

## Code

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    for (i = 0; i < argc; i++)
    {
        printf("Argument %d: %s\n", i, argv[i]);
    }

    return 0;
}
```

## Breakdown

* Loop starts at 0 to include program name.
* Condition must be `i < argc`.
* Stops automatically when `i == argc`.

---

# 10. Exercise 4 — Multiply Two Numbers

## Code

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int result;

    if (argc != 3)
    {
        printf("Error\n");
        return 1;
    }

    result = atoi(argv[1]) * atoi(argv[2]);

    printf("%d\n", result);
    return 0;
}
```

## Breakdown

### Step 1: Validate argument count

We expect:

```
program number number
```

That means `argc` must equal 3.

### Step 2: Convert strings to integers

All arguments are strings.

```
"2" is not the same as 2
```

`atoi()` converts a string into an integer.

### Step 3: Multiply and print

After conversion, multiplication works normally.

---

# 11. Exercise 5 — Add Many Numbers (With Validation)

## Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    int sum = 0;
    int i, j;

    for (i = 1; i < argc; i++)
    {
        for (j = 0; argv[i][j] != '\0'; j++)
        {
            if (!isdigit(argv[i][j]))
            {
                printf("Error\n");
                return 1;
            }
        }

        sum += atoi(argv[i]);
    }

    printf("%d\n", sum);
    return 0;
}
```

## Detailed Breakdown

### Outer Loop

Starts at index 1 to skip program name.

### Inner Loop

Checks each character inside the argument string.

### `isdigit()`

Ensures each character is between `'0'` and `'9'`.

If not → print `Error` and exit.

### Final Step

Convert valid strings and accumulate sum.

---

# 12. When to Use `argc` and `argv`

## Use Them When:

* Writing calculators
* Handling files (`./program file.txt`)
* Using flags (`./program -v`)
* Automation scripts

## Avoid When:

* Interactive programs using `scanf`
* Complex structured input better handled with files

---

# 13. Final Mental Model

When you run:

```bash
./program arg1 arg2 arg3
```

The OS builds:

```
argc = 4

argv = [
    "./program",
    "arg1",
    "arg2",
    "arg3"
]
```

Your program simply receives that structure and works with it.

---

# Key Takeaways

* `argc` counts arguments (including program name).
* `argv` is an array of strings.
* All command-line inputs are strings.
* Always validate before converting with `atoi()`.
* Loop carefully using `i < argc`.

---

End of Lecture.
