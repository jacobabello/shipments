from .shipment import Shipment


def generate_shipment(billoflading, manifest):
    return Shipment(billoflading, manifest)