# 🎉 FINAL PLD SESSION

# Looking Back, Building Forward

---

# Slide 1

# 🎉 Final PLD Session

## Looking Back, Building Forward

### Today's Goal

Today is not another project.

Today is not another checker.

Today is not another technical interview.

Today is a chance to:

✅ Build something

✅ Debug something

✅ Reflect on how much you've learned

✅ Celebrate the journey

---

### Think About This

A few months ago...

* Linux was new
* Git was confusing
* Networking sounded complicated
* Building an application seemed impossible

Today?

You do those things regularly.

Let's see how far we've come.

---

# Slide 2

# Today's Mission

### Part 1

🐛 Fix My Code Challenge

---

### Part 2

🛠 Build Your Own Tool

---

### Part 3

🌐 The Journey of a Request

---

### Part 4

🎓 Reflection Circle

---

# PART 1

# FIX MY CODE CHALLENGE

---

# Slide 3

# Why Are We Doing This?

### Reality Check

Many people think software engineers spend all day writing code.

Reality:

Most engineers spend their time:

* Reading code
* Understanding code
* Fixing code
* Debugging code

---

### Discussion

❓ Which is harder?

Writing your own code?

Or understanding someone else's?

---

### Key Takeaway

Being a great developer means becoming a great debugger.

---

# Slide 4

# Challenge #1

```python
def average(numbers):
    total = 0

    for n in numbers:
        total + n

    return total / len(numbers)
```

---

### Questions

1. What is this code trying to do?

2. What is wrong?

3. Why doesn't it work?

4. How would you fix it?

---

### Hint

Look carefully inside the loop.

---

# Slide 5

# Challenge #1 Solution

### The Bug

```python
total + n
```

Calculates a value.

But never saves it.

---

### Fix

```python
total += n
```

---

### Discussion

Why is this bug dangerous?

Because the program runs.

No error appears.

But the result is wrong.

---

### Key Takeaway

Not every bug crashes your program.

Some bugs silently produce incorrect results.

---

# Slide 6

# Challenge #2

```python
def greet(name):
    print("Hello " + Name)

greet("Raphael")
```

---

### Questions

What error appears?

Why?

---

### Hint

Python is case-sensitive.

---

# Slide 7

# Challenge #2 Solution

### Problem

```python
name
```

and

```python
Name
```

are different variables.

---

### Result

Python raises:

```python
NameError
```

---

### Key Takeaway

Programming languages are very literal.

Small details matter.

---

# Slide 8

# Challenge #3

```c
int age;

printf("%d\n", age);
```

---

### Questions

Will this compile?

Will it always work correctly?

---

### Think

What value does age contain?

---

# Slide 9

# Challenge #3 Solution

### Explanation

Local variables are NOT automatically initialized.

The variable may contain:

```text
0
14
999
-2389
```

Anything.

---

### Why?

Because memory already contains old data.

---

### Key Takeaway

Never assume variables contain safe values.

Initialize them.

---

# Slide 10

# Challenge #4

```c
char *str;

strcpy(str, "Hello");
```

---

### Questions

Why might this crash?

What memory are we writing into?

---

# Slide 11

# Challenge #4 Solution

### Problem

Memory was never allocated.

```c
char *str;
```

points nowhere useful.

---

### Analogy

Imagine mailing a package to a house that doesn't exist.

The package has nowhere valid to go.

---

### Result

Possible:

💥 Segmentation Fault

---

# Slide 12

# Challenge #5

A user can access:

```text
142.250.191.14
```

But cannot access:

```text
google.com
```

---

### Discussion

What is the most likely issue?

---

### Hint

What converts names into addresses?

---

# Slide 13

# Challenge #5 Solution

### Answer

DNS

Domain Name System

---

### Why?

The user can reach the destination.

But cannot translate:

```text
google.com
```

into an IP address.

---

### Key Takeaway

DNS is the Internet's phonebook.

---

# PART 2

# BUILD YOUR OWN TOOL

---

# Slide 14

# Build Something Useful

### Your Mission

Build ONE useful tool.

Not because you have to.

Because you can.

---

### Goal

Create the simplest working version.

Remember:

Done > Perfect

---

# Slide 15

# Project Ideas

Choose ONE

📄 PDF Merger

🎥 YouTube Downloader

🔒 Password Generator

📱 QR Generator

📁 File Organizer

🔗 URL Shortener

📊 Text Statistics Tool

---

### Time Limit

30 Minutes

---

# Slide 16

# During Development

Ask Yourself

### What is the smallest version that works?

Example:

Password Generator

Version 1:

Generate 8 random characters.

Done.

Mission accomplished.

---

### Key Takeaway

Software is built incrementally.

---

# PART 3

# THE JOURNEY OF A REQUEST

---

# Slide 17

# You Are The Request

Imagine you type:

```text
https://www.google.com
```

and press Enter.

---

### Question

What happens next?

---

### Today's Goal

Follow the request from your browser all the way to Google's servers.

---

# Slide 18

# Step 1 — DNS

## "I Don't Know Where Google Lives"

---

### Problem

Humans understand:

```text
google.com
```

Computers understand:

```text
142.250.x.x
```

---

### What DNS Does

