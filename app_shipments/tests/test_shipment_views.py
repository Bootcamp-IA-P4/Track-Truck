from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Shipment
from ..serializer import ShipmentSerializer

class ShipmentTests(APITestCase):

    def setUp(self):
        self.shipment_data = {
            'id': 1,
            'company_id': 1,
            'driver_id': 1,
            'description': 'Test shipment',
            'origin': 'Origin',
            'destination': 'Destination',
            'created_at': '2025-03-10T00:00:00Z',
            'finished_at': '2025-03-10T00:00:00Z'
        }
        #self.shipment = Shipment.objects.create(**self.shipment_data)
        self.client = APIClient()

    def test_shipment_create(self):
        url = reverse('shipment-create')
        response = self.client.post(url, self.shipment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shipment_list(self):
        url = reverse('shipment-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_company_shipments(self):
        url = reverse('company-shipments', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_driver_shipments(self):
        url = reverse('driver-shipments', args=[1])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_shipment_update(self):
        url = reverse('shipment-update')
        updated_data = self.shipment_data.copy()
        updated_data['description'] = 'Updated shipment'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Updated shipment')

    def test_shipment_delete(self):
        url = reverse('shipment-delete')
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Shipment.objects.count(), 0)