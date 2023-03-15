# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricCurrent(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.category = 'electric current'
        self.base_unit = self.converter.find_unit('amperes')
        self.units = self.converter.units[self.category]

    def test_amperes(self):
        """ Test ampere conversions. """
        expected_values = {
            "amperes": "1",
            "quectoamperes": "1E+30",
            "rontoamperes": "1E+27",
            "yoctoamperes": "1E+24",
            "zeptoamperes": "1E+21",
            "attoamperes": "1E+18",
            "femtoamperes": "1E+15",
            "picoamperes": "1E+12",
            "nanoamperes": "1E+9",
            "microamperes": "1E+6",
            "milliamperes": "1E+3",
            "centiamperes": "1E+2",
            "deciamperes": "1E+1",
            "decaamperes": "0.1",
            "hectoamperes": "0.01",
            "kiloamperes": "0.001",
            "megaamperes": "0.000001",
            "gigaamperes": "1E-9",
            "teraamperes": "1E-12",
            "petaamperes": "1E-15",
            "exaamperes": "1E-18",
            "zettaamperes": "1E-21",
            "yottaamperes": "1E-24",
            "ronnaamperes": "1E-27",
            "quettaamperes": "1E-30",
        }

        # Test all ampere conversions
        self.check_units(self.base_unit, self.units, expected_values)
