import unittest
from shipments import generate_shipment
from shipments.shipment import Shipment, Manifest, BillOfLading


class test_main_shipment(unittest.TestCase):
    def test_generate_shipment_should_return_shipment_obj(self):
        shipment = generate_shipment(BillOfLading(), Manifest())
        self.assertIsInstance(shipment, Shipment)

    def test_shipment_can_be_initialized_by_using_billoflading_and_manifest(self):
        with self.assertRaises(ValueError):
            generate_shipment(None, Manifest)
        with self.assertRaises(ValueError):
            generate_shipment(BillOfLading, None)
