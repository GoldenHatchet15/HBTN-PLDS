# Networking Basics — PLD Lecture
**Beginner-Friendly Deep Dive**
*Based on Holberton School – Networking Basics #0 and #1*

---

## Table of Contents
1. [Introduction to Networking](#1-introduction-to-networking)
2. [What is a Network?](#2-what-is-a-network)
3. [Types of Networks: LAN, WAN, Internet](#3-types-of-networks-lan-wan-internet)
4. [The OSI Model](#4-the-osi-model)
5. [IP Addresses](#5-ip-addresses)
6. [Public vs Private IP Addresses](#6-public-vs-private-ip-addresses)
7. [IPv4 vs IPv6](#7-ipv4-vs-ipv6)
8. [Localhost and 0.0.0.0](#8-localhost-and-00000)
9. [Subnets](#9-subnets)
10. [MAC Addresses](#10-mac-addresses)
11. [TCP vs UDP](#11-tcp-vs-udp)
12. [Ports](#12-ports)
13. [Ping and ICMP](#13-ping-and-icmp)
14. [The /etc/hosts File](#14-the-etchosts-file)
15. [Network Interfaces](#15-network-interfaces)
16. [Essential Networking Commands](#16-essential-networking-commands)
17. [Bash Script Requirements](#17-bash-script-requirements)
18. [Practice Exercises](#18-practice-exercises)
19. [Summary Cheat Sheet](#19-summary-cheat-sheet)

---

## 1. Introduction to Networking

Before two computers can exchange a single byte, they need a shared set of rules. Networking is that system of rules — it defines how devices find each other, how data gets packaged and sent, and how the receiving end knows what to do with what arrives.

Every time you do any of the following, networking is happening under the hood:

| Action | What's happening |
|---|---|
| Opening a website | Your browser fetches files from a remote server |
| Sending a Discord message | Your client connects to Discord's servers via TCP |
| Watching YouTube | Video data streams to you via the internet |
| SSH into a server | A secure encrypted tunnel opens over port 22 |
| Printing a file | Your laptop finds the printer on the local network |

Networking is not magic — it is a well-organized stack of rules called **protocols**. Everything in this lecture is just learning those rules.

---

## 2. What is a Network?

A **network** is any group of two or more devices that are connected in a way that allows them to exchange data.

That's it. The devices could be:

- Two laptops connected by an Ethernet cable
- A home with phones, a TV, a laptop, and a router on WiFi
- Thousands of servers in a data center
- Billions of devices connected across the entire planet (the Internet)

The **scale** changes, but the core idea doesn't: devices connected together to share information.

---

## 3. Types of Networks: LAN, WAN, Internet

### LAN — Local Area Network

A **LAN** is a network that covers a small, limited physical area. Every device on a LAN is relatively close together and connected through the same router or switch.

**Real-world examples:**
- Your home WiFi network
- The Holberton classroom network
- A small office with 20 computers
- A coffee shop's guest WiFi

**Key characteristics:**
- Fast — devices are close together and bandwidth is high
- Private — not directly accessible from outside
- You control it — your router manages all the devices

```
LAN Example:

Laptop ──────┐
             │
Phone ────── Switch/Router ──── Internet
             │
Printer ─────┘

All these devices share the same local network.
They can talk to each other AND reach the internet through the router.
```

> **Mental model:** A LAN is like the rooms inside a building. People inside can talk directly to each other. To reach someone outside the building, they need to go through the front door (the router).

---

### WAN — Wide Area Network

A **WAN** connects multiple LANs that are far apart from each other — different buildings, cities, or even countries.

**Real-world examples:**
- A bank with branches in San Juan, New York, and Miami — all connected
- A university with campuses in different cities
- A multinational company where employees in different countries share internal systems

```
WAN Example:

[ LAN: Office San Juan ]
         │
         │  (leased lines / internet backbone)
         │
[ LAN: Office New York ]
         │
         │
[ LAN: Office Miami ]
```

WANs are usually managed by telecom companies who provide the infrastructure (fiber cables, satellite links, etc.) that connects the distant LANs together.

> **Mental model:** If a LAN is the inside of one building, a WAN is the road system connecting multiple buildings in different cities.

---

### The Internet

The **Internet** is the largest WAN that exists. It connects billions of devices across every continent through a massive global infrastructure of routers, fiber optic cables, satellites, and data centers.

The Internet is not owned by any one company or government. It is a network of networks — every ISP (Internet Service Provider), every university, every company connects their own network to a shared global backbone.

```
Your Laptop
    │
    ▼
Home Router (your LAN)
    │
    ▼
ISP Network (e.g., Claro PR)
    │
    ▼
Internet Backbone (intercontinental cables)
    │
    ▼
Google's Data Center (another LAN)
    │
    ▼
google.com loads in your browser
```

---

## 4. The OSI Model

### Why Does It Exist?

Networking involves many different problems happening at the same time:
- How do you physically move signals through a cable?
- How do two devices on the same network address each other?
- How do you route data across thousands of routers to reach the right destination?
- How do you make sure all the data arrived correctly?
- How does a web browser know what to do with the data once it arrives?

The **OSI Model** (Open Systems Interconnection Model) breaks these problems into **7 distinct layers**, each responsible for one piece of the puzzle. This makes it easier to understand, design, and troubleshoot networks because you can ask: *"Which layer is this problem happening at?"*

---

### The 7 Layers

```
┌───────────────────────────────────────────────┐
│  Layer 7 — Application    │ HTTP, SSH, DNS     │
├───────────────────────────────────────────────┤
│  Layer 6 — Presentation   │ Encryption, TLS    │
├───────────────────────────────────────────────┤
│  Layer 5 — Session        │ Managing sessions  │
├───────────────────────────────────────────────┤
│  Layer 4 — Transport      │ TCP / UDP          │
├───────────────────────────────────────────────┤
│  Layer 3 — Network        │ IP Addresses       │
├───────────────────────────────────────────────┤
│  Layer 2 — Data Link      │ MAC Addresses      │
├───────────────────────────────────────────────┤
│  Layer 1 — Physical       │ Cables, WiFi       │
└───────────────────────────────────────────────┘
```

**Memory trick (bottom to top):** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

---

### Layer by Layer Breakdown

#### Layer 1 — Physical
This is the actual hardware: copper wires, fiber optic cables, radio waves (WiFi), and electrical signals. Data at this layer is raw bits: `0`s and `1`s transmitted as electrical pulses or light.

*Problems at this layer:* unplugged cable, broken Ethernet port, weak WiFi signal.

#### Layer 2 — Data Link
This layer handles communication between devices **on the same local network**. It uses **MAC addresses** to identify which physical device on your LAN should receive a frame of data. Your router and switch operate here.

*Problems at this layer:* MAC address conflicts, ARP issues.

#### Layer 3 — Network
This layer handles communication **across different networks** using **IP addresses**. Routers operate at this layer — they read the destination IP and decide where to forward the data next.

*Problems at this layer:* wrong IP configuration, routing failures.

#### Layer 4 — Transport
This layer decides **how** data is delivered: reliably with error checking (**TCP**), or quickly without guarantees (**UDP**). It also uses **port numbers** to direct data to the right application.

*Problems at this layer:* packet loss, connection timeouts.

#### Layers 5, 6, 7 — Session, Presentation, Application
These upper layers manage the connection lifecycle, data formatting (like encryption via TLS), and the actual application logic (your browser rendering a webpage, SSH terminal, etc.).

---

### Real Example: Loading youtube.com

```
Layer 7 — Your browser makes an HTTP/S request for youtube.com
Layer 6 — TLS encrypts your request
Layer 4 — TCP breaks your request into packets and tracks delivery
Layer 3 — IP routes each packet from your network to YouTube's servers
Layer 2 — Your router uses MAC addresses to move data inside the LAN
Layer 1 — Signals travel through your WiFi or cable
```

When YouTube responds, the same process runs in reverse — data goes up the layers until your browser reassembles the page.

---

## 5. IP Addresses

**IP** stands for **Internet Protocol**. An IP address is a numerical label assigned to every device connected to a network. It serves two purposes:

1. **Identification** — who is this device?
2. **Location** — where is this device on the network?

Think of it like a home mailing address. Just as a postal worker needs your exact address to deliver a package, a router needs a device's IP address to deliver data.

### IPv4 Address Format

```
192  .  168  .  1  .  10
 │       │      │    │
 └───────┴──────┴────┘
      4 groups of numbers
      each between 0 and 255
      separated by dots
```

Each group is called an **octet** (8 bits). A full IPv4 address is **32 bits** total.

---

## 6. Public vs Private IP Addresses

### Private IP Addresses

When devices connect inside a LAN (your home, office, school), they get assigned **private IP addresses**. These addresses exist only within your local network — they are not reachable directly from the internet.

**Reserved private ranges:**

| Range | Example |
|---|---|
| `10.0.0.0 – 10.255.255.255` | `10.0.0.5` |
| `172.16.0.0 – 172.31.255.255` | `172.16.4.20` |
| `192.168.0.0 – 192.168.255.255` | `192.168.1.10` |

These ranges are reserved globally — no website or public server will ever have one of these IPs. That's what makes them safe to reuse inside every home or company.

### Public IP Addresses

Your **ISP** (Claro, Liberty, AT&T, etc.) assigns your router a **public IP address** — this is the address the rest of the internet uses to find you. Every device on your home network shares this one public IP when communicating with the outside world.

```
Home LAN:
  Laptop  → 192.168.1.5  (private)
  Phone   → 192.168.1.8  (private)
  TV      → 192.168.1.12 (private)
       │
       ▼
  Router: 192.168.1.1 (private, inside)
       │
       ▼ NAT (Network Address Translation)
       │
  Router: 73.44.91.20 (public, facing internet)
```

**NAT** (Network Address Translation) is the mechanism your router uses to translate between private and public IPs — it's why dozens of devices can share one public IP.

---

## 7. IPv4 vs IPv6

### The IPv4 Problem

IPv4 uses 32-bit addresses, which means there are about **4.3 billion** possible unique addresses. That sounds like a lot — but the world now has smartphones, smart TVs, laptops, servers, IoT sensors, cars, and more. We exceeded 4.3 billion internet-connected devices years ago.

### IPv6 — The Solution

**IPv6** uses 128-bit addresses. The number of possible addresses is approximately **340 undecillion** (3.4 × 10³⁸). That is enough for every grain of sand on Earth to have trillions of IP addresses.

```
IPv4:   192.168.1.1
        (32 bits, ~4.3 billion addresses)

IPv6:   2001:0db8:85a3:0000:0000:8a2e:0370:7334
        (128 bits, ~340 undecillion addresses)
```

IPv6 addresses are written as **8 groups of 4 hexadecimal digits**, separated by colons. Groups of all zeros can be shortened using `::`.

```
Full:       2001:0db8:0000:0000:0000:0000:0000:0001
Shortened:  2001:db8::1
```

### Transition

The internet is gradually moving from IPv4 to IPv6. Most modern systems support both simultaneously — this is called **dual-stack** networking.

---

## 8. Localhost and 0.0.0.0

### Localhost — 127.0.0.1

`127.0.0.1` is called the **loopback address**. When your computer sends data to this address, it never actually leaves your machine — the operating system intercepts it and loops it back to itself.

This is used to:
- Test a web server you're running locally
- Run a database or API locally before deploying
- Debug network software without needing another device

```bash
ping 127.0.0.1     # Your computer pings itself
ping localhost     # Same thing — 'localhost' maps to 127.0.0.1 in /etc/hosts
```

```
Your App → 127.0.0.1:5000
              │
              └──► Loops back internally
              │
Your App ◄────┘   (never hits the network)
```

### 0.0.0.0

When a server binds to `0.0.0.0`, it means: **"listen on ALL available network interfaces."**

A machine can have multiple interfaces — WiFi, Ethernet, a VPN, and loopback. Binding to `0.0.0.0` means accepting connections from any of them.

```bash
# Only your own machine can connect:
python3 -m http.server 8000 --bind 127.0.0.1

# Any device on the network (or internet) can connect:
python3 -m http.server 8000 --bind 0.0.0.0
```

| Address | Meaning |
|---|---|
| `127.0.0.1` | Only this machine (loopback) |
| `0.0.0.0` | All interfaces — accept from anywhere |

---

## 9. Subnets

A **subnet** (subnetwork) is a logical division of a larger network into smaller segments. Subnetting lets you split one large IP range into multiple smaller groups of devices.

### Why Subnet?

| Reason | Explanation |
|---|---|
| **Organization** | Separate departments: HR on one subnet, Engineering on another |
| **Security** | Devices on different subnets can be isolated by firewalls |
| **Performance** | Broadcast traffic stays within a subnet, reducing congestion |
| **IP Management** | Allocate only as many addresses as each group needs |

### Subnet Mask

A **subnet mask** tells a device which part of an IP address is the **network** and which part is the **host**.

```
IP Address:    192.168.1.10
Subnet Mask:   255.255.255.0

Network part:  192.168.1  (first 3 octets)
Host part:              10 (last octet)

All devices with 192.168.1.x are on the same subnet.
Valid hosts: 192.168.1.1 through 192.168.1.254
```

The subnet mask is often written in **CIDR notation** using a slash:

```
192.168.1.0/24   → 255.255.255.0 → 254 usable hosts
192.168.1.0/16   → 255.255.0.0   → 65,534 usable hosts
```

---

## 10. MAC Addresses

A **MAC address** (Media Access Control address) is a unique identifier hard-coded into every network interface card (NIC) at the factory. Unlike IP addresses, MAC addresses are tied to the physical hardware.

```
Format:   00:1A:2B:3C:4D:5E
          ──┬──  ────┬────
            │        │
         Manufacturer  Device-specific
         (OUI)         identifier
```

The first 3 bytes identify the manufacturer (e.g., Apple, Intel, Broadcom). The last 3 bytes are unique to that specific device.

### MAC vs IP — Key Differences

| Feature | IP Address | MAC Address |
|---|---|---|
| Layer | Layer 3 (Network) | Layer 2 (Data Link) |
| Scope | Works across networks | Works only within a LAN |
| Assignment | Assigned by DHCP or manually | Burned into hardware |
| Changes? | Yes — can change | No — (usually) permanent |
| Format | `192.168.1.10` | `00:1A:2B:3C:4D:5E` |

### How They Work Together

When your laptop sends data to a website:
- **IP address** is used to route the packet from your network to the destination server (Layer 3)
- **MAC address** is used to deliver the frame from your laptop to your router within the LAN (Layer 2)

The router uses a protocol called **ARP** (Address Resolution Protocol) to figure out which MAC address belongs to which IP address on the local network.

---

## 11. TCP vs UDP

Both **TCP** and **UDP** are **Layer 4 (Transport)** protocols. They define how data is packaged and sent between two endpoints. The fundamental tradeoff between them is **reliability vs speed**.

### TCP — Transmission Control Protocol

TCP establishes a **connection** before sending data and guarantees that every piece of data arrives correctly and in order. Here's how:

**The TCP Handshake (before any data flows):**
```
Client                        Server
  │                              │
  │──── SYN ────────────────────►│  "I want to connect"
  │◄─── SYN-ACK ─────────────────│  "OK, acknowledged"
  │──── ACK ────────────────────►│  "Great, let's go"
  │                              │
  │     [data transfer begins]   │
```

**What TCP guarantees:**
- Every packet is acknowledged — if one is lost, it's resent
- Packets arrive in the correct order
- Errors are detected and corrected
- The connection is cleanly closed when done

**Use TCP when:**
- Data must arrive completely and correctly
- Examples: loading a webpage, SSH sessions, file downloads, database queries

```
Analogy: TCP is like a certified postal delivery.
The sender gets a receipt confirming every package arrived.
If something gets lost, it gets re-sent.
```

---

### UDP — User Datagram Protocol

UDP sends data without establishing a connection first and without checking whether it arrived. It is **fire and forget**.

```
Client                        Server
  │                              │
  │──── data ───────────────────►│
  │──── data ───────────────────►│  (no acknowledgment)
  │──── data ───────────────────►│  (no guaranteed order)
```

**What UDP trades away for speed:**
- No delivery guarantee — packets can be lost
- No ordering — packets can arrive out of sequence
- No connection setup overhead

**Use UDP when:**
- Speed matters more than perfection
- A dropped packet is better than a delayed one
- Examples: video streaming, online gaming, VoIP calls, DNS lookups

```
Analogy: UDP is like shouting across a crowded room.
You say it once. Maybe they heard it, maybe they didn't.
You're not going back to check.
```

---

### TCP vs UDP Comparison

| Feature | TCP | UDP |
|---|---|---|
| Connection | Required (handshake) | None |
| Reliability | Guaranteed delivery | Best-effort only |
| Order | Guaranteed | Not guaranteed |
| Speed | Slower (overhead) | Faster (no overhead) |
| Error checking | Yes | Minimal |
| Use cases | HTTP, SSH, FTP | Gaming, video, DNS, VoIP |

---

## 12. Ports

An **IP address** identifies a device on the network. But a device can run dozens of services at the same time: a web server, an SSH server, a database, a chat app. How does the operating system know which program should receive incoming data?

That's what **ports** solve.

```
IP Address = The apartment building's street address
Port       = The specific apartment number inside

Sending to 192.168.1.10:80  →  the building at 192.168.1.10, apartment 80
Sending to 192.168.1.10:22  →  same building, but apartment 22 (SSH)
```

A port is just a **number from 0 to 65535** attached to a network connection. The OS uses it to route incoming data to the right process.

### Port Ranges

| Range | Name | Description |
|---|---|---|
| 0 – 1023 | Well-known ports | Reserved for standard services (requires root) |
| 1024 – 49151 | Registered ports | Used by common apps |
| 49152 – 65535 | Dynamic/ephemeral | Assigned temporarily to client connections |

### Ports You Must Memorize

| Service | Port | Protocol |
|---|---|---|
| SSH | **22** | TCP |
| HTTP | **80** | TCP |
| HTTPS | **443** | TCP |
| FTP | 21 | TCP |
| DNS | 53 | UDP/TCP |
| MySQL | 3306 | TCP |

### Real Example

```bash
# When you type this in a browser:
https://google.com

# Your browser actually connects to:
google.com:443

# When you SSH into a server:
ssh user@192.168.1.50
# Your client connects to:
192.168.1.50:22
```

---

## 13. Ping and ICMP

### What is Ping?

`ping` is a command-line tool used to test whether a device is reachable on the network and to measure how long it takes to get a response. It is the "are you there?" of networking.

```bash
ping google.com
```

```
PING google.com (142.250.80.46): 56 data bytes
64 bytes from 142.250.80.46: icmp_seq=0 ttl=117 time=12.4 ms
64 bytes from 142.250.80.46: icmp_seq=1 ttl=117 time=11.9 ms
64 bytes from 142.250.80.46: icmp_seq=2 ttl=117 time=12.1 ms
```

**What this output means:**
- `64 bytes from ...` — a response was received
- `icmp_seq` — sequence number of this particular ping
- `ttl` — Time To Live, decremented at each router hop
- `time` — round-trip time in milliseconds (lower = faster)

### ICMP — Internet Control Message Protocol

Ping works by sending **ICMP Echo Request** packets and waiting for **ICMP Echo Reply** packets. ICMP is a Layer 3 protocol used for diagnostics and error reporting — it is not for transferring data, only for sending network status messages.

```
Your machine                 Target
     │                          │
     │──── ICMP Echo Request ──►│
     │◄─── ICMP Echo Reply ─────│
     │                          │
     └── time measured here ────┘
```

### Interpreting Ping Results

| Result | Meaning |
|---|---|
| `64 bytes from ...` | Host is reachable, good latency |
| `Request timeout` | Host didn't respond (offline, firewall, or unreachable) |
| `Unknown host` | DNS couldn't resolve the hostname |
| High `time` values | Network is slow or congested |

```bash
# Ping a specific number of times (Linux: -c, macOS: -c)
ping -c 4 google.com

# Ping your own machine
ping localhost
ping 127.0.0.1
```

---

## 14. The /etc/hosts File

`/etc/hosts` is a plain-text file on Linux/macOS that maps **hostnames to IP addresses locally**, before DNS is consulted. It is essentially a manual DNS override that lives on your machine.

When you type `ping myserver`, the OS checks `/etc/hosts` first. If it finds a match, it uses that IP — no DNS query is made.

### View the File

```bash
cat /etc/hosts
```

Default contents on most Linux systems:
```
127.0.0.1   localhost
127.0.1.1   your-hostname
::1         localhost ip6-localhost ip6-loopback
```

### Add a Custom Entry

```bash
sudo nano /etc/hosts
```

Add a line at the bottom:
```
192.168.1.50   myserver
```

Now:
```bash
ping myserver          # resolves to 192.168.1.50
ssh user@myserver      # same as ssh user@192.168.1.50
curl http://myserver   # makes HTTP request to 192.168.1.50
```

### Common Use Cases

| Use Case | Example Entry |
|---|---|
| Local development | `127.0.0.1   myapp.local` |
| Name a LAN device | `192.168.1.20   raspberry-pi` |
| Block a website | `0.0.0.0   annoying-site.com` |
| Override DNS for testing | `1.2.3.4   staging.mycompany.com` |

> **Important:** Changes to `/etc/hosts` only affect the machine they're made on. Other devices on the network are unaffected.

---

## 15. Network Interfaces

A **network interface** is any connection point between your computer and a network — physical or virtual. Each interface has its own IP address and MAC address.

Common interfaces on a Linux machine:

| Interface | Description |
|---|---|
| `eth0` / `enp3s0` | Wired Ethernet |
| `wlan0` / `wlp2s0` | WiFi (wireless) |
| `lo` | Loopback (127.0.0.1) |
| `tun0` | VPN tunnel (virtual) |

### Display Network Interfaces

**Modern method (preferred):**
```bash
ip addr
```

**Legacy method (still common):**
```bash
ifconfig
```

### Reading `ip addr` Output

```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    link/ether 00:1a:2b:3c:4d:5e brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

- `eth0` — interface name
- `link/ether 00:1a:2b:3c:4d:5e` — MAC address
- `inet 192.168.1.10/24` — IPv4 address with subnet mask

---

## 16. Essential Networking Commands

### `ping` — Test Connectivity

```bash
ping google.com          # Continuous ping (Ctrl+C to stop)
ping -c 4 google.com     # Send exactly 4 pings
ping 127.0.0.1           # Ping localhost
```

---

### `netstat` — View Active Connections and Ports

```bash
netstat -tulnp
```

| Flag | Meaning |
|---|---|
| `-t` | Show TCP connections |
| `-u` | Show UDP connections |
| `-l` | Show only listening ports |
| `-n` | Show IPs (no DNS lookup) |
| `-p` | Show the process using the port |

Sample output:
```
Proto  Local Address     State       PID/Program
tcp    0.0.0.0:22        LISTEN      1234/sshd
tcp    0.0.0.0:80        LISTEN      5678/nginx
```

This tells you SSH (port 22) and a web server (port 80) are running.

---

### `nc` (Netcat) — The Networking Swiss Army Knife

`nc` can open raw TCP/UDP connections. Use it to test if a port is open on a remote host.

```bash
nc -zv google.com 80     # Test if port 80 is open on google.com
nc -zv google.com 443    # Test HTTPS port
```

Output if open:
```
Connection to google.com 80 port [tcp/http] succeeded!
```

Output if closed/filtered:
```
nc: connectx to google.com port 9999 (tcp) failed: Connection refused
```

| Flag | Meaning |
|---|---|
| `-z` | Scan without sending data |
| `-v` | Verbose output |

---

### `telnet` — Test Port Connectivity (Legacy)

```bash
telnet google.com 80
```

If the connection opens, the port is accessible. Type `GET / HTTP/1.0` and press Enter twice to request a page manually. Many systems no longer have `telnet` by default.

---

### `cut` — Extract Text Fields

Useful in scripts when parsing network command output.

```bash
echo "192.168.1.10:80" | cut -d ":" -f1   # Output: 192.168.1.10
echo "192.168.1.10:80" | cut -d ":" -f2   # Output: 80
```

| Flag | Meaning |
|---|---|
| `-d ":"` | Delimiter — split on this character |
| `-f1` | Field number to extract |

---

### `ip addr` — Show Network Interfaces (Modern)

```bash
ip addr          # Show all interfaces
ip addr show     # Same
```

---

## 17. Bash Script Requirements

All scripts for Holberton networking tasks must follow these conventions:

### Shebang Line

Every script must start with:
```bash
#!/usr/bin/env bash
```

This tells the OS to run the script using `bash` located via the `env` command (more portable than hardcoding `/bin/bash`).

### Comment Line

The second line must be a comment describing what the script does:
```bash
#!/usr/bin/env bash
# Displays all active network interfaces and their IP addresses
```

### Full Example Script

```bash
#!/usr/bin/env bash
# Checks if a host is reachable and displays its response time

HOST="google.com"

if ping -c 1 "$HOST" &>/dev/null; then
    echo "$HOST is reachable"
else
    echo "$HOST is unreachable"
fi
```

### Make a Script Executable

```bash
chmod +x script.sh     # Grant execute permission
./script.sh            # Run it
```

### Check Script Quality with Shellcheck

```bash
sudo apt install shellcheck    # Install
shellcheck script.sh           # Analyze for errors and style issues
```

Shellcheck catches common mistakes:
- Missing quotes around variables
- Incorrect use of `[` vs `[[`
- Deprecated syntax

---

## 18. Practice Exercises

Work through these hands-on. Type every command yourself — reading is not the same as doing.

---

**Exercise 1 — View Your IP Address**
```bash
ip addr
# or
ifconfig
```
*Identify your active interface. What is your IPv4 address? What is your MAC address?*

---

**Exercise 2 — Ping External and Local Hosts**
```bash
ping -c 4 google.com     # External host
ping -c 4 localhost      # Loopback
```
*Compare the response times. Which is faster and why?*

---

**Exercise 3 — Discover Listening Ports**
```bash
netstat -tulnp
```
*What services are currently running on your machine? Which ports are they using?*

---

**Exercise 4 — Test a Remote Port**
```bash
nc -zv google.com 80
nc -zv google.com 443
nc -zv google.com 9999   # This should fail
```
*What happens when you try a port that is not open?*

---

**Exercise 5 — Examine /etc/hosts**
```bash
cat /etc/hosts
```
*Add an entry mapping `192.168.1.1` to the name `myrouter`. Then ping `myrouter`.*

---

**Exercise 6 — Write a Script**

Write a bash script called `check_port.sh` that uses `nc` to check if port 80 is open on `google.com` and prints either "Port is open" or "Port is closed".

---

## 19. Summary Cheat Sheet

| Concept | Definition |
|---|---|
| **LAN** | Small local network (home, office) |
| **WAN** | Large network connecting multiple LANs |
| **Internet** | Global WAN connecting billions of devices |
| **OSI Model** | 7-layer framework for how networks work |
| **IP Address** | Logical identifier for a device on a network |
| **Private IP** | IP used inside a LAN (not reachable from internet) |
| **Public IP** | IP assigned by ISP, visible on the internet |
| **IPv4** | 32-bit address space (~4.3B addresses) |
| **IPv6** | 128-bit address space (solves IPv4 exhaustion) |
| **localhost** | `127.0.0.1` — refers to your own machine |
| **0.0.0.0** | All network interfaces |
| **Subnet** | Logical subdivision of a network |
| **MAC Address** | Physical hardware address (Layer 2) |
| **TCP** | Reliable, ordered, connection-oriented protocol |
| **UDP** | Fast, connectionless, no delivery guarantee |
| **Port** | Numeric endpoint that directs data to the right app |
| **SSH** | Port 22 |
| **HTTP** | Port 80 |
| **HTTPS** | Port 443 |
| **Ping** | Tool to test if a host is reachable |
| **ICMP** | Protocol used by ping |
| **/etc/hosts** | Local hostname-to-IP mapping file |
| **Network Interface** | Connection point between device and network |

---

### Final Note

Networking feels overwhelming at first because everything connects to everything else — you can't fully understand ports without IP, can't understand IP without the OSI model, and so on.

The way to actually learn this is: **run the commands**. Type `ping`, read `ifconfig`, break into `/etc/hosts`. The concepts become concrete the moment you see them behave in a real terminal. Every exercise above is designed to make that happen.

You already have the foundation. Now go put it to work.
