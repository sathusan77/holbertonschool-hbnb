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

```bash
python3 -m venv venv
source venv/bin/activate
