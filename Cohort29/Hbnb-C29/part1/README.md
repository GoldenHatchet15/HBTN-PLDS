# HBnB Evolution - Technical Documentation

## Project Information

- **Project Name**: HBnB Evolution
- **Project Type**: UML Technical Documentation
- **Repository**: holbertonschool-hbnb
- **Directory**: part1

---

# Introduction

## Project Overview

HBnB Evolution is a simplified AirBnB-like web application designed using a layered software architecture.

The platform allows users to:

- Register and manage accounts
- Create and manage property listings
- Leave reviews for places
- Manage amenities associated with places

The system is designed around object-oriented principles and UML modeling to create a clear blueprint before implementation begins.

---

## Purpose of This Document

This technical document provides a complete architectural and business logic overview of the HBnB Evolution application.

The purpose of this documentation is to:

- Define the overall architecture of the application
- Describe the Business Logic Layer and entity relationships
- Visualize system workflows through sequence diagrams
- Serve as a reference for future implementation phases

This document will guide developers during the implementation of the application.

---

# Documentation Contents

This document includes:

1. High-Level Architecture
2. Business Logic Layer
3. API Interaction Flow

---

# High-Level Architecture

## Overview

The HBnB Evolution application follows a three-layer architecture:

- Presentation Layer
- Business Logic Layer
- Persistence Layer

Communication between layers is coordinated through the facade pattern.

This architecture separates responsibilities and improves:

- Maintainability
- Scalability
- Code organization
- Separation of concerns

---

## Architecture Diagram

The High-Level Package Diagram can be found here:

[High-Level Package Diagram](./diagrams/0.package_diagram.md)

### Main Architectural Components

### Presentation Layer

Handles:

- API endpoints
- Request validation
- User interaction
- Response formatting

Examples:

- UserAPI
- PlaceAPI
- ReviewAPI
- AmenityAPI

---

### Business Logic Layer

Handles:

- Core business rules
- Entity models
- Application logic

Main entities:

- User
- Place
- Review
- Amenity

---

### Persistence Layer

Handles:

- Data storage
- Database communication
- Data retrieval
- Repository operations

Examples:

- UserRepository
- PlaceRepository
- ReviewRepository
- AmenityRepository

---

## Facade Pattern

The facade pattern acts as a communication bridge between the Presentation Layer and the Business Logic Layer.

Benefits of the facade pattern include:

- Reduced coupling
- Simplified interactions
- Better maintainability
- Centralized business operations

---

# Business Logic Layer

## Overview

The Business Logic Layer contains the core entities and business rules of the HBnB Evolution application.

The system uses an abstract `BaseModel` class to provide common attributes and methods for all entities.

Each entity contains:

- UUID4 unique identifier
- Creation timestamp
- Update timestamp

---

## Business Logic Diagram

The Detailed Class Diagram can be found here:

[Detailed Class Diagram](./diagrams/1.class_diagram.md)

---

## Main Entities

### User

Represents application users.

Responsibilities:

- User registration
- Profile management
- Authentication support

Relationships:

- Owns places
- Writes reviews

---

### Place

Represents property listings.

Responsibilities:

- Store listing information
- Manage amenities
- Associate with owners

Relationships:

- Belongs to a user
- Receives reviews
- Contains amenities

---

### Review

Represents user feedback for places.

Responsibilities:

- Store ratings
- Store comments
- Associate users and places

Relationships:

- Written by users
- Belongs to places

---

### Amenity

Represents features available at places.

Examples:

- WiFi
- Parking
- Pool
- Air conditioning

Relationships:

- Associated with multiple places

---

# API Interaction Flow

## Overview

Sequence diagrams are used to visualize how requests move through the system layers.

These diagrams show the communication between:

- Client
- API Layer
- Facade
- Business Models
- Persistence Layer
- Database

---

## Sequence Diagrams

The API sequence diagrams can be found here:

[Sequence Diagrams](./diagrams/2.sequence_diagrams.md)

---

## Included API Calls

### User Registration

Shows how a new user account is created and stored in the system.

---

### Place Creation

Shows how authenticated users create property listings.

---

### Review Submission

Shows how users submit reviews for places.

---

### Fetching Places

Shows how the system retrieves filtered lists of places.

---

# Design Decisions

## Layered Architecture

The application uses a layered architecture to clearly separate system responsibilities.

Benefits include:

- Cleaner code structure
- Easier maintenance
- Improved scalability
- Better testing capabilities

---

## BaseModel Inheritance

All entities inherit from `BaseModel`.

This avoids duplicated attributes and methods across entities.

Shared functionality includes:

- UUID identifiers
- Timestamps
- Common CRUD methods

---

## Facade Pattern

The facade pattern simplifies communication between layers.

Instead of allowing APIs to directly manipulate models and repositories, all interactions pass through the facade.

This improves:

- Modularity
- Maintainability
- Encapsulation

---

# Conclusion

This technical document provides a complete UML-based overview of the HBnB Evolution application.

The documentation includes:

- High-Level Package Diagram
- Detailed Class Diagram
- Sequence Diagrams for API workflows

Together, these diagrams define the architecture, business logic, and communication flow of the system.

This documentation serves as the foundation for future implementation phases of the project.

---

# References

- UML Documentation
- Mermaid.js Documentation
- Layered Architecture Pattern
- SOLID Principles
- Facade Design Pattern