DNS translates:

```text
google.com
```

↓

```text
142.250.x.x
```

---

### Real-Life Analogy

DNS is your phone contacts.

You remember:

Mom

Your phone remembers:

(787) XXX-XXXX

---

### Key Takeaway

DNS translates names into IP addresses.

---

# Slide 19

# Step 2 — TCP

## "How Do I Know My Message Arrives?"

---

### What TCP Provides

✅ Reliability

✅ Ordering

✅ Error Checking

---

### Analogy

Certified Mail

You want confirmation your package arrived.

---

### Three-Way Handshake

```text
Client -> SYN -> Server

Client <- SYN ACK <- Server

Client -> ACK -> Server
```

---

### Translation

SYN

"Can we talk?"

SYN-ACK

"Yes."

ACK

"Great."

---

### Key Takeaway

TCP guarantees reliable communication.

---

# Slide 20

# Step 3 — HTTPS

## "How Do I Know This Is Really Google?"

---

### Problem

What if someone pretends to be Google?

---

### Solution

TLS Certificates

Digital Identity Cards

---

### HTTPS Provides

🔒 Encryption

🪪 Authentication

✅ Integrity

---

### Without HTTPS

* Password theft
* Data interception
* Identity theft

---

### Key Takeaway

HTTPS protects your data.

---

# Slide 21

# Step 4 — Firewall

---

### What Does A Firewall Do?

Acts like security at a building.

---

### Responsibilities

Allow traffic

Block traffic

Inspect traffic

---

### Common Port

HTTPS:

```text
443
```

---

### Key Takeaway

Firewalls help protect networks.

---

# Slide 22

# Step 5 — Load Balancer

---

### Problem

Google has billions of users.

Can one server handle all of them?

No.

---

### What A Load Balancer Does

Distributes requests across servers.

---

```text
User
 ↓
Load Balancer
 ↓
 ├─ Server A
 ├─ Server B
 └─ Server C
```

---

### Analogy

Airport check-in desk.

---

### Key Takeaway

Load balancers improve performance and reliability.

---

# Slide 23

# Step 6 — Web Server

---

### Examples

Apache

Nginx

---

### Responsibilities

Receive requests

Serve static files

Forward dynamic requests

---

### Static Files

* HTML
* CSS
* JavaScript
* Images

---

### Key Takeaway

Web servers receive requests.

---

# Slide 24

# Step 7 — Application Server

---

### What Happens Here?

The application's logic runs.

---

### Examples

Python

NodeJS

Java

PHP

---

### Example

User logs in.

Application checks:

* Username
* Password
* Permissions

---

### Key Takeaway

Application servers make decisions.

---

# Slide 25

# Step 8 — Database

---

### What Is Stored Here?

* Accounts
* Emails
* Search History
* Products

---

### Examples

MySQL

PostgreSQL

MongoDB

---

### Think About It

What happens if the database crashes?

---

### Key Takeaway

Databases are the application's memory.

---

# Slide 26

# Step 9 — Monitoring

---

### Question

How do engineers know a server crashed at 3 AM?

---

### Monitoring Tools

Grafana

Prometheus

Datadog

---

### What Is Monitored?

CPU

RAM

Disk

Network

Errors

---

### Key Takeaway

Monitoring helps detect problems before users do.

---

# Slide 27

# Full Journey

```text
Browser
 ↓
DNS
 ↓
TCP
 ↓
HTTPS
 ↓
Firewall
 ↓
Load Balancer
 ↓
Web Server
 ↓
Application Server
 ↓
Database
 ↓
Response
```

---

### Discussion

Could Day-One You explain this diagram?

---

### Think About It

Look how much you've learned.

---

# PART 4

# REFLECTION CIRCLE

---

# Slide 28

# Reflection Question #1

### Think About Day One

Who were you when you started?

---

### Discussion

What were you feeling?

* Nervous?
* Excited?
* Overwhelmed?
* Confused?

---

# Slide 29

# Reflection Question #2

Did you honestly think you would make it this far?

Why?

Why not?

---

### Take Your Time

There is no wrong answer.

---

# Slide 30

# Reflection Question #3

What was the hardest moment of your journey?

Examples:

* Simple Shell
* Pointers
* React
* Docker
* Time Management

---

# Slide 31

# Reflection Question #4

What project are you most proud of?

Why?

---

### Think Beyond Grades

What made YOU proud?

---

# Slide 32

# Reflection Question #5

What can you do today that Day-One You would find impressive?

---

### Examples

Build APIs

Use Linux

Debug code

Explain networking

Build full-stack applications

---

# Slide 33

# Reflection Question #6

What advice would you give future students?

---

### If You Could Go Back

What would you tell yourself?

---

# Slide 34

# Reflection Question #7

Where do you see yourself one year from now?

---

### Think Big

Developer?

Freelancer?

Startup Founder?

DevOps Engineer?

Full Stack Engineer?

---

# Slide 35

# Final Message

Look around the room.

These are the people who shared this journey with you.

You struggled together.

You learned together.

You succeeded together.

---

### Remember

Many people start.

Not everyone finishes.

You did.

---

# 🎉 Congratulations Cohort 🎉

You earned it.
