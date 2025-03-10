from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from app_users.models import User
from .models import Driver

class DriverAPITestCase(TestCase):
    def setUp(self):
        """Configura los datos iniciales para los tests."""
        self.client = APIClient()
    
    # Crear usuario de prueba
        self.user = User.objects.create_user(
            username=f'driveruser{self._testMethodName}',  
            email=f'driver{self._testMethodName}@example.com',  
            password='DriverPass123!',
            user_type='driver'
        )

    # Crear conductor de prueba asociado a este usuario
        self.driver = Driver.objects.create(
            user=self.user,
            name='John Doe',
            truck_plate=f'ABC-{self._testMethodName}',  
            phone='123456789'
        )

        self.valid_payload = {
            'user': self.user.id,  
            'name': 'Updated Driver',
            'truck_plate': f'XYZ-{self._testMethodName}',  
            'phone': '987654321'
        }

        
        self.invalid_payload = {
            'user': self.user.id,
            'name': '',  
            'truck_plate': '',  
            'phone': 'abc'  
        }

    def test_get_all_drivers(self):
        """Prueba obtener todos los conductores."""
        response = self.client.get(reverse('drivers:get_all_drivers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_create_valid_driver(self):
        """Prueba crear un conductor con datos válidos."""
        new_user = User.objects.create_user(
            username=f'newdriver{self._testMethodName}', 
            email=f'newdriver{self._testMethodName}@example.com', 
            password='DriverPass123!',
            user_type='driver'
        )

        valid_payload = {
            'user': new_user.id,  
            'name': 'Updated Driver',
            'truck_plate': f'XYZ-{self._testMethodName}',  
            'phone': '987654321'
        }

        response = self.client.post(reverse('drivers:create_driver'), data=valid_payload, format='json')

        print("Response status:", response.status_code)
        print("Response content:", response.json())  

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_create_invalid_driver(self):
        """Prueba que no se pueda crear un conductor con datos inválidos."""
        response = self.client.post(reverse('drivers:create_driver'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_driver_by_id(self):
        """Prueba obtener un conductor por su ID."""
        response = self.client.get(reverse('drivers:driver_detail', kwargs={'id': self.driver.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_valid_driver(self):
        """Prueba actualizar un conductor con datos válidos."""
        response = self.client.put(reverse('drivers:driver_detail', kwargs={'id': self.driver.id}),
                                   data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_driver(self):
        """Prueba que no se pueda actualizar un conductor con datos inválidos."""
        response = self.client.put(reverse('drivers:driver_detail', kwargs={'id': self.driver.id}),
                                   data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_driver(self):
        """Prueba eliminar un conductor."""
        response = self.client.delete(reverse('drivers:driver_detail', kwargs={'id': self.driver.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

