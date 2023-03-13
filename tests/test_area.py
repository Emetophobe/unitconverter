# Copyright (c) 2022-2023 Mike Cunningham


from tests import AbstractTestCase


class TestArea(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('square meters')
        self.units = self.converter.units['area']

    def test_square_meters(self):
        """ Test square meter conversions. """
        expected_values = {
            "square meters": "1",
            "square yoctometers": "1E+48",
            "square zeptometers": "1E+42",
            "square attometers": "1E+36",
            "square femtometers": "1E+30",
            "square picometers": "1E+24",
            "square nanometers": "1E+18",
            "square micrometers": "1E+12",
            "square millimeters": "1E+6",
            "square centimeters": "1E+4",
            "square decimeters": "1E+2",
            "square decameters": "0.01",
            "square hectometers": "0.0001",
            "square kilometers": "0.000001",
            "square megameters": "1E-12",
            "square gigameters": "1E-18",
            "square terameters": "1E-24",
            "square petameters": "1E-30",
            "square exameters": "1E-36",
            "square zettameters": "1E-42",
            "square yottalmeters": "1E-48",
            "acres": "0.0002471053814671653422482439292",
            "ares": "0.01",
            "circular inches": "1973.525241769719368993170121",
            "hectares": "0.0001",
            "hides": "0.000002061855670103092783505154639",
            "roods": "0.0009884215258686613689929757168",
            "square feet": "10.76391041670972230833350556",
            "square feet (US)": "10.76386736114295424114588269",
            "square inches": "1550.003100006200012400024800",
            "square miles": "3.861021585424458472628811394E-7",
            "square rods (poles)": "0.03953686103474645475971902867",
            "square yards": "1.195990046301080256481500617",
            "squares": "0.1076391041670972230833350556",
            "townships": "1.072505995952342722966012717E-8",
        }

        # Test all square meter conversions
        self.check_units(self.base_unit, self.units, expected_values)
