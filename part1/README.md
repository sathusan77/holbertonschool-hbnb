HBnB – Part 1: UML Design

This section presents the architectural and conceptual modeling of the HBnB application.

The goal of Part 1 is to design a clear and well-structured foundation before starting the implementation phase.
The diagrams created in this part represent how the system is organized, how the main domain entities are structured, and how different layers interact with each other.

Overview

Part 1 is organized into three main components:

1. High-Level Architecture

📄 high_level_package_diagram.md

This diagram provides a global view of the system architecture based on a layered approach:

Presentation Layer

Business Logic Layer

Persistence Layer

It also highlights the use of the Facade pattern, which acts as a single entry point to the business logic and helps maintain a clear separation between layers.

2. Business Logic Layer – Class Diagram

📄 Business_Logic_Layer.md

This diagram focuses on the main domain entities of the application:

User

Place

Review

Amenity

It defines:

The attributes of each entity

The shared properties through inheritance

The relationships and multiplicities between entities

This modeling step describes the functional structure of the system without being tied to technical implementation details.

3. API Interaction Flow – Sequence Diagrams

📄 Diagrams_API_Calls.md

These diagrams show how API requests move through the different system layers.

They illustrate:

Input validation handled by the Presentation Layer

Business rule processing coordinated by the Facade

Data storage managed by the Persistence Layer

This ensures that the runtime behavior of the system follows the architecture defined in the design phase.HBNB
