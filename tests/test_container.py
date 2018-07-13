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

    def test_can_add_cargo(self):
        container = Container('000001')
        cargo = container.add_cargo('001', 'Fake Cargo Description', 10)
        self.assertIsInstance(cargo, Cargo)

    def test_get_cargo_by_sequence_number(self):
        container = Container('000001')
        cargo = container.add_cargo('001', 'Fake Cargo Description', 10)

        self.assertEqual(container.get_cargo_by_sequence_number('001'), cargo)

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
