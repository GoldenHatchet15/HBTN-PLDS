# Networking Basics #0



## Mission
Discover how computers communicate by investigating your own machine, creating a server, and connecting to other devices.



# Today's Goal

By the end of this session you should be able to explain:

- What a network is
- What an IP address is
- What a MAC address is
- What localhost is
- What a server is
- What a port is
- What a LAN is
- What a WAN is
- What TCP and UDP are
- How computers communicate

---

# Warm-Up Question

How many of you used the Internet today?

Now ask yourself:

How did data travel between your computer and Google?

Today we will discover the answer.

---

# Mission 1: Who Am I On The Network?

Run:

```bash
ip addr or ifconfig
```

Find:

1. Your IP Address
2. Your MAC Address
3. Your Interface Name

## What Are We Looking At?

Every device connected to a network needs an identity.

Think about your home address.

Without an address:
- Mail cannot arrive
- Packages cannot be delivered
- Nobody knows where you are

Computers work exactly the same way.

---

# IP Address

Example:

```text
192.168.1.10
```

## What Is An IP Address?

IP stands for Internet Protocol.

An IP address is a unique logical address assigned to a device on a network.

### Analogy

| Real Life | Networking |
|------------|------------|
| House Address | IP Address |

### Key Takeaway

IP addresses tell information where it needs to go.

---

# MAC Address

Example:

```text
00:1A:2B:3C:4D:5E
```

## What Is A MAC Address?

MAC stands for Media Access Control.

A MAC address is the physical address of a network card.

### MAC vs IP

| IP Address | MAC Address |
|------------|-------------|
| Logical | Physical |
| Can Change | Usually Permanent |
| Layer 3 | Layer 2 |

### Key Takeaway

IP identifies location.
MAC identifies hardware.

---

# What Is A Network?

A network is:

> Two or more devices connected together so they can exchange information.

Examples:

- Home WiFi
- School Network
- Office Network
- Internet

---

# Mission 2: Can We Reach The Internet?

Run:

```bash
ping google.com -c 4
```

## What Is Ping?

Ping asks:

"Hello, are you there?"

The destination responds:

"Yes, I am here."

### What Ping Measures

- Connectivity
- Reachability
- Response Time

---

# ICMP

Ping uses ICMP:

Internet Control Message Protocol

Used for:
- Diagnostics
- Troubleshooting
- Connectivity testing

---

# Mission 3: Talk To Yourself

Run:

```bash
ping localhost -c 4
```

Then:

```bash
ping 127.0.0.1 -c 4
```

## What Is Localhost?

Localhost means:

```text
THIS COMPUTER
```

Address:

```text
127.0.0.1
```

This is called the Loopback Address.

### Why Is It Fast?

Google:

You → Router → ISP → Internet → Google

Localhost:

You → You

The packet never leaves your machine.

---

# Why Developers Use Localhost

Examples:

- React → localhost:3000
- Flask → localhost:5000
- Node.js → localhost:3000
- MySQL → localhost:3306

---

# Mission 4: Become A Server

Run:

```bash
python3 -m http.server 8000
```

## What Just Happened?

You created a web server.

### What Is A Server?

A server is:

> A program waiting for requests.

Servers are not necessarily giant computers.

Examples:

- Google
- YouTube
- Discord
- Databases

---

# What Is Port 8000?

The number 8000 is a port.

## What Is A Port?

Think of an apartment building.

Address:
123 Main Street

Apartment:
301

The address gets you to the building.
The apartment gets you to the correct room.

Networking works the same way.

---

# IP vs Port

IP Address:

Which computer?

Port:

Which application?

Example:

```text
192.168.1.10:8000
```

Means:

Computer 192.168.1.10
Application listening on port 8000

---

# Common Ports

| Service | Port |
|----------|------|
| SSH | 22 |
| HTTP | 80 |
| HTTPS | 443 |
| DNS | 53 |
| MySQL | 3306 |
| Python Server | 8000 |

---

# Open The Browser

Visit:

```text
http://localhost:8000
```

What happened?

The browser sent a request.
The server received the request.
The server responded.

Networking just happened.

---

# Mission 5: Connect To Another Student

Find your IP:

```bash
ip addr or ifconfig
```

Have a partner connect to:

```text
http://YOUR-IP:8000
```

---

# Client vs Server

Student A:

SERVER

Student B:

CLIENT

Relationship:

Client → Request → Server

Server → Response → Client

### Key Takeaway

The client asks.
The server answers.

---

# What Is A LAN?

LAN = Local Area Network

Examples:

- Home
- School
- Office
- Classroom

Characteristics:

- Small area
- Fast
- Private

---

# LAN Diagram

```text
Laptop
   \
Phone ---- Router
   /
Printer
```

---

# What Is A WAN?

WAN = Wide Area Network

A WAN connects multiple LANs together.

Example:

Puerto Rico ↔ Miami ↔ New York

---

# The Internet

The Internet is:

> A network of networks.

Thousands of LANs connected through WANs.

---

# TCP

Question:

What if half a webpage arrived?

Would the page work?

Probably not.

## What Is TCP?

TCP stands for Transmission Control Protocol.

TCP guarantees:

- Delivery
- Correct Order
- Error Checking

Analogy:

Certified mail.

---

# UDP

UDP stands for User Datagram Protocol.

UDP prioritizes:

- Speed

Instead of:

- Reliability

Examples:

- Gaming
- Streaming
- Voice Calls

Analogy:

Shouting across a room.

---

# The OSI Model

Networking responsibilities are organized into layers.

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

---

# OSI Example

When your partner loaded your webpage:

Application → Browser

Transport → TCP

Network → IP

Data Link → MAC

Physical → WiFi

---

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

# Final Takeaway

Networking is not magic.

It is simply:

- Devices
- Addresses
- Data
- Communication Rules

Working together to move information around the world.
