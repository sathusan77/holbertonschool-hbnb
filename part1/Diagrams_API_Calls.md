## 1️⃣ User Registration

Client        API Layer        Business Logic        Database
  |               |                  |                  |
  | POST /users   |                  |                  |
  |-------------->|                  |                  |
  |               | Validate data    |                  |
  |               |----------------->|                  |
  |               |                  | check_email()    |
  |               |                  |----------------->|
  |               |                  |<-----------------|
  |               |                  | email exists?    |
  |               |                  |
  |               |<-----------------| Error (409)      |
  |<--------------|                  |                  |
  |               |                  |                  |
  |               |                  | create_user()    |
  |               |                  |----------------->|
  |               |                  | save_user()      |
  |               |                  |----------------->|
  |               |                  |<-----------------|
  |               |<-----------------| Success          |
  |<--------------| 201 Created      |                  |

