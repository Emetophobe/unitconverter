# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestCatalyticActivity(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('katal')
        self.units = self.converter.units['catalytic activity']

    def test_katal(self):
        """ Test katal conversions. """
        expected_values = {
            "katal": "1",
            "quectokatal": "1E+30",
            "rontokatal": "1E+27",
            "yoctokatal": "1E+24",
            "zeptokatal": "1E+21",
            "attokatal": "1E+18",
            "femtokatal": "1E+15",
            "picokatal": "1E+12",
            "nanokatal": "1E+9",
            "microkatal": "1E+6",
            "millikatal": "1E+3",
            "centikatal": "1E+2",
            "decikatal": "1E+1",
            "decakatal": "1E-1",
            "hectokatal": "1E-2",
            "kilokatal": "1E-3",
            "megakatal": "1E-6",
            "gigakatal": "1E-9",
            "terakatal": "1E-12",
            "petakatal": "1E-15",
            "exakatal": "1E-18",
            "zettakatal": "1E-21",
            "yottakatal": "1E-24",
            "ronnakatal": "1E-27",
            "quettakatal": "1E-30",
            "mole per second": "1",
        }

        # Test all katal conversions
        self.check_units(self.base_unit, self.units, expected_values)
