# RESTful APIs
### Holberton School

This is a lecture covering:
- APIs and REST
- HTTP vs HTTPS
- HTTP Methods and Status Codes
- JSON
- curl
- Python requests
- http.server
- Flask APIs
- Authentication and Authorization
- JWT

> **How to use this PLD:** Don't just read it — type the commands and run the code yourself. APIs are something you understand by *poking at them*, not by memorizing definitions. Every code block here is meant to be tried.

---

# Learning Objectives

By the end of this PLD, students should be able to:

- Explain what an API is
- Explain REST and RESTful APIs
- Differentiate HTTP and HTTPS
- Understand requests and responses
- Explain common HTTP methods
- Explain common HTTP status codes
- Consume APIs using curl
- Consume APIs using Python requests
- Build a simple API using http.server
- Build a simple API using Flask
- Understand authentication and authorization
- Understand JWT authentication

---

# What Is an API?

API stands for **Application Programming Interface**.

That sounds scary, but the idea is simple: an API is just a way for two programs to talk to each other. You use APIs constantly without realizing it. When a weather app shows you the forecast, it didn't *measure* the weather itself — it asked a weather service's API, and the service answered.

### The Restaurant Analogy

We'll come back to this analogy all lecture, so let's set it up properly:

- **Customer = Client** (your app, your browser, your code)
- **Waiter = API** (the messenger)
- **Kitchen = Server** (where the work actually happens)
- **Order = Request** (what you ask for)
- **Food = Response** (what you get back)

Here's the key insight: **you never walk into the kitchen yourself.** You don't need to know how the kitchen works, what brand of stove they use, or where they keep the salt. You just tell the waiter what you want, and food shows up. The API hides all the complicated kitchen stuff and gives you a simple, predictable way to make requests.

That's *why* APIs are so useful: they let programs cooperate without needing to understand each other's insides.

---

# What Is REST?

REST stands for **Representational State Transfer**.

Don't worry about that mouthful. In practice, REST is just **a popular set of rules for designing APIs** so that everyone builds them in a similar, predictable way. Before REST became common, every API was a little snowflake with its own weird conventions. REST gave developers a shared playbook.

An API that follows these rules is called a **RESTful API**.

RESTful APIs usually use:

- **HTTP** — the same protocol your browser uses to load websites
- **URLs (Endpoints)** — addresses that point to specific things, like `/users` or `/posts/5`
- **JSON** — a simple text format for the data being sent back and forth
- **Status Codes** — short numbers that say whether things went well or badly
- **Stateless Communication** — explained right below

The nice thing: because so many APIs follow these same patterns, once you learn how to use *one* RESTful API, you basically know how to use *thousands* of them.

---

# What Does Stateless Mean?

**Stateless** means the server does not automatically remember previous requests. Every request starts with a blank slate.

Back to the restaurant: imagine a waiter with *zero* memory. Every single time you speak, you have to re-introduce yourself: "Hi, I'm at table 5, I'm the one who ordered the pasta, and now I'd like more water." Annoying for a human waiter — but great for servers, because it means the server doesn't have to keep track of millions of ongoing conversations. Each request carries everything needed to handle it.

**Why this matters:** because each request stands on its own, you can't assume the server "knows who you are" from a previous request. That's exactly why we later need things like tokens (see the JWT section) — they're how a request proves who it is, every single time.

---

# HTTP vs HTTPS

**HTTP** = Hypertext Transfer Protocol
**HTTPS** = Hypertext Transfer Protocol Secure

They do the same job — moving requests and responses around — but HTTPS adds **encryption** (using something called SSL/TLS). Encryption scrambles the data so that anyone snooping on the connection just sees gibberish instead of your password or credit card number.

| | HTTP | HTTPS |
|--------|--------|--------|
| Encrypted? | No | Yes |
| Default port | 80 | 443 |
| Safe for passwords? | No | Yes |
| Used today? | Rarely | Almost everywhere |

**Simple rule of thumb:** if a site asks for *anything* private — a password, a payment, personal info — it should be HTTPS. That little padlock icon in your browser's address bar means HTTPS is active.

---

# Requests and Responses

Before we get into methods, let's nail down the two halves of every API conversation.

A **request** is what the client sends. It includes:
- A **method** (what you want to do — get something? create something?)
- A **URL / endpoint** (what you want to do it to)
- Optional **headers** (extra info, like "I'm sending JSON")
- An optional **body** (the actual data, used when creating or updating)

