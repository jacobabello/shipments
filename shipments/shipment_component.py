import abc


class ShipmentComponent(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate_json(self):
        pass