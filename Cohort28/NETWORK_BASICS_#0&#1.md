# Networking Basics #0
# Networking Detective Lab
### Interactive PLD Presentation
### Holberton School

---

# Slide 1
# Networking Detective Lab

## Networking Basics #0

### Mission:
Discover how computers communicate.

---

# Slide 2
# Today's Goal

By the end of this session you should be able to explain:

✅ What a network is

✅ What an IP address is

✅ What a MAC address is

✅ What localhost is

✅ What a server is

✅ What a port is

✅ LAN vs WAN

✅ TCP vs UDP

✅ How computers communicate

---

# Slide 3
# Warm-Up Question

## How many of you used the Internet today?

🙋

---

## Follow-up Question

How many of you know exactly what happened between:

Your Laptop

↓

Your Router

↓

Your ISP

↓

Google?

---

### Key Idea

Today we are going to discover that process ourselves.

---

# Slide 4
# Mission 1
## Who Am I On The Network?

Run:

```bash
ip addr
```

Find:

1. Your IP Address
2. Your MAC Address
3. Your Interface Name

---

## What Are We Looking At?

Every device connected to a network needs an identity.

Think about your home address:

```text
123 Main Street
```

Without an address:

- Mail cannot be delivered
- Packages cannot arrive
- Nobody knows where you are

Computers have the same problem.

---

### Question

Why would computers need addresses?

---

### Answer

So data knows exactly where it needs to go.

---

### Key Takeaway

An address allows devices to find each other.

---

# Slide 5
# IP Address

Look for something like:

```text
192.168.1.10
```

or

```text
10.0.0.25
```

---

## What Is An IP Address?

IP stands for:

**Internet Protocol**

An IP Address is:

> A unique logical address assigned to a device on a network.

---

### Real Life Analogy

| Real Life | Networking |
|------------|------------|
| House Address | IP Address |

---

### Example

```text
192.168.1.10
```

means:

"This specific computer on this network."

---

### Key Takeaway

IP Addresses tell data where to go.

---

# Slide 6
# MAC Address

Look for something like:

```text
00:1A:2B:3C:4D:5E
```

---

## What Is A MAC Address?

MAC stands for:

**Media Access Control**

A MAC Address is:

> The physical address of your network card.

---

### Think Of It Like

IP Address:

```text
Your home address
```

MAC Address:

```text
Your social security number
```

or

```text
A serial number
```

---

### Important Difference

| IP | MAC |
|-----|-----|
| Logical | Physical |
| Can Change | Usually Permanent |
| Layer 3 | Layer 2 |

---

### Key Takeaway

IP identifies location.

MAC identifies hardware.

---

# Slide 7
# What Is A Network?

A Network is:

> Two or more devices connected together so they can exchange information.

---

### Examples

- Home WiFi
- School Network
- Office Network
- The Internet

---

### Visual

```text
Laptop
   \
Phone ---- Router
   /
Printer
```

All devices can communicate.

---

### Key Takeaway

A network exists whenever devices can exchange data.

---

# Slide 8
# Mission 2
## Can We Reach The Internet?

Run:

```bash
ping google.com -c 4
```

---

### Question

What happened?

What information do you see?

---

# Slide 9
# What Is Ping?

Ping asks:

```text
Hello?
Are you there?
```

---

Google replies:

```text
Yes.
I am here.
```

---

### What Ping Measures

- Connectivity
- Reachability
- Response Time

---

### Example Output

```text
64 bytes from ...
time=15ms
```

---

### Key Takeaway

Ping verifies whether another device can be reached.

---

# Slide 10
# ICMP

Ping uses a protocol called:

## ICMP

Internet Control Message Protocol

---

### Purpose

ICMP is used for:

- Diagnostics
- Troubleshooting
- Connectivity Testing

---

### Not Used For

❌ Websites

❌ Videos

❌ Games

---

### Used For

✅ Testing connections

---

# Slide 11
# Mission 3
## Talk To Yourself

Run:

```bash
ping localhost -c 4
```

Then:

```bash
ping 127.0.0.1 -c 4
```

---

### Question

Why is localhost so fast?

---

# Slide 12
# What Is Localhost?

Localhost means:

```text
THIS COMPUTER
```

---

Its address is:

```text
127.0.0.1
```

---

This is called:

## The Loopback Address

---

### Key Takeaway

Localhost is your own machine.

---

# Slide 13
# What Does Loopback Mean?

Google:

```text
You
↓
Router
↓
ISP
↓
Internet
↓
Google
```

---

Localhost:

```text
You
↓
You
```

---

The packet never leaves your computer.

---

### Key Takeaway

Localhost allows software to communicate with itself.

---

# Slide 14
# Why Developers Use Localhost

Examples:

React:

