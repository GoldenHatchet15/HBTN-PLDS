# Introduction to SQL & Relational Databases
### A Comprehensive Beginner's Guide

---

## Section 1: Introduction to Databases

### 1. What is a Database?

A database is an organized collection of data that can be easily accessed, managed, and updated. Rather than storing information in scattered text files or spreadsheets, a database provides a structured system that makes retrieval fast and reliable.

Think of a database as a highly organized digital filing cabinet. Each drawer represents a category (like students or orders), and each folder within a drawer contains a specific record. The real power of a database is that you can search, filter, and connect information across different drawers instantly.

#### Real-World Examples

- A university stores student records, grades, and course registrations in a database.
- An e-commerce site tracks products, customer orders, and inventory using a database.
- A bank manages account balances and transaction histories through a database.
- Social networks like Instagram store user profiles, posts, and relationships in databases.

#### Types of Databases

| Relational (SQL) | Non-Relational (NoSQL) |
|---|---|
| Data stored in tables (rows & columns) | Data stored in flexible formats (JSON, key-value, graphs) |
| Uses SQL to query data | Uses database-specific query languages |
| Strong data consistency and integrity | Flexible schema, easier to scale horizontally |
| Examples: MySQL, PostgreSQL, SQLite, SQL Server | Examples: MongoDB, Firebase, Redis, Cassandra |
| Best for: structured, predictable data | Best for: large-scale, rapidly changing data |

> In this course, we focus exclusively on relational databases and SQL, which remain the industry standard for most business and web applications.

#### Why Use a Database Instead of a Spreadsheet?

- **Performance:** Databases handle millions of records efficiently; spreadsheets slow down quickly.
- **Multi-user Access:** Multiple users can read/write simultaneously without conflicts.
- **Security:** Fine-grained control over who can access or modify specific data.
- **Data Integrity:** Constraints prevent invalid or duplicate data from being entered.
- **Relationships:** Data in different tables can be linked and queried together.

---

## Section 2: Relational Database Concepts

### 2. Understanding Relational Databases

A relational database organizes data into tables — like a structured spreadsheet — and defines relationships between those tables. Understanding a few key concepts will make SQL much easier to learn.

#### Tables: Rows and Columns

Every piece of data in a relational database lives in a table. A table is made up of:

- **Columns** (also called fields): Define what type of data is stored (e.g., name, age, email).
- **Rows** (also called records): Each row is one complete entry in the table.

**Example — a `students` table:**

| id | name | age | email |
|---|---|---|---|
| 1 | Alice Rivera | 20 | alice@email.com |
| 2 | John Doe | 21 | john@email.com |
| 3 | Maria Santos | 19 | maria@email.com |

#### Primary Keys

A **Primary Key** is a column (or combination of columns) that uniquely identifies each row in a table. Think of it like a student ID card number — no two students share the same ID.

**Primary Key Rules:**
- Must be **UNIQUE** — no two rows can have the same primary key value.
- Must **NOT be NULL** — every row must have a value for the primary key.
- Should remain **STABLE** — it should never change after it's set.
- Commonly an auto-incrementing integer (1, 2, 3...) or a UUID.

#### Foreign Keys

A **Foreign Key** is a column in one table that references the Primary Key of another table. This creates a relationship between tables, which is what makes relational databases so powerful.

**Example:** An `enrollments` table can connect students to courses:

| enrollment_id | student_id (FK) | course_id (FK) | grade |
|---|---|---|---|
| 1 | 1 → Alice | 101 → Math | A |
| 2 | 2 → John | 102 → Science | B+ |
| 3 | 1 → Alice | 102 → Science | A- |

Here, `student_id` references the `id` column in the `students` table, and `course_id` references the `id` column in a `courses` table. This lets you query across multiple tables to answer questions like *"What courses is Alice enrolled in and what are her grades?"*

---

## Section 3: What is SQL?

### 3. SQL — Structured Query Language

SQL (Structured Query Language) is the standard language used to communicate with relational databases. Pronounced either as "S-Q-L" or "sequel", it was developed in the 1970s by IBM and has been an industry standard ever since.

SQL allows you to do four fundamental things — collectively called **CRUD operations:**

| Operation | SQL Command | What It Does |
|---|---|---|
| Create | `INSERT` | Add new data into a table |
| Read | `SELECT` | Retrieve and view data from a table |
| Update | `UPDATE` | Modify existing data in a table |
| Delete | `DELETE` | Remove data from a table |

#### Popular SQL Database Systems

