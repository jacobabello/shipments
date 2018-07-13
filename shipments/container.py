from shipments.shipment_component import ShipmentComponent


class Container(ShipmentComponent):

    __type_of_services__ = {
        'BB': 'Break Bulk',
        'CS': 'Container Station',
        'CY': 'Container Yard',
        'HH': 'House‑to‑House',
        'HL': 'Headload or Devanning',
        'HP': 'House‑to‑Pier',
        'MD': 'Mixed Delivery',
        'NC': 'Non Containerized',
        'PH': 'Pier to House',
        'PP': 'Pier to Pier',
        'RR': 'Roll on ‑ Roll Off'
    }

    def __init__(self, container_number):
        self.container_number = container_number

    def generate_json(self):
        pass

    def set_length(self, lenght):
        self.lenght = lenght
        return self

    def set_height(self, height):
        self.height = height
        return self

    def set_width(self, width):
        self.width = width
        return self

    def set_load_status(self, load_status):
        self.load_status = load_status
        return self

    def set_type_of_service(self, type_of_service):

        if type_of_service not in self.__type_of_services__.keys():
            raise ValueError('Type Of Service %s is invalid' % type_of_service)

        self.type_of_service = type_of_service
        return self

    def get_length(self):
        return self.lenght

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_load_status(self):
        return self.load_status

    def get_type_of_service(self):
        return self.__type_of_services__[self.type_of_service]
