# 1 User Registration

sequenceDiagram
    actor User
    participant Service as API Layer
    participant Logic as Business Layer
    participant Repo as Data Layer

    User->>Service: POST /users (data)
    Service->>Service: Check JSON & required fields
    Service->>Logic: register_user(data)

    Logic->>Repo: email_exists(email)
    Repo-->>Logic: true | false

    alt Email already used
        Logic-->>Service: Registration failed
        Service-->>User: 409 Conflict
    else Email available
        Logic->>Logic: Build User object
        Logic->>Repo: save(User)
        Repo-->>Logic: saved
        Logic-->>Service: User created
        Service-->>User: 201 Created
    end

