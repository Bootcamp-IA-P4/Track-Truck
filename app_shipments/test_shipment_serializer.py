from rest_framework import serializers
from rest_framework.test import APITestCase
from .models import Shipment
from .serializer import ShipmentSerializer
from django.utils import timezone

# GENERA ERROR EN INVALID DATA. PENDIENTE DE ARREGLAR

class ShipmentSerializerTest(APITestCase):

    def setUp(self):
        self.shipment_data = {
            'id': 1,
            'company_id': 1,
            'driver_id': 1,
            'description': 'Test shipment',
            'origin': 'Origin',
            'destination': 'Destination',
            'created_at': timezone.now(),
            'finished_at': timezone.now()
        }
        self.shipment = Shipment.objects.create(**self.shipment_data)
        self.serializer = ShipmentSerializer(instance=self.shipment)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'company_id', 'driver_id', 'description', 'origin', 'destination', 'created_at', 'finished_at']))

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['id'], self.shipment_data['id'])
        self.assertEqual(data['company_id'], self.shipment_data['company_id'])
        self.assertEqual(data['driver_id'], self.shipment_data['driver_id'])
        self.assertEqual(data['description'], self.shipment_data['description'])
        self.assertEqual(data['origin'], self.shipment_data['origin'])
        self.assertEqual(data['destination'], self.shipment_data['destination'])

    def test_invalid_data(self):
        invalid_data = self.shipment_data.copy()
        invalid_data['company_id'] = None
        serializer = ShipmentSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['company_id']))