- **MySQL** — The most widely used open-source SQL database, common in web development.
- **PostgreSQL** — Powerful open-source database with advanced features; preferred for complex applications.
- **SQLite** — Lightweight, file-based database; great for mobile apps and learning.
- **Microsoft SQL Server** — Enterprise-grade database used in corporate environments.
- **Oracle DB** — Enterprise SQL database, common in large financial systems.

The core SQL syntax is largely the same across all these systems. If you learn MySQL, you can quickly adapt to any of the others.

---

## Section 4: Installing & Accessing MySQL

### 4. Installing MySQL

We will use MySQL for this course because it is free, widely used, and easy to set up on Ubuntu Linux. Follow the steps below to get your environment ready.

#### Step-by-Step Installation on Ubuntu

**Step 1: Update the package list**

Always update your package list before installing anything to ensure you get the latest version:

```sql
sudo apt update
```

**Step 2: Install the MySQL server**

```bash
sudo apt install mysql-server
```

This installs the MySQL server, client tools, and all necessary dependencies. You may be prompted to confirm with `Y`.

**Step 3: Start the MySQL service**

After installation, start the MySQL service so it runs in the background:

```bash
sudo service mysql start
```

**Step 4: Verify the installation**

Confirm MySQL installed correctly by checking its version:

```bash
mysql --version
```

You should see output similar to: `mysql  Ver 8.0.xx  Distrib 8.0.xx, for Linux (x86_64)`

**Step 5: Log into MySQL**

Access the MySQL command-line interface as the root user:

```bash
sudo mysql -uroot -p
```

> **Note on the password prompt:**
> - On fresh Ubuntu installations, the default root password is often empty — just press Enter.
> - If you set a password during installation, enter it here.
> - Once logged in, you will see the MySQL prompt: `mysql>`

---

## Section 5: Basic SQL Commands

### 5. Basic SQL Commands

All SQL commands end with a semicolon (`;`). This tells MySQL where the statement ends. Commands are case-insensitive, but it is a strong convention to write SQL keywords in `UPPERCASE` and table/column names in `lowercase`.

### 5a. Database Operations

#### Listing All Databases

To see what databases currently exist on your MySQL server:

```sql
SHOW DATABASES;
```

MySQL comes with some built-in databases (`information_schema`, `mysql`, `performance_schema`). These are system databases — **do not modify or delete them.**

#### Creating a Database

Create a new database using the `CREATE DATABASE` command. The `IF NOT EXISTS` clause prevents an error if the database already exists:

```sql
CREATE DATABASE IF NOT EXISTS school_db;
```

> **Best Practice:**
> - Use lowercase and underscores for database and table names (e.g., `school_db`, not `SchoolDB`).
> - Use `IF NOT EXISTS` to write safer, re-runnable scripts.
> - Choose names that describe the data — `school_db` is clear and professional.

#### Selecting (Switching to) a Database

Before you can work with tables inside a database, you must tell MySQL which database to use:

```sql
USE school_db;
```

After running this command, all subsequent table operations will apply to `school_db` until you switch to another database or close the session.

#### Deleting a Database

To permanently delete an entire database and all its tables:

```sql
DROP DATABASE IF EXISTS school_db;
```

> ⚠️ **Warning:** `DROP DATABASE` is irreversible. All tables and data inside the database will be permanently deleted. Always double-check which database you are targeting before running this command.

---

### 5b. Table Operations

#### Creating a Table

A table must be defined with column names and data types before any data can be inserted. Here is how to create a `students` table:

```sql
CREATE TABLE students (
    id     INT          NOT NULL AUTO_INCREMENT,
    name   VARCHAR(100) NOT NULL,
    age    INT,
    email  VARCHAR(150),
    PRIMARY KEY (id)
);
```

**Understanding each part:**

| Keyword / Type | Explanation |
|---|---|
| `INT` | Integer number (e.g., 1, 42, 1000). Used for IDs, ages, counts. |
| `VARCHAR(100)` | Variable-length text, up to 100 characters. Use for names, emails, titles. |
| `NOT NULL` | This column cannot be left empty. A value is required. |
| `AUTO_INCREMENT` | MySQL automatically assigns the next number (1, 2, 3...) — no need to specify the ID. |
| `PRIMARY KEY (id)` | Designates the `id` column as the unique identifier for each row. |

#### Listing Tables in the Current Database

```sql
SHOW TABLES;
```

Displays all tables inside whichever database you have selected with `USE`.

---

### 5c. Data Operations (CRUD)

#### INSERT — Adding Data

Use `INSERT INTO` to add a new row of data into a table:

