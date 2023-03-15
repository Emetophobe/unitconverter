# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestDoseEquivalent(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('sievert')
        self.units = self.converter.units['dose equivalent']

    def test_sievert(self):
        """ Test sievert conversions. """
        expected_values = {
            "sievert": "1",
            "quectosievert": "1E+30",
            "rontosievert": "1E+27",
            "yoctosievert": "1E+24",
            "zeptosievert": "1E+21",
            "attosievert": "1E+18",
            "femtosievert": "1E+15",
            "picosievert": "1E+12",
            "nanosievert": "1E+9",
            "microsievert": "1E+6",
            "millisievert": "1E+3",
            "centisievert": "1E+2",
            "decisievert": "1E+1",
            "decasievert": "1E-1",
            "hectosievert": "1E-2",
            "kilosievert": "1E-3",
            "megasievert": "1E-6",
            "gigasievert": "1E-9",
            "terasievert": "1E-12",
            "petasievert": "1E-15",
            "exasievert": "1E-18",
            "zettasievert": "1E-21",
            "yottasievert": "1E-24",
            "ronnasievert": "1E-27",
            "quettasievert": "1E-30",
            "roentgen equivalent man": "1E-2",
        }

        # Test all sievert conversions
        self.check_units(self.base_unit, self.units, expected_values)
