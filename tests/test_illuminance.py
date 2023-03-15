# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestIlluminance(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('lux')
        self.units = self.converter.units['illuminance']

    def test_lux(self):
        """ Test lux conversions. """
        expected_values = {
            "lux": "1",
            "quectolux": "1E+30",
            "rontolux": "1E+27",
            "yoctolux": "1E+24",
            "zeptolux": "1E+21",
            "attolux": "1E+18",
            "femtolux": "1E+15",
            "picolux": "1E+12",
            "nanolux": "1E+9",
            "microlux": "1E+6",
            "millilux": "1E+3",
            "centilux": "1E+2",
            "decilux": "1E+1",
            "decalux": "1E-1",
            "hectolux": "1E-2",
            "kilolux": "1E-3",
            "megalux": "1E-6",
            "gigalux": "1E-9",
            "teralux": "1E-12",
            "petalux": "1E-15",
            "exalux": "1E-18",
            "zettalux": "1E-21",
            "yottalux": "1E-24",
            "ronnalux": "1E-27",
            "quettalux": "1E-30",
        }

        # Test all lux conversions
        self.check_units(self.base_unit, self.units, expected_values)
