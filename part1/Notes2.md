# 📘 TASK 2 — Detailed Explanation of Sequence Diagrams

This document explains clearly each sequence diagram.
It is designed to help during an oral presentation and to understand the logic represented visually.

Each diagram illustrates:

- the request flow
- the separation between layers
- the central role of the Facade
- the absence of direct database access from the API

------------------------------------------------------------------

# 1️⃣ User Registration — Explanation

## 🎯 Purpose

This diagram shows how a new user is created while enforcing business rules such as email uniqueness.

## 🧠 How to read the diagram

The flow goes from left to right:

Client → Presentation Layer → Business Facade → Persistence → Response back to Client.

## 🪜 Logical Steps

1. The Client sends a POST /users request with user data.

2. The Presentation Layer validates:
   - JSON format
   - required fields
   - correct data types

   It does NOT apply business rules.

3. The request is forwarded to the Business Layer through the Facade.

4. The Facade checks with Persistence whether the email already exists.

5. alt block:
   - If email exists → return 400 or 409 error.
   - Otherwise → continue.

6. The Facade creates the User entity (id + timestamps).

7. The Facade asks Persistence to save the User.

8. Persistence confirms storage.

9. Response returns to Client → 201 Created.

## 🎓 What this diagram proves

- The API never talks directly to the database.
- Business validation is centralized in the Facade.
- Persistence only stores data.
- Email uniqueness is enforced before creation.

------------------------------------------------------------------

# 2️⃣ Place Creation — Explanation

## 🎯 Purpose

This diagram shows that a Place depends on an existing User (owner) and optionally Amenities.

## 🧠 Flow structure

Client → API → Facade → Persistence → Response.

## 🪜 Logical Steps

1. Client sends POST /places.

2. Presentation validates request format.

3. Facade receives the creation request.

4. Facade verifies that the owner exists.

alt block:
- If owner not found → 404 error.
- If owner exists → continue.

5. Facade validates business rules:
   - price value
   - latitude range
   - longitude range

6. opt block:
   If amenities are provided, Facade asks Persistence to verify them.

   alt inside:
   - Invalid amenities → 400 error.
   - Valid → continue.

7. Facade creates the Place entity (owner + id + timestamps).

8. Persistence saves the Place.

9. Response → 201 Created.

## 🎓 What this diagram proves

- A Place cannot exist without an owner.
- Business validation is not done in the API.
- Optional logic is clearly separated (opt block).
- Persistence remains passive.

------------------------------------------------------------------

# 3️⃣ Review Submission — Explanation

## 🎯 Purpose

This diagram demonstrates that a Review depends on both a User and a Place.

## 🧠 Flow structure

Client → API → Facade → Persistence → Response.

## 🪜 Logical Steps

1. Client sends POST /reviews.

2. API validates request structure.

3. Facade verifies that the User exists.

alt block:
- If User not found → 404.
- Otherwise → continue.

4. Facade verifies that the Place exists.

alt block:
- If Place not found → 404.
- Otherwise → continue.

5. Facade validates rating range.

alt block:
- Invalid rating → 400.
- Valid → continue.

6. Facade creates Review entity (links + id + timestamps).

7. Persistence saves Review.

8. Response → 201 Created.

## 🎓 What this diagram proves

- Review is a dependent entity.
- All validations occur before saving.
- Business consistency is protected.
- The diagram matches the Class Diagram relationships.

------------------------------------------------------------------

# 4️⃣ Fetching a List of Places — Explanation

## 🎯 Purpose

This diagram illustrates a read-only flow without modifying data.

## 🧠 Simplified flow

Client → API → Facade → Persistence → Response.

## 🪜 Logical Steps

1. Client sends GET /places with filters.

2. Presentation:
   - parses query parameters
   - validates format

3. Facade checks business consistency of filters.

4. Persistence performs the query.

5. List of Places is returned.

6. Response → 200 OK.

## 🎓 What this diagram proves

- Clear difference between read and write flows.
- No entity creation.
- Same architectural separation.
- Fully consistent with other diagrams.

------------------------------------------------------------------

# 🧩 Global Summary

Each diagram shows how a request moves across the three architectural layers:

- Presentation Layer handles input/output.
- Business Layer (via Facade) applies business rules.
- Persistence Layer stores or retrieves data.

Important UML elements:

- alt blocks represent business decisions.
- opt blocks represent optional behavior.

------------------------------------------------------------------

# ✅ Final Conclusion

These diagrams do not describe technical implementation details.

They describe:

- processing logic
- responsibility separation
- central role of the Facade
- alignment with the Class Diagram (Task 1)
- compliance with the architecture defined in Task 0

They serve as a bridge between:

- Business modeling (Task 1)
- Future implementation (Part 2 and Part 3)

