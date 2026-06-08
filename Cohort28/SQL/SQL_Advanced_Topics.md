# SQL Advanced Topics
## Joins & User Privilege Management

> **Who is this for?** This lecture is for students who already know the basics of SQL — creating tables, inserting data, and running SELECT queries. Now we go one step further: combining data from multiple tables and controlling who can access your database.

---

## Table of Contents
1. [What is a JOIN and Why Do We Need It?](#1-what-is-a-join-and-why-do-we-need-it)
2. [The Four Types of Joins](#2-the-four-types-of-joins)
   - [INNER JOIN](#a-inner-join)
   - [LEFT JOIN](#b-left-join)
   - [RIGHT JOIN](#c-right-join)
   - [FULL OUTER JOIN](#d-full-outer-join)
3. [Managing User Privileges](#3-managing-user-privileges-in-mysql)
4. [Hands-On Exercises](#4-hands-on-exercises)
5. [Summary & Recap](#5-summary--recap)
6. [Q&A and Discussion](#6-qa-and-discussion)

---

## 1. What is a JOIN and Why Do We Need It?

### The Problem

Imagine you are building a database for a company. You have two tables:

- An **employees** table that stores each employee's name and salary.
- A **departments** table that stores each department's name.

You want to answer questions like:
- *"What department does Alice work in?"*
- *"Which employees belong to Engineering?"*
- *"Are there any departments with no employees yet?"*

Each employee has a `department_id` column that points to a department. But if you look at the employees table alone, you only see a number like `1` or `2` — not the actual department name. To get the name, you need to look it up in the departments table.

A **JOIN** is how SQL connects two tables so you can see information from both in one result.

---

### Setting Up Our Example Data

Before we look at any JOIN, let's create the two tables we will use throughout this lecture. Run this in your MySQL terminal:

```sql
-- First, create the departments table
CREATE TABLE departments (
    id              INT NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Then create the employees table
-- department_id connects each employee to a department
CREATE TABLE employees (
    id            INT NOT NULL AUTO_INCREMENT,
    name          VARCHAR(100) NOT NULL,
    department_id INT,
    salary        INT,
    PRIMARY KEY (id)
);

-- Add three departments
INSERT INTO departments (department_name) VALUES
    ('Engineering'),   -- gets id = 1
    ('Marketing'),     -- gets id = 2
    ('HR');            -- gets id = 3

-- Add four employees
-- Notice: Carlos has NULL for department_id (not assigned yet)
INSERT INTO employees (name, department_id, salary) VALUES
    ('Alice Rivera',   1,    75000),
    ('John Doe',       1,    80000),
    ('Maria Santos',   2,    65000),
    ('Carlos Mendez',  NULL, 50000);
```

Here is what our data looks like right now:

**employees table:**

| id | name           | department_id | salary |
|----|----------------|---------------|--------|
| 1  | Alice Rivera   | 1             | 75000  |
| 2  | John Doe       | 1             | 80000  |
| 3  | Maria Santos   | 2             | 65000  |
| 4  | Carlos Mendez  | NULL          | 50000  |

**departments table:**

| id | department_name |
|----|-----------------|
| 1  | Engineering     |
| 2  | Marketing       |
| 3  | HR              |

> **Two important things to notice:**
> - **Carlos** has `NULL` for `department_id` — he has not been assigned to a department yet.
> - **HR** (id = 3) exists in the departments table, but no employee points to it — it currently has no employees.
>
> These two "gaps" will behave differently depending on which JOIN you use. Keep them in mind as you read through the examples.

---

### How a JOIN Works — The Big Picture

Every JOIN needs three things:

1. **Two tables** — the ones you want to combine.
2. **A shared column** — the column that links them. Here: `employees.department_id` and `departments.id`.
3. **A join type** — tells SQL what to do when there is no match on one side.

The basic JOIN syntax looks like this:

```sql
SELECT columns_you_want
FROM left_table
JOIN_TYPE right_table
ON left_table.shared_column = right_table.shared_column;
```

The table you write after `FROM` is called the **left table**.
The table you write after `JOIN` is called the **right table**.
This distinction matters a lot for LEFT JOIN and RIGHT JOIN.

---

## 2. The Four Types of Joins

A helpful way to picture joins is to imagine two overlapping circles — like a Venn diagram:

```
     employees          departments
    [  Carlos  [ Alice  ]  HR  ]
               [ John   ]
               [ Maria  ]
       left      middle    right
      only      (matched)  only
```

- The **middle** = employees who have a matching department (Alice, John, Maria).
- The **left only** side = employees with no department match (Carlos).
- The **right only** side = departments with no employee match (HR).

Each JOIN type decides which of these zones to include in the result.

---

### a) INNER JOIN

**Returns only rows that have a match in BOTH tables.**

This is the most common type of JOIN. It only includes the middle of the Venn diagram — rows that successfully connect between both tables. Any row that has no match on the other side is simply left out.

```
     employees          departments
    [          [ Alice  ]          ]
               [ John   ]
               [ Maria  ]
                  ↑
            Only the matched middle
```

#### Example

```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;
```

Let's walk through what this query does, line by line:

1. `FROM employees` — start with the employees table.
2. `INNER JOIN departments` — bring in the departments table.
3. `ON employees.department_id = departments.id` — only connect rows where these two values are equal.
4. `SELECT employees.name, departments.department_name` — show only these two columns in the result.

**Result:**

| name          | department_name |
|---------------|-----------------|
| Alice Rivera  | Engineering     |
| John Doe      | Engineering     |
| Maria Santos  | Marketing       |

#### Why are Carlos and HR missing?

- **Carlos Mendez** — his `department_id` is `NULL`. NULL doesn't equal any id, so there is no match. INNER JOIN excludes him.
- **HR** — no employee has `department_id = 3`, so HR has no match in the employees table. INNER JOIN excludes it too.

> **When to use INNER JOIN:**
> Use it when you only want complete, matched data. For example: *"Show me all employees who have been assigned to a department."*

---

### b) LEFT JOIN

**Returns ALL rows from the left table, plus matching rows from the right table. Where there is no match, the right-side columns show NULL.**

LEFT JOIN says: *"Give me everything from the left table — and if a right-side match exists, include it. If not, just put NULL."*

```
     employees          departments
    [  Carlos  [ Alice  ]          ]
               [ John   ]
               [ Maria  ]
         ↑         ↑
    Carlos        Matched
    (NULL on      employees
     right side)
```

#### Example

```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.id;
```

The only change from INNER JOIN is replacing `INNER JOIN` with `LEFT JOIN`.

**Result:**

| name           | department_name |
|----------------|-----------------|
| Alice Rivera   | Engineering     |
| John Doe       | Engineering     |
| Maria Santos   | Marketing       |
| Carlos Mendez  | NULL            |

#### What changed?

Carlos Mendez now appears in the result! Even though he has no matching department, LEFT JOIN says *"include him anyway — just put NULL where the department name would be."*

HR still does not appear because it lives in the **right** table (departments), and LEFT JOIN only guarantees that the **left** table (employees) is fully included.

> **When to use LEFT JOIN:**
> Use it when you want all records from the main table, even incomplete ones. For example: *"Show me all employees, and if they have a department, show it."*

#### Bonus tip — Finding unassigned employees

You can combine LEFT JOIN with `WHERE ... IS NULL` to find employees that have NO department at all:

```sql
SELECT employees.name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
WHERE departments.id IS NULL;
```

After a LEFT JOIN, any employee with no matching department will have `NULL` in every `departments` column. Filtering for `WHERE departments.id IS NULL` gives you exactly those unmatched employees.

---

### c) RIGHT JOIN

**Returns ALL rows from the right table, plus matching rows from the left table. Where there is no match, the left-side columns show NULL.**

RIGHT JOIN is the mirror image of LEFT JOIN. Instead of guaranteeing everything from the left, it guarantees everything from the **right** table.

```
     employees          departments
    [          [ Alice  ]   HR   ]
               [ John   ]
               [ Maria  ]
                   ↑          ↑
               Matched       HR
               employees  (NULL on
                           left side)
```

#### Example

```sql
SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.id;
```

**Result:**

| name          | department_name |
|---------------|-----------------|
| Alice Rivera  | Engineering     |
| John Doe      | Engineering     |
| Maria Santos  | Marketing       |
| NULL          | HR              |

#### What changed?

HR now appears with `NULL` in the name column — because no employee belongs to HR, but RIGHT JOIN guarantees that all departments show up.

Carlos disappears again because he is in the **left** table (employees), and RIGHT JOIN does not guarantee the left table is fully included.

> **When to use RIGHT JOIN:**
> Use it when you want all records from the second (right) table. For example: *"Show me all departments, and if they have employees, show them."*

> **Practical tip:** RIGHT JOIN is rarely used in practice. You can always get the same result by swapping the table order and using LEFT JOIN. Both of these queries return identical results:
>
> ```sql
> -- Using RIGHT JOIN
> SELECT e.name, d.department_name
> FROM employees AS e
> RIGHT JOIN departments AS d ON e.department_id = d.id;
>
> -- Using LEFT JOIN with tables swapped (same result)
> SELECT e.name, d.department_name
> FROM departments AS d
> LEFT JOIN employees AS e ON e.department_id = d.id;
> ```

---

### d) FULL OUTER JOIN

**Returns ALL rows from BOTH tables. Matched rows are combined. Unmatched rows appear with NULL on the missing side.**

This is the most complete join. It shows everything — matched rows in the middle, AND the unmatched rows from both sides.

```
     employees          departments
    [  Carlos  [ Alice  ]   HR   ]
               [ John   ]
               [ Maria  ]
         ↑         ↑          ↑
     Carlos      Matched      HR
     (NULL on    employees  (NULL on
      right)                 left)
```

#### Example

```sql
SELECT employees.name, departments.department_name
FROM employees
FULL OUTER JOIN departments
ON employees.department_id = departments.id;
```

**Expected result:**

| name           | department_name |
|----------------|-----------------|
| Alice Rivera   | Engineering     |
| John Doe       | Engineering     |
| Maria Santos   | Marketing       |
| Carlos Mendez  | NULL            |
| NULL           | HR              |

#### Important: MySQL does NOT support FULL OUTER JOIN

If you run that query in MySQL, you will get an error. MySQL is simply missing this feature. However, you can get the exact same result by combining a LEFT JOIN and a RIGHT JOIN with `UNION`:

```sql
-- Get all employees + their departments (or NULL)
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id

UNION

-- Get all departments + their employees (or NULL)
SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;
```

`UNION` combines the results of both queries into one list and automatically removes duplicate rows. The final result is equivalent to FULL OUTER JOIN.

> **When to use FULL OUTER JOIN:**
> Use it when you need to see everything and can't afford to miss anything. For example: *"Give me a full audit showing all employees AND all departments, and flag anything that has no connection."*

---

### All Four JOINs at a Glance

| Join Type      | Carlos appears? | HR appears? | Use when...                                 |
|----------------|-----------------|-------------|---------------------------------------------|
| `INNER JOIN`   | ❌ No           | ❌ No       | You only want fully matched records         |
| `LEFT JOIN`    | ✅ Yes (NULL)   | ❌ No       | You need all records from the left table    |
| `RIGHT JOIN`   | ❌ No           | ✅ Yes (NULL)| You need all records from the right table   |
| `FULL OUTER`   | ✅ Yes (NULL)   | ✅ Yes (NULL)| You need everything from both tables        |

---

### Cleaner Queries with Table Aliases

Writing `employees.name` and `departments.department_name` over and over gets long and messy. SQL lets you give tables short nicknames called **aliases** using the `AS` keyword:

```sql
-- Long version
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;

-- Short version using aliases — same result
SELECT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.id;
```

`AS e` means "within this query, refer to `employees` as just `e`." You can pick any name you like. Short aliases become especially useful when joining three or more tables.

---

## 3. Managing User Privileges in MySQL

### Why Does This Matter?

Think about a web application connected to a MySQL database. The app uses a database account to run queries. Now imagine a security vulnerability in the app gives an attacker access to that account.

- If the account had `ALL PRIVILEGES` → the attacker can delete your entire database.
- If the account only had `SELECT` → the attacker can only read data, nothing else.

This is why controlling what each user can do is so important. The guiding rule is:

> **Give users only the permissions they actually need — nothing more.**

This is called the **Principle of Least Privilege**, and it's a fundamental concept in database security.

---

### What Kinds of Privileges Exist?

| Privilege        | What the user can do                  | Who typically needs it |
|------------------|---------------------------------------|------------------------|
| `SELECT`         | Read and query data from tables       | Reporting tools, analysts |
| `INSERT`         | Add new rows to tables                | Applications that create records |
| `UPDATE`         | Change existing data in tables        | Applications that edit records |
| `DELETE`         | Remove rows from tables               | Admins, trusted apps |
| `CREATE`         | Create new tables or databases        | Developers |
| `DROP`           | Delete tables or databases            | DBAs only |
| `ALL PRIVILEGES` | Everything — full control             | Trusted admins only |

---

### Privilege Scopes — How Specific Can You Get?

You can apply privileges at different levels of specificity:

```sql
-- All databases on the entire server (very broad)
GRANT SELECT ON *.* TO 'user'@'localhost';

-- Everything inside one specific database
GRANT SELECT ON school_db.* TO 'user'@'localhost';

-- Only one specific table inside one database
GRANT SELECT ON school_db.students TO 'user'@'localhost';
```

The narrower the scope, the safer. A reporting user who only needs to read from `school_db` should not have access to other databases on the same server.

---

### a) Checking What Privileges a User Has

Before making any changes, it is good practice to first see what a user can already do:

```sql
-- Check what privileges a specific user has
SHOW GRANTS FOR 'user_0d_1'@'localhost';
```

The output might look like this:
```
GRANT SELECT, INSERT ON school_db.* TO 'user_0d_1'@'localhost'
```

This tells you: `user_0d_1` (connecting from the same machine) can run `SELECT` and `INSERT` on everything inside `school_db`, but nothing else.

---

### Understanding `'username'@'host'`

Every MySQL user has two parts — a username AND a host. The host controls **where the user is allowed to connect from**:

| Host             | What it means                                 |
|------------------|-----------------------------------------------|
| `'localhost'`    | Can only connect from the same computer       |
| `'%'`            | Can connect from anywhere (any IP address)    |
| `'192.168.1.10'` | Can only connect from that one specific IP    |

For local development, `'localhost'` is fine. On a real production server, always be as specific as possible.

---

### b) Creating a New User and Granting Privileges

You always create the user first, then grant privileges in a separate step.

#### Creating a superuser (full access)

Appropriate for a trusted admin or developer who needs to manage everything:

```sql
-- Step 1: Create the user account with a password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Step 2: Grant full access to all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Step 3: Apply the changes right away
FLUSH PRIVILEGES;
```

> **What does `FLUSH PRIVILEGES` do?**
> MySQL stores permission information in memory for speed. `FLUSH PRIVILEGES` tells it to reload that information from the database right now. You should always run it after granting or revoking any permissions to make sure your changes take effect immediately.

#### Creating a read-only user (restricted access)

Appropriate for a reporting tool or a student who should only be able to view data:

```sql
-- Create the user account
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT on one specific database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
```

Now `user_0d_2` can run `SELECT` queries on `hbtn_0d_2`, but cannot `INSERT`, `UPDATE`, `DELETE`, or `DROP` anything. If they try, MySQL will return an "Access denied" error.

---

### c) Revoking a Privilege

If a user no longer needs a certain privilege, use `REVOKE` to remove it without deleting their account:

```sql
-- Remove the SELECT privilege from user_0d_2 on hbtn_0d_2
REVOKE SELECT ON hbtn_0d_2.* FROM 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

-- Confirm it worked
SHOW GRANTS FOR 'user_0d_2'@'localhost';
```

`REVOKE` has the opposite effect of `GRANT` and uses the same syntax. After revoking, the user account still exists — the user can still log in, they just no longer have that specific permission.

---

### d) Deleting a User

When an account is no longer needed at all, delete it completely:

```sql
-- Delete the user account entirely
DROP USER 'user_0d_2'@'localhost';
```

After this command, `user_0d_2` is gone. They cannot log in, and all their permissions are removed.

#### What is the difference between REVOKE and DROP USER?

| | `REVOKE` | `DROP USER` |
|---|---|---|
| What it does | Removes a specific permission | Removes the entire account |
| Can the user still log in? | Yes | No |
| Is the account still there? | Yes | No |
| Analogy | Taking away one room key | Canceling the entire access card |

---

## 4. Hands-On Exercises

### Exercise 1: Practice JOINs

Make sure the `employees` and `departments` tables are set up from the beginning of this lecture.

**Step 1:** Verify your data is correct.
```sql
SELECT * FROM employees;    -- should return 4 rows
SELECT * FROM departments;  -- should return 3 rows
```

**Step 2:** Write an `INNER JOIN` to show each employee's name alongside their department name.
- Expected result: 3 rows — Carlos should NOT appear.

**Step 3:** Write a `LEFT JOIN` to show ALL employees, along with their department name (or NULL if they don't have one).
- Expected result: 4 rows — Carlos appears with NULL.

**Step 4:** Write a `RIGHT JOIN` to show ALL departments, along with their employees (or NULL if the department has no employees).
- Expected result: 4 rows — HR appears with NULL.

**Step 5:** Simulate a `FULL OUTER JOIN` using `UNION`.
- Expected result: 5 rows — both Carlos and HR appear.

**Step 6:** Rewrite your INNER JOIN from Step 2 using aliases: `e` for employees and `d` for departments.

---

### Exercise 2: Managing Users

**Step 1:** Create a user `db_admin` with all privileges on all databases.
```sql
CREATE USER 'db_admin'@'localhost' IDENTIFIED BY 'Admin@Secure123';
GRANT ALL PRIVILEGES ON *.* TO 'db_admin'@'localhost';
FLUSH PRIVILEGES;
```

**Step 2:** Create a user `db_reader` with only `SELECT` access on `company_db`.
```sql
CREATE USER 'db_reader'@'localhost' IDENTIFIED BY 'Reader@Secure456';
GRANT SELECT ON company_db.* TO 'db_reader'@'localhost';
FLUSH PRIVILEGES;
```

**Step 3:** Verify both users' grants.
```sql
SHOW GRANTS FOR 'db_admin'@'localhost';
SHOW GRANTS FOR 'db_reader'@'localhost';
```

**Step 4:** Grant `INSERT` and `UPDATE` on just the `employees` table to `db_reader`.
```sql
GRANT INSERT, UPDATE ON company_db.employees TO 'db_reader'@'localhost';
FLUSH PRIVILEGES;
```

**Step 5:** Revoke the `INSERT` privilege from `db_reader` and verify it's gone.
```sql
REVOKE INSERT ON company_db.employees FROM 'db_reader'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'db_reader'@'localhost';
```

**Step 6:** Delete the `db_reader` account entirely.
```sql
DROP USER 'db_reader'@'localhost';
```

---

## 5. Summary & Recap

### SQL Joins

A JOIN connects rows from two tables based on a shared column.

- **`INNER JOIN`** — only shows rows that match in both tables. Unmatched rows are excluded.
- **`LEFT JOIN`** — shows everything from the left table. Missing matches from the right appear as NULL.
- **`RIGHT JOIN`** — shows everything from the right table. Missing matches from the left appear as NULL.
- **`FULL OUTER JOIN`** — shows everything from both tables. Simulated in MySQL with `UNION`.
- **Aliases** (`AS e`, `AS d`) make your queries shorter and easier to read.

### User Privileges

- **`GRANT`** — gives a user a specific permission.
- **`REVOKE`** — removes a specific permission (the account stays).
- **`DROP USER`** — deletes the account entirely.
- **`SHOW GRANTS FOR`** — shows what a user is allowed to do.
- **`FLUSH PRIVILEGES`** — applies your changes immediately.
- Always follow the **Principle of Least Privilege** — only give users what they actually need.

### New Commands Introduced

| Command | What It Does |
|---------|-------------|
| `INNER JOIN ... ON` | Returns only matched rows from both tables |
| `LEFT JOIN ... ON` | Returns all rows from the left table |
| `RIGHT JOIN ... ON` | Returns all rows from the right table |
| `UNION` | Combines results of two queries, removing duplicates |
| `CREATE USER` | Creates a new database user account |
| `GRANT ... ON ... TO` | Gives a user a permission |
| `REVOKE ... ON ... FROM` | Takes away a permission from a user |
| `SHOW GRANTS FOR` | Shows all permissions a user has |
| `FLUSH PRIVILEGES` | Applies privilege changes immediately |
| `DROP USER` | Deletes a user account completely |

---

## 6. Q&A and Discussion

### Common Questions

---

**Q: Why do we split data across multiple tables instead of putting everything in one big table?**

Imagine storing the department name and location inside the employees table. If Engineering moves to a different building, you'd have to update that information for every single engineer — potentially hundreds of rows. With separate tables, you update one row in the departments table and every employee automatically reflects the change. This approach also prevents typos and inconsistencies. This concept is called **database normalization**, and it's one of the core principles of good database design.

---

**Q: My JOIN returned way more rows than I expected. What happened?**

This usually means there are duplicate matching values in one of your tables. For example, if three employees all have `department_id = 1`, and you join with departments, each of those three employees will appear once for each matching department row. Double-check your `ON` condition and make sure you are joining on the right columns. Adding `DISTINCT` can help remove exact duplicate rows:

```sql
SELECT DISTINCT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.id;
```

---

**Q: What happens if I accidentally run UPDATE or DELETE without a WHERE clause?**

It applies to **every single row** in the table. For example:

```sql
-- This does NOT delete one employee — it deletes ALL of them
DELETE FROM employees;

-- This sets EVERY employee's salary to 0
UPDATE employees SET salary = 0;
```

This is one of the most common and costly mistakes in SQL. Always write and double-check your `WHERE` clause before running `UPDATE` or `DELETE`. A good habit: run a `SELECT` with the same `WHERE` clause first to confirm you're targeting the right rows.

---

**Q: Do I really need FLUSH PRIVILEGES every time?**

In MySQL 8 and newer, `GRANT` and `REVOKE` often take effect immediately without it. But it is still best practice to always run `FLUSH PRIVILEGES`. On older MySQL versions, forgetting it means your changes might not apply until the server restarts — which leads to confusing bugs where you granted a permission but the user still gets "Access denied."

---

**Q: Can I join more than two tables at once?**

Yes. You can chain multiple JOINs in a single query:

```sql
-- Join three tables together
SELECT e.name, d.department_name, l.building
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.id
INNER JOIN locations AS l ON d.location_id = l.id;
```

Each `JOIN ... ON` adds another table to the result. The aliases become very important here to keep things readable.

---

### Discussion Topics

- Think about a social media app like Instagram. What tables might it have? How would you use JOINs to show a user's posts along with their profile picture and username?
- If you were the database admin for your school, what privileges would you give to a student, a teacher, and an IT admin? Why would they differ?
- Can you think of a real-world situation where accidentally running `DELETE FROM table;` without a `WHERE` clause could cause a serious problem?
- Why might a company create a separate read-only database user for their analytics team instead of sharing the main application account?

---

### Common Error Messages and What They Mean

| Error | What it means | How to fix it |
|-------|---------------|---------------|
| `ERROR 1064: Syntax error` | Typo in your SQL | Check for missing commas, quotes, or semicolons |
| `ERROR 1046: No database selected` | You forgot to run `USE database_name;` | Run `USE your_database;` first |
| `ERROR 1044: Access denied for user` | The user lacks permission | Check with `SHOW GRANTS` and use `GRANT` to add it |
| `ERROR 1396: CREATE USER failed` | That username already exists | Use `CREATE USER IF NOT EXISTS` |
| `JOIN returns 0 rows` | The column values don't match | Verify the data types and values in both join columns |
