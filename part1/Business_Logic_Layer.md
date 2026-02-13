# Business Logic Layer – Detailed Class Diagram

```mermaid
classDiagram

%% =========================
%% Base Abstract Model
%% =========================

class BaseEntity {
    <<abstract>>
    +UUID id
    +datetime created_at
    +datetime updated_at
    +touch()
}

%% =========================
%% Core Entities
%% =========================

class User {
    +string first_name
    +string last_name
    +string email
    +string password_hash
    +boolean is_admin
    +update_profile(data)
    +activate_admin()
}

class Place {
    +string title
    +string description
    +decimal price_per_night
    +float latitude
    +float longitude
    +update_details(data)
    +add_amenity(Amenity)
    +remove_amenity(Amenity)
}

class Review {
    +int rating
    +string comment
    +edit_review(text)
}

class Amenity {
    +string name
    +string description
    +rename(new_name)
}

%% =========================
%% Inheritance
%% =========================

BaseEntity <|-- User
BaseEntity <|-- Place
BaseEntity <|-- Review
BaseEntity <|-- Amenity

%% =========================
%% Relationships
%% =========================

User "1" --> "0..*" Place : creates
User "1" --> "0..*" Review : authors
Place "1" --> "0..*" Review : contains
Place "1" o-- "0..*" Amenity : composed_of
Review --> User
Review --> Place

