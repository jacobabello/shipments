import unittest

from shipments.cargo import Cargo
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

    def test_get_cargo_by_sequence_number(self):
        container = Container('000001')
        container.add_cargo('001', 'Fake Cargo Description', 10)

        self.assertIsInstance(container.get_cargo_by_sequence_number('001'), Cargo)

    def test_get_all_cargoes(self):
        container = Container('000001')
        container.add_cargo('001', 'Fake Cargo 1st Description', 10)
        container.add_cargo('002', 'Fake Cargo 2nd Description', 20)

        cargoes = container.get_all_cargoes()
        self.assertEqual(len(cargoes), 2)
        self.assertIsInstance(cargoes[0], Cargo)
        self.assertIsInstance(cargoes[1], Cargo)

    def test_cannot_add_existing_sequence_number(self):
        container = Container('000001')
        container.add_cargo('001', 'Fake Cargo 1st Description', 10)

        with self.assertRaises(ValueError):
            container.add_cargo('001', 'Fake Cargo 1st Description', 10)

    def test_json_data_single_container(self):
        real_json = {
            'Container Number': '000001',
            'Length': 100,
            'Height': 100,
            'Width': 100,
            'Load status': 'Loaded',
            'Type of service': 'Break Bulk'
        }

        container = Container('000001')\
            .set_height(100)\
            .set_length(100)\
            .set_width(100)\
            .set_load_status('Loaded')\
            .set_type_of_service('BB')

        self.assertEqual(container.generate_json(), real_json)

    def test_json_data_cargo(self):
        real_json = {
            'Container Number': '000001',
            'Length': 100,
            'Height': 100,
            'Width': 100,
            'Load status': 'Loaded',
            'Type of service': 'Break Bulk',
            'Cargoes': [
                {
                    'Product description': "Fake Product Description",
                    'Piece count': 10
                }
            ]
        }

        container = Container('000001')
        container.set_height(100)
        container.set_length(100)
        container.set_width(100)
        container.set_load_status('Loaded')
        container.set_type_of_service('BB')
        container.add_cargo('001', 'Fake Product Description', 10)

        self.assertEqual(container.generate_json(), real_json)

    def test_json_data_multiple_cargo(self):
        real_json = {
            'Container Number': '000001',
            'Length': 100,
            'Height': 100,
            'Width': 100,
            'Load status': 'Loaded',
            'Type of service': 'Break Bulk',
            'Cargoes': [
                {
                    'Product description': "Fake Product Description 1",
                    'Piece count': 10
                },
                {
                    'Product description': "Fake Product Description 2",
                    'Piece count': 20
                },
                {
                    'Product description': "Fake Product Description 3",
                    'Piece count': 30
                }
            ]
        }

        container = Container('000001')
        container.set_height(100)
        container.set_length(100)
        container.set_width(100)
        container.set_load_status('Loaded')
        container.set_type_of_service('BB')
        container.add_cargo('001', 'Fake Product Description 1', 10)
        container.add_cargo('002', 'Fake Product Description 2', 20)
        container.add_cargo('003', 'Fake Product Description 3', 30)

        self.assertEqual(container.generate_json(), real_json)
