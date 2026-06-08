# 🎉 FINAL PLD FACILITATOR GUIDE

# Looking Back, Building Forward

**Audience:** Final Cohort Session
**Duration:** 90–120 Minutes
**Facilitator:** Raphael Santos

---

# BEFORE THE SESSION

## Goal

This is NOT another lecture.

This is NOT another project.

This is NOT another technical interview.

This session should feel like:

* A celebration
* A reminder of how much they've learned
* A final opportunity to build something
* A chance to reflect on their journey

Students will remember this PLD far longer than they will remember another technical explanation.

---

# SCHEDULE

| Activity              | Time      |
| --------------------- | --------- |
| Opening               | 5 min     |
| Fix My Code Challenge | 15–20 min |
| Build Your Own Tool   | 30 min    |
| Journey of a Request  | 20–25 min |
| Reflection Circle     | 30–45 min |
| Closing               | 5 min     |

---

# OPENING

## Duration: 5 Minutes

## What To Say

Good morning everyone.

Today is a little different.

This is our last PLD together.

Today is not about checkers.

Today is not about projects.

Today is not about grades.

Today is about looking back and realizing how far you've come.

A few months ago many of you:

* Had never used Linux
* Didn't know Git
* Didn't know networking
* Didn't know how websites worked
* Had never built an application

Today those things are normal conversations for you.

Let's celebrate that.

---

# PART 1 — FIX MY CODE CHALLENGE

## Duration: 15–20 Minutes

---

# Instructor Note

One of the biggest misconceptions about software engineering is:

> Programmers spend all day writing code.

Reality:

Most developers spend more time:

* Reading code
* Debugging code
* Understanding code

Than writing new code.

Today's challenge demonstrates exactly that.

---

# Challenge 1

```python
def average(numbers):
    total = 0

    for n in numbers:
        total + n

    return total / len(numbers)
```

---

## Ask

What is this code trying to do?

Expected Answer:

Calculate the average.

---

What is wrong?

Expected Answer:

```python
total + n
```

doesn't save the result.

Should be:

```python
total += n
```

---

## Teaching Note

Many students focus on syntax.

This bug is about logic.

The code runs.

The code is wrong.

That distinction is important.

---

# Challenge 2

```python
def greet(name):
    print("Hello " + Name)

greet("Raphael")
```

---

## Ask

Will this run?

Why not?

Expected Answer:

NameError

Python is case-sensitive.

---

## Teaching Note

Reinforce:

```python
name
```

and

```python
Name
```

are different variables.

---

# Challenge 3

```c
int age;

printf("%d\n", age);
```

---

## Ask

Will this compile?

Yes.

Will it behave correctly?

No.

---

## Explanation

age contains garbage data.

Local variables are not initialized automatically.

---

## Common Question

Why does it sometimes print 0?

Answer:

Coincidence.

The memory happened to contain 0.

Never rely on it.

---

# Challenge 4

```c
char *str;

strcpy(str, "Hello");
```

---

## Ask

What happens?

---

Expected Answer

Potential segmentation fault.

---

## Explanation

Memory was never allocated.

str points nowhere useful.

You are trying to write into memory that does not belong to you.

---

## Real Life Analogy

Imagine writing a letter to a house that doesn't exist.

The mail has nowhere valid to go.

---

# Challenge 5

A user can visit:

```text
142.250.191.14
```

But cannot visit:

```text
google.com
```

---

## Ask

What is the likely issue?

Expected Answer:

DNS

---

# Challenge 6

Student runs:

```bash
git push
```

and gets rejected.

---

## Ask

Possible reasons?

Expected Answers

* Remote has new commits
* Need git pull first
* Wrong branch
* Permission issue

---

# Debrief

Ask:

What was harder?

Writing code?

Or understanding someone else's code?

Most professional developers spend more time reading code than writing it.

---

# PART 2 — BUILD YOUR OWN TOOL

## Duration: 30 Minutes

---

# Instructor Introduction

Now it's your turn.

You're going to build something useful.

Not because someone assigned it.

Not because there's a checker.

Not because there's a deadline.

Simply because you can.

---

# Project Options

Students choose ONE.

* PDF Merger
* YouTube Downloader
* Password Generator
* QR Code Generator
* File Organizer
* URL Shortener
* Text Statistics Tool

---

# Instructions

Work individually or in pairs.

Goal:

Build a working version.

Not a perfect version.

---

# What To Say

Remember:

Software engineering is not:

"Can I build the perfect version?"

It's:

"Can I build a working version?"

---

# Demo Session

Select 2–3 volunteers.

Applaud every demo.

Celebrate effort.

Not perfection.

---

# PART 3 — THE JOURNEY OF A REQUEST

## Duration: 20–25 Minutes

---

# Introduction

Tell students:

For the next few minutes...

YOU are the request.

You just typed:

```text
https://www.google.com
```

and pressed Enter.

What happens now?

Let's find out.

---

# STEP 1 — DNS

## "I don't know where Google lives"

---

# What To Say

Computers don't understand:

```text
google.com
```

Computers communicate using:

```text
142.250.x.x
```

IP addresses.

The first problem is:

How do we find Google's IP address?

---

# DNS

DNS stands for:

Domain Name System.

DNS is the Internet's phonebook.

---

# Real-Life Analogy

Ask:

