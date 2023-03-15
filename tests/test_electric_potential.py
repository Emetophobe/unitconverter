# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricCurrent(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('volts')
        self.units = self.converter.units['electric potential']

    def test_amperes(self):
        """ Test ampere conversions. """
        expected_values = {
            "volts": "1",
            "quectovolts": "1E+30",
            "rontovolts": "1E+27",
            "yoctovolts": "1E+24",
            "zeptovolts": "1E+21",
            "attovolts": "1E+18",
            "femtovolts": "1E+15",
            "picovolts": "1E+12",
            "nanovolts": "1E+9",
            "microvolts": "1E+6",
            "millivolts": "1E+3",
            "centivolts": "1E+2",
            "decivolts": "1E+1",
            "decavolts": "1E-1",
            "hectovolts": "1E-2",
            "kilovolts": "1E-3",
            "megavolts": "1E-6",
            "gigavolts": "1E-9",
            "teravolts": "1E-12",
            "petavolts": "1E-15",
            "exavolts": "1E-18",
            "zettavolts": "1E-21",
            "yottavolts": "1E-24",
            "ronnavolts": "1E-27",
            "quettavolts": "1E-30",
        }

        # Test all volt conversions
        self.check_units(self.base_unit, self.units, expected_values)
