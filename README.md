# Lohmann Task 

# User Management API

## Requirements
- Docker
- Python 3.9+
- SQlite 3

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

- <img width="1050" alt="image" src="https://github.com/user-attachments/assets/2a9ac404-1cb0-4fb9-b68d-e13a204246eb" />


## Tests
1. Run tests:
    ```bash
    python manage.py test
    ```

## Steps to create this enviroment : 

To build the backend with Django that meets the given task requirements, we’ll cover the steps for setting up a **RESTful API** to manage users, integrate a **SQLite database**, and ensure **Dockerization**, **logging**, and **documentation**. Here’s a breakdown and solution using **Django**.

---

### **Step 1: Project Setup**
1. **Set up a virtual environment:**
   ```bash
   python3 -m venv userapi_env
   source userapi_env/bin/activate  # On Windows: userapi_env\Scripts\activate
   ```
   
2. **Install Django, Django Rest Framework (DRF), SQLite and others:**
   ```bash
   pip install django djangorestframework
   ```

3. **Create a new Django project and an app:**
   ```bash
   django-admin startproject user_api
   cd user_api
   python manage.py startapp users
   ```

4. **Register the app and Django Rest Framework in settings.py** (`user_api/settings.py`):
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'users',  # add the users app
   ]
   ```

### **Step 2: Set Up the User Model**
In `users/models.py`, define the user model:

```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
```

After creating the model, **migrate the database** to reflect changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

### **Step 3: Create the Serializers for User Model**
In `users/serializers.py`, create a serializer for the `User` model to define how data will be formatted:

```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']
```

### **Step 4: Create the Views for CRUD Operations**
In `users/views.py`, use Django REST framework's **viewsets** to define the CRUD operations:

```python
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

### **Step 5: Set Up URLs**
In `users/urls.py`, set the routes for the API:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Then, in `user_api/urls.py`, include the users app routes:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # API base URL
]
```

### **Step 6: Add Logging and Error Handling**
Add logging to the project settings (`settings.py`):

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

For error handling, you can create custom error responses in your views (in case of missing fields or invalid JSON).

### **Step 7: Write Unit Tests for CRUD Operations**
In `users/tests.py`, write test cases using **pytest** or **Django's test framework**:

```python
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserApiTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'Alice', 'email': 'alice@example.com'}

    def test_create_user(self):
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_users(self):
        self.client.post('/api/users/', self.user_data, format='json')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

Run the tests:
```bash
python manage.py test
```
<img width="1433" alt="image" src="https://github.com/user-attachments/assets/f2e2a1f8-7c1b-4113-8fe7-54196fd509ad" />


### **Step 8: Docker Setup**
To dockerize the app, create a `Dockerfile`:

```dockerfile
# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the app port
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Create `requirements.txt`:

```txt
Django
djangorestframework
drf-yasg
```

And a `docker-compose.yml`:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/usr/src/app
    environment:
      - DEBUG=True
```

Build and run the application:

```bash
docker-compose up --build
```

<img width="1293" alt="image" src="https://github.com/user-attachments/assets/e1a7b5dc-ae91-4579-8710-5a1958a05268" />

<img width="1436" alt="image" src="https://github.com/user-attachments/assets/b46a8564-d6e3-4de3-b06e-5b837da8679d" />


---

### **Optional Enhancements:**
1. **JWT Authentication**: Implement JWT authentication using `djangorestframework-simplejwt`.
2. **Email Verification**: Send verification emails when a user registers (optional for basic functionality).
3. **Pagination**: For GET `/users/`, implement pagination if the number of users is large.
