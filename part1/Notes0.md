# 📦 HBnB – Part 1: Technical Documentation

This document contains explanatory notes for **Task 0 and Task 1** of the HBnB Evolution project.  
It explains the architectural choices made before starting the implementation.

------------------------------------------------------------------

# 🧱 TASK 0 — High-Level Package Diagram

## Global Architecture Overview

Presentation
     |
     v
   Facade (Business Layer)
     |
     v
Business Entities
     |
     v
Persistence

------------------------------------------------------------------

## 🎯 Objective

The goal of Task 0 is to present a high-level view of the HBnB application architecture.

This diagram helps to understand:

- how the application is structured,
- how responsibilities are separated,
- how different parts of the system interact.

The architecture follows a layered design pattern.  
This approach separates technical responsibilities from business responsibilities.

------------------------------------------------------------------

## 🧩 General Structure

The system is divided into three main layers:

1. Presentation Layer  
2. Business Logic Layer  
3. Persistence Layer  

Each layer has a clearly defined responsibility.

------------------------------------------------------------------

## 1️⃣ Presentation Layer

The Presentation Layer is the entry point of the application.

It handles requests coming from:

- users,
- HTTP clients,
- front-end applications,
- or external systems.

It exposes APIs (Application Programming Interfaces).  
An API allows clients to interact with the system, for example:

- create a user,
- create a place,
- submit a review,
- retrieve places.

Main responsibilities:

- receive client requests,
- validate request format and parameters,
- forward the request to the Business Layer,
- return an HTTP response.

This layer does NOT:

- contain business rules,
- access the database directly.

It only acts as an interface between the outside world and the application core.

------------------------------------------------------------------

## 2️⃣ Business Logic Layer

The Business Logic Layer represents the core of the system.

It contains:

- business rules,
- domain models.

Business rules define how the system behaves.  
For example:

- a User can create a Place,
- a Review must be linked to both a User and a Place.

The main domain entities are:

- User
- Place
- Review
- Amenity

Each entity defines:

- attributes (state),
- methods (behavior),
- relationships with other entities.

------------------------------------------------------------------

### 🔹 The Role of the Facade

The Business Layer exposes a Facade.

The Facade provides a simplified interface to the business logic.

Instead of interacting directly with entities,  
the Presentation Layer always calls the Facade.

The Facade:

- coordinates business operations,
- applies validation rules,
- communicates with the Persistence Layer.

Benefits of using a Facade:

- reduces coupling between layers,
- protects internal business logic,
- centralizes use cases,
- improves maintainability.

------------------------------------------------------------------

## 3️⃣ Persistence Layer

The Persistence Layer is responsible for data management.

Its main responsibilities are:

- storing application data,
- retrieving stored data,
- abstracting the storage mechanism.

It interacts with the database system.

This layer:

- does not apply business rules,
- does not make functional decisions,
- only performs read and write operations.

It is used exclusively by the Business Logic Layer.

------------------------------------------------------------------

## 🔁 Layer Communication

The communication between layers follows a strict direction:

Presentation Layer  
        ↓  
Business Logic Layer (via Facade)  
        ↓  
Persistence Layer  

The Persistence Layer never calls upper layers.

This structure ensures:

- clear separation of concerns,
- better code organization,
- easier maintenance,
- improved scalability.

------------------------------------------------------------------