A **response** is what the server sends back. It includes:
- A **status code** (did it work? — that's the number, like 200 or 404)
- Optional **headers**
- A **body** (the data you asked for, usually as JSON)

Every interaction is just this back-and-forth: **request goes out, response comes back.** Everything else in this lecture is just details about what goes inside those two things.

---

# HTTP Methods

The **method** is the verb of your request — it tells the server *what kind of action* you want. Think of them as the few basic things you can do to any piece of data.

## GET — *"Show me."*
Retrieve data. This is read-only: it never changes anything. Loading a web page is a GET.

## POST — *"Make a new one."*
Create new data. For example, submitting a sign-up form creates a new user.

## PUT — *"Replace this entirely."*
Replace existing data with a full new version. If you PUT a user, you send *all* their fields, and the old version is completely overwritten.

## PATCH — *"Just change this part."*
Partially update data. If you only want to change a user's email and leave everything else alone, PATCH is the polite way to do it.

## DELETE — *"Get rid of it."*
Remove data.

> **The mental model that makes this click:** GET / POST / PUT / PATCH / DELETE map almost perfectly onto the four things you can do to *any* data: **C**reate (POST), **R**ead (GET), **U**pdate (PUT/PATCH), **D**elete (DELETE). Developers call this **CRUD**. If you remember CRUD, you remember the methods.

---

# Common Status Codes

When the server answers, it sends back a 3-digit **status code**. You don't have to memorize all of them — just learn what the *first digit* means and you can guess the rest.

- **2xx — Success.** "It worked." 🎉
- **4xx — You messed up.** Something was wrong with *your* request.
- **5xx — The server messed up.** Your request was fine; the server broke.

Here are the ones you'll actually run into:

| Code | Meaning | In plain words |
|------|----------|----------------|
| 200 | OK | It worked, here's your data |
| 201 | Created | Your new thing was made successfully |
| 400 | Bad Request | Your request was malformed — check what you sent |
| 401 | Unauthorized | You didn't log in / your token is missing or bad |
| 403 | Forbidden | You're logged in, but not allowed to do this |
| 404 | Not Found | That thing doesn't exist |
| 409 | Conflict | It clashes with something (e.g. that email is taken) |
| 500 | Internal Server Error | The server crashed — not your fault |

> **401 vs 403 trips up everyone.** 401 = "I don't know who you are." 403 = "I know who you are, and you can't do that." One is about *identity*, the other is about *permission*.

---

# JSON

JSON stands for **JavaScript Object Notation**. Despite the name, it's used everywhere, not just in JavaScript. It's the standard way APIs send data because it's easy for both humans and machines to read.

A JSON object is just **keys and values** wrapped in curly braces:

```json
{
  "name": "Jane",
  "age": 28,
  "city": "Los Angeles"
}
```

The rules are short:
- Data lives in `"key": value` pairs
- Text values go in **double quotes** (`"Jane"`) — single quotes are not allowed
- Numbers, `true`, `false`, and `null` are written without quotes
- You can nest objects and use lists with square brackets `[ ]`

A slightly richer example shows nesting and a list:

```json
{
  "name": "Jane",
  "age": 28,
  "hobbies": ["reading", "cycling"],
  "address": {
    "city": "Los Angeles",
    "country": "USA"
  }
}
```

If you've used a Python dictionary, JSON will feel very familiar — that's not a coincidence, and it's exactly why Python makes JSON so easy to work with.

---

# Using curl

`curl` is a command-line tool for making requests *without writing any code*. It's perfect for quickly testing an API, and it's already installed on most systems.

First, check it's there:

```bash
curl --version
```

### A basic GET request

```bash
curl https://jsonplaceholder.typicode.com/posts
```

This prints a big list of fake blog posts as JSON. (`jsonplaceholder` is a free practice API — it's safe to hammer with test requests.)

### Just the headers, please

Sometimes you only care about the response *metadata*, not the data itself:

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

You'll see the status code and headers, including a line like `HTTP/2 200` — there's that 200 we talked about.

### A POST request (creating data)

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"title":"foo"}' \
https://jsonplaceholder.typicode.com/posts
```

Let's break down the new pieces, because this is where curl looks intimidating but really isn't:
- `-X POST` — use the POST method (default is GET)
- `-H "Content-Type: application/json"` — a header telling the server "I'm sending you JSON"
- `-d '{"title":"foo"}'` — the **body**, the actual data you're sending

The server responds with the new post it created, including a `201 Created` style result.

---

# Using Python Requests

curl is great for quick tests, but inside a program you'll want code. The `requests` library is the friendliest way to talk to APIs in Python.

Install it:

```bash
pip install requests
```

A basic GET:

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.status_code)   # e.g. 200

posts = response.json()       # turns the JSON into a Python list/dict
print(posts[0])               # look at the first post
```

Notice how clean this is compared to curl: `requests.get(...)` makes the request, and `.json()` automatically converts the response into normal Python objects you can loop over and use.

A POST with `requests` is just as readable:

```python
import requests

new_post = {"title": "foo", "body": "bar", "userId": 1}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post          # 'json=' handles the headers AND the body for you
)

print(response.status_code)   # 201
print(response.json())        # the created post, echoed back
```

> **Handy habit:** always check `response.status_code` (or `response.ok`) before trusting the data. If the request failed, `response.json()` might not contain what you expect.

---

# Building an API with http.server

So far we've been the **customer**. Now let's step into the **kitchen** and build a server of our own.

`http.server` is built into Python — nothing to install. It's not what you'd use for a real product, but it's perfect for *seeing the mechanics* of a server with no magic hidden away.

Here's a tiny working server. Save it as `server.py`:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Decide what to send based on the URL the client asked for
        if self.path == "/status":
            self.send_response(200)              # status code
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            body = {"status": "OK"}
            self.wfile.write(json.dumps(body).encode())
        else:
            self.send_response(404)              # unknown endpoint
            self.end_headers()
            self.wfile.write(b"Not Found")

# Start the server on port 8000
server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
```

Run it:

```bash
python3 server.py
```

Then, in another terminal, talk to your own server:

```bash
curl http://localhost:8000/status
```

You should get back `{"status": "OK"}`. Congratulations — you just built and called your own API. Notice how *manual* everything is: you set the status code, set each header, and write the body yourself. That's a lot of bookkeeping... which is exactly the problem Flask solves.

---

# Building an API with Flask

Flask is a lightweight framework that handles all that bookkeeping for you, so you can focus on *what* your API does instead of plumbing.

Install it:

```bash
pip install flask
```

The classic minimal app:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

app.run()
```

A few things to notice:
- `@app.route("/")` connects a URL to a function. Visit `/` and Flask runs `home()`.
- Whatever the function returns becomes the response body.
- That `@` line is a **decorator** — for now, just read it as "when someone visits this URL, run the function below."

Now compare this to our `http.server` example by returning JSON — watch how much shorter it is:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({"status": "OK"})     # Flask sets the headers + 200 for you

app.run()
```

That's the whole point of a framework: the same result as our hand-built server, but with the tedious parts handled automatically.

---

# Authentication vs Authorization

These two words look almost identical and get mixed up constantly. Here's the clean split:

**Authentication** — *Who are you?*
Proving your identity. Logging in with a username and password is authentication.

**Authorization** — *What are you allowed to do?*
Checking your permissions. A regular user and an admin might both be logged in (authenticated), but only the admin is *authorized* to delete other people's accounts.

> **Memory trick:** **Authe**ntication = identity, **Autho**rization = permission. You always authenticate *first*, then the system authorizes what you can do.

Tie it back to our status codes: a **401** is an *authentication* failure ("who are you?"), and a **403** is an *authorization* failure ("you can't do that").

---

# JWT

**JWT** = JSON Web Token. Remember how REST is *stateless* — the server doesn't remember you between requests? A JWT is the clever solution: it's a token (a long string) that the client holds onto and sends with every request to prove who it is.

The typical flow:

1. **User logs in** with their username and password
2. **Server validates** those credentials
3. **Server generates a token** and sends it back
4. **Client stores the token** (often in the browser or app)
5. **Client sends the token** on every future request

That token rides along in a header that looks like this:

```http
Authorization: Bearer TOKEN_HERE
```

Think of the token like a **wristband at a concert.** You show your ID once at the entrance (login), and in return you get a wristband (the token). After that, you don't re-prove your identity at every door — security just glances at the wristband. The server works the same way: it checks the token instead of asking you to log in again on every request. That's how a *stateless* server can still know who you are.

> A JWT actually carries a little encoded information about the user inside it, and it's digitally signed so it can't be faked. You don't need the deep details yet — just understand it as a tamper-proof wristband the client shows on every request.

---

# Final Review

Try answering these out loud before peeking back at the lecture:

- What is an API? *(Hint: think of the waiter.)*
- What is REST, and what makes an API "RESTful"?
- What's the difference between HTTP and HTTPS, and when must you use HTTPS?
- What does **stateless** mean, and why does it matter?
- Name the main HTTP methods and the CRUD action each one maps to.
- What do the **2xx**, **4xx**, and **5xx** status code families mean?
- What's the difference between **401** and **403**?
- What is JSON, and how does it relate to a Python dictionary?
- How would you make a GET and a POST request with `requests`?
- What problem does Flask solve compared to `http.server`?
- What's the difference between **authentication** and **authorization**?
- What is a JWT, and how does it let a stateless server recognize you?

---

### Going further (optional)

If you want to keep exploring after this PLD:
- Build a small Flask API with all four CRUD operations on a list of items kept in memory.
- Use `requests` to consume a real public API (try a free one — many list at *public-apis* directories).
- Add a fake login endpoint that hands out a token, and a protected endpoint that requires it.