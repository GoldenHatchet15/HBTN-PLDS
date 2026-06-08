# Flask To-Do API — Complete Classroom Lecture

> **Audience:** Beginners who know basic Python. Intermediate developers will find deeper sections on security, design patterns, and trade-offs.
> **Goal:** By the end of this lecture, you can build, explain, and extend a production-style RESTful API with Flask.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [What Problem This Solves](#2-what-problem-this-solves)
3. [Prerequisites and Key Concepts](#3-prerequisites-and-key-concepts)
4. [Architecture and High-Level Design](#4-architecture-and-high-level-design)
5. [Folder and File Structure](#5-folder-and-file-structure)
6. [Technologies and Dependencies](#6-technologies-and-dependencies)
7. [Data Models and Database Design](#7-data-models-and-database-design)
8. [Application Flow — End to End](#8-application-flow--end-to-end)
9. [API Endpoints — Deep Dive](#9-api-endpoints--deep-dive)
10. [Authentication with JWT](#10-authentication-with-jwt)
11. [Rate Limiting](#11-rate-limiting)
12. [CORS — Cross-Origin Resource Sharing](#12-cors--cross-origin-resource-sharing)
13. [API Documentation with Swagger](#13-api-documentation-with-swagger)
14. [Testing the API](#14-testing-the-api)
15. [Design Patterns Used](#15-design-patterns-used)
16. [Security Considerations](#16-security-considerations)
17. [Performance Considerations](#17-performance-considerations)
18. [Real-World Use Cases](#18-real-world-use-cases)
19. [Potential Improvements and Technical Debt](#19-potential-improvements-and-technical-debt)
20. [Common Interview Questions](#20-common-interview-questions)
21. [Practical Exercises](#21-practical-exercises)
22. [Glossary](#22-glossary)

---

## 1. Project Overview

This repository contains a **RESTful API** for a To-Do List application built with the **Flask** Python web framework. It demonstrates a complete, production-oriented API with:

- User registration and login
- JWT-based authentication (stateless tokens)
- CRUD operations on tasks (Create, Read, Update, Delete)
- A SQLite database managed by SQLAlchemy
- Rate limiting to prevent abuse
- CORS support for browser-based frontends
- Swagger documentation for the API

Think of it as the **back-end server** that any frontend (web app, mobile app, CLI) could talk to over HTTP.

---

## 2. What Problem This Solves

### The Problem

Modern applications are composed of separate layers:
- A **frontend** (what the user sees — React, Angular, mobile apps)
- A **backend** (business logic and data storage)

These layers need a **common language to communicate**. That language is an **API** (Application Programming Interface), specifically a **REST API** which uses standard HTTP verbs and JSON.

Without a proper backend API:
- The frontend cannot store data permanently
- Multiple frontends cannot share the same data
- There is no way to enforce authentication or business rules

### What This Project Provides

| Need | Solution |
|------|----------|
| Store tasks persistently | SQLite database via SQLAlchemy |
| Identify who is making a request | JWT tokens issued on login |
| Protect write operations | `@jwt_required()` decorator |
| Prevent system overload | Rate limiting via Flask-Limiter |
| Allow browser apps to connect | CORS via Flask-CORS |
| Document the API for developers | Swagger JSON spec |

---

## 3. Prerequisites and Key Concepts

Before studying this project, you should understand:

### HTTP Basics

HTTP (HyperText Transfer Protocol) is how computers talk on the web. Every request has:
- A **method** (verb): `GET`, `POST`, `PUT`, `DELETE`
- A **URL** (path): e.g., `/tasks/3`
- **Headers**: metadata like `Authorization: Bearer <token>`
- A **body**: the data payload, usually JSON

| HTTP Method | Meaning | Example |
|-------------|---------|---------|
| GET | Read data | Fetch all tasks |
| POST | Create data | Register a user |
| PUT | Update data | Mark task complete |
| DELETE | Remove data | Delete a task |

### REST Principles

REST (Representational State Transfer) is an architectural style with six constraints:

1. **Client-Server**: The UI and data are separate
2. **Stateless**: Each request contains all needed information (no server-side sessions)
3. **Uniform Interface**: Consistent URL patterns and HTTP verbs
4. **Layered System**: Client doesn't know if it's talking to a proxy or origin server
5. **Cacheable**: Responses can declare themselves cacheable
6. **Code on Demand** (optional): Server can send executable code

### JSON

JavaScript Object Notation — the data format used by this API:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

### What is a Framework?

Flask is a **micro-framework** — it provides routing, request handling, and response building without imposing a rigid project structure. You choose which extensions to add.

---

## 4. Architecture and High-Level Design

```mermaid
graph TB
    subgraph Client["Client (Browser / Mobile / Script)"]
        FE[Frontend App]
        SCRIPT[test_api.py]
    end

    subgraph Server["Flask Server (app.py)"]
        CORS_MW[CORS Middleware]
        RATE[Rate Limiter]
        ROUTER[Flask Router]
        AUTH[JWT Middleware]

        subgraph Routes
            REG[POST /register]
            LOGIN[POST /login]
            GET_T[GET /tasks]
            POST_T[POST /tasks]
            PUT_T[PUT /tasks/<id>]
            DEL_T[DELETE /tasks/<id>]
        end

        ORM[SQLAlchemy ORM]
    end

    subgraph DB["Database Layer"]
        SQLITE[(SQLite: tasks.db)]
    end

    FE -->|HTTP Request| CORS_MW
    SCRIPT -->|HTTP Request| CORS_MW
    CORS_MW --> RATE
    RATE --> ROUTER
    ROUTER --> AUTH
    AUTH --> Routes
    Routes --> ORM
    ORM --> SQLITE
```

### Request Lifecycle

Every HTTP request goes through these layers in order:

```
1. Network  →  2. CORS Check  →  3. Rate Limit Check  →  4. Route Match
     →  5. JWT Validation (if protected)  →  6. Route Handler  →  7. ORM Query
     →  8. Database  →  9. JSON Response  →  10. Client
```

---

## 5. Folder and File Structure

```
4.RESTful_API/
├── env/                        # Python virtual environment (do not edit)
│   ├── bin/                    # Executables: flask, python, pip
│   └── lib64/                  # Installed packages (Flask, SQLAlchemy, etc.)
│
└── flask_todo_api/             # The actual application
    ├── app.py                  # ★ Main application — all logic lives here
    ├── test_api.py             # Integration test script
    ├── requirement.txt         # Dependency list (currently empty)
    ├── README.md               # Placeholder README
    ├── instance/
    │   └── tasks.db            # SQLite database file (auto-created)
    ├── static/
    │   └── swagger.json        # OpenAPI/Swagger documentation
    └── __pycache__/            # Python bytecode cache (auto-generated)
```

### File-by-File Explanation

| File | Purpose |
|------|---------|
| `app.py` | The heart of the application. Defines models, routes, and configuration |
| `test_api.py` | A standalone script that calls the API and prints pass/fail results |
| `swagger.json` | Describes the API in OpenAPI 2.0 format so tools can visualize it |
| `requirement.txt` | Should list dependencies; currently empty — use `pip freeze` to populate |
| `instance/tasks.db` | The SQLite database file, managed automatically by Flask-SQLAlchemy |

---

## 6. Technologies and Dependencies

### Core Framework

**Flask** (version in env: 3.x)

Flask is a lightweight Python web framework built on top of Werkzeug (WSGI toolkit) and Jinja2 (templating). For APIs, we use it without the templating engine.

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
```

`Flask(__name__)` tells Flask to locate resources relative to the current file.

### Extensions

```mermaid
graph LR
    FLASK[Flask Core]
    FLASK --> SA[flask-sqlalchemy\nDatabase ORM]
    FLASK --> JWT[flask-jwt-extended\nAuthentication]
    FLASK --> LIM[flask-limiter\nRate Limiting]
    FLASK --> CORS[flask-cors\nCross-Origin]
    SA --> SQLA[SQLAlchemy]
    SQLA --> SQLITE[(SQLite)]
```

| Extension | Package | Role |
|-----------|---------|------|
| Flask-SQLAlchemy | `flask_sqlalchemy` | Connects Flask to databases using Python objects |
| Flask-JWT-Extended | `flask_jwt_extended` | Creates and validates JSON Web Tokens |
| Flask-Limiter | `flask_limiter` | Enforces request rate limits per IP |
| Flask-CORS | `flask_cors` | Adds CORS headers to responses |
| Requests | `requests` | Used in test_api.py to make HTTP calls |

### Database

**SQLite** — a file-based relational database. No separate server process needed. Ideal for development and small apps. The database file (`tasks.db`) lives in the `instance/` folder, which Flask creates automatically.

---

## 7. Data Models and Database Design

### ORM Concept

An **ORM** (Object-Relational Mapper) lets you work with your database using Python classes instead of raw SQL. SQLAlchemy translates Python to SQL and back.

```python
# Python class  →  SQL table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
```

This creates the SQL equivalent:

```sql
CREATE TABLE task (
    id INTEGER NOT NULL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
```

### Entity Relationship Diagram

```mermaid
erDiagram
    USER {
        int id PK
        string username UK "max 50 chars, unique"
        string password "max 100 chars, plain text"
    }

    TASK {
        int id PK
        string title "max 100 chars"
        boolean completed "default: false"
    }
```

> Note: In this version, users and tasks are not linked — any authenticated user can modify any task. A real application would add a `user_id` foreign key on `Task`.

### The `to_dict()` Method

```python
def to_dict(self):
    return {"id": self.id, "title": self.title, "completed": self.completed}
```

This **serializes** a Python object into a plain dictionary, which `jsonify()` can then convert to a JSON HTTP response. Without this, Flask cannot convert a SQLAlchemy model object directly to JSON.

---

## 8. Application Flow — End to End

### Startup Sequence

```
python app.py
    │
    ├── Flask app created
    ├── Config applied (database URI, JWT secret, etc.)
    ├── SQLAlchemy initialized
    ├── JWTManager initialized
    ├── Limiter initialized
    ├── CORS initialized
    ├── Models defined (User, Task classes)
    ├── db.create_all() ── creates tables if they don't exist
    └── app.run(debug=True) ── starts HTTP server on port 5000
```

### Registration Flow

```
POST /register  {"username": "alice", "password": "secret"}
    │
    ├── Rate limiter: max 5 requests/minute from this IP?
    ├── Extract JSON from request body
    ├── Query DB: does user "alice" exist?
    │   ├── YES → return 400 "Username already exists"
    │   └── NO  → create User, save to DB, return 201
    └── Response: {"message": "User registered successfully"}
```

### Login Flow

```
POST /login  {"username": "alice", "password": "secret"}
    │
    ├── Rate limiter: max 10 requests/minute?
    ├── Query DB: find user with matching username AND password
    │   ├── NOT FOUND → return 401 "Invalid credentials"
    │   └── FOUND → generate JWT token with username as identity
    └── Response: {"token": "eyJhbGciOiJIUzI1NiIs..."}
```

### Authenticated Task Creation

```
POST /tasks  body: {"title": "Buy groceries"}
             headers: Authorization: Bearer eyJhbGciO...
    │
    ├── JWT middleware: decode and validate token
    │   ├── INVALID/MISSING → return 401 Unauthorized
    │   └── VALID → extract username from token
    ├── Rate limiter: max 10 requests/minute?
    ├── Create Task object with title from request
    ├── Add to DB session and commit
    └── Response: {"id": 1, "title": "Buy groceries", "completed": false}
```

---

## 9. API Endpoints — Deep Dive

### Complete Endpoint Table

| Method | Path | Auth Required | Rate Limit | Description |
|--------|------|:---:|-----------|-------------|
| POST | `/register` | No | 5/min | Register a new user |
| POST | `/login` | No | 10/min | Login, receive JWT token |
| GET | `/tasks` | No | 100/hr (default) | List all tasks |
| POST | `/tasks` | Yes | 10/min | Create a new task |
| PUT | `/tasks/<id>` | Yes | 10/min | Update a task |
| DELETE | `/tasks/<id>` | Yes | 5/min | Delete a task |

### Route Anatomy

```python
@app.route("/tasks/<int:task_id>", methods=["PUT"])  # ① Route definition
@jwt_required()                                       # ② Auth guard
@limiter.limit("10 per minute")                       # ③ Rate limit
def update_task(task_id):                             # ④ Handler function
    task = Task.query.get(task_id)                    # ⑤ DB lookup
    if task:
        data = request.json                           # ⑥ Parse body
        task.title = data.get("title", task.title)    # ⑦ Partial update
        task.completed = data.get("completed", task.completed)
        db.session.commit()                           # ⑧ Save
        return jsonify(task.to_dict())                # ⑨ Respond
    return jsonify({"error": "Task not found"}), 404  # ⑩ Error response
```

**Breakdown:**
1. `@app.route` registers the URL pattern. `<int:task_id>` captures and type-converts a path segment.
2. `@jwt_required()` rejects requests without a valid token before the function runs.
3. `@limiter.limit()` overrides the default rate limit for this specific route.
4. The function receives `task_id` as a Python integer argument.
5. `Task.query.get(task_id)` generates `SELECT * FROM task WHERE id = ?`.
6. `request.json` parses the request body as JSON.
7. `.get("title", task.title)` — if "title" is not in the request, keep the existing value. This enables **partial updates (PATCH-like behavior)**.
8. `db.session.commit()` writes changes to disk.
9. `jsonify()` converts a dict to a JSON HTTP response with `Content-Type: application/json`.
10. Returning a tuple `(response, status_code)` sets the HTTP status code.

### HTTP Status Codes Used

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 OK | Success | Successful GET, PUT, DELETE |
| 201 Created | Resource created | POST /register, POST /tasks |
| 400 Bad Request | Client error | Username already exists |
| 401 Unauthorized | Auth failed | Bad credentials, missing token |
| 404 Not Found | Resource missing | Task ID not in database |

---

## 10. Authentication with JWT

### What is JWT?

A **JSON Web Token** is a compact, URL-safe string that encodes a claim about a user. It has three parts separated by dots:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9    ← Header (algorithm)
.eyJzdWIiOiJhbGljZSIsImV4cCI6MTY...}    ← Payload (data)
.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV    ← Signature (proof of integrity)
```

The **payload** contains the identity and expiration. The **signature** is a cryptographic hash using the `JWT_SECRET_KEY`, which prevents tampering.

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    participant DB as Database

    C->>S: POST /login {username, password}
    S->>DB: SELECT user WHERE username=? AND password=?
    DB-->>S: User found
    S-->>C: {token: "eyJ..."}

    Note over C: Client stores token

    C->>S: POST /tasks {title: "Buy milk"}<br/>Authorization: Bearer eyJ...
    S->>S: Validate JWT signature
    S->>S: Extract identity from payload
    S->>DB: INSERT INTO task...
    DB-->>S: OK
    S-->>C: {id: 1, title: "Buy milk", completed: false}
```

### Why Stateless Auth?

Traditional sessions store user state on the server. JWT is **stateless** — the server doesn't store anything. The token itself contains all needed information. This makes the API horizontally scalable: any server can validate any token.

### Code Walkthrough

```python
# Create token on login
token = create_access_token(identity=user.username)
# → Encodes {"sub": "alice", "exp": <timestamp>, "iat": <timestamp>}
# → Signs with JWT_SECRET_KEY
# → Returns base64url-encoded string

# Protect a route
@jwt_required()
def create_task():
    # Only runs if Authorization header contains valid Bearer token
    current_user = get_jwt_identity()  # "alice" — extract identity if needed
```

### Security Note on JWT Secret

```python
app.config["JWT_SECRET_KEY"] = "supersecretkey"
```

This is **insecure for production**. Anyone who knows this key can forge tokens. In production, use a random 256-bit value from an environment variable.

---

## 11. Rate Limiting

### What is Rate Limiting?

Rate limiting prevents a single client from overwhelming the server with requests — protecting against brute force attacks and denial-of-service.

```python
limiter = Limiter(get_remote_address, app=app, default_limits=["100 per hour"])
```

- `get_remote_address` — identifies clients by their IP address
- `default_limits=["100 per hour"]` — every route gets this limit unless overridden

### Per-Route Limits

```python
@app.route("/register", methods=["POST"])
@limiter.limit("5 per minute")   # Tight limit — prevents bot registration
def register():
    ...

@app.route("/login", methods=["POST"])
@limiter.limit("10 per minute")  # Prevents password brute-forcing
def login():
    ...
```

When a client exceeds the limit, Flask-Limiter automatically returns **HTTP 429 Too Many Requests**.

---

## 12. CORS — Cross-Origin Resource Sharing

### The Problem

Browsers enforce a **same-origin policy**: JavaScript running on `http://myapp.com` cannot fetch data from `http://api.myapp.com` unless the API explicitly allows it.

### The Solution

CORS headers tell the browser which origins are permitted:

```
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
```

### Code Analysis — A Bug to Notice

```python
# Line 22: Allows ALL origins for ALL routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# ... models and db.create_all() ...

# Line 44: Restricts /tasks/* to specific origins
CORS(app, resources={r"/tasks/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:5500"]}})
```

**This is a bug.** `CORS()` is called twice, and the second call does not undo the first — it adds additional policies. The first wildcard `*` policy is still active. This is a security issue: the intent was to restrict `/tasks/*` to specific frontends, but the earlier wildcard overrides that intent.

**Correct approach:**

```python
CORS(app, resources={
    r"/tasks/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:5500"]},
    r"/register": {"origins": "*"},
    r"/login": {"origins": "*"},
})
```

---

## 13. API Documentation with Swagger

The `static/swagger.json` file describes the API using **OpenAPI 2.0** format. Tools like Swagger UI read this file and generate interactive documentation.

```json
{
  "swagger": "2.0",
  "info": { "title": "To-Do List API", "version": "1.0" },
  "paths": {
    "/tasks": {
      "get": { "summary": "Get all tasks" },
      "post": { "summary": "Create a new task", "parameters": [...] }
    }
  }
}
```

The `flask_swagger_ui` package (installed in the env) can serve this file as a web page. To enable it, you would add:

```python
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
```

Then visit `http://localhost:5000/api/docs` to see the interactive docs.

---

## 14. Testing the API

### How `test_api.py` Works

The test script is an **integration test** — it tests the actual running API, not mocked functions. This is different from unit tests (which test functions in isolation).

```python
def run_tests():
    test_register()           # 1. Create user
    token = test_login()      # 2. Get JWT token
    if token:
        test_get_tasks()      # 3. Read all tasks
        test_create_task(token)  # 4. Create a task (stores ID globally)
        test_get_tasks()      # 5. Verify it appears
        test_update_task(token)  # 6. Mark it complete
        test_get_tasks()      # 7. Verify update
        test_delete_task(token)  # 8. Remove it
        test_get_tasks()      # 9. Verify deletion
```

### Key Testing Technique — Global State

```python
TASK_ID = None  # Module-level variable

def test_create_task(token):
    global TASK_ID  # Modify the module-level variable
    ...
    TASK_ID = response.json().get("id")
```

`global` is used here to share the created task's ID between test functions. While functional, this is brittle — a better approach uses a test fixture or returns the value.

### Testing with curl

You can also test the API directly from a terminal:

```bash
# Register
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret"}'

# Login
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret"}'

# Create task (replace TOKEN with the token from login)
curl -X POST http://localhost:5000/tasks \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries"}'

# Get all tasks
curl http://localhost:5000/tasks
```

---

## 15. Design Patterns Used

### 1. Decorator Pattern

Python decorators (`@`) wrap functions with additional behavior without modifying them. This API uses decorators heavily:

```python
@app.route("/tasks", methods=["POST"])  # Register this function as a URL handler
@jwt_required()                          # Wrap it with auth validation
@limiter.limit("10 per minute")          # Wrap it with rate limiting
def create_task():
    ...
```

The execution order when a request arrives is **outermost first**: rate limiter → JWT check → handler function.

### 2. Active Record Pattern (via SQLAlchemy)

Each model class knows how to interact with its own database table:

```python
# Create
new_task = Task(title="Buy groceries")
db.session.add(new_task)
db.session.commit()

# Read
task = Task.query.get(task_id)     # SELECT * WHERE id = ?
tasks = Task.query.all()           # SELECT * FROM task

# Update (modify object, then commit)
task.completed = True
db.session.commit()

# Delete
db.session.delete(task)
db.session.commit()
```

### 3. Application Factory Pattern (partial)

The app is created at module level (`app = Flask(__name__)`). A more advanced version would use a factory function `create_app()` to allow multiple configurations (testing, production, development). This project does not implement a full factory pattern.

### 4. Data Transfer Object (DTO)

The `to_dict()` method is a simple DTO — it transforms a domain object (Task) into a plain data structure suitable for serialization:

```python
def to_dict(self):
    return {"id": self.id, "title": self.title, "completed": self.completed}
```

---

## 16. Security Considerations

### Critical Issues in Current Code

| Issue | Risk | Fix |
|-------|------|-----|
| Passwords stored in plain text | Database breach exposes all passwords | Use `bcrypt` or `argon2` to hash passwords |
| `JWT_SECRET_KEY = "supersecretkey"` | Attackers can forge tokens | Use `os.environ.get("JWT_SECRET_KEY")` with a random 256-bit key |
| CORS applied twice (conflicting) | May expose API to unintended origins | Configure CORS once with explicit rules |
| No input validation | Malformed requests may cause 500 errors | Validate request fields before processing |
| No HTTPS mentioned | Traffic is readable in transit | Deploy behind TLS/SSL (nginx/gunicorn) |
| Any user can modify any task | No ownership enforcement | Add `user_id` to Task and check ownership |

### Password Hashing Example (the correct approach)

```python
from werkzeug.security import generate_password_hash, check_password_hash

# Registration
new_user = User(
    username=data["username"],
    password=generate_password_hash(data["password"])
)

# Login
user = User.query.filter_by(username=data["username"]).first()
if user and check_password_hash(user.password, data["password"]):
    token = create_access_token(identity=user.username)
```

---

## 17. Performance Considerations

### SQLite Limitations

SQLite is single-writer: only one process can write at a time. For production with multiple concurrent users, switch to PostgreSQL or MySQL:

```python
# Development
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

# Production
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@host/dbname"
```

### Flask Development Server

`app.run(debug=True)` uses Flask's built-in development server, which:
- Handles only one request at a time
- Auto-reloads on code changes
- Should **never** be used in production

For production, use **gunicorn** or **uWSGI**:

```bash
gunicorn -w 4 app:app  # 4 worker processes
```

### Rate Limiter Storage

By default, Flask-Limiter stores rate limit counters in memory. If the app has multiple processes, each has its own counter, breaking the limit guarantee. For production, configure a shared Redis backend:

```python
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379"
)
```

---

## 18. Real-World Use Cases

This pattern — Flask REST API + SQLAlchemy + JWT — is the foundation of countless production systems:

1. **Task Management Apps** — Trello, Asana backends expose similar CRUD APIs
2. **Mobile App Backends** — React Native / Flutter apps talk to REST APIs
3. **Microservices** — Each service exposes a REST API that other services consume
4. **IoT Data Collection** — Devices POST sensor readings to a REST endpoint
5. **Headless CMS** — Content is managed through APIs consumed by frontends

The concepts you learn here (routing, authentication, database models, rate limiting, CORS) apply to any web backend language or framework.

---

## 19. Potential Improvements and Technical Debt

### Short-Term Fixes (Security)

1. **Hash passwords** with bcrypt before storing
2. **Move secrets to environment variables** — never hardcode them
3. **Fix the double CORS configuration**
4. **Add input validation** — check that `title` is a non-empty string

### Medium-Term Features

5. **Add task ownership** — link tasks to the user who created them
6. **Add pagination** to `GET /tasks` — return 20 tasks per page, not all at once
7. **Use a proper test framework** — pytest with fixtures instead of the current script
8. **Populate `requirement.txt`** — run `pip freeze > requirement.txt`

### Long-Term Architecture

9. **Switch to PostgreSQL** for production deployments
10. **Add caching** with Redis for frequently read data
11. **Implement refresh tokens** — current JWT tokens expire, forcing re-login
12. **Add logging** — structured logs for debugging and monitoring
13. **Use an application factory** (`create_app()`) to support multiple configs
14. **Add API versioning** — prefix routes with `/api/v1/` to allow future changes

---

## 20. Common Interview Questions

**Conceptual**

1. What is REST and what are its constraints?
2. What is the difference between `PUT` and `PATCH`?
3. Why are JWT tokens stateless? What are the implications?
4. What is an ORM and what problem does it solve?
5. Why should passwords never be stored in plain text?

**Code-Based**

6. What does `@jwt_required()` do? Where does the check happen?
7. What is the `db.session` and why do you need to call `commit()`?
8. What does `nullable=False` mean on a database column?
9. What happens if you call `Task.query.get(9999)` for a non-existent task?
10. What is the difference between `return jsonify({"error": "..."}), 404` and just `return jsonify({"error": "..."})`?

**Security-Focused**

11. What is a brute force attack and how does rate limiting prevent it?
12. What is CORS and why does the browser enforce it?
13. What is the risk of a hardcoded JWT secret key?
14. Why is `debug=True` dangerous in production?

---

## 21. Practical Exercises

**Beginner**
1. Run the API and use `test_api.py` to create, update, and delete a task. Observe the output.
2. Add a `GET /tasks/<id>` endpoint that returns a single task by its ID.
3. Add a `description` field to the `Task` model and migration.

**Intermediate**
4. Add password hashing using `werkzeug.security`.
5. Move `JWT_SECRET_KEY` to an environment variable using `os.environ`.
6. Add input validation: return 400 if `title` is missing or empty on POST /tasks.
7. Implement task ownership: a task can only be updated/deleted by the user who created it.

**Advanced**
8. Add pagination to `GET /tasks`: support `?page=1&limit=10` query parameters.
9. Convert `test_api.py` to a proper pytest test suite.
10. Add a `/api/docs` endpoint that serves the Swagger UI using `flask_swagger_ui`.
11. Deploy the API on a VPS using gunicorn and nginx.

---

## 22. Glossary

| Term | Definition |
|------|-----------|
| **API** | Application Programming Interface — a defined way for programs to communicate |
| **REST** | Representational State Transfer — an architectural style for APIs using HTTP |
| **Endpoint** | A specific URL that handles a specific type of request (e.g., `GET /tasks`) |
| **Route** | The mapping from a URL pattern to a Python function in Flask |
| **JSON** | JavaScript Object Notation — a human-readable data format |
| **HTTP Method** | The verb of an HTTP request: GET, POST, PUT, DELETE |
| **Status Code** | A 3-digit number in an HTTP response indicating success or failure |
| **ORM** | Object-Relational Mapper — maps Python classes to database tables |
| **Model** | A Python class that represents a database table (User, Task) |
| **Migration** | A versioned change to the database schema |
| **JWT** | JSON Web Token — a signed, self-contained authentication token |
| **Bearer Token** | An HTTP Authorization header value: `Authorization: Bearer <token>` |
| **CORS** | Cross-Origin Resource Sharing — browser security policy for cross-domain requests |
| **Rate Limiting** | Restricting how many requests a client can make in a time window |
| **SQLite** | A lightweight, file-based SQL database |
| **Session** | SQLAlchemy's unit of work — collects changes and applies them on `commit()` |
| **Decorator** | Python syntax (`@`) that wraps a function with additional behavior |
| **Middleware** | Code that runs between the incoming request and the route handler |
| **CRUD** | Create, Read, Update, Delete — the four basic database operations |
| **Serialization** | Converting a Python object to a JSON-compatible format |
| **Primary Key** | A unique identifier for each row in a database table |
| **Foreign Key** | A column that references the primary key of another table |
| **Virtual Environment** | An isolated Python installation with its own packages (`env/`) |
| **Gunicorn** | A production-grade WSGI HTTP server for Python applications |
| **WSGI** | Web Server Gateway Interface — the Python web server standard |
| **Plain Text Password** | A password stored without hashing — a critical security vulnerability |
| **Bcrypt** | A strong password hashing algorithm designed to be slow |
| **OpenAPI/Swagger** | A specification format for describing REST APIs |
| **Integration Test** | A test that exercises multiple components together (e.g., API + database) |
| **Unit Test** | A test that tests a single function or class in isolation |
