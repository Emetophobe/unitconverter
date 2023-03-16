# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestAmountSubstance(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('mole')
        self.units = self.converter.units['amount substance']

    def test_mole(self):
        """ Test mole conversions. """
        expected_values = {
            "mole": "1",
            "quectomole": "1E+30",
            "rontomole": "1E+27",
            "yoctomole": "1E+24",
            "zeptomole": "1E+21",
            "attomole": "1E+18",
            "femtomole": "1E+15",
            "picomole": "1E+12",
            "nanomole": "1E+9",
            "micromole": "1E+6",
            "millimole": "1E+3",
            "centimole": "1E+2",
            "decimole": "1E+1",
            "decamole": "1E-1",
            "hectomole": "1E-2",
            "kilomole": "1E-3",
            "megamole": "1E-6",
            "gigamole": "1E-9",
            "teramole": "1E-12",
            "petamole": "1E-15",
            "examole": "1E-18",
            "zettamole": "1E-21",
            "yottamole": "1E-24",
            "ronnamole": "1E-27",
            "quettamole": "1E-30",
            "atom": "602214150000004428050534.2425",
        }

        # Test all mole conversions
        self.check_units(self.base_unit, self.units, expected_values)
