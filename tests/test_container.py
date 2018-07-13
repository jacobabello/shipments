import unittest

from shipments.container import Container
from shipments.shipment_component import ShipmentComponent


class test_container(unittest.TestCase):

    def test_container_should_be_object_of_components(self):
        self.assertIsInstance(Container('CONTINERNUMBER'), ShipmentComponent)

    def test_container_data(self):
        container = Container('000001')

        self.assertEqual(container.set_length(100), container)
        self.assertEqual(container.set_height(100), container)
        self.assertEqual(container.set_width(100), container)
        self.assertEqual(container.set_load_status('Loaded'), container)
        self.assertEqual(container.set_type_of_service('BB'), container)
        self.assertEqual(container.get_length(), 100)
        self.assertEqual(container.get_height(), 100)
        self.assertEqual(container.get_width(), 100)
        self.assertEqual(container.get_load_status(), 'Loaded')
        self.assertEqual(container.get_type_of_service(), 'Break Bulk')

    def test_invalid_type_of_service(self):
        container = Container('000001')
        with self.assertRaises(ValueError):
            container.set_type_of_service('ZZ')