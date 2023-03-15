# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLuminousIntensity(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('candela')
        self.units = self.converter.units['luminous intensity']

    def test_candela(self):
        """ Test candela conversions. """
        expected_values = {
            "candela": "1",
            "quectocandela": "1E+30",
            "rontocandela": "1E+27",
            "yoctocandela": "1E+24",
            "zeptocandela": "1E+21",
            "attocandela": "1E+18",
            "femtocandela": "1E+15",
            "picocandela": "1E+12",
            "nanocandela": "1E+9",
            "microcandela": "1E+6",
            "millicandela": "1E+3",
            "centicandela": "1E+2",
            "decicandela": "1E+1",
            "decacandela": "1E-1",
            "hectocandela": "1E-2",
            "kilocandela": "1E-3",
            "megacandela": "1E-6",
            "gigacandela": "1E-9",
            "teracandela": "1E-12",
            "petacandela": "1E-15",
            "exacandela": "1E-18",
            "zettacandela": "1E-21",
            "yottacandela": "1E-24",
            "ronnacandela": "1E-27",
            "quettacandela": "1E-30",
        }

        # Test all candela conversions
        self.check_units(self.base_unit, self.units, expected_values)
