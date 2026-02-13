## 1️⃣ User Registration

User
-----
+ id : UUID
+ first_name : string
+ last_name : string
+ email : string
+ password : string

Methods:
+ register()
+ update_profile()
+ delete()


## 2️⃣ Place Creation

Place
------
+ id : UUID
+ title : string
+ description : string
+ price : float
+ latitude : float
+ longitude : float
+ owner_id : UUID

Methods:
+ create_place()
+ update_place()
+ delete_place()


Relationship:
One User → can create → Multiple Places


## 3️⃣ Review Submission

Review
-------
+ id : UUID
+ text : string
+ rating : int
+ user_id : UUID
+ place_id : UUID

Methods:
+ create_review()
+ update_review()
+ delete_review()


Relationship:
One User → can write → Multiple Reviews  
One Place → can have → Multiple Reviews


## 4️⃣ Fetching List of Places

System Behavior
----------------
+ get_all_places()
+ get_place_by_id(id)
+ filter_places_by_price()
+ filter_places_by_location()

This allows users to:
- See all places
- Search for a place
- Filter results

