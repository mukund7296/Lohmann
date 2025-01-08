# Lohmann Task 

# User Management API

## Requirements
- Docker
- Python 3.9+

## How to Run
1. Build and start the application using Docker:
    ```bash
    docker-compose up --build
    ```
2. Access the API at: `http://localhost:8000/api/users/`

## Endpoints
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/<id>/` - Get a specific user
- `PUT /api/users/<id>/` - Update a user
- `DELETE /api/users/<id>/` - Delete a user

## Tests
1. Run tests:
    ```bash
    python manage.py test
    ```

## Swagger UI
Access Swagger documentation at: `http://localhost:8000/swagger/`
