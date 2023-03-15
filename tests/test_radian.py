# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestRadian(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('radian')
        self.units = self.converter.units['plane angle']

    def test_radian(self):
        """ Test radian conversions. """
        expected_values = {
            "radian": "1",
            "quectoradian": "1E+30",
            "rontoradian": "1E+27",
            "yoctoradian": "1E+24",
            "zeptoradian": "1E+21",
            "attoradian": "1E+18",
            "femtoradian": "1E+15",
            "picoradian": "1E+12",
            "nanoradian": "1E+9",
            "microradian": "1E+6",
            "milliradian": "1E+3",
            "centiradian": "1E+2",
            "deciradian": "1E+1",
            "decaradian": "1E-1",
            "hectoradian": "1E-2",
            "kiloradian": "1E-3",
            "megaradian": "1E-6",
            "gigaradian": "1E-9",
            "teraradian": "1E-12",
            "petaradian": "1E-15",
            "exaradian": "1E-18",
            "zettaradian": "1E-21",
            "yottaradian": "1E-24",
            "ronnaradian": "1E-27",
            "quettaradian": "1E-30",
        }

        # Test all radian conversions
        self.check_units(self.base_unit, self.units, expected_values)
