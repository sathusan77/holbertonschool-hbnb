erDiagram
    USERS {
        string id PK
        string email
        string first_name
        string last_name
        string password
        boolean is_admin
        datetime created_at
        datetime updated_at
    }

    PLACES {
        string id PK
        string name
        string description
        string city
        string state
        string country
        float price_by_night
        int number_rooms
        int number_bathrooms
        int max_guest
        float latitude
        float longitude
        string user_id FK
        datetime created_at
        datetime updated_at
    }

    REVIEWS {
        string id PK
        string text
        string user_id FK
        string place_id FK
        datetime created_at
        datetime updated_at
    }

    AMENITIES {
        string id PK
        string name
        datetime created_at
        datetime updated_at
    }

    PLACE_AMENITY {
        string place_id PK, FK
        string amenity_id PK, FK
    }

    %% Relationships
    USERS ||--o{ PLACES : "owns"
    USERS ||--o{ REVIEWS : "writes"
    PLACES ||--o{ REVIEWS : "receives"
    PLACES }o--o{ AMENITIES : "has"