How many of you know your mother's name?

Everyone raises their hand.

Ask:

How many know her phone number from memory?

Far fewer.

Humans remember names.

Computers remember numbers.

DNS translates between them.

---

# DNS Lookup Process

Explain:

Browser checks cache.

↓

Operating system checks cache.

↓

Router checks cache.

↓

ISP DNS checks cache.

↓

Root DNS server.

↓

TLD DNS server.

↓

Authoritative DNS server.

↓

IP address returned.

---

# Common Student Question

Why not one giant DNS server?

---

# Answer

Too much traffic.

Too slow.

Single point of failure.

Distributed systems scale better.

---

# Key Takeaway

DNS translates names into IP addresses.

---

# STEP 2 — TCP

## "How do I know my message arrives?"

---

# What To Say

Now we know Google's address.

How do we communicate reliably?

TCP.

Transmission Control Protocol.

---

# TCP Provides

* Reliability
* Ordering
* Error Checking

---

# Analogy

Certified Mail.

You want confirmation the package arrived.

---

# Three-Way Handshake

Draw:

Client → SYN → Server

Client ← SYN ACK ← Server

Client → ACK → Server

---

# Translation

SYN:

"Can we talk?"

SYN ACK:

"Yes."

ACK:

"Great."

---

# Common Student Question

Why not send data immediately?

Answer:

Need confirmation.

Need synchronization.

Need both sides ready.

---

# STEP 3 — HTTPS / TLS

## "How do I know this is really Google?"

---

# Ask

What if someone pretends to be Google?

---

# Introduce

TLS Certificate.

Digital identity card.

---

# Real Life Analogy

Passport.

Driver's License.

Government ID.

---

# HTTPS Provides

Authentication

Who are you?

Encryption

Can anyone read this?

Integrity

Was anything modified?

---

# Without HTTPS

* Password theft
* Credit card theft
* Session hijacking

---

# STEP 4 — FIREWALL

---

# What To Say

Traffic reaches Google's network.

The firewall acts like security at a building.

---

# Responsibilities

Allow traffic.

Block traffic.

Inspect traffic.

---

# Ask

What port does HTTPS use?

Answer:

443

---

# STEP 5 — LOAD BALANCER

## "Google has billions of users"

---

# Ask

Could one computer serve the entire Internet?

No.

---

# Load Balancer

Distributes requests among multiple servers.

---

# Analogy

Airport check-in counters.

One employee directs people to different lines.

---

# Common Student Question

What happens if a server dies?

Answer:

Load balancer sends traffic elsewhere.

---

# Introduce

Redundancy

Having backups available.

---

# Introduce

SPOF

Single Point Of Failure.

---

# Ask

What happens if we only have one server?

Students should identify SPOF.

---

# STEP 6 — WEB SERVER

Examples:

Apache

Nginx

---

# Responsibilities

Receive requests.

Serve static files.

Forward dynamic requests.

---

# Ask

What is a static file?

Expected Answers

* HTML
* CSS
* Images
* JavaScript

---

# STEP 7 — APPLICATION SERVER

---

# What To Say

This is where the actual code runs.

Examples:

* Python
* NodeJS
* Java
* PHP

---

# Example

User logs in.

Application checks:

* Username
* Password
* Permissions

---

# Key Idea

Web Server receives.

Application Server thinks.

---

# STEP 8 — DATABASE

---

# Ask

Where does Google store:

Emails?

Accounts?

Search history?

---

Expected Answer

Database.

---

# Examples

MySQL

PostgreSQL

MongoDB

---

# Key Idea

Database = Long-Term Memory

---

# Ask

What happens if the database dies?

Possible Answers

* Errors
* Missing data
* Application failure

---

# STEP 9 — MONITORING

---

# Ask

How do engineers know a server crashed at 3 AM?

---

# Monitoring

Examples:

* Grafana
* Prometheus
* Datadog

---

# Metrics

CPU

RAM

Disk

Network

Errors

---

# Final Architecture Diagram

Draw:

Browser

↓

DNS

↓

IP Address

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

---

# Final Question

Could Day-One You explain any of this?

Most students answer:

No.

That's how much you've grown.

---

# PART 4 — REFLECTION CIRCLE

## Duration: 30–45 Minutes

---

# Instructor Note

This is the most important part.

Do not rush it.

If you're behind schedule:

Cut technical discussion.

Do not cut reflection.

---

# Ground Rules

Everyone speaks.

No interruptions.

No judging.

No rushing.

---

# Question 1

Who were you when you arrived at Holberton?

---

# Question 2

Did you think you would make it this far?

Why or why not?

---

# Question 3

What was the hardest moment?

Possible examples:

* Shell
* Pointers
* React
* Docker
* Time management
* Personal struggles

---

# Question 4

What project are you most proud of?

Why?

---

# Question 5

What can you do today that Day-One You would find impressive?

---

# Question 6

What advice would you give future students?

---

# Question 7

Where do you see yourself one year from now?

---

# Facilitator Tip

Allow silence.

Some students need time to think.

Silence is not a problem.

---

# CLOSING

Look around the room.

These people shared this journey with you.

You struggled together.

You learned together.

You succeeded together.

Many people start.

Not everyone finishes.

You did.

Congratulations.

Be proud of yourselves.

🎉 You earned it. 🎉
