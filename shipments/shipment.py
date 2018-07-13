from shipments.billoflading import BillOfLading
from shipments.manifest import Manifest


def type_hint(object, object_type):
    if (type(object)) != object_type:
        raise ValueError('object %s is not type of %s' % (object, object_type))


class Shipment(object):
    def __init__(self, billoflading, manifest):
        type_hint(billoflading, BillOfLading)
        type_hint(manifest, Manifest)

        self.billoflading = billoflading
        self.manifest = manifest
