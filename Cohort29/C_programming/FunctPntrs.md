# Function Pointers in C — Complete Lecture

**Instructor:** Raphael Santos

---

## Table of Contents

- [Function Pointers in C — Complete Lecture](#function-pointers-in-c--complete-lecture)
  - [Table of Contents](#table-of-contents)
  - [1. What is a Function Pointer?](#1-what-is-a-function-pointer)
  - [2. Why Function Pointers Exist](#2-why-function-pointers-exist)
  - [3. Functions Have Addresses](#3-functions-have-addresses)
  - [4. Function Pointer Syntax — Reading It Inside-Out](#4-function-pointer-syntax--reading-it-inside-out)
    - [The Clockwise/Spiral Rule](#the-clockwisespiral-rule)
  - [5. Why Parentheses Matter](#5-why-parentheses-matter)
    - [Without the parentheses around `*fp`](#without-the-parentheses-around-fp)
    - [With the parentheses around `*fp`](#with-the-parentheses-around-fp)
  - [6. Assigning a Function to a Pointer](#6-assigning-a-function-to-a-pointer)
  - [7. Calling a Function Through a Pointer](#7-calling-a-function-through-a-pointer)
  - [8. Complete Basic Example with Walkthrough](#8-complete-basic-example-with-walkthrough)
    - [Step-by-Step Walkthrough](#step-by-step-walkthrough)
  - [9. The Signature Must Match — Why This Matters](#9-the-signature-must-match--why-this-matters)
    - [Return type mismatch](#return-type-mismatch)
    - [Parameter count mismatch](#parameter-count-mismatch)
    - [Parameter type mismatch](#parameter-type-mismatch)
  - [10. Swapping Behavior at Runtime](#10-swapping-behavior-at-runtime)
  - [11. Passing Function Pointers to Functions](#11-passing-function-pointers-to-functions)
    - [Why This Matters](#why-this-matters)
  - [12. Callback Functions — Concept and Analogy](#12-callback-functions--concept-and-analogy)
    - [Real-World Analogy](#real-world-analogy)
    - [In Code](#in-code)
  - [13. Callback Example with Step-by-Step](#13-callback-example-with-step-by-step)
    - [Step-by-Step Walkthrough of `run_task(1, on_complete)`](#step-by-step-walkthrough-of-run_task1-on_complete)
  - [14. Arrays of Function Pointers — Dispatch Tables](#14-arrays-of-function-pointers--dispatch-tables)
    - [Why a Dispatch Table is Better Than if-else](#why-a-dispatch-table-is-better-than-if-else)
  - [15. Menu-Driven Program with Dispatch Table](#15-menu-driven-program-with-dispatch-table)
  - [16. Using `typedef` for Readability](#16-using-typedef-for-readability)
    - [How to Read a Function Pointer typedef](#how-to-read-a-function-pointer-typedef)
    - [Full Example with typedef](#full-example-with-typedef)
  - [17. Function Pointers Inside Structs](#17-function-pointers-inside-structs)
    - [Why This Pattern Matters](#why-this-pattern-matters)
  - [18. Real-World Example: `qsort` from the Standard Library](#18-real-world-example-qsort-from-the-standard-library)
    - [Sorting Integers](#sorting-integers)
    - [Step-by-Step: What `qsort` Does With Your Function Pointer](#step-by-step-what-qsort-does-with-your-function-pointer)
    - [Sorting in Descending Order](#sorting-in-descending-order)
  - [19. NULL Function Pointers and Safety](#19-null-function-pointers-and-safety)
    - [When NULL Pointers Are Useful](#when-null-pointers-are-useful)
  - [20. Common Mistakes and How to Avoid Them](#20-common-mistakes-and-how-to-avoid-them)
    - [Mistake 1: Forgetting the parentheses in the declaration](#mistake-1-forgetting-the-parentheses-in-the-declaration)
    - [Mistake 2: Calling an uninitialized pointer](#mistake-2-calling-an-uninitialized-pointer)
    - [Mistake 3: Calling the function when you mean to assign it](#mistake-3-calling-the-function-when-you-mean-to-assign-it)
    - [Mistake 4: Mismatched signature — especially with return type](#mistake-4-mismatched-signature--especially-with-return-type)
    - [Mistake 5: Forgetting to check for NULL before calling](#mistake-5-forgetting-to-check-for-null-before-calling)
    - [Mistake 6: Dereferencing confusion](#mistake-6-dereferencing-confusion)
  - [21. Mental Model and Memory Diagram](#21-mental-model-and-memory-diagram)
  - [22. Final Combined Example with Walkthrough](#22-final-combined-example-with-walkthrough)
    - [Walkthrough](#walkthrough)
  - [23. Interview Questions](#23-interview-questions)
  - [24. Summary and Quick Reference](#24-summary-and-quick-reference)
    - [Declaration Syntax](#declaration-syntax)
    - [With typedef](#with-typedef)
    - [The Four Operations](#the-four-operations)
    - [Common Patterns](#common-patterns)
    - [Signature Matching Rules](#signature-matching-rules)

---

## 1. What is a Function Pointer?

Before defining a function pointer, recall what a regular pointer is:

```c
int x = 10;
int *p = &x;
```

Here, `p` stores the **memory address** of the variable `x`. When you dereference `p`, you get back the value `10`.

A **function pointer** works on the same principle — except instead of storing the address of a variable, it stores the **address of a function**.

Every function you write in C exists somewhere in memory. It has a starting address — the address of its first instruction. A function pointer holds that address, which means you can:

- Call the function through the pointer
- Pass the function to another function as an argument
- Store it in an array and choose which one to call at runtime
- Put it inside a struct

This is a powerful concept that unlocks a whole class of programming patterns that are impossible with regular function calls alone.

---

## 2. Why Function Pointers Exist

Consider a situation where you want to write a single `calculate` function that can either add, subtract, or multiply two numbers — and the choice is made at runtime based on user input.

Without function pointers, you would need something like this:

```c
int calculate(int x, int y, char op)
{
    if (op == '+') return x + y;
    if (op == '-') return x - y;
    if (op == '*') return x * y;
    return 0;
}
```

This works for simple cases, but it has a problem: every time you want to add a new operation, you must **modify the function itself**. In a large codebase, this leads to long, fragile chains of if-else or switch statements.

With function pointers, you instead write:

```c
int calculate(int x, int y, int (*op)(int, int))
{
    return op(x, y);
}
```

Now `calculate` does not need to know anything about the operation. You pass the function in from outside. To add a new operation, you just write a new function and pass it in — you never touch `calculate` again.

This pattern is used throughout professional C programming and systems design:

| Use case | Description |
|----------|-------------|
| **Callbacks** | Pass a function to execute after an event |
| **Dispatch tables** | Array of functions — choose one by index |
| **Plugin systems** | Load behavior without recompiling |
| **Sorting** | Tell `qsort` how to compare elements |
| **Event handlers** | Register functions to respond to input |
| **State machines** | Each state is a function; the machine stores the current state as a pointer |

---

## 3. Functions Have Addresses

This is the foundational idea you must internalize before anything else makes sense.

When you write a function:

```c
int add(int a, int b)
{
    return a + b;
}
```

The compiler translates this into machine instructions and stores them in the **text segment** (also called the code segment) of your program's memory. Those instructions sit at a specific memory address — just like any variable.

You can verify this by printing the address:

```c
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    printf("Address of add: %p\n", (void *)add);
    return 0;
}
```

Sample output (will vary per machine and run):

```
Address of add: 0x5615a3f7b149
```

That hexadecimal value is where the function lives in memory. A function pointer stores exactly this address. When you "call through" the pointer, you are telling the CPU: "jump to this address and start executing."

---

## 4. Function Pointer Syntax — Reading It Inside-Out

Function pointer syntax is notoriously confusing for beginners. The key is to read it **inside-out, right-to-left**.

```c
int (*fp)(int, int);
```

Read it like this, starting from the variable name `fp`:

| Fragment | Reading |
|----------|---------|
| `fp` | "fp is..." |
| `*fp` | "...a pointer..." |
| `(*fp)(int, int)` | "...to a function that takes two ints..." |
| `int (*fp)(int, int)` | "...and returns an int." |

**Full reading:** `fp` is a pointer to a function that takes two integers and returns an integer.

### The Clockwise/Spiral Rule

Another way to read complex C declarations is the **clockwise rule**:

1. Start at the variable name
2. Move clockwise (right first, then up, then left)
3. Resolve each piece as you encounter it

```
        int    (*fp)    (int, int)
         ↑       ↑           ↑
      returns  pointer   takes these
```

With practice, this becomes natural. For now, the key takeaway is that the parentheses around `*fp` are **mandatory** and completely change the meaning, as you will see next.

---

## 5. Why Parentheses Matter

This is one of the most important syntactic details in C. Look at these two declarations side by side:

```c
int *fp(int, int);      /* NOT a function pointer */
int (*fp)(int, int);    /* IS a function pointer  */
```

They look almost identical, but they mean completely different things.

### Without the parentheses around `*fp`

```c
int *fp(int, int);
```

Because `()` has higher precedence than `*` in C, the compiler sees this as:

> `fp` is a **function** that takes two ints and **returns `int *`** (a pointer to int).

This is a **function declaration**, not a pointer declaration.

### With the parentheses around `*fp`

```c
int (*fp)(int, int);
```

The parentheses force the `*` to bind to `fp` first:

> `fp` is a **pointer** to a function that takes two ints and returns `int`.

This is a **function pointer declaration**.

The difference is critical. If you write the wrong one and try to assign a function address to it, you will either get a compiler error or, worse, silently incorrect behavior.

**Memory aid:** The parentheses around `*fp` are the "pointer cage" — they contain and protect the pointer nature of the variable. If you ever forget, ask yourself: *"Does the star belong to the variable, or does it belong to the return type?"* The parentheses make it belong to the variable.

---

## 6. Assigning a Function to a Pointer

Once you declare a function pointer, you assign a function to it by using the function's name — which, in C, automatically decays to the function's address (just like an array name decays to the address of its first element).

```c
int (*fp)(int, int);

fp = add;    /* using the function name directly */
```

You can also explicitly take the address with `&`:

```c
fp = &add;   /* explicitly taking the address */
```

Both are valid and equivalent. Most C programmers use the shorter form without `&`, since the function name already represents its address.

**What you cannot do:**

```c
fp = add();   /* WRONG — this calls add and tries to assign its return value */
fp = &add();  /* WRONG — same problem */
```

Always assign the function **name** (its address), never a **call** (its result).

---

## 7. Calling a Function Through a Pointer

Once a function pointer is assigned, there are two syntactically valid ways to call it:

```c
/* Form 1: direct call syntax — most common */
fp(2, 3);

/* Form 2: explicit dereference syntax */
(*fp)(2, 3);
```

Both produce exactly the same result. Form 1 is preferred by most programmers because it is cleaner and reads like a normal function call.

Form 2 is more explicit about what is happening — you are dereferencing a pointer to get the function, then calling it. Some instructors and style guides prefer it for clarity, especially when teaching.

You will see both in professional code. Know how to read them.

---

## 8. Complete Basic Example with Walkthrough

Here is a complete, minimal example putting everything together:

```c
#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int (*fp)(int, int);    /* declare function pointer */
    int result;

    fp = add;               /* assign the function */
    result = fp(5, 7);      /* call through the pointer */

    printf("Result: %d\n", result);
    return 0;
}
```

**Output:**

```
Result: 12
```

### Step-by-Step Walkthrough

**Step 1 — `int (*fp)(int, int);`**

A function pointer variable named `fp` is declared. It is not yet pointing at any function — it contains an indeterminate value (like any uninitialized variable).

**Step 2 — `fp = add;`**

The name `add` evaluates to the memory address of the `add` function. That address is stored in `fp`.

```
Memory:

  fp → [ address of add → 0x401136 ]

  At 0x401136:
  [ int add(int a, int b) { return a + b; } ]
```

**Step 3 — `result = fp(5, 7);`**

The CPU looks up the address stored in `fp`, jumps to that location, and executes the function with arguments `5` and `7`. The function returns `12`, which is stored in `result`.

**Step 4 — `printf(...)`**

Prints `Result: 12`.

The key insight: from the CPU's perspective, `fp(5, 7)` and `add(5, 7)` are identical. Both cause a jump to the same address with the same arguments.

---

## 9. The Signature Must Match — Why This Matters

A function pointer is tightly bound to a specific **function signature**. The signature consists of:

1. The **return type**
2. The **number of parameters**
3. The **type of each parameter** (in order)

The function pointer and the function it points to must agree on all three. Here is why each matters:

### Return type mismatch

```c
void (*fp)(int, int) = add;   /* WRONG: add returns int, not void */
```

If the caller does not expect a return value but the function produces one, the return value is simply discarded. If the caller expects a return value but the function does not produce one, the return is garbage. Either way, the behavior is undefined.

### Parameter count mismatch

```c
int (*fp)(int) = add;   /* WRONG: add takes 2 ints, not 1 */
```

The caller pushes one argument onto the stack, but the function expects two. The second parameter reads garbage from wherever the stack happens to be.

### Parameter type mismatch

```c
int (*fp)(float, float) = add;   /* WRONG: add takes int, not float */
```

`int` and `float` have different binary representations. The bits of a `float` interpreted as an `int` produce a meaningless number.

**The compiler will warn you** about these mismatches if the function is declared in scope. Pay attention to those warnings — in this area, a warning is almost always a real bug.

---

## 10. Swapping Behavior at Runtime

One of the most powerful uses of function pointers is switching which function runs **after** the program has started. This is something you simply cannot do with hardcoded function calls.

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int main(void)
{
    int (*operation)(int, int);

    /* First, point at add */
    operation = add;
    printf("Add result: %d\n", operation(10, 4));   /* prints 14 */

    /* Then, repoint at sub — no recompilation, no if-else */
    operation = sub;
    printf("Sub result: %d\n", operation(10, 4));   /* prints 6 */

    return 0;
}
```

**Output:**

```
Add result: 14
Sub result: 6
```

Notice that the call `operation(10, 4)` is written once. The behavior changes because the pointer changes. This is a fundamental technique in C — the behavior of a system can be reconfigured at runtime simply by changing which functions are pointed to.

---

## 11. Passing Function Pointers to Functions

A function pointer can be passed as a **parameter** to another function. This is how you give one function the ability to call another function it has never seen before.

The parameter syntax is exactly the same as the declaration syntax:

```c
int calculate(int x, int y, int (*op)(int, int))
{
    return op(x, y);
}
```

Here, `op` is a function pointer parameter. Whoever calls `calculate` decides what operation to perform by passing a function:

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int calculate(int x, int y, int (*op)(int, int))
{
    return op(x, y);   /* call whatever function was passed in */
}

int main(void)
{
    printf("Add: %d\n", calculate(8, 2, add));   /* passes add */
    printf("Sub: %d\n", calculate(8, 2, sub));   /* passes sub */
    printf("Mul: %d\n", calculate(8, 2, mul));   /* passes mul */

    return 0;
}
```

**Output:**

```
Add: 10
Sub: 6
Mul: 16
```

### Why This Matters

`calculate` is completely generic. It performs no arithmetic itself — it delegates entirely to whatever function you hand it. If you later write a `divide` function with the same signature, you can pass it to `calculate` without changing `calculate` at all.

This is the **open/closed principle** in action: the function is open for extension (new operations) but closed for modification (you never edit it).

---

## 12. Callback Functions — Concept and Analogy

A **callback** is a function that you pass to another function to be called at a later point — typically when some event occurs or some condition is met.

The name "callback" comes from the idea: "I am giving you my number. Call me back when you are ready."

### Real-World Analogy

Imagine you call a restaurant to make a reservation. The host says: "We are full right now, but leave me your phone number and I will call you when a table is free."

In this analogy:
- **You** are the programmer who registers a callback
- **Your phone number** is the function pointer
- **The restaurant host** is the library function or system that stores your callback
- **The phone call** is when your callback function gets invoked
- **"When a table is free"** is the event that triggers the callback

You hand over control, and the system calls you back when it needs you.

### In Code

```c
void process(void (*callback)(void))
{
    printf("Processing...\n");
    /* ... some work happens ... */
    callback();     /* "call back" when done */
}
```

`process` does not know or care what `callback` does. It just knows: when the work is done, invoke this function. The caller decides what that function is.

---

## 13. Callback Example with Step-by-Step

```c
#include <stdio.h>

void on_complete(void)
{
    printf("Task finished! Notifying user.\n");
}

void on_error(void)
{
    printf("Something went wrong! Logging error.\n");
}

void run_task(int success, void (*callback)(void))
{
    printf("Running task...\n");

    if (success)
        callback();     /* call whatever was passed in */
    else
        printf("Task failed before callback.\n");
}

int main(void)
{
    run_task(1, on_complete);   /* pass on_complete as the callback */
    run_task(0, on_error);      /* pass on_error as the callback */

    return 0;
}
```

**Output:**

```
Running task...
Task finished! Notifying user.
Running task...
Task failed before callback.
```

### Step-by-Step Walkthrough of `run_task(1, on_complete)`

| Step | What happens |
|------|-------------|
| `run_task` is called with `success = 1` and `callback = address of on_complete` | Function enters |
| `printf("Running task...\n")` | Prints first line |
| `if (success)` → true | Condition is satisfied |
| `callback()` | Jumps to `on_complete`, prints second line |
| Returns to `main` | Done |

The key point: `run_task` never mentions `on_complete` by name. It just calls whatever function address it received. You could pass a completely different function and `run_task` would behave differently — with zero changes to its own code.

---

## 14. Arrays of Function Pointers — Dispatch Tables

An array of function pointers is called a **dispatch table**. It maps indices (or keys) to functions, letting you select and call a function with a simple array lookup.

```c
int (*operations[3])(int, int) = {add, sub, mul};
```

Reading this: `operations` is an array of 3 pointers, each pointing to a function that takes two ints and returns int.

```c
operations[0](4, 2);   /* calls add(4, 2) → 6  */
operations[1](4, 2);   /* calls sub(4, 2) → 2  */
operations[2](4, 2);   /* calls mul(4, 2) → 8  */
```

### Why a Dispatch Table is Better Than if-else

Compare these two approaches for a program with 5 operations:

**Without dispatch table:**

```c
if (choice == 0)       result = add(a, b);
else if (choice == 1)  result = sub(a, b);
else if (choice == 2)  result = mul(a, b);
else if (choice == 3)  result = divide(a, b);
else if (choice == 4)  result = mod(a, b);
```

5 operations → 5 branches. 50 operations → 50 branches. Adding one more requires editing this block.

**With dispatch table:**

```c
int (*ops[5])(int, int) = {add, sub, mul, divide, mod};

result = ops[choice](a, b);
```

One line. Adding a new operation means appending to the array — the dispatch logic never changes.

This scales beautifully and is the foundation of many systems: virtual function tables (vtables) in C++, opcode dispatch in interpreters, system call tables in operating systems.

---

## 15. Menu-Driven Program with Dispatch Table

Here is a complete, practical example:

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int main(void)
{
    int choice;
    int a = 10, b = 5;
    int result;

    int (*ops[3])(int, int) = {add, sub, mul};
    const char *names[3] = {"Add", "Subtract", "Multiply"};

    printf("Select operation:\n");
    printf("  0 = Add\n");
    printf("  1 = Subtract\n");
    printf("  2 = Multiply\n");
    printf("Choice: ");
    scanf("%d", &choice);

    if (choice >= 0 && choice < 3)
    {
        result = ops[choice](a, b);
        printf("%s(%d, %d) = %d\n", names[choice], a, b, result);
    }
    else
    {
        printf("Invalid choice.\n");
    }

    return 0;
}
```

**Sample run (user enters `2`):**

```
Select operation:
  0 = Add
  1 = Subtract
  2 = Multiply
Choice: 2
Multiply(10, 5) = 50
```

The entire dispatch is `ops[choice](a, b)` — one line. The array index directly selects and invokes the right function. No if-else chain anywhere.

---

## 16. Using `typedef` for Readability

Function pointer syntax quickly becomes unreadable in real code, especially when the same pointer type appears many times. The `typedef` keyword lets you create an alias for the type, hiding the complexity.

**Without typedef:**

```c
int (*fp)(int, int);

int calculate(int x, int y, int (*op)(int, int));

int (*operations[3])(int, int) = {add, sub, mul};
```

**With typedef:**

```c
typedef int (*operation_t)(int, int);

operation_t fp;

int calculate(int x, int y, operation_t op);

operation_t operations[3] = {add, sub, mul};
```

The behavior is identical — the typedef just gives the pointer type a readable name. The `_t` suffix is a common convention for typedef'd types.

### How to Read a Function Pointer typedef

```c
typedef int (*operation_t)(int, int);
```

Read it as: "`operation_t` is a type alias for a pointer to a function that takes two ints and returns an int."

After the typedef, anywhere you would write the full `int (*)(int, int)` type, you can write `operation_t` instead.

### Full Example with typedef

```c
#include <stdio.h>

typedef int (*operation_t)(int, int);

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }

int calculate(int x, int y, operation_t op)
{
    return op(x, y);
}

int main(void)
{
    operation_t fp;

    fp = add;
    printf("add(3, 2) = %d\n", calculate(3, 2, fp));

    fp = sub;
    printf("sub(3, 2) = %d\n", calculate(3, 2, fp));

    return 0;
}
```

---

## 17. Function Pointers Inside Structs

A struct can hold a function pointer as one of its members. This gives structs **behavior** in addition to data — a concept that forms the foundation of object-oriented design in C.

```c
#include <stdio.h>

typedef struct
{
    int a;
    int b;
    int (*operate)(int, int);   /* function pointer member */
} Calculator;

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

int main(void)
{
    Calculator calc;

    calc.a = 10;
    calc.b = 5;

    /* Use add */
    calc.operate = add;
    printf("add: %d\n", calc.operate(calc.a, calc.b));

    /* Switch to mul — same struct, different behavior */
    calc.operate = mul;
    printf("mul: %d\n", calc.operate(calc.a, calc.b));

    return 0;
}
```

**Output:**

```
add: 50
mul: 50
```

Wait — both `10 + 5` and `10 * 5` happen to produce different results, but the point stands: the same `calc` struct produces different behavior depending on which function is assigned to `operate`.

### Why This Pattern Matters

This is how C simulates **methods** in object-oriented programming. If you have ever wondered how C++ implements virtual functions, this is essentially it. A vtable (virtual function table) is an array of function pointers stored inside or alongside an object, allowing different types to respond differently to the same call.

---

## 18. Real-World Example: `qsort` from the Standard Library

The `qsort` function from `<stdlib.h>` is one of the most famous real-world uses of function pointers in C. It sorts any array of any type — because you tell it how to compare elements by passing a comparison function.

**Signature:**

```c
void qsort(void *base, size_t nmemb, size_t size,
           int (*compar)(const void *, const void *));
```

- `base` — pointer to the array
- `nmemb` — number of elements
- `size` — size of each element in bytes
- `compar` — your comparison function

The comparison function must return:
- A **negative number** if the first argument should come first
- **Zero** if they are equal
- A **positive number** if the second argument should come first

### Sorting Integers

```c
#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b)
{
    int x = *(const int *)a;    /* cast void* back to int*, then dereference */
    int y = *(const int *)b;

    return x - y;               /* negative if x < y, 0 if equal, positive if x > y */
}

int main(void)
{
    int arr[] = {4, 1, 3, 2, 5};
    int i;

    qsort(arr, 5, sizeof(int), compare_ints);

    for (i = 0; i < 5; i++)
        printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

**Output:**

```
1 2 3 4 5
```

### Step-by-Step: What `qsort` Does With Your Function Pointer

1. `qsort` receives the address of `compare_ints` as a `void *`-based function pointer
2. Internally, it performs a sorting algorithm (typically quicksort or introsort)
3. Whenever it needs to compare two elements, it calls `compare_ints` via the pointer, passing pointers to the two elements
4. Based on the return value, it decides whether to swap the elements
5. It never knows the type of the data — all it knows is how many bytes each element is and how to compare two of them

This is the perfect demonstration of why function pointers are powerful: `qsort` is written once and works for **any data type** because the comparison logic is injected by the caller.

### Sorting in Descending Order

Simply flip the comparison:

```c
int compare_desc(const void *a, const void *b)
{
    int x = *(const int *)a;
    int y = *(const int *)b;

    return y - x;   /* reversed */
}
```

Pass `compare_desc` to `qsort` and you get `5 4 3 2 1`. No changes to `qsort` needed.

---

## 19. NULL Function Pointers and Safety

A function pointer that has not been assigned a valid function contains either an indeterminate value (if uninitialized) or `NULL` (if explicitly set).

**Calling an uninitialized or NULL function pointer crashes your program** — it is undefined behavior.

Always initialize function pointers to `NULL` when you declare them without an immediate assignment:

```c
int (*fp)(int, int) = NULL;
```

And always check before calling:

```c
if (fp != NULL)
{
    result = fp(10, 5);
}
else
{
    printf("No operation assigned.\n");
}
```

### When NULL Pointers Are Useful

NULL function pointers are a clean way to represent "no behavior registered yet." This is commonly seen in:

- Event systems where handlers are optional
- Plugin interfaces where not every slot needs to be filled
- Structs representing configurable objects

```c
typedef struct
{
    void (*on_start)(void);
    void (*on_stop)(void);
    void (*on_error)(const char *);
} EventHandler;

void run(EventHandler *h)
{
    if (h->on_start) h->on_start();

    /* ... do work ... */

    if (h->on_error) h->on_error("Something failed");
    if (h->on_stop)  h->on_stop();
}
```

Each handler is optional. If the caller does not set it, it stays NULL and `run` gracefully skips it.

---

## 20. Common Mistakes and How to Avoid Them

### Mistake 1: Forgetting the parentheses in the declaration

```c
/* WRONG — this declares a function that returns int* */
int *fp(int, int);

/* CORRECT — this declares a pointer to a function */
int (*fp)(int, int);
```

This is the single most common syntax error with function pointers. The parentheses around `*fp` are not optional.

---

### Mistake 2: Calling an uninitialized pointer

```c
int (*fp)(int, int);   /* declared but not assigned */
fp(1, 2);              /* undefined behavior — likely a crash */
```

Always assign before calling. Initialize to `NULL` immediately:

```c
int (*fp)(int, int) = NULL;
/* ... later, assign it ... */
fp = add;
fp(1, 2);   /* safe */
```

---

### Mistake 3: Calling the function when you mean to assign it

```c
int (*fp)(int, int);

fp = add();   /* WRONG — calls add with no arguments and assigns return value */
fp = add;     /* CORRECT — assigns the address of add */
```

---

### Mistake 4: Mismatched signature — especially with return type

```c
void print(int x) { printf("%d\n", x); }

int (*fp)(int) = print;   /* WRONG — return types differ */
void (*fp)(int) = print;  /* CORRECT */
```

---

### Mistake 5: Forgetting to check for NULL before calling

```c
void run(void (*callback)(void))
{
    callback();   /* crashes if caller passed NULL */
}

/* Safe version: */
void run(void (*callback)(void))
{
    if (callback != NULL)
        callback();
}
```

---

### Mistake 6: Dereferencing confusion

These are all equivalent — pick one style and be consistent:

```c
fp(2, 3);       /* most common */
(*fp)(2, 3);    /* explicit dereference */
(**fp)(2, 3);   /* technically valid but never do this */
```

---

## 21. Mental Model and Memory Diagram

Here is the complete mental model for function pointers:

```
Source code:
    int add(int a, int b) { return a + b; }

Compiled code (in memory, text segment):
    Address 0x401136: [ PUSH rbp | MOV eax, a | ADD eax, b | ... ]

Function pointer:
    int (*fp)(int, int) = add;

    fp variable in memory:
    [ 0x401136 ]
         │
         └──────────────────────────────────┐
                                            ▼
                                  [ add function code ]

Calling through the pointer:
    fp(5, 7)
    ↓
    "go to address stored in fp"
    ↓
    jump to 0x401136
    ↓
    execute add(5, 7)
    ↓
    return 12
```

The CPU does not care whether you wrote `add(5, 7)` or `fp(5, 7)`. Both result in a jump to the same address with the same arguments. The function pointer is just an indirection layer.

---

## 22. Final Combined Example with Walkthrough

This example brings together everything: typedef, array of function pointers, NULL checking, and passing a function pointer to a function.

```c
#include <stdio.h>

typedef int (*operation_t)(int, int);

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int calculate(int x, int y, operation_t op)
{
    if (op == NULL)
    {
        printf("Error: no operation provided.\n");
        return 0;
    }
    return op(x, y);
}

int main(void)
{
    operation_t ops[3] = {add, sub, mul};
    const char *labels[3] = {"Add", "Subtract", "Multiply"};
    int i;

    for (i = 0; i < 3; i++)
    {
        printf("%s(10, 5) = %d\n", labels[i], calculate(10, 5, ops[i]));
    }

    /* Test NULL safety */
    calculate(10, 5, NULL);

    return 0;
}
```

**Output:**

```
Add(10, 5) = 15
Subtract(10, 5) = 5
Multiply(10, 5) = 50
Error: no operation provided.
```

### Walkthrough

| Iteration | `ops[i]` | `calculate` calls | Result |
|-----------|----------|-------------------|--------|
| `i = 0` | address of `add` | `add(10, 5)` | `15` |
| `i = 1` | address of `sub` | `sub(10, 5)` | `5` |
| `i = 2` | address of `mul` | `mul(10, 5)` | `50` |
| NULL test | `NULL` | guard triggers | error message |

The loop body never changes. The dispatch table drives everything.

---

## 23. Interview Questions

**Q: What is a function pointer and why would you use one?**

A: A function pointer stores the address of a function in memory. You use one when you need to select or inject behavior at runtime — for example, to implement callbacks, build dispatch tables, or write generic algorithms like `qsort` that work with any comparison logic.

---

**Q: What is the difference between `int *fp(int, int)` and `int (*fp)(int, int)`?**

A: The first declares a function named `fp` that takes two ints and returns `int *`. The second declares a pointer named `fp` that points to a function taking two ints and returning `int`. The parentheses around `*fp` in the second form force the star to bind to `fp` rather than to the return type.

---

**Q: What happens if you call a NULL function pointer?**

A: Undefined behavior — on virtually all platforms, a segmentation fault (program crash). Always guard with a NULL check before calling a function pointer that might not be assigned.

---

**Q: What is a callback?**

A: A callback is a function passed to another function to be called at a later point, typically when some event or condition occurs. The receiving function stores the pointer and invokes it when appropriate, without knowing in advance which function will be passed.

---

**Q: How does `qsort` work with function pointers?**

A: `qsort` accepts a comparison function pointer with the signature `int (*)(const void *, const void *)`. During sorting, whenever it needs to determine the order of two elements, it calls this function via the pointer, passing pointers to the two elements. The comparison function casts them to the appropriate type and returns negative, zero, or positive to indicate ordering. This makes `qsort` completely type-agnostic.

---

**Q: What is a dispatch table?**

A: An array of function pointers. It maps integer indices to functions, allowing you to select and call the appropriate function with a single array lookup instead of a chain of if-else or switch statements. Used extensively in interpreters, system call tables, and event systems.

---

## 24. Summary and Quick Reference

### Declaration Syntax

```c
return_type (*pointer_name)(param_types);

/* Examples: */
int (*fp)(int, int);          /* takes 2 ints, returns int   */
void (*fp)(char *);           /* takes char*, returns nothing */
double (*fp)(double, int);    /* takes double and int, returns double */
```

### With typedef

```c
typedef return_type (*type_name)(param_types);

typedef int (*operation_t)(int, int);
operation_t fp = add;
```

### The Four Operations

| Operation | Syntax | Notes |
|-----------|--------|-------|
| Declare | `int (*fp)(int, int);` | Do not forget the parentheses around `*fp` |
| Assign | `fp = add;` | Use the function name, not a call |
| Call | `fp(2, 3);` | Exactly like a normal function call |
| NULL check | `if (fp != NULL) fp(2, 3);` | Always guard before calling |

### Common Patterns

| Pattern | What it enables |
|---------|----------------|
| Pass as parameter | Generic functions that accept injected behavior |
| Store in array | Dispatch tables — select behavior by index |
| Store in struct | Objects with configurable methods |
| Check for NULL | Optional callbacks and safe plugin interfaces |

### Signature Matching Rules

| Component | Must match? |
|-----------|-------------|
| Return type | Yes |
| Number of parameters | Yes |
| Type of each parameter | Yes |
| Parameter names | No (names are irrelevant to the pointer) |