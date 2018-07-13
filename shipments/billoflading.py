from shipments.shipment_component import ShipmentComponent


class BillOfLading(ShipmentComponent):

    __billtype__ = {
        '02': 'Regular Bill',
        '03': 'In-bond Automated',
        '05': 'Empty Equipment IIT',
        '13': 'Master Bill',
        '14': 'House Bill',
        '15': 'Master FROB',
        '16': 'House FROB',
        '17': 'Simple BOL FROB',
        '18': 'Master BOL w/in-bond'
    }

    def __init__(self, billoflading_number, bill_type_code, voyage_number):

        if bill_type_code not in self.__billtype__.keys():
            raise ValueError('Bill type code %s is not recognized' % bill_type_code)

        self.billoflading_number = billoflading_number
        self.bill_type_code = bill_type_code
        self.voyage_number = voyage_number
        self.master_billoflading_number = None

    def generate_json(self):

        json_response = {
            'Bill of lading number': self.billoflading_number,
            'Bill type': self.__billtype__[self.bill_type_code],
            'Voyage number': self.voyage_number
        }

        if self.bill_type_code in ('14', '16'):
            if self.master_billoflading_number is None:
                raise ValueError('House bill of lading detected please add master '
                                 'bill of lading number: add_master_bill_of_lading(eeee)')
            else:
                json_response['Master bill of lading number'] = self.master_billoflading_number

        return json_response

    def add_master_bill_of_lading_number(self, master_id):
        self.master_billoflading_number = master_id
