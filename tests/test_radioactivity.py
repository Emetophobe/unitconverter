# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestRadioactivity(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('becquerel')
        self.units = self.converter.units['radioactivity']

    def test_becquerel(self):
        """ Test becquerel conversions. """
        expected_values = {
            "becquerel": "1",
            "quectobecquerel": "1E+30",
            "rontobecquerel": "1E+27",
            "yoctobecquerel": "1E+24",
            "zeptobecquerel": "1E+21",
            "attobecquerel": "1E+18",
            "femtobecquerel": "1E+15",
            "picobecquerel": "1E+12",
            "nanobecquerel": "1E+9",
            "microbecquerel": "1E+6",
            "millibecquerel": "1E+3",
            "centibecquerel": "1E+2",
            "decibecquerel": "1E+1",
            "decabecquerel": "1E-1",
            "hectobecquerel": "1E-2",
            "kilobecquerel": "1E-3",
            "megabecquerel": "1E-6",
            "gigabecquerel": "1E-9",
            "terabecquerel": "1E-12",
            "petabecquerel": "1E-15",
            "exabecquerel": "1E-18",
            "zettabecquerel": "1E-21",
            "yottabecquerel": "1E-24",
            "ronnabecquerel": "1E-27",
            "quettabecquerel": "1E-30",
            "rutherford": "1E-6",
            "curie": "2.702702702702702702702702703E-11",
            "picocurie": "2.702702702702702702702702703E+1"
        }

        # Test all becquerel conversions
        self.check_units(self.base_unit, self.units, expected_values)
