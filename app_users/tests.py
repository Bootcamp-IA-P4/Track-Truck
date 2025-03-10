from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import User


class UserAPITestCase(TestCase):
    def setUp(self):
        """Configura los datos iniciales para los tests."""
        self.client = self.client
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "TestPass123!",
            "user_type": "driver",
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_signin_valid_user(self):
        """Prueba el registro de un usuario válido."""
        response = self.client.post(
            reverse("signin"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password": "NewPass123!",
                "user_type": "company",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_invalid_user(self):
        data = {
        "username": "",  # Datos inválidos
        "email": "correo_invalido",
        "password": "123"
    }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, "form")  

    def test_login_valid_user(self):
        """Prueba el login con credenciales válidas."""
        response = self.client.post(
            reverse("login"),
            {"email": self.user_data["email"], "password": self.user_data["password"]},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid_user(self):
        data = {
        "username": "usuario_invalido",
        "password": "contraseña_incorrecta"
    }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, "form")  

    def test_logout_user(self):
        """Prueba el cierre de sesión de un usuario autenticado."""
        self.client.login(email=self.user_data['email'], password=self.user_data['password'])  
        response = self.client.get(reverse('logout'))  
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)  

        

   