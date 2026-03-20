-- ============================================
-- HBnB Project Part 3 : SQL Schema + Initial Data
-- ============================================

DROP TABLE IF EXISTS place_amenity;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS amenities;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id VARCHAR(60) PRIMARY KEY,
    email VARCHAR(128) NOT NULL UNIQUE,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE places (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description VARCHAR(1024),
    city VARCHAR(128),
    state VARCHAR(128),
    country VARCHAR(128),
    price_by_night FLOAT DEFAULT 0.0,
    number_rooms INT DEFAULT 0,
    number_bathrooms INT DEFAULT 0,
    max_guest INT DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    user_id VARCHAR(60) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE reviews (
    id VARCHAR(60) PRIMARY KEY,
    text VARCHAR(1024) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE
);

CREATE TABLE amenities (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE place_amenity (
    place_id VARCHAR(60),
    amenity_id VARCHAR(60),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
);

INSERT INTO users (id, email, first_name, last_name, password, is_admin)
VALUES (
    'admin-uuid-0001',
    'admin@hbnb.com',
    'Admin',
    'User',
    '$2b$12$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    1
);

INSERT INTO amenities (id, name) VALUES ('amenity-uuid-01', 'Wifi');
INSERT INTO amenities (id, name) VALUES ('amenity-uuid-02', 'Air Conditioning');
INSERT INTO amenities (id, name) VALUES ('amenity-uuid-03', 'Pool');
INSERT INTO amenities (id, name) VALUES ('amenity-uuid-04', 'Kitchen');
INSERT INTO amenities (id, name) VALUES ('amenity-uuid-05', 'Parking');
