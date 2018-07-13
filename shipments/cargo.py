from shipments.shipment_component import ShipmentComponent


class Cargo(ShipmentComponent):
    def __init__(self, sequence_number, product_description, piece_count):
        self.sequence_number = sequence_number
        self.product_description = product_description
        self.piece_count = piece_count

    def get_sequence_number(self):
        return self.sequence_number

    def get_product_description(self):
        return self.product_description

    def get_piece_count(self):
        return self.piece_count
