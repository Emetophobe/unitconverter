# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLuminousFlux(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('lumen')
        self.units = self.converter.units['luminous flux']

    def test_lumen(self):
        """ Test lumen conversions. """
        expected_values = {
            "lumen": "1",
            "quectolumen": "1E+30",
            "rontolumen": "1E+27",
            "yoctolumen": "1E+24",
            "zeptolumen": "1E+21",
            "attolumen": "1E+18",
            "femtolumen": "1E+15",
            "picolumen": "1E+12",
            "nanolumen": "1E+9",
            "microlumen": "1E+6",
            "millilumen": "1E+3",
            "centilumen": "1E+2",
            "decilumen": "1E+1",
            "decalumen": "1E-1",
            "hectolumen": "1E-2",
            "kilolumen": "1E-3",
            "megalumen": "1E-6",
            "gigalumen": "1E-9",
            "teralumen": "1E-12",
            "petalumen": "1E-15",
            "exalumen": "1E-18",
            "zettalumen": "1E-21",
            "yottalumen": "1E-24",
            "ronnalumen": "1E-27",
            "quettalumen": "1E-30",
        }

        # Test all lumen conversions
        self.check_units(self.base_unit, self.units, expected_values)
