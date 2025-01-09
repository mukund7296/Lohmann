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

