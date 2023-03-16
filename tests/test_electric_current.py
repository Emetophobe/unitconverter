# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricCurrent(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('ampere')
        self.units = self.converter.units['electric current']

    def test_ampere(self):
        """ Test ampere conversions. """
        expected_values = {
            "ampere": "1",
            "quectoampere": "1E+30",
            "rontoampere": "1E+27",
            "yoctoampere": "1E+24",
            "zeptoampere": "1E+21",
            "attoampere": "1E+18",
            "femtoampere": "1E+15",
            "picoampere": "1E+12",
            "nanoampere": "1E+9",
            "microampere": "1E+6",
            "milliampere": "1E+3",
            "centiampere": "1E+2",
            "deciampere": "1E+1",
            "decaampere": "1E-1",
            "hectoampere": "1E-2",
            "kiloampere": "1E-3",
            "megaampere": "1E-6",
            "gigaampere": "1E-9",
            "teraampere": "1E-12",
            "petaampere": "1E-15",
            "exaampere": "1E-18",
            "zettaampere": "1E-21",
            "yottaampere": "1E-24",
            "ronnaampere": "1E-27",
            "quettaampere": "1E-30",
        }

        # Test all ampere conversions
        self.check_units(self.base_unit, self.units, expected_values)