```sql
-- Insert a single student
INSERT INTO students (name, age, email)
VALUES ('Alice Rivera', 20, 'alice@email.com');

-- Insert multiple students at once
INSERT INTO students (name, age, email) VALUES
    ('John Doe',    21, 'john@email.com'),
    ('Maria Santos',19, 'maria@email.com');
```

Because `id` is `AUTO_INCREMENT`, we skip it in the `INSERT` statement and MySQL assigns it automatically. The order of values in `VALUES(...)` must match the order of columns listed.

---

#### SELECT — Reading Data

`SELECT` is the most commonly used SQL command. It retrieves data from a table:

```sql
-- Select ALL columns from all rows
SELECT * FROM students;

-- Select only specific columns
SELECT name, age FROM students;

-- Select with a condition (WHERE clause)
SELECT * FROM students WHERE age > 19;

-- Sort results alphabetically by name
SELECT * FROM students ORDER BY name ASC;

-- Limit results to the first 5 rows
SELECT * FROM students LIMIT 5;
```

> **Pro Tip:** Avoid using `SELECT *` in production code — it retrieves all columns, which is inefficient. Instead, explicitly name the columns you need: `SELECT name, age FROM students;`. This makes queries faster and more readable.

---

#### UPDATE — Modifying Existing Data

`UPDATE` changes the value of one or more columns in existing rows:

```sql
-- Update the age of the student with id = 1
UPDATE students
SET age = 21
WHERE id = 1;

-- Update multiple columns at once
UPDATE students
SET age = 22, email = 'alice_new@email.com'
WHERE id = 1;
```

> ⚠️ **Critical Warning — Always Use WHERE with UPDATE:** If you forget the `WHERE` clause, MySQL will update **EVERY row** in the table! Always specify which row(s) to update using a `WHERE` condition.

---

#### DELETE — Removing Data

`DELETE` removes one or more rows from a table:

```sql
-- Delete a specific student
DELETE FROM students WHERE id = 1;

-- Delete all students older than 25
DELETE FROM students WHERE age > 25;

-- Verify the deletion
SELECT * FROM students;
```

> ⚠️ **Critical Warning — Always Use WHERE with DELETE:** `DELETE FROM students;` without a `WHERE` clause deletes **ALL rows** in the table! The table structure remains, but all data is gone — and this cannot be undone.

---

### Quick Reference — SQL Commands Summary

| Command | Description |
|---|---|
| `SHOW DATABASES;` | List all databases on the server |
| `CREATE DATABASE db_name;` | Create a new database |
| `DROP DATABASE db_name;` | Permanently delete a database |
| `USE db_name;` | Switch to a specific database |
| `SHOW TABLES;` | List all tables in current database |
| `CREATE TABLE t (...);` | Define a new table with columns |
| `INSERT INTO t (...) VALUES (...);` | Add a new row of data |
| `SELECT * FROM t;` | Retrieve all data from a table |
| `SELECT col FROM t WHERE ...;` | Retrieve filtered data |
| `UPDATE t SET col=val WHERE ...;` | Modify existing data |
| `DELETE FROM t WHERE ...;` | Remove specific rows |

---

## Section 6: Hands-On Exercises

### 6. Hands-On Exercises

These exercises will help you practice everything covered in this lecture. Work through them in order. If you get stuck, review the relevant section above.

---

#### Exercise 1: Create a Database and Table

**Objective:**
- Create a new database called `company_db`.
- Inside it, create an `employees` table with the specified columns.
- Verify the table was created successfully.

**Tasks:**
1. Create a database called `company_db`.
2. Switch to `company_db` using the `USE` command.
3. Create a table called `employees` with these columns:
   - `id` — INT, Primary Key, Auto Increment
   - `name` — VARCHAR(100), NOT NULL
   - `position` — VARCHAR(100)
   - `salary` — INT
4. Run `SHOW TABLES;` to confirm the table was created.

**Expected SQL:**

```sql
CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

CREATE TABLE employees (
    id       INT          NOT NULL AUTO_INCREMENT,
    name     VARCHAR(100) NOT NULL,
    position VARCHAR(100),
    salary   INT,
    PRIMARY KEY (id)
);

SHOW TABLES;
```

---

#### Exercise 2: Insert and Retrieve Data

**Tasks:**
1. Insert at least 3 employee records into the `employees` table.
2. Retrieve all records using `SELECT *`.
3. Retrieve only the `name` and `salary` columns.
4. Retrieve only employees with a salary greater than 40000.

**Expected SQL:**

