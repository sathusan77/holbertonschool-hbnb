# HBnB Evolution - Technical Documentation

## 1. Context and Objective

This document describes the architecture and design of the HBnB Evolution application.

The application allows:
- User management
- Place management
- Review management
- Amenity management

---

# 2. High-Level Package Diagram

## Architecture Explanation

The application follows a three-layer architecture:

- Presentation Layer
- Business Logic Layer
- Persistence Layer

The communication is handled using the Facade pattern.

## Package Diagram

```mermaid
classDiagram

package "Presentation Layer" {
    class UserAPI
    class PlaceAPI
    class ReviewAPI
    class AmenityAPI
}

package "Business Logic Layer" {
    class HBnBFacade
    class User
    class Place
    class Review
    class Amenity
}

package "Persistence Layer" {
    class UserRepository
    class PlaceRepository
    class ReviewRepository
    class AmenityRepository
}

UserAPI --> HBnBFacade
PlaceAPI --> HBnBFacade
ReviewAPI --> HBnBFacade
AmenityAPI --> HBnBFacade

HBnBFacade --> User
HBnBFacade --> Place
HBnBFacade --> Review
HBnBFacade --> Amenity

HBnBFacade --> UserRepository
HBnBFacade --> PlaceRepository
HBnBFacade --> ReviewRepository
HBnBFacade --> AmenityRepository

