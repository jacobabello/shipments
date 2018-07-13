import os
import unittest
import unittest.mock
from shipments.carrier import Carrier
from shipments.shipment_component import ShipmentComponent


class test_carrier(unittest.TestCase):
    def test_carrier_should_be_object_of_components(self):
        self.assertIsInstance(Carrier('AAGJ'), ShipmentComponent)

    def test_carrier_should_read_sqlite_file(self):
        path = '/home/jacob/ninja/shipments/shipments/../sqlite/carrier_codes.sqlite'

        with unittest.mock.patch('sqlite3.connect') as mock_sqlite_read:
            Carrier('AAGJ')
            mock_sqlite_read.assert_called_with(path, isolation_level=None)

    def test_carrier_code_data(self):
        carrier = Carrier('AAGJ')
        self.assertEqual(carrier.get_scac_code(), 'AAGJ')
        self.assertEqual(carrier.get_name(), 'A & A LOGISTICS LLC')
        self.assertEqual(carrier.get_address(), '7600 NW 90TH')
        self.assertEqual(carrier.get_city(), 'JOHNSTON')
        self.assertEqual(carrier.get_state(), 'IA')
        self.assertEqual(carrier.get_country(), '')

    def test_json_return(self):
        real_json = {
            'scac_code': 'AAGJ',
            'name': 'A & A LOGISTICS LLC',
            'address': '7600 NW 90TH',
            'city': 'JOHNSTON',
            'state': 'IA',
            'country': ''
        }

        carrier = Carrier('AAGJ')
        self.assertEqual(carrier.generate_json(), real_json)
