# 🧠 TASK 1 — Detailed Class Diagram

## Business Logic Layer Documentation

------------------------------------------------------------------

### 📌 Scope of Task 1

Task 1 focuses ONLY on the Business Logic Layer.

Included:

- Domain entities
- Business rules
- Relationships between entities

Excluded:

- API endpoints / controllers
- Facade implementation
- Database / repositories / persistence logic

The goal is to model the domain, not the technical infrastructure.

------------------------------------------------------------------

### 📐 Purpose of a Class Diagram

A UML class diagram answers four main questions:

1. What classes exist in the system?
2. What data do they contain (attributes)?
3. What behaviors do they define (methods)?
4. How are they connected (UML relationships)?

This diagram represents the structure of the business domain.

------------------------------------------------------------------

### 🧩 Domain Entities

The required entities are:

- User
- Place
- Review
- Amenity

These are business concepts, independent from programming language or database technology.

------------------------------------------------------------------

### 📄 Attributes

All entities share common attributes:

- id (UUID4)
- created_at
- updated_at

To avoid duplication, these attributes can be defined in a parent class:

BaseModel

Each entity inherits from BaseModel.

Specific attributes per entity:

User:
- first_name
- last_name
- email
- password
- is_admin

Place:
- title
- description
- price
- latitude
- longitude

Review:
- rating
- comment

Amenity:
- name
- description

------------------------------------------------------------------

### ⚙️ Business Methods

Methods represent business behavior, not technical operations.

Examples of valid business methods:

- User.update_profile()
- Place.add_amenity()
- Place.remove_amenity()
- Review.update_content()
- Amenity.update_info()

Important:
There are NO persistence methods here (no save(), no SQL, no database logic).

------------------------------------------------------------------

### 🧬 Inheritance

All entities inherit from BaseModel.

UML notation:

User --|> BaseModel  
Place --|> BaseModel  
Review --|> BaseModel  
Amenity --|> BaseModel  

This ensures shared identity and timestamps across the system.

------------------------------------------------------------------

### 🔗 Business Relationships

User ↔ Place (Ownership)

- A User can own 0..* Places
- A Place has exactly 1 owner (User)

UML:
User "1" --> "0..*" Place : owns

--------------------------------------------------

User ↔ Review (Author)

- A User can write 0..* Reviews
- A Review is written by exactly 1 User

UML:
User "1" --> "0..*" Review : writes

--------------------------------------------------

Place ↔ Review (Target)

- A Place can have 0..* Reviews
- A Review belongs to exactly 1 Place

UML:
Place "1" --> "0..*" Review : has

--------------------------------------------------

Place ↔ Amenity (Many-to-Many)

- A Place can include 0..* Amenities
- An Amenity can belong to 0..* Places

UML:
Place "0..*" -- "0..*" Amenity : includes

------------------------------------------------------------------

### 🧪 Validation Questions

To verify the correctness of the diagram, we must be able to answer:

- Who owns a Place? → A User
- Who can write a Review? → A User
- What is an Amenity? → A feature that can be linked to multiple Places

If these answers are clear from the diagram, then the business model is consistent.

------------------------------------------------------------------

