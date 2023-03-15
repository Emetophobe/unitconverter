# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalResistance(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('ohm')
        self.units = self.converter.units['electrical resistance']

    def test_ohm(self):
        """ Test ohm conversions. """
        expected_values = {
            "ohm": "1",
            "quectoohm": "1E+30",
            "rontoohm": "1E+27",
            "yoctoohm": "1E+24",
            "zeptoohm": "1E+21",
            "attoohm": "1E+18",
            "femtoohm": "1E+15",
            "picoohm": "1E+12",
            "nanoohm": "1E+9",
            "microohm": "1E+6",
            "milliohm": "1E+3",
            "centiohm": "1E+2",
            "deciohm": "1E+1",
            "decaohm": "0.1",
            "hectoohm": "0.01",
            "kiloohm": "0.001",
            "megaohm": "0.000001",
            "gigaohm": "1E-9",
            "teraohm": "1E-12",
            "petaohm": "1E-15",
            "exaohm": "1E-18",
            "zettaohm": "1E-21",
            "yottaohm": "1E-24",
            "ronnaohm": "1E-27",
            "quettaohm": "1E-30",
        }

        # Test all ohm conversions
        self.check_units(self.base_unit, self.units, expected_values)
