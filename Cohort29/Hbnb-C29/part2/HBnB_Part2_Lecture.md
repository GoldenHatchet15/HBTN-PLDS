# HBnB - Part 2: Business Logic and API Endpoints

> **Project:** HBnB - BL and API | **Author:** Javier Valenzani | **Level:** Novice | **Team size:** 3
> **Repo:** `holbertonschool-hbnb` | **Directory:** `part2` | **Language:** Python

---

## Table of Contents

1. [What Is This Project About?](#1-what-is-this-project-about)
2. [The Big Picture: Application Architecture](#2-the-big-picture-application-architecture)
3. [Key Concepts You Must Understand](#3-key-concepts-you-must-understand)
4. [Project Structure](#4-project-structure)
5. [Learning Objectives](#5-learning-objectives)
6. [Tasks Breakdown](#6-tasks-breakdown)
7. [How to Approach Each Task](#7-how-to-approach-each-task)
8. [Testing Your API](#8-testing-your-api)
9. [Common Pitfalls](#9-common-pitfalls)
10. [Resources](#10-resources)

---

## 1. What Is This Project About?

In Part 1 (HBnB - UML), you **designed** the architecture of an AirBnB-like application on paper — UML diagrams, entity definitions, and relationships. Now in Part 2, you **build it**.

The goal is to implement:
- The **Business Logic Layer** — the Python classes that model your data (User, Place, Review, Amenity)
- The **Presentation Layer** — a RESTful API built with Flask and `flask-restx` that exposes CRUD endpoints

**What you are NOT doing yet:**
- JWT authentication / role-based access control (that's Part 3)
- A real database (you use in-memory storage for now; SQLAlchemy comes in Part 3)

Think of Part 2 as bringing your Part 1 blueprints to life as working code, without worrying about security or persistence yet.

---

## 2. The Big Picture: Application Architecture

The application follows a **three-layer architecture** with the **Facade pattern** connecting them:

```
┌─────────────────────────────────┐
│      Presentation Layer         │  ← Flask + flask-restx (API endpoints)
│   app/api/v1/users.py           │
│   app/api/v1/places.py  etc.    │
└────────────────┬────────────────┘
                 │  calls
                 ▼
┌─────────────────────────────────┐
│         Facade (HBnBFacade)     │  ← Single entry point to Business Logic
│   app/services/facade.py        │
└────────────────┬────────────────┘
                 │  calls
                 ▼
┌─────────────────────────────────┐
│      Business Logic Layer       │  ← Core models: User, Place, Review, Amenity
│   app/models/user.py            │
│   app/models/place.py  etc.     │
└────────────────┬────────────────┘
                 │  calls
                 ▼
┌─────────────────────────────────┐
│      Persistence Layer          │  ← In-Memory Repository (for now)
│   app/persistence/repository.py │
└─────────────────────────────────┘
```

### Why the Facade Pattern?

The **Facade** is a single object that the API talks to. It hides all the complexity of the business logic and the repository. This means:
- The API never directly touches the models
- The API never directly touches the database/repository
- If you swap in SQLAlchemy later (Part 3), only the Facade and repository need to change — the API stays the same

---

## 3. Key Concepts You Must Understand

### 3.1 The Facade Pattern

```python
# app/services/facade.py
class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        # ...

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)
```

The API endpoints call `facade.create_user()`, not `User()` directly.

### 3.2 In-Memory Repository

A dictionary-backed store that implements a common interface. In Part 3 this interface gets replaced by SQLAlchemy — the code that calls it doesn't change.

```python
class InMemoryRepository:
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        return next(
            (obj for obj in self._storage.values()
             if getattr(obj, attr_name) == attr_value),
            None
        )
```

### 3.3 Base Model with UUID and Timestamps

Every entity (User, Place, Review, Amenity) should inherit from a `BaseModel` that auto-generates:
- A **UUID** as `id`
- `created_at` timestamp
- `updated_at` timestamp

```python
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
```

### 3.4 flask-restx Namespaces and Models

`flask-restx` gives you:
- **Namespaces** — logical groupings of routes (like blueprints)
- **Models** — for request/response validation and Swagger documentation
- **Auto-generated Swagger UI** at `/api/v1/` when the app runs

```python
from flask_restx import Namespace, Resource, fields

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User created successfully')
    @api.response(400, 'Email already registered')
    def post(self):
        """Create a new user"""
        user_data = api.payload
        # ... call facade
```

---

## 4. Project Structure

```
part2/
├── app/
│   ├── __init__.py          ← Flask app factory
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py     ← User endpoints
│   │       ├── places.py    ← Place endpoints
│   │       ├── reviews.py   ← Review endpoints
│   │       └── amenities.py ← Amenity endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base_model.py    ← BaseModel with id, timestamps
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── facade.py        ← HBnBFacade class
│   └── persistence/
│       ├── __init__.py
│       └── repository.py    ← InMemoryRepository
├── config.py
├── requirements.txt          ← Must include flask and flask-restx
└── run.py                    ← Entry point
```

---

## 5. Learning Objectives

By the end of this project you should be able to:

1. **Modular Design** — Structure a Python project with proper separation of concerns between layers
2. **API Development** — Build and document RESTful APIs using Flask and `flask-restx`
3. **Business Logic** — Translate UML designs into working Python classes with validation
4. **Data Serialization** — Return extended/nested attributes in API responses (e.g., owner's name inside a Place response)
5. **Testing** — Test APIs with cURL and automated tools, document results

---

## 6. Tasks Breakdown

### Task 0 — Project Setup and Package Initialization
**Points: 10 | Review: Manual**

**What you do:**
- Create the full folder structure shown in Section 4
- Create all `__init__.py` files to make each folder a Python package
- Implement the `InMemoryRepository` class (provided — just understand it)
- Set up the Flask application factory and register the API blueprint
- Set up `flask-restx` with the base namespace

**Key deliverable:** Running `python run.py` should start the Flask server without errors.

**Approach:**
1. Start from the folder structure above and create all files
2. The in-memory repository code is given to you — copy and understand it
3. Set up `app/__init__.py` as an **app factory** (`create_app()` function)
4. Register `flask-restx`'s `Api` object and connect namespaces

---

### Task 1 — Core Business Logic Classes
**Points: 10 | Review: Manual**

**What you do:**
Implement the 4 core model classes based on your Part 1 UML design:

| Class | Key Attributes | Relationships |
|-------|---------------|---------------|
| `User` | first_name, last_name, email, password, is_admin | owns Places, writes Reviews |
| `Place` | title, description, price, latitude, longitude | owned by User, has Amenities, has Reviews |
| `Review` | text, rating | belongs to User and Place |
| `Amenity` | name | associated with Places |

**Validation rules you must enforce:**
- `User.email` — must be valid format, must be unique
- `User.first_name` / `last_name` — max 50 chars, required
- `Place.price` — must be positive float
- `Place.latitude` — must be between -90.0 and 90.0
- `Place.longitude` — must be between -180.0 and 180.0
- `Review.rating` — must be between 1 and 5
- `Review.text` — required, not empty

**Approach:**
1. Create `BaseModel` first with `id`, `created_at`, `updated_at`, and an `update()` method
2. Each entity inherits from `BaseModel` and adds its own attributes
3. Use `@property` setters for validation, raising `ValueError` on invalid input
4. For relationships, store IDs or object references (e.g., `place.owner_id`, or `place.owner`)

---

### Task 2 — User Endpoints
**Points: 10 | Review: Manual**

**Endpoints to implement:**

| Method | Route | Description | Status Codes |
|--------|-------|-------------|--------------|
| POST | `/api/v1/users/` | Create a user | 201, 400 |
| GET | `/api/v1/users/` | List all users | 200 |
| GET | `/api/v1/users/<user_id>` | Get user by ID | 200, 404 |
| PUT | `/api/v1/users/<user_id>` | Update a user | 200, 400, 404 |

**Important rules:**
- `DELETE` is NOT implemented for users in Part 2
- Password must NEVER appear in any response
- Email must be unique — return 400 if already registered

**The POST and GET-by-ID are given to you as an example.** You implement GET-all and PUT.

**Approach:**
```python
# Pattern for all endpoints
@api.route('/')
class UserList(Resource):
    def get(self):
        users = facade.get_all_users()
        return [{'id': u.id, 'first_name': u.first_name, ...} for u in users], 200

    def post(self):
        user_data = api.payload
        # Check email uniqueness
        if facade.get_user_by_email(user_data['email']):
            return {'error': 'Email already registered'}, 400
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, ...}, 201
```

---

### Task 3 — Amenity Endpoints
**Points: 10 | Review: Manual**

**Endpoints to implement:**

| Method | Route | Description | Status Codes |
|--------|-------|-------------|--------------|
| POST | `/api/v1/amenities/` | Create an amenity | 201, 400 |
| GET | `/api/v1/amenities/` | List all amenities | 200 |
| GET | `/api/v1/amenities/<amenity_id>` | Get amenity by ID | 200, 404 |
| PUT | `/api/v1/amenities/<amenity_id>` | Update an amenity | 200, 400, 404 |

**Important rules:**
- `DELETE` is NOT implemented for amenities in Part 2
- Amenity only has `name` — keep it simple

**Approach:** Follow the exact same pattern as users. This task is mostly about practicing the pattern independently, without the reference code provided.

---

### Task 4 — Place Endpoints
**Points: 10 | Review: Manual**

**Endpoints to implement:**

| Method | Route | Description | Status Codes |
|--------|-------|-------------|--------------|
| POST | `/api/v1/places/` | Create a place | 201, 400 |
| GET | `/api/v1/places/` | List all places | 200 |
| GET | `/api/v1/places/<place_id>` | Get place by ID | 200, 404 |
| PUT | `/api/v1/places/<place_id>` | Update a place | 200, 400, 404 |

**This is the most complex task.** Place has relationships:
- **owner** — a User (validate that the owner_id exists)
- **amenities** — a list of Amenity objects (validate each amenity_id)

**When returning a Place, include nested data:**
```json
{
  "id": "abc123",
  "title": "Cozy Apartment",
  "price": 100.0,
  "latitude": 18.46,
  "longitude": -66.10,
  "owner": {
    "id": "xyz789",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
  },
  "amenities": [
    {"id": "am1", "name": "WiFi"}
  ]
}
```

**Important rules:**
- `DELETE` is NOT implemented for places in Part 2
- Reviews are NOT included yet (that's Task 5)
- Validate `price > 0`, `-90 <= latitude <= 90`, `-180 <= longitude <= 180`

**Approach:**
1. When creating a Place, receive `owner_id` and list of `amenity_ids`
2. In the facade, validate that the owner and each amenity exist
3. When returning the place data, fetch and embed owner/amenity details

---

### Task 5 — Review Endpoints
**Points: 10 | Review: Manual**

**Endpoints to implement:**

| Method | Route | Description | Status Codes |
|--------|-------|-------------|--------------|
| POST | `/api/v1/reviews/` | Create a review | 201, 400 |
| GET | `/api/v1/reviews/` | List all reviews | 200 |
| GET | `/api/v1/reviews/<review_id>` | Get review by ID | 200, 404 |
| PUT | `/api/v1/reviews/<review_id>` | Update a review | 200, 400, 404 |
| DELETE | `/api/v1/reviews/<review_id>` | Delete a review | 200, 404 |
| GET | `/api/v1/places/<place_id>/reviews` | Get reviews for a place | 200, 404 |

**This is the only entity where DELETE is implemented in Part 2.**

**After this task, update your Place endpoint** to include the list of reviews when fetching a specific place.

**Approach:**
```python
@api.route('/<review_id>')
class ReviewResource(Resource):
    def delete(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200
```

Add `delete_review(review_id)` to your Facade and call `repo.delete(review_id)` in the repository.

---

### Task 6 — Testing and Validation
**Points: 10 | Review: Manual**

**What you do:**
1. Add/verify validation logic across all models
2. Run black-box tests using `cURL`
3. Write automated tests with `unittest` or `pytest`
4. Use the Swagger UI (auto-generated at `/api/v1/`) to test manually
5. Document your test results in a testing report

**cURL test examples:**
```bash
# Create a user
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john@example.com"}'

# Get all users
curl http://localhost:5000/api/v1/users/

# Create a place
curl -X POST http://localhost:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nice Place",
    "price": 75.0,
    "latitude": 18.46,
    "longitude": -66.10,
    "owner_id": "<user_id_here>",
    "amenities": []
  }'

# Test invalid data (should return 400)
curl -X POST http://localhost:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Bad", "price": -10, "latitude": 999, "longitude": 0, "owner_id": "fake"}'
```

---

## 7. How to Approach Each Task

### Recommended Order

```
Task 0 → Task 1 → Task 2 → Task 3 → Task 4 → Task 5 → Task 6
Setup    Models   Users    Amenities  Places   Reviews   Testing
```

This order matters because:
- You can't build endpoints without models
- Place depends on User (owner) and Amenity being done first
- Review depends on User and Place being done first

### Development Workflow Per Task

1. **Implement the model** (in `app/models/`)
2. **Add facade methods** (in `app/services/facade.py`)
3. **Implement the API namespace** (in `app/api/v1/`)
4. **Register the namespace** in the app
5. **Test with cURL** as you go

### Tips for the Facade

Keep a single `facade` instance. In Flask, create it in `app/__init__.py` and import it in each namespace file:

```python
# app/__init__.py
from app.services.facade import HBnBFacade
facade = HBnBFacade()

# app/api/v1/users.py
from app import facade
```

### Tips for Data Serialization

When your API returns objects, they need to be JSON-serializable. Build explicit `to_dict()` methods on your models:

```python
class User(BaseModel):
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
            # NEVER include password here
        }
```

---

## 8. Testing Your API

### Start the Server
```bash
cd part2
python run.py
```

### Access Swagger UI
Open `http://localhost:5000/api/v1/` in your browser — flask-restx generates interactive documentation automatically.

### HTTP Status Code Cheat Sheet

| Code | Meaning | When to use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT |
| 201 | Created | Successful POST |
| 400 | Bad Request | Invalid data, duplicate email, validation failure |
| 404 | Not Found | Resource with given ID doesn't exist |

### Writing Unit Tests
```python
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 201)

    def test_duplicate_email(self):
        data = {'first_name': 'A', 'last_name': 'B', 'email': 'a@b.com'}
        self.client.post('/api/v1/users/', json=data)
        response = self.client.post('/api/v1/users/', json=data)
        self.assertEqual(response.status_code, 400)
```

---

## 9. Common Pitfalls

1. **Returning model objects directly** — Flask can't serialize Python objects to JSON. Always return dictionaries.

2. **Forgetting to update `updated_at`** — Call `self.updated_at = datetime.now()` in your `update()` method.

3. **Circular imports** — If `facade.py` imports from `models/` and `models/` imports from `facade.py`, you'll get an error. Keep models independent — they should not import the facade.

4. **Password in response** — Never include `password` in any API response. Build your serialization carefully.

5. **Not validating related object IDs** — When creating a Place, always verify that `owner_id` maps to a real User and each `amenity_id` maps to a real Amenity. Return 400 if not.

6. **Namespace not registered** — If you create a new namespace file but forget to import and register it in `app/__init__.py`, your routes won't exist.

7. **requirements.txt** — Must include at least `flask` and `flask-restx`. The checker verifies `pip install -r requirements.txt` works without errors.

---

## 10. Resources

### Official Documentation
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [flask-restx Documentation](https://flask-restx.readthedocs.io/en/latest/)
- [Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)

### Design Patterns
- [Facade Pattern in Python](https://refactoring.guru/design-patterns/facade/python/example)

### RESTful API Design
- [RESTful API Best Practices](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
- [REST API Tutorial](https://restfulapi.net/)

### Project-Specific Guides (Holberton GitHub)
- [Task 0 - Project Init](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_00_init.md)
- [Task 1 - Business Logic](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_01_bl.md)
- [Task 2 - User Endpoints](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_02_user.md)
- [Task 3 - Amenity Endpoints](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_03_amenity.md)
- [Task 4 - Place Endpoints](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_04_place.md)
- [Task 5 - Review Endpoints](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_05_review.md)
- [Task 6 - Testing](https://github.com/Holberton-Uy/hbnb-doc/blob/main/part2/task_06_test.md)

### Testing Tools
- [cURL Guide](https://everything.curl.dev/)
- [Python Modules & Packages](https://realpython.com/python-modules-packages/)

---

*Lecture prepared for Cohort 29 — HBnB Part 2 PLD | 2026-06-10*
