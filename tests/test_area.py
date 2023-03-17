# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestArea(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('square meter')
        self.units = self.converter.units['area']

    def test_square_meter(self):
        """ Test square meter conversions. """
        expected_values = {
            "square meter": "1",
            "square yoctometer": "1E+48",
            "square zeptometer": "1E+42",
            "square attometer": "1E+36",
            "square femtometer": "1E+30",
            "square picometer": "1E+24",
            "square nanometer": "1E+18",
            "square micrometer": "1E+12",
            "square millimeter": "1E+6",
            "square centimeter": "1E+4",
            "square decimeter": "1E+2",
            "square decameter": "1E-2",
            "square hectometer": "1E-4",
            "square kilometer": "1E-6",
            "square megameter": "1E-12",
            "square gigameter": "1E-18",
            "square terameter": "1E-24",
            "square petameter": "1E-30",
            "square exameter": "1E-36",
            "square zettameter": "1E-42",
            "square yottalmeter": "1E-48",

            "are": "1E-2",
            "hectare": "1E-4",

            "square inch": "1550.003100006200012400024800",
            "square foot": "10.76391041670972230833350556",
            "square foot (US survey)": "10.76386736114295424114588269",
            "square yard": "1.195990046301080256481500617",
            "square mile": "3.861021585424458472628811394E-7",
            "square nautical mile": "2.915451895043731778425655977E-7",
            "circular inch": "1973.525241769719368993170121",

            "square rod": "0.03953686103474645475971902867",

            "imperial acre": "0.0002471053814671653422482439292",
            "US survey acre": "0.0002471045524071689972744367869",

            "hide": "0.000002061855670103092783505154639",
            "rood": "0.0009884215258686613689929757168",
            "square": "0.1076391041670972230833350556",
            "survey township": "1.072505995952342722966012717E-8",
        }

        # Test all square meter conversions
        self.check_units(self.base_unit, self.units, expected_values)
