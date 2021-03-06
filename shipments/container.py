from shipments.cargo import Cargo
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
        self.cargoes = {}
        self.list_of_cargoes = []

    def generate_json(self):
        json_data = {
            'Container Number': self.container_number,
            'Length': self.get_length(),
            'Height': self.get_height(),
            'Width': self.get_width(),
            'Load status': self.get_load_status(),
            'Type of service': self.get_type_of_service()
        }

        json_cargoes = []

        if len(self.list_of_cargoes) > 0:
            for cargo in self.list_of_cargoes:
                json_cargoes.append({
                    'Product description': cargo.get_product_description(),
                    'Piece count': cargo.get_piece_count()
                })

            json_data.update({'Cargoes': json_cargoes})

        return json_data

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

    def add_cargo(self, sequence_number, product_description, piece_count):
        """
        :rtype: Cargo
        """
        if sequence_number in self.cargoes.keys():
            raise ValueError('Sequence Number %s is already added' % sequence_number )

        cargo = Cargo(sequence_number, product_description, piece_count)
        self.cargoes.update({sequence_number: cargo})
        self.list_of_cargoes.append(cargo)

    def get_cargo_by_sequence_number(self, sequence_number):
        """
        :rtype: Cargo
        """
        return self.cargoes[sequence_number]

    def get_all_cargoes(self):
        """
        @rtype list of Cargo
        """
        return self.list_of_cargoes
