Task Instructions:

Create a small RESTful web service in Python that performs basic CRUD operations (Create, Read, Update, Delete) for a simple user management system. The development environment could be based on something like VS Code.

The following requirements must be met:

1. REST API

Implement a REST interface with at least the following endpoints:

GET /users – Returns a list of all registered users.
GET /users/ – Returns the data of a specific user.
POST /users – Creates a new user.
PUT /users/ – Modifies the data of an existing user.
DELETE /users/ – Deletes an existing user.
Ensure proper usage of HTTP status codes (e.g., 200 for "OK", 201 for "Created", 404 for "Not Found", 400 for "Bad Request", etc.).

Optional: Add filter or search functions (e.g., GET /users?username=Alice).

2. Database

Use a relational database (e.g., SQLite, PostgreSQL, MySQL) or a NoSQL database (e.g., MongoDB).

Set up a simple schema for the user table/collection.

Make sure that all CRUD operations interact correctly with the database.

Alternative: You can use an in-memory solution for rapid prototyping, but ensure that the code remains extendable.

3. Authentication & Authorization (Optional)

Implement basic authentication with JWT (JSON Web Tokens) or Basic Auth.

Only authenticated requests should be able to access certain endpoints (e.g., not everyone should be able to query or create user data).

You can allow open endpoints (e.g., for creating a new user) and only protect certain endpoints (e.g., for editing and deleting users).

4. Error Handling & Logging

Provide meaningful error messages in JSON format for invalid inputs (e.g., missing fields, invalid JSON format).

Log important events (e.g., user creation, updates, deletions, error messages, etc.) using either console logs or a logging framework.

5. Structure & Documentation

The code should be well-structured (e.g., based on MVC/MVT principles or a modular structure).
Follow PEP8 guidelines for formatting.
Model a user with at least the following fields:
id (unique identifier, e.g., automatically generated)
username (string, unique)
email (string)
created_at (timestamp for account creation)
You can extend this model (e.g., add first name, last name, password hash, etc.).

6. Evaluation Criteria

Tips for the Candidate:

Framework: You may use Flask, FastAPI, or Django. FastAPI is great for quickly generating OpenAPI documentation.
Database: SQLite is good for a quick start as it doesn't require external installation. For production-level solutions, PostgreSQL or another DB might be more suitable.
Structure: Pay attention to a sensible separation between models, routes/views/endpoints, and possibly services or repositories.
Tests: Focus on core functionality. You don’t need to cover all edge cases, but show that you know how to write tests.
Time Management: Plan ahead and set priorities. Do fewer features, but ensure they work solidly and are well-tested.
Documentation: Document your important functions and classes (e.g., with docstrings).
Optionally, provide an OpenAPI/Swagger documentation or at least a README with clear instructions on how to start and test the service.
7. Automated Tests

Write some unit and/or integration tests to check the basic functionalities (e.g., using pytest, unittest, or another framework).

Test at least one endpoint per CRUD operation.

Bonus: Set up a CI pipeline (e.g., GitHub Actions, GitLab CI) to automate testing.

8. Deployment

Create a Dockerfile (and optionally a docker-compose.yml) to allow local startup of the application with the database.

Document the commands in the README on how to build and run the application:

docker build -t myuserapi .
docker run -p 8000:8000 myuserapi
Alternatively, provide a local development guide (e.g., using virtualenv or pipenv to start the project).

9. Code Quality & Architecture

Clean, well-maintained code (with modules, classes, functions).
Readable implementation according to PEP8 standards.
Proper error handling and logical separation of responsibilities (e.g., separating database access into a distinct module).
10. Test Coverage

Ensure unit tests and/or integration tests are available and easy to run. Ideally, automate testing with every commit (or pull request) in the CI system.

11. Documentation & Usability

A README that explains how to set up, start, and test the project.
Optionally, API documentation (e.g., using Swagger/OpenAPI).
12. Optional Extensions

Implement JWT authentication or Basic Auth to protect the endpoints.
Provide a Docker/Kubernetes deployment.
Add additional features like email verification, password hashing, pagination, etc.
Task Timeline Recommendations:

Setup & Project Structure: Set up your virtual environment, create project directories (e.g., app, tests, Dockerfile).
Models & DB: Create your user model and configure the database.
CRUD Endpoints: Implement the REST API step by step with the GET/POST/PUT/DELETE endpoints.
Tests: Write initial tests for your endpoints (unit or integration tests).
Docker: Create your Dockerfile and test the container locally.
README & CI (Optional): Write a concise procedure and provide the project in a Git repository.
This is a step-by-step guide on how you can create a Django project to fulfill the challenge requirements. Let me know if you need help in setting up specific sections!
