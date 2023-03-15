# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalInductance(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('henry')
        self.units = self.converter.units['electrical inductance']

    def test_volts(self):
        """ Test volt conversions. """
        expected_values = {
            "henry": "1",
            "quectohenry": "1E+30",
            "rontohenry": "1E+27",
            "yoctohenry": "1E+24",
            "zeptohenry": "1E+21",
            "attohenry": "1E+18",
            "femtohenry": "1E+15",
            "picohenry": "1E+12",
            "nanohenry": "1E+9",
            "microhenry": "1E+6",
            "millihenry": "1E+3",
            "centihenry": "1E+2",
            "decihenry": "1E+1",
            "decahenry": "1E-1",
            "hectohenry": "1E-2",
            "kilohenry": "1E-3",
            "megahenry": "1E-6",
            "gigahenry": "1E-9",
            "terahenry": "1E-12",
            "petahenry": "1E-15",
            "exahenry": "1E-18",
            "zettahenry": "1E-21",
            "yottahenry": "1E-24",
            "ronnahenry": "1E-27",
            "quettahenry": "1E-30",
        }

        # Test all volt conversions
        self.check_units(self.base_unit, self.units, expected_values)
