from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserAPITestCase(TestCase):
    def setUp(self):
        """Configura los datos iniciales para los tests."""
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'user_type': 'driver'
        }
        self.user = User.objects.create_user(**self.user_data)
    def test_signin_valid_user(self):
        """Prueba el registro de un usuario válido."""
        response = self.client.post(reverse('signin'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'NewPass123!',
            'user_type': 'company'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
