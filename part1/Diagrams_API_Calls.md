## 1️⃣ User Registration

Client
   |
   | POST /users (user_data)
   v
API Layer
   | Validate request (JSON + required fields)
   v
Business Layer
   | verify_email_not_used(email)
   |
   |---- If email already exists ----
   |        return 409 Conflict
   |
   |---- If email is available ----
   |        create_user_object()
   v
Persistence Layer
   | store_user(User)
   v
Business Layer
   | User successfully created
   v
API Layer
   | 201 Created (user info)
   v
Client

## 2️⃣ Place Creation

Client
   |
   | POST /places (place_data)
   v
Presentation (API)
   | Validate JSON + required fields
   v
Business Layer
   | check_user_exists(owner_id)
   | create_place(place_data)
   v
Persistence Layer
   | save_place(Place)
   v
Business Layer
   | Success
   v
Presentation
   | 201 Created (place payload)
   v
Client

## 3️⃣ Review Submission

Client
   |
   | POST /reviews (review_data)
   v
Presentation (API)
   | Validate JSON
   v
Business Layer
   | check_user_exists(user_id)
   | check_place_exists(place_id)
   | create_review(review_data)
   v
Persistence Layer
   | save_review(Review)
   v
Business Layer
   | Success
   v
Presentation
   | 201 Created (review payload)
   v
Client

## 4️⃣ Fetching List of Places

Client
   |
   | GET /places
   v
Presentation (API)
   v
Business Layer
   | get_all_places()
   v
Persistence Layer
   | fetch_places()
   v
Business Layer
   | return list
   v
Presentation
   | 200 OK (list of places)
   v
Client

