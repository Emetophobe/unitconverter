# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricPotential(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('volt')
        self.units = self.converter.units['electric potential']

    def test_volt(self):
        """ Test volt conversions. """
        expected_values = {
            "volt": "1",
            "quectovolt": "1E+30",
            "rontovolt": "1E+27",
            "yoctovolt": "1E+24",
            "zeptovolt": "1E+21",
            "attovolt": "1E+18",
            "femtovolt": "1E+15",
            "picovolt": "1E+12",
            "nanovolt": "1E+9",
            "microvolt": "1E+6",
            "millivolt": "1E+3",
            "centivolt": "1E+2",
            "decivolt": "1E+1",
            "decavolt": "1E-1",
            "hectovolt": "1E-2",
            "kilovolt": "1E-3",
            "megavolt": "1E-6",
            "gigavolt": "1E-9",
            "teravolt": "1E-12",
            "petavolt": "1E-15",
            "exavolt": "1E-18",
            "zettavolt": "1E-21",
            "yottavolt": "1E-24",
            "ronnavolt": "1E-27",
            "quettavolt": "1E-30",
        }

        # Test all volt conversions
        self.check_units(self.base_unit, self.units, expected_values)
