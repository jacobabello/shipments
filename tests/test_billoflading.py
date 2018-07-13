import unittest
from shipments.billoflading import BillOfLading
from shipments.shipment_component import ShipmentComponent


class test_billoflading(unittest.TestCase):
    def test_bill_of_lading_should_be_object_of_components(self):
        self.assertIsInstance(BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE'), ShipmentComponent)

    def test_bill_type_code_not_recognize(self):
        with self.assertRaises(ValueError):
            BillOfLading('SAMPLEID', '99', 'SAMPLEVOYAGE')

    def test_generate_json_simple_bill_of_lading(self):
        real_json = {
            'Bill of lading number': 'SAMPLEID',
            'Bill type': 'Regular Bill',
            'Voyage number': 'SAMPLEVOYAGE'
        }

        bill_of_lading = BillOfLading('SAMPLEID', '02', 'SAMPLEVOYAGE')
        self.assertEqual(bill_of_lading.generate_json(), real_json)

    def test_generate_json_master(self):
        real_json = {
            'Bill of lading number': 'SAMPLEID',
            'Bill type': 'Master Bill',
            'Voyage number': 'SAMPLEVOYAGE'
        }

        bill_of_lading = BillOfLading('SAMPLEID', '13', 'SAMPLEVOYAGE')
        self.assertEqual(bill_of_lading.generate_json(), real_json)

    def test_generate_json_house(self):
        real_json = {
            'Bill of lading number': 'SAMPLEID',
            'Bill type': 'House Bill',
            'Voyage number': 'SAMPLEVOYAGE',
            'Master bill of lading number': 'MASTERID'
        }

        bill_of_lading = BillOfLading('SAMPLEID', '14', 'SAMPLEVOYAGE')
        bill_of_lading.add_master_bill_of_lading_number('MASTERID')
        self.assertEqual(bill_of_lading.generate_json(), real_json)


    def test_force_user_to_add_master_id(self):
        bill_of_lading = BillOfLading('SAMPLEID', '14', 'SAMPLEVOYAGE')
        with self.assertRaises(ValueError):
            bill_of_lading.generate_json()
