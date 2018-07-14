from shipments.billoflading import BillOfLading
from shipments.container import Container
from shipments.manifest import Manifest
from shipments.company import Company


def type_hint(object, object_type):
    if (type(object)) != object_type:
        raise ValueError('object %s is not type of %s' % (object, object_type))


class Shipment(object):

    def __init__(self, billoflading, manifest):
        type_hint(billoflading, BillOfLading)
        type_hint(manifest, Manifest)

        self.billoflading = billoflading
        self.manifest = manifest
        self.containers = {}
        self.company = {}

    def add_container(self, container_number):
        container = Container(container_number)
        self.containers.update({container_number: container})

        return container

    def get_container_by_container_number(self, container_number):
        if container_number not in self.containers.keys():
            raise ValueError('Container number %s is missing' % container_number)

        return self.containers[container_number]

    def add_company(self, company_type, name, address):

        if company_type not in ('consignee', 'shipper'):
            raise ValueError('Company Type %s is invalid' % company_type)

        company = Company(name, address)
        self.company.update({
            company_type: company
        })

        return company

    def get_company_by_type(self, company_type):
        """
        :rtype: Company
        """
        return self.company[company_type]
