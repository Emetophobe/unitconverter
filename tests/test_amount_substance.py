# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestEnergy(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('mole')
        self.units = self.converter.units['amount substance']

    def test_amount_substance(self):
        """ Test mole conversions. """
        expected_values = {
            "moles": "1",
            "quectomoles": "1E+30",
            "rontomoles": "1E+27",
            "yoctomoles": "1E+24",
            "zeptomoles": "1E+21",
            "attomoles": "1E+18",
            "femtomoles": "1E+15",
            "picomoles": "1E+12",
            "nanomoles": "1E+9",
            "micromoles": "1E+6",
            "millimoles": "1E+3",
            "centimoles": "1E+2",
            "decimoles": "1E+1",
            "decamoles": "0.1",
            "hectomoles": "0.01",
            "kilomoles": "0.001",
            "megamoles": "0.000001",
            "gigamoles": "1E-9",
            "teramoles": "1E-12",
            "petamoles": "1E-15",
            "examoles": "1E-18",
            "zettamoles": "1E-21",
            "yottamoles": "1E-24",
            "ronnamoles": "1E-27",
            "quettamoles": "1E-30",
            "atoms": "602214150000004428050534.2425",
        }

        # Test all mole conversions
        self.check_units(self.base_unit, self.units, expected_values)
