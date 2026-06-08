# Python — Object-Relational Mapping (ORM)

---

## Table of Contents
1. [Connecting Python to MySQL with MySQLdb](#1-connecting-python-to-mysql-with-mysqldb)
2. [Introduction to ORM](#2-introduction-to-object-relational-mapping-orm)
3. [Using SQLAlchemy ORM](#3-using-sqlalchemy-orm)
4. [Defining Models with SQLAlchemy](#4-defining-models-with-sqlalchemy)
5. [CRUD Operations with SQLAlchemy](#5-performing-crud-operations-with-sqlalchemy)
6. [Hands-On Exercises](#6-hands-on-exercises)
7. [Summary & Recap](#7-summary--recap)

---

## 1. Connecting Python to MySQL with MySQLdb

MySQLdb is a low-level Python module that lets you connect to a MySQL database and execute raw SQL queries directly from your Python code.

### a) Installing MySQLdb

```bash
$ sudo apt-get install python3-dev libmysqlclient-dev
$ sudo pip3 install mysqlclient
```

### b) Connecting and Querying

```python
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="hbtn_0e_0_usa",
    charset="utf8"
)

cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
```

**What each part does:**

| Part | Purpose |
|------|---------|
| `MySQLdb.connect(...)` | Opens a connection to the MySQL server |
| `conn.cursor()` | Creates a cursor object used to execute queries |
| `cur.execute(...)` | Sends a SQL query to the database |
| `cur.fetchall()` | Retrieves all rows from the last executed query |
| `cur.close()` / `conn.close()` | Closes the cursor and connection to free resources |

> **Important:** Always close your cursor and connection when done. Leaving connections open wastes server resources and can cause connection limit errors under heavy load.

---

## 2. Introduction to Object-Relational Mapping (ORM)

### What is ORM?

ORM (Object-Relational Mapping) is a technique that lets you interact with a database using Python objects instead of writing raw SQL queries. Each table in the database is represented as a Python class, and each row becomes an instance of that class.

**SQLAlchemy** is the most widely used ORM in Python.

### Why Use an ORM?

| Without ORM (Raw SQL) | With ORM (SQLAlchemy) |
|-----------------------|-----------------------|
| You write SQL strings manually | You interact with Python objects |
| SQL errors only surface at runtime | Errors caught earlier through Python |
| Switching databases requires rewriting queries | Switching databases requires minimal changes |
| Logic and SQL mixed together | Cleaner, more maintainable code |

### Side-by-Side Comparison

**Without ORM:**
```python
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
```

**With ORM:**
```python
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
```

No SQL string needed — just Python.

---

## 3. Using SQLAlchemy ORM

### a) Installing SQLAlchemy

```bash
$ sudo pip3 install SQLAlchemy
```

### b) Creating a Database Connection

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+mysqldb://root:root@localhost/hbtn_0e_0_usa',
    pool_pre_ping=True
)

Session = sessionmaker(bind=engine)
session = Session()
```

**Breaking down the connection string:**

```
mysql+mysqldb://root:root@localhost/hbtn_0e_0_usa
      ↑          ↑    ↑      ↑            ↑
   dialect    user  password host       database
```

**What each part does:**

| Part | Purpose |
|------|---------|
| `create_engine(...)` | Sets up the connection to the database |
| `pool_pre_ping=True` | Tests the connection before each use to avoid stale connections |
| `sessionmaker(bind=engine)` | Creates a session factory tied to the engine |
| `Session()` | Opens an active session for performing ORM operations |

> **What is a session?** Think of a session as a workspace. All your database operations (inserts, queries, updates, deletes) happen inside a session, and nothing is actually saved to the database until you call `session.commit()`.

---

## 4. Defining Models with SQLAlchemy

A **model** is a Python class that maps to a database table. Each attribute of the class corresponds to a column in the table.

### a) Mapping a Python Class to a MySQL Table

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id   = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
```

**What each part does:**

| Part | Purpose |
|------|---------|
| `declarative_base()` | Creates a base class that all models inherit from |
| `__tablename__` | Tells SQLAlchemy which table this class maps to |
| `Column(Integer, primary_key=True, autoincrement=True)` | An integer column that is the primary key and auto-increments |
| `Column(String(128), nullable=False)` | A string column (max 128 chars) that cannot be empty |

**The mapping in plain terms:**

```
Python class  →  Database table
State         →  states

Python attr   →  Table column
State.id      →  states.id      (INT, PRIMARY KEY, AUTO_INCREMENT)
State.name    →  states.name    (VARCHAR(128), NOT NULL)
```

### b) Creating Tables from Models

```python
Base.metadata.create_all(engine)
```

This tells SQLAlchemy to look at all classes that inherit from `Base` and create their corresponding tables in MySQL if they do not already exist. It is safe to run multiple times — it will not drop or recreate tables that already exist.

---

## 5. Performing CRUD Operations with SQLAlchemy

### a) Create — Adding New Data

```python
new_state = State(name="California")
session.add(new_state)
session.commit()

print(new_state.id)  # Prints the auto-assigned ID
```

**Step by step:**
1. `State(name="California")` — creates a new Python object (not yet in the database).
2. `session.add(new_state)` — stages it to be inserted.
3. `session.commit()` — sends the `INSERT` to the database and finalizes it.
4. After commit, `new_state.id` is automatically populated with the new row's ID.

---

### b) Read — Querying Data

```python
# Get all states, sorted by id
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
```

**Common query patterns:**

```python
# Get all records
session.query(State).all()

# Filter by a specific value
session.query(State).filter_by(name="California").all()

# Get the first result only
session.query(State).filter_by(id=1).first()

# Order results
session.query(State).order_by(State.name).all()

# Count records
session.query(State).count()
```

---

### c) Update — Modifying Existing Data

```python
state_to_update = session.query(State).filter_by(id=2).first()

if state_to_update:
    state_to_update.name = "New Mexico"
    session.commit()
```

**Step by step:**
1. Query for the object you want to change.
2. Check it exists with `if state_to_update`.
3. Modify the attribute directly on the Python object.
4. Call `session.commit()` — SQLAlchemy detects the change and sends an `UPDATE` to the database.

> **Note:** You do not need to call `session.add()` again when updating an existing object. SQLAlchemy tracks changes to objects it retrieved from the database automatically.

---

### d) Delete — Removing Data

```python
state_to_delete = session.query(State).filter_by(name="California").first()

if state_to_delete:
    session.delete(state_to_delete)
    session.commit()
```

**Step by step:**
1. Query for the object you want to remove.
2. Check it exists with `if state_to_delete`.
3. `session.delete(state_to_delete)` — marks it for deletion.
4. `session.commit()` — sends the `DELETE` to the database.

---

### CRUD Summary

| Operation | SQLAlchemy Method | SQL Equivalent |
|-----------|-------------------|----------------|
| Create | `session.add(obj)` + `session.commit()` | `INSERT INTO ...` |
| Read | `session.query(Model).all()` | `SELECT * FROM ...` |
| Update | modify attribute + `session.commit()` | `UPDATE ... SET ...` |
| Delete | `session.delete(obj)` + `session.commit()` | `DELETE FROM ...` |

---

## 6. Hands-On Exercises

### Task 1: Using MySQLdb

1. Install MySQLdb and connect to a local MySQL database.
2. Create a `states` table using a raw SQL query through a cursor.
3. Insert three records into the table.
4. Retrieve and print all records ordered by `id`.
5. Close the cursor and connection.

---

### Task 2: Using SQLAlchemy

1. Install SQLAlchemy and set up an engine connected to your local MySQL database.
2. Define a `State` model class mapped to a `states` table with `id` and `name` columns.
3. Run `Base.metadata.create_all(engine)` to create the table.
4. Open a session and insert a new state using `session.add()` and `session.commit()`.
5. Query and print all states ordered by `id`.
6. Update the name of the state with `id = 1`.
7. Delete the state you just updated.
8. Query all states again to confirm the deletion.

---

## 7. Summary & Recap

### MySQLdb
- Connects Python directly to MySQL using raw SQL.
- Requires manually writing SQL strings.
- Useful for simple scripts or when you need direct query control.

### SQLAlchemy ORM
- Abstracts SQL queries into Python objects and methods.
- Tables become classes; rows become instances.
- Changes are tracked in a **session** and flushed to the database on `session.commit()`.

### Key SQLAlchemy Components

| Component | What It Does |
|-----------|-------------|
| `create_engine()` | Establishes the database connection |
| `declarative_base()` | Base class all models inherit from |
| `Column(...)` | Defines a table column and its type |
| `sessionmaker()` | Factory for creating session objects |
| `session.add()` | Stages a new object for insertion |
| `session.query()` | Queries the database for objects |
| `session.commit()` | Saves all pending changes to the database |
| `session.delete()` | Marks an object for deletion |
| `Base.metadata.create_all()` | Creates tables from model definitions |

### MySQLdb vs SQLAlchemy

| Feature | MySQLdb | SQLAlchemy ORM |
|---------|---------|----------------|
| Query style | Raw SQL strings | Python methods and objects |
| Readability | Lower | Higher |
| Portability across DBs | No | Yes |
| Learning curve | Lower | Higher |
| Best for | Simple scripts, direct control | Larger applications, maintainability |
