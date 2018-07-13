import unittest

from shipments.cargo import Cargo
from shipments.shipment_component import ShipmentComponent


class test_cargo(unittest.TestCase):
    def test_container_should_be_object_of_components(self):
        self.assertIsInstance(Cargo('001', 'Fake Cargo 1st Description', 10), ShipmentComponent)

    def test_cargo_data(self):
        cargo = Cargo('001', 'Fake Cargo 1st Description', 10)
        self.assertEqual(cargo.get_sequence_number(), '001')
        self.assertEqual(cargo.get_product_description(), 'Fake Cargo 1st Description')
        self.assertEqual(cargo.get_piece_count(), 10)