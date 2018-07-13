from shipments.carrier import Carrier
from shipments.shipment_component import ShipmentComponent


class Manifest(ShipmentComponent):

    def generate_json(self):
        return {
            'Carrier': self.carrier.generate_json(),
            'Vessel name': self.get_vessel_name(),
            'Port of unlading': self.get_port_of_unlading(),
            'Foreign port of lading': self.get_foreign_port_of_lading(),
            'Manifest Quantity': self.get_manifest_quantity(),
            'Manifest Unit': self.get_manifest_unit(),
            'Weight': self.get_weight(),
            'Weight Unit': self.get_weight_unit(),
            'Measurement': self.get_measurement(),
            'Measurement Unit': self.get_measurement_unit()
        }

    def set_carrier_code(self, carrier_code):
        self.carrier = Carrier(carrier_code)

        return self

    def set_vessel_name(self, vessel_name):
        self.vessel_name = vessel_name

        return self

    def set_port_of_unlading(self, port):
        self.port_of_unlading = port

        return self

    def set_foreign_port_of_lading(self, port):
        self.port_of_lading = port

        return self

    def set_manifest_quantity(self, quantity):
        self.manifest_quantity = quantity

        return self

    def set_manifest_quantity_unit(self, unit):
        self.manifest_quantity_unit = unit

        return self

    def set_weigh(self, weight):
        self.weight = weight

        return self

    def set_weigh_unit(self, unit):
        self.weight_unit = unit

        return self

    def set_measurement(self, measurement):
        self.measurement = measurement

        return self

    def set_measurement_unit(self, unit):
        self.measurement_unit = unit

        return self

    def get_carrier(self):
        """
        :rtype: Carrier
        """
        return self.carrier

    def get_vessel_name(self):
        return self.vessel_name

    def get_port_of_unlading(self):
        return self.port_of_unlading

    def get_foreign_port_of_lading(self):
        return self.port_of_lading

    def get_manifest_quantity(self):
        return self.manifest_quantity

    def get_manifest_unit(self):
        return self.manifest_quantity_unit

    def get_weight(self):
        return self.weight

    def get_weight_unit(self):
        return self.weight_unit

    def get_measurement(self):
        return self.measurement

    def get_measurement_unit(self):
        return self.measurement_unit
