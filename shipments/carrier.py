import os
import sqlite3
from shipments.shipment_component import ShipmentComponent


class Carrier(ShipmentComponent):

    def __init__(self, carrier_code):
        con = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + "/../sqlite/carrier_codes.sqlite",
                              isolation_level=None)

        cur = con.cursor()

        cur.execute("SELECT * "
                    "FROM carrier_codes_2 "
                    "WHERE carrier_codes_2.scac = \"%s\"" % carrier_code)

        result = cur.fetchone()

        if result is not None:
            self.scac_code = str(result[1]).upper()
            self.name = result[3].upper()
            self.address = result[4].upper()
            self.city = result[5].upper()
            self.state = result[6].upper()
            self.country = result[8].upper()

    def generate_json(self):
        return {
            'scac_code': self.scac_code,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country
        }

    def get_scac_code(self):
        return self.scac_code

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_country(self):
        return self.country
