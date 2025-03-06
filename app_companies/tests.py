from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company
from app_users.models import User  # Importa tu modelo de usuario personalizado


class CompanyAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')

        self.company = Company.objects.create(
            user_id=self.user,
            name='Test Company',
            email='test@company.com',
            phone='1234567890',
            address='Test Address'
        )

        self.valid_payload = {
            'user_id': self.user.id,
            'name': 'Updated Company',
            'email': 'updated@company.com',
            'phone': '0987654321',
            'address': 'Updated Address'
        }

        self.invalid_payload = {
            'user_id': self.user.id,
            'name': '',
            'email': 'invalid_email',
            'phone': '123',
            'address': ''
        }

    def test_get_all_companies(self):
        response = self.client.get(reverse('companies:list_companies'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_valid_company(self):
        response = self.client.post(
            reverse('companies:create_company'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company(self):
        response = self.client.post(
            reverse('companies:create_company'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_single_company(self):
        response = self.client.get(
            reverse('companies:detail', kwargs={'id': self.company.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_company(self):
        response = self.client.get(
            reverse('companies:detail', kwargs={'id': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_company(self):
        response = self.client.put(
            reverse('companies:update_company', kwargs={'id': self.company.id}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_company(self):
         # Asegúrate de que el servidor está corriendo para este test
        response = self.client.put(
            reverse('companies:update_company', kwargs={'id': self.company.id}),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_company(self):
        response = self.client.delete(
            reverse('companies:delete_company', kwargs={'id': self.company.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_company(self):
        response = self.client.delete(
            reverse('companies:delete_company', kwargs={'id': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

