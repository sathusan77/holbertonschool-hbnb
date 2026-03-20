# HBnB - Part 3: Backend Amélioré avec Authentification et Base de Données

## Description
Implementation of the Backend, Authentication, and Database Integration for the HBnB application using Python, Flask, SQLAlchemy, and JWT.  
This part replaces in-memory storage with a persistent database (SQLite for development) and adds role-based access control.

## Project Structure

    part3/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   └── v1/
    │   │       ├── users.py
    │   │       ├── places.py
    │   │       ├── reviews.py
    │   │       └── amenities.py
    │   ├── models/
    │   │   ├── base_model.py
    │   │   ├── user.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   ├── amenity.py
    │   │   └── association.py
    │   ├── services/
    │   │   └── facade.py
    │   └── persistence/
    │       ├── repository.py
    │       └── sqlalchemy_repository.py
    ├── run.py
    ├── part3_init.sql
    ├── docs/
    │   └── ERD_part3.png
    ├── README.md
    └── requirements.txt

## Installation

1. Créer un environnement virtuel :

    python3 -m venv venv
    source venv/bin/activate

2. Installer les dépendances :

    pip install -r requirements.txt

> Exemple de `requirements.txt` :


3. Initialiser la base de données SQLite :

    sqlite3 hbnb.db < part3_init.sql

---

## Run

    python3 run.py

- Swagger UI available at: http://localhost:5000
- Use `/api/v1/auth/login` to get a JWT token for protected endpoints.

---

## API Endpoints

### Users
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /api/v1/users/ | List all users | Admin only |
| POST | /api/v1/users/ | Create a user | Admin only |
| GET | /api/v1/users/<id> | Get a user | Admin or owner |
| PUT | /api/v1/users/<id> | Update a user | Admin or owner |

### Amenities
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /api/v1/amenities/ | List all amenities | Public |
| POST | /api/v1/amenities/ | Create an amenity | Admin only |
| GET | /api/v1/amenities/<id> | Get an amenity | Public |
| PUT | /api/v1/amenities/<id> | Update an amenity | Admin only |
| DELETE | /api/v1/amenities/<id> | Delete an amenity | Admin only |

### Places
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /api/v1/places/ | List all places | Public |
| POST | /api/v1/places/ | Create a place | Authenticated user |
| GET | /api/v1/places/<id> | Get a place with owner and amenities | Public |
| PUT | /api/v1/places/<id> | Update a place | Owner or admin |
| DELETE | /api/v1/places/<id> | Delete a place | Owner or admin |

### Reviews
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /api/v1/reviews/ | List all reviews | Public |
| POST | /api/v1/reviews/ | Create a review | Authenticated user |
| GET | /api/v1/reviews/<id> | Get a review | Public |
| PUT | /api/v1/reviews/<id> | Update a review | Owner or admin |
| DELETE | /api/v1/reviews/<id> | Delete a review | Owner or admin |
| GET | /api/v1/reviews/places/<id> | Get all reviews for a place | Public |

---

## Architecture

- Presentation Layer: Flask + Flask-RESTX (REST API + Swagger doc)  
- Business Logic Layer: Models with validation + Facade pattern  
- Persistence Layer: SQLAlchemy Repository (SQLite for dev, MySQL for prod)  
- Authentication: JWT with role-based access (admin vs user)  
- Passwords hashed with bcrypt  

---

## Database Models

- **User**: id, email, first_name, last_name, password (hashed), is_admin  
- **Place**: id, name, description, city, state, country, price_by_night, number_rooms, number_bathrooms, max_guest, latitude, longitude, user_id  
- **Review**: id, text, user_id, place_id  
- **Amenity**: id, name  
- **place_amenity**: association table for Place ↔ Amenity  

### Relationships
- `User` → `Place` (1-N)  
- `User` → `Review` (1-N)  
- `Place` → `Review` (1-N)  
- `Place` ↔ `Amenity` (N-N via place_amenity)  

---

## ER Diagram

![HBnB ER Diagram](docs/ERD_part3.png)

> Diagram generated using Mermaid.js and exported as PNG for GitHub.

---

## Notes

- Passwords are hashed with bcrypt  
- Emails are unique  
- Only owners or admins can modify their resources  
- Users cannot review their own places or review the same place multiple times  

---

## Resources

- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Mermaid Live Editor](https://mermaid.live/)
