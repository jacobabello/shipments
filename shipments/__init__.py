from .shipment import Shipment
from .billoflading import BillOfLading
from .manifest import Manifest


def generate_shipment(billoflading, manifest):
    """
    :type billoflading BillOfLading
    :type manifest Manifest
    :rtype: Shipment
    """
    return Shipment(billoflading, manifest)


