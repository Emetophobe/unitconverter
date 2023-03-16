# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestTemperature(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('kelvin')
        self.units = self.converter.units['temperature']

    def test_kelvin(self):
        """ Test kelvin conversions. """
        expected_values = {
            "kelvin": "1",
            "quectokelvin": "1E+30",
            "rontokelvin": "1E+27",
            "yoctokelvin": "1E+24",
            "zeptokelvin": "1E+21",
            "attokelvin": "1E+18",
            "femtokelvin": "1E+15",
            "picokelvin": "1E+12",
            "nanokelvin": "1E+9",
            "microkelvin": "1E+6",
            "millikelvin": "1E+3",
            "centikelvin": "1E+2",
            "decikelvin": "1E+1",
            "decakelvin": "1E-1",
            "hectokelvin": "1E-2",
            "kilokelvin": "1E-3",
            "megakelvin": "1E-6",
            "gigakelvin": "1E-9",
            "terakelvin": "1E-12",
            "petakelvin": "1E-15",
            "exakelvin": "1E-18",
            "zettakelvin": "1E-21",
            "yottakelvin": "1E-24",
            "ronnakelvin": "1E-27",
            "quettakelvin": "1E-30",
            "celsius": "-272.15",
            "fahrenheit": "-457.87",
            "rankine": "1.8",
        }

        # Test all kelvin conversions
        self.check_units(self.base_unit, self.units, expected_values)
