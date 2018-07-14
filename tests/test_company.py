import unittest

from shipments.company import Company
from shipments.shipment_component import ShipmentComponent


class test_company(unittest.TestCase):
    def test_container_should_be_object_of_components(self):
        self.assertIsInstance(Company('shipper Name', 'shipper Address'), ShipmentComponent)

    def test_company_data(self):
        company = Company('shipper Name', 'shipper Address')
        self.assertEqual(company.get_name(), 'shipper Name')
        self.assertEqual(company.get_address(), 'shipper Address')

    def test_json_data(self):
        real_json = {
            'Name': 'shipper Name',
            'Address': 'shipper Address'
        }

        cargo = Company('shipper Name', 'shipper Address')
        self.assertEqual(cargo.generate_json(), real_json)