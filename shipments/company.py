from shipments.shipment_component import ShipmentComponent


class Company(ShipmentComponent):

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def generate_json(self):
        return {
            'Name': self.get_name(),
            'Address': self.get_address()
        }

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
