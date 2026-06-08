# HBnB UML Project — Teacher Introduction Guide

# Introduction

This project is designed to teach students how real software systems are planned before coding begins.

Instead of immediately building the application, students will first design the architecture and structure of the system using UML diagrams and technical documentation.

The project simulates the planning phase of a real-world software engineering project.

Students will learn how developers:
- organize applications into layers
- model business entities
- visualize system interactions
- document architecture professionally

The main goal is to help students develop **software design thinking**.

---

# What Students Will Be Doing

Students will create UML diagrams and technical documentation for a simplified AirBnB-like application called **HBnB Evolution**.

The application includes features such as:
- user accounts
- property listings
- reviews
- amenities

Students will NOT fully code the application in this project.

Instead, they will focus on designing:
- how the system is organized
- how components communicate
- how the entities relate to each other
- how requests move through the system

The project is divided into four main tasks.

---

# What Students Will Build

## 1. High-Level Package Diagram

Students will create a diagram showing the overall architecture of the application.

They will model:
- Presentation Layer
- Business Logic Layer
- Persistence Layer

They will also use the **Facade Pattern** to show how layers communicate.

This task helps students understand:
- separation of concerns
- layered architecture
- system organization

---

## 2. Detailed Class Diagram

Students will create a UML class diagram for the Business Logic Layer.

They will design the main entities:
- User
- Place
- Review
- Amenity

Students will define:
- attributes
- methods
- relationships
- inheritance
- multiplicity

This task helps students understand:
- object-oriented design
- relationships between entities
- system modeling

---

## 3. Sequence Diagrams

Students will create sequence diagrams for API requests.

The diagrams will show step-by-step how requests move through the system.

Students will model:
- User Registration
- Place Creation
- Review Submission
- Fetching Places

This task helps students understand:
- request flow
- interaction between layers
- runtime system behavior

---

## 4. Documentation Compilation

Students will organize all diagrams into professional technical documentation.

The final documentation will serve as a blueprint for future implementation.

Students will practice:
- technical writing
- documentation organization
- explaining design decisions
- professional formatting

---

# Main Concepts Students Will Learn

## Layered Architecture

Students will learn how applications are divided into layers with separate responsibilities.

### Presentation Layer
Handles:
- APIs
- requests
- responses
- user interaction

### Business Logic Layer
Handles:
- business rules
- application behavior
- core entities

### Persistence Layer
Handles:
- database operations
- saving and retrieving data

---

## UML Modeling

Students will use UML diagrams to visually represent software systems.

They will create:
- package diagrams
- class diagrams
- sequence diagrams

Students should understand that UML diagrams are:
- planning tools
- communication tools
- software blueprints

---

## Facade Pattern

Students will learn how the Facade Pattern simplifies communication between layers.

Instead of APIs directly interacting with every component, requests pass through a central facade.

Example:

```text
API → Facade → Business Logic → Persistence
```

This improves:
- organization
- maintainability
- separation of concerns

---

# Recommended Student Approach

## Step 1 — Understand the System

Before drawing diagrams, students should understand:
- what the application does
- who the main entities are
- how the entities interact

Questions students should ask:
- What is a User?
- What is a Place?
- What connects Reviews and Places?
- Why do Amenities exist?

---

## Step 2 — Identify Relationships

Students should carefully think about relationships between entities.

Examples:
- One user can own many places
- One place can receive many reviews
- Many places can share many amenities

This becomes the foundation of the class diagram.

---

## Step 3 — Think About Request Flow

Before creating sequence diagrams, students should think step-by-step about how requests work internally.

Example:

```text
What happens when a user registers?
```

Typical flow:
1. API receives request
2. Validation occurs
3. Business logic processes data
4. Persistence layer stores information
5. Response is returned

---

## Step 4 — Organize Documentation Professionally

Students should maintain a clean project structure.

Recommended structure:

```text
part1/
├── README.md
└── diagrams/
    ├── package_diagram.md
    ├── class_diagram.md
    └── sequence_diagrams.md
```

This teaches professional documentation organization.

---

# Common Student Mistakes

## Mixing Layer Responsibilities

Students often connect APIs directly to the database.

Reinforce:

```text
Presentation → Facade → Business Logic → Persistence
```

---

## Weak Relationship Modeling

Students sometimes forget multiplicity such as:
- one-to-many
- many-to-many

Encourage them to carefully think about how entities interact.

---

## Skipping Important Steps in Sequence Diagrams

Students often jump directly from request to response.

Remind them that systems usually involve:
- validation
- business processing
- database operations
- response generation

---

# Final Notes

This project is extremely important because it teaches students something many beginners skip:

## Designing software before building it.

Students are learning how professional developers:
- analyze systems
- organize architecture
- model entities
- visualize workflows
- communicate technical ideas

The goal is not just to complete diagrams.

The goal is to begin thinking like software engineers.