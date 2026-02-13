# Explanatory_Notes_API_Calls.md

## Task 2 — Sequence Diagrams for API Calls

This document explains for each API call:
1. The objective of the use case
2. The main processing steps
3. The role of each architectural layer (Presentation, Business Logic, Persistence)

------------------------------------------------------------
1️⃣ API Call — User Registration
------------------------------------------------------------

Objective:
Allow a new user to create an account in the system.

Short Description:
When a client sends a registration request, the system:
- receives user information
- validates the request format
- applies business rules (ex: unique email)
- creates a User entity
- saves the user
- returns a confirmation response

Key Steps:
1. The client sends POST /users with registration data.
2. The Presentation Layer validates the JSON structure and required fields.
3. The Presentation Layer calls the Business Layer (Facade).
4. The Business Layer:
   - checks that the email is not already used
   - validates business constraints
   - creates the User entity (with id and timestamps)
5. The Persistence Layer saves the User.
6. The response is returned to the client (201 Created or error).

Role of Each Layer:
- Presentation Layer: handles HTTP request and basic validation.
- Business Logic Layer: applies rules and creates the entity.
- Persistence Layer: stores the data in the database.

Purpose of the Diagram:
Show that all business logic is centralized in the Business Layer and that the API does not directly access the database.

------------------------------------------------------------
2️⃣ API Call — Place Creation
------------------------------------------------------------

Objective:
Allow a user to create a new Place (listing).

Short Description:
When a place is created, the system:
- receives place information
- validates the input
- verifies that the owner exists
- applies business rules
- creates the Place entity
- saves it in storage
- returns the created place

Key Steps:
1. The client sends POST /places with place data.
2. The Presentation Layer validates the request.
3. It calls the Business Layer through the Facade.
4. The Business Layer:
   - verifies that the owner (User) exists
   - validates price and coordinates
   - creates the Place entity
   - handles amenities if provided
5. The Persistence Layer saves the Place.
6. The system returns 201 Created.

Role of Each Layer:
- Presentation Layer: request validation and forwarding.
- Business Logic Layer: verifies owner and applies rules.
- Persistence Layer: saves the Place and related data.

Purpose of the Diagram:
Show that creating a Place requires business validations before persistence.

------------------------------------------------------------
3️⃣ API Call — Review Submission
------------------------------------------------------------

Objective:
Allow a user to submit a review for a Place.

Short Description:
When a review is submitted, the system:
- receives review data
- verifies that the user and place exist
- validates the rating
- creates a Review entity
- saves it
- returns confirmation

Key Steps:
1. The client sends POST /reviews.
2. The Presentation Layer validates the request format.
3. It calls the Business Layer.
4. The Business Layer:
   - checks that the User exists
   - checks that the Place exists
   - validates the rating (for example between 1 and 5)
   - creates the Review entity
5. The Persistence Layer saves the Review.
6. The system returns 201 Created.

Role of Each Layer:
- Presentation Layer: receives and validates request.
- Business Logic Layer: applies validation rules and creates Review.
- Persistence Layer: stores the review.

Purpose of the Diagram:
Show that Review depends on both User and Place and that validations happen before saving.

------------------------------------------------------------
4️⃣ API Call — Fetching List of Places
------------------------------------------------------------

Objective:
Allow a client to retrieve a list of places.

Short Description:
When a client requests a list, the system:
- receives query parameters
- validates filters
- retrieves matching data
- returns a list of places

Key Steps:
1. The client sends GET /places (with optional filters).
2. The Presentation Layer parses and validates parameters.
3. It calls the Business Layer.
4. The Business Layer:
   - validates search criteria
   - requests matching places from Persistence
5. The Persistence Layer retrieves data.
6. The system returns 200 OK with a list of places.

Role of Each Layer:
- Presentation Layer: handles request and parameters.
- Business Logic Layer: manages search logic.
- Persistence Layer: retrieves data from storage.

Purpose of the Diagram:
Show a read-only flow and confirm that data access happens only through the Persistence Layer.

------------------------------------------------------------
Common Architecture Principles
------------------------------------------------------------

For all API calls:

- The request starts in the Presentation Layer.
- The Presentation Layer always calls the Facade.
- The Business Layer centralizes business rules.
- The Persistence Layer handles data storage and retrieval.
- The response flows back through the same layers to the client.

