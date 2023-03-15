# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestSteradian(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('steradian')
        self.units = self.converter.units['solid angle']

    def test_steradian(self):
        """ Test steradian conversions. """
        expected_values = {
            "steradian": "1",
            "quectosteradian": "1E+30",
            "rontosteradian": "1E+27",
            "yoctosteradian": "1E+24",
            "zeptosteradian": "1E+21",
            "attosteradian": "1E+18",
            "femtosteradian": "1E+15",
            "picosteradian": "1E+12",
            "nanosteradian": "1E+9",
            "microsteradian": "1E+6",
            "millisteradian": "1E+3",
            "centisteradian": "1E+2",
            "decisteradian": "1E+1",
            "decasteradian": "1E-1",
            "hectosteradian": "1E-2",
            "kilosteradian": "1E-3",
            "megasteradian": "1E-6",
            "gigasteradian": "1E-9",
            "terasteradian": "1E-12",
            "petasteradian": "1E-15",
            "exasteradian": "1E-18",
            "zettasteradian": "1E-21",
            "yottasteradian": "1E-24",
            "ronnasteradian": "1E-27",
            "quettasteradian": "1E-30",
        }

        # Test all steradian conversions
        self.check_units(self.base_unit, self.units, expected_values)
