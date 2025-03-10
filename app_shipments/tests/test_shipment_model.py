from django.test import TestCase
from ..models import Shipment
from django.utils import timezone

# filepath: /c:/Users/Fernando/VSC/python/Track-Truck/app_shipments/test_models.py

class ShipmentModelTest(TestCase):

    def setUp(self):
        self.shipment_data = {
            'id': 1,
            'company_id': 123,
            'driver_id': 456,
            'description': 'Test shipment',
            'origin': 'Origin address',
            'destination': 'Destination address',
            'created_at': timezone.now(),
            'finished_at': timezone.now()
        }
        self.shipment = Shipment.objects.create(**self.shipment_data)

    def test_shipment_creation(self):
        self.assertIsInstance(self.shipment, Shipment)
        self.assertEqual(self.shipment.id, self.shipment_data['id'])
        self.assertEqual(self.shipment.company_id, self.shipment_data['company_id'])
        self.assertEqual(self.shipment.driver_id, self.shipment_data['driver_id'])
        self.assertEqual(self.shipment.description, self.shipment_data['description'])
        self.assertEqual(self.shipment.origin, self.shipment_data['origin'])
        self.assertEqual(self.shipment.destination, self.shipment_data['destination'])
        self.assertIsNotNone(self.shipment.created_at)
        self.assertIsNotNone(self.shipment.finished_at)

    def test_shipment_str(self):
        self.assertEqual(str(self.shipment), f"{self.shipment_data['id']}-{self.shipment_data['description']}")

    def test_shipment_company_id_not_null(self):
        with self.assertRaises(ValueError):
            Shipment.objects.create(
                id=2,
                company_id=None,
                driver_id=456,
                description='Test shipment 2',
                origin='Origin address 2',
                destination='Destination address 2',
                created_at=timezone.now(),
                finished_at=timezone.now()
            )

    def test_shipment_unique_id(self):
        with self.assertRaises(Exception):
            Shipment.objects.create(
                id=1,
                company_id=789,
                driver_id=101,
                description='Duplicate ID shipment',
                origin='Another origin',
                destination='Another destination',
                created_at=timezone.now(),
                finished_at=timezone.now()
            )