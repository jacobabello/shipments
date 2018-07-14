import unittest
from shipments import generate_shipment
from shipments.container import Container
from shipments.shipment import Shipment, Manifest, BillOfLading


class test_main_shipment(unittest.TestCase):
    def test_generate_shipment_should_return_shipment_obj(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())
        self.assertIsInstance(shipment, Shipment)

    def test_shipment_can_be_initialized_by_using_billoflading_and_manifest(self):
        with self.assertRaises(ValueError):
            generate_shipment(None, Manifest)
        with self.assertRaises(ValueError):
            generate_shipment(BillOfLading, None)

    def test_shipment_can_add_container(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())

        container = shipment.add_container('containernumber')
        self.assertIsInstance(container, Container)

    def test_can_get_container_object_by_container_number(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())

        container = shipment.add_container('containernumber')
        self.assertEqual(shipment.get_container_by_container_number('containernumber'), container)

    def test_throw_exception_if_container_number_is_missing(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())

        with self.assertRaises(ValueError):
            shipment.get_container_by_container_number('containernumber')

    def test_add_company_type_consignee(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())
        consignee = shipment.add_company('consignee', 'Consignee Name', 'Consignee Address')
        self.assertEqual(shipment.get_company_by_type('consignee'), consignee)

    def test_add_company_type_shipper(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())
        shipper = shipment.add_company('shipper', 'shipper Name', 'shipper Address')
        self.assertEqual(shipment.get_company_by_type('shipper'), shipper)

    def test_cannot_add_invalid_company_type(self):
        shipment = generate_shipment(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'),
                                     Manifest())
        with self.assertRaises(ValueError):
            shipment.add_company('invalid_company_type', 'invalid Name', 'invalid Address')