```sql
INSERT INTO employees (name, position, salary) VALUES
    ('Carlos Mendez', 'Software Engineer', 75000),
    ('Sofia Reyes',   'Product Manager',   90000),
    ('David Kim',     'Data Analyst',       55000);

-- Retrieve everything
SELECT * FROM employees;

-- Only name and salary
SELECT name, salary FROM employees;

-- Filter by salary
SELECT * FROM employees WHERE salary > 40000;
```

---

#### Exercise 3: Update and Delete Data

**Tasks:**
1. Give Carlos Mendez a raise — update his salary to 80000.
2. Delete David Kim's record from the table.
3. Run `SELECT * FROM employees;` after each change to verify the result.

**Expected SQL:**

```sql
-- Update salary
UPDATE employees
SET salary = 80000
WHERE name = 'Carlos Mendez';

SELECT * FROM employees; -- verify update

-- Delete a record
DELETE FROM employees WHERE name = 'David Kim';

SELECT * FROM employees; -- verify deletion
```

---

## Section 7: Summary & Real-World Applications

### 7. Summary & Key Takeaways

Excellent work making it through this lecture! Here is a recap of everything you have covered:

- A **database** is a structured collection of data. Relational databases organize data into tables connected by relationships.
- **Tables** consist of rows (individual records) and columns (data fields). Every table should have a Primary Key.
- **Foreign Keys** link tables together, allowing you to model real-world relationships between data.
- **SQL** is the standard language for interacting with relational databases. It is powerful, readable, and widely used.
- The four **CRUD operations** — CREATE, READ, UPDATE, DELETE — cover the vast majority of what you will do with a database.
- Always use **WHERE clauses** with `UPDATE` and `DELETE` to avoid accidentally changing or removing all your data.

#### Where SQL is Used in the Real World

| Industry / Field | How SQL is Used |
|---|---|
| Web Development | Storing user accounts, posts, comments, sessions, orders |
| Data Science | Querying large datasets for analysis, dashboards, and reports |
| Cybersecurity | Logging events, tracking intrusions, managing access controls |
| Finance & Banking | Transaction histories, account management, fraud detection |
| Healthcare | Patient records, appointment scheduling, medication tracking |
| E-Commerce | Products, inventory, customer orders, shipping data |

#### What's Next?

Now that you have the fundamentals, here are the topics you will explore in upcoming lessons:

- **JOINs** — Combining data from multiple tables in a single query.
- **Aggregate Functions** — `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` for calculating summaries.
- **GROUP BY and HAVING** — Grouping query results and applying conditions.
- **Indexes** — Speeding up queries on large datasets.
- **Transactions** — Ensuring data integrity across multiple operations.
- **Stored Procedures & Views** — Reusable query logic inside the database.

---

## Section 8: Q&A and Discussion

### 8. Q&A and Discussion

Use this time to reinforce understanding through questions and real-world scenarios.

#### Common Student Questions

**Q: What happens if I forget a semicolon at the end of a command?**
MySQL will wait for more input and display `->` instead of running the command. Simply type a semicolon and press Enter to execute it.

**Q: Is SQL case-sensitive?**
SQL keywords (`SELECT`, `FROM`, `WHERE`) are not case-sensitive. However, string values inside quotes may be case-sensitive depending on your database collation settings. It is best practice to always write SQL keywords in `UPPERCASE` for readability.

**Q: What's the difference between DELETE and DROP?**

```sql
DELETE FROM students WHERE id = 1;  -- Removes specific rows, table still exists
DROP TABLE students;                -- Removes the entire table structure and all data
DROP DATABASE school_db;            -- Removes the entire database
```

**Q: What if I update or delete without a WHERE clause?**
MySQL will apply the operation to every single row in the table. This is one of the most common and costly mistakes in SQL. Always double-check that your `WHERE` clause is correct before running `UPDATE` or `DELETE` commands.

---

#### Discussion Topics

- What kinds of data might a web application like a social media site need to store in a database?
- How would you design a database for a library system? What tables would you need?
- What are the risks of storing sensitive data (passwords, credit card numbers) in a database, and how can they be mitigated?
- Can you think of a situation where a NoSQL database might be a better choice than a relational database?

---

#### Debugging Tips for Common SQL Errors

| Error | Cause |
|---|---|
| `ERROR 1046 (No database selected)` | You forgot to run `USE database_name;` first. |
| `ERROR 1064 (Syntax error)` | Check for missing commas, parentheses, or semicolons. |
| `ERROR 1054 (Unknown column)` | Column name is misspelled or doesn't exist in the table. |
| `ERROR 1062 (Duplicate entry)` | You tried to insert a Primary Key value that already exists. |
