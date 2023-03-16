# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestPower(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('watt')
        self.units = self.converter.units['power']

    def test_watt(self):
        """ Test watt conversions. """
        expected_values = {
            "watt": "1",
            "quectowatt": "1E+30",
            "rontowatt": "1E+27",
            "yoctowatt": "1E+24",
            "zeptowatt": "1E+21",
            "attowatt": "1E+18",
            "femtowatt": "1E+15",
            "picowatt": "1E+12",
            "nanowatt": "1E+9",
            "microwatt": "1E+6",
            "milliwatt": "1E+3",
            "centiwatt": "1E+2",
            "deciwatt": "1E+1",
            "decawatt": "1E-1",
            "hectowatt": "1E-2",
            "kilowatt": "1E-3",
            "megawatt": "1E-6",
            "gigawatt": "1E-9",
            "terawatt": "1E-12",
            "petawatt": "1E-15",
            "exawatt": "1E-18",
            "zettawatt": "1E-21",
            "yottawatt": "1E-24",
            "ronnawatt": "1E-27",
            "quettawatt": "1E-30",
            "joules per second": "1",
        }

        # Test all watt conversions
        self.check_units(self.base_unit, self.units, expected_values)