```text
localhost:3000
```

Flask:

```text
localhost:5000
```

Node:

```text
localhost:3000
```

MySQL:

```text
localhost:3306
```

---

### Key Takeaway

Developers use localhost every day.

---

# Slide 15
# Mission 4
## Become A Server

Run:

```bash
python3 -m http.server 8000
```

---

### Question

What changed?

---

# Slide 16
# What Just Happened?

You created:

## A Web Server

---

### What Is A Server?

A Server is:

> A program waiting for requests.

---

### Common Misconception

A server is NOT:

❌ A giant computer

A server IS:

✅ Software waiting for connections

---

### Examples

- Google
- YouTube
- Discord
- Databases

---

# Slide 17
# What Is Port 8000?

Command:

```bash
python3 -m http.server 8000
```

---

What does:

```text
8000
```

mean?

---

# Slide 18
# What Is A Port?

Think of an apartment building.

---

Address:

```text
123 Main Street
```

gets you to the building.

---

Apartment:

```text
301
```

gets you to the correct room.

---

Networking works exactly the same way.

---

# Slide 19
# IP vs Port

IP Address:

```text
Which Computer?
```

Example:

```text
192.168.1.10
```

---

Port:

```text
Which Application?
```

Example:

```text
8000
```

---

Combined:

```text
192.168.1.10:8000
```

---

### Key Takeaway

IP = Computer

Port = Application

---

# Slide 20
# Common Ports

| Service | Port |
|----------|-------|
| SSH | 22 |
| HTTP | 80 |
| HTTPS | 443 |
| DNS | 53 |
| MySQL | 3306 |
| Python Server | 8000 |

---

# Slide 21
# Open The Browser

Visit:

```text
http://localhost:8000
```

---

### Question

What happened?

---

### Explanation

Browser:

1. Sent a request
2. Server received it
3. Server responded

---

Networking just happened.

---

# Slide 22
# Mission 5
## Connect To Another Student

Find your IP:

```bash
ip addr
```

---

Partner visits:

```text
http://YOUR-IP:8000
```

---

# Slide 23
# Stop And Think

What just happened?

---

Your classmate connected to:

### YOUR COMPUTER

---

### Why Did It Work?

Because:

- Both devices are on the same network
- They know each other's IP
- Port 8000 is listening
- A server is running

---

# Slide 24
# Client vs Server

Student A:

SERVER

---

Student B:

CLIENT

---

Relationship:

```text
Client
↓ Request
Server
↓ Response
Client
```

---

### Key Takeaway

The client asks.

The server answers.

---

# Slide 25
# What Is A LAN?

LAN:

## Local Area Network

---

Examples:

- Home
- School
- Office
- Classroom

---

### Characteristics

- Small area
- Fast
- Private

---

# Slide 26
# LAN Diagram

```text
Laptop
   \
Phone ---- Router
   /
Printer
```

---

All devices are nearby.

---

# Slide 27
# What Is A WAN?

WAN:

## Wide Area Network

---

Connects multiple LANs together.

---

### Example

```text
Puerto Rico
     |
Miami|
     |
New York
```

---

# Slide 28
# The Internet

The Internet is:

> A Network of Networks

---

Thousands of LANs

Connected by WANs

Working together

---

### Key Takeaway

The Internet is the largest network ever created.

---

# Slide 29
# TCP

Question:

What if half a webpage arrived?

Would the page work?

---

Usually:

No.

---

# Slide 30
# What Is TCP?

TCP stands for:

Transmission Control Protocol

---

TCP guarantees:

✅ Delivery

✅ Correct Order

✅ Error Checking

---

### Analogy

Certified Mail

You know it arrived.

---

# Slide 31
# UDP

UDP stands for:

User Datagram Protocol

---

UDP prioritizes:

⚡ Speed

instead of

✅ Reliability

---

### Examples

- Gaming
- Streaming
- Voice Calls

---

### Analogy

Shouting across a room.

---

# Slide 32
# The OSI Model

Everything we did today fits into layers.

---

```text
Application
Transport
Network
Data Link
Physical
```

---

# Slide 33
# OSI Example

When your partner loaded your webpage:

Application → Browser

Transport → TCP

Network → IP

Data Link → MAC

Physical → WiFi

---

### Key Takeaway

The OSI Model organizes networking responsibilities into layers.

---

# Slide 34
# Review Challenge

Explain:

1. What is an IP Address?
2. What is a MAC Address?
3. What is localhost?
4. What is a server?
5. What is a port?
6. What is a LAN?
7. What is TCP?

---

# Slide 35
# Final Takeaway

Networking Is Not Magic.

It Is Simply:

💻 Devices

📍 Addresses

📦 Data

📡 Communication Rules

Working Together

To Move Information Around The World.

---