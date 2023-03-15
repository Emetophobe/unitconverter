# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMagneticFluxDensity(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        # SI uses kilograms as the base unit for historical
        # reasons. I use grams because it makes sense.
        self.base_unit = self.converter.find_unit('tesla')
        self.units = self.all_units['magnetic flux density']

    def test_tesla(self) -> None:
        """ Test tesla conversions. """
        expected_values = {
            "tesla": "1",
            "quectotesla": "1E+30",
            "rontotesla": "1E+27",
            "yoctotesla": "1E+24",
            "zeptotesla": "1E+21",
            "attotesla": "1E+18",
            "femtotesla": "1E+15",
            "picotesla": "1E+12",
            "nanotesla": "1E+9",
            "microtesla": "1E+6",
            "millitesla": "1E+3",
            "centitesla": "1E+2",
            "decitesla": "1E+1",
            "decatesla": "1E-1",
            "hectotesla": "1E-2",
            "kilotesla": "1E-3",
            "megatesla": "1E-6",
            "gigatesla": "1E-9",
            "teratesla": "1E-12",
            "petatesla": "1E-15",
            "exatesla": "1E-18",
            "zettatesla": "1E-21",
            "yottatesla": "1E-24",
            "ronnatesla": "1E-27",
            "quettatesla": "1E-30",
            "gamma": "1E+9",
            "guass": "1E+4",
        }

        # Test all tesla conversions
        self.check_units(self.base_unit, self.units, expected_values)
