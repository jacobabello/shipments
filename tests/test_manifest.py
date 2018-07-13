import unittest

from shipments.carrier import Carrier
from shipments.manifest import Manifest
from shipments.shipment_component import ShipmentComponent


class test_manifest(unittest.TestCase):
    def test_manifest_should_be_object_of_components(self):
        self.assertIsInstance(Manifest(), ShipmentComponent)

    def test_manifest_data(self):
        manifest = Manifest()
        self.assertEqual(manifest.set_carrier_code('AAGJ'), manifest)
        self.assertEqual(manifest.set_vessel_name('SAMPLENAME'), manifest)
        self.assertEqual(manifest.set_port_of_unlading('Fake US Port'), manifest)
        self.assertEqual(manifest.set_foreign_port_of_lading('Fake Foreign Port'), manifest)
        self.assertEqual(manifest.set_manifest_quantity(100), manifest)
        self.assertEqual(manifest.set_manifest_quantity_unit('PCS'), manifest)
        self.assertEqual(manifest.set_weigh(100), manifest)
        self.assertEqual(manifest.set_weigh_unit('KG'), manifest)
        self.assertEqual(manifest.set_measurement(100), manifest)
        self.assertEqual(manifest.set_measurement_unit('V'), manifest)

        self.assertIsInstance(manifest.get_carrier(), Carrier)
        self.assertEqual(manifest.get_vessel_name(), 'SAMPLENAME')
        self.assertEqual(manifest.get_port_of_unlading(), 'Fake US Port')
        self.assertEqual(manifest.get_foreign_port_of_lading(), 'Fake Foreign Port')
        self.assertEqual(manifest.get_manifest_quantity(), 100)
        self.assertEqual(manifest.get_manifest_unit(), 'PCS')
        self.assertEqual(manifest.get_weight(), 100)
        self.assertEqual(manifest.get_weight_unit(), 'KG')
        self.assertEqual(manifest.get_measurement(), 100)
        self.assertEqual(manifest.get_measurement_unit(), 'V')

    def test_json_data(self):
        real_json = {
            'Carrier': {
                'scac_code': 'AAGJ',
                'name': 'A & A LOGISTICS LLC',
                'address': '7600 NW 90TH',
                'city': 'JOHNSTON',
                'state': 'IA',
                'country': ''
            },
            'Vessel name': 'SAMPLENAME',
            'Port of unlading': 'Fake US Port',
            'Foreign port of lading': 'Fake Foreign Port',
            'Manifest Quantity': 100,
            'Manifest Unit': 'PCS',
            'Weight': 100,
            'Weight Unit': 'KG',
            'Measurement': 100,
            'Measurement Unit': 'V'
        }

        manifest = Manifest()
        manifest.set_carrier_code('AAGJ')
        manifest.set_vessel_name('SAMPLENAME')
        manifest.set_port_of_unlading('Fake US Port')
        manifest.set_foreign_port_of_lading('Fake Foreign Port')
        manifest.set_manifest_quantity(100)
        manifest.set_manifest_quantity_unit('PCS')
        manifest.set_weigh(100)
        manifest.set_weigh_unit('KG')
        manifest.set_measurement(100)
        manifest.set_measurement_unit('V')

        self.assertEqual(manifest.generate_json(), real_json)