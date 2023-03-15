# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestFrequency(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('hertz')
        self.units = self.converter.units['frequency']

    def test_hertz(self):
        """ Test hertz conversions. """
        expected_values = {
            "hertz": "1",
            "quectohertz": "1E+30",
            "rontohertz": "1E+27",
            "yoctohertz": "1E+24",
            "zeptohertz": "1E+21",
            "attohertz": "1E+18",
            "femtohertz": "1E+15",
            "picohertz": "1E+12",
            "nanohertz": "1E+9",
            "microhertz": "1E+6",
            "millihertz": "1E+3",
            "centihertz": "1E+2",
            "decihertz": "1E+1",
            "decahertz": "1E-1",
            "hectohertz": "1E-2",
            "kilohertz": "1E-3",
            "megahertz": "1E-6",
            "gigahertz": "1E-9",
            "terahertz": "1E-12",
            "petahertz": "1E-15",
            "exahertz": "1E-18",
            "zettahertz": "1E-21",
            "yottahertz": "1E-24",
            "ronnahertz": "1E-27",
            "quettahertz": "1E-30",
        }

        # Test all hertz conversions
        self.check_units(self.base_unit, self.units, expected_values)
